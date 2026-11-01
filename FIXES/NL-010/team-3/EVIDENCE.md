# NL-010 Team 3 EVIDENCE: See Through and the File menu (steps 5–6)

Evidence officer: FABLE-T3B. Written 2026-11-01 before STEPS.md, for the architect FABLE-T3A. Law: no claim without a
key. Every key is `repo@sha path:line` measured on the clones under /home/user/estate/ at these heads:

- kuiper-belt@018b46aed50f28f7b1882a0dcaba6593ce522beb (main, clean; Edition 4 live)
- gridatlas@5ec7f62f213e2d20a02e86427daa182c0f38e4a4 (main, clean)
- globalgrid2050@c66759f0d7ac3489df9158da6eaa1330a37c069f (main, clean)
- galaxies-wafers@fff6fc6ad4f93a15fe8f6456942a1b44e5547105 (for Addendum 1 only)

Short forms below: `kb@018b46a` = kuiper-belt@018b46aed50f28f7b1882a0dcaba6593ce522beb; `ga@5ec7f62` =
gridatlas@5ec7f62f213e2d20a02e86427daa182c0f38e4a4; `gg@c66759f` = globalgrid2050@c66759f0d7ac3489df9158da6eaa1330a37c069f;
`ST` = `see-through/202610050609/` inside kuiper-belt.

## E1. See Through: pointer and newest folder

| Fact | Key |
|---|---|
| Stable pointer is a meta refresh to `202610050609/` | kb@018b46a see-through/index.html:7 |
| Pointer's fallback link, same stamp | kb@018b46a see-through/index.html:11 |
| Pointer forwards the hash: `location.replace('202610050609/' + location.hash)` | kb@018b46a see-through/index.html:12 |
| Newest dated folder is `202610050609` (siblings 202610050356, 202610050513; `ls see-through/`) | kb@018b46a see-through/ (directory listing) |
| Folder contents: LICENSE.md, NOTICE.md, README.md, descent.js (156,211 B), grid-data.js (587,233 B), index.html (1,032 B), kuiper-law.js, model.js, pf.js, plain.css, see3d.js, data/, licences/, vendor/ | kb@018b46a see-through/202610050609/ (listing) |
| The page loads kuiper-law.js, grid-data.js, vendor/maplibre-gl.js, pf.js, model.js, see3d.js, descent.js in that order | kb@018b46a ST index.html:10-16 |
| It opens the module with id `descent` from `window.KGModules`, sets `m.standalone = true`, calls `m.open(host)` | kb@018b46a ST index.html:19-22 |
| Window error collector `window.__errors` | kb@018b46a ST index.html:21 |
| The module registers itself: `{ id:'descent', label:'SEE THROUGH', sentence:'See through the universe to one substation', open, close, back }` | kb@018b46a ST descent.js:1072-1073 |
| Folder rule stated for See Through: stable link opens the newest dated folder; earlier folders kept unchanged | kb@018b46a see-through/README.md:23-25 |
| Last commits touching see-through: 8e24d1f, 9c5c140, ba378da, 55db60c (all 2026-10-05) | `git -C kuiper-belt log -- see-through` |

## E2. See Through: URL and hash grammar (the code that reads a substation name or query)

Finding first: **See Through reads no URL at all.** `grep -c 'location\.hash\|location\.search\|URLSearchParams'` over
descent.js, grid-data.js, kuiper-law.js, model.js, pf.js, see3d.js and vendor/joystick.js is 0 in every file
(kb@018b46a see-through/202610050609/*.js). The pointer forwards `location.hash` (E1) into a page that never reads it.
So the hash deep-link grammar for See Through does not exist today and must be specified, not described.

What does read a name:

| Fact | Key |
|---|---|
| The text box: `type='text'`, `placeholder='Substation name'`, `maxLength=80`, autocomplete off | kb@018b46a ST descent.js:907 |
| The GO button calls `goSearch`, title 'go to this substation' | kb@018b46a ST descent.js:917 |
| Input and GO are 44 px tall, GO at least 56 px wide | kb@018b46a ST descent.js:207 |
| `doSearch()`: query cut to 80 chars, `trim().toLowerCase()`, substring match `low[i].indexOf(q) >= 0` over every name; notes 'NO SUBSTATION NAME HERE CONTAINS THAT', 'ONE MATCH. PRESS GO', 'N MATCHES, n LIT. KEEP TYPING' | kb@018b46a ST descent.js:389-403 |
| `bestMatch()`: an exact lower-case match wins, else the first substring match | kb@018b46a ST descent.js:404-408 |
| `goSearch()`: doSearch, bestMatch, blur, `flyTo(i)` | kb@018b46a ST descent.js:409-415 |
| `flyTo(i)`: exits 3D, sets flight phase 'up' or 'down', caption `'DOWN TO ' + name`, `setView('map')`, `loadMap()` | kb@018b46a ST descent.js:417-425 |
| Names come from `window.KGGridData.substations.names`, lower-cased once into `D0.low` | kb@018b46a ST descent.js:70-71, 1054-1055 |
| `nameOf(i)` falls back to 'SUBSTATION i (NO NAME IN THE PUBLIC FILE)' | kb@018b46a ST descent.js:100 |
| Programmatic API `window.__descent`: `target(i)`, `fly(i)`, `find(name)` (exact lower-case match, returns index or -1), `sub(i)` → `{name, lat, lon, volt, op}`, `state()`, `view(v)`, `setD`, `jumpD`, `screenOf`, `mapPointOf`, `mapReady` | kb@018b46a ST descent.js:1034-1050 (find :1046, fly :1045, sub :1047) |
| The API is removed on close (`window.__descent = null`) | kb@018b46a ST descent.js:1069 |
| View buttons KUIPER, MAP, SAT, 3D via `setView(v, true)`; `data-v` on each | kb@018b46a ST descent.js:933-936 |
| Bottom-left chips GRID, SUBS, SPIDER, "lit when on (GridAtlas mobile chips)" | kb@018b46a ST descent.js:926-930 |
| `back()` in standalone mode clears the input and the target and returns to the stars | kb@018b46a ST descent.js:438-445 |
| Diary's worked example for the box: "Try: cowley" | kb@018b46a diary/20261005.html (text line 47 after tag strip) |

So the only grammar today is: a free-text substation name, case-insensitive, substring, exact match preferred, ≤80
chars, entered by hand or by `window.__descent.find(name)` then `.fly(i)`.

## E3. See Through: placement law file

| Fact | Key |
|---|---|
| `kuiper-law.js` header: "THE ONE LAW OF THE REAL KUIPER, lifted VERBATIM from the live page", source kuiper-belt index.html @ 7a65dd315b0c60b1baf9a7090206c900b2cfd0a1 | kb@018b46a ST kuiper-law.js:1-3 |
| `G32 = 2654435769, TW = 4096` (quoted from index.html:92) | kb@018b46a ST kuiper-law.js:32-33 |
| `keyPlace(k)`: `m = Math.imul((k % 2^32) >>> 0, G32) >>> 0; th = 2π m / 2^32; r = Math.sqrt(k + 0.5)` (quoted from index.html:250-251) | kb@018b46a ST kuiper-law.js:38-40 |
| `place(key)` opens the same law into `{key, m, turns, deg, theta, r, x, y}` | kb@018b46a ST kuiper-law.js:44-51 |
| `shader(k0, d)` reproduces the vertex shader in float32 | kb@018b46a ST kuiper-law.js:64-79 |
| `homeZoom`: radius = 80 % of half the clear box | kb@018b46a ST kuiper-law.js:88 |
| Constants frozen; `source: 'kuiper-belt@7a65dd3… index.html:92,143-148,250-251,333-335,357'` | kb@018b46a ST kuiper-law.js:110-117 |
| The Excel 137.5° spiral is labelled "NOT THE REAL KUIPER" (mirror image, no +0.5) | kb@018b46a ST kuiper-law.js:26-28, 98-108 |
| The live engine still has the same law at the same lines at HEAD: `const G32 = 2654435769, TW = 4096;` | kb@018b46a index.html:92 |
| `function keyPlace(k)` in the live engine | kb@018b46a index.html:250 |
| Same in Edition 4 (engine copy shifted by 28 lines) | kb@018b46a editions/202611012027/index.html:120, 278 |
| The published law sentence: "r = sqrt(key), theta = 2 pi frac(key x 2654435769 / 2^32)" | kb@018b46a cosmos/wafer-meta.json:12 |
| How the stars gather in See Through: particle p carries DRAW THE GRID key `floor((ki + 0.5) * SPACE / NRULE)`, placed by `L.place(key)`; particle j < 5800 lands on substation j (`pSub = p % NSUB`), `subKey[j]` is its STAR KEY | kb@018b46a ST descent.js:950-953 (comment), 962-967 (loop) |
| `NRULE = 20000` keys on desktop; phone takes the first 5,800 then every second key (12,900 stars) | kb@018b46a ST descent.js:19, 951-952, 954-955 |
| `NSUB = 5800`; `keyOfSub(i)` returns the star key that lands on substation i | kb@018b46a ST descent.js:20, 101 |
| Header law: "A star is a line of code today, not a substation. The stars gather into the grid; they do not address it." | kb@018b46a ST descent.js:11 |
| README: "The stars gather by the Kuiper placement rule, which follows H. Vogel (1979) and uses the golden-ratio multiplier of D. E. Knuth's Fibonacci hashing." | kb@018b46a see-through/README.md:34-35 |

## E4. See Through: licence (CERN-OHL-S v2) and NOTICE lines

| Fact | Key |
|---|---|
| LICENSE.md: See Through reuses globalgrid2050 simulator code (place-frame.mjs, mod/pylons-real.js, mod/substations.js; method of overlay.html, wire-look.js, morph.js, perf.js), "licensed CERN-OHL-S v2 (strongly reciprocal) … offered under the same licence: CERN Open Hardware Licence Version 2, Strongly Reciprocal" | kb@018b46a ST LICENSE.md:3-6 |
| Full text location `licences/globalgrid2050-CERN-OHL-S-2.0.txt` | kb@018b46a ST LICENSE.md:7; file present in ST licences/ |
| Data and libraries keep their own terms (OSM ODbL, CARTO, Esri, AWS Terrain Tiles, MapLibre BSD-3) | kb@018b46a ST LICENSE.md:9-10 |
| NOTICE.md title and licence line: "See Through is offered under CERN-OHL-S v2 (see LICENSE.md). All source repositories belong to Ventus Ltd" | kb@018b46a ST NOTICE.md:1-4 |
| Reuse table: descent.js from Learn the Kuiper `modules/descent.js`; kuiper-law.js and grid-data.js from Learn the Kuiper; pf.js from globalgrid2050 `energy-transition-simulator/202609282123/place-frame.mjs` (c5ac5219); model.js, see3d.js, vendor/joystick.js from globalgrid2050; `data/substations-footprints.odbl.json` ODbL 1.0 | kb@018b46a ST NOTICE.md:8-16 |
| OpenStreetMap: names, positions, voltages, operators, GridAtlas line files, outlines, `data/osm/*.json` (Overpass, each file carries its query, endpoint, time); on-screen credit "Substations and lines © OpenStreetMap contributors, ODbL" | kb@018b46a ST NOTICE.md:22-25 |
| GridAtlas line files (atlas-v9 data URL), ODbL, loaded at run time | kb@018b46a ST NOTICE.md:26-27 |
| CARTO, Esri World Imagery, AWS Terrain Tiles credits as shown on screen | kb@018b46a ST NOTICE.md:28-34 |
| MapLibre GL JS 4.7.1, BSD-3-Clause, text in `vendor/MAPLIBRE-LICENSE.txt` | kb@018b46a ST NOTICE.md:38-39 |
| Network use: no account, key or tracking; tiles, GridAtlas line files, one Overpass query for a site without a saved detail file | kb@018b46a ST NOTICE.md:43-44 |
| Acknowledgements: Fibonacci (1202), Bravais (1837), Vogel (1979), Knuth TAOCP vol. 3 §6.4 | kb@018b46a ST NOTICE.md:48-57 |
| The public README repeats the licence and credits | kb@018b46a see-through/README.md:27-36 |

## E5. See Through: substation count and data source

| Fact | Key |
|---|---|
| "any of 5,800 UK substations" | kb@018b46a see-through/README.md:3; ST README.md:1 |
| The embedded table: `var SUB = /*DATA-BEGIN*/{"n":5800, "lon": …` (base-36 deltas for lon, lat, voltage, operator) | kb@018b46a ST descent.js:15 |
| `var NSUB = 5800;` | kb@018b46a ST descent.js:20 |
| Source stated in the header: names from grid-data.js (OpenStreetMap, ODbL) plus the table "from the same public file, globalgrid2050.com/grid_substations.geojson. Built by descent/build_descent_data.py" | kb@018b46a ST descent.js:5-6 |
| grid-data.js header: built from globalgrid2050 `testcode/wafer-development-environment/202609180245-real-systems/*-network.json`; OSM layers ODbL, coastline Natural Earth | kb@018b46a ST grid-data.js:1-7 |
| grid-data.js substations object: `"source":"globalgrid2050.com/grid_substations.geojson, substations"`, `"attribution":"© OpenStreetMap contributors, ODbL …"`, `"n":5800` | kb@018b46a ST grid-data.js:8 (one long line, `substations` member) |
| Real lines from GridAtlas: `GA_DATA = 'https://ventusltd.github.io/gridatlas/atlas/releases/202608300453-atlas-v9/data/'`, GA_LINES 400 kV #0054ff, 275 kV #ff0000, 132 kV #00cc00 "GridAtlas ukConfig, shell :145-149" | kb@018b46a ST descent.js:30-31 |
| grid-data.js is loaded lazily next to descent.js (`ensureGridData`) | kb@018b46a ST descent.js:53-55 |
| Decoding: lon/lat = running sums / 1e5; Web Mercator frame is the bounding box of every substation | kb@018b46a ST descent.js:63-75 |

## E6. The homepage's description of See Through

| Fact | Key |
|---|---|
| Apps section entry `<details id="see-through">`, numbered with the ↣ glyph (not a two-digit number like 02 Kuiper): "See to grid connection probabilities iteratively / See Through: from the stars to one substation in 3D / Type the name of a UK substation and press GO. The stars gather into the grid, the real map and satellite view appear inside the circle, and an illustrative 3D model of the substation rises on the real ground, combining mapped features with estimates. About 5,800 mapped substations. An early step toward comparing connection options site by site; no connection probability is calculated today. Needs the internet. Open See Through →" | gg@c66759f homepage_versions/homepage_v134.html:18 (inside the Kuiper `<details id="kuiper">` block, after What is the Kuiper and Learn the Kuiper) |
| Registry row: `data-entity-id="see-through"`, link text "See to grid connection probabilities iteratively", key `see-through`, type application, "Intended purpose: Explore mapped substation records through illustrative 3D models that distinguish mapped features from estimated equipment … For: grid researchers, developers, learners", "See Through: from the stars to one substation in 3D", 5 October 2026, Operative, build `20261005-0609` | gg@c66759f homepage_versions/homepage_v134.html:35 |
| The homepage links to the dated folder directly, `https://ventusltd.github.io/kuiper-belt/see-through/202610050609/`, not to the stable pointer | gg@c66759f homepage_versions/homepage_v134.html:35 |
| Kuiper diary row describes "what Learn the Kuiper and See Through do" | gg@c66759f homepage_versions/homepage_v134.html:36 |
| Learn the Kuiper row, key `learn-the-kuiper` | gg@c66759f homepage_versions/homepage_v134.html:34 |
| Diary page (kuiper-belt): "Two things are open to everyone today … LEARN THE KUIPER / SEE THROUGH"; See Through paragraph "about 5,800 mapped substations. Try: cowley." | kb@018b46a diary/20261005.html (tag-stripped text lines 30-47) |

Gap worth knowing: `grep -i "see.through"` returns nothing in kuiper-belt README.md, LAWS.md, SPEC.md, NEXT.md,
PALETTE.md, editions/README.md or editions/202611012027/README.md (kb@018b46a). The Kuiper's own documents do not
mention See Through at all today; "star player" has no key anywhere except the owner's words in BRIEF.md:6-7.

## E7. Learn the Kuiper's pointer

| Fact | Key |
|---|---|
| Meta refresh to `202610050609/` | kb@018b46a learn-the-kuiper/index.html:7 |
| Fallback link and `location.replace('202610050609/' + location.hash)` | kb@018b46a learn-the-kuiper/index.html:11-12 |
| Nine dated folders 202610042225 … 202610050609 plus astra-codex, build-your-own-kuiper | kb@018b46a learn-the-kuiper/ (listing) |
| The newest folder loads See Through as a module: `<script src="modules/descent.js" onerror="this.remove()">` | kb@018b46a learn-the-kuiper/202610050609/modes.html:24 |
| README: "Only the real map in SEE THROUGH (under MORE) needs the internet" | kb@018b46a learn-the-kuiper/README.md:19-20 |
| Same stamp 202610050609 for both pointers; both forward the hash | kb@018b46a learn-the-kuiper/index.html:12, see-through/index.html:12 |
| Editions pointer uses the identical three-place pattern for 202611012027 | kb@018b46a editions/index.html:7, 11, 12 |

## E8. GridAtlas's File menu items and the code behind each

The menu bar module is `atlas/modules/202609031958-menu-bar.js` (1,805 lines).

| Fact | Key |
|---|---|
| Menu names in order: `['File', 'Edit', 'View', 'Scope', 'Grid', 'About']` | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:31 |
| Required engine nodes: `search: .search-bar-wrapper`, `header: .hud-header`, `exportButton: #btn-export`, `statusButton`, `fullscreenButton`, `radiusButton`, `radiusAreaButton`, `zoneButton`, `measureButton`; the bar is not built until all exist plus "63 unique layer controls" (the admission rule) | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:141-157 |
| **File item 1: the search bar** moved into File: `move(panels.File, ready.nodes.search)` | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1662 |
| What that search is in the shell: `#search-input` placeholder "Search project name...", results div, GO button `#search-btn` | ga@5ec7f62 atlas/releases/202608300453-atlas-v9/index.html:42-47 |
| **File item 2: the engine's Export button** `move(panels.File, ready.nodes.exportButton)` | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1663 |
| **File item 3: the engine modules group** `appendEngineModules(panels.File)` | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1586 |
| …fetched from `ENGINE_GRAPH_URL` (ventus-grid-engine genome/engine-graph.json); each node is an `<a role="button" target="_blank">` to `ENGINE_VIEW_URL + encodeURIComponent(node.label)`; groups by kind in ORDER canonical, extract, reference, fragment; silent on fetch failure | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:629-632, 641-647, 737-754, 757-762 |
| …the one runnable command: `RUN_COMMAND = 'git clone https://github.com/Ventusltd/ventus-grid-engine && cd ventus-grid-engine && node verify.mjs'`, button "⧉ Copy: clone the engine and run its 133 checks", copied with `navigator.clipboard.writeText`, falls back to showing the command | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:707-733 |
| …the architect's words behind it: "we are heading towards a grid OS in our website the menus must be neat, it should allow AI and humans to develop and use" (2026-09-05) and "The MJS apps that AI and humans can deploy as an IDE via menu … lets hand power to the people" | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:616-621, 690-694 |
| **File item 4: "Export this view" group** `appendExport(panels.File, doc)` returning 3 controls | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1587, 1350-1389 |
| …`#gridatlas-export-print` "⎙ Print · or save as PDF" → `printView(doc)` | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1366-1371 (printView :1034) |
| …`#gridatlas-export-pdf` "⤓ Save this view as a PDF" → `savePdf(doc, pdf)` (PDF bytes written in-page, `buildMapPdf` :1206) | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1374-1379 |
| …`#gridatlas-export-image` "⤓ Save an image of this view" → `saveImage(doc, image)`; refuses rather than saving a blank PNG | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1382-1387, 806-811 |
| …each export control is named by id and `data-gm-export="print|pdf|image"` because "ITS LABEL IS NOT A NAME" | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1354-1365 |
| …export stamps the generation and attribution on the artefact (`exportStamp`) | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:813-834 |
| Where the other menus get their items (for the mapping): Edit ← status button :1664; View ← fullscreen :1665 and Studies :1588, 771-792; Scope ← radius, radius-area, zone, measure :1666-1669 and gridpoint :1578; Grid ← 63 layer controls `buildLayerControls` :1428 and the curtain :1560-1566; About ← disclaimer, shoutout :1580-1583, Estate links :1585, 605-612, 1392-1407, attribution in small print :1590-1600 | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js (lines as listed) |
| Group headings inside a panel come from `appendGroup(panel, text)` | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:584 |
| `move(panel, node, label)` is the single primitive that relocates an engine control into a panel | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1490 |
| Mobile tray buttons are routed by text (`trayRoute`: clear/scope → Scope; grid/subs → Grid); GRID and SUBS chips stay on the map on a phone ("one tap on a phone, not two") | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1499-1504, 1506-1515, 1569-1575 |
| The VENTUS masthead is fused into the bar's centre (`brandSlot`), never into a panel | ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1671-1680 |

GridAtlas's own deep-link grammar (the lesson for "copy a link"): it is a **query parameter, not a hash**.

| Fact | Key |
|---|---|
| Repository root forwards `search + hash` to `./atlas/` | ga@5ec7f62 index.html:2 |
| The live route loads `./current.json` (schema `gridatlas.current.v2`) and mounts the shell and cartridges from it | ga@5ec7f62 atlas/index.html:39-42; atlas/current.json:1-13 |
| `cartridge_order`: streaming-parquet-bridge, uk-gazetteer-flyto, substation-intelligence, sld-sandbox, uk-lightning-overlay, uk-offtakers-overlay | ga@5ec7f62 atlas/current.json:14-21 |
| Deep-link identity: `"identity_parameter": "repd_ref"`, `"identity_rule": "EXACT_REPD_REF_ONLY"` | ga@5ec7f62 atlas/releases/202608300453-atlas-v9/deep-link-receiver-manifest.json:4-5 |
| The gazetteer cartridge (uk-gazetteer-flyto, v9.145, capabilities include `deep-link-publishes-resolved-technology-and-capacity`) writes the link with `url.searchParams.set('repd_ref', …); history.replaceState(…)` | ga@5ec7f62 atlas/cartridges/202609071213-place-global-search-v9-5.js:380-384 (current.json entry id uk-gazetteer-flyto) |
| A place selection deletes `repd_ref` from the URL and `map.flyTo({center, zoom, duration:1200})` | ga@5ec7f62 atlas/cartridges/202609071213-place-global-search-v9-5.js:558-570 |
| Arrival: `receiveExactRepdDeepLink` reads `new URLSearchParams(window.location.search).get('repd_ref')`; absent → `status:'ABSENT'` | ga@5ec7f62 atlas/cartridges/202609071213-place-global-search-v9-5.js:695-702 |
| Substation Intelligence also reads `repd_ref` from the query | ga@5ec7f62 atlas/cartridges/202609062358-substation-intelligence-v9-63.js:853, 6203 |
| `grep -c location.hash` over the atlas tree (js, mjs, html) finds no reader | ga@5ec7f62 atlas/ (0 files) |

## E9. The Kuiper engine's hash handling

Finding first: **the Kuiper engine reads no hash either.** `grep -c 'location.hash'` is 0 in kb@018b46a index.html and
in editions/202611012027/index.html. The only URL input is the `?selftest=` query. Everything below is what exists and
what a hash grammar would have to call.

| Fact | Key |
|---|---|
| `?selftest=YYYY-MM` lights that period and self-checks the pixels | kb@018b46a index.html:192-207 |
| `?selftest=new` → `showNew(24)`; `?selftest=phone` → `phoneSelftest`; `?selftest=repo:<name>` → `repoSelftest(decodeURIComponent)` | kb@018b46a index.html:208-211 |
| Same four in Edition 4 | kb@018b46a editions/202611012027/index.html:220, 236-239 |
| `flyTo(x, y, z)`: a 900 ms camera tween to world x, y at zoom z | kb@018b46a index.html:225 |
| `goKey(k)`: `keyPlace(k)` → target → `show(address(k))` → `flyTo(p[0], p[1], 14)` (this is "fly to a key") | kb@018b46a index.html:388 |
| `address(k)`: null unless `0 <= k < SPACE`; binary search `findBy('k0', k)` to the commit | kb@018b46a index.html:254, 252 |
| `home()` → `homeCamera()` | kb@018b46a index.html:249 |
| The find box `#goto` / `#gotoin`, placeholder "a key, or a repository name to send light through" | kb@018b46a index.html:64 |
| Tap targets: `data-k="n"` new code, `"r"` random line, `"/"` find, `"Backspace"` whole wafer; a click dispatches the same `keydown` | kb@018b46a index.html:66-67, 572-573 |
| Legend: "/ a key, a repository, or a period like 2026-07" | kb@018b46a index.html:68 |
| The `/` key opens the box: `e.key === '/'` → `gbox.style.display='block'; gin.focus()` | kb@018b46a index.html:589 |
| `r` → uniform random issued line `goKey(c.k0 + (j - c.cum))`; `n` → `showNew(24)`; Backspace → clear and `home()` | kb@018b46a index.html:587-590 |
| **The find grammar** on Enter: `raw = value.trim()`, `q = raw.replace(/[ ,_]/g,'')`; (1) `/^(20\d\d)(?:-(\d\d))?(?:-(\d\d))?$/` → `lightTime(y, m, d)`; (2) `/^(?:show\s+)?new(?:\s+code)?(?:\s+(\d+)\s*h?)?$/i` → `showNew(N or 24)`; (3) `/^\d+$/` → `goKey(Math.min(SPACE-1, Number(q)))`; (4) else repository by exact lower-case name, then by `includes` → `litRepo`, `home()`; Escape closes | kb@018b46a index.html:577-586 |
| `lightTime(y, m, d)` | kb@018b46a index.html:526 |
| `SPACE` and `N` come from cosmos/wafer.tsv (`N = issued; SPACE = k`); if it fails: "The wafer will not invent its keys." | kb@018b46a index.html:170, 180, 212 |
| The card tells the reader how to open a key as text: `python tools/key.py <k0>` | kb@018b46a index.html:406 |
| `tools/key.py`: key → repository (belt.tsv) → commit (commits/NN.tsv) → file, line (`git ls-tree`) → text (`git cat-file`); exits non-zero if the counts do not land | kb@018b46a tools/key.py:1-22 |
| Edition 4 layer: `loadEdition()` fetches keys.json, keeps `on_wafer && verified && 0 <= key < SPACE`, places each with `keyPlace(b.key)` | kb@018b46a editions/202611012027/index.html:628-638 |
| keys.json body fields usable as link targets: `id` (blob:line), `repo`, `commit`, `path`, `line`, `key`, `k0`, `destination` (GitHub blob URL with `#L<line>`), `on_wafer`, `verified`, `class` | kb@018b46a editions/202611012027/keys.json (bodies[0]; 346 bodies, `summary` + `bodies`) |
| `edCard(i)`: title, `repo path:line`, quote, "open on GitHub at <sha7>" link, details with `describe(address(key))` | kb@018b46a editions/202611012027/index.html:651-664 |
| `edFly(b)`: zoom 14, places the spark in the clear space under the bar and above the card | kb@018b46a editions/202611012027/index.html:676-680 |
| A tap within 9 px of a spark opens it; keys `e`/`E` step next/previous | kb@018b46a editions/202611012027/index.html:688-695 |
| The Edition 3/4 bar: `KUIPER EDITION 4` + titles edition, readout, lines, commands; "Borrowed in spirit from gridatlas atlas/modules/202609031958-menu-bar.js" | kb@018b46a editions/202611012027/index.html:696-703 |
| LINES panel: layer on/off, focus-only, next/previous, `#lyFind` filter over repo, path, title; picking a row closes the panel and flies | kb@018b46a editions/202611012027/index.html:704-708, 727-729, 731-738 |
| `setPanel(name)`: one panel open at a time; Escape and a tap on the wafer close it | kb@018b46a editions/202611012027/index.html:714-724 |
| Edition harness rules (pointer in three places, no `/belt/`, folder rule) | neural-link SESSIONS/202611012145-kuiper-edition-harness-notes.md "Rules that bind every edition" |

## E10. Keys for Addendum 1 (counts and the older law), for whoever consolidates

| Fact | Key |
|---|---|
| Live wafer today: issued_keys 45,735,836,396; unissued 17,604,284,400; address_space 63,340,120,796; silence_share 0.2779; commits 13,344; repositories 98; law string | kb@018b46a cosmos/wafer-meta.json:1-12 |
| wafer.tsv columns `unix lines repo_index sha12 gap_before`; 13,345 lines including the header (13,344 commits); repos.tsv 99 lines | kb@018b46a cosmos/wafer.tsv:1 (`wc -l`) |
| ci_check K2: wafer.tsv re-summed equals wafer-meta.json and repos.tsv | kb@018b46a tools/ci_check.py:9, 56-60 |
| galaxies-wafers law: `r = sqrt(key)`, `theta = key x 2.39996322972865332` (golden angle), `GOLDEN_ANGLE = π(3 − √5)`, `law: 'r = sqrt(key); theta = key * goldenAngle'` | galaxies-wafers@fff6fc6 wafer.mjs:11-12, 43, 46, 53 |
| galaxies-wafers README: "every permanently numbered line of the estate placed by one frozen law … It is the basemap and it never changes" | galaxies-wafers@fff6fc6 README.md:5 |
| The difference stated in See Through's own law file: the Kuiper uses `sqrt(k + 0.5)` and Fibonacci hashing; the plain golden-angle spiral is its mirror image | kb@018b46a ST kuiper-law.js:26-28 |

## E11. Gaps and cautions for the architect (each is a measured absence, not an opinion)

1. No hash reader exists in See Through (E2), in Learn the Kuiper's pointer target (only the pointer forwards it), or
   in the Kuiper engine and Edition 4 (E9). Steps 5–6 must specify a grammar and name the file and function that will
   read it; they may not describe it as existing.
2. GridAtlas's deep link is `?repd_ref=` in the query, written with `history.replaceState` (E8). A Kuiper grammar that
   uses the hash must say why it departs (the pointers already forward `location.hash`, see-through/index.html:12,
   learn-the-kuiper/index.html:12, editions/index.html:12; they do not forward `location.search`).
3. See Through's search is substring, case-insensitive, exact-first (descent.js:389-408); a link grammar that carries a
   name must say what happens on 0 and on many matches, with the existing notes as the words.
4. See Through's programmatic entry points are `window.__descent.find(name)` and `.fly(i)` (descent.js:1045-1046),
   set in `open()` and nulled in `close()`; a deep link arriving before `open()` finishes has nothing to call.
5. The homepage links to the dated folder `see-through/202610050609/` (homepage_v134.html:35), not to the pointer; a new
   See Through folder would leave the homepage one stamp behind unless its registry row is updated.
6. The Kuiper's own documents (README, LAWS, SPEC, NEXT, PALETTE, editions READMEs) do not mention See Through (E6
   gap). "Star player" therefore has to be written in, with the owner's words as its only source (BRIEF.md:6-7).
7. kuiper-law.js cites kuiper-belt@7a65dd3 while HEAD is 018b46a; the cited lines (:92, :250) still match at HEAD (E3),
   so the law is unchanged, but the citation is stale by commit.
8. "Open an app" has no precedent in the Kuiper; GridAtlas's precedent is the File menu's fetched engine-module group
   (anchors, `target=_blank`, silent on fetch failure) and About's Estate links (E8). An app registry is Team 4's; Team 3
   should reference it, not define it.
9. NL-009 round1 findings: at the time of writing only `FIXES/NL-009/round1/BRIEF.md` and an empty `img/` exist; I will
   re-check before the review and list what appears.

## E12. NL-009 round 1 findings that touch steps 5–6 (read 2026-11-01 ~21:00 UTC; folder re-checked before the review)

Files present: `FIXES/NL-009/round1/01-bar.md`, `06-seethrough.md`, `09-robust.md`, `BRIEF.md`, `img/`. Keys are
the neural-link paths (uncommitted at the time of reading; the harness commits).

| Finding | Key |
|---|---|
| 06 F1 BLOCKER: See Through is unreachable from Edition 4 (`grep -ci "see.through"` on the page → 0, README → 0; NOTICE names it once as a licence). Patch adds a fifth bar entry `<a class="gm-title" href="../../see-through/">see through</a>` (Pixel 7: 101×29 px), same tab, through the stable pointer; `goBack()` returns to the edition; 0 console errors on Pixel 7, Galaxy S24, Pixel 7 landscape | FIXES/NL-009/round1/06-seethrough.md "FINDINGS" 1 and PATCH hunk @@ -700,7 |
| 06 F5 decisions: same tab not `_blank` (homepage opens every app in the same tab; two WebGL pages on one phone; back gesture is the way home); link to the pointer `../../see-through/`, not the dated folder; family paragraph `#edapps` in the EDITION panel naming See Through (CERN-OHL-S v2) and Learn the Kuiper (code Apache-2.0, text CC BY 4.0) | FIXES/NL-009/round1/06-seethrough.md "FINDINGS" 5, 6 and PATCH hunk @@ -718,10 |
| 06 F4: See Through on Pixel 7 fits the phone (scrollWidth 412, scrollHeight 839); 13 controls all 44 px tall (name input 332×44 at y 56, GO 56×44, KUIPER MAP SAT 3D at y 713, GRID SUBS SPIDER ▲ ▼ at y 761); CARTO style blocked by the sandbox proxy; the app offers no way back to the edition except the browser back gesture | FIXES/NL-009/round1/06-seethrough.md "FINDINGS" 4 |
| 01 F1 BLOCKER: the bar is two rows at 360–430 px (75.1 px high; content 416.6 px); a fifth button at the present style would need 521 px. 01 F3 MAJOR: no room for SEE THROUGH at 11 px / .08 em / 8 px padding (391 px of buttons alone against 344 px). After 01's patch: five titles in one row at 360 (347.9 px, slack 12.1), bar 51 px, every title 44 px tall, title shrinks to the mark `KE4`, SEE THROUGH 80.4 px wide at 360 | FIXES/NL-009/round1/01-bar.md "FINDINGS" 1-3 and "Status after the patch" |
| 01 F2 MAJOR: titles 29 px tall, under 44/48 px touch targets; fixed by `(pointer:coarse)` min-height 44 px | FIXES/NL-009/round1/01-bar.md "FINDINGS" 2, "Design" |
| 09: READOUT slides under the bar after a pick (MAJOR); WebGL-off blank screen (MAJOR); no `<noscript>`, keys.json 404 only in hidden READOUT, Escape does not close the card, reduced motion ignored, ARIA missing (MINOR) | FIXES/NL-009/round1/09-robust.md "FINDINGS" 1-7 |

What this means for steps 5–6: the See Through button exists as a patch (06) and the bar budget for it is solved
by 01 only with the phone rule (10 px at 360, `KE4` mark). A step that makes See Through "the first and largest
entry" must reconcile with 01's measured budget (328 px for five titles at 360 px) or state the new budget with
numbers, and must keep 06's decisions (pointer not dated folder; same tab) or say why not.
