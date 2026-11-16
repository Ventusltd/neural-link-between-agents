# Agent 11 — Pipeline News Solar-1000 Evidence and Prospecting Engine
**Build training scope | 16 November 2026 | Owner: Ventus Ltd | Status: IMPLEMENTATION HANDOFF, NOT A LIVE RELEASE**

## 1. Mission
Build an evidence-grounded intelligence engine that saves a person the tedious work of prospecting thousands of renewable-energy projects. The initial experiment concerns **exactly the first 1,000 Solar Photovoltaics entries** in the official October 2026 Renewable Energy Planning Database (REPD) as represented by GlobalGrid2050 Pipeline News. Each project should receive at least one **genuinely useful, independently sourced remark wherever evidence exists**. A truthful “No independent evidence found; research attempted” outcome is mandatory when it does not. Never manufacture a remark to achieve a numerical target.

This is infrastructure intelligence, not an indiscriminate sales-lead scraper. Identify who owns a project, what changed, what may happen next, and why an informed professional might investigate or arrange a meeting. Measure time saved finding *qualified* opportunities, not merely headlines collected.

## 2. Mandatory context and ownership
Read these first:
- Live immutable V9.23: https://globalgrid2050.com/uk_renewables_pipeline/202611160020/
- Published V9.22 rollback: https://globalgrid2050.com/uk_renewables_pipeline/202611151300/
- Product source: https://github.com/Ventusltd/globalgrid2050
- Neural Link protocol: https://github.com/Ventusltd/neural-link-between-agents/blob/main/PROTOCOL.md
- Agent 10 coordination: https://github.com/Ventusltd/neural-link-between-agents/issues/40
- Release coordination: https://github.com/Ventusltd/neural-link-between-agents/issues/30

Act as **Agent 11**, the sole owner of the Solar-1000 research/implementation branch. First acknowledge the assignment in Neural Link, state the exact HEAD SHA, chosen repository and exclusive branch, and link a draft PR. Coordinate with Agents 3/4/5 on tests and editorial challenge, but do not modify Agent 9's GridAtlas receiver or another agent's branch. Neural Link issues are asynchronous messages, not automatically executing AI agents.

## 3. Freeze and identify the sample
Load the pinned October 2026 REPD source used by V9.23, filter exact **Technology = Solar Photovoltaics**, sort by canonical numeric REPD Ref ID and select the first 1,000 *after filtering*. Save their ordered IDs, canonical source SHA256, row hashes, snapshot identifier and extraction script. Assert exactly 1,000 distinct IDs, deterministic repeatability and that every ID belongs to the V9.23 source. Never filter by installed capacity unless the published dataset itself imposes its existing constraint. A project from an external example that is absent from these 1,000 must **not** be smuggled into the test set.

REPD name, capacity, developer, location, technology, planning status, dates and coordinates remain read-only. Maintain a separate, versioned notes sidecar keyed by **vertical + source + snapshot + REPD record ID**; preserve the existing MAP deep links, exports, chronology and all 7,775 source records.

## 4. Source discovery
For each selected row, search in descending authority: the relevant council planning register and decision documents; Planning Inspectorate/NSIP case files; developer, landowner and operator announcements; official grid and procurement disclosures; reputable local newspapers and trade publications; permitted public datasets. Query combinations of exact planning reference, authority, project name, postcode, developer, location and REPD ID. Confirm each source really describes the same physical project. Councils often use different sites, aliases, phases and project names; similar names are **not** sufficient.

Use Python adapters, permitted APIs, bounded searches, persistent HTTP caches, retries with backoff and source-specific rate limits. Respect robots.txt, licensing, data protection and publisher restrictions. Do not evade CAPTCHA, logins or paywalls. Keep raw evidence metadata and a short factual extraction; link to the original rather than reproduce copyrighted articles. Failed or unavailable sources are logged, not silently treated as negative project facts.

## 5. Evidence and remarks contract
Every evidence item records: asset key; source URL; source organisation; source type; exact matching evidence (planning ref/ID/geography/developer); quoted evidence span or locator where permitted; concise independently worded factual remark; event category; confidence; match rationale; extraction version; reviewer status; and four separate clocks: **event date, publication date, fetch date and first-seen date**. Unknown dates remain null. Fetch time must never masquerade as the event date.

Useful categories: planning submission/decision/appeal; project ownership or finance; developer/EPC or cable procurement; construction and commissioning; grid connection; community consultation/site meeting; and concrete next action. Each remark answers “What happened?”, “What is the source?” and “Why might this matter?”. Distinguish **verified source fact**, **project-match candidate** and **inference**. If the independent source contradicts REPD, show the discrepancy without changing the official status. Do not infer personal email addresses, individual intentions or private contact data.

A no-evidence record is an *explicit research status*, **not a sourced remark**. Track externally evidenced coverage and total reviewed coverage separately. Do not count a repeated REPD field or speculative headline as independent evidence.

## 6. Prospecting usefulness
Generate a neutral 15–30-word headline visible in the existing native **Machine Read Notes** column, followed by a 100–180-word expandable brief with original publisher links. Add event age, provenance, confidence, reason to investigate and proposed non-automated next action. Prioritisation may consider project stage, MW, change recency, likely electrical work and identifiable corporate entity; publish the scoring formula and reasons. Keep opportunity ranking **separate** from confirmed project facts. No automatic unsolicited outreach, private-person profiles or invented procurement mandates.

## 7. TestCode-first implementation
Use an isolated implementation branch and TestCode fixtures. Deliver executable modules for source adapter/search, entity resolution, event extraction, four-clock handling, deduplication, immutable JSON sidecar, enrichment reports and a deterministic CLI. Add automated mocks and hostile cases: duplicate project names across counties; wrong planning reference; nearby but distinct phases; ambiguous company; missing publication date; stale press recycled as new; inaccessible source; injection in HTML; malicious URLs; broken encoding; site ownership changes; failed network; and interrupted/replayed runs. Re-running the same snapshot must not duplicate remarks or mutate REPD bytes.

Show RED-to-GREEN Python tests and headless Chrome/WebKit evidence on the exact candidate SHA. Test table filtering, sorting, pagination and report restoration on desktop and 390px portrait/mobile landscape. Preserve every original MAP URL character-for-character. The known independent GridAtlas mobile nearest-result re-minimisation remains **RED until separately repaired**, even if Pipeline News static MAP-link tests pass.

## 8. Acceptance measurements
Produce a machine-readable 1,000-row coverage ledger: researched, independent source found, source verified, project match accepted, candidate only, no source, blocked, and actionable next step. Report unique source domains, category distribution, date completeness, provenance failures, cost per valid remark and processing time. Manually review at least **100 stratified rows**, including ambiguous/no-source projects, and run at least **50 negative/collision controls**. Target **at least 98% correct project attribution** among accepted independent remarks in the audited sample, with **zero known cross-project leaks**; disclose the denominator and any failure. Track useful leads per 100 rows and minutes required to find one credible meeting candidate against a manual baseline. Claim neither 100% evidence coverage nor commercial ROI without measured data.

## 9. Handover and release boundary
Commit a reproducible dataset manifest, Python source, licence and source registry, schemas, test fixtures, CI workflow, sample evidence receipts, coverage metrics and known-failure log. Use GitHub Actions with explicit budgets, bounded concurrency and cached incremental refreshes; a workflow can execute deterministic scripts but cannot autonomously improvise new agent code. Post signed findings and exact commit/PR/CI links in Neural Link. Prepare **V9.24 as a non-live candidate only** after the 1,000-row pilot passes. Do not overwrite, relabel or redeploy V9.22/V9.23, change the homepage pointer or alter GridAtlas. Any later public promotion is a separate owner-authorised release step.

**Definition of done:** the same 1,000 IDs appear in the source manifest and notes ledger; every row has a valid evidence-backed remark or honest no-evidence/blocked result; cited matches survive manual/adversarial audits; mobile and export regressions are documented; and a human can filter the table to find defensible next conversations without opening hundreds of irrelevant records.
