#!/usr/bin/env node
// NL-010 team 3: See Through and Edition 4 on Pixel 7 emulation, served from the kuiper-belt root on :8203.
// SwiftShader renders See Through's canvases slowly, so before each capture the page is told it is hidden
// (descent.js pauses its requestAnimationFrame loop on visibilitychange, descent.js:1019-1022) and told it is
// visible again afterwards. The capture is CDP Page.captureScreenshot with a 90 s limit.
'use strict';
const { chromium, devices } = require('playwright');
const fs = require('fs');
const OUT = '/tmp/nl010/team-3/img'; fs.mkdirSync(OUT, { recursive: true });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const report = {}; const save = () => fs.writeFileSync('/tmp/nl010/team-3/shots-report.json', JSON.stringify(report, null, 1));
async function pause(page, on) {
  await page.evaluate(h => { Object.defineProperty(document, 'hidden', { configurable: true, get: () => h }); document.dispatchEvent(new Event('visibilitychange')); }, on).catch(() => {});
}
async function shot(page, name) {
  const path = OUT + '/' + name; const t0 = Date.now();
  await pause(page, true);
  try { const cdp = await page.context().newCDPSession(page);
    const r = await Promise.race([cdp.send('Page.captureScreenshot', { format: 'png' }), sleep(90000).then(() => null)]);
    if (r) fs.writeFileSync(path, Buffer.from(r.data, 'base64')); else console.error('shot timeout', name);
    await cdp.detach().catch(() => {});
  } catch (e) { console.error('shot failed', name, String(e.message)); }
  await pause(page, false);
  console.error('step', name, (Date.now() - t0) + ' ms'); save();
}
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const ctx = await browser.newContext({ ...devices['Pixel 7'] });
  const page = await ctx.newPage();
  const errors = []; page.on('pageerror', e => errors.push(String(e.message))); page.on('console', m => { if (m.type() === 'error') errors.push(m.text().slice(0, 200)); });
  // 1. See Through first screen, arriving with a hash that nothing reads today
  await page.goto('http://127.0.0.1:8203/see-through/202610050609/#sub=Drax', { waitUntil: 'load', timeout: 120000 });
  await sleep(6000);
  report.st_first = await page.evaluate(() => {
    const R = el => { const r = el.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)]; };
    const btns = [...document.querySelectorAll('button')].map(b => ({ t: b.textContent.trim(), r: R(b), aria: b.getAttribute('aria-label') }));
    const inp = document.querySelector('input');
    const st = window.__descent && window.__descent.state();
    return { vw: innerWidth, vh: innerHeight, dpr: devicePixelRatio, buttons: btns, input: inp && { ph: inp.placeholder, r: R(inp) }, state: st, hash: location.hash,
      links: [...document.querySelectorAll('a')].map(a => a.href), title: document.title, space: window.KuiperLaw.constants.SPACE };
  });
  save();
  await shot(page, '01-see-through-first.png');
  // 2. the find and fly hooks (what a deep link would call)
  report.st_find = await page.evaluate(() => ({ drax: window.__descent.find('drax'), draxSub: window.__descent.sub(window.__descent.find('drax')), T_before: window.__descent.state().T }));
  save();
  await page.evaluate(() => window.__descent.fly(window.__descent.find('drax')));
  await sleep(3500);
  report.st_falling = await page.evaluate(() => window.__descent.state()); save();
  await shot(page, '02-see-through-falling.png');
  await sleep(9000);
  report.st_arrived = await page.evaluate(() => window.__descent.state()); save();
  await shot(page, '03-see-through-arrived.png');
  // 3. KUIPER view (stars only) at the bottom
  await page.evaluate(() => window.__descent.view('kuiper'));
  await sleep(2500);
  report.st_kuiper = await page.evaluate(() => window.__descent.state()); save();
  await shot(page, '04-see-through-kuiper-view.png');
  report.st_errors = errors.slice(); save();
  // 4. Edition 4 first screen
  errors.length = 0;
  await page.goto('http://127.0.0.1:8203/editions/202611012027/', { waitUntil: 'load', timeout: 120000 });
  await sleep(8000);
  report.ed_first = await page.evaluate(() => {
    const R = el => { const r = el.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)]; };
    const bar = document.getElementById('bar');
    return { vw: innerWidth, vh: innerHeight, bar: R(bar), barname: document.getElementById('barname').textContent,
      titles: [...bar.querySelectorAll('.gm-title')].map(b => ({ t: b.textContent, r: R(b) })), big: document.getElementById('big').textContent, hash: location.hash };
  });
  save();
  await shot(page, '05-edition4-first.png');
  report.ed_errors = errors.slice(); save();
  console.log(JSON.stringify(report, null, 1));
  await browser.close();
})().catch(e => { console.error('HARNESS', e); save(); process.exit(2); });
