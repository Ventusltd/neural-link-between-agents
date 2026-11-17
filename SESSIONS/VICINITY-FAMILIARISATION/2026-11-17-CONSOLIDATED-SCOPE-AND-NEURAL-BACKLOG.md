# Vicinity Familiarisation: real-grid tracing + consolidated Neural Link outstanding scope
**Owner-requested actionable work order | Snapshot 17 November 2026, approximately 23:40 UTC | PLANNING / NO PRODUCT RELEASE**

## 0. Authority, status and guardrails

This is a **new, separate** owner-requested synthesis. It does not replace the prior [17 Nov consolidated Pipeline/GJ engineering schedule](https://github.com/Ventusltd/neural-link-between-agents/blob/02168064dfea4929e28c04d4e9c3d6c78e148b41/SESSIONS/2026-11-17-CONSOLIDATED-PIPELINE-AND-VGE-GRID-JOURNEY-ENGINEERING-SCHEDULE.md), [AGENTS.md](https://github.com/Ventusltd/neural-link-between-agents/blob/main/AGENTS.md), [PROTOCOL.md](https://github.com/Ventusltd/neural-link-between-agents/blob/main/PROTOCOL.md), or the unmerged owner document archives [#56](https://github.com/Ventusltd/neural-link-between-agents/pull/56) and [#57](https://github.com/Ventusltd/neural-link-between-agents/pull/57). Treat the owner DOCX as a proposal, not validated source/licence evidence. Repository issues are asynchronous mailboxes: a role label, comment or PR is not proof that a worker is running. An open issue is not necessarily an unimplemented feature.

**Verified GitHub snapshot:** 34 open issues and 18 open PRs in Neural Link (16 draft, two ready: #23/#58); Neural Link main `02168064dfea4929e28c04d4e9c3d6c78e148b41`. Latest [#42 acceptance](https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6960671622) says Pipeline News **V9.41 / 202611171940 is publicly published**, exact CI and root/browser gates passed, with explicit headless-paint/early-hydration qualifications. Do not use older V9.22 language in [CURRENT_PIPELINE_NEWS_VERSION.md](https://github.com/Ventusltd/neural-link-between-agents/blob/main/CURRENT_PIPELINE_NEWS_VERSION.md) as the current live fact; update that policy via a separate reviewed coordination change. No Grid Journey PR is merged into the live GridAtlas generation as of this snapshot.

## 1. Product definition — 'Vicinity Familiarisation'

A non-expert opens **the existing native MapLibre GridAtlas**, expands a new **Layers → Vicinity Familiarisation / Grid Journeys** heading, selects a substation, grid asset, project or point, sets a **1–50 km geographic radius**, filters voltage classes (400, 275, 132, 66, 33, 11 kV as evidenced), and explores a London Underground-style network map. Users may select a destination, ask for a documented shortest journey, or run a bounded branch-cover 'neon train' to learn what is known locally. Show route steps, voltage changes and explicit transformer transfers. Keep current Grid Engine, 30/30/30 vicinity, lightning, substation intelligence, Offtakers and other cartridges intact.

Offer **two independently selectable neon journeys**: (a) *mapped corridor trace* on source-supported permitted GIS geometry; (b) *electrical network journey* only on independently identified published graph edges. They may overlap, but must never be silently equated. If a published ETYS circuit lacks GIS bends, show a **dotted schematic 'not surveyed route'** or text-only stop, not a fabricated underground line. If a mapped line lacks an approved circuit identity, it remains a **geographic corridor only**, not a connected feeder. Crossings, nearest neighbours and co-located buses are not electrical joints. An explicit published transformer edge is required for voltage transition. Preserve parallel circuit multiplicity, cycles and deterministic backtracking.

**Visualiser family** (reuse code only after exact source audit):
- **Kuiper / Vogel sunflower**: radial petals for eligible neighbouring nodes and branch options, source-coded by voltage; no claim of physical electron flow.
- **Faraday**: separate electric-field or design-study concepts where source-backed; label simulations as simulations, not operational telemetry.
- **See Through**: optional transparent/inspection view of the selected evidence, mapped/schematic/unknown layers, including mobile controls.
- **Solar Design Studio**: designed/proposed solar feeder overlays clearly separated from existing infrastructure.
- **Lightning**: optional time-stamped weather context; a satellite optical flash is not proof of a ground strike, circuit trip or fault.
- Future plugins: named 400/275/132/66/33/11 kV traces, equipment transitions, approved project connection context and user feedback.

Each edge/petal/trace carries a user-visible status: `REVIEWED_TOPOLOGY_AND_GEOMETRY`, `PUBLISHED_TOPOLOGY_SCHEMATIC`, `MAPPED_CORRIDOR_ONLY`, `NEARBY_NOT_CONNECTED`, `PROPOSED_DESIGN`, `WITHHELD_OR_UNKNOWN`. Display source name, vintage, source row/asset ID, rights, confidence/reviewer and precision; missing or restricted data yields no public route.

## 2. Existing tested building blocks (all five unmerged)

| ID | Repo / PR | Proven code or evidence | Remaining gate |
|---|---|---|---|
| GJ-01 | [data-grid-gb #12](https://github.com/Ventusltd/data-grid-gb/pull/12) | Byte-pinned evidence ledger and offline crosswalk contract; tested, no approved real circuits | Independent circuit identity, GIS provenance, rights, approved real pilot |
| GJ-02 | [ventus-grid-engine #4](https://github.com/Ventusltd/ventus-grid-engine/pull/4) | Deterministic bounded edge-cover traversal with branches, cycles, parallel edges, backtracking and strict transformer/voltage rules | Integrate radius/destination routing without altering existing BFS shortest-path API |
| GJ-03 | [gridatlas #93](https://github.com/Ventusltd/gridatlas/pull/93) | Removable native MapLibre Journey cartridge, controls and synthetic 4-edge/8-move demonstration; browser tests | New Layers heading, user-selectable 1–50 km radius and real lawful source, physical device QA |
| GJ-04 | [gridatlas #94](https://github.com/Ventusltd/gridatlas/pull/94) | Stacked official Sea Link planning context, no real circuit route | Separate planning context from present-day topology and real geometry |
| GJ-05 | [data-grid-gb #13](https://github.com/Ventusltd/data-grid-gb/pull/13) | NESO SCOTEX day-ahead aggregate scalars; per-circuit flow and direction deliberately null | Never animate this as local measured MW; only optional dated context |

GridAtlas main remained on V9.191 native-map restoration when checked; the preview PRs are not public promotions. Existing GridAtlas 30/30/30 vicinity is spatial screening, **not** electrical connection. NESO ETYS model has published topology, **not** complete GIS cable bends or a universal 11 kV dataset. Verify current PR heads/CI afresh before integration.

## 3. Data, licensing and NUAR gates

| Candidate source | Useful for | Hard limitation / action |
|---|---|---|
| NESO ETYS and Ventus `data-grid-gb` ETYS-derived graph | Published transmission nodes, circuit rows, transformers and planned changes | No assumption of exact physical route, live switching, feeder headroom or real-time direction; distinguish future works |
| Licensed DNO/TO open-data and LTDS/DSO releases (UKPN, NGED, ENWL, SSEN, SPEN, NPG) | Region-specific substations, published network maps and declared connections | Review each file's date, licence, geometry, voltage, asset IDs, redactions and topology before public display |
| OSM / OpenInfraMap / OS data where individually permitted | Mapped overhead lines, visible assets and cartographic corridors | Mapped geometry does not prove electrically connected circuits; respect attribution, completeness and precision |
| [NUAR](https://www.nuar.uk/) | Potential authorised underground-asset discovery and safe-dig context | **Not an assumed open public route feed.** Determine lawful eligibility, contractual terms, API/export rights, security and public-redistribution permission with the operator; default **NO INGEST / NO PUBLIC DISPLAY** of restricted buried assets. A permission-gated adapter may be designed without importing any asset data |
| Public user suggestions | Leads for verification and data-quality corrections | Never treat a crowd submission, guessed cable line or screenshot as proof of electrical topology; privacy/security moderation first |

Minimum data contract for a public route: `edge_uid, source_dataset, source_url, source_version, source_row_locator, source_sha256, licence, publish_allowed, reviewed_by, review_at, voltage_kv, from_bus_id, to_bus_id, circuit_identity, transformer_identity_if_cross_voltage, geometry_status, geometry_crs, geometry_precision, valid_as_of, retrieval_at, topology_status, confidence, disclosure_status`. Distinguish published source facts, deterministic derived facts, expert review and proposed/user-contributed facts. An edge may be navigable electrically without public geometry; a GIS feature may be drawable without being electrically navigable.

## 4. Five independent overnight increments (VF namespace, NOT Pipeline V9.xx)

| Increment | Product result | Proposed exclusive paths / producer | Tests, gate and rollback |
|---|---|---|---|
| **VF-01 Evidence pilot** | One deliberately small lawful regional pilot: reviewed mapped lines, stations, identities and explicit unknowns; 400/275/132 kV first if evidence supports, no fabricated 11/33 kV | Agent 1+2: `data-grid-gb/pipelines/vicinity/`, `data-grid-gb/derived/vicinity-pilot.v1.json` (new proposed paths) | Hash, CRS, licence, duplicates, crossing-not-junction, no nearest-neighbour connection, source-row and withholding fixtures. **HOLD** absent approved real pilot |
| **VF-02 Routing service** | Radius-limited (1–50 km) deterministic shortest and branch-cover journeys, edge identity, voltage/transformer transitions, bounded search and no-route explanations | Agent 3: `ventus-grid-engine/engine/vicinity-journey.js`, dedicated tests (proposed); consume GJ-02, do not rewrite BFS | 1/50 boundaries, cycles, parallel edges, unknown voltage, disconnected islands, explicit transfer, max work/memory, repeatability and source-stable IDs |
| **VF-03 Native Layers UX** | New GridAtlas Layers heading, voltage toggles, origin/destination/radius, two neon journey types, synthetic-safe fallback and readable legend | Agent 4: `gridatlas/tools/vicinity/` plus minimal native composer hook in owned preview generation; depends GJ-03/04 | Native MapLibre only, source/layer ID collision, reversible teardown, no other cartridge regressions, 390/393/1440 + landscape, reduced-motion and keyboard; **no live pointer** |
| **VF-04 Kuiper/Faraday visualisers** | Pluggable sunflower petals, multi-colour route traces, optional See Through, Solar Design Studio and lightning context, all separated by evidence mode | Agent 5: isolated visualiser adapters under `gridatlas/tools/vicinity/visualisers/`; source-code audit of `kuiper-belt`, `globalgrid2050/kuiper-grid`, See Through and Solar Design Studio | Same source graph, no invented network connections, motion controls, colour-independent legend, performance budgets and source/attribution tests |
| **VF-05 Feedback + GlobalGrid2050 integration** | Moderated 'missing circuit' feedback, safe public evidence metadata export to GlobalGrid2050, NUAR access decision document and staging acceptance | Agent 6+7+8: new feedback/adapter/test paths, separate `globalgrid2050` read-only consumer, independent security/browser reviewer | No precise restricted asset leakage, spam/rate limit/privacy, reviewed-only promotion, rights denial, public URL/CI/rollback gates. NUAR **adapter disabled** until written permissions |

**Overnight realism:** a useful **isolated synthetic demonstration, map-native controls, legal mapped-corridor pilot where permitted data already exists, deterministic routing tests and a preview PR** may be achievable. A verified all-voltage real London 1–50 km electrical network, underground 11 kV cable bends, full NUAR data access, real-time MW arrows, owner acceptance and physical handset QA are **not** promised by morning. Never publish a claimed 'real electrical route' unless VF-01 has an approved, identity-matched graph-and-geometry edge.

## 5. Exactly ten executable steps for one to eight Codex agents

One Codex agent can run sequentially. Up to eight active agents can use separate branches/worktrees, with a **single integrator** and no concurrent writes to release pointers. Assignments below are roles to invoke and ACK, **not evidence that eight agents are running**.

| Step | Agent | Action, handoff and exit |
|---|---|---|
| **1** | Root/integrator | Read AGENTS/PROTOCOL and current #42, freeze repo heads and existing live GridAtlas pointer, inspect Layers plugin/GJ/Kuiper/See Through/Faraday code, reserve exclusive branches, record current source/rights gaps. Exit: signed inventory and branch/path ownership. |
| **2** | Agent 1 — source/rights | Inventory real ETYS/DNO/OSM/OS candidate source URLs, data licences, geometry, update clocks and public rights. Determine NUAR legal/API eligibility separately. Exit: allow/withhold source ledger, no restricted asset download. |
| **3** | Agent 2 — topology/crosswalk | Build smallest independently reviewable pilot identity crosswalk; do not infer joins from proximity, crossings or voltage co-location. Exit: VF-01 fixtures and explicit zero-approved-edge result if evidence fails. |
| **4** | Agent 3 — engine | Implement VF-02 radius and route API against pinned VF-01 schema and GJ-02 planner; preserve source-row multiplicity and explicit transformer transitions. Exit: deterministic negative and performance tests. |
| **5** | Agent 4 — GridAtlas UX | Implement VF-03 native Layers heading and 1–50 km controls using synthetic fixture first; bind approved pilot only if VF-01 passes. Exit: removable MapLibre preview, browser tests, no live pointer. |
| **6** | Agent 5 — visualisers | Audit and adapt existing Kuiper/Faraday/See Through/Solar Studio concepts as opt-in renderer plugins. Exit: distinct sunflower/line modes and clear evidence labels with reduced-motion fallback. |
| **7** | Agent 6 — feedback/GlobalGrid | Implement VF-05 moderation schema and a permission-gated public-safe GlobalGrid2050 adapter; NUAR remains disabled. Exit: privacy/rights and provenance fixtures. |
| **8** | Agent 7 — independent QA | Adversarially test phantom joins, crossings, false 11 kV geometry, unauthorised data, zero results, 1/50 km, loops, performance, native map restoration and mobile. Exit: exact-head FAIL/PASS report and source receipts. |
| **9** | Agent 8 — integration reviewer | Verify disjoint PRs, current head dependencies, licences, rollback, screenshots and acceptance; reconcile open Neural Link backlog and duplicate #56/#57; recommend smallest safe merge sequence. Exit: release candidate review, no self-approval. |
| **10** | Root/integrator | Merge only accepted dependencies in order, stage native GridAtlas preview, obtain independent browser/physical QA and owner release decision. Update Neural #42 with exact commit/CI/rights and rollback; only then consider a new GridAtlas generation. |

**Timebox:** in an eight-hour night, budget roughly 1h inventory/rights, 2h data+engine contracts in parallel, 2h native UI/visualisers/feedback in parallel, 2h adversarial QA/integration, 1h staging and handoff. Real data and permissions are critical-path blockers; extend schedule rather than bypass them. Avoid competing producers writing `atlas/current.json`, `STATE.md`, homepage pins, immutable Pipeline directories or another agent's branch.

## 6. Neural Link open-issue inventory — all 34

Snapshot of GitHub **open issue** state; remaining action is a recommendation to verify, not a claim of currently executing code.

### Current command and release

| Issue | Remit | Remaining action / classification |
|---|---|---|
| [#42](https://github.com/Ventusltd/neural-link-between-agents/issues/42) | COMMAND / current coordination | Read latest owner instruction, producer receipts, Grid Journey dependencies and actual release status; one integrator, no automatic agent wake. |
| [#45](https://github.com/Ventusltd/neural-link-between-agents/issues/45) | Pipeline News meaningful release counter | Reconcile target with verified V9.41 and later releases; do not count draft/test releases or invent version targets. |
| [#30](https://github.com/Ventusltd/neural-link-between-agents/issues/30) | Older Phase-2 publishing train | Reconcile with #42/#45; preserve source/rights/CI veto receipts, then close or archive superseded instructions. |
| [#32](https://github.com/Ventusltd/neural-link-between-agents/issues/32) | Older ten-version overnight ledger | Reconcile target rows against actual dated public releases; mark missed/obsolete rows accurately. |
| [#19](https://github.com/Ventusltd/neural-link-between-agents/issues/19) | Phase-2 relevance and data-centre integration | Check which source/rights/identity requirements landed in current production; retain unresolved evidence gaps. |
| [#24](https://github.com/Ventusltd/neural-link-between-agents/issues/24) | ChatGPT-only Phase-2 controller | Verify historical handoffs and whether its control remit was superseded by #42; avoid duplicate integrators. |
| [#21](https://github.com/Ventusltd/neural-link-between-agents/issues/21) | Historical V9.20 publication | Verify immutable V9.20 receipts and close/archive if all scoped acceptance was completed. |

### Specialist and delivery work

| Issue | Remit | Remaining action / classification |
|---|---|---|
| [#43](https://github.com/Ventusltd/neural-link-between-agents/issues/43) | Covenant commitments | Tested source/ledger handoff exists; integrate only compatible primary-source figures and source clocks; missing compliance evidence remains UNKNOWN. |
| [#44](https://github.com/Ventusltd/neural-link-between-agents/issues/44) | GRID AGENT / forecasts / podcast | Tested 32-source/24-test grid catalogue handoff exists; check actual integration and remaining layer/source coverage, no inferred grid capacity. |
| [#46](https://github.com/Ventusltd/neural-link-between-agents/issues/46) | Integration Advisor | Initial schema-compatibility recipe merged in PR48; determine whether follow-on consumer tests remain before closing. |
| [#49](https://github.com/Ventusltd/neural-link-between-agents/issues/49) | Neural Memories | Validated handoff merged in PR50; refresh stale V9.25–V9.29 dependency ledger for current release and close/retain with reason. |
| [#51](https://github.com/Ventusltd/neural-link-between-agents/issues/51) | Furnace / CuPy offline review | PR52 research index merged; verify whether hourly local scheduler/reviews actually ran, avoid implying hosted GPU or adoption. |
| [#34](https://github.com/Ventusltd/neural-link-between-agents/issues/34) | Agent 6 news algorithms | Evaluate research PR33 against current producer code, editorial contradiction tests and source rights; research is not release. |
| [#37](https://github.com/Ventusltd/neural-link-between-agents/issues/37) | Spiders / CVAA / Kuiper links | Implement source-pinned read-only link bridge and stale-green rejection tests; PR36 is only research handoff. |
| [#40](https://github.com/Ventusltd/neural-link-between-agents/issues/40) | Agent 10 Machine Read Notes | Check TestCode prototype and current product integration; independently gate rights, chronology, mobile and evidence before release. |
| [#41](https://github.com/Ventusltd/neural-link-between-agents/issues/41) | Agent 11 Solar-1000 evidence | Check source-order vs numeric-Ref-ID cohort conflict, queue, identity matching, provenance and PR/CI; no automatic VERIFIED promotion. |

### REPD Q3 / older cross-repo work

| Issue | Remit | Remaining action / classification |
|---|---|---|
| [#12](https://github.com/Ventusltd/neural-link-between-agents/issues/12) | October 2026 REPD Q3 intake | Reconcile source ingestion, immutable release and remaining source-rights issues; close if resolved. |
| [#13](https://github.com/Ventusltd/neural-link-between-agents/issues/13) | Agent B Q3 source QA | Check independent regression receipts against current source and close/reopen concrete defects only. |
| [#14](https://github.com/Ventusltd/neural-link-between-agents/issues/14) | Agent C Q2 provenance | Confirm genuine Q2 restoration/provenance before administrative closure. |
| [#15](https://github.com/Ventusltd/neural-link-between-agents/issues/15) | Agent D Q3 Pipeline News | Check source-to-news binding and published candidate evidence; retire stale assignment. |
| [#16](https://github.com/Ventusltd/neural-link-between-agents/issues/16) | Agent E Q3 GridAtlas mapping | Check actual mapping/numerical QA and close or transfer live defects to GridAtlas. |
| [#17](https://github.com/Ventusltd/neural-link-between-agents/issues/17) | Agent F Q3 release gate | Check independent release/rollback sign-off; retire old gate once superseded. |
| [#20](https://github.com/Ventusltd/neural-link-between-agents/issues/20) | REPD and data-centres convergence | Reconcile verified DC data and licensing against current product; unresolved rights remain blocked. |

### Legacy Kuiper / agent mailboxes

| Issue | Remit | Remaining action / classification |
|---|---|---|
| [#1](https://github.com/Ventusltd/neural-link-between-agents/issues/1) | Original GridAtlas #73 Agent A/B | Reconcile with actual GridAtlas issue/PR state; preserve useful 30/30/30 and release receipts. |
| [#2](https://github.com/Ventusltd/neural-link-between-agents/issues/2) | Agent C onboarding | Mailbox, not an executing worker; archive/close if unused. |
| [#3](https://github.com/Ventusltd/neural-link-between-agents/issues/3) | Agent D onboarding | Mailbox, not an executing worker; archive/close if unused. |
| [#4](https://github.com/Ventusltd/neural-link-between-agents/issues/4) | Agent E onboarding | Mailbox, not an executing worker; archive/close if unused. |
| [#5](https://github.com/Ventusltd/neural-link-between-agents/issues/5) | Agent F Claude onboarding | Awaited acknowledgement; archive if superseded. |
| [#6](https://github.com/Ventusltd/neural-link-between-agents/issues/6) | Kuiper estate survey | Carry forward verified source/code inventory; check actual Kuiper edition status. |
| [#7](https://github.com/Ventusltd/neural-link-between-agents/issues/7) | UK DC 227→226 baseline design | Verify final canonicalisation, DCF hash and false-merge safeguards in current data, then close if done. |
| [#8](https://github.com/Ventusltd/neural-link-between-agents/issues/8) | GridAtlas v9.188 independent QA | Historical QA; transfer any still-reproducible defects, then archive. |
| [#9](https://github.com/Ventusltd/neural-link-between-agents/issues/9) | Kuiper Edition 5 / See Through mobile | Verify edition and actual Android acceptance; do not infer ten Fable agents completed. |
| [#10](https://github.com/Ventusltd/neural-link-between-agents/issues/10) | Kuiper ten-step estate OS roadmap | Reuse relevant GridAtlas layers/See Through lessons; verify whether proposed roadmap/modules were delivered. |
| [#11](https://github.com/Ventusltd/neural-link-between-agents/issues/11) | Neural Link twelve-agent protocol | Check current PROTOCOL/LINK-RULE against proposals; no persistent model socket or automatic wake. |

## 7. Neural Link open-PR inventory — all 18

**16 draft, two non-draft (#23 and #58).** A draft PR is not a completed implementation. Avoid auto-merging stale documentation over current main.

| PR | Contents | State | Review / close action |
|---|---|---|---|
| [#58](https://github.com/Ventusltd/neural-link-between-agents/pull/58) | Agent coordination efficiency and expired schedules | READY | Review STATUS.json, validator, CI and six retired cron triggers; merge only after independent checks. |
| [#57](https://github.com/Ventusltd/neural-link-between-agents/pull/57) | Vicinity owner document archive with README link | DRAFT | Compare to #56; retain one byte-verified archive after independent review, avoid duplicate DOCX. |
| [#56](https://github.com/Ventusltd/neural-link-between-agents/pull/56) | Vicinity owner document archive | DRAFT | Compare to #57; choose one canonical intake, close redundant branch without losing evidence. |
| [#55](https://github.com/Ventusltd/neural-link-between-agents/pull/55) | Five PN and five GJ milestone reconciliation | DRAFT | Review dependency manifest against latest V9.41 and GJ heads; merge if still useful; no code claim. |
| [#54](https://github.com/Ventusltd/neural-link-between-agents/pull/54) | Agent activation handshake documentation | DRAFT | Review against AGENTS.md and PROTOCOL.md; merge or consolidate with #58. |
| [#39](https://github.com/Ventusltd/neural-link-between-agents/pull/39) | Agent8→Agent9 TestCode/iPhone brief | DRAFT | Check if Agent9 executed the work; archive or merge only durable instructions. |
| [#38](https://github.com/Ventusltd/neural-link-between-agents/pull/38) | Agent8 continuity audit | DRAFT | Historical dated receipt; retain if useful, do not treat as current release. |
| [#36](https://github.com/Ventusltd/neural-link-between-agents/pull/36) | Spiders/CVAA handoff | DRAFT | Keep research provenance; separately implement bridge under #37. |
| [#35](https://github.com/Ventusltd/neural-link-between-agents/pull/35) | Pre-Agent7 historical research | DRAFT | Archive as dated research only if independent review passes. |
| [#33](https://github.com/Ventusltd/neural-link-between-agents/pull/33) | Agent6 news-algorithm hypotheses | DRAFT | Review against live code and counterexamples; do not equate hypotheses to implementation. |
| [#31](https://github.com/Ventusltd/neural-link-between-agents/pull/31) | Agent5 Agent1 recovery notes | DRAFT | Dated continuity only; check obsolescence before merge. |
| [#29](https://github.com/Ventusltd/neural-link-between-agents/pull/29) | Agent protocol/README refresh | DRAFT | Compare with current main, #54 and #58; avoid overwriting newer links. |
| [#28](https://github.com/Ventusltd/neural-link-between-agents/pull/28) | AgentA Phase2 veto receipt | DRAFT | Retain dated blocker history, do not reapply stale veto to V9.41. |
| [#27](https://github.com/Ventusltd/neural-link-between-agents/pull/27) | Agent3 news scope request | DRAFT | Verify ACK or close stale request. |
| [#26](https://github.com/Ventusltd/neural-link-between-agents/pull/26) | Agent4 editorial challenge | DRAFT | Review specific falsification cases; dated research only. |
| [#25](https://github.com/Ventusltd/neural-link-between-agents/pull/25) | Phase2 controller handoff | DRAFT | Retire if superseded by #42; keep immutable evidence. |
| [#23](https://github.com/Ventusltd/neural-link-between-agents/pull/23) | 14 Nov news sweep and audit | READY | Seven REPD conflicts and planning-register checks remain in its brief; verify before factual publication. |
| [#18](https://github.com/Ventusltd/neural-link-between-agents/pull/18) | Visible agent activity index | DRAFT | Compare with #58 STATUS.json; avoid two competing status authorities. |

**Immediate de-duplication:** #56 and #57 both archive the owner's Vicinity Familiarisation DOCX and searchable text. Independently compare file bytes/sha, path overlap and README changes, choose one canonical intake, preserve the other handoff link, and close the redundant PR only after review. #58 is a separate coordination-efficiency change with locally reported checks; hosted CI and independent review were not yet confirmed in the issue handoff.

## 8. Cross-repo dependencies, risks and non-goals

1. **Release history:** PN V9.41 is operative per #42; do not reopen frozen PN V9.25–V9.41 or conflate VF-01–05 with PN versions. `CURRENT_PIPELINE_NEWS_VERSION.md` and parts of `AGENTS.md` still describe V9.22/V9.23 and require a reviewed correction, not retroactive product edits.
2. **Source ownership:** `data-grid-gb` owns source/crosswalk/rights; `ventus-grid-engine` owns graph traversal; `gridatlas` owns native Layers/UI; `globalgrid2050` is an explicit, rights-safe consumer. Kuiper/Faraday/See Through/Solar Studio reuse must follow source audit and owner contracts.
3. **Privacy/security:** no restricted NUAR/utility cable geometry, customer locations, private coordinates, secrets or privileged URLs in this **public** Neural Link repository or public GitHub Actions logs. User feedback is quarantined and moderated; no anonymous report becomes a verified circuit.
4. **Scientific truth:** a moving neon cursor is educational route order, not measured current, electrons, AC power direction or available capacity. ETYS forecast/SCOTEX boundary scalars and lightning events cannot become per-circuit live arrows.
5. **Performance/accessibility:** deterministic bounded radius searches, source/layer namespace isolation, request cancellation, teardown, small mobile screens, touch/keyboard, reduced-motion and colour-independent confidence cues. Browser CI is not physical iPhone/Android certification.
6. **Rollback:** all VF work is branch/preview isolated. Preserve exact operative `atlas/current.json`, `STATE.md`, homepage pins and old release trees. Promotion needs independently checked source rights, exact-head CI, actual served bytes, browser acceptance, owner sign-off and a tested restore path.

## 9. Critical decisions for owner/integrator

- Choose the first **lawfully publishable, independently identifiable real pilot**: London 400/275/132 kV first if data allows, otherwise a region with better DNO geometry/rights. A geographical London preference does not prove the necessary datasets exist.
- Decide whether the first release is **mapped-corridor familiarisation only** or requires **reviewed electrical circuit identity** before the real trace toggle is enabled.
- Nominate source/licence reviewer and independent electrical topology reviewer; settle what is safe to show publicly for underground assets.
- Obtain a specific NUAR eligibility and redistribution decision **before** any authorised adapter is enabled; a website link is not a data licence.
- Set one current release integrator and agent concurrency ceiling; merge or close overlapping Neural Link coordination PRs only after review.
- Require a user-visible legend that never confuses nearby, mapped, electrically connected, planned and withheld states.

## 10. Definition of done

**Scope complete:** one canonical, source-linked work order; five non-colliding VF increments; ten agent steps; all 34 open issues and 18 open PRs classified; GJ-01..05 dependencies pinned; data rights and release gates documented.

**Product complete:** independently approved real pilot, tested native GridAtlas 1–50 km UI and route logic, evidence-status legend, source attribution, no false joins, cross-voltage proofs, accessible animation, independent CI/mobile QA, approved public release and rollback. This document does **not** claim those product gates have passed.

**Evidence index:** [Neural #42](https://github.com/Ventusltd/neural-link-between-agents/issues/42), [#45](https://github.com/Ventusltd/neural-link-between-agents/issues/45), [#44 grid catalogue](https://github.com/Ventusltd/neural-link-between-agents/issues/44#issuecomment-6923956362), [#43 policy handoff](https://github.com/Ventusltd/neural-link-between-agents/issues/43#issuecomment-6923919158), [#58 efficiency](https://github.com/Ventusltd/neural-link-between-agents/pull/58), [#56](https://github.com/Ventusltd/neural-link-between-agents/pull/56), [#57](https://github.com/Ventusltd/neural-link-between-agents/pull/57), [#55](https://github.com/Ventusltd/neural-link-between-agents/pull/55), and the five GJ PRs in §2. Revalidate all heads, status and CI at execution time.
