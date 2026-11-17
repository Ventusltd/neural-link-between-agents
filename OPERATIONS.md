# Agent efficiency and evidence workflow

Start with [STATUS.json](STATUS.json), then [PROTOCOL.md](PROTOCOL.md) and the newest [NL-042 comments](https://github.com/Ventusltd/neural-link-between-agents/issues/42). The index accelerates discovery; it does not replace reading unseen coordination messages or verifying current repository heads.

## Work allocation

Reserve one owner, repository, isolated branch, input commit and acceptance criteria per work package before editing. Reuse existing producer outputs and test harnesses. Stage helpers within the shared concurrency limit; release slots explicitly. One integrator owns each publication and ledger writer. A reviewer checks the exact proposed commit independently.

The owner explicitly authorized tonight's ten steps and five publications: three Pipeline News and two GridAtlas versions, both discoverable on globalgrid2050.com, retaining history, through 08:00 UTC on 18 November 2026. See the [command tracker](SESSIONS/2026-11-18-OVERNIGHT-COMMAND-TRACKER.md) and [authorization receipt](https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6964495738). Routine implementation, review, CI, merge and publication within that scope need no further owner prompt. Assign versions through fresh reservations and keep all release gates. This does not authorize unrelated collectors or reactivation of expired schedules.

## Python and CI execution

Run the smallest relevant deterministic Python contracts first, then the required integration, history and browser gates. Preserve source hashes, null semantics and negative cases. Reuse pinned fixtures; distinguish synthetic, saved-input and live observations.

Before retrying, inspect the failed job and exact source SHA. Retry only failed/cancelled jobs when supported and appropriate; one integrator owns the retry. An existing automatic retry must not be duplicated. Classify infrastructure failures separately from product defects, preserving both original results and retry evidence.

For future active workflows, cache dependency downloads using OS, runtime version and dependency-lock hashes. Keep installation and all assertions active on cache hits. Cache browser binaries only with exact Playwright version and platform keys; install required OS dependencies explicitly. Measure setup and test durations before claiming savings. Changes to product CI belong in that product repository and require its own review.

Do not cancel release/deployment writers to save time. Superseded read-only candidate jobs may use concurrency cancellation only when their artifacts are not required evidence. Expired bounded workflows should retain manual dispatch and their time guards but no recurring cron.

## Compact completion receipt

Post one milestone receipt with: work ID; owner; exact source SHA; tested inputs; commands and numerical results; CI URLs and attempt; review URL; public readback if relevant; unresolved limitations; next owner/action. Link detailed artifacts instead of repeating logs. Record BLOCKED, RETRYING, TESTED, REVIEWED, MERGED and PUBLICLY VERIFIED separately.

Update STATUS.json at ownership or milestone changes. Set checked_at_utc only when the linked evidence was actually checked. Keep historical evidence marked as such. Never copy credentials, private paths or session context into public receipts.

## Maintenance validation

Run `python automation/validate_operations.py` before committing index changes. The validator checks structure, unique IDs, states and HTTPS evidence links; it does not verify remote claims or confer release approval.
