// Bind the article corpus and the provisional register against only the 319 REPD refs added Jul->Oct 2026.
import {readFileSync, writeFileSync} from 'node:fs';
import {buildGazetteer, bindAll} from './b/discovery/project-binder.mjs';
import {reconcileProvisional} from '<workspace>/pipelinenews/cartridges/provisional-identity.mjs';
const [diffPath, csvCounty, resultsPath, registerPath, out] = process.argv.slice(2);
const added = JSON.parse(readFileSync(diffPath, 'utf8')).records.added.records_by_mw;
const county = JSON.parse(readFileSync(csvCounty, 'utf8'));
const tech = {'Solar Photovoltaics': 'solar', 'Battery': 'bess', 'Wind Onshore': 'wind_onshore', 'Wind Offshore': 'wind_offshore'};
const projects = added.map(r => ({repd_ref: String(r.ref), name: r.site, operator: r.operator, county: county[r.ref] ?? null, technology: tech[r.technology] ?? r.technology, status: r.status, capacity_mw: r.mw}));
const g = buildGazetteer(projects);
const rows = JSON.parse(readFileSync(resultsPath, 'utf8'));
const r = bindAll(rows.map(x => ({url: x.url, headline: x.headline})), g);
const register = JSON.parse(readFileSync(registerPath, 'utf8'));
const recon = reconcileProvisional(register.projects, projects, {path: diffPath, sha256: 'f'.repeat(64)});
const res = {added_refs: projects.length, gazetteer_aliases: g.alias_count, corpus_items: rows.length, counts: r.counts,
  hits: r.results.filter(x => x.outcome !== 'NO_MATCH').map((x, i) => ({item: x.item_id, outcome: x.outcome, reason: x.reason, candidates: x.candidates.map(c => c.repd_ref + ':' + c.name)})),
  provisional: recon.map(p => ({name: p.name, repd_ref: p.repd_ref, status: p.reconciliation.status, candidate_count: p.reconciliation.candidate_count}))};
writeFileSync(out, JSON.stringify(res, null, 1) + '\n'); console.log(JSON.stringify(res, null, 1));
