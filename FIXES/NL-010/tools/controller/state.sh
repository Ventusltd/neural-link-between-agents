#!/bin/bash
# state.sh: one line per watched thing (sha12 of each), for the controller's poll
H=/home/user/estate/kuiper-belt/editions/202611012135; S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad
cd $H
for f in handoff/01-shell/MODULE.sha256 handoff/01-shell/TEST.md handoff/01-shell/HANDOFF.md modules/202611012143-kuiper-shell.js \
 handoff/04-loader/MODULE.sha256 handoff/04-loader/TEST.md handoff/04-loader/index.html.rev5-on-live.patch \
 handoff/03-layers/MODULE.sha256 handoff/03-layers/TEST.md handoff/03-layers/HANDOFF.md handoff/03-layers/delete-moved.py modules/202611012141-layers.js \
 handoff/06-file/MODULE.sha256 handoff/06-file/TEST.md handoff/06-file/HANDOFF.md \
 handoff/05-see-through/MODULE.sha256 handoff/05-see-through/TEST.md handoff/07-apps/MODULE.sha256 handoff/07-apps/TEST.md handoff/07-apps/HANDOFF.md handoff/07-apps/img/element-card.png \
 handoff/08-drift/TEST.md handoff/08-drift/HANDOFF.md handoff/09-law/MODULE.sha256 handoff/09-law/TEST.md handoff/09-law/HANDOFF.md index.html modules.json; do
  if [ -f "$f" ]; then echo "$f $(sha256sum "$f" | cut -c1-12)"; else echo "$f -"; fi; done
for f in $S/journey/*.log; do grep -q "^exit" "$f" && echo "JOURNEY-DONE $(basename $f)"; done
echo "issue10 $(gh api repos/Ventusltd/neural-link-between-agents/issues/10 --jq .comments 2>/dev/null)"
