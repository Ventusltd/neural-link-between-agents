#!/usr/bin/env bash
# S1-build.sh - recreate uk_renewables_pipeline/202611140058 (V9.13) in a globalgrid2050
# checkout whose 202611132345 folder has tree 0c7a4ed5 (main d5de5a03 or later, BEFORE S2).
# Equivalent to S1-successor-release.patch (the 47 MB full-folder patch).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
P=uk_renewables_pipeline/202611132345; N=uk_renewables_pipeline/202611140058
test "$(git rev-parse HEAD:$P)" = 0c7a4ed5ea369e4a4e71a45cfa6fe9c186fae773
test ! -e "$N"
cp -a "$P" "$N"
rm -rf "$N/fixtures/2026q3" "$N/tests/run_v9_12.sh" "$N/tests/check_v9_12.mjs"
git apply -p1 "$(dirname "$0")/S1-delta.patch"
( cd "$N" && find . -type f | sed 's#^\./##' | sort | xargs sha256sum ) | diff - "$(dirname "$0")/S1-file-sha256.txt"
bash "$N/tests/run_v9_13.sh"
