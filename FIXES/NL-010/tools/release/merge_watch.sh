#!/bin/bash
# Merge a branch --no-ff into main (in the release worktree), push main, print the main sha, and watch the Pages run.
# Usage: merge_watch.sh <branch> "<merge subject>"
set -euo pipefail
BR="${1:?branch}"; SUBJ="${2:?subject}"
REPO=/home/user/estate/kuiper-belt
WTM=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/release/wt-main
cd "$REPO"; git fetch -q origin
git worktree remove --force "$WTM" 2>/dev/null || true
git worktree add -q --detach "$WTM" origin/main
cd "$WTM"
git checkout -q -B main-release origin/main
git -c user.name="$(git -C $REPO log -1 --format=%an)" -c user.email="$(git -C $REPO log -1 --format=%ae)" merge --no-ff -q "$BR" -m "$SUBJ

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm"
python3 tools/ci_check.py | tail -1 | grep -q 'RESULT: PASS' || { echo "ci_check FAILED after merge; not pushing"; exit 2; }
git push -q origin HEAD:main
git push -q origin "$BR:$BR" || true
SHA=$(git rev-parse HEAD); echo "MAIN_SHA=$SHA"
for i in $(seq 1 40); do
  out=$(gh api "repos/Ventusltd/kuiper-belt/actions/runs?head_sha=$SHA&per_page=5" -q '.workflow_runs[] | "\(.id) \(.name) \(.status) \(.conclusion)"' 2>/dev/null || true)
  echo "$(date -u +%H:%M:%S) $out" | tr '\n' ';'; echo
  if echo "$out" | grep -q 'pages build and deployment completed success'; then echo "PAGES_OK"; exit 0; fi
  if echo "$out" | grep -E 'completed (failure|cancelled)'; then echo "RUN_FAILED"; exit 3; fi
  sleep 15
done
echo "PAGES_TIMEOUT"; exit 4
