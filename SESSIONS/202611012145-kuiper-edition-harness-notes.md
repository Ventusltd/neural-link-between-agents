# Session notes: Kuiper edition harness (owner session, 31 Oct – 1 Nov 2026)

Written so the harness can free its context window and read these notes back. Everything a resuming agent needs is
here or linked. Owner: Vikram Kumar, Ventus Ltd. Owner's standing preferences: replies in plain flowing text, no
markdown, no headers, no bold, no bullet lists, no files unless asked; be brief.

## Mission so far

1. NL-006 (issue #6): a harness of 5 Fable controllers and 20 Opus workers mapped the whole estate (25 repositories
   cloned under `/home/user/estate/<repo>`) against the Kuiper code, focus gridatlas and data centres, and cut
   Kuiper Edition 1 (`pipelinenews/kuiper-edition/202610311905`, 354 register rows, 346 distinct lines, five chapters,
   proofs). Law: no claim without a key (`repo@sha path:line`).
2. NL-007 (issue #7): five Fable agents discussed in three rounds and committed the fix plan
   `FIXES/202610311905-datacentre-baseline.md` plus `FIXES/202610311905/patches/01–12`. Twenty Opus agents in ten
   pairs implemented it: data-grid-gb PR #7 (dc-a7 operator_match via `_op_core`, 227→226 records), gridatlas PR #80
   (preview, owner posted `ACCEPT 202610312138` there) and PR #81 (release; live 202610312138 v9.188),
   globalgrid2050-homepage PR #4, globalgrid2050 PR #49 (pin; restore point v135). Follow-up issues: data-grid-gb #8,
   gridatlas #82, homepage #5 (language gate "measured", pre-existing on main; MSI runner offline).
3. NL-008 (issue #8): five Fable QA agents. Findings fixed (CRLF, machine paths scrubbed, PR body prose). Governance
   finding recorded: the harness merged release PRs on chat authorisation against RELEASE.md "only the owner merges".
4. Kuiper editions published to GitHub Pages from `Ventusltd/kuiper-belt`:
   - Edition 1 `editions/202610311905` (own belt viewer; owner said the real Kuiper looked far better).
   - Edition 2 `editions/202611010114` (the real wafer engine with the verified lines as green sparks at their own
     keys; `tools/edition_keys.py`; 344 of 346 placed, 2 star-maker lines not on the wafer; 12/12 key.py round trips).
   - Edition 3 `editions/202611012022` (text moved into layers behind a GridAtlas-style menu bar: EDITION, READOUT,
     LINES, COMMANDS).
   - Edition 4 `editions/202611012027` (compact card, camera places the spark in clear space, LINES closes on pick,
     stable pointer fixed: it had carried Edition 1's `/belt/`). Live: https://ventusltd.github.io/kuiper-belt/editions/
     kuiper-belt main at 018b46aed50f28f7b1882a0dcaba6593ce522beb.

## Owner's latest instruction (1 Nov 2026, after seeing Edition 4)

"Summon 10 x fable agents to fix the UI well and put in See through as a button too, it's an app not covered well.
The issue is on mobile, test Android." Then move these notes to the neural link, free the context, read the notes again.
That work is NL-009 (issue to be opened in this repository). Outcome is Kuiper Edition 5, a new dated folder.

## Rules that bind every edition (do not relearn these)

- Folder rule: every change is a new dated folder `editions/YYYYMMDDHHMM` (UTC cut stamp); earlier folders are never
  edited. Version number = order of publication (Edition 5 next). The pointer `editions/index.html` names the stamp in
  three places (meta refresh, link, `location.replace`) and must point at `<stamp>/` (no `/belt/`).
- `editions/README.md` and the Editions section of the repository `README.md` get a new entry each time; the "current
  edition" sentence in `editions/README.md` is updated.
- Each folder: `index.html` (engine copy + edition layer), `keys.json` (byte-identical since Edition 2 unless the
  findings change), `README.md` with a "What changed from Edition N" section, `NOTICE.md`, `proof/edition-sha256.txt`
  (sha256 of every file except itself), `proof/keys-summary.json`, `proof/render-*.png`.
- The page loads `../../cosmos/repos.tsv` and `../../cosmos/wafer.tsv`; serve from the repository root to test.
- Before pushing kuiper-belt main: `python3 tools/ci_check.py` must print `RESULT: PASS`. Work on a branch
  `edition/<stamp>`, merge `--no-ff` into main, push main and the branch. Then watch GitHub Pages:
  `gh api "repos/Ventusltd/kuiper-belt/actions/runs?head_sha=<sha>&per_page=5"` until "pages build and deployment"
  is `completed success`. The sandbox cannot fetch github.io pages (proxy block), so verify by the run, not by curl.
- Test renders: Playwright with the pre-installed Chromium, flags `--use-gl=angle --use-angle=swiftshader
  --enable-unsafe-swiftshader --ignore-gpu-blocklist`; the wafer is slow under SwiftShader, so wait 6–8 s after
  load and after each fly, and give screenshots a 180 s timeout. Serve with `python3 -m http.server` from the
  kuiper-belt root. Earlier scripts: `/tmp/ed3-check.cjs`, `/tmp/ed3-phone.cjs`, `/tmp/ed4-check.cjs` (may be gone;
  write fresh ones in the scratchpad). For Android use Playwright's `devices['Pixel 7']` (or 5) with `hasTouch`,
  `isMobile`, `deviceScaleFactor`, and test real touch: `page.touchscreen.tap`, pinch via CDP `Input.synthesizeTouch`
  or dispatched pointer events.
- Edition layer essentials inside `index.html` (search for them): `loadEdition()`, `edPlaced` (uses
  `Object.assign({}, b, {x,y})`, order matters), `drawEdition()` wrapped into `draw`, `edCard(i)`, `edFly(b)`,
  `edNext(step)`, `setPanel(name)`, `placePanels()`, `safeBox` wrapped to start under `#bar`, `#lines` panel with
  `#lyAll`, `#lyFocus`, `#lyFind`, `#lineslist`, keys `e`/`E`, `n`, `r`, `/`, Backspace, Escape.
- GitHub posts carry the footer `---` newline `_Generated by [Claude Code](https://claude.ai/code)_`. Neural-link
  envelope per `PROTOCOL.md`. Agents never post ACCEPT; the owner does.
- The kuiper-belt `tools/ci_check.py` K1 privacy check scans tracked files for private digests; K3 checks page
  syntax; keep every page parseable.

## See Through (the app to add as a button)

`kuiper-belt/see-through/` is an app in the same repository: "from the stars to one substation in 3D", 5,800 UK
substations, MapLibre, satellite and terrain, CERN-OHL-S v2. Stable link https://ventusltd.github.io/kuiper-belt/see-through/
(pointer currently to `202610050609/`). The globalgrid2050 homepage lists it as entity `see-through`, "an application".
The owner says it is "not covered well": the edition's menu bar should carry a SEE THROUGH button that opens it
(`../../see-through/` relative to the edition folder keeps it on the same host), and the edition's README and the
EDITION panel should name it. Consider also a KUIPER / LEARN button set so the family of apps is reachable from one
bar, as the homepage does; keep the bar to one row on a phone.

## Known UI problems on mobile (owner screenshots, Android phone)

- Edition 2: HUD and subtitle took most of the screen (fixed in 3 by layers).
- Edition 3/4: the bar wraps to two rows at 393 px because the title "KUIPER EDITION n" plus four buttons do not fit;
  after "next verified line" the card covered the lower third and the spark could sit under it (Edition 4 reduced the
  card and moved the camera, but the owner has not yet confirmed it is good; assume more is needed).
- Not yet tested at all: real touch (pinch zoom vs page zoom, drag vs scroll, tap on a 4 px spark), Android Chrome's
  dynamic toolbar (100vh vs dvh), safe areas, landscape, font scaling, the LINES list on a small screen, the
  "details" toggle, the × hit target, the GitHub link opening a new tab, the back gesture closing a panel.

## Where things are on this machine (may not survive a new container)

- `/home/user/estate/kuiper-belt` (main, clean after Edition 4), `/home/user/estate/<repo>` for the other 24,
  `/home/user/neural-link-between-agents` (main), `/home/user/pipelinenews` (branch kuiper-edition-202610311905),
  `/home/user/globalgrid2050-homepage`, `/home/user/gg-domain`.
- Stamps: S2=202611010114, S3=202611012022, S4=202611012027.
- Remotes use the proxy; `gh api` works for Actions runs and issue comments; GitHub MCP tools work for PRs/issues.

## Offered, not requested

Putting the Kuiper edition on the globalgrid2050.com homepage (label → pin → deploy cycle, RELEASE.md steps).
