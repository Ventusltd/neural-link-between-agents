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
