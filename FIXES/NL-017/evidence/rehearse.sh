#!/bin/bash
# Rollback rehearsal for globalgrid2050 PR #57, in a throw-away local clone. No network, no push.
set -euo pipefail
cd <workspace>/teams/5/g2/clone
export GIT_AUTHOR_NAME=rehearsal GIT_AUTHOR_EMAIL=rehearsal@invalid GIT_COMMITTER_NAME=rehearsal GIT_COMMITTER_EMAIL=rehearsal@invalid
export GIT_AUTHOR_DATE=2026-11-14T00:00:00Z GIT_COMMITTER_DATE=2026-11-14T00:00:00Z
BASE=73cbdec10bbd3fe2f8313b60b1acc2d22d31b517; HEAD_PR=f9ccd703ca749ad8009274a18516625d9d1e5fa3
t0=$(date +%s.%N)
echo "## 0. Simulated merge of PR #57 into main (merge commit, tree = PR head tree; valid while main is still $BASE)"
M=$(git commit-tree "$HEAD_PR^{tree}" -p $BASE -p $HEAD_PR -m "simulated merge of PR #57")
git update-ref refs/heads/main-sim $M
echo "merge M=$M ; diff vs PR head: $(git diff --name-only $HEAD_PR $M | wc -l) paths"
echo "## A. Full rollback: revert the merge (equivalent of 'git revert -m 1 M')"
TA=$(git merge-tree --write-tree --merge-base=$M $M $BASE)
RA=$(git commit-tree $TA -p $M -m "Revert PR #57 (rehearsal)")
echo "revert commit RA=$RA ; paths differing from main $BASE: $(git diff --name-only $BASE $RA | wc -l) (must be 0)"
echo "## B. Revert only Claude's four commits (f9ccd703, 0c78c8c1, aa83e48a, 01ec01e9), newest first, keeping PR #56's commits"
cur=$M
for c in f9ccd703 0c78c8c1 aa83e48a 01ec01e9; do
  t=$(git merge-tree --write-tree --merge-base=$c $cur $c^1) || { echo "CONFLICT reverting $c"; exit 1; }
  cur=$(git commit-tree $t -p $cur -m "Revert $c (rehearsal)")
  echo "  reverted $c -> $cur"
done
echo "tree after B equals 6e58f280 tree: $( [ "$(git rev-parse $cur^{tree})" = "$(git rev-parse 6e58f280^{tree})" ] && echo YES || echo NO)"
echo "B vs main: $(git diff --name-status $BASE $cur | awk '{print $1}' | sort | uniq -c | tr '\n' ' ')"
echo "## C. Revert only the two data commits (0c78c8c1 release folder, aa83e48a datasets); keep automation and workflow fix"
cur=$M
for c in 0c78c8c1 aa83e48a; do
  t=$(git merge-tree --write-tree --merge-base=$c $cur $c^1) || { echo "CONFLICT reverting $c"; exit 1; }
  cur=$(git commit-tree $t -p $cur -m "Revert $c (rehearsal)"); echo "  reverted $c -> $cur"
done
echo "C: paths still present from 202611132345: $(git ls-tree -r --name-only $cur uk_renewables_pipeline/202611132345 | wc -l); *2026q3* data files left: $(git ls-tree -r --name-only $cur | grep -c -E '(^|/)(repd[^/]*-2026q3\.csv|dist/[^/]*2026q3[^/]*\.json)$' || true)"
echo "## D. Base-tree identity after A: every RUNBOOK pin re-checked by blob"
bad=0; while IFS=$'\t' read -r kind path pinned result note; do
  [ "$kind" = FILE ] || continue
  b1=$(git rev-parse "$BASE:$path"); b2=$(git rev-parse "$RA:$path"); [ "$b1" = "$b2" ] || { echo "  DIFF $path"; bad=1; }
done < <(tail -n +2 <workspace>/teams/5/g1/runbook-pins.tsv); echo "pins identical after A: $([ $bad = 0 ] && echo YES || echo NO)"
echo "## E. Restore single files by blob id (no history needed), verify sha256 against RUNBOOK pins"
mkdir -p <workspace>/teams/5/g2/restored
git cat-file blob e221065a7b144a9e4b691cf282e23a68c5661e45 > <workspace>/teams/5/g2/restored/repd_master.json
git cat-file blob 01fe17ae9531d3504490a1418a68350262b06f86 > <workspace>/teams/5/g2/restored/repd.csv
git cat-file blob cea655d7d0a332509ba11567a6655a00074cde8a > <workspace>/teams/5/g2/restored/large-files-allowlist.txt
( cd <workspace>/teams/5/g2/restored && sha256sum -c <<'S'
ca5da437ddb832f7e4e8d84bba1f2f6d40df6285089a43156452fdda7eebe0fe  repd_master.json
fdb6aec50647a4de88f63d33679b93cb2147417eddc43f3f31cbf12792a38aae  repd.csv
91526b11a4620f149dc674ddeb274a4f74b5123d720984b29348709481799e34  large-files-allowlist.txt
S
)
t1=$(date +%s.%N); echo "elapsed: $(echo "$t1 - $t0" | bc) s"
