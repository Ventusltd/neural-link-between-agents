# NL-009 round 1 · FABLE-09 · dimension "robust" (robustness, orientation, accessibility, failure states, Android)

Audited: `editions/202611012027/index.html` (Edition 4) at kuiper-belt HEAD 018b46aed50f28f7b1882a0dcaba6593ce522beb,
served from the repository root on port 8109, Playwright Chromium (SwiftShader), `devices['Pixel 7']` (412x839 css px,
dsf 2.625, touch), rotation and the Android dynamic toolbar simulated by `setViewportSize`. Scripts and raw
measurements: `/tmp/nl009/09/audit.cjs`, `/tmp/nl009/09/extra.cjs`, `/tmp/nl009/09/out-orig/result.json`,
`/tmp/nl009/09/out-patched/result.json` (machine-local, not committed). Screenshots: `img/09-robust-*.png`.

## FINDINGS

1. **MAJOR · the READOUT panel slides under the bar after any pick.** Pixel 7 portrait, READOUT open, press `e`:
   `#hud.style.top` = `0px`, rect y=0 h=311.8 while `#bar` is 75.1 px tall (two rows at 412 px), so the first two
   readout lines (RESOLVED/UNRESOLVED, the GPU line) are hidden behind the bar (`img/09-robust-before-readout-under-bar.png`).
   Cause: the engine's `layout()` sets `hud.style.top = elTop.offsetHeight + 'px'` on every `safeBox()` call (so on every
   `edFly`), and the EDITION panel it measures is `display:none`, hence 0; `placePanels()` only runs on `resize` and in
   `setPanel`. After the patch the top is `77.09px` in all four measured states (portrait, landscape, portrait again,
   toolbar −56 px). Before: `0px` first open, correct only after a resize.
2. **MAJOR · WebGL unavailable gives a blank black screen.** Launched with `--disable-webgl --disable-webgl2`: visible text
   elements = 0, `#hud` (where the refusal is written) has `display:none` under the Edition 3 CSS, no bar is built, and the
   console shows an uncaught `0` (`throw 0`). After: a `#refuse` strip (`role=alert`, z-index 30) says in words that
   WebGL2 is missing and where the lines are (`img/09-robust-after-no-webgl.png`), and the throw names itself
   (`Error: WebGL2 is not available`). The same strip is used for `webglcontextlost` and a failed `cosmos/wafer.tsv`.
3. **MINOR · no `<noscript>`.** With JavaScript off `document.body.innerText` is empty. After: one sentence in a
   `<noscript>` strip. (Measured with `javaScriptEnabled:false`.)
4. **MINOR · `keys.json` 404 is only said in the hidden READOUT.** With keys.json served as 404: READOUT does carry
   `EDITION 4 · keys.json did not load` (good), but the EDITION panel heading reads `0 VERIFIED LINES LIT` and the LINES
   panel reads `no line matches`; `e` does nothing silently. No JavaScript exception before or after (the only console line
   is the network 404 itself). After: EDITION heading `KEYS.JSON DID NOT LOAD · NO VERIFIED LINES LIT`, LINES panel
   `keys.json did not load`.
5. **MINOR · Escape does not close the card.** Panel open + card open: first Escape closes the panel (correct), second
   Escape leaves the card `display:block`. After: second Escape closes the card (and clears the selection), never while
   the `/` box is open.
6. **MINOR · `prefers-reduced-motion` is ignored.** Context with `reducedMotion:'reduce'`, press `e`: 31 distinct zoom
   values written to the HUD during the 900 ms fly. After: 1 value (`14.0`), the camera lands in the first frame. Done by
   wrapping `flyTo` in the edition layer; the engine's tween and the placement law are untouched.
7. **MINOR · ARIA and keyboard.** Before: `#bar` has no role/name; the four bar buttons have no `aria-expanded` /
   `aria-controls`; the four panels have no role or name; the card has no role and no live region; the "details" toggle
   is a `<span>` (`tabIndex -1`, unreachable by keyboard); the 344 LINES rows are `<div>`s, 0 focusable; `#lyFind` has a
   placeholder only; the bar is body child 8 (after the panels it controls). After: `#bar role=toolbar
   aria-label="Kuiper Edition menu"`, buttons carry `aria-controls=<panel id>` and `aria-expanded` kept in sync by
   `setPanel` (measured `true` on the open one, `false` on the rest); panels `role=region` with names edition / readout /
   lines / commands; card `role=region aria-label="verified line" aria-live=polite` (announces the chosen line on `e`);
   details is a `<button aria-expanded>` that toggles to `true`; LINES rows `role=button tabindex=0`, 344/344 focusable,
   Enter or Space on a row opens its card and closes the panel (measured: "6 of 344", panel closed); `#lyFind
   aria-label="filter lines"`; the bar is body child 0 so the Tab order is bar → open panel → card. Focus is visible:
   Chrome's default ring (`outline: auto 1px`, `:focus-visible` true) on the bar buttons before and after; nothing in the
   page removes it except the `/` input.

PASS without a patch (measured, same runs):
- Orientation portrait → landscape → portrait with READOUT and the card open: canvas buffers follow the window
  (412x839 → 839x412 → 412x839, CSS rect identical), `placePanels` recomputes (panel top 77.1 → 47.6 → 77.1), the chosen
  spark (magenta centroid on the overlay) stays in the clear space: y = 444.9 / 231.6 / 444.9 against bar bottom
  75 / 46 / 75 and card top 721.8 / 299.6 / 721.8.
- Android dynamic toolbar simulated as −56 px (412x783): canvas 412x783, card top 665.8, spark y 416.9, still clear.
- Deep link: the engine has no `location.hash` handling (grep: none in the page); `#1000000` loads normally with the
  edition layer (344 lit, 0 console errors), so there is nothing for the edition layer to break. `?selftest=` is the
  only URL parameter.
- Zero `pageerror`s and zero page console errors in the normal runs before and after (the single Canvas2D
  `willReadFrequently` warning is produced by the audit's own `getImageData` probe).

## PATCH

Unified diff against `editions/202611012027/index.html`, labels `a/` `b/`: from the kuiper-belt root
`git apply 09-robust.patch` (or `patch -p1 < 09-robust.patch`); `git apply --check` passed at HEAD 018b46a.
The extracted module script passes `node --check`. Nothing in keys.json, cosmos, or the placement law is touched;
the engine edits are the refusal messages only (lines 128, 193, 243) and are additive.

```diff
--- a/editions/202611012027/index.html
+++ b/editions/202611012027/index.html
@@ -80,11 +80,17 @@
   #card.open .cd{display:block}
   #card .ct{color:var(--cy);cursor:pointer;text-decoration:underline dotted}
   @media (max-width:640px){ #card{left:6px;right:6px;bottom:6px!important;max-height:34vh;font-size:11px} }
+  /* EDITION 5 (robust): a refusal is said on screen, not only in a hidden panel; the details toggle is a button */
+  #refuse,noscript .refuse{position:fixed;left:12px;right:12px;top:36%;z-index:30;background:#090c13f2;border:1px solid var(--am);color:var(--ink);
+    padding:12px 14px;font-size:13px;white-space:pre-line;max-width:min(640px,96vw);margin:0 auto}
+  #card button.ct{appearance:none;background:none;border:0;padding:0;margin:0;font:inherit;color:var(--cy);cursor:pointer;text-decoration:underline dotted}
+  @media (prefers-reduced-motion:reduce){ #top.open #sub,#top #sub{transition:none} }
   @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{font-size:11px;margin-right:4px} #bar .gm-title{padding:5px 8px}
     #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);left:0;right:0;max-width:none;max-height:62vh} #hud{text-align:left} }
 </style>
 </head>
 <body>
+<noscript><div class="refuse" role="alert">KUIPER EDITION 4 needs JavaScript and WebGL2 to draw the wafer. Nothing is drawn without them; the verified lines are listed in keys.json and README.md in this folder.</div></noscript>
 <canvas id="c"></canvas><canvas id="o"></canvas>
 <div id="top"><div id="big">loading</div><div id="sub">&nbsp;</div></div>
 <div id="hud">starting</div>
@@ -125,7 +131,9 @@
 const fmt = n => Math.round(n).toLocaleString('en-GB');
 function words(n){ if (n >= 1e9) return (n/1e9).toFixed(2)+' billion'; if (n >= 1e6) return (n/1e6).toFixed(2)+' million';
   if (n >= 1e3) return (n/1e3).toFixed(1)+' thousand'; return n >= 10 ? n.toFixed(0) : n.toFixed(2); }
-if (!gl) { hud.textContent = 'WebGL2 is not available. Refusing rather than drawing a fraction.'; throw 0; }
+function refuse(m){ hud.textContent = m; let d = document.getElementById('refuse');
+  if (!d) { d = document.createElement('div'); d.id = 'refuse'; d.setAttribute('role', 'alert'); document.body.appendChild(d); } d.textContent = m; }
+if (!gl) { refuse('WebGL2 is not available in this browser. Refusing rather than drawing a fraction of the wafer. The verified lines are in keys.json and README.md in this folder.'); throw new Error('WebGL2 is not available'); }
 
 const VS_FULL = `#version 300 es
 void main(){ vec2 p = vec2(float((gl_VertexID<<1)&2), float(gl_VertexID&2)); gl_Position = vec4(p*2.0-1.0,0.0,1.0); }`;
@@ -190,7 +198,7 @@
 gl.bindVertexArray(gl.createVertexArray());
 let lost = false;
 cv.addEventListener('webglcontextlost', e => { e.preventDefault(); lost = true;
-  hud.textContent = 'CONTEXT LOST. Nothing on screen is a count. Reload.'; });
+  refuse('CONTEXT LOST. Nothing on screen is a count. Reload.'); });
 
 // --------------------------------------------------------------------------------- the data
 // cosmos/wafer.tsv: every commit in time order with its measured lines and the unissued keys
@@ -237,7 +245,7 @@
   if (new URLSearchParams(location.search).get('selftest') === 'phone') setTimeout(phoneSelftest, 500);
   { const mr = (new URLSearchParams(location.search).get('selftest') || '').match(/^repo:(.+)$/);
     if (mr) setTimeout(() => repoSelftest(decodeURIComponent(mr[1])), 500); }
-}).catch(() => { hud.textContent = '../../cosmos/wafer.tsv did not load. The wafer will not invent its keys.'; });
+}).catch(() => { refuse('../../cosmos/wafer.tsv did not load. The wafer will not invent its keys.'); });
 
 // ------------------------------------------------------------------------ camera and address
 let cx = 0, cy = 0, zoom = 1, dirty = true, tween = null, litRepo = -1, target = null;
@@ -631,7 +639,7 @@
   catch (e) { ED = []; edMeta = { error: 'keys.json did not load' }; }
   edPlaced = ED.filter(b => b.on_wafer && b.verified && Number.isFinite(b.key) && b.key >= 0 && b.key < SPACE)
                .map(b => { const p = keyPlace(b.key); return Object.assign({}, b, { x:p[0], y:p[1] }); });
-  big.textContent = 'Kuiper Edition 4 · ' + fmt(edPlaced.length) + ' verified lines lit';
+  big.textContent = 'Kuiper Edition 4 · ' + (edMeta && edMeta.error ? edMeta.error + ' · no verified lines lit' : fmt(edPlaced.length) + ' verified lines lit');
   sub.textContent = 'Edition 1 verified ' + fmt(ED.length) + ' lines of the estate (354 keyed findings, 495 keys re-resolved; see ../202610311905/). '
     + 'Here each is a green spark at its own key on the one wafer: ' + sub.textContent;
   dirty = true;
@@ -655,12 +663,13 @@
 function edCard(i){
   const b = edPlaced[i], a = address(b.key);
   card.style.display = 'block'; card.classList.remove('open');
+  card.setAttribute('role', 'region'); card.setAttribute('aria-label', 'verified line'); card.setAttribute('aria-live', 'polite');
   card.innerHTML = '<button class="cx" aria-label="close">×</button>'
     + '<b>' + esc(b.title) + '</b>  <span style="color:var(--dim)">' + fmt(i + 1) + ' of ' + fmt(edPlaced.length) + '</span>'
     + '\n' + esc(b.repo) + '  ' + esc(b.path) + ':' + b.line
     + (b.quote ? '<div class="cq">' + esc(b.quote) + '</div>' : '')
     + '<a href="' + esc(b.destination) + '" target="_blank" rel="noopener">open on GitHub at ' + esc(String(b.commit).slice(0,7)) + '</a>'
-    + '  ·  <span class="ct">details</span>'
+    + '  ·  <button class="ct" aria-expanded="false">details</button>'
     + '<div class="cd">' + (b.pattern ? 'pattern: ' + esc(b.pattern) + '\n' : '') + 'found by ' + esc(b.worker) + ' ' + esc(b.finding) + ', verified by a controller\n' + describe(a) + '</div>';
   if (a && !a.silent) litRepo = a.c.repo;
   target = { x:b.x, y:b.y }; edSel = i; dirty = true;
@@ -668,7 +677,7 @@
 // the card toggles its details, closes on ×, and never swallows the link
 card.addEventListener('click', e => {
   if (e.target.closest('.cx')) { card.style.display = 'none'; edSel = -1; target = null; dirty = true; e.stopPropagation(); return; }
-  if (e.target.closest('.ct')) { card.classList.toggle('open'); e.stopPropagation(); return; }
+  if (e.target.closest('.ct')) { const on = card.classList.toggle('open'); e.target.closest('.ct').setAttribute('aria-expanded', on ? 'true' : 'false'); e.stopPropagation(); return; }
   if (e.target.closest('a')) { e.stopPropagation(); return; }
   e.stopPropagation();                                           // a tap on the card body keeps it open
 }, true);
@@ -695,41 +704,46 @@
 // Borrowed in spirit from gridatlas atlas/modules/202609031958-menu-bar.js: one row of titles, every panel
 // hidden until its title is tapped, one open at a time, closed by the same tap, by Escape, or by a tap on the
 // wafer. The wafer gets the whole screen; the readout, the commands and the edition's own text are layers.
-const bar = document.createElement('div'); bar.id = 'bar';
+const bar = document.createElement('div'); bar.id = 'bar'; bar.setAttribute('role', 'toolbar'); bar.setAttribute('aria-label', 'Kuiper Edition menu');
 bar.innerHTML = '<span id="barname">KUIPER EDITION 4</span>'
-  + '<button class="gm-title" data-panel="top">edition</button>'
-  + '<button class="gm-title" data-panel="hud">readout</button>'
-  + '<button class="gm-title" data-panel="lines">lines</button>'
-  + '<button class="gm-title" data-panel="foot">commands</button>';
-document.body.appendChild(bar);
+  + '<button class="gm-title" data-panel="top" aria-controls="top" aria-expanded="false">edition</button>'
+  + '<button class="gm-title" data-panel="hud" aria-controls="hud" aria-expanded="false">readout</button>'
+  + '<button class="gm-title" data-panel="lines" aria-controls="lines" aria-expanded="false">lines</button>'
+  + '<button class="gm-title" data-panel="foot" aria-controls="foot" aria-expanded="false">commands</button>';
+document.body.prepend(bar);
 const linesPanel = document.createElement('div'); linesPanel.id = 'lines'; linesPanel.className = 'gm-panel';
 linesPanel.innerHTML = '<div id="linesctl"><label><input type="checkbox" id="lyAll" checked> verified lines layer</label>'
   + '<label><input type="checkbox" id="lyFocus"> gridatlas + data centres only</label>'
-  + '<button data-k="e">next</button><button data-k="E">previous</button><input id="lyFind" placeholder="filter: repository, file or title"></div><div id="lineslist"></div>';
+  + '<button data-k="e">next</button><button data-k="E">previous</button><input id="lyFind" aria-label="filter lines" placeholder="filter: repository, file or title"></div><div id="lineslist"></div>';
 document.body.appendChild(linesPanel);
 const PANELS = { top: elTop, hud: hud, lines: linesPanel, foot: elFoot };
+for (const [k, el] of Object.entries(PANELS)) { el.setAttribute('role', 'region'); el.setAttribute('aria-label', { top:'edition', hud:'readout', lines:'lines', foot:'commands' }[k]); }
 let openPanel = null;
 function placePanels(){ const h = bar.getBoundingClientRect().height; for (const el of Object.values(PANELS)) el.style.top = (h + 2) + 'px'; }
 addEventListener('resize', placePanels);
 function setPanel(name){ placePanels();
   openPanel = (openPanel === name) ? null : name;
   for (const [k, el] of Object.entries(PANELS)) el.classList.toggle('gm-open', k === openPanel);
-  for (const b of bar.querySelectorAll('.gm-title')) b.classList.toggle('gm-on', b.dataset.panel === openPanel);
+  for (const b of bar.querySelectorAll('.gm-title')) { const on = b.dataset.panel === openPanel; b.classList.toggle('gm-on', on); b.setAttribute('aria-expanded', on ? 'true' : 'false'); }
   if (openPanel === 'lines') fillLines();
   dirty = true;
 }
 bar.addEventListener('click', e => { const b = e.target.closest('.gm-title'); if (b) { e.stopPropagation(); setPanel(b.dataset.panel); } });
-addEventListener('keydown', e => { if (e.key === 'Escape' && openPanel) setPanel(openPanel); });
+addEventListener('keydown', e => { if (e.key !== 'Escape' || gbox.style.display === 'block') return;
+  if (openPanel) setPanel(openPanel); else if (card.style.display === 'block') { card.style.display = 'none'; edSel = -1; target = null; dirty = true; } });
 cv.addEventListener('pointerdown', () => { if (openPanel) setPanel(openPanel); });
 elTop.classList.add('open');                                   // the long subtitle is readable once the panel is open
 // the safe rectangle now starts under the bar, and the hidden panels take no room
-{ const _safe = safeBox; safeBox = function(){ const s = _safe(); s.y0 = Math.max(s.y0, bar.getBoundingClientRect().bottom + 8); s.y1 = Math.max(s.y0 + 24, innerHeight - 8); return s; }; }
+{ const _safe = safeBox; safeBox = function(){ const s = _safe(); placePanels(); s.y0 = Math.max(s.y0, bar.getBoundingClientRect().bottom + 8); s.y1 = Math.max(s.y0 + 24, innerHeight - 8); return s; }; }
+// prefers-reduced-motion: the camera lands at once instead of flying for 900 ms
+{ const _fly = flyTo, rm = matchMedia('(prefers-reduced-motion: reduce)'); flyTo = function(x, y, z){ _fly(x, y, z); if (rm.matches && tween) tween.t0 -= tween.dur; }; }
 // the lines layer: on/off and focus-only, the list, the filter
 let lyOn = true, lyFocus = false, lyQuery = '';
 document.getElementById('lyAll').addEventListener('change', e => { lyOn = e.target.checked; dirty = true; });
 document.getElementById('lyFocus').addEventListener('change', e => { lyFocus = e.target.checked; dirty = true; fillLines(); });
 document.getElementById('lyFind').addEventListener('input', e => { lyQuery = e.target.value.trim().toLowerCase(); fillLines(); });
 document.getElementById('lyFind').addEventListener('keydown', e => e.stopPropagation());
+linesPanel.addEventListener('keydown', e => { const row = e.target.closest('[data-i]'); if (row && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); e.stopPropagation(); row.click(); } });
 linesPanel.addEventListener('click', e => { const k = e.target.getAttribute('data-k'); if (k) { e.stopPropagation(); dispatchEvent(new KeyboardEvent('keydown', { key:k })); return; }
   const row = e.target.closest('[data-i]'); if (row) { e.stopPropagation(); const i = +row.dataset.i; const b = edPlaced[i]; if (openPanel) setPanel(openPanel); edCard(i); edFly(b); } });
 function visibleLine(b){ return lyOn && (!lyFocus || b.class === 'focus'); }
@@ -738,8 +752,8 @@
   const rows = [];
   edPlaced.forEach((b, i) => { if (!visibleLine(b)) return;
     const hay = (b.repo + ' ' + b.path + ' ' + b.title).toLowerCase(); if (lyQuery && !hay.includes(lyQuery)) return;
-    rows.push('<div class="ln' + (i === edSel ? ' sel' : '') + (b.class === 'focus' ? ' focus' : '') + '" data-i="' + i + '"><b>' + esc(b.repo) + '</b> ' + esc(b.path) + ':' + b.line + '<br>' + esc(b.title) + '</div>'); });
-  list.innerHTML = rows.join('') || '<div class="ln">no line matches</div>';
+    rows.push('<div class="ln' + (i === edSel ? ' sel' : '') + (b.class === 'focus' ? ' focus' : '') + '" data-i="' + i + '" role="button" tabindex="0"><b>' + esc(b.repo) + '</b> ' + esc(b.path) + ':' + b.line + '<br>' + esc(b.title) + '</div>'); });
+  list.innerHTML = rows.join('') || '<div class="ln">' + (edMeta && edMeta.error ? esc(edMeta.error) : 'no line matches') + '</div>';
 }
 // the sparks obey the layer switches
 { const _drawEd = drawEdition; drawEdition = function(){ if (!lyOn) { hud.textContent += '\nEDITION 4 · verified lines layer off'; return; }
```

## TEST

Serve the kuiper-belt root (`python3 -m http.server 8109 --bind 127.0.0.1`), launch Chromium with
`--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`, context
`{...devices['Pixel 7']}`; wait 8 s after load and 6–7 s after each fly; `page.touchscreen.tap` on bar buttons.

1. Readout placement: tap READOUT, `page.keyboard.press('e')`, wait 7 s, read `document.getElementById('hud').style.top`
   and `getBoundingClientRect().y`: expect both ≈ `#bar` height + 2 (77 px at 412 px wide), not 0.
2. Rotation: `setViewportSize({width:839,height:412})`, wait 6 s, then back to 412x839: `#c.width/height` equal
   `innerWidth/innerHeight` each time; the `.gm-open` panel's `style.top` equals bar height + 2; the magenta spark
   (overlay pixels r>200,g<90,b>170) lies between the bar bottom and the card top. Repeat with 412x783 for the toolbar.
3. Escape: with a panel and the card open press Escape twice: panel closes, then `#card` display is `none`.
4. Reduced motion: context `reducedMotion:'reduce'`; observe `#hud` with a MutationObserver collecting the `zoom …`
   line; press `e`: expect a single value `14.0`.
5. keys.json: `context.route(/keys\.json$/, r => r.fulfill({status:404}))`; after load `#big` text contains
   `keys.json did not load`; LINES list says the same; no `pageerror`.
6. WebGL: launch with `--disable-webgl --disable-webgl2`; expect `#refuse[role=alert]` visible with the WebGL2 sentence;
   `pageerror` message is `WebGL2 is not available`, not `0`.
7. No JS: context `javaScriptEnabled:false`; `page.content()` contains the `<noscript>` sentence and it renders.
8. ARIA: `#bar[role=toolbar]`; each `.gm-title` has `aria-controls` naming an existing id and `aria-expanded` that flips
   to `true` when tapped; `#top,#hud,#lines,#foot` have `role=region` and `aria-label`; after `e`, `#card` has
   `role=region aria-live=polite`, `#card .ct` is a BUTTON with `aria-expanded`; open LINES: every `[data-i]` row has
   `tabindex=0`; focus one and press Enter: card opens, panel closes.

## LIMITS

- SwiftShader, not a phone: rotation and the dynamic toolbar are viewport resizes; no real Android Chrome, no TalkBack.
  ARIA is checked by attributes and keyboard behaviour, not by a screen reader.
- `#hud` is deliberately not `aria-live`: it is rewritten on every frame of a fly and would flood a reader; the card
  is the live region instead.
- `:focus-visible` on the LINES rows was verified by attribute and Enter behaviour; a programmatic `focus()` does not
  show the ring in Chromium, a real Tab does.
- Out of my dimension and left alone: the 26x26 px × target, the two-row bar at 412 px, and the fact that `edFly`
  centres between the bar and the card without allowing for an open panel (the spark was clear in my runs by margin,
  y 444.9 against a panel bottom of 389).
- `throw` after the WebGL refusal is kept (the engine refuses on purpose); it now carries a message.
