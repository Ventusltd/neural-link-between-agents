# Ventus Grid Engine 2.0 — Grid Journey on the real GridAtlas

**Date:** 17 November 2026. **Type:** independent source/code study and prototype scope. **Status:** NOT IMPLEMENTED OR PUBLISHED. No live GridAtlas, Pipeline News, Lightning, Kuiper, homepage or release pointer changes requested or authorised by this document.

## Owner concept

A minimal on-map neon pulse travels across all traceable electricity-network branches inside a selected geographic region. Think London Underground map, train journey, taxi or walk: substations are stations, public circuits are lines, transformers are the voltage-change interchange, and REPD solar, batteries, data centres and potential offtakers are nearby destinations. No train vehicles or fictional map. The real GridAtlas GIS is the only visual ground plane; actual available circuits govern any true electrical journey.

The existing Vicinity **30/30/30** logic is the discovery guide, NOT a 90-edge electrical network. GridAtlas offtaker source tools/offtakers/src/06b-dc-engine.js finds up to 30 substations >=33 kV and 30 REPD projects within 40 km, plus the 30 nearest conventional power sites at any distance (conventional lines drawn up to 100 km). A generic offtaker tap can also list 15 REPD sites and five substations. These Haversine screening spokes must **never** be silently promoted to source-supported electrical circuits.

## Existing verified architectural building blocks

1. **Ventus Grid Engine graph maths:** ventus-grid-engine/engine/network-topology.js exposes graph(), edgesAt(), nodesOfSite(), declared node voltage, source circuit/transformer identity, with planned-change edges excluded from present-day traversal. The extracted electrical-distance.js already provides between() (breadth-first fewest hops) and within() (hop-limited reachability), and rejects a circuit that changes declared voltage without a transformer. Proofs/electrical-distance.proof.mjs tests multihop travel, invalid voltage transitions and source-bounded semantics. Reuse these functions unchanged; create separate pure route-tour module.
2. **Actual network model:** data-grid-gb/derived/gb-transmission-network.v1.json with 921 sites, 2,679 nodes, 1,392 circuits, 1,472 transformers and 2,230 planned changes. Browser-sized connection-points.v3.json contains 886 sites >=132 kV; 489 geolocated by separately qualified OSM join, 397 unlocated. ETYS topology does not supply full GIS cable/OHL centreline or confirm connection headroom. This source has different coverage from the 33 kV+ Vicinity set. Do not invent geographic positions or join a 33 kV point to an ETYS busbar by proximity.
3. **Live GridAtlas:** atlas/current.json inspected generation 202611161720 with substation-intelligence, sld-sandbox, uk-lightning-overlay and uk-offtakers-overlay cartridges, plus map and loader modules. SLD already has animated neon/SCADA links and nearest-substation search. Offtaker overlay already draws native MapLibre GIS LineStrings, points and rings. Add an optional independently versioned Grid Journey cartridge; do not enlarge/rewrite the already large base SLD cartridge or alter historical generations.
4. **Kuiper and prior SLD visuals:** globalgrid2050/kuiper-grid/drawing/README.md, whole-site-routes.js and whole-site-route-view.js show native canvas, FIRE/string geometry, circuit selection, route highlighting and provisonal simulated layouts. energy-transition-simulator/202610290235/mod/engine/journey.mjs implements go substation 132 and next substation, but travels to geographically nearest substations rather than along proven electrical edges. Reuse tested animation/display conventions, not synthetic LV/MV plant assumptions. A standalone production-grade Faraday Pulse module was not independently identified in this code survey; require a concrete path and tests before promising integration.
5. **Lightning:** Ventusltd/lightning holds actual EUMETSAT MTG optical flashes, one-year coverage-aware history and a GridAtlas layer. These are not verified ground strikes. Use an optional separate historical or near-live environmental overlay, with source-collection coverage, not an assertion of circuit damage or fault propagation.
6. **Existing corridor research:** data-grid-gb/docs/routing/METHOD_AND_LIMITATIONS.md and LEGACY_LAYER_AUDIT.md explicitly separate approximate spatial screening from real cable design. Old GIS lines may lack junction identity, grade separation, access and survey data; intersecting polylines do not establish an electrical junction.

## Journey modes and precise meaning of ALL ROUTES

**Mode 1 — Follow every known branch (first priority):** Select an ETYS graph site or source node. Build a bounded source-supported connected subgraph, subject to explicitly defined radius (initially 40 km), selected voltage filter and optional max-hop/edge budget. Breadth-first search records reachable hop tiers; a deterministic depth-first **edge-cover traversal** then moves the neon cursor down each legal unique edge, returns along traversed edges to branches, explores loops and parallel circuits, and stops at data boundaries. Count each source edge once, even if animation uses it twice on a return trip. Order branches by hop tier, declared voltage/transformer type, mapped geographical distance where available and stable source ID. This is an **educational ordering**, not actual current direction or switching order. All simple paths are exponentially numerous in a meshed network and must not be promised; instead show all edges discovered within the bounded subgraph and publish edge/branch coverage.
 
**Mode 2 — A to B:** Reuse electrical-distance.between() for shortest published hop-count path, with optional later K=3–5 distinct alternatives and strict time/hop limits. Hop count is not kilometres; no headroom, load flow, fault current or connection approval inferred.

**Mode 3 — Vicinity 90 exploration:** Start from a data centre, offtaker or REPD project and reveal existing 30/30/30 groups. A dotted exploratory jump to a user-selected nearby geolocated ETYS transmission node is geographic navigation, **not an electrical edge**. Only after selecting a source-identified busbar/node does Follow Grid begin. Conventional sites outside 40 km remain explicitly marked as outside, not magically in-radius.

**Planned versus existing:** Planned changes may appear ghosted for teaching but are never traversed as current circuits. Transformer edges may legitimately change kV; circuits that appear to change declared kV without a transformer are refused. Source model gaps, isolated nodes, uncertain geometry and unsupported DNO levels are labelled, not hidden.

## Real GIS vs graph shape

Two separate graph dimensions must meet before the map draws a solid traversable real circuit alignment: (a) ETYS/source-approved electrical node/edge identity, AND (b) a source-linked spatial line geometry matched to that exact circuit. Where topology is published but the line geometry is unavailable, draw only an optional **dashed schematic endpoint connector over the real GIS**, labelled clearly as not the actual cable/OHL alignment. If either endpoint has no approved location, retain the electrical hop in the route ledger as unlocated, without an invented GIS segment. At the geographic boundary show truncated/beyond-radius branches, not a claim that power stops at the circle. A substation's OSM point proximity alone does not attach a nearby line.

## Minimal native interaction

Existing GridAtlas site card gets one action **JOURNEY**. Tiny mode selector Explore / Follow Grid / A-B, origin, radius, kV band, auto/next/back/clear. A single neon cursor moves across actual verified GIS geometry when present and across clearly dashed schematic connectors otherwise. Reached branches remain faint and completed unique edges are counted. Existing MapLibre map, original controls, search, layer toggles, MAP deep links, Lightning and off-taker cards must continue functioning. Minimal bottom sheet displays current source node, named voltage, path category, circuit/transformer type, source and location precision. No separate metro-style schematic should replace the GIS. Respect reduced-motion, keyboard, iPhone touch, landscape and screen-reader content.

Kuiper/wafer lens is an optional later drill-down to show one selected node/edge or illustrative SLD, not a dependency for Grid Journey 1.0. A physics-driven Faraday pulse, flow calculation, impedance aggregation and fault-level model require separately reviewed input/model validation and must not be implied by a travelling neon dot. Lightning optical events may be visually co-located but cannot assert equipment strike or damage.

## Isolated code ownership and proof

**ventus-grid-engine**: proposed pure journey/graph-adapter.mjs and journey/edge-tour.mjs accepting existing typed graph, returning immutable ordered steps with route/edge/source provenance and counts. Existing electrical-distance and network-topology remain read-only first pass.

**data-grid-gb**: versioned, licence-qualified geographic site and circuit geometry mapping. Record geometry kind real_mapped, schematic_endpoints, unlocated or not_available, with stable IDs and source digest. No inferred physical line from random polylines.

**gridatlas**: one preview-only map cartridge plus MapLibre lines/markers and concise status panel; no live/current.json pointer changes during R&D.

**Kuiper and lightning**: optional independent render components/layers, no source-of-truth authority over grid circuit identities.

**Neural Link**: this research note, issue handoffs and exact-CI acceptance only; no claim it wakes or starts agents. Ventus Grid Engine 2.0 is a proposed **separate engine major release**, not a reserved Pipeline News V9.34+ identifier.

### Adversarial tests required before a public demonstration
- All unique circuits visited exactly once even if the animated walk backtracks; parallel circuits not collapsed; loops and disconnected branches handled; stable deterministic order under input shuffle.
- Synthetic test with legal 400->132 kV transformer and illegal 400->132 kV circuit; no crossing where GIS lines touch; no 33 kV source topology invented.
- Planned edges excluded, incomplete source information returned as unknown, map geometry missing but graph still supported, radius boundary correctly labelled, source/licence/coordinate join traceable.
- Start from all three Vicinity groups and prove that 30/30/30 screening lines do not become circuit connectivity. Also 0, 1 and 90 candidates.
- Playwright touch 390/393/1440 and rotation, button first-tap, controls/scroll, no-GIS-geometry labels, reduced-motion, existing map/Lightning/Offtakers coexistence, no severe performance or memory leak.
- Prove exact-source hashes, deterministic Python/Node output and source rights; physical device sign-off distinct from emulation.

### Bounded prototype
Choose a small real **source-indexed** GB network region with a branch, loop and transformer where ETYS nodes and acceptable map coordinates are actually available. Derive a deterministic tour and render it over a previewed native GridAtlas. If exact circuit GIS lines cannot be matched, demonstrate with honestly dashed topology chords instead of implying an existing cable alignment. Never create a synthetic real-world grid link to make the demonstration pass.

**Sources (repositories):**
https://github.com/Ventusltd/ventus-grid-engine
https://github.com/Ventusltd/data-grid-gb
https://github.com/Ventusltd/gridatlas
https://github.com/Ventusltd/globalgrid2050
https://github.com/Ventusltd/kuiper-belt
https://github.com/Ventusltd/lightning

**Conclusion:** feasible as a source-constrained GIS graph walk and educational neon journey, with existing substantial code reuse. It is not feasible to claim every physical UK cable route, 90 genuine connections, real power-flow direction, spare grid capacity or complete GIS circuit centreline from the current publicly mapped data.
