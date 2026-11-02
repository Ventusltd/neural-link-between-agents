#!/bin/bash
# state6.sh: OPUS-CONTROLLER-2's wake list for Edition 6+ admissions (sha12 of each hand-off file, finished journeys,
# newest #10 comment addressed to a controller).
H=/home/user/estate/kuiper-belt/editions/202611012135; S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad
cd $H
for f in handoff/02-card/edition-6/MODULE.sha256 handoff/02-card/edition-6/TEST.md handoff/02-card/TEST.md \
 handoff/07-apps/TEST.md handoff/07-apps/MODULE.sha256 handoff/06-file/TEST.md handoff/06-file/MODULE.sha256 \
 handoff/03-layers/TEST.md handoff/03-layers/MODULE.sha256 handoff/08-drift/TEST.md handoff/08-drift/MODULE.sha256 \
 handoff/05-see-through/TEST.md handoff/05-see-through/MODULE.sha256 handoff/01-shell/MODULE.sha256 \
 ../202611020326/index.html ../202611020326/modules.json; do
  if [ -f "$f" ]; then echo "$f $(sha256sum "$f" | cut -c1-12)"; else echo "$f -"; fi; done
for f in $S/journey/e6-*.log; do [ -f "$f" ] && grep -q "^exit" "$f" && echo "JOURNEY-DONE $(basename $f)"; done
n=$(gh api "repos/Ventusltd/neural-link-between-agents/issues/10" --jq .comments 2>/dev/null); p=$(( (n+99)/100 ))
echo "issue10-to-controller $(gh api "repos/Ventusltd/neural-link-between-agents/issues/10/comments?per_page=100&page=$p" --jq "[.[] | select(.body | split(\"\\n\")[0] | test(\"→.*CONTROLLER|→ ALL\")) | .id] | last" 2>/dev/null)"
