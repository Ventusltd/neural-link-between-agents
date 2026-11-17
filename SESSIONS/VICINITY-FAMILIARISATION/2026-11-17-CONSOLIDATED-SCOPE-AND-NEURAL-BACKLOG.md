# Vicinity Familiarisation and Neural Link — consolidated scope of works and open backlog

**Status:** planning and repository audit, 17 November 2026, 23:36 GMT. **Owner request:** provide a normal, actionable scope and record it in the Neural Link repository. **This document is a proposed execution plan, not an implementation, agent activation, merge, deployment, rights approval or release acceptance.**

**Source of coordination:** https://github.com/Ventusltd/neural-link-between-agents/issues/42  
**Existing engineering schedule:** https://github.com/Ventusltd/neural-link-between-agents/blob/02168064dfea4929e28c04d4e9c3d6c78e148b41/SESSIONS/2026-11-17-CONSOLIDATED-PIPELINE-AND-VGE-GRID-JOURNEY-ENGINEERING-SCHEDULE.md  
**Execution reconciliation:** https://github.com/Ventusltd/neural-link-between-agents/pull/55  
**Owner's original Vicinity document, two competing archival drafts:** https://github.com/Ventusltd/neural-link-between-agents/pull/56 and https://github.com/Ventusltd/neural-link-between-agents/pull/57 . Both are unmerged and neither validates the proposal's licensing or engineering claims.

## 1. Verified baseline and what remains unbuilt

- **Neural Link:** 34 open issues and 17 open PRs (16 draft, one non-draft), at the audit timestamp. Open does not mean actively executing; many are historic coordination channels. A draft document does not prove product code.
- **Pipeline News:** V9.41 is publicly published according to the command's exact release and browser receipts: https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6960671622 . This supersedes older V9.25–V9.29 planning status and older release-count checkpoints. The Pipeline release train is **separate** from GridAtlas versioning and from Vicinity Familiarisation.
- **GJ-01:** data-grid-gb PR12, OPEN, evidence ledger/crosswalk; no accepted real circuit routes: https://github.com/Ventusltd/data-grid-gb/pull/12 .
- **GJ-02:** ventus-grid-engine PR4, OPEN, bounded deterministic edge-cover graph traversal with branches/cycles/parallel edges/backtracking: https://github.com/Ventusltd/ventus-grid-engine/pull/4 .
- **GJ-03:** gridatlas PR93, OPEN, removable native MapLibre synthetic Journey preview with Start/Pause/Next/Reset/Close; four invented edges/eight moves, one invented reviewed polyline, schematic/unlocated links: https://github.com/Ventusltd/gridatlas/pull/93 .
- **GJ-04:** gridatlas PR94, OPEN, stacked on GJ-03, one official Sea Link planning-context notice; **not** a real circuit geometry source: https://github.com/Ventusltd/gridatlas/pull/94 .
- **GJ-05:** data-grid-gb PR13, OPEN, NESO SCOTEX day-ahead source scalars; **not** per-circuit local power flow, direction, surveyed line geometry or real-time electricity movement: https://github.com/Ventusltd/data-grid-gb/pull/13 .
- Previously checked exact-head CI for all five GJ PRs passed, but their heads, integration state and CI must be rechecked immediately before any merge. None was merged at this audit.
- Existing GridAtlas DC Vicinity 30/30/30 is a spatial-neighbour tool, **not electrical connectivity**. The current Grid Journey native preview is synthetic, localhost-only and not publicly promoted. No real regional grid route is approved for public tracing.

## 2. Product vision and user journeys

**Product heading in the existing GridAtlas Layers plugin: “Vicinity Familiarisation / Grid Journeys”.** This is a new heading in the *existing native MapLibre composer*, not a second map, canvas, React replacement or new backend invented without source audit.

An ordinary user should explore electricity infrastructure as they explore a London Underground diagram: choose an origin, a destination or “Explore around me”; select a radius **1–50 km**; filter 400, 275, 132, 66, 33 and 11 kV where data is lawful and evidenced; follow a continuous path; pause at substations, junctions and documented transformer transitions; inspect branches and alternative routes; understand where published evidence ends. This is **grid familiarisation**, not a claim of measured current, capacity, operational switching or a safe-dig utility locator.

**Two independent journey modes:**
1. **A-to-B route:** choose two published, review-accepted nodes. Find a path only through admissible graph edges and documented voltage-transition equipment; otherwise show “No verified connection available” and optionally a clearly different schematic/geographic corridor.
2. **Local discovery / edge-cover:** choose an origin and 1–50 km radius. Use the existing bounded GJ-02 planner to traverse available graph edges with explicit backtracking; users may step through branches like changing Underground lines. A radius limits the *view/query*, not proof that an edge crossing the radius boundary is electrically disconnected.

**Selectable neon visualisers:** standard animated route, Kuiper/Helmut Vogel sunflower (distinct voltage-coloured petals/corridors), Faraday field-inspired educational overlay, See Through transparency/asset-inspection view, Solar Design Studio solar-to-grid context, and future plug-in visualisers. These are *renderers of the same approved evidence contract*, not independent source-of-truth graphs. Inventory and pin actual estate code before reusing any named concept; the visual metaphor is not evidence of circuit connectivity or of an existing ready-to-embed module. Lightning remains optional contextual weather/event data, never proof of a grid fault.

**Always-visible legend:** “Verified connection + reviewed route geometry”; “Published topology, schematic only”; “Geographical line/corridor, electrical connection unverified”; “Unknown / withheld”; “User suggestion, unverified”. Different strokes/animations and text labels must work without colour. Animation is an **educational cursor**, not electricity, electrons, MW flow or energisation. Reduce motion / manual step must work.

## 3. Source and rights feasibility — fail closed

| Source | Potential use | Admission gate |
|---|---|---|
| Existing GridAtlas composition and owner layer datasets | Source registry, existing MapLibre layers, site coordinates, lightning, DC Vicinity, Offtakers, REPD | Audit actual layer data owners, hashes, geometry and reuse rights; proximity is not connectivity |
| Ventus Grid Engine and data-grid-gb ETYS-derived assets | Published electrical nodes, circuit/transformer relationships and bounded route planner | Pin exact source row and node identity, voltage, topology confidence; ETYS topology is not a surveyed GIS cable route |
| NESO official ETYS, planning and SCOTEX | National network planning/context, some evidenced topology and forecast scalars | Separate planned vs operating, future ratings vs available capacity, national scalar vs per-circuit measurement |
| DNO/TO open data and LTDS/network maps (UKPN, NGED, SSEN, ENWL, NPG, SPEN, National Grid and others as relevant) | Possible 132/66/33/11 kV site/line geometry or published connectivity | Per-dataset licence, current source, coordinate reference, identity crosswalk, geometry precision and public redistribution rights; do not presume all underground 11 kV circuits are available |
| OpenStreetMap/OpenInfraMap and OS OpenData | Useful lawful geographical corridor context | Source-specific attribution and ODbL/OS terms, date and coverage; mapped visual lines do not establish topology, buried geometry or switching |
| NUAR — https://www.nuar.uk/ | Potential **authorised** underground-asset lookup for permitted purposes | **No automatic public ingestion, cache, export, crowdsourced disclosure or public MapLibre display.** Obtain written eligibility, access purpose, licence, security and downstream publication authorisation before any adapter; until then public adapter remains disabled/withheld |
| Elexon / licensed operational feeds | Possible time-scoped power-system context | Verify API licence, units, timestamps and whether data actually binds to a particular reviewed circuit; no inferred flow arrows |
| User submissions | Candidate missing/invisible-circuit observations | Private/moderated queue, minimised location precision, anti-doxxing and critical-infrastructure review; never auto-promote a suggestion into a real circuit |

**Evidence is two-dimensional:** (a) *geometry evidence* (surveyed/reviewed polyline, schematic, unknown) and (b) *electrical connectivity evidence* (source-verified, disputed, unknown). A shared coordinate, crossing, nearest substation or automatic line snapping cannot convert one into the other. Explicit transformer equipment is required for a voltage change. Parallel circuits, loops, missing data and ambiguous identities must be preserved, not silently collapsed.

## 4. Proposed technical architecture and interface contract

**Read-only data pipeline:** approved source → immutable byte/hash/source-rights receipt → source-row identity and explicit graph crosswalk → validated, radius-bounded spatial index → public-safe journey manifest → native GridAtlas cartridge → renderer adapters. A restricted source never flows to the public manifest merely because an operator can see it.

**Proposed new versioned contract** (design, not existing implementation): each node and edge has a stable source-specific identifier, type, voltage_kv or null, endpoints, topology_status, geometry_status, reviewed coordinates or null, source document locator, source SHA256, retrieval and validity dates, licence/public_display flag, confidence explanation and review decision. A route response adds radius_km, origin, destination, traversal algorithm/version, ordered edge IDs, explicit backtracks, clipping boundaries, missing segments and reason codes. Preserve raw source identities and separate geographic distance (km) from electrical distance/impedance. No implicit MW, MVA or direction fields.

**Reuse real files, do not fork:**
- data-grid-gb PR12: journey/contract.py, pipelines/grid_journey_crosswalk.py and tests/test_grid_journey.py;
- ventus-grid-engine PR4: engine/edge-cover-journey.js, engine/journey-evidence.js, existing network-topology.js and its proofs;
- gridatlas PR93: tools/journey/src/bootstrap.js, controller.mjs, journey.css, and native atlas/modules/202611171525-grid-journey-preview.js;
- gridatlas PR94: independent official-context cartridge; it is documentary context, not topology;
- data-grid-gb PR13: journey/flow_context.py, which must not be misrepresented as real local flow.

**New file ownership below is proposed, not a claim these paths exist:** data-grid-gb journey/vicinity/*; ventus-grid-engine engine/vicinity-journey.js and proofs/vicinity-*; gridatlas tools/vicinity/{contracts,ui,renderers,feedback,tests}/* and one new immutable atlas generation when the integrator assembles it. Source audit must locate the actual Layers heading/registration interface before writing. Do not edit historical immutable generations, operative atlas/current.json, STATE.md, homepage or existing producer branches without the owner's release gate.

## 5. Five incremental deliverables

### VF-01 — Rights-safe real regional evidence slice

**Owner:** Data/evidence agent; independent rights reviewer. **Dependencies:** GJ-01 contract; source licence decisions. **Output:** a single geographically bounded *reviewed* region, source manifest, per-feature provenance and admissibility flags, explicit unknowns, versioned GeoJSON/graph evidence only where permitted. Prefer one high-voltage corridor with independently verifiable geometry and topology before attempting all UK 11 kV circuits.

**Acceptance:** source hashes/identity replay; coordinate/CRS validation; no source rows lost; duplicate/parallel edge preservation; unreviewed source denied; NUAR restricted-source exclusion; nearest/crossing/co-location negative tests. **Rollback:** remove only the additive manifest/cartridge reference. **Gate:** at least one accepted real geometry + connectivity pair is required for a real A-to-B demo; otherwise demo remains synthetic/schematic.

### VF-02 — Real vicinity graph planner

**Owner:** Ventus Grid Engine agent. **Dependencies:** GJ-02 and VF-01. **Output:** 1–50 km bounded discovery and A-to-B routes using source-row graph edges; explicit branches, loops, backtracking, alternative routes and voltage/transformer restrictions. Geometry is a separate render input, not proof of a graph edge.

**Acceptance:** deterministic fixtures, finite CPU/memory and route lengths, zero fabricated edges, negative tests for missing transformer, false snapping, parallel circuits, disconnected components, bad radius, malformed/oversized input and changing source hash. Preserve existing shortest-path and edge-cover exports. **Rollback:** remove additive API; old engine stays unchanged.

### VF-03 — Native Layers heading and journey controls

**Owner:** GridAtlas native UI agent. **Dependencies:** GJ-03, actual Layers plugin source audit and VF-02 interface. **Output:** “Vicinity Familiarisation / Grid Journeys” in existing Layers UI; 1–50 km slider, voltage toggles, A-to-B/local discovery modes, start/pause/step/reset, route information, evidence badges and one shared native MapLibre map.

**Acceptance:** browser test on 390/393/1440 px plus landscape; keyboard, focus, reduced motion, close/remount, layer/source namespace collisions, style reload and coexistence with Vicinity/Lightning/Offtakers; no unexpected layer or map state after removal. **Rollback:** omit new cartridge from composition; historical bytes preserved.

### VF-04 — Multiple neon Kuiper / Faraday visualisers

**Owner:** Visualiser agent with separate read-only estate inventory agent. **Dependencies:** VF-02 and VF-03. **Output:** at least two selectable neon visualisations (A-to-B and neighbourhood) on the same approved route contract; initial sunflower-style voltage palette; extensible renderer interface for Faraday, See Through and Solar Design Studio without duplicating grid truth.

**Acceptance:** source pin and licence check for reused code/assets; voltage-specific styles; no line drawn where geometry unknown; schematic distinct from reviewed; no inferred flow direction; GPU/CPU/animation budget; reduced-motion manual step and screen-reader labels. **Rollback:** disable an individual renderer without removing the core journey feature.

### VF-05 — Feedback, integration, independent QA and controlled preview

**Owner:** Feedback agent; independent QA agent; sole integrator. **Dependencies:** VF-01–04. **Output:** optional “Suggest missing connection” feedback, moderation/triage, source-request queue and a controlled GridAtlas preview. Feedback must not publicly disclose sensitive underground routes or auto-edit canonical topology.

**Acceptance:** abuse/privacy checks, provenance and source-rights gate, stale/changed manifest rejection, mobile/browser regressions, no new map canvas, real route receipt where one exists, full release/rollback proof. **Rollback:** remove the additive cartridge and public manifest; retain safe audit receipts. **Release:** only the GridAtlas release owner can promote after independent review and actual acceptance. A localhost prototype is not a public release.

## 6. Exactly ten executable Codex steps — one to eight agents

Assign eight **roles**, not eight presumed running sessions. Each must ACK the command in Neural Link #42, use a separate worktree/branch, identify exclusive paths and submit a reviewable PR. A one-agent implementation is sequential; with eight genuinely active agents, steps 2–7 can overlap subject to contracts.

| Step | Agent | Work and handoff | Evidence / completion |
|---|---|---|---|
| **1** | A8 — coordinator/integrator | Freeze current source SHAs, PR heads, owners, scope, conflicts and GridAtlas release policy; reserve exclusive integration branch; record real 1–50 km requirements | Signed command ACK, dependency graph and exact baseline |
| **2** | A1 — evidence/data | Audit GridAtlas layer/source tables, ETYS, regional DNO/TO candidates, actual geometry and topology; produce reviewed regional source manifest | Reproducible hashes, licences, coverage/unknown matrix, VF-01 tests |
| **3** | A5 — estate/rights | Inventory actual Kuiper, Helmut Vogel, Faraday, See Through and Solar Design Studio code; determine NUAR eligibility and forbid unauthorised public export | Reuse map and per-source rights decision; no product branch edits |
| **4** | A2 — graph/engine | Extend pinned GJ-02 graph planner for radius and A-to-B; refuse inferred joins and voltage changes without evidence | Deterministic route/negative/performance tests, isolated engine PR |
| **5** | A3 — GridAtlas UI | Audit existing Layers registration; add heading and controls on one native MapLibre composer, with withheld-state fallback | Native browser, accessibility and lifecycle tests, isolated UI PR |
| **6** | A4 — renderers | Build separate neon route and local-exploration adapters, sunflower voltage palette, renderer slots for future concepts | Source-pinned, reduced-motion and no-phantom-line tests, isolated renderer PR |
| **7** | A6 — feedback | Implement moderation-ready unverified-circuit suggestion contract, privacy and restricted-asset protection | Abuse/validation tests; no automatic publication or topology changes |
| **8** | A8 — integration | Integrate reviewed commits in dependency order, preserving GJ-01→GJ-02→GJ-03→GJ-04 and optional GJ-05 distinctions; resolve same-repo branch collisions in one integration branch | Exact SHA composition, reproducible build, no live pointer writes |
| **9** | A7 — independent QA | Run real Chromium mobile/desktop, engine/property tests, data/rights tests, network failure and rollback checks; flag missing physical device tests | Independent PASS/FAIL/UNVERIFIED receipt at exact integrated head |
| **10** | A8 — release decision | Demonstrate synthetic + any genuinely accepted real region, publish preview only after permitted gates; report what remains withheld and whether public promotion is authorised | Owner acceptance or explicit HOLD; version, URLs, served bytes and rollback only if actually released |

**One-night realistic outcome:** 6–10 hours with eight truly active, non-conflicting agents may produce a well-tested *new preview*, real source-admissibility inventory, UI heading, graph adapter, neon modes and feedback prototype. A publicly verified 11 kV underground network, NUAR public data reuse, all-voltage nationwide connectivity, physical-device QA and production release are **not** credible overnight guarantees. A real trace is permitted only if an independent regional source review clears identity, geometry, connectivity and licence. With one agent, schedule sequentially across multiple days.

## 7. All 34 currently open Neural Link issues — action/status classification

**Snapshot:** 17 November 2026, 23:36 GMT. “Open” is GitHub state; “delivered”, “historical” and “requires reconciliation” are *work-status assessments*, not GitHub closure claims. Check newest comments before taking action.

### A. Current command, release and specialist work (14 issues)

| Issue | Scope | Remaining action |
|---|---|---|
| [#42](https://github.com/Ventusltd/neural-link-between-agents/issues/42) | Agent 13 / command / 200-task V9.25 board; latest V9.41 receipts and owner Vicinity document handoffs | Keep canonical command; reconcile newer release state and assign Vicinity roles without displacing publisher |
| [#45](https://github.com/Ventusltd/neural-link-between-agents/issues/45) | Five meaningful Pipeline releases, maximum 20 | Reconcile target/checkboxes against V9.41 actual public receipts; do not double-count GJ or stage builds |
| [#43](https://github.com/Ventusltd/neural-link-between-agents/issues/43) | Covenant policy/commitment evidence | Tested ledger handoff exists; check actual integration, source gaps and measured-delivery limits before marking released |
| [#44](https://github.com/Ventusltd/neural-link-between-agents/issues/44) | Grid Agent, owner layers/engine/podcast/2050 catalogue | Tested bounded catalogue exists (32 pinned inputs, 24 tests); determine downstream integration and unresolved sources |
| [#46](https://github.com/Ventusltd/neural-link-between-agents/issues/46) | Integration Advisor | First recipe delivered and PR48 merged; confirm consumer contract integration and close/retask only after ACK |
| [#49](https://github.com/Ventusltd/neural-link-between-agents/issues/49) | Neural Memories | PR50 merged; refresh release/agent ledger to current V9.41 and current GJ heads, then mark prior handoff done |
| [#51](https://github.com/Ventusltd/neural-link-between-agents/issues/51) | Furnace offline CuPy review | PR52 merged; confirm hourly schedule and four Astra review evidence; no GPU product adoption implied |
| [#40](https://github.com/Ventusltd/neural-link-between-agents/issues/40) | Agent 10 Machine Read Notes/TestCode | Verify final TestCode PR/CI and any production consumer separately; no TestCode experiment equals deployment |
| [#41](https://github.com/Ventusltd/neural-link-between-agents/issues/41) | Agent 11 REPD solar-1000 acquisition | Reconcile actual first-1000 selection, candidate matching, coverage/rights and TestCode handoff; no invented verified leads |
| [#34](https://github.com/Ventusltd/neural-link-between-agents/issues/34) | Agent 6 news algorithms | Review research PR33 against current production, transfer useful tests, do not merge stale producer assumptions |
| [#37](https://github.com/Ventusltd/neural-link-between-agents/issues/37) | Spiders–Kuiper–Stars–CVAA evidence links | Research PR36 exists; actual read-only bridge and 14 proposed negative tests remain unimplemented/unverified |
| [#30](https://github.com/Ventusltd/neural-link-between-agents/issues/30) | Older P2 release train | Reconcile historical release holds and receipts against V9.41; archive superseded mandates |
| [#32](https://github.com/Ventusltd/neural-link-between-agents/issues/32) | Older ten-iteration overnight ledger | Replace stale target/status with actual release receipts; close/retain as history only after review |
| [#19](https://github.com/Ventusltd/neural-link-between-agents/issues/19) | Phase 2 news relevance and verified DC integration | Check live DC provenance, rights and project identity; transfer only unfulfilled work to current release queue |

### B. Earlier Phase 2, REPD and release coordination (10 issues)

| Issue | Scope | Remaining action |
|---|---|---|
| [#24](https://github.com/Ventusltd/neural-link-between-agents/issues/24) | Earlier ChatGPT-only Phase 2 controller | Preserve handoffs; supersede outdated publication HOLD after checking actual V9.41 evidence |
| [#21](https://github.com/Ventusltd/neural-link-between-agents/issues/21) | V9.20 publication swarm | Confirm historical release and rollback receipt, then close as superseded |
| [#20](https://github.com/Ventusltd/neural-link-between-agents/issues/20) | REPD + data-centre convergence | Check what shipped, outstanding rights/joins and whether current DC stream covers it |
| [#12](https://github.com/Ventusltd/neural-link-between-agents/issues/12) | October REPD Q3 intake | Verify final original source hash, preservation and release history; archive when complete |
| [#13](https://github.com/Ventusltd/neural-link-between-agents/issues/13) | Agent B REPD source/regression QA | Verify recorded QA; close or reassign only a specific remaining defect |
| [#14](https://github.com/Ventusltd/neural-link-between-agents/issues/14) | Agent C genuine Q2 provenance | Check Q2 recovery evidence and source rights; do not treat prepared assignment as executed |
| [#15](https://github.com/Ventusltd/neural-link-between-agents/issues/15) | Agent D Q3 Pipeline integration | Check release outcome and preserved Q3 version |
| [#16](https://github.com/Ventusltd/neural-link-between-agents/issues/16) | Agent E GridAtlas Q3 numerical/map QA | Verify actual QA receipts; transfer unresolved map tests to current owner |
| [#17](https://github.com/Ventusltd/neural-link-between-agents/issues/17) | Agent F independent release gate/rollback | Verify review and rollback proof, not merely task creation |
| [#1](https://github.com/Ventusltd/neural-link-between-agents/issues/1) | Original GridAtlas #73 Agent A/B mailbox | Preserve audit history; reconcile old PR75 and current map baseline before closure |

### C. Historical Kuiper, estate, agent onboarding (10 issues)

| Issue | Scope | Remaining action |
|---|---|---|
| [#2](https://github.com/Ventusltd/neural-link-between-agents/issues/2) | Agent C onboarding | Await actual invocation/ACK or close obsolete mailbox |
| [#3](https://github.com/Ventusltd/neural-link-between-agents/issues/3) | Agent D onboarding | Same |
| [#4](https://github.com/Ventusltd/neural-link-between-agents/issues/4) | Agent E onboarding | Same |
| [#5](https://github.com/Ventusltd/neural-link-between-agents/issues/5) | Agent F Claude continuity | Retain historical context; no assumption of running Claude agent |
| [#6](https://github.com/Ventusltd/neural-link-between-agents/issues/6) | Kuiper estate survey / data-centre context | Review dated evidence for reusable concepts; do not count as current implementation |
| [#7](https://github.com/Ventusltd/neural-link-between-agents/issues/7) | 227→226 DC baseline fix plan | Verify resolved historical source counts/hashes; close or identify exact remaining defect |
| [#8](https://github.com/Ventusltd/neural-link-between-agents/issues/8) | v9.188 release QA | Archive after verifying historical acceptance |
| [#9](https://github.com/Ventusltd/neural-link-between-agents/issues/9) | Kuiper Edition 5 Android/See Through | Inventory actual mobile fixes and See Through button; reuse only accepted components |
| [#10](https://github.com/Ventusltd/neural-link-between-agents/issues/10) | Ten-step Kuiper/See Through/Stars/Spiders roadmap | Crosswalk actual components to new VF-04 renderer slots; avoid duplicate roadmaps |
| [#11](https://github.com/Ventusltd/neural-link-between-agents/issues/11) | Twelve-agent neural protocol/continuity | Check actual protocol artefacts; historical study does not imply active agents |

**Count reconciliation:** 14 + 10 + 10 = **34** open issues. Do not bulk-close without confirming last comments and dependent code.

## 8. All 17 open Neural Link PRs — disposition queue

The following are all **OPEN**, not merged, at the snapshot. Sixteen are **draft**; #23 is non-draft. Their product or documentation claims are not automatically accepted.

| PR | Contents | Recommended next action |
|---|---|---|
| [#57](https://github.com/Ventusltd/neural-link-between-agents/pull/57) | Draft owner Vicinity DOCX archive + searchable text + README link | Independently review bytes, privacy and links; choose canonical archive; avoid duplicate #56 |
| [#56](https://github.com/Ventusltd/neural-link-between-agents/pull/56) | Draft near-duplicate owner Vicinity DOCX archive | Compare hashes and text to #57; retain one canonical version, preserve provenance; do not merge both blindly |
| [#55](https://github.com/Ventusltd/neural-link-between-agents/pull/55) | Draft five Pipeline/five Grid Journey reconciliation | Review against latest V9.41 and GJ heads; keep distinct PN/GJ IDs |
| [#54](https://github.com/Ventusltd/neural-link-between-agents/pull/54) | Draft agent activation and ACK guide | Review against current AGENTS/PROTOCOL, then merge or close superseded guide |
| [#39](https://github.com/Ventusltd/neural-link-between-agents/pull/39) | Draft Agent8→9 iPhone/TestCode brief | Check whether Agent9 implemented it; archive or close stale instruction |
| [#38](https://github.com/Ventusltd/neural-link-between-agents/pull/38) | Draft Agent8 continuity audit | Verify historical head, then archive or close; not a live release receipt |
| [#36](https://github.com/Ventusltd/neural-link-between-agents/pull/36) | Draft Spiders/CVAA/Kuiper/Stars evidence handoff | Review/merge research if useful; separate actual browser bridge work |
| [#35](https://github.com/Ventusltd/neural-link-between-agents/pull/35) | Draft pre-Agent7 historical research | Preserve as historical; review whether superseded |
| [#33](https://github.com/Ventusltd/neural-link-between-agents/pull/33) | Draft news-algorithm research | Extract valid tests; recheck assumptions vs current production |
| [#31](https://github.com/Ventusltd/neural-link-between-agents/pull/31) | Draft Agent5 recovery state | Archive with dated/stale label or close if redundant |
| [#29](https://github.com/Ventusltd/neural-link-between-agents/pull/29) | Draft public protocol/README refresh | Compare current main, avoid overwriting newer README/Furnace links |
| [#28](https://github.com/Ventusltd/neural-link-between-agents/pull/28) | Draft Phase 2 veto watch | Retain historical veto evidence; not current release gate |
| [#27](https://github.com/Ventusltd/neural-link-between-agents/pull/27) | Draft Agent3 editorial scope request | Check ACK and work delivered; close stale scope proposal |
| [#26](https://github.com/Ventusltd/neural-link-between-agents/pull/26) | Draft Agent4 editorial challenge | Transfer falsification fixtures where still relevant; review/close |
| [#25](https://github.com/Ventusltd/neural-link-between-agents/pull/25) | Draft Phase 2 controller checkpoint | Preserve dated handoff; superseded by #42/current receipts |
| [#23](https://github.com/Ventusltd/neural-link-between-agents/pull/23) | Non-draft 14 Nov news sweep/audit | Verify seven REPD conflicts and unperformed planning-register checks before treating sweep as completed |
| [#18](https://github.com/Ventusltd/neural-link-between-agents/pull/18) | Draft agent activity/audit index | Compare to current README/RESEARCH and #54; avoid competing activity registries |

**Count reconciliation:** 17 open PRs. **Do not merge** stale docs, conflicting README updates or duplicate archive PRs without an explicit diff and review.

## 9. Priority and critical path across both programmes

**P0 — truthful baseline:** read newest #42 comments; reconcile Pipeline V9.41, current GridAtlas operative generation, all five GJ heads, the duplicated Vicinity archive PRs and the 34/17 open ledger. The main Neural Link AGENTS.md contains an older V9.22→V9.23 statement; treat it as stale release context and check CURRENT_PIPELINE_NEWS_VERSION.md plus actual production receipts. Do not silently rewrite release policy from this plan.

**P1 — regional real-grid evidence:** independent topology/geometry/rights acceptance. This is the critical path for *real* journeys. NUAR remains disabled absent explicit lawful permission. A topological ETYS edge without reviewed geometry gets a schematic, never an invented buried polyline.

**P2 — bounded planner + native Layers integration:** extend the tested GJ-02 engine and GJ-03 MapLibre preview; keep existing Offtakers, Vicinity, Lightning and all other layers operational. Maintain exact-source pinning and reversible cartridge registration.

**P3 — differentiated visualisers and feedback:** Kuiper sunflower, Faraday, See Through and Solar Design Studio adapters share one approved evidence model. Feedback enters a moderated unknown queue, never source truth.

**P4 — QA and controlled promotion:** independent data, security, browser and mobile acceptance; release owner chooses HOLD or publication. The new VF programme does not inherit Pipeline V9.xx release numbers or a blanket permission to change the live Atlas.

## 10. Release, threat and acceptance checklist

- **Rights/security:** public-safe input only; NUAR/restricted DNO coordinates withheld; no credentials, sensitive cable locations, private feedback or personal records in public Neural Link or browser assets.
- **Evidence:** every drawn real edge must trace to a reviewed source row and explicit licence; every route must identify connectivity status; null means unknown, not zero.
- **Anti-fabrication:** crossings, nearby substations, identical coordinates, shared name, user feedback, voltage similarity and spatial snapping never prove electrical connections; no invented transformer.
- **Electrical honesty:** cursor is educational; no flow direction, live MW, capacity, energisation, fault or weather-causation inference without separate suitable evidence.
- **Performance:** bounded radius, edge/vertex/move counts, memory/time, source download bytes, MapLibre layer namespace, no second canvas, cancellation on close/style reload, stable deterministic output.
- **Accessibility:** keyboard and touch, 44 px targets, focus return, text/line-pattern legend, reduced motion, manual step, landscape, screen-reader announcement; physical Android/iOS/Safari/VoiceOver remain pending until actually tested.
- **CI:** source hash/rights tests; property and adversarial graph tests; deterministic build; existing composer/layers unchanged; 390/393/1440 + landscape Chromium; network failures recorded; independent reviewer and exact-head CI.
- **Release:** only sole owner/integrator changes a new immutable Atlas generation and operative pointer after owner acceptance; retain old generation, record served SHA, verify live browser and rehearse rollback. No live publication is requested or executed by this document.

## 11. Decisions needed before real-route implementation

1. **First region:** select one permitted UK transmission corridor/area for a genuinely reviewed real route; do not promise all UK 11 kV lines.
2. **Evidence threshold:** require both real electrical connectivity and licensed reviewed geometry for a moving cursor; allow explicit schematic/geographical-only alternatives.
3. **NUAR:** nominate an authorised legal/data owner to determine whether any intended use and downstream display is permitted. Default remains no public NUAR content.
4. **Visual identity:** agree initial two journey modes and one sunflower renderer; Faraday/See Through/Solar Design Studio can follow via the same interface once actual code and rights are audited.
5. **Ownership:** confirm eight agent roles/branch reservations and one sole GridAtlas integrator; GitHub comments do not wake inactive agents.
6. **Release target:** preview-only overnight unless independent evidence, rights, mobile QA and owner acceptance support a later public release.

**Next command:** assign VF-01 evidence and VF-03 Layers interface source audits first; start VF-02 graph contract in parallel; hold any real-route animation until the evidence gate passes. Keep #42 as the canonical command mailbox and review PR56/57 before merging archival material.

## 12. Post-audit PR delta (17 November 2026, 23:45 GMT)

The 34-open-issue / 17-open-PR inventory above is a deliberately pinned **23:36 GMT snapshot**, not a continuously updated live count. A fresh GitHub PR read at approximately 23:45 GMT found **19 open PRs**: the original 17 plus the following two. The 34 issue rows and 17 historical PR rows above are unchanged.

| New PR | Scope | Next action |
|---|---|---|
| [#58](https://github.com/Ventusltd/neural-link-between-agents/pull/58) | Non-draft agent coordination efficiency, STATUS.json, Python validator, read-only workflow and removal of cron triggers from six expired workflows while retaining manual dispatch | Independently review workflow schedule removals and validator receipts; do not claim measured CI runtime savings or merge without reviewer |
| [#59](https://github.com/Ventusltd/neural-link-between-agents/pull/59) | Draft **this** additive Vicinity Familiarisation + Neural Link consolidated work order | Independently review current issue/PR state, source/legal caveats, owner instructions and branch diff; merge only after approval |

The newly observed #58 was created at 23:38 GMT after the original inventory cutoff. No issue or PR was closed or merged by preparing this report.
