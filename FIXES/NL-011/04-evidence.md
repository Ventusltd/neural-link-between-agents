# NL-011 study 04: evidence and truthfulness

STUDY-04, lens "evidence and truthfulness". Written 2026-11-02 01:05–01:30 UTC (clock read with `date -u` at 01:29).
Scope: claims made through the link on the night of 1–2 Nov: issues #9 and #10, FIXES/NL-009 and FIXES/NL-010, and
kuiper-belt `editions/202611012135/handoff/*/`. Short forms: `kb` = /home/user/estate/kuiper-belt (branch
edition/202611012135; I read it from 7fb8ccc, 01:05, to e927676, 01:16), `H/` = `kb/editions/202611012135/handoff/`,
`#10/<id>` = issue #10 comment id. My scripts and outputs are in
/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/ (`tools/keys.py`, `blobmap.tsv`,
`shaclaims.tsv`, `keys.json`, `drift-rerun.json`).

## Verdict

The hard evidence on the link is very good: none of the 201 sha256 values posted tonight was made up (200 equal real
bytes, 1 cannot be checked), all 33 MODULE.sha256 lines match the committed files, and 56 of 68 hand-sampled claims check
out (82 %), 9 are wrong (13 %) and 3 cannot be checked (4 %). The errors are not made-up numbers. They are stale
statements (a hash, a PASS or a base that was true earlier and was not updated), PASS verdicts put together from runs on
different bytes, one miscount, and times written without reading the clock. The harness erred most often (3 of 6 sampled
claims, all of them times), then leads (4 of 27). Evidence officers erred once in 13 and caught at least 20 defects
before posting, but a document edited after their review lost that protection.

## Findings

1. **Sample result: 56 verified, 9 wrong, 3 unverifiable of 68 claims** (Appendix A, one row per claim, keyed). I chose
   the claims to cover every role and every kind of claim: sha256 values, test counts, PASS verdicts, line keys, measured
   numbers, times. Each claim was checked against git objects, `/tmp/nl010-opus/*` reports or a re-run, never against
   another agent's prose. Big tables count as one claim each (A1, A2), so a large correct table does not raise the rate.

2. **sha256 census: 201 values from tonight, 200 verified, 0 wrong, 1 unverifiable.** The sources were every 64-hex
   value in `H/*/*.md`, `FIXES/NL-010/**/*.md` and the #9/#10 comments (`shaclaims.tsv`: 220 values; the 19 from #7/#8 on
   31 Oct are excluded). 124 equal the sha256 of a version of the named file committed on the edition branch
   (`blobmap.tsv`: 671 file versions from 96736f5..HEAD). I resolved 76 more against the named external commit:
   09-law's 17-row licence table, team 12's 32 file hashes at kb@aa04b3b, served-check's 9 homepage and door hashes at
   globalgrid2050-homepage@5a4abe41 and globalgrid2050@18aa446e, team 7's 6 source hashes, gridatlas@5ec7f62
   current.json:31/:641, and the patch result `db2ded89…` (Appendix A, A1, A2, A4, A6, A48–A50). The one unverifiable
   value is H/07-apps/TEST.md:11, a served modules.json that the test built on the fly. The census does not measure
   whether a hash was current, and that is where the hash errors were: H/07-apps/HANDOFF.md:8 gives apps.json
   `ba59b9bd…`, a real earlier version, while MODULE.sha256 and the file have been `027f6614…` since ee9c714 (A36).

3. **MODULE.sha256 census: 33 of 33 lines equal the committed file at HEAD e927676** (loop over
   `H/*/MODULE.sha256` + `H/04-loader/rev5/MODULE.sha256`). It also held at 7fb8ccc. The seal works whenever a team
   writes one. 06-file has a MODULE.sha256 but no TEST.md. 03-layers has none for its hand-off pass.

4. **Line-key census: 1,073 `repo@sha path:line` keys parsed, 709 with a quoted text.** 617 contain the quote at the
   keyed line. 91 were flagged by my heuristic. I re-read 18 of them by hand, and every one was a parser artefact: the
   next backtick was commentary, not the quote (for example `FIXES/NL-010/team-5/STEPS.md:73` names `:7`, `:11` and
   `:12`, and each one is right). Three real key defects were found:
   (a) `stars@cbca125 blocks/blocks.json:2`. The file is one line with no newline (`wc -l` = 0), so `:2` does not
   exist. The key appears in FIXES/NL-010/ROADMAP.md:550, FIXES/NL-010/team-4/STEPS.md:149, H/07-apps/PLAN.md:205 and
   in data/elements.json `register_note`. Team 7's evidence officer caught it (H/07-apps/EVIDENCE.md:289, defect b).
   (b) `gridatlas@5ec7f62 uk-lightning-overlay.js:7-8` (FIXES/NL-010/team-2/REVIEW.md:89, #10/6563995676). That commit
   holds 21 generations of the file, so the key cannot be resolved (`git ls-tree -r 5ec7f62 | grep -c
   uk-lightning-overlay` = 26 paths).
   (c) `ga@5ec7f62 menu-bar.js:1490` (H/05-see-through/EVIDENCE.md:115-117) is short for
   atlas/modules/202609031958-menu-bar.js. It resolves, but only by searching.

5. **Re-measurement reproduces the numbers whenever the inputs are pinned.** I re-ran:
   - rev 3 of the loader patch on index.html at a72c175. The result is 916 lines, sha256 `db2ded89…`, and
     `patch --dry-run` on 96736f5 gives "4 out of 16 hunks FAILED". Both match H/04-loader/EVIDENCE.md:213-215 (team 4
     evidence officer).
   - rev 2 on the camera base gives "1 out of 15 hunks FAILED", hunk 11 at fuzz 2, as #10/6564960147 says (OPUS-6
     builder).
   - The grep counts in ADMISSIONS.md row 1 match index.html `1b008b51…` (5 of 5).
   - The wafer re-sum is 13,344 rows, total 63,340,120,796, as in kuiper-law.js:36-38 and the 05 HANDOFF.
   - All 9 hook line numbers of #10/6564299733 match kb@96736f5 (OPUS-4 lead).
   - `see-through.json` at 934a4ca is 666,922 bytes and 666,920 characters, so line 1 is the "666,919-character line"
     of #10/6564872298.

   The one exception is shared state. `python3 tools/drift.py --heads data/drift.json` now writes `1640823a…`
   (118,433 B), not the recorded `388103129…` (118,553 B). The only difference is the reason string of the 22
   pipelinenews rows. The cause is /home/user/estate/pipelinenews, which another agent created at 00:55:59
   (`stat`), after drift.json was built. The tester's P1 PASS (H/08-drift/TEST.md, run 00:31–00:54) and the
   controller's E9 FAIL (#10/6566567995 item 4, 01:00) were both true when written.

6. **Wrong claims by role** (sample, Appendix A): harness 3 of 6 wrong, 1 unverifiable; lead 4 of 27; evidence officer
   1 of 13; tester 0 of 10 (2 unverifiable); controller 0 of 4; builder 0 of 2; Fable auditors and architects 0 of 5;
   1 wrong key shared by several roles (A41). The four lead errors:
   - a miscount: ADMISSIONS.md:14 says the base scored 12/16 on Galaxy S24, but report out-base5 says 13/16, with the
     three reds that the row itself names (A7);
   - a stale PASS: 08-drift HANDOFF "32 of 32", posted at 00:04, one minute after the shell it depended on was
     withdrawn; the tester measured 30/32 (#10/6566130521) (A26);
   - a PASS put together from two runs: 05 HANDOFF STATUS PASS uses run8 for Pixel 7 and run9 for Galaxy S24 (A34);
   - a stale hash: 07 HANDOFF apps.json (A36).

   The harness's three errors are times: #10/6563668560 is stamped 22:45Z but was posted 20:47 (+118 min);
   #10/6566414726 is stamped 01:12Z but was posted 00:47 (+24 min) and says "From 01:05Z" in the past tense; and three
   OVERNIGHT.md entries were future-dated. The harness corrected the OVERNIGHT.md entries itself (nl@f9d809e). The two
   issue comments were never edited (`updated_at` = `created_at`).

7. **Clock census, all 73 #9/#10 envelopes:** 62 within ±2 min of `created_at`, 10 off by 3 to 118 min, 1 without a
   minute (#10/6566485658, OPUS-1 lead, `[2026-11-02 UTC]`). 9 of the 10 are stamped later than the post. The two
   biggest are the harness's (+118, +24). OPUS-4 lead is off in 3 of its 5 posts (+5, +6, −6). Fable posts: 2 of 23 off
   (+3, +4: FABLE-T1A, FABLE-08).

8. **"PASS on both devices" held in one run for 5 of 6 PASS claims checked.**
   - 02-card: 41 PASS, both phones, one run (grep 41).
   - 01-shell rev 2: both phones PASS, Pixel 7 landscape A5 FAIL, disclosed. TEST.md's own verdict is "FAIL —
     HAND-OFF REFUSED".
   - 04-loader: 93/93 on each phone, in /tmp/nl010-opus/team-4/tester/out/full-rev4/report.json on page `1b008b51…`.
     H/04-loader/TEST.md has read "Status: running" from 22:14 to HEAD.
   - 08-drift: 49 PASS, 0 FAIL (34 rows on phones, 14 python, 1 files). The harness commit acaad83 calls this "49/49 on
     both phones".
   - The integrator's journeys G1/G2: 14/16 on each phone, reds only from the base.
   - The exception is 05-see-through. run8 (`report-run8-pixel7.json`) holds both phones, and Galaxy S24 failed `tap`
     in it. run9 (Galaxy only) served shell `1edf2e1a…` and file `013d6dda…`, while run8 served shell `4c0e8314…` and
     file `d8c236c0…`. The module bytes `87a88e48…` are the same in both runs. H/05-see-through/TEST.md:3 still reads
     "Hand-off status: REFUSED".

9. **Did the tests run on the bytes they name? Yes in every case I could check, but three records name bytes the run
   did not end on, or bytes nobody kept.**
   - H/07-apps/TEST.md ran on data from before the seal (apps.json `9ade18cf…`, elements.json `28b8b2df…`). This is
     disclosed only in the lead's PLAN.md:272-273.
   - The 23:07 run of team 2 tested `788256a9…`. The file was then changed in comment lines only
     (`git diff a72c175 febdd99`, lines 24-26), and the 23:33 run tested the final `e2baeaaa…`.
   - The 22:58 TEST.md of 01-shell (kb@6db1319) names test.cjs `1d68ccd5…`. No commit and no file under
     /tmp/nl010-opus/team-1 has that hash, so it cannot be checked.

10. **Admissions against the stated rule.** The admission rule is: HANDOFF plus a TEST.md reading PASS
    (H/10-integration/ADMISSIONS.md:3-5). Two of the four admissions did not meet it, and both say so in their rows.
    Row 1, loader + hello: "TEST.md still read 'running'". Row 4, shell rev 2: TEST.md verdict FAIL, admitted "on the
    harness's ruling". The truth was written down, but the rule was not followed.

11. **Unfilled templates on the record.** H/04-loader/HANDOFF.md:1,7 still carry `[__TIME__ UTC]` and
    `STATUS: __STATUS__`. H/07-apps/HANDOFF.md:1,5,7 still carry `[UTC_STAMP]`, `HEAD_SHA` and `TEST_STATUS`. Both
    teams' evidence officers flagged these (H/04-loader/EVIDENCE.md:414, H/07-apps/EVIDENCE.md:318), and both are still
    unfixed at HEAD. 01-shell's placeholders (H/01-shell/EVIDENCE.md:257) were fixed.

12. **Evidence officers lower the error rate, but only for the version they reviewed.**
    - Claims written by evidence officers were wrong 1 time in 13 (8 %). Lead and harness claims together were wrong 7
      times in 33 (21 %).
    - None of the 9 errors sits in a statement in the state an evidence officer passed. Four come from text written or
      edited without review or after it: A7 ADMISSIONS (not reviewed), A26 posted "before review"
      (#10/6566138043), A34, and A36 (edited at 00:46, after the officer's review at 00:37,
      H/07-apps/EVIDENCE.md:304-311).
    - Defects officers caught before posting:
      - team 4: six HANDOFF errors plus blocker B1 (H/04-loader/EVIDENCE.md:403-418; key re-check 199/199);
      - team 7: eight data defects a–h, all fixed (H/07-apps/EVIDENCE.md:285-298), plus four placeholders;
      - team 3: 14 RESOLVED rows;
      - team 6: 5 RESOLVED rows;
      - team 8: "PASS WITH CORRECTIONS" (#10/6566138043);
      - team 10's officer located the K1 token exactly (#10/6564872298; build script line 97 verified).
    - The officers' one error (A3) was self-inflicted. Team 12's officer quoted the forbidden token in order to report
      that it appears in 0 files, which put it in its own file. That turned ci_check red on the pushed branch
      (#10/6566545614), and the harness had to redact it (kb@93a5ae9).

13. **What cannot be checked and why.**
    - 4 of 12 evidence lists cite files under /tmp. Most of those files still exist; I used team 4's and team 10's
      reports. They will not survive a restart.
    - Harness claims about GitHub Actions runs (#10/6566064489: runs 41365403840 and 41364141297) cannot be reached from
      this sandbox. Team 13's served-check confirms them from logs.
    - WATCHER-B and the controller keep their evidence in a scratchpad shared by every agent of the session (the
      `journey/` folder in my own scratchpad). I verified WATCHER-B's 11 PASS / 7 FAIL there, and the controller's
      a4-shell 15/16.

## What to change (small, concrete)

1. **A hash in a HANDOFF line says when it was read**: `sha256 <hex> @ <commit or WT> <HH:MM date -u>`. Add a check
   (one `sha256sum -c` in ci_check, or the controller's loop) that fails when a HANDOFF hash differs from MODULE.sha256.
   This would have caught A36 and the stale data hashes in A37 / finding 9.
2. **One run, one set of bytes.** A PASS on both devices must come from one report whose manifest lists one sha per
   module. A PASS put together from several runs is written as "PASS (stitched: run8 P7, run9 S24; shell differs)".
   This fixes A34.
3. **Re-review after an edit.** Any edit to a reviewed HANDOFF/EVIDENCE/data file voids the officer's PASS until the
   officer re-signs with the new sha. A one-line `REVIEWED <sha256 of HANDOFF.md> <time>` at the foot is enough.
4. **The envelope time comes from `date -u`, pasted, never typed.** Add one check to the posting helper: refuse a header
   time more than 2 minutes from the clock. The harness's +118 and +24 comments should be edited now. The harness
   corrected OVERNIGHT.md but not the issue comments.
5. **Refuse to post a body that still holds `__[A-Z]+__`, `UTC_STAMP`, `HEAD_SHA` or `TEST_STATUS`.** One grep in the
   posting helper. This catches finding 11.
6. **The tester's verdict goes into TEST.md in the repository**, not only into /tmp. A loader "93/93" that exists only
   in /tmp/nl010-opus is a claim the link cannot show.
7. **Pin the environment of every reproducibility claim.** The estate clone list and its heads go into the record (the
   drift.json `heads` already does this, the reason strings do not). Agents do not create clones in
   /home/user/estate while a team's P1 is running.
8. **Evidence officers never quote a forbidden token, even inside a negative claim.** Write "the K1 tripwire token" and
   run `tools/ci_check.py` before handing the file to the harness.
9. **Keys name the full path.** `menu-bar.js:1490` and `uk-lightning-overlay.js:7` are not keys. Officers' key-check
   scripts (team 4's check_keys.py, 199/199) should reject a path that does not exist at the commit.

## Limits

- I chose the 68 sampled claims myself to cover all roles and claim types. They are not a random sample, so the role
  rates are rough estimates (n = 6 for the harness, 4 for the controller).
- "Verified" for a PASS means the cited report holds the stated result on the stated bytes. I did not re-run any
  Playwright test. The only things I re-ran were patch, grep, sha256sum, drift.py into my scratchpad, and
  tools/ci_check.py (RESULT: PASS, 738 files, at about 01:25). ci_check writes and deletes a temporary `.ci-*.mjs`
  in the kuiper-belt root.
- I ran `git fetch` in kuiper-belt and /home/user/gg-domain to resolve 18aa446e. This updated only remote-tracking refs
  (origin/edition/202611012135 → e927676, which the harness had already pushed). No working tree, local branch or
  file outside FIXES/NL-011/ was changed.
- My scratchpad is shared with the harness and other agents. I wrote `keys.json`, `blobmap.tsv` and `shaclaims.tsv`
  there and did not check whether files of those names existed before.
- The line-key census marks a key as matching when the quoted text appears in the keyed line range. Paraphrased keys
  (no backticked quote, 353) were not checked.
- Claims on #6–#8 (31 Oct) are outside "tonight" and were not sampled.

## Appendix A: the 68 sampled claims

V = verified, W = wrong, U = unverifiable. Role is the author's role as stated in the envelope or the file header.

| # | claim (key) | role | verdict | how checked |
|---|---|---|---|---|
| A1 | 17 licence files: bytes, git blob, sha256 (H/09-law/EVIDENCE.md:106-125) | evidence officer | V | `git rev-parse`/`cat-file`, 17/17 |
| A2 | 27 file hashes + pointer/README of see-through/202611020012 at kb@aa04b3b (H/12-see-through-reader/EVIDENCE.md:19-25,170-196) | evidence officer | V | 29/29 at aa04b3b. kuiper-law.js changed later (5050fbe, comment line 39), after the pin |
| A3 | "grep … [token] … 0 files" (H/12-see-through-reader/EVIDENCE.md §8 before kb@93a5ae9) | evidence officer | W | writing the token made it 1 file; ci_check K1 FAIL (#10/6566545614) |
| A4 | rev 3 patch on 390b15ae → 916 lines, `db2ded89…` (H/04-loader/EVIDENCE.md:213-215) | evidence officer | V | reproduced |
| A5 | rev 3 on 96736f5: 4 of 16 hunks FAILED (same :213) | evidence officer | V | `patch --dry-run` |
| A6 | gridatlas@5ec7f62 atlas/current.json:31, :641 sha values (H/04-loader/EVIDENCE.md:34,41) | evidence officer | V | `git show` |
| A7 | base journey "Galaxy S24 12/16" (H/10-integration/ADMISSIONS.md:14) | lead (integrator) | W | out-base5/report.json: 13 passed, 3 failed |
| A8 | base journey "Pixel 7 14/16" (same row) | lead (integrator) | V | report |
| A9 | grep counts keys-min.json 2, edBand 4, ED_MINBAND = 96 1, content-visibility:auto 1, "EDITION 2 ·" 0 on `1b008b51` (ADMISSIONS.md row 1) | lead (integrator) | V | grep on blob at 38ed53c |
| A10 | G1: P7 14/16, S24 14/16 (H/10-integration/GREEN.md:11) | lead (integrator) | V | out-a1-loader-* reports |
| A11 | G2: P7 14/16, S24 14/16 (GREEN.md:12) | lead (integrator) | V | out-a3-card-* reports |
| A12 | a2-shell reds per device (ADMISSIONS.md row 2) | lead (integrator) | V | out-a2-shell-* reports |
| A13 | shell edited after hand-off, `352c20c6…` ≠ `eeea4581…` (row 2) | lead (integrator) | V | module at 0cd7910 = 352c20c6, MODULE.sha256 unchanged since 6db1319 |
| A14 | `788256a9…` → `e2baeaaa…` is comment-only, lines 24-26 (H/02-card/HANDOFF.md:53-55) | lead | V | `git diff a72c175 febdd99` |
| A15 | 41 PASS rows, 0 FAIL (H/02-card/TEST.md) | tester | V | grep, all three versions |
| A16 | 344 placed bodies (02-card TEST/HANDOFF) | tester | V | keys.json summary on_wafer 344 |
| A17 | test.cjs `1d68ccd5…` (H/01-shell/TEST.md at kb@6db1319) | tester | U | no commit and no /tmp file has the hash |
| A18 | test.cjs `8bfa8140…` (01-shell TEST.md at 2e4afb0) | tester | V | = committed test.cjs at a72c175 |
| A19 | module `1edf2e1a…` 45,402 B, test.cjs `ed5facac…` (01-shell TEST.md at HEAD) | tester | V | committed 507df4f / af4827e, unchanged after |
| A20 | "PASS on Pixel 7 and Galaxy S24; one disclosed FAIL landscape A5" (H/01-shell/HANDOFF.md:7) | lead | V | TEST.md cells. TEST verdict reads FAIL |
| A21 | shell churn `352c20c6 → 4c0e8314 → 6fa6d5c0 → 1edf2e1a` (GREEN.md controller note) | controller (WATCHER-B) | V | 3 in git; 4c0e8314 in report-run8 manifest |
| A22 | w3: 11 PASS / 7 FAIL, 1 page error (#10/6566247657) | controller (WATCHER-B) | V | scratchpad journey/out-w3-pixel-7/report.json |
| A23 | loader overwritten with rev 5 `d9272b82…`, restored to `25a16f1d…` from b8e7c74 (#10/6566567995 item 2) | controller (Opus) | V | blobmap; file at HEAD = 25a16f1d |
| A24 | drift.py recomputes `1640823a7173`, 118,433 vs 118,553 (#10/6566567995 item 4) | controller (Opus) | V | reproduced |
| A25 | P1 two runs = data/drift.json `388103…` (H/08-drift/TEST.md) | tester | V | true for 00:31–00:54. Non-reproducible after 00:55:59 (finding 5) |
| A26 | STATUS PASS "32 of 32 on Pixel 7 and Galaxy S24" (H/08-drift/HANDOFF.md:7, #10/6565879640, 00:04) | lead | W | depended on the shell withdrawn at 00:03. Tester 30/32 (#10/6566130521) |
| A27 | the tester's fix is two lines (08-drift REVISION, #10/6566504289) | lead | V | `git diff 0cd7910 7966a47`: +2 |
| A28 | RESULT PASS 49 of 49 (same) | lead | V | TEST.md at acaad83: 49 PASS, 0 FAIL |
| A29 | "drift module revision (49/49 on both phones)" (kb@acaad83 message) | harness | V | all 49 pass. 34 rows are phone rows |
| A30 | 309/7/2/0/28, share 309/318, 21 of 22 heads (08-drift HANDOFF) | lead | V | data/drift.json summary |
| A31 | pipelinenews "no clone in the estate" (drift.json) | lead | V | estate clone created 00:55:59 (`stat`) |
| A32 | 93/93 PASS on each phone on page `1b008b51…` (H/04-loader/HANDOFF.md:38) | lead | V | tester report full-rev4 |
| A33 | "team 4's TEST.md still read 'running' at admission" (ADMISSIONS.md row 1) | lead (integrator) | V | TEST.md at 1a9505d…HEAD |
| A34 | STATUS PASS, run8 P7 + run9 S24 (H/05-see-through/HANDOFF.md:7, #10/6566607555) | lead | W | combined from two runs. S24 failed `tap` in run8. Shell/file bytes differ. TEST.md:3 REFUSED |
| A35 | module `87a88e48…` 26,000 B, data `44095071…` 666,940 B (05 HANDOFF:5) | lead | V | blobmap and MODULE.sha256 |
| A36 | apps.json `ba59b9bd…a334` (H/07-apps/HANDOFF.md:8) | lead | W | file and MODULE.sha256 = `027f6614…` since ee9c714 |
| A37 | tested apps.json `9ade18cf…`, elements `28b8b2df…` (H/07-apps/TEST.md:13-14) | tester | V | true of the run (versions db9a3f0/0cd7910). Pre-seal |
| A38 | apps.json 34 rows: 7 block + 25 homepage + 2 issued (07 HANDOFF) | lead | V | data/apps.json |
| A39 | elements counts 244 / 221 / 23 (H/07-apps/EVIDENCE.md:125) | evidence officer | V | data/elements.json |
| A40 | stars@cbca125 blocks/graph.json blob `6d361d33…`, sha `72349730…` (07 EVIDENCE:170) | evidence officer | V | `git rev-parse`, sha256sum |
| A41 | `stars@cbca125 blocks/blocks.json:2` (ROADMAP.md:550, team-4/STEPS.md:149, 07 PLAN.md:205) | Fable architect / roadmap / Opus 7 | W | file is one line. Caught by evidence officer 7 |
| A42 | live_register_source sha `07675d74…` (data/elements.json) | builder | V | sha256 at cbca125 |
| A43 | kuiper-belt main e92ad5d: order [hello, line-card], index `418ae14c…`, pointer on Edition 4 (#10/6566064489) | harness | V | `git show e92ad5d:` |
| A44 | header 01:12Z; "From 01:05Z all agents are Opus" (#10/6566414726) | harness | W | posted 00:47:47, never edited |
| A45 | header 22:45Z (#10/6563668560) | harness | W | posted 20:47:20 |
| A46 | OVERNIGHT.md entries 01:05Z, 01:12Z, 01:25Z | harness | W | self-corrected, nl@f9d809e |
| A47 | ci_check PASS on main, Actions runs 41365403840 / 41364141297 (#10/6566064489) | harness | U | Actions not reachable from here |
| A48 | 7 homepage file hashes at 5a4abe41 (FIXES/NL-010/served-check.md:41-47) | lead (team 13) | V | `git show` + sha256sum |
| A49 | door page `2f046fd8…` 1286 B, pin 5a4abe41 at 18aa446e (served-check.md:25,31) | lead (team 13) | V | gg-domain |
| A50 | e92ad5d blobs eff31e6c (84,309 B) and cf2d63bf (466 B) (served-check.md:57-58) | lead (team 13) | V | `git rev-parse` |
| A51 | 28 hooks: 9 line keys at kb@96736f5, "team-2 wrote :126" correction (#10/6564299733) | lead | V | sed on the blob |
| A52 | K1 token on build script :97 ('provenance'); 666,919-char line; file in 2c87ba4 (#10/6564872298) | evidence officer | V | `git show 934a4ca:` |
| A53 | see-through.json rebuilt: 666,945 B, `87d5db35…` (#10/6564873869) | lead | V | blob at a72c175 |
| A54 | K1 FAIL names see-through.json and its build script (#10/6564796205) | tester | V | token present at :97 (A52) |
| A55 | rev 2 patch: "1 out of 15 hunks FAILED", hunk 11 fuzz 2 (#10/6564960147) | builder | V | reproduced on a72c175 |
| A56 | gridatlas@5ec7f62 index.html:2 redirect; sha256sums.txt:18 `87a3aaf4…` (FIXES/NL-010/team-1/EVIDENCE.md:35,48) | Fable (T1B) | V | `git show` |
| A57 | kb@018b46a editions/index.html:12 `location.replace(…)` (team-2/EVIDENCE.md:359) | Fable (T2B) | V | `git show` |
| A58 | engine walk at kb@018b46a editions/202611012027/index.html:203-208 (team-3/STEPS.md:161) | Fable (T3A) | V | `git show` |
| A59 | edition_keys.py:2-14 "commit → wafer row" (team-4/EVIDENCE.md:271) | Fable (T4B) | V | line 8 |
| A60 | kb@b9901d4 cosmos/wafer-meta.json:4 = 63,363,988,142 (H/12-see-through-reader/EVIDENCE.md:288) | evidence officer | V | `git show` |
| A61 | keys.json 1,709,129, wafer.tsv 535,037, index.html 61,653, repos.tsv 2,467 B (FIXES/NL-009/round1/07-perf.md:36) | Fable (FABLE-07) | V | raw sizes exact. My gzip sizes differ by about 10 B (header) |
| A62 | SPACE 63,340,120,796 over 13,344 rows (kuiper-law.js:36-38; 05 HANDOFF) | lead | V | awk re-sum at 96736f5 |
| A63 | layers module `79167b55…` 52,576 B (#10/6565667126) | lead | V | blob at 2662a4f |
| A64 | layers keyed at `90ab25e2…` 52,894 B (H/03-layers/EVIDENCE.md:187) | evidence officer | V | blob at b8e7c74. Stale: HEAD module is `4f9c49c7…` |
| A65 | file.js `3ae05df7…` (67aa0c0) and `d8c236c0…` (febdd99) (H/06-file/EVIDENCE.md:13,18) | evidence officer | V | blobmap |
| A66 | modules.json loader 25a16f vs file d9272b at 00:55 (H/10-integration/EVIDENCE.md:67) | evidence officer | V | blobmap |
| A67 | ci_check FAIL K1 on team 12 EVIDENCE.md at 00:55 (#10/6566545614) | tester | V | token in the blob before 93a5ae9 |
| A68 | "ci_check was RESULT: PASS at 00:20 UTC (705 tracked files)" (same) | tester | U | working-tree run, no record |

Totals: V 56, W 9, U 3. By role (V/W/U):
- lead 23/4/0 (27, including the integrator and teams 11/13);
- tester 8/0/2;
- evidence officer 12/1/0;
- controller 4/0/0;
- builder 2/0/0;
- harness 2/3/1;
- Fable 5/0/0;
- shared wrong key 0/1/0.
