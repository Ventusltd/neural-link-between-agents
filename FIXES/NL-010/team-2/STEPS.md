REVIEW: OPEN

# Team 2 "layers": steps 3 and 4 of the NL-010 roadmap

Architect FABLE-T2A. Evidence officer FABLE-T2B (`EVIDENCE.md` and `REVIEW.md` beside this file; rows cited below as
E:A4.11 etc. are rows of that file, each a `repo@sha path:line` with the fragment on the line). Channel: issue #10.
Heads this file is keyed to: gridatlas `5ec7f62f213e2d20a02e86427daa182c0f38e4a4`, kuiper-belt
`018b46aed50f28f7b1882a0dcaba6593ce522beb`, elements `f7a92fb085c38dcbbd5cb469a66cd5ca61fb95bf`, testcode
`d09c185c8dacbc5c73afb2b0d0d8dad40745a544`, galaxies-wafers `fff6fc6ad4f93a15fe8f6456942a1b44e5547105`,
globalgrid2050 `c66759f0d7ac3489df9158da6eaa1330a37c069f`. Short form `gridatlas@5ec7f62 path:line` means that head.
Keys into this repository (`FIXES/NL-009/round1/*`, `SESSIONS/*`) are written as `neural-link path:line` (working tree,
uncommitted at the time of writing). No claim without a key; a gap is written as DISCLOSED (kuiper-belt@018b46a
LAWS.md:139-170), never papered over.

Vocabulary, shared with Team 5's STEPS.md: **the edition** is the next dated folder `kuiper-belt/editions/<stamp>/`
(Edition 5 or later); **the page** is its `index.html` (the engine copy plus the edition layer, integrator-owned);
**a module** (a Kuiper cartridge) is one file under `editions/<stamp>/modules/`, admitted by `modules.json`; **a layer**
is one record in `data/layers.json`, registered at run time in the layer registry; **the hook table** is `window.KY`,
the only surface a module may touch. Where this file and Team 5's draft differ (module file names, step 4 below), the
difference is stated for Team 5B to consolidate, not left for the Opus teams to discover.

What the two steps rest on, in one paragraph. GridAtlas keeps 63 layer switches behind one Grid menu that proxies the
engine's own 63 inputs and installs nothing until all 63 exist (gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:
8-21, :32-34, :122-127); its cartridges are stamped, hashed files admitted in an explicit order by a 124-line composer
that refuses on any mismatch and says so on one screen (gridatlas@5ec7f62 atlas/index.html:65-102, :32-36). The Kuiper
today has one layer, the verified lines, switched by three bare variables (`lyOn`, `lyFocus`, `lyQuery`,
kuiper-belt@018b46a editions/202611012027/index.html:728), drawn by wrapping `draw` twice (:654, :745), loaded from a
file whose failure is said only in a hidden readout (:631, :641; neural-link FIXES/NL-009/round1/09-robust.md:25-29),
and two more layer-like things that are not layers at all: a lit repository (`litRepo`, :243, a shader uniform at :350)
and a lit period (`lightTime`, :554-565). The estate already built a wafer "with layers, in the manner of Grid Atlas"
once, galaxies-wafers (galaxies-wafers@fff6fc6 README.md:3, :7), with a manifest of 201 layer records each carrying id,
label, group, preload, colour, file, bytes, features and sha256 (layers/manifest.json:5-17; count by
`python3 -c "import json;print(len(json.load(open('layers/manifest.json'))['layers']))"` = 201) and a layer format whose
geometry carries keys, never coordinates (README.md:11-18). Step 3 brings that registry to the Kuiper with the GridAtlas
proxy-and-refuse discipline; step 4 makes every layer, and every other feature the Opus teams build, a cartridge the
page admits by hash and hook, in order, loudly.

---

## Step 3. The Kuiper layer registry

**Goal.** One registry, `data/layers.json` plus `modules/<stamp>-layers.js`, holds every reference layer of the wafer as
a record with a key, a label, a group, a colour with a stated meaning, an order, a source with a sha256, a licence and a
live state; one WAFER panel (the Grid menu's place in the bar, Team 1's name for it, team-1/STEPS.md:146-153) shows one
row per layer with an on/off control that is the only original; every other surface (keys, readout, URL, File menu,
SCOPE and EDIT, the apps) proxies that original; a layer whose
data is missing, wrong or unlicensed is listed and says why in its row, in the heading and in an alert, and draws
nothing, while the wafer underneath keeps drawing. The first seven layers: verified lines, repositories, periods,
editions, See Through stars, elements, spider graphs.

**GridAtlas lesson (with keys).**
- A layer is a record, not a code path: the shell declares 60 layers as data (`ukConfig`, 11 groups, 60 ids,
  gridatlas@5ec7f62 atlas/releases/202608300453-atlas-v9/index.html:142-264; E:A1.4-A1.7), the engine indexes them by
  id (ventus-corev8engine.js:61; E:A1.8) and builds one `<input type=checkbox data-layer-id>` per record
  (ventus-corev8engine.js:991; E:A1.9). A layer with no config is shown `FAIL`, never drawn blank (:1137; E:A1.10).
- One owner-dispatched attribute per owner. The engine dispatches on `data-layer-id`; the Pipeline News module adds its
  three layers under `data-pn-layer` because "borrow the styling, never the attribute that another owner dispatches on"
  (gridatlas@5ec7f62 atlas/modules/202609030048-pipeline-news-layers.js:17-23, :358; E:A1.12-A1.15). The key is
  namespaced, `engine:<id>` / `pipeline:<id>` (menu-bar.js:79-85; E:A1.16).
- One original, many proxies. The Grid menu proxies the 63 ORIGINAL inputs so the engine's delegated handlers stay the
  only implementation (menu-bar.js:12-13; E:A2.1); a proxy change forwards to `original.click()` and nothing else
  (:1451-1462; E:A2.9); `syncLayer` mirrors checked, disabled and label from original to proxy, never back (:419-432;
  E:A2.12); a document-level `change` listener and a MutationObserver keep late and external changes in step
  (:1723-1726, :1739-1745; E:A2.13-A2.14); the dropdown and the restored panel drive the SAME 63 inputs so they cannot
  disagree (:312-319; E:A2.3).
- The label carries the live state. The label keeps its WAIT/LOAD/OK/FAIL suffix because the first menu stripped it
  and "made a successful load and a failed load indistinguishable in the only layer surface left on a phone"
  (menu-bar.js:91-98; E:A1.17). The group is read from where the control sits, never re-declared (:101-105; E:A1.18).
- Install nothing until the inventory is complete, then publish the inventory. `inventory()` demands 60 + 3 = 63,
  all unique, none keyless (menu-bar.js:107-128; E:A2.5); `menuBar.inspect()` publishes it (:130-139; E:A2.6); a
  later cartridge's contract is written against that probe, "menuBar.inspect() stays {60,3,63,63,true}"
  (gridatlas@5ec7f62 atlas/current.json:687; E:A2.7). A missing control is published as a failure with the counts found,
  console.error plus a `role=alert`, and the originals remain (menu-bar.js:1752-1768; E:A3.7-A3.9).
- The hit target is the whole row: the proxy input is stretched invisibly over its label so the control measures
  ≥ 44 px under any audit (menu-bar.js:1414-1425, :248-257; E:A2.10-A2.11).
- The estate's own precedent for a wafer layer manifest: galaxies-wafers@fff6fc6 layers/manifest.json:2 (`"substrate":
  "wafer.v1"`), :6-16 (`id`, `label`, `group`, `preload`, `colour`, `evidence`, `note`, `file`, `bytes`, `features`,
  `sha256`); its panel loads "as Grid Atlas does it": a row for every layer from the start, nothing fetched until ticked
  unless `preload: true`, one fetch per URL, a timeout on every fetch (layers-panel.mjs:23-30), states WAIT, QUEUE,
  LOAD, OK, EMPTY, FAIL, REFUSED (:117-118), a `refuse()` that writes the reason on the row (:325-330), and the ticked
  layers written to the URL as `?layers=a,b` (:508-522). A layer may ship EMPTY with its reason on its row ("Empty here
  means not anchored in these records, not absent from the estate", manifest.json:113-124, the spider layer). FINDING
  carried into this step: that manifest records a sha256 per layer file but no root module verifies it (`grep -n
  'sha256\|digest' *.mjs` at galaxies-wafers@fff6fc6 finds only app.mjs:141, the pack's digest); a recorded hash nobody
  checks is decoration. The Kuiper checks (3.5).

**Kuiper change.**

3.1 **The record.** `data/layers.json`, schema `kuiper.layers.v1`:
```json
{ "schema": "kuiper.layers.v1", "edition": "<stamp>", "substrate": "kuiper.wafer.v1",
  "order": ["periods", "repos", "editions", "lines", "see-through", "elements", "spider"],
  "layers": [ { "id": "lines", "key": "layer:lines", "label": "verified lines", "group": "THE EVIDENCE",
      "colour": "#22ee77", "meaning": "energised: a line verified against a clone", "draws": "points",
      "preload": true, "format": "edition-keys.v1",
      "source": { "file": "keys.json", "bytes": 0, "features": 346, "sha256": "<from proof/edition-sha256.txt>" },
      "licence": "Apache-2.0 (kuiper-belt); each quoted line keeps its repository's licence",
      "requires": ["keyPlace", "address", "o2", "line-card", "flyTo", "safeBox", "wafer"],
      "deeplink": { "param": "layers", "value": "lines" }, "module": "<module-stamp>-layers.js" } ] }
```
Every field is required except `deeplink`; `bytes` and `features` are measured by the build and checked at load (as
galaxies-wafers counts features against its index, layers-panel.mjs:400). `colour` must be one of PALETTE.md's hexes
and `meaning` must be that row's meaning (kuiper-belt@018b46a PALETTE.md:9-14: grey the record, cyan the instrument,
green energised, amber attention, magenta selected); "nothing is coloured for decoration. A shade must stand for a
stated, invertible quantity" (PALETTE.md:19), so a layer that needs a sixth colour asks the owner, it does not invent
one. A record's `requires` is checked by `tools/build_layers.py` to be a subset of the `requires` of the module named
in `module` (the module's list is the one the loader checks, 4.4); a record cannot promise a hook its module did not
ask for. `key` is the namespaced key in GridAtlas's sense (`layer:<id>`), the value of the
`data-ky-layer` attribute on the layer's original control, and the only attribute the registry dispatches on; no module
may create a `data-ky-layer`, `data-layer-id` or `data-pn-layer` control outside the registry (the Pipeline News rule).
`order` is the draw order, bottom first, kept as a separate list from the records exactly as `cartridge_order` is
(gridatlas@5ec7f62 atlas/current.json:14-21; E:A4.19). `substrate` names the wafer the keys belong to, so that a per-app
Kuiper of Addendum 1 (neural-link FIXES/NL-010/BRIEF.md:70-80, Team 4's step 8) can carry the same registry against
another substrate without a second format.

3.2 **The data format.** New layers are `code-feature-collection.v1`, galaxies-wafers' format: GeoJSON in shape,
geometry carrying keys never coordinates, `{"type":"Point","key":k}` and `{"type":"LineString","keys":[k1,k2]}`
(galaxies-wafers@fff6fc6 README.md:11-18). The verified-lines layer keeps `keys.json` as it is (`edition-keys.v1`:
`summary` + `bodies[]` with `key`, `on_wafer`, `verified`, kuiper-belt@018b46a editions/202611012027/index.html:629-632;
E:B2.3-B2.5) because the folder rule keeps `keys.json` byte-identical across editions (neural-link
SESSIONS/202611012145-kuiper-edition-harness-notes.md:43-45). Admission of a feature to the wafer is the edition's own
predicate, unchanged: finite key, `0 <= key < SPACE`, verified where the format has a `verified` field, then placed by
`keyPlace` and nothing else (index.html:632-633, :278; E:B2.5-B2.6, B1.11); what fails the predicate is counted and
named on the row, never placed (:649-651; E:B2.10), the seventh law (kuiper-belt@018b46a README.md:84).

3.3 **The registry module, `modules/<module-stamp>-layers.js`.** Registers through step 4's `KY.register` with
`provides: ["layers"]` and `requires` including `wafer` (the wafer's admission, 4.2) and `line-card` (Team 1's card
module, 3.3 last bullet). It builds the WAFER panel (`#layers`, registered through `KY.panels.add('wafer', el)`; the
title WAFER is Team 1's, GRID → WAFER at team-1/STEPS.md:146-153, LINES → WAFER + SCOPE + EDIT at :163) with one row per
record in `layers.json`, in `order`, grouped by `group` with a group title, each row a `<label>` holding the layer's
ORIGINAL `<input type=checkbox data-ky-layer="layer:<id>">`, stretched over the whole row as GridAtlas stretches its
proxy, a name, and a state tag. The panel answers NL-009's audit of today's LINES panel (neural-link
FIXES/NL-009/round1/05-lines.md): the list scrolls inside the panel, not the panel as one block (:16); every toggle row
is ≥ 44 px with the input over the whole row, not a 13 px box (:25); the filter field has a visible clear control and
Escape clears it (:40); a count line under the controls says `<shown> of <total> rows` (:54); rows are grouped, by
`group` for layers and by repository for the lines list (:58); the panel is full width on a phone, `left:0; right:0`
winning over any `width:min(…)` (:83). It exposes:
- `KY.layers.inspect()` → `{ layers, unique, complete, on: [ids], states: {id: WAIT|LOAD|OK|EMPTY|FAIL|REFUSED} }`,
  `complete` being `layers === unique === layers.json.layers.length && no empty key`, the five-part predicate of
  menu-bar.js:122-127 in Kuiper terms. Later modules write their contracts against this probe.
- `KY.layers.set(id, on)`: finds the original by `[data-ky-layer="layer:<id>"]` and, if its state differs, calls
  `original.click()`; nothing else flips a layer. The keyboard (`e`, `E`), the readout, the File menu, the See Through
  button, the URL and any app go through `set`. One delegated `change` listener on `#layers` is the single
  implementation of on/off (menu-bar.js:1451-1462 and :1723-1726 are the model).
- `KY.layers.get(id)` → the record plus its runtime state `{on, value, status, why, placed, total, loaded_sha256}`.
- `KY.layers.value(id, value)`: the one setter for a layer's value, the thing a layer shows when it has a choice: the
  lit repository (`repos`), the lit period (`periods`), the focus flag and the filter query (`lines`), the graph
  (`spider`). Team 1's SCOPE panel (focus, one repository, one period) and EDIT panel (filter, clear) are proxies that
  call `value` and `set` and read `get`; they own no state (team-1/STEPS.md:163; the proxy law of menu-bar.js:12-13).
  The `/` box's grammar (index.html:606-613) calls the same setter. A layer that is `on` with a null value is `OK · none
  lit` and draws nothing; `set('repos', true)` without a value is therefore not an error and opens nothing; `?layers=`
  carries ids only, never values (a value in a link is Team 3's hash grammar, 3.6).
- `KY.layers.register(record)`: for layers that arrive with a later module (See Through's stars from Team 3's step 5,
  elements and spider graphs from Team 4's step 7). The record must already be in `layers.json` with a `module` field
  naming the registering module; a module registering a layer the manifest does not list is refused with
  `layer <id> not in layers.json`; a listed layer whose module never registers it shows `WAIT · module <name> did not
  register` after the loader has finished (step 4), never a silent gap.
- The one draw hook. The registry calls `KY.draw.add(drawLayers)` once; `drawLayers` runs after the engine's
  `o2.clearRect` (index.html:384; E:B1.7) and iterates `order`, calling each on layer's `draw(o2, KY)`. The two wraps of
  Edition 4 (`draw` at :654, `drawEdition` at :745) and the `edNext` wrap (:747) are retired; the verified-lines layer
  becomes the first record and its draw function is `drawEdition` moved into the module, obeying its own `on`.
- The card is not this module's. Team 1's step 2 owns the card law and its module `<stamp>-line-card.js`
  (team-1/STEPS.md:255, :312, wrapping `edCard` and `fillLines`); `layers` lists `line-card` in `requires`, is admitted
  after it in `order` (4.5), and opens a line with `KY.modules['line-card'].api.show(body)` rather than owning the
  card's HTML. The `edCard` HTML of Edition 4 (index.html:655-667) therefore moves to Team 1's module, not to this one;
  `edFly`, the list and the stepping stay here.

3.4 **The state machine of a row** (galaxies-wafers' states, GridAtlas's suffix): `WAIT` listed, not asked for;
`LOAD` fetching; `OK · <placed> of <total>` placed; `EMPTY · <why>` loaded, nothing to place, the reason on the row;
`FAIL · <why>` the data did not load, hash, count or format failed; `REFUSED · <why>` the registry would not admit it
(licence unsettled, substrate mismatch, keys outside SPACE, module missing). The state is the label's suffix, as
GridAtlas keeps WAIT/LOAD/OK/FAIL in the label (E:A1.17), and is also written to the readout line that layer owns. A
layer with `preload: true` that is not `OK` after loading also changes the EDITION heading (`big`) to its `why` in words
(NL-009's finding: with keys.json served 404 the heading read `0 VERIFIED LINES LIT`, neural-link
FIXES/NL-009/round1/09-robust.md:25-29) and raises the `#refuse` strip, `role=alert`, that FABLE-09 added for the
missing-WebGL case (09-robust.md:18-22, patch lines :94-96). The wafer keeps drawing underneath: a layer failure never
stops the engine, as "Original controls remain available" (menu-bar.js:1763; E:A3.9).

3.5 **Loading, hashing, refusing.** On `on` (or at start when `preload`), the registry fetches `source.file` with
`cache: 'no-store'`, hashes the bytes with `crypto.subtle.digest('SHA-256')`, compares with `source.sha256`, compares
`byteLength` with `source.bytes` and the feature count with `source.features`, and on any difference sets `FAIL · sha256
mismatch` (or `bytes`, `features`) and draws nothing, the composer's rule applied to data (gridatlas@5ec7f62
atlas/index.html:75-81; E:A4.10-A4.11). An HTTP failure is `FAIL · <file> HTTP <status>`. A layer loads only after the
wafer admitted its own data: the module requires the hook `wafer` (4.2), a promise the page resolves to `{N, SPACE}`
once `N = issued; SPACE = k` has run (index.html:208, after the sum check at :206-207) and rejects with the refusal's
own words (`REFUSED: the commits of …` :207, or `… did not load. The wafer will not invent its keys.` :240); until it
settles every row is `WAIT · wafer`, and if it rejects every layer is `REFUSED · the wafer refused: <its words>`. This
replaces `loadEdition()` being called from inside the TSV promise (:219; E:B2.7, B4.6-B4.7). One fetch per URL, a
timeout on every fetch, as galaxies-wafers (layers-panel.mjs:29-30).

3.6 **The URL.** The ticked layers are the query parameter `?layers=<id>,<id>` (galaxies-wafers' grammar,
layers-panel.mjs:508-522; GridAtlas's deep links are query parameters, not hashes, Team 3 EVIDENCE.md:168), read once at
start through `KY.layers.set`, written with `history.replaceState` on every change. The parameter name `layers` is
reserved here; the full link grammar (what the hash carries: a key, a repository, a period, an edition, an app) is Team
3's step 6, which adopts this parameter. FINDING: the Kuiper's own pointer drops it today. `editions/index.html`
forwards only the hash, `location.replace('202611012027/' + location.hash)` (kuiper-belt@018b46a editions/index.html:12),
and its meta refresh carries nothing (:7), while GridAtlas's root forwards both,
`window.location.replace(target+window.location.search+window.location.hash)` (gridatlas@5ec7f62 index.html:2). So
`editions/?layers=lines,periods` opens with no layers. The fix is in the pointer law, Team 5's step 9 (9.1, the three
places): the pointer forwards `location.search + location.hash`, written by the integrator when the pointer moves to
Edition 5; the same forwarding is asked of `see-through/index.html` (:12, same idiom; E:B6.1) so a link into See Through
keeps its parameters. Step 3 test 6 opens through `editions/`, not only the dated folder.

3.7 **The first seven layers**, in `order` (draw order, bottom first), with what each is today and what admits it:

| id | key | label · group | draws | source today | licence | state at Edition 5 |
|---|---|---|---|---|---|---|
| `periods` | `layer:periods` | periods · THE WAFER | one annular band between `sqrt(k0)` and `sqrt(k1)` of the commits in a year, month or day, green | the engine's `lightTime(y,m,d)` (index.html:554-565; `litK`, `litCi` at :561) over `cosmos/wafer.tsv`; no file of its own, `source: {"engine": "../../cosmos/wafer.tsv"}`; the `/` grammar `2026-07` (:607-608) | Apache-2.0 (kuiper-belt) | OK when the wafer is; `on` means the band is shown, the period is the layer's `value` |
| `repos` | `layer:repos` | repositories · THE WAFER | the lit repository's commits, green, by the shader uniform `u_litRepo` (index.html:350, :154) and the point hot flag (:360) | `cosmos/repos.tsv`, 98 repositories (`wc -l` 99 with its header; kuiper-belt@018b46a cosmos/wafer-meta.json:7 `"repositories": 98`); `litRepo` (:243) becomes the layer's `value`; the readout's lit-repository lines (:371-378) become this row's suffix | Apache-2.0 (kuiper-belt); repository names only | OK when the wafer is; the `repo:<name>` self-test (:463-515) is its proof |
| `editions` | `layer:editions` | editions · THE WAFER | one amber ring at the radius of the first commit at or after each edition's cut stamp (`findBy('unix', …)` as `lightTime` does, :556), labelled with the number; tap opens that edition (Team 3's File: open an edition). An edition cut after the wafer's last commit has no such commit: it is counted and named on the row, drawn as an amber tick at the rim (`sqrt(SPACE)`) with the words `beyond the wafer's last commit`, never placed inside (the seventh law). Measured at kuiper-belt@018b46a: `last_unix` 1793539112 = 2026-11-01T13:18:32Z (cosmos/wafer-meta.json:9), so Editions 3 (202611012022) and 4 (202611012027) are beyond the rim and Editions 1 and 2 are placed | `data/editions.json`, built from `editions/README.md` (kuiper-belt@018b46a editions/README.md:12-24: 4 editions, stamps 202610311905, 202611010114, 202611012022, 202611012027) and the pointer (editions/index.html:7, :11, :12) | CC BY 4.0 (kuiper-belt data) | at the wafer of kuiper-belt@018b46a: `OK · 2 of 4 placed, 2 beyond the rim`; Edition 5 itself is a third beyond the rim until `cosmos/` is re-harvested |
| `lines` | `layer:lines` | verified lines · THE EVIDENCE | green sparks at their keys, bright green for `class: focus`, magenta when selected (index.html:645-648) | `keys.json`, 346 bodies, 344 on the wafer, hashed in `proof/edition-sha256.txt` (kuiper-belt@018b46a editions/202611012027/proof/edition-sha256.txt:4; E:B5.16) | Apache-2.0; each quoted line keeps its repository's licence (editions/202611012027/NOTICE.md:7-10) | OK · 344 of 346 (the two star-maker lines counted, not placed, README.md:48); `preload: true` |
| `see-through` | `layer:see-through` | See Through stars · THE APPS | cyan stars (the instrument) at the keys Team 3's step 5 assigns; tap deep-links into See Through | the record's `source.file`, `format` and `features` are Team 3's to write in step 5 (the registry names no other team's file); the registry admits `edition-keys.v1` and `code-feature-collection.v1` and refuses any other format in words (`REFUSED · format <x> not admitted`); today See Through's stars are "a line of code today, not a substation" placed by the same law (kuiper-belt@018b46a see-through/202610050609/descent.js:11; kuiper-law.js:7-10; E:B6.5) and the app reads no URL parameter (`grep -n 'location\.'` over descent.js and index.html at see-through/202610050609 finds nothing; Team 3 EVIDENCE.md:35-36) | CERN-OHL-S v2 for the app (see-through/202610050609/LICENSE.md:6; E:B6.3); ODbL for the substations (grid-data.js:7; E:B6.9) | first row of THE APPS and the largest label in the panel (the star player); `EMPTY · awaiting step 5 features` until Team 3's file exists, never absent from the list |
| `elements` | `layer:elements` | periodic table · THE APPS | one mark per `block:<Sym>` at the key of its first function line, grey (the record), amber when `state: UNSETTLED` (elements@f7a92fb ELEMENTS.md:7-13) | Team 4's step 7 writes the file and names it (its draft: `data/elements.json`, team-4/STEPS.md:186); the registry admits it when its `format` is `code-feature-collection.v1` and refuses any other in words on the row; the catalogue keys its functions by `line:<n>` of the 250,174-line numbered database (elements@f7a92fb README.md:16-17, ELEMENTS.md:3), which is galaxies-wafers' key space, not the Kuiper's 63,340,120,796-key address space (cosmos/wafer-meta.json:4); the mapping `line:<n>` → `repo@commit path:line` → Kuiper key by `tools/edition_keys.py` (:12) is Team 4's to build and prove | **unsettled**: no LICENSE file at elements@f7a92fb (`ls`: APPS.md CATALOGUE.md ELEMENTS.md README.md SURFACES.md build catalogue functions inputs tests; E:B6.17), Team 5's register | `REFUSED · licence unsettled (elements@f7a92fb has no LICENSE)` until Team 5 settles it; then `EMPTY · awaiting step 7 keys` until the mapping exists; listed from Edition 5 |
| `spider` | `layer:spider` | spider graphs · THE APPS | nodes as grey marks, edges as `LineString` key pairs drawn as chords, one graph at a time, the graph being the layer's `value` | Team 4's step 7 writes the files and names them (its draft: `data/graphs/overview.json`, `data/graphs/periodic-table.json` in `receiver-graph-v1` node/edge JSON, team-4/STEPS.md:166, :186); the registry admits a graph only as `code-feature-collection.v1` (nodes as Points with keys, edges as LineStrings with key pairs) and shows `REFUSED · format receiver-graph-v1 not admitted` otherwise, so the conversion is Team 4's or a later edition adds the format to the registry, and the disagreement surfaces on the row, not in a merge; built from the receiver manifest (testcode@d09c185 spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/spider/manifest.json:2 `receiver-manifest-v1`, 16 graphs incl. `periodic-table` at :57); node ids `family:N` and `block:<Sym>` need the same key mapping as elements | Apache-2.0 (testcode@d09c185 LICENSE:1); the graphs' own data is read live over https from other repositories, each named in the manifest entry | `EMPTY · awaiting step 7 keys`; the `?graph=<id>&focus=` grammar (v5 index.html:212) is the tap's deep link into the spider |

Two layers above (`periods`, `repos`) have no file: their source is the wafer itself, their proof is `ci_check` K2
(kuiper-belt@018b46a tools/ci_check.py:9) and the engine's own self-tests (`?selftest=2026-07` at index.html:220-235,
`?selftest=repo:<name>` at :238-239). The registry treats `source.engine` as admitted iff `N > 0 && SPACE > 0`.

3.8 **What the registry does not do.** It does not place anything: `keyPlace` is the only placement (E:B1.11). It does
not store x,y in any file (the format forbids coordinates; the Edition 4 `Object.assign({}, b, {x,y})` at :633 stays
as the run-time place and nothing else). It does not add bar titles: FABLE-01 measured the bar at 416.6 px of content
against 344-414 px available, two rows on every phone (neural-link FIXES/NL-009/round1/01-bar.md:13-17); the layers
live behind ONE title, as GridAtlas keeps 63 behind Grid; that title is WAFER, Team 1's mapping of GRID
(team-1/STEPS.md:146-153), adopted here for the owner's "keep it consistent". It does not decide licences (Team 5), deep links (Team 3)
or which app keys exist (Team 4); it refuses what they have not yet settled, in words, on the row.

**Module.** `editions/<stamp>/modules/<module-stamp>-layers.js` (the registry, the WAFER panel, the verified-lines
layer's draw, list, filter, stepping and `edFly` moved in from the page; the card stays Team 1's), `editions/<stamp>/
data/layers.json`, `editions/<stamp>/data/editions.json`; `tools/build_layers.py` (writes `layers.json` records' `bytes`,
`features`, `sha256` from the files, refuses a key outside `SPACE`, a colour outside PALETTE.md, or a record `requires`
not within its module's, as galaxies-wafers' builder "refuses to write a key the numbered database does not contain",
README.md:18); `tools/edition_check.py` E2/E6 of Team 5's step 9 extended to `data/*.json` hashes. Opus team 3 in Team
5's plan (`modules/03-layers.js` there; the name is reconciled in 4.3).

**Acceptance test on Android** (Playwright, pre-installed Chromium, `--use-gl=angle --use-angle=swiftshader
--enable-unsafe-swiftshader --ignore-gpu-blocklist`, `devices['Pixel 7']` and `devices['Galaxy S24']`, `hasTouch`,
served from the kuiper-belt root, 8 s after load and after each fly; the method of neural-link
FIXES/NL-009/round1/BRIEF.md:11-20):
1. Open `editions/<stamp>/`. `KY.layers.inspect()` returns `layers: 7, unique: 7, complete: true`; `#layers` holds 7
   `input[data-ky-layer]`, every value distinct and of the form `layer:<id>`; `document.querySelectorAll('[data-layer-id],
   [data-pn-layer]').length === 0`.
2. Tap the WAFER title: the panel opens under the bar (`placePanels`), its rect spans the viewport width on both
   devices (`left <= 0.5`, `right >= innerWidth - 0.5`; 05-lines.md:83), each layer row's
   `getBoundingClientRect().height >= 44` and its input's rect covers the row (05-lines.md:25), each row shows a state
   tag, the `lines` row reads `OK · 344 of 346`, the `editions` row reads `OK · 2 of 4 placed, 2 beyond the rim` at
   kuiper-belt@018b46a's `cosmos/` (3 beyond once Edition 5 is in `editions.json`), and the lines list scrolls inside
   the panel: with 344 rows the panel's own `scrollHeight` equals its `clientHeight` and the list element's does not
   (05-lines.md:16); a count line reads `344 of 344 rows`, and after typing `gridatlas` in the filter it reads the
   filtered count and the clear control empties the field and restores 344 (05-lines.md:40, :54).
3. `page.touchscreen.tap` at the centre of the `lines` row (not on the checkbox): `KY.layers.get('lines').on === false`,
   the readout gains `verified lines layer off`, and the overlay pixel at `edScreen(edPlaced[0])` is no longer green
   (read `o2.getImageData` at that point: G < 120 or not > R + 40); tap again: back to `OK`, green returns. Tap the
   `repos` row with no value: it reads `OK · none lit`, nothing new is drawn, no error.
4. Serve `keys.json` as HTTP 404: the `lines` row reads `FAIL · keys.json HTTP 404`, `#big` text contains `KEYS.JSON
   DID NOT LOAD`, `#refuse[role=alert]` is visible, the wafer canvas centre pixel is not black (the engine still draws),
   `pageerror` count 0, and `e` does not move the camera (no fly).
5. Serve a `keys.json` with one byte changed: row `FAIL · sha256 mismatch`, zero sparks drawn (no green pixel at any
   `edScreen` of the original 344 places), alert visible.
6. Open `editions/?layers=lines,periods` (through the pointer, not the dated folder) and `editions/<stamp>/?layers=
   lines,periods`: in both, `inspect().on` equals `['periods','lines']` in `order` order; untick `periods`: the URL
   becomes `?layers=lines` without a reload (`history.replaceState`). The first case passes only once the pointer
   forwards `location.search` (3.6, Team 5's step 9); until then it is recorded FAIL with that key.
7. `/` + `gridatlas` + Enter (which calls `KY.layers.value('repos', 'gridatlas')` and `set('repos', true)`): the `repos`
   row reads `OK · gridatlas` and the pixel test of `?selftest=repo:gridatlas` (index.html:463-515) still passes,
   `window.__selftest.PASS === true`; SCOPE's "one repository" control shows `gridatlas` ticked (it reads `get`, it owns
   nothing).
7b. Serve `../../cosmos/wafer.tsv` as HTTP 404: every row reads `REFUSED · the wafer refused: ../../cosmos/wafer.tsv did
   not load…`, the bar and the alert strip are present, `pageerror` 0.
8. The `see-through`, `elements` and `spider` rows are present with `EMPTY` or `REFUSED` and a non-empty `why`; no row is
   blank; the `see-through` row is the first of THE APPS and its label's font-size is the largest in the panel
   (computed style, measured).
9. `python3 tools/ci_check.py` prints `RESULT: PASS`; `node --check` on `modules/<stamp>-layers.js` exits 0; every
   `data/*.json` hashes to its `layers.json` record.

**Licence note.** The registry and its module: Apache-2.0 as kuiper-belt code; `layers.json`, `editions.json`: CC BY
4.0 as kuiper-belt data (kuiper-belt@018b46a README.md:157). Each record carries its own `licence` string, verified by
Team 5's register; a record with an empty or unsettled licence is listed `REFUSED · licence unsettled` and places
nothing (elements, until Team 5 settles it). See Through's layer names CERN-OHL-S v2 and ODbL on its row; the spider's
names Apache-2.0 and the licences of the graphs it draws.

**Opus team brief** (one team of four, step 3). You own `modules/<module-stamp>-layers.js`, `data/layers.json`,
`data/editions.json`, `tools/build_layers.py`, and the move of the verified-lines draw, list, filter, `edFly` and `e`/`E`
from the page into the module (index.html:626-654, :676-692, :705-709, :728-749; the card :655-674 goes to Team 1's
card module), keeping every behaviour NL-009 patched. You
touch `index.html` only to delete what you moved; the hook table is step 4's and you file a REQUEST on #10 for any hook
you need that it lacks. You do not touch `keys.json`, `cosmos/`, the placement law, the bar's titles (Team 1), the
link grammar beyond `?layers=` (Team 3), or any app's data (Team 4). You prove tests 1-9 on Pixel 7 and Galaxy S24,
with screenshots of the panel in WAIT, OK, FAIL and REFUSED, and you post one FINDING on #10 with the measurements.
Your module's `requires` list is exactly the hooks you call; the loader will refuse you if it is not.

---

## Step 4. The Kuiper cartridge format and the module boundary

**Goal.** Every feature the Opus teams build for an edition is one stamped file under `editions/<stamp>/modules/`,
listed with its sha256 in `editions/<stamp>/modules.json`, admitted by the page in manifest order only after its bytes
hash as recorded and every hook it requires exists, isolated in its own script element, registering itself through one
call, touching nothing but the hook table and its own host, and refused in words, in the readout and in an alert, for
any of: missing file, hash mismatch, stamp mismatch, missing hook, no registration, an install that throws. The page
without any module is a whole, working wafer. The modules are the only place code accumulates between editions, and
each is small enough to hold in your head.

**GridAtlas lesson (with keys).**
- The composer: a 124-line stable page that fetches `current.json` (`cache: 'no-store'`), checks schema, architecture
  and registry shape (gridatlas@5ec7f62 atlas/index.html:39-44; E:A4.1-A4.4), composes cartridges in `cartridge_order`,
  refuses a missing id (:65-67), accepts two slot kinds only (:62), demands an `after-cartridge` anchor already composed
  (:73), a 64-hex sha256 (:75), hashes the fetched bytes in the browser and refuses a mismatch (:78-81), turns the
  verified bytes into a blob-URL script tag stamped with the cartridge id (:82-83), refuses a slot or anchor not found
  exactly once (:92, :96), publishes `window.__GRIDATLAS_ATLAS__` with `loaded_cartridges: [{id, sha256}]` (:104-114),
  and on any invariant failure shows one screen, `GRIDATLAS COMPOSITION FAILED … The immutable shell was not changed`
  (:32-36; E:A4.16-A4.17).
- The record: `id`, `generation` (UTC minute), `version`, `type`, `slot`, `path` with the stamp in the file name,
  `sha256`, `contract`, `capabilities`, `immutable_shell_modified: false` (gridatlas@5ec7f62 atlas/current.json:24-41;
  E:A4.20-A4.28); later modules add `bytes`, `byte_budget`, `module_generation` (:642-644, :725-727), `reads_at_runtime`
  naming every global and DOM surface read and how it waits for it (:650-656, :737-746), `writes` naming the one
  namespace written (:657-659, :747-750), `isolation` ("its own script element: a parse or top-level error in the
  overlay no longer stops sld-sandbox", :660, :751), and a `contract` line saying which attributes it creates none of
  (:687). The contracts block makes the rules explicit: `cartridge_sha256_required`, `cartridge_order_explicit`,
  `shell_mutation_forbidden` (:825-830).
- Admission by a late module: install nothing until every dependency is present, publish `waiting_for` meanwhile, and
  after a bounded retry publish a loud failure (menu-bar.js:35, :1647-1656, :1752-1768, :1787-1797; E:A3.1-A3.11); the
  lightning overlay does the same against the menu bar's `installed`, the pipeline layers, the map and the groups
  (gridatlas@5ec7f62 atlas/modules/202610291043-uk-lightning-overlay.js:393-394) and publishes one frozen API
  `NS.ukLightning = Object.freeze({schema, generation, state, install, setOn, load, windowFor})` (:400) under the one
  namespace `window.__GRIDATLAS_MODULES__` (:7), returning at once if already installed (:8). A proof stub without a
  full DOM is refused, not retried (menu-bar.js:1770-1783; E:A3.10).
- The file: a cartridge is written as a new timestamped file beside the previous one and never rewritten
  (gridatlas@5ec7f62 atlas/cartridges/README.md:3-7); `tools/build-cartridge.mjs` assembles it from named parts,
  records each part's SHA-256 and refuses a missing part or a generation that already exists (tools/build-cartridge.mjs:
  1-14); the cartridge's header says it is assembled and must not be edited (E:A4.30). FINDING carried into this step
  (E:A4.32-A4.33): the live substation-intelligence cartridge's header says generation `202609060259` while its file
  name and `current.json` say `202609062358`; a stamp written twice drifts. The Kuiper writes the stamp once in the file
  name and once in the module's registration, and the loader refuses when they differ.
- The gate: the PR gate walks `cartridge_order`, requires each record, a path inside `atlas/`, an existing file and a
  matching sha256 (gridatlas@5ec7f62 tools/ci/pr-gate.mjs:170-179); the release flow re-hashes every cartridge before
  the pointer moves (docs/RELEASE.md:117; E:A5.9); the release folder carries `sha256sums.txt` (E:A4.39).
- The boundary: "One module, one responsibility, one proof, one public surface"; a module registers itself on a
  namespace, does not reach into another module's internals and touches the DOM only when rendering is its
  responsibility; a cartridge is a manifest of modules, not a place where code accumulates; a module is small enough to
  hold in your head, and if its proof needs three stubs the boundary is wrong; shared modules are shared, not copied
  (gridatlas@5ec7f62 governance/202609011940-modular-architecture-and-domain-map.md:26-49; E:A4.34-A4.37).
- The anti-lesson, in the Kuiper's own family: Learn the Kuiper loads its modules with `onerror="this.remove()"` and the
  comment "a missing file is skipped" (kuiper-belt@018b46a learn-the-kuiper/202610050609/modes.html:16-24), the host
  filters `window.KGModules` for anything with an `id` and an `open` (start-here.js:464), and only a tap says `X IS NOT
  LOADED HERE` (:467). Nothing is hashed, nothing is ordered, nothing is refused at load. See Through inherits the same
  `KGModules.push` (see-through/202610050609/descent.js:1073; E:B6.6). The Kuiper edition does the opposite.
- The Kuiper already names the thing: "a cartridge in the sense the wafer already uses: one small module, its own data,
  its own proof, loaded on demand. It does not grow for ever, and it does not know about any other cartridge"
  (kuiper-belt@018b46a SPEC.md:3-5; E:B5.6-B5.7).

**Kuiper change.**

4.1 **Where the boundary is today, measured.** The Edition 4 page is the engine plus an inline edition layer. The
script of kuiper-belt@018b46a index.html:102-590 and editions/202611012027/index.html:130-619 differ in exactly three
hunks (`diff` of those ranges; the engine's :591-594 are `requestAnimationFrame(frame)` and the closing tags, which the
edition repeats at :750-753): the two `cosmos` paths (engine :173 / edition :201 and :212 / :240) and the call
`loadEdition()` appended at engine :191 / edition :219. Everything from edition :620 to :749 is the edition layer, in
the engine's scope, reaching the engine by wrapping its functions (`draw` :654, `safeBox` :726, `drawEdition` :745,
`edNext` :747) and by writing its module-level variables directly (`litRepo` :665, `target` :666, `dirty` :666). A
separate file cannot do that: module-level `let`s are not reachable from another script. So the hook table is not an
option, it is the precondition of having modules at all.

4.2 **The hook table, `window.KY`**, built by the page (integrator) immediately after the engine's definitions and
before any module loads, frozen:
```js
window.KY = Object.freeze({
  schema: 'kuiper.hooks.v1', edition: '<stamp>',
  hooks: Object.freeze({                 // read-only functions and elements of the engine
    keyPlace, address, describe, findBy, flyTo, home, homeCamera, safeBox, lightTime, showNew, goKey, fmt, words, esc,
    cv, ov, o2, hud, big, sub, card, gbox, gin,
    get SPACE(){ return SPACE }, get N(){ return N }, get repos(){ return repos }, get commits(){ return commits },
    wafer /* a Promise: resolves {N, SPACE} right after index.html:208; rejects with the refusal's words (:207, :240) */ }),
  cam: { get x(){return cx}, get y(){return cy}, get zoom(){return zoom}, get atHome(){return atHome} },
  lit: { get repo(){return litRepo}, set repo(v){ litRepo = v; dirty = true },
         get K(){return litK}, get Ci(){return litCi}, set period(p){ /* lightTime result or null */ } },
  sel: { get target(){return target}, set target(t){ target = t; dirty = true } },
  redraw(){ dirty = true },
  draw: { add(fn, order){ /* one wrap of draw, owned by the page; fns run after o2.clearRect in ascending order */ } },
  panels: { add(name, el, title){ /* PANELS[name] = el; the bar title is Team 1's; setPanel/placePanels as Edition 4 */ },
            set: setPanel, place: placePanels },
  names: Object.freeze([ /* the admissible set, 4.2 */ ]),
  register(module){ /* 4.4: a closure of the loader, see there */ }, modules: {}, inspect(){ /* 4.6 */ } });
window.__KUIPER_MODULES__ = KY.modules;   // the alias Team 1's modules probe (team-1/STEPS.md:339)
```
One rule for what `requires` may name, applied by the loader and by E6 alike: the admissible set is
`Object.keys(KY.hooks)` ∪ `['cam', 'lit', 'sel', 'redraw', 'draw', 'panels']` ∪ the `provides` of modules admitted
earlier in `order`, and nothing else. `Object.keys(KY.hooks)` at Edition 5 is this list, in this order, and test 7
asserts it: `keyPlace, address, describe, findBy, flyTo, home, homeCamera, safeBox, lightTime, showNew, goKey, fmt,
words, esc, cv, ov, o2, hud, big, sub, card, gbox, gin, SPACE, N, repos, commits, wafer` (28 names). `KY.names` is that
set without the `provides`, frozen, so a module can read what it may ask for. The page's hook table is the Kuiper's
`inventory()`: the loader computes the set once and admits modules against it. Adding a hook is an edition change by
the integrator; removing one is forbidden while any module in `modules.json` requires it (checked by E6 below). The
`wafer` hook is how the wafer's admission becomes a dependency a data module declares and the shell does not (point 2
of REVIEW.md round 1): the bar and the card never wait on the 535,037-byte `cosmos/wafer.tsv` (`ls -l` at
kuiper-belt@018b46a) and are present when it refuses. Hooks named here that exist in Edition 4: `keyPlace` :278, `address` :282,
`describe` :284, `findBy` :280, `flyTo` :253, `home` :277, `homeCamera` :272, `safeBox` :262 (wrapped at :726; the
wrap moves into the page so the hook is the wrapped one), `lightTime` :554, `showNew` :420, `goKey` :416, `fmt`/`words`
:126, `esc` :681, `cv`/`ov`/`o2` :121, `hud`/`big`/`sub` :123, `card` (:91 `#card`), `gbox`/`gin` :604, `cx cy zoom
dirty tween litRepo target` :243, `litK litCi` :244, `atHome` :245, `setPanel` :714, `placePanels` :712, `PANELS` :710.

4.3 **The file.** `editions/<stamp>/modules/<module-stamp>-<name>.js`: `<module-stamp>` is the UTC minute the module was
cut, `YYYYMMDDHHMM`, `<name>` lower-case words and hyphens; a classic script (no `type="module"`, no `import`: one file
is the unit the loader hashes, as GridAtlas's slot takes one file, build-cartridge.mjs:4-9), wrapped in one IIFE with
`'use strict'`, no top-level identifier but what the IIFE declares. Its first line is a comment naming the module and
the licence only, `/* kuiper module <name>, Apache-2.0 (kuiper-belt) */`: the stamp lives in exactly two places, the
file name and the `generation` of the registration (4.4), and the loader and E6 compare those two; a header stamp
would be a third copy and E:A4.32 is the lesson that a stamp written twice drifts. A module is never edited after it is
listed in a published edition: a change is a new file with a new stamp (cartridges/README.md:3-7). A module cut for
Edition 5 may be carried into Edition 6 byte-identical, same file name, same sha256, as GridAtlas carries cartridges
across generations (`current.json` generation `202610292044` lists a cartridge of generation `202609241251`,
atlas/current.json:3, :25). This is why the stamp, not a step number, is in the name: the number is a property of one
edition's `order`; the stamp is the module's identity across editions. Two teams write it this way already (Team 1:
`<stamp>-kuiper-shell.js`, `<stamp>-line-card.js`, team-1/STEPS.md:200, :312) and two write `modules/NN-<name>.js`
(team-5/STEPS.md:15, :219-224; team-4/STEPS.md:17, :186). So that the Opus teams never hold two names: a module's
identity to the loader is `generation` + `sha256` in `modules.json`, whatever the file is called; the file-name check
applies when the name begins with twelve digits and a hyphen (`/^\d{12}-/`), and then the digits must equal
`generation`; and the default, if Team 5B does not rule otherwise in ROADMAP.md, is `<module-stamp>-<name>.js`, with
the step number as the manifest field `team` and the order in `modules.json`. If Team 5B keeps `NN-`, the law must say
how a byte-identical module keeps its identity when it is renumbered (answer under this scheme: by `generation` +
`sha256`, which do not change).

4.4 **The registration call.** A module's only side effect at parse time is one call:
```js
KY.register({ schema: 'kuiper.module.v1', id: 'layers', generation: '<module-stamp>',
  requires: ['keyPlace','address','o2','card','flyTo','safeBox','wafer','panels','draw','redraw','lit','line-card'],
  provides: ['layers'],
  install(KY){ /* builds its host <div id="ky-layers">, its panel, its listeners; returns its public API */ },
  inspect(){ /* returns its state, like menuBar.inspect() */ } });
```
`KY.register` does not install. It is a closure over the loader's own `let admitting = null`: the loader sets that
variable to `{id, path, sha256}` before injecting the script and clears it after, and `register` records the
registration against it. Nothing is ever assigned onto `KY` after `Object.freeze` (the Edition 4 page script has no
`'use strict'`, `grep -c "'use strict'"` = 0 at kuiper-belt@018b46a editions/202611012027/index.html, so a write to a
frozen object there would be a silent no-op, which is why the state is held in the closure and not on the table). The
loader then checks: the registered `id` equals the manifest id; `generation` equals the manifest's and, when the file
name begins with twelve digits, those digits (4.3); every name in `requires` is in the admissible set of 4.2 (the hook
table's names or a `provides` of a module admitted earlier in `order`; GridAtlas's `after-cartridge anchor … is not
composed before it`, atlas/index.html:73); then calls `install(KY)` inside `try`; on success writes
`KY.modules[id] = Object.freeze({ id, generation, sha256, api, inspect })` (the lightning overlay's frozen API, :400) and
the readout line `<id> admitted · <sha256 first 12>`. Nothing else is a module.

4.5 **The manifest, `editions/<stamp>/modules.json`**, the edition's `current.json`, integrator-owned:
```json
{ "schema": "kuiper.modules.v1", "edition": "<stamp>", "hooks": "kuiper.hooks.v1",
  "order": ["kuiper-shell", "line-card", "layers", "see-through", "file", "apps", "<algorithm>"],
  "modules": [ { "id": "layers", "generation": "<module-stamp>",
      "path": "modules/<module-stamp>-layers.js", "sha256": "<64 hex>", "bytes": 0, "byte_budget": 65536,
      "requires": ["keyPlace", "address", "o2", "card", "flyTo", "safeBox", "wafer", "panels", "draw", "redraw", "lit", "line-card"],
      "provides": ["layers"], "reads": ["data/layers.json", "keys.json", "data/editions.json"],
      "writes": ["window.KY.modules.layers", "#ky-layers", "#layers"],
      "creates_controls": "data-ky-layer only", "licence": "Apache-2.0", "team": "03", "step": 3,
      "proof": "proof/handoff/03-layers/" } ],
  "contracts": { "module_sha256_required": true, "order_explicit": true, "engine_mutation_forbidden": true,
                 "stamp_in_name_equals_generation": true, "hooks_frozen": true } }
```
`order` is a separate list from the records (A4.19); `requires`, `reads`, `writes` are GridAtlas's `reads_at_runtime`
and `writes` (atlas/current.json:650-659) made checkable; `byte_budget` as :643. The same sha256 appears in
`proof/edition-sha256.txt` for the same path (E:B5.15); E3 cross-checks the two.

4.6 **The loader**, in the page, started as soon as `window.KY` is built, before the `cosmos` fetch returns: GridAtlas
composes every cartridge first and each module waits for its own inventory (menu-bar.js:1647-1656 `waiting_for`;
E:A3.1-A3.6), so the shell and the card are admitted and visible while the 535,037-byte `wafer.tsv` loads, and stay
when it refuses; a module that needs the wafer lists `wafer` in `requires` and awaits that promise inside its own
`install` (3.5). The loader:
1. `fetch('modules.json', {cache:'no-store'})`; refuse the whole edition's modules on a wrong `schema`, `hooks` version
   or shape (one `#refuse` strip, `MODULES NOT ADMITTED: <why> · the wafer is unchanged`), the composer's one screen
   (atlas/index.html:35) scaled down to a page that still draws.
2. For each id in `order`: find the record (else `refused: in order but not in modules`), check `path` starts with
   `modules/` and has no `..`, `generation` is twelve digits and, when the file name begins with twelve digits and a
   hyphen, equals them (4.3), `sha256` is 64 hex; `fetch(path,
   {cache:'no-store'})` (`refused: HTTP <status>`); `crypto.subtle.digest` (`refused: sha256 mismatch`); `byteLength`
   against `bytes` and `byte_budget`; then inject `<script data-ky-module="<id>" src="blob:…">` as its own element and
   await its load, so a parse error or a top-level throw in one module cannot stop the next (GridAtlas isolation,
   current.json:660); then the registration checks of 4.4 (`refused: no registration`, `refused: id <x> ≠ <id>`,
   `refused: generation <a>, file name <b>`, `refused: missing hook <name>`, `refused: install threw <message>`).
3. Publish `window.__KUIPER_EDITION__ = { schema, edition, hooks, order, admitted: [{id, sha256}], refused: [{id,
   why}] }` (as `window.__GRIDATLAS_ATLAS__`, atlas/index.html:104-114) and `KY.inspect()` returning the same; write
   one readout line per module; if `refused` is non-empty, raise `#refuse` with `<n> module(s) refused: <ids and whys>`,
   `role=alert`, and keep the wafer, the bar and every admitted module working ("Original controls remain available").
4. Admit no module twice (the schema-and-return rule, menu-bar.js:37-38; lightning :8). Admit nothing outside `order`
   (a stray file in `modules/` is an E2 failure before the PR, and is never fetched by the page).

4.7 **What a module may touch.** Only: the hook table (`KY.hooks`, `KY.cam`, `KY.lit`, `KY.sel`, `KY.redraw`,
`KY.draw.add`, `KY.panels`), the APIs of modules it names in `requires` (`KY.modules.<id>.api`), its own host element
`#ky-<id>` which it creates and may remove, a panel element it registers through `KY.panels.add`, the files it names in
`reads`, and the globals it names in `writes`. It draws only on `o2` from a function given to `KY.draw.add`, never on
`cv`'s WebGL context. It flips a layer only through `KY.modules.layers.api.set`. It opens same-host apps in the same
tab (NL-009's decision, neural-link FIXES/NL-009/round1/06-seethrough.md:51) and off-host links with
`rel="noopener"`.

4.8 **What a module may not touch.** It may not reassign or wrap any engine function (`draw`, `safeBox`, `frame`,
`drawEdition`, `edNext`: the Edition 4 idiom is retired; `KY.draw.add` is the one seam); may not read or write an engine
variable except through `KY.cam`/`KY.lit`/`KY.sel`; may not create a `data-layer-id`, `data-pn-layer` or `data-ky-layer`
control, or a `.gm-title` in the bar (Team 1's shell owns titles; a module asks for a panel); may not fetch anything
not in `reads`, write any global not in `writes`, define a top-level name, use `import`/`type="module"`, `eval`,
`document.write`, `localStorage`, a timer loop that polls the DOM (the hook table makes GridAtlas's 40-second retry
unnecessary: if the hook is missing the module is refused at once), `target="_blank"` on the same host, or any colour
outside PALETTE.md; may not touch `keys.json`, `cosmos/`, the pointer, another module's host, or `index.html`; may not
exceed `byte_budget`; may not carry its stamp anywhere but the file name and `generation`; may not catch and swallow a
failure of its own data (it reports it through the layer state or `KY.modules.<id>.inspect().failures`, as
`failures: []` in pipeline-news-layers.js:112).

4.9 **Checks before the PR**, folded into Team 5's `tools/edition_check.py` (team-5/STEPS.md:79-81 E1-E5): E6 every file
in `modules/` is listed in `modules.json`, its record's `generation` is twelve digits and equals the file name's
leading digits when the name has them, its `licence` is non-empty, and its `requires` ⊆ the admissible set of 4.2 (the
hook table's names are read from the page's `KY.names` literal with the same regex K3 uses to find the script,
kuiper-belt@018b46a tools/ci_check.py:71, plus the `provides` of earlier records); E7 every `writes`/`reads` entry is matched by a literal in the file
and no `fetch(` literal in the file is outside `reads`; E8 `node --check` on every module and `grep -c "KY.register("`
equals 1. FINDING for Team 5: `tools/ci_check.py` K3 parses only root-level `*.html` (`os.listdir(ROOT)` at
tools/ci_check.py:68) and only the first `<script type="module">` (:71); editions' pages and `modules/*.js` are not
parsed by CI today. E1 as Team 5 drafts it closes that.

4.10 **What this gives the Opus teams.** A team writes one file, one data file, one proof folder, and a `modules.json`
record for the integrator; it can test its module alone against a page with an empty `modules.json` plus its own
record, and against the page with every record; the loader's readout tells it in one line whether it was admitted and,
if not, exactly why. A team that needs a hook the table lacks files a REQUEST on #10 naming the engine line it needs
(as this file does at 4.2); the integrator adds it as a new key and bumps nothing else.

**Module.** The hook table and the loader live in `editions/<stamp>/index.html` (integrator; Opus team 4 writes them
as `modules/<module-stamp>-loader.js` for review and the integrator moves the code into the page, since the loader
cannot load itself; Team 5's plan says the same, team-5/STEPS.md:253); `editions/<stamp>/modules.json`;
`tools/edition_check.py` E6-E8; a reference module `modules/<module-stamp>-hello.js` (twenty lines: registers, draws one
cyan ring at `keyPlace(0)`, exposes `inspect`) that every team's tests load first to prove the loader against a known
file, and which is removed from `order` before PR A (its sha256 stays in `proof/handoff/04-loader/`).

**Acceptance test on Android** (same rig as step 3):
1. With `modules.json` listing every module of the edition: `window.__KUIPER_EDITION__.admitted` has one entry per
   `order` entry, in that order, each `sha256` equal to the manifest's, `refused` is empty, `#refuse` is absent, the
   readout has one `admitted` line per module, `pageerror` count 0.
2. One byte changed in `modules/<module-stamp>-layers.js` (served, not committed): `refused: [{id:'layers', why:'sha256
   mismatch'}]`, every other module admitted, `#refuse[role=alert]` visible and readable at 360 px (its rect inside the
   viewport), the wafer canvas centre pixel non-black, the bar present, `pageerror` 0.
3. One module's record with `requires: ['noSuchHook']`: `refused … missing hook noSuchHook`; the module's host
   `#ky-<id>` absent; later modules that do not require it admitted; one that requires its `provides` refused with
   `missing hook <name>`.
4. A module file renamed so the twelve digits in its name differ from `generation` (and `path` updated to match):
   `refused … generation <a>, file name <b>`; renamed to a name with no leading digits: admitted (identity is
   `generation` + `sha256`, 4.3).
5. A module whose `install` throws (the hello module with a thrown `Error('test')`): `refused … install threw test`,
   all others admitted.
6. The module file deleted from the served folder: `refused … HTTP 404`.
7. `modules.json` emptied to `"order": [], "modules": []`: the wafer draws, `admitted: []`, no alert; `KY` is frozen
   (`Object.isFrozen(window.KY) === true`), `Object.keys(KY.hooks)` equals the 28-name list in 4.2, and
   `window.__KUIPER_MODULES__ === KY.modules`. Then, with the full manifest and `../../cosmos/wafer.tsv` served as
   HTTP 404: the bar (Team 1's `kuiper-shell`) and the card module are `admitted`, the refusal strip shows the engine's
   words (`did not load. The wafer will not invent its keys.`, index.html:240), `layers` is admitted but every row reads
   `REFUSED · the wafer refused: …`, and the time from `load` to the shell's `admitted` line is recorded with the
   `wafer.tsv` fetch still pending (the shell did not wait for 535,037 bytes).
8. `python3 tools/edition_check.py` E1-E8 PASS on the committed folder, and FAIL on each of the served mutations above
   when applied to a copy (hash, stamp, requires, stray file in `modules/`).
9. Measured and recorded, no threshold: time from `load` to the last `admitted` line on Pixel 7 under SwiftShader, and
   the sum of module `bytes` against the sum of `byte_budget`; both written into `proof/handoff/04-loader/`.

**Licence note.** The loader, the hook table and every module: Apache-2.0 as kuiper-belt code (kuiper-belt@018b46a
README.md:157); `modules.json` and `proof/`: CC BY 4.0. A module's record carries its own `licence` (SPDX string or the
exact non-SPDX name, e.g. `CERN-OHL-S-2.0` for code taken from See Through); a module whose `licence` is empty fails
E6 before the PR, and the loader refuses it at run time (`refused: no licence`). Code copied from GridAtlas's modules
(the menu-bar idioms) is Apache-2.0 under gridatlas's LICENSE and is cited by `repo@sha path:line` in the module's
header, as kuiper-law.js cites the engine (see-through/202610050609/kuiper-law.js:1-10).

**Opus team brief** (one team of four, step 4). You own the hook table (written as a patch to `index.html` that the
integrator applies), the loader (`modules/<module-stamp>-loader.js` as the reviewable reference, moved into the page by
the integrator), `modules.json`'s schema and the integrator's first record set, `tools/edition_check.py` E6-E8, the
hello module, and this step's tests 1-9 on Pixel 7 and Galaxy S24 with screenshots of tests 1, 2 and 7. You do not
touch the engine below the hook table, `keys.json`, `cosmos/`, the bar's titles (Team 1), any layer (Team 3 of the Opus
plan) or the link grammar (Team 6). You are admitted first in the integrator's order (team-5/STEPS.md:262-267) because
every other module is tested against you; you therefore publish your hook-table key list on #10 as a FINDING before
any other team's module is cut, and you add a key only by a new FINDING naming the engine line it exposes.

---

## Open items this team hands to others (DISCLOSED, not resolved here)

- Team 1: the name of the layers' title in the bar (Grid → LAYERS proposed) and the `KY.panels.add` hook's exact shape;
  the bar must stay one row at 360 px with it (neural-link FIXES/NL-009/round1/01-bar.md:13-17).
- Team 3: the features of `data/see-through.json` (which keys are "See Through's stars" on the wafer), the deep link
  a star opens, and the link grammar beyond `?layers=`.
- Team 4: the mapping `line:<n>` → Kuiper key for elements and spider nodes, and the app keys; until then those two
  layers are listed EMPTY.
- Team 5: elements' licence (none at elements@f7a92fb); E6-E8; the `<module-stamp>-<name>.js` vs `NN-<name>.js` choice;
  K3's root-only scope (tools/ci_check.py:68).
- NL-009: the `#refuse` strip (09-robust.md patch :94-96) and the 44 px touch rule (01-bar.md:51) are assumed to land in
  Edition 5; this team's rows and alerts use them rather than inventing a second surface.
