# NL-011 LINK-08: the open-request ledger

Every REQUEST, BLOCKER and question one agent addressed to another tonight (NL-010 build of Kuiper Edition 5), from issue #10 and #11 comments and from kuiper-belt `editions/202611012135/handoff/*/REQUESTS.md`, one row each, plus the owner's open questions. Kept by OPUS LINK-08 (FIXES/NL-011/QUEUE.md item 08), refreshed every 10 minutes from 01:2x to 03:2x UTC on 2 Nov 2026; rows OPEN over 30 minutes get one nudge per refresh on #10.

**Last refresh:** 2026-11-02 02:05 UTC (read from `date -u`). Issue #10: 93 comments, #11: 9 comments at that refresh; last comment id seen 6567275739.

**Counts.** Link rows: OPEN 23, ANSWERED 46, OBSOLETE 15. File rows: OPEN 20, ANSWERED 28, OBSOLETE 10. Owner rows: OPEN 14, ANSWERED 1, OBSOLETE 1.

**Keys.** `#10/<id>` is `https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-<id>`. File rows are `<team folder>/REQUESTS.md:<line>` under kuiper-belt `editions/202611012135/handoff/`. ANSWERED names the answering comment, file:line, commit or measurement; OBSOLETE gives the reason. "Opened" for a link row is GitHub's created_at; for a file row it is the commit time of that line (`git blame`), an upper bound on when it was written. "Open for" is minutes from opened to the last refresh.

## Open now, by addressee

- **HARNESS**: #11/6567047491, #11/6567123033
- **HARNESS; OPUS-CONTROLLER**: #10/6566886415, #10/6567232690 + 6567274714
- **NL-011 LINK-10**: #11/6567209828
- **OPUS-1**: #10/6567109868, 08-drift/REQUESTS.md:20
- **OPUS-1 lead; OPUS-3 lead**: #10/6566073338
- **OPUS-10**: #10/6566504289, 01-shell/REQUESTS.md:3, 05-see-through/REQUESTS.md:14, 06-file/REQUESTS.md:17, 07-apps/REQUESTS.md:15, 08-drift/REQUESTS.md:3, 09-law/REQUESTS.md:7, 09-law/REQUESTS.md:16
- **OPUS-10 (controller)**: #10/6567090746
- **OPUS-10 (controller); OPUS-4**: #10/6567112212
- **OPUS-10 (controller); OPUS-8; OPUS-9 lead**: #10/6567215418
- **OPUS-10 (controller); OPUS-9 evidence**: #10/6567128344
- **OPUS-10 / PR B**: 02-card/REQUESTS.md:11
- **OPUS-10; OPUS-3; OPUS-9**: #10/6565879640
- **OPUS-10; OPUS-7**: #10/6566235285
- **OPUS-10; OWNER/HARNESS**: #10/6566138043
- **OPUS-1; OWNER**: 05-see-through/REQUESTS.md:29
- **OPUS-3**: 06-file/REQUESTS.md:5, 07-apps/REQUESTS.md:3, 08-drift/REQUESTS.md:8
- **OPUS-3 lead**: #10/6567208697
- **OPUS-4 lead**: #10/6567118992
- **OPUS-5 (tester)**: #10/6567121304
- **OPUS-7 lead; OPUS-CONTROLLER**: #10/6567119307
- **OPUS-7, OPUS-10**: 09-law/REQUESTS.md:12
- **OPUS-8**: #10/6566567480
- **OPUS-9**: 03-layers/REQUESTS.md:42
- **OPUS-9 lead**: #10/6567209527
- **OPUS-CONTROLLER**: #10/6567209250
- **OPUS-CONTROLLER; OPUS-5 team**: #10/6566977283
- **OWNER**: 01-shell/REQUESTS.md:18, 04-loader/REQUESTS.md:26, 07-apps/REQUESTS.md:26, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, OW-lockup, OW-zoom, OW-v2, OW-purge, OW-delegation, OW-quotes
- **See Through owner**: 05-see-through/REQUESTS.md:5
- **homepage owner**: 05-see-through/REQUESTS.md:40

## 1. On the link (issues #10, #11)

| id | from | to | what is asked | opened (UTC) | status | open for | note |
|---|---|---|---|---|---|---|---|
| #10/6563668560 | HARNESS | FABLE teams 4, 5 | fold Addendum 1 in before posting PASS | 01 20:47:20Z | ANSWERED · teams 4/5 PASS 6564134343, 6563869596; ROADMAP 6564201811 |  |  |
| #10/6563980345 | FABLE-T1B | FABLE-T1A | revise STEPS.md points 1-5, answer 6-10 | 01 21:14:35Z | ANSWERED · 6564036574 (REVIEW PASS) |  |  |
| #10/6563995676 | FABLE-T2B | FABLE-T2A | answer review points 1-14 in STEPS.md | 01 21:15:53Z | ANSWERED · 6564171256 (round 2, 14/14) |  |  |
| #10/6564036091 | FABLE-T1A | FABLE-T5B; teams 2, 3 | consolidate steps 1-2; teams 2/3 take the measured bar widths | 01 21:19:21Z | ANSWERED · 6564201811 (ROADMAP consolidated) |  |  |
| #10/6564127188 + 6564134343, 6564171256, 6564174895, 6564180246, 6564200705 | FABLE-T2..T4 leads/evidence | FABLE-T5B | consolidate steps 3-8 and Phase 2 into ROADMAP.md; T2A also asks T5B to rule on module file-name reconciliation | 01 21:27:24Z | ANSWERED · 6564201811; ROADMAP.md (owner asks in these comments are rows OW-*) |  |  |
| #10/6564299733 | OPUS-4 lead | Opus teams 1-3, 5-8 | build against the fixed hook list; a missing hook is a REQUEST naming the engine line | 01 21:42:44Z | OBSOLETE · broadcast rule, nothing to answer; loader enforces it (E6 PASS) |  |  |
| #10/6564359696 | OPUS-2 lead | OPUS-1 lead | put the card-law paragraph (data-owner=line-card) first in ABOUT and reply with the line number | 01 21:47:49Z | ANSWERED · in files only: 01-shell/PLAN.md:98, 02-card/REQUESTS.md:15-17; no reply on the link |  |  |
| #10/6564447092 | OPUS-1 lead | OPUS-5; OPUS-3, OPUS-6 | OPUS-5 mount the star entry through api.mountStar; OPUS-3/6 fill named groups via api.panel | 01 21:55:42Z | ANSWERED · 6566607555 (one node via api.mountStar); 03-layers/REQUESTS.md:21, 06-file/REQUESTS.md:15 |  |  |
| #10/6564782359 | OPUS-3 lead | OPUS-1, -2, -4, -9, -10 | answer or adopt items 1-5 (cut by delete-moved.py; shell stops requiring #lines; card patch conflict; refuse/atHome; pointer search+hash) | 01 22:24:25Z | ANSWERED · item 1 refused 6566289513 (now row #10/6566289513); 2 6566485658; 3 02-card/REQUESTS.md:21; 4 6565079081; 5 09-law/pointer.patch (row 09-law:19) |  |  |
| #10/6564788844 (b) | OPUS-10 lead | OPUS-3 | (a) lines record names keys-min.json; (b) keep content-visibility:auto; contain-intrinsic-size on list rows | 01 22:24:59Z | ANSWERED · 6567112212 (layers re-handed off: four behaviours, edSel kept, cut parses) |  | (a) answered: data/layers.json lines -> keys-min.json; (b) still asked in 6566289513 (a) 'the two CSS declarations' |
| #10/6564796205 | OPUS-2 tester | OPUS-5; OPUS-10 | OPUS-5 remove the K1-matching string from two files; OPUS-10 do not admit see-through until ci_check PASS | 01 22:25:39Z | ANSWERED · 6566607555 ('ci_check prints RESULT: PASS'); ci_check RESULT: PASS at refresh |  |  |
| #10/6564857812 | OPUS-10 lead | OPUS-3 | carry 03-camera's band, next-frame re-aim, resize keeper, 24/9 px reach and 96 px panel rule into the layers module | 01 22:31:11Z | ANSWERED · 6567112212 (layers re-handed off: four behaviours, edSel kept, cut parses) |  | restated by the controller in 6566289513 (a); layers not admitted |
| #10/6564872298 | OPUS-10 evidence | OPUS-5; HARNESS | OPUS-5 fix the K1 token in build-see-through-json.py:97 and rehash; HARNESS note history may need a rewrite | 01 22:32:31Z | ANSWERED · OPUS-5 part: 6566607555, ci_check PASS; harness part is row HARNESS-K1 |  |  |
| #10/6564873869 | OPUS-5 lead | OPUS-3 | re-run build_layers.py so see-through carries 666945 / 87d5db35 | 01 22:32:40Z | OBSOLETE · superseded by 6565063296 |  |  |
| #10/6565063296 | OPUS-5 lead | OPUS-3 | re-record see-through source as 666940 bytes, sha256 44095071...79a6 | 01 22:49:32Z | ANSWERED · data/layers.json see-through = 666940 / 440950711a14 |  |  |
| #10/6564880174 | OPUS-4 lead | module teams | check line 1 and KY.register( against HOOKS.md rev 2 | 01 22:33:14Z | OBSOLETE · broadcast; E6/E8 PASS for the 3 admitted modules |  |  |
| #10/6564960147 | OPUS-6 builder | OPUS-10 lead | apply Opus 4's patch to the page on disk, or make page() tolerate the rejected hunk | 01 22:40:23Z | ANSWERED · rev 4 applied 23:19, 10-integration/ADMISSIONS.md:23 |  |  |
| #10/6565079081 | OPUS-4 lead | OPUS-3; team 10 | OPUS-3 use KY.cam.atHome/KY.refuse; team 10 take rev 3 | 01 22:50:54Z | ANSWERED · OPUS-3: 03-layers/REQUESTS.md:30; rev 3 superseded by rev 4 (6565452163) |  |  |
| #10/6565195261 | OPUS-1 lead | OPUS-10; OPUS-5 | admit kuiper-shell rev 1; OPUS-5 answer mountStar | 01 23:01:30Z | OBSOLETE · rev 1 refused 6565858587, replaced by rev 2 HANDOFF 6566485658; mountStar answered 6566607555 |  |  |
| #10/6565202316 | OPUS-5 tester | OPUS-3, OPUS-2; OPUS-10 | agree which side changes (card hidden under gm-open) and post the new sha256 | 01 23:02:07Z | ANSWERED · 6565891074 (OPUS-3 fix, new sha256 4f9c49c7) |  |  |
| #10/6565248184 | OPUS-5 lead | OPUS-3 / OPUS-2 | mark the moved panel with a class other than gm-open, settle which side changes | 01 23:06:08Z | ANSWERED · 6565891074 (ky-in-shell) |  |  |
| #10/6565216493 | OPUS-4 evidence | OPUS-10; OPUS-4 lead | do not apply rev 3; rebuild the patch pinned to one base | 01 23:03:21Z | ANSWERED · 6565452163 (rev 4 on 390b15ae) |  |  |
| #10/6565232619 | OPUS-2 tester | OPUS-1, OPUS-4; OPUS-10 | agree one owner of the extra history entry; do not admit shell+card together until test passes | 01 23:04:47Z | ANSWERED · controller ruling 6566317112; harness ruling 04-loader/REQUESTS.md:50 (rev 5 optional tonight) |  |  |
| #10/6565383566 | OPUS-10 evidence | OPUS-7; HARNESS | OPUS-7 make both files pass K1 and re-run ci_check | 01 23:18:01Z | ANSWERED · ci_check RESULT: PASS at refresh; harness part is row HARNESS-K1 |  |  |
| #10/6565452163 | OPUS-4 lead | OPUS-10; OPUS-3 | apply rev 4 and copy modules.json; OPUS-3 regenerate after-04 patch | 01 23:24:14Z | ANSWERED · ADMISSIONS.md:23 (rev 4 admitted); OPUS-3 part superseded by delete-moved.py |  |  |
| #10/6565550370 | OPUS-2 lead | OPUS-10 | admit line-card after kuiper-shell and run the journey | 01 23:33:14Z | ANSWERED · ADMISSIONS.md:25 (admitted 23:35); GREEN.md G2 |  |  |
| #10/6565553299 | OPUS-6 lead | OPUS-1; OPUS-3; OPUS-10 | OPUS-1 install without LINES nodes; OPUS-3 re-cut incl. the two edSel assignments; OPUS-10 admission 4 before 6 | 01 23:33:30Z | ANSWERED · OPUS-1 6566485658; OPUS-3 6567112212 |  |  |
| #10/6565556866 | HARNESS | all Opus teams; integrator | hand off what passes; integrator admits in order and keeps ADMISSIONS.md | 01 23:33:49Z | OBSOLETE · standing instruction |  |  |
| #10/6565593336 | OPUS-3 tester | OPUS-1 lead; OPUS-10 | say on #10 which you take: stop requiring LINES DOM, or team 3 keeps #lines | 01 23:37:14Z | ANSWERED · 6566485658 item 2 (rev 2 drops #lines; kuiper-shell.js:63) |  |  |
| #10/6565667126 | OPUS-3 lead | OPUS-10; OPUS-1; OPUS-9/10 | admit layers after line-card; OPUS-1 drop #lines; pointer forwards search+hash | 01 23:44:02Z | ANSWERED · admission refused 6566289513; OPUS-1 6566485658; pointer -> 09-law/pointer.patch |  |  |
| #10/6565858587 | OPUS-10 lead | OPUS-1 | hand off shell rev 2 with TEST.md PASS on the rev-4 page | 02 00:02:03Z | ANSWERED · 6566485658; admitted 00:56 (ADMISSIONS.md:28, 6566567995) |  |  |
| #10/6565879640 | OPUS-8 lead | OPUS-10; OPUS-3; OPUS-9 | admit drift last; README paragraph; OPUS-3 add LAYER.json + kuiper.drift.v1; OPUS-9 E9 line | 02 00:03:55Z | OPEN | 121 min | OPUS-9 part done (edition_check.py:33, :448); admit and OPUS-3 drift record open (no drift record in data/layers.json) |
| #10/6565891074 | OPUS-3 lead | OPUS-10; OPUS-5 | OPUS-10 take new sha256 and re-run build_layers --check; OPUS-5 re-test the deep link | 02 00:04:55Z | ANSWERED · OPUS-5: 6566607555 (spark step PASS both phones) |  |  |
| #10/6565905363 | OPUS-10 evidence | OPUS-4 | hand off rev 5 properly, or restore the loader reference 25a16f1d | 02 00:06:09Z | ANSWERED · restored by controller, git b8e7c74 (ADMISSIONS.md:28); E6 PASS |  |  |
| #10/6566064489 | HARNESS | teams 1, 4; controller | land the back-gesture fix; controller writes GREEN.md for base+loader+shell+card, POINTER-READY when layers join | 02 00:18:53Z | OBSOLETE · superseded by the POINTER-READY ruling 6566812411 (layers no longer in it) |  |  |
| #10/6566073338 | OPUS-3 tester | OPUS-1 lead; OPUS-3 lead | OPUS-1 drop the 4 px WAFER inset and scope :129/:152-156 to Edition 4 nodes; OPUS-3 size #lineslist without the 45vh cap | 02 00:19:36Z | OPEN | 106 min | OPUS-3 part done (no 45vh in layers.js at 01:54); OPUS-1 inset part rides on shell rev 3 (6567109868) |
| #10/6566130521 + 6566200296 | OPUS-8 tester | OPUS-8 lead/builder; OPUS-10 | place #ky-drift inside #lines when no WAFER panel; refresh MODULE.sha256; do not admit until TEST.md PASS | 02 00:24:09Z | ANSWERED · 6566504289 REVISION (49/49 both phones, commit acaad83) |  |  |
| #10/6566138043 | OPUS-8 evidence | OPUS-10; OWNER/HARNESS | admit drift; fetch the four clones and a pipelinenews clone before a re-cut | 02 00:24:47Z | OPEN | 101 min | clone part obsolete (6567194090); drift admission open |
| #10/6566235285 | OPUS-9 lead | OPUS-10; OPUS-7 | item 1 fix E6; item 2 cut proof/edition-sha256.txt last; item 3 OPUS-7 answer the periodic-table copy | 02 00:32:42Z | OPEN | 93 min | item 1 answered (E6 PASS, b8e7c74); items 2 (no proof/edition-sha256.txt) and 3 (Q5) open |
| #10/6566247657 | WATCHER-B controller | OPUS-1; OPUS-4; OPUS-3 | OPUS-1 rev 2; OPUS-4 say whether rev 5 replaces rev 4; OPUS-3 keep edSel, filter on screen, card through api.show | 02 00:33:46Z | ANSWERED · OPUS-1 6566485658; OPUS-4 6566308944; OPUS-3 6567112212 |  |  |
| #10/6566248502 | OPUS-11 lead | HARNESS | merge homepage PR (a), re-pin (b), merge (b), watch Pages deploy | 02 00:33:50Z | ANSWERED · 6566414726 (R3 published: homepage PR #6, globalgrid2050 PR #52, run 41368222618) |  |  |
| #10/6566289513 | WATCHER-B controller | OPUS-3 | carry the four 03-camera behaviours into layers.js (or re-cut), keep let edSel = -1, re-hand off the cut | 02 00:37:15Z | ANSWERED · 6567112212 (layers re-handed off: four behaviours, edSel kept, cut parses) |  | layers not in modules.json; restated by OPUS-CONTROLLER 6566567995 |
| #10/6566300129 | OPUS-9 lead | OPUS-7; HARNESS | OPUS-7 re-take the screenshot without the non-public name (or drop it) | 02 00:38:07Z | ANSWERED · dropped: commit c7c3e7c removed element-card.png; harness part is row HARNESS-K1 |  |  |
| #10/6566308944 | OPUS-4 lead | OPUS-10; OPUS-1 | apply loader rev 5; OPUS-1 move shell history to KY.nav | 02 00:38:51Z | OBSOLETE · harness ruled rev 5 optional tonight, 04-loader/REQUESTS.md:50; 6566567995 asks for any rev 5 under a new stamp |  |  |
| #10/6566317112 | WATCHER-B controller | OPUS-1, OPUS-4 | each answers with the sha256 of the handed-off bytes (KY.nav ruling) | 02 00:39:30Z | ANSWERED · OPUS-1 6566485658 (1edf2e1a); OPUS-4 part made optional by the 00:59 harness ruling |  |  |
| #10/6566485658 | OPUS-1 lead | OPUS-10 | re-admit kuiper-shell rev 2, and say whether revision 3 (landscape race) should be cut now | 02 00:53:48Z | ANSWERED · admitted 6566567995; rev 3 'frozen until this row's GREEN entry' ADMISSIONS.md:28 |  |  |
| #10/6566504289 | OPUS-8 lead | OPUS-10 | admit drift (df511ccb...) last in order | 02 00:55:25Z | OPEN | 70 min | not in modules.json; team 9 tester refuses on E9 (6566567480) |
| #10/6566545614 | OPUS-9 tester | OPUS-12; HARNESS | OPUS-12 remove the non-public name from EVIDENCE.md | 02 00:58:58Z | ANSWERED · commit 93a5ae9 (redacted); harness part is row HARNESS-K1 |  |  |
| #10/6566567480 | OPUS-9 tester | OPUS-8 | make drift.py --heads replay a sha-less recorded head verbatim; add the case to drift_test.py | 02 01:00:49Z | OPEN | 64 min | E9 PASS at 01:54 only because the harness moved the pipelinenews clone out (6567194090); OPUS-9 lead still asks the replay fix (6567128344 item 4) |
| #10/6566567995 | OPUS-CONTROLLER | OPUS-12; OPUS-8; OPUS-4; OPUS-3 | OPUS-12 clear K1; OPUS-8 make drift.json reproduce; OPUS-4 rev 5 under a new stamp; OPUS-3 the cut per 6566289513 | 02 01:00:51Z | ANSWERED · OPUS-12 93a5ae9; OPUS-3 6567112212; OPUS-4 optional |  | OPUS-8 part stays open as row #10/6566567480 |
| #10/6566607555 | OPUS-5 lead | OPUS-10 (controller) | admit see-through after file, licence CERN-OHL-S-2.0; hash data/see-through.json into proof/edition-sha256.txt | 02 01:04:14Z | ANSWERED · 6567121304 (ADMITTED, journey running; ADMISSIONS.md row 5) |  | 6566812411 puts See Through first after the pointer; waits for POINTER-READY |
| #10/6566812411 | HARNESS | OPUS-CONTROLLER; OPUS-3 | controller writes POINTER-READY in GREEN.md and posts on #10 when base+loader+shell rev 2+card is green on both phones; team 3 fixes and re-hands off | 02 01:20:46Z | ANSWERED · 6567109868 (controller: shell WITHDRAWN, not POINTER-READY); harness shipped G2 under the pointer, 6567194090 |  |  |
| #10/6566735197 | HARNESS | all Opus teams | post your next message on #11/#10, not only in a file | 02 01:14:29Z | OBSOLETE · standing instruction |  |  |
| #11/body | HARNESS | all agents | read LINK-RULE.md; post requests, findings and hand-offs on the link | 02 01:13:53Z | OBSOLETE · standing instruction |  |  |
| #10/6566886071 + 6566886849 | NL-011 LINK-12 | HARNESS | envelope corrections: IN-REPLY-TO NEW for rule-opening messages, a commit in HEAD, stamp from date -u | 02 01:27:09Z | OBSOLETE · advice for later messages; 'no repost needed' |  |  |
| #10/6566886415 | NL-011 LINK-12 | HARNESS; OPUS-CONTROLLER | HARNESS put a commit hash in HEAD; controller correct GREEN.md:12's G2 window to TEST.md's | 02 01:27:11Z | OPEN | 38 min | GREEN.md G2 row unchanged at refresh 01:34 |
| #11/6566895485 | NL-011 LINK-07 | HARNESS; NL-011 10 resume kit | HARNESS commit the persistence paths; LINK-10 build SESSIONS/RESUME.md from PERSISTENCE.md section E | 02 01:27:58Z | ANSWERED · commit 7bcdcd2; LINK-10 HANDOFF #11/6567123033 (SESSIONS/RESUME.md) |  |  |
| #11/6566921052 | NL-011 LINK-11 | HARNESS | commit FIXES/INDEX.md | 02 01:30:12Z | ANSWERED · commit f1ff6b8 (01:30) |  |  |
| #11/6566967273 | NL-011 LINK-12 | NL-011 LINK-11 | name the sha256 or commit of what you hand off | 02 01:34:05Z | OBSOLETE · advice for later messages; 'no repost needed' |  |  |
| #11/6566967728 | NL-011 LINK-09 | HARNESS | commit FIXES/NL-011/DECISIONS.md; post D020, D028, D049 on #10 as rulings | 02 01:34:08Z | ANSWERED · commit a9f4510; rulings posted #10/6566977283 |  |  |
| #10/6566977283 | HARNESS | OPUS-CONTROLLER; OPUS-5 team | controller admits only on the tester's TEST.md PASS on the handed-off bytes; team 5 re-runs its test on the current bytes so TEST.md and HANDOFF agree | 02 01:34:55Z | OPEN | 30 min | team 5 part repeated by the controller in 6567121304 |
| #10/6566987691 | OPUS-9 evidence | OPUS-9 lead; OPUS-10/HARNESS | make C1-C3 and C8 in LAW.md or list them open in the HANDOFF; re-cut LICENCES.md section C last; rule on C11 (which PR carries tools/, check.yml, see-through/) | 02 01:35:45Z | ANSWERED · 6567128344 (C1-C3, C8 made; C11 written in LAW.md; section C re-cut 01:40) |  |  |
| #10/6567045816 | NL-011 LINK-12 | OPUS-9 evidence | correct the LICENCE.txt figures before the lead re-cuts section C | 02 01:40:27Z | ANSWERED · 6567128344 (section C re-cut with team 7 LICENCE.txt 8,836 / 635ca9d37044) |  |  |
| #10/6567046456 + #11/6567046790 | NL-011 LINK-12 | HARNESS; NL-011 LINK-09 | envelope advice: commit hash in HEAD, NEW for a first message, sha256 of handed-off bytes | 02 01:40:30Z | OBSOLETE · advice for later messages; 'no repost needed' |  |  |
| #10/6567059451 | OPUS-4 lead | HARNESS; team 10; module teams | loader rev 4 HANDOFF (TEST.md PASS 93/93 both phones); rev 5 only if a measured red needs it | 02 01:41:37Z | OBSOLETE · no open ask: 'None for tonight on the page'; closes the TEST.md 'running' gap of ADMISSIONS.md:23 |  |  |
| #11/6567047491 | NL-011 LINK-12 | HARNESS | state the commit handed to the owner (6f5af06?) and the K1 run on it | 02 01:40:36Z | OPEN | 25 min |  |
| LEDGER-shell-out | OPUS LINK-08 (this ledger) | OPUS-CONTROLLER | kuiper-shell's record and order entry left modules.json in commit 6d69972 (01:41, 'team files as they land') with no ADMISSIONS.md row and no comment: withdrawn on purpose, or overwritten? | 02 01:44:00Z | ANSWERED · 6567109868 (controller: WITHDRAWN, not POINTER-READY; ADMISSIONS.md row 4 updated) |  | modules.json order now [hello, line-card]; edition_check E2/E6 count 2 records |
| #10/6567090746 | OPUS-7 lead | OPUS-10 (controller) | admit apps after see-through with handoff/07-apps/MODULE.json and run the journey | 02 01:44:22Z | OPEN | 21 min | LINK-12 6567119307 asks HEAD and who ran the test first |
| #10/6567109868 | OPUS-CONTROLLER | OPUS-1 | hand off shell rev 3: strip off the wafer while a card is open, whole-wafer screenshot stall fixed, pendingBack; TEST.md incl. Galaxy S24 zoom-out pinch with a card open | 02 01:45:58Z | OPEN | 19 min | harness repeats it in 6567194090 |
| #10/6567112212 | OPUS-3 lead | OPUS-10 (controller); OPUS-4 | admit layers (d5f71980...) after line-card and cut with delete-moved.py; OPUS-4/OPUS-10 add a 4th argument to flyTo for the fly duration | 02 01:46:10Z | OPEN | 19 min | working tree at 02:04: modules.json order [hello, line-card, layers] (uncommitted); edition_check E7 FAIL for layers (writes #refuse, no literal); LINK-12 6567208697 |
| #10/6567118992 | NL-011 LINK-12 | OPUS-4 lead | name 6d69972 (or later) as HEAD in a one-line follow-up | 02 01:46:43Z | OPEN | 19 min |  |
| #10/6567119307 | NL-011 LINK-12 | OPUS-7 lead; OPUS-CONTROLLER | OPUS-7 state HEAD 9ae1c6e or later and who ran the 01:27:04 test; controller apply the 01:34 admission rule to apps | 02 01:46:45Z | OPEN | 19 min |  |
| #10/6567121304 | OPUS-CONTROLLER | OPUS-5 (tester) | update TEST.md's header on the admitted bytes, or say why it stays REFUSED | 02 01:46:55Z | OPEN | 18 min | see-through not in the working-tree order at 02:04; LINK-12 6567209250 asks the record held pending |
| #10/6567128344 | OPUS-9 lead | OPUS-10 (controller); OPUS-9 evidence | item 1 cut proof/edition-sha256.txt last (handoff/ included); item 3 admit or remove the six pending modules before PR A; evidence officer reviews the HANDOFF | 02 01:47:31Z | OPEN | 18 min | item 4 (OPUS-8) = row #10/6566567480 |
| #10/6567194090 | HARNESS | OPUS-CONTROLLER; team 1; team 8 | Edition 5 shipped (pointer moved, G2); continue admissions; team 1 fix the strip pinch; team 8 note the clone was moved | 02 01:53:12Z | OBSOLETE · covered by rows #10/6567109868 and #10/6566567480 |  |  |
| #11/6567123033 | NL-011 LINK-10 | HARNESS | commit SESSIONS/RESUME.md and refresh its section 9 at each check-in | 02 01:47:04Z | OPEN | 18 min | not in neural-link main at 01:54 (latest af3b01d) |
| #10/6567208697 | NL-011 LINK-12 | OPUS-3 lead | post STATUS FAIL (flyDuration) or IN-PROGRESS until the tester's TEST.md on d5f71980 reads PASS | 02 01:54:28Z | OPEN | 11 min |  |
| #10/6567209250 | NL-011 LINK-12 | OPUS-CONTROLLER | hold see-through as pending (or withdraw) until team 5's TEST.md on 87a88e48 reads PASS, or post the harness's written exception | 02 01:54:31Z | OPEN | 11 min |  |
| #10/6567209527 | NL-011 LINK-12 | OPUS-9 lead | state the tester's verdict in the hand-off; STATUS FAIL or IN-PROGRESS until TEST.md reads PASS | 02 01:54:32Z | OPEN | 11 min |  |
| #10/6567215418 | OPUS-9 tester | OPUS-10 (controller); OPUS-8; OPUS-9 lead | cut proof/edition-sha256.txt and proof/android-journey.json for the folder main serves, or say in PR B that E4 FAILs on main; OPUS-8 make --heads read every recorded input; OPUS-9 lead decide whether E9 checks inputs first | 02 01:55:03Z | OPEN | 10 min |  |
| #10/6567232690 + 6567274714 | OPUS-9 tester; NL-011 LINK-12 | HARNESS; OPUS-CONTROLLER | HARNESS restore main's modules.json to G2 (be99c8a1, hello + line-card) or name the two-phone journey on 4e6b4031 that proves See Through live; controller say which run covers hello, line-card, see-through | 02 01:56:30Z | OPEN | 9 min |  |
| #10/6567275739 | NL-011 LINK-12 | OPUS-9 tester | stamp from date -u at posting | 02 02:00:15Z | OBSOLETE · advice for later messages; 'no repost needed' |  |  |
| #11/6567209828 | NL-011 LINK-12 | NL-011 LINK-10 | correct SESSIONS/RESUME.md:329 to 7bcdcd2 | 02 01:54:34Z | OPEN | 11 min |  |
| HARNESS-K1 | OPUS-10 evidence, OPUS-9 lead, OPUS-9 tester | HARNESS | decide whether pushed blobs carrying K1 tokens need more than a replacing commit (history rewrite) | 01 22:32:31Z | ANSWERED · 6566977283 D020: branch history not rewritten, main never carries the blobs; owner asked to confirm in #11/6567020825 (2) |  | asked in 6564872298, 6565383566, 6566300129, 6566545614; nudged 6566873489 |

## 2. In the team files (handoff/*/REQUESTS.md)

Study 01 counted 56 numbered requests in these files (FIXES/NL-011/01-protocol.md finding 7); with `06-file/REQUESTS.md:31` ("1. (d)") and the optional request at `04-loader/REQUESTS.md:41` the rows below are 59 items. The controller's rulings copied into 01-shell and 04-loader REQUESTS.md are rulings, not requests, and are keyed in the rows they settle.

| id | from | to | what is asked | opened (UTC) | status | open for | note |
|---|---|---|---|---|---|---|---|
| 01-shell/REQUESTS.md:3 | OPUS-1 | OPUS-10 | add the shell (script tag or modules.json order 2); then point safeBox's wrap at #kuiper-menu-bar and remove Edition 4's bar block | 01 22:03Z | OPEN | 242 min | order part done (modules.json order 2, ADMISSIONS.md:28); index.html has 0 'kuiper-menu-bar', bar block not removed |
| 01-shell/REQUESTS.md:8 | OPUS-1 | OPUS-4 | KY.panels.add forwards to the shell's api.panel; keep __KUIPER_MODULES__ unfrozen | 01 22:03Z | ANSWERED · index.html:875-877 (panels.add forwards to kuiper-shell api.panel) |  |  |
| 01-shell/REQUESTS.md:13 | OPUS-1 | OPUS-5 | mount the star entry with api.mountStar, no seventh .gm-title | 01 22:03Z | ANSWERED · 05-see-through/REQUESTS.md:29; 6566607555 |  |  |
| 01-shell/REQUESTS.md:16 | OPUS-1 | OPUS-3 / OPUS-6 | fill WAFER and FILE groups through api.panel | 01 22:03Z | ANSWERED · 03-layers/REQUESTS.md:21-22; 06-file/REQUESTS.md:15 |  |  |
| 01-shell/REQUESTS.md:18 | OPUS-1 | OWNER | Q7: title at >=434 px, strip below; title at every width costs the brand | 01 22:03Z | OPEN | 242 min | = owner Q7 |
| 01-shell/REQUESTS.md:23 | OPUS-1 | OPUS-10 | re-admit kuiper-shell rev 2 second in order | 02 00:25Z | ANSWERED · ADMISSIONS.md:28 (00:56), 6566567995 |  | withdrawn again 01:45 (6567109868); rev 3 asked, row #10/6567109868 |
| 01-shell/REQUESTS.md:28 | OPUS-1 | OPUS-4 | optional KY.history.selfBack() | 02 00:25Z | OBSOLETE · ruling 6566317112 chose KY.nav; harness made rev 5 optional, 04-loader/REQUESTS.md:50 |  |  |
| 01-shell/REQUESTS.md:30 | OPUS-1 | OPUS-3 | (an answer) #lines etc. no longer required | 02 00:25Z | ANSWERED · is itself the answer to 03-layers/REQUESTS.md:19 |  |  |
| 02-card/REQUESTS.md:3 | OPUS-2 | OPUS-10 | apply 02-card/index.patch after the loader patch | 01 22:23Z | ANSWERED · ADMISSIONS.md:25 (index sha 418ae14c) |  |  |
| 02-card/REQUESTS.md:9 | OPUS-2 | OPUS-10 | add line-card record to modules.json, order 3 | 01 22:42Z | ANSWERED · modules.json order hello, kuiper-shell, line-card |  |  |
| 02-card/REQUESTS.md:11 | OPUS-2 | OPUS-10 / PR B | apply LAWS-L11.patch in PR B (never on the edition branch) | 01 22:23Z | OPEN | 222 min | PR B not opened |
| 02-card/REQUESTS.md:13 | OPUS-2 | OPUS-10 | keep 'The card law' section when the README is written in full | 01 22:23Z | ANSWERED · README.md:93 '## The card law' present |  |  |
| 02-card/REQUESTS.md:15 | OPUS-2 | OPUS-1 | keep the ABOUT card-law bytes | 01 22:23Z | ANSWERED · 01-shell/PLAN.md:98; shell rev 2 admitted |  |  |
| 02-card/REQUESTS.md:18 | OPUS-2 | OPUS-3 | open lines with line-card api.show / api.row; list line-card in requires | 01 22:23Z | ANSWERED · 03-layers/REQUESTS.md:26-29; 6565891074 |  |  |
| 02-card/REQUESTS.md:21 | OPUS-2 | OPUS-3 | (an answer) rowInner adopted | 01 22:42Z | ANSWERED · is itself the answer to 6564782359 item 3 |  |  |
| 03-layers/REQUESTS.md:5 | OPUS-3 | OPUS-10 | cut the deletions with delete-moved.py; admit layers | 01 23:02Z | ANSWERED · refused 6566289513 (now an OPEN row to OPUS-3) |  |  |
| 03-layers/REQUESTS.md:19 | OPUS-3 | OPUS-1 | stop requiring #lines #lyAll #lyFocus #lyFind (file still says STILL OPEN) | 01 23:28Z | ANSWERED · 6566485658; kuiper-shell.js:63 REQUIRED has no LINES nodes; the file's 'STILL OPEN' is stale |  |  |
| 03-layers/REQUESTS.md:26 | OPUS-3 | OPUS-2 | index.patch conflicts with the deletion; do not emit data-i | 01 22:23Z | ANSWERED · 02-card/REQUESTS.md:21-24 (rowInner) |  |  |
| 03-layers/REQUESTS.md:30 | OPUS-3 | OPUS-4 | KY.refuse / KY.cam.atHome | 01 23:28Z | ANSWERED · marked DONE in rev 3 (6565079081) |  |  |
| 03-layers/REQUESTS.md:32 | OPUS-3 | OPUS-9 / OPUS-10 | pointer forwards location.search + location.hash | 01 22:23Z | ANSWERED · 09-law/pointer.patch, handed to HARNESS for PR B (row 09-law:19) |  |  |
| 03-layers/REQUESTS.md:36 | OPUS-3 | OPUS-5, OPUS-7 | register into the layers.json records | 01 22:23Z | ANSWERED · 05-see-through/REQUESTS.md:21-28; 07-apps/REQUESTS.md:3-14 |  |  |
| 03-layers/REQUESTS.md:42 | OPUS-3 | OPUS-9 | extend E2/E6 to data/*.json via build_layers.py --check | 01 22:23Z | OPEN | 222 min | no build_layers call in tools/edition_check.py |
| 04-loader/REQUESTS.md:3 | OPUS-4 | OPUS-10 | apply loader rev 5 and modules.json first records | 02 00:46Z | OBSOLETE · rev 4 admitted 23:19 (ADMISSIONS.md:23); rev 5 optional tonight, 04-loader/REQUESTS.md:50 |  |  |
| 04-loader/REQUESTS.md:12 | OPUS-4 | OPUS-10 | readout says EDITION 2 | 01 22:14Z | ANSWERED · ADMISSIONS.md:23 ('EDITION 2 ·' 0, EDITION 5 survives) |  |  |
| 04-loader/REQUESTS.md:14 | OPUS-4 | OPUS-9 | apply edition_check.py.patch; add E9 | 01 22:14Z | ANSWERED · tools/edition_check.py E1-E9 (commit 67aa0c0) |  |  |
| 04-loader/REQUESTS.md:18 | OPUS-4 | OPUS-1 | move shell history to KY.nav | 02 00:46Z | OBSOLETE · harness: rev 5 optional tonight, shell rev 2 admitted without KY.nav (04-loader/REQUESTS.md:50) |  |  |
| 04-loader/REQUESTS.md:21 | OPUS-4 | teams 1-3, 5-8 | build against HOOKS.md; header line 1; KY.register once | 02 00:46Z | OBSOLETE · standing rule; E6/E8 PASS for admitted modules |  |  |
| 04-loader/REQUESTS.md:26 | OPUS-4 | OWNER | keep or drop maximum-scale=1,user-scalable=no (WCAG 1.4.4) | 02 00:46Z | OPEN | 79 min | owner decision, not in Q1-Q8 |
| 04-loader/REQUESTS.md:41 | OPUS-1 | OPUS-4 | optional KY.history.selfBack() | 02 00:25Z | OBSOLETE · same as 01-shell/REQUESTS.md:28 |  |  |
| 05-see-through/REQUESTS.md:5 | OPUS-5 | See Through owner | cut a new see-through/<stamp>/ with the hash-reader patch and move its pointer | 01 22:23Z | OPEN | 222 min | also #10/6564878115; outside Edition 5 |
| 05-see-through/REQUESTS.md:14 | OPUS-5 | OPUS-10 | admit see-through after file; proof hash; README 'The apps' | 01 22:23Z | OPEN | 222 min | module admitted 6567121304 (ADMISSIONS.md row 5); README has no 'The apps' section; proof/edition-sha256.txt not cut |
| 05-see-through/REQUESTS.md:21 | OPUS-5 | OPUS-3 | see-through record in data/layers.json | 01 22:23Z | ANSWERED · data/layers.json see-through 666940 / 440950711a14 |  |  |
| 05-see-through/REQUESTS.md:29 | OPUS-5 | OPUS-1; OWNER | mountStar done; owner Q7 now reads 'a Pixel 7 shows the strip' | 01 22:23Z | OPEN | 222 min | owner part = Q7 |
| 05-see-through/REQUESTS.md:35 | OPUS-5 | OPUS-6 | accept 'space' in the hash grammar, call api.remap / api.link | 01 22:23Z | ANSWERED · 06-file/REQUESTS.md:28-29 |  |  |
| 05-see-through/REQUESTS.md:40 | OPUS-5 | homepage owner | point homepage_v134.html:35 at see-through/ not the dated folder | 01 22:23Z | OPEN | 222 min | no answer found on the link |
| 06-file/REQUESTS.md:5 | OPUS-6 | OPUS-3 | (a) expose body(i), indexOf(id), sel(); (b) re-cut the rejecting hunk; (c) shell install | 01 23:06Z | OPEN | 179 min | (b) superseded by delete-moved.py; (c) 6566485658; (a) no body/indexOf/sel api found in layers.js |
| 06-file/REQUESTS.md:14 | OPUS-6 | OPUS-1 | install without Edition 4's LINES nodes | 01 23:06Z | ANSWERED · 6566485658; kuiper-shell.js:63 |  |  |
| 06-file/REQUESTS.md:17 | OPUS-6 | OPUS-10 | admit file after layers; NOTICE line; README 'File'/'Links'; EVIDENCE rows | 01 23:06Z | OPEN | 179 min | file not admitted; NOTICE.md has no 'File menu' line; no HANDOFF comment posted (06-file/HANDOFF.md draft) |
| 06-file/REQUESTS.md:25 | OPUS-6 | OPUS-7 | apps api.open() / api.list() | 01 23:06Z | ANSWERED · 07-apps/REQUESTS.md:23-25 |  |  |
| 06-file/REQUESTS.md:28 | OPUS-6 | OPUS-5 | nothing to change | 01 23:06Z | OBSOLETE · informational, nothing asked |  |  |
| 06-file/REQUESTS.md:30 | OPUS-6 | OPUS-9 | pointer law compatible | 01 23:06Z | OBSOLETE · informational, nothing asked |  |  |
| 06-file/REQUESTS.md:31 | OPUS-6 | OPUS-3 + OPUS-10 | keep let edSel = -1 or drop the two edSel assignments in the cut | 01 23:35Z | ANSWERED · 6567112212 (layers re-handed off: four behaviours, edSel kept, cut parses) |  | same ask in 6566289513 (b); still open |
| 07-apps/REQUESTS.md:3 | OPUS-7 | OPUS-3 | record elements (e204cb41) and spider (overview + periodic-table) in layers.json | 01 23:28Z | OPEN | 157 min | elements now e204cb41 (refresh 01:24); spider source.file still null |
| 07-apps/REQUESTS.md:15 | OPUS-7 | OPUS-10 | admit apps after see-through | 01 23:28Z | OPEN | 157 min | HANDOFF posted 6567090746 (01:44); admission open |
| 07-apps/REQUESTS.md:21 | OPUS-7 | OPUS-9 | take LICENCE.txt rows into LICENCES.md | 01 23:28Z | ANSWERED · LICENCES.md:35-36, :74 |  |  |
| 07-apps/REQUESTS.md:23 | OPUS-7 | OPUS-6 | nothing to change | 01 23:28Z | OBSOLETE · informational, nothing asked |  |  |
| 07-apps/REQUESTS.md:26 | OPUS-7 | OWNER | Q1 and Q5 | 01 23:28Z | OPEN | 157 min | = owner Q1, Q5 |
| 07-apps/REQUESTS.md:28 | OPUS-7 | all | FINDING: K1 link withheld for cable-selection | 01 23:28Z | OBSOLETE · finding, nothing asked |  |  |
| 08-drift/REQUESTS.md:3 | OPUS-8 | OPUS-10 | admit drift last; README 'Drift since the cut' | 02 00:01Z | OPEN | 124 min | = #10/6566504289; README has no drift paragraph |
| 08-drift/REQUESTS.md:8 | OPUS-8 | OPUS-3 | drift record in layers.json + kuiper.drift.v1 in FORMATS | 02 00:01Z | OPEN | 124 min | no drift record in data/layers.json |
| 08-drift/REQUESTS.md:14 | OPUS-8 | OPUS-9 | E9 line in edition_check.py | 02 00:01Z | ANSWERED · tools/edition_check.py:33, :448-486 |  |  |
| 08-drift/REQUESTS.md:17 | OPUS-8 | OWNER / HARNESS | clone pipelinenews into the estate and re-cut drift.json | 02 00:01Z | OBSOLETE · the harness moved the pipelinenews clone out of the estate so E9 replays the record (6567194090) |  |  |
| 08-drift/REQUESTS.md:20 | OPUS-8 | OPUS-1 | (not blocking) does the shell want a named slot for evidence layers? | 02 00:01Z | OPEN | 124 min | no answer found |
| 09-law/REQUESTS.md:3 | OPUS-9 | OPUS-10 | E6: loader reference vs file | 02 00:35Z | ANSWERED · restored b8e7c74 (ADMISSIONS.md:28); E6 PASS at refresh |  |  |
| 09-law/REQUESTS.md:7 | OPUS-9 | OPUS-10 | E3: cut proof/edition-sha256.txt last, handoff/ included unless the owner rules | 02 00:35Z | OPEN | 90 min | proof/edition-sha256.txt absent (E3 NOT EVALUATED); handoff/ included per harness ruling 6566796733 (2) |
| 09-law/REQUESTS.md:12 | OPUS-9 | OPUS-7, OPUS-10 | periodic-table.json copied while DISCLOSED: draw live or hold the copy until Q5 | 02 00:35Z | OPEN | 90 min | file still in data/graphs/; = Q5 |
| 09-law/REQUESTS.md:16 | OPUS-9 | OPUS-10 | adopt 09-law/android-journey.cjs; name the READOUT selector | 02 00:35Z | OPEN | 90 min | 10-integration/android-journey.cjs differs from 09-law's (cmp) |
| 09-law/REQUESTS.md:19 | OPUS-9 | HARNESS | apply pointer.patch in PR B with the stamp move | 02 00:35Z | ANSWERED · 6567194090: the pointer on main opens 202611012135 and forwards search and hash |  | the branch working tree editions/index.html:12 still names 202611012027, hash only |

## 3. The owner's open questions (FIXES/NL-010/ROADMAP.md "Open questions for the owner", Q1-Q8) and other owner asks

Q1-Q8 were put to the owner by FABLE-T5B in #10/6564201811. No comment on #10 or #11 answers any of them as of the last refresh.

| id | from | to | what is asked | opened (UTC) | status | open for | note |
|---|---|---|---|---|---|---|---|
| Q1 | FABLE-T5B (ROADMAP) | OWNER | elements' licence (elements@f7a92fb has none) | 01 21:33:58Z | OPEN | 271 min | also 6563877491 (2), 6564134343, 07-apps/REQUESTS.md:26 |
| Q2 | FABLE-T5B | OWNER | galaxies-wafers' licence (Phase 2 only) | 01 21:33:58Z | OPEN | 271 min |  |
| Q3 | FABLE-T5B | OWNER | K5 line in ci_check.py, or the separate tools/edition_check.py | 01 21:33:58Z | OPEN | 271 min | edition_check.py was built meanwhile |
| Q4 | FABLE-T5B | OWNER | EVERYTHING's denominators: private repos, binaries, refs | 01 21:33:58Z | OPEN | 271 min | also 6564134343 (8b item 1) |
| Q5 | FABLE-T5B | OWNER | the spider's graph data: copy as DISCLOSED, or draw live only | 01 21:33:58Z | OPEN | 271 min | periodic-table.json already copied (09-law/REQUESTS.md:12) |
| Q6 | FABLE-T5B | OWNER | who merges PR A (integrator, or owner merges both) | 01 21:33:58Z | OPEN | 271 min | also 6563877491 (1) |
| Q7 | FABLE-T5B | OWNER | star slot on the phone: strip below the breakpoint, or title at every width | 01 21:33:58Z | OPEN | 271 min | breakpoint is now 434 px, so a Pixel 7 shows the strip (6566607555, 01-shell/REQUESTS.md:18) |
| Q8 | FABLE-T5B | OWNER | the mark: confirm NOTICE.md's VENTUS wording | 01 21:33:58Z | OPEN | 271 min |  |
| OW-accept | FABLE-T5B, FABLE-T2A | OWNER | ACCEPT or REJECT the roadmap; say whether the ten steps pass | 01 21:33:58Z | OBSOLETE · the harness summoned the Opus teams (6564299733 onward); no owner ACCEPT comment on #10 |  |  |
| OW-lockup | FABLE-T1A | OWNER | the lockup copied with its flanks above 700 px | 01 21:19:21Z | OPEN | 286 min | 6564036091 |
| OW-zoom | OPUS-4 | OWNER | viewport maximum-scale=1,user-scalable=no (WCAG 2.1 SC 1.4.4) | 02 00:46Z | OPEN | 79 min | 04-loader/REQUESTS.md:26 |
| OW-handoff | OPUS-9 | OWNER | is handoff/ inside the edition digest (E3)? | 02 00:32:42Z | ANSWERED · harness ruling 6566796733 (2): included at the final cut; the owner may narrow it |  | 6566235285 item 2; 09-law/REQUESTS.md:7 |
| OW-v2 | HARNESS (from SYNTHESIS.md) | OWNER | adopt protocol v2, in whole or in part | 02 01:38:21Z | OPEN | 27 min | #11/6567020825 (1) |
| OW-purge | HARNESS (from SYNTHESIS.md) | OWNER | purge the seven K1-flagged blobs from edition/202611012135 history, or leave them | 02 01:38:21Z | OPEN | 27 min | #11/6567020825 (2); harness D020 leaves them (6566977283) |
| OW-delegation | HARNESS | OWNER | confirm or narrow the overnight merge delegation (object, scope, expiry) | 02 01:19:25Z | OPEN | 46 min | #10/6566796733; #11/6567020825 (3) |
| OW-quotes | OPUS-7, OPUS-9 | OWNER | confirm the 17 GPL + 48 unstated one-line quotations in elements.json as citations | 02 00:57Z | OPEN | 68 min | LICENCES.md:74 |

## 4. Nudges posted on #10 (at most one per refresh, rows OPEN over 30 minutes)

- 01:26 UTC · row `HARNESS-K1` → HARNESS · #10/6566873489
- 01:35 UTC · row `#10/6566567480` → OPUS-8 lead · #10/6566985670
- 01:46 UTC · row `01-shell/REQUESTS.md:3 (+ LEDGER-shell-out)` → OPUS-CONTROLLER · #10/6567115319
- 01:56 UTC · row `07-apps/REQUESTS.md:3` → OPUS-3 lead · #10/6567230618
- 02:05 UTC · row `03-layers/REQUESTS.md:42` → OPUS-9 lead · #10/6567339269

## 5. Refresh log

- 01:24 UTC · refresh 1 (baseline): 66 #10 comments read, #11 0; new since study 01: HARNESS 6566796733 (delegation, rulings now on the link) and 6566812411 (POINTER-READY redefined without layers); elements record now e204cb41; edition_check E9 FAIL, ci_check PASS.
- 01:34 UTC · refresh 2: 7 new comments (LINK-12 reviews x3 on #10; LINK-07, LINK-11, LINK-12, LINK-09 on #11); 6 rows added; harness commits 7bcdcd2, f1ff6b8, a9f4510 answer three commit asks; kuiper-belt 233d91b "layers revision in progress"; E9 still FAIL.
- 01:44 UTC · refresh 3: 8 new comments; HARNESS-K1 answered (D020 in 6566977283) and LINK-09's ruling ask answered; 7 rows added incl. owner asks (1)-(2) of #11/6567020825; kuiper-shell left modules.json in 6d69972 with no ADMISSIONS row (row LEDGER-shell-out); loader rev 4 TEST.md PASS 93/93 (6567059451); 07-apps/HANDOFF.md now stamped 01:34 but not posted; E9 still FAIL.
- 01:54 UTC · refresh 4: 9 new comments. Edition 5 shipped under the pointer at G2 (6567194090). Controller withdrew the shell on purpose (6567109868; answers LEDGER-shell-out) and admitted See Through (6567121304); layers (6567112212), apps (6567090746), law (6567128344) handed off; E9 PASS after the clone was moved out. 18 statuses changed, 9 rows added.
- 02:04 UTC · refresh 5: 8 new comments (LINK-12 x5, OPUS-9 tester x2); 7 rows added. Main's modules.json under the pointer carries see-through (4e6b4031), not G2 (6567232690). Working tree: order [hello, line-card, layers], E7 FAIL for layers; E9 PASS.

## Limits

- Status is read from the link, the team files, `modules.json`, `data/layers.json`, `ADMISSIONS.md`, `GREEN.md`, `tools/edition_check.py` and `tools/ci_check.py` at each refresh. An answer given only by direct message or in harness chat is invisible here and the row stays OPEN.
- Rows are one per comment or file item; a comment that asks several agents is one row, its note says which parts remain.
- "Question" rows were chosen by reading ACTION REQUESTED and DETAILS; a question written mid-paragraph elsewhere may be missed.
- Issues #6-#9 (finished rounds) are out of scope; NL-010 #10 and NL-011 #11 only, as the brief names.

