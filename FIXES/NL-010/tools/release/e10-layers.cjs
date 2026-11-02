const { chromium, devices } = require('playwright');
(async () => { const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
 const c = await b.newContext({ ...devices['Pixel 7'] }); const p = await c.newPage(); const cons=[]; p.on('console', m => { if (m.type()==='error') cons.push(m.text()); });
 await p.goto('http://127.0.0.1:8796/editions/202611020825/', { waitUntil: 'load', timeout: 180000 }); await p.waitForTimeout(16000);
 const t = await p.evaluate(() => { const e=[...document.querySelectorAll('.ky-ly-rows')]; return e.slice(0,3).map(x => x.textContent.replace(/\s+/g,' ').trim().slice(0,700)); });
 console.log(t.join('\n')); console.log('console errors', cons.length, cons.slice(0,2).join(' | ')); await b.close(); })();
