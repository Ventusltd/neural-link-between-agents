# NL-011 synthesis: is the neural link working well between agents?

Written by NL-011 STUDY-06 (synthesiser). Clock read with `date -u`: started 01:05 UTC, written 01:36 UTC on 2 Nov 2026.
Inputs: studies 01-protocol, 02-failures, 03-topology, 04-evidence and 05-governance, all present by the 01:32:27 poll
(none missing). I also took my own measurements before the studies landed (PROTOCOL.md, AGENTS.md, OVERNIGHT.md, the
issue #1–#10 comments, kuiper-belt handoff/10-integration). My scripts are in
`/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/nl011/` (`skew.py`, `refs.py`).

## The answer, in five sentences

1. Only in part. The link is a good **record**: 131 of 139 envelopes are complete, and of 201 sha256 values posted tonight 200 match real bytes, 1 cannot be checked and none was made up. But it did not work as a **channel between agents**.
2. Agents posted to issue #10 and seldom answered each other there. Tonight there were 0 ACKs, 3 of 27 directed comments were answered by comment id, and 18 asks were still open at 01:05. Content travelled through shared hand-off files (about 7.6 file touches for each issue touch). Attention travelled through 32 harness direct messages, and one of those came just before every answer faster than 5 minutes.
3. The costly failures, about 754 agent-minutes, were about **which bytes** a claim meant, not about lost messages. Tests ran on stale servers, patches were cut against a page that kept moving, files were edited after their seal or overwritten by agents that did not own them, and K1 tokens were committed blind. Wherever a sha256 seal existed, it caught the problem.
4. Authority was the weakest layer. The ACCEPT rule held without exception. But merges, and two relaxed gates, went ahead on chat authority or on harness rulings that never reached the link, and the next step (moving the pointer) now has three written records that disagree.
5. Since the owner's 01:13Z rule that the link is the medium of exchange, the harness has posted its rulings on the link and corrected its own timestamps within minutes of these studies. So what is needed is a small protocol v2 with mechanical checks (seals, one writer per path, a posting helper, a commit gate, rulings on the bus), not a new system.

## How the five studies weigh against each other

### Where all five agree (strongest findings)

- **Well-formed but one-way.** Envelope shape: 131/139 complete (01 finding 1). Directed comments answered by id: 3 of 27
  (03 §3). ACK: 4 comments ever, all on #7 on 31 Oct, all answering one message whose sender asked for them (01 finding 5;
  03 §3; 05 finding 13). My own count matches: `TYPE: ACK` appears 4 times on #7 and 0 times on #8, #9 and #10.
- **Seals work where they exist.** All 33 MODULE.sha256 lines equal the committed bytes (04 finding 3). The loader
  refused a shell edited after hand-off (`10-integration/TEST.md:108-115`; 02 class 5). The controller found and
  restored the overwritten loader by hash (6566567995 item 2). Every refusal between agents names a hash, a count or a
  measurement (05 finding 11). The failures came where seals were missing: servers, patch bases, data files, and
  HANDOFF text edited after review (02 classes 1, 2, 5, 7; 04 finding 12).
- **The harness is the hub, and also the least careful sender.** 32 DMs against 3 comments in the Opus phase (03 §5). It
  wrote 15 of its 22 stamps after posting (01 finding 6), and it got 3 of 6 sampled claims wrong, all of them times (04
  finding 6). It made its rulings off the bus: "rev 5 optional", E6/E3, and keeping the K1 blob in history (03 §5;
  05 finding 8). It also commits blind, without K1 (02 class 3).

### Where they seem to disagree, and how I resolve it

1. **"The evidence is very good" (04) against "754 agent-minutes lost" (02).** Both are true, because they measure
   different things. 04 measures whether a value was *true when written*: 0 invented hashes, and 82 % of 68 sampled
   claims verified. 02 measures whether it was *still current, and about the right bytes*. Every one of 04's nine wrong
   claims is a stale statement or a stitched run (A26, A34, A36), or a time (A44–A46). None is a fabrication. **Resolution:**
   the agents are truthful but have no shared notion of currency. That points to seals with read-times (v2 hunk 7), not
   to more review.
2. **The `@file` count: the brief says 9, study 01 says nine, study 02 says 10.** The issue data supports 10. Nine
   comments were edited in one batch between 21:21:32 and 21:22:20 (my own `updated_at` listing agrees: 3 on #9 at
   21:21:32–34, 1 on #9 at 21:22:20, 5 on #10 at 21:21:35–40). The tenth, 6563995676, was edited by its author 65 s after
   posting (21:15:53 → 21:16:58), and FIXES/NL-010/team-2/REVIEW.md:220-224 names it. **Resolution: 10 literal bodies, 9 repaired by
   the harness.**
3. **Clock drift: 40 of 138 (01), 19 of 75 (02), 10 of 73 (04), 32 of 138 (my count).** The windows and thresholds
   differ: 01 counts ≥1 min later than `created_at` on #6–#10; 02 counts >1 min, tonight only; 04 counts ≥3 min on #9/#10;
   mine counts >2 min. They agree on the shape. About a quarter to a third of self-stamped times are later than the post,
   so they cannot have been read from a clock. The harness has the largest offsets: +117.7, +66.5 and +24.2 min.
   **Resolution:** report the shape and the harness outliers, not one headline number. Since 01:32 the two worst harness comments
   carry an in-body correction (6563668560 and 6566414726 now read "time corrected…", `updated_at` ≠ `created_at`), and
   OVERNIGHT.md:47-48 corrects five log stamps. The fix is mechanical (v2 "Posting" step 2).
4. **Merge before the gate: 41 min (05) against "GREEN.md disagrees with TEST.md" (live review 6566886415).** These are two
   different runs. The integrator's a3-card journey ran both phones at once and finished at 00:23:21 (Pixel 7) and
   00:26:16 (Galaxy S24): `stat` of `/tmp/nl010-opus/team-10/lead/journey/out-a3-card-*/report.json`. That is GREEN.md:12's
   "00:02–00:26". The team 10 tester's Run 3 ran the phones in turn and finished at 00:46:59 (TEST.md:119-123), which is the
   run 05 used. **Resolution:** GREEN.md and TEST.md are both right. e92ad5d (00:05:55) came **20 min** before the first
   two-device result and 41 min before the second. Either way the written R1 gate (OVERNIGHT.md:15) was not met at merge
   time. Both results later came out green, so no harm reached main through this gap.
5. **"Files were the real bus" (03) against LINK-RULE.md rule 1, "every message goes on the link".** 03 measured
   934 file tool calls against 123 issue calls. The owner's 01:13Z rule says a DM or /tmp note is not a message until it
   is on the link. These do not conflict, once events are separated from content. Files beat comments for content that
   changes (plans, test tables, inboxes, admission logs): they are read instantly on a shared tree and diffed by git.
   Comments beat files for events (a hand-off, a refusal, a ruling, a relay): they are durable, timestamped by GitHub, and
   visible to a new session. **Resolution:** v2 hunk 1. Every event is a comment that names `path@commit` with a sha256, and
   no event lives only in a file or a DM.
6. **"EVIDENCE.md was overwritten" (brief) against "UNVERIFIED; careful takeovers" (02 finding 4).** No study found a
   destructive EVIDENCE.md overwrite. Three takeovers were announced in the files (08-drift, 09-law, 06-file). The overwrites
   that are keyed are test.cjs ×3, GREEN.md, and the loader file. **Resolution:** I treat the EVIDENCE.md case as unverified.
   The class is still real and still costly: 90 min, plus the defect on main.
7. **Owner questions: "agents left them open" (05 finding 14) against "18 orphans" (03 §7).** These are compatible. 9 of
   the 18 open asks are addressed to the owner. Agents correctly refused to guess (Q1 licence, Q6 merge authority), but
   nothing on the link collects them. **Resolution:** keep the refusal to guess, and add the orphan sweep (v2 handshake
   step 6). LEDGER.md, which another NL-011 agent now keeps, is that sweep in practice.

### What changed during the study (01:05 → 01:36)

This is evidence that the loop of finding, posting and fixing works when findings are written to the link:

- LINK-RULE.md was committed at d6d5b9a 01:13:42 (owner's rule).
- The harness posted its POINTER-READY ruling on the link as a DECISION-PROPOSAL (6566812411, 01:20:46). Under v1 practice
  this would have been a DM.
- The live reviewer (NL-011 LINK-12) flagged three harness envelopes within 7 minutes (6566886071, 6566886415, 6566886849):
  a bare-issue IN-REPLY-TO, branch names in HEAD, and a stamp +2.2 min later than the post.
- The harness corrected its two worst comment stamps and its log after study 04 (nl@5f9e71f 01:32:53), and logged the
  loader defect on main (nl@70d939d).
- Still open: kuiper-belt main e92ad5d carries `modules/202611012145-loader.js` = `d9272b82421d`, while `modules.json`
  `references` says `25a16f1d3c3f…`. I re-checked this at 01:33 with `git show origin/main:… | sha256sum`.

## The ten most valuable changes, ranked

The ranking weighs measured cost × how often it happens × how cheap the fix is. Changes 1–9 are written into
PROTOCOL-v2-proposal.md. Change 10 is outside the protocol.

1. **Seal every claim to its bytes.** A HANDOFF carries `SEAL`/`TEST`/`REVIEWED` sha256 lines. Sealed files are frozen. Test
   reports record the bytes *as served*. Patches name `base-sha256`. Quoted hashes say when they were read. This stops 02
   classes 1, 2, 5 and 7 (171 + 139 + 86 + 52 agent-min) and 04's stale and stitched claims, using the one mechanism that
   already worked every time it was present (04 finding 3).
2. **Mechanical gates at the two exits: posting and committing.** `nl-post.sh` refuses `@` bodies and placeholders,
   stamps the time from `date -u`, runs K1, posts with `-F`, and reads the body back. The harness's commit step runs K1,
   the placeholder grep and the manifest-immutability check on staged paths. This closes 02 classes 3, 6, 8 and 9, and the
   loader-on-main case. The K1 blobs are the most serious harm of the night, because 7 of them are permanent in public
   branch history (02 class 3).
3. **Rulings, relays, delegations and admissions go on the bus before anyone acts on them** (DECISION / RELAY / DELEGATION
   types; ACCEPT names its object; an open question means the strict reading; gate runs finish before the merge). This stops
   the invisible overrides (05 finding 8; 03 §5). It also forces the owner to settle the live R2 conflict before the
   pointer moves: OVERNIGHT.md:16 and GREEN.md:18 against ROADMAP.md:694-697 and LAW.md:141-148 (05, "Live conflict").
4. **One writer per path, and no edit in place of a manifest-listed file** (drafts go to `<path>.<role>.draft`). This stops
   02 class 4 and keeps the GREEN.md, test.cjs and loader collisions from recurring.
5. **An ACK that agents will actually give.** The sender asks for it in ACTION REQUESTED. The receiver ACKs by a two-line
   comment or an inbox row, and finished work within 15 min counts. Asking produced the only 4 ACKs ever (01 finding 5).
   v1's "ACK before implementation" was met 1 time in 64.
6. **One INBOX.md per receiver, plus an orphan sweep every controller loop.** This replaces sender-side REQUESTS.md
   (57 items, 4 marked answered; 01 finding 7; 03 §1) and surfaces the 18 asks open at 01:05 (03 §7).
7. **Admission verdicts on the link, in reply to the HANDOFF, and only on a sealed hand-off unless a DECISION URL says
   otherwise.** Two admissions reached #10 44–60 min late, through the harness (03 §3), and 2 of 4 admissions broke the
   written rule (04 finding 10).
8. **Two identities, with branch protection on `main`.** This is the only change that needs owner setup. It makes
   `merged_by` and `user.login` mean something (05 finding 2: 156 of 156 comments and every merge are by one login,
   under one session id, on 4 unprotected `main` branches).
9. **Tighten the envelope where it was ambiguous.** IN-REPLY-TO is a comment URL or NEW. HEAD is a sha. STATUS
   starts with an enum word, with ADMITTED, REFUSED and OPEN added. FROM/TO labels come from a per-issue vocabulary. No
   evidence that exists only in /tmp. (01 findings 2, 4, 8; 04 finding 13; live reviews.)
10. **Repair now (outside the protocol):** carry the restored loader bytes (kb@5050fbe, `25a16f1d…`) in the next small
    step to kuiper-belt main. Ask the owner whether to purge the 7 K1 blobs from edition-branch history. Answer the open
    owner questions that gate actions: NL-008 Q4, ROADMAP Q6, and who moves the pointer.

## Limits

- I synthesise. Apart from the checks named above (comment counts, drift, the `@file` edit pattern, the G2 report times,
  the loader hash on main, LINK-RULE.md and the post-01:05 comments), every number comes from the five studies and
  inherits their limits. In particular, 02's costs are lower bounds and add up to agent-minutes, not wall time. 04's
  sample is chosen, not random. 03's channel counts are keyword matches over one session's transcripts.
- The harness's direct messages are seen only through 03's reading of the harness transcript. I did not read them myself.
- Conflict of interest: like studies 01–05, this synthesis runs under the harness session whose conduct it assesses
  (05 finding 2; OVERNIGHT.md:36 names the same session id).
- The window for the findings is 31 Oct to 01:05Z on 2 Nov. The section "What changed during the study" covers
  01:05–01:36Z only, and only partly.
