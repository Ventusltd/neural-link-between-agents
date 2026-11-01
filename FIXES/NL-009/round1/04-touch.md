# FABLE-04 · touch: gestures on Android Chrome · Kuiper Edition 4 (202611012027) → Edition 5

Auditor FABLE-04, dimension "touch". Page audited: `editions/202611012027/index.html` at kuiper-belt main
018b46aed50f28f7b1882a0dcaba6593ce522beb, served from the repository root on 127.0.0.1:8104. Every number below was
measured with the pre-installed Playwright Chromium (SwiftShader flags from the brief), `devices['Pixel 7']`
(412×839 CSS px, DPR 2.625, hasTouch, isMobile) and real synthesized touch through CDP `Input.dispatchTouchEvent`
(one and two touch points) or `page.touchscreen.tap`; a second pass on `devices['Galaxy S24']`. The harness is
`touch.cjs` (TEST below): it serves the page unmodified except for a `window.__k` probe appended to the module script
so the camera (`cx, cy, zoom`), `moved`, `openPanel`, the card state and `edScreen()` can be read; the probe is not in
the patch. Full JSON records: `results-before-Pixel_7.json`, `results-after-Pixel_7.json`, `results-after-Galaxy_S24.json`
(copied beside this file as `04-touch-results-*.json`).

What the engine does today (read from the page): `pointerdown` on `#c`, `pointermove`/`pointerup`/`pointercancel` on
`window`, one `Map` of pointers (one = drag, two = pinch about the world point between the fingers), `wheel` passive;
`canvas{touch-action:none}`, bar/keys/× buttons `touch-action:manipulation`, panels and card `auto`; viewport
`width=device-width,initial-scale=1,viewport-fit=cover` (no `maximum-scale`, no `user-scalable`);
`html,body{overflow:hidden;overscroll-behavior:none}`; no `contextmenu`, `popstate` or `user-select` handling;
tap = cumulative `|dx|+|dy| < 4` px with no time bound; the edition's spark pick on `pointerup` checks `moved` and
`pts.size` but not whether the press began on the canvas.

## FINDINGS

1. **Pinch on the bar or on any open panel zooms the browser page, not the wafer. MAJOR.** CDP two-finger pinch
   (80 → 240 px spread) centred on `#bar` → `visualViewport.scale` 1 → **5.0**, `pageTop` 14; the same on the open
   LINES panel (rect 0,77,396×520) → scale **5.0** (`T2b_pinch_bar`, `T2c_pinch_lines_panel`, before). The wafer's own
   zoom did not change (0.001259 before and after). Computed `touch-action`: `#bar` auto, `#lines` auto, `#top` auto,
   `#card` auto, `html` auto; viewport meta has no `maximum-scale`/`user-scalable`. Once page-zoomed, the fixed bar and
   card are off-screen and every later gesture is confused (img/04-before-pinch-panel.png). After the patch: scale
   stays **1.0** in both cases (`html,body` and every layer `touch-action:pan-x pan-y`, buttons too, plus
   `maximum-scale=1,user-scalable=no`). Pinch on the canvas itself was already correct and stays so: zoom ratio
   **2.000** for a 2× spread, world point under the pinch centre drifts **0.000000**, `visualViewport.scale` 1
   (`T2_pinch_canvas`).

2. **A tap on a bar button, or on the card's × , also reaches the canvas and picks a spark under it. MAJOR.** The
   edition's `pointerup` spark pick does not require the press to have begun on the canvas: with spark 5 placed under
   the centre of the LINES button (both at 323.4, 20.5), `page.touchscreen.tap` on the button opened the panel **and**
   set `edSel = 5` with the card shown (`T5a`, before: "BUG: bar tap reached the canvas"). With spark 7 placed under
   the card's × (386, 688.6), tapping × closed the card and immediately reopened it on line 7 (`T5b`, before:
   `card_after: block, edSel_after: 7`; img/04-before-close-reopens.png). The bar is translucent over a full-screen
   canvas and `edFly` places sparks near the card, so this is not rare. After: `edSel -1`, card `none` in both cases;
   the pick now requires `tapUp`, the engine's own verdict that the press began on `#c` and was a tap.

3. **Tapping the wafer to dismiss a panel also acts on the wafer. MINOR.** With READOUT open, a tap at (206, 629)
   closed the panel and opened the engine's address card for the key under the finger (`T5e`, before: "tap also acted
   on the wafer"). After: the dismissing `pointerdown` sets `moved = 99`, so the tap is consumed (`card_after: none`).

4. **Android back leaves the page while a panel or the card is open; Escape does not close the card. MAJOR (back), MINOR
   (Escape).** `history.length` 2 before and after opening LINES; `page.goBack()` with LINES open → `about:blank`
   (`T6a`, before), the same with the card open (`T6b`). Escape with the card open left it `block` (`T6d`). After:
   opening a panel or a card pushes one `history.pushState({kuiper:1})` entry (kept in step with the UI on every
   redraw, so every close path, including the engine's own, releases it with `history.back()`), `popstate` closes the
   open layer; back with LINES open → URL unchanged, `openPanel null`; back with the card open → card `none`; back
   with nothing open still leaves the page (`T6c`: `page_left true`). Escape now closes the card when no panel is open.
   Judgement on `pushState`: adopted. It is the Android convention for a sheet or dialog, costs one entry only while
   something is open, and the entry is created inside the tap's user activation so Chrome's back-intervention does
   not skip it.

5. **Tap versus drag: a 6 px finger jitter is a drag, so the tap is lost; a long press is a tap. MINOR.** The
   engine sums `|dx|+|dy|` over every move: a tap that wandered (3,2)→(5,5)→(6,6) measured `moved = 12` ≥ 4 and opened
   nothing (`T3`, before: `jittered_tap_6px_opens_card false`), while Android's own touch slop is 8 dp. A 900 ms hold
   with no movement counted as a tap (before: `held_900ms_opens_card true`). After: `moved` is the distance from the
   down point, slop 10 px for `pointerType === 'touch'` (4 px for a mouse), and a touch press of ≥ 700 ms (event
   timestamps) is not a tap. Measured with CDP event timestamps (so the finger timing is exact on a loaded machine):
   a 60 ms clean tap opens the card, the 6 px jitter (`moved 8.49`, 80 ms) opens the card, a 30 px drag (`moved 30`)
   does not, the 900 ms hold does not (after: `clean_down_to_up_ms 60, held_900ms_opens_card false,
   jittered_tap_6px_opens_card true, drag_30px_opens_card false`). One-finger drag itself was and is exact: 100 px right / 60 px down
   of finger moved the camera **100.00 / 60.00** px, `pointercancel` 0, `scrollY` 0, `visualViewport.pageTop` 0, scale
   1 (`T1_drag`), so the page never scrolls or pulls to refresh (`touch-action:none` on the canvas,
   `overscroll-behavior:none`).

6. **Double tap: no page zoom and no 300 ms delay, confirmed, but only by the canvas's `touch-action:none`. MINOR.**
   Two taps 120 ms apart on the canvas and on the open EDITION panel left `visualViewport.scale` 1; `pointerup` → `click`
   on a bar button is **1 ms** (`T4`). The panels, however, were `touch-action:auto`, which on Android Chrome permits
   double-tap zoom of the panel text (the emulator does not synthesize that gesture, so this is read from the computed
   style, not seen). After: `pan-x pan-y` everywhere outside the canvas, which disables double-tap zoom by definition.

7. **Long press: no `contextmenu` guard and no `user-select:none` on the canvas or the bar. MINOR.** A synthetic
   `contextmenu` on `#c` and on a bar button was **not** `defaultPrevented` before; computed `user-select` was `auto`
   on both (`T7`). Headless Chromium does not raise the Android long-press menu from CDP touch (0 `contextmenu` events
   on a 900 ms press before and after), so the menu itself is not shown here; the patch prevents `contextmenu` on both
   canvases and the bar and sets `user-select:none;-webkit-touch-callout:none` on them (after: both prevented,
   `user-select none`). Panel and card text stay selectable on purpose.

8. **A tap on the card's own padding closes the card. MINOR.** The engine's original `card` click handler (close on
   any click) is still attached; the edition's capture handler stops propagation, which does not stop a listener on the
   same node when the target is `#card` itself. Measured: tap at the card's bottom-right padding closed it before
   (`T5f`); after `stopImmediatePropagation()` it stays open. Taps on the quote, on "details" and on the link were
   already correct (`T5c`, `T5d`).

Not found: page scroll or pull-to-refresh from a canvas drag (0 px, item 5); browser zoom from a canvas pinch (item 1);
console errors (0 before and after, both devices).

## PATCH

Unified diff against `editions/202611012027/index.html`, made with `diff -u` from a copy in scratch. Apply from the
kuiper-belt root with `patch -p0 < 04-touch.patch` or `git apply -p0 04-touch.patch` (both verified clean against
main 018b46a). Gesture handling only: one viewport meta line, one CSS block, the engine's tap discrimination (the
pointer handlers are the engine's but they are this dimension's subject; the placement law, drawing and data are
untouched), and the edition layer's tap, Escape, back and context-menu handling. `node --check` on the extracted module
passes; zero console errors on load.

```diff
--- editions/202611012027/index.html
+++ editions/202611012027/index.html
@@ -2,7 +2,7 @@
 <html lang="en">
 <head>
 <meta charset="utf-8">
-<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
+<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
 <title>Kuiper Edition 4</title>
 <style>
   :root{--bg:#090c13;--ink:#d5dcea;--dim:#7d8799;--line:#1a2030;--hot:#e8b36a}
@@ -82,6 +82,12 @@
   @media (max-width:640px){ #card{left:6px;right:6px;bottom:6px!important;max-height:34vh;font-size:11px} }
   @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{font-size:11px;margin-right:4px} #bar .gm-title{padding:5px 8px}
     #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);left:0;right:0;max-width:none;max-height:62vh} #hud{text-align:left} }
+  /* EDITION 5, TOUCH: the wafer owns every gesture on the canvas (touch-action:none, above); everything else may
+     pan but never pinch-zoom or double-tap-zoom the page, so the browser's zoom cannot wreck the layout. The
+     canvas and the bar are not text: no selection handles, no callout, no context menu on a long press. */
+  html,body{touch-action:pan-x pan-y}
+  #bar,#top,#hud,#foot,#lines,#card,#goto,#bar .gm-title,#keys button,#linesctl button,#card .cx{touch-action:pan-x pan-y}
+  canvas,#bar{user-select:none;-webkit-user-select:none;-webkit-touch-callout:none}
 </style>
 </head>
 <body>
@@ -569,13 +575,18 @@
 // on a desktop land on the same key.
 const ZMAX = 60;
 let drag = null, moved = 0, pinch = null;
+// TAP OR DRAG (Edition 5): a finger jitters, so a tap is movement under a slop (10 px for touch, Android's
+// own, 4 px for a mouse) measured from the point it went down, and for touch a press shorter than 700 ms, so
+// a long press is not a tap. tapUp is the verdict of the last pointerup, read by the edition layer.
+let down = null, slop = 4, tapUp = false;
+function isTap(e){ return !!down && moved < slop && (e.pointerType !== 'touch' || e.timeStamp - down[2] < 700); }
 const pts = new Map();
 function pinchNow(){ const v = [...pts.values()], a = v[0], b = v[1];
   return { d:Math.hypot(a.x-b.x, a.y-b.y), mx:(a.x+b.x)/2, my:(a.y+b.y)/2 }; }
 cv.addEventListener('pointerdown', e => {
   pts.set(e.pointerId, { x:e.clientX, y:e.clientY });
   if (pts.size === 2) { const s = pinchNow(), w = toWorld(s.mx, s.my); pinch = { d0:s.d, z0:zoom, wx:w[0], wy:w[1] }; drag = null; moved = 99; }
-  else if (pts.size === 1) { drag = [e.clientX, e.clientY]; moved = 0; }
+  else if (pts.size === 1) { drag = [e.clientX, e.clientY]; down = [e.clientX, e.clientY, e.timeStamp]; slop = e.pointerType === 'touch' ? 10 : 4; moved = 0; }
 });
 addEventListener('pointermove', e => {
   if (pts.has(e.pointerId)) pts.set(e.pointerId, { x:e.clientX, y:e.clientY });
@@ -583,12 +594,13 @@
       zoom = Math.max(1e-4, Math.min(ZMAX, pinch.z0 * s.d / pinch.d0));
       cx = pinch.wx - (s.mx - innerWidth/2)/zoom; cy = pinch.wy + (s.my - innerHeight/2)/zoom;
       atHome = false; tween = null; dirty = true; } return; }
-  if (!drag) return; moved += Math.abs(e.clientX-drag[0]) + Math.abs(e.clientY-drag[1]);
+  if (!drag) return; moved = Math.max(moved, Math.hypot(e.clientX-down[0], e.clientY-down[1]));
   cx -= (e.clientX-drag[0])/zoom; cy += (e.clientY-drag[1])/zoom; drag = [e.clientX, e.clientY];
   atHome = false; tween = null; dirty = true; });
 function pointerGone(e){ pts.delete(e.pointerId); if (pts.size < 2) pinch = null; if (pts.size === 0) drag = null; }
 addEventListener('pointerup', e => {
-  if (drag && moved < 4 && N) { const [wx, wy] = toWorld(e.clientX, e.clientY), r = Math.hypot(wx, wy);
+  tapUp = !!drag && isTap(e);
+  if (tapUp && N) { const [wx, wy] = toWorld(e.clientX, e.clientY), r = Math.hypot(wx, wy);
     if (r*r < SPACE) { let k = zoom >= POINTS_FROM ? keyAt(wx, wy) : -1; const exact = k >= 0; if (!exact) k = Math.floor(r*r);
       target = exact ? { x:keyPlace(k)[0], y:keyPlace(k)[1] } : null; show(address(k)); } }
   pointerGone(e); });
@@ -670,7 +682,7 @@
   if (e.target.closest('.cx')) { card.style.display = 'none'; edSel = -1; target = null; dirty = true; e.stopPropagation(); return; }
   if (e.target.closest('.ct')) { card.classList.toggle('open'); e.stopPropagation(); return; }
   if (e.target.closest('a')) { e.stopPropagation(); return; }
-  e.stopPropagation();                                           // a tap on the card body keeps it open
+  e.stopImmediatePropagation();                                  // a tap on the card body keeps it open (also from the engine's own close-on-click)
 }, true);
 // fly so that the spark lands in the clear space: under the bar, above the card
 function edFly(b){
@@ -683,7 +695,7 @@
   const b = edPlaced[edSel]; edCard(edSel); edFly(b); }
 // a tap within 9 px of a spark opens that line (runs after the engine's own tap handler)
 addEventListener('pointerup', e => {
-  if (!edPlaced.length || moved >= 4 || pts.size > 0) return;
+  if (!edPlaced.length || !tapUp || pts.size > 0) return;          // tapUp: the press began on the canvas and was a tap
   let best = -1, bd = 81;
   for (let i = 0; i < edPlaced.length; i++) { const [x, y] = edScreen(edPlaced[i]); const d = (x - e.clientX)**2 + (y - e.clientY)**2; if (d < bd) { bd = d; best = i; } }
   if (best >= 0) { edCard(best); edFly(edPlaced[best]); }
@@ -719,8 +731,18 @@
   dirty = true;
 }
 bar.addEventListener('click', e => { const b = e.target.closest('.gm-title'); if (b) { e.stopPropagation(); setPanel(b.dataset.panel); } });
-addEventListener('keydown', e => { if (e.key === 'Escape' && openPanel) setPanel(openPanel); });
-cv.addEventListener('pointerdown', () => { if (openPanel) setPanel(openPanel); });
+addEventListener('keydown', e => { if (e.key !== 'Escape') return;
+  if (openPanel) setPanel(openPanel); else if (card.style.display === 'block') { card.style.display = 'none'; edSel = -1; target = null; dirty = true; } });
+cv.addEventListener('pointerdown', () => { if (openPanel) { setPanel(openPanel); moved = 99; } });   // the dismissing tap does nothing else
+for (const el of [cv, ov, bar]) el.addEventListener('contextmenu', e => e.preventDefault());        // a long press on the wafer or the bar is not a menu
+// ANDROID BACK (Edition 5). While a panel or the card is open the page holds one extra history entry, so the
+// back gesture closes the layer instead of leaving the page; with nothing open, back leaves as it should. The
+// entry follows the state on every redraw (every open or close sets dirty), so no close path is forgotten.
+let edHist = false;
+addEventListener('popstate', () => { edHist = false; if (openPanel) setPanel(openPanel); if (card.style.display === 'block') { card.style.display = 'none'; edSel = -1; target = null; dirty = true; } });
+{ const _draw = draw; draw = function(){ _draw(); const open = !!openPanel || card.style.display === 'block';
+    if (open && !edHist) { try { history.pushState({ kuiper:1 }, ''); edHist = true; } catch (e) {} }
+    else if (!open && edHist) { edHist = false; if (history.state && history.state.kuiper) history.back(); } }; }
 elTop.classList.add('open');                                   // the long subtitle is readable once the panel is open
 // the safe rectangle now starts under the bar, and the hidden panels take no room
 { const _safe = safeBox; safeBox = function(){ const s = _safe(); s.y0 = Math.max(s.y0, bar.getBoundingClientRect().bottom + 8); s.y1 = Math.max(s.y0 + 24, innerHeight - 8); return s; }; }
```

## TEST

1. `cd /home/user/estate/kuiper-belt && python3 -m http.server 8104 --bind 127.0.0.1 &`
2. Copy the harness `04-touch-harness.cjs` (kept beside this file) next to two copies of the page,
   `index.orig.html` (Edition 4 as is) and `index.html` (with this patch applied), and run
   `node touch.cjs before "Pixel 7"` then `node touch.cjs after "Pixel 7"` (and `after "Galaxy S24"`). Each run
   launches Chromium with `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`,
   `browser.newContext({...devices['Pixel 7']})`, routes `**/editions/202611012027/` to the chosen copy with a probe
   appended before `requestAnimationFrame(frame)` that exposes `cx, cy, zoom, moved, openPanel, card.style.display,
   edSel, edScreen`, waits for `edPlaced.length > 0` plus 7 s, and then, through `context.newCDPSession(page)` and
   `Input.dispatchTouchEvent`:
   - T1 one finger: touchStart at (206, 461), ten touchMoves of (+10, +6), touchEnd; expect camera moved exactly
     100 × 60 px, `pointercancel` 0, `scrollY` 0, `visualViewport.scale` 1.
   - T2 two fingers on the canvas: points (156, 461) and (256, 461) spread by 5 px each per step to 200 px; expect
     zoom ratio 2.000, world point under the centre unchanged, `visualViewport.scale` 1.
   - T2b/T2c the same pinch centred on `#bar`, then on the open LINES panel; expect `visualViewport.scale` to remain
     1 (it reads 5 before the patch). Screenshot.
   - T3 taps at the screen centre after Backspace+settle, each sent with explicit CDP `timestamp`s: a 60 ms tap, a
     900 ms hold, a tap wandering (3,2)→(5,5)→(6,6) in 80 ms, a 30 px drag in 120 ms; expect card open / closed /
     open / closed (before the patch: open / open / closed / closed).
   - T4 two taps 120 ms apart on the canvas and on the EDITION panel (scale stays 1); `page.touchscreen.tap` on
     READOUT and the `pointerup`→`click` interval (≈1 ms).
   - T5 put spark 5 under the LINES button centre via the probe (`cx = b.x − (sx − W/2)/14`, `cy = b.y + (sy − H/2)/14`,
     zoom 14), tap the button: expect panel open and `edSel −1`; put spark 7 under the card's ×, tap ×: expect card
     `none`; tap "details", the quote and the card's padding: card stays; open READOUT, tap the wafer: panel closed,
     no card.
   - T6 open LINES, `page.goBack()`: URL unchanged and panel closed; `edCard(2)` then back: card closed; nothing open
     then back: page left; `edCard(4)` then `keyboard.press('Escape')`: card closed.
   - T7 900 ms press on the canvas and on EDITION: no selection, no card; synthetic `contextmenu` on `#c` and on a
     bar button is `defaultPrevented`.
3. Expected after the patch (Pixel 7): every verdict `ok`, `console_errors []`; see the JSON quoted in FINDINGS.

## LIMITS

- Headless Chromium with mobile emulation does not synthesize the Android long-press context menu or the double-tap
  zoom gesture from raw touch points, so items 6 and 7 are shown by computed styles and `defaultPrevented`, not by a
  menu or a zoom seen on screen; the page-zoom from a pinch (item 1) is real and measured.
- SwiftShader on a machine shared by ten auditors makes a frame take seconds, and CDP waits for each touch event to
  be handled, so a tap sent with wall-clock sleeps can arrive as a 2–35 s press. The 700 ms bound reads the events'
  own timestamps (`e.timeStamp`), which on a phone are the input pipeline's and not the main thread's; the harness
  therefore passes explicit `timestamp` values to `Input.dispatchTouchEvent` in T3 (and waits for two short frames
  first). Without them the jittered tap was rejected on time, not on distance, in one run; with them it passes.
- `maximum-scale=1,user-scalable=no` is flagged by Lighthouse as an accessibility smell; the wafer has its own pinch
  zoom and the layers are text that Android's font scaling still enlarges. Remove the two tokens if the owner objects;
  `touch-action:pan-x pan-y` alone already blocks pinch and double-tap zoom on Android Chrome (T2b/T2c pass either
  way in the emulator, where the two mechanisms cannot be told apart).
- The history entry is reconciled on redraw. Closing a layer and reopening another within the few milliseconds before
  the `popstate` from `history.back()` arrives would close the new one; not reproducible by hand.
- Not in this patch (other dimensions): the spark hit radius is 9 CSS px (`bd = 81`), small for a finger; the × is
  26 px; the bar wrapping; `100vh` versus `dvh`; the desktop `wheel` listener is passive so Ctrl+wheel page-zooms on a
  laptop (not Android).
- Tested devices: Pixel 7 portrait and Galaxy S24 portrait; landscape not run.
