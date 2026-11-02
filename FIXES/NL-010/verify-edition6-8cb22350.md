# Verify: Kuiper Edition 6 as served at kuiper-belt 8cb22350 (OPUS-VERIFY-6, 2026-11-02 04:22 UTC)

## What was measured

- Source: clean worktree of kuiper-belt commit `8cb22350ce3d60aa6b5afeae7f20184da7606912` ("Publish Kuiper Edition 6
  (202611020326): the GridAtlas bar"), equal to `origin/main` at fetch time, served from `/tmp/verify-8cb` with
  `python3 -m http.server 8812 --bind 127.0.0.1`. Worktree clean (git status empty) before and after the runs.
- Entry: the pointer `http://127.0.0.1:8812/editions/` (redirects to `202611020326/`; the page reported
  "Kuiper Edition 6 · 344 verified lines lit" on both devices).
- Served hashes, read over HTTP before the runs (all equal to the edition's own `proof/edition-sha256.txt`):
  - `editions/202611020326/modules.json` sha256 `63ef6c4faf7a806e4eeb3599b14f6fc7c4673af980a194aebbab92fe7ce4e69c`;
    order `[hello, kuiper-shell, line-card]`.
  - `editions/202611020326/index.html` sha256 `e6d6f8edf3fdff60a36a992a4d9d22e467256c3a7332c6bc777cc57b77968621`.
  - `editions/index.html` (pointer) sha256 `dc6c8b0ba6c7a3a23f42819e14ab0269daa4ba84a683ccec221f243db2f8f382`.
  - modules served: `kuiper-shell` `2045c51ae1ac…bdf`, `line-card` `e2baeaaaf244…c957c065`, `hello` `ee2130b56e74…7dd53`
    (loader reference `25a16f1d3c3f…6e78`, never fetched).
- Script: OPUS-CONTROLLER's `FIXES/NL-010/tools/controller/journey-6.cjs` (sha256 `c0799771…d05209a5a3`; reads the
  shell's ids: `#kuiper-menu-bar`, ABOUT/WAFER/VIEW panels by `aria-controls`, `.lc-*` card, star strip),
  `node journey-6.cjs http://127.0.0.1:8812/editions/ <outdir> --device "<name>"`, one device per process,
  Playwright headless Chromium with `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader
  --ignore-gpu-blocklist` (the script's own launch flags), default timeouts (180 s per action). No wall-clock timeout.
- Machine load: load average about 7-14 on 4 cores during the runs (lower than the 41-46 of Edition 5's verify).
- Pixel 7 (412x839, dpr 2.625): 03:53:25-04:11:17 UTC. Galaxy S24 (360x780, dpr 3): 04:12:20-04:21:31 UTC.

## Per-step result

journey-6.cjs has 16 steps: G2's 16-step journey with `console` recorded per device instead of as a step, plus
`modules`; it has no `panel-dismiss` step (team 9's script, used for Edition 5, had 18).

| # | step | Pixel 7 | Galaxy S24 | Edition 5 verify (both) |
|---|---|---|---|---|
| 1 | load | PASS (bar one row: 6 titles tops 0×6, 412×34; wafer bbox 45,296-366,618) | PASS (one row, tops 0×6, 360×34; bbox 39,287-320,567) | FAIL (base red) |
| 2 | modules | PASS (admitted hello, kuiper-shell, line-card; refused none; 0 errors so far) | PASS (same) | PASS (hello, line-card) |
| 3 | edition-open | PASS | PASS | PASS |
| 4 | edition-close | PASS | PASS | PASS |
| 5 | lines-open | PASS | PASS | PASS |
| 6 | lines-filter | PASS | PASS | PASS |
| 7 | lines-pick | PASS (card 40 of 344) | PASS (card 40 of 344) | PASS |
| 8 | card-details | PASS (198.4 → 285.2 px = cap 285.3; details open, card scrollHeight 425) | PASS (198.4 → 265.2 = cap 265.2; details open, scrollHeight 458) | PASS |
| 9 | card-close | PASS | PASS | PASS |
| 10 | key-e-1 | PASS | PASS | PASS |
| 11 | key-e-2 | PASS | PASS | PASS |
| 12 | key-e-3 | PASS | PASS | PASS |
| 13 | pinch-drag | PASS (ratio 0.499, drag -90,70 exact; zoom-out moved 0.6/0.6/1.7 px; 321 s) | PASS (ratio 0.505; 0.7/0.8/1.5 px; 224 s) | PASS |
| 14 | spark-tap | PASS (card 323 = law's nearest, 1.6 px) | PASS (card 323, 1.7 px) | PASS |
| 15 | whole-wafer | HARNESS-LIMITED PASS (script: FAIL "wafer not whole on screen: null", its 180 s wafer screenshot timed out; every page condition met: COMMANDS opened under the bar, card closed, no magenta, panel closed; the step frame `14-whole-wafer.png` measured with the script's rule = bbox 45,275-366,597, 322×323, ratio 0.997, lit 0.2230) | PASS (bbox 39,266-320,547, 282×282; 132 s) | PASS |
| 16 | see-through | PASS (SEE THROUGH strip `a` → `../../see-through/`, same tab, opened `/see-through/202611020012/`) | PASS (same) | FAIL (base red) |
| — | console | on the edition page 0 console errors, 0 page errors; 2 entries after the see-through navigation (below) | same | PASS (0, 0) |

Rulings applied (HARNESS on #10): 03:44Z (issuecomment-6568437190) for Pixel 7 whole-wafer: the only failure is the
screenshot timeout and the frame measures whole (ratio 0.997 ≥ 0.95), so HARNESS-LIMITED, counts PASS. 04:00Z
(issuecomment-6568562808) for card-details: on both devices the card reached its height cap with the details shown
inside the card, card open, cap respected; the script itself already passed the step.

Frame check of the method: my re-measure of Pixel 7's `01-load.png` gives bbox 45,296-366,618, lit 0.2236, against
the script's in-page 45,296-366,618, lit 0.2239.

Totals: Pixel 7 16/16 with the 03:44Z ruling (15/16 raw, the one fail is whole-wafer HARNESS-LIMITED); Galaxy S24
16/16 raw. On G2's 16-step journey (modules out, console in): 16/16 on both, against 14/16 at G2 and at Edition 5's verify.

Console and page errors, both devices, identical: `request https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json
net::ERR_TUNNEL_CONNECTION_FAILED` and its console line `Failed to load resource: net::ERR_TUNNEL_CONNECTION_FAILED`.
They are off-page: they come after step 16 navigated to `/see-through/202611020012/`, whose `descent.js:35` fetches
that basemap style, which this sandbox's network cannot reach. The edition folder has no reference to that host, the
load step recorded 0 console errors and the modules step 0 errors so far. Page errors 0 on both. Edition 5 recorded no
off-page entries because it had no SEE THROUGH control to follow.

## Comparison with Edition 5's verify (FIXES/NL-010/verify-edition5-521dca75.md)

Edition 5 (521dca75): 16/18 per device on team 9's script, reds `load` (bar on two rows, tops 6/6/6/39, 75.1 px) and
`see-through` (no control) = the base reds. Edition 6 (8cb22350): both base reds now PASS on both devices: the shell's
bar is one row of six titles at 34 px, and its SEE THROUGH strip opens `../../see-through/`. Every step that was green
on Edition 5 is green (or HARNESS-LIMITED PASS) on Edition 6; `modules` now admits three modules including
`kuiper-shell`. No new red. **Result: PASS (base reds load and see-through PASS, as expected).**

## Limitations

- Different script from Edition 5's verify: journey-6.cjs (16 steps) not team 9's law-gate script (18 steps), so
  `panel-dismiss` was not measured on Edition 6 and `console` is a per-device record, not a step.
- Pixel 7 whole-wafer passes only through the harness ruling: the script's own wafer screenshot timed out (212 s step).
- The see-through page's basemap fetch fails here because of the sandbox network; on GitHub Pages with a normal
  network it may load. This verify does not measure the see-through page itself.
- Local `http.server`, not GitHub Pages; Playwright device emulation with SwiftShader, not real phones; one run per
  device; no `--law` pass, no Pixel 7 landscape.
- Reports and frames: this agent's scratchpad (`verify6/{pixel-7,galaxy-s24}.json`, `out-*/`), working space only.

---
_Generated by [Claude Code](https://claude.ai/code)_
