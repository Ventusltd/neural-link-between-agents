# GLOBALGRID2050 — Agent 13 / V9.25 engineering execution board
**Date:** 2026-11-16 (UTC)  
**Type:** OWNER-REQUESTED IMPLEMENTATION PLAN; no V9.25 code or deployment is claimed here.  
**Primary coordination:** https://github.com/Ventusltd/neural-link-between-agents/issues/41  
**Baseline:** GlobalGrid2050 main `42fdb5af4b1479507b38cf8142dba5da1a238fa0` at inspection. Revalidate immediately before work.  
**Task discipline:** All tasks are independent **15-minute maximum timeboxes**. A partial task is BLOCKED/IN-PROGRESS, *never PASS*; split the remaining work into another <=15 minute ticket with fresh ID and evidence. Task completion means committed code/test/config/receipt, not conversational assertion.

## Executive assessment and recommended strategy

**Recommendation:** Publish a *small working universal kernel* in V9.25: preserve the frozen 1,000 solar pilot; add one separate <=1,000 solar+BESS >20 MW research cohort; implement approved source-first and project-first acquisition, strict independent review and immutable weekly data snapshots; expose solar, BESS, data-centre and generic remaining-category views without asserting speculative evidence. Do not wait for 100% source coverage. A source adapter that lacks verified legal/technical access stays disabled. All six categories share schemas, with narrowly supported official-source adapters first; adding comprehensive sources later is a separate increment.

**Verified from current source:** `automation/news/` has `binder.py`, `pipeline_headlines.py`, `events.py`, `relevance.py`, `evidence_ledger.py`, `datacentre_feed.py` and `pipeline_feeds.json`. `.github/workflows/pipeline-headlines.yml` and `datacentre-news.yml` already refresh dedicated data branches. The `new_version.py` builder chooses the last registry entry as its parent. `scripts/import_homepage_owner.py` intentionally rewrites asset and catalogue paths and normalises newlines: owner index hashes must *not* be compared blindly with built root index hashes.

**Two specific pre-release defects (inspected 16 Nov):** `automation/pipeline_release/registry.json` V9.24 (`202611161244`) is still `release_candidate_known_unverified_sources` with `ci:null` and `merge_commit:null`, although merge PR #123 has been reported; `uk_renewables_pipeline/versions.json` lists V9.24 at top with PASS but its separate `release_candidate.operative` still identifies V9.23. Reconcile exact authoritative receipts and repair *mutable metadata only*, not the V9.24 historical tree.

**Evidence limitation:** `evidence_ledger.assess()` explicitly returns `accepted_for_publication: False` even after structural validation. No agent may redefine machine confidence as independent proof. The V9.24 pilot has 2 provisional leads (1019, 1020), 998 not researched, **0 independently verified findings**. Real reviewer/rights acceptance is mandatory for VERIFIED.

**Ownership and collision control:** Agent 13 alone owns integrating/releasing V9.25 and any homepage promotion. Implementation agents (suggested Agent 14 data contracts, 15 sources, 16 matching/history, 17 persistence, 18 CI, 20 DC/categories, 21 UI) own **separate topic branches** and work in named scopes; Agent 19 provides read-only independent verification. Do not assert Agent 12 is inactive merely because no matching V9.25 PR or branch was returned in inspection; recheck issue #41, GitHub and owner instructions immediately before code/release writes. No concurrent writers to registry, homepage pointer or final release branch. GitHub comments do not wake agents; each must ACK when next invoked.

**Effort estimate:** 200 x 15 minutes = **50 focused engineering hours** maximum planned task budgets, plus **25% integration/rework reserve (12.5 h)** = **62.5 engineer-hours** of planned work. This is an *effort*, not a promise of delivery time. With 4–6 truly concurrent scoped agents, a plausible critical-path elapsed range is **3–6 working days**, dependent on CI queue, owner coordination and third-party licensing. Publisher permissions, CAPTCHA-blocked sources, missing data or late GitHub schedules add unbounded waiting and must be logged explicitly. First functional evidence refresh can precede the V9.25 live release.

**Stages:** A = prerequisites and SHA integrity (01–04); B = verified contracts and acquisition (05–16); C = persistence, exports and category adapters (17–21); D = workflows/UI (22–23); E = QA, integration, public proof (24–25). Every track submits a small reviewed PR. Parallelise only after interfaces and identity contracts are frozen.

## Hard contracts / exit gates

1. **No source facts changed:** 7,775 official records, 3,604 solar count, immutable V9.24 and V9.23 bytes, existing MAP/CSV functionality.
2. **No conflation:** Solar-1000 remains sorted numerically, IDs 1018..2325; the separate research cohort uses strict `capacity_mw > 20` and may contain at most 1,000 solar+BESS projects. Stable manifests + SHA in exports.
3. **Evidence provenance:** original receipt, rights, project binding and event assertion distinct. `VERIFIED` needs an independent review decision and attributable receipt. Time precision maintained. Explicit negative research attempts.
4. **No speculative coordinates or connections:** preserve null geometry and do not infer grid capacity/contract from proximity.
5. **No silent side effects:** weekly data branch only; write-once snapshots, atomic latest pointer, fail-closed freshness/rights, branch-leased writes. No scheduled write to V9.25 release folder or home.
6. **Publishing:** actual source and transformed byte hashes, exact-head tests, original browser flows, Pages deployment and public served-byte readback. Declared GridAtlas mobile defect cannot become a fabricated PASS.

## Agent assignment and integration protocol

| Agent / proposed branch scope | Responsibilities | Forbidden writes |
| --- | --- | --- |
| 13 `release/v925-agent13` (create only after collision check) | release owner, integration, registry/pointer, public proof | other agents' branches |
| 14 `agent14/v925-contracts` | identity/schema, reviews contract, pilot manifests | homepage/registry |
| 15 `agent15/v925-sources` | source audits, RSS/API fetcher, incremental collection | release folder |
| 16 `agent16/v925-research` | research queue, official adapters, binder/event history | published data branch |
| 17 `agent17/v925-store` | SQLite, exports, snapshots, metrics | homepage |
| 18 `agent18/v925-release-qa` | metadata repair + CI workflow; propose PR, do not promote | operative pointer without Agent 13 |
| 19 `agent19/v925-independent-review` | independent source/rights/editorial/browser QA, read-only against producers | producer code or approval spoofing |
| 20 `agent20/v925-categories` | dcuk, grid, wind and relationships | REPD immutable facts |
| 21 `agent21/v925-ui` | additive panels, fullscreen, MAP/CSV compatibility | historical release trees |

Proposed labels are *handoff slots*, not evidence these agents currently run. Separate PRs must declare their exact ownership path and dependency; Agent 13 cherry-picks or merges accepted PRs only after exact-head checks. Every task report: `ID | scope | branch | SHA | CI URL | PASS/FAIL/BLOCKED | next 15-minute task`. No silent takeover of Agent 12/11 work.

## Granular execution board — 200 tasks, 15 minutes or less each


### 01 — Coordination, exclusive ownership and source pinning
Owner: **Agent 13 — integrator**. Dependencies: none. Planned budget: 120 min.

- [ ] **T001 — 15 min:** Read issue #41 plus newest comments; capture any superseding owner decisions in a dated note; attach a small commit, test or signed receipt.
- [ ] **T002 — 15 min:** Search main, V9.25 branches, open PRs and Agent 12 activity; record actual query evidence; attach a small commit, test or signed receipt.
- [ ] **T003 — 15 min:** Read AGENTS.md and Neural Link PROTOCOL.md; extract write and ACK restrictions; attach a small commit, test or signed receipt.
- [ ] **T004 — 15 min:** Record a single V9.25 release owner; reserve all other agents to non-publishing branches; attach a small commit, test or signed receipt.
- [ ] **T005 — 15 min:** Pin current globalgrid2050 main commit, homepage-owner commit and TestCode PR #16 head; attach a small commit, test or signed receipt.
- [ ] **T006 — 15 min:** Create per-agent exclusive branch/path ownership table and prohibited shared-file list; attach a small commit, test or signed receipt.
- [ ] **T007 — 15 min:** Write a one-screen decision log: MVP, deferred source coverage and no fake VERIFIED rows; attach a small commit, test or signed receipt.
- [ ] **T008 — 15 min:** Post owner/branch declaration and require each agent's explicit ACK before coding; attach a small commit, test or signed receipt.

### 02 — Baseline and immutable identity contracts
Owner: **Agent 14 — data contracts**. Dependencies: 01. Planned budget: 120 min.

- [ ] **T009 — 15 min:** Load V9.24 release and check immutable folder 202611161244 exists without modification; attach a small commit, test or signed receipt.
- [ ] **T010 — 15 min:** Record release counts 7,775 REPD and 3,604 solar from pinned artifacts; attach a small commit, test or signed receipt.
- [ ] **T011 — 15 min:** Locate and SHA256-pin V9.24 numeric Solar-1000 manifest, IDs 1018–2325; attach a small commit, test or signed receipt.
- [ ] **T012 — 15 min:** Write regression test asserting exactly those 1,000 distinct numeric REPD references; attach a small commit, test or signed receipt.
- [ ] **T013 — 15 min:** Write test preserving all below/at-20 MW pilot records without exclusion; attach a small commit, test or signed receipt.
- [ ] **T014 — 15 min:** Capture existing two provisional candidates and zero independently verified as baseline; attach a small commit, test or signed receipt.
- [ ] **T015 — 15 min:** Identify official REPD columns, canonical status vocabulary and capacity units; attach a small commit, test or signed receipt.
- [ ] **T016 — 15 min:** Save baseline fixture hashes and a no-mutation assertion for historical release directories; attach a small commit, test or signed receipt.

### 03 — Registry and release-pointer repair
Owner: **Agent 18 — CI/release engineer**. Dependencies: 01,02. Planned budget: 120 min.

- [ ] **T017 — 15 min:** Read registry tail and compare V9.24 entry with merged PR #123 receipt; attach a small commit, test or signed receipt.
- [ ] **T018 — 15 min:** Verify exact V9.24 merge SHA c2a12518 against the merge record before editing metadata; attach a small commit, test or signed receipt.
- [ ] **T019 — 15 min:** Check V9.24 full verification and Pages run conclusions; capture run URLs and timestamps; attach a small commit, test or signed receipt.
- [ ] **T020 — 15 min:** Identify missing registry CI and merge fields without changing stored tree hashes; attach a small commit, test or signed receipt.
- [ ] **T021 — 15 min:** Inspect versions.json head V9.24 and stale release_candidate operative V9.23; attach a small commit, test or signed receipt.
- [ ] **T022 — 15 min:** Find source of versions.json generation and define one authoritative operative pointer; attach a small commit, test or signed receipt.
- [ ] **T023 — 15 min:** Write a failing test for contradictory candidate/operative/version-list metadata; attach a small commit, test or signed receipt.
- [ ] **T024 — 15 min:** Create metadata-only repair PR with tests; leave all V9.24 frozen files untouched; attach a small commit, test or signed receipt.

### 04 — Homepage transformation and served-byte integrity
Owner: **Agent 18 — CI/release engineer**. Dependencies: 03. Planned budget: 120 min.

- [ ] **T025 — 15 min:** Verify seven owner files and SHA256 pins in catalogue/homepage-owner.json; attach a small commit, test or signed receipt.
- [ ] **T026 — 15 min:** Trace index.html rewrites in scripts/import_homepage_owner.py; attach a small commit, test or signed receipt.
- [ ] **T027 — 15 min:** Record transformed asset paths and final newline rules as deterministic operations; attach a small commit, test or signed receipt.
- [ ] **T028 — 15 min:** Implement test computing expected output SHA from pinned owner index bytes; attach a small commit, test or signed receipt.
- [ ] **T029 — 15 min:** Implement test comparing built homepage artifact hash with expected transformed hash; attach a small commit, test or signed receipt.
- [ ] **T030 — 15 min:** Implement served-byte check for public root and release HTML with cache headers; attach a small commit, test or signed receipt.
- [ ] **T031 — 15 min:** Write negative tests for wrong path, wrong pinned SHA and wrong release pointer; attach a small commit, test or signed receipt.
- [ ] **T032 — 15 min:** Record three separate receipts: source pins, build transform and public served bytes; attach a small commit, test or signed receipt.

### 05 — Canonical evidence and project schemas
Owner: **Agent 14 — data contracts**. Dependencies: 02. Planned budget: 120 min.

- [ ] **T033 — 15 min:** Enumerate existing evidence_ledger.py ArticleReceipt, ProjectBinding, EventAssertion and RightsAssessment keys; attach a small commit, test or signed receipt.
- [ ] **T034 — 15 min:** Define namespaced project IDs: repd:<id>, dcuk:<id>, grid:<id>, wind where applicable; attach a small commit, test or signed receipt.
- [ ] **T035 — 15 min:** Specify nullable dates with explicit day, month, year or unknown precision; attach a small commit, test or signed receipt.
- [ ] **T036 — 15 min:** Define research statuses NOT_RESEARCHED, RESEARCH_ATTEMPTED_NO_EVIDENCE, PROVISIONAL, VERIFIED, REJECTED; attach a small commit, test or signed receipt.
- [ ] **T037 — 15 min:** Define distinct confidence, acceptance, research-priority and event-impact fields; attach a small commit, test or signed receipt.
- [ ] **T038 — 15 min:** Add JSON schema for article receipt and source provenance with safe URL rules; attach a small commit, test or signed receipt.
- [ ] **T039 — 15 min:** Add JSON schema for project binding and event assertion without conflating identities; attach a small commit, test or signed receipt.
- [ ] **T040 — 15 min:** Add round-trip schema fixtures and reject invented timestamps or coordinates; attach a small commit, test or signed receipt.

### 06 — Rights, genuine independent review and acceptance
Owner: **Agent 14 — data contracts + Agent 19 reviewer**. Dependencies: 05. Planned budget: 120 min.

- [ ] **T041 — 15 min:** Document that evidence_ledger.assess currently never returns publishable acceptance; attach a small commit, test or signed receipt.
- [ ] **T042 — 15 min:** Define independent review register keyed to immutable receipt and binding hash; attach a small commit, test or signed receipt.
- [ ] **T043 — 15 min:** Separate review of source authenticity, legal rights, project identity and event claim; attach a small commit, test or signed receipt.
- [ ] **T044 — 15 min:** Reject self-review where proposing and reviewing roles are identical; attach a small commit, test or signed receipt.
- [ ] **T045 — 15 min:** Design revocation behaviour so a withdrawn decision cannot stay VERIFIED; attach a small commit, test or signed receipt.
- [ ] **T046 — 15 min:** Test a structurally complete but unauthenticated record remains PROVISIONAL; attach a small commit, test or signed receipt.
- [ ] **T047 — 15 min:** Test rights-only approval does not grant event acceptance or publication eligibility; attach a small commit, test or signed receipt.
- [ ] **T048 — 15 min:** Require externally attributable review evidence before the verified counter increments; attach a small commit, test or signed receipt.

### 07 — Source registry and safe configuration
Owner: **Agent 15 — acquisition**. Dependencies: 05,06. Planned budget: 120 min.

- [ ] **T049 — 15 min:** Inventory pipeline_feeds.json to reuse accepted feed entries and ownership; attach a small commit, test or signed receipt.
- [ ] **T050 — 15 min:** Choose additive evidence source registry format; avoid duplicate YAML/JSON competing owners; attach a small commit, test or signed receipt.
- [ ] **T051 — 15 min:** Define source ID, host allowlist, category, interval, timeout, bytes and rights policy; attach a small commit, test or signed receipt.
- [ ] **T052 — 15 min:** Create three approved-source test fixtures and one disabled/unlicensed-source fixture; attach a small commit, test or signed receipt.
- [ ] **T053 — 15 min:** Add validation for duplicate IDs and invalid URL schemes or hostnames; attach a small commit, test or signed receipt.
- [ ] **T054 — 15 min:** Add validation for malformed intervals, incompatible kind and unsupported output policy; attach a small commit, test or signed receipt.
- [ ] **T055 — 15 min:** Specify GitHub Actions secret references without storing credentials in source configuration; attach a small commit, test or signed receipt.
- [ ] **T056 — 15 min:** Add tests rejecting all redirect destinations absent from each source allowlist; attach a small commit, test or signed receipt.

### 08 — Publisher and public-register live probe
Owner: **Agent 15 — acquisition**. Dependencies: 07. Planned budget: 120 min.

- [ ] **T057 — 15 min:** Probe PV Magazine global feed status, date fields and link policy; save a health receipt; attach a small commit, test or signed receipt.
- [ ] **T058 — 15 min:** Probe PV-Tech source interface and document whether a permissioned endpoint exists; attach a small commit, test or signed receipt.
- [ ] **T059 — 15 min:** Probe Solar Power Portal public feed/API and record host, robots and attribution; attach a small commit, test or signed receipt.
- [ ] **T060 — 15 min:** Probe Energy Storage News public feed/API and record host, robots and attribution; attach a small commit, test or signed receipt.
- [ ] **T061 — 15 min:** Probe reNEWS or another renewable publisher and record actual supported endpoint; attach a small commit, test or signed receipt.
- [ ] **T062 — 15 min:** Probe one accessible Planning Inspectorate or GOV.UK public dataset/API; attach a small commit, test or signed receipt.
- [ ] **T063 — 15 min:** Probe one public local authority planning portal without bypassing access restrictions; attach a small commit, test or signed receipt.
- [ ] **T064 — 15 min:** Save rights-and-coverage matrix; keep uncertain sources disabled by default; attach a small commit, test or signed receipt.

### 09 — Transport: bounded HTTP fetching
Owner: **Agent 15 — acquisition**. Dependencies: 07. Planned budget: 120 min.

- [ ] **T065 — 15 min:** Implement shared HTTP request with identifiable User-Agent and explicit accept headers; attach a small commit, test or signed receipt.
- [ ] **T066 — 15 min:** Add connect/read timeouts and maximum downloaded response bytes; attach a small commit, test or signed receipt.
- [ ] **T067 — 15 min:** Constrain HTTPS and reject private/local hosts, credentials and unsafe schemes; attach a small commit, test or signed receipt.
- [ ] **T068 — 15 min:** Validate resolved addresses and every redirect hop against approved public endpoints; attach a small commit, test or signed receipt.
- [ ] **T069 — 15 min:** Classify HTTP 200, 304, 403, 404, 429 and 5xx outcomes; attach a small commit, test or signed receipt.
- [ ] **T070 — 15 min:** Add deterministic unit tests for denied redirect, oversized body and timeout; attach a small commit, test or signed receipt.
- [ ] **T071 — 15 min:** Parse RSS and Atom via the existing feed conventions, preserving canonical URLs; attach a small commit, test or signed receipt.
- [ ] **T072 — 15 min:** Add JSON/API adapter interface with an offline fixture and bounded response parser; attach a small commit, test or signed receipt.

### 10 — Incremental collection and source resilience
Owner: **Agent 15 — acquisition**. Dependencies: 09. Planned budget: 120 min.

- [ ] **T073 — 15 min:** Persist per-source ETag and Last-Modified only after successful validation; attach a small commit, test or signed receipt.
- [ ] **T074 — 15 min:** Send conditional requests and count HTTP 304 as a healthy unchanged fetch; attach a small commit, test or signed receipt.
- [ ] **T075 — 15 min:** Implement capped exponential backoff for 429 and transient 5xx; attach a small commit, test or signed receipt.
- [ ] **T076 — 15 min:** Stop retries immediately for 401/403/robots/licence restrictions; attach a small commit, test or signed receipt.
- [ ] **T077 — 15 min:** Store per-source last attempt, last success, next due and cursor metadata; attach a small commit, test or signed receipt.
- [ ] **T078 — 15 min:** Ensure one source failure retains previously accepted evidence unchanged; attach a small commit, test or signed receipt.
- [ ] **T079 — 15 min:** Implement stale-source warning and dry-run source health summary; attach a small commit, test or signed receipt.
- [ ] **T080 — 15 min:** Test idempotent second fetch creates no new logical article or false research-negative; attach a small commit, test or signed receipt.

### 11 — Solar-1000 and >20 MW priority manifests
Owner: **Agent 14 — data contracts**. Dependencies: 02,05. Planned budget: 120 min.

- [ ] **T081 — 15 min:** Reproduce the fixed numeric Solar-1000 manifest without rewriting it; attach a small commit, test or signed receipt.
- [ ] **T082 — 15 min:** Implement strict >20.0 MW test, excluding exactly 20.0 MW from priority research; attach a small commit, test or signed receipt.
- [ ] **T083 — 15 min:** Create deterministic eligible solar candidate listing from the frozen official register; attach a small commit, test or signed receipt.
- [ ] **T084 — 15 min:** Create deterministic eligible BESS candidate listing from the same pinned register; attach a small commit, test or signed receipt.
- [ ] **T085 — 15 min:** Define technology, capacity, status and evidence-gap priority weights with reasons; attach a small commit, test or signed receipt.
- [ ] **T086 — 15 min:** Merge and cap priority solar+BESS cohort at 1,000 stable unique IDs; attach a small commit, test or signed receipt.
- [ ] **T087 — 15 min:** Store both manifest source hashes, selection rules and per-category counts; attach a small commit, test or signed receipt.
- [ ] **T088 — 15 min:** Test reordering source CSV rows leaves priority IDs and output order unchanged; attach a small commit, test or signed receipt.

### 12 — Project-first search queue and budgets
Owner: **Agent 16 — project research**. Dependencies: 07,11. Planned budget: 120 min.

- [ ] **T089 — 15 min:** Define query seed using exact planning reference plus authority and REPD identity; attach a small commit, test or signed receipt.
- [ ] **T090 — 15 min:** Add distinctive project name plus local authority query variant; attach a small commit, test or signed receipt.
- [ ] **T091 — 15 min:** Add developer, county, capacity and known aliases query variant; attach a small commit, test or signed receipt.
- [ ] **T092 — 15 min:** Suppress ambiguous one-word project names unless independently corroborated; attach a small commit, test or signed receipt.
- [ ] **T093 — 15 min:** Add per-project query budget, per-source budget and request cost ceiling; attach a small commit, test or signed receipt.
- [ ] **T094 — 15 min:** Persist query string hash, attempt timestamp, source and search outcome; attach a small commit, test or signed receipt.
- [ ] **T095 — 15 min:** Implement cooldown so identical valid attempts are not immediately repeated; attach a small commit, test or signed receipt.
- [ ] **T096 — 15 min:** Test NOT_RESEARCHED changes to attempted-no-evidence only after real permitted queries finish; attach a small commit, test or signed receipt.

### 13 — Historical and official-source adapters
Owner: **Agent 16 — project research**. Dependencies: 09,12. Planned budget: 120 min.

- [ ] **T097 — 15 min:** Implement a permitted public API adapter for one planning-reference lookup; attach a small commit, test or signed receipt.
- [ ] **T098 — 15 min:** Store planning authority identity beside planning reference to prevent collisions; attach a small commit, test or signed receipt.
- [ ] **T099 — 15 min:** Implement one Planning Inspectorate project-query adapter or permitted download reader; attach a small commit, test or signed receipt.
- [ ] **T100 — 15 min:** Implement a GOV.UK public planning/energy publication query adapter; attach a small commit, test or signed receipt.
- [ ] **T101 — 15 min:** Parse committee recommendation separately from final granted or refused consent; attach a small commit, test or signed receipt.
- [ ] **T102 — 15 min:** Preserve partial historical dates exactly as published, with precision field; attach a small commit, test or signed receipt.
- [ ] **T103 — 15 min:** Record unavailable or CAPTCHA-protected planning portals as unsupported, not empty evidence; attach a small commit, test or signed receipt.
- [ ] **T104 — 15 min:** Test historical planning event retains original event date despite new article publication; attach a small commit, test or signed receipt.

### 14 — News-first intake and shared article normalisation
Owner: **Agent 15 — acquisition + Agent 16**. Dependencies: 09,13. Planned budget: 120 min.

- [ ] **T105 — 15 min:** Reuse pipeline_headlines.py dedupe and filter interfaces without changing its schedule; attach a small commit, test or signed receipt.
- [ ] **T106 — 15 min:** Read datacentre_feed.py to reuse accepted article and site index conventions; attach a small commit, test or signed receipt.
- [ ] **T107 — 15 min:** Normalise source title, publisher, retrieval URL, canonical URL and timestamps; attach a small commit, test or signed receipt.
- [ ] **T108 — 15 min:** Separate syndicated copies from independent publisher owners in article receipts; attach a small commit, test or signed receipt.
- [ ] **T109 — 15 min:** Hash lawfully retained original response bytes or allowed metadata consistently; attach a small commit, test or signed receipt.
- [ ] **T110 — 15 min:** Merge news-first and project-first receipts using stable article keys; attach a small commit, test or signed receipt.
- [ ] **T111 — 15 min:** Test same publisher article from both pathways creates one article receipt; attach a small commit, test or signed receipt.
- [ ] **T112 — 15 min:** Test one article can maintain multiple separate project-binding proposals; attach a small commit, test or signed receipt.

### 15 — False-positive-resistant identity matching
Owner: **Agent 16 — project research**. Dependencies: 05,14. Planned budget: 120 min.

- [ ] **T113 — 15 min:** Wrap existing binder.py EXACT/STRONG/PROBABLE/CANDIDATE/UNBOUND results; attach a small commit, test or signed receipt.
- [ ] **T114 — 15 min:** Require same authority with planning-reference comparison, not reference string alone; attach a small commit, test or signed receipt.
- [ ] **T115 — 15 min:** Add county and technology contradiction veto before accepting a match; attach a small commit, test or signed receipt.
- [ ] **T116 — 15 min:** Add test for same farm name in two different English counties; attach a small commit, test or signed receipt.
- [ ] **T117 — 15 min:** Add test for multi-project developer, adjacent sites and separate project phases; attach a small commit, test or signed receipt.
- [ ] **T118 — 15 min:** Add renamed developer and ownership transfer fixtures without silently changing REPD; attach a small commit, test or signed receipt.
- [ ] **T119 — 15 min:** Write persistent rejected-binding reason so a later run does not resuggest unchanged matches; attach a small commit, test or signed receipt.
- [ ] **T120 — 15 min:** Test geography-only and developer-only signals never count as independent project verification; attach a small commit, test or signed receipt.

### 16 — Event chronology, deduplication and conflict handling
Owner: **Agent 16 — project research**. Dependencies: 13,15. Planned budget: 120 min.

- [ ] **T121 — 15 min:** Map event assertions onto existing events.py event classes without replacing REPD events; attach a small commit, test or signed receipt.
- [ ] **T122 — 15 min:** Create stable event IDs from project identity, type, reference and dated basis; attach a small commit, test or signed receipt.
- [ ] **T123 — 15 min:** Group multiple publisher articles supporting one actual planning event; attach a small commit, test or signed receipt.
- [ ] **T124 — 15 min:** Separate two events when titles match but event dates or stages differ; attach a small commit, test or signed receipt.
- [ ] **T125 — 15 min:** Record historical actual-event date separately from article publication date; attach a small commit, test or signed receipt.
- [ ] **T126 — 15 min:** Preserve contradicting sources as independent competing assertions with status; attach a small commit, test or signed receipt.
- [ ] **T127 — 15 min:** Add progression tests for approval, finance, construction, energisation as distinct events; attach a small commit, test or signed receipt.
- [ ] **T128 — 15 min:** Test syndicated articles count as one development but retain all attribution links; attach a small commit, test or signed receipt.

### 17 — SQLite evidence store and review persistence
Owner: **Agent 17 — persistence/export**. Dependencies: 05,06,16. Planned budget: 120 min.

- [ ] **T129 — 15 min:** Create schema migration for source records and acquisition cursors; attach a small commit, test or signed receipt.
- [ ] **T130 — 15 min:** Create schema migration for article receipts and canonical URL keys; attach a small commit, test or signed receipt.
- [ ] **T131 — 15 min:** Create schema migration for project identities and article-project bindings; attach a small commit, test or signed receipt.
- [ ] **T132 — 15 min:** Create schema migration for event assertions, links and conflict sets; attach a small commit, test or signed receipt.
- [ ] **T133 — 15 min:** Create schema migration for independent review decisions and revocations; attach a small commit, test or signed receipt.
- [ ] **T134 — 15 min:** Create schema migration for research attempts, cooldowns and source health; attach a small commit, test or signed receipt.
- [ ] **T135 — 15 min:** Implement transaction-based upsert plus deterministic sort/export order; attach a small commit, test or signed receipt.
- [ ] **T136 — 15 min:** Test crash/retry preserves previous review decisions and prevents duplicate rows; attach a small commit, test or signed receipt.

### 18 — Immutable evidence snapshots and GeoJSON
Owner: **Agent 17 — persistence/export**. Dependencies: 11,17. Planned budget: 120 min.

- [ ] **T137 — 15 min:** Define snapshot ID UTC format and snapshot manifest schema with input hashes; attach a small commit, test or signed receipt.
- [ ] **T138 — 15 min:** Implement deterministic per-project summary JSON and separate source receipts JSON; attach a small commit, test or signed receipt.
- [ ] **T139 — 15 min:** Implement stable CSV with all selected IDs and explicit research status; attach a small commit, test or signed receipt.
- [ ] **T140 — 15 min:** Use authenticated WGS84 project geometry from source; keep unknown geometry null; attach a small commit, test or signed receipt.
- [ ] **T141 — 15 min:** Export solar-only and BESS-only GeoJSON plus a size-limited combined GeoJSON; attach a small commit, test or signed receipt.
- [ ] **T142 — 15 min:** Assert every GeoJSON feature ID exists in an official or approved site manifest; attach a small commit, test or signed receipt.
- [ ] **T143 — 15 min:** Write immutable snapshot directory and verify all contained hashes before promotion; attach a small commit, test or signed receipt.
- [ ] **T144 — 15 min:** Update one compatible latest.json pointer atomically only after validation; attach a small commit, test or signed receipt.

### 19 — Independent data-centre project identities
Owner: **Agent 20 — data-centre lane**. Dependencies: 05,17. Planned budget: 120 min.

- [ ] **T145 — 15 min:** Pin existing datacentre_pinned.json and current dcuk site identifiers; attach a small commit, test or signed receipt.
- [ ] **T146 — 15 min:** Record source data-centre register total, coordinate reliability and rights limitations; attach a small commit, test or signed receipt.
- [ ] **T147 — 15 min:** Define DC power units: IT MW, site demand MW and connection MW separately; attach a small commit, test or signed receipt.
- [ ] **T148 — 15 min:** Write fixture for same operator at two locations and same site with multiple phases; attach a small commit, test or signed receipt.
- [ ] **T149 — 15 min:** Implement additive data-centre intake adapter using permitted source registry; attach a small commit, test or signed receipt.
- [ ] **T150 — 15 min:** Link DC articles to dcuk IDs without generating REPD reference numbers; attach a small commit, test or signed receipt.
- [ ] **T151 — 15 min:** Export independent DC project JSON with provisional/verified evidence states; attach a small commit, test or signed receipt.
- [ ] **T152 — 15 min:** Test public DC site list preserves original IDs, status and map identity; attach a small commit, test or signed receipt.

### 20 — Other technologies and cross-project relationships
Owner: **Agent 20 — other-category adapters**. Dependencies: 05,19. Planned budget: 120 min.

- [ ] **T153 — 15 min:** Implement existing-REPD onshore wind identity adapter using common receipt contract; attach a small commit, test or signed receipt.
- [ ] **T154 — 15 min:** Implement existing-REPD offshore wind identity adapter using same contract; attach a small commit, test or signed receipt.
- [ ] **T155 — 15 min:** Define grid scheme identity namespace from approved official identifiers; attach a small commit, test or signed receipt.
- [ ] **T156 — 15 min:** Implement grid project adapter for one permitted official infrastructure source; attach a small commit, test or signed receipt.
- [ ] **T157 — 15 min:** Define typed relationships: co-located, developer-linked, proximity, connection-evidenced; attach a small commit, test or signed receipt.
- [ ] **T158 — 15 min:** Ensure proximity edges cannot become electrical or commercial connection assertions; attach a small commit, test or signed receipt.
- [ ] **T159 — 15 min:** Add empty-but-valid category outputs for sources not approved in V9.25; attach a small commit, test or signed receipt.
- [ ] **T160 — 15 min:** Test all six category outputs share schemas without merging unrelated identities; attach a small commit, test or signed receipt.

### 21 — Research priority, coverage and observability
Owner: **Agent 17 — persistence/export**. Dependencies: 11,17,19,20. Planned budget: 120 min.

- [ ] **T161 — 15 min:** Reuse relevance.py additive scoring; isolate research priority from article-match confidence; attach a small commit, test or signed receipt.
- [ ] **T162 — 15 min:** Expose distinct verified impact and age/freshness dimensions; attach a small commit, test or signed receipt.
- [ ] **T163 — 15 min:** Compute selected, attempted, unresearched, provisional, verified and rejected per category; attach a small commit, test or signed receipt.
- [ ] **T164 — 15 min:** Count independent events separately from syndicated article copies; attach a small commit, test or signed receipt.
- [ ] **T165 — 15 min:** Compute source success, unchanged, failed, stale and disabled totals; attach a small commit, test or signed receipt.
- [ ] **T166 — 15 min:** Compute previous-snapshot coverage deltas without counting timeouts as attempted-negative; attach a small commit, test or signed receipt.
- [ ] **T167 — 15 min:** Generate machine-readable audit report and human-readable bounded summary; attach a small commit, test or signed receipt.
- [ ] **T168 — 15 min:** Add threshold warnings for stale operative snapshot and consecutive collection failure; attach a small commit, test or signed receipt.

### 22 — Weekly GitHub Actions refresh and branch integrity
Owner: **Agent 18 — CI/release engineer**. Dependencies: 09,17,18,21. Planned budget: 120 min.

- [ ] **T169 — 15 min:** Create pipeline-project-evidence-weekly.yml with Monday 02:00 UTC and manual dispatch; attach a small commit, test or signed receipt.
- [ ] **T170 — 15 min:** Pin checkout commit/actions/python dependencies and least-privilege token permissions; attach a small commit, test or signed receipt.
- [ ] **T171 — 15 min:** Validate source config, owner inputs, output paths and snapshot ID before fetching; attach a small commit, test or signed receipt.
- [ ] **T172 — 15 min:** Restore accepted prior SQLite state and all cursors from isolated evidence-data branch; attach a small commit, test or signed receipt.
- [ ] **T173 — 15 min:** Run deterministic selection, bounded fetch, binding, events and export pipeline; attach a small commit, test or signed receipt.
- [ ] **T174 — 15 min:** Run network-free tests and a separate bounded approved live-source probe; attach a small commit, test or signed receipt.
- [ ] **T175 — 15 min:** Commit snapshot plus pointer using non-forcing branch lease with retry on races; attach a small commit, test or signed receipt.
- [ ] **T176 — 15 min:** Upload receipt/health artifacts and guard against any V9.25, homepage or historical-file write; attach a small commit, test or signed receipt.

### 23 — V9.25 interface and mobile acceptance
Owner: **Agent 21 — frontend/QA**. Dependencies: 18,19,20,21. Planned budget: 120 min.

- [ ] **T177 — 15 min:** Inspect frozen V9.24 table actions, SOLAR 1000 view, CSV and MAP contract; attach a small commit, test or signed receipt.
- [ ] **T178 — 15 min:** Implement additive evidence data loader with schema/version compatibility and offline fallback; attach a small commit, test or signed receipt.
- [ ] **T179 — 15 min:** Create prominent solar evidence panel and explicit no-evidence/unresearched statuses; attach a small commit, test or signed receipt.
- [ ] **T180 — 15 min:** Add Data Centre Projects tab preserving current independent site IDs; attach a small commit, test or signed receipt.
- [ ] **T181 — 15 min:** Add technology, capacity, stage, event, review-confidence and research-status filters; attach a small commit, test or signed receipt.
- [ ] **T182 — 15 min:** Implement original-source history view with provisional/source-rights warnings and URL sanitisation; attach a small commit, test or signed receipt.
- [ ] **T183 — 15 min:** Implement accessible full-screen project report at 390/393 mobile and 1440 desktop widths; attach a small commit, test or signed receipt.
- [ ] **T184 — 15 min:** Run genuine UI clicks for search, sorting, CSV, source URLs, MAP and GridAtlas nearest-card caveat; attach a small commit, test or signed receipt.

### 24 — Reproducible tests, release and public readback
Owner: **Agent 13 sole integrator + Agent 19 independent reviewer**. Dependencies: all earlier phases. Planned budget: 120 min.

- [ ] **T185 — 15 min:** Run offline pytest, schema, static JS, security and all inherited release tests against exact SHA; attach a small commit, test or signed receipt.
- [ ] **T186 — 15 min:** Run bounded live-source rehearsal; record counts of actual attempts versus verified findings; attach a small commit, test or signed receipt.
- [ ] **T187 — 15 min:** Verify previous 7,775 and 3,604 official rows, numeric pilot IDs and no historical changes; attach a small commit, test or signed receipt.
- [ ] **T188 — 15 min:** Confirm no existing V9.25 tree; run new_version.py once from accepted V9.24 registry parent; attach a small commit, test or signed receipt.
- [ ] **T189 — 15 min:** Integrate scoped PRs into one release branch, resolve conflicts and create one production PR; attach a small commit, test or signed receipt.
- [ ] **T190 — 15 min:** Run real browser widths and MAP-to-GridAtlas checks; independently review known 390px failures; attach a small commit, test or signed receipt.
- [ ] **T191 — 15 min:** Merge after required checks; promote homepage-owner pointer through its established CI/CD; attach a small commit, test or signed receipt.
- [ ] **T192 — 15 min:** Verify public V9.25 served bytes, latest evidence pointer, rollback routes and signed handover; attach a small commit, test or signed receipt.

### 25 — Handover, auditing and future iterations
Owner: **Agent 13 sole integrator**. Dependencies: 24. Planned budget: 120 min.

- [ ] **T193 — 15 min:** Record exact production, homepage and data-snapshot commits and workflow run URLs; attach a small commit, test or signed receipt.
- [ ] **T194 — 15 min:** Publish full category coverage metrics without conflating provisional with verified; attach a small commit, test or signed receipt.
- [ ] **T195 — 15 min:** List all Python modules, modified workflows, tests and source licences actually exercised; attach a small commit, test or signed receipt.
- [ ] **T196 — 15 min:** Record public URL, served-byte SHA receipts, cache headers and geographic exceptions; attach a small commit, test or signed receipt.
- [ ] **T197 — 15 min:** Document known defects, disabled sources, outstanding approvals and deliberate V9.26 deferrals; attach a small commit, test or signed receipt.
- [ ] **T198 — 15 min:** Create one resumption command per remaining failing task with latest branch and head; attach a small commit, test or signed receipt.
- [ ] **T199 — 15 min:** Attach independent reviewer sign-off and actual owner acceptance status without inference; attach a small commit, test or signed receipt.
- [ ] **T200 — 15 min:** Comment final handover to V9.25 issue and cross-reference issue #41; attach a small commit, test or signed receipt.

## Four mandatory hand-off gates
**Gate A / start of coding:** issue #41 checked, release-owner reservation acknowledged, old files pinned, all V9.24 registry inconsistencies captured.  
**Gate B / before a live collector:** source hosts + licensing audited; independent acceptance contract exists; timeout/SSRF/source failure tests pass; pilot manifests frozen.  
**Gate C / before product PR:** real approved source fetch demonstrably produces an immutable snapshot with honest verified/provisional/negative counts; data branch lease proven; UI fallback stable.  
**Gate D / before public claim:** main PR required checks and browser passed, homepage transforms verified, Page served V9.25 readback digest captured, rollback V9.24 and V9.23 still available. Report external GridAtlas 390 px failures as known issues.

## Minimum week-one proof and incremental exclusions

A good first weekly snapshot may show 1,000 selected but very few researched projects. Its success is **correct source receipts, research attempts, safe match proposals, independent acceptance boundaries, repeatable builds, and honest coverage**. Do not force 100% article matches. Defer paywalled publishers, mass council scraping, unsupported wind/grid source discovery, advanced cross-asset relationship suggestions and broad historical backfills beyond the first bounded cohort. Expand only when permissions, fixtures, cost caps and accepted tests exist.

## Authoritative reading list
- https://github.com/Ventusltd/globalgrid2050
- https://github.com/Ventusltd/globalgrid2050-homepage
- https://github.com/Ventusltd/neural-link-between-agents/issues/41
- https://github.com/Ventusltd/globalgrid2050/tree/main/automation/news
- https://github.com/Ventusltd/globalgrid2050/tree/main/automation/repd
- https://github.com/Ventusltd/globalgrid2050/blob/main/automation/pipeline_release/new_version.py
- https://github.com/Ventusltd/globalgrid2050/tree/main/uk_renewables_pipeline/202611161244
- https://github.com/Ventusltd/testcode/pull/16
- https://github.com/Ventusltd/globalgrid2050/pull/123
- https://github.com/Ventusltd/globalgrid2050-homepage/pull/18
- https://github.com/Ventusltd/globalgrid2050/pull/124
- https://github.com/Ventusltd/gridatlas/issues/87

**Status of this document:** scoping/assignment only, not implementation, independent verification or release. Exact code/test/link claims must be rechecked by the executing agents.
