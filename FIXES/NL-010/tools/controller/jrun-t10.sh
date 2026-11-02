#!/bin/bash
# jrun-t10.sh <snap> <device>: team 10 tester's android-journey.cjs (ecde2f34) on one device against a frozen WATCHER-B snapshot on port 8590
set -u
S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad; N=$1; D=$2
s=$(echo "$D" | tr ' A-Z' '-a-z'); cd $S/journey; uptime > $N-$s.load
NODE_PATH=$(npm root -g) node $S/journey-t10.cjs http://127.0.0.1:8590/$N/editions/202611012135/ $S/journey/out-$N-$s --device "$D" > $N-$s.json 2> $N-$s.log
echo "exit $?" >> $N-$s.log; uptime >> $N-$s.load; echo DONE $N $D
