# NL-012 log (append-only, newest last; times read with `date -u`; GitHub's timestamp wins)

## 2026-11-13T21:22Z  CLAUDE  FINDING  first comparison, globalgrid2050 `repd/2026-10-ingestion-20261113`@e2b7d877

STATUS: PASS for truncation; three open points.
- Against baseline 73cbdec1: added=8, modified=0, deleted=0. The six key REPD files are byte-identical.
- Added: `.github/workflows/repd-2026-q3-ingestion.yml`, `scripts/repd_q3_2026_ingest.py`,
  `docs/repd/2026-10-q3-ingestion.md`, and `backups/repd/2026-11-13-pre-october-ingestion/` (AUDIT-LOG.txt,
  manifest_v6.json, repd_source_reconciliation_v6.json, repd_sources_v6.py, repd_updater_v6_hardened.py).
- The four backup copies have the same blob hashes as their originals. The repd.csv blob named in AUDIT-LOG.txt
  (01fe17ae…) is correct.
- Open 1: the backup folder holds scripts, manifest and audit JSON, not the data. repd.csv is covered by git history
  and a 90-day Actions artifact; dist/repd_master.json and the three derived CSVs are not named in AUDIT-LOG.txt.
- Open 2: Actions run 43510048320 (pull_request) FAILED at 21:23Z before any Q3 download:
  "Baseline Q2 source hash mismatch; see Q2_BASELINE_SHA256_AUDIT.json". Artifact repd-october-2026-staging-4,
  7,722,918 bytes zipped. Claude could not download the artifact (blocked from its workspace): observed Q2 sizes UNVERIFIED.
- Open 3: Claude could not confirm the Q3 files exist. gov.uk asset hosts are unreachable from Claude's shell, and the
  publication page as fetched by Claude at about 21:12Z still listed July 2026 (Q2, updated 3 Aug 2026) as the latest.
  The two Q3 URLs in the script are UNVERIFIED from Claude's side.

## 2026-11-13T21:27Z  CLAUDE  FINDING  second comparison, same branch @fcc46887

STATUS: PASS for truncation; IN-PROGRESS.
- Commit fcc46887 "fix(repd): validate Q3 without mistaking replaced July files for historical Q2 baseline".
- Against baseline: added=8, modified=0, deleted=0; row counts and the 10,784 features unchanged.
- Runs 43510731287 (push) and 43510739859 (pull_request) in progress at 21:27Z.
- Question for CHATGPT (truncation rule 5): what evidence shows the July files were replaced at the source rather than
  cut short in transit? Please give old and new byte sizes, row counts and SHA-256 for the Q2 CSV and Excel.

## 2026-11-13T21:35Z  CLAUDE  FINDING  third comparison, same branch @b5db0b35

STATUS: PASS for truncation; Q3 existence now confirmed by CI; two open points.
- Commit b5db0b35 "fix(repd): quarantine five disputed Q3 dates, document both official values, stage only".
- Against baseline 73cbdec1: added=8, modified=0, deleted=0; repd.csv 15,182 lines, batteries 2,079, solar operational
  1,236, over 4 MW 943, repd_master.json 10,784 features, all unchanged. Only scripts/repd_q3_2026_ingest.py grew
  (8,924 to 15,719 bytes).
- Actions runs 43511649920 (push) and 43511657630 (pull_request) on b5db0b35: success. Run output:
  status STAGED_WITH_OFFICIAL_DATE_CONFLICTS, Q3 rows 14,967 (Q2 was 14,657, so Q3 is larger, not cut short).
  Compared with the historical root repd.csv, not Q2: new_refs 997, removed_refs 25, retained_refs 13,970,
  status_changed 908, technology_changed 3, csv_capacity_changed 77.
- This withdraws Claude's Open 3 of 21:22Z: the Q3 files exist and download in CI.
- Open A: the Q2 hash mismatch is no longer a failing gate; the comparison baseline was switched to repd.csv. The
  evidence asked for on the issue (Q2 sizes, hashes, row counts as now served) is still outstanding.
- Open B: five Q3 dates where CSV and Excel disagree are blanked in the staged canonical file and kept in the JSON
  audit; duplicate source rows are quarantined. Both need the owner's decision before any promotion.
- No reply from CHATGPT on the NL-012 issue yet (0 comments at this time).
