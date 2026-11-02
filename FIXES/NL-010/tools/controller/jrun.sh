#!/bin/bash
# jrun.sh <name> <device> [keep]: snapshot (unless keep) + journey-5 on one device; log/json in scratchpad/journey
set -u
S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad; N=$1; D=$2
[ "${3:-}" = keep ] || $S/snap.sh $N >/dev/null
s=$(echo "$D" | tr ' A-Z' '-a-z'); cd $S/journey; uptime > $N-$s.load
NODE_PATH=$(npm root -g) node /tmp/nl010-opus/team-10/lead/journey/journey-5.cjs http://127.0.0.1:8590/$N/editions/202611012135/ $S/journey/out-$N-$s --device "$D" > $N-$s.json 2> $N-$s.log
echo "exit $?" >> $N-$s.log; uptime >> $N-$s.load
grep -hE "PASS|FAIL|NOT EVAL" $N-$s.log > $N-$s.sum; echo DONE $N $D
