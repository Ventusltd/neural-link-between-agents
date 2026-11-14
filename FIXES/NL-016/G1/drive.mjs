// G1 headless-Chrome driver for a LOCAL COPY of GridAtlas (no live site reachable).
// Usage: node drive.mjs <scenarios.json> <outDir>
// The page is opened under its real origin (https://ventusltd.github.io/...) and every
// request is answered from local files:
//   ventusltd.github.io/<path>  -> http://127.0.0.1:8812/<path>  (site/ = gridatlas, data-gridatlas, dist copies)
//   globalgrid2050.com/<path>   -> http://127.0.0.1:8812/<path>
//   cdn.jsdelivr.net maplibre / duckdb -> local npm copies (same versions as pinned)
//   raw.githubusercontent.com   -> fetched for real with curl through the session proxy
//   basemap style / tiles / glyphs -> flat stub; everything else aborted and logged.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
const require = createRequire('/opt/npm-tools/node_modules/');
const { chromium } = require('playwright');

const [listFile, outDir] = process.argv.slice(2);
const scenarios = JSON.parse(fs.readFileSync(listFile, 'utf8'));
const LOCAL = 'http://127.0.0.1:8812';
const V3 = '<workspace>/teams/4/b/vendor/node_modules/maplibre-gl/dist';
const VD = '<workspace>/teams/12/vendor';
const TILE = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==', 'base64');
const STYLE = JSON.stringify({ version: 8, name: 'stub-dark', sources: {}, glyphs: 'https://stub.invalid/fonts/{fontstack}/{range}.pbf', layers: [{ id: 'bg', type: 'background', paint: { 'background-color': '#101418' } }] });
const ctype = f => f.endsWith('.css') ? 'text/css' : f.endsWith('.wasm') ? 'application/wasm' : f.endsWith('.json') || f.endsWith('.geojson') ? 'application/json' : 'application/javascript';

fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true,
  args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const all = [];
for (const s of scenarios) {
  const [w, h] = s.viewport || [1400, 900];
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, isMobile: !!s.mobile, hasTouch: !!s.mobile,
    deviceScaleFactor: s.mobile ? 2 : 1 });
  const page = await ctx.newPage();
  const rec = { name: s.name, url: s.url, viewport: [w, h], served: {}, missing: [], aborted: [], remote: [], errors: [], steps: [] };
  page.on('pageerror', e => rec.errors.push('pageerror: ' + String(e.message).slice(0, 240)));
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') rec.errors.push(m.type() + ': ' + m.text().slice(0, 240)); });
  await page.route('**/*', async route => {
    const u = route.request().url();
    let m;
    try {
      if ((m = u.match(/^https:\/\/stub\.invalid\/(harness\/[^?#]*)/))) { m[1] = '/' + m[1]; }
      if (m || (m = u.match(/^https:\/\/(?:ventusltd\.github\.io|globalgrid2050\.com)(\/[^?#]*)/))) {
        const local = LOCAL + m[1];
        const r = await fetch(local);
        const body = Buffer.from(await r.arrayBuffer());
        if (r.status >= 400) rec.missing.push(`${r.status} ${u.slice(0, 160)}`);
        else rec.served[m[1]] = body.length;
        return route.fulfill({ status: r.status, body, headers: { 'content-type': r.headers.get('content-type') || ctype(m[1]), 'access-control-allow-origin': '*' } });
      }
      if (/maplibre-gl@3\.6\.2\/dist\/maplibre-gl\.(js|css)/.test(u)) {
        const f = `${V3}/maplibre-gl.${u.endsWith('.css') ? 'css' : 'js'}`;
        return route.fulfill({ status: 200, body: fs.readFileSync(f), contentType: ctype(f) });
      }
      if (/duckdb-wasm@1\.29\.0\/\+esm/.test(u)) return route.fulfill({ status: 200, body: fs.readFileSync(`${VD}/duckdb-esm.js`), contentType: 'application/javascript', headers: { 'access-control-allow-origin': '*' } });
      if ((m = u.match(/duckdb-wasm@1\.29\.0\/(dist\/[^?#]+)/))) {
        const f = `${VD}/node_modules/@duckdb/duckdb-wasm/${m[1]}`;
        return route.fulfill({ status: 200, body: fs.readFileSync(f), contentType: ctype(f), headers: { 'access-control-allow-origin': '*' } });
      }
      if (/^https:\/\/raw\.githubusercontent\.com\//.test(u)) {
        const body = execFileSync('curl', ['-sS', '-m', '30', '-f', u], { maxBuffer: 1 << 28 });
        rec.remote.push(`${body.length} ${u.slice(0, 160)}`);
        return route.fulfill({ status: 200, body, contentType: ctype(u), headers: { 'access-control-allow-origin': '*' } });
      }
      if (/style\.json/.test(u)) return route.fulfill({ status: 200, contentType: 'application/json', body: STYLE });
      if (/\.pbf(\?|$)/.test(u) || /fonts\//.test(u)) return route.fulfill({ status: 200, body: Buffer.alloc(0), contentType: 'application/x-protobuf' });
      if (/arcgisonline|basemaps|\/tile\/|\{z\}|\/\d+\/\d+\/\d+(\.png|@2x)/.test(u)) return route.fulfill({ status: 200, body: TILE, contentType: 'image/png' });
    } catch (e) { rec.errors.push('route: ' + u.slice(0, 120) + ' ' + String(e).slice(0, 120)); return route.abort(); }
    if (u.startsWith('data:') || u.startsWith('blob:')) return route.continue();
    rec.aborted.push(u.slice(0, 160));
    return route.abort();
  });
  const t0 = Date.now();
  try { await page.goto(s.url, { waitUntil: 'load', timeout: 90000 }); } catch (e) { rec.errors.push('goto: ' + e.message.slice(0, 200)); }
  for (const [i, st] of (s.steps || [{ wait: 20000, shot: true }]).entries()) {
    if (st.wait) await page.waitForTimeout(st.wait);
    if (st.click) { try { await page.click(st.click, { timeout: 8000 }); } catch (e) { rec.steps.push({ i, clickErr: e.message.slice(0, 160) }); } }
    if (st.tapAt) { await page.mouse.click(st.tapAt[0], st.tapAt[1]); }
    if (st.eval) {
      let v; try { v = await page.evaluate(st.eval); } catch (e) { v = 'ERR ' + e.message.slice(0, 300); }
      rec.steps.push({ i, label: st.label || '', t: Date.now() - t0, value: v });
      if (st.tapResult && Array.isArray(v) && v.length === 2) { if (s.mobile) await page.touchscreen.tap(v[0], v[1]); else await page.mouse.click(v[0], v[1]); }
    }
    if (st.waitAfter) await page.waitForTimeout(st.waitAfter);
    if (st.shot) {
      const f = path.join(outDir, `${s.name}${typeof st.shot === 'string' ? '-' + st.shot : ''}.png`);
      await page.screenshot({ path: f, fullPage: !!st.full }).catch(e => rec.errors.push('shot ' + e.message));
      rec.steps.push({ i, shot: f });
    }
  }
  rec.ms = Date.now() - t0;
  rec.errors = [...new Set(rec.errors)].slice(0, 40);
  rec.aborted = [...new Set(rec.aborted)];
  all.push(rec);
  await ctx.close();
}
await browser.close();
fs.writeFileSync(path.join(outDir, 'results.json'), JSON.stringify(all, null, 1));
for (const r of all) console.log(JSON.stringify({ name: r.name, ms: r.ms, served: Object.keys(r.served).length, missing: r.missing.length, aborted: r.aborted.length, errors: r.errors.length }));
