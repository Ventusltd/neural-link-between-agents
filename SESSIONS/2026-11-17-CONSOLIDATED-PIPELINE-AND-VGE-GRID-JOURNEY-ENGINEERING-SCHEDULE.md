# Consolidated engineering scope — Pipeline News V9.34–V9.38 + VGE 2.0 Grid Journey
**17 November 2026 | Ventus Ltd / GlobalGrid2050 | Documentation only — no code release or version reservation**

## 0. Decision record and authoritative predecessors

**Owner instruction:** consolidate the earlier release schedules with the latest code-versus-official-source study; retain all useful previous research; provide the next five **separate** Grid Journey implementation increments without interfering with the five **Pipeline News** proposals. This document is a **planning synthesis**, not authorisation to merge or publish; ROOT/release owner must verify current heads before committing any new product code.

Read in order:
1. [Corrected Pipeline News history and provisional V9.34–V9.38 schedule](https://github.com/Ventusltd/neural-link-between-agents/blob/ff97515f44c7d1e9bc4884d3b08706defd9c0b7d/SESSIONS/2026-11-17-PIPELINE-NEWS-VERSION-RECONCILIATION-AND-V934-V938-SCOPE.md).
2. [VGE 2.0 Grid Journey technical design](https://github.com/Ventusltd/neural-link-between-agents/blob/e141971ce4981ac51b3cc348d6ffd7f3b504765b/SESSIONS/2026-11-17-VGE20-GRID-JOURNEY-NEON-TOPOLOGY-FLOW-SCOPE.md).
3. [Release coordination issue #45](https://github.com/Ventusltd/neural-link-between-agents/issues/45) and [integration/command issue #42](https://github.com/Ventusltd/neural-link-between-agents/issues/42).
4. Source repos: [GridAtlas](https://github.com/Ventusltd/gridatlas), [Ventus Grid Engine](https://github.com/Ventusltd/ventus-grid-engine), [data-grid-gb](https://github.com/Ventusltd/data-grid-gb), [GlobalGrid2050](https://github.com/Ventusltd/globalgrid2050), [Kuiper](https://github.com/Ventusltd/kuiper-belt), [Lightning](https://github.com/Ventusltd/lightning).
5. New Deep Research working report, 17 November 2026, on reusable code, DNO/TSO sources and neon train. It is *research input only*. Specific errors are corrected below; this commit supersedes its proposed numbering and unsupported shortcuts.

**Current history at inspection:** the homepage-owner catalogue `globalgrid2050-homepage/data/homepage.json` selects Pipeline News V9.33 edition `202611170512`. The product `globalgrid2050/uk_renewables_pipeline/versions.json` generated 07:29 UTC still describes V9.33 as a candidate and V9.32 operative; the discrepancy is already documented and held for ROOT audit. Do not treat that lagging registry as permission to republish or alter immutable directories. V9.25–V9.27 had candidate editions; V9.28–V9.32 were published; V9.33 homepage selected and independently reported published. Future V9.34–V9.38 labels below remain **provisional**, not reserved.

**Two namespaces, not one:** Pipeline News uses the V9.xx sequence. Grid Journey is a GridAtlas/VGE module; its five development milestones are **GJ-01 … GJ-05**, **not** Pipeline News V9.39 … V9.43. ROOT and the GridAtlas owner allocate actual future edition IDs later. The Deep Research report numbered V9.39 through V9.44 — **six** versions while saying five — and those labels have no standing. This avoids collisions with Pipeline News release ownership and history.

## 1. Purpose: a learning journey, not a load-flow animation

Tap a generator, offtaker, data centre, REPD project or documented substation in the **existing MapLibre GridAtlas**. Show a tiny neon dot tracing *published, properly identified* circuit edges in a bounded, deterministic order; visit eligible branches, cycles and parallel circuits, with explicit backtracking. Distinguish actual source-supported GIS polyline geometry from schematic node-to-node edges. Allow students to inspect the network, the evidence gap and the meaning of grid direction.

This is **not** a literal railway, a new map, a cable-laying planner, an energisation claim, an AC electron trajectory or an electrical study. No power-flow or short-circuit solver is mandatory. `Vicinity 30/30/30` discovers nearby candidates; it does not confer a connection, electrical distance or available headroom. A proposed generator/offtaker is not presumed physically connected.

Three independent directions must be shown separately:
- **Journey heading:** selected order of animation; educational, may traverse either way.
- **Published circuit topology:** graph edges and transformers, not known real-time switch state or instantaneous MW direction.
- **Measured, forecast or modelled power-flow:** separate time-stamped, signed datum **only** at the source's actual granularity (individual transformer, interconnector, or NESO aggregate boundary). If no validated sign exists: `Flow direction unavailable`.

## 2. Code evidence — reuse, not reconstruction

| Source path / contract | Verified behaviour and reuse | Critical missing piece / constraint |
|---|---|---|
| `gridatlas/atlas/current.json` | Native MapLibre composer `gridatlas.current.v2`; generation `202611161720` inspected; `sld-sandbox`, `substation-intelligence`, `uk-lightning-overlay`, `uk-offtakers-overlay` cartridges | Add **isolated, removable preview cartridge** and its proof; do not edit operative pointer or replace map with React/Canvas |
| `gridatlas/tools/offtakers/src/06b-dc-engine.js`; `docs/OFFTAKERS-SOURCE.md` | DC tap: nearest 30 ≥33 kV substations inside **40 km**; 30 REPD inside **40 km**; 30 nearest conventional assets irrespective of distance, draw links only ≤100 km. 5-node legacy `nearestSubstations` and 30-node `gridScope.scope` are distinct; licence-aware CSV and straight-line screening | 90 is **at most**, and spatial; existing drawn straight lines are **not** cable circuits; never blindly seed nearest OSM site as connected |
| `data-grid-gb/derived/gb-transmission-network.v1.json`; `README.md` | NESO ETYS Appendix B-derived 921 sites, 2,679 nodes, 1,392 circuits, 1,472 transformers, 2,230 planned changes | Published network **model**, not surveyed circuit polylines or current breaker/switch status; future changes must not become an operative traversal |
| `data-grid-gb/derived/connection-points.v3.json` | 886 ≥132 kV names; 489 coordinate joins and 397 without located joins at prior audit | Ambiguous names, sites without coordinates, different DNO voltage coverage: maintain reviewed ETYS↔GIS identity crosswalk; no nearest-dot substitution |
| `ventus-grid-engine/engine/network-topology.js` | `index(product)` checks `data-grid-gb.transmission-network.v1`; `index.graph()` exposes `edgesAt(node)`, `nodesOfSite(code)`, voltage/site lookups, circuit and transformer rows, and excludes `planned_change` from graph edges | Node graph, not circuit GIS geometry. Preserve parallel physical units; do not collapse records merely because endpoints match |
| `ventus-grid-engine/engine/electrical-distance.js` | `between(index,from,to,{maxHops,voltageKv})` BFS fewest-hop path; `within(...)` neighbourhood; rejects an invalid cross-voltage **circuit**; an explicit transformer is required | Neither is all-edge traversal. Implement edge-cover in a separate module, reuse legal-edge rules; do not modify proven shortest-path API |
| `globalgrid2050/energy-transition-simulator/.../mod/engine/journey.mjs` | Actual substation navigation and camera transitions | Reuse navigation ideas only, not implicit network edges |
| `globalgrid2050/kuiper-grid/drawing/whole-site-routes.js`; `whole-site-route-view.js`; `kuiper-belt/cosmos/{wafer,pulse}.tsv` | Drawing, route IDs, native visual tracing and neon pulse idioms | Synthetic solar feeders/SLDs are **design drawings**, not independently verified real GB infrastructure |
| `gridatlas/tools/lightning/src/` and `Ventusltd/lightning` | Source-built overlay pattern, timestamp handling, MapLibre lifecycle | EUMETSAT optical flash ≠ ground strike or proven network failure; weather unrelated to topology or MW |
| `data-grid-gb/docs/routing/{LEGACY_LAYER_AUDIT,METHOD_AND_LIMITATIONS}.md` | Existing road/rail lines useful as display layers | Road/rail crossings and proposed corridors do not identify cable joints or existing electrical connectivity |

**Important correction to Deep Research:** it stated transformers could be “assumed” when 400 and 132 kV lines meet. That is **prohibited**: only independently recorded transformer edges, windings/buses and valid voltage transition may be traversed. It also said “no existing graph search code shown”, overlooking `electrical-distance.js`; and incorrectly assumed all `grid_*kv` LineStrings can be safely treated as one-to-one ETYS circuit paths. The latter need explicit circuit-identity provenance and spatial joins, not endpoint snapping alone.

Additional constraints: `physicalUnits(records)` in `network-topology.js` counts mirrored circuit landings by node pair; retain published parallel-unit multiplicity. If source rows do not expose a stable unique circuit key, derive a documented deterministic **per-source-row UID** preserving multiplicity and geometry status; do not automatically deduplicate parallel circuits. An ETYS site may contain distinct voltage buses; merely co-locating buses at a site does not prove an electrical bridge, bus coupler closed or an active transformer. Published ETYS circuit adjacency is not live switching telemetry.

## 3. Official data and engineering-evidence ladder

| Data / authority | Permitted product claim | Not permitted |
|---|---|---|
| [NESO ETYS 2025 official appendices](https://www.neso.energy/research-publications/etys/documents), A/B/C | Appendix A schematic/geographic reference; Appendix B published model connectivity, impedances and equipment; Appendix C **modelled future winter-peak** diagrams with scenario/version | Current live flow on an individual local cable; exact geographic underground bends from a schematic; a circuit energisation inference |
| [NESO Day Ahead Constraint Flows and Limits](https://www.neso.energy/data-portal/day-ahead-constraint-flows-and-limits) and [field meanings](https://www.neso.energy/data-portal/day-ahead-constraint-flows-and-limits/day_ahead_constraint_flows_and_limits) | Half-hour **day-ahead forecast** net `Flow_MW` across named **constraint boundary**; published PDF defines positive direction. `Limit_MW` context, vintage/time and licensed source | Per-circuit flow, real-time measurement or connection capacity. After 22 April 2024 methodology changed (expected mitigation/optimisation no longer considered) — flag series break |
| [Elexon BMRS/Insights API](https://bmrs.elexon.co.uk/api-documentation/endpoint); [interconnectors](https://bmrs.elexon.co.uk/interconnector-flows) | Time-specific interconnector import/export and generation/demand/BM unit context, **after verifying series-specific sign convention** | Treating every local circuit as carrying BMU generation or inferring DNO feeder direction |
| [UKPN DSO open data](https://dso.ukpowernetworks.co.uk/dso-data); [UKPN SGT header](https://ukpowernetworks.opendatasoft.com/explore/assets/ukpn-super-grid-transformer-header/) | Published named GSP/SGT/transformer measurements at actual instrument and timestamp, **where accessible and licensed** | UK-wide DNO coverage; simultaneous network state; current through every child feeder |
| [UKPN primary transformer half-hourly methodology](https://ukpowernetworks.opendatasoft.com/explore/assets/ukpn-primary-transformer-power-flow-historic-half-hourly-spn/) | Measurements are historian-derived half-hour averages; public LTDS drawings can be planning rather than operational; redactions and possible manual join error | **Any direction arrow by default**. Publisher explicitly warns polarity/directionality inconsistent; current magnitude positive irrespective of direction; some records redacted under Utilities Act |
| Official DNO LTDS/DSO publications (UKPN, NGED, ENWL, SSEN Distribution, SPEN, NPg), TO works / NESO / Ofgem notices | Source-specific planning and asset context, network drawings, declared links, actual dated works where rights permit | General UK distribution feeder topology presumed uniformly downloadable, open-licensed or operationally switched as diagrammed |
| GridAtlas OSM / Ordnance Survey line layers | Geospatial **mapped feature** with CRS and exact attribution/rights/accuracy caveat | Calling a GIS LineString an ETYS circuit without approved crosswalk, assuming OSM/OS licences are interchangeable, or snapping at a crossing to create a false junction |

**Evidence states** (machine-readable and visible): 
1. `verified_circuit_and_polyline` — named published circuit matched to independently justified, permitted GIS segment(s): animate on actual line and disclose precision, e.g. mapped overhead route vs underground approximate;
2. `published_topology_only` — correct ETYS node-to-node edge, endpoints located but circuit bends unknown: **dotted schematic** straight connector with conspicuous `not a cable route` label or node-to-node jump;
3. `published_node_unlocated` — node/edge real in the model but no defensible coordinates: text stop only, no invented geometry;
4. `vicinity_screening_only` — close OSM substation/project/generator: explore nearby assets without electrical animation;
5. `ambiguous_or_licence_blocked` — abstain; report reason and source.
A source with mapped LineString geography but **no electrical identity** is a map feature, not a justified `verified_circuit_and_polyline`.

For all claims, retain `source_url`, source licence, original record/page/row, downloaded_at, source/as-of timestamp, hash, site/bus/edge identifiers, coordinate basis, identity confidence and manual review decision. A North→South **general boundary tendency** in an ETYS scenario is context, not a default arrow for one circuit; direction can reverse in differing states.

## 4. GJ engineering architecture and traversal contract

Proposed additions (paths are intended ownership locations, **not existing files**):
- **Source/data owner — `data-grid-gb`**: `pipelines/grid_journey_crosswalk.py` (reviewable ETYS↔GIS site/edge identity joins), `derived/grid-journey-crosswalk.v1.json` and source/rights manifest. Publish counts for exact, ambiguous, absent, topology-only, geometry-supported, restricted; preserve source and edition hashes. Do not amend original ETYS network or OSM immutable inputs.
- **Algorithm owner — `ventus-grid-engine`**: `engine/edge-cover-journey.js` reads existing `index.graph()`; separate `journey-evidence.js` for stable edge UID, electrical legality, graph subset and proof-classification. Return JSON plan, not paint pixels or calculate MW. No duplicate engine or repo.
- **Presentation owner — `gridatlas`**: `tools/journey/src/` with removable after-cartridge MapLibre GeoJSON line/symbol layer, existing substation/DC-card hook, restore and lifecycle guards, provenance labels, reduced-motion, Start/Next/Reset, keyboard/touch. Its own source hash/proof, byte budget and independent first-tap Safari/mobile acceptance.
- **Optional later flow-context adapters — `data-grid-gb` or agreed data owner**: source-specific NESO signed *boundary* series, Elexon named *interconnector* series, UKPN named transformer measurements; each independently verified and licence reviewed. No shared generic “flow on every circuit” field.

**Contract sketch**:
```ts
JourneyQuery = {
  seed: { namespace, assetId, siteCode?, voltageKv?, chosenNode? },
  sourceBundleSha, crosswalkSha,
  bounds: { radiusKm, maxNodes, maxEdges, maxMoves, maxMillis },
  modes: ["published_circuits"], // optional later "vicinity" and "flow_context"
  requireReviewedIdentity: true
}
JourneyStep = {
  kind: "advance" | "backtrack" | "stop" | "unlocated",
  edgeUid?: string, nearNode, farNode?, geometryStatus, sourceRef,
  voltageKv?, transformerRef?, order, estimatedGeometry?: false
}
JourneyResult = {
  selectedComponent, steps, eligibleEdges, visitedUniqueEdges,
  excluded: { ambiguous, unlocated, licence, planned, illegalVoltage, outsideBounds },
  truncated, inputDigests, coverage, caveats
}
```
Static TS example is illustrative; choose implementation language consistent with the existing JS engine and pinned data. Evidence-gated seeds may represent a *site* with several distinct nodes: require chosen node/voltage or expose multiple component choices. REPD/developer declaration of connection site is not proof of exact intermediate feeder or operational connection.

**Deterministic finite edge-cover walk** (not all simple paths; exponential in cyclic graphs):
```text
graph := existingTopology.index(pinnedETYS).graph()
eligible := filterBySourceReviewStatusVoltageRadiusAndBounds(graph, reviewedCrosswalk)
adj := canonicalUndirectedMultigraph(eligible, preserveParallelEdgeUIDs)
start := userSelectedReviewedNode
visitedEdgeUIDs := Set()
steps := []
function cover(u):
  for e in stableSort(adj[u], voltageClass, edgeKind, publisher, edgeUID, farNode):
    if e.uid in visitedEdgeUIDs: continue
    v := oppositeEndpoint(e, u)
    visitedEdgeUIDs.add(e.uid)
    steps.append(advance(e, u, v))
    cover(v)
    steps.append(backtrack(e, v, u))  # actual continuity; may retraverse a circuit
cover(start)
report(edgesCovered / eligibleReachableEdges, excluded, truncation)
```
Implement **iteratively with a stack** if node count risks recursion limits, and budget total moves/geometry bytes/time before playback. A cycle can be traversed then re-traversed on the way back; that is a real itinerary, not “power flowing backwards”. Count unique *eligible edges* rather than unique nodes, retain parallel-circuit count, and never silently teleport across disconnected components. If bounds trigger, mark `truncated` and provide a reason; unlocated stops and evidence-refused edges do not receive a pretend GIS trace. Voltage transition only through actual transformer edge; do not count merely co-located buses as connected. The `between()` shortest path remains independent.

**Acceptance fixtures:** 9-node radial, two branches, triangle cycle, parallel A–B circuits with distinct IDs, two substations whose lines cross on the map but have no junction, adjacent but unconnected 132/33 kV lines, explicit 400/132 transformer, co-located voltage buses **without** transformer, planned 2029 circuit, one-ended/mirrored source records, unlocated/ambiguous site, no licence for underground geometry, no seed, disconnected component, bounds exhaustion, two runs same pinned digest. Assert edge coverage, ordered continuity/backtracks, deterministic JSON output, no invalid voltage crossing, honest geometry status and refusal counts. Golden tests for two published-but-unsurveyed ETYS lines must render **dotted**, never “exact cable route”.

## 5. Consolidated release schedule A — Pipeline News (unchanged five *proposals*)

All five must remain attached to the existing **Pipeline News** release sequence; labels provisional until ROOT checks current authoritative homepage, product registry, source pin, open PRs and release ownership. Actual implementation can regroup only with logged owner approval. These are not GridAtlas/VGE release IDs.

| Proposed label | Scope from earlier schedule | Reuse / acceptance evidence | Interdependency with Grid Journey |
|---|---|---|---|
| **V9.34** | Better useful multi-source news intelligence | `automation/news/` existing 50-feed acquisition/binder, evidence ledger; >=100 actual pinned articles where available, original publisher, correct time semantics, false positive/rights tests; never auto-VERIFIED | Official DNO/TSO notices can later be contextual highlights, never topology edges |
| **V9.35** | Substantial ticker: 50–100 **real** items, remove visible Pause | Reuse `layers/{model,ticker}.mjs`, 12-item existing pagination; accessible keyboard/touch, reduced motion, 0/1/10/71/100 cases; preserve approved shell and attribution | Journey animation also requires independent motion accessibility; not the same UI component |
| **V9.36** | Repair MAP first-tap end-to-end visibility into GridAtlas (issue #87) | Exact REPD ID/deeplink/receiver/card and real visible map result; known cases 12588, 2470, 14535, 12453; desktop, mobile emulation **and** real Safari sign-off | **Blocking dependency** for Journey entry from Pipeline News: fix or isolate existing map receiver before journey UI |
| **V9.37** | Real grid upgrade intelligence from official publications, not static DNO directory | Permitted, timestamped notices, real upgrades and public planning/local authority decisions, source IDs, negative identity tests; zero is valid when no qualifying records | May seed *event annotations* along journey; not current circuit proof or power-flow direction |
| **V9.38** | Python distillation of DNO/TSO/local planning/government PDFs and publications | Source-specific extractors and SHA/version/page-level fact records, voltage/MW/time typed claims, corrections and nulls; compact dashboard results, no dumped document | Data extraction can support reviewed ETYS/TO/DNO evidence; **cannot automatically authorise** circuit joins |

**Pipeline gates for every release:** preserve unchanged source REPD and frozen Solar-1000 records, historic versions, sortable/paginated data and exports; source-rights and publisher attribution; explicit UNKNOWN over invented values; exact-head CI, schema/negative/data tests, old/new browser regression, homepage owner/publisher integration, public HTTPS served-byte and action checks, exact rollback receipts. ROOT is sole publisher. No "version count" without meaningful change. Production releases remain separate from candidate branches.

## 6. Consolidated release schedule B — Grid Journey: precisely FIVE milestone increments

**GJ numbers are local work-package labels, not shipped GridAtlas edition tags.** Code and data owners work on isolated branches with independently tested pull requests. Publish only to PREVIEW until a distinct authorised promotion.

| Milestone | Deliverable and specific code surface | Required engineering acceptance | Promotion rule |
|---|---|---|---|
| **GJ-01 — Evidence and identity baseline** | Inventory latest `gridatlas/atlas/current.json`, `data-grid-gb` ETYS B and GIS line sources; prototype reviewed site/edge identity crosswalk and licence/precision table. Expose generator/offtaker site candidate selection while retaining 30/30/30 proximity caveat. | Fixtures for same-name different sites, missing 397 coordinates, two bus voltages, REPD planned vs operating, ambiguous join; report exact match/abstain counts and dataset hashes. | Docs + isolated data test only; no live layer |
| **GJ-02 — Source-backed multigraph and itinerary** | `ventus-grid-engine/engine/edge-cover-journey.js` as **separate** module using existing `network-topology.index().graph()` and unchanged `electrical-distance.between()`. Include deterministic edge UID, parallel edges, cycles, explicit transformer-only voltage changes, move caps and refusal ledger. | Positive/negative 9-node fixtures, complete edge-cover continuity, canonical stable digest, no inferred connections, bounded runtime/memory; independent electrical-source QA. | Tested algorithm library/PR; no map promotion |
| **GJ-03 — Native GIS neon PREVIEW** | `gridatlas/tools/journey/src/` source-built, isolated after-cartridge; one minimal Journey action in existing card, glow dot along **verified polylines only**, dotted topology-only connectors with warning, next/backtrack/reset and source labels. | Official manifest composition hash; no double listeners/source collisions; 390/393/1440 and mobile landscape; first-tap map/card, 44px controls, VoiceOver/keyboard, reduced motion, no jank budgets; rollback/removal proof. | Preview URL only, operative `atlas/current.json` unchanged |
| **GJ-04 — UK DNO/TO evidence enrichment and honesty** | Source-specific, rights-checked UKPN and other DNO LTDS / TO diagram inventory; reviewed circuit geometry matches where feasible, missing/ambiguous/unlocated coverage UI and provenance; generator vs offtaker **journey starts** (not imaginary upstream/downstream MW). | At least one hand-reviewed real regional example if eligible sources exist, refuse all unknowns, explicit schematic-vs-surveyed route labels, do not claim map 132 kV coverage is complete. Regression with existing substation, offtaker, lightning layers and issue #87. | Independent source and engineering QA; preview stays until qualified |
| **GJ-05 — Optional direction context and release-readiness** | Distinct NESO **boundary forecast**, Elexon **interconnector flow**, and source-qualified UKPN **named transformer** time layers where verified. Keep motion dot direction independent of MW arrows. Full launch and rollback dossier for authorised GridAtlas owner. | Sign/time/zone/settlement unit tests; UKPN inconsistent polarity yields NO arrow, missing data yields null, NESO B6 north→south scenario does not colour every feeder, no real-time claim from ETYS C. Verify rights/access and served-site functional tests. | Owner may approve publication **after** independent checks; otherwise remain documented preview |

Sequence **GJ-01 → GJ-02 → GJ-03 → GJ-04 → GJ-05** is a dependency order, not a promised five-night or five-hour timetable. Execute in parallel only where interfaces and ownership are pinned; GJ-02 may use synthetic fixtures before GJ-01 crosswalk settles, but public real-route acceptance depends on GJ-01. GJ-05 data sources may fail rights or sign review; the rest of the journey remains valuable without any dynamic flow arrows. A preview-only GJ-03 must never silently amend live GridAtlas release manifest.

**Cross-stream schedule constraint:** Pipeline V9.36 resolves the existing map first-tap/receiver defect before claiming Pipeline News → Journey integrated acceptance. GJ-04 evidence may consume independently validated adapters arising from V9.37/V9.38, but the release trains remain separately owned and individually reversible. The GridAtlas manifest has after-cartridge, hash and byte-budget rules; obtain new slot/budget approval instead of assuming the 80 kB offtaker budget applies to a new cartridge.

## 7. Negative tests, clinical precision and operator safety

The release **must fail** (or refuse individual route) when any of these occur:
- Close OSM substation incorrectly treated as declared grid connection or current path; nearest generator incorrectly treated as supply to a data centre;
- GeoJSON lines crossed or shared substation point incorrectly treated as electrical junction/switch status; different-voltage circuits joined without a published transformer; duplicate mirrored landings counted as duplicate circuits; parallel circuits lost through deduplication;
- ETYS planned upgrade, line rating, fault current or connection queue mistakenly shown as available headroom/energised circuit;
- ETYS winter/summer scenario or NESO day-ahead boundary net forecast labelled present actual circuit MW; Elexon BMU energy/notifications injected into an unrelated DNO feeder;
- UKPN primary transformer arrow rendered when its directional polarity has not been resolved or when data redacted; positive measured current treated as directional;
- An underground cable shown with exact bends solely because it has endpoint coordinates; offshore interconnector straight chord shown as surveyed seabed alignment;
- Lightning optical flashes presented as confirmed ground strikes or causal proof of asset damage;
- Ambiguous site identity, orphaned node, unknown coordinates, missing licence/blocked API or incomplete source data silently replaced with estimates;
- Unbounded DFS on cycles, invisible backtracking/teleportation, misleading 100% coverage including disconnected components, excess animation against reduced-motion preference;
- A new GridAtlas cartridge breaks existing MAP/deep links/Offtakers/Lightning, leaks event listeners, changes the homepage shell or production current manifest without owner release authority.

A technical educational caption should be permanently accessible: **“Journey shows documented network connectivity. The travelling light is a learning cursor, not measured current or a power-flow simulation. Dotted links are schematic; missing routes are not invented.”**

## 8. Deliverable contracts, quality dashboard and change control

Each GJ milestone PR must attach (a) authoritative input SHA and licence manifest, (b) code diff/functions affected, (c) positive/negative fixtures and test run URLs, (d) counts of eligible edges, mapped polylines, topology-only links, ambiguous/unlocated nodes and excluded edges, (e) manual source review samples, (f) desktop/mobile/browser observations, (g) before/after UI and memory/size budgets, and (h) rollback instructions. A nonzero unknown count is honest; zero unknowns without provenance is suspect.

The five-version Pipeline News proposals need their separate publication receipts in #45. Grid Journey progress/coordination belongs in #42 or a new dedicated GridAtlas issue opened by the owner. **Do not edit existing authoritative scope files or overwrite the 17 November commits; cross-reference them.** Nothing in this document authorises code deployment, publication, changes to source licences, paid/paywalled scraping or the assertion that a live source-backed circuit path exists between arbitrary mapped locations.

## 9. Official research references checked

- NESO [ETYS 2025 Appendix A/B/C and date catalogue](https://www.neso.energy/research-publications/etys/documents): 30 June 2026 official release; B carries connectivity/parameters, C future scenario power flow.
- NESO [Day Ahead Constraint Flows and Limits](https://www.neso.energy/data-portal/day-ahead-constraint-flows-and-limits) and [field documentation](https://www.neso.energy/data-portal/day-ahead-constraint-flows-and-limits/day_ahead_constraint_flows_and_limits): boundary `Flow_MW` calculated day-ahead, defined positive arrows, data/snapshot updates and April 2024 method change; not real-time per-circuit.
- UKPN [Primary Transformer Historic Half Hourly — SPN](https://ukpowernetworks.opendatasoft.com/explore/assets/ukpn-primary-transformer-power-flow-historic-half-hourly-spn/): explicit inconsistent directionality, current non-directionality, redaction/privacy, manually joined LTDS↔operational records and discrepancies between planning diagrams and operational switching.
- [Elexon API endpoints](https://bmrs.elexon.co.uk/api-documentation/endpoint), [interconnector flows](https://bmrs.elexon.co.uk/interconnector-flows); inspect each endpoint's time/sign semantics, corrections and rights before adapter acceptance.
- [GridAtlas code/manifest and offtaker source documentation](https://github.com/Ventusltd/gridatlas/blob/main/docs/OFFTAKERS-SOURCE.md); [Ventus electrical graph code](https://github.com/Ventusltd/ventus-grid-engine/blob/main/engine/network-topology.js); [shortest-hop code](https://github.com/Ventusltd/ventus-grid-engine/blob/main/engine/electrical-distance.js); [data-grid-gb](https://github.com/Ventusltd/data-grid-gb).

**Status at commit:** Research + schedule only. No implementation branch created; no CI claimed; no current.json / homepage / live release change.
