// Offline measurement: bind the existing Pipeline News article corpus to the Q2 and Q3 registers.
// usage: node measure-binding.mjs <pipelinenews clone> <october repo copy> <out dir>
import {readFileSync, writeFileSync, mkdirSync} from 'node:fs';
import path from 'node:path';
import {resolveRegister, decodeProjects} from './b/tools/intelligence/register-source.mjs';
import {computeDelta, operatorAliases} from './b/tools/intelligence/register-delta.mjs';
import {buildGazetteer, bindAll} from './b/discovery/project-binder.mjs';

const [pn, oct, out] = process.argv.slice(2);
mkdirSync(out, {recursive: true});
const read = file => JSON.parse(readFileSync(file, 'utf8'));

// Article corpus, deduplicated by URL.
const items = new Map();
const add = (item) => { const key = item.url; if (!key) return; if (!items.has(key)) items.set(key, item); else items.get(key).sources.push(...item.sources); };
const news = read(path.join(pn, 'releases/202609060232-pipelinenews/data/202608271524-fd2212a8c76d-v8-fast-news.json'));
const F = name => news.fields.indexOf(name);
for (const row of news.rows) add({id: row[F('gg_article_id')], url: row[F('url')], headline: row[F('headline')], evidence_snippet: row[F('evidence_snippet')],
  published: row[F('published')], source: row[F('source')], curated: {role: row[F('role')], repd_ref: row[F('repd_ref')] || null, project: row[F('project')] || null}, sources: ['v8-fast-news']});
const sector = read(path.join(pn, 'releases/202609060232-pipelinenews/data/202608272130-sector-intelligence.json'));
const S = name => sector.fields.indexOf(name);
for (const row of sector.rows) add({id: row[S('intelligence_item_id')], url: row[S('canonical_url')], headline: row[S('title')], summary: row[S('summary')],
  published: row[S('source_published_at')], topic: row[S('topic_code')], curated: {role: 'SECTOR_CONTEXT', repd_ref: null}, sources: ['sector-intelligence']});
const rss = read(path.join(pn, 'discovery/products/bbc-rss.json'));
for (const row of rss.items) add({id: row.id, url: row.url, headline: row.headline, published: row.source_published_at, curated: {role: row.binding_status, repd_ref: null}, sources: ['bbc-rss']});
const corpus = [...items.values()];

const q2 = resolveRegister(pn, {release: '202609060232-pipelinenews'});
const q3 = resolveRegister(oct, {release: '202611132345-pipelinenews'});
const q2p = decodeProjects(q2.payload), q3p = decodeProjects(q3.payload);
const delta = computeDelta(q2p, q3p, {previous: q2, next: q3});
writeFileSync(path.join(out, 'register-delta-q2-q3.json'), JSON.stringify(delta, null, 2) + '\n');
const siteAliases = new Map(delta.site_renamed.map(row => [row.repd_ref, [row.from]]));
const g2 = buildGazetteer(q2p);
const g3 = buildGazetteer(q3p, {extraAliases: siteAliases, operatorAliases: operatorAliases(delta)});
const r2 = bindAll(corpus, g2), r3 = bindAll(corpus, g3);

const added = new Set(delta.added);
const summary = {
  corpus: {items: corpus.length, by_source: corpus.reduce((acc, item) => { for (const s of new Set(item.sources)) acc[s] = (acc[s] ?? 0) + 1; return acc; }, {}),
    curated_primary: corpus.filter(item => item.curated.role === 'PRIMARY_MATCH').length},
  registers: {q2: {path: q2.path, sha256: q2.sha256, projects: q2p.length}, q3: {path: q3.path, sha256: q3.sha256, projects: q3p.length}},
  gazetteer: {q2_aliases: g2.alias_count, q3_aliases: g3.alias_count},
  q2_counts: r2.counts, q3_counts: r3.counts,
  delta_counts: delta.counts, delta_gate: delta.gate,
};
// Agreement with curated PRIMARY bindings (hand-approved / v5-v6 builder output).
const agreement = {curated_primary: 0, same_ref: 0, same_development: 0, different_ref: 0, abstained: 0, details: []};
corpus.forEach((item, i) => {
  if (item.curated.role !== 'PRIMARY_MATCH') return;
  agreement.curated_primary++;
  const got = r3.results[i];
  if (got.repd_ref === item.curated.repd_ref) agreement.same_ref++;
  else if (got.outcome === 'PRIMARY_MATCH' && got.related_components.some(c => c.repd_ref === item.curated.repd_ref)) agreement.same_development++;
  else if (got.outcome === 'PRIMARY_MATCH') { agreement.different_ref++; agreement.details.push({headline: item.headline, curated: item.curated, got: got.repd_ref, cand: got.candidates}); }
  else { agreement.abstained++; agreement.details.push({headline: item.headline, curated: item.curated, got: got.outcome, reason: got.reason, cand: got.candidates.map(c => c.repd_ref + ' ' + c.name)}); }
});
summary.agreement_with_curated_primary = {...agreement, details: undefined};
// New bindings that only exist because of Q3 refs.
const newlyBound = [];
corpus.forEach((item, i) => {
  const a = r2.results[i], b = r3.results[i];
  const refs = [b.repd_ref, ...b.candidates.map(c => c.repd_ref)].filter(Boolean);
  if (refs.some(ref => added.has(ref))) newlyBound.push({headline: item.headline, url: item.url, q2: a.outcome, q3: b.outcome, q3_ref: b.repd_ref, candidates: b.candidates});
});
summary.items_touching_refs_added_since_july = newlyBound.length;
summary.changed_outcome_q2_to_q3 = corpus.filter((_, i) => r2.results[i].outcome !== r3.results[i].outcome || r2.results[i].repd_ref !== r3.results[i].repd_ref).length;
// Bound projects whose status changed Q2->Q3: review signal.
const statusMap = new Map(delta.status_changed.map(row => [row.repd_ref, row]));
summary.bound_items_with_status_change = r3.results.filter(r => r.repd_ref && statusMap.has(r.repd_ref)).map(r => ({repd_ref: r.repd_ref, ...statusMap.get(r.repd_ref)}));

const rows = corpus.map((item, i) => ({url: item.url, headline: item.headline, sources: [...new Set(item.sources)], topic: item.topic ?? null,
  curated: item.curated, q2: pick(r2.results[i]), q3: pick(r3.results[i])}));
function pick(r) { return {outcome: r.outcome, reason: r.reason, repd_ref: r.repd_ref, capacity_check: r.capacity_check?.status ?? null, reported_mw: r.capacity_check?.reported_mw, register_mw: r.capacity_check?.register_mw, candidates: r.candidates.map(c => `${c.repd_ref}:${c.name}`), related: r.related_components.map(c => c.repd_ref)}; }
writeFileSync(path.join(out, 'binding-results.json'), JSON.stringify(rows, null, 1) + '\n');
writeFileSync(path.join(out, 'binding-summary.json'), JSON.stringify({...summary, disagreements: agreement.details, newly_bound: newlyBound}, null, 1) + '\n');
console.log(JSON.stringify(summary, null, 1));
