// Per-page gain/loss table, January files vs 2026q3 files, applying each page's own filter.
// Decodes like a browser XHR (UTF-8, invalid bytes -> U+FFFD), parses with papaparse 5.4.1 (header, skipEmptyLines).
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('<workspace>/teams/4/b/vendor/');
const Papa = require('papaparse');
const G = '<workspace>/gg-wt/';
const read = f => Papa.parse(new TextDecoder('utf-8').decode(fs.readFileSync(G + f)), { header: true, skipEmptyLines: true }).data;
const ref = r => (r['Ref ID'] || '').trim();
const xy = r => parseFloat(r['X-coordinate']) && parseFloat(r['Y-coordinate']);
const capBlank = r => (r['Installed Capacity (MWelec)'] || '').trim() === '';
const cap = r => parseFloat(r['Installed Capacity (MWelec)']) || 0;
const all = r => true;
const solarPlan = r => {
  const t = (r['Technology Type'] || '').toLowerCase(), s = (r['Development Status'] || '').toLowerCase();
  if (!t.includes('solar')) return false;
  if (['refused', 'abandoned', 'withdrawn', 'operational', 'decommissioned'].some(w => s.includes(w))) return false;
  const c = cap(r); return c >= 1 && c <= 50;
};
const pages = [
  ['repd-atlas.md (/atlas/)', 'repd.csv', 'repd-2026q3.csv', all],
  ['uk_grid-batteries.md', 'repd-grid-batteries.csv', 'repd-grid-batteries-2026q3.csv', all],
  ['uk_operating_large_solar_farms.md', 'repd-solar-operational-over-4mw.csv', 'repd-solar-operational-over-4mw-2026q3.csv', all],
  ['repd-uk-operational-solar.md', 'repd-solar-operational.csv', 'repd-solar-operational-2026q3.csv', all],
  ['uk_offshore_wind_atlas.md', 'repd.csv', 'repd-2026q3.csv', r => r['Technology Type'] === 'Wind Offshore'],
  ['uk_onshore_wind_atlas.md', 'repd.csv', 'repd-2026q3.csv', r => r['Technology Type'] === 'Wind Onshore'],
  ['uk_solar_in-planning-1-50mw.md', 'repd.csv', 'repd-2026q3.csv', solarPlan],
  ['repd_atlas_grid_model.md', 'repd.csv', 'repd-2026q3.csv', all],
];
const cache = {};
const get = f => (cache[f] ||= read(f));
const out = [];
for (const [name, jf, of, filt] of pages) {
  const o = { page: name };
  for (const [k, f] of [['jan', jf], ['oct', of]]) {
    const rows = get(f).filter(filt);
    const drawn = rows.filter(xy);
    o[k] = {
      file: f, rows: rows.length, drawn: drawn.length,
      noXY: rows.filter(r => !xy(r)).map(r => `${ref(r)} ${(r['Site Name'] || '').trim()} [${(r['Development Status (short)'] || r['Development Status'] || '').trim()}${capBlank(r) ? '' : ', ' + r['Installed Capacity (MWelec)'] + ' MW'}]`),
      blankCapDrawnAs0MW: drawn.filter(capBlank).length,
      fffdRowsDrawn: drawn.filter(r => JSON.stringify(r).includes('�')).length,
      mojibakeRowsDrawn: drawn.filter(r => /Ã|Â|â€/.test(JSON.stringify(r))).length,
      dupRefs: rows.length - new Set(rows.map(ref)).size,
      refs: new Set(drawn.map(ref)),
      salters: drawn.filter(r => ['18561', '18562'].includes(ref(r))).map(r => `${ref(r)} ${r['Site Name']} X=${r['X-coordinate']} Y=${r['Y-coordinate']} county=${r['County']}`),
    };
  }
  o.gainedDrawn = [...o.oct.refs].filter(x => !o.jan.refs.has(x)).length;
  o.lostDrawn = [...o.jan.refs].filter(x => !o.oct.refs.has(x)).length;
  o.lostDrawnExamples = [...o.jan.refs].filter(x => !o.oct.refs.has(x)).slice(0, 8);
  delete o.jan.refs; delete o.oct.refs;
  out.push(o);
}
// newly blank-coordinate offshore projects
const offJan = new Set(out[4].jan.noXY.map(s => s.split(' ')[0]));
out[4].newlyNoXY = out[4].oct.noXY.filter(s => !offJan.has(s.split(' ')[0]));
// atlas master json
for (const f of ['dist/repd_master.json', 'dist/repd_master_2026q3.json']) {
  const d = JSON.parse(fs.readFileSync(G + f, 'utf8'));
  const by = {}; let z = 0, nul = 0, sal = [];
  for (const ft of d.features) {
    const p = ft.properties; by[p.tech] = (by[p.tech] || 0) + 1;
    if (p.capacity === 0) z++; if (p.capacity === null || p.capacity === undefined || p.capacity === '') nul++;
    if (['18561', '18562'].includes(String(p.repd_ref))) sal.push(`${p.repd_ref} ${p.name} ${ft.geometry.coordinates}`);
  }
  out.push({ master: f, features: d.features.length, byTech: by, capacityZero: z, capacityNull: nul, salters: sal });
}
fs.writeFileSync(process.argv[2], JSON.stringify(out, null, 1));
for (const o of out) {
  if (o.page) console.log(`${o.page}: jan ${o.jan.rows}/${o.jan.drawn} oct ${o.oct.rows}/${o.oct.drawn} | noXY ${o.jan.noXY.length}->${o.oct.noXY.length} | 0MW ${o.jan.blankCapDrawnAs0MW}->${o.oct.blankCapDrawnAs0MW} | FFFD ${o.jan.fffdRowsDrawn}->${o.oct.fffdRowsDrawn} | mojibake ${o.jan.mojibakeRowsDrawn}->${o.oct.mojibakeRowsDrawn} | dup ${o.jan.dupRefs}->${o.oct.dupRefs} | +${o.gainedDrawn} -${o.lostDrawn} | salters ${o.oct.salters.length}`);
  else console.log(JSON.stringify(o));
}
