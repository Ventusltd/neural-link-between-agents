// drift-probe.cjs <url>: OPUS-CONTROLLER-2. Pixel 7, SwiftShader flags. After load, report what the drift module shows:
// the #ky-drift section text (first 300 chars), any refusal text in #refuse, and the HUD's DRIFT line.
const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await (await b.newContext({ ...devices['Pixel 7'] })).newPage();
  await p.goto(process.argv[2], { waitUntil: 'load' }); await p.waitForTimeout(15000);
  const r = await p.evaluate(() => ({
    admitted: (window.KY && KY.state && KY.state.admitted || []).map(m => m.id || m),
    drift: (document.querySelector('#ky-drift') || {}).textContent ? document.querySelector('#ky-drift').textContent.replace(/\s+/g, ' ').slice(0, 300) : null,
    refuse: (document.querySelector('#refuse') || {}).textContent || null,
    hudDrift: ((document.querySelector('#hud') || {}).textContent || '').split('\n').filter(l => /DRIFT/i.test(l)).slice(0, 2),
  }));
  console.log(JSON.stringify(r)); await b.close();
})();
