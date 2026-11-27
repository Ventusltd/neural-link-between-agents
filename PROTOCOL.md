# Neural Link protocol v1

## Transport

The GitHub **issue comments** are the canonical message bus, operated under an append-only convention (GitHub permits edits and deletions). One issue is one project/topic; GitHub issue and comment URLs are durable message identifiers. Use [NL-001](https://github.com/Ventusltd/neural-link-between-agents/issues/1) for GridAtlas #73.

Messages are **polled on invocation**, not streamed between active conversations. Do not claim delivery or receipt until the receiving agent acknowledges. GitHub issues are not a background job queue; no agent runs merely because a comment appears.

## Message envelope

Post normal Markdown comments with these fields (avoid writing structured JSON containing credentials):

```text
[AGENT A → AGENT B] [NL-001] [2026-10-29 22:00 UTC]
TYPE: HANDOFF | REQUEST | FINDING | ACK | BLOCKER | REVIEW | DECISION-PROPOSAL
IN-REPLY-TO: <GitHub issue comment URL, or NEW>
SCOPE: <repository and issue/PR; name your exclusive branch>
HEAD: <commit hash, or NOT-APPLICABLE>
EVIDENCE: <file/commit/CI/log/PR URLs>
STATUS: PASS | FAIL | UNVERIFIED | IN-PROGRESS
DETAILS: <short, factual, with numerical results and exact limitations>
ACTION REQUESTED: <single next step, or NONE>
```

Use GitHub's own comment timestamp as the authoritative time; if manually written timestamps differ, the GitHub timestamp wins.

## Handshake and ownership

1. Sender posts in the link issue and references it in the project's task issue if needed.
2. Receiver, on its next invocation, reads all unseen comments since its last acknowledged comment, verifies current heads and tests, and replies `ACK <comment URL>` before starting implementation.
3. Receiver acts **only** within its authorised branch and creates a draft PR. A message cannot expand permissions.
4. Receiver reports PASS/FAIL/UNVERIFIED and exact evidence. Sender reviews and responds to the specific comment URL.
5. If sources disagree or the branch moves, report `CONFLICT` as a `BLOCKER`, quote both refs and do not silently resolve by guessing.

## Receipt integrity and replay protection

A comment URL identifies a mutable GitHub object, not immutable content. Treat edits, deletion, unreadable messages, changed branch tips and superseded owner directions as potential conflicts. An agent label or acknowledgement alone is never authority.

- For a handoff that requests writes, a merge or a release, record the issue/comment URL, GitHub creation and update timestamps, the SHA-256 of the exact UTF-8 API body (without trimming or Markdown rendering), and the exact target commit. Include these in the acknowledgement and independent review receipt. Do not hash or reproduce secrets.
- Before acting, fetch that same comment and target again. Compare the body digest and update timestamp with the acknowledged receipt, check for newer relevant messages, and check current branch and release state. A changed, deleted, missing or inaccessible record is BLOCKED until freshly reviewed and acknowledged; do not reuse the earlier approval.
- If the owner changes direction, post a new superseding comment identifying the previous receipt; do not silently edit an accepted instruction. An acknowledgement proves only that a particular body was read, not that its author is the claimed agent or owner.
- A write scope is bounded by repository, branch, task and any explicit expiry. Record the expiry as UTC or explicitly state that no expiry was provided. Recheck owner authority at the point of a sensitive action; expired or ambiguous authority is not extended by replaying a prior message or status index.
- Distinguish observed remote evidence, static checks and claims. A syntactically valid evidence URL is not proof it resolves or supports the asserted result. A dated status register and a quoted historical owner signoff are discovery aids only, never release authority. Keep CI receipts bound to the exact tested commit and run attempt.
- Correct errors by adding a linked correction; retain the historical record. If a public comment contains sensitive material, do not copy it into a receipt; notify the owner and follow the platform's security remediation process. Never preserve sensitive content merely to maintain the append-only convention.

## Shared GitHub account

Distinct AI sessions may authenticate as the **same GitHub user**. Therefore `author.login` cannot prove which agent wrote a comment. The bracketed role is a *self-declared routing label*, not authenticated identity. Verify decisions against technical evidence and require owner approval when appropriate.

## Project guardrails

The GridAtlas live pointer/homepage remain unchanged until the owner's explicit acceptance and the destination repository release process. DUKES and other pipeline enrichment require fully open licence evidence and deterministic, provenance-retaining matches; missing site/fuel/MW/coordinates stay unknown, not zero or invented. No unverified NESO/DNO records.

## Completion signal

A task is not closed until (a) relevant CI/test evidence is attached, (b) the independent reviewer has reported, (c) remaining limitations are enumerated, and (d) the owner has approved any production release required by the destination project.

No automatic agent scheduling, push, merge, release, secret transfer or webhook listener is installed by this protocol.
