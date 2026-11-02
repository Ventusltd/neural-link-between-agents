#!/usr/bin/env node
// see-through-c5.cjs <url> <outdir> [--device "Pixel 7"] (OPUS-CONTROLLER-5, 2026-11-02): the controller's own check of the
// see-through module on a frozen snapshot, SwiftShader flags as journey-6.cjs. Measures:
//   S1 loader: every modules.json order entry admitted, none refused, see-through among them;
//   S2 the layers row "See Through stars" reads OK (label.ky-ly[data-id=see-through] .st, layers.api.get('see-through'));
//   S3 stars keyed to real data: data/see-through.json fetched in the page; every feature key == floor((j+0.5)*SPACE/20000)
//      (BigInt), every key < SPACE, features == placed == total, and the bytes' sha256 == the layers.json record;
//   S4 the layer draws: switched on through its original input, the overlay gains pixels of the layer's colour;
//   S5 nothing goes off-origin at load: every request URL starts with the snapshot origin (off-origin ones are aborted and listed);
//   S6 the shell's See Through entry: exactly one #kuiper-star, an <a> to ../../see-through/ on this origin, same tab.
// Page errors and console errors are counted. Report JSON to stdout and <outdir>/check.json; screenshots <outdir>/NN-*.png.
'use strict';
const { chromium, devices } = require('playwright');
const fs = require('fs'), path = require('path');
const argv = process.argv.slice(2), pos = argv.filter(a => !a.startsWith('--'));
const di = argv.indexOf('--device'), DEV = di >= 0 ? argv[di + 1] : 'Pixel 7';
const URL0 = pos[0], OUT = path.resolve(pos[1]); fs.mkdirSync(OUT, { recursive: true });
const ORIGIN = new URL(URL0).origin + '/';
(async () => {
  const R = { device: DEV, url: URL0, start: new Date().toISOString(), steps: [], pageerrors: [], console_errors: [], off_origin: [], requests: 0 };
  const step = (id, pass, m) => { R.steps.push({ id, pass: !!pass, m }); console.error('[' + DEV + '] ' + (pass ? 'PASS' : 'FAIL') + ' ' + id + ' ' + JSON.stringify(m).slice(0, 600)); };
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const ctx = await browser.newContext({ ...devices[DEV] });
  await ctx.route(u => !u.href.startsWith(ORIGIN), r => { R.off_origin.push(r.request().url().slice(0, 200)); return r.abort(); });
  const p = await ctx.newPage();
  p.on('request', () => R.requests++);
  p.on('pageerror', e => R.pageerrors.push(String(e && e.message || e)));
  p.on('console', m => { if (m.type() === 'error') R.console_errors.push(m.text().slice(0, 300)); });
  const shot = n => p.screenshot({ path: path.join(OUT, n + '.png'), timeout: 120000 }).catch(e => (R.shot_errors = R.shot_errors || []).push(n + ': ' + e.message.split('\n')[0]));
  try {
    await p.goto(URL0, { timeout: 180000 });
    await p.waitForFunction(() => { try { const E = window.__KUIPER_EDITION__; const L = KY.modules.layers.api; const g = L.get('see-through');
      return E && E.admitted.some(a => a.id === 'see-through') && g && g.status !== 'WAIT' && g.status !== 'LOAD' && L.get('lines').status === 'OK'; } catch (e) { return false; } }, null, { timeout: 300000, polling: 500 });
    await p.waitForTimeout(6500);
    const offAtLoad = R.off_origin.slice();
    // S1
    const s1 = await p.evaluate(async () => { const E = __KUIPER_EDITION__; const mj = await (await fetch('modules.json', { cache: 'no-store' })).json();
      return { order: mj.order, admitted: E.admitted.map(a => a.id), refused: E.refused.map(r => r.id || r), loader_admitted_in_order: JSON.stringify(mj.order) === JSON.stringify(E.admitted.map(a => a.id)) }; });
    step('S1 loader: every order entry admitted, none refused, see-through among them', s1.loader_admitted_in_order && s1.refused.length === 0 && s1.admitted.includes('see-through'), s1);
    // S2
    const s2 = await p.evaluate(() => { const L = KY.modules.layers.api, g = L.get('see-through'); const lab = document.querySelector('#layers label.ky-ly[data-id="see-through"]'); const st = lab && lab.querySelector('.st');
      return { status: g.status, why: g.why, tag: g.tag, placed: g.placed, total: g.total, loaded_sha256: g.loaded_sha256, label: g.label, rec_module: g.module, record_source: g.source, history: g.history,
        row_text: lab ? lab.textContent.trim().replace(/\s+/g, ' ') : null, st_text: st ? st.textContent : null, st_data_s: st && st.getAttribute('data-s'), aria: lab && lab.getAttribute('aria-label'), input_disabled: !!(lab && lab.querySelector('input').disabled),
        st_inspect: KY.modules['see-through'] && KY.modules['see-through'].api.inspect() }; });
    step('S2 layers row "See Through stars" reads OK', s2.status === 'OK' && s2.st_data_s === 'OK' && /^OK · /.test(s2.st_text || '') && s2.label === 'See Through stars' && s2.placed > 0 && s2.placed === s2.total, s2);
    await shot('01-wafer-panel-closed');
    // S3
    const s3 = await p.evaluate(async () => { const H = KY.hooks, SPACE = BigInt(H.SPACE); const g = KY.modules.layers.api.get('see-through');
      const res = await fetch('data/see-through.json', { cache: 'no-store' }); const buf = await res.arrayBuffer();
      const hex = [...new Uint8Array(await crypto.subtle.digest('SHA-256', buf))].map(b => (b < 16 ? '0' : '') + b.toString(16)).join('');
      const j = JSON.parse(new TextDecoder().decode(buf)); const fs = j.features || []; let badKey = 0, beyond = 0, notPoint = 0, named = 0; const js = new Set();
      for (const f of fs) { const gm = f.geometry || {}; if (gm.type !== 'Point') { notPoint++; continue; } const jj = f.properties && (f.properties.j ?? f.properties.star_j ?? f.properties.sub); if (jj == null) { badKey++; continue; } js.add(jj);
        const want = ((BigInt(jj) * 2n + 1n) * SPACE) / 40000n; if (BigInt(gm.key) !== want) badKey++; if (BigInt(gm.key) >= SPACE) beyond++; if (f.properties && f.properties.name) named++; }
      return { bytes: buf.byteLength, sha256: hex, record_sha256: g.source && g.source.sha256, record_bytes: g.source && g.source.bytes, record_features: g.source && g.source.features, features: fs.length, distinct_j: js.size, bad_key: badKey, beyond_space: beyond, not_point: notPoint, named, space: String(SPACE), data_space: j.space || (j.properties && j.properties.space) || null, placed: g.placed, total: g.total, schema: j.schema || j.type }; });
    step('S3 stars keyed to real data (key_j = floor((j+0.5)*SPACE/20000), sha256 = record)', s3.features > 0 && s3.bad_key === 0 && s3.beyond_space === 0 && s3.not_point === 0 && s3.distinct_j === s3.features && s3.features === s3.placed && s3.placed === s3.total && s3.sha256 === s3.record_sha256 && s3.bytes === s3.record_bytes && s3.features === s3.record_features, s3);
    // S4: switch the layer on through its original and count pixels of its colour on the overlay
    const s4 = await p.evaluate(async () => { const L = KY.modules.layers.api; const g = L.get('see-through'); const col = g.colour; const before = count(); L.set('see-through', true); await new Promise(r => setTimeout(r, 1500)); KY.redraw && KY.redraw(); await new Promise(r => setTimeout(r, 1500));
      const after = count(); return { colour: col, on: L.get('see-through').on, before, after };
      function count() { const o = document.getElementById('o'); if (!o || !o.width) return -1; const d = o.getContext('2d').getImageData(0, 0, o.width, o.height).data; let n = 0; const rc = parseInt(col.slice(1, 3), 16), gc = parseInt(col.slice(3, 5), 16), bc = parseInt(col.slice(5, 7), 16);
        for (let i = 0; i < d.length; i += 4) { if (d[i + 3] > 60 && Math.abs(d[i] - rc) < 40 && Math.abs(d[i + 1] - gc) < 40 && Math.abs(d[i + 2] - bc) < 40) n++; } return n; } });
    step('S4 the layer draws when switched on (overlay pixels of its colour)', s4.on === true && s4.after > s4.before && s4.after > 100, s4);
    await shot('02-layer-on');
    // S5
    step('S5 nothing off-origin at load', offAtLoad.length === 0, { origin: ORIGIN, requests: R.requests, off_origin_at_load: offAtLoad });
    // S6
    const s6 = await p.evaluate(() => { const els = [...document.querySelectorAll('#kuiper-star')]; const a = els[0]; const r = a && a.getBoundingClientRect(); const cs = a && getComputedStyle(a);
      return { count: els.length, tag: a && a.tagName, href: a && a.getAttribute('href'), resolved: a && new URL(a.getAttribute('href'), location.href).href, same_origin: a && new URL(a.getAttribute('href'), location.href).origin === location.origin, target: a && a.getAttribute('target'), text: a && a.textContent.trim(), aria: a && (a.getAttribute('aria-label') || a.getAttribute('title')), parent: a && a.parentElement && (a.parentElement.id || a.parentElement.className), rect: r && { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }, display: cs && cs.display, visible: !!(r && r.width > 0 && r.height > 0) }; });
    step('S6 shell See Through entry: one #kuiper-star <a> to ../../see-through/, same origin, same tab, visible', s6.count === 1 && s6.tag === 'A' && s6.href === '../../see-through/' && s6.same_origin && !s6.target && s6.visible, s6);
    await shot('03-entry');
  } catch (e) { R.harness_error = String(e && e.stack || e); console.error('HARNESS ' + R.harness_error); }
  R.end = new Date().toISOString(); R.pass = !R.harness_error && R.steps.length === 6 && R.steps.every(s => s.pass) && R.pageerrors.length === 0;
  fs.writeFileSync(path.join(OUT, 'check.json'), JSON.stringify(R, null, 1)); console.log(JSON.stringify(R, null, 1));
  await browser.close(); process.exit(R.pass ? 0 : 1);
})();
