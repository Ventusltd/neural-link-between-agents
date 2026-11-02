const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  for (const [name, dev] of [['pixel7', devices['Pixel 7']], ['s24', devices['Galaxy S24']]]) {
    const c = await b.newContext({ ...dev }); const p = await c.newPage(); const errs=[];
    p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://127.0.0.1:8797/editions/202611021017/', { waitUntil: 'load', timeout: 180000 });
    await p.waitForTimeout(14000);
    const st = await p.evaluate(() => { const s = window.__KUIPER_EDITION__ || {}; const bar = document.querySelector('#gridatlas-menu-bar, nav[id*="menu"], #bar'); const r = bar && bar.getBoundingClientRect();
      const titles=[...document.querySelectorAll('.gm-title, nav button')].map(e=>e.textContent.trim()).filter(Boolean).slice(0,10);
      return { admitted: s.admitted, refused: s.refused, bar: r && [Math.round(r.top), Math.round(r.height), Math.round(r.width)], titles, wordmark: !!document.querySelector('.ventus-main') }; });
    console.log(name, JSON.stringify(st), 'pageerrors', errs.length, errs.slice(0,2).join(' | '));
    if (name==='pixel7') await p.screenshot({ path: '/tmp/e11-pixel7.png', timeout: 300000, animations: 'disabled' });
    await c.close();
  }
  await b.close();
})().catch(e => { console.log('ERR', e.message.split('\n')[0]); process.exit(1); });
