#!/bin/bash
# snap.sh <name>: frozen mirror of the kuiper-belt root for one journey run; the edition folder is copied (no handoff/), the rest symlinked
set -e
R=/home/user/estate/kuiper-belt; S=/tmp/nl010-opus/team-10/lead/snap/$1
rm -rf "$S"; mkdir -p "$S/editions"
for f in "$R"/* "$R"/.[!.]*; do b=$(basename "$f"); [ "$b" = editions ] || [ "$b" = .git ] || ln -s "$f" "$S/$b"; done
for f in "$R"/editions/*; do b=$(basename "$f"); [ "$b" = 202611012135 ] || ln -s "$f" "$S/editions/$b"; done
mkdir "$S/editions/202611012135"; (cd "$R/editions/202611012135" && tar cf - --exclude=./handoff .) | (cd "$S/editions/202611012135" && tar xf -)
(cd "$S/editions/202611012135" && find . -type f ! -path './proof/*' | sort | xargs sha256sum) > "$S.sha256"
echo "$S"
