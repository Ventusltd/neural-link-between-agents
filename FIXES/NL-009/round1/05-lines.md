# NL-009 round 1 — FABLE-05 — dimension "lines": the LINES layer panel on Android phones

Page audited: `editions/202611012027/index.html` (Edition 4) at kuiper-belt HEAD 018b46aed50f28f7b1882a0dcaba6593ce522beb.
Method: Playwright Chromium (SwiftShader flags from the brief), `devices['Pixel 7']` (412x839 CSS px, dpr 2.625) and
`devices['Galaxy S24']` (360x780, dpr 3), `Pixel 7 landscape` (863x360) and a 1280x800 desktop page for regression,
real touch only (`page.touchscreen.tap`, CDP `Input.dispatchTouchEvent` drags), served on port 8105. Every number
below is a `getBoundingClientRect`, a computed style, a `scrollHeight`/`clientHeight`, a `performance.now()`
difference, a `requestAnimationFrame` interval or a pixel count on the overlay canvas; scripts in `/tmp/nl009/05/`
(`measure.cjs`, `bench.cjs`, `desk.cjs`), raw JSON in `/tmp/nl009/05/out/`. Zero console errors and zero page errors
before and after, on every device.

## FINDINGS

Values are Pixel 7 / Galaxy S24 unless one number is given.

1. **MAJOR — the panel scrolls as one block, not the list inside it.** `#lines` is the scroll container
   (`scrollHeight` 22,812 px vs `clientHeight` 518 px / 24,432 vs 482); `#lineslist` has no scroll of its own
   (`listScrolls false`). The first swipe therefore carries the two toggles, NEXT/PREVIOUS and the filter input off
   the top of the panel; a 300 px touch drag moved `#lines.scrollTop` to 321 / 325 and the controls were gone. The page
   itself never moved (`scrollY` 0, `visualViewport.offsetTop` 0, `body overflow hidden`), which is correct. After the
   patch `#lines` is a flex column with `overflow:hidden`, `#lineslist` is the only scroller (22,422 px inside a 385 px
   list / 23,529 inside 342), the controls stay in place while scrolling and typing (`ctlVisibleWhileTyping true`),
   and all four panels get `overscroll-behavior:contain` so a list at its end cannot chain into the page.

2. **MAJOR — tap targets under 44 px.** Toggle labels 21 px tall with 13x13 px checkboxes, default accent, 11 px text;
   NEXT and PREVIOUS 29 px tall; the filter input 29 px tall. After: labels 44 px tall (flex, `min-height:44px`) with
   20x20 px checkboxes in the energised green (`accent-color rgb(34,238,119)`), the checked label's text turns ink
   (`label:has(input:checked)`), buttons 44 px tall and at least 44 px wide, input 44 px tall. A real tap on each label
   toggles its checkbox (`lyAll` checked -> false -> true; `lyFocus` false -> true -> false).

3. **MINOR — the filter input is 11 px** (`type=text`, no `inputmode`, `enterkeyhint` or `autocapitalize`). Chromium's
   zoom-to-legible-scale is disabled for a page whose viewport is `width=device-width`
   (`VisualViewport::ShouldDisableDesktopWorkarounds`), and `visualViewport.scale` stayed 1 after a real tap into the
   field, so Android does not zoom this page on focus; 11 px is still below a readable size for typing, and iOS Safari
   (which the engine's own comments name as a reader) would zoom. After: 16 px, `inputmode=search`,
   `enterkeyhint=search`, `autocapitalize=off autocorrect=off spellcheck=false`, and Enter blurs the field so the
   keyboard goes away and the list is what remains. Typing still never reaches the engine's key commands
   (`stopPropagation` kept).

4. **MAJOR — a filter cannot be cleared.** No clear control; Escape in the field was swallowed and did nothing; the only
   way out was select-all + backspace on the soft keyboard. After: a 44x44 px clear button (`#lyClear`) appears when the
   field has text and vanishes when it is empty; one real tap gives value `""`, `lyQuery ''` and 344 rows again; Escape
   clears the field, a second Escape blurs it.

5. **MINOR — the soft keyboard.** The panel height came from `62vh`, i.e. the layout viewport. Chrome on Android (108+)
   by default shrinks only the visual viewport when the keyboard opens, so with a 320 px keyboard on the Pixel 7 the
   panel's bottom (597 px) sits about 78 px behind the keyboard (top about 519 px) and the end of the list cannot be
   reached while typing. After: `placePanels` sets `--panelmax` from `min(innerHeight, visualViewport.height)` minus the
   bar (72 % of that on a phone, 62 % on a desktop, all of it when the visual viewport is more than 100 px shorter than
   the layout viewport, i.e. the keyboard is up) and listens to `visualViewport resize`. Emulated by shrinking the
   viewport to 519 / 460 px (the `resizes-content` path): panel 312 / 270 px, fits, list scrolls inside, input at y
   136-180, 3 / 2 rows visible under the controls (before: 5 / 4, with 95 px of controls that scrolled away).

6. **MINOR — the count of rows is shown nowhere.** 344, 174 or 126 rows look the same. After: a count line under the
   controls: `344 lines in 21 repositories · 174 gridatlas + data centres`; filtered `126 of 344 lines match
   "gridatlas"`; focus `174 of 344 lines · gridatlas + data centres only`; layer off `layer off · 344 lines hidden`.

7. **MINOR — no grouping; rows are tall.** 344 rows in key order (data-centres-gb, globalgrid2050, pipelinenews,
   gridatlas, data-grid-gb ... interleaved), each repeating its repository name in bold, rows 45-96 / 45-113 px tall
   (median 62; 103 / 168 rows over 64 px because repository plus path wrap), none under 44. After: grouped by
   repository, largest first (gridatlas 121, kuiper-belt 61, data-grid-gb 35, globalgrid2050 34, pipelinenews 22,
   data-centres-gb 18, particle-physics-drawing-engine 8, ventus-grid-engine 8, gridmachine1 6, time-stone 5, maths 4,
   ... 21 groups), a sticky 40 px header per repository with its count (green for the focus repositories), tap a header
   to fold or unfold it (folding is ignored while a filter is typed, so search results are never hidden), rows sorted by
   path then line, 12 px text, path:line in bold and the title clamped to two lines: 45-94 px, median 62, none under 44.
   Opening LINES now scrolls the selected row into view (and unfolds its group), so after `e` or NEXT the list shows
   where you are. `e`/`E` keep stepping in key order; the card's "n of 344" is unchanged.

8. **PASS — the focus filter.** The toggle yields exactly 174 rows, headers gridatlas (121), data-grid-gb (35),
   data-centres-gb (18), and the sparks follow (unchanged code). Typing `gridatlas` yields 126 rows (121 gridatlas, 2
   data-gridatlas, 3 whose path or title contains the word): the free-text filter is a search, the toggle is the exact
   set; the count line says which is in force.

9. **PASS — picking a row (Edition 4 behaviour).** Before and after, on both phones: right after `touchscreen.tap` on a
   gridatlas row the panel is closed (`gm-open` false) and the card is `display:block` ("4 of 344" before, "338 of 344"
   after, the grouped order picks a different first gridatlas row); 8 s later the magenta ring of the selected spark
   (142-147 sampled overlay pixels) has its centroid at y = 369 / 340 before and 386 / 348 after, between the bar's
   bottom (75 px) and the card's top (671 / 612 before, 705 / 629 after): the spark lands in the clear space. One fix
   is included: the edition's window `pointerup` listener (the 9 px spark hit-test) ran for taps on a panel row, the bar
   and the card too (it only checks `moved` and `pts`), so a row tap first opened whichever spark lay within 9 px under
   the panel and then the row's line; it now returns unless `e.target` is the wafer canvas.

10. **MINOR — the panel is not full width on a phone.** `width:min(720px,96vw)` beat `left:0;right:0`: 395.5 px wide
    on a 412 px screen / 345.6 on 360, left-aligned with the gap on the right only. After: `width:auto` on phones, 412 /
    360 px; desktop unchanged at 720 px.

11. **PASS — performance with 344 rows.** On a quiet machine, opening the panel from the bar button (`setPanel` ->
    `fillLines` -> `innerHTML`) took 1.4 ms in the handler and 24 ms including a forced layout before the patch, 5.3 ms
    and 17 ms after it (first after-run); the final patch could only be timed on a box at load average 47-83 (ten
    auditors under SwiftShader, 72 Chromium processes), where paired runs gave 2.5-9.9 / 55-88 ms for the patched page
    against 2.4-11.2 / 25-167 ms for the original in the same process, and the original alone produced 433-1,483 ms
    frames during a touch drag. The variance between two rounds of the same page exceeds every difference between the
    CSS variants tried (`bench.cjs`: with and without `overflow-wrap:anywhere`, the two-line clamp, sticky headers), so
    no scroll-jank delta is claimed either way. 365 DOM nodes need no virtualisation; `content-visibility:auto` was tried
    and dropped (no measurable gain, and it repaints rows as they enter view).

12. **PASS (brief) — EDITION, READOUT, COMMANDS height and scroll rules.** Heights 182 / 237, 261 / 278 and 111 / 111
    px (Pixel 7 / S24) against a cap of 520 / 484 px before and 543 / 500 after: each fits the viewport, needs no inner
    scroll, leaves 466-650 px of wafer below, and the page never scrolls. Landscape 863x360: cap 216 px, READOUT's 225
    px of text scrolls inside it, LINES 216 px with the list inside. The patch changes only their cap (`--panelmax`,
    computed from the real viewport instead of `vh`) and adds overscroll containment. The two-row 75 px bar on both
    phones belongs to dimension 01; the panels start under it at 77 px through `placePanels`, which is kept.

## PATCH

One unified diff against `editions/202611012027/index.html`, made with `diff -u` from a copy in `/tmp/nl009/05/`.
From the kuiper-belt root it applies with `patch -p0 < 05-lines.diff` and with `git apply -p0 --check` (both verified on
a fresh copy of the file; the result is byte-identical to the tested page, sha256
636c8b1397b627c1165c95725ea9fc1fb14104d3ecfa45d90207428b0b3dc23b). `node --check` passes on the extracted module script;
the page loads with zero console errors on Pixel 7, Galaxy S24, Pixel 7 landscape and 1280x800. Scope: the Edition 3
panel CSS block, `linesPanel.innerHTML`, `placePanels`, one line in `setPanel`, one guard in the edition `pointerup`
listener, the `ly*` handlers, `fillLines`, and `placePanels();` before `requestAnimationFrame(frame)`. Nothing in
`keys.json`, `cosmos/`, the placement law, the card or the camera.

```diff
--- editions/202611012027/index.html
+++ editions/202611012027/index.html
@@ -63,16 +63,32 @@
   #bar .gm-title:hover,#bar .gm-title.gm-on{background:rgba(80,220,240,.16);color:#fff;border-color:var(--cy)}
   #top,#hud,#foot,#lines{display:none}
   #top.gm-open,#hud.gm-open,#foot.gm-open,#lines.gm-open{display:block}
-  #top,#hud,#foot,#lines{position:fixed;top:40px;left:0;right:auto;bottom:auto;max-width:min(680px,96vw);max-height:60vh;overflow:auto;
+  #top,#hud,#foot,#lines{position:fixed;top:40px;left:0;right:auto;bottom:auto;max-width:min(680px,96vw);max-height:var(--panelmax,60vh);overflow:auto;overscroll-behavior:contain;
     z-index:11;background:#090c13f2;border:1px solid #1d6470;border-radius:0 0 6px 6px;padding:10px 12px;pointer-events:auto;text-align:left}
   #hud{right:0;left:auto;max-width:min(560px,96vw)} #foot{border-top:1px solid #1d6470}
   #top #sub{max-height:none;overflow:visible;margin-top:4px}
   #lines{left:0;right:0;max-width:none;width:min(720px,96vw)}
-  #linesctl{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
-  #linesctl label{color:#8fb3bd} #linesctl input[type=text],#linesctl #lyFind{flex:1 1 180px;background:var(--bg);color:var(--ink);border:1px solid #12414a;padding:5px 8px;font:inherit}
-  #linesctl button{background:#0b1a20;color:#8fb3bd;border:1px solid #12414a;padding:5px 9px;font:inherit;text-transform:uppercase;cursor:pointer}
-  #lineslist .ln{padding:5px 6px;border-top:1px solid #121a26;cursor:pointer;color:var(--dim)} #lineslist .ln b{color:var(--ink);font-weight:600}
-  #lineslist .ln.focus b{color:var(--gn)} #lineslist .ln.sel{background:rgba(255,43,214,.12)} #lineslist .ln:hover{background:rgba(80,220,240,.10)}
+  /* EDITION 5 (NL-009 FABLE-05): the panel is a column; the controls stay put and only the list scrolls, inside
+     itself, never the page. Every tap target is 44 px; the filter is 16 px so Android Chrome does not zoom on focus;
+     the list is grouped by repository (sticky headers, tap to fold) and says how many rows it shows. */
+  #lines.gm-open{display:flex;flex-direction:column;overflow:hidden}
+  #linesctl{flex:none;display:flex;flex-direction:column;gap:4px;margin-bottom:4px}
+  #linesctl .lyrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
+  #linesctl label{display:flex;align-items:center;gap:6px;min-height:44px;padding:0 4px 0 2px;white-space:nowrap;color:#8fb3bd;cursor:pointer;-webkit-tap-highlight-color:transparent;user-select:none}
+  #linesctl label:has(input:checked){color:var(--ink)}
+  #linesctl input[type=checkbox]{width:20px;height:20px;margin:0;accent-color:var(--gn);flex:none}
+  #linesctl #lyFind{flex:1 1 120px;min-width:0;min-height:44px;background:var(--bg);color:var(--ink);border:1px solid #12414a;padding:8px 10px;font:inherit;font-size:16px;border-radius:0;appearance:none}
+  #linesctl #lyFind:focus{outline:none;border-color:var(--cy)}
+  #linesctl button{min-height:44px;min-width:44px;background:#0b1a20;color:#8fb3bd;border:1px solid #12414a;padding:0 10px;font:inherit;text-transform:uppercase;cursor:pointer;touch-action:manipulation}
+  #linesctl button:active{border-color:var(--cy);color:var(--cy)}
+  #lyClear{display:none;font-size:20px;line-height:1;padding:0} #lyClear.on{display:inline-block}
+  #lycount{color:var(--dim);padding:2px 2px 0;line-height:1.4}
+  #lineslist{flex:1 1 auto;min-height:0;overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch}
+  #lineslist .lg{position:sticky;top:0;z-index:1;display:flex;align-items:center;gap:8px;min-height:40px;padding:4px 8px;background:#0b1a20;color:var(--cy);border-top:1px solid #12414a;cursor:pointer;text-transform:uppercase;letter-spacing:.06em;touch-action:manipulation;user-select:none}
+  #lineslist .lg .n{color:var(--dim);letter-spacing:0;text-transform:none} #lineslist .lg.focus{color:var(--gn)} #lineslist .lg .ch{width:12px;color:var(--dim)}
+  #lineslist .ln{min-height:44px;padding:6px 8px;border-top:1px solid #121a26;cursor:pointer;color:var(--dim);line-height:1.35;overflow-wrap:anywhere;touch-action:manipulation} #lineslist .ln b{color:var(--ink);font-weight:600}
+  #lineslist .ln .t{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
+  #lineslist .ln.focus b{color:var(--gn)} #lineslist .ln.sel{background:rgba(255,43,214,.12);box-shadow:inset 3px 0 var(--mg)} #lineslist .ln:hover{background:rgba(80,220,240,.10)}
   #card{bottom:12px!important;z-index:13;max-height:30vh;overflow:auto;padding:8px 36px 8px 12px;position:fixed}
   #card .cx{position:absolute;right:6px;top:4px;width:26px;height:26px;border:1px solid #12414a;color:#8fb3bd;background:transparent;font:inherit;cursor:pointer;touch-action:manipulation}
   #card .cq{color:#cde;border-left:2px solid #3a4150;padding-left:8px;margin:4px 0;white-space:pre-wrap}
@@ -81,7 +97,8 @@
   #card .ct{color:var(--cy);cursor:pointer;text-decoration:underline dotted}
   @media (max-width:640px){ #card{left:6px;right:6px;bottom:6px!important;max-height:34vh;font-size:11px} }
   @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{font-size:11px;margin-right:4px} #bar .gm-title{padding:5px 8px}
-    #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);left:0;right:0;max-width:none;max-height:62vh} #hud{text-align:left} }
+    #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);left:0;right:0;max-width:none;max-height:var(--panelmax,62vh)} #hud{text-align:left}
+    #lines{width:auto} #lineslist .ln,#lineslist .lg,#linesctl label,#linesctl button,#lycount{font-size:12px} #lyClear{font-size:20px} }
 </style>
 </head>
 <body>
@@ -683,7 +700,7 @@
   const b = edPlaced[edSel]; edCard(edSel); edFly(b); }
 // a tap within 9 px of a spark opens that line (runs after the engine's own tap handler)
 addEventListener('pointerup', e => {
-  if (!edPlaced.length || moved >= 4 || pts.size > 0) return;
+  if (e.target !== cv || !edPlaced.length || moved >= 4 || pts.size > 0) return;
   let best = -1, bd = 81;
   for (let i = 0; i < edPlaced.length; i++) { const [x, y] = edScreen(edPlaced[i]); const d = (x - e.clientX)**2 + (y - e.clientY)**2; if (d < bd) { bd = d; best = i; } }
   if (best >= 0) { edCard(best); edFly(edPlaced[best]); }
@@ -703,19 +720,27 @@
   + '<button class="gm-title" data-panel="foot">commands</button>';
 document.body.appendChild(bar);
 const linesPanel = document.createElement('div'); linesPanel.id = 'lines'; linesPanel.className = 'gm-panel';
-linesPanel.innerHTML = '<div id="linesctl"><label><input type="checkbox" id="lyAll" checked> verified lines layer</label>'
-  + '<label><input type="checkbox" id="lyFocus"> gridatlas + data centres only</label>'
-  + '<button data-k="e">next</button><button data-k="E">previous</button><input id="lyFind" placeholder="filter: repository, file or title"></div><div id="lineslist"></div>';
+linesPanel.innerHTML = '<div id="linesctl">'
+  + '<div class="lyrow"><label><input type="checkbox" id="lyAll" checked> lines layer</label>'
+  + '<label><input type="checkbox" id="lyFocus"> gridatlas + data centres</label></div>'
+  + '<div class="lyrow"><input id="lyFind" type="text" inputmode="search" enterkeyhint="search" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="filter: repo, file or title" aria-label="filter the lines by repository, file or title">'
+  + '<button id="lyClear" aria-label="clear the filter">\u00d7</button><button data-k="E" aria-label="previous verified line">prev</button><button data-k="e" aria-label="next verified line">next</button></div>'
+  + '<div id="lycount"></div>'
+  + '</div><div id="lineslist"></div>';
 document.body.appendChild(linesPanel);
 const PANELS = { top: elTop, hud: hud, lines: linesPanel, foot: elFoot };
 let openPanel = null;
-function placePanels(){ const h = bar.getBoundingClientRect().height; for (const el of Object.values(PANELS)) el.style.top = (h + 2) + 'px'; }
-addEventListener('resize', placePanels);
+function placePanels(){ const h = bar.getBoundingClientRect().height;
+  const vv = Math.min(innerHeight, (window.visualViewport && visualViewport.height) || innerHeight), avail = vv - (h + 2) - 8;
+  const frac = innerHeight - vv > 100 ? 1 : (narrow() ? 0.72 : 0.62);              // keyboard up: use what is left; else leave wafer to tap
+  document.documentElement.style.setProperty('--panelmax', Math.max(140, Math.round(avail * frac)) + 'px');
+  for (const el of Object.values(PANELS)) el.style.top = (h + 2) + 'px'; }
+addEventListener('resize', placePanels); if (window.visualViewport) visualViewport.addEventListener('resize', placePanels);
 function setPanel(name){ placePanels();
   openPanel = (openPanel === name) ? null : name;
   for (const [k, el] of Object.entries(PANELS)) el.classList.toggle('gm-open', k === openPanel);
   for (const b of bar.querySelectorAll('.gm-title')) b.classList.toggle('gm-on', b.dataset.panel === openPanel);
-  if (openPanel === 'lines') fillLines();
+  if (openPanel === 'lines') { if (edSel >= 0) lyClosed.delete(edPlaced[edSel].repo); fillLines(); const s = linesPanel.querySelector('.ln.sel'); if (s) s.scrollIntoView({ block:'center' }); }
   dirty = true;
 }
 bar.addEventListener('click', e => { const b = e.target.closest('.gm-title'); if (b) { e.stopPropagation(); setPanel(b.dataset.panel); } });
@@ -725,21 +750,38 @@
 // the safe rectangle now starts under the bar, and the hidden panels take no room
 { const _safe = safeBox; safeBox = function(){ const s = _safe(); s.y0 = Math.max(s.y0, bar.getBoundingClientRect().bottom + 8); s.y1 = Math.max(s.y0 + 24, innerHeight - 8); return s; }; }
 // the lines layer: on/off and focus-only, the list, the filter
-let lyOn = true, lyFocus = false, lyQuery = '';
-document.getElementById('lyAll').addEventListener('change', e => { lyOn = e.target.checked; dirty = true; });
+let lyOn = true, lyFocus = false, lyQuery = ''; const lyClosed = new Set();
+const lyFindEl = document.getElementById('lyFind'), lyClearEl = document.getElementById('lyClear');
+document.getElementById('lyAll').addEventListener('change', e => { lyOn = e.target.checked; dirty = true; fillLines(); });
 document.getElementById('lyFocus').addEventListener('change', e => { lyFocus = e.target.checked; dirty = true; fillLines(); });
-document.getElementById('lyFind').addEventListener('input', e => { lyQuery = e.target.value.trim().toLowerCase(); fillLines(); });
-document.getElementById('lyFind').addEventListener('keydown', e => e.stopPropagation());
+lyFindEl.addEventListener('input', e => { lyQuery = e.target.value.trim().toLowerCase(); lyClearEl.classList.toggle('on', !!e.target.value); fillLines(); });
+lyFindEl.addEventListener('keydown', e => { e.stopPropagation();                   // typing e, n, r, / or Escape here is text, not a command
+  if (e.key === 'Enter') lyFindEl.blur();                                          // puts the keyboard away, the list is what is left
+  else if (e.key === 'Escape') { if (lyFindEl.value) { lyFindEl.value = ''; lyFindEl.dispatchEvent(new Event('input')); } else lyFindEl.blur(); } });
+lyClearEl.addEventListener('click', e => { e.stopPropagation(); lyFindEl.value = ''; lyFindEl.dispatchEvent(new Event('input')); });
 linesPanel.addEventListener('click', e => { const k = e.target.getAttribute('data-k'); if (k) { e.stopPropagation(); dispatchEvent(new KeyboardEvent('keydown', { key:k })); return; }
+  const g = e.target.closest('.lg'); if (g) { e.stopPropagation(); const r = g.dataset.g; if (lyClosed.has(r)) lyClosed.delete(r); else lyClosed.add(r); fillLines(); return; }
   const row = e.target.closest('[data-i]'); if (row) { e.stopPropagation(); const i = +row.dataset.i; const b = edPlaced[i]; if (openPanel) setPanel(openPanel); edCard(i); edFly(b); } });
 function visibleLine(b){ return lyOn && (!lyFocus || b.class === 'focus'); }
 function fillLines(){
-  const list = document.getElementById('lineslist'); if (!list) return;
-  const rows = [];
+  const list = document.getElementById('lineslist'), count = document.getElementById('lycount'); if (!list) return;
+  const groups = new Map(); let shown = 0;
   edPlaced.forEach((b, i) => { if (!visibleLine(b)) return;
     const hay = (b.repo + ' ' + b.path + ' ' + b.title).toLowerCase(); if (lyQuery && !hay.includes(lyQuery)) return;
-    rows.push('<div class="ln' + (i === edSel ? ' sel' : '') + (b.class === 'focus' ? ' focus' : '') + '" data-i="' + i + '"><b>' + esc(b.repo) + '</b> ' + esc(b.path) + ':' + b.line + '<br>' + esc(b.title) + '</div>'); });
+    shown++; if (!groups.has(b.repo)) groups.set(b.repo, []); groups.get(b.repo).push(i); });
+  const order = [...groups.keys()].sort((a, c) => groups.get(c).length - groups.get(a).length || a.localeCompare(c));
+  const rows = [];
+  for (const repo of order) { const ids = groups.get(repo).sort((a, c) => edPlaced[a].path.localeCompare(edPlaced[c].path) || edPlaced[a].line - edPlaced[c].line);
+    const closed = !lyQuery && lyClosed.has(repo), focus = edPlaced[ids[0]].class === 'focus';
+    rows.push('<div class="lg' + (focus ? ' focus' : '') + (closed ? ' closed' : '') + '" data-g="' + esc(repo) + '"><span class="ch">' + (closed ? '\u25b8' : '\u25be') + '</span>' + esc(repo) + ' <span class="n">' + fmt(ids.length) + (ids.length === 1 ? ' line' : ' lines') + '</span></div>');
+    if (closed) continue;
+    for (const i of ids) { const b = edPlaced[i];
+      rows.push('<div class="ln' + (i === edSel ? ' sel' : '') + (b.class === 'focus' ? ' focus' : '') + '" data-i="' + i + '"><b>' + esc(b.path) + ':' + b.line + '</b><div class="t">' + esc(b.title) + '</div></div>'); } }
   list.innerHTML = rows.join('') || '<div class="ln">no line matches</div>';
+  const total = edPlaced.length, focusN = edPlaced.reduce((n, b) => n + (b.class === 'focus' ? 1 : 0), 0);
+  if (count) count.textContent = !lyOn ? 'layer off \u00b7 ' + fmt(total) + ' lines hidden'
+    : shown === total ? fmt(total) + ' lines in ' + order.length + ' repositories \u00b7 ' + fmt(focusN) + ' gridatlas + data centres'
+    : fmt(shown) + ' of ' + fmt(total) + ' lines' + (lyQuery ? ' match \u201c' + lyQuery + '\u201d' : '') + (lyFocus ? ' \u00b7 gridatlas + data centres only' : '');
 }
 // the sparks obey the layer switches
 { const _drawEd = drawEdition; drawEdition = function(){ if (!lyOn) { hud.textContent += '\nEDITION 4 · verified lines layer off'; return; }
@@ -747,6 +789,7 @@
 { const _edNext = edNext; edNext = function(step){ if (!edPlaced.length) return; let i = edSel, n = edPlaced.length;
     for (let t = 0; t < n; t++) { i = (i + step + n) % n; if (visibleLine(edPlaced[i])) break; }
     edSel = i; const b = edPlaced[edSel]; edCard(edSel); edFly(b); }; }
+placePanels();
 requestAnimationFrame(frame);
 </script>
 </body>
```

## TEST

Serve the kuiper-belt root (`python3 -m http.server 8105 --bind 127.0.0.1`) with the patch applied to the Edition 5
folder and run, with the brief's Chromium flags and `devices['Pixel 7']` (then `devices['Galaxy S24']`):

1. `page.goto(url)`, wait 7 s. Expect no console errors. `getComputedStyle(document.documentElement).getPropertyValue('--panelmax')` is a px value (set by `placePanels()` at load).
2. Tap the LINES title (`page.touchscreen.tap` at the centre of `#bar [data-panel=lines]`), wait 0.5 s. Expect `#lines.gm-open` with `display:flex`, `#lines.getBoundingClientRect().bottom <= innerHeight`, `#lines.scrollHeight <= #lines.clientHeight + 1`, and `#lineslist.scrollHeight > #lineslist.clientHeight` with `overflow-y:auto` (the list scrolls, not the panel); `#lines.getBoundingClientRect().width === innerWidth` on a phone.
3. Measure: every `#linesctl label`, `#linesctl button` (visible ones) and `#lyFind` has height >= 44; each checkbox is 20x20; `getComputedStyle(#lyFind).fontSize === '16px'`; `#lyFind.getAttribute('inputmode') === 'search'`; `document.querySelectorAll('#lineslist .ln').length === 344`; no `.ln` has height < 44; `#lineslist .lg` count is 21 and the first header reads `gridatlas 121 lines`; `#lycount` reads `344 lines in 21 repositories · 174 gridatlas + data centres`.
4. CDP `Input.dispatchTouchEvent` drag of 300 px upward inside `#lineslist`, 20 moves at 16 ms. Expect `#lineslist.scrollTop > 200`, `scrollY === 0`, `visualViewport.offsetTop === 0`, and `#lyFind` still inside the viewport.
5. Tap `#lyFind`; expect `document.activeElement.id === 'lyFind'` and `visualViewport.scale === 1`. `page.keyboard.type('gridatlas')`: expect 126 rows and `#lycount` `126 of 344 lines match “gridatlas”`; `#lyClear` is displayed. `page.setViewportSize({width:412,height:519})` (the keyboard as resizes-content): expect `#lines` bottom <= 519, `#lineslist` still scrolling inside, `#lyFind` inside the viewport. Restore the size. Tap `#lyClear`: expect value `''`, 344 rows, `#lyClear` hidden.
6. Tap the second label (`gridatlas + data centres`): expect `#lyFocus.checked`, 174 rows, headers exactly `gridatlas`, `data-grid-gb`, `data-centres-gb`, count `174 of 344 lines · gridatlas + data centres only`. Tap again: 344 rows. Tap the first label twice: `#lyAll` goes false (count `layer off · 344 lines hidden`, list says `no line matches`) then true.
7. Tap a header (e.g. `kuiper-belt`): its rows disappear and the header shows `▸`; tap again: they return.
8. `scrollIntoView` the first row after the `gridatlas` header and `touchscreen.tap` its centre. Immediately: `#lines` no longer `.gm-open`, `#card` `display:block` containing `of 344`. After 8 s: read `#o`'s `getImageData`, take the centroid of pixels with r > 200, g < 90, b > 170; expect it between `#bar`'s bottom and `#card`'s top. Press `e` (or tap NEXT in LINES) and reopen LINES: expect the `.ln.sel` row inside the list's visible box.
9. Tap EDITION, READOUT, COMMANDS in turn: each panel's bottom <= innerHeight, `overscroll-behavior-y: contain`, and the page not scrollable.
10. Desktop regression at 1280x800: LINES 720 px wide, cap 462 px, list scrolls inside, no errors.

## LIMITS

- Playwright's Android emulation opens no soft keyboard and performs no focus zoom; the keyboard was emulated by shrinking the viewport (the `resizes-content` path). The default `resizes-visual` path (visual viewport shrinks, layout viewport does not) is handled in code (`visualViewport.height` in `placePanels`, resize listener) but was not exercised; a check on a real Android phone is wanted.
- Timings are from a shared 4-core box at load average 47-83 under SwiftShader; the quiet-machine numbers (24 ms / 17 ms to open 344 rows) are the first runs only. Scroll frame times on this box say nothing about a phone's GPU compositor.
- `label:has(input:checked)` needs Chrome 105+ (Android Chrome has had it since 2022); without it only the label's colour change is lost, the checkbox still shows state.
- The grouped list is in repository order while `e`/`E` step in key order; the card's "n of 344" is the key order, as before.
- Overlap for the integrator: `placePanels` (also measured by dimension 01's bar work) and the one-line `pointerup` guard (touch/spark dimension); everything else is inside the LINES panel's own CSS and handlers. The bar's two-row wrap (75 px) is not addressed here.
- The pre-existing tap-to-close on the wafer (`cv pointerdown` closes the panel) still lets the same tap's `pointerup` select a spark under the finger; outside this dimension, noted for the touch auditor.
- Not changed: `#card`, `edFly`, keys, sparks, `keys.json`, `cosmos`, the README (the integrator's "What changed from Edition 4" should name the grouped, counted, clearable LINES list).
