const { chromium, devices } = require('playwright'); const fs = require('fs');
const BASE = 'http://127.0.0.1:8440/editions/202611012135/';
(async () => { const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  for (const v of ['base', 'touch', 'full']) { const ctx = await b.newContext({ ...devices['Pixel 7'] }), p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.route(u => u.href === BASE, r => r.fulfill({ status: 200, contentType: 'text/html', body: fs.readFileSync(__dirname + '/' + v + '.html') }));
    await p.route(BASE + 'modules.json', r => r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ schema: 'kuiper.modules.v1', edition: '202611012135', hooks: 'kuiper.hooks.v1', order: [], modules: [] }) }));
    await p.goto(BASE); await p.waitForTimeout(7000);
    await p.evaluate(() => { window.__rs = 0; addEventListener('resize', () => window.__rs++); });
    const out = [];
    for (const [w, h] of [[839, 412], [412, 839], [412, 783]]) { await p.setViewportSize({ width: w, height: h }); await p.waitForTimeout(4000);
      out.push(await p.evaluate(() => ({ iw: innerWidth, ih: innerHeight, cw: document.getElementById('c').width, ch: document.getElementById('c').height, vv: visualViewport && [visualViewport.width, visualViewport.height, visualViewport.scale], dw: document.documentElement.clientWidth, rs: window.__rs }))); }
    console.log(v, JSON.stringify(out), errs); await ctx.close(); }
  await b.close(); })();
