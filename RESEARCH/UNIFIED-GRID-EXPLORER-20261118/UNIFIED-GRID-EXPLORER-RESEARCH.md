# Ventus Unified Grid Explorer — research synthesis and implementation brief

**Date:** 18 November 2026  
**Status:** RESEARCH DELIVERABLE — for independent technical review; **not** product acceptance, a release, proof of licensing, or an engineering calculation.  
**Coordination:** [NL-042](https://github.com/Ventusltd/neural-link-between-agents/issues/42) · [Dedicated research lane NL-064](https://github.com/Ventusltd/neural-link-between-agents/issues/64) · [Draft PR 63](https://github.com/Ventusltd/neural-link-between-agents/pull/63).  
**Scope:** Read-only review of existing Ventus projects plus proposed contracts/architecture. Product repositories, agents' branches and release pointers have not been altered by this study.

## 1. Executive finding

Ventus already has the components for an evidence-labelled **Grid Journeys** interface: REPD/project locations and geographic layers in GridAtlas; official GB transmission topology and equipment parameters in data-grid-gb; canonical geodesy and deep-link contracts in ventus-grid-engine; Elexon historical time series in data-gb-electricity; a bounded DNO/TSO source registry; source-qualified data-centre features; and a lightning overlay. These must be integrated through **small, versioned contracts** rather than reimplementing their mathematics or treating a nearby substation as a connection offer.

The first usable product should let a visitor pick any real project, substation or map point; vary a **shared geographic vicinity radius from 1 to 50 km in exactly 1 km steps**; show available source-qualified assets and voltages; open origin-to-destination journeys; trace *documented* electrical graph edges if topology and geometry support them; and create isolated illustrative scenarios. It must clearly separate four classes of claims:

1. **Observed/official asset facts**: cited records, original identifier, collection date, license and quality state.
2. **Geographic statements**: distances and within-radius membership, with CRS/method and geometry uncertainty.
3. **Electrical topology statements**: documented node/edge adjacency and ratings, not a solved operating state.
4. **Hypothetical or illustrated outputs**: user additions, inferred geometry, explanatory pulses and possible routes.

A physical connection, available capacity, actual circuit route, power-flow direction, transient response or planning consent must **never** be inferred from proximity, a diagram or an unsolved network graph.

## 2. Evidence inventory — source-to-role matrix

The table distinguishes **verified repository documentation** from **candidate reuse**, and does not pretend README references prove a deployed import or live test. Linked files were freshly read through the connected GitHub service for this handover; a complete code-level dependency audit and current source-head pinning remain follow-up actions.

| Component | Located source | Supported observation / candidate role | Qualification |
| --- | --- | --- | --- |
| GridAtlas V9 | [README](https://github.com/Ventusltd/gridatlas/blob/main/README.md), [atlas/coordinate-systems.json](https://github.com/Ventusltd/gridatlas/blob/main/atlas/coordinate-systems.json) | DESNZ REPD, offshore/geodetic reconciliation, browser arrival and map/cable-engine composition; evidence-gated project identity | DOCUMENTED. Review deployed generation, engine composition and versioned manifests independently. |
| Ventus Grid Engine | [README](https://github.com/Ventusltd/ventus-grid-engine/blob/main/README.md), [engine/](https://github.com/Ventusltd/ventus-grid-engine/tree/main/engine), [deeplink/contract.js](https://github.com/Ventusltd/ventus-grid-engine/blob/main/deeplink/contract.js) | Pure distance/area/geodesy/nearest-search, deep-link builder/parser, compute receipts, proofs; first-choice reuse rather than rewriting geometry | DOCUMENTED. Engine explicitly says deployed callers do not automatically import its modules. |
| GB transmission data | [README](https://github.com/Ventusltd/data-grid-gb/blob/main/README.md), [connection-points.v3.json](https://github.com/Ventusltd/data-grid-gb/blob/main/derived/connection-points.v3.json), [network.v1.json](https://github.com/Ventusltd/data-grid-gb/blob/main/derived/gb-transmission-network.v1.json) | ETYS-derived identity, substations, buses, circuits, transformer and fault/rating records. README reports 886 sites in connection-point product, 489 spatially located and 397 unlocated; larger topology product has 2,679 nodes, 1,392 circuits, 1,472 transformers | DOCUMENTED dataset counts, **not** rerun numerical audit. Product states it is NOT a solved load-flow case. |
| GB electricity time series | [README](https://github.com/Ventusltd/data-gb-electricity/blob/main/README.md), [DATA_SOURCES.md](https://github.com/Ventusltd/data-gb-electricity/blob/main/DATA_SOURCES.md) | Elexon FUELINST, FUELHH and price series; partitioned Parquet with explicit keys; layer for *national/market context*, not individual circuit flows | DOCUMENTED. Great Britain, **not all UK**; preserve provisional versus settled statuses. |
| DNO/TSO operator catalogue | [README](https://github.com/Ventusltd/data_uk_dno_and_tso/blob/main/README.md) | Operators, network areas, source registry, schema/audit tooling; first stage is declared-only and manually gated | DOCUMENTED; **not** proof that distribution feeder topology or automated live feeds already exist. |
| UK data centres | [README](https://github.com/Ventusltd/data-centres-gb/blob/main/README.md), [docs/data-sources.md](https://github.com/Ventusltd/data-centres-gb/blob/main/docs/data-sources.md) | OSM/Overpass source records, Parquet and GeoJSON; a local FastAPI read service can expose intentionally installed generations | DOCUMENTED; facility identity, owner, capacity and connection must remain unknown without separate proof. Source does **not** scrape Data Center Map; that source is expressly excluded. |
| Lightning | [README](https://github.com/Ventusltd/lightning/blob/main/README.md), [data/uk_lightning.geojson](https://github.com/Ventusltd/lightning/blob/main/data/uk_lightning.geojson) | EUMETSAT optical-flash overlay and UTC coverage/history metadata | DOCUMENTED. Flashes are **not** verified ground strikes; missing coverage is UNKNOWN, not zero. |
| Homepage and Pipeline News | [globalgrid2050](https://github.com/Ventusltd/globalgrid2050), [globalgrid2050-homepage](https://github.com/Ventusltd/globalgrid2050-homepage) | Distinct publishing and consumer/version surfaces; REPD and candidate intelligence can link to map journey | KNOWN estate boundary; latest publication heads must be checked separately. No edit in this research lane. |
| Kuiper / Vogel | [GlobalGrid2050 public site](https://globalgrid2050.com/) and [research intake](./START-HERE.md) | Optional educational schematic/star layout; keep it as a non-geographic view with explicit labels | PROPOSED REUSE. Executable module, coordinates, dependencies and reuse rights need code-level confirmation. |
| Faraday pulse | [Ventus Grid Engine site](https://ventusltd.github.io/ventus-grid-engine/?graph=federation) | Educational network-traversal animation concept | UNVERIFIED library/API. Do not represent the animation as measured current, electrical propagation or load-flow. |
| Solar Design Studio | [GlobalGrid2050 public site](https://globalgrid2050.com/) | Separate terrain and solar design workflow; potential deep link from user-created solar node | PROPOSED INTEGRATION. Do not duplicate its geometry kernel before inspecting real files/tests. |

**Newly confirmed correction to the Deep Research text:** the earlier draft characterised data-centres-gb as scraping Data Center Map; its repository README says the opposite, and specifically prohibits copying that source into the database. Another earlier draft suggested MIT/Apache software licences or public availability confer rights to source data; **they do not**. The same draft underweighted the existing reusable grid engine; its README identifies concrete APIs and tests. This committed version takes the repository documentation as the stronger available evidence.

**Source tracking rule:** Before writing adapters, record each repository's current commit SHA, the exact input dataset release/hash, the file path and schema version in an immutable evidence matrix. A README blob SHA or a dated command checkpoint is **not** the latest repository commit SHA. The older NL-042 overnight tracker contains dated historical source baselines and must not be mistaken for current live state.

## 3. Intended user experience

The common beginner-to-engineer flow is: **Search/select origin → adjust radius → inspect real assets and provenance → choose destination → compare documented pathways → optionally add an isolated hypothetical asset or line → export/share an explicitly labelled result**.

At a minimum:

- Origin types: REPD project, transmission substation, evidence-qualified distribution site, data centre/offtaker or arbitrary coordinate. A feature without valid coordinates may appear in the registry but must not silently map at [0,0] or disappear from non-map search.
- Exactly one source of truth for **radius_km**: integer 1…50, default set by the host product only after review. Map circle, asset search, voltage filters, origins, paths and result counts must carry this same value in shared state.
- Radius means **geographic distance from the selected origin**, not travel distance, cable length, reach of an electrical connection, tariff zone or capacity. The map may show a line crossing the boundary, labelled as a clipped/partial feature rather than a wholly contained circuit.
- User-selectable voltage levels are filtered from **recorded** levels, never guessed from a line's appearance.
- Path types: (a) straight-line/geodesic proximity, (b) surveyed or mapped geometry where licensed and attributable, (c) documented graph path with known edge IDs, and (d) invented user scenario. A route must carry its **path_kind** visibly.
- Layperson view: nearby substations/lines and what is known. Advanced view: bus/transformer transitions, multiedges, source limitations, parameters, scenario deltas and export receipts.
- Mobile: address the actual tap → arrival → project identity → real engine calculation → visible result journey; hiding a computed result under a minimised card is an acceptance failure. Test 390/393 px, portrait/landscape and Back. Use keyboard and screen-reader labels and a reduced-motion mode.
- The **Grid Journeys — exploring the patterns of energy** branding and neutral non-military language remain compatible with NL-042 direction.

## 4. Proposed canonical contract and data model

A spatial feature and a topological element are different things. The unified model should keep original source keys, licence and uncertainty alongside any cross-repository identity match.

### Canonical Asset v1 (illustrative, not a released schema)

~~~json
{
  "schema": "ventus.asset.v1",
  "id": "urn:ventus:repd:12588",
  "source_identity": {"system": "DESNZ_REPD", "key": "12588"},
  "asset_type": "generation_project",
  "name": "Example project (not a live data assertion)",
  "point": {"crs": "EPSG:4326", "lon": null, "lat": null},
  "geometry_status": "unknown",
  "voltage_kv": null,
  "capacity_mw": null,
  "connection_node_id": null,
  "connection_evidence_state": "unverified",
  "provenance": {
    "source_url": null,
    "source_record_id": "12588",
    "retrieved_at_utc": null,
    "dataset_generation": null,
    "sha256": null,
    "licence": null,
    "rights_status": "review_required"
  }
}
~~~

Null is **unknown/unavailable**, never zero. Use externally stable keys, preferably namespaced rather than a fabricated universal UUID. The above ID demonstrates a format only; it does not assert that the example's capacity, coordinates or grid connection are known. Country and GB/NI jurisdiction should be explicit on records, since Elexon GB series do not describe Northern Ireland.

### Edge and topology distinctions

- **Asset**: project, substation, data centre, industrial demand or weather observation, each with provenance.
- **Electrical node**: busbar/bay or transformer terminal with known voltage and operator identifiers where documented.
- **Electrical edge**: distinct circuit/transformer with documented endpoints, parameters and status; parallel circuits remain separate edges.
- **GeoFeature**: Point/LineString/Polygon geometry, quality and CRS; not itself a claim of electrical connectivity.
- **Identity match**: source-key pair plus deterministic matching method and reviewed confidence/evidence; fail closed on ambiguities.
- **Scenario delta**: add/disable/change a hypothetical node/edge, preserving underlying immutable source graph unchanged.
- **Computation receipt**: inputs, source generations, algorithm version, result, unsupported flags and completion state.

An edge's documented electrical terminals may exist without public route geometry; a mapped overhead line may exist without confirmed terminal mapping. Do not connect them simply because endpoints are visually close.

### Shared journey/query contract v1 — PROPOSED

Retain compatibility with the NL-042 overnight shared-entry vocabulary: **journey=vicinity**, **origin_type**, **origin_id**, **latitude**, **longitude**, and integer **radius 1–50 km**. Any renaming must be owned and tested jointly by the emitter and receiver.

~~~text
GET /v1/vicinity?origin_type=repd&origin_id=12588&radius_km=15&voltage_kv=132,275,400
GET /v1/journey?from_id=urn:ventus:node:A&to_id=urn:ventus:node:B&mode=documented_topology
POST /v1/scenarios/evaluate
~~~

These are **design sketches, not a claim that production API endpoints exist**. For browsers statically hosted on GitHub Pages, build-time materialisation plus local indexes and deferred layers may be cheaper and safer than a new authenticated REST backend. Introduce a server only when profiling or source update requirements demonstrate a need.

**Required responses:** schema_version, input echo, source_generation(s), feature/edge IDs, path_kind, calculation_kind, evidence_state, provenance, warnings, missing_data, and is_complete. For unsupported graph path, return a typed **NO_DOCUMENTED_PATH_IN_AVAILABLE_DATA** rather than inventing a straight-line electrical edge.

### Radius semantics / coordinate accuracy

The established Ventus Grid Engine intentionally retains its deployed WGS84-radius constant for compatibility, and documents alternatives and errors in [its README](https://github.com/Ventusltd/ventus-grid-engine/blob/main/README.md). **Do not silently change deployed distance mathematics.** Select and version one exact distance convention for radius membership, use existing geodesy functions, and explicitly test boundary conditions. Local EPSG:27700 planar geometry may serve UK metric geometric operations if transformed with a documented method; it is not interchangeable with the existing spherical-distance method at thresholds without measured discrepancies. Geometry and representative-point uncertainty often dominate small differences between sphere constants.

For line geometry crossing the radius, use the actual polyline-to-centre distance/intersection (not merely one endpoint) and distinguish 'intersects vicinity' from 'endpoints within vicinity'. A corridor/route label is conditional on traceable source geometry.

## 5. Topology tracing and computation boundaries

A source-confirmed **multigraph** is the correct base: real electrical buses/nodes, circuit/transformer edges, parallel edges preserved, disconnected components retained, and switching/status unknowns left explicit.

- Offer **hop count** and, where all required attributes are present and units/transformer handling are unambiguous, **edge-weighted** exploratory path comparisons. Do not imply the path is energised, available for connection, or the direction electricity currently flows.
- Publish edge-list completeness and topology coverage. A route traversing undocumented gaps must stop and explain missing evidence. Never fill a missing feeder by nearest-neighbour geometry.
- Only use impedance-weighted labels if the edge parameters genuinely mean comparable engineering quantities: the data-grid-gb topology states an R/X/B **100 MVA base**, which is not interchangeable with ohms/km without appropriate base, voltage and unit transformations.
- Scenario engine starts with **graph edits** (hypothetical circuit, substation, transformer, generator/storage/load). Every scenario uses an explicit user assumption ledger and is logically separate from official assets. Recompute adjacency and route display; do not calculate thermal security, protection coordination, voltage profile or power flow until a separately validated solver has the required switching, injections, demand, base quantities and boundaries.
- An optional moving 'train' or pulse along selected line segments is **illustrative tracing only**. Require reduced-motion support and the on-screen caption 'Illustrative journey — not measured current or power flow'.

## 6. Data-centre and other offtaker integration

Treat a demand facility as an independent asset class with source record IDs, operating/planned status, parent-campus uncertainty, proposed MW versus contracted/observed MW as separate fields, and a typed connection_evidence_state. The OSM facility record might identify a building but **does not necessarily establish the owner, a megawatt demand, a UK transmission entry point or a valid electrical relationship**.

Source safeguards:
- Use OSM-qualifying source records only as allowed by their terms; [data-centres-gb README](https://github.com/Ventusltd/data-centres-gb/blob/main/README.md) says Data Center Map is excluded because its terms prohibit scraping and external-database copying.
- Preserve OSM element grain instead of automatically merging elements into operating facilities.
- Display unknown capacities as UNKNOWN. Never use zero as a placeholder.
- A distance to 15 nearest projects is a *geographic association*, not a verified power purchase agreement, point of connection or corporate identity.
- Candidate REPD/news links must remain candidate until independently source-matched.

## 7. Auxiliary components and rights

**Lightning:** use an optional optical-flash layer with query window, UTC coverage, archive index and attribution. Its optical positions are not proven ground impacts or site-specific risk measurements.

**Kuiper/Vogel:** evaluate optional educational schematic reuse only after inspecting actual module code, attribution and licensing. The London 'tube'/'sunflower' diagram may be topologically instructive but is not a cartographic corridor and must never displace the real geographic map. Keep its visual transform reversible and separate from WGS84 geometry.

**Faraday:** educational pulse visual only until a reusable source-verified module and validated engineering interpretation are found; no claim to solve transients.

**Solar Design Studio:** use a deep link to a distinct detailed design tool in first iteration; treat generation in explorer as a point/area asset with capacity and source, not a substitute for string configuration, geotechnical layout or engineering assurance.

**Rights table — critical correction:** an Apache-2.0/MIT repository **code** licence never by itself establishes rights to redistribute its upstream NESO, DESNZ, OSM, satellite, publisher or vendor data. OSM data are **ODbL 1.0**, not CC BY-SA; maps/tiles and imagery have separate licensing/attribution conditions. Government datasets may have OGL or other terms, but verify the precise product and revision. Even publicly readable DNO records can have different reuse constraints. Store source_url, exact rights statement, retrieval date, derivative status and publication eligibility per layer. Withhold unlicensed data instead of assuming source visibility permits copying.

## 8. Implementation architecture

Recommended initial architecture: **version-pinned, static-first source products + explicit normalization/adapters + geospatial/graph indexes + one browser-visible Journey controller**, with an optional read-only service added only if required. Preserve the existing MapLibre/GitHub Pages surfaces, edition immutability, single publisher and tested deep-link paths rather than starting with an unrelated UI rewrite.

~~~mermaid
flowchart LR
  subgraph Sources
    REPD[DESNZ REPD]
    ETYS[NESO ETYS / data-grid-gb]
    DNO[DNO and TSO source register]
    DC[OSM data-centre features]
    TS[Elexon / GB time series]
    WX[EUMETSAT lightning]
  end
  subgraph Build["Pinned and audited build"]
    A[Source fetch + hashes + rights]
    N[Canonical asset/geometry adapters]
    G[Typed multigraph + spatial index]
    V[Contracts + deterministic validation]
  end
  REPD --> A
  ETYS --> A
  DNO --> A
  DC --> A
  TS --> A
  WX --> A
  A --> N --> G --> V
  subgraph Web["Existing GridAtlas / Pipeline News presentation"]
    O[Origin + 1-50 km radius]
    M[Geographic map + source states]
    J[Journey + source-qualified alternatives]
    S[Illustrative scenario overlay]
  end
  V --> O
  O --> M
  O --> J
  J --> S
~~~

~~~mermaid
sequenceDiagram
  participant U as User
  participant PN as Pipeline News
  participant A as GridAtlas receiver
  participant D as Shared geodesy/topology adapter
  U->>PN: Select REPD asset / JOURNEY
  PN->>A: Versioned deep link + identity + radius
  A->>A: Validate coordinates/identity
  A->>D: Query within radius and optional topology path
  D-->>A: Sources, geometry, results, warnings, missing evidence
  A-->>U: Real map, source states and visible result
  U->>A: Change radius / select alternative
  A->>D: Requery using same origin/radius contract
  D-->>A: Updated evidence-labelled result
~~~

For performance, establish baseline budgets (not unsupported success claims): benchmark mobile cold/warm load, 1/10/50 km queries, worst-case dense area, pan/zoom, cross-browser animation, map memory, bytes transferred, slow 4G, and topology path search. Use compact derived JSON/GeoJSON, Parquet in offline production, vector tiles where warranted, source generation caching, worker-based heavy spatial operations, and progressive layer fetch. A 50 km circle is not guaranteed to contain 'only a few hundred' objects in London; measure actual density and enforce feature/byte limits with an explicit 'refine selection' state.

## 9. Dependency-ordered delivery / exclusive ownership proposal

These are **future work packages**, not tasks assigned to current workers without their command leads' agreement.

| ID | Deliverable | Dependency | Proposed owner / acceptance |
| --- | --- | --- | --- |
| R0 | Exact source-head/commit/paths/licence and current release inventory | None | Independent evidence auditor. Verify branch, current served state and upstream rights. |
| R1 | Asset + edge + provenance JSON Schema and identity rules | R0 | Data-contract owner. Validate fixtures including null, duplicate, unlocated, ambiguous match and cross-GB/NI cases. |
| R2 | Lock radius and shared deep-link contract against existing engine | R0–R1 | Grid Analyser + Train Conductor together. Boundary, invalid coordinates, 1/50 km, URL round-trip and Back tests. |
| R3 | Data adapters with never-overwrite, provenance-preserving outputs | R1 | Existing data owners. Deterministic outputs, schema diff, hashes, rights and missing-value receipts. |
| R4 | Spatial/context query and map source states | R2–R3 | Train Conductor's GridAtlas lane when allocated. Radius consistency, geometry intersections, filters and mobile. |
| R5 | Electrical multigraph journey and alternative path explorer | R3–R4 | Grid engine / independent graph QA. Parallel edges, disconnected topology, transformer transitions, no invented paths. |
| R6 | Data-centre/offtaker and official grid-change context | R3–R5 | Data-centre / Grid Intelligence owners. Source and operating-state review, no inferred connected MW. |
| R7 | Isolated hypothetical scenario editor + educational animation | R5 | Separate scenario owner. Undo/redo, no source mutation, assumptions, reduced motion, never measured-flow labels. |
| R8 | Cross-product publication/rollback acceptance | R2–R7 | Single designated publisher plus independent reviewer. Live deep link, served source hash, device QA and historical URL preservation. |

Test matrix should include: 1/50 km boundary and step=1; REPD with and without coordinates; a substation named ambiguously across sources; location geometry without known terminals; a circuit with no geometry; crossing line; two parallel edges; transformer voltage transition; a disconnected island; unknown switch state; null demand; unlicensed source; wrong EPSG; staged versus served version mismatch; browser Back, keyboard and mobile collapsed panel; lightning unsearched period; changing radius during an in-flight query; no internet; user scenario export/import and rollback.

**Completion states:** SOURCE VERIFIED → CONTRACT TESTED → INTEGRATION TESTED → INDEPENDENT REVIEWED → RELEASE APPROVED → PUBLISHED → PUBLIC READBACK VERIFIED. A green isolated test is not evidence of a successful public edition. Do not conflate research merging with product publishing.

## 10. Phases and risks

**Phase A — protect and inventory.** Read current agent ledgers and target repos; pin exact sources and licensed data; freeze schema/URL semantics. No changes to published editions.

**Phase B — connect minimum viable Grid Journey.** One origin, 1–50 km shared radius, source-aware substations/circuits/offtakers, visible spatial result, optional documented graph path, mobile MAP→JOURNEY parity.

**Phase C — add advanced topology and context.** Multigraph alternatives, transformer and circuit metadata, upstream development notices, time-series context (not site flow), confidence/coverage panels, typed data-centre links.

**Phase D — add sandbox learning.** Hypothetical elements, comparison views, exportable assumptions and optional Kuiper/Faraday-like illustration, with distinct 'schematic' and 'measured' language.

**Phase E — validate scale and quality.** Benchmarks, accessibility, property-based graph/geodesy tests, legal review, data freshness, release/rollback and independent acceptance.

Principal risks: confusing proximity with electrical connection; using data of unconfirmed reuse rights; treating incomplete topology as a closed network; silently diverging from deployed geodesy; confusing 100 MVA-base per-unit quantities with route ohms; associating OSM elements with companies/loads without evidence; conflating national time-series demand with a feeder; mobile result visibility and stale deep links; duplicated code/branch ownership; and treating an animated line as a physical power flow.

## 11. Codex / agent handover

Read [the dedicated Codex monitoring file](./AGENT-LANE-AND-CODEX-MONITOR.md), [NL-064](https://github.com/Ventusltd/neural-link-between-agents/issues/64), [NL-042](https://github.com/Ventusltd/neural-link-between-agents/issues/42) and [PR 63](https://github.com/Ventusltd/neural-link-between-agents/pull/63). Report all exact source/head/CI gaps before implementation; independently reconcile the current product state, source code and licences. A GitHub issue is a mailbox, not a persistent executing agent.

**Research acceptance status:** The report and Mermaid diagrams are committed as a **research synthesis**. Full code-path dependency verification, source revision pinning for every repo, independent licence sign-off, simulation suitability and integration testing **remain open**. PR #63 stays draft, for owner/agent review. This study does not certify the product, change any live source, grant publication authority or assert any current electricity network condition.
