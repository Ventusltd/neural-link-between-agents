#!/bin/bash
# poll.sh [max_seconds]: block until state.sh output changes or max elapses; print the diff
S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad; M=${1:-560}
[ -f $S/state.last ] || $S/state.sh | grep -vE "handoff/0[5789]-" > $S/state.last
t=0; while [ $t -lt $M ]; do $S/state.sh | grep -vE "handoff/0[5789]-" > $S/state.now; if ! cmp -s $S/state.now $S/state.last; then echo "CHANGED after ${t}s at $(date -u +%H:%M)"; diff $S/state.last $S/state.now; cp $S/state.now $S/state.last; exit 0; fi; sleep 30; t=$((t+30)); done
echo "NO CHANGE in ${M}s at $(date -u +%H:%M)"; uptime
