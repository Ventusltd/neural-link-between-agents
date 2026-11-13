# Agent activity and audit trail

This is an index, not a continuously running agent connection. GitHub Issues contain communications; commits and Actions contain verifiable activity. Agents respond only when invoked or scheduled.

## Current collaboration

- [NL-012 REPD Q3 ingestion and independent Claude QA](https://github.com/Ventusltd/neural-link-between-agents/issues/12)
- [GlobalGrid2050 draft PR #56](https://github.com/Ventusltd/globalgrid2050/pull/56)
- [GlobalGrid2050 Actions](https://github.com/Ventusltd/globalgrid2050/actions)
- [Neural-link Actions](https://github.com/Ventusltd/neural-link-between-agents/actions)
- [Claude's independent QA branch](https://github.com/Ventusltd/neural-link-between-agents/tree/nl-012-repd-q3-watch/FIXES/NL-012)

## November 2026 REPD evidence

- **Source independently verified by Claude (22:07 UTC):** Q3 official CSV `48e76c49f33a1090e78108d1ea9bfe689b35963ea3be1bb4f6516d038a5ff862` (5,219,160 bytes), workbook `87811e249395a05b223db6855952334f425e66cc9a2106caea0e38fd9e5037ea` (5,378,656 bytes). Each has 14,968 rows, 14,967 distinct Ref IDs, 53 columns; only exact duplicate Ref 7679. The final Ref ID is 21493. See [Claude's independent evidence](https://github.com/Ventusltd/neural-link-between-agents/issues/12#issuecomment-6866106908).
- **Candidate blocking defect discovered:** 25 planning submission dates use month-first CSV encoding, not just the five originally disputed cells. 19 additional values would fail day-first parsing; five were blanked. **Claude explicitly recorded FAIL on staged dates**, so staging source checks do not constitute release sign-off. Preserve the raw government files untouched.
- **Historical baseline limitation:** Original July/Q2 official bytes remain unavailable. The Q3 source evidence lives on [a non-production evidence branch](https://github.com/Ventusltd/globalgrid2050/tree/repd/2026-10-raw-evidence-20261113/evidence/repd-2026-q3); [candidate PR #56](https://github.com/Ventusltd/globalgrid2050/pull/56) is draft and unmerged.
- **Audit index branch:** `audit/nl-012-visibility-20261113`, draft [PR #18](https://github.com/Ventusltd/neural-link-between-agents/pull/18). This is a proposed index, not live continuous logging.

## Audit convention

For each meaningful event, record UTC timestamp, actor, repository and branch, commit SHA, Actions run URL and conclusion, source SHA-256 and record counts where applicable, finding, resolution and reviewer acknowledgement in NL-012. Never mark a pending CI run as passed. Preserve previous logs and backups. Do not publish private data. This index does not authorise merges or deployment.

## Visibility

The repository homepage's latest-commit timestamp changes only when a branch receives a commit; comments in Issues do not update that timestamp. The default branch will show this index only after owner-reviewed merge. See the issue for current activity.
