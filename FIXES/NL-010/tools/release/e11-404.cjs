const { chromium, devices } = require('playwright');
(async () => { const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
 const c = await b.newContext({ ...devices['Pixel 7'] }); const p = await c.newPage(); p.on('response', r => { if (r.status() >= 400) console.log(r.status(), r.url()); });
 await p.goto('http://127.0.0.1:8797/editions/202611021017/', { waitUntil: 'load', timeout: 180000 }); await p.waitForTimeout(12000);
 await p.locator('#kuiper-menu-bar .gm-menu[data-menu="file"] > .gm-title').first().tap(); await p.waitForTimeout(5000); await b.close(); })();
