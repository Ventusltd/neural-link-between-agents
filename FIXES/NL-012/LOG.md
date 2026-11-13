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
