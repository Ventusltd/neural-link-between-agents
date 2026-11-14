# Pipeline News version train (Engineer Guardian), NL-015

Appended once per cycle. Times are UTC, 14 November 2026.

## V9.14 = 202611140128 (parent 202611140058, tree 18f870e1)
- Added: data-centre capex and politics headline panel (N4 script, unchanged); nav links to versions.html and to the data-centres page. Also the train's tooling: automation/pipeline_release/, workflow verify-pipeline-versions.yml, versions.json, versions.html, docs/pipeline/RELEASE-TRAIN.md.
- Tree: 227f2c9edc9440489fc7122cbd222fe991071a65. Data digest equal to parent. MAP hrefs identical to parent: 7,775 of 7,775.
- Runner: tests/run_v9_14.sh PASS (local and CI).
- CI: PR #74. Verify Pipeline News versions run 43541196726 FAILURE on the first commit (workflow checkout lacked 202609082224, needed by the V9.12 runner; a workflow fault, not a version fault), run 43541314987 SUCCESS on 0a2444df. PR file size guard run 43541314999 SUCCESS. Public language gate: never runs.
- Merge commit: 3d679cdb6e755bdbd2a5dede37188d5a2ff8c06a at 01:35.
- Known faults: full 46 MB copy (slimmed from V9.15). Panel shows only lanes with headlines; feed held 5 headlines. Live site not checked from this workspace. Issue post: see issue 15.

## V9.15 = 202611140136 (parent 202611140128, tree 227f2c9e)
- Added: GridAtlas data state on the rows it concerns (97 active October rows not in the GridAtlas register generation 202608290716; list in gridatlas/map_link_state.json and versions.json map_link_state; note below the row's actions, MAP link untouched; note hidden when GridAtlas serves another project-search generation). Folder 16 MB (fixtures v5, v6, v7.2 not copied). Tooling: gridatlas_resolve.py (re-runnable, --require-active), size budget 17 MB in CI, workflow dispatch input gridatlas_registry_url.
- Tree: 9eae71204ef1e70057cc81ec49d1e765137f36d2. Data digest equal to parent. MAP hrefs identical to parent: 7,775 of 7,775.
- Measure: active rows 5,334; resolved 5,237; not resolved 97; other statuses 2,412; 29 no-longer-active rows still held by GridAtlas. Against Team 4's P1 registry (202611132345): 3 not resolved: REPD 2484, 6483, 20218 (all three share the REPD point 52.62 N, 2.55 E; the GridAtlas compiler keeps longitudes below 2.5 E, compile-atlas-v9.py line 115).
- Runner: tests/run_v9_15.sh PASS (local and CI).
- CI: PR #75. Verify Pipeline News versions run 43541887007 SUCCESS. PR file size guard run 43541887050 SUCCESS.
- Merge commit: 9f2d94cfbc4a9c2e4806ac93dc973ce07e578a7d at 01:56.
- Known faults: the 97 are measured from files, not on the live map; the row note could not be seen against the live GridAtlas composition from this workspace (tested with a local copy of current.json).

## V9.16 = 202611140156 (parent 202611140136, tree 9eae7120)
- Added: nearest data-centre register site in each PROJECT RECORD (convergence sidecar byte copy keyed by REPD ref; straight-line, labelled screening; link opens GridAtlas on the site with latitude/longitude/zoom=13/project). GridAtlas state re-measured against the released October registry (gridatlas b0a3a93; registry sha256 fdda9b6e): 5,331 of 5,334 active rows resolve; 3 (2484, 6483, 20218) lie east of the compiler's 2.5 E bound and are marked with that reason; 2,441 non-active; 26 without map point; 0 unexplained. Tooling: CSV export check, reasons in gridatlas_resolve.py, size budget 18 MB.
- Tree: b0d94bc0d814285b675467ed59b6c0804aaa2400. MAP hrefs identical to parent: 7,775 of 7,775.
- Runner: tests/run_v9_16.sh PASS (local and CI).
- CI: PR #76. Verify run 43543937369 FAILURE (Chrome did not start on the runner; affected every version; tool fault), run 43544934300 SUCCESS on 4868a040. Size guard 43544934884 SUCCESS.
- Merge commit: 1dc14b6f6f1e73b53bd2df8fb06e39f0573f40b0 at 02:16.
- Known faults: one nearest site per project only; GridAtlas state measured from files, not the live map; issue post 02:17 covers V9.15 and V9.16.

## V9.17 = 202611140216 (parent 202611140156, tree b0d94bc0)
- Added: register changes July to October 2026 REPD: labelled list of the twelve highest-scored changes, and the change in the PROJECT RECORD of each of 274 projects (308 events from dist/news/repd_events_2026q3.json, keyed by REPD ref, not rescored or reworded).
- Tree: 2a6faf461c0771bb8cfe5c47a4e138af710b868f. MAP hrefs identical to parent: 7,775 of 7,775. CSV 7,775 rows, same columns.
- Runner: tests/run_v9_17.sh PASS (local and CI).
- CI: PR #77. Verify run 43545673886 SUCCESS. Size guard 43545673869 SUCCESS.
- Merge commit: 896e7f4b778e25bfc9db2fd54e58598a23237bc1 at 02:26.
- Known faults: PROCESS FAULT BY THE GUARDIAN: merged 10 minutes after V9.16 (02:16), inside the 20-minute minimum spacing; the merge call was chained after a time check by mistake. Nothing was reverted. The next publication is held to 02:46 or later. List shows twelve changes only.

## V9.18 = 202611140223 (parent 202611140216, tree 2a6faf46): RELEASE CANDIDATE
- Added (corrections after ChatGPT's V9.16 review, no new data-centre content): attribution block and per-entry line; register source entries for all 226 sites; settlement-level points labelled and rounded; location-only link wording; stated failure when context cannot load; nav trimmed. Tooling: feature probes (6, at two widths), drawn MAP links equal contract hrefs, release-candidate state, datacentre_features in versions.json.
- Tree: 0edd36f51365f9f5b7cdca2927c7e78c4615e41d. MAP hrefs identical to parent: 7,775 of 7,775.
- Runner: tests/run_v9_18.sh PASS (local and CI).
- CI: PR #79. Verify run 43546692462 SUCCESS. Size guard 43546692491 SUCCESS.
- Merge commit: 244cb1f82ac3ce04988c57a59d21f6316a0e2d21 at 02:46.
- Release candidate request posted on issue 15 (live browser and served-byte checks, pointer promotion by ChatGPT).
- Known faults: licence status unverified at source; live sites unchecked; datacentres/index.html (not guardian scope) still lacks attribution.
