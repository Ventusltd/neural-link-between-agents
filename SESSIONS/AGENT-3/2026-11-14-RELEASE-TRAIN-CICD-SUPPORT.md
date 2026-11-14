
# Agent 3 — P2 release train CI/CD support

TYPE: OWNER-DIRECTED INTEGRATION PLAN / AGENT 3 INDEPENDENT QA
SOURCE: https://github.com/Ventusltd/neural-link-between-agents/issues/30
STATUS: PROPOSED / PUBLICATION HOLD. No implementation or deployment change.
SCOPE: This file only, on Agent 3's existing documentation branch and draft PR #27. All cross-agent messages remain in neural-link issues.

## Outcome and release slice

Ship **one** separately numbered, immutable solar-only Pipeline News successor, preferably V9.22+ when content differs from existing V9.21. Do not rewrite September (202609082224), October Q3 (202611132345), or operative V9.20 (202611140306). Include only properly licensed and independently evidenced new articles whose REPD project identity is proven. Exclude every unlicensed data-centre record and unverified news item across JSON, rendered UI, export CSV, hyperlinks and MAP; archive historical records clearly. If zero new articles meet the bar, show an honest "no newly verified headlines" state rather than fabricated content.

## Agents — one code owner per lane

**Agent 1 (producer):** Create one NEW isolated producer-fix branch with exact baseline SHA. Reproduce and fix 24 strict v2 acid failures (R01/R07/R08/R10 and related) plus seven Agent4 editorial failures, without skipping/xfailing tests. Separate immutable exact-URL fetched-body SHA receipts from independent per-(REPD Ref, URL) identity-binding receipts. Verify true two-project shared-URL positive and wrong-project R07 negative; reject duplicate and conflicting receipts. Include source-rights and event-date checks; preserve fail-closed writer when no cleared news.

**Agent 4 (editorial):** Validate false-positive/false-negative identity scenarios (Bypass, Foston, North Ray, shared URL), official/fresh/historical/planning-search tiers, event versus crawl time and prominent mobile-first presentation. Review actual producer HEAD and report exact failing/passing case URLs.

**Agent 2 (independent QA/veto):** Challenge exact head and real publisher responses, source-rights terms, canonical publisher owners, 200 project identities, dates, false positives, synthetic spoofing and partial source failures. Independently verify candidate includes no unlicensed data centres.

**Agent 3 (source/browser/CD auditor):** Independently check pinned DESNZ October CSV SHA256 48e76c49f33a1090e78108d1ea9bfe689b35963ea3be1bb4f6516d038a5ff862, XLSX 87811e249395a05b223db6855952334f425e66cc9a2106caea0e38fd9e5037ea; 14,968 raw rows, 14,967 unique references, 53 fields; top-200 identity SHA 3a23c8495f00e613a8f0f81b2db5374a19ba89d832e913c6f821823def6b49a5. Guard original Git trees September 6247a0c3c00e8e88324d9ea55b22d67dbbb1be90, Q3 0c7a4ed5ea369e4a4e71a45cfa6fe9c186fae773, V9.20 365d7df093368c39c3878daacf65449ba32e7267. Run independent real browser 1440 and 390, actual CSV download / unique REPD count, MAP click with correct GridAtlas Ref ID, zero JS errors, independent public served-byte SHA256 and dry-run rollback.

**Agent A (integrator/release):** Own ONE NEW isolated integration branch, consume reviewed producer and QA fixes, build next immutable version folder and manifest, secure the release receipt, stage and preview; only after independent gates all green follow the owner-homepage repo release process. The operative pointer is in Ventusltd/globalgrid2050-homepage data/homepage.json; validate/promote with scripts/releases.py, then update the pinned homepage-owner bundle in globalgrid2050 and deploy. Preserve the numbered homepage restore-point check and the last known-good V9.20 path. Confirm Pages deployment actually triggers on changed Pipeline News directories.

## Strict CI/CD order

1. **BASELINE:** Freeze and record exact source/release/PR SHAs and current public pointer, preserve complete backups, check destination AGENTS and release rules. All agents ACK scope in neural-link #30.
2. **OFFLINE FAIL FIRST:** Producer demonstrates original red cases, fixes them and runs all negative/positive tests. Every required job must complete successfully, no skip/xfail/continue-on-error downgrade.
3. **SOURCE/RIGHTS:** For each included headline obtain real publisher response bytes/SHA, canonical URL, owner, independent project-identity evidence, licensed redistribution and actual publish/event UTC. Exclude unsupported edges, general Energy24 items, and all unverified DC content. Fail closed if missing.
4. **INTEGRATION:** Agent A assembles only verified solar assets into a separately named immutable folder. Run exact HEAD full strict acid, Agent4 editorial suite, source-rights and no-DC closure. Prior published version trees unchanged.
5. **BEFORE PUBLICATION:** Agent3 and Agent2 independently exercise real 1440/390 page, table, filters, actual export CSV and MAP receiver; check deployed preview bytes against expected content digests. A mock-only browser PASS does not qualify.
6. **PROMOTE/CD:** On all required gates PASS, capture homeowner release restore point, validate new release in globalgrid2050-homepage, promote operative pointer there, import/pin accepted owner bundle in globalgrid2050 and dispatch/check the Pages deployment as required by existing rules. No routine extra approval under issue #30 standing owner direction, but no bypass of independent acceptance.
7. **LIVE PROOF / ROLLBACK:** Independently fetch public home link and new immutable URL; rehash served HTML/JS/CSV and compare accepted source hashes, repeat browser/CSV/MAP, record previous owner pointer and non-destructive rollback rehearsal to V9.20. If any post-deploy gate fails, use documented reversal to known-good release; do not destroy old version folders.

## Current no-go evidence at start

globalgrid2050 #105 HEAD a0c334ab1c068a29879f285ff89957cc87c6e894 last strict integrated 24 FAIL/193 PASS; #104 HEAD e1a9f767c7a41a2a02c9745df273a373ff8ad1e8 editorial seven red. The frozen project snapshot has 416 unverified per-project news bindings and 15 unreviewed source-rights entries; 258 DC licences unresolved. The standalone shared-URL structural contract in #109 passes 19 synthetic tests but does not prove real publisher bytes or identity. Agent1 TestCode #11 synthetic master is not a substitute for source/rights/live QA. Re-check all heads and CI before claiming current status.

## GO / NO-GO

**GO** only with exact HEAD strict full-suite PASS; independent article/REPD/source-rights approval for every included item; complete DC exclusion; immutable history; true 1440/390+CSV+MAP; served-byte SHA; rollback dry-run PASS. **NO-GO** on any required FAIL, missing receipt, expired rights or UNVERIFIED gate. An empty, honestly labelled fresh-headlines panel is safer than invented verified news.

ACTION REQUESTED: Agent 1 to ACK issue #30, reserve exact producer branch/head and publish one failure-to-fix matrix mapping all strict and editorial reds to reproducible CI. Agent A to assemble; Agent2/3/4 to review. All handoffs posted via this neural-link repo, not merely project PRs.
