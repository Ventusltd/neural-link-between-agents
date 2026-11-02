const { chromium, devices } = require('playwright');
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const out = {};
  for (const [name, ctxOpts] of [['pixel7', { ...devices['Pixel 7'] }], ['w360', { viewport: { width: 360, height: 780 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true }], ['desktop1280', { viewport: { width: 1280, height: 800 } }]]) {
    const ctx = await browser.newContext(ctxOpts);
    const page = await ctx.newPage();
    const errs = []; page.on('pageerror', e => errs.push(String(e))); page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await page.goto('http://127.0.0.1:8771/editions/202611012027/', { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(7000);
    const m = await page.evaluate(() => {
      const r = s => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); const cs = getComputedStyle(e); return { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height), font: cs.font, color: cs.color, bg: cs.backgroundColor, display: cs.display }; };
      const titles = [...document.querySelectorAll('#bar .gm-title')].map(b => ({ text: b.textContent, ...(() => { const r = b.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }; })() }));
      const rows = new Set(titles.map(t => t.y)); const nameR = document.getElementById('barname').getBoundingClientRect(); rows.add(Math.round(nameR.y));
      return { vw: innerWidth, vh: innerHeight, bar: r('#bar'), barname: r('#barname'), titles, barRows: rows.size, top: r('#top'), hud: r('#hud'), foot: r('#foot'), card: r('#card'), lines: r('#lines'), bodyFont: getComputedStyle(document.body).font };
    });
    out[name] = { ...m, errors: errs };
    await page.screenshot({ path: `/tmp/nl010/team-1/B/ed4-${name}.png` });
    await ctx.close();
  }
  console.log(JSON.stringify(out, null, 1));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
