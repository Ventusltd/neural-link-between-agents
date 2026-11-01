# FABLE-06 · seethrough · See Through as a button in the edition, and the family of Kuiper apps

Audited: `kuiper-belt/editions/202611012027/index.html` at kuiper-belt main 018b46aed50f28f7b1882a0dcaba6593ce522beb,
served from the repository root on port 8106, Playwright Chromium (SwiftShader) with `devices['Pixel 7']` (412×839,
DPR 2.625, touch), `devices['Galaxy S24']` (360×780) and `devices['Pixel 7 landscape']` (863×360). Scripts in
`/tmp/nl009/06/` (`before.cjs`, `seethrough.cjs`, `after.cjs`); raw measurements in `before.json`, `seethrough.json`,
`after.json`, `after2.json` there.

## FINDINGS

1. **BLOCKER (owner's request): See Through is unreachable from Edition 4.** `grep -ci "see.through"` on
   `editions/202611012027/index.html` → 0, on `editions/202611012027/README.md` → 0; `NOTICE.md` names it once, as a
   licence only. The bar carries four titles (EDITION, READOUT, LINES, COMMANDS, measured `#bar .gm-title` count 4),
   the EDITION panel is the engine subtitle plus the Edition 1 sentence, the COMMANDS panel links only `Ventusltd/law`.
   The repository `README.md` names See Through nowhere either (only the diary line 200 names Learn the Kuiper). By
   contrast the globalgrid2050 homepage (`homepage_v134.html`, entity `see-through`, "application") carries "Open See
   Through →" to `kuiper-belt/see-through/202610050609/`, in the same tab (the homepage has 0 `target="_blank"`).
   After the patch: a fifth bar entry `a.gm-title[href="../../see-through/"]` (Pixel 7: 101×29 px, same font 11 px,
   same padding 5px 8px, same border as the four buttons; landscape 112×33 px), a touch tap on its centre navigates to
   `http://127.0.0.1:8106/see-through/202610050609/` (title "See Through") through the stable pointer; `goBack()`
   returns to `editions/202611012027/` with 5 bar entries, no panel open, "Kuiper Edition 4 · 344 verified lines lit",
   0 console errors. Measured on all three devices. **PASS.**

2. **MAJOR (FABLE-01's dimension, measured here because the fifth entry changes the budget): the bar is two rows on a
   phone, before and after.** Pixel 7: `#bar` height 75 px, items `KUIPER EDITION 4` 131 + EDITION 71 + READOUT 71 +
   LINES 56 + COMMANDS 78 (+ gaps 16 + padding 16) = 439 px against 412 px (Galaxy S24: 360 px); with SEE THROUGH
   (101 px) 544 px. Dropping the name alone leaves five titles at 377 px + 16 gaps + 16 padding = 409 px, still over
   396 px (Pixel 7) and 344 px (S24). To make one row at 360 px the five titles must total ≤ 328 px, i.e. about 50 px
   less than now: for example padding 5px 6px (−20 px), letter-spacing .04em (−17 px over 38 characters), bar padding
   6 px (−4 px), and a nowrap bar with `overflow-x:auto` as the fallback; the link is `flex:0 0 auto` so it stays
   reachable by a horizontal scroll if FABLE-01 chooses that. **FAIL (unchanged by this patch; not its scope).**

3. **MINOR: in landscape (863×360) the family paragraph needs a scroll inside the EDITION panel.** The panel is capped
   at 60vh = 216 px; its scrollHeight is 295 px, so `#edapps` (y 203, bottom 334) is reached by scrolling the panel,
   which already scrolls (`overflow:auto`). Portrait Pixel 7: panel 359 px high, scrollHeight 357, `#edapps` bottom
   425 < panel bottom 436, fully visible without scrolling (screenshot `img/06-after-edition-panel-pixel7.png`);
   Galaxy S24 likewise (panel 447, `#edapps` bottom 513 < 524). Accepted as is.

4. **See Through itself on Pixel 7 (recorded, not fixed).** `http://127.0.0.1:8106/see-through/` → pointer →
   `202610050609/`, HTTP 200, `load` + 8 s in 8.4 s under SwiftShader. The first screen fits the phone: `scrollWidth`
   412 = viewport, `scrollHeight` 839 = viewport, no visible element beyond the right or bottom edge, 13 controls
   (name input 332×44 at y 56, GO 56×44, ♪ and X 44×44 at y 8, KUIPER MAP SAT 3D at y 713 and GRID SUBS SPIDER ▲ ▼
   at y 761, all 44 px tall), two canvases at 824×1678 device pixels. `window.__errors` empty, 0 page errors, 0
   console errors from the app; one failed request `basemaps.cartocdn.com/.../style.json`
   `net::ERR_TUNNEL_CONNECTION_FAILED` (the sandbox proxy blocks it; the app's own README says the map needs the
   internet, so this is the environment, not a defect; it will also fail the Esri and AWS tiles here). Frame time over
   60 frames: mean 72.7 ms, max 3,383 ms (one first-frame hitch under software GL; not representative of a phone GPU).
   Observed, not a finding: the app offers no way back to the edition or the family except the browser back gesture,
   which the same-tab link in finding 1 relies on. Screenshot `img/06-see-through-pixel7.png`.

5. **Decisions.** (a) Same tab, not a new tab: the homepage opens every app of the family in the same tab; on Android
   Chrome a `target="_blank"` tab is invisible (no tab strip) so the user cannot tell the difference except that the
   edition stays alive in the background, and two WebGL pages (the wafer; MapLibre plus the 3D) on one phone are the
   case where Chrome discards the background tab anyway; the back gesture is the documented route home and measured
   to work (finding 1). The GitHub link in the card keeps `_blank` because it leaves the host. (b) No APPS or KUIPER
   entry: it would add 70–80 px to a bar already 132 px over at 412 px (finding 2) for a second link to a thing the
   EDITION panel now names with its licence and stable link; the family (See Through, Learn the Kuiper) lives in the
   EDITION panel instead, two sentences with links and licences. (c) The link is `../../see-through/` (the pointer),
   not the dated folder: the pointer always opens the newest See Through, as the homepage's dated link does not.

6. **Link resolution (measured with `new URL(href, base)` in the page and by fetch).** From
   `http://127.0.0.1:8106/editions/202611012027/`: `../../see-through/` → `http://127.0.0.1:8106/see-through/` (200),
   `../../learn-the-kuiper/` → 200. Against the Pages base `https://ventusltd.github.io/kuiper-belt/editions/202611012027/`
   → `https://ventusltd.github.io/kuiper-belt/see-through/` and `.../learn-the-kuiper/`; against any future stamp
   `editions/<stamp>/index.html` the same. The pointer `editions/index.html` uses `location.replace('<stamp>/')`, so
   the document base is always the dated folder with a trailing slash, and both servers (http.server, GitHub Pages)
   redirect a slash-less folder URL before the page loads. The Pages URL itself cannot be fetched from this sandbox
   (proxy), so the live check is by construction, not by request.

Not in scope but seen: the four buttons and the link are 29 px tall on a phone, under the 44–48 px touch target
(FABLE hit-target dimension).

## PATCH

Unified diff against `editions/202611012027/index.html`; from the kuiper-belt root `patch -p0 < 06-seethrough.patch`
(dry run checked clean against main 018b46a; the applied copy is byte-identical to the tested page). `node --check`
on the extracted module script: PASS. 44 lines, +22. Also at `/tmp/nl009/06/06-seethrough.patch`.

```diff
--- editions/202611012027/index.html
+++ editions/202611012027/index.html
@@ -61,6 +61,8 @@
   #bar .gm-title{appearance:none;border:1px solid #12414a;background:transparent;color:#8fb3bd;font:inherit;
     text-transform:uppercase;letter-spacing:.08em;padding:6px 10px;cursor:pointer;touch-action:manipulation}
   #bar .gm-title:hover,#bar .gm-title.gm-on{background:rgba(80,220,240,.16);color:#fff;border-color:var(--cy)}
+  #bar a.gm-title{text-decoration:none;display:inline-block;flex:0 0 auto}   /* EDITION 5: SEE THROUGH is a link, same look as the titles */
+  #edapps{margin-top:6px;color:var(--dim)} #edapps a{color:#66ccff}
   #top,#hud,#foot,#lines{display:none}
   #top.gm-open,#hud.gm-open,#foot.gm-open,#lines.gm-open{display:block}
   #top,#hud,#foot,#lines{position:fixed;top:40px;left:0;right:auto;bottom:auto;max-width:min(680px,96vw);max-height:60vh;overflow:auto;
@@ -700,7 +702,11 @@
   + '<button class="gm-title" data-panel="top">edition</button>'
   + '<button class="gm-title" data-panel="hud">readout</button>'
   + '<button class="gm-title" data-panel="lines">lines</button>'
-  + '<button class="gm-title" data-panel="foot">commands</button>';
+  + '<button class="gm-title" data-panel="foot">commands</button>'
+  + '<a class="gm-title" href="../../see-through/" title="See Through: from the stars to one substation in 3D">see through</a>';
+// EDITION 5: SEE THROUGH (../../see-through/, this repository, CERN-OHL-S v2) opens in the same tab: the homepage
+// launches every app of the family that way, the Android back gesture is the way home, and two WebGL pages
+// (the wafer and MapLibre with the 3D) in two tabs of one phone would only see the first one discarded.
 document.body.appendChild(bar);
 const linesPanel = document.createElement('div'); linesPanel.id = 'lines'; linesPanel.className = 'gm-panel';
 linesPanel.innerHTML = '<div id="linesctl"><label><input type="checkbox" id="lyAll" checked> verified lines layer</label>'
@@ -718,10 +724,18 @@
   if (openPanel === 'lines') fillLines();
   dirty = true;
 }
-bar.addEventListener('click', e => { const b = e.target.closest('.gm-title'); if (b) { e.stopPropagation(); setPanel(b.dataset.panel); } });
+bar.addEventListener('click', e => { const b = e.target.closest('.gm-title'); if (b && b.dataset.panel) { e.stopPropagation(); setPanel(b.dataset.panel); } });
 addEventListener('keydown', e => { if (e.key === 'Escape' && openPanel) setPanel(openPanel); });
 cv.addEventListener('pointerdown', () => { if (openPanel) setPanel(openPanel); });
 elTop.classList.add('open');                                   // the long subtitle is readable once the panel is open
+// EDITION 5: the two apps of the family live in this repository and open on this host from their stable pointers
+{ const apps = document.createElement('div'); apps.id = 'edapps';
+  apps.innerHTML = 'The family: <a href="../../see-through/">See Through</a>, from the stars to one substation in 3D (any of 5,800 UK '
+    + 'substations rising on the real satellite ground with its pylons, drawn by rule from open map data; CERN-OHL-S v2; the SEE THROUGH '
+    + 'button above), and <a href="../../learn-the-kuiper/">Learn the Kuiper</a>, a small game about the one rule that places every dot '
+    + 'here, one dot and two numbers (code Apache-2.0, text CC BY 4.0). Both gather their stars by the placement law of this wafer, '
+    + 'r = \u221akey, \u03b8 = key \u00d7 golden angle, and both stay on this host: see-through/ and learn-the-kuiper/ always open the newest dated folder.';
+  elTop.appendChild(apps); }
 // the safe rectangle now starts under the bar, and the hidden panels take no room
 { const _safe = safeBox; safeBox = function(){ const s = _safe(); s.y0 = Math.max(s.y0, bar.getBoundingClientRect().bottom + 8); s.y1 = Math.max(s.y0 + 24, innerHeight - 8); return s; }; }
 // the lines layer: on/off and focus-only, the list, the filter
```

## README.md addition (separate block; the integrator pastes it into Edition 5's `README.md` after "Using it")

```markdown
## The apps

The kuiper-belt repository carries two apps built on the same placement law as this wafer. Both are reachable from
this edition on the same host; the bar's SEE THROUGH entry opens the first, the EDITION panel links both.

- **See Through** (`../../see-through/`, stable link https://ventusltd.github.io/kuiper-belt/see-through/, which
  always opens the newest dated folder, today `202610050609/`): "from the stars to one substation in 3D". Type the
  name of any of 5,800 UK substations and press GO; the stars gather into the grid, the real map and satellite view
  appear inside the circle, and the substation rises in 3D on the real terrain with its pylons, drawn by rule from
  open map data (MapLibre GL JS; substations, lines and outlines © OpenStreetMap contributors, ODbL; imagery Esri;
  terrain AWS Terrain Tiles; it needs the internet). Licence: CERN Open Hardware Licence v2, Strongly Reciprocal
  (CERN-OHL-S v2), the licence of the globalgrid2050 code it reuses; `LICENSE.md` and `NOTICE.md` in each dated
  folder. How it relates to the wafer: its stars gather by the same law that places every spark here, r = √key,
  θ = key × golden angle (`kuiper-law.js` in See Through; Vogel 1979, Knuth's golden-ratio multiplier), so the field
  of stars a substation falls out of is this wafer's rule applied to the grid. The link opens in the same tab, as the
  globalgrid2050 homepage opens it; the back gesture returns to the edition.
- **Learn the Kuiper** (`../../learn-the-kuiper/`, stable link https://ventusltd.github.io/kuiper-belt/learn-the-kuiper/):
  a small game about the one rule, one dot and two numbers, until you can place any dot yourself; its MORE menu holds
  the first SEE THROUGH module, from which the app above grew. Code Apache-2.0 as the repository, text and generated
  data CC BY 4.0; parts adapted from globalgrid2050 keep CERN-OHL-S v2.

The wafer itself without the edition layer is `../../index.html`. Nothing in this edition's `keys.json`, cosmos or
placement law changes for the apps; they are links.
```

## TEST (what a reviewer runs)

1. `cd /home/user/estate/kuiper-belt && python3 -m http.server 8106 --bind 127.0.0.1 &` (after the integrator has
   applied the patch to the Edition 5 folder; substitute the stamp below).
2. Playwright: `chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']})`,
   `browser.newContext({...devices['Pixel 7']})`, `page.goto('http://127.0.0.1:8106/editions/<stamp>/')`, wait 7 s.
3. Assert `document.querySelectorAll('#bar .gm-title').length === 5`, the fifth is an `A` with
   `getAttribute('href') === '../../see-through/'` and `getAttribute('target') === null`; its `getBoundingClientRect()`
   height equals the EDITION button's (29 px on Pixel 7 with Edition 4's phone padding); `new URL(href, location.href)`
   ends in `/see-through/` and `fetch(...)` of it returns 200.
4. `page.touchscreen.tap(cx, cy)` on the EDITION button; assert `#top.gm-open` and that `#edapps` holds two anchors,
   `../../see-through/` and `../../learn-the-kuiper/`, and its text contains `CERN-OHL-S v2` and `Apache-2.0`.
5. `page.touchscreen.tap` on the centre of SEE THROUGH with `page.waitForNavigation()` armed; assert `page.url()` ends
   in `/see-through/202610050609/` (or the newest See Through stamp) and `page.title() === 'See Through'`.
6. `page.goBack({waitUntil:'load'})`, wait 6 s; assert the URL is the edition folder, 5 bar entries, no `.gm-open`,
   and zero console errors on the edition page (ignore `ERR_TUNNEL_CONNECTION_FAILED` from See Through's CARTO style
   in this sandbox).
7. Repeat 2–6 with `devices['Galaxy S24']` and `devices['Pixel 7 landscape']`; in landscape also scroll `#top` to the
   bottom and assert `#edapps` is within the panel's box.
8. Static: `node --check` on the script extracted from `index.html`; `python3 tools/ci_check.py` → `RESULT: PASS`.
Script that does 2–7: `/tmp/nl009/06/after.cjs` (argument: device name), results in `/tmp/nl009/06/after.json`.

## LIMITS

- The one-row bar is FABLE-01's; this patch adds the fifth entry in the same class and measures the cost (finding 2)
  but does not reflow the bar. If FABLE-01 renames or shortens titles, "SEE THROUGH" should keep its name (it is the
  app's name on the homepage and in its README); at 11 px with .08em spacing and 5px 8px padding it is 101 px.
- The Pages URL could not be fetched from the sandbox (proxy block); resolution is proven by `new URL` against the
  Pages base and by the same relative path served from the repository root.
- See Through was tested only to its first screen (load, fit, errors, frame time) under SwiftShader without internet;
  the fall to a substation, the satellite ground and the 3D were not exercised. Nothing in See Through was changed.
- The patch names "Kuiper Edition 4" nowhere new; the integrator's rename to Edition 5 is unaffected. The comment block
  in the bar's code says "EDITION 5", as the integrator's folder will.
- The EDITION panel paragraph is plain text and anchors appended to `#top` after the engine's `#sub`; the engine never
  rewrites `#top`'s children (`sub.textContent` only), so it survives the engine's own subtitle updates.
- Not touched: `keys.json`, `cosmos/`, the placement law, the card, the LINES panel, keys.
