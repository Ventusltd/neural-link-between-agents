// usage: node measure.cjs <url> <device> <outpng|-> [widthxheight override] [fontScale]
const { chromium, devices } = require('playwright');
const [,, url, devName, out, patched, wh, fs] = process.argv;
const fsmod = require('fs');
const PROBE = "\n;Object.defineProperty(window,'__probe',{value:{safeBox:()=>safeBox(),placePanels:()=>placePanels(),panels:()=>PANELS,setPanel:n=>setPanel(n),open:()=>openPanel}});\n";
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const dev = Object.assign({}, devices[devName]);
  if (wh) { const [w, h] = wh.split('x').map(Number); dev.viewport = { width: w, height: h }; }
  const ctx = await browser.newContext(dev);
  const page = await ctx.newPage();
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  await page.route(u => /\/editions\/202611012027\/(index\.html)?$/.test(u.pathname), async route => {
    let body = (patched && patched !== '-') ? fsmod.readFileSync(patched, 'utf8') : await (await route.fetch()).text();
    body = body.replace('</script>', PROBE + '</script>');
    route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body });
  });
  await page.goto(url, { waitUntil: 'load', timeout: 120000 });
  if (fs) await page.addStyleTag({ content: `#bar{font-size:calc(1em*${fs})} #barname{font-size:calc(1em*${fs})}` });
  await page.waitForTimeout(7000);
  const m = await page.evaluate(() => {
    const r = el => { const b = el.getBoundingClientRect(); return { x: +b.x.toFixed(1), y: +b.y.toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1), bottom: +b.bottom.toFixed(1), right: +b.right.toFixed(1) }; };
    const bar = document.getElementById('bar'), bn = document.getElementById('barname');
    const cs = getComputedStyle(bar), bncs = getComputedStyle(bn);
    const btns = [...bar.querySelectorAll('.gm-title')].map(b => { const c = getComputedStyle(b); return { text: b.textContent, rect: r(b), font: c.fontSize, ls: c.letterSpacing, pad: c.padding, minH: c.minHeight, lh: c.lineHeight }; });
    const rows = [...new Set(btns.map(b => Math.round(b.rect.y)))];
    const P = window.__probe; const sb = P.safeBox();
    P.placePanels();
    const tops = Object.fromEntries(Object.entries(P.panels()).map(([k, el]) => [k, el.style.top]));
    const last = btns[btns.length - 1];
    return {
      inner: [innerWidth, innerHeight], dpr: devicePixelRatio, coarse: matchMedia('(pointer:coarse)').matches,
      bar: { rect: r(bar), pad: cs.padding, gap: cs.gap, wrap: cs.flexWrap, ovx: cs.overflowX, scrollW: bar.scrollWidth, clientW: bar.clientWidth, font: cs.fontSize },
      barname: { text: bn.textContent, rect: r(bn), font: bncs.fontSize, ls: bncs.letterSpacing, visibleText: bn.innerText },
      buttons: btns, rows, rowCount: rows.length,
      slack: +(bar.clientWidth - parseFloat(cs.paddingRight) - last.rect.right).toFixed(1),
      safeBox: sb, safeStartsUnderBar: sb.y0 >= bar.getBoundingClientRect().bottom + 8 - 0.01,
      panelTops: tops, panelTopOK: Object.values(tops).every(t => parseFloat(t) >= bar.getBoundingClientRect().height + 2 - 0.01),
      vhUnits: { card: getComputedStyle(document.getElementById('card')).maxHeight, lines: getComputedStyle(document.getElementById('lines')).maxHeight, vh100: innerHeight, docH: document.documentElement.clientHeight },
      fontFamily: getComputedStyle(document.body).fontFamily,
    };
  });
  // open a panel and check it starts under the bar, then close it
  const pan = await page.evaluate(() => { const P = window.__probe; P.setPanel('top'); const t = document.getElementById('top').getBoundingClientRect(); const b = document.getElementById('bar').getBoundingClientRect(); P.setPanel('top'); return { panelTop: +t.top.toFixed(1), barBottom: +b.bottom.toFixed(1), ok: t.top >= b.bottom }; });
  m.openedPanel = pan;
  // touch tap the last button and see that the right panel opens (foot = commands)
  const tap = await page.evaluate(() => { const b = document.querySelector('#bar .gm-title[data-panel="foot"]').getBoundingClientRect(); return [b.x + b.width/2, b.y + b.height/2]; });
  await page.touchscreen.tap(tap[0], tap[1]);
  await page.waitForTimeout(400);
  m.tapOpensCommands = await page.evaluate(() => window.__probe.open() === 'foot' && getComputedStyle(document.getElementById('foot')).display === 'block');
  await page.evaluate(() => { const P = window.__probe; if (P.open()) P.setPanel(P.open()); });
  await page.waitForTimeout(600);
  m.errors = errors;
  console.log(JSON.stringify(m, null, 1));
  if (out && out !== '-') { await page.screenshot({ path: out, scale: 'css', timeout: 180000 }); }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
