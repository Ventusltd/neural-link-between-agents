# RESUME: how a brand-new session picks up the overnight Kuiper Edition 5 work from the link alone

Written by NL-011 LINK-10 "resume kit", 2026-11-02. The clock read 01:20Z at the start and 01:46Z at the last state
read (`date -u`). It was tested cold in `/tmp/nl011-10/` by cloning from GitHub through the proxy, not from local
paths (section 13). The reader starts with nothing but GitHub access to the Ventusltd repositories. Every step below
was run once, in the order given. Where a step failed the first time, the fix is already in the text.

Owner: Vikram Kumar, Ventus Ltd. Channels: NL-010 build https://github.com/Ventusltd/neural-link-between-agents/issues/10,
NL-011 link study https://github.com/Ventusltd/neural-link-between-agents/issues/11. Owner's reply style: plain
flowing text, no markdown, no headers, no bullet lists, no files unless asked, brief.

## 1. Access (do this first)

1. Attach the five repositories you will write to or call the API on. Use the `add_repo` tool with `access: "push"`
   for each: `Ventusltd/neural-link-between-agents`, `Ventusltd/kuiper-belt`, `Ventusltd/globalgrid2050`,
   `Ventusltd/globalgrid2050-homepage` and `Ventusltd/gridatlas`. Without this, `gh api repos/Ventusltd/<repo>/...`
   answers 403 "GitHub access to this repository is not enabled for this session" (measured 01:23Z for the estate
   repositories that were not attached).
2. The other estate repositories are public. `git clone` reads them through the proxy with nothing attached (measured
   for all 19 at 01:27Z). Attach them only if you need their API.
3. `gh` works for REST only. GraphQL is refused, so `gh pr view` and `gh pr list` fail with "GitHub GraphQL is not
   available". Use `gh api repos/Ventusltd/<repo>/pulls/<n>` and `.../commits/<sha>/check-runs` instead. Posting:
   `gh api repos/Ventusltd/neural-link-between-agents/issues/<n>/comments -F body=@file`. The flag is capital F.
   Lower-case `-f` posts the literal text "@file"; that happened nine times tonight.
4. If git or curl fails through the proxy, read `/root/.ccr/README.md` and run `curl -sS "$HTTPS_PROXY/__agentproxy/status"`.
   Never disable TLS checks. The sandbox cannot fetch `*.github.io` pages, so verify a publish by its Actions run.

## 2. Clone (tested commands; R is the root)

Use `R=/home/user`. The harness tools hard-code `/home/user/estate/kuiper-belt` (section 7), and kuiper-belt
`tools/drift.py` and `tools/edition_check.py` E9 look for the estate clones beside kuiper-belt (`$R/estate/<repo>`).

```bash
R=/home/user; mkdir -p $R/estate && cd $R/estate
git clone https://github.com/Ventusltd/neural-link-between-agents          # main; the link's files
git clone https://github.com/Ventusltd/kuiper-belt                         # all branches come with it
git -C kuiper-belt checkout edition/202611012135                           # the Opus working branch (local tracking branch)
git clone https://github.com/Ventusltd/globalgrid2050-homepage
git clone https://github.com/Ventusltd/gridatlas
# globalgrid2050 has 5.6 GB at HEAD: clone it blobless and sparse (316 MB, 30 s), with the Kuiper door and the workflows
git clone --filter=blob:none --sparse https://github.com/Ventusltd/globalgrid2050
git -C globalgrid2050 sparse-checkout set kuiper-editions .github
# the estate clones the drift tool and edition_check E9 need: every repository named in keys.json (21 with heads, plus pipelinenews)
for r in cvaa data-centres-gb data-grid-gb data-gridatlas elements energy-transition-simulator galaxies-wafers \
  grid-distance-maths gridmachine1 kuiper-drawing-engine maths particle-physics-drawing-engine pipelinenews \
  star-maker stars time-stone trillion-loop ventus-grid-engine worlds-; do git clone -q https://github.com/Ventusltd/$r & done; wait
```

Measured cold: neural-link and kuiper-belt took 37 s; the 19 estate clones in parallel took 5 min 43 s, about 2.3 GB.
pipelinenews alone is 1.1 GB. Do not clone globalgrid2050 without `--sparse`: the plain blobless clone filled 5.6 GB.
Keep the repository named `kuiper-belt` exactly, because the tools find it by name. The pipelinenews branch
`kuiper-edition-202610311905` (Edition 1's register) comes with the clone; it is not needed tonight.

## 3. Read the state, in this order

1. `neural-link-between-agents/LINK-RULE.md`: the owner's rule of 01:13Z. The link is the medium of exchange.
2. `SESSIONS/202611012145-kuiper-edition-harness-notes.md`: the mission, the folder rule, the See Through brief and
   the mobile problems. Its "Where things are on this machine" section is out of date in a new container; use
   section 2 above.
3. `SESSIONS/state/`: `overnight-queue.md` (the harness queue and its NOTE/COMMIT RULE lines), `PERSISTENCE.md`
   (what lived only in /tmp and where it is now), `stamps.env` (S2–S5), `journeys/` (the controller's and integrator's
   journey results), `inflight/team-1-shell-rev3/` (shell revision 3, staged; see 9.3).
4. `FIXES/NL-010/OVERNIGHT.md`: the plan R0–R4 and the log. Harness stamps before 01:02Z are approximate to ±10 min.
   GitHub run and commit times win (log entries of 01:02Z and 01:22Z).
5. `FIXES/NL-010/OPUS-BRIEF.md`, then in `FIXES/NL-010/ROADMAP.md` the Preface, step 9 (the release law), step 10,
   "The ten Opus teams", "Integration order" and "Open questions for the owner" (Q1–Q8).
6. `FIXES/NL-011/`: `LEDGER.md` (every open request, by addressee), `DECISIONS.md` (every ruling with its key),
   `SYNTHESIS.md` and `PROTOCOL-v2-proposal.md` (what the study says to change).
7. kuiper-belt, branch `edition/202611012135`, folder `editions/202611012135/handoff/10-integration/`:
   `CONTROLLER.md` (one line per controller loop; read the last one), `ADMISSIONS.md` (one row per admission attempt),
   `GREEN.md` (admitted states with no new red step; the word POINTER-READY appears here when R2 may go),
   `JOURNEY.md`, `TEST.md`, `BASE.md`. Then every `handoff/NN-*/` (HANDOFF.md, TEST.md, REQUESTS.md, MODULE.sha256).
8. The thread, newest last. Read #10 since the last comment you acknowledged; a new session reads at least from
   the delegation record on:
   `gh api "repos/Ventusltd/neural-link-between-agents/issues/10/comments?per_page=100&since=2026-11-02T01:19:00Z" --jq '.[]|"\(.id) \(.created_at)\n\(.body)\n====="'`
   and `issues/11/comments` the same way. Key comments: delegation 6566796733 (01:19:25Z), POINTER-READY definition and
   admission order 6566812411 (01:20:46Z), link rule 6566735197, controller REVIEW of shell rev 2 6566567995, See
   Through HANDOFF 6566607555, layers refusal 6566289513.
9. Post an ACK on #10 (PROTOCOL.md handshake) that names the newest comment you read and the heads you found
   (`git -C $R/estate/kuiper-belt rev-parse origin/main origin/edition/202611012135`).

## 4. Is the owner's delegation still in force? Decide before any merge

The delegation is recorded on #10 at 01:20Z (comment 6566796733, GitHub time 01:19:25Z). Its object: the harness may
merge new dated edition folders to kuiper-belt main and move the editions pointer to them. On globalgrid2050 and
globalgrid2050-homepage it may merge only the Kuiper door, the deploy allow-list line and the Kuiper editions card. It
may dispatch deploys and read-only checks. Scope: tonight's NL-010 work only. It suspends RELEASE.md's "only the owner
merges" and LAW.md 9.6 for exactly these objects. It does not cover GridAtlas releases, data pipelines, deletions or
any other repository. **Expiry: the owner's next message.**

A brand-new session exists because the owner (or an automation the owner set) started it. So: if the message that
started you is from the owner and does not renew or narrow the delegation in words, treat it as **expired**. The same
holds if any owner comment appears on #10 or #11 after 01:19:25Z. Once it has expired, nothing merges except through
LAW.md 9.6: PR A (preview), the owner's `ACCEPT <stamp>` as the first line of a comment on PR A, then PR B (pointer),
which only the owner merges. Agents never post ACCEPT. Write which reading you took as a DECISION-PROPOSAL on #10
before you act on it.

The written delegation covers editions folders and the editions pointer. It does not name `see-through/` folders or
the `see-through/index.html` pointer (team 12's work, 9.5). Treat those as owner-only even while the delegation stands.

## 5. The rules (each with where it is written)

- LINK-RULE.md 1–6. Every agent-to-agent message, ruling, refusal and hand-off is a comment on #10 (build) or #11
  (link study). Use the PROTOCOL.md envelope `[FROM → TO] [NL-0xx] [UTC from date -u]`, then TYPE, IN-REPLY-TO, SCOPE,
  HEAD, EVIDENCE, STATUS, DETAILS and ACTION REQUESTED. End with a blank line, `---`, then
  `_Generated by [Claude Code](https://claude.ai/code)_`. A file in /tmp or a direct message is not a message. State
  lives in the repositories (SESSIONS/, FIXES/<NL>/). Times come from `date -u`.
- The folder rule (harness notes; LAW.md 9.1). Every change is a new dated folder `editions/YYYYMMDDHHMM`, and earlier
  folders are never edited. Each folder holds index.html, keys.json, modules.json, modules/, README.md ("What changed
  from Edition N"), NOTICE.md, LICENCES.md, proof/edition-sha256.txt, proof/keys-summary.json, proof/render-*.png,
  proof/android-journey.json and proof/ci_check.log. Each release adds an entry to editions/README.md (and updates its
  "current edition" sentence) and to the Editions section of the root README.md.
- The pointer in three places (LAW.md 9.2). `editions/index.html` names the stamp at line 7 (meta refresh), line 11
  (the link) and line 12 (`location.replace`). It points at `<stamp>/` with no `/belt/`. From Edition 5 the
  `location.replace` forwards `location.search + location.hash` (handoff/09-law/pointer.patch). edition_check E4
  refuses an Edition 5+ pointer that forwards only the hash. On main e92ad5d the pointer still names `202611012027`.
- `python3 tools/ci_check.py` must print `RESULT: PASS` (K1 privacy, K2 sums, K3 syntax, K4 order) before any push
  to kuiper-belt main. `python3 tools/edition_check.py` (E1–E9; `--pre-cut` until the integrator cuts, after which E3
  covers handoff/ moved to proof/handoff/) must print `RESULT: PASS` before the pointer moves.
- The K1 privacy check (LINK-RULE 5). Before committing or posting any file, run `leaks()` from kuiper-belt
  `tools/check_proof.py`; it must return 0. Write a name whose digest is on the not-public list as "[K1-forbidden
  name]".
  `python3 -c "import sys; sys.path.insert(0,'$R/estate/kuiper-belt/tools'); from check_proof import leaks; print(leaks(open(sys.argv[1],encoding='utf-8',errors='replace').read()))" FILE`.
  For staged kuiper-belt files, run `python3 $R/estate/neural-link-between-agents/FIXES/NL-010/tools/k1-staged.py`
  from the kuiper-belt root after `git add`. On a failure, `git reset` the file and tell its team on #10.
- History rule (overnight-queue.md NOTE lines). The branch `edition/202611012135` carries K1 tripwires in its history
  (commits b8e7c74, b4a5dba, 38ed53c, b9d514c and the see-through.json commits before the fix). Main must never receive
  that history. A preview reaches main only by **path checkout from the branch tip onto a fresh branch from
  origin/main**, as one commit (`FIXES/NL-010/tools/release/r1_squash.sh`), then a `--no-ff` merge of that one-commit
  branch. Never `git merge edition/202611012135`. `FIXES/NL-010/tools/release/k1hist.py` shows where each tripwire
  entered and left.
- Who touches what (OPUS-BRIEF, ROADMAP table). Teams touch only their "may touch" column. index.html, modules.json,
  ADMISSIONS.md and GREEN.md belong to the controller. The pointer, editions/README.md and the root README change only
  in the release step. cosmos/, tools/key.py, tools/edition_keys.py, every earlier edition folder and see-through/
  folders other than team 12's new one are untouchable.
- Agents never post ACCEPT. The harness commits. Agent workers do not commit or push unless their brief says so.

## 6. Where the state is

| what | where |
|---|---|
| harness queue, persistence map, stamps, journey results, in-flight shell rev 3 | neural-link `SESSIONS/state/` |
| plan R0–R4 and the overnight log | neural-link `FIXES/NL-010/OVERNIGHT.md` |
| the roadmap, briefs and team STEPS | neural-link `FIXES/NL-010/` (ROADMAP.md, OPUS-BRIEF.md, BRIEF.md, team-1..5/) |
| homepage card and served-domain hand-offs | neural-link `FIXES/NL-010/handoff-11-homepage.md`, `handoff-13-served.md`, `served-check.md` |
| harness and controller tools | neural-link `FIXES/NL-010/tools/` (`k1-staged.py`; `release/` r1_squash.sh, merge_watch.sh, k1hist.py; `controller/` crun.sh, jrun.sh, jrun-t10.sh, snap.sh, state.sh, poll.sh, k1.py; `journey/` journey-5.cjs and the integrator's snap/jrun; `evidence/` the /tmp scripts the hand-offs cite) |
| the link study, ledger and decision log | neural-link `FIXES/NL-011/` |
| the edition being built | kuiper-belt branch `edition/202611012135`, folder `editions/202611012135/` (index.html, modules.json, modules/, data/, proof/) |
| the edition hand-off folders | `editions/202611012135/handoff/` 00-stub, 01-shell, 02-card, 03-layers, 04-loader, 05-see-through, 06-file, 07-apps, 08-drift, 09-law, 10-integration, 12-see-through-reader |
| the release law and the gate tool | kuiper-belt `editions/LAW.md`, `tools/edition_check.py` (on the branch) |
| team 12's new See Through folder | kuiper-belt branch `edition/202611012135`, `see-through/202611020012/` |
| live main | kuiper-belt main e92ad5d (Edition 5 preview folder, pointer on Edition 4); globalgrid2050 main 18aa446e (door `kuiper-editions/` and homepage card) |

The edition branch's working tree on the old machine changes between the harness's "team files as they land" commits.
After a container loss, only what is on `origin/edition/202611012135` exists. Check its last commit time against the
newest HANDOFF on #10.

## 7. The tools hard-code the old machine's paths: fix them in a copy, never in the repository

`FIXES/NL-010/tools/{controller,release,journey}/*.sh` and `k1-staged.py` name the following paths:
`/home/user/estate/kuiper-belt` (true again if you used R=/home/user),
the old scratchpad `/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad` (SP) and
`/tmp/nl010-opus/team-10/lead/journey/journey-5.cjs`. Copy them to your own scratchpad (`$SCRATCH`) and rewrite them
there:

```bash
mkdir -p $SCRATCH/journey $SCRATCH/snap $SCRATCH/release
cp $R/estate/neural-link-between-agents/FIXES/NL-010/tools/controller/*.sh $R/estate/neural-link-between-agents/FIXES/NL-010/tools/release/*.sh $SCRATCH/
cp $R/estate/neural-link-between-agents/FIXES/NL-010/tools/journey/journey-5.cjs $SCRATCH/
sed -i -e "s#/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad#$SCRATCH#g" \
       -e "s#/tmp/nl010-opus/team-10/lead/journey/journey-5.cjs#$SCRATCH/journey-5.cjs#g" $SCRATCH/*.sh
```

`k1-staged.py` imports from `/home/user/estate/kuiper-belt/tools`. It works unchanged with R=/home/user; otherwise use
the one-liner in section 5. `jrun-t10.sh` wants `$SCRATCH/journey-t10.cjs`; get it with
`git -C $R/estate/kuiper-belt show 2662a4f:editions/202611012135/handoff/10-integration/android-journey.cjs > $SCRATCH/journey-t10.cjs`.
The release scripts commit with a `Claude Fable 5.1` co-author line. Change it to the attribution your own session is given.

## 8. Checks to run on arrival (cold results at 01:33Z, kuiper-belt edition/202611012135 at e927676)

- `python3 tools/ci_check.py`: RESULT: PASS (K1 738 tracked files, 0 private digests).
- `python3 tools/edition_check.py` with all 22 clones present: **RESULT: FAIL, E9 only**. data/drift.json has sha256
  388103129b90, while the drift re-computed from the recorded heads gives 1640823a7173 (118,553 vs 118,433 bytes). This
  is the same FAIL the controller posted at 01:00Z (6566567995 item 4). It is team 8's to fix; see 9.2. With the
  estate clones missing, E9 reads NOT EVALUATED and the result is PASS, so a PASS without the clones proves nothing
  about drift. E2 lists 5 modules pending admission. E3 reads NOT EVALUATED until the cut. E4 PASS (the pointer is
  still on 202611012027).
- modules.json `order` in the pushed branch at 01:33Z: [hello, kuiper-shell, line-card]. The controller withdrew the
  shell at 01:37Z, so the next harness commit carries [hello, line-card] (be99c8a1, G2). The cold clone served from its root gave 200 for
  `editions/`, `editions/202611012135/`, `modules.json`, `cosmos/repos.tsv`, `cosmos/wafer.tsv` and `see-through/`.

## 9. The open steps (state at 01:46Z; re-read GREEN.md, CONTROLLER.md and #10 first)

1. **R2, the pointer, when GREEN.md says POINTER-READY.** The ruling of 01:20Z (6566812411) defines POINTER-READY as
   base + loader + kuiper-shell rev 2 + line-card green on Pixel 7 and Galaxy S24, with no new red step and the base's
   two reds (bar on two rows; no SEE THROUGH control) turned green. Layers no longer blocks it. **State at 01:45Z:
   NOT POINTER-READY.** The a4-shell verdict (CONTROLLER.md loop 8, GREEN.md note) was Pixel 7 15/16 and Galaxy S24
   13/16. Shell rev 2 cured both base reds. It added `pinch-drag` and `spark-tap` on Galaxy S24 (the SEE THROUGH strip
   sits over the wafer above an open card and takes a pinch finger; the spark moved 144 px), and `whole-wafer` on both
   (the wafer screenshot timed out, a harness limit under load). The controller withdrew the shell at 01:37Z. modules.json
   is back to G2 (be99c8a1, [hello, line-card]); that is the published preview state. A REVIEW to OPUS-1 was next. R2
   now waits for a shell revision that moves the strip out of the wafer's touch area over an open card, then a green
   two-phone run. When the controller writes POINTER-READY and posts it on #10, the harness does the following, if
   section 4 allows it:
   (a) the integrator's cut: README "What changed from Edition 4" naming every admitted module and NL-009 fix folded
   in, NOTICE.md, LICENCES.md, handoff/ moved to proof/handoff/, proof/edition-sha256.txt over every file;
   `edition_check.py` (no `--pre-cut`) PASS. That needs E9 green (9.2), or a written ruling on #10 that drift is outside
   this cut.
   (b) r1_squash.sh, path checkout of the folder and tools from the branch tip onto a fresh branch from origin/main.
   This also replaces the known defect on main: modules.json names loader reference 25a16f1d, but the file on main
   carries d9272b82.
   (c) In that same worktree, move the pointer: three places to `202611012135/`, `location.search + location.hash`.
   Add the editions/README.md entry, update its current-edition sentence, and add the root README Editions entry.
   Then `ci_check` and `edition_check` must PASS.
   (d) Run k1-staged.py, then merge_watch.sh: a `--no-ff` merge to main, a push, and a watch on
   `gh api "repos/Ventusltd/kuiper-belt/actions/runs?head_sha=<sha>&per_page=5"` until "pages build and deployment"
   reads completed success.
   (e) Record the step in OVERNIGHT.md and on #10 with the run id, take screenshots from the journey for the owner, and
   run the journey once more through `editions/` (the pointer).
   Once the pointer names 202611012135, that folder is frozen (folder rule; OVERNIGHT R4). Later admissions are cut
   into the next dated folder (Edition 6) with its own stamp and branch. Before cutting, confirm this reading on #10;
   the 01:20Z ruling says "a set worth a new number becomes a new dated edition".
2. **The remaining admissions, in this order** (6566812411). Each one is admitted by the controller on a frozen
   snapshot and journeyed on both phones; each green set becomes a new preview.
   (1) See Through, team 5: handed off 6566607555, module 87a88e48…, licence CERN-OHL-S-2.0. It was tested without
   the layers module, so the registry path is NOT EVALUATED.
   (2) Drift, team 8: handed off with a revision, 49/49 on both phones. E9 FAIL: data/drift.json must reproduce from
   tools/drift.py, or the differing inputs must be named.
   (3) File, team 6: in team 5's run (6566607555) the loader refused it (`missing hook layers`) because layers is not admitted.
   Say on #10 whether File waits for layers or drops that `requires`.
   (4) Apps, team 7: its K1 screenshot is removed; the hand-off is finishing.
   (5) Layers, team 3: refused (REVIEW 6566289513; TEST.md run 9). It must carry the four behaviours (the 96 px
   panel close, the card-resize keeper, the fly duration and content-visibility), keep `edSel`, have one scroller and
   scope the shell's leftover list CSS. LEDGER rows 6564857812, 6565553299 and 6566073338 are open.
   (6) Law, team 9: edition_check E1–E9, LAW.md and LICENCES.md are delivered. LAW.md lands with the release.
3. **Shell revision 3** (the pendingBack fix for the Pixel 7 landscape A5 race), sha256 50146d19…, 46,325 B. It is
   staged in `SESSIONS/state/inflight/team-1-shell-rev3/`. Rev 2 got no GREEN row (withdrawn 01:37Z), so the next
   shell hand-off has to carry both the A5 fix and the strip-over-wafer fix of 9.1. Delete the staged
   copy once kuiper-belt handoff/01-shell/MODULE.sha256 reads 50146d19.
4. **gridatlas PR #83** (https://github.com/Ventusltd/gridatlas/pull/83, branch `served-check-kuiper-editions`, head
   ce1246ea, team 13). Open, not draft. It adds three report-only lines to `tools/release/check-served.mjs` (the door,
   the pointer and the homepage row). Checks at 01:36Z: size-guard success, dc-browser-smoke skipped, **cartridge-gate
   failure** on one unrelated test, `not ok 80 - H3/I1/J2: tapping a flash opens a Lightning-owned docked card`
   (run 41370165741, job 125038723260). Main's own checks are green. gridatlas is outside the delegation, so do not
   merge it. Find out whether test 80 also fails on main (re-run the job, or run the gate on main). Post the finding
   on #10 and leave the merge to the owner.
5. **Team 12's See Through reader folder** (`see-through/202611020012/` on the edition branch, a copy of 202610050609
   with team 5's hash-reader patch; plus the pointer `see-through/index.html` in three places, forwarding search +
   hash, and a README row). TEST.md at 01:22Z: **REFUSED, run 2 FAIL 19/21 on Pixel 7**. R1 is blocking: `readLink()`
   in descent.js does not clear `S.note` or `S.input` on hashchange. F1–F3 are open for the lead. No HANDOFF is posted
   yet. When it passes, it ships as its own path-checkout preview. Moving the see-through pointer is owner-only
   (section 4).
6. Owner questions still open: ROADMAP Q1–Q8. Q7 changed: the shell measured the title threshold at 434 px, not
   381, so a Pixel 7 also shows the strip. Also open: homepage issue #5 and the governance finding of NL-008.
   Collected in FIXES/NL-011/LEDGER.md "OW-*" rows.

## 10. The controller's duties (OPUS-CONTROLLER; CONTROLLER.md header and the rulings of 00:59Z–01:20Z)

- Owns admissions: index.html, modules.json, the rows of ADMISSIONS.md, GREEN.md. Never edits a team's module and
  never posts ACCEPT.
- Admits a module only when its handoff folder has MODULE.sha256 equal to the file on disk, a TEST.md reading PASS on
  Pixel 7 and Galaxy S24 with zero console errors, and the HANDOFF on #10. The record goes into modules.json verbatim
  from handoff/NN/MODULE.json. Then the controller freezes a snapshot (snap.sh: the edition folder copied without
  handoff/, the rest symlinked, sha256 list beside it) and runs journey-5.cjs on it, one device at a time, on port 8590.
- If a step that was green turns red, the controller withdraws the record and posts a REVIEW on #10 naming the step
  and the measurement. If no new red appears on either phone, it writes the GREEN.md row. It writes POINTER-READY in
  GREEN.md when the 01:20Z definition is met, and posts that on #10.
- Wake list: `state.sh` in the order 5, 8, 6, 7, 3, 9, polled by `poll.sh`. Each loop adds one line to CONTROLLER.md
  with the clock time.
- Keeps `edition_check.py --pre-cut` and `ci_check.py` green, and names the team on any K1, E6 or E9 failure. When a
  team overwrites a referenced file in place (as happened with the loader rev 5), the controller restores the
  recorded bytes from git and asks for a new stamped file.
- Runs the K1 check on every post (tools/controller/k1.py) and posts with `-F body=@file`.

The harness's own duties (OVERNIGHT.md "Watchers" and the check-in log): wake about every 40 minutes. At each wake it
commits landed files on `edition/202611012135` ("team files as they land", after k1-staged.py), commits neural-link
state, relaunches ended agents (20 concurrent; Opus only since 01:05Z), publishes each GREEN state as a path-checkout
preview, moves the pointer at POINTER-READY, and logs every step in OVERNIGHT.md and on #10.

## 11. How to run the Android journey

Needs: Playwright and its Chromium are preinstalled; `NODE_PATH=$(npm root -g)`, never install. In the cold check,
`devices['Pixel 7']` and `devices['Galaxy S24']` exist and `node --check` on the journey passes. Use the SwiftShader
flags `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist` (inside the scripts).
Wait 6–8 s after load and after each fly; screenshots have a 180 s timeout. A one-device run takes 15–30 min under
load (the G1 and G2 pairs took 23:19–23:47Z and 00:02–00:26Z).

```bash
cd $R/estate/kuiper-belt && git checkout edition/202611012135
# the controller's way: a frozen snapshot, then one device at a time (scripts rewritten as in section 7)
$SCRATCH/snap.sh a5-mystate                      # -> $SCRATCH/snap/a5-mystate (edition copied, rest symlinked)
(cd $SCRATCH/snap && python3 -m http.server 8590 --bind 127.0.0.1 &)
$SCRATCH/jrun.sh a5-mystate "Pixel 7" keep       # -> $SCRATCH/journey/a5-mystate-pixel-7.{json,log,sum}
$SCRATCH/jrun.sh a5-mystate "Galaxy S24" keep
# the plain way: serve the repository root and run the team 10 tester's script (also does --all: + Pixel 7 landscape)
python3 -m http.server 8502 --bind 127.0.0.1 &   # from the kuiper-belt root; the page loads ../../cosmos/*.tsv
NODE_PATH=$(npm root -g) node editions/202611012135/handoff/10-integration/android-journey.cjs \
  http://127.0.0.1:8502/editions/202611012135/ $SCRATCH/out --device "Pixel 7"
```

Read the result against GREEN.md. The base reds are `load` (bar on two rows) and `see-through`; with the shell
admitted both must be green. A run that cannot evaluate a step writes NOT EVALUATED with the reason, and that list
goes into the PR body. The journey steps are ROADMAP 9.4 (a)–(o): bar one row at 360 and 393 px; each title opens and
closes on the same tap, a wafer tap and the back gesture; SEE THROUGH opens `../../see-through/`; a LINES pick shows
the card with the line of code as header; NEXT three times; pinch zooms the wafer; a 4 px spark is hit; landscape and
font scale 1.3; every module admitted.

## 12. First moves for a resuming harness (in order)

1. Do sections 1–3, and post the ACK on #10.
2. Decide section 4 and post it as a DECISION-PROPOSAL.
3. Run section 8. If anything differs from the values above, post it as a FINDING.
4. Read GREEN.md. If it says POINTER-READY and the delegation stands, do 9.1. If not, relaunch the controller with
   section 10 as its brief and the wake list of 9.2.
5. Open items for the owner go on #10 addressed to OWNER in one comment: section 4's reading, Q1–Q8, PR #83 and the
   see-through pointer.

## 13. Cold test record (LINK-10, 01:23Z–01:38Z, scratch `/tmp/nl011-10/estate`)

Run: every clone of section 2 from `https://github.com/Ventusltd/...` through the proxy (all exit 0); the branch
checkout; listing of SESSIONS/, SESSIONS/state/, FIXES/NL-010/tools/ and FIXES/NL-011/; the handoff folders on the
branch (152 tracked files in handoff/); ci_check; edition_check without and with the estate clones; a local serve of
the edition; the Playwright device check; `node --check` of the journey. Failures found and fixed in this text:
(1) `gh api` on unattached repositories returns 403, so add_repo was added (1.1); (2) `gh pr view` fails because
GraphQL is refused, so REST calls are given (1.3); (3) the plain blobless clone of globalgrid2050 wrote 5.6 GB, so
the clone is now sparse (2); (4) `edition_check` without the estate clones passes with E9 NOT EVALUATED, so the 19
clones were added and the real E9 FAIL is recorded (8); (5) the tools hard-code the old scratchpad and a /tmp journey
path, so a rewrite in a copy is given (7); (6) at 01:23Z the journey copies, PERSISTENCE.md and inflight/ were not yet
pushed (the harness pushed them in 6f5af06, checked by a pull at 01:38Z). Also run (01:40Z–01:45Z, load 38): section 7's copy-and-rewrite (no old path left), snap.sh against the cold clone
(24 files hashed), and journey-5.cjs on that snapshot, Pixel 7, cut off by a 240 s timeout. load, modules (3
admitted: hello, kuiper-shell, line-card), edition-open/close, lines-open/filter/pick, card-details/close and
key-e-1..3 had passed when the timeout closed the browser. The timeout caused the one harness FAIL, so the run is
not a verdict. Not run here: a full two-phone journey, and any merge, push or post other than this kit's one
HANDOFF on #11.
