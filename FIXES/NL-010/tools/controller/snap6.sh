#!/bin/bash
# snap6.sh <name> [modules.json] [module-file ...]: OPUS-CONTROLLER-2. Frozen mirror of the kuiper-belt root for one
# journey run on Edition 6+ (editions/202611020326 copied without handoff/, everything else symlinked). Optional
# candidate manifest and module files are overlaid into the SNAPSHOT ONLY; the working tree is never touched.
set -e
R=/home/user/estate/kuiper-belt; ED=${ED:-202611020326}
S=/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/snap/$1; shift
rm -rf "$S"; mkdir -p "$S/editions"
for f in "$R"/* "$R"/.[!.]*; do b=$(basename "$f"); [ "$b" = editions ] || [ "$b" = .git ] || ln -s "$f" "$S/$b"; done
for f in "$R"/editions/*; do b=$(basename "$f"); [ "$b" = "$ED" ] || ln -s "$f" "$S/editions/$b"; done
mkdir "$S/editions/$ED"; (cd "$R/editions/$ED" && tar cf - --exclude=./handoff --exclude=./GREEN.md --exclude=./CONTROLLER.md .) | (cd "$S/editions/$ED" && tar xf -)
if [ -n "${1:-}" ]; then cp "$1" "$S/editions/$ED/modules.json"; shift; fi
for m in "$@"; do cp "$m" "$S/editions/$ED/modules/"; done
(cd "$S/editions/$ED" && find . -type f ! -path './proof/*' | LC_ALL=C sort | xargs sha256sum) > "$S.sha256"
echo "$S"
