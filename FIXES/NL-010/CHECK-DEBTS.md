# Check debts of the shipped Kuiper editions (prepared, not shipped)

FABLE-FIN-1, 2026-11-02 10:38Z (`date -u`). Measured with `tools/edition_check.py` from branch
edition/202611012135 (tip 9b08cd1; the tool's last commit 6d69972) run against a clean worktree of kuiper-belt
origin/main 94aa593 with `--root <worktree> --estate /home/user/estate`. The tool and editions/LAW.md exist only on the
branch; main has tools/ci_check.py only. Result on main as is: E1 E2 E3 E4 E5 E8 PASS, **E6 FAIL, E7 FAIL, E9 FAIL**.
Shipped folders are frozen (LAW.md 9.1): every fix below lands either in the tool or in the next edition's cut, never
in a folder that is on main. Candidate (tool changes only, no module byte changes) on the branch under
`editions/202611012135/handoff/13-check-debts/` (edition_check.patch, ec-main-orig.txt, ec-main-patched.txt, README.md);
not admitted.

## E6: the loader reference copy carries KY_EDITION 202611012135

- Check: kuiper-belt@9b08cd1 tools/edition_check.py:371 `if pblock is not None and rb != pblock` compares the hook-table
  block (BEGIN..END, `block_of` at :77) of the reference `modules/202611012145-loader.js` with the page's block.
- Fact: in every shipped folder from Edition 6 the two blocks differ in exactly one line. kuiper-belt@94aa593
  editions/202611021017/modules/202611012145-loader.js:20 `const KY_EDITION = '202611012135';` against
  editions/202611021017/index.html:844 `const KY_EDITION = '202611021017';` (blocks: loader.js 7-133, index.html 831-957,
  12,526 bytes each; measured with difflib on the worktree). The page's stamp must move with the folder because the
  loader refuses a manifest whose edition differs from the page's (index.html:938), and the reference file is an
  admitted, hashed record (modules.json `references`, sha256 checked at :364) that the release does not rewrite.
- Fix A (tool, safe, prepared): normalise the KY_EDITION line before comparing and report the two stamps in the PASS
  text. Patch: `handoff/13-check-debts/edition_check.patch` (adds KYED at :48, replaces :370-372). Measured: E6 PASS on
  main with the patch (ec-main-patched.txt), FAIL without (ec-main-orig.txt). No module byte changes.
- Fix B (next cut, the team 4 loader owner): a reference copy stamped for the new edition under a new file name, with
  the hook-table block re-copied from that edition's index.html; then Fix A's normalisation is never exercised.

## E7: prose in the drift and apps records' writes

- Check: tools/edition_check.py:420-431; each `writes` entry must be a literal in the module file (:425), each `reads`
  entry too (:429).
- Facts (kuiper-belt@94aa593 editions/202611021017/modules.json): :167 drift writes `"#hud (one DRIFT line per frame,
  appended)"`; :212 apps writes `"#card (element card)"`; :213 `"history entry {kyApps}"`; :214 `"layers elements,
  spider (via KY.modules.layers.api.register)"`. The same four lines ship in 202611020528 (drift only), 202611020629,
  202611020825 and 202611021017 (apps from Edition 9). The records are copied verbatim from the teams' MODULE.json
  (handoff/08-drift, handoff/07-apps) by the controller; the modules themselves write `#hud` (drift.js:135-137 via H.hud),
  `#card`, `history.pushState({ kyApps: 1 })` (apps.js:315) and register the layers `elements` and `spider`.
- Fix A (tool, safe, prepared): strip one trailing parenthetical annotation before the literal test (ANNOT at :49,
  patch at :423). Measured with the patch: drift passes; apps still fails on two entries that have no literal at all
  (`history entry {kyApps}`, `layers elements, spider`), which is the right verdict: prose with no literal is not a record.
- Fix B (next cut, team 7's MODULE.json, then the controller's modules.json of the next folder): apps writes become
  `"#card"`, `"history.pushState"`, `"elements"`, `"spider"` (each a literal in apps.js; team 7 to confirm the layer
  ids are what it registers), and drift's `"#hud"`. No module byte changes; modules.json of the NEXT folder only.

## E9: data/drift.json does not re-compute

- Check: edition_check.py E9 re-runs tools/drift.py --heads against the recorded heads (:487). On main every folder
  from 202611012135 re-computes to a different sha256 at the same byte count (118,553). The harness noted at 01:53Z that
  the pipelinenews clone under /home/user/estate changed the replay (OVERNIGHT.md); it was moved to
  /home/user/pipelinenews-for-next-drift-cut, and the E9 replay now depends on which clones the estate holds.
- Not prepared here: team 8 (drift) owns it. The fix is a recorded estate (the clone set and each head) inside
  drift.json so the replay is byte-identical regardless of the host, or a ruling on #10 that E9 reads NOT EVALUATED
  when the estate differs from the recorded one.

## New (found 10:38Z): data/apps.json and data/elements.json still stamped 202611012135

- Facts (worktree of 94aa593): editions/202611020629, 202611020825 and 202611021017 `data/apps.json` and
  `data/elements.json` carry `"edition": "202611012135"` while index.html, modules.json, data/drift.json,
  data/editions.json and data/layers.json carry the folder's stamp. The apps module does not refuse on edition (no
  edition test in 202611012309-apps.js), so the page works; the drift module does refuse (202611020240-drift.js:61), which
  is why drift.json is regenerated at each cut and apps.json is not.
- Fix (next cut): the release recipe re-stamps or regenerates every data file that carries an `edition` field
  (tools/release/RECIPE.md step 4 gains apps.json and elements.json), and edition_check gains an E10: every
  `editions/<stamp>/data/*.json` with an `edition` field equals the stamp. A cvaa vaccine with that exact check is filed
  today (Ventusltd/cvaa, kuiper-belt-data-stamp-is-the-page-stamp).

## New (found 10:48Z by the cvaa vaccine kuiper-belt-no-private-names): K1 skips tracked files over 3,000,000 bytes

- Check: kuiper-belt@94aa593 tools/ci_check.py:40 scans a tracked file only if its size is at most 3,000,000 bytes, and
  :46 then prints "852 tracked files scanned, 0 match" counting every tracked file, scanned or not. k1-staged.py has the
  same bound (FIXES/NL-010/tools/k1-staged.py:11).
- Facts (clean worktree of main 94aa593, `leaks()` from tools/check_proof.py run file by file, counts only): four tracked
  files over the bound each carry 6 tokens whose digests are on the not-public list: data/20260918T234128Z/estate-network.json
  (3,112,373 B), data/20260918T234405Z/estate-bodies.json (3,116,099 B), data/20260918T234855Z/estate-bodies.json
  (3,116,751 B), data/20260919T001154Z/estate-bodies.json (3,137,106 B). data/20260918T231829Z/estate-network.json
  (2,928,364 B, scanned by ci_check) carries 0. These are the 18-19 September harvest snapshots, on main since then;
  not touched tonight, and not touched by FIN-1 (deletions and history are the owner's: delegation 6566796733).
- Fix (owner's decision, prepared nowhere): remove or redact the four files in a commit the owner makes (history keeps
  them unless rewritten); then ci_check K1 scans every tracked file regardless of size, or at least prints the skipped
  ones as a FAIL. The cvaa vaccine reports an unscanned file as a finding, never a pass.
