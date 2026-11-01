# NL-009 round 1 — 01-bar: the menu bar on Android phones

Auditor FABLE-01, dimension "bar" (`#bar`, `#barname`, `.gm-title`). Page audited: `editions/202611012027/index.html`
(Edition 4, kuiper-belt main 018b46aed50f28f7b1882a0dcaba6593ce522beb), served from the repository root on port 8101,
Playwright 1.63 Chromium (SwiftShader), devices Pixel 7 (412×839, dpr 2.625), Pixel 5 (393×727), Galaxy S24 (360×780),
Pixel 7 at 430×932, Pixel 7 landscape (863×360), Galaxy S24 landscape (780×360); all with `hasTouch`, `isMobile`,
`(pointer:coarse)` true. Numbers are `getBoundingClientRect` / `getComputedStyle` after a 7 s settle. The container's
monospace is DejaVu Sans Mono (advance 0.602 em); Android's `monospace` is Droid Sans Mono (0.600 em), so the widths
transfer within 0.5 %. Scripts: `/tmp/nl009/01/measure.cjs`, `hover.cjs`, `fly.cjs` (scratch, not committed).

## FINDINGS

1. **BLOCKER — the bar is two rows on every phone width.** Bar height 75.1 px at 360, 393, 412 and 430 px; button
   rows at y = 6 and y = 39 (COMMANDS alone on row 2). Content: title "KUIPER EDITION 4" 130.6 px + margin 8 +
   buttons 70.5 + 70.5 + 55.5 + 78 px + 3 gaps × 4 = 416.6 px, against 344–414 px available (width − 16 px padding).
   A fifth button at the same style (SEE THROUGH, 11 characters × 7.5 px + 18 = 100.5 px) would need 521 px.
   Landscape (780 and 863 px) is one row, 45.6 px.
2. **MAJOR — titles are below the touch target.** Button height 29.0 px in portrait (5 + 17.05 line + 5 + 2 border)
   and 32.6 px in landscape, against 44 px (iOS) / 48 dp (Android); the whole bar row is only 75 px because it wraps.
3. **MAJOR — there is no room for SEE THROUGH at the present style.** At 11 px, letter-spacing .08 em, padding 8 px:
   the five labels (38 characters × 7.5 px = 285) + 5 × 18 px chrome + 4 gaps × 4 = 391 px of buttons alone, more
   than the 344 px a 360 px phone has even with no title at all. Even at 11 px with letter-spacing .02 em and
   padding 5 px the row (260 + 50 + 10 + 15 gaps + 24.5 mark + 12 bar padding) is 371.5 px > 360. Therefore the
   label size must follow the width (10 px at 360): the alternative, an overflow "more", would hide exactly the
   button the owner asked for; icons add width, they do not save it. Measured after the patch: the row needs
   347.9 px at 360 (slack 12.1 px), and the size is back at 10.8 px by 393, 11.3 px by 412, 11.8 px by 430.
4. **MINOR — the lit look sticks after a touch tap.** `(hover:hover)` is false on Pixel 7, yet `#bar .gm-title:hover`
   applies after `touchscreen.tap`: after tap-open then tap-close, COMMANDS has `gm-on` false but background
   rgba(80,220,240,.16) and colour #fff, i.e. it still looks open.
5. **MINOR — no safe-area insets on the bar.** The page declares `viewport-fit=cover` but `#bar` pads a flat 8 px;
   on a cutout phone in landscape (or Android 15 edge-to-edge) the first title can sit under the cutout. Playwright
   reports `env(safe-area-inset-*)` as 0, so this is by inspection, not by measurement.
6. **MINOR — dynamic toolbar (100vh vs dvh), measured, not patched here.** The bar is `position:fixed; top:0`, so
   Chrome's retracting toolbar does not move it. `vh` is used only as maxima: `#card` 34vh = 285.3 px and the panels
   62vh = 520.2 px at innerHeight 839; with the 56 dp toolbar showing the real viewport is 783 px, so 62vh overstates
   by 35 px, but the panels are top-anchored at 53 px (53 + 520 = 573 < 783) and the card is bottom-anchored, so
   nothing is clipped. Recommendation for the panels/card patch: `@supports (height:1dvh){...max-height:62dvh}`.
7. **PASS — safeBox and placePanels follow the bar.** Before: bar bottom 75.1 → `safeBox().y0` 83.1 (= bottom + 8),
   panel tops 77.1 px (= height + 2). After the patch: bar 51 → y0 59, tops 53; with a 1.3× font scale the bar wraps
   to 98 px → y0 106, tops 100. Opening EDITION by touch: panel top 53.0 ≥ bar bottom 51.0. After `e` the selected
   spark lands at y = 383.4 on Pixel 7 (bar 51, card top 721.8) and y = 149.3 in landscape (card top 247.6).

Status after the patch: F1 PASS (rows [3] at 360/393/412/430, bar 51 px, last button right edge 341.9/360.8/373.3/384.8
leaving 12.1/26.2/32.7/39.2 px), F2 PASS (every title 44.0 px tall on all six viewports), F3 PASS (SEE THROUGH present,
80.4 px wide at 360, 89.5 at 412, 112 at 863), F4 PASS (after tap-close: background transparent, colour #8fb3bd),
F5 UNVERIFIED in emulation (the CSS parses: computed padding 3px 6px with env() = 0), F6 not in this patch, F7 PASS.
Zero console errors and zero page errors on every run; `node --check` of the extracted module passes.

Design: one phone rule at ≤ 640 px: `#bar{font-size:clamp(10px,2.75vw,12px); gap:3px; padding 6px sides}`,
`.gm-title{padding:0 5px; letter-spacing:.02em; flex:0 0 auto}`, title shrinks to the mark `KE4` (the full name stays
in the EDITION layer and in `title`/`aria-label`); one touch rule `(pointer:coarse)`: `min-height:44px` titles and
3 px bar padding, so the row is 51 px in portrait and landscape alike (was 75.1 / 45.6); hover only under
`(hover:hover)`; `env(safe-area-inset-*)` on the bar's padding. Titles never shrink, so a large system font scale
wraps the bar (measured at 1.3×: two rows, 98 px) and the panels and the camera follow the measured height.

## PATCH

Against `editions/202611012027/index.html`; applies with `patch -p1 < 01-bar.diff` from the kuiper-belt root and with
`git apply --check` (both verified on a copy; the result is byte-identical to the tested file,
sha256 e911f59a840f516ee12d58280b5196595e4c1a8e73d32d40d3e26efb8cd7907b). The fifth title is
`<button class="gm-title" data-app="see-through">see through</button>`; the bar's click handler now only toggles
titles that carry `data-panel`, so this button does nothing until FABLE-06 gives it its action (an
`<a class="gm-title" href="../../see-through/">` renders identically: inline-flex, no underline, nowrap). The width
budget assumes the label SEE THROUGH (11 characters); the mark `KE4` and the title become `KE5` / `KUIPER EDITION 5`.

```diff
--- a/editions/202611012027/index.html
+++ b/editions/202611012027/index.html
@@ -55,12 +55,19 @@
     #goto{min-width:0;left:8px;right:8px;transform:none;top:30%}
   }
   /* EDITION 3: the bar is the only thing on screen at rest; every panel is a layer under it */
-  #bar{position:fixed;top:0;left:0;right:0;z-index:12;display:flex;gap:4px;align-items:center;padding:6px 8px;
+  #bar{position:fixed;top:0;left:0;right:0;z-index:12;display:flex;gap:4px;align-items:center;
+    padding:calc(6px + env(safe-area-inset-top,0px)) calc(8px + env(safe-area-inset-right,0px)) 6px calc(8px + env(safe-area-inset-left,0px));
     background:#090c13e6;border-bottom:1px solid #12414a;overflow-x:auto;white-space:nowrap}
   #barname{color:var(--cy);letter-spacing:.14em;font-size:12px;margin-right:8px;text-transform:uppercase}
-  #bar .gm-title{appearance:none;border:1px solid #12414a;background:transparent;color:#8fb3bd;font:inherit;
+  #barname .bn-short{display:none}
+  #bar .gm-title{appearance:none;display:inline-flex;align-items:center;justify-content:center;flex:0 0 auto;border:1px solid #12414a;
+    background:transparent;color:#8fb3bd;font:inherit;line-height:1.3;text-decoration:none;white-space:nowrap;
     text-transform:uppercase;letter-spacing:.08em;padding:6px 10px;cursor:pointer;touch-action:manipulation}
-  #bar .gm-title:hover,#bar .gm-title.gm-on{background:rgba(80,220,240,.16);color:#fff;border-color:var(--cy)}
+  #bar .gm-title.gm-on{background:rgba(80,220,240,.16);color:#fff;border-color:var(--cy)}
+  @media (hover:hover){ #bar .gm-title:hover{background:rgba(80,220,240,.16);color:#fff;border-color:var(--cy)} }
+  /* NL-009 01-bar: on a touch screen every title is a 44 px target (Android 48 dp, iOS 44 pt; the bar's
+     3 px padding brings the row to 51 px), and the lit look does not stick after a tap (hover:hover). */
+  @media (pointer:coarse){ #bar{padding-top:calc(3px + env(safe-area-inset-top,0px));padding-bottom:3px} #bar .gm-title{min-height:44px} }
   #top,#hud,#foot,#lines{display:none}
   #top.gm-open,#hud.gm-open,#foot.gm-open,#lines.gm-open{display:block}
   #top,#hud,#foot,#lines{position:fixed;top:40px;left:0;right:auto;bottom:auto;max-width:min(680px,96vw);max-height:60vh;overflow:auto;
@@ -80,7 +87,15 @@
   #card.open .cd{display:block}
   #card .ct{color:var(--cy);cursor:pointer;text-decoration:underline dotted}
   @media (max-width:640px){ #card{left:6px;right:6px;bottom:6px!important;max-height:34vh;font-size:11px} }
-  @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{font-size:11px;margin-right:4px} #bar .gm-title{padding:5px 8px}
+  /* NL-009 01-bar: ONE row on a phone. Measured at 11 px the five titles EDITION READOUT LINES COMMANDS SEE THROUGH
+     (38 characters of 0.6 em monospace) need 372 px with a 3-character mark, more than a 360 px screen, so the size
+     follows the width: clamp(10px, 2.75vw, 12px) is 10 px at 360, 10.8 at 393, 11.3 at 412, 11.8 at 430. The title
+     shrinks to the mark KE4 (the EDITION layer carries the full name). Titles never shrink (flex 0 0 auto); if the
+     system font scale is large the bar wraps rather than clips, and placePanels and safeBox measure the real height. */
+  @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible;gap:3px;font-size:clamp(10px,2.75vw,12px);
+      padding-left:calc(6px + env(safe-area-inset-left,0px));padding-right:calc(6px + env(safe-area-inset-right,0px))}
+    #barname{font-size:11px;margin-right:0} #barname .bn-long{display:none} #barname .bn-short{display:inline}
+    #bar .gm-title{padding:0 5px;letter-spacing:.02em}
     #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);left:0;right:0;max-width:none;max-height:62vh} #hud{text-align:left} }
 </style>
 </head>
@@ -696,11 +711,12 @@
 // hidden until its title is tapped, one open at a time, closed by the same tap, by Escape, or by a tap on the
 // wafer. The wafer gets the whole screen; the readout, the commands and the edition's own text are layers.
 const bar = document.createElement('div'); bar.id = 'bar';
-bar.innerHTML = '<span id="barname">KUIPER EDITION 4</span>'
+bar.innerHTML = '<span id="barname" title="Kuiper Edition 4"><span class="bn-long">KUIPER EDITION 4</span><span class="bn-short" aria-label="Kuiper Edition 4">KE4</span></span>'
   + '<button class="gm-title" data-panel="top">edition</button>'
   + '<button class="gm-title" data-panel="hud">readout</button>'
   + '<button class="gm-title" data-panel="lines">lines</button>'
-  + '<button class="gm-title" data-panel="foot">commands</button>';
+  + '<button class="gm-title" data-panel="foot">commands</button>'
+  + '<button class="gm-title" data-app="see-through">see through</button>';   // the fifth title: FABLE-06 gives it its action, the bar gives it its room
 document.body.appendChild(bar);
 const linesPanel = document.createElement('div'); linesPanel.id = 'lines'; linesPanel.className = 'gm-panel';
 linesPanel.innerHTML = '<div id="linesctl"><label><input type="checkbox" id="lyAll" checked> verified lines layer</label>'
@@ -718,7 +734,7 @@
   if (openPanel === 'lines') fillLines();
   dirty = true;
 }
-bar.addEventListener('click', e => { const b = e.target.closest('.gm-title'); if (b) { e.stopPropagation(); setPanel(b.dataset.panel); } });
+bar.addEventListener('click', e => { const b = e.target.closest('.gm-title[data-panel]'); if (b) { e.stopPropagation(); setPanel(b.dataset.panel); } });
 addEventListener('keydown', e => { if (e.key === 'Escape' && openPanel) setPanel(openPanel); });
 cv.addEventListener('pointerdown', () => { if (openPanel) setPanel(openPanel); });
 elTop.classList.add('open');                                   // the long subtitle is readable once the panel is open
```

## TEST

1. `cd /home/user/estate/kuiper-belt && python3 -m http.server 8101 --bind 127.0.0.1 &` (Edition 5 folder in place of
   202611012027 below).
2. Run this with `node` (Playwright pre-installed), once per device in `['Pixel 7','Galaxy S24','Pixel 7 landscape']`:

```js
const { chromium, devices } = require('playwright');
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  for (const dn of ['Pixel 7', 'Galaxy S24', 'Pixel 7 landscape']) {
    const page = await (await browser.newContext(devices[dn])).newPage();
    const errors = []; page.on('pageerror', e => errors.push(e.message)); page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await page.goto('http://127.0.0.1:8101/editions/202611012027/', { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(7000);
    const m = await page.evaluate(() => { const bar = document.getElementById('bar'); const bs = [...bar.querySelectorAll('.gm-title')].map(b => b.getBoundingClientRect());
      return { w: innerWidth, barH: bar.getBoundingClientRect().height, rows: [...new Set(bs.map(r => Math.round(r.top)))].length, n: bs.length,
        minBtnH: Math.min(...bs.map(r => r.height)), lastRight: bs[bs.length - 1].right, title: document.getElementById('barname').innerText,
        font: getComputedStyle(bs.length ? bar.querySelector('.gm-title') : bar).fontSize }; });
    const c = await page.evaluate(() => { const b = document.querySelector('#bar .gm-title[data-panel="foot"]').getBoundingClientRect(); return [b.x + b.width / 2, b.y + b.height / 2]; });
    await page.touchscreen.tap(c[0], c[1]); await page.waitForTimeout(300);
    const open = await page.evaluate(() => { const p = document.getElementById('foot').getBoundingClientRect(), b = document.getElementById('bar').getBoundingClientRect(); return { shown: getComputedStyle(document.getElementById('foot')).display === 'block', underBar: p.top >= b.bottom }; });
    await page.touchscreen.tap(c[0], c[1]); await page.waitForTimeout(300);
    const after = await page.evaluate(() => getComputedStyle(document.querySelector('#bar .gm-title[data-panel="foot"]')).backgroundColor);
    console.log(dn, JSON.stringify({ ...m, open, afterCloseBg: after, errors }));
  }
  await browser.close();
})();
```

3. Expect, per device: `n` 5, `rows` 1, `barH` 51, `minBtnH` 44, `lastRight` < `w` − 6 (Pixel 7 ≈ 373.3, Galaxy S24
   ≈ 341.9, landscape ≈ 599.5), `title` "KE4" (KE5) on the two portrait phones and "KUIPER EDITION 4" (5) in landscape,
   `font` 11.33px / 10px / 12px, `open` {shown:true, underBar:true}, `afterCloseBg` "rgba(0, 0, 0, 0)", `errors` [].
4. Press `e` (`page.keyboard.press('e')`, wait 7 s) and check the selected spark (magenta ring) sits below the bar
   and above the card in the screenshot; before/after renders are in `img/01-bar-*.png`.

## LIMITS

- `env(safe-area-inset-*)` and Chrome's retracting toolbar cannot be emulated in Playwright; F5 is by inspection and
  F6 by arithmetic on the measured `vh` values. A real Pixel 7 in Chrome confirms both in one look.
- Android's system font scale was emulated by multiplying the bar's font-size by 1.3, not by Chrome's own setting;
  the result (graceful wrap, panels and camera follow) is the behaviour to expect, not a measurement of Chrome's.
- Width budget holds for the monospace fallback Android actually uses (Droid Sans Mono, 0.600 em); a phone with a
  wider user font would wrap, never clip. The budget at 360 px leaves 12.1 px: a sixth title (KUIPER / LEARN as the
  notes offer) does not fit on one row at ≤ 393 px and would need the overflow the brief reserves for that case.
- Not touched: `keys.json`, `cosmos/`, the engine's placement law, the panels' and card's own sizes (F6 is a
  recommendation to those patches), the action of SEE THROUGH (FABLE-06).
