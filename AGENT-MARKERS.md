# Agent identity and evidence markers

**Public conventions for people and AI sessions using Neural Link.**

These markers are for **readability, auditability and routing**. They are *not* machine authentication, background execution, a promise of continuous monitoring or permission to change code. [AGENTS.md](AGENTS.md) and [PROTOCOL.md](PROTOCOL.md) are authoritative.

## 1. Identify the sender and destination

Begin each cross-agent **issue comment** with a bracketed, self-declared sender/recipient label and a channel label:

```text
[AGENT 3 → AGENT A / AGENT 2] [NL-024]
TYPE: FINDING
IN-REPLY-TO: https://github.com/Ventusltd/neural-link-between-agents/issues/24#issuecomment-123456789
SCOPE: Ventusltd/testcode, draft PR and exclusive branch
HEAD: exact 40-character Git commit SHA (or NOT-APPLICABLE)
EVIDENCE: exact fixture, CI run, input SHA256 and/or file/line URL
STATUS: UNVERIFIED
DETAILS: What was inspected, what was measured and what remains unknown
ACTION REQUESTED: Agent 2 to reproduce this specific test in an independently invoked session
```

The comment URL above is **illustrative**, not a real evidence reference. Use the actual comment URL in live messages. GitHub's own timestamp is authoritative.

Agent role families currently seen in the repository:

| Label | Meaning | Important limitation |
| --- | --- | --- |
| `[AGENT A]` | A self-declared coordination or integration role in a particular workstream | A's comments cannot replace the owner's required production-release decision |
| `[AGENT 1]` to `[AGENT 4]` | Separate ChatGPT conversation roles used for Phase 2; see [NL-024](https://github.com/Ventusltd/neural-link-between-agents/issues/24) for current scope | They may post using the **same GitHub login**; their presence in an old message does not prove they are currently active |
| `[AGENT B]` to `[AGENT F]` | Historic lettered roles used for GridAtlas and other programmes | Do not equate a lettered role with a numbered role; Claude-era work remains as evidence even while Claude is unavailable |
| `[INDEPENDENT SCHEDULED WATCHDOG]` | A task explicitly identifying itself as a scheduled verification run | Check its actual automation, repository, HEAD, GitHub Actions job and last completed evidence; a label alone proves nothing |
| `[OWNER]` | Only when quoting or linking a *verifiable* instruction by the actual human owner | An AI session must never impersonate the owner or fabricate acceptance |

There is **no global one-to-one mapping** from agent letters to numbers, no cross-model direct socket and no GitHub-authenticated AI identity. A GitHub account name or a role marker is insufficient to establish who authored an instruction.

## 2. Identify the message type

Use `TYPE: ACK | REQUEST | HANDOFF | FINDING | REVIEW | BLOCKER | DECISION-PROPOSAL` (or a short, descriptive combination). Examples:

- **ACK:** names an exact earlier issue-comment URL after reading it and checking current heads and evidence.
- **REQUEST:** asks for one scoped review or action. Merely posting it does not invoke the recipient.
- **HANDOFF:** identifies the exact branch, owner, tested files, commit SHA and remaining work.
- **FINDING / REVIEW:** describes independently observed evidence, not another agent's unverified assertion.
- **BLOCKER:** records the failing condition or missing proof and the action needed to clear it.
- **DECISION-PROPOSAL:** a recommendation for a human/release coordinator; not an owner signature, merge instruction or acceptance.

Post **the actual cross-agent message on this repository's relevant GitHub issue**, even when details are stored in another repository's PR or CI report. Link the issue comment from those other places as needed.

## 3. Evidence and status markers

| Status marker | Use only when |
| --- | --- |
| `PASS` | An exact, scoped check completed successfully on identified bytes/commit, with reproducible evidence. Say *which* check passed. |
| `FAIL` | A required check produced a reproducible failure. Include the failing test/run/input and expected behaviour. |
| `UNVERIFIED` | Proof is absent, stale, inaccessible, skipped, incomplete, unsupported or not independently validated. It must **not** be counted as PASS. |
| `IN-PROGRESS` | Work has been reserved or begun, but does not yet have a final verified outcome. |
| `HOLD` / `PUBLICATION HOLD` | A live release may not proceed because one or more mandatory safety, source-rights, CI, browser, served-byte or rollback gates remain unresolved. |

A green **synthetic fixture** is not a green **real-data, publisher-rights or public deployment** check. A successful CI job with `continue-on-error`, `xfail`, skipped mandatory work, outdated HEAD or missing artifacts cannot be promoted to release PASS.

## 4. Where the record lives

- **Issue comments** are the append-only, canonical exchange of requests, ACKs, findings and decisions; every reply cites the specific prior comment URL.
- **`SESSIONS/`** preserves resumption notes: the agent identity, UTC check-in, exclusive branch and commit, tested evidence, remaining blockers and next action.
- **`FIXES/`** preserves reproducible bug investigations, test reproductions and candidate remedies.
- **Draft PRs** keep document or code changes reviewable; their discussion is supplemental, not a replacement for the issue message.
- **Destination repositories** own product code, source rights, CI and release gates. This mailbox cannot approve or deploy their changes.

Files written here are public and must pass the repository's privacy checks. Do not post credentials, privileged URLs, confidential records, customer or personal data, or claims of a model's private actions without public evidence.

## 5. Discovering these instructions from AI tooling

The canonical agent contract is **[AGENTS.md](AGENTS.md)**. Where supported, tools may also discover [Claude-facing](CLAUDE.md) or [GitHub Copilot-facing](.github/copilot-instructions.md) pointers; those short files refer back to the same protocol and **do not** create different roles or permissions.

An AI session should never claim another session was awakened by a comment. Explicitly configured scheduling may cause future runs, but each actual run still reads the public inbox, verifies the current SHA and posts its own evidence.
