# NL-010 Team 1 (the shell, steps 1–2) — EVIDENCE

Evidence officer FABLE-T1B. Channel: https://github.com/Ventusltd/neural-link-between-agents/issues/10. Law: no claim
without a key. Every key below is `repo@sha path:line` against the clones under `/home/user/estate/`, sha from
`git log -1` in that clone on 2026-11-01:

| repo | sha (git log -1 in the clone) | note |
|---|---|---|
| gridatlas | `5ec7f62f213e2d20a02e86427daa182c0f38e4a4` (short `5ec7f62`) | the clone's checked-out branch is `preview/202610312138-gridatlas-v9.188`; `git diff main --stat` over `index.html`, `atlas/index.html`, `atlas/modules/202609031958-menu-bar.js`, `atlas/cartridges/202609062358-substation-intelligence-v9-63.js` and `atlas/releases/202608300453-atlas-v9/` is empty, so every shell key below is identical on local `main` (`cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e`). |
| gridatlas, remote | `41729af0b49dcfbe8f2a3ebc485eff217a61b84d` (origin/main, 2026-10-31T22:53:11Z, read with `gh api repos/Ventusltd/gridatlas/commits/main`) | the live pointer on GitHub names generation `202610312138` (`gh api .../contents/atlas/current.json` line 3); the clone's `atlas/current.json:3` still says `202610292044`. The shell, the menu bar module and the substation-intelligence cartridge are the same bytes in both generations (see A1). |
| kuiper-belt | `018b46aed50f28f7b1882a0dcaba6593ce522beb` (short `018b46a`) | main, clean |
| globalgrid2050 | `c66759f0d7ac3489df9158da6eaa1330a37c069f` (short `c66759f`) | main |
| neural-link-between-agents | working tree (not a git repository on this machine) | NL-009 round 1 files read at 20:53 UTC |

Method. (1) Static reads of the files keyed below. (2) Measurement: the GridAtlas composer was run locally
(`python3 -m http.server 8772` from the gridatlas root, Playwright Chromium with SwiftShader; the sandbox proxy
blocks cdn.jsdelivr.net and github.io, so `maplibre-gl@3.6.2` was answered from the estate's vendored copy
`kuiper-belt/see-through/202610050609/vendor/maplibre-gl.js` (v4.7.1 banner) and the CARTO style with a one-layer stub;
every other external request aborted). The menu bar therefore installed through its real admission rule
(`__GRIDATLAS_MODULES__.menuBar.installed === true`, 63 layer controls) and its geometry is the real CSS laid out by
Chromium; the monospace face is the container's DejaVu Sans Mono, so widths transfer to Android (Droid Sans Mono)
within ~0.5 % (FABLE-01's measurement, FIXES/NL-009/round1/01-bar.md). Kuiper Edition 4 was served from the
kuiper-belt root on 8771 and measured at 360×780, Pixel 7 (412×839) and 1280×800. Scripts:
`/tmp/nl010/team-1/B/measure-ga-B.cjs`, `/tmp/nl010/team-1/B/measure-ed4-B.cjs`; outputs beside them (machine-local).
Numbers that come from a measurement say so; everything else is a line of source.

---

## A. The GridAtlas shell

### A1. What is live, and how it is composed (the pointer)

| element | key | what the line says |
|---|---|---|
| root redirect | gridatlas@5ec7f62 index.html:2 | `window.location.replace('./atlas/' + search + hash)`; meta `gridatlas-current-route` = `atlas` |
| composer: fetch pointer | gridatlas@5ec7f62 atlas/index.html:35-39 | fetches `./current.json` (`cache:no-store`), requires `schema === 'gridatlas.current.v2'` and `architecture === 'IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES'` |
| composer: fetch immutable shell | gridatlas@5ec7f62 atlas/index.html:41-47 | fetches `current.shell.index`, injects `<base href=shell.base>` |
| composer: cartridge loop | gridatlas@5ec7f62 atlas/index.html:55-85 | for each id in `cartridge_order`: type `script`, slot `replace-script` or `after-cartridge`, `sha256` must match the fetched bytes (`:75`), blob URL script tag swapped into the shell |
| composer: public state | gridatlas@5ec7f62 atlas/index.html:88-99 | `window.__GRIDATLAS_ATLAS__` = {generation, release_id, shell, cartridge_order, loaded_cartridges}; `document.write(html)` |
| composer: failure | gridatlas@5ec7f62 atlas/index.html:27-31 | "GRIDATLAS COMPOSITION FAILED … The immutable shell was not changed." |
| pointer: generation | gridatlas@5ec7f62 atlas/current.json:3 | `"generation": "202610292044"` in the clone; `202610312138` on origin/main `41729af` (remote read, see table above) |
| pointer: architecture, routes | gridatlas@5ec7f62 atlas/current.json:5-8 | `IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES`, `live_route /gridatlas/atlas/`, `release_id 202608300453-atlas-v9`, `release_route /gridatlas/atlas/releases/202608300453-atlas-v9/` |
| pointer: shell | gridatlas@5ec7f62 atlas/current.json:9-13 | `shell.index ./releases/202608300453-atlas-v9/index.html`, `shell.base ./releases/202608300453-atlas-v9/` |
| pointer: cartridge order | gridatlas@5ec7f62 atlas/current.json:14-21 | six: streaming-parquet-bridge, uk-gazetteer-flyto, substation-intelligence, sld-sandbox, uk-lightning-overlay, uk-offtakers-overlay |
| pointer: the cartridge that carries the menu bar | gridatlas@5ec7f62 atlas/current.json:566-573 | id `substation-intelligence`, generation `202609062358`, slot `replace-script`, path `./cartridges/202609062358-substation-intelligence-v9-63.js`, sha256 `d94b0de50deddac77643325b10fbe490ce44b8c406dbc6c67e6e7cadbdaa8ec6` (verified: `sha256sum` of the file in the clone = the same digest) |
| pointer: explicit order flag | gridatlas@5ec7f62 atlas/current.json:828 | `"cartridge_order_explicit": true` |
| release manifest: immutability | gridatlas@5ec7f62 atlas/releases/202608300453-atlas-v9/release-manifest.json:16 | `"immutable_after_publication": true` |
| release digests | gridatlas@5ec7f62 atlas/releases/202608300453-atlas-v9/sha256sums.txt:18,21,22 | `index.html 87a3aaf4…`, `ventus-corev8engine.js 9a75901e…`, `ventusv8.css 1d4be1b6…` |
| composition manifest names the masthead rule | gridatlas@5ec7f62 atlas/manifests/202610292044-composition.json:590 | capability `ventus-masthead-fused-into-menu-bar-never-a-closed-panel` (and `:591` `scada-panel-restored-branded-head-real-nodes-moved-not-cloned`, `:592` `layer-controls-44px-min-hit-target-via-full-size-invisible-input`) |
| release law | gridatlas@5ec7f62 docs/RELEASE.md:3-4, :40-41, :49-54 | a release moves `atlas/current.json` from live to an accepted preview; the owner comments `ACCEPT G`; "Agents never record acceptance"; "Only the owner merges a release" |
| durable state | gridatlas@5ec7f62 STATE.md:5 | composition `202610292044 · 202608300453-atlas-v9 · streaming-parquet-bridge → … → uk-offtakers-overlay` |

The menu bar exists twice in the repository: as the module `atlas/modules/202609031958-menu-bar.js` (1,805 lines) and
inside the cartridge the composer actually loads, `atlas/cartridges/202609062358-substation-intelligence-v9-63.js`
lines 4,346–6,151 (keys for both are given below; the module key is the readable one, the cartridge key is the live one).
`diff` of the module's `install()` (:1647-1746) against the cartridge's (:5996-6105) shows ONE difference: the cartridge
does not move the search bar into File (cartridge :6011-6016, "The search bar is NOT moved. It is the one control a person
needs before they know which menu to open … It stays in .map-container"); everything else is the same text. The live
bytes rule where they differ.

### A2. The immutable shell (the v8 page the bar is installed into)

| element | key | what the line says |
|---|---|---|
| viewport | gridatlas@5ec7f62 atlas/releases/202608300453-atlas-v9/index.html:6 | `width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no` |
| stylesheet | …/index.html:9 | `ventusv8.css` |
| fullscreen letterhead (second wordmark) | …/index.html:17-20 | `#fs-letterhead` → `.ventus-main` "Ventus", `.ventus-sub` "Cables &amp; Connectivity&reg;" |
| the HUD header (the masthead the bar fuses) | …/index.html:22-34 | `.dashboard > .hud-header`: SYSTEM TIME clock `#clock`, `.ventus-brand` (`.ventus-main` "Ventus", `.ventus-sub` "Cables & Connectivity®"), "2050 TARGET" `#days` |
| the map | …/index.html:36-37 | `.map-container#map-container > #map` |
| attribution | …/index.html:38-40 | `.custom-map-attrib` OpenStreetMap / CARTO / Open Charge Map |
| fullscreen button, search | …/index.html:41-48 | `#btn-fullscreen`, `.search-bar-wrapper` (`#search-input`, `#search-btn` GO) |
| the six map commands | …/index.html:50-57 | `.map-controls`: `#btn-export` Export CSV, `#btn-radius`, `#btn-radius-area`, `#btn-zonedraw`, `#btn-status` Status Colours, `#btn-measure` |
| SCADA panel head (third wordmark) | …/index.html:112-119 | `.scada-wrapper > .scada-brand` (`.scada-brand-main` "Ventus", `.scada-brand-sub`, `.scada-brand-tag` "globalgrid2050.com \| open infrastructure intelligence") |
| status legend, layer host | …/index.html:120-126 | `.status-legend` (Operational / Under Construction / Consented / Applied), `.scada-keys#scada-ui-container` (the engine builds the 60 layer checkboxes here) |
| disclaimer | …/index.html:127-129 | `.disclaimer-box` |
| scripts | …/index.html:133-139 | maplibre 3.6.2, worker bridge, postcode search, `ventus-corev8engine.js`, pre-snapped adapter |
| the 60 engine layers | …/index.html:142-261 | `ukConfig`: 11 groups (Topology 7, Assets 6, Supermarkets 11, Transit 9, Leisure 1, Global Data Backbone 1, Supply Chain 3, Highway 4, EV 1, Heavy Industry 1, REPD 16) = 60 |
| engine start | …/index.html:263-267 | `window.initVentusMap({config, center:[-3.5,54], zoom:4.2})` |
| basemap style URL | …/ventus-corev8engine.js:613 | `https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json` |
| page face and ground | …/ventusv8.css:1 | `font-family:'Courier New', monospace; background:#000; color:white` |
| `.hud-header` | …/ventusv8.css:4 | `background:#0a0a0a; border:1px solid #333; border-radius:6px; padding:6px 12px; display:flex; justify-content:space-between` |
| `.hud-val` | …/ventusv8.css:5 | `16px bold #00ffff` |
| `.ventus-brand` | …/ventusv8.css:6 | centred column |
| **`.ventus-main` (the wordmark, v8 size)** | …/ventusv8.css:7 | `font-family:-apple-system,sans-serif; font-size:17px; font-weight:800; color:#fff; letter-spacing:5px; text-transform:uppercase; margin-bottom:2px` |
| **`.ventus-sub`** | …/ventusv8.css:8 | `-apple-system,sans-serif; 6.5px; color:#888; letter-spacing:2px; uppercase` |
| `.scada-brand*` | …/ventusv8.css:13-16 | 11px/800/4px main, 6px sub, 7px tag |
| `#fs-letterhead` | …/ventusv8.css:103-106 | `fixed; top:8px; right:12px; z 512`; main 15px/800/5px; sub 6px; shown only under `body.fs-active` |
| short-viewport rule | …/ventusv8.css:152-155 | `@media (max-height:600px)`: `.ventus-main{font-size:13px}` |

Negative findings (searched, not found). `find gridatlas -iname '*logo*' -o -iname '*ventus*.svg' -o -iname
'*ventus*.png'` returns nothing; `grep -n '<img\|\.svg\|\.png\|logo'` over the shell `index.html` and `ventusv8.css`
returns nothing; `grep -ni logo` over `ventus-corev8engine.js`, `README.md`, `docs/RELEASE.md`, `STATE.md` returns
nothing. **The Ventus "logo" on GridAtlas is not an image file. It is the typographic wordmark `VENTUS` over
`CABLES & CONNECTIVITY®` set by the two CSS rules at ventusv8.css:7-8 and re-sized by the menu bar at A5.** It is a
`<div>`, inside no `<a>`, with no click handler (measured: `insideAnchor:false`, see A9), so it links to nothing.

### A3. The menu bar module and its six menus

| element | module key (gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js) | live copy (gridatlas@5ec7f62 atlas/cartridges/202609062358-substation-intelligence-v9-63.js) | what it says |
|---|---|---|---|
| purpose and rule, in prose | :1-21 | :4346-4366 | "installs nothing until the engine's 60 layer controls and the three Pipeline News controls are all present and uniquely identified"; "the Grid menu proxies those 63 ORIGINAL inputs"; "action buttons are moved as the same DOM nodes"; "A missing control leaves the old interface reachable and is published as a failure" |
| schema, ids | :27-30 | :4376-4379 | `gridatlas.menu-bar.v2`, `BAR_ID gridatlas-menu-bar`, `STYLE_ID`, `FAILURE_ID` |
| **the six names** | :31 | :4380 | `var MENUS = ['File', 'Edit', 'View', 'Scope', 'Grid', 'About'];` |
| expected inventory | :32-35 | :4381-4384 | 60 engine + 3 Pipeline News = 63; `MAX_TRIES = 160` × 250 ms = 40 s |
| public state | :40-57 | :4389-4406 | `window.__GRIDATLAS_MODULES__.menuBar` {installed, controls_moved, layer_controls, panel_counts, failure, closed_at_rest, one_identity_surface…} |
| inventory() | :107-124 | :4456-4474 | counts `input[type=checkbox][data-layer-id]` and `[data-pn-layer]` under `#scada-ui-container`; complete only at 60 + 3 = 63 unique non-empty keys |
| required() | :141-159 | :4490-4509 | the nodes the bar needs: `.map-container`, `.map-controls`, `.search-bar-wrapper`, `.hud-header`, `#btn-export`, `#btn-status`, `#btn-fullscreen`, `#btn-radius`, `#btn-radius-area`, `#btn-zonedraw`, `#btn-measure`; else `missing.push('63 unique layer controls')` |
| buildBar(): three zones | :481-503 | :4830-4852 | `<nav id=gridatlas-menu-bar aria-label="Atlas menu">` = `.gm-side-left` + `.gm-brand-slot` + `.gm-side-right`; prose: "Fusing the brand into the CENTRE of the same 36px strip … no extra row and therefore no map height stolen on a phone" |
| buildBar(): a title and its panel | :505-516 | :4854-4865 | `<button class=gm-title>` with `aria-haspopup=menu`, `aria-expanded`, `aria-controls`; `<div class=gm-panel role=group hidden>` |
| Grid panel head/body | :517-536 | :4866-4885 | the Grid panel is `.gm-panel-grid` with `.gm-panel-head` (the real `.scada-brand` + `.status-legend`) over a scrollable `.gm-panel-body` |
| **left three / right three** | :544 | :4894 | `(index < 3 ? left : right).appendChild(menu)` → File Edit View left, Scope Grid About right |
| keyboard | :554-583 | :4903-4932 | Escape closes; ←/→ move between titles; Home/End; ↓ opens and focuses the first control |
| closed at rest | :405-416, :1730 | — | `closeAll()`; `state.closed_at_rest = true`; install ends with `closeAll()` |
| one open at a time | :468-479 | — | `openMenu()` closes all, toggles, syncs Grid, clamps the panel into the viewport |
| clampPanel | :447-466 | — | JS-measured guarantee that no panel resolves outside the viewport (margin 4 px) |

What each menu holds, and where it came from (every move is the same DOM node, `move()` at :1490-1497 / :5839):

| menu | contents | key |
|---|---|---|
| File | Export CSV; the engine's modules fetched from `ventus-grid-engine/genome/engine-graph.json`; Export group (print as slide / save image / write PDF / print source code). (The module file also moves the search bar here, :1662; the LIVE cartridge does not, :6011-6016, and keeps it on the map.) | :1663 (`exportButton`); cartridge :6017; :629-641 `ENGINE_GRAPH_URL`, `appendEngineModules`; :1350 `appendExport`; :1034 `printView`; prose :614-627 "we are heading towards a grid OS … the menus must be neat, it should allow AI and humans to develop and use" (the architect, 2026-09-05) |
| Edit | Status Colours | :1664 `move(panels.Edit, ready.nodes.statusButton)` |
| View | Fullscreen; Exit full screen; GB conditions; Studies (GB electricity price and grid constraint series) | :1665, :1556-1558, :1588 `appendStudies(panels.View)` (function at :777) |
| Scope | Radius Search, Radius Area, Poly Zone, Measure, Grid Finding Scope (`#btn-gridpoint`); mobile-tray "clear/scope" chips | :1666-1669, :1578 (module); `trayRoute` :1499-1503 |
| Grid | the 63 layer controls, proxied, grouped by the engine's `.key-group` titles, each a 44 px `.gm-layer` row whose own `<input>` covers the label; head = the real `.scada-brand` + `.status-legend`; the fullscreen layer curtain tab | :1428-1488 `buildLayerControls` (proxy `data-gridatlas-layer-proxy`, forwards `original.click()`), :1685-1686 `move(gridHead, …)`, :1560-1566 curtain; CSS :253-269 |
| About | version ledger `#gridatlas-version-ledger`; disclaimer; podcast shout-out; Estate links (Grid engine · the maths, Federation map, Spider printer); the map attribution LAST in small print | :1557, :1580-1583, :605-613 `ESTATE_LINKS`, :1585 `appendEstateLinks(panels.About)` (function at :1392), :1590-1611 attribution ("Attribution bar clashes move that to about and in small print at the bottom" — the architect, quoted :1598-1600) |

Two layer chips, GRID and SUBS, are deliberately left ON THE MAP at every width, not inside a menu:
`chipStaysOnMap()` :1521-1552 (returns `true` unconditionally; prose quotes the architect "in mobile view the Grid and
subs buttons are nice show them on desktop TOO"; ledger v9.131 at A8).

### A4. The admission rule (install, retry, loud failure)

| step | key | what it says |
|---|---|---|
| install refuses while anything is missing | module :1647-1656 / cartridge :5996-6005 | `var ready = required(doc); … if (ready.missing.length) { state.waiting_for = ready.missing.slice(); return false; }` |
| only then: style, bar, proxies, moves | :1658-1669 / :6007-6023 (the cartridge omits the search move and says why at :6011-6016) | `installStyle; bar = buildBar; buildLayerControls(ready.found);` then the eight `move(panels.…)` calls |
| the masthead is moved into the bar's centre | :1671-1679 / :6033 | `move(brandSlot, ready.nodes.header)` — the SAME `.hud-header` node, "never a closed panel" |
| the bar is inserted as the map container's first child | :1688-1689 / :6042-6043 | `ready.nodes.host.insertBefore(bar, ready.nodes.host.firstChild); documentElement.classList.add('gridatlas-menu-hosted')` |
| bar height is measured, not assumed | :387-402 | `syncAttribClearance`: reads `bar.getBoundingClientRect().height`, sets `--gridatlas-menu-bar-clear = height + 8`; ResizeObserver :1690-1697 |
| one click + one change listener, installed once | :1711-1727 | "The retry path cannot multiply effects" |
| late adoption | :1554-1645, :1739-1745 | `adoptLate()` from a MutationObserver re-homes late nodes; the `lastElementChild` guard at :1612-1618 prevents the feedback loop that "crashed the renderer outright under the 393x852 arrival gate" |
| retry loop | :1770-1797 / :6124-6151 | `start()`: refuses a partial DOM; `install()` now, else every 250 ms; after 160 tries `loudFailure` |
| **loud failure** | :1752-1768 / :6106-6122 | `console.error('[GRIDATLAS MENU] menu not installed: expected 60 engine + 3 Pipeline News layer controls; found a + b')` and a fixed `role=alert` strip: "… Original controls remain available." |
| identity surface | :1734 | `state.one_identity_surface = true` (the v8 wordmark nodes are moved, never cloned; `#fs-letterhead` hidden at :371 `.gridatlas-menu-hosted #fs-letterhead{display:none!important}`) |

### A5. The logo: which file, its pixel size, its position, what it links to

| fact | key | value |
|---|---|---|
| which file | gridatlas@5ec7f62 atlas/releases/202608300453-atlas-v9/index.html:29-32 + ventusv8.css:7-8 | no image: the `<div class="ventus-brand">` with `.ventus-main` "Ventus" and `.ventus-sub` "Cables &amp; Connectivity&reg;" (rendered uppercase by CSS) |
| where it sits | module :1679 + :481-503, CSS :184-205 | inside `.gm-brand-slot`, the centre zone of the 36 px bar, flex-centred between the two `flex:1 1 0` side groups |
| the slot | CSS :184-186 | `.gm-brand-slot{flex:0 1 auto;min-width:0;max-width:64%;display:flex;align-items:center;justify-content:center;overflow:hidden;padding:0 6px;text-align:center}` |
| the fused header | CSS :187-194 | `.hud-header{display:flex!important;position:static!important;width:auto!important;gap:11px;margin:0;padding:0;background:none;border:0}`; children `line-height:1.05`; `small 6.5px`; `.hud-val 10.5px` |
| **wordmark size in the bar (desktop)** | CSS :203-205 (cartridge :4552-4554) | `.ventus-main{font-size:14px;font-weight:800;letter-spacing:.2em;margin:0;color:#fff}`; `.ventus-sub{font-size:5.5px;letter-spacing:.14em}` (face inherited from ventusv8.css:7-8: `-apple-system, sans-serif`, uppercase) |
| **wordmark size in the bar (≤ 700 px)** | CSS :372-378 (cartridge :4721-4727) | `@media(max-width:700px)`: bar 34 px; `.gm-brand-slot{max-width:48%;padding:0 2px}`; the clock and the 2050 countdown (`.hud-header>div:first-child`, `:last-child`) `display:none` so only the wordmark remains; `.ventus-main{font-size:11px;letter-spacing:.14em}`; `.ventus-sub{font-size:4.5px}` |
| why | CSS prose :176-183 | "'The VENTUS logo is the best part' — the architect's own words. It is the hero of this strip: sized and weighted to outrank the six menu titles either side of it" |
| what it links to | shell index.html:29-32 (a `div`, no `href`, no `onclick`); measured `insideAnchor:false` (A9) | nothing; it is identity, not navigation |
| second and third wordmarks | :371 (`#fs-letterhead` hidden when hosted); :1685 (`.scada-brand` moved into the Grid panel head) | one identity surface: the same words appear in the bar and at the head of the Grid panel; the fullscreen letterhead is suppressed |
| measured, 1280×800 (local composition, see Method) | /tmp/nl010/team-1/B/ga-desktop1280.json | see A9 |

### A6. Where labels and commands sit relative to the map (the CSS that positions them)

| rule | key | value |
|---|---|---|
| **the bar** | module :166-172 / cartridge :4515-4521 | `#gridatlas-menu-bar{position:absolute;top:0;left:0;right:0;height:36px;z-index:10020;display:flex;align-items:stretch;gap:0;padding-left:env(safe-area-inset-left);padding-right:env(safe-area-inset-right);box-sizing:border-box;background:rgba(4,10,13,.95);border-bottom:1px solid rgba(80,220,240,.3);font:11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;backdrop-filter:blur(7px);isolation:isolate}` — absolute inside `.map-container` (it is inserted as that container's first child, :1688), i.e. the bar lies ON the map's top edge |
| **a title** | :174-176 / :4523-4525 | `.gm-title{appearance:none;border:0;background:transparent;color:#cfeef6;min-height:36px;padding:0 11px;font:inherit;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap}` |
| title hover / open | :177-178 | `background:rgba(80,220,240,.16);color:#fff`; focus ring `2px solid #6bebff` :179-180 |
| side groups | :181-183 | `.gm-side{display:flex;align-items:stretch;flex:1 1 0;min-width:0}` left `justify-content:flex-start`, right `flex-end` |
| **a panel (dropdown)** | :206-210 | `.gm-panel{position:absolute;top:100%;left:0;min-width:240px;max-width:min(92vw,420px);max-height:min(72dvh,620px);overflow:auto;overscroll-behavior:contain;padding:6px;background:rgba(4,10,13,.98);border:1px solid rgba(80,220,240,.32);border-top:0;box-shadow:0 12px 34px rgba(0,0,0,.68)}` |
| right-hand panels | :219 | `.gm-side-right .gm-panel{left:auto;right:0}` |
| **a command in a panel** | :220-225 | `button,[role=button]{display:flex;align-items:center;width:100%;min-height:44px;position:static!important;margin:0 0 3px;padding:7px 10px;border:0;border-radius:2px;color:#cfeef6;font:11px/1.35 ui-monospace…;text-align:left;letter-spacing:.03em;text-transform:none}` |
| a group heading in a panel | :244-246 | `.gm-layer-group{margin:5px 0 2px;padding:6px 8px 3px;border-top:1px solid #19343b;color:#6fa2ae;font-size:10px;letter-spacing:.08em;text-transform:uppercase}` |
| a layer row | :253-269 | `.gm-layer{display:flex;gap:10px;min-height:44px;padding:7px 9px}`; the `<input>` is `position:absolute;inset:0;opacity:0` (full-row hit target); `.gm-layer-box` 20×20, checked `#4fd7ee` |
| Grid panel columns | :275-284 | `min-width:min(94vw,360px);max-width:min(96vw,900px)`; `@media(min-width:560px)` 2 columns, `(min-width:900px)` 3 |
| search inside File | :285-289 | `.search-bar-wrapper{position:static!important;display:grid;grid-template-columns:minmax(150px,1fr) auto;width:min(82vw,390px)}`; `.search-input{min-height:44px}` |
| attribution clears the bar | :357-358 | `.gridatlas-menu-hosted .custom-map-attrib{top:var(--gridatlas-menu-bar-clear,44px)!important;z-index:10025!important}` |
| **phone rule** | :372-382 / :4721-4731 | `@media(max-width:700px){#bar{height:34px} .gm-title{min-height:34px;padding:0 6px;font-size:9px;letter-spacing:.025em} .gm-brand-slot{max-width:48%} … .gm-panel{position:fixed;top:34px;left:4px!important;right:4px!important;width:auto;max-width:none;max-height:calc(100dvh - 40px);padding-bottom:calc(6px + env(safe-area-inset-bottom))} .gm-panel-grid{max-width:none}}` |
| the v8 layers panel stays under the map on desktop, collapsed on a phone | :293-330 | `.gridatlas-menu-hosted .scada-wrapper{display:flex!important}`; `#gridatlas-dash-toggle{display:inline-flex!important}`; prose: "restore v8 panels but keep dropdowns file, edit, scope, grid, about" (the architect, 2026-09-04) |
| sheet stacking | :333-334 | `html.gridatlas-sheet-open #bar{z-index:10020;pointer-events:auto}` |
| what is left ON the map at rest (measured, A9) | the live cartridge keeps the shell's search bar in `.map-container` (cartridge :6011-6016; the module file's :1662 move is the one line the cartridge dropped); the gazetteer cartridge (`atlas/current.json:58-65`, id `uk-gazetteer-flyto`, `202609071213-place-global-search-v9-5.js`, replace-script for `202608291818-place-postcode-search.js`) gives it its placeholder and results; measured on the map: at 1280×800 "Search project, address, postcode" + GO at the top right, 36 px under the bar (partner's measurement (981.8,77) 283×24; my screenshot `ga-desktop1280.png`); on a phone it is a 44 px row (partner: (135.8,77) 261×44 on Pixel 7). Also on the map: the GRID and SUBS chips (A9) and, on a phone, the v8 `LAYERS` toggle and the sandbox's collapsed "Tools ▸" strip. | the sld-sandbox cartridge adapts to the bar: `atlas/cartridges/202609241334-sld-sandbox-v9-8.js:3907` (`top = max(bounds.top, #gridatlas-menu-bar bottom)`), `:5834` (`stack.classList.add('gm-tools-collapsed')`), `:8611` (reads the bar's rect) |

### A7. The palette the shell draws with (for "consistent UI")

| colour | where in the bar | key |
|---|---|---|
| ground `rgba(4,10,13,.95)` bar, `.98` panel | bar, panel | module :169, :208 |
| cyan line `rgba(80,220,240,.3)` / `.32` | bar border-bottom, panel border | :169, :209 |
| title ink `#cfeef6`, hover `#fff` on `rgba(80,220,240,.16)` | titles, commands | :174, :178, :226-227 |
| group heading `#6fa2ae` on `#19343b` rule | panel groups | :245-246 |
| checked layer `#4fd7ee`, box border `#4a8b96`, focus `#6bebff` | layer rows | :259-266, :180 |
| wordmark `#fff`, sub `#888` | brand | ventusv8.css:7-8 |
| the estate's shared meanings (cyan instrument `#2ee6e6`, green energised `#22ee77`, amber attention `#ffb000`, magenta selected `#ff2bd6`, ground `#090c13`) | the Kuiper's declared palette, which names GridAtlas chrome as cyan | kuiper-belt@018b46a PALETTE.md:8-15, :20-21 |

### A8. The ledger: how the bar got here (owner-facing history on the page)

All in the cartridge's on-page version ledger, gridatlas@5ec7f62 atlas/cartridges/202609062358-substation-intelligence-v9-63.js:4212
(one JSON line; entries quoted by version): v9.92 "collapse the chrome into File, Edit, View and About at the top,
closed at rest"; v9.95 "withdraw the menu bar from the live Atlas on two testers' evidence"; v9.100 "Consolidate the
existing interface into exactly File, Edit, View, Scope, Grid, and About menus; expose all 60 engine and 3 Pipeline
News layer controls through their original handlers; … remain closed at rest and fail closed unless all 63 unique layer
controls exist"; v9.104 "Grid keeps each layer tick plus its live V8 status visible"; v9.110 "the v8 VENTUS masthead is
fused into the six-menu bar's own centre so it is present at every width and cannot be torn into a closed panel";
v9.111 "Hide the v8 fullscreen letterhead whenever the menu bar hosts the fused VENTUS masthead"; v9.116 "Bring the v8
layers panel back beneath the menu bar, open on a desktop and collapsed with its toggle visible on a phone"; v9.117
"About: the map attribution moves in, last and in small print … File: the engine's canonical modules are listed";
v9.120 "View gains a Studies group"; v9.121 "File gains an Export group"; v9.131 "GRID and SUBS chips on the map at
every width".

### A9. Measured geometry of the live shell (local composition, Chromium/SwiftShader; see Method)

Recorded in `/tmp/nl010/team-1/B/ga-<viewport>.json` and screenshots beside them (also the partner's independent run
`/tmp/nl010/team-1/measure-desktop-1280x800.json`, which agrees on the bar and the titles). Numbers are
`getBoundingClientRect` after the bar installed through its own admission rule (`installed:true`, `layer_controls:63`,
`panel_counts {File 8, Edit 1, View 5, Scope 4, Grid 3, About 8}` in the partner's state dump).

| viewport | measurement | value |
|---|---|---|
| 1280×800 | composition | `__GRIDATLAS_ATLAS__` generation `202610292044` (the clone's pointer); `menuBar.installed true`, `layer_controls 63`, `panel_counts {File 8, Edit 1, View 5, Scope 4, Grid 3, About 8}`, 0 page errors |
| 1280×800 | `#gridatlas-menu-bar` | x 5 y 5, **1270 × 36 px**; `position:absolute`; font `11px/11px ui-monospace, SFMono-Regular, Menlo, monospace`; background `rgba(4,10,13,.95)`; border-bottom `1px solid rgba(80,220,240,.3)`; z 10020; `.map-container` 1272 × 458 at (4,4), so the bar is the top 36 px OF the map |
| 1280×800 | titles (text x,y w×h) | File 5,5 51×36 · Edit 56,5 51×36 · View 106,5 51×36 · Scope 1109,5 58×36 · Grid 1166,5 51×36 · About 1217,5 58×36; computed `11px`, `letter-spacing 0.55px`, uppercase, `rgb(207,238,246)` (= `#cfeef6`) |
| 1280×800 | `.gm-brand-slot` | x 516 y 5, 247 × 35 px (centred: 511 px of bar either side) |
| 1280×800 | **`.ventus-main` in the bar** | rect x 607 y 12, **76 × 15 px**; computed `14px`, weight `800`, `letter-spacing 2.8px` (= .2em), `-apple-system, sans-serif`, `rgb(255,255,255)`, uppercase; `insideAnchor:false`, no `onclick` |
| 1280×800 | **`.ventus-sub` in the bar** | rect x 600 y 27, **90 × 6 px**; `5.5px`, `letter-spacing 0.77px`, `rgb(136,136,136)` |
| 1280×800 | `.hud-header` parent | `gm-brand-slot` (the v8 node was moved, A4); `#fs-letterhead` computed `display:none` |
| 1280×800 | panels when opened (x,y w×h) | File 5,40 240×373 · Edit 56,40 240×60 · View 106,40 240×181 · Scope 926,40 240×201 · Grid 841,40 376×576 · About 1035,40 240×438 — every panel's top is 40 = bar bottom (5 + 36 − 1); left-group panels hang from their title's left edge, right-group panels end at the bar's right edge (A6 :219) |
| 1280×800 | panel contents seen | File: Export CSV, Export this view, Print/PDF, Print source code, Save PDF, Save image · Edit: Status Colours · View: ⛶, GB prices historic, Exit, Studies · Scope: Radius Search, Radius Area, Poly Zone, Measure · Grid: group headings (Topology, Assets, Supermarkets…) with `400kV [OK]`-style rows · About: Versions v9.138, Estate (Grid engine · the maths, Federation map, Spider printer), OpenStreetMap / Open Charge Map credit |
| 1280×800 | screenshots | `/tmp/nl010/team-1/B/ga-desktop1280.png`, `ga-desktop1280-menu0..5.png` (File … About open) |
| 360×780 and Pixel 7 | | see the rows below |
| 360×780 (`isMobile, hasTouch, dsf 3`) | composition | `installed true`, `layer_controls 63`, `panel_counts {File 8, Edit 1, View 5, Scope 7, Grid 3, About 8}` (Scope gains the mobile tray's three routed chips), 0 page errors |
| 360×780 | `#gridatlas-menu-bar` | x 5 y 5, **350 × 34 px**, `position:absolute` inside `.map-container` (4,4 352×768); computed bar `font-size 11px`, titles `9px`, `letter-spacing 0.225px`, `padding 0 6px`, `min-height 34px` |
| 360×780 | titles (text x,y w×h) | File 5,5 34.6×34 · Edit 39.6,5 34.6×34 · View 74.2,5 34.6×34 · Scope 240,5 40.2×34 · Grid 280.2,5 34.6×34 · About 314.8,5 40.2×34 — **one row** (all y = 5); six titles sum 218.8 px; last right edge 355 = bar right |
| 360×780 | `.gm-brand-slot` / `.hud-header` | slot x 141.2, 77.6 × 33 (centre 180 = viewport centre); `.hud-header` 143.2,13.4 73.6×16.3; its three children computed `display` = `none, flex, none` (clock and 2050 counter hidden by the phone rule, A5) |
| 360×780 | **`.ventus-main`** | x 152.2 y 13.4, **55.5 × 11.5 px**; `11px`, weight `800`, `letter-spacing 1.54px` (= .14em), `-apple-system, sans-serif`, `rgb(255,255,255)`; `insideAnchor:false` |
| 360×780 | **`.ventus-sub`** | x 143.2 y 24.9, **73.6 × 4.7 px**; `4.5px`, `letter-spacing 0.63px`, `rgb(136,136,136)` |
| 360×780 | on the map at rest | the two chips `⚡ Grid` (15,697) 65.7×44 and `◉ Subs` (84.7,697) 65.7×44 (`chipStaysOnMap`, A3); `.scada-wrapper` collapsed to 352×0 at y 776; `#fs-letterhead` `display:none`; `.custom-map-attrib` 0×0 (moved into About) |
| 360×780 | the Grid panel when opened | (9,39) 342 × 740 px, `position:fixed` (the phone rule `top:34px;left:4px;right:4px;max-height:calc(100dvh - 40px)`) |
| Pixel 7 (412×839) | the same, wider | bar (5,5) 402×34, one row; titles File 5 · Edit 39.6 · View 74.2 · Scope 292 · Grid 332.2 · About 366.8 (same widths); slot x 167.2 77.6×33 (centre 206 = viewport centre); `.ventus-main` 178.2,13.4 55.5×11.5 11px/800/1.54px; `.ventus-sub` 169.2,24.9 73.6×4.7; chips `⚡ Grid` (15,756) 65.7×44, `◉ Subs` (84.7,756) 65.7×44; 0 errors |
| all | screenshots | `/tmp/nl010/team-1/B/ga-w360.png`, `ga-w360-grid.png`, `ga-pixel7.png`; the partner's independent run (`/tmp/nl010/team-1/measure-*.json`, `brand.out`, `FIXES/NL-010/team-1/img/gridatlas-bar-*.png`) gives the same numbers for the bar, the titles, the slot and the wordmark at 1280, 412 and 360 (and adds 863×360 landscape: bar 36 px, full lockup back, panels `absolute`) |

Caveat on one number in the partner's dump: its `ventusMain` block (`font-size 15px, letter-spacing 5px, rect 0×0`)
is the hidden `#fs-letterhead .ventus-main` (first match in document order, ventusv8.css:104), not the wordmark in the
bar; the bar's own wordmark is the `#gridatlas-menu-bar .ventus-main` node measured above.

---

## B. The Kuiper hooks the shell attaches to (kuiper-belt@018b46a)

### B1. The engine (`index.html`, 594 lines; Edition 4 carries a copy with the edition layer appended)

| hook | engine key | Edition 4 key (editions/202611012027/index.html) | what it is |
|---|---|---|---|
| `#top` (the header: `#big` title, `#sub` subtitle) | index.html:15-16, DOM :61 | :15-16, DOM :89 | `position:fixed;top:0;left:0;padding:10px 14px;z-index:10;max-width:60vw;background:#090c13d9`; `#big` 19px → cyan uppercase 15px `.16em` (:29) |
| `#hud` (the readout) | :17, DOM :62 | :17, DOM :90 | `fixed;top:0;right:0;…;text-align:right;white-space:pre-line;max-width:38vw` |
| `#card` | :18-20, DOM :63 | :18-20, DOM :91 | `fixed;left:14px;bottom:64px;z-index:10;background:#090c13ee;border:1px solid var(--line);padding:9px 12px;white-space:pre-line;display:none;max-width:min(680px,92vw)`; `#card b{color:var(--hot)}` → amber (:32) |
| `#foot` (the commands) | :21-23, DOM :65-73 | :21-23, DOM :93-101 | `fixed;left:0;right:0;bottom:0;padding:8px 14px;border-top:1px solid var(--line);background:#090c13ee;z-index:10;line-height:1.7`; `#keys` buttons (new code, random line, find, [next verified line,] whole wafer) at :37-42 / :93-95 |
| `#goto` (the `/` box) | :24-26, DOM :64 | :24-26, DOM :92 | `fixed;left:50%;top:38%` |
| page face | :11 | :11 | `font:12px/1.55 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace`; `--bg:#090c13 --ink:#d5dcea --dim:#7d8799 --line:#1a2030 --hot:#e8b36a` (:8); SCADA meanings `--cy:#2ee6e6 --gn:#22ee77 --am:#ffb000 --mg:#ff2bd6` (:27-28) |
| phone rule (≤ 640 px) | :44-56 | :44-56 | `#top,#hud` full width strips; `#big` 13px; `#sub` collapsed until `#top.open`; `#card{left:8px;right:8px;max-height:34vh}`; `#foot .long{display:none}`; `#keys button{padding:9px 11px}` |
| `layout()` | :231-233 | :258-261 | HUD under the header on a phone; `card.style.bottom = foot.offsetHeight + 10` ("the card never hides the commands") |
| **`safeBox()`** | :234-240 | :262-268 | measures `#top`, `#hud` (bottom edge) and `#foot` (top edge) with `getBoundingClientRect` and returns `{x0:8, x1:innerWidth-8, y0:top+8, y1:max(top+24, bot-8)}`; prose :226-230: "Nothing here is assumed" |
| `homeCamera()` / `home()` | :244-249 | :270-275 | the wafer is fitted to `safeBox()`, radius `0.80 ×` half the smaller side |
| `show(a)` (the engine's card) | :387 | — | `card.style.display='block'; card.innerHTML = describe(a)` |
| card tap closes (engine) | :575 | — | `card.addEventListener('click', () => { card.style.display='none' })` |
| Backspace = whole wafer | :590 | :692 (edition adds `edSel=-1`) | |

### B2. Edition 4's bar and panels (the thing the GridAtlas shell replaces)

| hook | key (kuiper-belt@018b46a editions/202611012027/index.html) | what it says |
|---|---|---|
| prose: borrowed from GridAtlas | :694-696 | "Borrowed in spirit from gridatlas atlas/modules/202609031958-menu-bar.js: one row of titles, every panel hidden until its title is tapped, one open at a time…" |
| **`#bar` CSS** | :58-59 | `position:fixed;top:0;left:0;right:0;z-index:12;display:flex;gap:4px;align-items:center;padding:6px 8px;background:#090c13e6;border-bottom:1px solid #12414a;overflow-x:auto;white-space:nowrap` |
| `#barname` | :60 | `color:var(--cy);letter-spacing:.14em;font-size:12px;margin-right:8px;text-transform:uppercase` |
| `.gm-title` | :61-63 | `border:1px solid #12414a;background:transparent;color:#8fb3bd;font:inherit;text-transform:uppercase;letter-spacing:.08em;padding:6px 10px;touch-action:manipulation`; hover/`.gm-on` `rgba(80,220,240,.16)` `#fff` border cyan |
| panels hidden at rest | :64-65 | `#top,#hud,#foot,#lines{display:none}`; `.gm-open{display:block}` |
| panel geometry | :66-70 | `position:fixed;top:40px;…;max-width:min(680px,96vw);max-height:60vh;overflow:auto;z-index:11;background:#090c13f2;border:1px solid #1d6470;border-radius:0 0 6px 6px;padding:10px 12px`; `#hud{right:0;left:auto}`; `#lines{width:min(720px,96vw)}` |
| **phone rule that makes the bar wrap** | :83-84 | `@media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{font-size:11px;margin-right:4px} #bar .gm-title{padding:5px 8px} #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);…;max-height:62vh} }` |
| the bar is built | :697-703 | `bar.id='bar'; bar.innerHTML = '<span id="barname">KUIPER EDITION 4</span>' + four `<button class="gm-title" data-panel="top|hud|lines|foot">edition|readout|lines|commands</button>`; appended to body |
| the LINES panel | :704-708 | `#lines.gm-panel` with `#lyAll`, `#lyFocus`, next/previous, `#lyFind`, `#lineslist` |
| **`PANELS`** | :710 | `{ top: elTop, hud: hud, lines: linesPanel, foot: elFoot }` |
| **`placePanels()`** | :712-713 | every panel's `top = bar.getBoundingClientRect().height + 2`; re-run on `resize` |
| **`setPanel(name)`** | :714-720 | toggles `openPanel`, `.gm-open` on the panel, `.gm-on` on the title; `fillLines()` for LINES; `dirty = true` |
| close on tap / Escape / wafer | :721-723 | bar click → `setPanel`; `keydown Escape`; `cv pointerdown` |
| **`safeBox` wrapped to start under the bar** | :726 | `safeBox = function(){ const s = _safe(); s.y0 = Math.max(s.y0, bar.getBoundingClientRect().bottom + 8); s.y1 = Math.max(s.y0 + 24, innerHeight - 8); return s; }` |
| layer switches, list, filter | :728-744 | `lyOn`, `lyFocus`, `lyQuery`, `fillLines()` |
| draw / step wrappers | :654, :745-749 | `draw` wrapped with `drawEdition`; `edNext` honours the switches |

### B3. The card today (the thing the card law changes)

| hook | key | what it says |
|---|---|---|
| card CSS (Edition 4) | :76-82 | `#card{bottom:12px!important;z-index:13;max-height:30vh;overflow:auto;padding:8px 36px 8px 12px}`; `.cx` 26×26 close; `.cq` the quoted line (`border-left:2px solid #3a4150;white-space:pre-wrap`); `.cd` details hidden until `#card.open`; `.ct` toggle; phone `max-height:34vh;font-size:11px` |
| **`edCard(i)`: the header is the title, the key is the second line** | :655-666 | `card.innerHTML = '<button class="cx">×</button>' + '<b>' + esc(b.title) + '</b>  n of N' + '\n' + esc(b.repo) + '  ' + esc(b.path) + ':' + b.line + (quote ? '<div class="cq">…</div>') + '<a href=destination target=_blank>open on GitHub at ' + commit7 + '</a>' + ' · details' + '<div class="cd">pattern / found by / describe(a)</div>'` — so today `b.title` (the finding's title) is the header and `repo path:line` is the second line |
| card events | :668-674 | × closes; `details` toggles; the link is not swallowed; a tap on the body keeps it open |
| **`edFly(b)`** | :676-680 | zoom 14; `my` = midpoint between `safeBox().y0` and the top of the card (measured `card.getBoundingClientRect().height + 12`) |
| `edNext`, tap within 9 px, keys e/E | :682-692 | |
| the record a card is built from | editions/202611012027/keys.json (byte-identical since Edition 2; harness notes) | fields used: `title, repo, path, line, quote, destination, commit, pattern, worker, finding, key, on_wafer, verified, class` (:633-634, :656-664) |
| README's description of the card | editions/202611012027/README.md:16-18 | "The card is compact: the title with 'n of 344', the repository and `path:line`, the quoted line, the GitHub link at the commit, and a 'details' toggle" |

### B4. Where the card law has to be written (the owner: "the line code is the header have that clearly written")

| place | key | today |
|---|---|---|
| the page | editions/202611012027/index.html:655-666 (`edCard`) and the `#foot .long` sentence :96-101 | header = `b.title`; the foot names "its line and its GitHub link" |
| the edition README | editions/202611012027/README.md:16-18 ("The card is compact…") and :57 (the index.html row) | describes the card; does not state the law |
| the editions index | editions/README.md:3-4 (current-edition sentence), :8-11 (Edition 4 entry) | "each line keyed by `repo@commit path:line`" (:6) |
| the repository README | README.md:29-48 "The first law: no claim without a key"; :84-94 "The seventh law: every body must be openable"; :189-197 "Editions" | the laws are numbered in prose here and in LAWS.md |
| **LAWS.md** | LAWS.md:1-4 (header: "Each law below states what is measured, how it is computed, and what would prove it wrong. A law that cannot be falsified is not a law"); L1–L10 at :12, :26, :42, :57, :72, :82, :100, :111, :128, :139; the file ends at :172 after L10's "Falsified by" | a new law goes after :172 as L11 in the same shape (statement, derivation, **Falsified by:**) |
| the folder rule that governs any of these edits | SESSIONS/202611012145-kuiper-edition-harness-notes.md (this repository) "Rules that bind every edition" | every change is a new dated folder; `editions/index.html` names the stamp in three places |

### B5. Pointers, READMEs, licences, See Through, the homepage

| element | key | what it says |
|---|---|---|
| editions pointer | kuiper-belt@018b46a editions/index.html:7, :11, :12 | `meta refresh … url=202611012027/`, the link, `location.replace('202611012027/' + location.hash)` |
| See Through pointer | kuiper-belt@018b46a see-through/index.html:7, :11, :12 | the same three places → `202610050609/` |
| See Through, what it is | see-through/202610050609/README.md:1-3 | "fall from a field of stars to any of 5,800 UK substations, then watch it rise in 3D … Type a substation name and press GO" |
| See Through licence | see-through/202610050609/NOTICE.md:3 | CERN-OHL-S v2 |
| edition licences | editions/202611012027/NOTICE.md:3-5, :7-10 | code Apache-2.0, text/data CC BY 4.0; quoted lines keep their repository's licence (Apache-2.0, CERN-OHL-S v2, CC BY 4.0, ODbL 1.0, OGL v3) |
| Edition 4 README, the menu bar sentence | editions/202611012027/README.md:41-46 | "At rest the screen is the wafer and a menu bar: EDITION, READOUT, LINES, COMMANDS, each a layer…" |
| ci_check | kuiper-belt tools/ci_check.py (harness notes: K1 privacy, K3 page syntax; `RESULT: PASS` before push) | |
| how the estate presents its apps | globalgrid2050@c66759f homepage_versions/homepage_v134.html:13 (highlight cards, GridAtlas → `https://ventusltd.github.io/gridatlas/atlas/`), :18 (Kuiper section: What is the Kuiper, Learn the Kuiper, **See Through** "Open See Through →" `kuiper-belt/see-through/202610050609/`, Kuiper diary), :35 (entity `see-through`, "application"), :65 ("Funded by VENTUS LTD") | the homepage carries no image logo either: `grep -ni 'logo\|\.svg'` over v134 returns nothing but the title and these rows |

### B6. Measured geometry of Edition 4 (served from the kuiper-belt root, Chromium/SwiftShader, 7 s settle)

| viewport | `#bar` | `#barname` | titles (text, x, y, w, h) | rows | errors |
|---|---|---|---|---|---|
| 360×780 (`isMobile, hasTouch, dsf 3`) | 0,0 360×**75** px; font 11px ui-monospace; bg rgba(9,12,19,.9) | x 8 y 12, 131×17, cyan rgb(46,230,230) | edition 147,6 71×29 · readout 221,6 71×29 · lines 296,6 56×29 · **commands 8,39 78×29** | **two** (y 6 and y 39) | 0 |
| Pixel 7 (412×839) | 0,0 412×**75** | same | same four rectangles | **two** | 0 |
| 1280×800 | 0,0 1280×46; font 12px | x 8 y 13, 142×19 | edition 162,6 79×33 · readout 246,6 79×33 · lines 329,6 63×33 · commands 396,6 87×33 | one | 0 |

Source: `/tmp/nl010/team-1/B/measure-ed4-B.json`, screenshots `ed4-w360.png`, `ed4-pixel7.png`, `ed4-desktop1280.png`.
This agrees with FABLE-01 (FIXES/NL-009/round1/01-bar.md finding 1: 75.1 px at 360/393/412/430; content 416.6 px
against 344–414 px available) and FABLE-06 (06-seethrough.md finding 2).

### B7. NL-009 round 1 findings that bear on the shell (read 2026-11-01 20:53 UTC; three of ten files present)

| file | finding | consequence for steps 1–2 |
|---|---|---|
| FIXES/NL-009/round1/01-bar.md F1 BLOCKER | the bar is two rows on every phone width (75.1 px; COMMANDS alone on row 2) | the one-row rule at 360 px is a hard acceptance test |
| 01-bar.md F2 MAJOR | titles 29 px tall against 44/48 px touch targets | the GridAtlas bar is 34 px on a phone with 9 px titles (A6) — GridAtlas itself is UNDER 44 px; the step must say which it follows and why |
| 01-bar.md F3 MAJOR | no room for a fifth title at the present style; label size must follow width (`clamp(10px,2.75vw,12px)`), mark `KE4`/`KE5` instead of "KUIPER EDITION 4" | the brand zone + six titles budget at 360 px must be computed, not hoped |
| 01-bar.md F4–F6 MINOR | hover sticks after a tap (`(hover:hover)`), no safe-area insets on the bar, `vh` vs `dvh` | GridAtlas already uses `env(safe-area-inset-*)` on the bar (A6 :167-168) and `dvh` on panels (:207, :381) |
| 01-bar.md F7 PASS | `safeBox` and `placePanels` follow the measured bar height | the hooks at B2 hold under a taller or wrapped bar |
| 06-seethrough.md F1 BLOCKER | See Through unreachable from Edition 4 (`grep -ci see.through` → 0 in index.html and README) | a fifth entry `a.gm-title[href="../../see-through/"]` is patched in, same tab, through the pointer |
| 06-seethrough.md F5 | decisions: same tab (homepage has 0 `target=_blank`), link the pointer not the dated folder, no second APPS entry | Team 3 owns See Through; the shell must leave the slot |
| 09-robust.md F1 MAJOR | READOUT slides under the bar after a pick: the engine's `layout()` writes `hud.style.top` from a `display:none` `#top` (0 px); `placePanels()` only runs on resize and in `setPanel` | any new bar must own the panel tops the way GridAtlas's `syncAttribClearance` owns the attribution offset (A4) |
| 09-robust.md F2–F7 | no-WebGL refusal strip, `<noscript>`, keys.json 404 said on screen, Escape closes the card, reduced motion, ARIA (`role=toolbar`, `aria-expanded`/`aria-controls`, panels `role=region`, card `aria-live=polite`) | GridAtlas's bar already carries `aria-haspopup`, `aria-expanded`, `aria-controls`, `role=group` (A3 :505-516) |

---

## C. Gaps, negatives and things the reviewer will hold the steps to

1. **There is no Ventus logo file to copy.** The GridAtlas logo is text (A2 negative findings, A5). "Exactly like
   GridAtlas" therefore means: the same two lines, the same face stack (`-apple-system, sans-serif`), the same weight
   (800), the same tracking (`.2em` desktop / `.14em` phone in the bar), the same sizes (14 px / 5.5 px desktop,
   11 px / 4.5 px ≤ 700 px), white over `#888`, centred in the bar between the left three and the right three titles,
   not linked. A step that proposes an SVG, a PNG, a different face, or a link on the mark is not "exactly like GridAtlas".
2. **GridAtlas's bar is 36 px / 34 px, inside the map container (`position:absolute`), not `position:fixed` on the
   window.** The Kuiper's panels are `position:fixed` and its canvas is the whole window (`canvas{position:fixed;inset:0}`,
   editions/202611012027/index.html:13), so the Kuiper's bar can be `fixed` at `top:0` and be the same thing visually;
   the step should say so rather than pretend the CSS can be copied byte for byte.
3. **GridAtlas's phone titles are 9 px on a 34 px bar** (A6 phone rule), below the 44 px target NL-009 asks for. The
   step must choose: GridAtlas's numbers exactly (and record the hit-target debt), or 44 px titles (and record the
   departure from "exactly").
4. **The menu-name mapping needs one line of evidence per name.** GridAtlas: File = open/search/export/modules,
   Edit = colours, View = fullscreen/studies, Scope = measuring tools, Grid = the layer switches, About = ledger,
   attribution, estate links (A3 table). The Kuiper's present four are EDITION, READOUT, LINES, COMMANDS (B2 :697-703).
5. **The live generation moved after the clone** (A1 table: `202610292044` in the clone, `202610312138` on
   origin/main). The shell bytes did not (the preview and release of NL-007 changed `uk-offtakers-overlay` and the pointer
   only; `git diff main` on the shell files is empty); any step that quotes the live generation should quote `202610312138`
   and say the shell is unchanged.
6. **The admission rule is the lesson, not the number 63.** GridAtlas counts its 63 original inputs because they exist
   in the v8 DOM before the bar does (A4). The Kuiper's equivalents are the hooks at B1–B2: `#top #hud #foot #card`,
   `safeBox`, `setPanel`/`placePanels`, `PANELS`, `keys.json` loaded (`edPlaced.length`), `cosmos/wafer.tsv` loaded.
   A Kuiper bar module should refuse, loudly and visibly (09-robust F2's `#refuse` strip exists for exactly this), when
   any of these is missing.
7. **Owner's words, mapped to evidence** (for the review): "logo exactly like gridatlas on the top" → A5; "labels and
   commands must be like the gridatlas not near the top copy the gridatlas UI" → A3, A6 (titles in the bar, commands in
   dropdown panels at 44 px rows, group headings, the two chips that stay on the map); "keep it consistent and build it
   around the kuiper" → B1–B2 (the bar is the only chrome; everything else is a layer; `safeBox` gives the wafer the
   rest); "the line code is the header have that clearly written" → B3 (`edCard` :655-666 puts `b.title` first today),
   B4 (page, README, LAWS.md L11).
