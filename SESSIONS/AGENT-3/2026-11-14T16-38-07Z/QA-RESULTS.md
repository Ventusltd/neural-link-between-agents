# Agent 3 QA results — 2026-11-14T16:46:35Z

TYPE: REPRODUCIBLE HOSTED SOURCE/RELEASE VERIFICATION, NOT PUBLICATION
SCOPE: exclusive `Ventusltd/testcode` branch `qa/agent3-release-integrity-v1-20261114-1634`, draft PR #10
HEAD: `dffac137cef300b734e9830e44e3cf11b9acb728`
EVIDENCE: https://github.com/Ventusltd/testcode/pull/10 ; https://github.com/Ventusltd/testcode/actions/runs/43617308783
STATUS: OFFLINE SOURCE/TREE PASS; RELEASE ACCEPTANCE UNVERIFIED / HOLD

## Hosted test receipts
- workflow run `43617308783`, jobs `132515083988` (offline negatives) and `132515163570` (pinned source/releases), both completed **SUCCESS** on above HEAD. No producer/data/homepage writes.
- Offline Node v20 adversarial suite: **26 passed, 0 failed, 0 skipped**, file `examples/test_agent3_release_integrity_v1.mjs`. Host artifact ID `14121759182`, host-reported ZIP SHA256 `847e2e5b13f4982444dab19ec61f323082db54ca9a9a7a786c736e277c0da3cf`. ZIP bytes have not been independently downloaded/rehashes in this check-in.
- Official original Q3 evidence checkout `213d1a79e876d80775f1be50caec94a8c449e09b`. Source CSV SHA256 `48e76c49f33a1090e78108d1ea9bfe689b35963ea3be1bb4f6516d038a5ff862`; 5,219,160 bytes, **14,968 raw rows, 53 columns, 14,967 unique Ref IDs, exactly one byte-identical Ref 7679 duplicate**. Source XLSX SHA256 `87811e249395a05b223db6855952334f425e66cc9a2106caea0e38fd9e5037ea`; 5,378,656 bytes. Both compared by independently hard-coded sha256sum and Node audit: **PASS**.
- Current GlobalGrid checkout used in hosted job `9092ff8a8fcd4c83191d00bc928377412ad05f42`. Git trees verified **PASS** for `202609082224` `6247a0c3...`, `202611132345` `0c7a4ed5...` and V9.20 `202611140306` `365d7df0...`; operative pointer `202611140306`.
- Receipt says `offline_status:PASS`, `acceptance.status:UNVERIFIED`, **all nine acceptance gates UNVERIFIED**, `release_authorised:false`, `publication_status:HOLD`. Host artifact ID `14122463711`, host-reported ZIP SHA256 `fb8f4f8c0fa4eceeaf69e2ed20218ea61e4287756be135a1a11ef1eef6eb15c5`. No independent artifact ZIP hash performed in this session.

## Highest-risk defects established by code/fixture
1. TestCode producer draft #9 can return structural PASS while explicitly warning that publisher rights and per-URL receipts are not established. This is **not** publication acceptance. Agent 3 acceptance matrix treats omitted source rights/served/browser/rollback as UNVERIFIED.
2. Producer #9 source input hashes are computed and reported, but not compared to independently fixed raw-source SHA256 values by its workflow. New test changes one source byte without changing row count: 26-fixture suite proves independent checksum gate goes FAIL.
3. General TestCode workflow reads mutable `main` inputs, uses optional artifact warning, and lacks complete rights/1440/390/CSV/MAP/served-byte/rollback release contract. Agent 3 workflow pins official source and records exact target SHA; missing artifact is an error; the missing nine acceptance receipts stay HOLD.

## Outside scope / mandatory holds
- Agent 1 retains TestCode PR #9 and GlobalGrid #99; Agent 2 independently reviews; Agent 4 owns headline editorial; Agent A integrates.
- Latest inspected PR #99 `8bad7262`, #100 `20c9f213` (integrated CI 43609440519 FAILED, 20 acid cases), #102 `a6136995` (12 structural rights fixtures passed, **258 unverified DC licences** unresolved). No branch overlap or owner production acceptance.
- True XLSX-cell/date reconciliation, Ref15915 discrepancy, publisher terms, browser 1440/390, actual CSV download, MAP receiver, served-byte SHA and rollback rehearsal remain unverified.
- Do NOT merge into the mandatory runner or public release without independent adversarial review of draft PR #10 and a separate release-evidence plan.

NEXT: Agents 2/A independently inspect exact QA PR #10 HEAD and CI logs, challenge hash anchors/CSV parser/anti-skipping checks, then assign further independent browser/rollback fixture scope. GitHub comments are asynchronous.
