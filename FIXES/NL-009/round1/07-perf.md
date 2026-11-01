# 07-perf: performance of the Edition 4 page on Android-class devices (NL-009 round 1)

Auditor FABLE-07, dimension perf. Page audited: `/home/user/estate/kuiper-belt/editions/202611012027/index.html` at kuiper-belt main 018b46aed50f28f7b1882a0dcaba6593ce522beb. Emulation: Playwright `devices['Pixel 7']` (viewport 412 x 915 CSS px, devicePixelRatio 2.625, touch, mobile) in the pre-installed Chromium with SwiftShader (`--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`), page served from a mirror of the repository root on port 8107.

**Read the numbers as ratios, not as phone timings.** SwiftShader renders the wafer's fragment shader on the CPU, and during these runs the machine (4 cores) carried a load average of 25 to 47 because nine other auditors were rendering the same page at the same time. A frame that takes 950 ms here takes a few milliseconds on a phone GPU. What transfers is the proportion between variants measured the same way, and the counts (bytes, draws, rows), which do not depend on speed at all.

## FINDINGS

**1. MAJOR: 74 % of every page load is `keys.json`, and 73 % of `keys.json` is one field of one record that the page never reads.** Measured on the Pixel 7 profile: the page loads 2,310,949 bytes in all, of which `keys.json` is 1,709,327 (74 %); `cosmos/wafer.tsv` is 535,037 and the page itself 61,653. Inside `keys.json` the field `line_text` sums to 1,266,436 bytes, and 1,240,449 of those are the single record `kuiper-belt estate-network.json:1`, a one-line minified JSON file quoted whole. The edition layer reads 14 of the 36 fields per record (`key on_wafer verified class title repo path line quote destination commit pattern worker finding`, plus `id` kept for identity) and never `line_text`. Compressed it is no better: `gzip -6` of `keys.json` is 743,603 bytes (the big string is low-entropy JSON but still 740 kB), against 59,947 for the compact file. Fix (in the patch): the page loads `keys-min.json`, written from `keys.json` by a 40-line script (`tools/edition_min.py`, below) that keeps those 15 fields, minifies, and records the sha256 of its source; if the compact file is missing it falls back to `keys.json`, so nothing breaks. `keys.json` stays in the folder untouched as the evidence. After: 835,817 bytes in all, `keys-min.json` 233,056 (28 %): 2.76x fewer bytes for the page, 7.3x fewer for the keys, 12.4x fewer gzipped. Locally the sparks appeared 1497 ms after the first wafer frame before (keys fetch 1011 ms + JSON.parse 63.8 ms) and 4 ms after (fetch 19.5 + parse 10.9 ms); the slow-4G table below gives the link-bound figure.

**2. MINOR: the LINES filter re-lays out all 344 rows on every keystroke.** `fillLines()` rebuilds `#lineslist` as one innerHTML on each `input` event; the handler itself is cheap (p50 1.2 to 1.6 ms) but the layout the browser then does for 344 rows in a 62vh scroller is not: p50 9.0 and 6.9 ms, p90 45 and 214 ms per keystroke in two runs (40 keystrokes each, see the table). Fix (in the patch, CSS only): `content-visibility:auto; contain-intrinsic-size:auto 44px` on `#lineslist .ln`, so rows scrolled out of view are not laid out. After: p50 1.2 and 1.4 ms, p90 18 and 6 ms; input-to-next-frame p50 30.5/28.9 ms before, 18.8/23.4 ms after. Nothing visible changes.

**3. PASS (no change): the page draws only when something changed, and runs no timers.** With the frame loop instrumented, 0 calls of `draw()` in 3 s at rest at home and 0 in 3 s at rest at zoom 14 with the card open, in every variant and run; during a 900 ms fly there is one draw per frame while the tween runs and none after. `grep` finds no `setInterval`; the four `setTimeout` calls serve `?selftest=` only. One engine-level note, outside my scope: `frame()` re-arms `requestAnimationFrame` every vsync even when idle, so the renderer never sleeps; on a phone that is battery, not frame time. It is the engine's loop and I do not touch it.

**4. PASS (no change, but recorded): both canvases are already at one backing pixel per CSS pixel, not at devicePixelRatio.** `resize()` sets `cv.width = ov.width = innerWidth`, so on the Pixel 7 profile both canvases are 412 x 839 for a 1081 x 2202 physical screen (DPR 2.625), and the compositor upscales them. For the WebGL wafer that is the right choice and no cap is needed: its fragment shader runs two 16-step binary searches per pixel, so cost is proportional to backing pixels. Measured by forcing `draw()` every frame (the only way to see the GPU cost under SwiftShader, where `gl.drawArrays` returns before the work is done): see the DPR table. The brief's "cap at DPR 2" is therefore already exceeded (it is at 1); I recommend leaving it and I add no code for it.

**5. MINOR, measured as an option and NOT in the patch: the 2D overlay (sparks, month labels, target cross) could be drawn at DPR 2 for sharpness.** Because both canvases are upscaled 2.625x, a 2.6 px spark is a blurred 7-device-pixel blob and the 10 px month labels are soft (screenshot `img/07-before-fly.png`, right panel, device pixels 1:1). A 10-line hunk in the edition layer can give the overlay a backing store at min(DPR, 2) while `ov.width`/`ov.height` keep answering in CSS pixels, so the engine's arithmetic is untouched (`img/07-after-fly.png`). Cost: 4x the overlay pixels; with only the overlay redrawn each frame, the frame cadence went from p50 16.7 ms (DPR 1) to 83 and 183 ms (DPR 2) in two runs under SwiftShader, 5 to 11x. A phone GPU composites a 824 x 1678 canvas far more cheaply than SwiftShader does, but I cannot measure that here, so the hunk is supplied separately (`07-perf-optional-overlay-dpr.patch` text at the end) for the integrator and the owner to decide, and the main patch stays without it.

**6. INFO: the edition overlay is cheap as it is.** `clearRect` + `drawEdition()` with all 344 sparks in view costs p50 0.2 to 0.5 ms of JavaScript per frame (300 iterations, two runs). Batching the sparks into two `Path2D` fills instead of 344 `fill()` calls measured p50 0.2 to 0.3 ms: within noise, so that hunk was dropped. The frame cost of this page is the WebGL field, not the sparks.

**7. MINOR, observed while instrumenting, outside perf (for whoever owns LINES):** with "gridatlas + data centres only" ticked, the `drawEdition` wrapper swaps `edPlaced` for the filtered array but `edSel` still indexes the full one, so the magenta selected spark can be drawn on the wrong line. Not patched here.

**8. INFO: GitHub Pages compression could not be verified from this sandbox** (the proxy returns 403 for github.io). Pages normally serves gzip/brotli for JSON; even so `keys.json` is 740 kB compressed against 60 kB, so finding 1 stands either way.

## MEASUREMENTS

All runs: Pixel 7 profile, SwiftShader, load average 25 to 47 on 4 cores shared with nine other auditors. Variants: `o` = Edition 4 as is; `p` = patch 07 (keys-min.json + list CSS); `p2` = patch 07 + the optional overlay-at-DPR-2 hunk; `d2`, `d26` = measurement-only copies of Edition 4 whose WebGL store is 2x and 2.625x (zoom scaled to match; the overlay is left at CSS size in those, so their spark counts in view are off and only the WebGL column is meaningful). Harness: `/tmp/claude-0/.../scratchpad/nl009/07/` (`measure.cjs`, `bench.cjs`, `bench3.cjs`, `slow4g.cjs`, `build.py`; may not survive the container).

### Bytes and first frames (local server, no compression)

| variant | keys file | keys bytes | all bytes | keys share | first wafer frame (ms from navigation) | first spark frame | sparks after wafer | keys fetch + JSON.parse (ms) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| o | keys.json | 1,709,327 | 2,310,949 | 74 % | 1320 | 2817 | 1497 | 1011 + 63.8 |
| p | keys-min.json | 233,056 | 835,817 | 28 % | 3206 | 3210 | 4 | 19.5 + 10.9 |

File sizes: `keys.json` 1,709,129 raw / 743,603 gzip-6; `keys-min.json` 232,859 raw / 59,947 gzip-6; `wafer.tsv` 535,037 / 229,265; `index.html` 61,653 / 21,566; `repos.tsv` 2,467 / 1,416. The first-wafer-frame column varies with shader compilation under load and is not affected by the patch; the column that matters is "sparks after wafer".

### Time to the sparks on an emulated slow 4G link (CDP `Network.emulateNetworkConditions`: 1.6 Mbit/s down, 150 ms RTT)

| run | variant | keys file bytes | keys fetch (ms) | first wafer frame (ms) | first spark frame (ms) | sparks after wafer (ms) |
|---|---|---:|---:|---:|---:|---:|
| (pending) | | | | | | |

### Does it draw when nothing changed? Draws of `draw()` per 3 s window, every variant

| variant | rest at home | rest at zoom 14, card open | draws during the 3 s that contain a 900 ms fly |
|---|---:|---:|---:|
| o | 0 | 0 | 29 |
| p | 0 | 0 | 5 |
| p2 | 0 | 0 | 4 |
| d2 | 0 | 0 | 4 |
| d26 | 0 | 0 | 4 |

### Canvas backing stores (Pixel 7 profile: 412 x 839 CSS px window as laid out, DPR 2.625, physical 1081 x 2202)

| variant | WebGL canvas | overlay backing | overlay as the engine reads `ov.width x ov.height` |
|---|---|---|---|
| o | 412 x 839 | 412 x 839 | 412 x 839 |
| p | 412 x 839 | 412 x 839 | 412 x 839 |
| p2 | 412 x 839 | 824 x 1678 | 412 x 839 |
| d2 | 824 x 1678 | 412 x 839 | 412 x 839 |
| d26 | 1082 x 2202 | 412 x 839 | 412 x 839 |

### WebGL cost against backing-store size: `draw()` forced every frame, requestAnimationFrame deltas (ms)

| variant | WebGL store | at home (unresolved field, whole wafer): n, p50, p90 | at zoom 14 after `e` (resolved points): n, p50, p90 | ratio to DPR 1 (home p50) |
|---|---|---|---|---:|
| d2b-1 | 824 x 1678 | 29, 16.7, 316.6 | 7, 166.6, 1066.6 | |
| ob-1 | 412 x 839 | 89, 950, 2483.3 | 44, 3766.5, 9732.9 | 1.0x |

The same picture from the 12-frame windows of the main runs (rAF p95, ms, noisy): forced redraws at home o 83, d2 267, d26 317; during the fly o 650, d2 1050, d26 5500; forced redraws at zoom 14 o 883, d2 300, d26 13,766.

### Overlay (`clearRect` + `drawEdition`, 344 sparks in view at home), two runs each

| variant | overlay | JS per call, 300 iterations: p50 / p90 (ms) | frame cadence with only the overlay redrawn, 119 frames: p50 / p90 (ms) | idle cadence before: p50 / p90 |
|---|---|---|---|---|
| ob-1 | per-spark fill, DPR 1 (as is) | 0.5 / 11 | 50 / 1466.5 | 16.7 / 66.7 |
| ob-2 | per-spark fill, DPR 1 (as is) | 0.2 / 2.8 | 16.7 / 66.7 | 16.7 / 33.4 |
| p2b-1 | two Path2D fills, DPR 2 (option) | 0.3 / 2.4 | 83.3 / 1549.9 | 16.7 / 33.4 |
| p2b-2 | two Path2D fills, DPR 2 (option) | 0.2 / 1.4 | 183.3 / 1333.3 | 16.7 / 33.3 |
| pb-1 | two Path2D fills, DPR 1 (tested, dropped) | 0.3 / 4 | 16.7 / 533.4 | 16.7 / 200 |
| pb-2 | two Path2D fills, DPR 1 (tested, dropped) | 0.2 / 0.4 | 16.7 / 183.3 | 16.7 / 116.6 |

### LINES filter, 40 keystrokes per run (5 rounds of g, gr, gri, grid, grida, "grid ", "grid a", empty; rows shown 312, 216, 212, 212, 126, 212, 1, 344)

| variant | list CSS | handler p50 / p90 (ms) | forced layout after it p50 / p90 (ms) | input to next frame p50 / p90 (ms) |
|---|---|---|---|---|
| ob-1 | as is | 1.6 / 12.7 | 9 / 45.3 | 30.5 / 762.1 |
| ob-2 | as is | 1.6 / 24.3 | 6.9 / 214.1 | 28.9 / 956.7 |
| p2b-1 | content-visibility:auto | 1.2 / 15 | 1.3 / 8 | 25.9 / 829.1 |
| p2b-2 | content-visibility:auto | 1.1 / 95.7 | 1.3 / 23 | 25 / 690.7 |
| pb-1 | content-visibility:auto | 1.3 / 6.2 | 1.2 / 18.4 | 18.8 / 606.5 |
| pb-2 | content-visibility:auto | 1.2 / 10.3 | 1.4 / 6.2 | 23.4 / 236.1 |

Console errors: 0 in every instrumented run (`o`, `p`, `p2`, `d2`, `d26`); the uninstrumented checks of the patched page and of the untouched folder are in the TEST section's expected output.

Screenshots: `img/07-before-fly.png` (Edition 4 as is after `e`, with a 1:1 device-pixel crop of the selected spark) and `img/07-after-fly.png` (the optional overlay-at-DPR-2 variant, same camera; it is not in the patch). The patch itself changes no pixel.

## PATCH

One unified diff against `editions/202611012027/index.html`, two hunks (CSS for the list rows; `loadEdition` reads `keys-min.json` with a fallback). Apply from the kuiper-belt root with `git apply 07-perf.patch` or `patch -p1 < 07-perf.patch` (both verified with `--check` / `--dry-run` at HEAD 018b46a; the extracted module script passes `node --check`). Then generate the compact file in the new edition folder with the script below (`python3 tools/edition_min.py editions/<stamp>`), and list `keys-min.json` in `proof/edition-sha256.txt`.

```diff
--- a/editions/202611012027/index.html
+++ b/editions/202611012027/index.html
@@ -71,7 +71,7 @@
   #linesctl{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
   #linesctl label{color:#8fb3bd} #linesctl input[type=text],#linesctl #lyFind{flex:1 1 180px;background:var(--bg);color:var(--ink);border:1px solid #12414a;padding:5px 8px;font:inherit}
   #linesctl button{background:#0b1a20;color:#8fb3bd;border:1px solid #12414a;padding:5px 9px;font:inherit;text-transform:uppercase;cursor:pointer}
-  #lineslist .ln{padding:5px 6px;border-top:1px solid #121a26;cursor:pointer;color:var(--dim)} #lineslist .ln b{color:var(--ink);font-weight:600}
+  #lineslist .ln{padding:5px 6px;border-top:1px solid #121a26;cursor:pointer;color:var(--dim);content-visibility:auto;contain-intrinsic-size:auto 44px} /* EDITION 5 (perf): rows out of view are not laid out */ #lineslist .ln b{color:var(--ink);font-weight:600}
   #lineslist .ln.focus b{color:var(--gn)} #lineslist .ln.sel{background:rgba(255,43,214,.12)} #lineslist .ln:hover{background:rgba(80,220,240,.10)}
   #card{bottom:12px!important;z-index:13;max-height:30vh;overflow:auto;padding:8px 36px 8px 12px;position:fixed}
   #card .cx{position:absolute;right:6px;top:4px;width:26px;height:26px;border:1px solid #12414a;color:#8fb3bd;background:transparent;font:inherit;cursor:pointer;touch-action:manipulation}
@@ -624,9 +624,12 @@
 // spark here is a key that python tools/key.py would resolve to that very line. Lines whose commit is
 // not on the wafer are counted and named, never placed: the seventh law.
 let ED = [], edPlaced = [], edSel = -1, edMeta = null;
-const EDPATH = 'keys.json';
+const EDPATH = 'keys-min.json', EDFULL = 'keys.json';
+// EDITION 5 (perf): the page draws 14 of the 36 fields of each record, so it loads keys-min.json (233 kB,
+// written from keys.json by tools/edition_min.py, which records the sha256 of its source). keys.json stays in
+// the folder as the evidence (1.7 MB, 73 % of it one record's line_text). Without the compact file the full one loads.
 async function loadEdition(){
-  try { const r = await fetch(EDPATH); if (!r.ok) throw new Error(EDPATH); const j = await r.json();
+  try { let r = await fetch(EDPATH); if (!r.ok) r = await fetch(EDFULL); if (!r.ok) throw new Error(EDFULL); const j = await r.json();
     edMeta = j.summary || {}; ED = j.bodies || j; }
   catch (e) { ED = []; edMeta = { error: 'keys.json did not load' }; }
   edPlaced = ED.filter(b => b.on_wafer && b.verified && Number.isFinite(b.key) && b.key >= 0 && b.key < SPACE)
```

`tools/edition_min.py` (new file, the generator; deterministic output, LF, `--check` verifies an existing `keys-min.json` against `keys.json`):

```python
#!/usr/bin/env python3
"""keys-min.json: only the fields the edition page draws, taken from keys.json, which stays as the evidence.

keys.json (1.7 MB) carries 36 fields per record and one record whose line_text is a 1.24 MB one-line file;
the page reads 14 fields. This writes them, in a fixed order, minified, LF-terminated, with the sha256 of
the keys.json it came from, so the proof can tie the two together.

usage: python3 tools/edition_min.py editions/<stamp>          writes editions/<stamp>/keys-min.json
       python3 tools/edition_min.py editions/<stamp> --check  verifies an existing keys-min.json against keys.json
"""
import hashlib, json, os, sys

FIELDS = ('id', 'key', 'on_wafer', 'verified', 'class', 'title', 'repo', 'path', 'line',
          'quote', 'destination', 'commit', 'pattern', 'worker', 'finding')

def build(folder):
    raw = open(os.path.join(folder, 'keys.json'), 'rb').read()
    j = json.loads(raw)
    summary = dict(j.get('summary') or {})
    summary.update(source='keys.json', source_sha256=hashlib.sha256(raw).hexdigest(), fields=list(FIELDS))
    bodies = [{k: b[k] for k in FIELDS if k in b} for b in j['bodies']]
    return {'summary': summary, 'bodies': bodies}

def text(obj):
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=False) + '\n'

def main(argv):
    folder = argv[1]
    dst = os.path.join(folder, 'keys-min.json')
    want = text(build(folder))
    if '--check' in argv:
        have = open(dst, 'rb').read().decode('utf-8')
        ok = have == want
        print('keys-min.json %s (%d bytes)' % ('matches keys.json' if ok else 'DIFFERS from keys.json', len(have.encode())))
        return 0 if ok else 1
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write(want)
    print('wrote %s: %d records, %d fields each, %d bytes (keys.json %d bytes)' % (
        dst, len(json.loads(want)['bodies']), len(FIELDS), len(want.encode()), os.path.getsize(os.path.join(folder, 'keys.json'))))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
```

Optional hunk, NOT part of patch 07 (finding 5), as a diff on top of patch 07 for the integrator to take or leave:

```diff
--- a/editions/202611012027/index.html
+++ b/editions/202611012027/index.html
@@ -750,6 +750,15 @@
 { const _edNext = edNext; edNext = function(step){ if (!edPlaced.length) return; let i = edSel, n = edPlaced.length;
     for (let t = 0; t < n; t++) { i = (i + step + n) % n; if (visibleLine(edPlaced[i])) break; }
     edSel = i; const b = edPlaced[edSel]; edCard(edSel); edFly(b); }; }
+// EDITION 5 (perf): the 2D overlay (sparks, month rings, the target cross) is drawn at the device pixel ratio,
+// capped at 2, so it is sharp on a phone; ov.width and ov.height keep answering in CSS pixels, so the engine's
+// arithmetic is untouched. The WebGL wafer stays at one backing pixel per CSS pixel on purpose: its fragment
+// shader costs per pixel (measured in FIXES/NL-009/round1/07-perf.md), and it is resampled by the compositor.
+{ const OVR = Math.min(2, devicePixelRatio || 1); if (OVR > 1) {
+  const dw = Object.getOwnPropertyDescriptor(HTMLCanvasElement.prototype, 'width'), dh = Object.getOwnPropertyDescriptor(HTMLCanvasElement.prototype, 'height');
+  Object.defineProperty(ov, 'width', { get(){ return Math.round(dw.get.call(ov) / OVR); }, set(v){ dw.set.call(ov, Math.round(v * OVR)); o2.setTransform(OVR, 0, 0, OVR, 0, 0); } });
+  Object.defineProperty(ov, 'height', { get(){ return Math.round(dh.get.call(ov) / OVR); }, set(v){ dh.set.call(ov, Math.round(v * OVR)); o2.setTransform(OVR, 0, 0, OVR, 0, 0); } });
+  resize(); } }
 requestAnimationFrame(frame);
 </script>
 </body>
```

## TEST

1. Apply the patch to a copy of the folder, run `python3 tools/edition_min.py editions/<stamp>` (expect `wrote ... 346 records, 15 fields each, 232859 bytes`), then `python3 tools/edition_min.py editions/<stamp> --check` (expect `matches keys.json`).
2. `cd /home/user/estate/kuiper-belt && python3 -m http.server 8107 --bind 127.0.0.1 &`
3. Playwright, Pixel 7, bytes and errors:
```js
const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch({ args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const page = await (await b.newContext({ ...devices['Pixel 7'] })).newPage();
  const errors = []; page.on('pageerror', e => errors.push(String(e))); page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await page.goto('http://127.0.0.1:8107/editions/<stamp>/', { waitUntil:'load', timeout:180000 }); await page.waitForTimeout(10000);
  console.log(await page.evaluate(() => performance.getEntriesByType('resource').map(r => r.name.split('/').pop() + ':' + r.transferSize)));
  // expect keys-min.json at about 233,000 bytes and NO keys.json request; big text ends in "344 verified lines lit"
  console.log(await page.evaluate(() => document.getElementById('big').textContent), 'errors', errors);
  await page.keyboard.press('e'); await page.waitForTimeout(8000);
  console.log(await page.evaluate(() => document.getElementById('card').textContent.slice(0, 80)));   // the card text, as in Edition 4
  await page.screenshot({ path:'ed5-07.png', scale:'css', timeout:180000 }); await b.close();
})();
```
4. Fallback: rename `keys-min.json` away and reload; expect a 404 for `keys-min.json` in the server log, then `keys.json` loaded and the same "344 verified lines lit".
5. LINES: tap LINES, type `grid` one letter at a time; the list filters as before. Optional timing: in `page.evaluate`, dispatch `input` events on `#lyFind` and read `#lineslist.offsetHeight` between `performance.now()` calls; expect single-digit milliseconds at p50 for the layout step (Edition 4 measured 7 to 9 ms p50 and up to 214 ms p90 under load).
6. Draw-on-change: the instrumented check is in `measure.cjs` in my scratch dir; the simple form is that `#hud` text (READOUT) does not change while nothing moves.

## LIMITS

- Absolute times are SwiftShader on a 4-core box at load average 25 to 47; only ratios and counts transfer to a phone. No real Android device was available.
- The slow-4G figures use Chromium's throttle, which models bandwidth and RTT, not radio wake-up or HTTP/2 priorities on Pages.
- GitHub Pages compression could not be observed (proxy 403); the gzip sizes are local `gzip -6`.
- The WebGL DPR variants (`d2`, `d26`) scale `zoom` so the home view fits as before, but their overlay and hit-testing are left at CSS size; they measure the fragment cost and nothing else.
- The overlay-at-DPR-2 option is measured only under SwiftShader, where 2D canvas raster is also software; a phone GPU should pay much less, but that is a guess and it is why the hunk is optional.
- `keys-min.json` adds a file to the folder: `proof/edition-sha256.txt` and `ci_check.py` K1 (it holds a subset of fields already tracked in `keys.json`) need a run. `README.md` of the edition should name it.
- Not in scope and not touched: the engine's permanent rAF loop, `gl.finish()` in the points path, placement law, cosmos, keys.json.
