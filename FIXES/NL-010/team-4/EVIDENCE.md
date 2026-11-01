# NL-010 Team 4 EVIDENCE (steps 7–8, "the OS of the estate, baby steps") — FABLE-T4B

Written 1 Nov 2026 before STEPS.md existed. Every claim below carries a key `repo@sha path:line`; where a fact is an
absence (no licence file) the key is the command that measured it. Repositories are the clones under
`/home/user/estate/` at these heads (all equal to `origin/HEAD` where checked):

| repo | sha | notes |
|---|---|---|
| elements | f7a92fb085c38dcbbd5cb469a66cd5ca61fb95bf | `git ls-remote origin HEAD` = same sha; full history |
| testcode | d09c185c8dacbc5c73afb2b0d0d8dad40745a544 | full history |
| kuiper-belt | 018b46aed50f28f7b1882a0dcaba6593ce522beb | Edition 4 head, as the harness notes say |
| globalgrid2050 | c66759f0d7ac3489df9158da6eaa1330a37c069f | SHALLOW clone: first-commit dates inside it are not provable here |
| galaxies-wafers | fff6fc6ad4f93a15fe8f6456942a1b44e5547105 | full history, 161 commits, all 15 Sep 2026 |
| stars | cbca125bb5eeb7d0ffb02f4546d60eb5d47dadc9 | SHALLOW clone |
| gridatlas | 5ec7f62f213e2d20a02e86427daa182c0f38e4a4 | |

Scratch measurements: `/tmp/nl010/team-4/app-file-sets.json` (produced by the script quoted in E8).

## E1. The apps the estate already catalogues

### E1a. elements/APPS.md: the seven `block:<Sym>` apps (elements@f7a92fb APPS.md:7–13)

| line | key | title | category | functions |
|---|---|---|---|---|
| APPS.md:7 | `block:Ra` | REPD Grid Atlas core engine (v3 to v8) | Map cartridges | 24 |
| APPS.md:8 | `block:Cg` | Cable trench geometry | Solar, BESS and cables | 24 |
| APPS.md:9 | `block:Sb` | Solar and BESS single-line sandbox | Solar, BESS and cables | 24 |
| APPS.md:10 | `block:St` | Solar electrical topology (text engine) | Solar, BESS and cables | 24 |
| APPS.md:11 | `block:Pn` | Pipeline News app | Pipeline News | 24 |
| APPS.md:12 | `block:Gp` | Grid proximity panel | Pipeline News | 24 |
| APPS.md:13 | `block:Wf` | Wider fleet panel | Pipeline News | 21 |

The header (APPS.md:3) pins the build: "Built 2026-09-15T19:18:47Z from the block register generated
2026-09-15T18:28:26.149Z (sha256 `d356562b2e8f`) and the numbered database of 250,174 lines. Keys are the estate's
permanent keys; none is invented." The register copy is `elements@f7a92fb inputs/blocks-2026-09-15T182826149Z.json`
(244 blocks; `catalogue/provenance.json` names its URL `https://ventusltd.github.io/stars/blocks/blocks.json` and its
sha256 `d356562b2e8f0312...`, 403,894 bytes).

Note for the architect: none of the seven is See Through, GridAtlas v9 (cartridges are elements, not apps:
`block:Si` substation-intelligence is kind cartridge, ELEMENTS.md:41), the spider (`block:Gn` "Genome and spiders"
is kind tool, ELEMENTS.md:68), Learn the Kuiper or the Kuiper. The periodic table itself appears only as
`block:x973` "Table", kind auto, "Functions from galaxies-wafers iterations/05-periodic-table/table.mjs"
(ELEMENTS.md:239). An app registry for the Kuiper therefore has to be a union of three sources (E1a, E1b, E1c),
and the roadmap must say which key each entry carries.

### E1b. elements/CATALOGUE.md rows (elements@f7a92fb CATALOGUE.md:5–10)

| line | what | key | count |
|---|---|---|---|
| CATALOGUE.md:7 | elements (register blocks) | `block:<Sym>` | 244 |
| CATALOGUE.md:8 | apps (blocks of kind app) | `block:<Sym>` | 7 |
| CATALOGUE.md:9 | served surfaces | `surface:<url>` | 97 |
| CATALOGUE.md:10 | functions over 10 line occurrences | `family:<n>` | 5720 of 10985 |

CATALOGUE.md:12: "A function's first and last line keys are the ends of its line sequence, not a numeric range."

### E1c. The homepage's entity table (globalgrid2050@c66759f0 homepage_versions/homepage_v134.html:32–56)

Each row is `<tr data-entity-id="…"><th scope="row"><a href="STABLE LINK">Title</a><small class="entity-key">id</small>
… <details class="entity-type"><summary>TYPE</summary>`. The 25 rows, in page order:

| line | entity-id | type | title | stable link |
|---|---|---|---|---|
| 32 | kuiper | engine | Kuiper | https://globalgrid2050.com/kuiper/ |
| 33 | what-is-kuiper | reference | What is the Kuiper? | https://ventusltd.github.io/kuiper-belt/what-is-kuiper.html |
| 34 | learn-the-kuiper | application | Learn the Kuiper | https://ventusltd.github.io/kuiper-belt/learn-the-kuiper/202610050609/ |
| 35 | see-through | application | See to grid connection probabilities iteratively | https://ventusltd.github.io/kuiper-belt/see-through/202610050609/ |
| 36 | kuiper-diary | reference | Kuiper diary | https://ventusltd.github.io/kuiper-belt/diary/20261005.html |
| 37 | gridatlas | application | GridAtlas | https://ventusltd.github.io/gridatlas/atlas/ |
| 38 | ventus-grid-engine | engine | VENTUS Grid Engine | https://ventusltd.github.io/ventus-grid-engine/ |
| 39 | faraday-pulse | engine | Faraday pulse | https://ventusltd.github.io/faraday/ |
| 40 | dc-string-drawing | drawing | DC string drawing | https://globalgrid2050.com/solar-bess-topology-v7/dc-ac-lv-topology-review/index.html#topo_tab_string |
| 41 | ac-block-diagram | drawing | AC block diagram | https://globalgrid2050.com/solar-bess-topology-v7/dc-ac-lv-topology-review/index.html#topo_scada |
| 42 | deep-grid-engine | reference | Deep grid engine | https://ventusltd.github.io/ventus-grid-engine/genome/ |
| 43 | pipeline-news | catalogue | Pipeline News | https://globalgrid2050.com/uk_renewables_pipeline/202609082224/ |
| 44 | solar-design-studio | application | Solar Design Studio | https://globalgrid2050.com/energy-transition-simulator/202609282123/overlay.html |
| 45 | electrical-scene-explorer | drawing | Electrical Scene Explorer | https://globalgrid2050.com/solar-design-studio/202609262041-site-world/ |
| 46 | energy-transition-simulator | application | Energy Transition Simulator | https://globalgrid2050.com/energy-transition-simulator/202609282123/overlay.html |
| 47 | identity-registry | catalogue | Identity Registry | https://ventusltd.github.io/globalgrid2050-ip-and-mac-addresses/ |
| 48 | electricity-market-intelligence | application | Electricity Market Intelligence | https://globalgrid2050.com/uk_energy_tracking_v6/ |
| 49 | generation-history | application | Generation history | https://globalgrid2050.com/uk_energy_tracking_v6/generation_history/ |
| 50 | metals-cable-prices | application | Metals & Cable Prices | https://globalgrid2050.com/copper_and_aluminium_prices_historic_trends/ |
| 51 | lv-ac-dc-prices | application | LV AC & DC cable estimates | https://globalgrid2050.com/lv_ac_dc_price_estimator/ |
| 52 | 33kv-cable-prices | application | 33 kV cable estimates | https://globalgrid2050.com/33kv_uk_dap_price_estimator/ |
| 53 | cable-engineering | reference | Cable Engineering | https://globalgrid2050.com/ac_cables_knowledge/ |
| 54 | dc-cable-guide | reference | DC cable guide | https://globalgrid2050.com/dc_cables_knowledge/ |
| 55 | conductor-resistance | reference | Conductor resistance | https://globalgrid2050.com/conductor_resistances/ |
| 56 | cable-selection | application | Cable selection | https://globalgrid2050.com/cable_selection/ |

Measured absences (grep on homepage_v134.html): no row for the spider sandbox, the periodic table, `elements` or
`stars`. The featured cards (line 13, `#highlightCards`) are solar-design-studio, gridatlas,
electricity-market-intelligence, cable-engineering. The homepage opens every app in the same tab (0 `target="_blank"`,
per NL-009 round1 06-seethrough.md finding 5a). The See Through and Learn the Kuiper rows link to the DATED folder
`202610050609/`, not the pointer; `kuiper-belt@018b46ae see-through/index.html:7,12` is the pointer to the same stamp.

## E2. The `block:<Sym>` key rule (elements@f7a92fb)

- README.md:9 "Every element, app and function with more than 10 lines of code has a unique key. Each key is one the
  estate already uses and never reuses. None is invented here."
- README.md:13 `| element | block:<Sym> | the live block register, one per block |`
- README.md:14 `| app | block:<Sym> | register blocks whose kind is app |`
- README.md:15–17 the other key families: `surface:<url>`, `family:<n>`, `line:<n>` ("endpoints, not a numeric range").
- README.md:25 the checker `tests/check_catalogue.py` rebuilds every row from the pinned inputs; README.md:27–31 what it
  does not prove (that the register is right; that `depends_on`/`used_by` edges are real: "399 register references
  from 17 blocks name 109 distinct target blocks the register does not hold"; that keys were never reused; that any
  surface is live).
- catalogue/provenance.json `rule.apps` = "register blocks whose kind is app"; `register.url` =
  `https://ventusltd.github.io/stars/blocks/blocks.json`, pinned sha256 `d356562b2e8f03…`, generated 2026-09-15T18:28:26Z.
- The symbol comes from the register: each block has `symbol`, `number`, `kind`, `category`, `files`, `live`, `repos`,
  `first_written`, `depends_on`, `used_by`, `functions`, `named_functions`, `inside`, `needs`, `source`, `state`
  (fields of `inputs/blocks-2026-09-15T182826149Z.json`, measured by loading it).
- DRIFT WARNING, measured: the LIVE register in `stars@cbca125b blocks/blocks.json` has `generated_utc`
  2026-10-31T18:45:22.798Z and 606 blocks; `stars@cbca125b blocks/graph.json` has 663 nodes and 2,481 edges. The
  elements catalogue is pinned to the 15 Sep register (244 blocks, 7 apps). A periodic-table layer in the Kuiper must
  say which register it reads (the pinned copy, or the live URL) and refuse to mix them.

## E3. The spider sandbox: what it is and which live URLs it reads

Source: testcode@d09c185c `spider/INDEX.md` and `spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/`.
Published in one commit, `testcode 35bdbcf 2026-09-14 15:32:15 +0100` "spider: publish five timestamped Spider
dashboard test versions (v1 click-fix to v5 front door)".

- INDEX.md:3–4 "Each folder is a self-contained build of the Spider dashboard that reads the live GlobalGrid2050 data
  over https."; INDEX.md:13 v5 "the front door (overview graph, map of maps) registered as data; brand header restored
  byte-faithful … front door renders 15 graphs"; INDEX.md:15–16 open v5 on
  `?graph=overview&focus=GLOBALGRID2050%20architecture`.
- v5 folder contents: `index.html` (43,618 bytes) and `spider/{identity.json, manifest.json, overview-graph.json}` only.
- Brand header: index.html:113 `<span class="ey">Ventus · Global Grid 2050</span><h1>The Spider Sandbox</h1>`.
- The graphs it reads are listed in `spider/manifest.json` (schema `receiver-manifest-v1`), one https URL each:

| manifest.json line | graph id | title | live URL read |
|---|---|---|---|
| 8 | federation | Federation | https://ventusltd.github.io/ventus-grid-engine/spider/data/nodes.json |
| 16 | globalgrid2050-contents | globalgrid2050 contents | https://ventusltd.github.io/ventus-grid-engine/spider/data/contents/nodes.json |
| 24 | engine-graph | Engine population | https://ventusltd.github.io/ventus-grid-engine/genome/engine-graph.json |
| 32 | genome-spider | genome-spider output | https://ventusltd.github.io/ventus-grid-engine/spider/data/genome-spider.json |
| 40 | gridatlas-lineage | GridAtlas cartridge lineage | https://ventusltd.github.io/spiders/species/genome-spider/data/gridatlas-lineage.json |
| 49 | modular | Reuse | https://ventusltd.github.io/stars/modular/graph.json |
| 59 | periodic-table | Inventory | https://ventusltd.github.io/stars/blocks/graph.json |
| 69 | proof-of-work | Audit | https://ventusltd.github.io/stars/proof/graph.json |
| 79 | structure | Structure | https://ventusltd.github.io/stars/structure/graph.json |
| 89 | chemistry | Compatibility | https://ventusltd.github.io/stars/spider/graphs/chemistry.json |
| 99 | vedic | Classification | https://ventusltd.github.io/stars/spider/graphs/vedic.json |
| 109 | random | Sampling | https://ventusltd.github.io/stars/spider/graphs/random.json |
| 119 | generated-apps | Applications | https://ventusltd.github.io/code-generator/spider/graphs/apps.json |
| 129 | sense | Assessment | https://ventusltd.github.io/stars/sense/graph.json |
| 139 | decisions | Decisions | https://ventusltd.github.io/stars/decisions/graph.json |
| 149 | overview | Overview (front door) | `./spider/overview-graph.json` (local, 16 nodes, 15 edges) |

- How it loads them: index.html:258 `RECEIVER_MANIFEST_PATH="./spider/manifest.json"`; :286 fetches it;
  :280–283 `loadManifestScope` fetches each `entry.path` and on failure shows `placeholderScope` ("not yet emitted");
  :239 `DATA_BASE="./spider/data/"` and :243 `loadRoot()` try `nodes.json`/`edges.json` there and fall back to the
  embedded `ROOT_NODES` snapshot (:143) returning "snapshot"; :244 `CONTENTS_BASE="./spider/data/contents/"`;
  :300 reads `./spider/identity.json` (282 labels that appear in two or more graphs, for "Also in").
- Third-party script: index.html:108 `<script src="https://ventusltd.github.io/spiders/species/seer-spider/estate-menu/estate-menu.js" defer>`.
- Other live constants: :139 `GH_BASE` (data-federation-map repo), :140 `LIVE_PAGE` (federation control ledger),
  :213 `STARS="https://ventusltd.github.io/stars/"`, :245 `MONO_GH="https://github.com/Ventusltd/globalgrid2050"`.
- Measured gaps a Kuiper app must know: index.html:99 links `./spider/federation_radial.css` and :239 reads
  `./spider/data/…`, but the v5 folder ships no css and no `spider/data/` (0 css files; only the three JSON files
  above). Served from testcode alone, the stylesheet 404s and the Federation root is the snapshot, not live. Two of
  the fifteen paths (engine-graph, genome-spider) are documented as "may not exist yet" (index.html:267–268).
- The graph data shape the Kuiper would consume: `normaliseGenericGraph` (index.html:272–278) accepts `{nodes:[{id,
  label|title, type|nodeKind|repo_type, rag|status, reason|status_reason|path, gh, ext}], edges:[[from,to,type] |
  {from|source, to|target, type}]}` or GeoJSON `features`.
- Precedent for "spider as a graph layer on the wafer": galaxies-wafers@fff6fc6a iterations/index.json entry n=32
  "Spider and Galaxy — one universe, two views" (commit c3ae65c6, 2026-09-15T21:24:55+01:00), folder
  `iterations/32-spider-and-galaxy/` (`atlas-join.mjs`, `bridge.mjs`); and `layers/manifest.json` spider layer with
  0 features "with the reason" (galaxies-wafers commit fd851b9, 2026-09-15 17:29:17 +0100).

## E4. Licences of what step 7–8 brings in

| thing | licence | key |
|---|---|---|
| spider sandbox (testcode) | Apache-2.0 | testcode@d09c185c LICENSE:1–3 ("Apache License Version 2.0, January 2004"); NOTICE:1–2 "testcode / Copyright 2026 Ventus Ltd"; NOTICE:10–12 "Licensed under the Apache License, Version 2.0 … a copy is in the LICENSE file"; NOTICE:25–32 third-party data keeps its own terms (DESNZ REPD, NESO ETYS, OpenStreetMap, CARTO, Open Charge Map) |
| the spider's graph DATA (15 URLs in E3) | NOT stated in testcode; each lives in stars, ventus-grid-engine, spiders, code-generator | stars@cbca125b has NO LICENSE file (`ls LICENSE* NOTICE*` → none; only `stars/LINES.md:11311` "A published derived graph needs its licence position settled before it ships."). The others were not checked here (not team 4 sources); team 5 must verify |
| elements repository | NO licence file and no licence statement | elements@f7a92fb: `find . -maxdepth 2 -iname 'LICEN*' -o -iname 'NOTICE*'` → nothing; `grep -rni 'licen\|copyright\|apache\|CC BY' *.md catalogue/*.json build/*.py tests/*.py` → nothing. Tree: APPS.md CATALOGUE.md ELEMENTS.md README.md SURFACES.md build/ catalogue/ functions/ inputs/ tests/ .gitattributes. The GitHub API (`gh api repos/Ventusltd/elements/license`) is not reachable from this session (403, repository not attached), so the file tree is the proof |
| the block register the elements read | not stated | stars (above): no LICENSE file; `stars@cbca125b blocks/blocks.json` generated 2026-10-31T18:45:22.798Z |
| the pre-Kuiper wafer (galaxies-wafers) | not checked for a licence file here; README.md:5 states inheritance | galaxies-wafers@fff6fc6a README.md:5 "inherited unchanged from testcode/202609151339" |
| Kuiper engine and editions | Apache-2.0 | kuiper-belt@018b46ae LICENSE:1–3; editions/202611012027/NOTICE.md:3 "Code in this folder … Apache License 2.0"; NOTICE.md:7–10 quoted lines keep their repository's licence (OGL v3 for DESNZ/DUKES) |
| See Through | CERN-OHL-S v2 | kuiper-belt@018b46ae see-through/202610050609/LICENSE.md:5–7 "offered under the same licence: CERN Open Hardware Licence Version 2, Strongly Reciprocal. Full text: licences/globalgrid2050-CERN-OHL-S-2.0.txt"; NOTICE.md:3 |
| See Through data | ODbL 1.0 (OpenStreetMap), Esri terms, Terrain Tiles attribution, MapLibre BSD-3 | see-through/202610050609/NOTICE.md:16 (`data/substations-footprints.odbl.json`, ODbL), :22–27 (OpenStreetMap, GridAtlas line files ODbL loaded at run time), :28–34 (CARTO, Esri, AWS Terrain Tiles), :38–39 (MapLibre GL JS 4.7.1, BSD-3-Clause) |

So two of the three things step 7 brings in (the elements catalogue and the block register it is built from) have
no licence file today. The roadmap must not claim a licence for them; it must name the gap and route it to team 5.

## E5. The Kuiper engine's hooks a launcher and a periodic-table layer would use

All keys `kuiper-belt@018b46ae editions/202611012027/index.html:<line>` (Edition 4, the current page), with the
engine's own line in `index.html` where the function is the engine's.

Data and the law:
- :196–201 the data: `tsv('../../cosmos/repos.tsv')`, `tsv('../../cosmos/wafer.tsv')`; comment :196–197 "One file,
  about 400 kB, and then nothing else is ever fetched to draw the whole."
- :202–208 `repos = {i, name, lines, seen, commits}`; `commits = {unix, lines, repo, sha, gap, k0, cum, k1}`; `k0` is
  the first key of a commit, `k1` the key after its last; :206–207 the REFUSAL "REFUSED: the commits of X sum to …,
  the belt says …" when a repository's commits do not sum to repos.tsv; :208 `N = issued; SPACE = k`.
- :120 `const G32 = 2654435769, TW = 4096;`
- :278–279 `keyPlace(k)`: `m = imul(k mod 2^32, G32)`, `th = 2π m / 2^32`, `r = sqrt(k + 0.5)` → `[r cos th, r sin th]`
  (engine index.html:250). This is the placement law every layer must use: a layer never stores x,y, only keys.
- :282–283 `address(k)` → `{k, i, c, m}` or `{silent:true, next}` by binary search `findBy('k0', k)` (:280); null when
  `k >= SPACE` (engine :254). :284–293 `describe(a)` prints "key … · line … of N ever issued", repo, commit, "the
  text itself: python tools/key.py <k>".
- :240 the refusal when the TSV does not load: "../../cosmos/wafer.tsv did not load. The wafer will not invent its keys."

Camera, safe space, draw:
- :253 `flyTo(x, y, z)` (engine :225); :272–277 `homeCamera()`, `home()` (engine :249); :262 `safeBox()` (engine :234)
  and its Edition 3 wrap :726 so the safe rectangle starts under `#bar`; :247 `narrow = () => innerWidth <= 640`.
- :332 `draw()` (engine :304); :654 the wrap pattern `{ const _draw = draw; draw = function(){ _draw(); drawEdition(); }; }`
  — a new layer hooks `draw` exactly this way, and sets `dirty = true` to request a frame (:637).
- :414 `toWorld(px, py)`; :639 `edScreen(b)` = world→screen for a placed body.
- :416 `goKey(k)` (engine :388): place, `target`, `show(address(k))`, `flyTo(…, 14)`.
- :604–613 the go-to box `#goto`/`#gotoin`: Enter parses a year/month/day, "new [N h]", a bare key number
  (`goKey(min(SPACE-1, n))`), or a repository name (`litRepo`, `home()`). This is the only address-entry hook today;
  there is no `location.hash` handling in the page (grep `location.hash|hashchange` → none).
- :614–618 engine keys: `r` random issued line, `n` show new, `/` go-to box, Backspace home; :600–601 `#keys`
  tap targets dispatch synthetic `keydown`.

The edition layer (the pattern a periodic-table layer copies):
- :626–627 state `ED, edPlaced, edSel, edMeta`; `EDPATH = 'keys.json'`.
- :628–638 `loadEdition()`: fetch, `edMeta = j.summary`, `ED = j.bodies`; `edPlaced = ED.filter(b => b.on_wafer &&
  b.verified && Number.isFinite(b.key) && b.key >= 0 && b.key < SPACE).map(b => Object.assign({}, b, {x, y}))` via
  `keyPlace(b.key)` (:632–633; the harness notes: order of `Object.assign` matters); it is called from the data
  promise at :219 after `home()`.
- :640–653 `drawEdition()` on the 2-D overlay `o2`: culls off-screen, radius 2.6/3.2/6 px, colours
  `rgba(34,238,119,…)` green and `rgba(255,43,214,…)` for the selection; writes its count into `hud.textContent`;
  :649–651 the "not on the wafer … counted, not placed" sentence (the seventh law, :625).
- :655–667 `edCard(i)`: the card markup (`<b>title</b>`, `repo path:line`, quote, "open on GitHub at sha7", details
  with `describe(address(key))`); :669–674 card click rules; :676–680 `edFly(b)` flies so the spark lands between
  the bar and the card (zoom 14); :682–683 `edNext(step)`; :685–690 tap within 9 px (`bd = 81`) picks a spark, runs
  after the engine's own handler; :691–692 keys `e`/`E`/Backspace.

The menu bar and panels (the launcher's hooks):
- :694–697 the comment: "Borrowed in spirit from gridatlas atlas/modules/202609031958-menu-bar.js: one row of titles,
  every panel hidden until its title is tapped, one open at a time".
- :698–704 `#bar` with `#barname` "KUIPER EDITION 4" and four `button.gm-title[data-panel]`: edition, readout, lines,
  commands. :705–709 `#lines.gm-panel` with `#lyAll`, `#lyFocus`, next/previous, `#lyFind`, `#lineslist`.
- :710 `PANELS = { top: elTop, hud, lines: linesPanel, foot: elFoot }`; :712 `placePanels()` tops every panel at
  bar height + 2; :714–720 `setPanel(name)` toggles one open panel, `gm-open`/`gm-on` classes, fills the lines list;
  :721 bar click → `setPanel`; :722 Escape closes; :723 a pointerdown on the canvas closes.
- :728–734 layer switches `lyOn`, `lyFocus`, `lyQuery`; :735 `visibleLine(b)`; :736–743 `fillLines()` rows
  `div.ln[data-i]`; :745–749 wraps of `drawEdition` and `edNext` that obey the switches.
- A launcher that is "one baby step" has, today, exactly these seams: one more `gm-title` in `#bar` (NL-009 round1
  06-seethrough.md finding 1 added `a.gm-title[href="../../see-through/"]`, measured 101×29 px on Pixel 7), one more
  entry in `PANELS`, and the `draw` wrap for a layer. There is no window manager, no iframe, no app registry file and
  no hash router in Edition 4 (greps above).
- GridAtlas's admission rule the launcher must copy, for the record (team 2's lesson): gridatlas@5ec7f62f
  atlas/modules/202609031958-menu-bar.js:8–16 "it installs nothing until the engine's 60 layer controls and the three
  Pipeline News controls are all present and uniquely identified; the Grid menu proxies those 63 ORIGINAL inputs".

Phone budget the launcher inherits (NL-009 round1, folded, not repeated): 01-bar.md finding 1 the bar is two rows at
360–430 px (75.1 px high; 416.6 px of content against 344–414 available); finding 3 five labels at the present style
need 391 px of buttons alone, so the label size must follow the width (10 px at 360); 06-seethrough.md finding 5b: an
APPS or KUIPER entry "would add 70–80 px to a bar already 132 px over", so FABLE-06 put the family in the EDITION
panel instead. Any launcher step must state its pixel budget at 360 px against these numbers.

## E6. The keys of the four candidate algorithms' inputs

### E6a. `editions/202611012027/keys.json` (kuiper-belt@018b46ae; byte-identical since Edition 2 per the harness notes)

Top level `{summary, bodies}`. `summary`: `bodies` 346, `on_wafer` 344, `verified` 344, `keyed` 344, `quote_matches`
337, `quote_not_at_line` (a list of 7 `{id, repo, path, line, key, quote_line, quote_key, check}` objects; e.g.
`gridatlas tools/release/acceptance.mjs:15` key 62884836484, quote found at line 16). `bodies`: 346 objects with the
fields (measured, sorted): `blob, blob_at_path, blob_lines, blob_matches_body, class, commit, commit_lines_measured,
commit_lines_wafer, destination, finding, id, k, k0, key, line, line_end, line_text, lines_before, on_wafer, open,
path, pattern, quote, quote_check, quote_key, quote_line, quote_matches, r, reason, repo, repo_name_differs,
repo_on_wafer, theta, title, verified, wafer_row, worker, x, y`. Counts: `on_wafer` true 344 / false 2; `verified`
true 344 / false 2; `class` focus 174 / estate 172. First body: `id` "0048802883266c68…:5", repo data-centres-gb,
commit f9f47286…, path `.gitattributes`, line 5, key 36064705400, k0 36064705396, `destination`
`https://github.com/Ventusltd/data-centres-gb/blob/f9f47286…/.gitattributes#L5`, worker W08, finding F15.

How a key is made (kuiper-belt@018b46ae tools/edition_keys.py:2–14): `commit → wafer row` (sha12 = commit[:12]),
`row → k0` (cumulative gap_before + lines in order, key.py load()), `path → lines_before` (walking `git ls-tree -r
<commit>` in git's order, summing `lines_of()` for every blob; symlinks included, submodules skipped),
`key = k0 + lines_before + (line - 1)`; :10–12 if the measured commit total differs from the wafer row's `lines`
the body is `verified: false` "with both numbers; nothing is invented".

### E6b. `cosmos/wafer.tsv` and `cosmos/repos.tsv` columns (kuiper-belt@018b46ae)

- cosmos/wafer.tsv:1 header `# unix	lines	repo_index	sha12	gap_before`; 13,345 lines = 1 header + 13,344 commits
  (wafer-meta.json `commits` 13344); first row :2 `1748560273	2	69	7b9eabb832ea	0`.
- cosmos/repos.tsv:1 header `# repo_index	name	lines`; 99 lines = 1 header + 98 repositories (wafer-meta
  `repositories` 98). Rows that matter to team 4: :11 `9 elements 643461`, :21 `19 stars 366853541`,
  :22 `20 star-maker 22207132`, :33 `31 testcode 784124557`, :68 `66 globalgrid2050 41877174755`,
  :59 `57 data-federation-map-for-globalgrid2050-all-repos 1652459`, :63 `61 globalgrid2050-homepage 298055`.
- How the engine reads them: index.html:202–205 (E5): `repo_index` indexes repos.tsv; `gap_before` is added to the
  running key before the commit's `lines`; `k0`/`k1` per commit; the per-repo sum must equal repos.tsv `lines` or the
  wafer REFUSES (:206–207).
- Totals: cosmos/wafer-meta.json `issued_keys` 45735836396, `unissued_keys` 17604284400, `address_space`
  63340120796, `silence_share` 0.2779, `commits` 13344, `repositories` 98, `first_unix` 1748560273 (2025-05-29),
  `last_unix` 1793539112 (2026-11-01), `gap_keys_per_second` 600, `cap_seconds` 1209600, `law` "r = sqrt(key),
  theta = 2 pi frac(key x 2654435769 / 2^32)".
- The check: tools/ci_check.py:9 "K2 cosmos/wafer.tsv re-summed equals cosmos/wafer-meta.json, and equals
  cosmos/repos.tsv"; :53 `issued, silent = sum(int(r[1]) for r in w), sum(int(r[4]) for r in w)`; :55
  `ok2 = issued == meta['issued_keys'] == repo_sum and silent == meta['unissued_keys'] and len(w) == meta['commits']`;
  :56–57 prints "K2 sums: issued 45,735,836,396, meta …, repositories …, silent …, commits 13344".
- The binary rule: tools/key.py:39–42 `lines_of(body)`: `if b'\x00' in body[:8000]: return -1`; otherwise
  `body.count(b'\n') + (1 if body and not body.endswith(b'\n') else 0)`. So a blob with a NUL in its first 8,000 bytes
  is binary, counts −1 and issues NO keys; a text blob issues one key per line, a last line without newline counted.
  key.py:49–50 the cache `data/blob-lines-history.tsv` is "Never trusted blind: the one blob a key lands in is always
  read for real and its count compared, and a mismatch refuses." key.py:8–9 the resolution chain
  key → repository (binary search over cosmos/belt.tsv) → commit (cosmos/commits/NN.tsv).

### E6c. See Through's substation data (kuiper-belt@018b46ae see-through/202610050609/)

- README.md:1 "fall from a field of stars to any of 5,800 UK substations, then watch it rise in 3D on the real
  satellite ground, drawn by rule from open map data, with its pylons."
- descent.js:15 the embedded table `SUB = /*DATA-BEGIN*/{…}` with fields (measured by parsing): `n` 5800, `lon`
  (delta-coded base-36 string), `lat` (same), `v` (index per substation into `vd`), `o` (index into `od`), `vd` (115
  distinct voltage strings such as "132000;33000"), `od` (105 distinct operator names, e.g. "National Grid Electricity
  Distribution", "UK Power Networks"), `source` "globalgrid2050.com/grid_substations.geojson (same 5,800 features and
  order as gr…)", `attribution` "(c) OpenStreetMap contributors, ODbL". descent.js:20 `NSUB = 5800`; :19 `NRULE =
  20000` "particle i carries key floor((i + 0.5) * SPACE / NRULE)"; :70–72 names come from
  `KGGridData.substations.names`; :94 "VOLTAGE NOT IN THE PUBLIC FILE"; :100 "SUBSTATION i (NO NAME IN THE PUBLIC
  FILE)"; :950–952 particle p goes to substation p mod 5,800 (desktop all 20,000 keys; phone 12,900 stars).
- grid-data.js:1–8 `window.KGGridData = {substations, grid400, grid132, uk}`; `substations` = `{label "every
  substation", source "globalgrid2050.com/grid_substations.geojson, substations", attribution "© OpenStreetMap
  contributors, Open Database Licence (ODbL); published at globalgrid2050.com", law "one node per substation, no
  edges: the particles cluster at each", file "substations-network.json", n 5800, xy (11,600 ints, 1e-4 frame
  units), e [], names {index → name}}`; built from
  `globalgrid2050 testcode/wafer-development-environment/202609180245-real-systems/*-network.json` (grid-data.js:1–2).
- descent.js:30 `GA_DATA = 'https://ventusltd.github.io/gridatlas/atlas/releases/202608300453-atlas-v9/data/'`
  (GridAtlas line files `grid_<kv>kv.geojson`, :298) loaded at run time; `data/osm/*.json` per-site Overpass detail
  (7 files: 201, 229, 2392, 259, 324, 350, 463); `data/substations-footprints.odbl.json` (NOTICE.md:16).
- So the substation key is the INDEX 0…5799 in the `grid_substations.geojson` order (descent.js SUB.source), not an
  OSM id; an algorithm that joins See Through to the wafer must say so and must carry ODbL attribution.

### E6d. The elements' inputs (elements@f7a92fb)

`catalogue/provenance.json`: register (E2) plus the numbered database at
`https://globalgrid2050.com/testcode/202609142202/data/`: `all-lines.meta.json` (812 bytes), `all-lines.bin`
(1,000,696 bytes), `families.json` (2,221,286 bytes), `lines.bin` (2,659,760 bytes), each pinned by sha256. These
are the SAME files the pre-Kuiper wafer reads (E7: galaxies-wafers app.mjs:59). `catalogue/apps.json` rows carry
`key, number, symbol, title, description, kind, category, category_title, state, functions_inside, function_keys[]`.

## E7. The pre-Kuiper wafer (Addendum 1 item 3)

galaxies-wafers@fff6fc6a (full history):
- First commits: `be00f1e 2026-09-15 17:13:57 +0100 Initial commit`; `0a7e2a9 2026-09-15 17:20:14 +0100 Wafer
  substrate, frozen, with layers in Grid Atlas's grammar`; `fd851b9 17:29:17 Layers: star-generator (6 features) and
  spider (0 features, with the reason)`; last `fff6fc6 2026-09-15 23:24:46 +0100`; 161 commits in one day.
- README.md:5 "The ground is the wafer: every permanently numbered line of the estate placed by one frozen law,
  `r = sqrt(key)`, `theta = key x golden angle`. It is the basemap and it never changes (`wafer.mjs`). The page
  (`index.html`, `app.mjs`, `lib.mjs`) is inherited unchanged from testcode/202609151339
  (https://globalgrid2050.com/testcode/202609151339/)."
- The law constants: wafer.mjs:11–14 `r = sqrt(key)`, `theta = key x 2.39996322972865332… (the golden angle)`;
  wafer.mjs:43 `GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5))`; :44–49 `SUBSTRATE = {id 'wafer.v1', law 'r = sqrt(key);
  theta = key * goldenAngle', frozen_utc '2026-09-15T15:00:00Z'}`; :52–55 `place(key)`; :69 `extent = max =>
  Math.sqrt(max)`. lib.mjs:11 `GOLDEN = Math.PI * (3 - Math.sqrt(5))`, :12 `SPACING = 1.0`; app.mjs:12
  `r = SPACING * sqrt(key)  theta = key * GOLDEN`.
- The counts: app.mjs:3–7 "Every line of code in the estate that has been given a permanent number is one point on one
  surface. There are 250,174 of them and they are numbered 1 to 342,795 … numbers missing from the sequence were never
  issued. Those gaps are drawn as gaps." wafer.mjs:28 "The estate's line numbers run to 342,795 today."
- Its data: app.mjs:59 `DATA = 'https://globalgrid2050.com/testcode/202609142202/data/'`; :128–131 `all-lines.meta.json`,
  `all-lines.bin` (Uint32), `all-lines.len.bin` (Uint16), `all-lines.family.bin` (Uint8); :145–147 `families.json`,
  `lines.bin`. proof/wafer.check.mjs:9 reads the same from `../../202609142202/data/`.
- Periodic table on that wafer: iterations/index.json n=5 "The Line Wafer — the periodic table of blocks, on the
  numbered surface" (commit 8c7a0561, 2026-09-15T21:41:10+01:00); iterations/05-periodic-table/table.mjs:1–14 "the
  periodic table, as a strip along the bottom of the wafer. One cell per block of the live register, grouped by
  category … Tapping a cell hydrates layers/modules/module-<Sym>.json … and flies the wafer to the block's first
  line"; :15 `REGISTER = 'https://ventusltd.github.io/stars/blocks/blocks.json'`; :16 `TABLE =
  'https://ventusltd.github.io/stars/table.html'`; :18–21 the category colours (geodesy #00cc00, network #0054ff,
  connections #ff0000, constants #ff9900, cartridges #ffff00, layers #b200ff, arrival #ff00ff, news #ff4500, solar
  #ffd700, interface #00ffff, proofs #39ff14, other #8b93a7). stars@cbca125b table.html:5 `<title>Periodic table of
  globalgrid2050 architecture development</title>`, :97 fetches `./blocks/blocks.json`.
- Apps on that wafer: iterations/index.json n=26 "Apps, Layers, Substrate — the estate's apps as tabs over its
  numbered lines" (commit 96f3f07b, 2026-09-15T20:05:53+01:00), folder `iterations/26-apps-layers-substrate/`
  (`apps.mjs`, `layers-panel.mjs`, `queue.mjs`).
- Origin in globalgrid2050@c66759f0: `testcode/202609151339/` (README.md, app.mjs, index.html, lib.mjs, proof/,
  style.css; README.md:9 "250,174 lines are numbered 1 to 342,795"); lib.mjs:11–12 byte-identical to galaxies-wafers
  lib.mjs:11–12 (diff -q: lib.mjs identical, app.mjs differs). NO `wafer.mjs` in testcode/202609151339 (the frozen
  substrate file first appears in galaxies-wafers 0a7e2a9). `testcode/wafer-development-environment/`: index.html,
  shared/, versions.json (13 stamps from 202609170036-estate to 202609190330-cable-cross-sections), 63 entries in the
  folder; the clone is shallow so the first commit dates of these paths (`git log` shows acd2f242 2026-09-16 04:31
  as the oldest reachable) are a lower bound, not a proof.

Comparison the architect may state with these keys (no other numbers): pre-Kuiper 250,174 issued keys in an address
space of 342,795 (silence 92,621 = 27.0 %) placed by `r = sqrt(key)`, `theta = key × golden angle`, key = permanent
line number from the numbered database of 14 Sep 2026; Kuiper today 45,735,836,396 issued keys in 63,340,120,796
(silence 17,604,284,400 = 27.79 %, wafer-meta `silence_share`) placed by `r = sqrt(key + 0.5)`, `theta = 2π ·
frac(key · 2654435769 / 2^32)` (Edition 4 index.html:278; wafer-meta `law`), key = running total over 13,344 commits
of 98 repositories in time order with 600 silent keys per second of gap capped at 14 days (wafer-meta
`gap_keys_per_second`, `cap_seconds`). The two keys do NOT share a space: a pre-Kuiper key is one distinct numbered
line of a snapshot; a Kuiper key is one line of one blob in one commit (key.py:39–42). "What moved" is therefore a
change of unit, not a renumbering, and the roadmap must say so.

## E8. App file sets for per-app Kuipers (Addendum 1 item 1)

Register field `files` of each app block in `elements@f7a92fb inputs/blocks-2026-09-15T182826149Z.json`: a list of
`{repo "Ventusltd/<name>", commit <40-hex>, path, live}`. Measured against kuiper-belt@018b46ae cosmos/repos.tsv
(names) and cosmos/wafer.tsv (sha12), script output saved at `/tmp/nl010/team-4/app-file-sets.json`:

| key | files in register | repos of those files | files whose repo is on the wafer | files whose commit sha12 is a wafer row | register `repos` field |
|---|---|---|---|---|---|
| block:Ra | 8 | code-generator, globalgrid2050 | 8 | 8 | code-generator, globalgrid2050, gridatlas, youengineer-code-review |
| block:Cg | 8 | cable-trench-or-drill, globalgrid2050, layout-tool, testcode | 8 | 8 | same four |
| block:Sb | 8 | globalgrid2050 | 8 | 8 | globalgrid2050, testcode, layout-tool |
| block:St | 8 | solar-electrical-topology-analysis-engine-text-based | 8 | 8 | same |
| block:Pn | 8 | data-grid-gb, data-gridatlas, gridatlas, pipelinenews | 8 | 8 | + globalgrid2050, spiders, testcode, code-generator, ventus-grid-engine |
| block:Gp | 8 | pipelinenews | 8 | 8 | pipelinenews |
| block:Wf | 2 | globalgrid2050, pipelinenews | 2 | 2 | same |

Limits, measured: the register never lists more than 8 files per block (max 8; 17 blocks have exactly 8; 139 have 1),
and for Ra, Sb and Pn the `repos` field names repositories that the `files` list does not. So the register's `files`
is a sample of an app's file set, not the whole; a per-app Kuiper cannot take it as the denominator. All 50 listed
files resolve to a commit that IS a wafer row, so each has a Kuiper key range today (`k0 + lines_before` by
edition_keys.py:4–9).

For the apps outside the register (See Through, Learn the Kuiper, the spider, the periodic table) the file set is a
folder of one repository: `kuiper-belt see-through/202610050609/` (12 entries: LICENSE.md NOTICE.md README.md data/
descent.js grid-data.js index.html kuiper-law.js licences/ model.js pf.js plain.css see3d.js vendor/),
`kuiper-belt learn-the-kuiper/202610050609/`, `testcode spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/`
(index.html + spider/ 3 JSON), `stars table.html` + `blocks/`. Those folders are dated and never edited (the folder
rule), so "that app's commits" is the set of wafer rows of that repository whose trees contain the folder: a
measurable set, not yet measured here.

## E9. What the owner asked, in the words that bind steps 7–8

BRIEF.md owner's words: "This is just the beginning of the intelligent algorithms. Also bring in periodic table and
spider sandbox. Turn the kuiper into the OS of the estate in baby steps." Team 4 line of the brief: "the app registry
from elements/APPS.md and CATALOGUE.md (block:<Sym> keys), the periodic table as a layer and an app, the spider
sandbox as an app and a graph layer, a launcher model that is one baby step (no window manager yet), and the first
intelligent algorithm the Kuiper runs over the estate (name it, give its inputs, its key, its refusal rule)".
Addendum 1 items 1–3 (per-app Kuipers; the overarching Kuiper that counts EVERYTHING; the unique-lines Kuiper and
the comparison with the pre-Kuiper wafer) are to be written by team 4 "into step 8 or as steps 8a–8c", gated on the
owner's acceptance of steps 1–10.

## E10. Review checklist I will apply to STEPS.md

1. Every number and every file named in steps 7–8 has a key from this file or a new key the architect adds.
2. The app registry says which of E1a/E1b/E1c each entry comes from and what key it carries; it does not invent keys
   for apps the register does not hold (See Through, spider, periodic table have no `block:` key today).
3. The periodic table step names its register (pinned 15 Sep copy, 244 blocks, or live 606 blocks) and places cells by
   `keyPlace()` only (E5), never by stored x,y.
4. The spider step names the fifteen URLs (E3) or the manifest file, and the two measured gaps (css, root data).
5. The launcher is one baby step: it uses the `#bar`/`PANELS`/`setPanel` seams (E5), states its 360 px budget against
   NL-009 01-bar/06-seethrough numbers, and promises no window manager.
6. The first algorithm names its inputs by key (E6a–d), its own key, and its refusal rule in the engine's idiom
   ("REFUSED …", "did not load … will not invent").
7. Licences: Apache-2.0 for the spider code, none claimed for elements or stars (E4); See Through CERN-OHL-S v2 and ODbL.
8. Addendum 8a–8c: per-app file sets per E8 with the 8-file cap stated; the counting rules per E6b (binary rule, K2
   sums 45,735,836,396); the comparison per E7 with the unit change stated.
9. Line 1 of STEPS.md is "REVIEW: PASS" or "REVIEW: OPEN"; the format follows the ROADMAP format in BRIEF.md (goal,
   GridAtlas lesson with key, Kuiper change, module, acceptance test on Android, licence note, Opus team brief).
