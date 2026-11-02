#!/bin/bash
# poll6.sh [max_seconds]: block until state6.sh output changes or max elapses; print the diff (OPUS-CONTROLLER-2)
D=$(dirname "$0"); S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad; M=${1:-560}
[ -f $S/state6.last ] || $D/state6.sh > $S/state6.last
t=0; while [ $t -lt $M ]; do $D/state6.sh > $S/state6.now; if ! cmp -s $S/state6.now $S/state6.last; then echo "CHANGED after ${t}s at $(date -u +%H:%M)"; diff $S/state6.last $S/state6.now; cp $S/state6.now $S/state6.last; exit 0; fi; sleep 45; t=$((t+45)); done
echo "NO CHANGE in ${M}s at $(date -u +%H:%M)"; uptime
