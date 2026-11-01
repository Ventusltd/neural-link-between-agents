# FABLE-10 journey: the Android end-to-end journey and the shared test harness (NL-009 round 1)

Edition audited: `editions/202611012027` (Edition 4), kuiper-belt main `018b46aed50f28f7b1882a0dcaba6593ce522beb`, served at `http://127.0.0.1:8110/editions/202611012027/`.
Harness: `/home/user/neural-link-between-agents/FIXES/NL-009/android-journey.cjs` (Playwright, Chromium with SwiftShader, `devices['Pixel 7']`, `devices['Galaxy S24']`, `devices['Pixel 7 landscape']`, real touch only: `page.touchscreen.tap`, CDP `Input.dispatchTouchEvent` for pinch, drag and in-panel scroll).
Baseline report: `round1/10-journey-baseline.json` (this is what reviewers rerun on Edition 5).

## Baseline on Edition 4

| step | Pixel 7 | Galaxy S24 | Pixel 7 landscape | what is measured |
|---|---|---|---|---|
| `load` | FAIL | FAIL | PASS | load: zero console errors, wafer drawn, bar one row |
| `edition-open` | PASS | PASS | PASS | tap EDITION: panel opens under the bar and scrolls inside |
| `edition-close` | PASS | PASS | PASS | tap EDITION again: panel closes |
| `lines-open` | PASS | PASS | PASS | tap LINES: panel opens under the bar with the rows |
| `lines-filter` | PASS | PASS | PASS | type "acceptance": the list narrows to matching rows, input and first row on screen |
| `lines-pick` | PASS | PASS | PASS | tap the first row: LINES closes, camera flies, card opens, spark in the clear space |
| `card-details` | PASS | PASS | PASS | tap details: the card grows, stays under its cap and on screen |
| `card-close` | PASS | PASS | PASS | tap ×: the card closes and the selection clears |
| `key-e-1` | PASS | PASS | PASS | press e (1): next line, card open, spark in the clear space |
| `key-e-2` | PASS | PASS | PASS | press e (2): next line, card open, spark in the clear space |
| `key-e-3` | PASS | PASS | PASS | press e (3): next line, card open, spark in the clear space |
| `pinch-drag` | PASS | PASS | PASS | pinch out then drag: the wafer zooms and pans, the page neither scrolls nor zooms |
| `spark-tap` | PASS | PASS | PASS | tap a green spark: the card for the nearest spark opens and the camera places it clear |
| `whole-wafer` | PASS | PASS | PASS | tap COMMANDS then WHOLE WAFER: the card closes and the whole wafer is on screen under the bar |
| `see-through` | FAIL | FAIL | FAIL | tap SEE THROUGH: ../../see-through/ opens (new tab or navigation) |

Pixel 7: 13 passed, 2 failed · Galaxy S24: 13 passed, 2 failed · Pixel 7 landscape: 14 passed, 1 failed. Console errors on load: 0/0/0.

## FINDINGS

1. **MAJOR — the bar wraps to two rows on every portrait phone.** Pixel 7 (412 px): `.gm-title` tops [6, 6, 6, 39], `#bar` height 75.1 px; Galaxy S24 (360 px): tops [6, 6, 6, 39], height 75.1 px. COMMANDS sits on a second row under the title "KUIPER EDITION 4"; the clear space starts at 75.1 px instead of one row. Landscape (863 px) is one row: tops [6, 6, 6, 6], height 45.6 px. Step `load` FAILS on both portrait devices for this reason alone (zero console errors, wafer drawn: lit fraction 0.2312, bbox [45, 296, 366, 618] on Pixel 7). Screenshot `img/10-journey-load-bar-two-rows.png`. Edition 5 must keep the bar to one row at 360 px with SEE THROUGH added, which means a shorter title (or none) and shorter button padding, and the script will check it.

2. **MAJOR — there is no SEE THROUGH control.** `#bar` holds four `.gm-title` buttons (edition, readout, lines, commands) and no button or link whose text matches `/see through/i` or whose `href` contains `see-through`. Step `see-through` FAILS on all three devices with "no SEE THROUGH control in #bar". The app at `../../see-through/` (stable pointer to `202610050609/`) is reachable only by typing the URL.

3. **MINOR — after WHOLE WAFER the COMMANDS layer stays open over the wafer.** Tapping `#foot button[data-k="Backspace"]` homes the camera and closes the card (card open after: False, selected spark: None), but the panel stays (`panelStayedOpenAfterTap: True`, panel rect {'left': 0, 'top': 77.1, 'right': 412, 'bottom': 188.5, 'width': 412, 'height': 111.4} on Pixel 7), so the user sees the commands, not the wafer, until a second tap on the canvas. The script closes it with a tap in the empty corner and then measures the whole disc (bbox [45, 296, 366, 617]), so the step passes; a pick in LINES already closes its panel, WHOLE WAFER should do the same.

4. **MINOR — lit-repository points look like verified-line sparks.** After every pick the engine lights the line's repository (`litRepo`) in bright green on the WebGL layer; at zoom 14 the overlay `#o` carries no green spark at all (`greensInView: 0` before the zoom-out) while the screenshot after the third `e` shows dozens of green points of the lit repository (`img/10-journey-key-e-3-lit-repo-green.png`). One colour, two meanings, on the one screen where the user is asked to tell them apart. Not in my dimension to fix; recorded for the palette owner.

5. **MINOR — touch targets.** The card's × is [26, 26] CSS px (Android guidance 48 dp); the direct spark tap accepts a touch within 9 px (`bd = 81` squared in the edition's `pointerup` handler) of a dot drawn at 2.6–3.2 px radius. The script taps the measured centroid of a spark, so `spark-tap` measures the law, not the thumb: tapped {'x': 309.1, 'y': 449.7, 'px': 33}; greens in view 0; predicted nearest by the law: line 323 at 1.7 px (second nearest 29.4 px); card shows 323 (Pixel 7); Galaxy S24: tapped {'x': 258.6, 'y': 424.6, 'px': 33}; greens in view 0; predicted nearest by the law: line 323 at 1.5 px (second nearest 25.7 px); card shows 323; landscape: tapped {'x': 431.7, 'y': 80.6, 'px': 34}; greens in view 0; predicted nearest by the law: line 323 at 1.1 px (second nearest 13.7 px); card shows 323.

6. **MINOR — the keyboard `e` is dead while the LINES filter has focus.** `#lyFind` stops `keydown` propagation, so after typing a filter and picking a row (the panel hides, focus may stay in the input) a hardware/Bluetooth keyboard `e` does nothing until something else is tapped. The script blurs the active element before pressing `e`; without that blur the first `e` is swallowed. On a touch-only phone this is moot (NEXT in LINES and NEXT VERIFIED LINE in COMMANDS dispatch the key event themselves).

What passes on Edition 4 and must keep passing on Edition 5 (measured): EDITION opens under the bar (panel top 77.1 px vs bar bottom 75.1 px, `overflow-y: auto`, in-panel touch scroll {'scrollable': 0, 'ok': True, 'note': 'panel content fits, nothing to scroll'}) and closes on the second tap; LINES opens with 344 rows, the filter "acceptance" leaves 7 rows all matching; the first row closes the panel, flies the camera (the first frame after the tap had no spark drawn yet, so the flight distance was not measurable; the rest position is) and leaves the spark at y=386.3 between bar bottom 75.1 and card top 704.7 with `elementFromPoint` = `#c`; details grow the card from 128.3 to 285.2 px under the cap 285.3 px (833 ≤ 839); × closes it; `e` ×3 gives cards [1, 2, 3] of 344 with the spark at y=[395, 369.1, 369.1] (clear window [85.1, 711.8]); pinch and drag move the wafer and never the page: pinch 220→110 px: spark distance from the finger midpoint [100, 50] → ratio 0.5 (expected 0.5); drag (−90, +70) moved the spark [-90, 70]; page scroll [0, 0], visualViewport.scale 1; zoom-out pinches y×300→12 (spark moved 0.9 px, ok True), y×300→12 (spark moved 0.6 px, ok True), y×300→17.6 (spark moved 1.6 px, ok True) (Pixel 7); Galaxy S24: pinch 220→110 px: spark distance from the finger midpoint [100, 50.2] → ratio 0.502 (expected 0.5); drag (−90, +70) moved the spark [-90, 70]; page scroll [0, 0], visualViewport.scale 1; zoom-out pinches y×288.2→12 (spark moved 0.8 px, ok True), y×289.6→12 (spark moved 0.8 px, ok True), y×290.8→13.8 (spark moved 1.5 px, ok True).

## PATCH

None in this dimension. The deliverable is the harness and the baseline. Patches 01–09 are expected to flip `load` (one-row bar) and `see-through` to PASS; finding 3 is a one-line change (`if (openPanel) setPanel(openPanel);` after the WHOLE WAFER dispatch, or closing the panel in the `#keys` click handler) that whoever owns COMMANDS may take.

## Element ids and texts the script relies on (integrator: keep them in Edition 5 or update the script header)

- `#bar` holding `.gm-title` buttons with `data-panel="top"` (text EDITION), `"hud"` (READOUT), `"lines"` (LINES), `"foot"` (COMMANDS); the open title carries class `gm-on`; `#barname` is the title span. A SEE THROUGH control is any `<button>` or `<a>` inside `#bar` whose text matches `/see\s*-?\s*through/i` or whose `href` contains `see-through`; it may open a new tab (`target="_blank"`) or navigate in place; the resulting URL must contain `/see-through/`.
- Panels `#top` (EDITION, containing `#big` and `#sub`), `#hud`, `#lines`, `#foot`; an open panel carries class `gm-open` and is `display:block`; its `overflow-y` must be `auto` or `scroll`.
- `#lines`: `#lyFind` (filter input, typed into after a tap), `#lineslist` with rows `.ln[data-i]`; the first matching row is tapped at its centre.
- `#foot`: `#keys button[data-k="Backspace"]` (text WHOLE WAFER).
- `#card`: shown with inline `display:block`; its text contains `n of N` (the script parses the first `(\d+) of (\d+)`); `.ct` toggles details (class `open` on `#card`, `.cd` becomes visible); `.cx` closes. The cap is read from computed `max-height` (vh or px).
- Canvases `#c` (WebGL wafer) and `#o` (2d overlay). The selected spark is magenta (`rgba(255,43,214)` disc plus 14 px ring) and other sparks green (`rgba(34,238,119)`) on `#o`, with `#o.width === innerWidth` (one canvas pixel per CSS pixel). The hit test at the spark's point must return `#c`.
- `keys.json` beside the page: `bodies[]` with `key`, `on_wafer`, `verified`, in the order the page builds `edPlaced` (filter `on_wafer && verified && finite key >= 0`, order preserved). The script re-derives each spark's world position with the placement law (`r = sqrt(key + 0.5)`, `theta = 2*pi*frac(key*G/2^32)`, `G = 2654435769`) and relies on the fly ending at zoom 14 and on the pinch law `zoom = zoom0 * d / d0` to know the camera; if Edition 5 changes the fly zoom, change the constant `14` in `solve(p, 14)`.
- `#big` text contains `verified lines lit` once `keys.json` has loaded (the load wait).
- Keyboard: `e` steps to the next line (the script blurs the active element first, because `#lyFind` stops keydown propagation).

## TEST

```
cd /home/user/estate/kuiper-belt && python3 -m http.server 8110 --bind 127.0.0.1 &
node /home/user/neural-link-between-agents/FIXES/NL-009/android-journey.cjs \
  http://127.0.0.1:8110/editions/<stamp>/ /tmp/nl009/journey-<stamp> --all
```

Exit code 0 means every step passed on Pixel 7, Galaxy S24 and Pixel 7 landscape; the JSON on stdout (also `<outdir>/report.json`) lists `pass`, `measured` and `note` per step, and `<outdir>/<device>/NN-<step>.png` is the screenshot of each step at CSS scale. `--device "Pixel 7"` runs one device; `--devices "A,B"` a list. Compare against `round1/10-journey-baseline.json` (Edition 4): the steps that must flip to pass are `load` (bar one row), `spark-tap`, `whole-wafer` and `see-through`; everything that passes in the baseline must still pass. On a loaded machine a step can take minutes (frames at zoom 14 under SwiftShader); a screenshot that times out is recorded as `FAILED:` in `measured.screenshot` and does not fail the step.

## LIMITS

- Measured under SwiftShader on a machine shared with nine other Chromium runs (load average 50–80 on 4 cores): frame times are not representative of a phone; the assertions are geometric and do not depend on speed, but each run takes 15–40 minutes.
- `e` is a keyboard key; a phone user taps NEXT in LINES or NEXT VERIFIED LINE in COMMANDS, which dispatch the same key event. The script does not test the Android back gesture, font scaling, the dynamic toolbar (`100vh` vs `dvh`) or safe-area insets, because Playwright's emulation has none of them; `visualViewport.scale` and `scrollY` are checked after every gesture instead.
- The spark tap is predicted with the placement law and `keys.json`; a page that changes the fly zoom or the pinch law makes `spark-tap` report `cameraKnown:false` rather than a false failure.
- The See Through step only checks that the URL reached contains `/see-through/`; the app itself needs MapLibre tiles from the internet, which the sandbox blocks.
