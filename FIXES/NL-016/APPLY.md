# How to apply the Team 4 packages (for the owner or the harness; agents in this session have no push route to gridatlas)

## GridAtlas: preview P1 (22 files) and the standalone test fix

Two text diffs plus the binary data files:
- `gridatlas/patch-0-lightning-test-clock-fix.diff`: only `tools/ci/lightning/overlay-engine.test.mjs` (tests 80 and 98).
  It applies alone to main `41729af`. Tests 80 and 98 fail on main today, so every gridatlas PR gate (pr-file-size-guard.yml
  runs pr-gate.mjs) is red until this lands. Evidence: `gridatlas/logs/test80-98-matrix.log`. On the original test file, test 80
  fails at real time and passes with the clock set to 2026-10-26. Test 98 fails with the clock set to 00:05 UTC. The fixed file
  passes all 207 at both times, on the live module 202610291043 and on the preview module.
- `gridatlas/gridatlas-P1-repd-2026q3-preview.diff`: the 22-file preview. It includes patch-0's change, so apply one or the
  other, not both. The two data files are excluded from the text diff. They are copied with their sha256 in
  `<workspace>/teams/4/a/P1-files/` (`P1-files.sha256`):
  - `data/repd_projects_202611132345.parquet` `cc9b7f046fe24497114c9cc356d7d0e54830890722af90a83c397eab1056d789`
  - `data/repd_browser_registry_202611132345.json` `fdda9b6e4fd14cb234cdc7baaac9a6c0f45c5594179c2eaa4b58e874ac6d8f58`
  The full 22-file tree is in the same folder. The preview can be rebuilt from scratch with
  `bash <workspace>/auto/gridatlas/scripts/build_preview.sh` and then the split edit described in REPORT.md §A.1.

```bash
# in a fresh worktree of gridatlas main 41729af (never the working clone)
git worktree add -b preview/202611132345-gridatlas-v9.189 ../ga-preview origin/main && cd ../ga-preview
git apply /path/to/FIXES/NL-016/gridatlas/gridatlas-P1-repd-2026q3-preview.diff
cp <workspace>/teams/4/a/P1-files/data/repd_projects_202611132345.parquet data/
cp <workspace>/teams/4/a/P1-files/data/repd_browser_registry_202611132345.json data/
(cd <workspace>/teams/4/a/P1-files && sha256sum -c ../P1-files.sha256)      # 22 OK
git add -N . && node tools/ci/pr-gate.mjs --base origin/main                 # expect 19/19
node tools/scope/loop.mjs lint && node tools/scope/loop.mjs state --stdout | cmp - STATE.md
git add -A && git commit -m "202611132345-gridatlas-v9.189: preview, REPD records re-pinned to October 2026 (Q3), data-only"
git push -u origin preview/202611132345-gridatlas-v9.189
gh api -X POST repos/Ventusltd/gridatlas/pulls -f head=preview/202611132345-gridatlas-v9.189 -f base=main -F draft=true \
  -f title='202611132345 v9.189 preview: REPD records October 2026 (Q3), data-only' -F body=@PR-DESCRIPTION-gridatlas-P1.md
```
`publish-preview.mjs` cannot publish this preview: it handles only the monolithic lightning shape and requires
`G-sld-sandbox-v9-8.js`. So this is a hand PR. The change set is additive apart from 7 modified tooling and test files and the
allowlist line. The release afterwards follows docs/RELEASE.md: the owner's `ACCEPT 202611132345`, then
`release-accepted.mjs --generation 202611132345 --push`, which the owner merges with rebase, then `check-live.mjs`.

### Exact file list (P1)
```
M .github/large-files-allowlist.txt
A atlas/cartridges/202611132345-place-global-search-v9-5.js
A atlas/manifests/202611132345-composition.json
A atlas/manifests/202611132345-place-global-search-v9-5-parts.json
A atlas/modules/202611132345-uk-offtakers-overlay.js
A atlas/parts/202611132345-place-global-search-repd-2026q3.js
A atlas/v/202611132345/current.json
A atlas/v/202611132345/index.html
A atman/202611132345-verify-atlas-v9.py
A compiler/202611132345-compile-atlas-v9.py
A contracts/202611132345-atlas-v9-source.json
A data/repd_browser_registry_202611132345.json
A data/repd_projects_202611132345.parquet
A data/repd_v9_manifest_202611132345.json
M tools/ci/lightning/overlay-engine.test.mjs
M tools/ci/offtakers/overlay-offtakers.test.mjs
M tools/offtakers/generations.json
M tools/offtakers/src/04-repd-record-m5.js
M tools/offtakers/src/06-tap-card.js
M tools/offtakers/src/06b-dc-engine.js
A tools/proofs/202611132345-uk-gazetteer-flyto.proof.mjs
A tools/proofs/202611132345-uk-offtakers-overlay.proof.mjs
```
The alternative is the 27-file single generation, which adds the lightning module, its proof and the lightning src and
registry edits: `<workspace>/auto/gridatlas/repo/` and `gridatlas-repd-2026q3-preview.diff`. It gives 21/22 with the test fix.
The one failure is the lightning parity proof, which needs an owner decision (PR description, "Why two steps").

## globalgrid2050: legacy page switch (optional)
- Recommended: the 7 `globalgrid2050/switch-per-page/current--*.diff` files, one line each. Each applies alone
  (`git apply --check` passes on main `1d5dad64`).
- Not recommended: the `historical--*.diff` files (grid model V2, atlas v3 to v8, topology v6 and v7).
- After applying, dispatch `deploy-pages.yml`, because root `*.md` is not in its push paths. Take a checkpoint first, as the
  owner asked. Rollback means reverting the commit, since `repd.csv` and the other January files are never touched.
