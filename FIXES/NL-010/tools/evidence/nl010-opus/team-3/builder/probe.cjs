const { chromium, devices } = require('playwright');
const fs = require('fs');
const ED = 'http://127.0.0.1:8431/editions/202611012135/';
const SHIM = fs.readFileSync('/tmp/nl010-opus/team-3/builder/shim/index.html');
const scen = process.argv[2] || 'ok', dev = process.argv[3] || 'Galaxy S24';
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const d = dev === 'landscape' ? devices['Pixel 7 landscape'] : devices[dev];
  const ctx = await b.newContext({ ...d }); const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push('pageerror ' + e.message)); page.on('console', m => { if (m.type() === 'error') errs.push('console ' + m.text()); });
  await page.route(/\/editions\/202611012135\/(index\.html)?(\?[^#]*)?$/, r => r.fulfill({ status: 200, contentType: 'text/html', body: SHIM }));
  if (scen === '404') await page.route(/\/editions\/202611012135\/keys\.json/, r => r.fulfill({ status: 404, body: 'no' }));
  if (scen === 'tamper') await page.route(/\/editions\/202611012135\/keys\.json/, async r => { const res = await r.fetch(); const buf = Buffer.from(await res.body()); buf[100] = buf[100] === 0x41 ? 0x42 : 0x41; r.fulfill({ status: 200, contentType: 'application/json', body: buf }); });
  if (scen === 'nosha') await page.route(/\/data\/layers\.json/, async r => { const res = await r.fetch(); const j = JSON.parse(await res.text()); j.layers.forEach(l => { if (l.id === 'lines') delete l.source.sha256; }); r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(j) }); });
  if (scen === 'nowafer') await page.route(/\/cosmos\/wafer\.tsv/, r => r.fulfill({ status: 404, body: 'no' }));
  await page.goto(ED, { waitUntil: 'load' }); await page.waitForTimeout(+(process.env.WAITMS||8000));
  const before = await page.evaluate(() => { const L = KY.modules.layers && KY.modules.layers.api; return { inspect: L && L.inspect(), big: document.getElementById('big').textContent, refuse: (document.getElementById('refuse') || {}).textContent }; });
  // open the WAFER panel by touch
  const t = await page.locator('#bar [data-panel=wafer]').boundingBox(); await page.touchscreen.tap(t.x + t.width / 2, t.y + t.height / 2); await page.waitForTimeout(800);
  const m = await page.evaluate(() => { const p = document.getElementById('layers'), pr = p.getBoundingClientRect();
    const rows = [...p.querySelectorAll('input[data-ky-layer]')].map(i => { const l = i.closest('label'), r = l.getBoundingClientRect(), ir = i.getBoundingClientRect(), font = getComputedStyle(l.querySelector('.nm') || l).fontSize;
      return { k: i.getAttribute('data-ky-layer'), h: +r.height.toFixed(1), top: +r.top.toFixed(0), bottom: +r.bottom.toFixed(0), covers: ir.left <= r.left + .5 && ir.right >= r.right - .5 && ir.top <= r.top + .5 && ir.bottom >= r.bottom - .5, visibleInPanel: r.bottom <= pr.bottom + .5 && r.top >= pr.top - .5, font, text: l.textContent.trim().replace(/\s+/g,' ') }; });
    const list = document.getElementById('lineslist');
    return { panel: { top: pr.top, bottom: pr.bottom, left: pr.left, right: pr.right, sh: p.scrollHeight, ch: p.clientHeight }, vh: innerHeight, vw: innerWidth, list: list && { sh: list.scrollHeight, ch: list.clientHeight }, count: (document.getElementById('lycount') || {}).textContent, small: [...p.querySelectorAll('button,label,.lg,input#lyFind')].filter(e => e.offsetParent && e.getBoundingClientRect().height < 44).map(e => (e.className || e.tagName) + ':' + e.getBoundingClientRect().height.toFixed(0)).slice(0, 8), rows }; });
  console.log(JSON.stringify({ scen, dev, before, m, errs }, null, 1));
  await page.screenshot({ path: '/tmp/nl010-opus/team-3/builder/' + scen + '-' + dev.replace(/ /g, '_') + '.png', timeout: 180000 });
  await b.close();
})().catch(e => { console.error(e); process.exit(2); });
