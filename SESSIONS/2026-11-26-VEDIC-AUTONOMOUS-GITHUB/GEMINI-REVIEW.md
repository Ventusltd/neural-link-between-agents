# VEDIC — Gemini independent architecture review
26 November 2026 · TACIT b t b · Review addendum, not production authorisation

The supplied Gemini proposal and SVG validate the broad GitHub-only direction, including AST extraction, CPU sparse analysis, compressed receipts, durable state, append-only admission and independent release gates. The principal difference is that Gemini requires a daily human review flip and human PR approval; this does not fulfil the previously requested unattended admission objective.

## Decision register

| Gemini recommendation | Disposition | Reason / change |
|---|---|---|
| CPU-based AST extraction and sparse TF-IDF | Adopt conditionally | Reuse existing producer; benchmark incremental parsing and bounded top-k retrieval. |
| Under five seconds / under 300 MB RAM | Unverified performance hypothesis | Require measured end-to-end wall time, peak RSS, matrix density, candidate recall and actual runner type; do not promise performance. |
| Permanent family hashes | Adopt | Keep stable identity separate from mutable similarity clusters; preserve historical membership. |
| Nearest family ID fallback when a hash changes | Reject | Can silently skip work. Stop on identity mismatch, reconcile from immutable registry evidence and replay deferred IDs before checkpoint migration. |
| Daily 100-family pulse | Adopt | Retain existing 03:37 UTC schedule, single-writer and durable work queue. |
| External LLM drafting | Optional, disabled by default | Deterministic static analysis first. If separately authorised, use bounded, schema-constrained proposals only; no credentials, source disclosure or spending without approval. Model outputs are untrusted candidates, not proof. |
| Two-repository threshold | Modify | Use as priority signal, not an eligibility gate: important unique functions may exist in only one repository. |
| Human approval of every candidate and PR | Reject as default | Explicit one-time policy approval, independent required CI and protected auto-merge for evidence-backed static commands; ambiguous cases remain held. If branch rules require human approval, no bypass. |
| Permanent queue archive and replay | Adopt | Exact replay, immutable historical rows, atomic queue partition with dictionary, and no ID allocation until validation. |
| Daily Parquet committed to research branch | Modify | Keep small essential state/dispositions in Git, compressed batch telemetry in expiring artifacts or separate bounded storage; avoid unbounded binary Git history. |
| Weekly producer rebuild + repository dispatch on every push | Modify | Integrate with existing producer cadence; use incremental content-addressed updates, debounce and concurrency controls. Avoid full rebuild on every commit. |

## Computational caution
33,221 squared equals 1,103,634,841 pair positions. A dense float32 all-pairs similarity result alone would occupy about 4.4 GB (decimal), before working arrays; float64 about 8.8 GB. Sparse representation is not a guarantee of small memory because common tokens can make the result dense. Use bounded query batches, sparse top-k retrieval, and exact-hash / contract indexes first. Benchmark recall on known duplicates and distinct operations; similarity is a reconciliation hint, not a semantic equivalence proof. Exact family identity must not depend on an adjustable TF-IDF clustering threshold.

## Recommended unified flow
Existing Modular Star producer → pinned AST/capability metadata → daily bounded incremental discovery → exact and ranked duplicate checks → deterministic evidence-backed command policy → protected proposal → independent replay/CI → authorised auto-merge → existing Pages release and exact served-file verification.

Keep the LLM path optional for uncertain candidate drafting; such drafts are not automatically admitted unless the independent deterministic policy can establish every required fact. The default should remain self-contained in GitHub-hosted Actions, without external paid inference, local hardware or active chat sessions. No requirement for positive daily growth; zero valid admissions is a legitimate outcome.

## Acceptance and governance
Retain all acceptance criteria in PROPOSAL.md, adding benchmark evidence, similarity false-positive/false-negative fixtures, identity-mismatch recovery tests, one-repository valid capability fixtures, and a test proving that untrusted candidate content cannot control workflow execution or bypass admission policy. The attached Gemini graphic is a useful description of the human-gated alternative, not the approved autonomous architecture. The original architecture and growth graphics remain unchanged.

No production workflow, credentials, permissions or branch protection changed by this review.

TACIT b t b
