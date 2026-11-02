# The release recipe used for Kuiper Editions 7 to 11 (2 November 2026, 04:46Z to 10:22Z)

Written by FABLE-FIN-1 at 10:35Z (`date -u`) from the shipped commits on kuiper-belt main and the harness log
(FIXES/NL-010/OVERNIGHT.md). Keys: kuiper-belt@94aa593 (Edition 11), 35ef064 (10), fdf6e35 (9), 87031c6 (8),
4ee309d (7); the GREEN commits on branch edition/202611012135: 84f1c1ed (E6-G1 -> 7), 553e58d (E6-G2 -> 8),
b553b1f (E6-G3 -> 9), 85c0bc6 (E9-G1 -> 10), 977de9c (E10-G1 -> 11). Each GREEN row lives in
`editions/<base stamp>/GREEN.md` on the branch (202611020326, 202611020629, 202611020825) and names the branch commit
to ship with the sha256 of its index.html and modules.json.

Rule learned at 02:57Z (OVERNIGHT.md, correction 521dca75): a release checks out a NAMED COMMIT's folder and verifies
its index.html and modules.json sha256 against the GREEN row before anything else. It never reads the branch's live
working tree (a432b43 shipped a manifest no GREEN row named).

Authority: the owner's delegation on #10 (6566796733, renewed 6567437030 "use your initiative and ship builds"). It
expires with the owner's next message; see SESSIONS/RESUME.md section 4 before pushing main.

## Steps (N = the new edition number, S = its stamp, B = the base folder's stamp on the branch, G = the GREEN commit)

```bash
S=$(date -u +%Y%m%d%H%M)                       # the stamp is read from the clock at the cut, never written from memory
KB=/home/user/estate/kuiper-belt; WT=/tmp/kb-e$N
git -C $KB fetch -q origin
git -C $KB worktree add $WT origin/main -b release-e$N     # a clean worktree of origin/main; never the branch tree
cd $WT
# 1. the GREEN commit's folder, verified against the row before copying
git show $G:editions/$B/modules.json | sha256sum          # must equal the GREEN row's modules.json column
git show $G:editions/$B/index.html   | sha256sum          # must equal the row's index.html column
mkdir -p editions/$S && git archive $G editions/$B | tar -x --strip-components=2 -C editions/$S
rm -f editions/$S/CONTROLLER.md editions/$S/GREEN.md editions/$S/README.md editions/$S/data/drift.json
rm -rf editions/$S/proof                                   # rebuilt below; keep nothing of the base's proof
# 2. stamp the page and the manifest (the loader refuses a manifest whose edition differs from the page's: index.html:938)
sed -i "s/const KY_EDITION = '$B'/const KY_EDITION = '$S'/" editions/$S/index.html
sed -i "s/Kuiper Edition $((N-1))/Kuiper Edition $N/g" editions/$S/index.html     # <title> and the big.textContent label
python3 - "$S" "$B" <<'PY'
import json, sys
S, B = sys.argv[1:3]; p = f'editions/{S}/modules.json'; m = json.load(open(p))
m['edition'] = S
for r in m['modules']:
    if r.get('id') == 'layers':                      # the layers record carries edition and built_by (Edition 10+)
        r['edition'] = S; r['built_by'] = f'tools/build_layers.py --edition {S}'
json.dump(m, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
PY
# 3. prose: README.md ("What changed from Edition N-1", the GREEN row, the measurements), NOTICE.md re-stamped,
#    editions/README.md (new entry + the "current edition" sentence), root README.md Editions entry,
#    and the pointer editions/index.html in its three places (line 7 meta refresh, line 11 link, line 12 location.replace,
#    forwarding location.search + location.hash)
# 4. the data files (Edition 10+): registry, then drift from the tested heads
python3 tools/build_layers.py --edition $S            # writes data/editions.json and measures data/layers.json
python3 - "$S" <<'PY'
import json, sys; S = sys.argv[1]; p = f'editions/{S}/data/layers.json'; d = json.load(open(p)); d['edition'] = S
json.dump(d, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
PY
python3 tools/build_layers.py --edition $S --check    # exit 0: nothing would change
git show $G:editions/$B/data/drift.json > /tmp/heads-$S.json   # the heads the GREEN row was tested with
python3 tools/drift.py --edition $S --heads /tmp/heads-$S.json  # writes editions/$S/data/drift.json with edition S
# 5. render check on both phones against this worktree (port 8797 in the e11-* scripts; edit the URL and port)
(python3 -m http.server 8797 --bind 127.0.0.1 >/dev/null 2>&1 &)
NODE_PATH=$(npm root -g) node e11-check.cjs      # admitted/refused, bar one row, wordmark, 0 page errors; Pixel 7 screenshot
NODE_PATH=$(npm root -g) node e11-apps.cjs       # the drift line and the launcher (Edition 9+)
NODE_PATH=$(npm root -g) node e11-layers.cjs     # the layers rows (Edition 10+)
KEYS=editions/$S/keys.json LINE1=<a placed line id> NODE_PATH=$(npm root -g) node e11-touch.cjs http://127.0.0.1:8797/editions/$S/ /tmp/touch-$S --device "Pixel 7"   # FILE by touch (Edition 11+)
NODE_PATH=$(npm root -g) node e11-404.cjs        # every response under 400 (the proof file 404s until step 6)
cp /tmp/e11-pixel7.png editions/$S/proof/render-pixel7.png   # and the module's own frame as render-pixel7-<module>.png
# 6. the proof over every file in the folder, then the gates
(cd editions/$S && find . -type f ! -path ./proof/edition-sha256.txt | LC_ALL=C sort | xargs sha256sum > proof/edition-sha256.txt)
(cd editions/$S && sha256sum -c --quiet proof/edition-sha256.txt)
python3 tools/ci_check.py                          # RESULT: PASS (K1 privacy, K2 sums, K3 syntax, K4 order)
git add -A && python3 /home/user/neural-link-between-agents/FIXES/NL-010/tools/k1-staged.py   # K1 on the staged files
git commit -m "Kuiper Edition $N ($S): <what changed> on Edition $((N-1)); pointer moved" -m "Co-Authored-By: ..." -m "Claude-Session: ..."
# 7. the engine commits cosmos/*.tsv to main from Actions ("engine" workflow): rebase over it, re-check, push, watch
git fetch -q origin && git rebase origin/main && python3 tools/ci_check.py
git push origin HEAD:main                           # only under the delegation (RESUME.md section 4)
SHA=$(git rev-parse HEAD); gh api "repos/Ventusltd/kuiper-belt/actions/runs?head_sha=$SHA&per_page=5" --jq '.workflow_runs[]|"\(.name) \(.status) \(.conclusion)"'
# "pages build and deployment" and "checking engineer" must both read completed success; record the run ids in
# OVERNIGHT.md and in a HANDOFF on #10. The sandbox cannot fetch the live site: the run is the evidence.
```

## The scripts in this folder

- `e10-check.cjs`, `e11-check.cjs`: the two-phone render check (Pixel 7, Galaxy S24) as run for Editions 10 and 11; they
  differ only in port and stamp. `e10-apps.cjs`/`e11-apps.cjs`: the drift line and the app launcher. `e10-layers.cjs`/
  `e11-layers.cjs`: the layers rows. `e11-touch.cjs`: the controller's FILE touch check (byte-identical to
  `../controller/file-touch-c4.cjs` except the port 8797 for 8590). `e11-404.cjs`: every HTTP status at or above 400.
  All hard-code `http://127.0.0.1:<port>/editions/<stamp>/` and `/tmp/<name>.png`; change those two strings for the next cut.
  Playwright and Chromium are preinstalled; `NODE_PATH=$(npm root -g)`; never install.
- `k1-staged.py`: the K1 privacy check on `git diff --cached` (same bytes as `../k1-staged.py`); run from the kuiper-belt
  worktree after `git add`.
- `r1_squash.sh`, `merge_watch.sh`, `k1hist.py`: the Edition 5 preview tools (path checkout of the branch tip, the
  `--no-ff` merge with a Pages watch, and the K1 history walk). From Edition 7 the recipe above replaced r1_squash.sh: a
  copy of one GREEN commit's folder into a fresh worktree of origin/main, never a merge of the branch.
