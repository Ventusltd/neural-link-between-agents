#!/usr/bin/env node
// file-touch-c4.cjs <url> <outdir> [--device "Pixel 7"] (OPUS-CONTROLLER-4, 2026-11-02): the controller's own touch check of
// FILE on a frozen snapshot: real taps only (page.touchscreen.tap), SwiftShader flags as journey-6.cjs. Measures:
//   T1 FILE opens from the bar title (data-open=file, #ky-file visible);
//   T2 every visible tap target in #ky-file (button, a, input) is >= 44 px tall;
//   T3 Open a key <KEY0> + GO opens the line card (line-card inspect().open, #card shown, header = that line);
//   T4 Open a line <LINE0> + GO opens the line card on that line (the openIndex / #lyFind path for engine-owned lines).
// Page errors are counted. Report JSON to stdout and <outdir>/touch.json; screenshots <outdir>/NN-*.png.
'use strict';
const { chromium, devices } = require('playwright');
const fs = require('fs'), path = require('path');
const argv = process.argv.slice(2), pos = argv.filter(a => !a.startsWith('--'));
const di = argv.indexOf('--device'), DEV = di >= 0 ? argv[di + 1] : 'Pixel 7';
const URL0 = pos[0], OUT = path.resolve(pos[1]); fs.mkdirSync(OUT, { recursive: true });
const KEY0 = 36064705400, LINE0 = process.env.LINE1;   // LINE1: a different placed line than KEY0's, so T4 changes the card
(async () => {
  const R = { device: DEV, url: URL0, start: new Date().toISOString(), steps: [], pageerrors: [], console_errors: [] };
  const step = (id, pass, m) => { R.steps.push({ id, pass: !!pass, m }); console.error('[' + DEV + '] ' + (pass ? 'PASS' : 'FAIL') + ' ' + id + ' ' + JSON.stringify(m)); };
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const ctx = await browser.newContext({ ...devices[DEV] });
  await ctx.route(u => !u.href.startsWith('http://127.0.0.1:8590/'), r => r.abort());
  const p = await ctx.newPage();
  p.on('pageerror', e => R.pageerrors.push(String(e && e.message || e)));
  p.on('console', m => { if (m.type() === 'error') R.console_errors.push(m.text()); });
  const shot = n => p.screenshot({ path: path.join(OUT, n + '.png'), timeout: 120000 }).catch(e => (R.shot_errors = R.shot_errors || []).push(n + ': ' + e.message.split('\n')[0]));
  const tapSel = async sel => { const el = p.locator(sel).first(); await el.scrollIntoViewIfNeeded(); const b = await el.boundingBox(); if (!b) throw new Error('no box ' + sel); await p.touchscreen.tap(b.x + b.width / 2, b.y + Math.min(b.height / 2, 22)); return b; };
  const card = () => p.evaluate(() => { const lc = KY.modules['line-card'].api.inspect(); const h = document.querySelector('#card .lc-h code'); const c = document.getElementById('card');
    return { open: lc.open, index: lc.index, header: h ? h.textContent : null, display: c ? getComputedStyle(c).display : null, hash: location.hash }; });
  try {
    await p.goto(URL0, { timeout: 180000 });
    await p.waitForFunction(() => { try { return window.__KUIPER_EDITION__ && __KUIPER_EDITION__.admitted.some(a => a.id === 'file') && KY.modules.layers.api.get('lines').status === 'OK' && document.getElementById('ky-file'); } catch (e) { return false; } }, null, { timeout: 300000, polling: 500 });
    await p.waitForTimeout(6500);
    R.admitted = await p.evaluate(() => ({ admitted: __KUIPER_EDITION__.admitted.map(a => a.id), refused: __KUIPER_EDITION__.refused }));
    const bodies = JSON.parse(fs.readFileSync(process.env.KEYS, 'utf8')).bodies;
    const b0 = bodies.find(b => b.key === KEY0), bl = bodies.find(b => b.id === LINE0 || (b.blob + ':' + b.line) === LINE0);
    R.expect = { key: b0 && { id: b0.id, line_text: b0.line_text }, line: bl && { id: bl.id, key: bl.key, line_text: bl.line_text } };
    // T1
    await tapSel('#kuiper-menu-bar .gm-menu[data-menu="file"] > .gm-title'); await p.waitForTimeout(1200);
    const t1 = await p.evaluate(() => { const b = document.getElementById('kuiper-menu-bar'), f = document.getElementById('ky-file'), r = f && f.getBoundingClientRect(); return { open: b.getAttribute('data-open'), w: r && Math.round(r.width), h: r && Math.round(r.height) }; });
    step('T1 FILE opens by touch', t1.open === 'file' && t1.w > 0 && t1.h > 0, t1); await shot('01-file-open');
    // T2
    const t2 = await p.evaluate(() => [...document.querySelectorAll('#ky-file button, #ky-file a, #ky-file input')].filter(e => { const r = e.getBoundingClientRect(), s = getComputedStyle(e); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; })
      .map(e => ({ t: ((e.querySelector && e.querySelector('.ky-file-label')) || e).textContent.trim().slice(0, 40) || e.id || e.tagName, tag: e.tagName, h: Math.round(e.getBoundingClientRect().height * 10) / 10 })));
    const minH = Math.min(...t2.map(x => x.h)); R.rows = t2;
    step('T2 every visible FILE target >= 44 px', t2.length > 0 && minH >= 44, { targets: t2.length, min_h: minH, below: t2.filter(x => x.h < 44) });
    // T3
    await tapSel('#ky-file-key-in'); await p.keyboard.type(String(KEY0)); await tapSel('#ky-file-key .ky-go'); await p.waitForTimeout(9000);
    const t3 = await card(); await shot('02-open-key');
    step('T3 Open a key opens the line card', t3.open && t3.display !== 'none' && b0 && t3.header === b0.line_text, t3);
    // T4
    const open = await p.evaluate(() => document.getElementById('kuiper-menu-bar').getAttribute('data-open'));
    if (open !== 'file') { await tapSel('#kuiper-menu-bar .gm-menu[data-menu="file"] > .gm-title'); await p.waitForTimeout(1200); }
    await p.locator('#ky-file-line-in').fill(''); await tapSel('#ky-file-line-in'); await p.keyboard.type(LINE0); await tapSel('#ky-file-line .ky-go'); await p.waitForTimeout(9000);
    const t4 = await card(); await shot('03-open-line');
    step('T4 Open a line opens the line card on that line', t4.open && t4.display !== 'none' && bl && t4.header === bl.line_text, t4);
  } catch (e) { R.harness_error = String(e && e.stack || e); console.error('HARNESS ' + R.harness_error); }
  R.end = new Date().toISOString(); R.pass = !R.harness_error && R.steps.length === 4 && R.steps.every(s => s.pass) && R.pageerrors.length === 0;
  fs.writeFileSync(path.join(OUT, 'touch.json'), JSON.stringify(R, null, 1)); console.log(JSON.stringify(R, null, 1));
  await browser.close(); process.exit(R.pass ? 0 : 1);
})();
