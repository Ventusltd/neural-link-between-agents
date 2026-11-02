const { chromium, devices } = require('playwright');
const URL = 'http://127.0.0.1:8443/editions/202611012135/';
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  for (const dev of ['Pixel 7', 'Galaxy S24']) {
    const ctx = await b.newContext({ ...devices[dev] }); const p = await ctx.newPage();
    const errs = [], cons = [];
    p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') cons.push(m.text()); });
    await p.goto(URL); await p.waitForTimeout(7000);
    const r = await p.evaluate(() => {
      const KY = window.KY, E = window.__KUIPER_EDITION__;
      let writeThrows = null; try { KY.x = 1; writeThrows = false; } catch (e) { writeThrows = e.constructor.name; }
      return { frozen: Object.isFrozen(KY), hooks: Object.keys(KY.hooks), hooksFrozen: Object.isFrozen(KY.hooks), names: KY.names.length,
        alias: window.__KUIPER_MODULES__ === KY.modules, admitted: E.admitted, refused: E.refused, failures: E.failures, timings: E.timings,
        bytes: E.bytes, budget: E.byte_budget, refuse: !!document.getElementById('refuse'), hello: KY.modules.hello && KY.modules.hello.inspect(),
        scripts: [...document.querySelectorAll('script[data-ky-module]')].map(s => s.dataset.kyModule), N: KY.hooks.N, SPACE: KY.hooks.SPACE,
        writeFromPage: writeThrows };
    });
    console.log(dev, JSON.stringify(r)); console.log(dev, 'pageerror', errs.length, errs.slice(0,3), 'console.error', cons.length, cons.slice(0,3));
    await ctx.close();
  }
  await b.close();
})();
