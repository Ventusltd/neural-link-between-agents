import {readFileSync, writeFileSync} from 'node:fs';
import {verifyRegisterBytes, buildSites, bindDataCentres} from './b/discovery/datacentre-binder.mjs';
const [geo, pn, out] = process.argv.slice(2);
const reg = buildSites(verifyRegisterBytes(readFileSync(geo)));
const sector = JSON.parse(readFileSync(`${pn}/releases/202609060232-pipelinenews/data/202608272130-sector-intelligence.json`, 'utf8'));
const S = n => sector.fields.indexOf(n);
const news = JSON.parse(readFileSync(`${pn}/releases/202609060232-pipelinenews/data/202608271524-fd2212a8c76d-v8-fast-news.json`, 'utf8'));
const F = n => news.fields.indexOf(n);
const items = new Map();
for (const r of sector.rows) items.set(r[S('canonical_url')], {id: r[S('intelligence_item_id')], url: r[S('canonical_url')], headline: r[S('title')], summary: r[S('summary')], frozen_topic: r[S('topic_code')]});
for (const r of news.rows) if (!items.has(r[F('url')])) items.set(r[F('url')], {id: r[F('gg_article_id')], url: r[F('url')], headline: r[F('headline')], evidence_snippet: r[F('evidence_snippet')], frozen_topic: null});
const list = [...items.values()];
const res = bindDataCentres(list, reg);
const named = reg.sites.filter(s => s.identities.length).length;
const summary = {register_sites: reg.sites.length, sites_with_name_identity: named, alias_count: reg.aliases.length,
  map_status: reg.sites.reduce((a, s) => (a[s.map_status] = (a[s.map_status] ?? 0) + 1, a), {}),
  items: list.length, frozen_data_centre_topic_items: list.filter(i => i.frozen_topic === 'DATA_CENTRES').length, counts: res.counts,
  rows: res.results.filter(r => r.outcome !== 'NOT_DATA_CENTRE_TOPIC').map((r, i) => ({headline: list.find(x => (x.id ?? x.url) === r.item_id).headline, outcome: r.outcome, reason: r.reason, dc_site_id: r.dc_site_id, site: r.site_name ?? null, map: r.map_status, candidates: r.candidates.slice(0, 5).map(c => `${c.dc_site_id}:${c.name}`)}))};
writeFileSync(out, JSON.stringify(summary, null, 1) + '\n'); console.log(JSON.stringify(summary, null, 1));
