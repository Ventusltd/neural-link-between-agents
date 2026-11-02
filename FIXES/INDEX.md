# INDEX: every NL issue, every FIXES/ and SESSIONS/ entry, and where the Kuiper Edition 5 work lives

Kept by NL-011 LINK-11 "index" (FIXES/NL-011/QUEUE.md item 11). Clock read with `date -u` at writing: 2026-11-02T01:26Z.
Newest first in every list. Every line carries a key. Key forms: `#N` = https://github.com/Ventusltd/neural-link-between-agents/issues/N;
`#N/c<id>` = that issue's comment `#issuecomment-<id>`; `nl@<sha>` = a commit of this repository; `kb@<sha>` = a commit of
Ventusltd/kuiper-belt; `HO/` = kuiper-belt `editions/202611012135/handoff/` on branch edition/202611012135 (working tree
as read at 01:20-01:26Z, tip `kb@e927676`); `path:line` = a line of that file. Comment counts and last-comment times are from
`gh api repos/Ventusltd/neural-link-between-agents/issues/<n>/comments --paginate` at 01:23Z; last-commit keys are from
`git log -1 --format='%h %ad' -- <path>` in this repository at 01:26Z. Times are GitHub's (PROTOCOL.md: the GitHub timestamp
wins); harness stamps in OVERNIGHT.md before 01:02Z are approximate to about 10 minutes (FIXES/NL-010/OVERNIGHT.md:47-48).

## 1. NL issues (#11 to #1)

| # | title (short) | opened | state | comments · last comment | what it decided | key |
|---|---|---|---|---|---|---|
| 11 | NL-011: twelve Opus agents study and run the neural link; the link is the medium of exchange | 2026-11-02T01:13:53Z | open | 0 · none yet (this index posts the first HANDOFF) | Opened the study (01–06) and the link-running agents (07 persistence, 08 ledger, 09 decisions, 10 resume kit, 11 index, 12 live reviewer); put LINK-RULE.md in force: every agent message, ruling and resumable state lives on the link | #11 body; LINK-RULE.md; nl@d6d5b9a |
| 10 | NL-010: the ten-step roadmap, GridAtlas lessons into the Kuiper, See Through the star player | 2026-11-01T20:43:25Z | open | 66 · 2026-11-02T01:20:46Z | ROADMAP.md is the governing document (Fable teams 1–5 PASS, consolidated by T5B); 40 then 50 Opus agents build Edition 5 202611012135; overnight delegation recorded (harness may merge new edition folders, move the pointer, and merge only the Kuiper door, deploy allow-list line and homepage card); four rulings moved onto the link (loader reference rev 4, E3 at final cut, shell rev 2 admitted with A5 MINOR, page owns card history); POINTER-READY = base + loader + shell rev 2 + line-card green on both phones; order after the pointer 5, 8, 6, 7, 3, 9 | #10/c6564201811; #10/c6566796733; #10/c6566812411 |
| 9 | NL-009: Kuiper Edition 5, mobile UI fixed by ten Fable agents, See Through as a button (Android) | 2026-11-01T20:36:23Z | open | 10 · 2026-11-01T23:42:50Z | Ten round-1 Android findings with patches (01 bar … 10 journey); Edition 4 baseline journey red on `load` (bar two rows) and `see-through` (no control); patches folded into Edition 5 by Opus teams 1, 2, 3, 4, 10 | #9/c6565653998; FIXES/NL-009/round1/; FIXES/NL-010/OPUS-BRIEF.md (NL-009 paragraph) |
| 8 | NL-008: QA of release 202610312138 (v9.188), data baseline 226/225, homepage pin, Kuiper edition 202610311905 | 2026-10-31T23:22:25Z | open | 6 · 2026-10-31T23:39:01Z | Consolidated QA verdict: PASS for the release, data, served homepage and the edition; one MAJOR (process), five MINOR; housekeeping fixes only | #8/c6550679096 |
| 7 | NL-007: fix plan, UK data-centre baseline 227 → 226 (Wapseys Wood), DCFSHA re-pin, composition note, Cowley pin | 2026-10-31T20:39:09Z | open | 50 · 2026-10-31T23:21:31Z | Five-agent design then implementation: generation 202610312138 (v9.188) released, pinned on the homepage and served (gridatlas main 41729af0) | #7/c6550516723; FIXES/202610311905/patches/12-steps-5-7-evidence.md |
| 6 | NL-006: Kuiper edition 202610311905, estate map vs Kuiper code (harness + 25-agent swarm) | 2026-10-31T19:05:40Z | open | 10 · 2026-11-01T20:33:27Z | Kuiper Editions 1–4 published one after another (202610311905 at kb@b4b4979, 202611010114 at kb@64697d7, 202611012022 at kb@7dc70eb, 202611012027 at kb@018b46a); the editions pointer opens Edition 4 | #6/c6551009550; #6/c6551737158; #6/c6563430092; #6/c6563512049 |
| 5 | NL-005: Agent F (Claude), onboarding and continuity handoff | 2026-10-29T22:29:50Z | open | 4 · 2026-10-29T22:57:02Z | Agent F relayed the owner's chat acceptance of GridAtlas 202610292044 and ruled a relay is not acceptance: the owner must post `ACCEPT` on gridatlas PR #75 himself | #5/c6510460987 |
| 4 | NL-004: Agent E, awaiting assignment | 2026-10-29T22:00:49Z | open | 2 · 2026-10-29T22:10:49Z | Mailbox handshake only (ACK both ways); no write scope given | #4/c6509491541 |
| 3 | NL-003: Agent D, awaiting assignment | 2026-10-29T22:00:47Z | open | 2 · 2026-10-29T22:10:47Z | Mailbox handshake only; no write scope given | #3/c6509490982 |
| 2 | NL-002: Agent C, awaiting assignment | 2026-10-29T22:00:45Z | open | 2 · 2026-10-29T22:10:46Z | Mailbox handshake only; no write scope given | #2/c6509490425 |
| 1 | NEURAL-LINK 001: GridAtlas #73, Agent A ↔ Agent B | 2026-10-29T21:57:21Z | open | 7 · 2026-10-29T22:46:01Z | First use of the link: data-centre count 204 vs 227 reconciled (old PR #74 vs data-grid-gb PR #3); browser QA PR #77 PASS; served preview UNVERIFIED | #1/c6510280293; #1/c6509658721 |

All eleven issues are open (`gh api repos/Ventusltd/neural-link-between-agents/issues/<n> --jq .state`, 01:20Z).

## 2. FIXES/ and SESSIONS/ (newest last commit first)

Status words: LIVE-LOG (still appended), DONE (closed work), IN-PROGRESS, UNCOMMITTED (on disk, not yet in git at 01:26Z).

| path | what it is | issue | status | key |
|---|---|---|---|---|
| FIXES/INDEX.md | this index | #11 | UNCOMMITTED (the harness commits) | FIXES/NL-011/QUEUE.md item 11 |
| FIXES/NL-011/ | the study of the link and the link-running agents' files | #11 | IN-PROGRESS | nl@70d939d |
| FIXES/NL-011/LEDGER.md | LINK-08 open-request ledger (every open REQUEST/BLOCKER, refreshed every 10 min) | #11 | UNCOMMITTED, IN-PROGRESS | `git status --short` 01:26Z |
| FIXES/NL-011/QUEUE.md | launch queue for agents 07–12 kept on the link | #11 | LIVE-LOG ("queue complete") | nl@70d939d |
| FIXES/NL-011/02-failures.md | study 02, failure catalogue | #11 | DONE (file landed) | nl@aa48eae |
| FIXES/NL-011/03-topology.md | study 03, topology and latency | #11 | DONE (file landed) | nl@1325317 |
| FIXES/NL-011/05-governance.md | study 05, governance and authority (led to the delegation record #10/c6566796733) | #11 | DONE (file landed) | nl@96b2c93 |
| FIXES/NL-011/01-protocol.md, 01-protocol.py | study 01, protocol adherence, and its counting script | #11 | DONE (file landed) | nl@ca4ab8a |
| FIXES/NL-011/BRIEF.md | brief for the six study agents | #11 | DONE | nl@3e13873 |
| FIXES/NL-011/ (04, 06, DECISIONS.md, PROTOCOL-v2-proposal.md, SYNTHESIS.md) | expected, not on disk at 01:26Z | #11 | PENDING | FIXES/NL-011/BRIEF.md; QUEUE.md item 09 |
| SESSIONS/state/ | harness state on the link: overnight queue, edition stamps, in-flight work, journey snapshots | #10, #11 | LIVE-LOG | nl@70d939d |
| SESSIONS/state/overnight-queue.md | the harness's queue, launch log and commit rule (run k1-staged after `git add`) | #10 | LIVE-LOG | nl@70d939d |
| SESSIONS/state/stamps.env | edition stamps S2–S5 (S5=202611012135) | #10 | UNCOMMITTED | `git status --short` 01:26Z |
| SESSIONS/state/inflight/team-1-shell-rev3/ | kuiper-shell rev 3 (`pendingBack`) frozen until rev 2's GREEN row | #10 | UNCOMMITTED, HELD | HO/10-integration/ADMISSIONS.md:28 |
| SESSIONS/state/journeys/ (controller/, team10-lead/) | snapshot sha256 lists of admission journeys | #10 | UNCOMMITTED | `git status --short` 01:26Z |
| FIXES/NL-010/ | the Kuiper Edition 5 roadmap, briefs, overnight log, served check, hand-offs of teams 11/13, tools | #10 | IN-PROGRESS | nl@70d939d |
| FIXES/NL-010/OVERNIGHT.md | overnight plan (owner ACCEPT, small steps R0–R4) and its log; time correction at :47 | #10 | LIVE-LOG | nl@70d939d |
| FIXES/NL-010/tools/ | harness and controller scripts moved into the repo: k1-staged.py, controller/ (crun, snap, state, poll, k1), release/ (r1_squash, merge_watch, k1hist), journey/, evidence/nl009/ | #10 | committed in part (8 files); controller/jrun*.sh, journey/, evidence/, release/k1hist.py UNCOMMITTED; poll.sh, state.sh modified | nl@f5b7358; `git status --short` |
| FIXES/NL-010/handoff-13-served.md | Opus team 13 hand-off: gridatlas branch served-check-kuiper-editions ce1246e, PR body | #10 | DONE (PR #83 open) | nl@fd963f9; gridatlas PR #83 |
| FIXES/NL-010/served-check.md | team 13's served-domain check: door, homepage card bundle, Edition 5 preview | #10 | DONE | nl@a9b5919 |
| FIXES/NL-010/handoff-11-homepage.md | Opus team 11 hand-off: Kuiper editions card on globalgrid2050.com | #10 | DONE (deployed) | nl@3c17c9a |
| FIXES/NL-010/team-11/ | team 11 PLAN.md, render-pixel7.cjs, img/ (Pixel 7 card and catalogue row) | #10 | DONE | nl@3c17c9a |
| FIXES/NL-010/OPUS-BRIEF.md | brief for the Opus teams (where to work, roles, ports, posting rule) | #10 | DONE | nl@c2d9b33 |
| FIXES/NL-010/team-2/ | Fable team 2 STEPS.md, EVIDENCE.md, REVIEW.md (PASS) | #10 | DONE | nl@886677a; #10/c6564171256 |
| FIXES/NL-010/ROADMAP.md | consolidated ten-step roadmap, the governing document; Opus table at :965-982 | #10 | DONE | nl@81662d7; #10/c6564201811 |
| FIXES/NL-010/team-3/ | Fable team 3 (See Through, File menu) STEPS, EVIDENCE, REVIEW PASS, img/ | #10 | DONE | nl@c4f9701; #10/c6564200705 |
| FIXES/NL-010/team-4/ | Fable team 4 STEPS, EVIDENCE, REVIEW PASS | #10 | DONE | nl@a432b4f; #10/c6564134343 |
| FIXES/NL-010/BRIEF.md | brief for the five Fable roadmap teams | #10 | DONE | nl@d7805cc |
| FIXES/NL-010/team-1/ | Fable team 1 (shell) STEPS, EVIDENCE, REVIEW PASS, img/ | #10 | DONE | nl@4ed9bfe; #10/c6564036091 |
| FIXES/NL-010/team-5/ | Fable team 5 (law and proof, consolidator) STEPS, EVIDENCE, REVIEW | #10 | DONE | nl@07e50be; #10/c6563877491 |
| FIXES/NL-009/ | Android UI round 1 by ten Fable agents | #9 | DONE | nl@1cdf6d7 |
| FIXES/NL-009/round1/ | BRIEF.md, findings 01-bar … 10-journey with patches, results JSON, img/ (57 tracked files) | #9 | DONE | nl@1cdf6d7; #9/c6565653998 |
| FIXES/NL-009/android-journey.cjs | reusable Playwright Android journey (FABLE-10), base of journey-5.cjs | #9 | DONE | nl@418e215 |
| SESSIONS/202611012145-kuiper-edition-harness-notes.md | harness session notes, read first by a resuming agent (#9, #10 cite it) | #6, #9, #10 | DONE (frozen at 20:36Z) | nl@04b8b87 |
| FIXES/202610311905/ | NL-007 fix: patches/ 01–12, OWNER-PUSH-1/2, README, bundles, gate logs, steps 5–7 evidence (23 files) | #7, #8 | DONE | nl@388c7b6 |
| FIXES/202610311905-datacentre-baseline.md | NL-007 design document: baseline 227 → 226, DCFSHA re-pin, composition note | #7 | DONE | nl@2cb893f |

## 3. Where the Kuiper Edition 5 work lives

Repository Ventusltd/kuiper-belt, branch `edition/202611012135` (tip kb@e927676, 292 commits in `git log origin/edition/202611012135`),
edition folder `editions/202611012135/`. Live admitted order: `modules.json` order [hello, kuiper-shell, line-card]
(editions/202611012135/modules.json "order", read 01:22Z). GREEN.md holds G1 and G2 only; POINTER-READY not yet written
(HO/10-integration/GREEN.md:11-12; ruling #10/c6566812411). Steps follow ROADMAP.md:971-982 (teams 1–10) and OVERNIGHT.md:41 (teams 11–13 added).

| team | step | module path (in kuiper-belt) | hand-off folder | HANDOFF comment on #10 | admission state (ADMISSIONS.md / GREEN.md / latest) | key |
|---|---|---|---|---|---|---|
| 13 | served-domain check | Ventusltd/gridatlas branch `served-check-kuiper-editions` ce1246e, `tools/release/check-served.mjs` (+30 lines) | neural-link FIXES/NL-010/handoff-13-served.md, served-check.md | not posted on #10 | not an edition module; gridatlas PR #83 OPEN, not merged | handoff-13-served.md:5-10; `gh api repos/Ventusltd/gridatlas/pulls/83` 01:23Z |
| 12 | See Through hash reader | `see-through/202611020012/` (copy of 202610050609 with team 5's reader patch) + pointer `see-through/index.html` | HO/12-see-through-reader/ (PLAN, EVIDENCE, LICENCE, test.cjs, img; no HANDOFF.md) | not posted | not in the admission order; K1 FAIL in its EVIDENCE.md found 00:58Z and cleared on the branch (OVERNIGHT.md:46) | HO/12-see-through-reader/PLAN.md:3-5; #10/c6566545614 |
| 11 | homepage card (R3) | Ventusltd/globalgrid2050-homepage `data/homepage.json` entity `kuiper-editions` (owner bundle 5a4abe41), pinned in globalgrid2050 `catalogue/homepage-owner.json` | neural-link FIXES/NL-010/handoff-11-homepage.md, team-11/ | https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6566248502 | not an edition module; DEPLOYED (globalgrid2050 main 18aa446e, run 41368222618 success) | served-check.md:12-13,36 |
| 10 | 10 integration and proof | `index.html`, `keys.json`, `modules.json`, `README.md`, `NOTICE.md`, `proof/` | HO/10-integration/ (ADMISSIONS, GREEN, CONTROLLER, WATCHER-B, JOURNEY, TEST, BASE, android-journey.cjs) | none (integrator; REVIEW refusing shell rev 1: https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6565858587) | OPUS-10 lead ended 00:36Z; WATCHER-B then OPUS-CONTROLLER (from 00:47Z) write the rows; page `418ae14c` | HO/10-integration/ADMISSIONS.md:27; CONTROLLER.md:5 |
| 9 | 9 law and register | `tools/edition_check.py` (E1–E9), `editions/LAW.md`, `editions/202611012135/LICENCES.md`, `.github/workflows/check.yml` | HO/09-law/ | not posted | not admitted (not a page module); team 9 tester: HAND-OFF REFUSED 01:04Z (ci_check K1 FAIL, E9 drift) | HO/09-law/TEST.md:9; HO/09-law/MODULE.sha256; #10/c6566567480 |
| 8 | 8 the drift | `editions/202611012135/modules/202611012325-drift.js`, `tools/drift.py`, `data/drift.json` | HO/08-drift/ | https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6565879640 (revision https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6566504289) | handed off, not yet admitted; TEST.md 49/49; E9 FAIL (drift.json not reproducible, `--heads` replay) asked of OPUS-8; second in order after the pointer | HO/08-drift/TEST.md:62; CONTROLLER.md:7; #10/c6566812411 |
| 7 | 7 the OS, baby step one (apps) | `editions/202611012135/modules/202611012309-apps.js`, `data/apps.json`, `data/elements.json`, `data/graphs/*.json` | HO/07-apps/ | not posted (HANDOFF.md still has placeholders `UTC_STAMP`, `TEST_STATUS`) | not admitted; TEST.md PASS for team-7 gates, E' NOT EVALUATED; fourth in order after the pointer | HO/07-apps/HANDOFF.md:1,7; HO/07-apps/TEST.md:5 |
| 6 | 6 the File menu | `editions/202611012135/modules/202611012231-file.js` | HO/06-file/ | not posted (evidence officer: HOLD) | not admitted; loader refused `file` (`missing hook layers`) in team 5's run; third in order after the pointer | HO/06-file/EVIDENCE.md:226; HO/05-see-through/HANDOFF.md:7 |
| 5 | 5 See Through, the star player | `editions/202611012135/modules/202611012141-see-through.js`, `data/see-through.json` | HO/05-see-through/ | https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6566607555 | handed off PASS (run8 Pixel 7, run9 Galaxy S24), not yet admitted; first in order after the pointer | HO/05-see-through/HANDOFF.md:7; CONTROLLER.md:8 |
| 4 | 4 the cartridge law (hook table + loader) | `index.html.patch` rev 4 (d49be8ce); `editions/202611012135/modules/202611012145-loader.js` (reference, rev 4 25a16f1d); `modules/202611012145-hello.js` | HO/04-loader/ | not posted (HANDOFF.md placeholders `__TIME__`, `__STATUS__`); hook-table FINDING https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6564299733 | ADMITTED row 1, 23:19Z; GREEN G1 (Pixel 7 14/16, Galaxy S24 14/16, base reds only); main e92ad5d carries the rev 5 reference bytes (known defect, never fetched by the page) | HO/10-integration/ADMISSIONS.md:23; GREEN.md:11; OVERNIGHT.md:48 |
| 3 | 3 the layer registry | `editions/202611012135/modules/202611012141-layers.js`, `data/layers.json`, `data/editions.json`, `tools/build_layers.py`, `index.html.patch` | HO/03-layers/ | https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6565667126 | not admitted; pre-integration FAIL (run 9 refused, edSel page error); no longer blocks the pointer; fifth in order after it | HO/03-layers/TEST.md:3; #10/c6566289513; #10/c6566812411 |
| 2 | 2 the card law | `editions/202611012135/modules/202611012143-line-card.js` (e2baeaaa) | HO/02-card/ | https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6565550370 | ADMITTED row 3, 23:35Z; GREEN G2 (hello + line-card, Pixel 7 14/16, Galaxy S24 14/16, 0 console errors) | HO/10-integration/ADMISSIONS.md:25; GREEN.md:12 |
| 1 | 1 the shell | `editions/202611012135/modules/202611012143-kuiper-shell.js` (rev 2, 1edf2e1a) | HO/01-shell/ | rev 1 https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6565195261; rev 2 https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6566485658 | rev 1 REFUSED 00:03Z (row 2); rev 2 ADMITTED 00:56–00:59Z (row 4); Pixel 7 journey 15/16 at 01:20Z (`load` and `see-through` turned green; `whole-wafer` screenshot timeout), Galaxy S24 started 01:21Z; no GREEN row yet | HO/10-integration/ADMISSIONS.md:24,28; CONTROLLER.md:10; #10/c6566567995 |

Other folders in HO/: `00-stub/` (team 10's loader stub and stub server, STUB.md); controller records `CONTROLLER.md`, `WATCHER-B.md` in 10-integration.

## 4. What is live

| what | commit | run | state | key |
|---|---|---|---|---|
| kuiper-belt main: Edition 5 preview folder (base + loader/hook table + hello + line-card; shell withdrawn at that cut; pointer on Edition 4) | kb@e92ad5dde7cc (2026-11-02T00:05:55Z) | Pages "pages build and deployment" 41365403840 success (00:07:42Z); "checking engineer" 41365404779 success | LIVE as preview at https://ventusltd.github.io/kuiper-belt/editions/202611012135/ (page sha256 418ae14c); editions pointer still opens 202611012027 (Edition 4) | `gh api repos/Ventusltd/kuiper-belt/commits/main` 01:23Z; served-check.md:53-54; OVERNIGHT.md:41 |
| globalgrid2050 homepage card (R3): globalgrid2050-homepage PR #6 merged 5a4abe41; re-pinned in globalgrid2050 PR #52 | globalgrid2050 main 18aa446e9788 (00:38:17Z); homepage 5a4abe41b7a9 (00:36:18Z) | Deploy GlobalGrid2050 Pages 41368222618 success (00:45:53Z); homepage deploy 41368038877 success; served-homepage check 41369293571 PASS (homepage.json 3460dc92 served) | LIVE: the Kuiper nest on www.globalgrid2050.com carries "Kuiper editions" linking /kuiper-editions/ | served-check.md:12-13,36; OVERNIGHT.md:45; `gh api .../globalgrid2050/pulls/52` |
| globalgrid2050 deploy allow-list (kuiper-editions/**) | globalgrid2050 PR #51 merged 0b3369d066c3 (23:58:47Z) | (no deploy of its own; next deploys include the door folder) | LIVE in main | OVERNIGHT.md:39 |
| globalgrid2050 door (R0): /kuiper-editions/ forwards to the editions pointer | globalgrid2050 PR #50 merged 3248bf7f1c3d (23:38:59Z) | Deploy GlobalGrid2050 Pages 41364141297 success (dispatched by hand, finished 23:58:37Z) | LIVE: door sha256 2f046fd8 (1286 bytes) → ventusltd.github.io/kuiper-belt/editions/ → Edition 4 | OVERNIGHT.md:39; served-check.md:4 |

Not live: Edition 5 as the pointer (R2 waits for POINTER-READY, #10/c6566812411); served bytes of /kuiper-editions/ and of the
github.io editions URLs were not fetched by any check (served-check.md "Not proved"); gridatlas PR #83 adds that check and is open.
The edition branch is ahead of main by the shell rev 2 admission and the other teams' files (kb@e927676 vs kb@e92ad5d).
