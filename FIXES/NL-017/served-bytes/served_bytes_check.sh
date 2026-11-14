#!/usr/bin/env bash
# Served-byte check for globalgrid2050 main after the PR #57 merge (merge commit 07b6d51702a1, tree 683f5b162c34).
# Prepared by Team 5 (NL-017). Read-only: only HTTP GETs. Needs bash, curl, sha256sum (or shasum -a 256), awk.
# Usage:  ./served_bytes_check.sh served-manifest.tsv [after-merge|after-rollback] [base_url]
#   after-merge (default): NEW/MOD/PIN rows must return 200 with the exact sha256; JEKYLL rows 200 only; SKIP rows are reported.
#   after-rollback: NEW rows must return 404; PIN rows must still match.  (MOD rows are scripts; after rollback they return to main's
#   old bytes, which this manifest does not list, so they are reported only.)
# Output: one TSV line per path (result, http status, bytes, sha256, path) and a summary; exit 0 only if every required row passes.
set -uo pipefail
MAN=${1:?manifest}; MODE=${2:-after-merge}; BASE=${3:-https://globalgrid2050.com}
if command -v sha256sum >/dev/null; then H="sha256sum"; else H="shasum -a 256"; fi
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
pass=0; fail=0; info=0; bust="cb=$(date -u +%s)"
printf 'result\tstatus\tbytes\tsha256\tpath\n'
while IFS=$'\t' read -r expect path want bytes origin; do
  [ "$expect" = expect ] && continue
  url="$BASE/$path"; [[ "$MODE" = after-merge && "$path" == */index.html ]] && url="$BASE/${path%index.html}"
  # Jekyll (jekyll-optional-front-matter, as the deploy log of run 43535023721 shows) renders *.md to *.html and does not publish
  # the raw .md; a README.md becomes the folder index only when the folder has no index.html. So check the rendered URL, status only.
  if [ "$expect" = JEKYLL ] && [[ "$path" == *.md ]]; then url="$BASE/${path%.md}.html"; fi
  code=$(curl -sS -L --max-time 60 -o "$tmp/f" -w '%{http_code}' "$url?$bust" 2>/dev/null || echo 000)
  got=$($H "$tmp/f" 2>/dev/null | cut -c1-64); size=$(wc -c < "$tmp/f" 2>/dev/null | tr -d ' ')
  res=INFO
  case "$MODE:$expect" in
    after-merge:NEW|after-merge:MOD|after-merge:PIN|after-rollback:PIN)
      if [ "$code" = 200 ] && [ "$got" = "$want" ]; then res=PASS; else res=FAIL; fi ;;
    after-merge:JEKYLL) [ "$code" = 200 ] && res=PASS || res=FAIL ;;
    after-rollback:NEW) [ "$code" = 404 ] && res=PASS || res=FAIL ;;
  esac
  case $res in PASS) pass=$((pass+1));; FAIL) fail=$((fail+1));; *) info=$((info+1));; esac
  printf '%s\t%s\t%s\t%s\t%s\n' "$res" "$code" "$size" "$got" "$path"
  [ "$res" = FAIL ] && [ "$expect" != JEKYLL ] && [ "$code" = 200 ] && printf '#   want %s (%s bytes)\n' "$want" "$bytes"
done < "$MAN"
echo "# mode=$MODE base=$BASE pass=$pass fail=$fail info=$info  (UTC $(date -u +%FT%TZ))"
echo "# A FAIL with status 200 and a different hash on a PIN row means a pre-existing file changed: stop and roll back."
echo "# Pages CDN may serve old bytes for some minutes after a deploy: re-run after 10 minutes before acting on NEW-row 404s."
[ "$fail" -eq 0 ]
