# Pipeline News version train (Engineer Guardian), NL-015

Appended once per cycle. Times are UTC, 14 November 2026.

## V9.14 = 202611140128 (parent 202611140058, tree 18f870e1)
- Added: data-centre capex and politics headline panel (N4 script, unchanged); nav links to versions.html and to the data-centres page. Also the train's tooling: automation/pipeline_release/, workflow verify-pipeline-versions.yml, versions.json, versions.html, docs/pipeline/RELEASE-TRAIN.md.
- Tree: 227f2c9edc9440489fc7122cbd222fe991071a65. Data digest equal to parent. MAP hrefs identical to parent: 7,775 of 7,775.
- Runner: tests/run_v9_14.sh PASS (local and CI).
- CI: PR #74. Verify Pipeline News versions run 43541196726 FAILURE on the first commit (workflow checkout lacked 202609082224, needed by the V9.12 runner; a workflow fault, not a version fault), run 43541314987 SUCCESS on 0a2444df. PR file size guard run 43541314999 SUCCESS. Public language gate: never runs.
- Merge commit: 3d679cdb6e755bdbd2a5dede37188d5a2ff8c06a at 01:35.
- Known faults: full 46 MB copy (slimmed from V9.15). Panel shows only lanes with headlines; feed held 5 headlines. Live site not checked from this workspace. Issue post: see issue 15.
