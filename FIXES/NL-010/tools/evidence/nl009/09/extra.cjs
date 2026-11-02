const { chromium, devices } = require('playwright'); const fs = require('fs');
const PAGE = fs.readFileSync('/tmp/nl009/09/index.html', 'utf8'); const URL = 'http://127.0.0.1:8109/editions/202611012027/';
const ARGS = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'];
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const browser = await chromium.launch({ args: ARGS });
  const ctx = await browser.newContext({ ...devices['Pixel 7'], reducedMotion: 'reduce' });
  await ctx.route(u => /editions\/202611012027\/(index\.html)?$/.test(u.pathname), r => r.fulfill({ status: 200, contentType: 'text/html', body: PAGE }));
  const page = await ctx.newPage(); const log = []; page.on('pageerror', e => log.push(String(e.message))); page.on('console', m => { if (m.type() === 'error') log.push(m.text()); });
  await page.goto(URL); await sleep(8000);
  await page.evaluate(() => { window.__zooms = []; const h = document.getElementById('hud'); new MutationObserver(() => { const m = h.textContent.match(/zoom ([\d.]+) px per key|zoom 1 px = ([^\n]+)/); if (m) { const v = m[1] ? +m[1] : ('1px=' + m[2]); if (window.__zooms[window.__zooms.length - 1] !== v) window.__zooms.push(v); } }).observe(h, { childList: true, characterData: true, subtree: true }); });
  await page.keyboard.press('e'); await sleep(6000);
  console.log('reduced_motion zooms', JSON.stringify(await page.evaluate(() => window.__zooms)));
  // keyboard path through LINES: Tab to the LINES button, Enter, Tab into the list, Enter on a row
  await page.keyboard.press('Escape'); await sleep(200);
  const b = await page.$('#bar [data-panel="lines"]'); const r = await b.boundingBox(); await page.touchscreen.tap(r.x + r.width / 2, r.y + r.height / 2); await sleep(600);
  const rows = await page.evaluate(() => ({ rows: document.querySelectorAll('#lineslist [data-i]').length, focusable: document.querySelectorAll('#lineslist [data-i][tabindex="0"][role="button"]').length, expanded: document.querySelector('#bar [data-panel="lines"]').getAttribute('aria-expanded') }));
  console.log('lines rows', JSON.stringify(rows));
  await page.evaluate(() => document.querySelector('#lineslist [data-i="5"]').focus());
  const f = await page.evaluate(() => { const a = document.activeElement; return a.dataset.i + ' fv=' + a.matches(':focus-visible') + ' outline=' + getComputedStyle(a).outlineStyle; });
  await page.keyboard.press('Enter'); await sleep(6000);
  const after = await page.evaluate(() => ({ panel: !!document.querySelector('.gm-open'), card: getComputedStyle(document.getElementById('card')).display, title: document.querySelector('#card b').textContent, nOf: document.querySelector('#card span').textContent }));
  console.log('row focus', f, 'after Enter', JSON.stringify(after));
  // details button by keyboard
  await page.evaluate(() => document.querySelector('#card .ct').focus()); await page.keyboard.press('Enter'); await sleep(200);
  console.log('details', JSON.stringify(await page.evaluate(() => ({ open: document.getElementById('card').classList.contains('open'), expanded: document.querySelector('#card .ct').getAttribute('aria-expanded') }))));
  console.log('errors', JSON.stringify(log));
  await browser.close();
})();
