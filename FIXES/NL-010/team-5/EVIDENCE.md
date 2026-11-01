# NL-010 team 5 EVIDENCE (FABLE-T5B, evidence officer, "law and proof")

Written first, before any step was drafted. Every claim below carries a key `repo@sha path:line`; a line range means the
whole range was read. Heads measured with `git rev-parse HEAD` in `/home/user/estate/<repo>` at 2026-11-01 20:45 UTC:

| repo | sha (short) | full |
|---|---|---|
| gridatlas | 5ec7f62 | 5ec7f62f213e2d20a02e86427daa182c0f38e4a4 |
| kuiper-belt | 018b46a | 018b46aed50f28f7b1882a0dcaba6593ce522beb (main, as the harness notes say) |
| elements | f7a92fb | f7a92fb085c38dcbbd5cb469a66cd5ca61fb95bf |
| testcode | d09c185 | d09c185c8dacbc5c73afb2b0d0d8dad40745a544 |
| globalgrid2050 | c66759f | c66759f0d7ac3489df9158da6eaa1330a37c069f |
| galaxies-wafers | fff6fc6 | fff6fc6ad4f93a15fe8f6456942a1b44e5547105 (last commit 2026-09-15 23:24 +0100) |

Nothing under `/home/user/estate/` was edited. `ci_check.py` was run on a copy of kuiper-belt in the scratchpad.

## 1. GridAtlas RELEASE.md: the eight steps (the lesson for the edition release law, step 9)

Source: `gridatlas@5ec7f62 docs/RELEASE.md` (there is no `RELEASE.md` at the repository root; the brief's name resolves to
`docs/RELEASE.md`, which `AGENTS.md` in this repository also names).

| # | step | key | what the row says, in short |
|---|---|---|---|
| 1 | cut | docs/RELEASE.md:38 | `make-generation.mjs --gen G --version v9.N`; G is a real, later UTC minute; version unused and higher than every recorded one; G's files do not exist yet; budget checked |
| 2 | preview PR | docs/RELEASE.md:39 | `publish-preview.mjs --generation G --push`; change set additive; never the pointer, STATE.md, the loader or `atlas/releases/**`; draft PR; CI size-guard + cartridge-gate green |
| 3 | owner acceptance | docs/RELEASE.md:40 | the owner comments `ACCEPT G` (first line) or adds label `accepted:G`; by an owner login, not a GitHub App, no agent signature, after G's cut time; `REJECT G` withdraws it |
| 4 | release | docs/RELEASE.md:41 | `release-accepted.mjs --generation G --push`; draft release PR; the owner merges it with rebase |
| 5 | live bytes | docs/RELEASE.md:42 | `check-live.mjs --generation G --wait`; the `live-bytes` job of `202608301321-verify-live.yml` passed for main's head |
| 6 | homepage | docs/RELEASE.md:43 | `homepage-bump.mjs label`, `pin` (+ restore point), `deploy`; domain clone sparse |
| 7 | served | docs/RELEASE.md:44 | `check-served.mjs` or the CI `served-homepage` mode; served bytes match the pin byte for byte |
| 8 | rollback | docs/RELEASE.md:45 | `rollback-generation.mjs --release-commit <sha>` (route C); homepage promotes the previous release back |

Rules the scripts enforce: agents never record acceptance (docs/RELEASE.md:49-53); only the owner merges a release, every
PR a draft (:54-55); one budget, no new workflow (:56-58). The release writes only `atlas/current.json` and `STATE.md`
(:147-151), so it is revertable byte for byte. The gate list in order: lint, state identical, verify-compose, proofs,
contract parity with no new FAIL row, rollback dry run (:155-163). The pointer schema and architecture:
`gridatlas@5ec7f62 atlas/current.json:2` (`gridatlas.current.v2`), `:5` (`IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES`),
`:14-21` (`cartridge_order`, six ids), `:31` (a cartridge's `sha256`). Owner acceptance is also the law of this
repository: `neural-link-between-agents AGENTS.md` "never move the live generation, homepage, atlas/current.json or
STATE.md without explicit owner acceptance" (section "On every invocation", item 5) and "No agent may ... declare
`ACCEPT <generation>`" (section "Security model").

## 2. kuiper-belt LAWS.md: the laws (what a Kuiper law looks like: measured, computed, falsifiable)

Source: `kuiper-belt@018b46a LAWS.md`. Preface: "A law that cannot be falsified is not a law" (LAWS.md:3-4).

| law | key | one line |
|---|---|---|
| L1 shepherd computed, never declared | LAWS.md:12-22 | argmax of normalised commits + inbound refs; falsified by a run that does not print both terms |
| L2 semi-major axis = distance from the shepherd | LAWS.md:26-38 | `a = a_min + (a_max - a_min)(1 - 1/(1+hops))`; never placed for looks |
| L3 eccentricity = how erratic the work is | LAWS.md:42-53 | `stdev(gaps)/median(gaps)` clamped; fewer than 3 commits: `e_undefined`, never guessed |
| L4 inclination = divergence from the main line | LAWS.md:57-68 | from resolved references, not names |
| L5 mass = how much there is | LAWS.md:72-78 | bytes, or counted lines at file depth; `radius ∝ log(1+m)` |
| L6 resonance p:q | LAWS.md:82-96 | residual ≤ 0.05 with p,q ≤ 8, else "no resonance"; residual recorded |
| L7 epoch t | LAWS.md:100-107 | positions at t from commits at or before t only |
| L8 openness, the only law that judges | LAWS.md:111-124 | `open` = destination resolved and fetched; `score = dim/all` printed every run |
| L9 reproducibility | LAWS.md:128-135 | identical coordinates on any two machines; seed from the body's own key |
| L10 reconciliation: the bond grants only what its words grant | LAWS.md:139-172 | four verdicts HONOURED / OVERREACHED / NOT EVALUATED / DISCLOSED (:152-157); four rules (:161-168); settled by pinned evidence alone, never recency, seniority or a model's judgement (:146-148) |

The card law the owner asks for ("the line of code is the header") is not yet in LAWS.md: `grep -n -i "header\|card"
LAWS.md` returns nothing at this sha. It is written in the Edition 4 card code only: `editions/202611012027/index.html:655`
(`edCard(i)`) and the README description of the card at `editions/202611012027/README.md:16-19`. Step 1 (team 1) adds it.

## 3. kuiper-belt tools/ci_check.py: the four checks

Source: `kuiper-belt@018b46a tools/ci_check.py`. Docstring: "what GitHub checks on every push, on its own machine, knowing
nothing local ... it fails closed" (tools/ci_check.py:2-7).

| check | key (definition) | key (code) | what |
|---|---|---|---|
| K1 privacy | :8 | :37-48 | every tracked file ≤ 3 MB scanned with `check_proof.leaks` (tools/check_proof.py:47-55: sha256 of every name token against `NOT_PUBLIC` digests) |
| K2 sums | :9 | :50-60 | `cosmos/wafer.tsv` re-summed equals `cosmos/wafer-meta.json` `issued_keys`, `unissued_keys`, `commits`, and equals `cosmos/repos.tsv` |
| K3 syntax | :10 | :62-80 | every `tools/*.py` parses (`ast.parse`); the `<script type="module">` of every `*.html` **at the repository root only** (`os.listdir(ROOT)`, :68) passes `node --check` |
| K4 order | :11 | :82-93 | keys in time order, no negative gap, address space closes against `wafer-meta.json` |

`RESULT: PASS` only if all pass (:95-98). Measured run (copy of the repository at 018b46a, `python3 -I tools/ci_check.py`,
2026-11-01 20:53 UTC): `K1 privacy: 526 tracked files scanned, 0 match a private digest`; `K2 sums: issued 45,735,836,396,
meta 45,735,836,396, repositories 45,735,836,396, silent 17,604,284,400, commits 13344: agree`; `K3 syntax: 14 tools, 5 pages`;
`K4 order: 0 commits out of order or overlapping; address space 63,340,120,796 vs 63,340,120,796`; `RESULT: PASS`.

Finding for step 9 (not a claim about intent, a measurement): K3 parses 5 pages, all at the root. `editions/*/index.html`
and `see-through/*/index.html` are not parsed by CI (tools/ci_check.py:68 lists `ROOT` only). The edition page is the one
every edition changes. The release law for editions must therefore add an edition check (parse `editions/<stamp>/index.html`,
check the pointer's three places, re-hash `proof/edition-sha256.txt`) or the law "keep every page parseable" (harness notes,
"Rules that bind every edition", last bullet) is enforced by nobody but the agent.

The measuring-machine engineer that CI cannot run: `tools/check_proof.py:7-14` (C1 live, C2 sums, C3 privacy, C4 PROOF.md
disclaimer, C5 three random keys resolve by git alone, C6 a second opinion that can never pass or fail a proof by itself).

## 4. The editions pointer and the folder rule

- Pointer: `kuiper-belt@018b46a editions/index.html:7` (`<meta http-equiv="refresh" content="0; url=202611012027/">`), `:11`
  (the link `href="202611012027/"`), `:12` (`location.replace('202611012027/' + location.hash)`). Three places, one stamp,
  no `/belt/`.
- The rule in words: `editions/README.md:3-4` (numbered in order of publication, keyed by cut stamp; "The number is for people;
  the stamp is the key"; current edition Kuiper Edition 4), `:6-10` (stable link opens the newest dated folder; stamp written
  in three places; earlier folders unchanged; find the newest from the pointer, not by sorting names).
- The repository README's Editions section: `README.md:189-196`.
- Edition 4 folder contents (measured `ls`): `index.html` (61,653 bytes), `keys.json`, `README.md`, `NOTICE.md`,
  `proof/edition-sha256.txt` (8 lines, sha256 of every file except itself), `proof/keys-summary.json` (`bodies 346`,
  `on_wafer 344`, `verified 344`), `proof/render-desk-card-1280x800.png`, `proof/render-phone-card.png`,
  `proof/render-phone-card-details.png`.
- Edition layer hooks in `editions/202611012027/index.html`: `:201` loads `../../cosmos/repos.tsv` and `../../cosmos/wafer.tsv`;
  `:240` the refusal when wafer.tsv does not load ("The wafer will not invent its keys"); `:627-628` `EDPATH = 'keys.json'`,
  `loadEdition()`; `:640` `drawEdition()`; `:655` `edCard(i)`; `:676` `edFly(b)`; `:682` `edNext(step)`; `:699-703` the bar
  (`KUIPER EDITION 4`, buttons `edition`, `readout`, `lines`, `commands`); `:705-709` the LINES panel (`#lyAll`, `#lyFocus`,
  `#lyFind`, `#lineslist`); `:710` `PANELS`; `:712` `placePanels()`; `:714` `setPanel(name)`; `:726` `safeBox` wrapped to
  start under `#bar`.
- See Through's own pointer, same pattern: `see-through/index.html:7,11,12` → `202610050609/`. Learn the Kuiper's too
  (`editions/README.md:8-9` names it as the model).

## 5. Licence files, verified from the files

### kuiper-belt (the Kuiper, the editions, See Through, Learn the Kuiper live here)
- `kuiper-belt@018b46a LICENSE:1-3` Apache License Version 2.0 (202 lines, sha256 `fdeda10cf13d92cb…`). GitHub API
  `license.spdx_id` = `Apache-2.0` (gh api repos/Ventusltd/kuiper-belt, 20:49 UTC).
- `README.md:156-157`: "Code is licensed under Apache-2.0, see LICENSE; documentation and generated data under CC BY 4.0."
  `README.md:152-153`: every input carries its source and licence inside the file it produces.
- `editions/README.md:27`: "Code Apache-2.0, text and data CC BY 4.0, as the repository."
- `editions/202611012027/NOTICE.md:3-5` (code Apache-2.0, docs/register/proof CC BY 4.0), `:7-10` (every quoted line keeps its
  repository's licence: Apache-2.0, CERN-OHL-S v2 for globalgrid2050-derived material and see-through, CC BY 4.0, ODbL 1.0,
  OGL v3; "A quote here is a citation with its key, not a relicensing"), `:12-14` (Vogel 1979, Knuth TAOCP 3 §6.4).

### see-through (the star player): CERN-OHL-S v2 code, ODbL data, BSD-3 MapLibre
- Folder pointer: `see-through/index.html:7,11,12` → `202610050609/` (newest dated folder; `README.md:23-25` says the stable
  link always opens the newest dated folder and earlier folders are kept unchanged).
- `see-through/README.md:27-36` "Credits and licences": CERN-OHL-S v2 (see `LICENSE.md` in each dated folder); OSM ODbL 1.0;
  CARTO, Esri, AWS Terrain; MapLibre BSD-3-Clause; the placement rule after Vogel and Knuth.
- `see-through/202610050609/LICENSE.md:1-10`: reuses globalgrid2050 simulator code (place-frame.mjs, pylons-real.js,
  substations.js, the method of overlay.html, wire-look.js, morph.js, perf.js) licensed CERN-OHL-S v2 (strongly reciprocal);
  See Through "is a separate app built on that code and is offered under the same licence"; full text
  `licences/globalgrid2050-CERN-OHL-S-2.0.txt`; data and libraries keep their own terms (:9-10).
- `see-through/202610050609/NOTICE.md:3` (offered under CERN-OHL-S v2), `:8-16` the table of reused files and their licences
  (`descent.js` from Learn the Kuiper; `pf.js` from `energy-transition-simulator/202609282123/place-frame.mjs` at c5ac5219;
  `data/substations-footprints.odbl.json` ODbL 1.0), `:22-27` OpenStreetMap ODbL 1.0 and the GridAtlas atlas-v9 line files
  (OSM-derived, ODbL, loaded at run time), `:28-34` CARTO, Esri World Imagery, AWS Terrain Tiles with the Environment Agency
  credit, `:38-39` MapLibre GL JS 4.7.1 BSD-3-Clause (`vendor/MAPLIBRE-LICENSE.txt`), `:43-44` network use (tiles, the
  GridAtlas line files, one Overpass query; no account, key or tracking).
- `see-through/202610050609/licences/globalgrid2050-CERN-OHL-S-2.0.txt:1` ("This project is licensed under the CERN Open
  Hardware Licence Version 2 - Strongly Reciprocal (CERN OHL-S v2)"), 15,156 bytes. Origin:
  `globalgrid2050@c66759f LICENSE.txt:1-5` (the same header, dated 2026-04-03).
- `see-through/202610050609/vendor/MAPLIBRE-LICENSE.txt:1` ("Copyright (c) 2023, MapLibre contributors").
- The two earlier dated folders `202610050356` and `202610050513` carry the same three files (`LICENSE.md`, `NOTICE.md`,
  `licences/`), measured with `find`.
- Because `descent.js` and `kuiper-law.js` come from Learn the Kuiper: `learn-the-kuiper/202610050609/NOTICE.md:7-11` (code
  Apache-2.0, docs and data CC BY 4.0; `modules/grid.js` and `modules/zoom.js` adapted from globalgrid2050 under CERN-OHL-S v2).
  See Through relicenses nothing: it states CERN-OHL-S v2 for the whole folder because the simulator code it builds on is
  CERN-OHL-S v2 (LICENSE.md:5-6).

Consequence for the roadmap: anything the Kuiper copies **out of** See Through (its descent, its 3D model code) carries
CERN-OHL-S v2 into the edition. Linking to See Through (a button, a deep link) carries nothing. Steps 5-6 must say which.

### gridatlas: Apache-2.0 code; third-party data excluded by its own NOTICE
- `gridatlas@5ec7f62 LICENSE:2-4` Apache License Version 2.0 (202 lines, sha256 `cfc7749b96f63bd3…`). GitHub API
  `license.spdx_id` = `Apache-2.0`.
- `NOTICE:1-12` (Copyright 2026 Ventus Ltd, Apache-2.0), `:17-23` why Apache (patent grant, attribution travels), `:25-32`
  "WHAT THIS LICENCE DOES NOT COVER": third-party data (DESNZ REPD, NESO ETYS appendices, OpenStreetMap, CARTO basemaps,
  Open Charge Map) keeps its own terms. `README.md` carries no licence word (`grep -i licen` empty); the NOTICE is the
  statement.
- Consequence: the GridAtlas **UI** (menu bar module `atlas/modules/202609031958-menu-bar.js`, the shell, the wordmark CSS)
  may be copied into the Kuiper under Apache-2.0 with the NOTICE attribution carried. GridAtlas **data** (line files) stays
  ODbL and is already credited by See Through (`see-through/202610050609/NOTICE.md:26-27`).

### testcode (the spider sandbox `testcode/spider/` and `testcode/spider-lab/` live inside it): Apache-2.0
- `testcode@d09c185 LICENSE:2-4` Apache License Version 2.0 (202 lines, sha256 `cfc7749b96f63bd3…`, byte-identical to
  gridatlas/LICENSE). `NOTICE:1-12` (testcode, Copyright 2026 Ventus Ltd, Apache-2.0; "The test code engine").
  GitHub API for testcode was not reachable from this session (403, repository not attached), so the file is the evidence.
- `testcode/spider/INDEX.md:1-5` (five timestamped builds, published by the MSI lab 2026-09-14 14:32:03 UTC, each reading
  live GlobalGrid2050 data over https), `:7-13` the five versions, `:15-16` the front door (`?graph=overview&focus=...`, 15
  graphs). `grep -i licen` on `spider/INDEX.md` and on `spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/index.html`
  is empty: the spider carries no licence file of its own and is covered by the repository's `LICENSE`/`NOTICE`. v5 folder
  files: `index.html`, `spider/identity.json`, `spider/manifest.json`, `spider/overview-graph.json` (measured `ls`).
- Consequence: the spider dashboard may be embedded or linked under Apache-2.0 with testcode's NOTICE carried; the data it
  reads at run time (globalgrid2050 catalogue over https) keeps its own terms, which the spider itself does not state.

### elements (the periodic table): NO LICENCE FILE, licence UNVERIFIED
- `elements@f7a92fb`: 25 tracked files (`git ls-files | wc -l`); no `LICENSE`, no `NOTICE`; `grep -rn -i "licen|apache|copyright"`
  over every tracked file returns nothing (the only hit is a git sample hook). `README.md:1-25`, `ELEMENTS.md`, `APPS.md`,
  `CATALOGUE.md`, `SURFACES.md`, `catalogue/*.json`, `build/build_catalogue.py`, `tests/` carry no licence word.
- GitHub API `repos/Ventusltd/elements` was not reachable from this session (403, repository not attached), so the
  repository's licence metadata could not be read either.
- What elements is: `README.md:9-17` (every element, app and function with more than 10 lines has a key the estate already
  uses: `block:<Sym>` elements and apps, `surface:<url>`, `family:<n>`, `line:<n>`); `CATALOGUE.md:7-8` (244 elements, 7 apps);
  `APPS.md:3` (built 2026-09-15T19:18:47Z from the block register sha256 `d356562b2e8f` and the numbered database of 250,174
  lines), `:7-13` the seven apps (`block:Ra`, `Cg`, `Sb`, `St`, `Pn`, `Gp`, `Wf`); `catalogue/provenance.json:2-14` (rule and
  register URL `https://ventusltd.github.io/stars/blocks/blocks.json`, bytes 403,894, copy under `inputs/`).
- Verdict under L10: `DISCLOSED`. The periodic table's licence is an open question for the owner (question Q1 below). Until the
  owner adds a LICENSE (Apache-2.0 would match every sibling repository, but that is a choice, not a fact), the roadmap may
  **link** to the catalogue (keys and titles, which are the estate's own) and must not **copy** its text into the edition.

### galaxies-wafers (the wafer that predates the Kuiper, Phase 2): no licence file either
- `galaxies-wafers@fff6fc6`: no `LICENSE`/`NOTICE` in the root listing; `grep -i licen README.md` empty. Phase 2 compares it
  by measurement (numbers, not copied code), which needs no licence; copying `wafer.mjs` would. Owner question Q2.

### ODbL and CC BY 4.0, where each is stated
- ODbL 1.0: `see-through/202610050609/NOTICE.md:16,22-27`; `editions/202611012027/NOTICE.md:9`; `gridatlas NOTICE:30` (OSM
  named as excluded third-party data).
- CC BY 4.0: `kuiper-belt README.md:157`; `editions/README.md:27`; `editions/202611012027/NOTICE.md:4-5`;
  `learn-the-kuiper/202610050609/NOTICE.md:7-8`.

## 6. Keys the other teams will need and this officer checked (for the consolidation)

GridAtlas shell (team 1): `gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:31` (`MENUS = ['File', 'Edit', 'View',
'Scope', 'Grid', 'About']`), `:34` (`EXPECTED_LAYER_CONTROLS = 63`), `:8-12` (the stricter admission rule; the Grid menu
proxies the 63 original inputs), `:157` (missing `'63 unique layer controls'` is a refusal), `:184-191` (the VENTUS masthead
fused into the centre of the same 36 px strip, "The VENTUS logo is the best part"), `:192-205` (`.gm-brand-slot` max-width
64 %, `.ventus-main` 14 px weight 800 letter-spacing .2em, `.ventus-sub` 5.5 px), `:377-378` (phone sizes 11 px / 4.5 px).
The logo is a **text wordmark**, not an image file: `atlas/releases/202608300453-atlas-v9/index.html:113-118` (`.scada-brand`:
"Ventus", "Cables &amp; Connectivity&reg;", "globalgrid2050.com | open infrastructure intelligence") and `:18,30`
(`.ventus-main` "Ventus"). `find -iname "*logo*"` in gridatlas (outside node_modules) returns no file.

Layers (team 2): `atlas/current.json:5,14-21,31` above; `menu-bar.js:421-426` (proxy mirrors the original control's checked,
disabled and label), `:1442` (`data-gridatlas-layer-proxy`).

See Through and File (team 3): section 5 above; the homepage's presentation `globalgrid2050@c66759f
homepage_versions/homepage_v134.html:18` (entity `see-through` inside the Kuiper group, "Open See Through →" to
`kuiper-belt/see-through/202610050609/`) and `:35` (table row, type `application`, "no connection probability is calculated
today" in the text at :18). NL-009 round 1 at 20:52 UTC holds one file, `FIXES/NL-009/round1/06-seethrough.md`: finding 1
BLOCKER, See Through unreachable from Edition 4 (`grep -ci "see.through"` 0 in index.html and README.md), fixed by a fifth
bar entry `a.gm-title[href="../../see-through/"]` 101×29 px on Pixel 7, same tab, back gesture returns (lines 11-22);
finding 2 MAJOR, the bar is two rows: 439 px of items against 412 px (Pixel 7) and 360 px (Galaxy S24), 544 px with SEE
THROUGH; one row at 360 px needs the five titles ≤ 328 px (lines 24-32). Other auditors' files were not yet present; the
consolidator re-reads the folder before writing ROADMAP.md.

OS of the estate (team 4): elements keys above; `testcode/spider/INDEX.md:15-16`; `kuiper-belt SPEC.md:75` ("Registration with
the Spider" heading) and `NEXT.md:11-16` (19,257 bodies, 66 repositories, 41,658 tracked paths, 250,174 numbered lines,
245,170 placed, generator `tools/estate.py`, state at 2026-09-19).

## 7. Phase 2 keys (Addendum 1): what the live wafer counts, and the wafer that predates the Kuiper

Current wafer (kuiper-belt@018b46a):
- `cosmos/wafer-meta.json:2` issued_keys 45,735,836,396; `:3` unissued_keys 17,604,284,400; `:4` address_space
  63,340,120,796; `:5` silence_share 0.2779; `:6` commits 13,344; `:7` repositories 98; `:8-9` first_unix 1748560273,
  last_unix 1793539112; `:10-11` gap_keys_per_second 600, cap_seconds 1,209,600; `:12` law
  `r = sqrt(key), theta = 2 pi frac(key x 2654435769 / 2^32)`.
- `cosmos/wafer.tsv:1` header `unix lines repo_index sha12 gap_before`; 13,344 data rows (measured). `cosmos/repos.tsv:1` header
  `repo_index name lines`; 98 data rows (measured; row 0 `faraday 240995`, row 1 `law 15397`).
- The sums agree: ci_check K2 line quoted in section 3.
- What is counted: one issued key per line in every file in every commit (`tools/wafer_keys.py:10`); unissued keys = 600 per
  second of silence capped at a fortnight (`:11,33-34`). A blob with a NUL byte in its first 8,000 bytes is binary: counted
  as a blob, excluded from line totals (`tools/count_lines.py:14`; the same rule in `tools/harvest.py:77-78`, "not text: it
  has no lines"); line = `\n` count plus one for an unterminated last line (`tools/harvest.py:80`). `tools/key.py:49` ("sha ->
  lines for text blobs, measured earlier. Never trusted blind"). Three numbers never conflated: head 25,335,587 lines measured
  2026-09-19, history never counted, authored (`tools/count_lines.py:10-12`). Which repositories: the 98 named in
  `cosmos/repos.tsv` (public ones; `tools/wafer_keys.py:20` "redacted where not public"). Branches: the shards are commits
  "in every repository ... in one order, by its own timestamp" (`:5-7`); whether every branch or only main is walked is not
  stated in these lines and is an open question for team 4's step 8b (Q4).

The wafer that predates the Kuiper (galaxies-wafers@fff6fc6, and its parent globalgrid2050@c66759f testcode/202609151339):
- Law: `galaxies-wafers wafer.mjs:43` `GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5))`; `:44-49` `SUBSTRATE` id `wafer.v1`, law
  `r = sqrt(key); theta = key * goldenAngle`, `frozen_utc 2026-09-15T15:00:00Z`, "Never changes. New arrangements are new
  substrates"; `:52-54` `place(key)`; `:69` `extent = sqrt(max)`. `README.md:5` ("every permanently numbered line of the
  estate placed by one frozen law ... inherited unchanged from testcode/202609151339"); `README.md:11-18` the layer format
  (geometry carries permanent keys, never coordinates).
- Counts: `app.mjs:4-5` "There are 250,174 of them and they are numbered 1 to 342,795"; `app.mjs:12` `r = SPACING * sqrt(key)
  theta = key * GOLDEN`; `app.mjs:59` the numbered database at `https://globalgrid2050.com/testcode/202609142202/data/`;
  `app.mjs:138-139` the on-screen count line (numbered lines, 1 to max, carried by a family). Parent:
  `globalgrid2050@c66759f testcode/202609151339/README.md:9` ("250,174 lines are numbered 1 to 342,795 ... numbers missing
  from the sequence were never issued"). The same 250,174 is the denominator of elements (`elements APPS.md:3`).
- Layers that already exist on the old wafer, for the comparison: `galaxies-wafers layers/manifest.json:2-3` (substrate
  `wafer.v1`, built 2026-09-15T16:17:31Z); files `layers/periodic-table.json`, `layers/spider.json`, `layers/blocks.json`,
  `layers/sld-sandbox.json`, `layers/deeplink.json` among 16 (measured `ls`). `iterations/index.json:3` count 42.
- The later development environment: `globalgrid2050@c66759f testcode/wafer-development-environment/` holds 40 dated folders
  from `202609162333-estate` to `202609191355-proof-8` (measured `ls`); the Kuiper's own first home was
  `.../202609190230-kuiper-belt/` (`kuiper-belt NEXT.md:8`), not present in this clone's listing.
- The two laws differ in the angle: the old wafer multiplies the key by the golden angle (`wafer.mjs:46`); the Kuiper takes
  `2 pi frac(key x 2654435769 / 2^32)` (`wafer-meta.json:12`), Knuth's multiplier (`editions/202611012027/NOTICE.md:13`). The
  radii agree (`sqrt(key)`). The comparison in Phase 2 must state this before any count is compared.

## 8. Open questions this evidence raises for the owner (carried into ROADMAP.md)

- Q1 elements has no LICENSE or NOTICE file at f7a92fb. Which licence? (Every sibling is Apache-2.0 code / CC BY 4.0 text.)
- Q2 galaxies-wafers has no LICENSE or NOTICE file at fff6fc6. Same question, needed only if its code (not its numbers) is reused.
- Q3 CI K3 does not parse edition pages (ci_check.py:68). May the edition release law add an edition check to `ci_check.py`
  (a new K5), or must it stay a separate tool so `ci_check.py` is unchanged?
- Q4 For the overarching Kuiper: every branch or only main; private repositories counted but unnamed (as the K1 digests imply)
  or excluded; binaries named-not-placed (count_lines.py:14) or counted in bytes (LAWS.md:74).
