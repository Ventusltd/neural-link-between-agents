# NL-011 study 03: coordination topology and latency

Lens: who talked to whom, through which channel, how fast, who everyone waited on, and which requests were never
answered. Window: 2026-11-01 20:00Z (NL-009/NL-010 launch) to 2026-11-02 01:05Z (last edition-branch commit
`7fb8ccc`). All times come from GitHub `created_at`, git commit times or harness transcript timestamps. Times that
agents wrote themselves are used only where marked "(agent stamp)".

## Verdict

Tonight's coordination ran hub-and-spoke through the harness, not over the link: agents handed back to it (81 task
notifications after 21:36Z) and it pushed messages on by direct message (32 SendMessage calls, 12 of them literal
relays "from OPUS-x via the harness"), and all but one answer faster than 5 minutes followed one of those DMs. The shared
handoff files were the real bus for content (agents' tool calls touched them about 7.6 times as often as issue #10),
while the issue was a broadcast log that was almost never answered by reference: 3 of 27 directed comments drew a reply
by comment id, there were 0 ACKs, and the integrator posted neither of its two admissions there. Everyone waited on one serial
admissions slot (integrator, then WATCHER-B, then OPUS-CONTROLLER; addressed in 35 of 49 Opus-phase comments and 19 of 57
REQUESTS.md items), which admitted 3 modules in 97 minutes while the shell/loader history conflict held the queue for
1 h 51 min and left 18 traced asks open at 01:05.

## Findings

### 1. Message counts per channel

| channel | count (window) | key / command |
|---|---|---|
| Issue comments, all tonight | 75: #10 63, #9 10, #6 2 | `gh api repos/Ventusltd/neural-link-between-agents/issues/<n>/comments --paginate`, filtered `created_at >= 2026-11-01T20:00Z` |
| #10 Fable phase (20:47–21:34) | 14 (1 harness REQUEST, 6 DECISION-PROPOSAL, 7 REVIEW) | same |
| #10 Opus phase (21:42–01:04) | 49: 21 FINDING, 12 REQUEST, 9 HANDOFF, 5 REVIEW, 1 REVISION, 1 DECISION-PROPOSAL; 46 by agents and watchers, 3 by the harness | same, TYPE field parsed |
| #9 (FABLE auditors → HARNESS) | 10 FINDINGs, 0 replies on the issue | #9 comments 6563699634 … 6565653998 |
| REQUESTS.md (9 handoff folders) | 57 numbered items, plus 4 rulings or notes written into another team's file (WATCHER-B ruling ×2 at `01-shell/REQUESTS.md:33-35` and `04-loader/REQUESTS.md:44-46`, OPUS-CONTROLLER at `04-loader/REQUESTS.md:48-50`, OPUS-1 at `04-loader/REQUESTS.md:30-42`); 24 commit snapshots touched them | `grep -cE '^[0-9]+\.' handoff/*/REQUESTS.md`; `git log origin/edition/202611012135 -- <file>` |
| PLAN.md (11 files) | 90 commit snapshots (06-file 18, 07-apps 17, 03-layers 14, 05-see-through 14, 04-loader 9, 01 5, 09 5, 02 4, 08 2, 10 1, 12 1); at least 83 time-stamped role entries ("23:27 BUILDER → LEAD, TESTER") in 5 of them | `git log` per file; grep for `HH:MM ROLE` |
| Integration logs | ADMISSIONS.md 5 rows, WATCHER-B.md 17 lines, CONTROLLER.md 4 loops, GREEN.md 2 states + 1 note | `handoff/10-integration/*.md` |
| Harness → agent DMs | 52 SendMessage tonight (32 after 21:36): 12 agent-to-agent relays, 1 owner relay, 19 harness instructions, rulings or wake-ups | harness transcript `e5bfe783…jsonl`, tool_use name `SendMessage` |
| Agent → harness | 81 task notifications after 21:36 (128 tonight); agents' SubagentHandback 55 after 21:36 | same transcript; `subagents/*.jsonl` |
| Agent → agent DM | 1 attempt (FABLE-T4A → "FABLE-T4B", 21:06:42, addressed by label not id) | `subagents/*.jsonl` |
| Agent launch prompts | 103 launches (79 Opus, 24 Fable) for 70 distinct roles; 23 roles relaunched (integrator lead 4×, WATCHER-B 3× plus 4 SendMessage resumes) | harness transcript, tool_use `Agent` |
| OVERNIGHT.md log | 12 entries: 5 by Watcher A, 7 by the harness (`FIXES/NL-010/OVERNIGHT.md:36-47`) | file |

Agents' own tool calls after 21:36, classified by the path or command they touched (`subagents/*.jsonl`):

- PLAN.md: 356 calls by 45 agents
- HANDOFF/TEST/MODULE.sha256: 307 calls by 43 agents
- REQUESTS.md: 130 calls by 36 agents
- Integration logs: 123 calls by 21 agents
- Monitors on handoff files: 18
- Issue reads: 74 calls by 29 agents
- Issue posts: 49 calls by 24 agents

Files: 934 calls. Issue: 123 calls. The ratio is about 7.6 : 1.

### 2. Per-team traffic on #10 (Opus phase)

Senders:
- OPUS-4, OPUS-5 and OPUS-10: 6 each
- OPUS-3 and OPUS-8: 5 each
- OPUS-2 and OPUS-9: 4 each
- OPUS-1, HARNESS and WATCHER-B: 3 each
- OPUS-6: 2
- OPUS-11 and OPUS-CONTROLLER: 1 each
- **OPUS-7, OPUS-12, OPUS-13: 0**

Team 7 worked all night (07-apps/PLAN.md has 17 snapshots) but never posted. Teams 12 and 13 coordinated only
through files and the harness (`handoff/12-see-through-reader/`, `FIXES/NL-010/handoff-13-served.md`).

By role:
- lead: 27
- tester: 9
- evidence officer: 5
- builder: 1
- unlabelled (HARNESS, WATCHER-B, OPUS-CONTROLLER): 7

Within-team messages that went over the issue, by agent-written label: 9 in the Opus phase.
- OPUS-4 evidence → OPUS-4 lead: 6565216493
- OPUS-3 tester → OPUS-3 lead: 6565593336, 6566073338
- OPUS-8 tester → OPUS-8 lead: 6566130521, 6566200296
- OPUS-8 evidence → OPUS-8 lead: 6566138043
- OPUS-9 tester → OPUS-9 lead: 6566567480
- OPUS-10 evidence → OPUS-10 lead: 6564872298, 6565905363

The Fable phase had 7 B → A REVIEWs on the issue.

Who was addressed in the Opus phase:

| addressee | comments naming it in TO (of 49) |
|---|---|
| HARNESS | 45 |
| OPUS-10 | 35 |
| OPUS-3 | 17 |
| OPUS-1 | 14 |
| OPUS-4 | 14 |
| OPUS-2 | 8 |
| OPUS-5 | 8 |
| OPUS-8 | 8 |
| OPUS-9 | 6 |
| OPUS-7 | 5 |
| OPUS-6 | 4 |
| OPUS-12 | 2 |
| OWNER | 2 |

REQUESTS.md items by addressee, tallied by hand from the bold lead of each of the 57 items:

| addressee | items |
|---|---|
| OPUS-10 integrator | 19 (33%) |
| OPUS-3 layers | 9 |
| Owner, See Through owner, homepage owner or harness | 8 |
| OPUS-1 | 7 |
| OPUS-9 | 6 |
| OPUS-4 | 3 |
| OPUS-5 | 3 |
| OPUS-6 | 3 |
| OPUS-7 | 3 |
| OPUS-2 | 1 |

`10-integration`, `00-stub` and `12-see-through-reader` have no REQUESTS.md. The integrator answered through
ADMISSIONS.md rows only.

### 3. The issue was write-mostly

- **ACKs.** Tonight there were 0 comments of TYPE ACK (`PROTOCOL.md:31`, handshake step 2, requires one). On 31 Oct,
  NL-007 had 4 (6549176572, 6549179380, 6549181555, 6549183224).
- **IN-REPLY-TO.** Of the 49 Opus-phase comments, 24 point at a comment id, 20 point only at the issue URL and 5 say
  NEW.
- **Directed comments answered by id.** There were 27 REQUEST, HANDOFF, REVIEW or REVISION comments. Only 3 drew a
  later comment from their addressee (or its stand-in) that cited them by id:
  - OPUS-3's 6564782359 was answered by OPUS-4's 6565079081 after 26 m 29 s.
  - OPUS-10's 6564857812 was answered by OPUS-4's 6565079081 after 19 m 43 s.
  - OPUS-1's 6566485658 was answered by OPUS-CONTROLLER's 6566567995 after 7 m 03 s.
  - The other references were senders citing their own earlier comment (8 cases).
- **The integrator's admissions never reached the issue.**
  - The loader was admitted at 23:19 and the card at 23:35 (ADMISSIONS.md:23,25). Neither was posted by the
    integrator. They first appear on #10 in the harness's R1 HANDOFF 6566064489 at 00:18:53, 60 and 44 minutes
    later.
  - The integrator's three #10 comments are a FINDING, a REQUEST and the one refusal REVIEW 6565858587. Its own plan
    puts only refusals on #10 (`10-integration/PLAN.md:17`).
  - The first admission posted by the slot's holder was OPUS-CONTROLLER's REVIEW 6566567995 (01:00:51), for shell rev
    2.
- **#9 was a sink.** The 10 FABLE findings got no reply on the issue. The harness carried them forward by brief
  (`OPUS-BRIEF.md:28-30`) and by DM. Example: FABLE-03 posted at 22:26:53, and the harness DM'd the integrator
  "03-camera patch has landed" at 22:27:56.

### 4. Request-to-response latency

Both ends are timestamped in every row. File-side ends are bounded by the commit that first carries the answer (the
working tree is shared, so the real time can be earlier). Rows are split by whether a harness DM sat between the
request and the answer.

**No DM in between:**

| request | answer | latency |
|---|---|---|
| OPUS-2 → OPUS-1 ABOUT slot, 6564359696 21:47:49 | 01-shell/PLAN.md "ABOUT now starts with Opus 2's card-law" (LEAD status 22:12, agent stamp), commit f6a2bcc 22:14:54; never answered on #10 | ≤ 27.1 m |
| OPUS-3 item 3 → OPUS-2, 6564782359 22:24:25 | 02-card/REQUESTS.md:21 "answer to issuecomment-6564782359 item 3", commit a72c175 22:42:06 | ≤ 17.7 m |
| OPUS-3 item 4 → OPUS-4, same | 6565079081 22:50:54 (rev 3) | 26.5 m |
| OPUS-10 → OPUS-4, 6564857812 22:31:11 | 6565079081 22:50:54 | 19.7 m |
| OPUS-5 → OPUS-3 hash 87d5db35, 6564873869 22:32:40 | data/layers.json carries 87d5db35 at a72c175 22:42:06 (`git log -S87d5db35`) | ≤ 9.4 m |
| OPUS-5 → OPUS-3 hash 44095071, 6565063296 22:49:32 | layers.json carries 44095071 at 6db1319 23:02:06 | ≤ 12.6 m |
| OPUS-8 HANDOFF 6565879640 00:03:55 | own tester refuses, 6566130521 00:24:09 | 20.2 m |
| OPUS-3 HANDOFF 6565667126 23:44:02 | WATCHER-B REVIEW refuses, 6566289513 00:37:15 | 53.2 m |

Median: about 20 minutes.

**Harness DM in between:**

| request (issue or file) | harness DM | answer | request → answer | DM → answer |
|---|---|---|---|---|
| OPUS-1 HANDOFF 6565195261 23:01:30 | 23:18:31 to the integrator: "Resume the admission loop; team 1 is ready" | admitted 23:21 (ADMISSIONS.md:24) | 19.5 m | 2.5 m |
| OPUS-4 evidence REVIEW 6565216493 23:03:21 | 23:13:13 "BLOCKER from OPUS-4 evidence officer via the harness" | rev 4 at 23:15 (04-loader/PLAN.md:62, agent stamp), commit 1a9505d 23:15:38 | 12.3 m | 2.4 m |
| K1 token, OPUS-2 tester 6564796205 22:25:39 | 22:41:17 "BLOCKER from the harness for OPUS-5 lead" | fixed 22:49 (05-see-through/PLAN.md:102); 6565063296 22:49:32 | 23.9 m | 8.3 m |
| OPUS-1 FINDING mountStar 6564447092 21:55:42 | 23:01:58 "REQUEST from OPUS-1 lead via the harness" | 05-see-through/PLAN.md:110 at 23:04 (agent stamp) | ~68 m | ~2 m |
| OPUS-10 keys-min, 6564788844 22:24:59 | 23:14:37 "From OPUS-3 evidence officer via the harness" | layers.json `lines` → keys-min `e153dfa4` at 2662a4f 23:24:57 | ≤ 60 m | ≤ 10.3 m |
| Shell refusal 6565858587 00:02:03 | 00:29:02 "the whole integration order waits on your shell rev 2" | HANDOFF rev 2 6566485658 00:53:48 | 51.8 m | 24.8 m |
| OPUS-8 tester REQUEST 6566200296 00:29:51 | 00:46:56 "Tester refused: apply drift-fix.patch" | REVISION 6566504289 00:55:25 | 25.6 m | 8.5 m |
| Loader file overwritten (E6), OPUS-10 evidence 6565905363 00:06:09, OPUS-9 6566235285 00:32:42 | 00:56:49 "Harness rulings … E6" | restored by OPUS-CONTROLLER, logged at 00:59 (CONTROLLER.md:7) | ~53 m | ≤ 2.2 m |
| Shell rev 2 HANDOFF 6566485658 00:53:48 | 00:54:33 "Shell rev 2 handed off: admit now" | admitted 00:56 (ADMISSIONS.md:28) | 2.2 m | 1.5 m |

Medians: about 26 minutes from request to answer, about 2.5 minutes from DM to answer.

Every sub-5-minute answer tonight came right after a harness DM. The one exception is the card admission 2 minutes
after its HANDOFF (23:33:14 → 23:35), and even there the integrator had the harness's ordered work list from 23:18:31.

The harness was sometimes ahead of the link too:
- The integrator admitted the loader at 23:19 "on the harness's instruction" (ADMISSIONS.md:23). OPUS-4's REQUEST to
  apply rev 4 (6565452163) was posted 5 minutes later, at 23:24:14.
- The harness's redaction commit 93a5ae9 (00:58:57) landed 1 second before OPUS-9 tester's K1 FINDING 6566545614
  (00:58:58).
- OPUS-CONTROLLER still asked OPUS-12 to clear K1 at 01:00:51 (6566567995), about 2 minutes after the redaction.

Fable phase, for contrast: the harness's REQUEST 6563668560 (20:47:20) drew all 5 team DECISION-PROPOSALs between
21:05:59 and 21:33:52 (18.6–46.5 m). Three of the five posts came 21 s to 59 s after a harness DM to that agent (DMs at
21:05:38, 21:18:22, 21:27:51; posts at 21:05:59, 21:19:21, 21:28:02).

### 5. Harness relays: the real bus

- **Agent-to-agent relays.** 12 DMs after 21:36 are literal relays. 6 cross teams:
  - OPUS-1 → OPUS-5 and OPUS-1 → OPUS-4 at 23:01:58 and 23:02:00
  - OPUS-1 tester → OPUS-4 at 23:05:46
  - integrator's journey → OPUS-1 and → OPUS-4 at 23:48:39 and 23:48:44
  - OPUS-5 tester → OPUS-3 at 23:48:46
- **Intra-team relays.** The other 6 relays stayed inside a team, which shows that PLAN.md alone did not wake a
  teammate:
  - OPUS-4 builder → tester, twice: 22:27:33 and 22:41:21
  - OPUS-4 evidence → lead: 23:13:13
  - OPUS-3 evidence → lead: 23:14:37
  - OPUS-7 builder → lead: 23:27:57
  - OPUS-9 builder → lead at 00:46:12, "it waited 8 minutes for your reply in PLAN.md"
- **Relays left traces in files but not on the link:**
  - `04-loader/REQUESTS.md:30` ("via the harness")
  - `04-loader/PLAN.md:76,92`
  - `05-see-through/PLAN.md:110,119` ("the harness relayed OPUS-1's …")
  - `03-layers/PLAN.md:189`
  - `10-integration/ADMISSIONS.md:23,28` ("on the harness's instruction", "on the harness's ruling")
  - `CONTROLLER.md:7` ("harness ruling 1", "ruling 2")
  - `WATCHER-B.md:5,15`
  - `GREEN.md:16` ("owner via the harness")
  - `OVERNIGHT.md:39` ("teams 1 and 4 told") and `:46` ("controller told to admit it now")
- **Ratio.** The harness sent 32 DMs and posted 3 comments on #10 in the Opus phase, about 11 : 1.
- **Interface rulings never reached the link.** Two rulings by the harness only exist in files and DMs:
  - "rev 5 optional tonight" (`04-loader/REQUESTS.md:50`, `ADMISSIONS.md:28`)
  - E6 and E3 (`CONTROLLER.md:7`, DM 00:56:49)

  The first one quietly overrode WATCHER-B's on-issue ruling 6566317112 (00:39:30, "KY.nav is the one owner") about
  15–20 minutes after it was posted.

### 6. Bottlenecks: who everyone waited on, and for how long

1. **The admissions slot (integrator → WATCHER-B → OPUS-CONTROLLER).**
   - It was addressed in 35/49 Opus-phase comments and 19/57 REQUESTS.md items.
   - It made 3 admissions in 97 minutes: loader 23:19, card 23:35, shell rev 2 00:56. One refusal: shell rev 1, 00:03
     (ADMISSIONS.md:23-28).
   - The slot changed hands twice in 11 minutes: the integrator ended at 00:36 (ADMISSIONS.md:27), WATCHER-B took
     over, and OPUS-CONTROLLER took over at 00:47 (CONTROLLER.md:5).
   - WATCHER-B's run ended twice by handback, at 00:34 and 00:37 (WATCHER-B.md:13,17). The integrator lead was
     launched 4 times.
   - The order is strictly serial: 4, 1, 2, 3, 6, 5, 7, 8, 9 (ADMISSIONS.md:3). Since the layers HANDOFF at 23:44 (81
     minutes by 01:05), these have queued behind it: see-through (HANDOFF 01:04:14), apps (HANDOFF.md committed 00:38),
     drift (REVISION 00:55:25) and law. CONTROLLER.md:8 records "waits behind 3, 6 by order".
2. **The shell and loader history owner (Android back).** This blocked the whole queue.

   | time | event | key |
   |---|---|---|
   | 23:04:47 | OPUS-2 tester predicts the conflict and asks OPUS-1 and OPUS-4 to agree | 6565232619 |
   | 23:21 | the shell is admitted anyway | ADMISSIONS.md:24 |
   | 23:36 | Watcher A measures `lines-pick` and `card-details` red | OVERNIGHT.md:37 |
   | 23:48:39 | the harness relays the blocker to OPUS-1 and OPUS-4 | DM |
   | 00:02:03 | refused | 6565858587 |
   | 00:02 → 00:22 | the shell file churns 352c20c6 → 4c0e8314 → 6fa6d5c0 → 1edf2e1a while MODULE.sha256 stays eeea4581; WATCHER-B logs "no new hand-off" on 7 consecutive loops (00:10–00:39) | WATCHER-B.md:4-18 |
   | 00:29:02 | the harness tells OPUS-1 "the whole integration order waits on your shell rev 2" | DM |
   | 00:39:30 | WATCHER-B rules that KY.nav owns history | 6566317112 |
   | 00:53:48 | rev 2 is handed off without KY.nav | 6566485658 |
   | 00:56 | admitted on the harness's ruling | ADMISSIONS.md:28 |

   - Prediction to fix admitted: 1 h 51 m.
   - Refusal to re-admission: 54 m.
   - Final bytes (1edf2e1a, 00:22, WATCHER-B.md:14) to HANDOFF: about 31 m.
   - OPUS-1 and OPUS-4 never answered each other on #10.
3. **The loader patch (04-loader/index.html.patch).**
   - Everyone built against it. From the hook-table FINDING 6564299733 (21:42:44) to rev 4's admission (23:19) took
     96 minutes.
   - It went through 5 revisions: rev 2 at 22:14, rev 3 at 22:55 (withdrawn after review), rev 4 at 23:15, rev 5 at
     00:10 (never handed off; reverted by 01:05 per CONTROLLER.md:8). Revision times are agent stamps from
     `04-loader/PLAN.md:24,52,62,90`.
   - While it moved, teams built private pages to test on:
     - The shared stub died on the first request (FINDING 6564960147, 22:40:23).
     - The OPUS-6 builder kept its own stub-b.cjs and the OPUS-6 lead its own mksite.py (`06-file/PLAN.md`, entries
       22:44 and 22:58).
     - OPUS-2's tester ran without `window.KY` (`02-card/PLAN.md:48`).
   - Rev 5's in-place overwrite of the listed loader file broke E6 from about 00:02 to 00:59 (WATCHER-B.md:4,
     CONTROLLER.md:7).
4. **OPUS-3 (layers): second hub and largest orphan holder.**
   - It was addressed in 17 comments and 9 REQUESTS.md items, and it holds 5 of the orphans below.
   - It could not finish without the shell (`03-layers/REQUESTS.md:19`, "STILL OPEN"). That made the chain
     layers → shell → loader history owner, so every later team (6, 5, 7, 8, 9) waited behind those three.
5. **Late starts from the 20-agent cap** (`OVERNIGHT.md:31-32`). The first launches went out at 21:36–21:39 for every
   team, but leads started much later (agent stamps):
   - team 6: 22:31 (`06-file/PLAN.md:3`)
   - team 7: 23:10 (`07-apps/PLAN.md:1`)
   - team 8: 23:24 (`08-drift/PLAN.md:3`)
   - team 9: 00:05 (`09-law/PLAN.md:3`)

   That is 50–150 minutes late. Team 8's lead and team 9's lead each did parts alone because teammates had not
   arrived (`08-drift/PLAN.md:34`, `09-law/PLAN.md:20-27`).

### 7. Orphan requests (no answer in any channel by 01:05)

1. OPUS-10 → OPUS-3, 6564857812 (22:31:11): carry 03-camera's band, keeper, reach and 96 px rule into layers. Still
   open; the cut was refused for exactly these at 00:37:15 (6566289513). Open 2 h 34 m+.
2. OPUS-10 → OPUS-3, 6564788844 (b) (22:24:59): keep the 07-perf `content-visibility` CSS. Listed as removed in
   6566289513. Open 2 h 40 m+. Part (a), keys-min, was answered.
3. OPUS-6 → OPUS-3, 6565553299 (23:33:30) and `06-file/REQUESTS.md:31-34`: `edSel` undefined. Measured again by
   WATCHER-B at 00:33 (GREEN.md:22-23). Open 1 h 31 m+.
4. OPUS-7 → OPUS-3, `07-apps/REQUESTS.md:3-14` (committed 23:28): record `elements` as e204cb41… and the two spider
   files. Now `data/layers.json` has `elements` sha256 28b8b2df… and `spider` source.file null, while
   `sha256sum data/elements.json` is e204cb41…. Open 1 h 37 m+.
5. OPUS-8 → OPUS-3, 6565879640 (00:03:55) and `08-drift/REQUESTS.md:8-13`: add the `drift` record. `data/layers.json`
   has no `drift` id (ids: periods, repos, editions, lines, see-through, elements, spider). Open 61 m+.
6. OPUS-2 tester → OPUS-1 and OPUS-4, 6565232619: "agree on one owner". Never answered by either; settled by third
   parties (WATCHER-B, then the harness).
7. WATCHER-B → OPUS-1 and OPUS-4, 6566317112: "each answers here with the sha256". No comment cites it. OPUS-4 posted
   nothing after 00:38:51.
8. OPUS-3 tester → OPUS-1, 6565593336 (23:37:14) and 6566073338 (00:19:36): "say on #10 which of the two you take". No
   OPUS-1 comment until the rev 2 HANDOFF.
9. OPUS-9 → OPUS-7, 6566235285 item 3 (00:32:42): register or periodic-table copy. OPUS-7 posted nothing tonight.
10. Requests to the owner or outside the edition, 9 items, none answered on the link tonight (the owner posted 0
    comments):
    - Q7: `01-shell/REQUESTS.md:18`
    - viewport zoom: `04-loader/REQUESTS.md:26`
    - Q1 and Q5: `07-apps/REQUESTS.md:26`
    - pipelinenews clone: `08-drift/REQUESTS.md:17`
    - See Through folder cut: 6564878115 and `05-see-through/REQUESTS.md:5`
    - homepage link: `05-see-through/REQUESTS.md:40`
    - pointer patch for PR B: `09-law/REQUESTS.md:19`
    - `EDITION 2 ·` readout: `04-loader/REQUESTS.md:12`
    - DISCLOSED copy: `09-law/REQUESTS.md:12`

Tally of the asks traced here: 35 in all (the 17 rows of section 4 plus the 18 open items of this section).
- 12 were answered within 30 minutes of the request. 5 of those followed a harness DM; the other 7 were answered in a
  file, or by a comment from a receiver that was already polling.
- 18 were still open at 01:05: the 9 agent-to-agent items above plus 9 to the owner or outside the edition.

## Which channel carried the coordination tonight

Three layers, plainly:

- **Signalling.** The harness's DMs and agents' handbacks woke agents and moved decisions. Every fast answer came after
  one.
- **Shared state.** The handoff files were what agents read and acted on: REQUESTS.md, PLAN.md, MODULE.sha256,
  TEST.md and ADMISSIONS.md. They saw them instantly on a shared working tree, not through git (the edition branch
  had 43 commits since 21:30, with a median gap of 2.7 minutes and a maximum of 28.4).
- **Log.** Issue #10 was a public announcement log: rich, well-formed envelopes, rarely answered by id, never
  ACKed, and missing the integrator's two admissions.

The files were the bus for content; the harness was the bus for attention. The issue was neither.

## What to change (small, concrete)

1. **Give each receiver one inbox file and make it the request bus.**
   - Add `handoff/<NN>/INBOX.md`, append-only, one row per ask: `id | utc (date -u) | from | ask | status
     OPEN/ACK/DONE/REFUSED | answer-ref`.
   - The receiver flips the status in place.
   - Retire "write your needs in your own REQUESTS.md". Tonight people already wrote into the receiver's file
     (`04-loader/REQUESTS.md:30-50`).
2. **Make the admitting agent post one line per verdict on #10**, ADMIT or REFUSE, with IN-REPLY-TO set to the HANDOFF
   comment. Tonight requesters had to poll ADMISSIONS.md, and the first public word of two admissions came 44–60
   minutes late.
3. **Log every harness relay.** Each DM gets one line in `FIXES/<NL>/RELAYS.md` (utc, from, to, comment id or file
   path), or a 1-line mirror comment for BLOCKER and ruling relays. Then the link shows the 12 relays and the rulings
   (rev 5 optional, E6, E3) that actually moved work.
4. **Give every agent a wake-up on its inbox.** Each agent runs one Monitor on its INBOX.md (and its team PLAN.md), so
   the 6 intra-team relays become unnecessary.
5. **Break the serial admission queue.** Independent modules (apps, drift, see-through) can be admitted against the
   last GREEN state on their own snapshots, so they do not wait behind layers.
6. **Time-box contested interfaces.** When two teams name the same shared resource (history state, base index.html,
   the loader file), the controller rules within 15 minutes on #10, and the harness does not override it silently.
   Tonight: prediction 23:04, ruling 00:39, override about 00:56.
7. **Sweep for orphans each loop.** The controller lists OPEN inbox rows older than 30 minutes in CONTROLLER.md. The 9
   open agent-to-agent items above would have surfaced between 23:30 and 01:05.
8. **Keep the admissions slot alive.** Run the controller as a single long-lived loop that survives turn ends,
   instead of the integrator (4 launches) handing to WATCHER-B (3 launches plus 4 resumes) handing to the controller.

## Limits

- **Transcript classification.** Channel counts in section 1 come from keyword matching on tool calls in
  `/root/.claude/projects/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594{.jsonl,/subagents/*.jsonl}`. One Bash call
  that reads several files counts once, and a call that mentions none of the keywords is not counted, so file counts
  are lower bounds. These transcripts are this session's only; the subagents' incoming DMs are seen only as the
  harness's outgoing calls.
- **File-side timing.** File-side answer times are bounded by harness commit snapshots, because agents share one
  working tree. A "≤" latency can be shorter. PLAN.md role-entry counts (83) only match one stamp format.
- **Agent-written times.** These are marked. 7 of 74 issue envelopes are ≥ 5 minutes off their GitHub time, and the
  harness was up to +117.7 minutes off (6563668560). OVERNIGHT.md:47 corrects three harness stamps.
- **Window.** Issue data was fetched at 01:06Z. Later traffic (harness comments at about 01:14Z, the NL-011 issue) is
  outside the window.
- **Sources that do not match the brief.** The brief lists "FIXES (NL-007 rounds …)", but no `FIXES/NL-007` folder
  exists in this checkout. Issues #7 (50 comments) and #8 (6) are dated 31 Oct, not tonight; only #6 (2), #9 (10) and
  #10 (63) carry tonight's traffic.
- **Orphan list.** "Answered" means a measurable change (a file, hash or comment) that the ask names. An ask answered
  only in an agent's head, or in a scratch directory under /tmp/nl010-opus, counts as open.

Commands (scripts kept in the session scratchpad, `/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/scripts/`):

- `parse.py` and `stats.py`: issue envelopes, types, addressees, reply links, skew
- `tx.py` and `reads.py`: harness DMs, launches and agents' channel use
- `git log --format='%h %ad' --date=format:%H:%M origin/edition/202611012135 -- <file>`: file snapshot times
- `git log -S<hash> -- editions/202611012135/data/layers.json`: when requested records landed
