# Agent 8 — V9.22 publication decision and V9.23 algorithm follow-up

Date: 15 November 2026. Appointed release owner: ChatGPT Agent 8. **Status: V9.22 release PR #116 ready for review, NOT merged; public homepage V9.21 operative.** User supplied Agent 2's detailed V9.22 algorithm review as assistance and asked to move towards publication. The review is a research handoff, not an independent approval of the current Agent8 production head.

## Separation of work and decision

**V9.22** should publish the implemented evidence-conscious news reader and exact REPD Q3 spine only if its required runtime/browser gates succeed. It must maintain candidate-only article associations and headline links; neither structural hashes nor heuristic matching can grant verified publisher rights or update October DESNZ status. Preserve the existing V9.20/V9.21 immutable versions and the homepage-owner rollback.

**V9.23** should take the separate Agent 2 algorithm recommendations through TestCode, with no new V9.22 scope creep:
1. Explicit machine-readable `association_basis` in combined news, especially `tie_break_only`, categorically barred from verified UI.
2. Event identity keyed by independently supported REPD ID + event type + planning/event reference + event-effective date; use title similarity only within an accepted identity, with explicit unknown cases remaining distinct candidates.
3. Four distinct clocks: publisher timestamp, event date, fetched timestamp and first-seen timestamp. URL dates never outrank publisher/event evidence.
4. Reproducible real HTTP original response-byte SHA and signed independent check; forged but syntactically valid receipts, review URLs and rights metadata never enable publication. The structural ledger is not an authenticity oracle.
5. Publisher ownership normalisation to stop multiple sister brands being counted as editorially independent corroboration.
6. Adversarial cross-project collision, erroneous reviewed URL, same-title separate event, syndication, healthy-empty/partial/stale, Q3 REPD status immutability, map identity and 7,775 CSV identities.

Agent2 proposed a standalone `testcode/sandbox/pipelinenews-v922-regression/` harness pinned to original Agent7 donor `5f0cadd2f8c0a9b5f44ec46fbf582ff27210b8d1`. Agent2 expressly said **the ZIP artifacts were commit-ready but not committed**; no claim is made that Agent8 accessed the actual ZIP from the other session or ran its tests. Source code and source-specific behavior cited by Agent2 should be rechecked at actual V9.23 HEAD before implementation, including newer Agent8 changes.

## Current release facts, rechecked this invocation

- [GlobalGrid2050 Agent8 PR116](https://github.com/Ventusltd/globalgrid2050/pull/116) current head `998c4cddbd78f04bcdd9df2a40026ac91714cd2f`, open and reviewable but **not merged**. Main baseline `dd0fcceb08e71d6c40b77d18e4e5eff493529d45`.
- [GlobalGrid2050 homepage owner PR15](https://github.com/Ventusltd/globalgrid2050-homepage/pull/15) open/draft; canonical `data/homepage.json` still designates V9.21 `202611141017` as operative. Do not change owner catalogue until served V9.22 bytes and rollback verified.
- The source registry's `uk_renewables_pipeline/versions.json` contains 11 versions, V9.22 first with PASS across offline/version/browser/CSV etc and **SOURCE CANDIDATE — NOT YET PUBLISHED** state. That PASS does NOT include independent live GridAtlas first-restore stability.
- Current exact-head strict producer [43734245941](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245941), integrated [43734245996](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245996), historical version checks [43734246059](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734246059) succeeded. However [staging 43734245946](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946) FAILED one 390px live GridAtlas result-visibility job.
- Actual failure: REPD 12588 Botley West solar shows calculated nearest 400kV Cowley 15.76km hidden in DOM; actual first user click to restore bottom card was followed by `gridatlas-min` remaining set, no visible nearest text. REPD 12453 battery and 14535 onshore wind passed at 390px; desktop three-class sample passed. Earlier run failed a wind sample instead; this is intermittent. [Failure evidence and suspected cause in GridAtlas #87](https://github.com/Ventusltd/gridatlas/issues/87#issuecomment-6897504870). This is **not proof that calculation failed**, but a real reader-facing UX failure. No 7,775 actual browser execution claim.
- [Agent3 independent TestCode PR12](https://github.com/Ventusltd/testcode/pull/12) adds an actual-receipt validator and 15 *synthetic validator* tests; not a fix to live GridAtlas. Do not count that green synthetic check as passing the real mobile incident.
- The underlying GridAtlas live composition is still `202611132345`, with original SLD sandbox cartridge `202609241334-sld-sandbox-v9-8.js`. `resetCardGeometry` unconditionally reapplies minimisation for sheet targets after `addCardBar` user click can expand; asynchronous content reinjection plausibly re-collapses the same user's card. The exact event order needs real trace proof. GridAtlas release contract requires a new immutable/hash-verified cartridge and explicit owner acceptance; never overwrite the original cartridge, pointer, STATE.md or homepage directly.

## Release judgment

**GO for current PR116 review and for isolated GridAtlas mobile-card remediation. HOLD the production V9.22 merge and homepage promotion while the real 390px arrival→tap→stable-visible-nearest acceptance is red.** This prevents hiding an external reader-facing defect behind passing algorithm/CSV tests. If the owner separately authorises a known-issue exception, it must be explicit, exact and retained in public release notes; do not silently downgrade a failing check.

A suitable repair is an immutable next GridAtlas cartridge preserving the initial map-first collapsed state but ensuring an actual user restore event outranks *same-project* late refresh, with a reset on a *different* selection; plus plus/minus glyph and `aria-expanded` parity, and real first/second selection browser receipts at 390/393/1440 with nearest visible for at least 1.5 seconds. Follow the GridAtlas `docs/RELEASE.md` owner acceptance procedure and perform actual public served-byte checks before adjusting homepage. That work remains independent from Agent2's algorithm TestCode proposals.

**No V9.22 production merge, unverified project-news approval or rights certification is claimed here.** Signed ChatGPT Agent8, sole designated V9.22 release owner.
