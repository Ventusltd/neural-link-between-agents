// Nearest-substation QA for the October preview records, using GridAtlas's own shipped code, not a re-implementation:
//  - distanceKm: atlas/modules/202609011950-geodesy.js, run in node:vm with a window stub;
//  - voltagesKv, representativePoint, MIN_KV/LINK_COUNT/MAX_LINK_KM: extracted verbatim from the live sld-sandbox
//    cartridge atlas/cartridges/202609241334-sld-sandbox-v9-8.js and evaluated;
//  - substations: atlas/releases/202608300453-atlas-v9/data/grid_substations.geojson (the payload the live link code reads).
// Usage: node nearest_substation_check.mjs <gridatlas work dir> <q2.parquet-as-json> <oct.parquet-as-json> <out.json>
import fs from 'node:fs';
import vm from 'node:vm';
const [W, q2f, octf, out] = process.argv.slice(2);
const ctx = { window: {}, Math, Number, String, Array, Object, JSON };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(`${W}/atlas/modules/202609011950-geodesy.js`, 'utf8'), ctx);
const distanceKm = ctx.window.__GRIDATLAS_MODULES__.geodesy.distanceKm;
const sld = fs.readFileSync(`${W}/atlas/cartridges/202609241334-sld-sandbox-v9-8.js`, 'utf8');
const grab = (name) => { const i = sld.indexOf(`function ${name}(`); let d = 0, j = sld.indexOf('{', i);
  for (let k = j; k < sld.length; k++) { if (sld[k] === '{') d++; else if (sld[k] === '}' && --d === 0) return sld.slice(i, k + 1); } };
const consts = sld.match(/const MIN_KV = (\d+);[\s\S]*?const LINK_COUNT = (\d+);[\s\S]*?const MAX_LINK_KM = (\d+);/);
const MIN_KV = +consts[1], LINK_COUNT = +consts[2], MAX_LINK_KM = +consts[3];
const voltagesKv = new Function(`${grab('voltagesKv')}; return voltagesKv;`)();
const representativePoint = new Function(`${grab('representativePoint')}; return representativePoint;`)();
const subsRaw = JSON.parse(fs.readFileSync(`${W}/atlas/releases/202608300453-atlas-v9/data/grid_substations.geojson`, 'utf8')).features;
const subs = [];
for (const f of subsRaw) { // the same qualifying filter as loadSubstations()
  const kv = voltagesKv(f.properties); if (!kv.length || Math.max(...kv) < MIN_KV - 0.5) continue;
  const at = representativePoint(f.geometry); if (!at) continue;
  subs.push({ at, kv: kv.filter(v => v >= MIN_KV - 0.5).sort((a, b) => b - a), name: f.properties?.name || '' });
}
const nearest = (lon, lat) => subs.map(s => ({ ...s, km: distanceKm(lon, lat, s.at[0], s.at[1]) })).sort((a, b) => a.km - b.km);
const q2 = new Map(JSON.parse(fs.readFileSync(q2f, 'utf8')).map(r => [r.repd_ref, r]));
const oct = JSON.parse(fs.readFileSync(octf, 'utf8'));
const res = { substations_loaded: subsRaw.length, substations_qualifying: subs.length, MIN_KV, LINK_COUNT, MAX_LINK_KM, groups: {} };
const rows = [];
for (const r of oct) {
  const old = q2.get(r.repd_ref);
  const kind = !old ? 'added' : (Math.abs(old.longitude - r.longitude) > 1e-6 || Math.abs(old.latitude - r.latitude) > 1e-6) ? 'moved' : null;
  if (!kind) continue;
  const placeholder = r.longitude === 0 && r.latitude === 0;
  const row = { kind, repd_ref: r.repd_ref, name: r.name, technology: r.technology, status: r.status, capacity_mw: r.capacity_mw,
    region: r.region, county: r.county, lon: r.longitude, lat: r.latitude, placeholder };
  if (!placeholder) {
    const n = nearest(r.longitude, r.latitude);
    row.nearest = { name: n[0].name || 'Unnamed substation', kv: n[0].kv[0], km: +n[0].km.toFixed(3) };
    row.drawn_links = n.filter(s => s.km <= MAX_LINK_KM).slice(0, LINK_COUNT).length;
    if (old && kind === 'moved') row.moved_km = +distanceKm(old.longitude, old.latitude, r.longitude, r.latitude).toFixed(3);
    // coarse sanity: a Scottish record south of 54.6 N, or an English/Welsh record north of 55.9 N
    row.region_lat_mismatch = (/scotland/i.test(r.region || '') && r.latitude < 54.6) || (/^(?!.*scotland)/i.test(r.region || '') && /england|wales|london|midlands|east|west|south|north|yorkshire/i.test(r.region || '') && r.latitude > 55.9);
  }
  rows.push(row);
}
for (const k of ['added', 'moved']) {
  const g = rows.filter(r => r.kind === k), m = g.filter(r => !r.placeholder);
  const kms = m.map(r => r.nearest.km).sort((a, b) => a - b);
  res.groups[k] = { records: g.length, placeholder_no_map: g.filter(r => r.placeholder).map(r => `${r.repd_ref} ${r.name}`),
    measured: m.length, nearest_km_median: kms[Math.floor(kms.length / 2)], nearest_km_p95: kms[Math.floor(kms.length * 0.95)], nearest_km_max: kms[kms.length - 1],
    beyond_40km_no_links: m.filter(r => r.drawn_links === 0).map(r => `${r.repd_ref} ${r.name} [${r.technology}] ${r.nearest.km} km to ${r.nearest.name}`),
    region_lat_mismatch: m.filter(r => r.region_lat_mismatch).map(r => `${r.repd_ref} ${r.name} region=${r.region} county=${r.county} lat=${r.lat}`),
    moved_over_5km: k === 'moved' ? m.filter(r => r.moved_km > 5).map(r => `${r.repd_ref} ${r.name} moved ${r.moved_km} km`) : undefined };
}
// Known source-coordinate faults that the nearest-substation answer inherits.
res.salters_lane = rows.concat(oct.filter(r => ['18561', '18562'].includes(r.repd_ref)).map(r => ({ repd_ref: r.repd_ref, name: r.name, county: r.county, lon: r.longitude, lat: r.latitude,
  nearest: (() => { const n = nearest(r.longitude, r.latitude)[0]; return { name: n.name, kv: n.kv[0], km: +n.km.toFixed(3) }; })() })))
  .filter(r => ['18561', '18562'].includes(r.repd_ref)).filter((r, i, a) => a.findIndex(x => x.repd_ref === r.repd_ref && !!x.kind === !!r.kind) === i);
res.rows = rows;
fs.writeFileSync(out, JSON.stringify(res, null, 1));
const { rows: _, ...summary } = res;
console.log(JSON.stringify(summary, null, 1).slice(0, 6000));
