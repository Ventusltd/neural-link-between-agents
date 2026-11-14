# NL-014: genuine July 2026 (Q2) REPD baseline and full July -> October comparison (Team 2)

Source of the July files: globalgrid2050 branch `repd/2026-07-verified-archive-20261113` @ `d015479f718d697312738f127ba72cd63cf8042e`,
`evidence/repd-2026-q2-original/official-sources/`, read with one shallow fetch and `git show`. No branch was checked out or created.
Only aggregate REPD statistics appear here. Re-runnable scripts are in `scripts/`.

| Check | Result |
|---|---|
| July CSV sha256 / bytes | 84c1b5f958a934d8b4b86ec88f50bdcf43830ded7ff2efc27bffca0c98695035 / 5,087,389: matches the pin |
| July XLSX sha256 / bytes | 624a0a9712c58a7a93716e51f2bf054eec8b1af7170f6f9516cc10cd248e2657 / 5,185,558: matches the pin |
| Structure (automation/repd/verify_release.py, exit 0; scripts/indep_verify.py agrees) | 14,657 rows, 53 fields in every row, header exact, 14,657 unique refs, 0 duplicates, CSV and XLSX ref sets equal and in the same order |
| July quirks | 1 month-first date, 16 "NA" Operational dates, 55 Offshore Wind Round numbers stored as Excel dates, 951 records with embedded newlines |
| clean.py on July | 1,435 cells changed, all logged, 0 unexplained; output sha256 52e2c81c...601b |
| V6 derived files (project_identity_v6, major_projects_v6, manifest_v6, repd_source_reconciliation_v6) | byte-identical when rebuilt from the raw July bytes with main's and with PR #57's scripts (scripts/rerun_v6.py). The "July derived file fidelity UNVERIFIED" caveat is CLOSED |
| Coordinate fixture repd_q2_coordinates.json (cites workbook 99ec4d05) | all 14,657 records identical when rebuilt from the canonical 624a0a97 workbook (scripts/rebuild_coords.py). Only the cited workbook name and hash differ. The 99ec4d05 bytes themselves are not available: UNVERIFIED why they differ |

## July -> October (clean.py output vs clean.py output, all 53 columns)
- Records 14,657 -> 14,967: 319 added (8,816.1 MW), 9 removed (169.8 MW), 14,648 retained. 373 status changes. 17 capacity edits
  (net -253.0 MW). This matches Agent A's delta.
- automation/repd/diff.py and the independent scripts/indep_diff.py agree on every column. 644 retained refs have a real change
  (645 raw-vs-raw; the extra one is the July month-first date).
- Operator: 530 changed, of which 493 only switch " / " to " & ". Address: 521 changed, all line-break/spacing removal.
- The 33 columns the earlier report did not compare: see UNCOMPARED_COLUMNS.md. Per-technology tables: TECH_TABLES.md.
- The earlier PR #57 report compared against Q3_CANONICAL_STAGED.csv, which keeps Offshore Wind Round in Excel-date form. That
  gave 55 artificial changes. The regenerated report (patch held for the harness) fixes this; its headline figures are unchanged.

## January -> July (trend series)
- 13,995 -> 14,657: 680 added, 18 removed, 723 status changes, +25,851.6 MW known capacity.
- Solar Site Area: filled for 1,623 onshore wind records in January, blanked by July.
