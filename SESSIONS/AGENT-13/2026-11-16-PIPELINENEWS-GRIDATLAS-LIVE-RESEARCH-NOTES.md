# LIVE RESEARCH NOTE — Pipeline News vs GridAtlas (initial evidence index)
**UTC observation:** 2026-11-16 approximately 18:44 UTC. **Status:** preliminary GitHub audit, NOT the final deep research or independent acceptance. **Audience:** Codex agents working concurrently. **Repository:** Ventusltd/neural-link-between-agents. **Policy:** append independent receipts, do not alter production from this note.

## IMPORTANT: current development has overtaken the original V9.25 plan
At this observation the public GitHub API reports these **merged** PRs in `Ventusltd/globalgrid2050`:
- [#125 V9.25 consolidated UK/Global pipeline and guarded evidence snapshots](https://github.com/Ventusltd/globalgrid2050/pull/125), merged 2026-11-16 18:02:24Z, merge commit `60c778d9789b88ce6a803ac84bff9099e423eec2`.
- [#126 V9.26 source-aware news priority](https://github.com/Ventusltd/globalgrid2050/pull/126), merged 18:06:51Z, merge commit `53c437fa23debe16036b87ba3d59cfaca3900105`.
- [#127 V9.27 explained project research priority](https://github.com/Ventusltd/globalgrid2050/pull/127), merged 18:07:04Z, merge commit `fb4bd1baaa50c5102a791cf88b9ef23f3fc89a67`.
- The inspected main HEAD was `65bcc01e0d7e4dc073e759345727e53cf7a95752`, a catalogue regeneration commit at 18:17:59Z. **Recheck HEAD before each claim**.
- An `assist/v929-context-composition-20261116` branch exists. Existence is not acceptance or release. **Do not tell agents to restart V9.25 from scratch**.

**Merge is not proof of live deployment, source acceptance, independent verification or correct public-root bytes.** Read exact CI run, operative pointer, homepage owner pin and live readback before declaring published.

## High-value source modules to independently inspect and reuse
All paths below were observed on `globalgrid2050` main at this observation:
1. `automation/news/acquisition/research_queue.py`: pinned Solar-1000 source-manifest verification. Preserve official REPD identity and numeric order.
2. `automation/news/acquisition/fetch.py`, `normalise.py`, `sources.yaml`, `run.py`: bounded collection, provenance and rights gate.
3. `automation/news/acquisition/match.py`: 1,621-byte conservative matcher, explicit REPD IDs or unambiguous complete project names, always `PROVISIONAL`. This is a useful narrow baseline, **not** independently validated factual evidence.
4. `automation/news/acquisition/evidence_store.py`, `publish.py`: SQLite persistence and snapshot publication. Inspect idempotence, failure atomicity and Git race behavior before reuse.
5. `automation/news/acquisition/analytics.py`: DuckDB/Parquet analytical readback, CPU-only; source README cites `Ventusltd/data-gridatlas` compiler at commit `8bf88da9e210ce9f61dc0398869d3369f3fa2445`.
6. `automation/news/news_algorithm.py`, `build_news_priority.py`, `NEWS_PRIORITY.md`: V9.26 separate headline rank sidecar tied to exact input SHA, not replacement of original articles.
7. `automation/news/prospecting.py`, `build_prospecting_priority.py`, `PROSPECTING.md`: V9.27 source-bound project research triage; read exact owner policy and distinguish discovery-only signals from admissible project evidence.
8. `automation/pipeline_release/feature_contracts.py`, `verify.py`, `new_version.py`, `docs/pipeline/RELEASE-TRAIN.md`: inherited contracts and immutable release checks.
9. `uk_renewables_pipeline/202611161630/` (V9.25), `202611161734/` (V9.26), `202611161747/` (V9.27): inspect generated assets, build manifests and tests; do not edit historical release trees.

## Immediate verified caveats from repository documentation
- `automation/news/acquisition/README.md` says the PV Magazine source is **disabled** pending rights acceptance. A 16:27:39Z transport probe reported HTTP 200, 10 articles, SHA `840b79c7a26eca9afc67ec689317cc67e559abb13dad4027a539994a7c9acd56`, **zero** strict Solar-1000 matches. The docs state **no real project evidence snapshot published**. Revalidate these claims and do not turn a probe into accepted evidence.
- `automation/news/NEWS_PRIORITY.md` says V9.26 rank sidecar `dist/pipeline_headlines.rank.json` binds the original `dist/pipeline_headlines.json` by SHA256, count, identity, profile and clock; stale/invalid sidecar falls back to date order. It is editorial ranking, **not project verification**.
- `automation/news/PROSPECTING.md` distinguishes permitted discovery-only Bloomberg headline/link metadata from project-evidence input: do not promote paywalled discovery clues into project or financing facts.
- PR #125 claims tests (519 pytest passed, 4 skipped, 12 XPASS; 115 Playwright) and a 12-site/10-country partial DC sample; PR #126 claims 123 pytest, 8 Node, 54 Chrome; PR #127 claims 97 pytest, 41 Node, 21 Chrome + 21 Chromium. **These are PR-author claims, not independent re-executions.**
- `acquisition/publish.py` uses `git push --force-with-lease=refs/heads/pipeline-evidence-data:<expected-head>` with a direct-parent check. This is a conditional compare-and-swap style push, **not** an unconditional normal push; audit protected branch rules and concurrent writers carefully. Never simplify this to unsafe force push.

## GridAtlas comparison — concrete baseline, open investigation
- The V9.25 analytics README cites `Ventusltd/data-gridatlas` compiler `compiler/202608291015-build-v8-transplant.py` at `8bf88da9e210ce9f61dc0398869d3369f3fa2445`: explicit DuckDB schemas, one thread, sorted ZSTD Parquet, readback and SHA256 receipts.
- The companion pinned runbook `runbooks/202608291507-data-gridatlas-automation.md` is cited for file closure, schema/count/hash verification and immutable conflict rejection.
- The current Pipeline UI includes `scripts/core/atlas-receiver-v9-7.js`, `scripts/core/atlas-interconnector-link-v9-8.js`, `gridatlas/map_link_state.json`, canonical project tables and MAP deep-link contracts.
- **Do not assume GridAtlas and Pipeline News share one identity space.** Compare source IDs, coordinate/null semantics, project-type separation, serialization order, schema migrations, maps/deep links, lineage, immutable build closure, release gates and public bytes.
- This is a comparison **target list**, not a completed code-quality ranking. Deep Research should inspect code, run tests and produce a scored, evidence-linked reuse recommendation.

## Computer-science gates for all 16 concurrent Codex agents
- **Concurrency:** 16 active local PowerShell Codex processes are owner-reported, not independently observable through GitHub. Require each to announce branch, owned paths, base SHA, intended PR and integration owner in issue #42. No duplicate path writers; no agent independently promotes a release.
- **Versioning:** Never mutate immutable V9.25/V9.26/V9.27 release folders; build a successor and verify exact parent. Reconcile `registry.json`, `versions.json`, owner homepage pin and served root before publication.
- **Data identity:** Preserve 7,775 REPD, 3,604 solar and exact V9.24 numeric Solar-1000 (1,000) as regression invariants. Separate >20MW solar+BESS research cohort.
- **Evidence:** No automatic VERIFIED. Model raw observation, normalized article, candidate project association, review decision and published assertion separately. Every promoted fact needs source rights, exact identity, clock precision and independent acceptance.
- **Safety:** Bound HTTP; validate redirects and DNS/IP targets; retry with caps; fail closed on critical source/schema errors; do not publish partial snapshots as complete.
- **Persistence:** SQLite uniqueness and transactions, deterministic export and replay, immutable snapshot generation, stale-HEAD rejection, rollback pointer.
- **Frontend:** News original text and publisher link must survive ranking; unknown values stay null; escape source content; verify MAP and GridAtlas links at mobile and desktop.
- **Quality:** Property/metamorphic tests for order invariance, dedup, replay, clock precision, name collisions and source conflicts. Exact CI run URL, PR head, test command, test output, output hash and public readback for every claim.
- **GPU:** CuPy is not justified by default for 1,000–7,775 records and I/O-bound feeds. Prefer CPU DuckDB/SQLite; benchmark GPU only on a measured vectorized bottleneck with CPU parity.

## Research follow-up to produce
[ ] Map **actual** current main + open PRs + successor branches, not stale plan assumptions.
[ ] Compare implementations with GridAtlas pinned source, tests and public behavior.
[ ] Identify best reusable functions by exact file/commit/line and measured correctness.
[ ] Audit 16-agent GitHub conflict surface, integration gates and live publication safety.
[ ] Produce prioritized findings with reproducible commands, failing fixtures, impact and owner.
[ ] Append the completed deep research report or link it here; never overwrite source code from research alone.

## Coordination
- [Agent 13 board / issue #42](https://github.com/Ventusltd/neural-link-between-agents/issues/42)
- [Agent coordination / issue #41](https://github.com/Ventusltd/neural-link-between-agents/issues/41)
- [Full 200-task plan](https://github.com/Ventusltd/neural-link-between-agents/blob/0da2ba75f1eb27f8571ec6bb14a418d488615c7d/SESSIONS/AGENT-13/2026-11-16-V925-EXECUTION-PLAN-15MIN.md)

**Agent usage:** treat this file as a time-stamped evidence index. It does not assign work, authorize release, prove live deployment, or replace AGENTS.md / issue #42 owner protocol.
