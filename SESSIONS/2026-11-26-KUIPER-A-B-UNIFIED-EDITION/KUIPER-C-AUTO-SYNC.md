# KUIPER C — AUTOMATIC HARVEST, DATA SYNCHRONISATION AND CI/CD RELIABILITY
26 November 2026 | Issued by TACIT b t b a | Neural Link #97

## 1. Mission and full inherited context

Kuiper A measures unique and total code counts. Kuiper B combines the original minimalist GlobalGrid2050 Kuiper appearance with Edition 12 functionality, especially FILE, and is the sole release integrator. Kuiper C owns the missing automated connection: after public estate code changes, the existing harvest should produce a consistent verified wafer/counter snapshot, publish it and make the approved Kuiper on both public URLs display that same snapshot without a human or local computer intervening for routine data refreshes. No new renderer, counter definition, repository or competing collector. Six TACIT research agents remain separate.

Read the complete A/B 1,489-word mandate at the immutable link:
https://raw.githubusercontent.com/Ventusltd/neural-link-between-agents/14fbc637729c53ac1811c0ae650e7e41b232e4fb/SESSIONS/2026-11-26-KUIPER-A-B-UNIFIED-EDITION/MANDATE.md
Read Neural Link AGENTS.md, PROTOCOL.md, OPERATIONS.md and issue 97, including A ACK #7199827625 and B ACK #7199828490. Read destination repository README, release, security and CI rules. Resolve fresh heads before work. Owner wants automatic updates, not merely a manual refresh instruction. GitHub-hosted CI/CD, no local machine, no agent-dependent polling, no new ChatGPT automation.

## 2. Verified diagnosis (dated starting evidence, not perpetual state)

- Ventusltd/kuiper-belt .github/workflows/engine.yml blob 4d9e95ed37aa5331ee0ed9ef0dab59146ea41ea8 has cron '17 */6 * * *' (00:17, 06:17, 12:17, 18:17 UTC, best-effort scheduling) plus manual dispatch. It runs pre-check, tools/harvest.py, check, tools/wafer_topup.py, check, then commits standing.tsv, pulse.tsv, wafer.tsv, repos.tsv and wafer-meta.json. Existing concurrency group engine has cancel-in-progress false; job timeout 80 minutes, topup step 30 minutes. Reuse this writer rather than adding another.
- Actual successful run 45864009760, harvest job 140062053900, began around 17:01 UTC. Harvest measured 84 of 84 eligible public repositories; topup read 95 of 95 public repositories; populations differ. Added 175 commits and 619,294,212 keys; issued rose from 96,921,589,773 to 97,540,883,985. K2/K4 reconciliation passed; commit/push step executed. Latest indexed commit timestamp 17:02:58 UTC. Do not call this a scheduled run without verifying its event.
- Pages run 45864556283 job 140064212184 reported success at 17:05:34 UTC, deployment ID f7a4cb9e3a764a72b7133bb275bb5387ea083be2. Verify exact build inputs and public served bytes; a successful deployment by itself does not prove custom-domain synchronisation or correct displayed count. Determine actual workflow name/path and trigger, not guesses.
- Kuiper-belt main wafer-meta.json blob 6a8b198bf63e96044dbd5f289d172043b7495ef1: 97,540,883,985 issued, 18,908,364,000 unissued, 116,449,247,985 address positions, 16,774 commits, 101 repository rows. Historical occurrences include repeated snapshots and text, not unique code, operations or physical processors.
- Ventusltd/globalgrid2050 kuiper/current.json blob a2b7db18658afff66ec4d2ab80a69e7a6cd4c473 still selects generation 202609200300 and frozen shell 202609192301-kuiper-shell; bundled wafer metadata blob 1590c193a4e9e8fa752b08ef852db90570793eaf contains 37,929,255,811 issued, 53,302,718,011 positions. Composer loads pinned shell/cartridges and shell-relative data; no automatic propagation from refreshed kuiper-belt register established. Preserve the old immutable generation as rollback.
- Edition 12 stamp 202611021201 loads shared cosmos data but its See Through layer is sealed to 63,777,293,432 positions. B owns resealing/release of compatible assets. A owns exact counter data and classification. C must prevent mixed-generation wafer, counters and derived layers. Do not rewrite old immutable edition files.
- tools/harvest.py counts current default-head text, with public-only inventory, missed-repository disclosure and fail-closed threshold. tools/wafer_topup.py appends public commits after last_unix using shallow history, exact existing law; late-pushed older timestamps may be omitted. Do not back-insert or renumber any existing key, rebuild from stale original shards, or claim complete estate coverage without actual inventory. Record missed/late commits separately and propose compatible remediation if necessary. Current standing count is not unique code count.

## 3. Exclusive scope and collaboration

Reserve agent/kuiper-c-auto-sync-20261126 in Ventusltd/kuiper-belt from verified main, and if necessary agent/kuiper-c-domain-sync-20261126 in Ventusltd/globalgrid2050 for isolated deployment-contract tests. Create draft PR(s) only as needed. C owns refresh orchestration, CI trigger/recovery, snapshot manifest, data-sync adapter, stale detection and post-deploy verification. A owns measurement/dedup implementation and counter schema; B owns UI/edition modules, existing stable route and final release integration. Do not change A/B or TACIT branches. Agree shared manifest and file ownership on issue 97 before editing shared workflows. B is the single production integration writer; C designs automated routine data refresh, not a competing publication path.

## 4. Turn 1 — trace the existing chain and diagnose gaps

- Inspect actual scheduled/manual engine runs and failures, workflow settings, branch protection, runner availability, Actions and Pages trigger events, build/deployment source commits, artifact hashes, public data URLs, old custom-domain composer and pointers. Trace one actual source commit through harvest, snapshot, build, deployment and rendered DOM on both public routes. Record UTC at each stage and elapsed time.
- Check whether GITHUB_TOKEN-generated pushes suppress downstream push-triggered workflows or whether existing Pages deployment is already correctly chained. Treat this as a hypothesis until verified; do not introduce personal access tokens or broad secrets. Check scheduling delays, default branch, disabled schedules, permissions, concurrency, path filters, CORS, browser cache and stale relative paths.
- Establish a precise freshness scorecard: latest discovered commit, latest eligible indexed commit, last successful measurement, snapshot digest, last publish, last public readback, two displayed counts, coverage, stale age, last green. Distinguish no-change success from stale failure. Verify all exact inputs and report actual blockers rather than inventing root causes.
- Agree A's counter manifest and B's UI data contract, including late/missing state and generation-bound layer requirements. Propose smallest safe architecture.

## 5. Turn 2 — implement one self-maintaining candidate pipeline

- Retain existing scheduled engine and single writer. Start with existing six-hour cadence; measure actual durations, runner costs, API limits and queue contention. Propose hourly or more frequent lightweight discovery only if measured safe, with coalesced incremental batches and a slower full reconciliation. No full estate rescan every minute or every push. Routine refresh must not require any agent session.
- Design explicit trusted handoff from successful harvest to validation and deploy; use existing reusable workflow/jobs or supported workflow_run/dispatch chaining as appropriate. Validate triggering repository/ref/commit/event and artifacts, least privilege, trusted protected workflow definitions, no execution of untrusted PR artifacts, no secret exposure. No duplicate jobs, self-trigger loops, recursive commit storms or concurrent writers.
- Assemble an atomic immutable snapshot: full wafer/repo/metadata data, A's counters/coverage receipt and B-compatible derived layers or explicit fail-closed layer state. Exact decimal strings and SHA256 pins; never display numbers from a different snapshot than the wafer. Reuse incremental blob caches; no-change idempotence and loop protection. Do not overstate historical completeness or silently omit legitimate generated code because of loop controls; agree exclusions with A and document.
- Separate versioned application releases from routine measured data generations. Preserve historic frozen payloads and stable route. Propose a small data-only latest pointer resolved by the approved shell, hash-validated with same-origin or approved CORS-compatible fetch, with safe cached last-good fallback. No arbitrary mutable code served through data channel. If existing composer cannot support safely, B integrates reviewed compatible changes; no bypass of hash seals. Ensure See Through and other SPACE-bound data are regenerated from same snapshot or explicitly unavailable; never project mismatched data.
- Make stale state visible to B's UI (last measured UTC, last indexed UTC, coverage, status); no fake live ticker. Publish only measured aggregates and licensed data. Keep failure evidence; do not publish partially acquired counts as complete.
- Reuse existing Actions, Pages and domain release contracts. Test in isolated staging without moving real production pointers. C does not authorise automatic production writes or credentials; submit exact proposed bounded data-only policy to owner for approval before activation. Once that policy is approved, ordinary validated data refreshes should not need manual release acceptance each time; application/code changes still require existing release gates.

## 6. Turn 3 — independent end-to-end acceptance and recovery

- In CI exercise two successive simulated/pinned harvest snapshots using actual producer/validator contracts and B's approved candidate (or explicit predecessor if unavailable). Confirm new eligible commits change total, unique count changes only according to A's definition, no-change refresh is idempotent and prior keys remain exact. Test malformed metadata, missed repository, late timestamp, inconsistent hash, stale counter, partial layer, duplicate run, simultaneous triggers, failed publication, stale cached browser, unavailable network and rollback. Assert no unapproved production change.
- Deploy to isolated staging using existing gates where possible. Headless Chromium/WebKit desktop and mobile check actual displayed counters against same manifest, FILE menu, wafer interaction, See Through status, freshness and no page errors. Cross-domain public readback only after B's authorised publication; compare exact served hashes, generation and rendered counts, not HTTP status alone.
- Establish health evidence on every refresh: start/end, duration, source cutoff, coverage, snapshot/release digests, last-green/failure reasons. Propose bounded retry and existing GitHub failure notification/summary, no new recurring assistant schedule. Failure retains last verified snapshot and explicit stale indicator; no partial promotion. Document restore pointer, test rollback in staging, avoid blindly rolling back newer accepted release.
- Deliver one practical runbook and owner decision packet: existing workflow map, root-cause evidence, exact proposed changes, measured cadence and staleness objective, minimal permissions, policy separating data-only automation from code promotion, proof and rollback. Acceptance is an actual hands-free CI chain that can be rerun and independently verified, not merely adding cron. A independently checks counts; B verifies interface and owns release; C independently checks freshness and post-deploy consistency. No production activation before approved policy and B's exact release gate.

## 7. Communication and references

Post ACK and turn receipts on issue 97: exact branch/head, workflow/event/job IDs, input/output hashes, replay commands, observed timestamps/counts, actual PASS/FAIL/OPEN and next action. Coordinate early with A and B. If their inputs are not ready, test verified predecessor fixtures and report blocked integration. No claims of background execution or receipt before ACK.

https://github.com/Ventusltd/neural-link-between-agents/issues/97
https://github.com/Ventusltd/kuiper-belt/blob/main/.github/workflows/engine.yml
https://github.com/Ventusltd/kuiper-belt/blob/main/tools/harvest.py
https://github.com/Ventusltd/kuiper-belt/blob/main/tools/wafer_topup.py
https://github.com/Ventusltd/kuiper-belt/actions/runs/45864009760
https://github.com/Ventusltd/kuiper-belt/actions/runs/45864556283
https://github.com/Ventusltd/kuiper-belt/blob/main/cosmos/wafer-meta.json
https://github.com/Ventusltd/globalgrid2050/blob/main/kuiper/current.json
https://github.com/Ventusltd/kuiper-belt/blob/main/editions/202611021201/README.md
https://globalgrid2050.com/kuiper/
https://ventusltd.github.io/kuiper-belt/editions/

Three Kuiper agents. One measured dataset. One verified public experience.
FOCUS ON THE CORE MISSION.
TACIT b t b a 🖖
