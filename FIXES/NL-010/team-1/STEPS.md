REVIEW: OPEN

# NL-010 team 1 ("the shell"): steps 1 and 2

Architect FABLE-T1A; evidence officer FABLE-T1B (EVIDENCE.md, REVIEW.md in this folder). Channel: issue #10.
Keys: `gridatlas@5ec7f62` is `/home/user/estate/gridatlas` at 5ec7f62f213e2d20a02e86427daa182c0f38e4a4 (main, 31 Oct 2026);
`kuiper-belt@018b46a` is `/home/user/estate/kuiper-belt` at 018b46aed50f28f7b1882a0dcaba6593ce522beb (main, Edition 4);
`nl@FIXES/NL-009/round1/...` are the Android audit files in this repository, read at 20:55 UTC and again before posting.

## How the live GridAtlas shell was measured (the keys behind every number below)

Served `/home/user/estate/gridatlas` with `python3 -m http.server 8201`, opened `http://127.0.0.1:8201/atlas/` in
Playwright Chromium (SwiftShader flags from the harness notes) at 1280×800, `devices['Pixel 7']` (412×839 css px,
dpr 2.625, touch), a 360×740 phone and `devices['Pixel 7 landscape']`. Scripts and raw JSON:
`/tmp/nl010/team-1/measure-gridatlas.cjs`, `measure-brand.cjs`, `measure-*.json`, `panels-*.json`, `brand-measure.json`,
screenshots `shell-*.png`, `brand-*-bar.png`, `menu-*.png` (scratch, not committed; copies of the bar strips are under
`FIXES/NL-010/team-1/img/` if the harness wants them).

Limitation, stated: the sandbox proxy denies `cdn.jsdelivr.net` and `basemaps.cartocdn.com` (curl: `CONNECT tunnel
failed, response 403`). Without them MapLibre never fires `load`, the engine never builds its 63 layer controls, and the
menu bar refuses to install, exactly as its admission rule says: the page showed the strip
`#gridatlas-menu-bar-failure` "menu not installed: expected 60 engine + 3 Pipeline News layer controls; found 0 + 0"
at (8,8) 1264×33 px (`measure-desktop-1280x800.json`, first run). That refusal is itself lesson 1.4 below. For the
measurements the two hosts were answered from the page's own origin: `maplibre-gl@3.6.2` from the See Through vendor
copy (`kuiper-belt@018b46a see-through/202610050513/vendor/maplibre-gl.js`, MapLibre 4.7.1) and the Carto style as an
empty style with one background layer. Every other external request was aborted. The shell's HTML, CSS and the menu
module's bytes are the served ones; only the basemap is a stub, and no number below depends on a tile.

## What the live GridAtlas shell is (measured 1 Nov 2026)

The composed page is the immutable shell `atlas/releases/202608300453-atlas-v9/index.html` with the six cartridges of
`atlas/current.json` (generation 202610292044, `IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES`); the menu bar is the module
`atlas/modules/202609031958-menu-bar.js` inlined into the live `substation-intelligence` cartridge
`atlas/cartridges/202609062358-substation-intelligence-v9-63.js` (schema `gridatlas.menu-bar.v2` at its line 4376;
`MENUS = ['File','Edit','View','Scope','Grid','About']` at 4380). Keys for every CSS value are given against the
module file; the same text sits in the cartridge at lines 4515–4731.

| what | measured (1280×800) | measured (Pixel 7, 412 px) | measured (360 px) | source of the value (key) |
|---|---|---|---|---|
| bar element | `nav#gridatlas-menu-bar`, `aria-label="Atlas menu"`, rect (5,5) 1270×36, `position:absolute; top:0; left:0; right:0` inside `.map-container` (the map's 1 px border puts it at 5,5), z-index 10020 | (5,5) 402×34 (the same 1 px border; `position:absolute` inside `.map-container`, which is 404×827) | (5,5) 350×34 | `menu-bar.js:167-172`, `:480-483` |
| bar height | 36 px | 34 px (`barHeightCSS 34px`) | 34 px | `:167` (36), `:372` (`@media(max-width:700px)` 34) |
| bar background, border, blur | `rgba(4,10,13,.95)`, `border-bottom:1px solid rgba(80,220,240,.3)`, `backdrop-filter:blur(7px)` | same | same | `:169-171` |
| bar font | `11px/1 ui-monospace,SFMono-Regular,Menlo,monospace` | titles 9px | titles 9px | `:170`, `:373` |
| menu titles | FILE EDIT VIEW left group; SCOPE GRID ABOUT right group; `button.gm-title`, uppercase, `letter-spacing:.05em` (0.55 px), `color:#cfeef6`, `padding:0 11px`, `min-height:36px`; widths 50.7/50.7/50.7 and 57.9/50.7/57.9 px; one row at y=5 | 9 px, `letter-spacing:.025em` (0.225 px), `padding:0 6px`, `min-height:34px`; widths 34.6/34.6/34.6 and 40.2/34.6/40.2 px (sum 218.8); one row, `titleRows:1`, last right edge 407 = bar right, `scrollWidth 402 = clientWidth` | same widths (sum 218.8 px); one row; last right edge 355 = bar right; no horizontal scroll | `:174-177`, `:373`, `buildBar :504-535` (index<3 → left) |
| title hover / open | `background:rgba(80,220,240,.16); color:#fff`; focus ring `2px solid #6bebff` inset | same | same | `:178-181` |
| the three zones | `.gm-side-left` (5,5) 511×35 · `.gm-brand-slot` (516,5) 247×35 · `.gm-side-right` (764,5) 511×35; the two sides are `flex:1 1 0`, so the brand is centred whatever the titles weigh | sides 162.2 px each, slot (167.2,5) 77.6×33 (`max-width:48%`, `padding:0 2px`) | sides 136.2 px each, slot (141.2,5) 77.6×33 | `:181-183`, `:192-194`, `:486-500` |
| the Ventus logo: what it is | **not an image file.** `find` for `*logo*`, `*ventus*.png|svg` in the repository: none; `img`/`svg` inside the bar: 0. It is the v8 masthead `div.hud-header` (shell `index.html:23-33`) moved as the same DOM node into the brand slot (`move(brandSlot, ready.nodes.header)` `:1679`), holding `div.ventus-brand > div.ventus-main "Ventus" + div.ventus-sub "Cables &amp; Connectivity&reg;"` | same node | same node | shell `index.html:29-32`; `ventusv8.css:6-8`; `menu-bar.js:184-205`, `:1671-1679` |
| logo natural size (as the v8 masthead, before the menu installs) | `.ventus-brand` 130.3×30.2 at (574.8, 22.9) in a 1272×68 `.hud-header`; `.ventus-main` 17px/800/5px tracking/#fff uppercase; `.ventus-sub` 6.5px/#888/2px | — | — | first-run `measure-desktop-1280x800.json` (bar not installed); `ventusv8.css:7-8` |
| logo rendered size in the bar | `.ventus-brand` **90.0×20.5 at (599.7, 12.3)**: `.ventus-main` 14px/800/`.2em`/#fff, `.ventus-sub` 5.5px/`.14em`/#888 uppercase; flanked by SYSTEM TIME (66×35) and 2050 TARGET (57×23), gap 11 px | `.ventus-brand` **73.6×16.3 at (169.2, 13.4)**; `.ventus-main` 55.5×11.5, 11px/800/1.54px (`.14em`)/#fff; `.ventus-sub` 73.6×4.7, 4.5px/0.63px/#888; clock and counter `display:none` | `.ventus-brand` 73.6×16.3 at (143.2, 13.4); same type | `:195-205` (desktop), `:374-378` (phone: `.ventus-main` 11px `.14em`, `.ventus-sub` 4.5px, first and last `.hud-header>div` hidden, slot `max-width:48%`) |
| logo position | horizontally centred in the bar (slot centre 640.0 = viewport centre), vertically centred (12.3+20.5/2 = 22.5 ≈ 5+36/2) | slot centre 206.0 = viewport centre 206; brand vertical centre 21.55 vs bar centre 22.0 | slot centre 180.0 = viewport centre 180 | `:192-199` |
| logo link | **none**: `vm.closest('a')` null, no `onclick`, cursor default; the wordmark is identity, not navigation; `#fs-letterhead` (a second copy) is `display:none` under the bar | same | same | `:355-371`, `brand-measure.json brandIsLink:false` |
| where labels and commands sit relative to the map | after install **nothing floats on the map except the search box**: `.search-bar-wrapper` (981.8, 77) 283×24 (right, 36 px under the bar) and the v8 `HIDE LAYERS` toggle at the bottom-right (1135.6, 744) 132×44 of the desktop's lower SCADA panel. Moved into the menus as the same nodes: `.map-controls` (Export, Radius search, Radius area, Poly zone, Status, Measure: `display:none` at rest), `#btn-fullscreen`, `.custom-map-attrib`, `.disclaimer-box`, `.podcast-shoutout`, `.scada-brand`; `controls_moved: 17`, `layer_controls: 63 (60+3)`, `panel_counts {File:8, Edit:1, View:5, Scope:4, Grid:3, About:8}` | three things, all 44 px tall: `.search-bar-wrapper` (135.8, 77) 261×44 (right edge 397, 10 px in from the bar's), a collapsed phone tools strip `.map-controls.gm-tools-collapsed` "Tools ▸ ⚡ Grid ◉ Subs" (15, 756) 135×44 bottom-left, and the v8 `▴ LAYERS` toggle (308.5, 783) 91.5×44 bottom-right above a collapsed SCADA wrapper (height 0); `controls_moved: 20`, `panel_counts {File:8, Edit:1, View:5, Scope:7, Grid:3, About:8}`; the Grid panel holds 63 checkboxes in 13 groups. Open panels sit at (9, 39) 394 px wide, `fixed`; File 373 px tall with 7 rows of 44 px and 20 px group headings, Grid 799 px and scrolls (`panels-pixel7.json`) | search (83.8, 77) 261×44; toggle (256.5, 684) 91.5×44; otherwise the same | `required() :143-159`, `install :1647-1720`, state `NS.menuBar` |
| panels | `.gm-panel` `top:100%` of its title, `min-width:240px; max-width:min(92vw,420px); max-height:min(72dvh,620px)`, `rgba(4,10,13,.98)`, border `1px solid rgba(80,220,240,.32)` no top; right-group panels `right:0`; every row `min-height:44px`, `11px/1.35` same mono, `#cfeef6`, hover `rgba(80,220,240,.14)`; group headings `.gm-layer-group` 10px `#6fa2ae` uppercase `.08em` | all six panels `position:fixed` (`top:34px; left:4px; right:4px; max-height:calc(100dvh - 40px)`) | same (`fixed`); in landscape 863×360 the bar is 36 px again and the panels `absolute`, because the rule is on width, not on the device | `:206-213`, `:218-224`, `:245-247`, `:379-382` |
| one open at a time, closed at rest | `closed_at_rest:true`; Escape closes; ArrowLeft/Right between titles; ArrowDown opens | same | same | `:405-445`, `:539-577` |
| admission rule | installs nothing until the 63 controls and 11 named nodes exist; otherwise publishes `#gridatlas-menu-bar-failure` and leaves the old interface reachable (measured, see limitation) | same | same | `:1-22`, `:30`, `:134-159`, `:1647` |

Landscape Pixel 7 (863×360): bar (5,5) 853×36, titles 11 px (50.7/57.9 px), the full lockup with SYSTEM TIME and 2050
TARGET back (`.ventus-brand` 90×20.5 at (391.2, 12.3)), panels `absolute`: the phone rule is `max-width:700px`, so a phone
in landscape gets the desktop bar (`brand-measure.json`).

What the Kuiper has today, for contrast (`kuiper-belt@018b46a editions/202611012027/index.html`): `div#bar`
`position:fixed; top:0`, padding 6px 8px, `#090c13e6`, border `#12414a`, a text title `KUIPER EDITION 4` 12px cyan
`.14em` and four bordered buttons EDITION READOUT LINES COMMANDS (`:58-63`, `:699-703`); the commands sit as a `#keys`
strip and a long sentence inside the EDITION panel (`:94-96`); no Ventus wordmark anywhere in the page (`grep -i ventus`
→ only two GitHub links); the bar wraps to two rows (75.1 px) on every phone width and the titles are 29 px tall
(`nl@FIXES/NL-009/round1/01-bar.md` findings 1–2, `06-seethrough.md` finding 2).

---

## Step 1 — The shell contract: the GridAtlas bar, logo and menus built around the wafer

**Goal.** The Kuiper's next edition opens under the same shell as the live GridAtlas: one 36 px bar (34 px on a phone)
across the top of the instrument, the VENTUS wordmark fused into its centre exactly as GridAtlas renders it, three
titles left and three right in GridAtlas's face, colour and spacing, every panel closed at rest and dropped from its
title, every label and command inside a panel row and nothing floating over the wafer, one row on a 360 px Android
phone. "Exactly as GridAtlas" is defined by the measured table above, not by resemblance.

**GridAtlas lesson (with keys).**
1.1 The bar is one strip at the top of the map, 36 px, `rgba(4,10,13,.95)` with a 1 px `rgba(80,220,240,.3)` rule and a
7 px blur, mono 11 px, titles uppercase `.05em` `#cfeef6` (`gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:167-181`;
measured (5,5) 1270×36 at 1280 px).
1.2 Three zones, not six siblings: two `flex:1 1 0` side groups and a brand slot between them, so the brand is centred
whatever the titles weigh, and every panel has a real left or right anchor (`:181-183`, `:486-500`, measured 511/247/511).
1.3 "The VENTUS logo is the best part": the wordmark is the v8 masthead's own node, moved once into the bar, never
cloned, never a second row, never a closed panel; 14 px/800/`.2em` white over 5.5 px/`.14em` `#888` "CABLES &
CONNECTIVITY®"; on a phone 11 px/`.14em` over 4.5 px with the clock and the 2050 counter hidden; it is identity, not a
link (`:184-205`, `:372-378`, `:1671-1679`; shell `atlas/releases/202608300453-atlas-v9/index.html:29-32`;
`ventusv8.css:7-8`; measured 90.0×20.5 at (599.7,12.3)).
1.4 Admission rule: install nothing until every hook is present and uniquely identified; a missing control leaves the
old interface reachable and publishes a failure strip rather than being skipped (`:1-22`, `:134-159`, `:1647`;
measured: the strip at (8,8) 1264×33 when the engine had 0 + 0 controls).
1.5 Commands move as the same DOM nodes into panel rows of 44 px, in the panel's own type (`11px/1.35` mono), and the
map keeps only the search box under the bar; result surfaces stay with the map (`:218-224`, `:143-159`; measured
`controls_moved:17`, only `.search-bar-wrapper` left over the map at (981.8,77)).
1.6 Phone rule at `max-width:700px`: bar 34 px, titles 9 px `.025em` padding `0 6px`, panels `position:fixed; top:34px;
left:4px; right:4px; max-height:calc(100dvh - 40px)` with `env(safe-area-inset-*)` on the bar (`:168`, `:372-382`).
1.7 The six names are the architect's vocabulary, File Edit View Scope Grid About, and the Grid menu proxies the
engine's own inputs so the engine's handlers stay the only implementation (`:16-21`, `:29`, `:4380` in the cartridge).

**Kuiper change.** A shell module replaces Edition 4's `#bar` and `#keys` strip; the wafer engine and its placement law
are untouched. The contract, each line testable:

C1 Bar: `nav#kuiper-menu-bar[aria-label="Kuiper menu"]`, `position:fixed; top:0; left:0; right:0` (the Kuiper has no
`.map-container`; the wafer canvas is the window, so fixed at the window's top is the same place GridAtlas's absolute
top inside the map is), `height:36px`, `z-index` above the card and the panels, background `rgba(4,10,13,.95)`,
`border-bottom:1px solid rgba(80,220,240,.3)`, `backdrop-filter:blur(7px)`, `font:11px/1 ui-monospace,SFMono-Regular,
Menlo,monospace`, `padding-left/right:env(safe-area-inset-left/right)`. At `max-width:700px` height 34 px. These are
GridAtlas's values verbatim; the Kuiper's own palette (`PALETTE.md`: cyan `#2ee6e6`, ground `#090c13`) stays for the
wafer and the card, the bar takes GridAtlas's chrome because the owner asked for the same UI, and the two grounds
differ by less than the blur.
C2 Zones: `.gm-side.gm-side-left` (`flex:1 1 0`), `.gm-brand-slot` (`flex:0 1 auto; max-width:64%`, 48 % on a phone),
`.gm-side.gm-side-right` (`flex:1 1 0; justify-content:flex-end`).
C3 The logo: the brand slot holds `div.hud-header > div.ventus-brand > div.ventus-main` "Ventus" + `div.ventus-sub`
"Cables &amp; Connectivity&reg;" with GridAtlas's classes and CSS copied verbatim (`.ventus-main` 14px 800 `.2em` #fff
uppercase; `.ventus-sub` 5.5px `.14em` #888 uppercase; phone 11px/4.5px; `line-height:1.05`; centred). No image file is
introduced, because GridAtlas has none. The clock and the 2050 counter are not copied: they are GridAtlas's HUD, not its
logo, and GridAtlas itself hides them on a phone. Not a link, as in GridAtlas. Acceptance compares the wordmark's
computed style and rendered box to GridAtlas's at the same viewport within 1 px.
C4 Titles: `button.gm-title[aria-haspopup=menu][aria-expanded][aria-controls]`, uppercase, `.05em`, `#cfeef6`,
`padding:0 11px`, `min-height` = bar height; hover/open `rgba(80,220,240,.16)` + `#fff`; focus `2px solid #6bebff` inset;
phone 9 px `.025em` `0 6px`. Left group index 0–2, right group 3–5. On a coarse pointer each title's hit box extends to
44 px by an invisible `::after` below the bar, so the visible strip stays GridAtlas's 34 px and NL-009's touch finding
(01-bar F2) is met; measured by `elementFromPoint(x, 40)` resolving to the title.
C5 The six names, mapped. The Kuiper keeps GridAtlas's six words where the meaning carries and changes one:

| GridAtlas | holds there (measured `panel_counts`) | Kuiper name | holds in the Kuiper (owner of the content) |
|---|---|---|---|
| FILE | the engine's modules fetched from the engine graph, export CSV, the study link (8 rows) | FILE | open a key, open an edition, open an app, copy a link, the hash deep-link grammar (step 6, team 3); the edition's README, NOTICE, keys.json, proof as rows |
| EDIT | the search box (1 row) | EDIT | the find box `/` (a key, a repository, a period), the LINES filter, clear the selection (`Backspace`) |
| VIEW | fullscreen, status, measure, the SLD sandbox (5 rows) | VIEW | readout on/off, whole wafer, random line `r`, new code `n`, next/previous verified line `e`/`E`, reduced motion |
| SCOPE | radius, radius area, polygon zone, clear (4 rows) | SCOPE | the focus: all repositories / gridatlas + data centres (today's `#lyFocus`), one repository, one period, one commit |
| GRID | the 63 layer switches with the SCADA brand head and legend (3 groups) | WAFER | the layer registry: verified lines, repositories, periods, editions, See Through stars, elements, spider graphs (steps 3–4, team 2). "Grid" is GridAtlas's subject; the Kuiper's subject is the wafer, so the word changes and the position and the proxy rule do not |
| ABOUT | the estate links, versions, attribution, disclaimer (8 rows) | ABOUT | the edition's name and stamp, the laws (`LAWS.md`), licences (`NOTICE.md`), the estate links (See Through, Learn the Kuiper, GridAtlas, the homepage), the attribution of the data |

The star slot: See Through is "the star player" (step 5, team 3). The shell reserves the first position of the left
group for it, before FILE, as `a.gm-title[href="../../see-through/"]` in the same face; whether it is a seventh title
or the first row of FILE is step 5's decision; the width budget at 360 px for a seventh title is given in the
acceptance test so the decision is measured, not argued. Edition 4's four names map as: EDITION → ABOUT (the text) and
the brand slot (the name), READOUT → VIEW, LINES → WAFER + SCOPE + EDIT (switch, focus, filter), COMMANDS → VIEW + EDIT.
C6 Labels and commands: every command is a 44 px row inside a panel (`button`, `a[role=button]`, or a layer row with a
20 px box), `11px/1.35` mono `#cfeef6`, hover `rgba(80,220,240,.14)`; group headings `.gm-layer-group` 10 px `#6fa2ae`
uppercase. At rest nothing is drawn over the wafer but the bar; the find box, when open, sits where GridAtlas's search
does: right-aligned, directly under the bar, `width:min(82vw,390px)`, 44 px tall; the card (step 2) is the one result
surface and stays with the wafer, bottom-left as Edition 4 placed it. GridAtlas's phone keeps two 44 px strips at the
bottom corners (Tools, LAYERS); the Kuiper copies the shape for exactly two: the star entry's phone form if step 5 wants a
bottom-left strip, and nothing else, because the wafer's bottom third is where the card lands. The engine's `safeBox()` starts under the bar
(Edition 4 `:726`) and the camera law of Edition 4 (`edFly`) is unchanged.
C7 Panels: `.gm-panel` at `top:100%` of its title, `min-width:240px; max-width:min(92vw,420px); max-height:min(72dvh,
620px)`, `rgba(4,10,13,.98)`, `1px solid rgba(80,220,240,.32)` no top; right group `left:auto; right:0`; phone
`position:fixed; top:34px; left:4px; right:4px; max-height:calc(100dvh - 40px)`; one open at a time; closed by the same
title, Escape, a tap on the wafer, the Android back gesture (a `history.pushState` entry per open panel, popped on
close); `role=group aria-labelledby`. Keyboard as GridAtlas: ArrowLeft/Right, Home/End, ArrowDown opens.
C8 Admission rule (the shell is a Kuiper cartridge in team 2's sense): the module installs nothing until the engine's
hooks exist and are unique — `#c`, `#o`, `#top`, `#hud`, `#foot`, `#keys` with its five `data-k` buttons, `#lines`
with `#lyAll #lyFocus #lyFind #lineslist`, `#card`, and the functions `safeBox`, `draw`, `edCard`, `edFly`, `edNext`,
`setPanel` — then moves the existing nodes into the panels as the same nodes (listeners kept) and collapses the old
containers only after the complete inventory is built. A missing hook leaves Edition 4's bar reachable and writes
`#kuiper-menu-bar-failure` (`role=alert`, GridAtlas's strip) naming what is missing. `window.__KUIPER_MODULES__.menuBar`
publishes `{schema:'kuiper.menu-bar.v1', installed, controls_moved, failure, panel_counts}` for the test.
C9 One row at 360 px: the shell is accepted only when every `.gm-title` and the brand share one `y` at 360, 393, 412
and 430 px portrait and in landscape, with the measured slack written in the README. The names are chosen to fit:
FILE EDIT VIEW · VENTUS · SCOPE WAFER ABOUT at 9 px with `0 6px` padding is 302.0 px of 360 (GridAtlas's six titles at
360 px measured 218.8 px and the brand slot 77.6 px, 296.4 px in a 350 px bar, slack 53.6 px; WAFER is five letters like
SCOPE, 40.2 px, so the Kuiper's six are 224.4 px, plus the slot 77.6 px, slack 58.0 px in a 360 px bar). A seventh title
SEE THROUGH in the same face needs 11 × 5.65 + 12 ≈ 74 px, 16 px more than the slack: as a title it does not fit at 360
without changing GridAtlas's face, which is why the star slot's form is step 5's measured decision. Titles never shrink below 9 px; a system font scale that overflows
wraps nothing: the bar gets `overflow-x:auto` as the last resort and the README says so.
C10 Written in the page: a comment block at the head of the shell module naming this contract, the GridAtlas keys
and the date measured, as GridAtlas's module does (`:1-22`).

**Module.** `editions/<stamp>/modules/<stamp>-kuiper-shell.js` (one file, stamp, sha256 in the edition's cartridge list
per step 3), schema `kuiper.menu-bar.v1`, loaded by `index.html` after the engine; its CSS installed by the module into
`<style id="kuiper-menu-bar-css">` so the bar's values live in one place with their keys. Touches: `index.html` (one
script tag, removal of the Edition 3 bar block `:693-726` once the module has installed), nothing in `cosmos/`,
`keys.json`, `tools/key.py`, or the placement law.

**Acceptance test on Android** (`/tmp/nl010/team-1/accept-step1.cjs`, to be committed with the edition as
`proof/accept-shell.cjs`): Playwright Chromium with the harness flags, `devices['Pixel 7']`, `Galaxy S24` (360×780),
Pixel 7 at 393 and 430 px, `Pixel 7 landscape`, 1280×800; serve the kuiper-belt root; 8 s settle. PASS when all hold:
A1 `#kuiper-menu-bar` rect `y=0`, `x=0`, width = viewport, height 34 (≤700 px) / 36; `installed:true`, `failure:null`.
A2 six `.gm-title` (plus the star entry if step 5 makes it a title), texts FILE EDIT VIEW SCOPE WAFER ABOUT, all with the
same rounded `y`, last right edge ≤ viewport − safe inset; `scrollWidth === clientWidth` (no horizontal scroll) at 360.
A3 the wordmark: `#kuiper-menu-bar .ventus-main` computed `font-size 11px` (≤700) / `14px`, `font-weight 800`, colour
`rgb(255,255,255)`, `text-transform uppercase`; `.ventus-sub` `4.5px`/`5.5px`, `rgb(136,136,136)`; `.ventus-brand`
centre within 1 px of the viewport centre and of the bar's vertical centre; `closest('a')` null; rendered box within
1 px of GridAtlas's measured box at the same viewport (73.6×16.3 on Pixel 7 and at 360 px, 90.0×20.5 at 1280×800 and in landscape).
A4 at rest the only elements with a non-empty client rect over the wafer and outside the bar are the two canvases
(`#c`, `#o`) and, after a pick, `#card`; `#keys`, `#top`, `#hud`, `#foot`, `#lines` have `display:none` or live inside a
hidden panel.
A5 every panel row `getBoundingClientRect().height ≥ 44`; `touchscreen.tap` on each title opens exactly one panel whose
`top ≥ bar bottom` and `right ≤ viewport`, a second tap closes it, Escape closes it, `page.goBack()` closes it and stays
on the page; tapping a VIEW row "next verified line" lands the selected spark between the bar's bottom and the card's
top (Edition 4's `edFly` law, NL-009 01 F7 numbers).
A6 `elementFromPoint(titleCentreX, 40)` is that title on a coarse pointer (the 44 px hit box).
A7 zero `pageerror`, zero console errors; `node --check` of the module.
A8 the admission rule: with `#keys` removed before load, `installed:false`, `#kuiper-menu-bar-failure` visible with text
naming `#keys`, Edition 4's `#bar` still clickable.
A9 the same script against GridAtlas at `http://127.0.0.1:8201/atlas/` (basemap stubbed as above) prints the same
table for `#gridatlas-menu-bar`, so the two shells are compared number to number in one run.

**Licence note.** GridAtlas is Apache-2.0 (`gridatlas@5ec7f62 LICENSE:1-2`, `NOTICE:1-12`, Copyright 2026 Ventus Ltd);
the CSS values and the menu module's structure copied into the Kuiper (Apache-2.0, `kuiper-belt@018b46a NOTICE.md`)
carry GridAtlas's NOTICE line in the shell module's header and in the edition's `NOTICE.md`. The words "Ventus" and
"Cables & Connectivity®" are the owner's mark, used here by the owner's instruction; the ® is kept as GridAtlas writes
it. No third-party asset is added (no logo file exists to add). MapLibre is not part of the shell.

**Opus team brief (team 1 of 10, four agents).** Build `<stamp>-kuiper-shell.js` to C1–C10; do not edit the engine
above the Edition 2 marker (`index.html:620`) or any file under `cosmos/`; your own files are the module, the script tag,
the `proof/accept-shell.cjs` test and its JSON output in `proof/`; copy every CSS value from the keys in this step and
cite the key beside it; run A1–A9 on the six viewports and paste the numbers into the edition README under "The shell,
measured"; FAIL loudly on any missing hook; do not decide the star slot (team 3) or the WAFER rows (team 2) — leave a
named, empty group for each with its owner's schema name; hand the measured widths at 360 px to teams 2 and 3 on the
issue before they add rows or titles. Done when A1–A9 PASS on all six viewports and the evidence officer reproduces
them from the committed script.

---

## Step 2 — The card law: the line of code is the header

**Goal.** Every card the Kuiper shows for a keyed line opens with the line of code itself, verbatim, as its header;
the key follows; every human name for the line comes after. The law is written in three places with one wording: the
page, the edition README, and `LAWS.md` as law L11.

**GridAtlas lesson (with keys).** GridAtlas's menu does not restate a layer's label from a cleaned attribute; it shows
the engine's own live text, WAIT/LOAD/OK/FAIL suffix included, because a stripped label made a success and a failure
indistinguishable on a phone (`gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:92-100`). The same discipline
for the Kuiper: the header of a card is the source's own text at the key, never the finder's title for it. And the
Kuiper's own first law: a statement with a key is a fact, without one a candidate (`kuiper-belt@018b46a README.md:29-40`);
a title is a candidate, the line at the key is the fact, so the fact leads.

**Kuiper change.**
K1 The card (`#card`, Edition 4 `index.html:655-666`) is rebuilt in this order and no other:
   row 1, the header: `<header class="ch"><code>` the text of the line at the key (`keys.json bodies[].line_text`, which
   is what `python tools/key.py <key>` returns), escaped, `white-space:pre-wrap`, the instrument's mono, `#fff`,
   `font-weight:600`, nothing before it, no count, no title;
   row 2, the key: `repo@commit7 path:line` and the wafer key number, `#cde`, as a link to the GitHub blob at the commit;
   row 3 onward, the names: the title from the register, "n of 344", the pattern, the finder, the position, behind the
   existing "details" toggle (a `button[aria-expanded]`, NL-009 09 F7);
   when the register's quote is not the line at the key (7 of 346, `keys.json summary.quote_not_at_line`), a row 2b
   shows the quote with its own `quote_key` and the words "quoted one line below"; the header is never the quote.
K2 The card's `aria-label` is the header text; `aria-live=polite` announces it on `e`.
K3 The law is written in the page, in the ABOUT panel, first paragraph, exact wording:
   "The line of code is the header. Every card opens with the line itself, verbatim from the key; the key is the second
   row; every name a person gave the line comes after."
   and as a comment at the head of the card module with the same sentence.
K4 The edition README gets a section `## The card law` whose first paragraph is the same sentence, followed by one
   rendered example (the header, the key, the names) and the falsification test.
K5 `LAWS.md` gets, after L10 (`kuiper-belt@018b46a LAWS.md:139`), in the file's own form:

   ```
   ## L11. The line of code is the header

   On every card the instrument shows for a keyed line, the first row is the line of code itself, byte for byte the
   text `tools/key.py <key>` returns for that key, in the instrument's monospace; the second row is the key,
   `repo@commit path:line`; every name a person gave the line (a title, a pattern, a finder, a count) comes after
   both. A card whose first row is a title, a count or a label is not a card of this instrument.

   **Falsified by:** a card whose first visible row differs from the text at its key; a card that shows a line
   without its key on the next row; or a quote shown as the header when the quote is not the line at the key.
   ```
   The sentence in K3 is the short form of L11; L11 is the law; the README quotes both.
K6 The LINES list rows (`fillLines`, `:737-744`) follow the same order: the line text first, then the key, then the title.

**Module.** `editions/<stamp>/modules/<stamp>-line-card.js`, schema `kuiper.card.v1`, wrapping `edCard` (and `fillLines`)
after the shell has installed; touches `index.html` (script tag), `README.md` (the section), `LAWS.md` (L11),
`NOTICE.md` (nothing new to license). `keys.json` stays byte-identical to Edition 2's; `line_text` is already in it.

**Acceptance test on Android** (`proof/accept-card.cjs`): Pixel 7 and 360×780, touch; after `touchscreen.tap` on
VIEW → next verified line, and for ten random `edPlaced[i]` opened by `edCard(i)`:
B1 `#card` first element child is `header.ch`, its `textContent` equals `edPlaced[i].line_text` exactly (and, for the
7 `quote_not_at_line` bodies, differs from `quote` while a `.cq` row shows the quote with `quote_key`);
B2 the second row's text contains `repo`, the 7-character commit, `path:line` and the key number, and its link's `href`
equals `destination`;
B3 the title appears only after the second row; `card.getBoundingClientRect().top` ≥ the selected spark's `y` + 14 and
the card's height ≤ 34 % of the viewport (Edition 4's cap);
B4 the ABOUT panel's first paragraph equals the K3 sentence; `README.md` contains it; `LAWS.md` contains the L11 heading
and the "Falsified by" line (checked by `grep -F` in the test, the three strings compared byte for byte);
B5 `python3 tools/key.py <key>` for the same ten keys returns the header text (the test shells out, as
`proof/keys-summary.json` did for 12 round trips);
B6 the LINES rows: first text node equals `line_text`;
B7 zero page errors; `tools/ci_check.py` prints `RESULT: PASS`.

**Licence note.** The quoted lines keep their repositories' licences as Edition 4's `NOTICE.md` states (Apache-2.0,
CERN-OHL-S v2, CC BY 4.0, ODbL 1.0, OGL v3; `kuiper-belt@018b46a editions/202611012027/NOTICE.md:7-11`); showing the line
as the header is the same citation with its key, not a relicensing; nothing new is brought in.

**Opus team brief (team 2 of 10, four agents).** Build `<stamp>-line-card.js` to K1–K6 after team 1's shell has
installed (depend on `window.__KUIPER_MODULES__.menuBar.installed`); write the L11 text into `LAWS.md` and the K3
sentence into the README and the ABOUT panel byte for byte as given here, no paraphrase; do not change `keys.json`, the
register, or any line's key; run B1–B7 and commit the JSON under `proof/`; if a body has no `line_text`, the card
refuses with the words "no text at key" rather than falling back to the title (a check that examines nothing refuses).
Done when B1–B7 PASS on both devices and the evidence officer confirms the three wordings are identical.

---

## NL-009 findings folded in (not repeated)

- 01-bar F1–F3, F5 → C1, C4, C9 (one row, 44 px hit box, safe-area insets); F4 → hover only under `(hover:hover)` in C4;
  F6 → `dvh` in C7; F7 → C6 keeps `safeBox`/`placePanels` following the measured bar.
- 06-seethrough F1, F5, F6 → the star slot in C5 with `../../see-through/` (the pointer, same tab); F2 → C9's budget.
- 09-robust F1 → C7 (panels placed from the measured bar on every open, not only on resize); F2 → C8's failure strip
  reuses the `#refuse` pattern; F5 → Escape order in C7 then the card; F7 → ARIA in C4, C7, K2.
Anything NL-009 round 1 adds after this is read by team 5B at consolidation.
