#!/bin/bash
# R1: squash the edition branch onto a fresh branch from origin/main, in a separate worktree so the
# Opus teams' working tree on edition/202611012135 is not disturbed. Usage: r1_squash.sh "<modules admitted>"
set -euo pipefail
MODS="${1:?modules admitted}"
REPO=/home/user/estate/kuiper-belt
WT=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/release/wt
STAMP=202611012135
cd "$REPO"
git fetch -q origin
git worktree remove --force "$WT" 2>/dev/null || true
git branch -D edition/$STAMP-squash 2>/dev/null || true
git worktree add -q -B edition/$STAMP-squash "$WT" origin/main
cd "$WT"
paths=()
for f in editions/$STAMP tools/build_layers.py tools/edition_min.py tools/edition_check.py tools/apps_registry.py tools/element_keys.py tools/drift.py editions/LAW.md .github/workflows/check.yml; do
  if git cat-file -e "edition/$STAMP:$f" 2>/dev/null; then paths+=("$f"); fi
done
echo "taking: ${paths[*]}"
git checkout -q edition/$STAMP -- "${paths[@]}"
git add -A "${paths[@]}"
git -c user.name="$(git -C $REPO log -1 --format=%an)" -c user.email="$(git -C $REPO log -1 --format=%ae)" commit -q -F - <<MSG
Kuiper Edition 5 ($STAMP) preview: $MODS

Preview merge (pointer unchanged, editions/index.html still opens 202611012027/). Squash of branch
edition/$STAMP: the edition folder editions/$STAMP/ with its modules, manifest, handoff folders and proof,
plus the edition tools. Admitted by the integrator (handoff/10-integration/ADMISSIONS.md) with the Android journey
(handoff/10-integration/TEST.md) on Pixel 7 and Galaxy S24. NL-010 owner ACCEPT (chat) recorded in
neural-link FIXES/NL-010/OVERNIGHT.md.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm
MSG
git log --oneline -1
git show --stat HEAD | tail -1
echo "--- ci_check on the squash branch"
python3 tools/ci_check.py
