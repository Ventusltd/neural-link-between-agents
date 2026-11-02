# NL-011 study 02: failure catalogue (lens: coordination failures, 1 Nov 20:36 – 2 Nov 01:05 UTC)

Written by NL-011 STUDY-02, the time read with `date -u` at writing: 2026-11-02T01:18Z. Study only. Nothing posted,
committed or edited outside this file.

**Verdict.** The link was not where most failures were caught: of the nine classes below, the issue thread caught the
first case of only four (the `@file` bodies, K1, the moving base and handoffs posted before review). The other five were
found in hand-off files (PLAN.md, TEST.md, WATCHER-B.md, CONTROLLER.md) or by the loader's own sha256 check, and the
link was told late or never. The costliest failures were not about messages. They were about *which bytes* a claim was
about: tests run on a stale or wrong server (about 171 min of void work), patches cut against a page that kept moving
(about 139 min), K1 tokens committed by the harness's blind commits (100 min at the branch head, and all seven blobs
still in history), and files written by an agent that did not own them (90 min, plus a loader-reference mismatch that is
**still live on kuiper-belt main e92ad5d**). Each class has a one-line rule that would have stopped it, and most of
those rules are a check on a sha256 or a grep that one script can run before posting, committing or admitting.

## How cost is measured

- **Cost (min)** = minutes of work that was voided or blocked, from the timestamp of the failure to the timestamp of the
  state that closed it (GitHub `created_at`/`updated_at`, commit dates from `git log --date=iso`, or `date -u` stamps
  that the file says were read from the clock). Where a class has several incidents, their minutes are added. Incidents
  run in parallel, so the sum is agent-minutes, not wall-clock minutes. **Exposure** is how long the defect stood.
- **Caught by**: **L** = an issue comment on the link; **F** = a hand-off or log file; **H** = the harness (a direct
  message to an agent, a harness commit or a log entry); **T** = a tool refused it (the loader, ci_check).
- Keys: `#c<id>` = an issue comment on Ventusltd/neural-link-between-agents. `kb@<sha>` = kuiper-belt commit.
  `nl@<sha>` = neural-link commit. `H/` = `kuiper-belt/editions/202611012135/handoff/`.
- Window: "tonight" means 1 Nov 20:36 (nl@04b8b87) to 2 Nov 01:05 (kb@7fb8ccc). In that window #6, #9 and #10 carry
  75 comments. #6–#8 traffic from 31 Oct is used only for comparison.

## Ranked table

| rank | failure class | incidents | first (key, UTC) | last (key, UTC) | cost (min) | exposure | caught first by | smallest rule |
|---|---|---|---|---|---|---|---|---|
| 1 | tests run on a stale or wrong server/snapshot | 13 void runs in 5 teams | `H/06-file/PLAN.md:245` server never bound 23:05 | `H/06-file/PLAN.md:244` builder's correction 01:02 | **171** | 23:05–01:02 | F (only) | a run records the sha256 of what the *server* returned; if it differs from the bytes under test, the run is void |
| 2 | patches cut against a moving base | 4 teams (01, 03, 04, 05/07) | #c6564857812 22:31 (hunk 12 FAILED) | kb@7fb8ccc rev 5 shelved 01:05 | **139** | 22:31–01:05 | L | line 1 of a patch states `base-sha256`; apply refuses any other page |
| 3 | K1 privacy tokens committed to the branch | 5 incidents, 7 blobs | kb@2c87ba4 22:03:40 | kb@93a5ae9 00:58:57 | **100** | 100 min at head; history permanent | L (3 of 5) | the harness runs `tools/ci_check.py` before each "files as they land" commit and leaves failing paths unstaged |
| 4 | files overwritten by an agent that does not own them | 5 (test.cjs ×3, GREEN.md, loader reference) | `H/02-card/TEST.md:91` 21:52 | kb@5050fbe loader restored 01:02:27 | **90** + main still wrong | main: 00:05:55 → open | F | one writer per path; a listed module file is never edited in place |
| 5 | module or data edited after hand-off (sha256 ≠ manifest) | 4 (shell, apps data, drift, line-card) | kb@0cd7910 shell 352c20c6 23:59:40 | `H/10-integration/CONTROLLER.md:7` E9 00:59 (open) | **86** | 23:59–open | T (the loader) | when MODULE.sha256 is written the files go read-only; a change needs a new stamp |
| 6 | placeholders left in HANDOFF.md / TEST.md | 2 HANDOFF.md, 1 TEST.md, 1 comment header | kb@4a4ee2d `__STATUS__` 22:23 | kb@7fb8ccc still present 01:05 | **84** | 162 min (loader) | F (only) | the integrator and the poster refuse a file matching `__[A-Z]+__\|UTC_STAMP\|HEAD_SHA\|TEST_STATUS\|TEST_TABLE` |
| 7 | handoffs posted (or admitted) before review | 4 + 1 near miss | loader admitted 23:19 with TEST.md "running" | #c6566607555 01:04:14 | **52** | — | L | the integrator ignores a HANDOFF that does not quote the evidence verdict and the tester's TEST.md sha256 |
| 8 | literal `@file` comment bodies | **10** comments (9 repaired by the harness, 1 by its author) | #c6563699634 20:50:05 | #c6564036574 21:19:23 | **32** (link span); 145 comment-min | 20:50:05–21:22:20 | F, then L | post through one script that refuses a body starting with `@` and reads the body back |
| 9 | times not read from a clock | 19 comments ahead of `created_at` (10 by ≥3 min); 5 of 9 harness log entries; 9 file stamps | #c6563668560 (+117.7 min) 20:47:20 | `H/04-loader/PLAN.md` "01:10 UTC" committed 01:05:10 | **0** blocked (trust cost) | — | F, H | the envelope time comes from `date -u` in the same command that posts or writes |

The total is about 754 agent-minutes in 4 h 29 min of wall clock.

## Findings

### 1. Tests run on a stale or wrong server/snapshot. Cost 171 min, 13 void runs, caught only in files

- **Wrong server, 117 min.** Team 6's builder ran every Galaxy S24 run from 23:05 to 01:02 on a stale stub. Its
  `python3 -m http.server 8461` "never bound: Address already in use" because its own stub (`node stub-b.cjs`, started
  22:43) still held the port. The runs it reported at 23:06 and 00:11 as on "my copy of the lead's scratch site" were not
  (`H/06-file/PLAN.md:244-251`). The builder itself caught it, in a file, at 01:02. Nothing went to the link. Port
  contention shows up again at `H/06-file/PLAN.md:81` ("8460 is held by another team's server").
- **Inconsistent snapshot, 2 min.** Integrator Run 2 (00:00) froze a manifest naming kuiper-shell `eeea4581…` while the
  file on disk was already `352c20c6…`, and it was aborted at 00:01 (`H/10-integration/TEST.md:108-117`).
- **Controller measured a page that was reverted, 7 min.** WATCHER-B's w1-fix/w2-adm runs (23:55–00:02) measured the
  integrator's *uncommitted* index `5617077b`. The integrator reverted it to `418ae14c` during the run
  (`H/10-integration/WATCHER-B.md:3-4`).
- **Stale page or data under test, 45 min.** Team 5's run7 was void at 00:12 because the page on disk changed under it
  (the preview patch refused, so it fell back to a shim), and the next valid run started at 00:45
  (`H/05-see-through/PLAN.md:138-139`). Its run3 sha256 mismatches "came from files edited mid-run"
  (`H/05-see-through/PLAN.md:100-101`). Team 7's run 1 used team 6's 22:50 index, which had no `refuse` hook. Its run 3
  used the module of 23:37, which lacked the 23:47 fix. Its run 4 read the pre-00:00 elements.json. Its FINAL TEST.md
  (00:39) hashed apps.json `9ade18cf…`, not the sealed `ba59b9bd…`/`027f6614…`, and the re-run did not start until
  00:51 (`H/07-apps/PLAN.md:183-189, 229-233, 239-243, 272-286`). Team 3's run 5 (23:20) ran on "a page without KY", and
  its run 7 read a MODULE.json copied one minute before the lead changed it (`H/03-layers/PLAN.md:143, 203-204`).
- Void runs counted: team 6 3, team 7 4, team 5 2, team 3 2, team 10 1, WATCHER-B 1, giving **13**. Load averages of
  57–95 (`H/10-integration/WATCHER-B.md:3-12`) and "about 15 Playwright runs at once" (`H/05-see-through/PLAN.md:135`)
  stretched every void run.
- **Rule:** every test report records the sha256 of index.html, modules.json and each module *as fetched from the
  server during the run*. If any of them differs from the bytes named as under test, the run is void. A server is
  started by a script that fails if the port does not bind.

### 2. Patches cut against a moving base. Cost 139 min, caught first on the link

- **First:** #c6564857812 (OPUS-10, 22:31:11). Once 03-camera was applied to the base (now `390b15ae…`), NL-009
  04-touch's hunk 12 "no longer applies" (`H/10-integration/BASE.md:60-62`). At 22:35 team 1 wrote "index.html is moving
  under Opus 10" and pinned every key at 96736f5 (`H/01-shell/EVIDENCE.md:20`).
- **Team 4, 48 min (22:31 → 23:19).** Rev 3 of the loader patch diffed "the live, moving page against a page built on
  96736f5", so applying it "would have undone 48 of the 50 lines team 10 added" (`H/04-loader/PLAN.md:64-66`). The team's
  own evidence officer caught it as a BLOCKER on the link (#c6565216493, 23:03:21). Rev 4, cut against the frozen base,
  was admitted at 23:19 (`H/10-integration/ADMISSIONS.md:23`).
- **Team 3.** At 23:20 "the base index.html moved again … team 4's patch no longer applies", so the line patch was dropped
  and the cut was redone by content (`H/03-layers/PLAN.md:142-146`; `H/03-layers/REQUESTS.md:7`: "a line patch goes stale
  each time"). That cut was refused at 00:37 because it removed base lines (`ED_MINBAND`, `edKeep`, `tween.dur`, 07-perf
  CSS; #c6566289513). Layers was still not admitted at 01:05, 28 min after the refusal.
- **Team 7.** Team 3's patch "does NOT apply … 2 of 6 hunks fail" on the integrator's page, so team 7 tested without it
  (`H/07-apps/PLAN.md:186-187`; `H/07-apps/TEST.md:115`).
- **Team 4 rev 5, 63 min (00:02 → 01:05).** It was cut against `390b15ae`, which "applies only after rev 4 is reverted"
  (`H/10-integration/WATCHER-B.md:4`). The controller ruled at 00:39 that it be re-cut as a delta on the live page
  (#c6566317112). It was then shelved under a new stamp (`H/04-loader/PLAN.md` "01:10 UTC" section, committed in
  kb@7fb8ccc 01:05:10).
- **Rule:** line 1 of every patch states `base-sha256: <64 hex>`, and the integrator applies a patch only to a page with
  that hash. When the integrator changes the base, it writes one line in BASE.md (new sha256, time from `date -u`).
  Team 4's rev-4 practice (diff against a frozen copy, "never against the live file", `H/04-loader/PLAN.md:72`) is the
  rule. It was learned after the cost.

### 3. K1 privacy tokens committed to the branch. Cost 100 min at the head; 7 blobs permanent in history

Measured by replaying `tools/check_proof.leaks()` (the function K1 calls) over every blob changed in
`96736f5..origin/edition/202611012135`. The script is in the scratchpad (`k1hist.py`). The output is below.

| # | file(s) | in (commit, UTC) | caught (key, UTC, by) | out (commit, UTC) | min at head |
|---|---|---|---|---|---|
| 1 | data/see-through.json, handoff/05-see-through/build-see-through-json.py | kb@2c87ba4 22:03:40 | #c6564796205 22:25:39 (L, OPUS-2 tester); "HARNESS BLOCKER" `H/05-see-through/PLAN.md:102` (H) | kb@6db1319 23:02:06 | 58.4 |
| 2 | data/apps.json, data/graphs/periodic-table.json, data/elements.json | kb@b8e7c74 23:14:44, kb@38ed53c 23:21:33 | #c6565383566 23:18:01 (L); builder `H/07-apps/PLAN.md:111` 23:27 (F) | kb@2662a4f 23:24:57 | 10.2 |
| 3 | handoff/07-apps/img/element-card.png | kb@b9d514c 00:26:36 | #c6566300129 00:38:07 (L); `H/10-integration/CONTROLLER.md:5` 00:47 (F) | kb@c7c3e7c 00:49:41 (removed by the harness) | 23.1 |
| 4 | handoff/12-see-through-reader/EVIDENCE.md | kb@7966a47 00:50:54 | #c6566545614 00:58:58 (L); #c6566567995 01:00:51 | kb@93a5ae9 00:58:57 (redacted by the harness) | 8.1 |

There are 5 incidents in all, because incident 2 counts as two (the elements.json blob arrived 7 minutes after the first
pair). Every blob is still in branch history (`H/07-apps/PLAN.md:214-216`; `H/07-apps/EVIDENCE.md:277`). Main never
carried one (R1 was squashed at e92ad5d 00:05:55, before incidents 3 and 4). The cause is structural: the harness commits
"files as they land" every few minutes without running K1. OPUS-9's tester named the fix in #c6566545614: "run
`python3 tools/ci_check.py` before the harness commits".
**Rule:** the harness's commit step runs K1 on the staged files and leaves any failing path unstaged, with a one-line
note to its owner.

### 4. Files overwritten by an agent that does not own them. Cost 90 min, plus one defect still live on main

- **Loader reference, 61 min on the branch, still open on main.** Team 4's lead "overwrote
  `modules/202611012145-loader.js` with rev 5 in place" (`H/04-loader/PLAN.md:111-112`). In git, the file was
  `25a16f1d…` at kb@b8e7c74 23:14:44 and `d9272b82…` at kb@833bd6e 00:01:04, and it was restored at kb@5050fbe 01:02:27
  (`git show <c>:editions/202611012135/modules/202611012145-loader.js | sha256sum`). Team 9 caught it in a file
  (`H/09-law/REQUESTS.md:3-6`: "the same mismatch is on main at e92ad5d"), and so did WATCHER-B
  (`H/10-integration/WATCHER-B.md:4`, 00:02). The link was told at 01:00:51 (#c6566567995 item 2). **Checked at writing:**
  `origin/main` e92ad5d `modules.json` `references[0]` = `25a16f1d3c3f`, while the file on main = `d9272b82421d`. The
  published preview still fails edition_check E6.
- **test.cjs, 3 times.** On team 2, "another team-2 agent wrote to this path at 21:52" and again at 22:07. The tester
  merged at about 21:58 and kept copies (`H/02-card/TEST.md:91`; `H/02-card/test.cjs:4`). On team 4, the lead's drafts of
  21:52 and 22:01 went over the tester's file, and the tester put a banner on top by kb@f6a2bcc 22:14:54
  (`H/04-loader/TEST.md:3-6`). Team 5 carries the same banner pre-emptively (`H/05-see-through/TEST.md:8-9`). On team 3,
  the lead edited the tester's test.cjs at 22:56 ("TESTER: please check both lead edits", `H/03-layers/PLAN.md:113-117`).
- **GREEN.md.** WATCHER-B wrote it at 00:27, and the integrator "rewrote GREEN.md as its own table" at 00:28
  (`H/10-integration/WATCHER-B.md:10-11`).
- **Apps data.** When the builder went silent, team 7's lead rebuilt the builder's `data/elements.json` (23:59,
  `H/07-apps/PLAN.md:234-238`). Team 5's regenerated `data/see-through.json` broke team 3's hash record
  (`H/03-layers/PLAN.md:117`).
- **EVIDENCE.md:** in the files I found role takeovers that were done with care, not destructive overwrites. Team 8's
  evidence officer "takes over the draft the lead wrote" (`H/08-drift/EVIDENCE.md:3-5`, 00:02). Team 9's evidence officer
  "owns EVIDENCE.md from 00:36 (the lead's measured sections kept)" (`H/09-law/PLAN.md:69`). Team 6's evidence officer
  wrote "LEAD: please leave EVIDENCE.md to me" (`H/06-file/PLAN.md:120`). A destructive EVIDENCE.md overwrite is
  **UNVERIFIED** here.
- Cost: loader 61, team 4 test.cjs 22, team 2 test.cjs 6, GREEN.md 1, for a total of 90 (main is still open after 59+
  min).
- **Rule:** PLAN.md names one writer per path. Anyone else writes `<path>.<role>.draft` and says so. A file listed in
  `modules.json` (records or `references`) is never edited in place: a change is a new stamped file. The harness can
  enforce the second part at commit time by refusing a change to a listed file whose manifest sha256 did not change.

### 5. Module or data edited after hand-off (sha256 ≠ manifest). Cost 86 min, caught first by the loader

- **Shell, 54 min.** It was admitted at 23:21 as `eeea4581…` (`H/10-integration/ADMISSIONS.md:24`). The file then changed
  in place: `352c20c6` (kb@0cd7910 23:59:40), `6fa6d5c0` (kb@89e03f0 00:16:13), then `1edf2e1a` (kb@507df4f 00:25:32),
  and WATCHER-B logged a fourth, `4c0e8314` (`H/10-integration/WATCHER-B.md:6`). Through all of this MODULE.sha256 still
  said `eeea`. The loader refused it ("kuiper-shell refused: sha256 mismatch", `H/10-integration/TEST.md:110-113`). It was
  withdrawn at 00:01 and refused on the link at 00:02:03 (#c6565858587), and rev 2 was handed off at 00:53:48
  (#c6566485658). The loader worked as designed. The process did not stop an author from editing admitted bytes.
- **Apps data, 26 min.** It was resealed after the tester's FINAL run (00:39 → 00:40 → a lead re-run from 00:51,
  `H/07-apps/PLAN.md:272-286`, the lead re-run at :282).
- **Drift, 6 min to 01:05 and still open.** `tools/drift.py` changed after MODULE.sha256 was written
  (`H/08-drift/EVIDENCE.md:309`), and E9 fails: `data/drift.json` is `388103129b90` but recomputes as `1640823a7173`
  (`H/10-integration/CONTROLLER.md:7`).
- **Line-card, 0 min.** It tested `788256a9…`, while the file is `e2baeaaa…` after a comment-only change. Team 2
  disclosed this, and the journey measured the admitted bytes (`H/10-integration/ADMISSIONS.md:25`).
- **Rule:** writing MODULE.sha256 seals the files (`chmod a-w` on the module and its data). Any later change is a new
  stamp and a new hand-off. The tester's run is void if a sealed sha256 changes.

### 6. Placeholders left in HANDOFF.md / TEST.md. Cost 84 min, caught only in files

- **Team 4 HANDOFF.md, 162 min of exposure.** `STATUS: __STATUS__` is in every committed version, from kb@4a4ee2d (22:23)
  to the tip kb@7fb8ccc (01:05). `[__TIME__ UTC]` was added at kb@db9a3f0 (23:28) and is still there. The check was
  `git show <c>:…/04-loader/HANDOFF.md | grep -o '__\(TIME\|STATUS\)__'`. **Team 4 TEST.md** has read "Status: running"
  in its only committed version (kb@f6a2bcc 22:14, 8 lines) through the tip. The HANDOFF and PLAN cite a "93/93 PASS"
  that TEST.md does not hold. The placeholders were named as a reason nothing was admissible at 00:02, 00:10 and 00:47
  (`H/10-integration/WATCHER-B.md:4,6`; `H/10-integration/CONTROLLER.md:5`), and they held rev 5 out until the 00:59
  ruling: **57 min**.
- **Team 7 HANDOFF.md, 27 min.** `UTC_STAMP`, `HEAD_SHA`, `TEST_STATUS` and `TEST_TABLE` have been there since
  kb@af4827e 00:38 and are still present at the tip. WATCHER-B logged "Team 7 HANDOFF.md landed" and then, in the same
  minute, "still a template" (`H/10-integration/WATCHER-B.md:16-17`).
- **Comment header.** The shell rev 2 HANDOFF #c6566485658 is stamped `[2026-11-02 UTC]`, with no time.
- **Rule:** before posting or admitting, run one grep that refuses
  `__[A-Z]+__|UTC_STAMP|HEAD_SHA|TEST_STATUS|TEST_TABLE` in HANDOFF.md, and refuses a TEST.md without a final `PASS` or
  `FAIL` line.

### 7. Handoffs posted (or admitted) before review. Cost 52 min, caught on the link

Of the 11 HANDOFF/REVISION comments tonight, three were posted before review and one module was admitted with no
reviewed handoff:

- **Loader (team 4)** was "admitted 23:19 UTC on the harness's instruction", while "team 4's TEST.md still read
  'running'" (`H/10-integration/ADMISSIONS.md:23`) and HANDOFF.md said `__STATUS__`. The verdict it promised ("recorded
  here when it lands") never landed in TEST.md (finding 6).
- **Card (team 2)** #c6565550370 23:33:14: "The HANDOFF text itself was not reviewed because it did not exist yet: NOT
  EVALUATED" (`H/02-card/EVIDENCE.md:296-297`).
- **Drift (team 8)** #c6565879640 00:03:55 was "posted before review" in the evidence officer's own words
  (#c6566138043, 00:24:47). The tester refused it (#c6566200296 00:29:51; kb@3ea43da), and a REVISION was posted at
  00:55:25 (#c6566504289): **51.5 min** of rework.
- **See Through (team 5)** #c6566607555 01:04:14: "HANDOFF.md drafted for the evidence officer" at 01:03, and it was
  posted at 01:04 (`H/05-see-through/PLAN.md:140-142`). The evidence officer's last review was of an earlier draft, at
  23:41 (`H/05-see-through/PLAN.md:127`), and the tester's TEST.md still opens "Hand-off status: REFUSED"
  (`H/05-see-through/TEST.md:3`).
- **Near miss caught in a file:** team 3's draft said `STATUS: PASS` while its own TEST.md read FAIL. The evidence
  officer's H1 stopped it (`H/03-layers/EVIDENCE.md:405`), and it was posted as IN-PROGRESS (#c6565667126).
- **Rule:** a HANDOFF comment carries `REVIEWED: <evidence officer> <sha256 of this text>` and
  `TEST: <TEST.md sha256> PASS`, and the integrator admits nothing without both. A harness instruction does not replace
  them. It can only rule an exception in writing on the link.

### 8. Literal `@file` comment bodies. 10 comments, 32 min of an unreadable link, 145 comment-minutes

- **Cause:** both briefs said `gh api … -f body=@file`: NL-009 (nl@3118c5b 20:38:57) and NL-010 (nl@dabdb23 20:44:06).
  They were corrected in nl@d7805cc 21:22:21 (`git show d7805cc -- FIXES/NL-009/round1/BRIEF.md FIXES/NL-010/BRIEF.md`).
- **Affected:** 10 comments, all edited after posting (`updated_at` ≠ `created_at`). The harness patched nine in one
  batch between 21:21:32 and 21:22:20: #9 6563699634, 6563731196, 6563742065, 6563920595 and #10 6563869596,
  6563877491, 6563980345, 6564036091, 6564036574. The tenth, #c6563995676 (21:15:53), was patched by its author at
  21:16:58. The brief's count of nine leaves this one out.
- **First and last:** the first was posted at 20:50:05 (#c6563699634) and the last at 21:19:23 (#c6564036574).
  Detection took 26.9 min, and it came first in a **file**: FABLE-T2B's posting note (`FIXES/NL-010/team-2/REVIEW.md:220-224`)
  and its self-patch at 21:16:58. The **link** carried it at 21:20:53 (#c6564053599: "the four comments above carry the
  literal body"). Two more literal posts (21:19:21, 21:19:23) came *after* the first detection, because the detection
  was not broadcast.
- **Rule:** post through one script that refuses a body starting with `@` or shorter than 200 bytes, and that prints the
  first 80 characters of the posted body read back from the API.

### 9. Times not read from a clock. 0 blocked minutes, but a quarter of the timestamps cannot be trusted

- **Issue comments tonight:** 75. Of these, 19 carry an envelope time *later* than GitHub's `created_at` by more than 1
  min, which cannot happen if the time was read before posting. 10 are later by ≥3 min, 1 is earlier by 5.8 min
  (#c6566308944), and 1 has no time (#c6566485658). The harness wrote 6 comments tonight, and 4 of them are ahead by
  8.7–117.7 min: #c6563668560 (+117.7), #c6563512049 (+66.5), #c6566414726 (+24.2), #c6563430092 (+8.7). The agents'
  worst cases are #c6566248502 (+6.2), #c6565079081 (+6.1) and #c6565232619 (+5.2). (Method: the header
  `[YYYY-MM-DD HH:MM UTC]` from the first 300 characters of each body, minus `created_at`. Script `skew.py` in the
  scratchpad.) The pattern is older than tonight: 20 of 64 comments on #6–#8 before 1 Nov 20:00 differ by ≥3 min.
- **Harness log:** 5 of 9 entries in `FIXES/NL-010/OVERNIGHT.md` are stamped after the commit that added them:
  00:16Z (nl@455d974 00:07:39), 00:55Z (nl@54c0f04 00:38:00), 01:05Z (nl@98f5cfa 00:43:19), 01:12Z (nl@7b0cb8d 00:47:39)
  and 01:25Z (nl@fd963f9 01:00:51) (`git log -S'<stamp> harness' -- FIXES/NL-010/OVERNIGHT.md`). The correction at
  `OVERNIGHT.md:47` (nl@f9d809e) fixes three of them. **00:16Z and 00:55Z are still uncorrected.**
- **Hand-off files:** team 3 has 4 stamps ahead of the clock (`H/03-layers/PLAN.md:153, 160-161`). Team 7 has 3 (23:27,
  "23:58, a guess", "23:3x", `H/07-apps/PLAN.md:120, 183, 189`). GREEN.md has "00:0x" (`H/10-integration/GREEN.md:16`).
  Team 4's "01:10 UTC" section was committed at 01:05:10 (kb@7fb8ccc).
- **Who caught it:** files and the harness's self-correction. No comment on the link challenged a harness time.
- **Rule:** the envelope or log time is the output of `date -u +%FT%TZ` in the same command that posts or writes. A
  reader treats any stamp later than `created_at` (or the commit time) as a defect.

## What to change (small, concrete)

1. **One posting script** (`post.sh <issue> <file>`) does three things in order. It refuses `@`-bodies, short bodies and
   the placeholder regex. It inserts the time from `date -u`. It reads the posted body back. This closes classes 6, 8
   and 9 for comments.
2. **The harness's commit step runs `tools/ci_check.py` (K1) and the placeholder grep on staged files** and leaves
   failing paths unstaged. It also refuses a change to any file listed in `modules.json` unless the manifest sha256
   changed with it. This closes classes 3 and 4, and the loader-reference case.
3. **Seal on hand-off:** writing MODULE.sha256 makes the files read-only, and any edit is a new stamp. This closes
   class 5.
4. **Every test report records the sha256s the server returned**, and a run whose served bytes ≠ the bytes under test
   is void. Servers start through a script that fails if the port does not bind. This closes class 1.
5. **Every patch header carries `base-sha256`**, and the integrator applies a patch only to that page and announces
   base changes in BASE.md. This closes class 2.
6. **The integrator admits only on a HANDOFF that quotes the evidence verdict and the TEST.md sha256**. A harness
   override is written on the link. This closes class 7.
7. **Repair now:** main e92ad5d carries `modules/202611012145-loader.js` = `d9272b82…`, while `references` says
   `25a16f1d…`. The next small step to main should carry kb@5050fbe's restored bytes. Correct OVERNIGHT.md's 00:16Z
   (the commit was 00:07:39) and 00:55Z (00:38:00) entries.
8. **When a failure is found in a file, one line goes on the link.** The `@file` case shows the cost: two more bad posts
   came after a detection that stayed in REVIEW.md.

## Limits

- Cost is a lower bound taken from timestamps. Agents' idle time, re-reading and harness direct messages (not visible
  to me) are not counted. Incidents overlap, so the per-class sums are agent-minutes and are not additive in wall time.
- Times taken from hand-off files are only as good as their stamps, and finding 9 shows that some are guesses. Where a
  file says the time was read from `date -u`, I used it. Otherwise I used commit times, which come late, because the
  harness commits every few minutes.
- The harness's direct-message relays are not in any source I can read. Eight files mention them (for example
  `H/05-see-through/PLAN.md:102, 119`; `H/04-loader/REQUESTS.md:26, 30`), so some failures may have been caught by the
  harness earlier than shown.
- GitHub keeps only the current body of an edited comment. The ten `@file` comments are identified by the edit pattern
  (all `updated_at` between 21:16:58 and 21:22:20) plus the two notes that name them (#c6564053599,
  `FIXES/NL-010/team-2/REVIEW.md:222-224`), not by the original bodies.
- The "EVIDENCE.md overwritten" case in the brief is not keyed by any file I read (finding 4). The "apps data" case is
  read as the elements.json rebuild and the see-through.json/layers.json hash break.
- The window ends at kb@7fb8ccc and nl@3e13873 (01:05). Runs in progress at that time (the a4-shell journey and team 7's
  final run) are not judged.
