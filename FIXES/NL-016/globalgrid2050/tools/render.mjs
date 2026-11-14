// Headless Chrome render check of legacy REPD pages on January vs October data.
// Usage: node render.mjs <baseUrl> <outDir> <pageList.json>
// All non-localhost requests are intercepted: CDN libraries are served from local npm copies
// (same versions as the pages pin), map tiles get a flat dark PNG, everything else is aborted.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
const require = createRequire('/opt/npm-tools/node_modules/');
const { chromium } = require('playwright');

const [base, outDir, listFile] = process.argv.slice(2);
const pages = JSON.parse(fs.readFileSync(listFile, 'utf8'));
const V = '<workspace>/teams/4/b/vendor/node_modules';
const LEAFLET_HOOK = `;(function(){var c=0,m=0;window.__leaf={get circle(){return c},get marker(){return m}};
var oc=L.circleMarker;L.circleMarker=function(){c++;return oc.apply(this,arguments)};
var om=L.marker;L.marker=function(){m++;return om.apply(this,arguments)};})();`;
const MAPLIBRE_HOOK = `;(function(){var M=maplibregl.Map;maplibregl.Map=class extends M{constructor(o){super(o);(window.__maps=window.__maps||[]).push(this);}};})();`;
const libs = [
  [/leaflet@1\.9\.4\/dist\/leaflet\.js/, `${V}/leaflet/dist/leaflet.js`, LEAFLET_HOOK],
  [/leaflet@1\.9\.4\/dist\/leaflet\.css/, `${V}/leaflet/dist/leaflet.css`],
  [/leaflet\.markercluster@1\.4\.1\/dist\/leaflet\.markercluster\.js/, `${V}/leaflet.markercluster/dist/leaflet.markercluster.js`],
  [/MarkerCluster\.Default\.css/, `${V}/leaflet.markercluster/dist/MarkerCluster.Default.css`],
  [/MarkerCluster\.css/, `${V}/leaflet.markercluster/dist/MarkerCluster.css`],
  [/maplibre-gl@3\.[0-9.]+\/dist\/maplibre-gl\.js/, `${V}/maplibre-gl/dist/maplibre-gl.js`, MAPLIBRE_HOOK],
  [/maplibre-gl@3\.[0-9.]+\/dist\/maplibre-gl\.css/, `${V}/maplibre-gl/dist/maplibre-gl.css`],
  [/PapaParse\/5\.4\.1\/papaparse\.min\.js/, `${V}/papaparse/papaparse.min.js`],
  [/proj4js\/2\.11\.0\/proj4\.js/, `${V}/proj4/dist/proj4.js`],
  [/jquery-3\.7\.0\.min\.js/, `${V}/jquery/dist/jquery.min.js`],
  [/jquery\.dataTables\.min\.js/, `${V}/datatables.net/js/jquery.dataTables.min.js`],
  [/jquery\.dataTables\.min\.css/, `${V}/datatables.net-dt/css/jquery.dataTables.min.css`],
  [/@turf\/turf@6\/turf\.min\.js/, `${V}/@turf/turf/turf.min.js`],
];
// 1x1 dark PNG
const TILE = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==', 'base64');
const REPD_IDS = ['solar','solar_roof','wind','bess','biomass','tidal','hydrogen','hydro','flywheel','act','geothermal','caes',
  'solar_operational','wind_onshore_operational','wind_offshore_operational','bess_operational'];

fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true,
  args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const results = [];
for (const p of pages) {
  const ctx = await browser.newContext({ viewport: { width: 1400, height: 1000 } });
  const page = await ctx.newPage();
  const rec = { name: p.name, url: p.url, errors: [], failed: [], aborted: [], data: [] };
  page.on('pageerror', e => rec.errors.push(String(e.message).slice(0, 300)));
  page.on('console', m => { if (m.type() === 'error') rec.errors.push('console: ' + m.text().slice(0, 300)); });
  page.on('requestfailed', r => { const u = r.url(); if (u.startsWith(base)) rec.failed.push(u.replace(base, '')); });
  page.on('response', async r => {
    const u = r.url();
    if (!u.startsWith(base)) return;
    if (/repd[^/]*\.(csv|json)(\?|$)/.test(u)) rec.data.push({ url: u.replace(base, ''), status: r.status(), bytes: (await r.body().catch(() => Buffer.alloc(0))).length });
    else if (r.status() >= 400) rec.failed.push(`${r.status()} ${u.replace(base, '')}`);
  });
  await page.route('**/*', async route => {
    const u = route.request().url();
    if (u.startsWith(base)) return route.continue();
    for (const [re, file, hook] of libs) if (re.test(u)) {
      let body = fs.readFileSync(file, "utf8"); if (hook) body += "\n" + hook;
      return route.fulfill({ status: 200, body, contentType: file.endsWith('.css') ? 'text/css' : 'application/javascript' });
    }
    if (/style\.json/.test(u)) return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({
      version: 8, name: 'stub-dark', glyphs: 'https://stub.invalid/fonts/{fontstack}/{range}.pbf', sources: {},
      layers: [{ id: 'bg', type: 'background', paint: { 'background-color': '#1b1b1d' } }] }) });
    if (/\.pbf(\?|$)/.test(u)) return route.fulfill({ status: 200, body: Buffer.alloc(0), contentType: 'application/x-protobuf' });
    if (/\{?\d+\}?\/\d+\/\d+(@2x)?\.png|basemaps|tile|openstreetmap\.org\/\d/.test(u)) return route.fulfill({ status: 200, body: TILE, contentType: 'image/png' });
    rec.aborted.push(u.slice(0, 120)); return route.abort();
  });
  const t0 = Date.now();
  try { await page.goto(base + p.url, { waitUntil: 'load', timeout: 60000 }); } catch (e) { rec.errors.push('goto: ' + e.message.slice(0, 200)); }
  await page.waitForTimeout(p.wait || 8000);
  if (p.toggle) {
    // atlas pages: switch on every REPD layer checkbox
    rec.toggled = await page.evaluate(ids => {
      let n = 0;
      for (const id of ids) for (const el of document.querySelectorAll(`input[data-layer-id="${id}"], input#${id}, input#chk-${id}, input#toggle-${id}`)) {
        if (el.type === 'checkbox' && !el.checked) { el.click(); n++; }
      }
      return n;
    }, REPD_IDS);
    await page.waitForTimeout(p.wait2 || 15000);
  }
  if (p.evalAfter) {
    rec.evalAfter = await page.evaluate(p.evalAfter).catch(e => 'ERR ' + e.message);
    await page.waitForTimeout(p.wait2 || 10000);
  }
  rec.ms = Date.now() - t0;
  rec.counts = await page.evaluate(ids => {
    const o = {};
    if (window.__leaf) { o.leafletCircleMarkers = window.__leaf.circle; o.leafletMarkers = window.__leaf.marker; }
    if (window.jQuery && jQuery.fn.dataTable) {
      o.tables = [...document.querySelectorAll('table')].filter(t => jQuery.fn.dataTable.isDataTable(t)).map(t => jQuery(t).DataTable().rows().count());
    }
    if (window.__maps) {
      o.maps = window.__maps.map(m => {
        const src = {};
        try {
          for (const [id, s] of Object.entries(m.style.sourceCaches || {})) {
            const so = m.getSource(id);
            if (so && so.type === 'geojson' && so._data && typeof so._data === 'object' && so._data.features) src[id] = so._data.features.length;
            else if (so && so.type === 'geojson' && typeof so._data === 'string' && /repd/.test(so._data)) src[id] = 'url:' + so._data;
          }
        } catch (e) { src.err = String(e); }
        let rendered = null;
        try {
          const lyr = (m.getStyle().layers || []).filter(l => /repd/i.test(l.source || '') || ids.includes(l.id)).map(l => l.id);
          const vis = lyr.filter(id => m.getLayoutProperty(id, 'visibility') !== 'none');
          const per = {}; for (const id of vis) per[id] = m.queryRenderedFeatures({ layers: [id] }).length;
          rendered = { layers: lyr.length, visible: vis.length, features: vis.length ? m.queryRenderedFeatures({ layers: vis }).length : 0, perLayer: per };
        } catch (e) { rendered = String(e).slice(0, 120); }
        return { sources: src, rendered };
      });
    }
    o.bodyTextSample = document.body.innerText.replace(/\s+/g, ' ').slice(0, 300);
    o.replacementChars = (document.body.innerText.match(/�/g) || []).length;
    return o;
  }, REPD_IDS).catch(e => ({ err: String(e) }));
  const shot = path.join(outDir, p.name + '.png');
  await page.screenshot({ path: shot, fullPage: false }).catch(e => rec.errors.push('shot: ' + e.message));
  rec.screenshot = shot;
  results.push(rec);
  console.log(JSON.stringify({ name: rec.name, ms: rec.ms, data: rec.data, counts: { ...rec.counts, bodyTextSample: undefined }, errors: rec.errors.length, failed: rec.failed.length, aborted: rec.aborted.length }));
  await ctx.close();
}
await browser.close();
fs.writeFileSync(path.join(outDir, 'results.json'), JSON.stringify(results, null, 1));
