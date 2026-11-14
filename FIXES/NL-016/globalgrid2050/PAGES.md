# Legacy globalgrid2050 atlas and table pages: January files vs the 2026q3 files (Team 4, NL-016, strand B)

Checked against globalgrid2050 main `1d5dad64`: every page file below is byte-identical to the copy the patches were made from.
Data files: `repd.csv` (January, sha256 `fdb6aec5…`, cp1252), `repd-2026q3.csv` (`d937ae16…`, UTF-8), the three `-2026q3` subsets
(`c8e58d5c…` batteries, `ed41f198…` solar >1 MW, `17d6169a…` solar >4 MW), `dist/repd_master.json` (`ca5da437…`, 10,784 features)
and `dist/repd_master_2026q3.json` (`3ffe6c5c…`, 11,293 features). The old files stay byte-identical; the switch only repoints URLs.

How the renders were made: a copy of the pages and data under `<workspace>/teams/4/b/site`, served by `python3 -m http.server`
on 127.0.0.1, then opened in `/usr/bin/google-chrome` (Chrome for Testing 153, headless, via Playwright 1.63). Front matter was
stripped and `{{ site.baseurl }}` replaced with an empty string; Jekyll itself was not run. CDN libraries were served from npm
copies of the exact versions the pages pin. Map tiles and the Carto style are stubs (flat dark background), so the screenshots show
markers on a blank map. The counts come from hooks on `L.circleMarker`, DataTables `rows().count()` and the MapLibre GeoJSON
sources. Tool: `tools/render.mjs`. The counts match the earlier Node harness (`<workspace>/auto/pages`).

## Per page (Jan → Oct; each page applied with its own filter)

| page | reads now | markers / rows drawn, Jan → Oct | gains | loses / caveats on October data | render on Oct | recommendation |
|---|---|---|---|---|---|---|
| repd-atlas.md (/atlas/) | repd.csv | 13,970 → 14,931 | +986 refs drawn; "�" rows 198 → 0 (cp1252 read as UTF-8 in January) | −25 refs drawn (left REPD or lost X/Y); 36 rows have no X/Y and are skipped (25 in Jan); 1,362 blank-capacity rows show "0 MW" (1,264 in Jan); refs 18561/18562 "Salters Lane" (county Tyne and Wear) plot near High Wycombe | PASS, 0 errors | switch (current product page, no version in name) |
| uk_grid-batteries.md | repd-grid-batteries.csv | 2,022 → 2,177 | +224; January mojibake ("Â", 30 rows) gone | −69 refs no longer in the October subset (reason not classified); 474 blank capacities show "0 MW"; 4 without X/Y; one of 18561/18562 is on this page, in the wrong place | PASS | switch |
| uk_operating_large_solar_farms.md | ...-over-4mw.csv | 923 → 939 | +17; mojibake (6 rows) gone | −1; ref 1613 (Sainsbury's 169 stores) has no X/Y in both | PASS | switch |
| repd-uk-operational-solar.md | repd-solar-operational.csv | 1,208 → 1,228 | +21; mojibake (10 rows) gone | −1; ref 1613 has no X/Y | PASS | switch |
| uk_offshore_wind_atlas.md | repd.csv, Wind Offshore | 93 → 96 | +3; "�" rows 28 → 0 | 15 offshore projects have blank X/Y, so they are skipped (8 in January): 10913 North Falls 1,000 MW, 10919 Morgan 1,500, 10922 Morecambe 480, 11109 and 20217 Dogger Bank SE and SW 1,500 each, 13429 Ossian 3,600, 13431 Muir Mhòr 1,000, 13528 Cenos 1,350, plus 7 not in the January file: 10920 Morven North 1,450, 21087 Morven South 1,450, 11613 Buchan 1,000, 13417 Cluaran Deas Ear 1,008, 13428 Machair 2,000, 13432 Marram 3,000, 13735 Spiorad na Mara 900. In total 22,738 MW of offshore capacity is not drawn | PASS | switch, with the blank-coordinate list stated |
| uk_onshore_wind_atlas.md | repd.csv, Wind Onshore | 2,695 → 2,771 | +77; "�" rows 34 → 0 | −1; 108 blank capacities show "0 MW"; 2 rows carry source mojibake as published (3052 "BrÃ¢n", 4049 "SrÃ²n MÃ³r") | PASS | switch |
| uk_solar_in-planning-1-50mw.md (/repd_solar_pipeline/) | repd.csv, solar, not dead or operational, 1 to 50 MW | 1,657 → **1,730** | +144 | −71 refs that left the page's filter (status or capacity changed; not classified one by one); the count depends on capacity precision: CSV-precision file 1,730, XLSX-precision staged file 1,707 (23 sites printed as "1" are 0.996 to 0.99975 MW) | PASS | switch; state the precision rule |
| repd_atlas_grid_model.md (/repd_atlas_grid_model/) | repd.csv | 13,970 → 14,931 GeoJSON features (clustered) | as /atlas/ | as /atlas/; the page's filters are not wired (crawl note 16) | PASS | **historical** (V2 in historical_builds.html, "LIVE, REACHABLE UNVERIFIED"): keep on January |
| repd_grid_atlasv3 … v8 | /dist/repd_master.json | source 10,784 → 11,293; drawn at the UK view (all REPD layers on, glow layers counted) v3/v4/v5 12,994 → 13,558, v6/v8 16,034 → 16,675, v7 16,009 → 16,650 | per layer: solar 2,819 → 2,892, solar_roof 3,240 → 3,528, wind 1,538 → 1,574, bess 2,066 → 2,167, hydro 151 → 155 | flywheel layer becomes empty (ref 6865 decommissioned); 1,121 blank capacities carried as `capacity: 0.0` by repd_updater.py; 18561/18562 at the High Wycombe point; v4 throws `Identifier 'GRID_CONFIG' has already been declared` six times on both datasets (pre-existing pasted-code defect) | PASS (v4 with the same pre-existing errors on Jan and Oct) | **historical** (each listed in historical_builds.html with a source commit; V9 GridAtlas is the successor): keep on January. v8 is the only one marked "WORKING VERIFIED"; switch it only on an owner decision |
| solar-bess-topology-v6, v7 gis-sld-financial-sandbox | /dist/repd_master.json (map layer, plus site search in v7 ui.js) | operating-asset layers at the UK view: v6 2,212 → 2,258 (solar 1,221 → 1,241, onshore 774 → 781, offshore 48 → 49, bess 169 → 187); v7 bess 2,066 → 2,167 | more operating assets | none found | PASS | **historical** (listed under "Solar & BESS Topology" as V6 Testing Phase and V7 Workspace): keep. v7 is linked from the homepage for its topology tools, not for REPD |
| solar-bess-topology-v8 | gis-sld-v5-map.js and ui.js name /dist/repd_master.json | no REPD request on load (0 on both) | | the two files that name repd_master are not loaded by any HTML in v8 (dead code) | PASS, no REPD fetch | no change needed; left out of the patch |

## Patches (unified diffs against globalgrid2050; `git apply --check` passes on main 1d5dad64)
- `switch-per-page/current--*.diff`: 7 files, one line each (the `csvUrl` constant). These are the recommended switch.
- `switch-per-page/historical--*.diff`: 10 files, optional and not recommended. They change 1 line (grid model), 12 to 58 lines
  (atlas v3 to v8: every layer object names the URL) and 1 to 2 lines (topology v6/v7).
- `switch-current-pages.diff` and `switch-historical-optional.diff` hold the same changes, bundled.

Deploy note: `.github/workflows/deploy-pages.yml` push paths do not include root `*.md` (crawl note 16 §5). Applying the switch
therefore deploys nothing until deploy-pages is dispatched or another trigger fires. Dispatching it is a live step for the harness.

Things that stay wrong on October data whichever file is used, and are data, not page code:
blank capacity is drawn as "0 MW" (`parseFloat(...) || 0` in every page; `capacity: 0.0` in repd_master); 36 records with no
coordinate are not drawn; 18561/18562 sit at X 492983 Y 188837 (Buckinghamshire) although their county is Tyne and Wear. In
October, ref 18563 (same site) was moved 364 km to Tyne and Wear, which suggests the other two are a source error.
