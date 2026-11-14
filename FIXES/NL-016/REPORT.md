# Team 4 REPORT: NL-016, maps (GridAtlas October preview and the legacy globalgrid2050 atlas pages)

Master: Claude Opus, 14 Nov 2026, 00:25 to about 01:30 UTC. Public copy: `FIXES/NL-016/` (this file, APPLY.md,
PR-DESCRIPTION-gridatlas-P1.md, gridatlas/, globalgrid2050/). Working files: `<workspace>/teams/4/a` (GridAtlas) and
`<workspace>/teams/4/b` (pages).

**Workers:** none launched. This session has no Agent or Task tool (ToolSearch for it returns only SendMessage, TaskStop and
similar). The brief allows "do that piece yourself", so the master did all nine pieces (A1 to A5, B1 to B4) alone.

Nothing was committed, pushed, merged, dispatched or accepted. No file was edited in `<workspace>/gridatlas`, `<workspace>/gg-wt`
or any other clone. GridAtlas work ran in plain copies (`a/work`, `a/work-split`). In the P1 copy, `atlas/current.json`,
`STATE.md`, `atlas/index.html` and `atlas/releases/**` are byte-identical to the clone (checked with cmp and diff -rq).

## A. GridAtlas (clone 41729af, live 202610312138, preview 202611132345 v9.189)

### A.1 The three failing pr-gate checks: all explained, two fixed
- **overlay-engine test 80 (H3/I1/J2), both modules.** Clock rot. The test pins a flash at 2026-10-25T11:15:58Z and selects the
  7D window, so from about 1 Nov 2026 the flash is outside the window and no card opens. It fails on main today, which makes every
  gridatlas PR gate red. `gridatlas/logs/test80-98-matrix.log`: the original fails at real time and passes with the clock set to
  2026-10-26 (`tools/clockshift.mjs` preload). Fix: the flash is placed 2 h before now and the expected string is computed.
- **overlay-engine test 98 (J3), both modules.** The regex `COLLECTOR LAST RAN \d\d:\d\d UTC` has no optional date. The module
  adds a date when the collector run (now − 10 min) falls on the previous UTC day, so the test fails only from 00:00 to 00:10
  UTC. The B10 run was at 00:04. The original fails with the clock at 2026-11-15T00:05Z and passes at 00:48 real time. Fix: an
  optional date group, the same form the same regex already uses for SEARCHED TO. With the fixed file, all 207 tests pass at real
  time and at 00:05 on both the live module (202610291043) and the preview module. Standalone patch:
  `gridatlas/patch-0-lightning-test-clock-fix.diff`; `git apply --check` passes on 41729af.
- **proof 202611132345-uk-lightning-overlay** (`uk-gazetteer-flyto differs from 202610291043`). `tools/proofs/lightning-cartridge.mjs`
  checks arrival parity against a monolithic reference. Every script before sld-sandbox must be identical, and
  sld(R) + '\n' + overlay(G) must equal sld(R). A data re-pin changes the gazetteer, which precedes sld-sandbox, and the
  lightning module. No reference with the new gazetteer exists. This is not a data defect. With the tests fixed, the 27-file
  build gives 21/22 with only this FAIL (`logs/full-pr-gate-testsfixed.log`).
  Resolution: **split the release.** P1 (22 files) leaves lightning unchanged and gives **19/19 PASS**
  (`logs/P1-pr-gate.log`). A later lightning-only cut through `tools/lightning/make-generation.mjs` then passes the proof as
  designed. The alternative, amending the proof, is an owner decision.

How P1 was made: the B10 build minus the lightning module, its proof and the lightning src and registry edits. In both
manifests the lightning entry is replaced by the live entry (generation 202610312138, module 202610291043).
`atlas/v/202611132345/current.json` is re-derived with `tools/release/lib.mjs` (`deriveCurrent` + `rerootForPreview`), and the
composition note is reworded. The gazetteer and offtakers proofs pass. Data-contract parity shows the same 3 known FAIL rows as
base. The P1 diff (`gridatlas/gridatlas-P1-repd-2026q3-preview.diff`, data files excluded) applies to 41729af. The data files and
the full tree are in `<workspace>/teams/4/a/P1-files` (sha256 in `gridatlas/P1-files.sha256`).

One inconsistency in the 27-file manifest: the lightning entry's `uk_lightning.module` still names `202610291043` while its
`path` is the 202611132345 module. P1 avoids it.

### A.2 Capacity precision: settled
`tools/m5_precision_evidence.py`, an offline replica of the module's RpQ/RpZ/RpJ join, reproduces all three figures exactly.
The drawn register is globalgrid2050 `dist/repd_master.json` (= data-gridatlas repd_master_v8_oracle), 10,784 rows, sha256
`ca5da437…`.
- Q2 202608290716: **10,503**. October at CSV precision: **10,423**. October at XLSX precision: **8,973** (10,423 − 1,450). That
  is, 1,450 joins break because the XLSX value differs from the CSV value (0.384 vs 0.38, 24.995 vs 25, 0.579 vs 0.58).
- The register's capacities have at most 3 decimals (0 dp 4,380, 1 dp 3,527, 2 dp 2,872, 3 dp 5), so only CSV precision can
  match them.
- The −80 against Q2 is register change, not precision: 86 lost (45 refs no longer active, 24 MW changed, 12 points moved,
  4 names changed, 1 point and MW) and 6 gained. Examples are in `logs/m5-precision-evidence.json`.
- **Rule:** compile GridAtlas from the CSV-precision cleaned file (`repd-2026q3.csv`, `d937ae16…`), never from XLSX or staged
  values. The preview already does this. The same rule explains Pipeline News 7,775 vs 7,798 (Team 3).

### A.3 Nearest substation and NO MAP on the new records
`tools/nearest_substation_check.mjs` runs GridAtlas's own code. Geodesy `distanceKm` comes from `atlas/modules/202609011950-geodesy.js`
in node:vm. `voltagesKv`, `representativePoint` and MIN_KV 33 / LINK_COUNT 5 / MAX_LINK_KM 40 are extracted from the live
sld-sandbox 202609241334. Substations: 5,800 loaded, all qualifying. Output: `logs/nearest-substation-oct-preview.json`.
- 328 added refs: all have a usable point. Nearest substation of 33 kV or more: median 1.36 km, p95 6.14 km, max 17.3 km. None is
  beyond 40 km, and none is flagged by a coarse region/latitude check.
- 19 refs moved. The large moves are corrections into the stated county: 8912 Bolfornought 581 km to Stirling, 18563 Salters Lane
  364 km to Tyne and Wear, 21008 244 km to Co. Down, 13290 Corshellach 223 km to Moray, 21026 196 km to Northamptonshire,
  7871 Artfield 104 km to Dumfries and Galloway.
- Not corrected: 18561/18562 Salters Lane (county Tyne and Wear) still sit at -0.659, 51.591 near High Wycombe, so their nearest
  substation (an unnamed 33 kV site, 3.4 km) is wrong. This is a source fault: report it, do not patch it.
- Blank coordinates: 36 active records (in live too) are converted from BNG (0,0) to the false origin (-7.55716, 49.766807) and
  stay in the snapshot. The gazetteer (`hasSafeMapPoint`, cartridge line 321), the sld-sandbox
  (PLACEHOLDER_COORDINATES_FALSE_ORIGIN, line 6604) and the offtakers module (line 118) all refuse that point, so the outcome is
  NO MAP, not a false origin (`logs/no-map-blank-coordinates.txt`). 6 offshore refs get Crown Estate lease points. 7 offshore
  refs new since January (10920, 11613, 13417, 13428, 13432, 13735, 21087) have none and stay RESOLVED_UNMAPPED.

### A.4 Pipeline News MAP links into GridAtlas, live vs preview (coordinator item A3)
All 7,775 MAP links of the operative `uk_renewables_pipeline/202611132345` were replayed through the receivers' logic. The tool is
`tools/a3_map_links.py`; output in `logs/a3-map-links-summary.json` and `a3-map-links.csv`. This is offline, from the code. The
live site is UNVERIFIED.
- 7,749 links carry a point, so the sld-sandbox arrival measures nearest kV from the link point. 26 links have no point.
- Live 202610312138: RESOLVED 5,246, RESOLVED_UNMAPPED 20, NOT_IN_ACTIVE_REGISTER 2,509. 97 of the 2,509 have an active status
  (83 are new since 202609082224): the map moves but no identity card opens.
- Live: 12 links resolve to a July register point that differs from the October link point. The card and the measurement then
  disagree by up to 581 km (8912 Bolfornought).
- With P1: active rows with no card go from 97 to 3 (2484, 6483, 20218, Norfolk Vanguard E/W and Boreas, lon 2.55, outside the
  compiler's 2.5 E limit). Card/link mismatches go from 12 to 0. 29 links lose their card because the ref became inactive in
  October (22 refused, 6 withdrawn, 1 appeal lodged).

### A.5 Pre-existing issues the preview carries (not introduced, not fixed here)
- The compiler (line 124) and globalgrid2050 `scripts/repd_updater.py` (280-281) both apply `biomass > 100 MW → /1000`. This
  shrinks 7 real plants: Drax units 1 to 4 at 645 MW → 0.645, Lynemouth 420 → 0.42, Upper Bighouse 260 → 0.26, BAEF 102 → 0.102
  (`logs/capacity-rescale-and-blank.txt`). Both must be fixed together, or the record join breaks for those rows.
- Blank capacity is written as 0.0: 1,126 parquet rows (NOT NULL schema) and 1,121 repd_master features. This conflicts with
  "blank is unknown".
- The offshore reconcile tools and `atlas/coordinate-systems.json` still pin the January `repd.csv`. The drawn REPD layer is still
  the April data-gridatlas partition.

## B. Legacy globalgrid2050 pages (main 1d5dad64; the page files are unchanged since the patches were made)
The full table is in `globalgrid2050/PAGES.md`, the counts in `render-table.md` and `render-results.json`, and the screenshots
(30 PNG) in `screenshots/`. Method: headless Chrome against a local copy served by http.server, with the CDN libraries served from
npm copies of the pinned versions and map tiles stubbed (`tools/render.mjs`). **Every page renders on October data with 0 page
errors.** The exception is atlas v4, which shows the same 6 pre-existing `GRID_CONFIG` redeclaration errors on both datasets.

| page | Jan → Oct drawn | verdict |
|---|---|---|
| repd-atlas.md (/atlas/) | 13,970 → 14,931 | switch |
| uk_grid-batteries.md | 2,022 → 2,177 | switch |
| uk_operating_large_solar_farms.md | 923 → 939 | switch |
| repd-uk-operational-solar.md | 1,208 → 1,228 | switch |
| uk_offshore_wind_atlas.md | 93 → 96 (15 offshore projects, 22,738 MW, have no coordinates and are not drawn) | switch, with the caveat stated |
| uk_onshore_wind_atlas.md | 2,695 → 2,771 | switch |
| uk_solar_in-planning-1-50mw.md | 1,657 → 1,730 (1,707 at XLSX precision) | switch |
| repd_atlas_grid_model.md | 13,970 → 14,931 | historical (V2): stay on January |
| repd_grid_atlasv3 to v8 | source 10,784 → 11,293 features; flywheel layer becomes empty | historical: stay (v8 only on an owner decision) |
| solar-bess-topology v6, v7 | operating assets 2,212 → 2,258 (v6) | historical: stay |
| solar-bess-topology v8 | no REPD fetch; its repd_master files are not loaded by any HTML | no change |

Gains on October data: new refs (+986 on /atlas/), and the January "�" rows (198 on /atlas/, 28 offshore) and subset mojibake
disappear. Losses and caveats on either dataset: blank capacity shown as "0 MW" (1,362 rows on /atlas/, 474 batteries);
18561/18562 misplaced; 36 records without coordinates not drawn.

Patches: `globalgrid2050/switch-per-page/`, one diff per page (7 current, 10 historical); each passes `git apply --check` on
1d5dad64. Bundles: `switch-current-pages.diff` and `switch-historical-optional.diff`. Root `*.md` is not in the deploy-pages.yml
push paths, so the switch needs a deploy dispatch (a harness step, after a checkpoint).

## Requests
- Owner:
  - choose between the two-step release (P1, then a lightning cut) and amending the lightning proof;
  - land patch-0 first, because every gridatlas PR gate is red until tests 80 and 98 are fixed;
  - decide whether atlas v8 switches.
- ChatGPT (real browser, live site):
  - open `https://ventusltd.github.io/gridatlas/atlas/?repd_ref=8912&technology=bess&latitude=56.1206&longitude=-3.8951&zoom=12`.
    Expected today: the card goes to the July point (52.36 N, 2.31 E) while the kV measurement is taken at Stirling;
  - confirm that `?repd_ref=11058&technology=wind_onshore&latitude=51.5625467&longitude=-3.5086672&zoom=12` opens no identity card.

## What remains
- The browser audit of the GridAtlas preview route. It needs the data-gridatlas and DuckDB CDN assets; lane G1 serves the live
  clone locally.
- The lightning-only cut after P1.
- The drawn-layer refresh in data-gridatlas.
- The biomass /1000 and blank-as-zero fixes.
- The offshore lease reconcile against October.
