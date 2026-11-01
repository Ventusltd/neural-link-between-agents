# NL-009 round 1 — FABLE-03 — dimension "camera": edFly, zoom 14, spark hit-testing on Android

Audited page: `/home/user/estate/kuiper-belt/editions/202611012027/index.html` (Edition 4, kuiper-belt main
018b46aed50f28f7b1882a0dcaba6593ce522beb). Served from the kuiper-belt root on port 8103; Playwright Chromium with
`--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`; contexts `devices['Pixel 7']`
(412×839 CSS px, dpr 2.625, touch), `devices['Pixel 7 landscape']` (863×360) and a 393×851 @2.75 viewport (the owner's
393 px width). Real touch only: `page.touchscreen.tap` and CDP `Input.dispatchTouchEvent` for drags. All rectangles below
are `getBoundingClientRect` values in CSS px; spark positions are the page's own `edScreen(edPlaced[edSel])`; "band" is
the clear space between the lowest obstacle at the top (bar, open panel) and the card's top. The page is a
`<script type="module">`, so the measuring script reaches its state through a one-line hook appended to the served
copy (`window.__ev = s => eval(s)`), never written into the repository. Zero console errors in every run, before and
after the patch.

## FINDINGS

1. **MAJOR — the spark's touch target is 9 px; a touch 15 px off the spark replaces the card with an engine record while
   the pink ring stays on the spark.** Pixel 7 portrait, baseline, after a pick (spark at (206, 395)): a real touch at
   (221, 395), 15 px right of the spark, left `edSel` unchanged (0 → 0) and set the card to
   `key 36,064,774,006 was never issued · silence of 63.0 thousand keys before…` (the engine's own tap handler,
   `show(address(k))`, runs on every wafer tap). Same at 22 px (`key 36,064,805,652 was never issued`). Only the exact
   tap (0 px) opened the line. The spark is a 2.6–3.2 px dot; 9 px CSS at Pixel 7's 0.17 mm/px is a 1.6 mm radius, a
   fifth of Android's 48 dp (8 mm) target. After the patch the reach is 24 px for a touch (48 px = 48 dp diameter) and
   9 px for a mouse, resolved to the nearest spark: the touches at 15 px and 22 px keep the line (`edSel` 2 → 2, card
   still "One Earth radius for the whole estate… 3 of 344") in portrait and in landscape. Nearest-spark resolution is
   never ambiguous: at zoom 14 the nearest other spark is at least 1,413.7 px away (see 6). The ring is drawn: the
   overlay pixel 14 px right of the selected spark is rgba(255,43,214,·) before and after.

2. **MAJOR — NEXT / PREVIOUS inside the LINES panel leaves the panel open and flies the spark under it.** Baseline,
   Pixel 7 portrait: LINES panel rect 0–396 × 77–597 (520 px, 62 vh) stays open; the spark lands at (206, 370), i.e.
   under the panel; band left under the panel 597–671 = 73 px. Landscape: panel 48–264, spark at (431.5, 147), under
   it. The engine's `safeBox` knows `#top`, `#hud` and `#foot` but not `#lines`, so `edFly` aimed as if the panel were
   not there. After: `edFly` measures every `.gm-open` panel; if the band left is under 96 px it closes the panel (as
   a LINES row already did) and aims at the band: portrait spark (206, 390) in band 75–705, Δcentre (0, 0); landscape
   (431.5, 147) in 46–248, Δ (0, 0); `openPanel` null in both.

3. **MAJOR (landscape) — a pick with the EDITION panel open squeezes the spark into a 32 px slot.** Baseline landscape:
   panel `#top` bottom 200 (+8 margin = 208), card top 240 → band 32 px; the spark lands at (431.5, 236.4), 4 px above
   the card's top edge, half of its 6 px selected radius under the card. In portrait the same case is survivable
   (panel 77–260, spark at (206, 462) in 260–671). After: the panel is closed when the band is under 96 px (landscape:
   spark (431.5, 142.8) in 46–240, Δ (0, 0)); in portrait the 183 px panel stays open and the spark is centred in the
   411 px band beneath it (Δ (0, 0)).

4. **MINOR — the edition's tap handler does not look at the event target: after a tap on the wafer, a tap on the card
   (or the bar) picks the spark behind it.** The handler keyed only on the engine's `moved < 4 && pts.size === 0`;
   `moved` is reset only by a canvas pointerdown, so after any tap on the wafer a later touch on the card body over a
   spark ran the search. Measured on Pixel 7, baseline: after a real touch on the empty wafer the camera was panned so that spark 7 lay behind the card body, and a real touch on the card at that point changed `edSel` 0 → 7 and flew the camera to it. After: `e.target !== cv` returns early;
   same sequence, `edSel` unchanged (2 → 2). The engine's own handler already requires `drag`, which only a canvas
   pointerdown sets, so this was an edition-layer gap only.

5. **MINOR — a drag is "moved ≥ 4 px of cumulative path", so a finger's wobble loses the tap; and the camera is aimed
   once, from a card height read in the same task as its innerHTML.** A drag that starts on the spark and moves 20 px
   is correctly not a tap before and after (spark follows the finger; `edSel` 0 → 0, card unchanged); a 120 px drag
   picks nothing before and after; a 2 px jitter picks before and after. A six-move 1 px wobble (path 8 px, net 0):
   before, `edSel` −1 → −1, the tap is dropped (the engine's cumulative `moved` is 8 ≥ 4); after, −1 → 0, the line opens. After the patch a tap is one pointer that went down on the canvas and came up within 10 px of that
   point (Android's touch slop is 8 dp) with under 48 px of path, however long it stayed down. For the camera, the
   patch aims from the live band, aims again on the next animation frame (the card is laid out and painted by then;
   it retargets the running tween rather than restarting it), and re-centres through a `ResizeObserver` on the card
   and on `resize` when the spark would leave the band (details toggle growing a long quote, a turned phone — after a
   pick `atHome` is false so the engine does not re-fit on rotation). Measured: the plain pick was centred within 3 px
   before (asymmetric margins: Δ (0, −3) on every pick) and at Δ (0, 0) after, portrait and landscape; details open on
   Pixel 7 grows the card 111 → 278–285 px (the 34 vh cap) and the spark at y 373–395 stays clear in both versions, so
   the keeper does not move the camera there; rotation is covered by the reviewer script (step 8).

6. **MINOR — zoom 14 on a 393 px screen: the spark is unambiguous, the context is gone, and that is the engine's own
   reading scale; no change.** At zoom 14 the screen is 28.1 key spacings wide (29.4 at 412 px). Over all 344 sparks
   the nearest other spark at zoom 14 is at least 1,413.7 px away (101 key spacings; mean 76,477 px); 0 sparks have a
   neighbour within 24 px, so exactly 1 spark is in view after every pick and the 24 px hit test can never pick the
   wrong one. The other sparks would not come into view before zoom ≈ 0.3 (where the nearest pair is 30 px apart and
   the spark is a dot in the disc), so lowering the zoom buys no context; `goKey` (the **r** key) reads at 14 too. The
   context belongs to the card's "n of 344" and the LINES panel, not to the camera. 393 px pick: spark (196.5, 404.4) in band 75–734 (card 111 px), Δ (0, 0); second pick (196.5, 370.3) with a 179 px card, Δ (0, 0); touches at 15 and 22 px keep the line.

7. **MINOR — the fly is a fixed 900 ms; under SwiftShader it rendered 3–7 frames.** Baseline Pixel 7 portrait, box
   otherwise quiet: home → zoom 14 fly: 7 rAF callbacks in 2,244 ms, mean frame 374 ms, max 833 ms; the next pick
   (zoom 14 → 14): 26 frames, median 16.7 ms, one 1,417 ms stall. Later runs were taken with ten auditors' browsers on
   this 4-core box (load average 59–64): patched fly 1: 14 frames, median 16.7 ms, max 1,183 ms; fly 2: 56 frames,
   median 16.7 ms, max 233 ms; landscape fly 2 once stalled 5.8 s. The pattern is one heavy frame at the zoom
   crossing from home (< 1, the field shader) to 14 (per-line points, up to `MAX_CALLS` = 3,000 draw calls) and
   16.7 ms frames once there. For a mid-range Android (Adreno 6xx class) the 412×839 shader is cheap, but 3,000 draw
   calls a frame is 20–40 ms of CPU, so expect 25–50 fps during the fly and a one-off stall of a few hundred ms on the
   first pick; UNVERIFIED on hardware. The patch does not touch the engine's draw; it shortens the fly for short hops
   (300–900 ms by screen distance and zoom ratio, so an **e → e** step at the same zoom is ~300–400 ms of heavy
   redraw instead of 900) and honours `prefers-reduced-motion: reduce` (instant).

8. **INFO — observations outside this dimension, for the other auditors.** The bar is 75 px (two rows) at 412 px and
   46 px in landscape, which is what the camera measures; the overlay canvas is sized in CSS px (`ov.width =
   innerWidth`), so the sparks and the ring are drawn at 1× and upscaled 2.6× on Pixel 7 (soft edges); in landscape
   the LINES panel is 216 px (60 vh) and rows beyond the third are scrolled out of reach (my row-tap step hit the card
   instead — a test artefact noted in LIMITS); the engine card for a tap on empty wafer ("key … was never issued")
   replaces the edition card while `edSel` keeps the ring, which is the card dimension's call.

Status after the patch (Pixel 7 portrait and landscape): 1 PASS, 2 PASS, 3 PASS, 4 PASS, 5 PASS (wobble: before FAIL, after PASS), 6 PASS (no change
needed), 7 UNVERIFIED on hardware (SwiftShader only), 8 not in scope.

## PATCH

Unified diff against `editions/202611012027/index.html`, to be applied to the Edition 5 copy of the page. Produced with
`diff -u` from copies in `/tmp/nl009/03/`; verified to apply with `patch -p0` from the kuiper-belt root (and with
`git apply`); `node --check` of the extracted module script passes; zero console errors on load. It touches only `edFly`
(replaced by `edBand`/`edAim`/`edFly`/`edKeep`) and the edition's `pointerup` hit test (plus a `pointerdown`/`pointercancel`
bookkeeping pair). No change to keys.json, cosmos, the placement law, the engine's own handlers, the card or the panels'
markup. One behavioural note for the integrator: a pick now closes an open panel **only** when the band it leaves is
under 96 px (the 62 vh LINES/EDITION panels on a phone, any panel in landscape); the 183 px EDITION panel in portrait
stays open. If the panels auditor decides every pick closes every panel, delete the `ED_MINBAND` condition.

```diff
--- editions/202611012027/index.html
+++ editions/202611012027/index.html
@@ -672,20 +672,53 @@
   if (e.target.closest('a')) { e.stopPropagation(); return; }
   e.stopPropagation();                                           // a tap on the card body keeps it open
 }, true);
-// fly so that the spark lands in the clear space: under the bar, above the card
+// fly so that the spark lands in the clear band: under the bar and any open panel, above the card. The band is
+// measured from the live rectangles, measured again on the next frame (the card has been laid out and painted by
+// then) and whenever the card changes height (details, a long quote, a turned phone), so the spark never ends under
+// the card or the bar. A panel that would cover the band is closed by the pick, as a LINES row already does.
+const ED_Z = 14, ED_MARGIN = 8, ED_MINBAND = 96;
+function edBand(){
+  const s = safeBox(); let top = s.y0, bot = innerHeight - ED_MARGIN;
+  for (const el of document.querySelectorAll('.gm-open')) { const r = el.getBoundingClientRect(); if (r.height > 0 && r.top < innerHeight/2) top = Math.max(top, r.bottom + ED_MARGIN); }
+  if (card.style.display === 'block') { const r = card.getBoundingClientRect(); if (r.height > 0) bot = Math.min(bot, r.top - ED_MARGIN); }
+  if (bot < top + 24) bot = top + 24;
+  return { x0:s.x0, x1:s.x1, y0:top, y1:bot };
+}
+function edAim(b, z){ const a = edBand(), mx = (a.x0 + a.x1)/2, my = (a.y0 + a.y1)/2;
+  return { x:b.x - (mx - innerWidth/2)/z, y:b.y + (my - innerHeight/2)/z, z }; }
+let edFlown = null;
 function edFly(b){
-  const z = 14, s = safeBox(); const cardH = card.style.display === 'block' ? card.getBoundingClientRect().height + 12 : 0;
-  const mx = (s.x0 + s.x1)/2, my = (s.y0 + Math.max(s.y0 + 40, s.y1 - cardH))/2;
-  atHome = false; flyTo(b.x - (mx - innerWidth/2)/z, b.y + (my - innerHeight/2)/z, z);
+  const g = edBand(); if (openPanel && g.y1 - g.y0 < ED_MINBAND) setPanel(openPanel);
+  const z = ED_Z, [sx, sy] = edScreen(b), far = Math.hypot(sx - innerWidth/2, sy - innerHeight/2) + Math.abs(Math.log2(z/zoom))*120;
+  const t = edAim(b, z); atHome = false; edFlown = b; flyTo(t.x, t.y, z);
+  tween.dur = matchMedia('(prefers-reduced-motion: reduce)').matches ? 1 : Math.max(300, Math.min(900, 300 + far*0.6));   // a short hop is quick, home to spark takes the full 900 ms
+  requestAnimationFrame(() => { if (edFlown !== b || !tween) return; const u = edAim(b, z); tween.x1 = u.x; tween.y1 = u.y; });   // aim again once the card is laid out
 }
+// the card grew or shrank, or the phone was turned, after the fly: keep the spark inside the band
+function edKeep(){ if (tween || edSel < 0 || !edFlown || card.style.display !== 'block' || document.querySelector('.gm-open')) return;
+  const b = edPlaced[edSel]; if (!b) return; const a = edBand(), [sx, sy] = edScreen(b);
+  if (sx >= a.x0 + 12 && sx <= a.x1 - 12 && sy >= a.y0 + 12 && sy <= a.y1 - 12) return;
+  const t = edAim(b, zoom); flyTo(t.x, t.y, zoom); tween.dur = 350; }
+if (typeof ResizeObserver === 'function') new ResizeObserver(() => edKeep()).observe(card);
+addEventListener('resize', () => requestAnimationFrame(edKeep));
 function esc(v){ return String(v == null ? '' : v).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
 function edNext(step){ if (!edPlaced.length) return; edSel = (edSel + step + edPlaced.length) % edPlaced.length;
   const b = edPlaced[edSel]; edCard(edSel); edFly(b); }
-// a tap within 9 px of a spark opens that line (runs after the engine's own tap handler)
+// a tap on the wafer opens the nearest spark within reach: 24 px for a finger (Android's touch target), 9 px for a
+// mouse. A tap is one pointer that went down on the canvas and came up within 10 px of where it went down, however
+// long it stayed (a finger's wobble is not a drag, a slow press is still a tap); a drag, a pinch, or a tap on the
+// bar, the card or a panel never picks a spark, and sparks of a layer that is switched off are not hit. Runs after
+// the engine's own tap handler.
+const ED_TAP_TOUCH = 24, ED_TAP_MOUSE = 9, ED_SLOP = 10;
+let edDown = null;
+cv.addEventListener('pointerdown', e => { edDown = pts.size === 1 ? { id:e.pointerId, x:e.clientX, y:e.clientY } : null; });
+addEventListener('pointercancel', () => { edDown = null; });
 addEventListener('pointerup', e => {
-  if (!edPlaced.length || moved >= 4 || pts.size > 0) return;
-  let best = -1, bd = 81;
-  for (let i = 0; i < edPlaced.length; i++) { const [x, y] = edScreen(edPlaced[i]); const d = (x - e.clientX)**2 + (y - e.clientY)**2; if (d < bd) { bd = d; best = i; } }
+  const d = edDown; edDown = null;
+  if (!d || d.id !== e.pointerId || e.target !== cv || !edPlaced.length || pts.size > 0 || moved >= 48) return;
+  if (Math.hypot(e.clientX - d.x, e.clientY - d.y) > ED_SLOP) return;
+  const R = e.pointerType === 'mouse' ? ED_TAP_MOUSE : ED_TAP_TOUCH; let best = -1, bd = R*R;
+  for (let i = 0; i < edPlaced.length; i++) { if (!visibleLine(edPlaced[i])) continue; const [x, y] = edScreen(edPlaced[i]); const q = (x - e.clientX)**2 + (y - e.clientY)**2; if (q < bd) { bd = q; best = i; } }
   if (best >= 0) { edCard(best); edFly(edPlaced[best]); }
 });
 addEventListener('keydown', e => { if (gbox.style.display === 'block') return;
```

## TEST

Serve the Edition 5 folder from the kuiper-belt root (`python3 -m http.server 8103 --bind 127.0.0.1`), save the script
below as `verify.cjs` outside the repository, and run `node verify.cjs http://127.0.0.1:8103/editions/<stamp>/ "Pixel 7"`
(then again with `"Pixel 7 landscape"`). Every line must start with PASS. Allow ~6 minutes under SwiftShader on a quiet
machine; the page's state is read through the same test-only `__ev` hook described above.

Expected on Edition 4 (before): step 3 FAIL (card text is the engine record), step 5 FAIL after a wafer tap, step 6
PASS in portrait but FAIL in landscape, step 7 FAIL (panel still open, `ok:false`), step 9 FAIL. Expected after: all PASS.

Measured output of this script against the patched page on Pixel 7 (this machine, loaded):

```
PASS 1 pick: spark in band {"W":412,"H":839,"edSel":0,"x":206,"y":398,"barB":75,"cardT":722,"panel":null,"top":75,"bot":722,"ok":true,"dy":0,"text":"×Bytes on d …
PASS 2 details open: spark still in band {"W":412,"H":839,"edSel":0,"x":206,"y":398,"barB":75,"cardT":555,"panel":null,"top":75,"bot":555,"ok":true,"dy":83,"tex …
PASS 3 tap 20 px off the spark keeps the line {"W":412,"H":839,"edSel":0,"x":206,"y":398,"barB":75,"cardT":722,"panel":null,"top":75,"bot":722,"ok":true,"dy":0, …
PASS 4 drag of 20 px is not a tap (no fly back to centre) {"W":412,"H":839,"edSel":0,"x":226,"y":401,"barB":75,"cardT":722,"panel":null,"top":75,"bot":722,"ok": …
PASS 5 tap on the card does not pick the spark behind it {"sel":0,"behind":7}
PASS 6 pick with a panel open: spark in the band left {"W":412,"H":839,"edSel":1,"x":206,"y":465,"barB":75,"cardT":671,"panel":"top","top":260,"bot":671,"ok":tr …
PASS 7 NEXT in LINES: panel closed, spark in band {"W":412,"H":839,"edSel":2,"x":206,"y":373,"barB":75,"cardT":671,"panel":null,"top":75,"bot":671,"ok":true,"dy …
PASS 8 rotation after a pick keeps the spark in the band {"W":839,"H":412,"edSel":2,"x":420,"y":159,"barB":46,"cardT":281,"panel":null,"top":46,"bot":281,"ok":t …
PASS 9 wobbly finger (path 8 px, net 0) is a tap {"W":412,"H":839,"edSel":2,"x":206,"y":373,"barB":75,"cardT":671,"panel":null,"top":75,"bot":671,"ok":true,"dy" …
PASS 10 no console errors []
```

```js
// NL-009 patch 03 (camera + hit-test) reviewer check. node verify.cjs <url> [device]   e.g. node verify.cjs http://127.0.0.1:8103/editions/<stamp>/ "Pixel 7"
const { chromium, devices } = require('playwright');
const [,, URL, DEV = 'Pixel 7'] = process.argv;
const pass = (name, ok, detail) => console.log((ok ? 'PASS ' : 'FAIL ') + name + ' ' + detail);
(async () => {
  const browser = await chromium.launch({ args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const page = await (await browser.newContext({ ...devices[DEV] })).newPage();
  const errors = []; page.on('pageerror', e => errors.push(e.message)); page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  // the page is a module: reach its scope through a one-line hook appended to the module (test only, never in the page)
  await page.route(u => /\/editions\/[0-9]{12}\/(index\.html)?$/.test(u.pathname), async r => { const b = (await (await r.fetch()).text()); const i = b.lastIndexOf('</script>');
    r.fulfill({ status:200, contentType:'text/html; charset=utf-8', body: b.slice(0, i) + ';window.__ev = s => eval(s);\n' + b.slice(i) }); });
  const ev = (fn, ...a) => page.evaluate(([s, a]) => __ev('(' + s + ')').apply(null, a), [fn.toString(), a]);
  const settle = async (ms) => { await page.waitForFunction(() => typeof __ev === 'function' && !__ev('tween'), null, { timeout:60000 }); await page.waitForTimeout(ms); };
  const probe = () => ev(() => { const W = innerWidth, H = innerHeight, br = document.getElementById('bar').getBoundingClientRect(), cr = card.getBoundingClientRect();
    const op = document.querySelector('.gm-open'), pr = op && op.getBoundingClientRect(); const [x, y] = edSel >= 0 ? edScreen(edPlaced[edSel]) : [NaN, NaN];
    const top = Math.max(br.bottom, pr ? pr.bottom : 0), bot = card.style.display === 'block' ? cr.top : H;
    return { W, H, edSel, x:Math.round(x), y:Math.round(y), barB:Math.round(br.bottom), cardT:Math.round(cr.top), panel: op ? op.id : null, top:Math.round(top), bot:Math.round(bot),
      ok: x > 6 && x < W - 6 && y > top + 6 && y < bot - 6, dy: Math.round(y - (top + bot)/2), text: card.textContent.replace(/\s+/g, ' ').slice(0, 50) }; });
  await page.goto(URL, { waitUntil:'load', timeout:120000 });
  await page.waitForFunction(() => typeof __ev === 'function' && __ev('N > 0 && edPlaced.length > 0'), null, { timeout:120000 }); await page.waitForTimeout(8000);
  // 1. a pick lands the spark in the band between bar and card, centred
  await page.keyboard.press('e'); await settle(6000); let p = await probe();
  pass('1 pick: spark in band', p.ok && Math.abs(p.dy) <= 4, JSON.stringify(p));
  // 2. details open: card grows, spark is kept in the band
  const ct = await (await page.$('#card .ct')).boundingBox(); await page.touchscreen.tap(ct.x + ct.width/2, ct.y + ct.height/2); await page.waitForTimeout(500); await settle(4000); p = await probe();
  pass('2 details open: spark still in band', p.ok, JSON.stringify(p));
  const ct2 = await (await page.$('#card .ct')).boundingBox(); await page.touchscreen.tap(ct2.x + ct2.width/2, ct2.y + ct2.height/2); await page.waitForTimeout(500); await settle(3000);
  // 3. a touch 20 px from the spark picks it (24 px reach); the card shows the same line
  p = await probe(); const title = await ev(() => edPlaced[edSel].title.slice(0, 20)); const sel = p.edSel;
  await page.touchscreen.tap(p.x + 20, p.y); await page.waitForTimeout(500); await settle(3000); p = await probe();
  pass('3 tap 20 px off the spark keeps the line', p.edSel === sel && p.text.includes(title), JSON.stringify(p));
  // 4. a drag that begins on the spark and moves 20 px is not a tap
  const cdp = await page.context().newCDPSession(page); const s = p;
  await cdp.send('Input.dispatchTouchEvent', { type:'touchStart', touchPoints:[{ x:s.x + 2, y:s.y, id:1 }] });
  for (const d of [8, 14, 22]) { await page.waitForTimeout(40); await cdp.send('Input.dispatchTouchEvent', { type:'touchMove', touchPoints:[{ x:s.x + d, y:s.y + 3, id:1 }] }); }
  await cdp.send('Input.dispatchTouchEvent', { type:'touchEnd', touchPoints:[] }); await page.waitForTimeout(500); await settle(2000); p = await probe();
  pass('4 drag of 20 px is not a tap (no fly back to centre)', p.edSel === sel && p.x !== s.x, JSON.stringify(p));
  // 5. after a tap on the empty wafer, a tap on the card body over a spark behind it does not pick that spark
  await page.touchscreen.tap(p.W*0.8, p.top + 30); await page.waitForTimeout(800); await settle(2000);
  const r = await ev(() => { const cr = card.getBoundingClientRect(), px = cr.left + cr.width/2, py = cr.top + cr.height*0.6, j = (edSel + 7) % edPlaced.length, b = edPlaced[j];
    tween = null; cx = b.x - (px - innerWidth/2)/zoom; cy = b.y + (py - innerHeight/2)/zoom; dirty = true; return { j, px, py }; });
  await page.waitForTimeout(2500); await page.touchscreen.tap(r.px, r.py); await page.waitForTimeout(500); await settle(2000); p = await probe();
  pass('5 tap on the card does not pick the spark behind it', p.edSel !== r.j, JSON.stringify({ sel:p.edSel, behind:r.j }));
  // 6. EDITION panel open, then a pick: the spark is in the band left (the panel is closed only if it would cover it)
  const bb = await (await page.$('#bar [data-panel=top]')).boundingBox(); await page.touchscreen.tap(bb.x + bb.width/2, bb.y + bb.height/2); await page.waitForTimeout(400);
  await page.keyboard.press('e'); await settle(5000); p = await probe();
  pass('6 pick with a panel open: spark in the band left', p.ok, JSON.stringify(p));
  // 7. NEXT inside LINES: same
  const lb = await (await page.$('#bar [data-panel=lines]')).boundingBox(); await page.touchscreen.tap(lb.x + lb.width/2, lb.y + lb.height/2); await page.waitForTimeout(400);
  const nb = await (await page.$('#lines button[data-k="e"]')).boundingBox(); await page.touchscreen.tap(nb.x + nb.width/2, nb.y + nb.height/2); await settle(5000); p = await probe();
  pass('7 NEXT in LINES: panel closed, spark in band', p.panel === null && p.ok, JSON.stringify(p));
  // 8. turning the phone after a pick: the spark is re-centred in the new band
  const vp = page.viewportSize(); await page.setViewportSize({ width:vp.height, height:vp.width }); await page.waitForTimeout(1500); await settle(4000); p = await probe();
  pass('8 rotation after a pick keeps the spark in the band', p.ok, JSON.stringify(p));
  await page.setViewportSize(vp); await page.waitForTimeout(1500); await settle(4000);
  // 9. a wobbly finger (six 1-px moves, net 0) is a tap
  p = await probe(); await ev(() => { card.style.display = 'none'; edSel = -1; dirty = true; });
  await cdp.send('Input.dispatchTouchEvent', { type:'touchStart', touchPoints:[{ x:p.x, y:p.y, id:1 }] });
  for (const [dx, dy] of [[1,0],[2,1],[2,2],[1,2],[0,1],[0,0]]) { await page.waitForTimeout(30); await cdp.send('Input.dispatchTouchEvent', { type:'touchMove', touchPoints:[{ x:p.x + dx, y:p.y + dy, id:1 }] }); }
  await cdp.send('Input.dispatchTouchEvent', { type:'touchEnd', touchPoints:[] }); await page.waitForTimeout(500); await settle(3000); p = await probe();
  pass('9 wobbly finger (path 8 px, net 0) is a tap', p.edSel >= 0, JSON.stringify(p));
  pass('10 no console errors', errors.length === 0, JSON.stringify(errors));
  await browser.close();
})().catch(e => { console.error('FAILED', e); process.exit(1); });
```

## LIMITS

- All timing was taken under SwiftShader on a 4-core box shared by the ten auditors (load average 59–64 during most
  runs); the frame numbers in finding 7 are indicative of where the heavy frames are, not of Android frame rates.
  Two of my Chromium instances run concurrently crashed each other, so every run here is sequential.
- Galaxy S24 (360 px) was not run for want of machine time; the geometry in finding 6 is independent of width (25.7
  keys across at 360 px) and the band arithmetic is the same code path. The 393 px viewport was run for the pick only.
- The landscape "row in LINES" step is a test artefact: row 3 is scrolled below the 216 px panel and my tap landed on
  the card. The panel's reach in landscape is for the panels auditor.
- The rotation keeper (`edKeep` on `resize`) is exercised by `verify.cjs` step 9 (viewport swap), not by a device
  orientation event; Android's dynamic toolbar resize is covered by the same path but was not simulated.
- The engine's tap handler still shows its own record for a touch more than 24 px from any spark; whether the edition
  card should then drop the ring (`edSel = -1`) is the card auditor's decision, not changed here.
- Housekeeping incident: at about 21:08 UTC a `pkill -f "node measure"` of mine matched FABLE-08's measurement
  process (`/tmp/nl009/08`, same machine) and killed it; it restarted shortly after, but FABLE-08's patched Pixel 7
  run from around that time may have been cut short and should be checked.
- Scratch material (scripts, raw JSON probes, all screenshots): `/tmp/nl009/03/` (`measure.cjs`, `verify.cjs`,
  `out-*.json`, `out-*.png`); not in any repository.
