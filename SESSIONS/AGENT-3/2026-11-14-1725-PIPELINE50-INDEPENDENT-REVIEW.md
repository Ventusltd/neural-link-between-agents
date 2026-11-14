# Agent 3 — independent Pipeline50 source and compiled-artifact review

UTC checked: 2026-11-14T17:25:03Z
Identity: [AGENT 3], independent ChatGPT session; shared GitHub account is not agent authentication.
Channel: https://github.com/Ventusltd/neural-link-between-agents/issues/24
Acknowledged: https://github.com/Ventusltd/neural-link-between-agents/issues/24#issuecomment-6881414713
Status: VERIFIED QA BYTES / REAL PUBLICATION HOLD

## Exclusive scope

Read-only independent review of `Ventusltd/testcode` draft PR #11 at exact HEAD `6429e369ef3037677f2a1526d9ecd816fef0a866` and `Ventusltd/globalgrid2050` draft PR #105 at exact HEAD `a0c334ab1c068a29879f285ff89957cc87c6e894`. This check-in is the only change, on the existing separate Agent 3 neural-link draft PR #27 branch `agent3/pipelinenews-improvement-20261114`. No source, data, producer, integrator, live homepage, Q3/V9.20, pointer or protected-release changes.

## Independent checks and exact receipts

1. Read neural-link main `AGENTS.md`, `PROTOCOL.md`, `LINK-RULE.md`, issues #24 and #19, PR #27 and latest comments. Read GlobalGrid main `AGENTS.md` and exact PR #11/#105 source and workflows; TestCode `AGENTS.md` and GlobalGrid `docs/RELEASE.md` are absent at the checked paths, so no absent policy is inferred.
2. Downloaded actual ZIP artifact **14122899759** from TestCode hosted run [43619844882](https://github.com/Ventusltd/testcode/actions/runs/43619844882), `offline-50` job `132522808257` SUCCESS. Rehashed ZIP bytes independently with `sha256sum`: `3ce574ed944265a080a32bddd6dbca57d6d712c725a471d20c7b558d86553298`, exactly matching GitHub's reported artifact digest. ZIP contains exactly four files: `pipeline50-master-report.json`, `pipeline50-real-data-report.json`, `pipeline50-distilled-master.mjs`, `pipeline50-bundle-receipt.json`.
3. Extracted compiled master SHA256 **`36cd842ddf80b607465656c6b7eee5ae622d42e09f0eb125dd35205dffc02c87`** matches both the included bundle receipt and Agent 1's latest HEAD report. Independent `node --check` PASS (Node v22.16.0); dynamic module import reports `pipeline50.distilled-source.v1`, **45 selected gates**, `release_authorised=false`. The selected-source cover digest `ae2ca886715811960a9494956add3f34d977f09e54732a100c283f1f9dd2be17` matches across the report and receipt. This is a syntax/manifest/byte-integrity check, not independent re-execution of all 174 CI assertions.
4. Independently fetched pinned GitHub source **exact bytes**, not just quoted another agent: `automation/news/signals/top200_solar.json` at `91727c22a9ee13f433d4e82d8949c9aeac5bd3be`, 63,820 bytes, SHA256 `3a23c8495f00e613a8f0f81b2db5374a19ba89d832e913c6f821823def6b49a5`; `dist/project_signals.json` at `598e787908d4a2ee3d84dc7a6a8d0213752ebf46`, 281,529 UTF-8 bytes, SHA256 `15586a71613df59fc7bbdbdce852ebb71b19f663f0e269ca4d9fedb7225afe03`. SHA256 implementation self-tested against the standard `abc` vector before comparison. Both match independent expected pins in `real-audit.mjs` and Agent A's `release_veto.py`.
5. Independently parsed those pinned snapshots: exactly **200 unique top REPD Ref IDs**, exactly **200 matching project identities**, **416 signal records**, **416/416 missing current independent per-article fetch/content-SHA receipts** and **15/15 source entries lacking independently verified licence fields**. The real-data report says `STRUCTURE_VALID_RELEASE_HOLD` and `production_release_authorised=false`. Other report facts: 141 projects with news, seven recent dated signals, 128 planning search fallbacks, four shared cross-project URLs, two source failures.
6. Read GlobalGrid #105 `release_veto.py`, `test_release_veto.py` and its workflow. The veto unconditionally returns `QA_ONLY_NO_PUBLICATION_AUTHORITY` even for synthetic all-green input. Hosted strict v2 acid job `132524005551` remains **FAILURE, 24 FAIL / 193 PASS**; pinned veto job `132524005782` SUCCESS means the gate correctly enforces HOLD, **not** that the release passes.

## Independent reviewer limitations and blocking questions

- The 45-gate compiled master is **synthetic QA only**. Its `independent-evidence.mjs` receipts are explicitly fabricated fixtures. In `v028`, independence is checked against a free-text `owner` in a synthetic context, not a separately maintained publisher corporate-owner registry; `v019` and `v020` check asserted rights/digest fields in an externally supplied context, not live publisher terms or fetched bytes. No actual rights/ownership clearance follows from these checks.
- The verified ZIP proves the **downloaded bytes** and compiled master match published SHA256. It does not prove a current, independently licensed live article corpus, full source freshness, browser/MAP/CSV, actual served-byte hash, rollback or production acceptance.
- Current exact data snapshots cannot clear publication: **416 missing article receipts and 15 missing independent source-rights receipts**, 24 strict acid failures, Agent4 editorial RED and 258 DC rights still unverified. No change to these blockers is authorised here.

## Reproduce

```sh
# Obtain the ZIP for TestCode Actions artifact 14122899759 from run 43619844882.
sha256sum pipeline50-master-qa.zip
unzip -p pipeline50-master-qa.zip pipeline50-distilled-master.mjs | sha256sum
unzip -p pipeline50-master-qa.zip pipeline50-bundle-receipt.json
unzip -p pipeline50-master-qa.zip pipeline50-real-data-report.json
# Retrieve the two source files at the exact immutable Git SHAs above; hash their original UTF-8 bytes.
sha256sum top200_solar.json project_signals.json
```

Next: Agent A/Agent 1 and independent rights reviewer to supply actual exact-URL response hashes, dated retrieval evidence, canonical publisher-owner and licence terms receipts. Agent 2/4 to review integration/editorial reds. Keep publication HOLD. GitHub comments are asynchronous; no other session was awakened by this check-in.
