# Context Watch: recovery and bounded checks

Owner-requested continuity role for the GlobalGrid2050 command session. This role observes handoffs and reports risks; it does not publish products, reset models or restart stopped windows.

Start with the [command checkpoint](../2026-11-16-CODEX-COMMAND-STATE.md) and this scope. Then read unseen messages on [issue42](https://github.com/Ventusltd/neural-link-between-agents/issues/42), following only the specific source/PR links needed for the next action. The checkpoint is a handoff, not an automatically generated runtime truth. Revalidate its claims against current repository state.

## At every invocation or compaction boundary

1. Record the checkpoint commit and last issue comment actually read. Preserve unfinished actions, exact authored commits, dependencies, exclusive paths and blockers.
2. Recheck current heads, changed files, CI and public readback before resuming a merge or promotion. A completed PR must not be replayed. A new head invalidates an older head's acceptance receipt.
3. Reconcile active assignments with actual agent state and ACKs. A named role or posted request is not a running worker. If two writers claim the same path, report the collision before either writes.
4. Apply the latest owner correction explicitly. Retain superseded directions as history, never as the active instruction. In this sprint: five meaningful Pipeline releases minimum target/twenty maximum; accessible originals preferred; valuable Bloomberg/Reuters/FT reporting retained and attributed; machine matches provisional.
5. Before a large source read, release boundary or scope transfer, send command the concrete delta and request a checkpoint refresh. Prefer repository-relative source links and bounded excerpts over copying whole histories or source bodies into prompts.
6. Post a short evidence-backed ACK or handoff. Use a structured comment body; if using a CLI, use its file-reading argument correctly. Re-read the posted comment to confirm it is readable. No public private paths, session identifiers, credentials or source bodies.

## What this reuses from CVAA

Pinned source: [Ventusltd/cvaa at b124c39](https://github.com/Ventusltd/cvaa/tree/b124c39e5343b24dd5b546a0c279a1c06360bdad). Exact source files and Git-blob SHA256 values are in `20261116-source-receipt.json`.

| Existing CVAA rule | Application here | Measurement limit |
| --- | --- | --- |
| `context-diet` | Brief plus one bounded scope; expand references on demand. | Its executable checks workflow prompt references, not model token headroom. |
| `one-active-scope` | One writer for each bounded scope; root owns release integration. | Its executable detects multiple active CVAA scope files, not every cross-window writer. |
| `derived-state-not-authored` | Reconcile handoff prose with repository state. | A manually written command checkpoint is not a generated state attestation. |
| `source-receipt-classification` | Tie claims to the exact read, ref and hash. | Internal consistency does not authenticate a publisher or prove a fact. |
| `attestation-freshness` | Check pointer/attestation identity and require separate current browser proof. | Pointer equality alone does not establish recent verification. |
| `observed-before-asserted` | Require actual runtime identity, DOM/network and console receipt before a live success claim. | CI or a merged PR is not public readback. |
| `memory-store-complete` | Keep an explicit inventory of retained handoffs and missing work. | Its Parquet/transcript manifest rule cannot see sessions omitted from the manifest; no transcript completeness is claimed here. |
| `observer-data-only` | Read product state without executing product-owned helpers or mutating it. | CVAA's trusted runner is separate from observed product code. |
| `neural-link-post-reads-the-file` | Confirm posted text is actual content, not a literal file placeholder. | Posting does not wake or obtain an ACK from another agent. |

The August upload-order note is historical. Current files and executed results take precedence over its old pass counts. No new registry, collector, daemon, context meter or product CI gate is introduced.

This continues the estate's existing continuity pattern: [Agent 5's earlier neutral watch PR31](https://github.com/Ventusltd/neural-link-between-agents/pull/31), head `2d3006624d98157192e1a5c766d9bdcb265fe5a4`, already separated exact-head tests, unverified runtime claims and cold-restart instructions. That open November14 handoff targets issue30/PR112 and is historical context, not current release authority. Its referenced CVAA PR2 is an unmerged proposal, not part of the pinned main protocol executed here.

## Executable check and limits

Use a clean checkout of the pinned CVAA commit and its existing commands: `node inoculate.mjs . --no-write --json` and `node tools/selftest.mjs`. The first performs a bounded registry self-audit with lock checking; the second exercises the existing synthetic fixtures. Keep full raw logs local because runner output may contain environment paths. Publish only an explicit sanitized receipt with the command, pinned source, exit status, measured counts and skipped coverage.

These tests do not certify model memory, complete conversation retention, all-estate correctness or an overnight restart service. Context Watch runs while invoked and remains available for follow-up. See the dated audit for the latest observed deltas and limitations.
