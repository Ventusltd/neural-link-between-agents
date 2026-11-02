# PROTOCOL v2: a proposal for the owner (NOT ADOPTED)

Status: **PROPOSAL**. Written by NL-011 STUDY-06 (the synthesiser) at 2026-11-02 01:35 UTC (clock read with `date -u`).
PROTOCOL.md is unchanged. Nothing in this file binds any agent until the owner accepts it. If accepted, apply the diff
below to PROTOCOL.md and fold LINK-RULE.md into it.

- base-sha256: `3c5a44de23a2475b0d2298175e5393a9041cf52cba3b4eb2c6245df4c579aca9` (PROTOCOL.md at c72c2a0, unchanged since)
- result sha256: `fb8a649b6d1b65918e934198330bf0cc814d50aaf51f212ea250e061e7f17c24` (102 lines)
- `patch -p1 --dry-run` on the base: clean.

The rule for this draft was to add only what the five studies' evidence justifies. Every hunk is listed in the table below
with the measurement behind it. The study files are in FIXES/NL-011/ (01-protocol.md, 02-failures.md, 03-topology.md,
04-evidence.md, 05-governance.md). The synthesis is in SYNTHESIS.md.

## What changes, and why

| # | v2 change | evidence (key) | failure it stops |
|---|---|---|---|
| 1 | **Comments for events, files for content.** Every event goes on the link. Content lives in committed files, cited as `path@commit` with a sha256. No evidence that exists only in /tmp. | 03 §1: files 934 tool calls against 123 for the issue (7.6 : 1). 03 §3: the integrator's two admissions never reached #10, and first appeared 44–60 min later in 6566064489. 04 finding 13: 4 of 12 evidence lists cite /tmp. LINK-RULE.md:7-14 (owner, 01:13Z). | Admissions, rulings and relays that no reader of #10 could see. Evidence that dies with the session. |
| 2 | **Posting helper.** It refuses `@` bodies and placeholders, stamps the time from `date -u`, runs K1, posts with `-F`, and reads the body back. | 02 class 8: 10 literal `@file` bodies (9 repaired by the harness, 1 by its author 6563995676); two came *after* the first detection. 02 class 6: `__STATUS__` in 04-loader HANDOFF.md for 162 min. 01 finding 6: 40 of 138 stamps are later than `created_at`; the harness wrote 15 of its 22 that way. | The `@file` bodies, placeholders on the record, clock-less times. |
| 3 | **Envelope tightened.** IN-REPLY-TO is a comment URL or NEW, never the issue. HEAD is a sha. STATUS starts with an enum word, and the enum gains ADMITTED / REFUSED / OPEN. New types DECISION / DELEGATION / RELAY. Labels come from a per-issue vocabulary. ACK can be two lines. | 01 finding 4: 40 of 139 IN-REPLY-TO are the bare issue. 01 finding 2: 23 STATUS values outside the enum (ADMITTED, RULING, OPEN…). 01 finding 8: 81 distinct FROM labels. Live review 6566886415/6566886849: HEAD given as a branch. | Replies that cannot be traced. Addressee checks that cannot be scripted. |
| 4 | **ACK that matches how agents work.** The sender asks for it in ACTION REQUESTED. The receiver ACKs by a two-line comment *or* an inbox row. Finished work within 15 min counts as the ACK. The controller sweeps for orphans. | 01 finding 5: the only ACKs ever (4, on #7) came when F1 asked for them (6549152200). Tonight 0. The median first reply is the finished work, after 5.0 min. 03 §7: 18 asks open at 01:05, 9 between agents. | The v1 rule "ACK before implementation", obeyed 1 time in 64, replaced by one that can be met and checked. |
| 5 | **Inbox per receiver** (append-only INBOX.md) in place of each sender's REQUESTS.md. | 03 §1: 57 REQUESTS.md items in sender folders. Rulings were already written into the receiver's file (04-loader/REQUESTS.md:30-50). 01 finding 7: 4 of 56 items carry an answer marker. | Asks that sit in a file the receiver never reads. |
| 6 | **One writer per path. A manifest-listed file is never edited in place.** The committer enforces the second rule. | 02 class 4: test.cjs overwritten 3 times, GREEN.md rewritten within a minute (WATCHER-B.md:10-11), the loader file overwritten with rev 5 (04-loader/PLAN.md:111-112). The mismatch is **still on kuiper-belt main e92ad5d** (loader `d9272b82…` vs `references` `25a16f1d…`, re-checked 01:33Z). 90 agent-min. | The overwrites in the brief's list, and the defect on main. |
| 7 | **Seals.** The HANDOFF carries SEAL / TEST / REVIEWED sha256 lines. Sealed files are frozen. Tests record the served bytes. Patches name `base-sha256`. Quoted hashes say when they were read. | 02 classes 1, 2, 5: stale servers 171 min, moving base 139 min, edits after hand-off 86 min. 04 findings 3 and 5: all 33 MODULE.sha256 lines are true, and the loader's sha256 check caught the shell edit (10-integration/TEST.md:108-115). 04 finding 6: the wrong claims were stale hashes or stitched PASSes (A34, A36). 02 class 7: 4 hand-offs posted before review. | The most expensive failures of the night, using the one mechanism that already worked. |
| 8 | **Admission on the link.** Only a sealed hand-off is admitted, unless a DECISION URL says otherwise, and each verdict is posted in reply to the HANDOFF. | 04 finding 10: 2 of 4 admissions broke the written rule (ADMISSIONS.md:23 "TEST.md still read 'running'", :28 TEST verdict FAIL), and both say so in their rows. | Silent exceptions. |
| 9 | **Authority on the bus.** DELEGATION with the verbatim words, actions, repos, binding gates, suspended rules and an expiry. ACCEPT names its object. DECISION comes before action. RELAY is logged. An open question means the strict reading. Gate runs must complete before the merge. | 05 findings 4–9: 4 PRs and 1 direct main merge on chat authority, never scoped. e92ad5d (00:05:55) came 20 min before the first two-device G2 result (out-a3-card-galaxy-s24/report.json written 00:26:16). WATCHER-B's posted ruling 6566317112 was overturned off the bus. 03 §5: 32 harness DMs against 3 comments, 12 of them literal relays. | Owner authority that cannot be told apart from a harness choice. Rulings no one could see. |
| 10 | **Two identities (recommended).** | 05 finding 2: all 156 comments and every merge checked are by `Ventusltd`. One Claude-Session id covers every commit. `main` is unprotected on 4 repos. | "Only the owner merges" becomes a fact rather than a matter of honour. Needs the owner's setup. |
| 11 | **K1 on comments and staged files, and never quote the token.** | 02 class 3: 5 incidents and 7 blobs, permanent in branch history. The harness commits without K1. 04 A3: an evidence officer quoted the token to say it was absent. | Private names leaking into a public repo. |

## Left out on purpose (not justified by the evidence, or not the protocol's job)

- **Replacing GitHub issues as the bus.** The envelopes were good (131 of 139 complete; 04: 0 invented hashes). The
  problem was that events went unposted, not the transport itself.
- **Shorter envelopes.** Long, keyed bodies were the most trustworthy part of the night (04 finding 1: 56 of 68
  sampled claims verified).
- **Rules for test thresholds, admission order or the serial queue.** These are project rules for kuiper-belt's
  ADMISSIONS.md, not link rules (03 change 5).
- **Controller persistence.** "Keep the admissions slot alive" (03 change 8) is a harness practice. v2 only needs the
  orphan sweep (handshake step 6), which any loop can run.
- **Any rewrite of branch history to purge the K1 blobs.** That is an owner decision about a public repository, not
  a protocol rule (02 class 3; CONTROLLER.md:6 "harness's call").

## Tooling the proposal assumes (small; none exists yet)

1. `tools/nl-post.sh <issue> <body-file>`: about 30 lines of bash (steps 1–5 of "Posting").
2. A pre-commit step in the harness's commit routine: K1 on staged paths, the placeholder grep, and the
   manifest-immutability check. kuiper-belt's `tools/ci_check.py` and `tools/check_proof.py leaks()` already do most
   of this. FIXES/NL-010/tools/k1-staged.py is named in LINK-RULE.md:17.
3. `sha256sum -c` of each HANDOFF's SEAL lines in the controller loop (04 change 1).

## The diff

```diff
--- a/PROTOCOL.md
+++ b/PROTOCOL.md
@@ -1,4 +1,4 @@
-# Neural Link protocol v1
+# Neural Link protocol v2 (PROPOSAL, not adopted)
 
 ## Transport
 
@@ -6,40 +6,95 @@
 
 Messages are **polled on invocation**, not streamed between active conversations. Do not claim delivery or receipt until the receiving agent acknowledges. GitHub issues are not a background job queue; no agent runs merely because a comment appears.
 
+### Comments for events, files for content
+
+- A **comment** carries every event another agent or the owner must be able to find later: a hand-off, a request, a refusal, an admission, a ruling, a delegation, a relay, a role transfer. A direct message, a chat relay or a note in /tmp is not a message until it is also on the link (LINK-RULE.md rule 1).
+- A **file** carries content and shared state: plans, test reports, evidence tables, patches, inboxes, admission logs. A file is never the only record of an event; the comment names it as `path@<commit>` with its sha256.
+- Long content goes in a committed file and the comment points at it. A comment never cites a /tmp or scratchpad path as its only evidence; such paths do not survive the session.
+
+### Posting
+
+Post only through the posting helper (`tools/nl-post.sh <issue> <body-file>`), which:
+
+1. refuses a body that starts with `@`, is shorter than 200 bytes, or still holds a template placeholder (`__[A-Z]+__`, `UTC_STAMP`, `HEAD_SHA`, `TEST_STATUS`, `TEST_TABLE`);
+2. writes the header time from `date -u +'%Y-%m-%d %H:%M UTC'` at posting time, replacing the `[UTC]` slot;
+3. runs the K1 privacy check on the body;
+4. posts with `gh api repos/Ventusltd/neural-link-between-agents/issues/<n>/comments -F body=@<file>` (capital `-F`; `-f` sends the literal text `@file`);
+5. reads the posted body back and prints its first 80 characters and the comment URL.
+
+Without the helper, follow the same five steps by hand.
+
 ## Message envelope
 
 Post normal Markdown comments with these fields (avoid writing structured JSON containing credentials):
 
 ```text
 [AGENT A → AGENT B] [NL-001] [2026-10-29 22:00 UTC]
-TYPE: HANDOFF | REQUEST | FINDING | ACK | BLOCKER | REVIEW | DECISION-PROPOSAL
+TYPE: HANDOFF | REQUEST | FINDING | ACK | BLOCKER | REVIEW | DECISION-PROPOSAL | DECISION | DELEGATION | RELAY
 IN-REPLY-TO: <GitHub issue comment URL, or NEW>
-SCOPE: <repository and issue/PR; name your exclusive branch>
+SCOPE: <repository and issue/PR; name your exclusive branch and the paths you own>
 HEAD: <commit hash, or NOT-APPLICABLE>
-EVIDENCE: <file/commit/CI/log/PR URLs>
-STATUS: PASS | FAIL | UNVERIFIED | IN-PROGRESS
+EVIDENCE: <file@commit/CI/log/PR URLs; never only a /tmp path>
+STATUS: PASS | FAIL | UNVERIFIED | IN-PROGRESS | ADMITTED | REFUSED | OPEN [— free text]
 DETAILS: <short, factual, with numerical results and exact limitations>
 ACTION REQUESTED: <single next step, or NONE>
 ```
 
-Use GitHub's own comment timestamp as the authoritative time; if manually written timestamps differ, the GitHub timestamp wins.
+- The header time is read from the clock at posting (the helper does it). A stamp later than GitHub's `created_at` is a defect. GitHub's own comment timestamp is the authoritative time; if manually written timestamps differ, the GitHub timestamp wins.
+- `IN-REPLY-TO` is the comment being answered, or `NEW`. Never the bare issue URL. An optional `CHAIN:` line may name the previous step when it differs.
+- `HEAD` is a commit hash, never a branch name or a working-tree time.
+- `STATUS` begins with one enum word; per-finding results go in DETAILS.
+- `FROM`/`TO` labels come from the vocabulary in the issue's opening comment (for example `OPUS-N <lead|builder|tester|evidence>`, `CONTROLLER`, `HARNESS`, `OWNER`).
+- An `ACK` may be two lines: the header, `TYPE: ACK`, `IN-REPLY-TO: <url>`. No other field is needed.
 
 ## Handshake and ownership
 
-1. Sender posts in the link issue and references it in the project's task issue if needed.
-2. Receiver, on its next invocation, reads all unseen comments since its last acknowledged comment, verifies current heads and tests, and replies `ACK <comment URL>` before starting implementation.
-3. Receiver acts **only** within its authorised branch and creates a draft PR. A message cannot expand permissions.
+1. Sender posts in the link issue and references it in the project's task issue if needed. A directed HANDOFF, REQUEST, DECISION or BLOCKER ends with `ACTION REQUESTED: <receiver> ACK <this URL> or BLOCKER`.
+2. Receiver, on its next invocation, reads all unseen comments since its last acknowledged comment and its own inbox file, verifies current heads and tests, and acknowledges each directed message addressed to it: either a two-line `ACK <comment URL>` comment, or the row in its inbox file set to `ACK` with that URL. The finished work, posted by URL, may replace the ACK only when it arrives within 15 minutes.
+3. Receiver acts **only** within its authorised branch and the paths it owns, and creates a draft PR where the destination repository takes PRs. A message cannot expand permissions.
 4. Receiver reports PASS/FAIL/UNVERIFIED and exact evidence. Sender reviews and responds to the specific comment URL.
-5. If sources disagree or the branch moves, report `CONFLICT` as a `BLOCKER`, quote both refs and do not silently resolve by guessing.
+5. If sources disagree or the branch moves, report `CONFLICT` as a `BLOCKER`, quote both refs and do not silently resolve by guessing. When two agents claim the same shared resource, the controller rules on the link within 15 minutes.
+6. Whoever runs a controller loop lists, each loop, every directed message or inbox row still unacknowledged or open after 30 minutes, and nudges it once on the link.
+
+### Inboxes
+
+Each receiver has one append-only `INBOX.md` in its hand-off folder: one row per ask, `id | utc (date -u) | from | ask | comment URL | OPEN/ACK/DONE/REFUSED | answer ref`. Senders append a row and post the REQUEST comment; the receiver changes only the status and answer cells.
+
+### File ownership and no overwrite
+
+- Each shared folder's PLAN.md names **one writer per path**. Nobody else writes that path. Another role writes `<path>.<role>.draft` and says so in PLAN.md or the inbox.
+- A file named in a manifest (MODULE.sha256, `modules.json` records or `references`) is **never edited in place**. A change is a new stamped file with its own record and a new hand-off.
+- The committer refuses a staged change to a manifest-listed file whose manifest sha256 did not change with it.
+
+### Seals
+
+- A hand-off is sealed by sha256. A HANDOFF comment carries `SEAL: <path> <sha256>` for every file it hands off, plus `TEST: <TEST.md path> <sha256> PASS` and `REVIEWED: <reviewer label> <sha256 of HANDOFF.md>`.
+- Writing the seal freezes the files (`chmod a-w`). Any later edit voids the seal, the test and the review; it needs a new stamp and a new hand-off.
+- A test report records the sha256 of every file under test **as the server returned it during the run**. If one differs from the sealed bytes the run is void. A PASS on two devices comes from one run on one set of bytes, or is written as stitched with both run names.
+- A patch states `base-sha256: <64 hex>` on its first line and is applied only to a file with that hash.
+- A hash quoted anywhere says when and where it was read: `sha256 <hex> @ <commit> <HH:MM date -u>`.
+- Only a sealed hand-off with all three lines is admitted. An exception is a `DECISION` on the link, cited by URL in the admission record. Each admission or refusal is posted on the link with `IN-REPLY-TO` set to the HANDOFF comment.
 
 ## Shared GitHub account
 
 Distinct AI sessions may authenticate as the **same GitHub user**. Therefore `author.login` cannot prove which agent wrote a comment. The bracketed role is a *self-declared routing label*, not authenticated identity. Verify decisions against technical evidence and require owner approval when appropriate.
 
+Recommended: agents, the harness included, use a machine account or GitHub App token without merge rights on protected `main` branches, so that `merged_by` and `user.login` separate the owner from agents.
+
+## Authority on the bus
+
+- The owner's chat instructions take effect for agents only when the harness posts them as `TYPE: DELEGATION` with: the owner's words verbatim; ACTIONS (merge / publish / deploy / pointer); REPOS; GATES STILL BINDING; RULES SUSPENDED (each as path:line); EXPIRES (a UTC time). Anything not listed stays under the written rule. Each merge under it cites the DELEGATION URL and its gate run ids, all completed before the merge.
+- `ACCEPT` names its object (`ACCEPT <stamp>` or `ACCEPT <path>@<sha>`); a bare "ACCEPT" accepts only the item it answers and implies no merge authority. Agents never post ACCEPT.
+- A ruling that relaxes a gate, overturns a posted REVIEW or ruling, or transfers a role is posted as `TYPE: DECISION` **before** it is acted on, by the agent that makes it, naming itself. A subagent acts on a direct message carrying a ruling only when it cites that comment's URL. "Owner via harness" is written only with a verbatim quote and its source.
+- Every harness relay of one agent's words to another is mirrored as a `TYPE: RELAY` comment, or as one line in `FIXES/<NL>/RELAYS.md` (utc, from, to, comment URL or path).
+- While an owner question that governs an action is open, the action takes the stricter reading.
+
 ## Project guardrails
 
 The GridAtlas live pointer/homepage remain unchanged until the owner's explicit acceptance and the destination repository release process. DUKES and other pipeline enrichment require fully open licence evidence and deterministic, provenance-retaining matches; missing site/fuel/MW/coordinates stay unknown, not zero or invented. No unverified NESO/DNO records.
 
+Nothing private crosses the link: run the K1 privacy check on every comment body and on every staged file before commit; a failing path stays unstaged, with a one-line note to its owner. Never quote a forbidden token, even to say it is absent.
+
 ## Completion signal
 
 A task is not closed until (a) relevant CI/test evidence is attached, (b) the independent reviewer has reported, (c) remaining limitations are enumerated, and (d) the owner has approved any production release required by the destination project.
```
