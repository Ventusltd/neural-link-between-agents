#!/bin/bash
# state.sh: the controller's wake list (sha12 of each), order 5, 8, 6, 7, 3, 9 (harness ruling 01:2x)
H=/home/user/estate/kuiper-belt/editions/202611012135; S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad
cd $H
for f in handoff/01-shell/MODULE.sha256 handoff/04-loader/MODULE.sha256 handoff/05-see-through/MODULE.sha256 \
 handoff/08-drift/MODULE.sha256 handoff/08-drift/TEST.md handoff/08-drift/HANDOFF.md \
 handoff/06-file/MODULE.sha256 handoff/06-file/TEST.md handoff/06-file/HANDOFF.md \
 handoff/07-apps/TEST.md handoff/07-apps/HANDOFF.md handoff/03-layers/TEST.md handoff/03-layers/HANDOFF.md \
 handoff/09-law/HANDOFF.md handoff/09-law/TEST.md index.html modules.json; do
  if [ -f "$f" ]; then echo "$f $(sha256sum "$f" | cut -c1-12)"; else echo "$f -"; fi; done
for f in $S/journey/*.log; do grep -q "^exit" "$f" && echo "JOURNEY-DONE $(basename $f)"; done
echo "issue10-to-me $(gh api "repos/Ventusltd/neural-link-between-agents/issues/10/comments?per_page=100&page=1" --jq "[.[] | select(.body | split(\"\\n\")[0] | test(\"CONTROLLER|OPUS-10\")) | .id] | last" 2>/dev/null) $(gh api "repos/Ventusltd/neural-link-between-agents/issues/10/comments?per_page=100&page=2" --jq "[.[] | select(.body | split(\"\\n\")[0] | test(\"CONTROLLER|OPUS-10\")) | .id] | last" 2>/dev/null)"
