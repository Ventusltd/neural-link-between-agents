# NL-010 Team 2 (layers, steps 3–4): EVIDENCE

Evidence officer FABLE-T2B, 1 Nov 2026. Law: no claim without a key. Every row below is `repo@sha path:line` against
the clones under `/home/user/estate/` (all at origin/main, clean worktrees), with a literal fragment that stands on that
line. `/tmp/nl010/team-2/check_keys.py` re-reads every row and PASSes only if the sha matches HEAD, the line exists and
the fragment is on it. Nothing in this file is remembered; everything was read today.

Heads: gridatlas@5ec7f62f213e · kuiper-belt@018b46aed50f · elements@f7a92fb085c3 · testcode@d09c185c8dac ·
globalgrid2050@c66759f0d7ac. Kuiper page under study: `kuiper-belt/editions/202611012027/index.html` (Edition 4), 753
lines; the engine it copies is `kuiper-belt/index.html`, 594 lines.

Reading order the owner set: GridAtlas layer management ("the 63 controls, the proxying, cartridge_order, hashes in
current.json, the admission and failure code, the release pointer") then the Kuiper hooks a layer registry will use.

## A. GridAtlas layer management: the lessons

### A1. The 63 layer controls (60 engine + 3 Pipeline News), and where they are built

| # | lesson | key | fragment on that line |
|---|---|---|---|
| A1.1 | The menu bar states the inventory it will accept: 60 engine, 3 pipeline, 63 total | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:32 | `EXPECTED_ENGINE_LAYERS = 60` |
| A1.2 | same, pipeline | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:33 | `EXPECTED_PIPELINE_LAYERS = 3` |
| A1.3 | same, total | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:34 | `EXPECTED_LAYER_CONTROLS = 63` |
| A1.4 | The 60 engine layers are DATA, not code: the immutable shell declares `ukConfig`, 11 groups, exactly 60 `id:` entries (measured: lines 142–261, 60 ids, 60 unique) | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/index.html:142 | `const ukConfig = [` |
| A1.5 | first group | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/index.html:144 | `group: "Topology (GeoJSON)"` |
| A1.6 | first layer row: id, label, colour, type, url, snap, preload | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/index.html:146 | `{ id: "400",  label: "400kV", color: "#0054ff"` |
| A1.7 | the config is handed to the engine once | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/index.html:264 | `config: ukConfig` |
| A1.8 | The engine indexes that config by id | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/ventus-corev8engine.js:61 | `const layerConfigById = new Map(` |
| A1.9 | A control is an `<input type=checkbox data-layer-id=…>` built from the config row | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/ventus-corev8engine.js:991 | `input.setAttribute('data-layer-id', layer.id)` |
| A1.10 | A layer with no config fails visibly (`FAIL` state), it is not drawn blank | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/ventus-corev8engine.js:1137 | `updateUIState(layerId, 'FAIL')` |
| A1.11 | The live engine is the substation-intelligence cartridge (replaces `ventus-corev8engine.js`); the same builder line lives there | gridatlas@5ec7f62f213e atlas/cartridges/202609062358-substation-intelligence-v9-63.js:1060 | `input.setAttribute('data-layer-id', layer.id)` |
| A1.12 | The 3 Pipeline News controls deliberately do NOT carry `data-layer-id`, because the engine dispatches on it: borrow the styling, never the attribute another owner dispatches on | gridatlas@5ec7f62f213e atlas/modules/202609030048-pipeline-news-layers.js:16 | `WHY IT DOES NOT USE data-layer-id` |
| A1.13 | same, the rule | gridatlas@5ec7f62f213e atlas/modules/202609030048-pipeline-news-layers.js:22 | `borrow the styling, never` |
| A1.14 | the three controls are a table | gridatlas@5ec7f62f213e atlas/modules/202609030048-pipeline-news-layers.js:81 | `const CONTROLS = [` |
| A1.15 | and carry their own attribute | gridatlas@5ec7f62f213e atlas/modules/202609030048-pipeline-news-layers.js:358 | `input.setAttribute('data-pn-layer', control.id)` |
| A1.16 | A layer's key is namespaced: `engine:<id>` or `pipeline:<id>` | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:79 | `function layerKey(input)` |
| A1.17 | A layer's label keeps its live WAIT/LOAD/OK/FAIL suffix (the first menu stripped it and made success and failure indistinguishable on a phone) | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:92 | `WAIT/LOAD/OK/FAIL` |
| A1.18 | A layer's group is read from the DOM it sits in (`.key-group .key-title`), never re-declared | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:101 | `function layerGroup(input)` |

### A2. The proxying: the Grid menu drives the SAME 63 original inputs

| # | lesson | key | fragment |
|---|---|---|---|
| A2.1 | The rule in the header: the Grid menu proxies the 63 ORIGINAL inputs so the engine's delegated handlers remain the only implementation | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:12 | `the Grid menu proxies those 63 ORIGINAL inputs` |
| A2.2 | Action buttons are MOVED as the same DOM nodes (listeners survive), result panels stay with the map | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:14 | `moved as the same DOM nodes` |
| A2.3 | Two surfaces, one truth: the dropdown and the restored panel drive the same 63 inputs so they cannot disagree | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:314 | `this panel drive the SAME 63 original inputs` |
| A2.4 | `inventory()` collects the originals from `#scada-ui-container` by attribute | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:107 | `function inventory(doc)` |
| A2.5 | `complete` is a five-part predicate: 60, 3, 63, 63 unique, no empty key | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:122 | `complete: engine.length === EXPECTED_ENGINE_LAYERS` |
| A2.6 | The inventory is published as a read-only probe: `menuBar.inspect()` | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:130 | `state.inspect = function ()` |
| A2.7 | A later cartridge's contract is written against that probe: it must stay `{60,3,63,63,true}` and may create no layer attribute | gridatlas@5ec7f62f213e atlas/current.json:687 | `menuBar.inspect() stays {60,3,63,63,true}` |
| A2.8 | `buildLayerControls`: one proxy per original, keyed, grouped | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1428 | `function buildLayerControls(found)` |
| A2.9 | A proxy change forwards to `original.click()`, nothing else: the engine listener owns hydration | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1458 | `try { original.click(); }` |
| A2.10 | The proxy is stretched invisibly over the whole label so its own rect is the ≥44 px control under any measurement | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1419 | `function layerCheckbox(kind)` |
| A2.11 | the CSS of that hit target | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:257 | `position:absolute;inset:0` |
| A2.12 | `syncLayer` mirrors checked, disabled and label from original to proxy, never the other way | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:419 | `function syncLayer(key)` |
| A2.13 | One document `change` listener keeps proxies in step when the original is toggled elsewhere | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1723 | `doc.addEventListener('change'` |
| A2.14 | A MutationObserver adopts late controls and re-syncs | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1740 | `observer = new MutationObserver(` |
| A2.15 | Basemaps are radios proxied the same way | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1480 | `if (proxy.checked && !original.checked` |
| A2.16 | The six menu names are the architect's vocabulary | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:31 | `MENUS = ['File', 'Edit', 'View', 'Scope', 'Grid', 'About']` |
| A2.17 | The module is idempotent under a schema name and publishes its state in a namespace | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:37 | `window.__GRIDATLAS_MODULES__` |

### A3. The admission rule and the failure code (fail loudly, leave the original reachable)

| # | lesson | key | fragment |
|---|---|---|---|
| A3.1 | Header: installs nothing until all 63 are present and uniquely identified | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:10 | `it installs nothing until` |
| A3.2 | A missing control leaves the old interface reachable and is published as a failure, never silently skipped | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:17 | `A missing control leaves the old interface reachable` |
| A3.3 | `required()` names every node the install needs; `missing` lists what is absent | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:141 | `function required(doc)` |
| A3.4 | the inventory predicate is one of the requirements | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:157 | `missing.push('63 unique layer controls')` |
| A3.5 | `installed` flips only after the complete inventory is built | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1731 | `state.installed = true` |
| A3.6 | A retry window, bounded: 160 × 250 ms = 40 s, because the register UI is built after map load | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:35 | `MAX_TRIES = 160` |
| A3.7 | `loudFailure`: console.error + a visible `role=alert` naming the counts found | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1752 | `function loudFailure(doc)` |
| A3.8 | the message states expected and found | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1755 | `expected 60 engine + 3 Pipeline News layer controls; found` |
| A3.9 | the alert says the originals remain | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1763 | `Original controls remain available` |
| A3.10 | `start()` refuses a partial document (proof stubs) without starting the retry loop | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1776 | `menu not installed: full document unavailable` |
| A3.11 | the retry ends in loudFailure, not silence | gridatlas@5ec7f62f213e atlas/modules/202609031958-menu-bar.js:1795 | `loudFailure(document)` |

### A4. Cartridges: a stamped, hashed file admitted by the composer only when its slot exists

| # | lesson | key | fragment |
|---|---|---|---|
| A4.1 | The composer is a stable 124-line page; it fetches `current.json` with `cache: 'no-store'` | gridatlas@5ec7f62f213e atlas/index.html:39 | `fetch('./current.json', { cache: 'no-store' })` |
| A4.2 | schema is checked | gridatlas@5ec7f62f213e atlas/index.html:42 | `gridatlas.current.v2` |
| A4.3 | architecture contract is checked | gridatlas@5ec7f62f213e atlas/index.html:43 | `IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES` |
| A4.4 | registry shape is checked | gridatlas@5ec7f62f213e atlas/index.html:44 | `cartridge registry malformed` |
| A4.5 | The shell is fetched from `atlas/releases/<release_id>/` and given a `<base>` so its relative paths stay inside the release | gridatlas@5ec7f62f213e atlas/index.html:52 | `<base href=` |
| A4.6 | Cartridges are composed in `cartridge_order`, each must exist | gridatlas@5ec7f62f213e atlas/index.html:65 | `for (const id of current.cartridge_order)` |
| A4.7 | missing id fails | gridatlas@5ec7f62f213e atlas/index.html:67 | `missing cartridge ${id}` |
| A4.8 | Two slot kinds only: `replace-script` and `after-cartridge` | gridatlas@5ec7f62f213e atlas/index.html:62 | `SLOTS = ['replace-script', 'after-cartridge']` |
| A4.9 | an `after-cartridge` anchor must already be composed | gridatlas@5ec7f62f213e atlas/index.html:73 | `is not composed before it` |
| A4.10 | The hash must be a 64-hex SHA-256 | gridatlas@5ec7f62f213e atlas/index.html:75 | `invalid SHA-256` |
| A4.11 | The bytes are hashed in the browser and compared; a mismatch refuses the cartridge | gridatlas@5ec7f62f213e atlas/index.html:81 | `SHA-256 mismatch` |
| A4.12 | The verified bytes become a blob URL script tag stamped `data-gridatlas-cartridge` | gridatlas@5ec7f62f213e atlas/index.html:83 | `data-gridatlas-cartridge=` |
| A4.13 | A `replace-script` slot that is not in the shell fails | gridatlas@5ec7f62f213e atlas/index.html:92 | `shell slot ${cartridge.replace_script} not found` |
| A4.14 | An anchor must be found exactly once | gridatlas@5ec7f62f213e atlas/index.html:96 | `not found exactly once` |
| A4.15 | The composed page publishes what loaded: `window.__GRIDATLAS_ATLAS__` with `loaded_cartridges` {id, sha256} | gridatlas@5ec7f62f213e atlas/index.html:111 | `loaded_cartridges` |
| A4.16 | Any invariant failure is one loud screen: `GRIDATLAS COMPOSITION FAILED … The immutable shell was not changed` | gridatlas@5ec7f62f213e atlas/index.html:35 | `GRIDATLAS COMPOSITION FAILED` |
| A4.17 | `invariant()` throws; nothing is skipped | gridatlas@5ec7f62f213e atlas/index.html:20 | `if (!condition) throw new Error(message)` |
| A4.18 | current.json: the pointer's schema | gridatlas@5ec7f62f213e atlas/current.json:2 | `"schema": "gridatlas.current.v2"` |
| A4.19 | current.json: the order is a separate list from the records | gridatlas@5ec7f62f213e atlas/current.json:14 | `"cartridge_order": [` |
| A4.20 | A cartridge record: id | gridatlas@5ec7f62f213e atlas/current.json:24 | `"id": "streaming-parquet-bridge"` |
| A4.21 | its generation stamp (UTC minute) | gridatlas@5ec7f62f213e atlas/current.json:25 | `"generation": "202609241251"` |
| A4.22 | its version | gridatlas@5ec7f62f213e atlas/current.json:26 | `"version": "v9.156"` |
| A4.23 | its slot | gridatlas@5ec7f62f213e atlas/current.json:28 | `"slot": "replace-script"` |
| A4.24 | the shell script it replaces | gridatlas@5ec7f62f213e atlas/current.json:29 | `"replace_script": "202608292311-maplibre-worker-bridge.js"` |
| A4.25 | its path, stamped file name | gridatlas@5ec7f62f213e atlas/current.json:30 | `"path": "./cartridges/202609241251-streaming-parquet-bridge-v9-5.js"` |
| A4.26 | its sha256 | gridatlas@5ec7f62f213e atlas/current.json:31 | `"sha256": "60be8215ba873ac2886786bf6e3fd51e5764e7c5e26684fde71ebe9974a329a2"` |
| A4.27 | its contract file | gridatlas@5ec7f62f213e atlas/current.json:32 | `"contract": "../ui/cartridges/202609241251-streaming-parquet-bridge-v9-5.mjs"` |
| A4.28 | it declares it did not modify the shell | gridatlas@5ec7f62f213e atlas/current.json:41 | `"immutable_shell_modified": false` |
| A4.29 | The contract file is a frozen object with schema `gridatlas.cartridge.v1`, generation, version, slot | gridatlas@5ec7f62f213e ui/cartridges/202609241251-streaming-parquet-bridge-v9-5.mjs:2 | `schema: 'gridatlas.cartridge.v1'` |
| A4.30 | A cartridge file's header says it is ASSEMBLED from parts and must not be edited: edit a part, rebuild under a new generation | gridatlas@5ec7f62f213e atlas/cartridges/202609062358-substation-intelligence-v9-63.js:4 | `ASSEMBLED by tools/build-cartridge.mjs` |
| A4.31 | the menu bar is one of its listed modules | gridatlas@5ec7f62f213e atlas/cartridges/202609062358-substation-intelligence-v9-63.js:19 | `atlas/modules/202609031958-menu-bar.js` |
| A4.32 | FINDING: that header carries generation `202609060259` while the file name and current.json say `202609062358` (A4.33): the stamp is written in two places and they disagree. A Kuiper cartridge must carry one stamp, checked against its file name | gridatlas@5ec7f62f213e atlas/cartridges/202609062358-substation-intelligence-v9-63.js:2 | `generation 202609060259` |
| A4.33 | current.json's record for the same cartridge | gridatlas@5ec7f62f213e atlas/current.json:567 | `"generation": "202609062358"` |
| A4.34 | A cartridge is a manifest of modules, not a place where code accumulates | gridatlas@5ec7f62f213e governance/202609011940-modular-architecture-and-domain-map.md:38 | `manifest of modules` |
| A4.35 | A module is small enough to hold in your head; if its proof needs three stubs the boundary is wrong | gridatlas@5ec7f62f213e governance/202609011940-modular-architecture-and-domain-map.md:43 | `small enough to hold in your head` |
| A4.36 | Shared modules are shared, not copied | gridatlas@5ec7f62f213e governance/202609011940-modular-architecture-and-domain-map.md:46 | `Shared modules are shared, not copied` |
| A4.37 | Every module has its own proof against stubs | gridatlas@5ec7f62f213e governance/202609011940-modular-architecture-and-domain-map.md:32 | `tools/proofs/modules/<name>.proof.mjs` |
| A4.38 | The atlas README: the only mutable application pointer is current.json; new features must be bounded cartridges, never a copy of the application | gridatlas@5ec7f62f213e atlas/README.md:5 | `The only mutable application pointer is` |
| A4.39 | The release folder carries its own `sha256sums.txt` | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/sha256sums.txt:1 | `202608291818-place-postcode-search.js` |
| A4.40 | and declares itself immutable after publication | gridatlas@5ec7f62f213e atlas/releases/202608300453-atlas-v9/release-manifest.json:16 | `"immutable_after_publication": true` |

### A5. The release pointer: how current.json moves

| # | lesson | key | fragment |
|---|---|---|---|
| A5.1 | A release moves `atlas/current.json` (and STATE.md) from the live generation to a preview generation already on main | gridatlas@5ec7f62f213e docs/RELEASE.md:3 | `A **release** moves` |
| A5.2 | The tools never touch `atlas/releases/**` and never decide that something should ship | gridatlas@5ec7f62f213e docs/RELEASE.md:12 | `touch` |
| A5.3 | the owner's authorisation is a required argument written into the commit | gridatlas@5ec7f62f213e docs/RELEASE.md:13 | `owner's authorisation is a required argument` |
| A5.4 | Acceptance is the owner's comment `ACCEPT G` (first line) or label `accepted:G` | gridatlas@5ec7f62f213e docs/RELEASE.md:40 | `ACCEPT G` |
| A5.5 | Only the owner merges the release PR, with rebase | gridatlas@5ec7f62f213e docs/RELEASE.md:54 | `Only the owner merges a release` |
| A5.6 | Agents never record acceptance | gridatlas@5ec7f62f213e docs/RELEASE.md:49 | `Agents never record acceptance` |
| A5.7 | Live is the expected predecessor: the live generation must equal G's `previous_generation` | gridatlas@5ec7f62f213e docs/RELEASE.md:110 | `Live is the expected predecessor` |
| A5.8 | The tested preview IS the release: `atlas/v/<G>/current.json` must equal the pointer about to be written | gridatlas@5ec7f62f213e docs/RELEASE.md:119 | `The tested preview is the release` |
| A5.9 | Every cartridge the manifest names must hash to its recorded sha256 before the pointer moves | gridatlas@5ec7f62f213e docs/RELEASE.md:117 | `each hashing to its recorded sha256` |
| A5.10 | Loader first, then the pointer: the composer may change alone only if it composes byte-identical output for the live pointer | gridatlas@5ec7f62f213e docs/RELEASE.md:236 | `Loader first, then the pointer` |
| A5.11 | same, in the tool | gridatlas@5ec7f62f213e tools/release/loader-swap.mjs:7 | `may change WITHOUT atlas/current.json only when` |
| A5.12 | The pointer files are exactly two | gridatlas@5ec7f62f213e tools/release/lib.mjs:30 | `POINTER_FILES = Object.freeze(['atlas/current.json', 'STATE.md'])` |
| A5.13 | Acceptance is read from GitHub, by owner login, not through an App, carrying no agent signature, after cut time; latest verdict wins | gridatlas@5ec7f62f213e tools/release/acceptance.mjs:16 | `WHAT COUNTS` |
| A5.14 | `--record` refuses to run under Claude Code, Codex or CI | gridatlas@5ec7f62f213e tools/release/acceptance.mjs:26 | `refuses` |
| A5.15 | current.json records `previous_generation` (the chain) | gridatlas@5ec7f62f213e atlas/current.json:4 | `"previous_generation": "202610291044"` |
| A5.16 | the release the shell comes from | gridatlas@5ec7f62f213e atlas/current.json:7 | `"release_id": "202608300453-atlas-v9"` |
| A5.17 | the shell block: index and base inside the release folder | gridatlas@5ec7f62f213e atlas/current.json:11 | `"index": "./releases/202608300453-atlas-v9/index.html"` |
| A5.18 | `last_known_green` is kept in the pointer | gridatlas@5ec7f62f213e atlas/current.json:821 | `"last_known_green"` |
| A5.19 | the composition manifest the pointer was cut from | gridatlas@5ec7f62f213e atlas/current.json:863 | `"composition_manifest": "./manifests/202610292044-composition.json"` |
| A5.20 | the manifest has the same schema as the pointer (the tested preview is the release) | gridatlas@5ec7f62f213e atlas/manifests/202610292044-composition.json:2 | `"schema": "gridatlas.current.v2"` |
| A5.21 | the loader version the pointer needs | gridatlas@5ec7f62f213e atlas/current.json:889 | `"loader": "v2"` |

## B. Kuiper hooks a layer registry will use (Edition 4 page, and the engine it copies)

### B1. The canvases, `draw`, the `o2` overlay, `litRepo`

| # | hook | key | fragment |
|---|---|---|---|
| B1.1 | Two canvases: `#c` (WebGL wafer) and `#o` (2D overlay) | kuiper-belt@018b46aed50f editions/202611012027/index.html:88 | `<canvas id="c"></canvas><canvas id="o"></canvas>` |
| B1.2 | `o2` is the overlay's 2D context; every layer drawn in screen space draws on it | kuiper-belt@018b46aed50f editions/202611012027/index.html:121 | `o2 = ov.getContext('2d')` |
| B1.3 | `hud`, `big`, `sub` are the text surfaces a layer may append to | kuiper-belt@018b46aed50f editions/202611012027/index.html:123 | `const hud = document.getElementById('hud'), big = document.getElementById('big')` |
| B1.4 | Camera and selection state are module-level lets: `cx, cy, zoom, dirty, tween, litRepo, target` | kuiper-belt@018b46aed50f editions/202611012027/index.html:243 | `let cx = 0, cy = 0, zoom = 1, dirty = true, tween = null, litRepo = -1, target = null` |
| B1.5 | `draw()` is a plain function binding, so it can be wrapped (the engine's extension point) | kuiper-belt@018b46aed50f editions/202611012027/index.html:332 | `function draw(){` |
| B1.6 | `draw` passes `litRepo` to the shader as `u_litRepo` (lighting a repository is a GPU uniform, not an overlay) | kuiper-belt@018b46aed50f editions/202611012027/index.html:350 | `gl.uniform1i(U(PF,'u_litRepo'), litRepo)` |
| B1.7 | `draw` clears the overlay each frame before its own rings, boundary and crosshair; a layer wrapper must draw AFTER this | kuiper-belt@018b46aed50f editions/202611012027/index.html:384 | `o2.clearRect(0,0,ov.width,ov.height)` |
| B1.8 | `show(a)` sets `litRepo` from an address: the card and the light are one action | kuiper-belt@018b46aed50f editions/202611012027/index.html:415 | `if (a && !a.silent) litRepo = a.c.repo` |
| B1.9 | `frame()` is the rAF loop that redraws when `dirty` | kuiper-belt@018b46aed50f editions/202611012027/index.html:323 | `function frame(){` |
| B1.10 | `flyTo(x,y,z)` is the only camera mover | kuiper-belt@018b46aed50f editions/202611012027/index.html:253 | `function flyTo(x, y, z)` |
| B1.11 | `keyPlace(k)` is the placement law `r = sqrt(k), theta = golden` every layer must use to put a key on the wafer | kuiper-belt@018b46aed50f editions/202611012027/index.html:278 | `function keyPlace(k)` |
| B1.12 | `address(k)` resolves a key to its commit, or null outside SPACE | kuiper-belt@018b46aed50f editions/202611012027/index.html:282 | `function address(k)` |
| B1.13 | `safeBox()` is the rectangle left for the camera after the text surfaces | kuiper-belt@018b46aed50f editions/202611012027/index.html:262 | `function safeBox(){` |
| B1.14 | Touch state the tap handlers consult: `pts` (active pointers) | kuiper-belt@018b46aed50f editions/202611012027/index.html:572 | `const pts = new Map()` |
| B1.15 | The go-to box `#goto` / `gbox` whose open state suppresses keyboard layers | kuiper-belt@018b46aed50f editions/202611012027/index.html:604 | `const gbox = document.getElementById('goto')` |
| B1.16 | Same hooks in the engine the edition copies: `o2` | kuiper-belt@018b46aed50f index.html:93 | `o2 = ov.getContext('2d')` |
| B1.17 | engine `draw` | kuiper-belt@018b46aed50f index.html:304 | `function draw(){` |
| B1.18 | engine `litRepo` | kuiper-belt@018b46aed50f index.html:215 | `litRepo = -1, target = null` |
| B1.19 | engine `keyPlace` | kuiper-belt@018b46aed50f index.html:250 | `function keyPlace(k)` |
| B1.20 | engine `frame` | kuiper-belt@018b46aed50f index.html:295 | `function frame(){` |

### B2. The edition layer: `keys.json` loading, `edPlaced`, the `drawEdition` wrapper

| # | hook | key | fragment |
|---|---|---|---|
| B2.1 | The layer's state: `ED` (all bodies), `edPlaced` (on the wafer), `edSel`, `edMeta` | kuiper-belt@018b46aed50f editions/202611012027/index.html:626 | `let ED = [], edPlaced = [], edSel = -1, edMeta = null` |
| B2.2 | The layer's data file is a relative path beside the page | kuiper-belt@018b46aed50f editions/202611012027/index.html:627 | `const EDPATH = 'keys.json'` |
| B2.3 | `loadEdition()` fetches it, reads `summary` and `bodies` | kuiper-belt@018b46aed50f editions/202611012027/index.html:630 | `edMeta = j.summary` |
| B2.4 | A failed load is recorded as an error the readout will print, not an empty success | kuiper-belt@018b46aed50f editions/202611012027/index.html:631 | `edMeta = { error: 'keys.json did not load' }` |
| B2.5 | Admission of a body to the wafer: `on_wafer && verified && finite key && 0 <= key < SPACE`, then `keyPlace` | kuiper-belt@018b46aed50f editions/202611012027/index.html:632 | `edPlaced = ED.filter(b => b.on_wafer && b.verified && Number.isFinite(b.key) && b.key >= 0 && b.key < SPACE)` |
| B2.6 | `Object.assign({}, b, {x,y})`: the body's own fields win nothing over the computed place (order matters) | kuiper-belt@018b46aed50f editions/202611012027/index.html:633 | `Object.assign({}, b, { x:p[0], y:p[1] })` |
| B2.7 | `loadEdition()` is called from the TSV promise after `home()`: a layer loads only after the wafer's own data admitted itself | kuiper-belt@018b46aed50f editions/202611012027/index.html:219 | `home(); dirty = true; loadEdition();` |
| B2.8 | `edScreen(b)` maps wafer to overlay pixels | kuiper-belt@018b46aed50f editions/202611012027/index.html:639 | `function edScreen(b)` |
| B2.9 | `drawEdition()` draws the sparks on `o2` and appends a count line to the readout | kuiper-belt@018b46aed50f editions/202611012027/index.html:640 | `function drawEdition(){` |
| B2.10 | bodies not on the wafer are counted and named, never placed (the seventh law) | kuiper-belt@018b46aed50f editions/202611012027/index.html:651 | `not on the wafer (named in keys.json), counted, not placed` |
| B2.11 | THE WRAPPER: `draw` is replaced by `_draw(); drawEdition();` — this is how every layer today reaches the frame | kuiper-belt@018b46aed50f editions/202611012027/index.html:654 | `{ const _draw = draw; draw = function(){ _draw(); drawEdition(); }; }` |
| B2.12 | `edCard(i)` writes the card: title, `repo path:line`, quote, GitHub link at the commit, details | kuiper-belt@018b46aed50f editions/202611012027/index.html:655 | `function edCard(i){` |
| B2.13 | the card line that is the key | kuiper-belt@018b46aed50f editions/202611012027/index.html:660 | `esc(b.repo) + '  ' + esc(b.path) + ':' + b.line` |
| B2.14 | the card lights the repository too | kuiper-belt@018b46aed50f editions/202611012027/index.html:665 | `if (a && !a.silent) litRepo = a.c.repo` |
| B2.15 | `edFly(b)` places the spark in the clear space between bar and card | kuiper-belt@018b46aed50f editions/202611012027/index.html:676 | `function edFly(b){` |
| B2.16 | `edNext(step)` steps the selection | kuiper-belt@018b46aed50f editions/202611012027/index.html:682 | `function edNext(step)` |
| B2.17 | A tap within 9 px opens the nearest spark, after the engine's own tap handler | kuiper-belt@018b46aed50f editions/202611012027/index.html:685 | `addEventListener('pointerup', e => {` |
| B2.18 | keys `e`/`E`/Backspace, suppressed while the go-to box is open | kuiper-belt@018b46aed50f editions/202611012027/index.html:691 | `if (gbox.style.display === 'block') return;` |
| B2.19 | FINDING: the readout line still says `EDITION 2` inside Edition 4's drawEdition, while the off-switch says `EDITION 4`: a stamp written by hand in three places has already drifted | kuiper-belt@018b46aed50f editions/202611012027/index.html:650 | `'\nEDITION 2 · '` |

### B3. The menu bar, the LINES panel and the layer switches (`lyOn`, `lyFocus`, `lyFind`)

| # | hook | key | fragment |
|---|---|---|---|
| B3.1 | The bar is declared as borrowed in spirit from the GridAtlas menu bar | kuiper-belt@018b46aed50f editions/202611012027/index.html:695 | `Borrowed in spirit from gridatlas atlas/modules/202609031958-menu-bar.js` |
| B3.2 | `#bar` with a name span and four `.gm-title` buttons (edition, readout, lines, commands) | kuiper-belt@018b46aed50f editions/202611012027/index.html:699 | `<span id="barname">KUIPER EDITION 4</span>` |
| B3.3 | the LINES title | kuiper-belt@018b46aed50f editions/202611012027/index.html:702 | `data-panel="lines">lines</button>` |
| B3.4 | The LINES panel's controls: `#lyAll` (the layer switch), `#lyFocus`, next/previous, `#lyFind`, `#lineslist` | kuiper-belt@018b46aed50f editions/202611012027/index.html:706 | `<input type="checkbox" id="lyAll" checked> verified lines layer` |
| B3.5 | `PANELS` is a name→element map; `setPanel(name)` opens one at a time | kuiper-belt@018b46aed50f editions/202611012027/index.html:710 | `const PANELS = { top: elTop, hud: hud, lines: linesPanel, foot: elFoot }` |
| B3.6 | `placePanels()` measures the bar's height and seats panels under it | kuiper-belt@018b46aed50f editions/202611012027/index.html:712 | `function placePanels()` |
| B3.7 | `setPanel` | kuiper-belt@018b46aed50f editions/202611012027/index.html:714 | `function setPanel(name)` |
| B3.8 | Escape closes; a pointerdown on the wafer closes | kuiper-belt@018b46aed50f editions/202611012027/index.html:723 | `cv.addEventListener('pointerdown', () => { if (openPanel) setPanel(openPanel); })` |
| B3.9 | `safeBox` is wrapped to start under the bar (the same wrapping idiom as `draw`) | kuiper-belt@018b46aed50f editions/202611012027/index.html:726 | `{ const _safe = safeBox; safeBox = function(){` |
| B3.10 | The layer switches are three module-level lets | kuiper-belt@018b46aed50f editions/202611012027/index.html:728 | `let lyOn = true, lyFocus = false, lyQuery = ''` |
| B3.11 | `#lyAll` change → `lyOn`, `dirty` | kuiper-belt@018b46aed50f editions/202611012027/index.html:729 | `lyOn = e.target.checked; dirty = true` |
| B3.12 | `#lyFocus` change → `lyFocus`, refill list | kuiper-belt@018b46aed50f editions/202611012027/index.html:730 | `lyFocus = e.target.checked` |
| B3.13 | `#lyFind` input → `lyQuery` | kuiper-belt@018b46aed50f editions/202611012027/index.html:731 | `lyQuery = e.target.value.trim().toLowerCase()` |
| B3.14 | `visibleLine(b)` is the one predicate the list, the stepping and the drawing share | kuiper-belt@018b46aed50f editions/202611012027/index.html:735 | `function visibleLine(b){ return lyOn &&` |
| B3.15 | `fillLines()` renders the list rows with `data-i` | kuiper-belt@018b46aed50f editions/202611012027/index.html:736 | `function fillLines(){` |
| B3.16 | THE SECOND WRAPPER: `drawEdition` is wrapped again so the sparks obey `lyOn`/`lyFocus`; off prints a readout line, not silence | kuiper-belt@018b46aed50f editions/202611012027/index.html:745 | `{ const _drawEd = drawEdition; drawEdition = function(){ if (!lyOn) {` |
| B3.17 | `edNext` is wrapped to skip invisible lines | kuiper-belt@018b46aed50f editions/202611012027/index.html:747 | `{ const _edNext = edNext; edNext = function(step)` |
| B3.18 | Bar CSS: fixed, top, z-index 12, flex | kuiper-belt@018b46aed50f editions/202611012027/index.html:58 | `#bar{position:fixed;top:0;left:0;right:0;z-index:12;display:flex` |
| B3.19 | `.gm-title` and `.gm-on`, the GridAtlas class names reused | kuiper-belt@018b46aed50f editions/202611012027/index.html:63 | `#bar .gm-title:hover,#bar .gm-title.gm-on` |
| B3.20 | Panels show only with `.gm-open` | kuiper-belt@018b46aed50f editions/202611012027/index.html:65 | `#top.gm-open,#hud.gm-open,#foot.gm-open,#lines.gm-open{display:block}` |
| B3.21 | At ≤640 px the bar is allowed to WRAP (the two-row problem NL-009 is auditing) | kuiper-belt@018b46aed50f editions/202611012027/index.html:83 | `@media (max-width:640px){ #bar{flex-wrap:wrap` |

### B4. `cosmos/*.tsv`: the wafer's own data, and its refusal

| # | hook | key | fragment |
|---|---|---|---|
| B4.1 | `tsv(url)` throws on a non-OK fetch and drops `#` comment lines | kuiper-belt@018b46aed50f editions/202611012027/index.html:199 | `async function tsv(url){ const r = await fetch(url); if (!r.ok) throw new Error(url);` |
| B4.2 | The page loads exactly two files, relative to the edition folder | kuiper-belt@018b46aed50f editions/202611012027/index.html:201 | `Promise.all([tsv('../../cosmos/repos.tsv'), tsv('../../cosmos/wafer.tsv')])` |
| B4.3 | repos.tsv columns | kuiper-belt@018b46aed50f cosmos/repos.tsv:1 | `# repo_index	name	lines` |
| B4.4 | wafer.tsv columns | kuiper-belt@018b46aed50f cosmos/wafer.tsv:1 | `# unix	lines	repo_index	sha12	gap_before` |
| B4.5 | Keys are issued in time order from `gap_before` and `lines`: `k0`, `k1`, `cum` | kuiper-belt@018b46aed50f editions/202611012027/index.html:204 | `k += +p[4]; const c = { unix:+p[0], lines:+p[1], repo:+p[2], sha:p[3], gap:+p[4], k0:k, cum:issued }` |
| B4.6 | THE REFUSAL: if a repository's commits do not sum to what repos.tsv declared, the wafer refuses to draw | kuiper-belt@018b46aed50f editions/202611012027/index.html:207 | `REFUSED: the commits of` |
| B4.7 | `N` (issued) and `SPACE` (address space) are set only after the sum passes | kuiper-belt@018b46aed50f editions/202611012027/index.html:208 | `N = issued; SPACE = k;` |
| B4.8 | A failed load says so and invents nothing | kuiper-belt@018b46aed50f editions/202611012027/index.html:240 | `did not load. The wafer will not invent its keys.` |
| B4.9 | The engine's own comment on the two-file contract | kuiper-belt@018b46aed50f editions/202611012027/index.html:196 | `cosmos/wafer.tsv: every commit in time order` |
| B4.10 | wafer-meta.json holds the totals ci_check re-sums (commits 13344, repositories 98, law `r = sqrt(key)`) | kuiper-belt@018b46aed50f cosmos/wafer-meta.json:6 | `"commits": 13344` |
| B4.11 | belt.tsv (key.py's repository shard) | kuiper-belt@018b46aed50f cosmos/belt.tsv:1 | `# repo	entry_lines	entries	commits	head_lines	first_commit_unix` |
| B4.12 | standing.tsv (heads per repository) | kuiper-belt@018b46aed50f cosmos/standing.tsv:1 | `# repository	head	head_unix	files	lines` |
| B4.13 | pulse.tsv (the estate over time) | kuiper-belt@018b46aed50f cosmos/pulse.tsv:1 | `# unix	repositories	missed	files	lines_standing` |
| B4.14 | ci_check K2: wafer.tsv re-summed equals wafer-meta.json and repos.tsv | kuiper-belt@018b46aed50f tools/ci_check.py:9 | `K2  cosmos/wafer.tsv re-summed equals cosmos/wafer-meta.json` |
| B4.15 | ci_check K3: every page's script must parse | kuiper-belt@018b46aed50f tools/ci_check.py:10 | `the script inside every page parses as JavaScript` |
| B4.16 | ci_check K4: keys in time order, no overlap | kuiper-belt@018b46aed50f tools/ci_check.py:11 | `K4  keys are in time order` |
| B4.17 | `edition_keys.py` gives each body its key by key.py's walk: `key = k0 + lines_before + (line - 1)` | kuiper-belt@018b46aed50f tools/edition_keys.py:12 | `key    =  k0 + lines_before + (line - 1)` |
| B4.18 | a body whose walk does not close is `verified: false` with both numbers; nothing invented | kuiper-belt@018b46aed50f tools/edition_keys.py:15 | `verified: false` |
| B4.19 | `key.py`: key → repository → commit → file,line → text, by git alone | kuiper-belt@018b46aed50f tools/key.py:8 | `key -> repository` |

### B5. The laws and folder rules the registry inherits

| # | hook | key | fragment |
|---|---|---|---|
| B5.1 | First law: no claim without a key | kuiper-belt@018b46aed50f README.md:29 | `## The first law: no claim without a key` |
| B5.2 | Seventh law: every body must be openable; a body with no destination is drawn dim and counted | kuiper-belt@018b46aed50f README.md:84 | `## The seventh law: every body must be openable` |
| B5.3 | the dim count is the belt's own score | kuiper-belt@018b46aed50f README.md:92 | `The count of dim bodies is the belt's own score` |
| B5.4 | L8 openness is the only law that judges | kuiper-belt@018b46aed50f LAWS.md:111 | `## L8. Openness: the only law that judges` |
| B5.5 | L10: a layer's own summary is not independent proof of that summary | kuiper-belt@018b46aed50f LAWS.md:163 | `A layer's own summary is not independent proof of that summary` |
| B5.6 | The Kuiper already defines a cartridge: one small module, its own data, its own proof, loaded on demand; it does not know about any other cartridge | kuiper-belt@018b46aed50f SPEC.md:3 | `It is a cartridge in the sense the wafer already uses` |
| B5.7 | same | kuiper-belt@018b46aed50f SPEC.md:4 | `one small module, its own data, its own proof, loaded on demand` |
| B5.8 | NEXT.md records the menu as borrowed from the GridAtlas module, panels hidden at rest | kuiper-belt@018b46aed50f NEXT.md:32 | `borrowed from` |
| B5.9 | NEXT.md: two keyed sources must agree before context is shown | kuiper-belt@018b46aed50f NEXT.md:30 | `Two keyed sources must agree` |
| B5.10 | Palette: green is energised / lit, magenta is selected, cyan is the instrument, amber is attention | kuiper-belt@018b46aed50f PALETTE.md:11 | `#22ee77` |
| B5.11 | Folder rule: an edition is numbered in order of publication and keyed by its stamp | kuiper-belt@018b46aed50f editions/README.md:3 | `Version numbers: an edition is numbered in order of publication` |
| B5.12 | the pointer `editions/index.html` names the stamp in three places | kuiper-belt@018b46aed50f editions/README.md:8 | `written in three places in` |
| B5.13 | pointer: meta refresh | kuiper-belt@018b46aed50f editions/index.html:7 | `url=202611012027/` |
| B5.14 | pointer: location.replace | kuiper-belt@018b46aed50f editions/index.html:12 | `location.replace('202611012027/' + location.hash)` |
| B5.15 | Each edition folder hashes every file except itself | kuiper-belt@018b46aed50f editions/202611012027/proof/edition-sha256.txt:3 | `./index.html` |
| B5.16 | keys.json's own hash in that proof | kuiper-belt@018b46aed50f editions/202611012027/proof/edition-sha256.txt:4 | `./keys.json` |
| B5.17 | The README's Editions entry for Edition 4 | kuiper-belt@018b46aed50f README.md:191 | `**Kuiper Edition 4 (202611012027)**` |

### B6. The other layers the registry will carry: See Through stars, elements, spider graphs

| # | hook | key | fragment |
|---|---|---|---|
| B6.1 | See Through's stable pointer, same three-place idiom | kuiper-belt@018b46aed50f see-through/index.html:7 | `url=202610050609/` |
| B6.2 | What it is: from a field of stars to any of 5,800 UK substations | kuiper-belt@018b46aed50f see-through/202610050609/README.md:1 | `fall from a field of stars to any of 5,800 UK substations` |
| B6.3 | Licence: CERN-OHL-S v2 | kuiper-belt@018b46aed50f see-through/202610050609/LICENSE.md:6 | `CERN Open Hardware Licence Version 2, Strongly Reciprocal` |
| B6.4 | See Through is already a module bundle: seven scripts in order | kuiper-belt@018b46aed50f see-through/202610050609/index.html:10 | `<script src="kuiper-law.js"></script>` |
| B6.5 | `kuiper-law.js` carries the SAME placement law as the wafer, cited by engine line | kuiper-belt@018b46aed50f see-through/202610050609/kuiper-law.js:7 | `r = sqrt(k),  theta = 2 pi frac(k G / 2^32),  G = 2654435769` |
| B6.6 | See Through's modules register themselves in `window.KGModules` with an `id` — an existing module registry hook in the estate | kuiper-belt@018b46aed50f see-through/202610050609/descent.js:1073 | `[]).push(M)` |
| B6.7 | and the host looks the module up by id | kuiper-belt@018b46aed50f see-through/202610050609/index.html:19 | `x.id==='descent'` |
| B6.8 | the descent publishes a probe `window.__descent` | kuiper-belt@018b46aed50f see-through/202610050609/descent.js:1034 | `window.__descent = {` |
| B6.9 | The substations are ODbL OpenStreetMap data, attributed in the data file header | kuiper-belt@018b46aed50f see-through/202610050609/grid-data.js:7 | `OpenStreetMap contributors, ODbL` |
| B6.10 | the stars' dataset: 5,800 substations, one node per substation, no edges (in the `KGGridData.substations` object on this line) | kuiper-belt@018b46aed50f see-through/202610050609/grid-data.js:8 | `"n":5800` |
| B6.11 | The homepage lists See Through as entity `see-through` | globalgrid2050@c66759f0d7ac homepage_versions/homepage_v134.html:35 | `data-entity-id="see-through"` |
| B6.12 | Elements: the key grammar `block:<Sym>` | elements@f7a92fb085c3 README.md:13 | `` `block:<Sym>` `` |
| B6.13 | an app is a block of kind app | elements@f7a92fb085c3 README.md:14 | `register blocks whose kind is app` |
| B6.14 | the counts: 244 elements, 7 apps, 97 surfaces | elements@f7a92fb085c3 CATALOGUE.md:7 | `244` |
| B6.15 | the first app row | elements@f7a92fb085c3 APPS.md:7 | `` `block:Ra` `` |
| B6.16 | an element row (state UNSETTLED is data a layer can colour by) | elements@f7a92fb085c3 ELEMENTS.md:7 | `` `block:At` `` |
| B6.17 | FINDING for Team 5: the elements clone has no LICENSE file at its root (ls: APPS.md CATALOGUE.md ELEMENTS.md README.md SURFACES.md build catalogue functions inputs tests); its README names none | elements@f7a92fb085c3 README.md:1 | `#` |
| B6.18 | Spider sandbox: five timestamped versions, each the one before plus one change | testcode@d09c185c8dac spider/INDEX.md:1 | `# Spider dashboard: five timestamped test versions` |
| B6.19 | the v5 front door: one card whose fifteen wires are the fifteen graphs | testcode@d09c185c8dac spider/INDEX.md:15 | `?graph=overview&focus=` |
| B6.20 | the graphs are JSON under `./spider/data/` | testcode@d09c185c8dac spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/index.html:239 | `const DATA_BASE="./spider/data/"` |
| B6.21 | a live manifest may replace the built-in list | testcode@d09c185c8dac spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/index.html:258 | `RECEIVER_MANIFEST_PATH="./spider/manifest.json"` |
| B6.22 | the spider's own `draw()` renders a focus node with its in/out neighbours | testcode@d09c185c8dac spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/index.html:231 | `function draw(){const nodes=S().nodes,focus=nodes[current]` |
| B6.23 | `?graph=&focus=` is its deep-link grammar | testcode@d09c185c8dac spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/index.html:212 | `?graph=${encodeURIComponent(g)}&focus=` |
| B6.24 | testcode's licence is Apache-2.0 | testcode@d09c185c8dac LICENSE:2 | `Apache License` |

## C. What the evidence says a Kuiper reference-layer registry must be (the review bar for STEPS.md)

These are the tests I will hold STEPS.md to. Each is traceable to the rows above.

1. A layer is a RECORD, not a code path: id, label, group, colour (from PALETTE.md), source file, licence (A1.4–A1.7,
   B5.10). The 60 GridAtlas layers are one array of records; the Kuiper's seven kinds (verified lines, repositories,
   periods, editions, See Through stars, elements, spider graphs) must be records in one registry with one key grammar.
2. One namespaced key per layer, like `engine:` / `pipeline:` (A1.16); never two layers with the same attribute an
   owner dispatches on (A1.12–A1.13).
3. Every layer switch drives ONE original state and every surface proxies it (A2.1, A2.3, A2.9, A2.12); the Kuiper
   today has `lyOn`/`lyFocus`/`lyQuery` as bare lets (B3.10) and the LINES checkbox as the only original (B3.4); the
   registry must become that original and the bar must proxy it, so the dropdown and any restored panel cannot disagree.
4. A layer draws by wrapping `draw` after `o2.clearRect` (B1.7, B2.11) or by setting a uniform (B1.6); the registry
   owns the wrap once, in registry order (the Kuiper's `cartridge_order`), instead of each layer re-wrapping (B2.11,
   B3.16 are two wraps of the same function today).
5. A layer's data loads only after the wafer admitted its own (B2.7, B4.6–B4.7); a failed load is a printed error
   (B2.4, B4.8), and the layer's label carries its live state as GridAtlas' WAIT/LOAD/OK/FAIL does (A1.17, A1.10).
6. A body enters a layer only by the admission predicate: verified, keyed, inside SPACE, placed by `keyPlace` (B2.5,
   B1.11); what is not on the wafer is counted and named, never placed (B2.10, B5.2–B5.3).
7. A Kuiper cartridge = one module file, stamp `YYYYMMDDHHMM` in its file name AND one matching stamp inside (A4.21,
   A4.25, A4.30, A4.32 is the counter-example), a sha256 recorded in a pointer file beside the page (A4.26, B5.15–B5.16),
   a contract that names the hooks it needs (A4.27, A4.29) and a proof (A4.37).
8. Admission by the composer: fetch, hash in the browser, compare, refuse on mismatch, compose in order, and refuse
   when a hook/slot is absent (A4.6–A4.14); failure is one loud screen that says the shell was not changed (A4.16),
   or for a late module a `role=alert` that says the originals remain (A3.7–A3.9); never a silent skip (A3.2).
9. The composed page publishes what loaded (A4.15), a probe like `menuBar.inspect()` (A2.6), and later modules'
   contracts are written against that probe (A2.7).
10. The pointer moves only as a new dated folder plus three-place pointer (B5.11–B5.14), the tested preview is the
    release (A5.8), hashes are checked before the move (A5.9), and the owner accepts (A5.4–A5.6).
11. Owner's words: "reference layer management like gridatlas", "consistent", "built around the kuiper": the Grid
    menu's names and layer-panel grammar (A2.16, A1.18) are the ones to carry; the wafer, its laws (B5.1–B5.7) and its
    `o2`/`draw`/`keyPlace` hooks (B1) are the centre everything is built around, not replaced.
12. Licences per layer: See Through CERN-OHL-S v2 (B6.3), its substations ODbL (B6.9), testcode Apache-2.0 (B6.24),
    kuiper-belt Apache-2.0 code / CC BY 4.0 text and data (editions/README.md last line), elements: no LICENSE file
    found (B6.17), to be settled by Team 5.

## D. NL-009 round1 findings that bear on layers (read 20:58 UTC)

`FIXES/NL-009/round1/` held `BRIEF.md` and an empty `img/` at 20:44 UTC; by 20:58 UTC three audits had landed. The
ones a layer registry must answer (keys are into this repository's files, not the estate):

| # | finding (auditor) | key | what it means for steps 3–4 |
|---|---|---|---|
| D1 | BLOCKER: the bar is two rows at 360, 393, 412 and 430 px; a fifth title at the present style needs 521 px (FABLE-01) | neural-link-between-agents FIXES/NL-009/round1/01-bar.md:13 | Layer switches cannot be more bar titles; they belong in ONE Grid-like panel, as GridAtlas keeps 63 switches behind one title (A2.16) |
| D2 | MINOR: a `keys.json` 404 is said only in the hidden READOUT; the EDITION heading still reads "0 verified lines lit" (FABLE-09) | neural-link-between-agents FIXES/NL-009/round1/09-robust.md:25 | A layer's load state must be on its own label (WAIT/LOAD/OK/FAIL, A1.17) and in the heading, not only in a hidden panel |
| D3 | MINOR: the 344 LINES rows are `<div>`s, 0 focusable; `#lyFind` has no label (FABLE-09) | neural-link-between-agents FIXES/NL-009/round1/09-robust.md:38 | Layer rows need `role=button tabindex=0` and ≥44 px targets, as GridAtlas stretches the proxy over the whole label (A2.10–A2.11) |
| D4 | MAJOR: WebGL unavailable gives a blank black screen (FABLE-09) | neural-link-between-agents FIXES/NL-009/round1/09-robust.md:18 | Registry admission must fail loudly when a hook (`gl`, `o2`) is absent, as A3.7–A3.9 and A4.16 |
| D5 | BLOCKER (owner): See Through is unreachable from Edition 4 (FABLE-06) | neural-link-between-agents FIXES/NL-009/round1/06-seethrough.md:11 | The See Through stars layer and its button are Team 3's step; Team 2's registry must carry the layer record and its deep link, not a second button |
| D6 | Auditors agree the fix is a `(pointer:coarse)` rule with `min-height:44px` titles and the edition name shrinking to a mark (FABLE-01) | neural-link-between-agents FIXES/NL-009/round1/01-bar.md:51 | The Grid-like LAYERS panel inherits the same touch rule |

Re-read before REVIEW; REVIEW.md names the state then.
