# Neural Memories: current build handoff

Observation: **2026-11-16 17:52 UTC**. Owner: NEURAL MEMORIES; release execution stays with COMMAND. Root can continue publishing in parallel. This document and [the checked ledger](20261116-build-ledger.json) consolidate declared sprint handoffs, not all conversations or the estate.

The ledger contains 18 components, five proposed releases, authored and integrated commits, dependency order, source-linked test reports, next commands, rollback boundaries and seven supporting handoffs. Twenty-three authored commit objects were checked in the product repository. Producer test counts are **reported passes** unless independently observed; these are not whole-release acceptance.

| Increment | Current composition | Next concrete gate |
| --- | --- | --- |
| V9.25 / 202611161630 | PR125, head 425338b6488de4da9203f97b5e9c7740157d554e; public-readback repair integrated | Six fresh workflows at this head, MAP acceptance and public served-byte/browser checks |
| V9.26 / 202611161734 | PR126, head f4d222844915438fba9323daba1808ce31c375a0; consolidated news priority consumer | Recheck stacked parent after readback repair; full CI, then live existing headline refresh |
| V9.27 / 202611161747 | Formal scaffold eb252f79c21b5217f3d38c4032c31b2d1ae159a8; consumer wiring in progress | PROSPECTING_V927 integrates existing core/UI/export chain into this new version |
| V9.28 | Global DC component handoffs; no formal release yet | Transplant older candidate delta into a new folder; keep documents, facility leads and group context distinct |
| V9.29 | Filing figures, grid/solar demand context, covenant ledger and estate sources | Integrate dependencies once; show dated source-grounded context, then release CI and browser verification |

**Public Pipeline increment count: 0 at observation.** A direct HTTP read of the homepage configuration returned 200, still naming Pipeline V9.24. Its digest is in the ledger. This is configuration-byte evidence, not a live-browser pass. Later publication needs a fresh receipt before changing this count.

GridAtlas PR92 is merged as **1de35f9eca360a5d80d81542230fef546917f5c5**, after green candidate run [43921559147](https://github.com/Ventusltd/gridatlas/actions/runs/43921559147). Parent reports public run [43922522238](https://github.com/Ventusltd/gridatlas/actions/runs/43922522238) is running; actual public acceptance remains pending. Do not replay the merge or relabel failed, closed PR90. Its next read-only check in the GridAtlas checkout is:

```sh
node tools/release/check-live.mjs --generation 202611161720 --wait
```

## Build steps for the integrator

Use repository-relative paths. Run mutations only in the named owner's clean successor branch. Before cherry-picking, compare the candidate history and owned paths against the ledger: authored commits and integrated cherry-picks have different IDs. A test count at one component/head does not transfer to another.

For V9.25 and each final product candidate:

```sh
python3 automation/pipeline_release/verify.py --browser --check
```

V9.25's readback repair was authored as **06bc78da7e5714f20ae045e42b8e00c1133a29dc** and integrated as **425338b6488de4da9203f97b5e9c7740157d554e**. Parent reports 21 readback unit tests passed. The earlier five green runs at 063adcae do not cover this new composition; all six fresh workflows are required.

V9.26 already contains NEWS ranking as **8aef1d141676041b61dbae0ec65ac0bdbee8408c** and its consumer as **c7779b2ac5ef31d6c49580d1f94a9bd81ca21b1c**. Do not reapply their authored commits. After its source merge, run the existing refresh:

```sh
gh workflow run pipeline-headlines.yml --repo Ventusltd/globalgrid2050 --ref main
```

Require successful run and matching input/sidecar readback before claiming public priority. Actual sidecar schema is `globalgrid2050.news.headline-priority.v1`; the earlier advisor's illustrative editorial name is not an implemented contract.

The prospective V9.27 composition is ordered as follows. These commands are a review recipe for a clean successor missing these components, not instructions to replay them onto the active worker branch:

```sh
git cherry-pick 2ac95439225f440c4b2e35adb1ea51229354b6f1
git cherry-pick 7b45a05f1677c72c563ed114b96e05899d741c26
git cherry-pick dc09aa85679bd995298c552617bd3ddbe2a77dfa
git cherry-pick fda83cd966348080f3f911cb534a40b4962019dd
git cherry-pick fb7dc5610656ea757611d5941f86f28d5613e9e6
git cherry-pick 19d5634bbd86f2082f6bc1aed251d453ec80fa58
python -m automation.news.build_prospecting_priority --as-of 2026-11-16T17:40:00Z --out-dir tmp/prospecting-review
```

Use a new review output directory. That timestamp reproduces a historical bundle; do not describe it as a current collection. The UI prototype equivalent at 64be28e1 must not also be applied. The ledger records the 97 pytest, 41 Node and three-width Chrome producer receipt. Validate the actual inline consumer, source links, CSV and MAP after composition. The ranked 1,000 are a separate subset, never replacement membership for the immutable Solar-1000.

For V9.28, inspect the authored delta first:

```sh
git show 35facd949c033dbf1915cc0f32d7e82b3b49cf22 -- uk_renewables_pipeline/202611161630/global-datacentres/NEXT_INCREMENT.md
```

This component changes the older V9.25 folder and needs a **transplant into the new formal release**, including adapted tests. Direct cherry-pick would mutate the historical candidate path. Follow with official-source and parent-group components from the ledger. Keep the original 12 site identities, null coordinates, 38 quarantined rows and source dates explicit. One hundred leads plus three official documents does not mean 103 verified facilities.

For V9.29, integrate FIGURES before its grid, solar and covenant consumers. Integrate covenant history before the covenant ledger. The command after that composition is:

```sh
python -m pytest -q automation/news/tests/test_filing_figures.py automation/news/tests/test_grid_dc_context.py automation/news/tests/test_solar_dc_context.py automation/news/tests/test_policy_commitments.py automation/news/tests/test_grid_intelligence.py
```

The ledger gives exact source commit IDs and matching test commands for WEST/ASIA, Android and each optional component. WEST/ASIA live intake remains disabled; fixtures are not fresh filings. GRID's 541,282 features are source rows, not unique projects. Requested/rejected power, historical pledges and equipment MVA do not establish commissioned capacity, project connections or legal compliance.

## Checks before a public count increases

- Preserve all 7,775 REPD rows, 3,604 solar and the pinned numeric Solar-1000 ordering/hash. Keep evidence provisional; V9.25's disabled source, unknown rights and zero strict real matches mean its original evidence outcome remains unmet.
- Keep the inherited Solar-1000 migration inherited. Declaring it again in V9.26 causes duplicate-migration failure.
- Finalize with explicit candidate state; do not rely on a helper's default publication label. Require relevant CI at the exact resulting head, including real browser flows.
- Distinguish source bytes, transformed owner/build bytes and public served bytes. Test homepage/version/evidence pointers together. Actual Android remains unavailable, not a desktop-emulation pass.
- Record deployed commit, served HTML SHA256 and actual browser receipt. Preserve the prior homepage pin and V9.24/V9.23 routes for rollback; use ordinary tested Git updates.

No fabricated receipt is acceptable to reach the owner's five-version target. A software-only candidate can remain useful while the source/evidence gate is blocked, without a claim that the evidence task is complete.

## Keeping this memory useful

This is the handoff layer alongside Context Watch and Integration Advisor; it does not replace their roles or introduce a scheduler. CVAA source principles used here are pinned in the ledger: declare the inventory, bind claims to source receipts and state missing coverage. This is not CVAA's complete transcript/Parquet store and does not claim transcript completeness or automatic wake-up.

1. Read the latest issue42 and the ledger observation time before using a command. Unacknowledged windows are not counted as active.
2. On new composition, update head and integration receipt; reset its CI to pending. Never carry an old head's pass forward.
3. Preserve producer reports as reports. Add observed CI and public receipts separately. Distinguish missing/failed/unavailable.
4. Validate, commit a small ledger delta and post the new commit link to issue49/42. Keep private paths and private STONES content out.
5. Root remains the sole release owner. The 10-minute idle-poll direction and support assignments are recorded by root in [issue42 comment6924410756](https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6924410756); no automatic process is claimed here.

From this repository:

```sh
python SESSIONS/AGENT-13/NEURAL-MEMORIES/validate.py
python -m unittest discover -s SESSIONS/AGENT-13/NEURAL-MEMORIES -p test_validate.py -v
```

The stdlib validator checks dependency cycles/missing nodes, exact commit syntax, counts, provisional-only invariant, historical-path transplant instruction, CI/head consistency, public receipt requirements, obvious private-path leakage and duplicate JSON keys. Its 13 tests inject these failures. It does not authenticate GitHub/browser receipts or execute the recorded commands; a local PASS means the declared handoff is internally consistent.
