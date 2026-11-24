# Agent 22 — SatNav reviewed 100-step work board

2026-11-24 | [NL-084](https://github.com/Ventusltd/neural-link-between-agents/issues/84) | [historical IDs 13–21](https://github.com/Ventusltd/neural-link-between-agents/issues/42)

**PLANNING ONLY — implementation, integration, tagging and publication HOLD.** Owner requested review and coordination recording. This board is an amended proposal, not a verified source audit. SatNav base observed 6113a9b5ce53f4ebcfe76be644a6e0ce5516b70c; reverify before acting. Six roles continue prior numbering: 22 architect (self-reserved); 23 terrain; 24 router; 25 HUD; 26 offline; 27 independent QA (proposed, no ACK). New agents use 28 onward after conflict checks. Historical A–F and numerical identities retained. Refer to AGENTS.md, PROTOCOL.md, OPERATIONS.md, NL-042, #64, #81. Do not infer session activity from issue comments.

## Scope decisions and gates
- Keep three modes distinct: public-road graph, authorised field routes, indicative cable corridor planning. No automatic entry into compounds/private land, no inferred access from a gate or geometric proximity. Unknown data is unknown. No routing through hard barriers. Navigation not safety-certified.
- Standalone SatNav static app, no own backend, login or paid keys. Optional external OSRM/Overpass/terrain requests only with documented terms, privacy, rate limits and fallback. Public OSM tile bulk/offline downloads prohibited; use permitted packs. No offline road routing beyond cached licensed graph coverage. Device capabilities are not guaranteed.
- Preserve GridAtlas Vicinity, Pipeline News MAP/A4, all immutable releases, canonical data and homepage. Reuse verified interfaces and design tokens, not a new data ecosystem. Integration later on isolated branches with separate owner approval.
- Pin inputs, rights, source SHA, task ID, expected artifacts, exact-head tests, independent reviews, failures, rollback. Python/CI preprocessing, deterministic fixtures, Chromium/WebKit, real mobile separately. Performance and slopes are targets/assumptions only. No claim of 250k LOC/69 repositories without census.
- State transitions NOT_STARTED → RESERVED → IMPLEMENTED → TESTED → REVIEWED → VERIFIED, or BLOCKED; only independent evidence grants VERIFIED. One state writer (Agent 22) reconciles agent receipts; each owner writes only their own branch. No phase progression until prerequisites verified; T099 precedes final tag T098, T100 after deployment, T097 checks prerequisites and cannot assert future tasks passed. T001–010 are proposed phase 1, not executed by recording this board. T085–094 are the ten specified replays, T095 consolidates. Original phase range overlaps corrected: 1–15,16–35,36–50,51–66,67–73,74–100.

## Work board
| Task | Agent | Bounded deliverable / gate |
|---|---:|---|
| T001 | 22 | Create SatNav coordination state and proposed contracts (not locked). |
| T002 | 22 | Audit actual GridAtlas exports, active layers and deep links; pin source SHA. |
| T003 | 22 | Audit simulator LiDAR fetcher, CRS, nodata and elevation buffer; do not assume availability. |
| T004 | 22 | Audit Overpass helpers and data/usage rights; define feature schema. |
| T005 | 22 | Define CostGridSpec: CRS, origin, dimensions, resolution, masks and typed arrays. |
| T006 | 22 | Define Worker request/response, errors, cancellation and route metadata. |
| T007 | 22 | Define TelemetryPacket including fix age and uncertainty. |
| T008 | 22 | Define OfflinePackManifest, hashes, licences, coverage and expiry. |
| T009 | 22 | Audit and lock native SCADA tokens only after parity review. |
| T010 | 27 | Independently validate proposed schemas, rights and exact pinned inputs; approve contract lock only on evidence. |
| T011 | 22 | Prepare compact <4k-token handoffs and dependency/ownership reservations. |
| T012 | 23 | Scaffold cost-grid-builder.js on exclusive SatNav branch. |
| T013 | 24 | Scaffold hybrid-router-worker.js with typed messages, cancellation and errors. |
| T014 | 25 | Scaffold scada-nav-hud.js and CSS with existing SCADA parity. |
| T015 | 26 | Scaffold offline-corridor-cache.js and nav-sw.js. |
| T016 | 23 | Implement and validate local metric CRS transforms against reference points; <0.5m target. |
| T017 | 23 | Allocate Float32 grid and separate known/unknown, access and hazard masks; no default permission. |
| T018 | 23 | Resample licensed EA DTM to adaptive 5/10m cells; preserve nodata. |
| T019 | 23 | Evaluate licensed terrain fallback, resolution/coverage and offline packaging. |
| T020 | 23 | Implement Horn slope with nodata and edge handling. |
| T021 | 23 | Rasterise road vectors with road access/profile constraints (0.15x proposed). |
| T022 | 23 | Rasterise tracks/bridleways with mode-specific rights (0.35x proposed). |
| T023 | 23 | Rasterise footways/paths for FOOT_SURVEY (0.4x proposed). |
| T024 | 23 | Rasterise buildings as hard obstacles. |
| T025 | 23 | Rasterise waterways; only evidenced mode-compatible crossings, not generic fords. |
| T026 | 23 | Rasterise hedges/fences/walls; protect hard obstacle mask. |
| T027 | 23 | Model mode-compatible gates/stiles with permission evidence; never punch unrelated obstacle. |
| T028 | 23 | Generate indicative verge/margin buffers; 2–5m requires appropriate resolution. |
| T029 | 23 | Audit and ingest licensed ALC/flood layers; proposed 2.5x and 3x penalties. |
| T030 | 23 | Compile modes and configurable slope assumptions; unknown/access restrictions fail closed for navigation. |
| T031 | 23 | Snap only to authorised reachable access points; report offset, refuse unsafe snaps. |
| T032 | 27 | Test river/bridge, fence/gate, corner cutting, cliff and missing/access data negatives. |
| T033 | 27 | Benchmark 600x600 construction, device and p50/p95; <80ms aspirational. |
| T034 | 23 | Implement transferable buffers without losing retained offline source. |
| T035 | 27 | Publish Phase 2 test receipt only after exact-head tests and independent review. |
| T036 | 24 | Implement typed-array binary min heap, stale-entry handling and deterministic tie breaks. |
| T037 | 24 | Implement 8-connected search with diagonal cost and corner-cut prevention. |
| T038 | 24 | Implement admissible octile heuristic using actual lower-bound cost, verify against Dijkstra. |
| T039 | 24 | Implement bounded parent backtracking and no-route error. |
| T040 | 24 | Implement obstacle- and cost-preserving smoothing; retain hazard/transition points. |
| T041 | 24 | Attach vertex arrays for elevation, slope, surface, cumulative 2D/3D distance; valid GeoJSON. |
| T042 | 24 | Implement optional >5km OSRM road leg after terms/privacy review; verified access-point handoff within 1.5km when feasible. |
| T043 | 24 | Use licensed cached offline road graph; otherwise clearly stop outside coverage; no DEM road substitute. |
| T044 | 24 | Generate >30-degree turns, surface transitions and configurable grade alerts. |
| T045 | 24 | Generate evidence-based manoeuvres, no fabricated gate access or street names. |
| T046 | 24 | Emit GeoJSON FeatureCollection route, waypoints, hazards with provenance. |
| T047 | 24 | Implement debounced reroute based on GPS accuracy, 25m alert/30m proposed reroute thresholds. |
| T048 | 27 | Test five permitted rural journeys using public or synthetic access fixtures; no restricted-site entry. |
| T049 | 27 | Benchmark worker peak memory and p50/p95 latency; <25MB/<150ms targets not claims. |
| T050 | 27 | Publish Phase 3 exact-head verification receipt. |
| T051 | 25 | Implement geolocation permission, high-accuracy and stale-fix state. |
| T052 | 25 | Implement accuracy-aware smoothing and stationary jitter handling. |
| T053 | 25 | Implement iOS/Android compass permission, heading reliability and fallback. |
| T054 | 25 | Implement wake lock acquisition/release/visibility lifecycle. |
| T055 | 25 | Implement distance, bearing and segment-aware signed cross-track error. |
| T056 | 25 | Implement waypoint advancement with accuracy, route progress and passed-plane guards. |
| T057 | 25 | Implement heading-up 3D chase and north-up 2D; disable when unsafe or heading unknown. |
| T058 | 25 | Implement route/breadcrumb/tether/accuracy layers using audited style tokens. |
| T059 | 25 | Implement concise next manoeuvre banner. |
| T060 | 25 | Implement remaining distance, XTE, elevation, grade and accuracy readout. |
| T061 | 25 | Implement 48px thumb controls and separation of planning mode from active navigation. |
| T062 | 25 | Implement local speech voice discovery and deduplicated utterances; visual fallback. |
| T063 | 25 | Implement 100m/25m prompts and configurable 25m off-course alert with hysteresis. |
| T064 | 25 | Implement daylight/high contrast mode and reduced motion. |
| T065 | 27 | Test touch, safe areas, denied permissions and Safari/Chrome layouts; distinguish physical testing. |
| T066 | 27 | Publish Phase 4 receipt with exact source and device matrix. |
| T067 | 26 | Implement versioned IndexedDB stores and migration/rollback. |
| T068 | 26 | Enumerate corridor tiles only for licensed self-hosted/packaged sources; enforce coverage and size budgets. |
| T069 | 26 | Implement scoped service worker for app shell and permitted assets; version and invalidate. |
| T070 | 26 | Implement atomic corridor pack with cost/elevation/vector/route hashes and completeness. |
| T071 | 26 | Implement quota estimates, storage persistence capability and purge UI. |
| T072 | 26 | Test offline reload and reroute within complete cached coverage; missing pack fails explicitly. |
| T073 | 27 | Publish Phase 5 receipt including airplane-mode/browser tests and physical-device distinction. |
| T074 | 22 | Propose GridAtlas Navigate Here adapter using stable asset ID and authorised access point; audit count; preserve existing MAP/Vicinity. |
| T075 | 22 | Propose Pipeline News Navigate to Site adapter; preserve REPD and immutable releases. |
| T076 | 22 | Propose simulator/Solar Design Studio handoff; verify actual interfaces and permissions. |
| T077 | 22 | Implement validated deep links and coordinate privacy warning after integration approval. |
| T078 | 23 | Implement local opt-in GPX/GeoJSON/CSV track recorder; no automatic sharing. |
| T079 | 22 | Define cable estimator adapter for indicative 3D distance, grade and land breakdown; no engineering certification. |
| T080 | 22 | Define local field-note pins with opt-in export and no public upload. |
| T081 | 27 | Run integration tests GridAtlas → SatNav → offline → cable planning, preserve MAP/A4 and Vicinity. |
| T082 | 27 | Audit privacy, third-party coordinate disclosure, local retention and purge. |
| T083 | 27 | Verify static deployment and no paid keys or runtime bundler dependency. |
| T084 | 22 | Prepare homepage catalogue change only as separate owner-authorised release candidate. |
| T085 | 27 | Replay steep Highland synthetic/authorised terrain fixture. |
| T086 | 27 | Replay Fenland flood/ditch fixture. |
| T087 | 27 | Replay Somerset hedge maze fixture. |
| T088 | 27 | Replay urban-to-authorised-site transition fixture. |
| T089 | 27 | Replay GPS loss fixture. |
| T090 | 27 | Replay mid-walk reroute fixture. |
| T091 | 27 | Replay low-battery/wake-lock fallback fixture. |
| T092 | 27 | Replay iOS orientation permission fixture. |
| T093 | 27 | Replay Android local TTS availability fixture. |
| T094 | 27 | Replay 3G tile timeout fixture. |
| T095 | 27 | Consolidate ten replay receipts and regression matrix (additional explicit step to remove 85–95 ambiguity). |
| T096 | 27 | Log defects to state, route bounded repairs to owners; retest exact heads. |
| T097 | 27 | Verify applicable steps with evidence; no fictitious 100/100 pass; gate final deployment separately. |
| T098 | 22 | Prepare v1.0.0 tag only after all prerequisite gates and explicit owner approval. |
| T099 | 22 | Prepare accessible static about/learning page; include in release candidate before tagging (ordering dependency). |
| T100 | 27 | Verify owner-approved live Pages bytes, rollback and actual mobile field readiness; no self-certification. |

## Owner destination amendment — NL-084 #7138850753
P1 served preview remains immutable and partial physical acceptance recorded (#7138653815, #7138775416). Successor reserved: `agent22/satnav-destination-20261124`, parent `f4ce7ccdc9e8f4bc15915605a07071b9363d5dfb`, contract `41b2b21f52c911bb9d51b1ed804f04cec578c3b7`.
| Existing task | Next bounded action | Gate |
|---|---|---|
| T002 | Agent23 audit exact GridAtlas gazetteer, marker inputs, source identity, UK coverage and terms; 22 integrates reviewed adapter | No invented geocoder or live export |
| T074 | Agent22 primary place search and map choice; explicit Use this destination handoff, optional signed coordinates | Agent24 normalization and access distinction review |
| T077 | Preserve canonical and legacy deep links; isolated successor, no live GridAtlas edits | Agent31 end-to-end browser and real Safari |
| T082 | Agent29 deterministic failure/privacy fixtures, Agent30 independent review, Agent28 acceptance/regression | No live GPS disclosure, no production regression |
Separate owner approval for successor publication. Existing P1 and all public paths retained. Implementation and provider review pending.
