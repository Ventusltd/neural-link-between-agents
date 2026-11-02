#!/bin/bash
# jrun.sh <name>: snapshot + journey-5 on Pixel 7 and Galaxy S24 in parallel; summary to journey/<name>.sum
set -u
L=/tmp/nl010-opus/team-10/lead; N=$1
[ "${2:-}" = keep ] || $L/snap.sh $N >/dev/null
cd $L/journey; uptime > $N.load
for d in "Pixel 7" "Galaxy S24"; do s=$(echo $d | tr ' A-Z' '-a-z');
  NODE_PATH=$(npm root -g) node journey-5.cjs http://127.0.0.1:8500/$N/editions/202611012135/ $L/journey/out-$N-$s --device "$d" > $N-$s.json 2> $N-$s.log & done
wait; uptime >> $N.load
grep -hE "PASS|FAIL" $N-pixel-7.log $N-galaxy-s24.log > $N.sum; echo DONE $N; cat $N.sum
