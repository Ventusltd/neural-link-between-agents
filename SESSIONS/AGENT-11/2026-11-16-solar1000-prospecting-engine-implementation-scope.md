# Agent 11 — Pipeline News Solar-1000 Evidence and Prospecting Engine
**Build training scope | 16 November 2026 | Owner: Ventus Ltd | Status: IMPLEMENTATION HANDOFF, NOT A LIVE RELEASE**

## 1. Mission
Build an evidence-based prospecting engine for **exactly the first 1,000 Solar Photovoltaics entries** in the October 2026 Renewable Energy Planning Database (REPD), as published in Pipeline News. Seek at least one **useful independent-source remark per project**. Where none exists, write “No independent evidence found; research attempted”. Never invent evidence to reach 100%.

Identify owners, developments, likely next steps and reasons to investigate or visit. Measure time saved finding *qualified* opportunities, not headline volume.

## 2. Mandatory context and ownership
Read these first:
- Live immutable V9.23: https://globalgrid2050.com/uk_renewables_pipeline/202611160020/
- Published V9.22 rollback: https://globalgrid2050.com/uk_renewables_pipeline/202611151300/
- Product source: https://github.com/Ventusltd/globalgrid2050
- Neural Link protocol: https://github.com/Ventusltd/neural-link-between-agents/blob/main/PROTOCOL.md
- Agent 10 coordination: https://github.com/Ventusltd/neural-link-between-agents/issues/40
- Release coordination: https://github.com/Ventusltd/neural-link-between-agents/issues/30

**Agent 11** owns an exclusive Solar-1000 implementation branch. Acknowledge in Neural Link with HEAD SHA, branch and draft PR. Request Agents 3/4/5 for independent tests. Do not modify Agent 9’s GridAtlas receiver. Issue comments do not start AI agents.

## 3. Freeze and identify the sample
From the V9.23 pinned REPD source, filter **Technology = Solar Photovoltaics**, sort by numeric REPD Ref ID and select the first 1,000 *after filtering*. Save IDs, source SHA256, row hashes, snapshot and extraction script. Test distinct IDs, repeatable ordering and V9.23 membership; never add external examples to the sample.

Keep all official REPD fields read-only. Store a versioned notes sidecar keyed by **vertical + source + snapshot + REPD record ID**. Preserve all 7,775 rows, MAP links and exports.

## 4. Source discovery
Search each row against councils’ planning records, Planning Inspectorate/NSIP files, developer/operator notices, grid and procurement documents, reputable news and licensed public datasets. Combine planning reference, authority, project name, postcode, developer, location and REPD ID. Confirm physical-project identity; similar names **never** suffice.

Use Python source adapters, licensed APIs, bounded searches, caching, backoff and rate limits. Respect robots.txt, copyright, GDPR and access restrictions; never bypass paywalls or CAPTCHA. Save metadata and short factual extracts with original links. Log source failures.

## 5. Evidence and remarks contract
Each item stores asset key, URL, publisher, source type, matching clues, source locator, independent factual remark, category, confidence, rationale, extraction version, reviewer status and four clocks: **event, publication, fetched and first-seen dates**. Unknown dates are null; fetch date is not event date.

Categories: planning, ownership/finance, EPC/procurement, construction, grid, consultation/visits and next action. Explain what happened, source and commercial relevance. Separate **verified fact**, **candidate match** and **inference**. Flag REPD contradictions without changing official status. No personal contact harvesting.

No-evidence status is **not a sourced remark**. Report independently evidenced coverage separately from reviewed coverage. REPD repetition and speculative headlines do not qualify.

## 6. Prospecting usefulness
Display a neutral 15–30-word headline in the native **Machine Read Notes** column and a 100–180-word expandable brief with sources, dates, confidence, commercial relevance and suggested human next step. Publish a transparent prioritisation score based on stage, MW, recency and potential electrical work. Ranking is not a verified fact; no automatic outreach.

## 7. TestCode-first implementation
Develop in TestCode first: adapters, entity resolution, extraction, four-clock model, deduplication, versioned sidecar, reports and CLI. Test duplicate names, wrong planning refs, separate phases, ambiguity, missing dates, recycled news, inaccessible sites, injected text, malicious URLs, encoding, network failure and interrupted/replayed runs. Reruns must be idempotent.

Provide RED-to-GREEN Python and Chrome/WebKit evidence pinned to SHA. Test sort, filter, pagination, fullscreen report, desktop/390px mobile and original MAP-link parity. Existing GridAtlas mobile re-minimisation remains **RED** until separately fixed.

## 8. Acceptance measurements
Publish a 1,000-row ledger: researched, independently sourced, verified, accepted, candidate, no-source, blocked and actionable. Measure source diversity, categories, timestamps, false matches, cost and throughput. Audit **100 stratified rows** and **50 collision/negative controls**. Aim for **≥98% correct attribution** among accepted audited remarks and zero known cross-project leaks; disclose denominators. Benchmark credible meeting opportunities per 100 rows and minutes per qualified lead against manual prospecting. Never claim unmeasured ROI.

## 9. Handover and release boundary
Commit manifest, code, licence registry, schemas, fixtures, CI, evidence receipts, metrics and failure log. Bound GitHub Actions costs and refresh cadence; automated workflows execute scripts, not independent AI invention. Post exact PR/SHA/CI receipts in Neural Link. Prepare **V9.24 as non-live candidate only**. Never overwrite V9.22/V9.23, change homepage or GridAtlas. Public promotion requires separate owner authorisation.

**Done:** 1,000 deterministic IDs, one evidenced remark or honest fallback per row, auditable source matches, tested mobile/export behaviour and a filterable list of defensible next conversations.
