# Rollback checklist for globalgrid2050 PR #57 (rehearsed, not executed on GitHub)

Prepared by Team 5 (NL-017), 14 Nov 2026. Head under test: `f9ccd703ca749ad8009274a18516625d9d1e5fa3`; main `73cbdec10bbd3fe2f8313b60b1acc2d22d31b517`.
Rehearsal script and log: `rehearse.sh`, `rehearse.log` (team folder g2/). It ran in a throw-away local clone (`git clone --no-checkout <workspace>/gg-wt`),
with no network and no push.

## What the rehearsal proved (2026-11-14 ~00:30Z)

| Step | Result | Evidence |
|---|---|---|
| Simulated merge M = commit with the PR head tree on top of main | tree identical to f9ccd703 (0 paths differ) | rehearse.log section 0 |
| A. Revert the whole merge (`git revert -m 1 M`) | tree identical to main 73cbdec1: 0 paths differ. 0.29 s with plumbing, 2.2 s with porcelain in a sparse checkout | rehearse.log A; porcelain run gave `diff vs main: 0` |
| B. Revert only Claude's four commits (f9ccd703, 0c78c8c1, aa83e48a, 01ec01e9) | no conflict; tree equals 6e58f280 (PR #56 tip): 14 files added vs main, 0 modified | rehearse.log B |
| C. Revert only the two data commits (0c78c8c1, aa83e48a) | no conflict; 0 files left under 202611132345, 0 `*2026q3*` data files left | rehearse.log C |
| D. After A, every RUNBOOK section 2.1 path has its main blob | 64 of 64 identical | rehearse.log D |
| E. Restore by blob id without history | `repd_master.json`, `repd.csv`, `.github/large-files-allowlist.txt` restored; sha256 OK against RUNBOOK pins | rehearse.log E |

Limits: the rehearsal could not exercise GitHub itself (the Revert button, Pages redeploy, CDN cache). It assumes main is still
73cbdec1 when the PR merges; if main moves first, the merge tree differs and the rehearsal must be re-run on the real merge commit.

## Commands for the owner (or an agent the owner names), after a merge

```sh
# 0. Record what is live before acting
MERGE=<merge commit sha on main>          # gh pr view 57 -R Ventusltd/globalgrid2050 --json mergeCommit -q .mergeCommit.oid
git fetch origin main && git checkout -B rollback-57 origin/main

# A. Full rollback (recommended if anything published by the merge is wrong)
git revert -m 1 --no-edit "$MERGE"
git diff --stat 73cbdec10bbd3fe2f8313b60b1acc2d22d31b517 HEAD      # must print nothing if main had no other commits since
#    then open a PR from rollback-57 (or use the GitHub "Revert" button on PR #57) and the OWNER merges it.
#    The revert deletes uk_renewables_pipeline/202611132345/**, so deploy-pages.yml fires again (path filter uk_renewables_pipeline/**)
#    and republishes the site without the new files.

# B. Keep PR #56's source-intake commits, drop Claude's four commits (squash/rebase merges: revert the single merge commit instead)
git revert --no-edit f9ccd703 0c78c8c1 aa83e48a 01ec01e9

# C. Drop only the data and the release folder, keep automation/repd and docs
git revert --no-edit 0c78c8c1 aa83e48a

# E. Restore one file to its pinned bytes, without history (example: dist/repd_master.json)
git cat-file blob e221065a7b144a9e4b691cf282e23a68c5661e45 > dist/repd_master.json
echo "ca5da437ddb832f7e4e8d84bba1f2f6d40df6285089a43156452fdda7eebe0fe  dist/repd_master.json" | sha256sum -c
#    Every pinned blob and sha256 is in docs/repd/RUNBOOK.md section 2.1 and in Team 5's g1/runbook-pins.tsv.

# F. Verify after the revert is deployed: run served_bytes_check.sh in "after-rollback" mode (Team 5, FIXES/NL-017/)
```

## Update 00:50Z: main moved on to 1a416f4b (three merges)

main history (first parents): `73cbdec1` → `07b6d517` (PR #57) → `67635070` (PR #60, follow-up: only edits files PR #57 added) →
`1a416f4b` (PR #61, homepage pin to globalgrid2050-homepage `cdd5e1f2`: changes `catalogue/homepage-owner.json`, adds one QA workflow).
Read from the compare API. 1a416f4b vs 73cbdec1: 318 added, 6 modified, 0 deleted. 62/64 RUNBOOK pins identical; the changed ones are
the allowlist (append) and `catalogue/homepage-owner.json` (the pointer).

```sh
# P. Roll back ONLY the homepage pointer (Pipeline News link back to 202609082224, pin 9914285b); data stays published
git revert -m 1 --no-edit 1a416f4bb84f3ef984263cbc825d1cd5c597d0df
grep '"commit"' catalogue/homepage-owner.json      # must show 9914285b691766c8f20b25fc83147f59c0389938
# Q. Roll back everything to 73cbdec1, newest first
git revert -m 1 --no-edit 1a416f4b 67635070 07b6d517
git diff --stat 73cbdec10bbd3fe2f8313b60b1acc2d22d31b517 HEAD   # must print nothing if nothing else landed on main
```
P and Q were NOT rehearsed on the real commits: the local clone's shallow history could not fetch the parents. Expected effect taken from the
first-parent diffs above, which are disjoint, so no conflicts are expected. Section A (rehearsed) covers 07b6d517 alone.
Either revert pushed to main fires deploy-pages.yml (`catalogue/**`, `uk_renewables_pipeline/**`).

## Notes

- If PR #57 is merged by squash, the branch commit ids above do not exist on main; use the single squash commit with `git revert <sha>` (no `-m`).
- Nothing in PR #57 modifies or deletes a pre-existing data file (gate 1), so rollback never has to restore old data: it only removes new files
  and restores the 5 modified files (allowlist plus four V6 scripts whose defaults keep July).
- The evidence branches created by CI (`repd/2026-10-reviewed-evidence-*`, `repd/2026-07-verified-archive-20261113`) are not touched by a revert.
  Deleting them is a separate owner decision and is not needed for rollback.
- Pages CDN caching: allow about 10 minutes after the redeploy before treating a served-byte mismatch as a failure (UNVERIFIED for this site).
