# Agent 1 — Five-slot GlobalGrid2050 command register

Snapshot: 2026-11-16 approximately 19:18–19:25 UTC. Purpose: coordination/recovery only. This file is an isolated-branch proposal, NOT a production change, new agent creation, release approval, or claim that local Codex processes are running.

## Authority and single source of truth

- Working coordination issue: https://github.com/Ventusltd/neural-link-between-agents/issues/42 . This register is the compact snapshot; new owner decisions require a dated issue #42 comment and a refreshed register rather than silent changes.
- Product code: https://github.com/Ventusltd/globalgrid2050 . Current main readback SHA 65bcc01e0d7e4dc073e759345727e53cf7a95752. Neural Link main at initial branch cut: 3174f75c6eade8309c726eb3371b46a9d558f80a.
- Homepage ownership: https://github.com/Ventusltd/globalgrid2050-homepage/pull/20 ; open DRAFT/HOLD, head 498f4b6317d5a5a07793619e67d375eda087262f, not merged. Homepage main data/homepage.json operative pipeline release ID = 202611161244 (V9.24). Do not alter this pointer.
- Product PR #125 (V9.25), #126 (V9.26) and #127 (V9.27) are merged; dated candidate pages may exist, but V9.24 remains operative and later visual changes are not owner-accepted. Never overwrite immutable release directories.
- Latest active product brief: https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6925408796 ; command takeover of V9.28 interface and scoped Grid assignment: https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6925553227 ; 'unfreeze' means development only, NOT lifting PR20 hold: https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6925813697 .

## Five-agent *proposal* (not a claim of five connected/running Codex sessions)

| Slot / pre-existing role | Exclusive edit rights / outcome | Last evidenced activity and ref | CI / status | Immediate blocker |
| --- | --- | --- | --- | --- |
| 1. Existing ROOT product integrator / V9.28 frame | Only NEW V9.28 edition 202611161757 HTML frame, presentation/styles and release integration. One GLOBALGRID2050 HEADLINES block followed by one REPD PIPELINE ANALYTICS block and tabs. No public priority numbers or extra panels. | Last root assignment issue comment 6925553227 at 18:38:29 UTC; remote branch v9.28-codex-integration SHA d90a2dda1f6426f4d10c525bced640ddb5b8faab. Earlier INTERFACE_V924 was interrupted, with no authored checkpoint. | Corrected frame exact-head CI UNKNOWN; five independent main-branch tests do not prove it. Status: unfinished / requires local ACK. | V9.24 visual/browser comparison, real 390/393/1440 receiver acceptance, publication HOLD. |
| 2. Existing SUPPORT DC consumer | Only automation/news/datacentre-ui/** component and its tests. Formal edition HTML/index/CSS belongs to slot 1; data JSON/Parquet/manifests belong to existing separately authored DC DATA contributor, not this seat. Send a host hook to root. UK-first tab, honest provenance. | DC DATA authored commit 4154862feeec6dbfa06d3b35285ff05532df9375; support UI contract issue comment 6924668954, root handoff 6924720396 at 18:03:17 UTC. UI branch/head UNKNOWN. | Support reported 32 local model tests PASS at its earlier checkpoint; exact-head hosted CI UNKNOWN. Status: consumer wiring incomplete/not independently verified. | Need UI branch/head ACK, edition host hook and browser tests. |
| 3. Existing ADDITIONAL Ventus News Engine worker | Reuse existing pipeline news owner/source, rights/evidence, attribution/binding modules. Engine/package changes only after confirming authoritative repo. No second scheduler, formal index, release metadata, UI CSS, or collector-source licence bypass. | Explicit task issue comment 6925309176 at 18:28:05 UTC, existing candidates Ventusltd/pipelinenews and pipelinenews-gridatlas-20260906 in comment 6925383229. Actual owned branch, commit and active process UNKNOWN. | CI UNKNOWN; status: assignment evidenced but implementation receipt/ACK not recovered. | Owner-repo discovery and explicit exclusive path ACK. Rights UNKNOWN; ZERO independently verified pilot matches. |
| 4. Existing GRID SOURCES worker | Only new automation/news/grid_watch/** and scoped tests; official UK grid source coverage first, EU context second. Never edit GridAtlas/MAP receiver, engine, edition HTML or competing collectors; existing MAP owner remains separate. | Root allocation issue comment 6925553227 at 18:38:29 UTC. GRID SOURCES branch, commit and process activity UNKNOWN. Historical GridAtlas PR #92 merged, but that is NOT proof of new grid_watch work. | CI UNKNOWN; status: assigned, code checkpoint not recovered. | Need branch/head ACK; verifiable operator source rights, identity and provenance. |
| 5. Existing THIRD context-UI worker | Only automation/news/context-ui/** and its component tests; no full-page frame, external figures owner files, live release, or root CSS. Handoff to slot 1 through an immutable input/hash interface. | Pushed branch v9.29-third-context-ui head 26896c1141b3686b3fb18baf05b545bb36fc8b26, checkpoint issue comment 6925274319 at 18:26:35 UTC. | Agent-reported 30 Node tests PASS plus installed-Chrome 17 checks each at 375/768/1440 with memory routes; exact-head hosted CI / public HTTP browser verification UNKNOWN. Status: tested component handoff, integration outstanding. | Root must accept/reject tiny hook and real served-browser proof. |

Roster policy: these are existing named workstreams mapped to a maximum of five proposed seats. GitHub cannot prove active local Codex processes, local token budgets, remaining context, stopped sessions or live worker count. Do not state 'five agents running'. If other previously allocated workers (project_signals, module architect, visual guard, MAP/engine) remain active, obtain owner re-prioritisation and explicit ACKs before treating this as an enforced five-session cap. Do not create, wake, terminate or silently reassign agents by posting comments.

## Token and context accounting

| Seat | Actual tokens used | Remaining context | Observation method |
| --- | --- | --- | --- |
| 1 ROOT | UNKNOWN | UNKNOWN | No connected local Codex session meter |
| 2 SUPPORT DC | UNKNOWN | UNKNOWN | No connected local Codex session meter |
| 3 ADDITIONAL News Engine | UNKNOWN | UNKNOWN | No connected local Codex session meter |
| 4 GRID SOURCES | UNKNOWN | UNKNOWN | No connected local Codex session meter |
| 5 THIRD Context UI | UNKNOWN | UNKNOWN | No connected local Codex session meter |

An older command file quotes a timestamped 119,118 / 258,400 context observation for a different past checkpoint; it is NOT current consumption, and cannot be assigned to these seats. GitHub Actions runner time and commit counts are not token consumption. If local Codex CLI supplies a live meter, the actual agent must supply timestamp, model and source, with confidential machine/session identifiers omitted; never infer or estimate.

## Exact GitHub Actions monitoring receipts

All five first-run push-triggered independent read-only test workflows are now COMPLETED / SUCCESS. These are testing workflows, not autonomous Codex producers and not a V9.28 exact-branch acceptance:

1. Release/browser: https://github.com/Ventusltd/neural-link-between-agents/actions/runs/43935346713 ; workflow SHA 3814c94e6c5d3aa94b44ce4d1193d3f24ac63f74 ; completed 19:09:07 UTC.
2. News/attribution: https://github.com/Ventusltd/neural-link-between-agents/actions/runs/43935352267 ; SHA 516d1d8f1f8c13ce05823665ff6da66a83e8ce78 ; completed 19:04:30 UTC.
3. Evidence/rights: https://github.com/Ventusltd/neural-link-between-agents/actions/runs/43935359050 ; SHA 4716d2d51f704da5ccdde00f75107dc9b737ce3e ; completed 19:04:45 UTC.
4. MAP contract: https://github.com/Ventusltd/neural-link-between-agents/actions/runs/43935363502 ; SHA d8e30b0cae6e5b5af6c99e15ff6013529a32fbd8 ; completed 19:04:20 UTC.
5. Homepage/rollback: https://github.com/Ventusltd/neural-link-between-agents/actions/runs/43935369168 ; SHA 3174f75c6eade8309c726eb3371b46a9d558f80a ; completed 19:04:21 UTC.

Per issue comment 6926193488 the existing workflows use best-effort hourly schedule at minute 13 and a hard stop on 2026-11-17 08:00 UTC. Check future individual runs separately. A green Actions job does not mean any local agent is online, source permissions accepted, a new version published, or homepage owner acceptance.

## Checkpoint and context recovery protocol — applies to EACH of the five seats

At start and after each compaction: read latest issue #42 comments after this snapshot; read this document; read AGENTS.md and the active branch's code-owner instructions; fetch exact remote HEAD, compare base/tree and open PRs; verify path ownership and absence of competing edit; recheck last CI against the exact SHA. Do NOT resume from stale context alone.

After each bounded milestone (prefer a tested atomic commit): post one issue #42 ACK/checkpoint with (1) seat and existing owner name; (2) branch, base and FULL pushed commit SHA or explicitly LOCAL/UNPUSHED; (3) exact changed paths and ownership; (4) observed last activity UTC; (5) tests, exit codes, GitHub run URLs and precise PASS/FAIL/PENDING/UNKNOWN; (6) verified blockers and next single small step; (7) local token used/remaining only if actually exposed, else UNKNOWN; (8) whether production/pointer was untouched. No secret tokens, workstation paths or local session IDs.

Per-seat recovery first actions:
- Seat 1: compare V9.24 black/monospace/cyan-yellow shell with NEW 202611161757; preserve 7775 REPD, 3604 solar, exact ordered 1000 pilot, CSV/MAP; request output hooks instead of accepting others' frame edits; run real 390/393/1440 and public-byte proof before any release discussion.
- Seat 2: read DC DATA 4154862 handoff and existing 100 leads/22 countries/38 quarantined audit; distinguish official 3 records, 6 group rows, and original 12; test only datacentre-ui; deliver host hook and explicit unknown/null handling.
- Seat 3: inspect Ventusltd/pipelinenews and existing acquisition/ranking/binding modules before writing; demonstrate exact article-rights receipts and conservative identity tests; source remains disabled without independent acceptance.
- Seat 4: inspect grid_watch namespace and authoritative TSO source fixtures; keep UK grid coverage bounded; output provenance/UNLINKED rather than invented electrical connection and do not touch existing GridAtlas engine ownership.
- Seat 5: read its own 26896c head and v9.29 composer da0f9076 dependency closure; keep 14 provisional UNLINKED contexts, 3 actual typed claims and unknown quantities; offer module host hook only, no extra panel.

## Release veto and outstanding acceptance

- Homepage PR20 stays DRAFT/HOLD; operative homepage pipeline is V9.24 (ID 202611161244). Do not merge PRs, create releases, publish a new edition, edit home data or alter the pointer as part of this coordination task.
- Latest owner UI requirement: exactly one GLOBALGRID2050 HEADLINES block then one REPD PIPELINE ANALYTICS block with tabs; V9.24 compact black/monospace/cyan-yellow styling; no public ranking numbers, standalone Register Changes or Solar-1000 Evidence Pilot panels; NEWS SIGNAL folded into MACHINE READ NOTES. Backend scoring does not imply verification.
- Formal publication may be contemplated later only by the separately authorized release owner after exact-head CI, real browser/CSV/MAP/receiver verification, source-rights review, publisher attribution, unchanged historic artifacts, owner visual acceptance, public served-byte integrity and rollback proof. This document gives no approval.

## Current blockers and next command

1. Missing direct live Codex session visibility: active status, actual tokens and remaining context UNKNOWN across all seats. Require explicit fresh ACK per existing owner; do not guess.
2. Missing pushed/current branch or exact-head hosted CI for SUPPORT DC, News Engine, GRID SOURCES; root corrected frame unfinalized; THIRD tests are component-level only.
3. Existing #42 describes more historical workstreams than five proposed seats; to enforce the cap, resolve any genuinely active extras with the owner rather than silently stopping work.
4. V9.24 visual rejection of PR20 remains a hard publication blocker; independent live acceptance of corrected next interface not yet documented.
5. Source rights, verified matching coverage and complete real Grid Engine receiver behaviour remain separate gates, despite green smoke tests.

Next command: seek fresh, disjoint owner ACKs on issue #42 for these five proposed seats and use the five established read-only Actions runs as independent regression signals. No production writes by Agent 1 command controller.

Evidence: https://github.com/Ventusltd/neural-link-between-agents/issues/42 ; https://github.com/Ventusltd/globalgrid2050-homepage/pull/20 ; https://github.com/Ventusltd/globalgrid2050/pull/125 ; https://github.com/Ventusltd/globalgrid2050/pull/126 ; https://github.com/Ventusltd/globalgrid2050/pull/127 .
