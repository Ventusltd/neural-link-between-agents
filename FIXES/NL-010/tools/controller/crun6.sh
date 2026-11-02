#!/bin/bash
# crun6.sh <snap> <device>: OPUS-CONTROLLER-2. Run journey-6.cjs on one device against an existing snap6.sh snapshot,
# served by the scratchpad/snap http.server on port 8590. Chromium flags come from the script (SwiftShader / ANGLE).
# Output scratchpad/journey/<snap>-<dev>.{log,json,sum,load}
set -u
S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad; N=$1; D=$2; ED=${ED:-202611020326}
s=$(echo "$D" | tr ' A-Z' '-a-z'); mkdir -p $S/journey; cd $S/journey
{ uptime; date -u +%H:%M:%S; } > $N-$s.load
NODE_PATH=$(npm root -g) timeout 3300 node ${JS:-/home/user/neural-link-between-agents/FIXES/NL-010/tools/controller/journey-6.cjs} http://127.0.0.1:8590/$N/editions/$ED/ $S/journey/out-$N-$s --device "$D" > $N-$s.json 2> $N-$s.log
echo "exit $?" >> $N-$s.log; { uptime; date -u +%H:%M:%S; } >> $N-$s.load
grep -hE "\] (PASS|FAIL)" $N-$s.log > $N-$s.sum; echo DONE $N $D
