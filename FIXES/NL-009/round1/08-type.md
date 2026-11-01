# NL-009 round 1 · FABLE-08 · type: typography and legibility on Android phones

Page audited: `editions/202611012027/index.html` (Edition 4) at kuiper-belt main 018b46aed50f28f7b1882a0dcaba6593ce522beb.
Emulation: Playwright Chromium (SwiftShader), `devices['Pixel 7']` (412x839 CSS px, dpr 2.625) and a 360x640 phone (dpr 3,
isMobile, hasTouch), real `page.touchscreen.tap` on the bar titles, 8 s settle after load and 7 s after `e`. Script:
`/tmp/nl009/08/measure.cjs` (scratch, not in a repository); raw numbers `/tmp/nl009/08/measure-{orig,patched}-{pixel7,s360}.json`.
Nothing under `/home/user/estate/kuiper-belt` was edited; the patched copy was served from the scratch tree on port 8108.

## FINDINGS

Measured before the patch (Pixel 7 / 360x640, CSS px and device px, screen share, characters per line).

1. **MAJOR · every phone text is 11 CSS px.** `@media (max-width:640px){html,body{font-size:11px}}` and `#card{font-size:11px}`
   put the subtitle, the READOUT, every LINES row, the card body, the quote, the link, the details and every button at 11 px
   = 28.9 device px on the Pixel 7 (33 at dpr 3), about 8 pt, in a thin monospace at 5.4:1 grey. Only `#big` (13 px) is
   larger. Android's own body norm is 14 sp; Chrome's is 16 px. The owner's complaint was room, and the room is words
   (finding 3), not size. Patched: a type scale `--t-body 13px, --t-small 12px, --t-title 14px, --t-bar 11px, --t-ui 12px,
   --lh 1.45` on the phone (desktop keeps 12/11/15/12/12 and 1.55); measured after: body 13 px = 34.1 device px (39 at
   dpr 3), READOUT, details, controls and the law sentence 12 px = 31.5 (36), LINES rows 13 px at line-height 1.35 so a
   row stays 46 px (was 45). Line length after: 42–49 characters on the 360 phone, 47–53 on the Pixel 7 (45–75 is the band).

2. **MAJOR · the COMMANDS panel on a phone shows no text at all.** `#foot .long{display:none}` under 640 px hides the whole
   sentence, so the laws sentence (r = √key, θ = key × golden angle) and "a chart, not a design" are absent on the phone:
   56 characters shown (the five buttons), 0 of the required sentences. Patched: the sentence is split into `.long`
   (the keyboard list, desktop only), `.short` (tap a spark, tap the wafer, drag, pinch; phone only) and `.law` (the law,
   the silence rings, the unresolved pixels, the warranty, "a chart, not a design", the link; always shown). After:
   380 characters on the phone including both required sentences; the panel is 240.7 px (28.7 %) on the Pixel 7 and
   259.5 px (40.6 %) on 360x640, of which the five buttons in two rows are 85 px; it scrolls under the 62 vh cap.
   The desktop keeps every word it had except the opening "KUIPER EDITION 4: the verified lines …", which is the
   EDITION panel's sentence.

3. **MAJOR · the EDITION panel is 88 words / 492 characters.** 182.5 px = 21.8 % of the Pixel 7 screen, 236.8 px = 37 % of
   360x640, at 11 px. The first clause repeats the bar ("Kuiper Edition 4 ·"), the register bookkeeping ("354 keyed
   findings, 495 keys re-resolved; see ../202610311905/") is for the README, and the engine's own 60-word subtitle is
   concatenated after it. Patched: `#big` = "344 verified lines lit"; `#sub` = 64 words / 360 characters built from the same
   variables: what Edition 1 verified (link to the register), what is lit here and what is not on the wafer, the wafer in
   one line (lines, commits, repositories, centre and rim dates) and one sentence naming and linking See Through
   (`../../see-through/`, same host) as the harness notes ask. After: 197 px = 23.5 % on the Pixel 7 (8 % taller than
   before at 18 % larger type and 27 % fewer words), 215.9 px = 33.7 % on 360x640 (9 % shorter).

4. **MINOR · READOUT.** 441 characters at 11 px, 175 px (20.9 %) / 209.5 px (32.7 %). The edition's own line is labelled
   "EDITION 2" and spends 90 characters on the legend. Patched: 383 characters at `--t-small` 12 px, 178.5 px (21.3 %) /
   213.3 px (33.3 %), label "EDITION ·". The engine's lines are untouched.

5. **MINOR · the card.** 11 px; 111 px (13.3 %) / 128 px (20 %), with details open 278 px (33.1 %) / 218 px (34 %, scrolls).
   Patched: body 13 px, details 12 px; 139 px (16.6 %) / 158 px (24.7 %); details open still capped at 34 vh and scrolling.
   The spark stays in the clear space after the patch (Pixel 7: spark y = 380, card top 694; 360x640: spark y = 271, card
   top 476; measured from the magenta ring on the overlay canvas), because `edFly` measures the card as drawn.

6. **PASS · contrast** against `#090c13` (the panels are 95 % of it): `--dim #7d8799` 5.40:1 (AA for body, the lowest),
   `#8fb3bd` bar titles and READOUT 8.71:1, `--cy #2ee6e6` 12.65:1, `--gn #22ee77` LINES focus names 12.63:1, the spark
   itself at 70 % alpha 6.46:1, `--am #ffb000` card title 10.68:1, `--ink` 14.21:1, quote `#cde` 14.11:1, link `#66ccff`
   10.85:1. No colour changed.

7. **MINOR · text-size-adjust.** Only `-webkit-text-size-adjust:100%` is set; the unprefixed property is missing. 100 %
   is right here: it stops Chrome's font boosting (which only applies to desktop-width pages anyway) and does not
   block the Android Text scaling setting, which Blink applies on top of a non-auto text-size-adjust. Patched: the
   unprefixed `text-size-adjust:100%` added. The Android font scale cannot be emulated by this Chromium (injecting
   `text-size-adjust:125%` changed no rectangle, the autosizer is inactive in headless emulation), so a 125 % scale was
   proxied with `zoom:1.25` on the text containers: before, EDITION 316.8 px (37.8 %) / 338 px (52.8 %), card at 42.5 %
   (the proxy also scales the vh cap; a real scale keeps 34 vh and scrolls), bar 92.6 px in three rows; after, EDITION
   293 px (34.9 %) / 316.6 px (49.5 %), bar 89.9 px. Everything still fits under its cap and scrolls.

8. **MINOR · the monospace stack on Android.** `ui-monospace,SFMono-Regular,Menlo,Consolas,monospace`: Chromium does not
   know `ui-monospace` (a WebKit generic) and Android has none of the next three, so every Android phone renders the
   generic `monospace`, which stock Android and Pixels map to Droid Sans Mono (one weight: `<b>` at 600 is synthetic
   bold; √ U+221A is not in it and comes from a Noto fallback). Samsung maps `monospace` to its own face. On this Linux
   Chromium the same fallback lands on DejaVu Sans Mono (`CSS.getPlatformFontsForNode` on `#barname`). No change
   proposed: no Android system monospace is better, and a web font is outside a chart that must load from one folder.

9. **Out of scope, measured:** the bar wraps to three rows (75 px, 9 % / 11.7 %) at 11 px; that is widths, not type. The
   patch keeps `--t-bar` at 11 px on a phone so the bar does not widen further; the bar's owner can raise it once the
   row fits.

## PATCH

Unified diff against `editions/202611012027/index.html`, made with `diff -u` from the scratch copies; applies from the
kuiper-belt root with `patch -p0 < 08-type.patch` (round trip verified byte-identical). CSS and panel copy only: the
type-scale variables, the `#foot` markup, `loadEdition`'s two text assignments and `drawEdition`'s HUD line. keys.json,
cosmos and the placement law are untouched; `node --check` on the extracted module passes; zero console errors on load.
`sub` becomes `innerHTML` for two links; every interpolated value is a number or an ISO date from the page's own data.

```diff
--- editions/202611012027/index.html
+++ editions/202611012027/index.html
@@ -6,20 +6,25 @@
 <title>Kuiper Edition 4</title>
 <style>
   :root{--bg:#090c13;--ink:#d5dcea;--dim:#7d8799;--line:#1a2030;--hot:#e8b36a}
+  /* TYPE SCALE (NL-009 FABLE-08). Four sizes, one line height, set per breakpoint; nothing else names a px size for text.
+     Desktop keeps the 12 px it had. A phone reads larger (13 px body = 34 device px on a Pixel 7, 11 px was 29) and
+     says less: the room the text took was words, not size. --t-bar stays 11 px on a phone so the bar does not widen. */
+  :root{--t-body:12px;--t-small:11px;--t-title:15px;--t-bar:12px;--t-ui:12px;--lh:1.55}
+  @media (max-width:640px){ :root{--t-body:13px;--t-small:12px;--t-title:14px;--t-bar:11px;--t-ui:12px;--lh:1.45} }
   *{box-sizing:border-box}
   html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);
-    font:12px/1.55 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;overflow:hidden;
-    overscroll-behavior:none;-webkit-text-size-adjust:100%}
+    font:var(--t-body)/var(--lh) ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;overflow:hidden;
+    overscroll-behavior:none;-webkit-text-size-adjust:100%;text-size-adjust:100%}
   canvas{position:fixed;inset:0;width:100%;height:100%;display:block;touch-action:none}
   #c{z-index:1} #o{z-index:3;pointer-events:none}
   #top{position:fixed;top:0;left:0;padding:10px 14px;z-index:10;pointer-events:none;max-width:60vw;background:#090c13d9;border-bottom-right-radius:6px}
-  #big{font-size:19px;letter-spacing:.03em} #sub{color:var(--dim);margin-top:2px}
+  #big{font-size:var(--t-title);letter-spacing:.03em} #sub{color:var(--dim);margin-top:2px}
   #hud{position:fixed;top:0;right:0;padding:10px 14px;z-index:10;color:var(--dim);text-align:right;white-space:pre-line;max-width:38vw;background:#090c13d9;border-bottom-left-radius:6px}
   #card{position:fixed;left:14px;bottom:64px;z-index:10;color:var(--ink);background:#090c13ee;
     border:1px solid var(--line);padding:9px 12px;white-space:pre-line;display:none;max-width:min(680px,92vw)}
   #card b{color:var(--hot);font-weight:600}
   #foot{position:fixed;left:0;right:0;bottom:0;padding:8px 14px;color:var(--dim);border-top:1px solid var(--line);
-    background:#090c13ee;z-index:10;line-height:1.7}
+    background:#090c13ee;z-index:10;line-height:var(--lh)}
   #foot b{color:var(--ink);font-weight:600} a{color:#66ccff}
   #goto{position:fixed;left:50%;top:38%;transform:translateX(-50%);z-index:20;display:none;background:var(--bg);
     border:1px solid var(--dim);padding:10px 12px;min-width:min(520px,86vw)}
@@ -27,7 +32,7 @@
   /* SCADA MEANINGS, one colour one meaning: x-ray grey is the record, cyan is the instrument,
      green is energised (lit), amber is attention (new), magenta is selected. */
   :root{--cy:#2ee6e6;--gn:#22ee77;--am:#ffb000;--mg:#ff2bd6}
-  #big{color:var(--cy);text-transform:uppercase;letter-spacing:.16em;font-size:15px}
+  #big{color:var(--cy);text-transform:uppercase;letter-spacing:.16em;font-size:var(--t-title)}
   #top,#hud{border:1px solid #12414a;border-top:0} #top{border-left:0} #hud{border-right:0;color:#8fb3bd}
   #card{border-color:#1d6470} #card b{color:var(--am)} #foot{border-top-color:#12414a} #foot b{color:var(--cy)}
   #goto{border-color:var(--cy)}
@@ -37,27 +42,27 @@
      eat a third of the screen, so it collapses and opens on a tap; nothing is deleted. The
      keyboard commands get tap targets, because a phone has no n, no r and no slash. */
   #keys{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:6px}
-  #keys button{background:#0b1a20;color:#8fb3bd;border:1px solid #12414a;padding:7px 10px;font:inherit;
+  #keys button{background:#0b1a20;color:#8fb3bd;border:1px solid #12414a;padding:7px 10px;font:inherit;font-size:var(--t-ui);
     text-transform:uppercase;letter-spacing:.06em;cursor:pointer;touch-action:manipulation}
   #keys button:hover,#keys button:active{border-color:var(--cy);color:var(--cy)}
+  #foot .short{display:none}                       /* the gesture line is for a phone; the key list is for a keyboard */
   #top{cursor:pointer}
   @media (max-width:640px){
-    html,body{font-size:11px}
     #top,#hud{left:0;right:0;max-width:none;border-radius:0;border-left:0;border-right:0;padding:7px 10px}
     #hud{text-align:left;border-right:0}
-    #big{font-size:13px;letter-spacing:.10em}
+    #big{letter-spacing:.10em}
     #sub{max-height:0;overflow:hidden;margin-top:0}
     #top.open #sub{max-height:38vh;overflow:auto;margin-top:4px}
     #card{left:8px;right:8px;max-width:none;max-height:34vh;overflow:auto}
     #foot{padding:7px 10px}
-    #foot .long{display:none}
+    #foot .long{display:none} #foot .short{display:inline}
     #keys button{padding:9px 11px}
     #goto{min-width:0;left:8px;right:8px;transform:none;top:30%}
   }
   /* EDITION 3: the bar is the only thing on screen at rest; every panel is a layer under it */
   #bar{position:fixed;top:0;left:0;right:0;z-index:12;display:flex;gap:4px;align-items:center;padding:6px 8px;
     background:#090c13e6;border-bottom:1px solid #12414a;overflow-x:auto;white-space:nowrap}
-  #barname{color:var(--cy);letter-spacing:.14em;font-size:12px;margin-right:8px;text-transform:uppercase}
+  #bar{font-size:var(--t-bar)} #barname{color:var(--cy);letter-spacing:.14em;margin-right:8px;text-transform:uppercase}
   #bar .gm-title{appearance:none;border:1px solid #12414a;background:transparent;color:#8fb3bd;font:inherit;
     text-transform:uppercase;letter-spacing:.08em;padding:6px 10px;cursor:pointer;touch-action:manipulation}
   #bar .gm-title:hover,#bar .gm-title.gm-on{background:rgba(80,220,240,.16);color:#fff;border-color:var(--cy)}
@@ -71,16 +76,17 @@
   #linesctl{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
   #linesctl label{color:#8fb3bd} #linesctl input[type=text],#linesctl #lyFind{flex:1 1 180px;background:var(--bg);color:var(--ink);border:1px solid #12414a;padding:5px 8px;font:inherit}
   #linesctl button{background:#0b1a20;color:#8fb3bd;border:1px solid #12414a;padding:5px 9px;font:inherit;text-transform:uppercase;cursor:pointer}
-  #lineslist .ln{padding:5px 6px;border-top:1px solid #121a26;cursor:pointer;color:var(--dim)} #lineslist .ln b{color:var(--ink);font-weight:600}
+  #linesctl,#hud,#foot .short,#foot .law{font-size:var(--t-small)}
+  #lineslist .ln{padding:5px 6px;border-top:1px solid #121a26;cursor:pointer;color:var(--dim);line-height:1.35} #lineslist .ln b{color:var(--ink);font-weight:600}
   #lineslist .ln.focus b{color:var(--gn)} #lineslist .ln.sel{background:rgba(255,43,214,.12)} #lineslist .ln:hover{background:rgba(80,220,240,.10)}
   #card{bottom:12px!important;z-index:13;max-height:30vh;overflow:auto;padding:8px 36px 8px 12px;position:fixed}
   #card .cx{position:absolute;right:6px;top:4px;width:26px;height:26px;border:1px solid #12414a;color:#8fb3bd;background:transparent;font:inherit;cursor:pointer;touch-action:manipulation}
   #card .cq{color:#cde;border-left:2px solid #3a4150;padding-left:8px;margin:4px 0;white-space:pre-wrap}
-  #card .cd{display:none;color:var(--dim);margin-top:6px;border-top:1px solid #121a26;padding-top:6px}
+  #card .cd{display:none;color:var(--dim);margin-top:6px;border-top:1px solid #121a26;padding-top:6px;font-size:var(--t-small)}
   #card.open .cd{display:block}
   #card .ct{color:var(--cy);cursor:pointer;text-decoration:underline dotted}
-  @media (max-width:640px){ #card{left:6px;right:6px;bottom:6px!important;max-height:34vh;font-size:11px} }
-  @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{font-size:11px;margin-right:4px} #bar .gm-title{padding:5px 8px}
+  @media (max-width:640px){ #card{left:6px;right:6px;bottom:6px!important;max-height:34vh} }
+  @media (max-width:640px){ #bar{flex-wrap:wrap;white-space:normal;overflow:visible} #barname{margin-right:4px} #bar .gm-title{padding:5px 8px}
     #top,#hud,#foot,#lines{top:calc(var(--barh,46px) + 0px);left:0;right:0;max-width:none;max-height:62vh} #hud{text-align:left} }
 </style>
 </head>
@@ -93,9 +99,9 @@
 <div id="foot">
   <div id="keys"><button data-k="n">new code</button><button data-k="r">random line</button><button
     data-k="/">find</button><button data-k="e">next verified line</button><button data-k="Backspace">whole wafer</button></div>
-  <span class="long"><b>KUIPER EDITION 4</b>: the verified lines of Edition 1 drawn as green sparks at their own keys on this wafer; <b>e</b> steps through them, tap one for its line and its GitHub link &middot; <b>n</b> show new code &middot; <b>r</b> random line &middot; <b>/</b> a key, a repository, or a period like 2026-07 &middot; <b>click</b> lights the repository under the
-  pointer through all of time &middot; drag &middot; scroll &middot; <b>backspace</b> whole wafer &middot; one law at every zoom:
-  r = &radic;key, &theta; = key &times; golden angle &middot; dark rings are silence between commits, measured &middot; unresolved
+  <span class="long"><b>e</b> next verified line, or tap a spark for its line and its GitHub link &middot; <b>n</b> new code &middot; <b>r</b> random line &middot; <b>/</b> a key, a repository, or a period like 2026-07 &middot; <b>click</b> lights the repository under the pointer through all of time &middot; drag &middot; scroll &middot; <b>backspace</b> whole wafer &middot; </span><span
+  class="short">tap a spark for its line &middot; tap the wafer to light a repository &middot; drag, pinch &middot; </span><span
+  class="law">one law at every zoom: r = &radic;key, &theta; = key &times; golden angle &middot; dark rings are silence between commits, measured &middot; unresolved
   pixels are computed from the law, not drawn &middot; provided as is, without warranty of any kind; a chart, not a design
   &middot; <a href="https://github.com/Ventusltd/law">the laws</a></span>
 </div>
@@ -631,9 +637,13 @@
   catch (e) { ED = []; edMeta = { error: 'keys.json did not load' }; }
   edPlaced = ED.filter(b => b.on_wafer && b.verified && Number.isFinite(b.key) && b.key >= 0 && b.key < SPACE)
                .map(b => { const p = keyPlace(b.key); return Object.assign({}, b, { x:p[0], y:p[1] }); });
-  big.textContent = 'Kuiper Edition 4 · ' + fmt(edPlaced.length) + ' verified lines lit';
-  sub.textContent = 'Edition 1 verified ' + fmt(ED.length) + ' lines of the estate (354 keyed findings, 495 keys re-resolved; see ../202610311905/). '
-    + 'Here each is a green spark at its own key on the one wafer: ' + sub.textContent;
+  const notOn = ED.length - edPlaced.length, day = u => new Date(u*1000).toISOString().slice(0,10);
+  big.textContent = fmt(edPlaced.length) + ' verified lines lit';
+  sub.innerHTML = 'Edition 1 verified ' + fmt(ED.length) + ' lines of the estate (<a href="../202610311905/">the register</a>). '
+    + fmt(edPlaced.length) + ' are green sparks here, each at its own key' + (notOn ? '; ' + fmt(notOn) + ' are not on the wafer, counted, not placed' : '') + '. '
+    + 'The wafer: ' + words(N) + ' lines, ' + fmt(commits.length) + ' commits, ' + repos.length + ' repositories, '
+    + day(commits[0].unix) + ' at the centre, ' + day(commits[commits.length-1].unix) + ' at the rim. '
+    + '<a href="../../see-through/">See Through</a>, the sister app: from the stars to one UK substation in 3D.';
   dirty = true;
 }
 function edScreen(b){ return [(b.x - cx)*zoom + ov.width/2, ov.height/2 - (b.y - cy)*zoom]; }
@@ -647,9 +657,9 @@
     o2.fillStyle = sel ? 'rgba(255,43,214,.95)' : (focus ? 'rgba(34,238,119,.95)' : 'rgba(34,238,119,.70)'); o2.fill();
     if (sel) { o2.strokeStyle = 'rgba(255,43,214,.9)'; o2.lineWidth = 1.5; o2.beginPath(); o2.arc(x, y, 14, 0, 6.2832); o2.stroke(); } }
   const notOn = ED.length - edPlaced.length;
-  hud.textContent += '\nEDITION 2 · ' + fmt(edPlaced.length) + ' verified lines on this wafer, ' + fmt(onScreen) + ' in view'
-    + (notOn ? ' · ' + fmt(notOn) + ' not on the wafer (named in keys.json), counted, not placed' : '')
-    + ' · bright green: gridatlas and the data-centre repositories · green: the rest of the estate';
+  hud.textContent += '\nEDITION · ' + fmt(edPlaced.length) + ' verified lines, ' + fmt(onScreen) + ' in view'
+    + (notOn ? ' · ' + fmt(notOn) + ' not on the wafer (keys.json), counted, not placed' : '')
+    + ' · bright green gridatlas and data centres, green the rest';
 }
 { const _draw = draw; draw = function(){ _draw(); drawEdition(); }; }
 function edCard(i){
```

## TEST

```js
// node test08.cjs  (serve kuiper-belt root first: python3 -m http.server 8108 --bind 127.0.0.1)
const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  for (const opts of [{ ...devices['Pixel 7'] }, { viewport:{width:360,height:640}, deviceScaleFactor:3, isMobile:true, hasTouch:true }]) {
    const page = await (await b.newContext(opts)).newPage(); const errs = [];
    page.on('console', m => m.type() === 'error' && errs.push(m.text())); page.on('pageerror', e => errs.push(e.message));
    await page.goto('http://127.0.0.1:8108/editions/<stamp>/', { timeout: 180000 }); await page.waitForTimeout(8000);
    const tap = async n => { const r = await page.locator('#bar [data-panel=' + n + ']').boundingBox(); await page.touchscreen.tap(r.x + r.width/2, r.y + r.height/2); await page.waitForTimeout(400); };
    const fs = sel => page.evaluate(s => getComputedStyle(document.querySelector(s)).fontSize, sel);
    console.log('body', await fs('body'), 'expect 13px; hud', await fs('#hud'), 'expect 12px; bar', await fs('#bar'), 'expect 11px');
    await tap('foot'); const law = await page.locator('#foot .law').innerText();
    console.log('law visible', await page.locator('#foot .law').isVisible(), /r = √key/.test(law), /a chart, not a design/.test(law), 'short visible', await page.locator('#foot .short').isVisible());
    await tap('foot'); await tap('top'); const sub = await page.locator('#sub').innerText();
    console.log('edition words', sub.split(/\s+/).length, '(expect < 70), names See Through', /See Through/.test(sub), await page.locator('#sub a[href="../../see-through/"]').count() === 1);
    await tap('top'); await page.keyboard.press('e'); await page.waitForTimeout(7000);
    const c = await page.locator('#card').boundingBox(); const ih = await page.evaluate(() => innerHeight);
    console.log('card', await fs('#card'), 'expect 13px; card share', (100*c.height/ih).toFixed(1), '% (expect <= 34); errors', errs);
    await page.screenshot({ path: 'test08-' + opts.viewport.width + '.png', timeout: 180000 });
  }
  await b.close();
})();
```

Expected: body 13px, hud 12px, bar 11px; law visible true true true, short visible true; edition words < 70 with the
See Through link; card 13px and at most 34 % of the screen; errors []. On a desktop context (1280x800) the same
script should print body 12px and `#foot .short` not visible.

## LIMITS

- The Android Text scaling setting was not emulated (headless Chromium ignores an injected `text-size-adjust:125%`);
  the 125 % numbers are a `zoom:1.25` proxy on the text containers, which also scales the vh caps. The claim that Blink
  applies the accessibility factor on top of `text-size-adjust:100%` is from Blink's TextAutosizer and not measured here.
- Which font an Android phone renders was reasoned from Chromium's family handling and Android's fonts.xml, not seen on
  a device; this Chromium rendered DejaVu Sans Mono. Samsung's monospace mapping was not checked.
- Contrast was computed against the flat panel colour `#090c13`; the panels are 95 % opaque over the wafer, and a
  bright wafer region under a panel lowers the ratios slightly. The card over lit sparks was not sampled.
- The EDITION panel on the Pixel 7 is 15 px taller after the patch than before (bigger type, fewer words); shorter
  still would mean dropping the wafer sentence or the register link, which I did not do.
- The COMMANDS panel is now the tallest layer on a 360x640 phone (40.6 %) because the law text is required and the five
  buttons take two rows; it scrolls under the 62 vh cap. If the bar's owner reflows the buttons to one row it drops
  by 45 px.
- The See Through sentence links `../../see-through/` from the EDITION panel; it does not add the bar button, which is
  another agent's patch. Both can land together; the texts do not overlap in the file.
- `#barname` and the `<title>` still say Edition 4; the integrator renames them for Edition 5 as usual (not in this diff).
