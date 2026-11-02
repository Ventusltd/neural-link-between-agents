#!/bin/bash
# crun.sh <snap> <device> [index.html] [modules.json]: OPUS-CONTROLLER. Freeze a snapshot (snap.sh), optionally overlay a
# candidate page and manifest into the snapshot only, then run journey-5.cjs (team 10 lead's admission script) on one
# device on port 8590 (serves scratchpad/snap). Output journey/<snap>-<dev>.{log,json,sum,load}
set -u
S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad; N=$1; D=$2
s=$(echo "$D" | tr ' A-Z' '-a-z'); E=$S/snap/$N/editions/202611012135
if [ ! -d "$E" ]; then $S/snap.sh $N >/dev/null || exit 3
  [ -n "${3:-}" ] && cp "$3" $E/index.html
  [ -n "${4:-}" ] && cp "$4" $E/modules.json
  (cd $E && find . -type f ! -path './proof/*' | sort | xargs sha256sum) > $S/snap/$N.sha256
fi
cd $S/journey; uptime > $N-$s.load; date -u +%H:%M >> $N-$s.load
NODE_PATH=$(npm root -g) timeout 3000 node /tmp/nl010-opus/team-10/lead/journey/journey-5.cjs http://127.0.0.1:8590/$N/editions/202611012135/ $S/journey/out-$N-$s --device "$D" > $N-$s.json 2> $N-$s.log
echo "exit $?" >> $N-$s.log; uptime >> $N-$s.load; date -u +%H:%M >> $N-$s.load
grep -hE "\] (PASS|FAIL)" $N-$s.log > $N-$s.sum; echo DONE $N $D
