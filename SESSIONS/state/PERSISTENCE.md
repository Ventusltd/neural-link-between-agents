# PERSISTENCE: what lived only on this machine, and where it lives now (NL-011 LINK-07)

Written by NL-011 LINK-07 "persistence", 2026-11-02, survey 01:15Z to 01:26Z (clock read with `date -u`). Rule:
LINK-RULE.md item 3 (state lives in this repository; /tmp and scratchpads are working space). Every file copied here
passed the K1 check first (`leaks()` from kuiper-belt tools/check_proof.py printed 0 for each one; no replacement was
needed). It was also scanned for credential patterns, and none were found. Nothing is committed by this agent; the
harness commits.

Abbreviations: SP = the harness session scratchpad `/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad`;
OP = `/tmp/nl010-opus` (the Opus teams' working space, 597 MB); KB = `/home/user/estate/kuiper-belt`; T = `FIXES/NL-010/tools`.

Decisions: **COPY** (copied into this repository; the path is given), **IN-REPO** (already in a pushed repository, so
no copy was needed; the key is given), **NOTE** (large or regenerable; described here with how to get it back),
**DROP** (temporary; nothing a resuming session needs).

## A. COPY: copied into this repository by LINK-07

| item (machine path) | what it is | now lives at |
|---|---|---|
| OP/team-10/lead/journey/journey-5.cjs (sha256 2e14b375…, 42,996 B) | the admission journey: it is cited in CONTROLLER.md and GREEN.md, crun.sh runs it, and every G-row is measured by it | T/journey/journey-5.cjs |
| OP/team-10/lead/journey/android-journey.cjs (234a2a0c…, 39,204 B) | the 22:19 version cited in handoff/10-integration/JOURNEY.md:10 | T/journey/android-journey.2219.234a2a0c.cjs |
| OP/team-10/lead/snap.sh, jrun2.sh | the integrator's snapshot and two-device runner (port 8500; GREEN G1/G2 were run this way) | T/journey/team10-lead-snap.sh, team10-lead-jrun.sh |
| SP/jrun.sh, SP/jrun-t10.sh | WATCHER-B's one-device runners (journey-5 / the team 10 tester's script) | T/controller/jrun.sh, jrun-t10.sh |
| SP/k1hist.py | walks the edition branch history and reports where K1 tripwires entered and left (the basis of the squash-before-merge rule) | T/release/k1hist.py |
| 53 scripts that committed hand-off docs cite by a /tmp path (OP/team-1..12 evidence, probes and tests; /tmp/nl010/team-1..4; /tmp/nl009/01,06,08,09) | the evidence keys behind EVIDENCE.md/TEST.md lines. Found with `grep -rhoE '/tmp/nl0[0-9]{2}(-opus)?/…\.(py\|cjs\|mjs\|sh\|js)'` over KB handoff/ and this repo, keeping the files that still exist | T/evidence/<path after /tmp/> (e.g. T/evidence/nl010-opus/team-9/evidence/verify_keys.py) |
| SP/journey/*.{sum,log,load,json} (19 non-empty files) and SP/snap/*.sha256 (6) | the controller's journey results and frozen-snapshot manifests (w1-fix, w2-adm, w3, w4, c1-nav5, a4-shell). a4-shell was still running at 01:25Z, so its files are partial | SESSIONS/state/journeys/controller/ |
| OP/team-10/lead/journey/*.{json,log,sum,load} (23) and OP/team-10/lead/snap/*.sha256 (4) | the integrator's runs behind GREEN.md G1 and G2 (base, base5, a1-loader, a2-shell, a3-card) | SESSIONS/state/journeys/team10-lead/ |
| OP/team-1/lead/rev3/ (202611012143-kuiper-shell.js sha256 50146d19…, 46,325 B; MODULE.json; MODULE.sha256; rev3.md draft HANDOFF) | **in-flight**: shell revision 3 (the pendingBack race fix). At 01:25Z it had not landed: KB handoff/01-shell/MODULE.sha256 still reads 1edf2e1a (rev 2) | SESSIONS/state/inflight/team-1-shell-rev3/. Delete it once KB carries 50146d19 |
| /tmp/s2.env … /tmp/s5.env | stamps S2=202611010114, S3=202611012022, S4=202611012027, S5=202611012135 | SESSIONS/state/stamps.env |

## B. IN-REPO: already persisted (no copy needed)

- SP/snap.sh, crun.sh, state.sh, poll.sh: the harness copied them byte-identical to T/controller/ at 01:15Z (with k1.py).
  SP/release/r1_squash.sh and merge_watch.sh are byte-identical to T/release/. /tmp/k1-staged.py is identical to
  T/k1-staged.py. The queue's COMMIT RULE names /tmp/k1-staged.py; use T/k1-staged.py.
- /tmp/opus-queue.txt is the harness's live queue; it is mirrored to SESSIONS/state/overnight-queue.md. At 01:15Z the
  two differed only in line 1 (whether 08 ledger was still pending), so the harness keeps this mirror current.
- The team test harnesses are in KB handoff/*/ (01-shell, 02-card, 03-layers, 04-loader, 05-see-through, 06-file,
  07-apps and 12-see-through-reader test.cjs; 08-drift test.cjs and drift_test.py; 09-law android-journey.cjs and
  test_edition_check.py; 10-integration android-journey.cjs; 00-stub stub-serve.cjs).
- SP/journey-t10.cjs (ecde2f34) = KB commit 2662a4f `editions/202611012135/handoff/10-integration/android-journey.cjs`.
  To get it back for jrun-t10.sh: `git -C KB show 2662a4f:editions/202611012135/handoff/10-integration/android-journey.cjs`.
- OP/team-10/tester/android-journey.cjs (b7b9b074) = KB 4543070, same path. OP/team-10/controller/loader-rev5-d9272b82.js
  = KB 833bd6e `editions/202611012135/modules/202611012145-loader.js`. OP/team-4/lead/rev5keep/* is in KB handoff/04-loader/
  (rev5/ and the patches).
- SP/w/modules.be99c8a1.json (the G2 manifest) is in KB acaad83. SP/w3-shell-src.json is in KB 01ca766.
- The KB branch edition/202611012135 is pushed. Local and origin were both at 4543070 at 01:19Z and later moved
  together to e927676. The working tree was clean at 01:20Z. By 01:27Z it held 9 changed or new files again (teams 3 and 12, plus
  CONTROLLER.md). Those exist only on this machine until the harness's next "team files as they land" commit, so that
  commit at each check-in is the persistence step for KB. Local-only branches are contained in origin: KB
  edition/202611012135-preview (736ece9, 0 commits ahead of origin/main), KB edition/202611012027, and globalgrid2050
  kuiper-editions-card (059ced08, in origin/main). A scan of every repo under /home/user and /home/user/estate found
  no other dirty tree, stash or unpushed branch.
- SP/opus13/check-served.mjs is in gridatlas ce1246e (branch served-check-kuiper-editions, PR #83). SP/opus13/verify-live.yml
  is in gridatlas 1adbd24. SP/opus13/import_homepage_owner.py is globalgrid2050 scripts/import_homepage_owner.py. SP/cpl.py
  is byte-identical to globalgrid2050 scripts/check_public_language.py.
- Every post draft was found on the link (its three longest lines matched the bodies of #9/#10): 35 team drafts under
  OP/*/post(s)/ and handoff drafts, plus 6 harness drafts (SP/handoff-comment.md, post-a4.md, post-finding-w3.md,
  post-review-03cut.md, post-review-nav.md, 04/comment.final.md). The integrator's working notes OP/team-10/evidence/
  {questions,checks,live-modules,live-candidates,nl009,poll,review}.md, the team 3 and team 7 evidence parts, and
  team-12 lead-evidence-0059.md all matched 3/3 inside KB handoff/*.md.

## C. NOTE: not copied (large or regenerable); how to get it back

- **Watch results**: /tmp/pages-e92ad5d.txt shows "pages build and deployment completed success 41365403840" and
  checking engineer 41365404779. /tmp/pr6-checks.txt shows checks=completed/success. /tmp/deploy-18aa446e.txt shows
  "Deploy GlobalGrid2050 Pages completed success 41368222618". All are recorded in FIXES/NL-010/OVERNIGHT.md.
- **Frozen snapshots** SP/snap/<name>/ (31 MB) and OP/team-10/{lead,tester}/snap/<name>/ are symlink mirrors of KB
  plus a copy of the edition folder without handoff/. They can be rebuilt with snap.sh, but only from the KB state of
  that moment, so the manifests (*.sha256, copied in A) are the record.
- **Running servers** (they die with the container). The controller's port 8590 serves SP/snap
  (`python3 -m http.server 8590 --bind 127.0.0.1` with that directory as cwd). The other journey ports: 8500 serves
  OP/team-10/lead/snap, 8501 serves KB root, 8502 serves OP/team-10/tester/snap/r4. About 40 further team servers run
  on ports 81xx/82xx/84xx/86xx/87xx. At 01:2xZ these journeys were running: the controller's a4-shell (journey-5 on
  8590), the team 10 tester r4, team 9 journey2, and the team 4/6/7/12 tests.
- **/tmp/kb-release** (68 MB) is a git worktree of KB main at e92ad5d. Recreate it with `git -C KB worktree add <dir> origin/main`.
- **SP/kb-copy** (77 MB) is a copy of KB editions 1 to 4. It is regenerable from KB.
- **/tmp/keys-src.json** (1.7 MB) is the source of keys.json (Edition 2). Regenerate it with KB tools/edition_keys.py;
  keys.json itself is committed in every edition folder.
- **/tmp/edition-layer.js, /tmp/bar-layer.js, /tmp/bar-css.txt** are the Edition 2 and 3 layer sources. They are
  embedded in the committed KB editions/202611010114, 202611012022 and 202611012027 index.html.
- **Clones**: /home/user/estate/<25 repos>, /home/user/estate/pipelinenews (frozen drift input),
  /home/user/globalgrid2050-homepage, /home/user/gg-domain, /home/user/pipelinenews. Re-clone them through the proxy;
  the branches are listed in B.
- **Session transcripts**: /root/.claude/projects/-home-user/e5bfe783-….jsonl (27 MB) and its subagents/ (312 files,
  162 MB). Not copied, because of their size and because they hold unscrubbed text that is not K1-checked. What
  mattered in them is on #10, in OVERNIGHT.md and in KB handoff/.
- **NL-011 study scratch** in SP (c/, t/, t2/, s/, scripts/, tools/keys.py, nl011/, nl011-05/, issues/, comments.json,
  blobmap.tsv, shaclaims.tsv, skew.py, keys.json, out.txt, t2.out, replied.json, req_heads.txt, kb-objs/nl-objs). It
  belongs to NL-011 agents 01–06, can be regenerated with `gh api …/issues/<n>/comments`, and those agents' reports
  must name the commands. LINK-07's own helpers are in SP/l07/.
- **Team run folders** in OP (run*/, out*/, probe*/, try*/, dbg*/, site/, screenshots, team-7 builder/clones 260 MB).
  Their results are in the committed KB handoff/*/TEST.md and EVIDENCE.md. The superseded per-run TEST.md copies
  (team 1 and team 7) are not needed.
- **Background task ids** (b4est9kvw etc.) are session-local. The send_later scheduled task trig_01NzUfCwezDi6GMZN2T2tMdK is server-side.

## D. DROP: temporary

- Session internals: /tmp/claude-*, *.diag.log, claude-code.log, mcp-config-*.json, claude-append-system-prompt.txt,
  cc-socks, environment-manager*, .ses, shell snapshots. **Never copy these** (they may carry tokens).
- NL-006 to NL-009 scratch, whose work is finished and committed elsewhere: /tmp/c1–c5, f1–f5*, ga*, gg-rp, w01–w20,
  w12_*, p*-handoff.md, p7b-*.tap, p7i-suite.txt, p10*, belt-*, ed2–ed4 *.cjs and PNGs, scaffold-G.mjs,
  lightning-at-G.mjs, /tmp/nl009 (43 MB; only the four cited scripts were copied in A), /tmp/nl010 (only the cited
  scripts were copied), nl010-t2-*, edition-check-fixture-*, served-*, tmp.*, ky-stub-*, ruby-build logs.
- SP: 04/, nl009/, nl009-02/, render/, render-out/, servedtest/, the rest of opus13/, door.html, pin.json, intent.txt,
  hc-*.txt, hb.txt, dm-out.html, kb-main.html, mb.js, http8590.log, state.last/state.now, __pycache__,
  journey-5.copy.cjs (ff545c24: journey-5 before the star-strip mask, superseded).
- OP/team-10/lead/jrun.sh (superseded by jrun2.sh, copied) and OP/team-10/tester/snap.sh (the lead's script with
  another output folder).
- Cited but already gone at 01:20Z: /tmp/nl010/team-1/accept-step1.cjs. The other "missing" hits were .json paths cut
  short by the regex.

## E. Resuming from this repository on a new machine

1. Clone neural-link-between-agents and kuiper-belt (`git checkout edition/202611012135`), plus gridatlas,
   globalgrid2050 and globalgrid2050-homepage if R3 follow-ups are needed. Install Playwright globally; use the
   preinstalled Chromium. Use `NODE_PATH=$(npm root -g)`.
2. Choose a work folder `W` and copy into it: T/controller/*.sh, and T/journey/journey-5.cjs as `W/journey-5.cjs`. Repoint the scripts:
   `sed -i "s#/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad#$W#g; s#/tmp/nl010-opus/team-10/lead/journey/journey-5.cjs#$W/journey-5.cjs#g; s#/home/user/estate/kuiper-belt#<KB clone>#g" $W/*.sh`
   Then `mkdir -p $W/snap $W/journey`.
3. Serve the snapshots: `(cd $W/snap && python3 -m http.server 8590 --bind 127.0.0.1 &)`. Run
   `$W/crun.sh <name> "Pixel 7"` and `$W/crun.sh <name> "Galaxy S24"`. Read `$W/journey/<name>-<device>.sum`.
4. Release: T/release/r1_squash.sh, then merge_watch.sh (repoint REPO and the worktree paths the same way).
   T/release/k1hist.py, run from the KB root, shows whether the branch history is K1-clean. Before each commit, run
   `python3 T/k1-staged.py`.
5. State to read first: SESSIONS/state/overnight-queue.md, FIXES/NL-010/OVERNIGHT.md (log), and KB
   handoff/10-integration/{CONTROLLER,GREEN,ADMISSIONS}.md, then issue #10 since its last acknowledged comment.
