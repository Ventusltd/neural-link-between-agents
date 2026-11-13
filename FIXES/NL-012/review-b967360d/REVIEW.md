# REPD October 2026 ingestion: engineering review (agent 8)

Scope: `repd_q3_2026_ingest.py`, `repd_sources_v6.py`, `repd_q3_staging_verify.py` at commit b967360d
(branch `repd/2026-10-ingestion-20261113`), reviewed from the copy in `<copy of branch at b967360d>/scripts/`.
Nothing was pushed, committed, published or written outside `work8/`. No network was used.

## Result in brief

- The delivered script, run offline on the real October files, stages 14,967 rows and its candidate is
  correct for the 25 known cells. It contains **one high-severity silent-error path** (date columns it never
  checks) and **one high-severity next-quarter failure** (the allow-list), plus the medium and low items below.
- The general date rule (`repd_date_rule.py`) finds **exactly the same 25 cells without being given any ref,
  column name or count**, and the patched script produces a candidate **byte-identical** to the allow-list
  version (SHA-256 `9b1f87eb…f381343`).
- Tests: **77 passed, 0 failed** against the patched scripts. The 26 end-to-end regression tests run against
  the scripts as delivered give **12 failed, 14 passed**; the 14 are all "must reject" cases, which pass only
  because the delivered script rejects every input that lacks the 25 hard-coded refs.
- New things the rule flagged are in section 3.

One correction to the known history: 25 cells carry the month-first format, but only **24 change text**.
Ref 21435 is `09/09/2026`, which reads the same either way. The five that are valid but wrong as day-first
dates are 21424, 21438, 21456 (`09/11/2026`) and 21463, 21464 (`09/10/2026`).

## 1. Code review

Line numbers are `ingest` = `repd_q3_2026_ingest.py`, `sources` = `repd_sources_v6.py`,
`verify` = `repd_q3_staging_verify.py`. "Demonstrated" means reproduced here, on the real files mutated in
memory (`scratch/demo_defects.py`, output in `scratch/demo_defects.out`) or in `tests/test_unpatched_defects.py`.

### Defects

| # | Severity | Where | Defect |
|---|---|---|---|
| H1 | High | ingest 124, 186, 240; verify 74-79 | **Half the date columns are never checked.** Only 8 columns are treated as dates. The workbook has 16: the 8, plus Appeal Lodged, Appeal Withdrawn, Appeal Refused, Appeal Granted, Secretary of State - Intervened / Refusal / Granted, and Judicial Review (1,765 dates in the raw file this quarter). These are copied from CSV text, not compared with Excel, not normalised, and not checked by the verifier. Demonstrated: swapping one Appeal Lodged cell (ref 56, `01/11/2006` to `11/01/2006`) gives stage `STAGED…`, no failures, and the wrong date in the candidate. The eight columns are clean this quarter, so the October candidate is not affected. |
| H2 | High (next quarter) | ingest 31-37, 132, 151-181, 196-198, 217-221, 246 | **Ref allow-list.** It fails closed, so it cannot corrupt data, but it rejects any other release. Demonstrated: if the publisher corrects the 25 CSV cells, the script reports 26 failures and rejects. A month-first cell in any other column or ref also rejects, with a "material disagreement" message that does not say why. The gates `== 25` (180) and `== 5` (221) are counts of this one file. |
| M1 | Medium | sources 183; then 247-250 | **The text `NA` in Excel is read as missing.** `pd.read_excel` is called with default NA parsing. Because the candidate's Planning Application Reference is taken from Excel for every row, refs **9873 and 11989**, which say `NA` in both official files, are blank in the candidate. Not reported anywhere. |
| M2 | Medium | ingest 49, 135, 248 | **Blank-equivalent date text is dropped without a count.** 16 `NA` and 1 whitespace-only cell in Operational, 1 whitespace-only cell each in Planning Permission Refused and Secretary of State - Refusal become blank; the report has no figure for it. |
| M3 | Medium | ingest 186-213 | **Only 15 of 53 columns are compared between CSV and Excel**; the other 38 are trusted from the CSV. A full comparison (`scratch/explore6.py`) finds: Address of ref 15915 has `?` in the CSV where Excel has a zero-width joiner (lossy export); X/Y coordinates lost a leading zero in the CSV for refs 9713, 11443, 11444, 11925, 21169 (the same fault the script does repair for planning references); Turbine Capacity (23 cells) and Solar Site Area (1 cell) are rounded in the CSV while Installed Capacity is restored from Excel. None is reported. |
| M4 | Medium | sources 71-75, 234-236 | **Whitespace is rewritten in every column and not counted.** 5,410 cells differ from the official CSV for this reason: 2,498 whitespace-only cells blanked, 2,912 text cells altered (non-breaking space and tab turned into a space, line breaks inside a cell joined with a space, runs collapsed, edges trimmed). The Q3 report records none of it. The policy is defensible; the silence is the defect. |
| M5 | Medium (next quarter) | ingest 111-119 | **Previous-release floor is the constant 14,657**, not the size of the release actually compared against. And a baseline containing a duplicate row raises at 114: the October CSV (ref 7679 twice) cannot be used as next quarter's baseline. Demonstrated. |
| M6 | Medium | verify 53-95 | **The verifier never compares candidate values with the source**, apart from the 25 dates and the date format of 8 columns. A changed Site Name, capacity or planning reference would pass. Its gates are `assert` statements (38-114), which `python -O` removes entirely. |
| M7 | Medium (latent) | sources 96-103, 241-242 | **Non-numeric capacity text becomes blank.** `norm_number` returns `None` for anything it cannot parse; if CSV and Excel both say, for example, `TBC`, they compare equal (ingest 207-209) and the candidate gets an empty capacity. This quarter the only such cells are 15 whitespace-only ones. |
| L1 | Low | sources 165-172 | A truncated record is padded with missing values, not refused (demonstrated: a 3-field last line is accepted with 16 fields missing). Caught indirectly by ingest 120 if the newline is also lost, and by verify 39 on the raw file. |
| L2 | Low | ingest 46-47 | A time-of-day on an Excel date is discarded silently. Four real cells have one (see 3c). |
| L3 | Low | ingest 170 | The chronology gate (date not later than Record Last Updated) is not an invariant: 108 ordinary Planning Application Submitted dates in this release are later than their Record Last Updated. It holds for the 25 by coincidence of when they were entered. |
| L4 | Low | ingest 373; sources 418 | `to_csv` without `lineterminator` uses the platform default, so the candidate hash differs between Linux and Windows runners. |
| L5 | Low | ingest 316-319 | The old Q2 URLs are fetched first and saved as `REPD_Publication_Q2_2026.*` even when their hashes do not match, so `official-sources/` can hold mislabelled files; a 404 on an old URL stops the Q3 intake before it starts. |
| L6 | Low | ingest 272, 361 | `csv_rows` and the log line "CSV rows" give the de-duplicated count (14,967); the file has 14,968. |
| L7 | Low | ingest 88-89, 141 | "Exactly identical" duplicates are compared after whitespace collapse, and CSV/Excel agreement on duplicates compares refs only, not how many times each occurs. |
| L8 | Low | ingest 329 | Writes a literal backslash-n (`"\\n"`). Overwritten at 346, so harmless. |
| L9 | Low | sources 88, 298 | The `%m/%d/%Y` fallback that caused the earlier miss is still in `norm_date` and still used by the Q2 `reconcile` path. |
| L10 | Low | verify 38, 60-67, 101, 114, 16-24 | Pinned to this file: 53 columns, 14,968, 14,967, ref 7679, last ref 21493, 25, 5, 10,784 features, seven git blob ids. Reasonable as a tripwire for October; all need editing for the next release. `PUBLICATION_DATE = "2026-11-13"` (ingest 27) could not be checked against gov.uk from here. |

Checked and found sound: the CSV parse (pandas result equals an independent `csv` parse cell for cell,
despite mixed line endings); cp1252 decoding and UTF-8-with-BOM output (every non-ASCII character
survives; the candidate re-reads and re-writes byte-identically); duplicate handling for ref 7679; capacity
substitution (1,584 cells gain Excel precision, all within 0.005 MW, none change otherwise); the one
planning-reference leading zero (ref 11250, `58270` to `058270`); column order; fail-closed behaviour on
conflicting duplicates and on differing ref sets.

### Style, not defects

- ingest 142-143 and 146 can never fire (`q2.indexed` has already raised on the same condition).
- The module is imported as `q2` while processing Q3; two lists of date columns are kept in two files.
- The stage is named `STAGED_WITH_SOURCE_DATE_LOCALE_NORMALISATIONS` even when there are none.
- `strict_date_iso` and `day_first` become unused after the proposed patch and can be deleted.

## 2. General date rule (`work8/repd_date_rule.py`)

Standalone, 571 lines, depends only on `openpyxl`. It reads the workbook with openpyxl and not pandas,
because pandas discards the number format (the evidence the rule needs) and turns `NA` into missing.

Rule, per cell of every date column:

1. A column is a date column if the caller requires it, or if every Excel cell in it that is not
   blank-equivalent is a true date on or after 1 March 1900. No column names are built in.
2. If Excel holds a true date, that is the value. The CSV text must equal it as d/m/yyyy, or as m/d/yyyy
   **only when that cell's own number format is explicitly month-first**, or as yyyy-mm-dd.
3. Empty, whitespace, `NA`, `N/A` give a blank and are counted per column and token; Excel must agree.
4. Everything else fails: unparseable text, a date in one file only, two different dates, a day/month swap the
   format does not explain, a time-of-day, a non-date Excel cell (text dates in both files are accepted only
   when the day is above 12).
5. Output is strict dd/mm/yyyy, with one provenance record per non-empty cell.

The decision that matters: almost every date cell in the workbook has built-in format 14, which openpyxl
reports as `mm-dd-yy`. That is Excel's "system short date" and is rendered in the machine's locale, so the
rule does **not** treat it as month-first (checked against `xl/styles.xml`: ids 14, 164 `m/d/yyyy`,
165 `dd/mm/yyyy;@`, 166 `[$-10452]dd/mm/yyyy;@`). Only the custom code 164 unlocks the month-first reading.

Run on the real October files (`real_run/date_rule_summary.json`, `real_run/date_rule_provenance.csv`,
57,410 records, about 10 seconds), with no refs and no required columns supplied:

| Outcome | Cells |
|---|---|
| CSV dd/mm/yyyy equals Excel date | 57,211 |
| Month-first, text corrected from Excel | 24 |
| Month-first format, day equals month (ref 21435) | 1 |
| Blank-equivalent (16 `NA`, 158 whitespace-only) | 174 |
| Failures | 0 |

The 25 month-first cells are refs 21419, 21420, 21424, 21426, 21430, 21432, 21435, 21436, 21437, 21438,
21439, 21443, 21446, 21453, 21454, 21456, 21457, 21462, 21463, 21464, 21466, 21468, 21469, 21471, 21478,
all in Planning Application Submitted: the same set as the allow-list. 16 date columns were discovered.

## 3. What else the rule flagged on the real files

a. **Ref 20820, Planning Application Submitted = 27/11/2026**, two weeks after publication. Same in both
   files, so it is kept and flagged, like the known ref 20029 (Planning Permission Granted 15/12/2026).
   This one was not on the known list.

b. **Judicial Review is a date column** (24 true dates, 2013 to 2018, plus 155 whitespace-only cells). The
   delivered script does not treat it as one.

c. **Offshore Wind Round: 55 cells hold a round number stored with a date format.** Excel values are
   1, 2, 3 and, in four cells, 2.5; the official CSV prints them as `01/01/1900`, `02/01/1900`, `03/01/1900`
   (refs 2470-2546, 14144, 20218; the 2.5 cells are 2504, 2526, 2533, 2539). The candidate carries these
   pseudo-dates unchanged. The rule reports them and does not alter them; what the candidate should say is
   an owner decision.

d. Blank-equivalent counts by column: Operational 16 `NA` + 1 whitespace; Judicial Review 155 whitespace;
   Planning Permission Refused 1 (ref 20); Secretary of State - Refusal 1 (ref 11998).

## 4. Tests (`work8/tests`, synthetic data only)

`python3 -m pytest tests -q` from `work8/`: **77 passed, 0 failed** (1.5 s).

| File | Tests | Target |
|---|---|---|
| `test_ingest_regression.py` | 26 | `reconcile()` end to end on synthetic CSV + XLSX bytes; numbered 01-11 to match the requested list |
| `test_date_rule_unit.py` | 42 | the standalone rule |
| `test_unpatched_defects.py` | 9 | the scripts as delivered; a pass means the defect is reproduced |

`REPD_TEST_TARGET=original python3 -m pytest tests/test_ingest_regression.py`: **12 failed, 14 passed**.
Every test that expects acceptance fails on the delivered script (allow-list and 14,657 floor); the 14 that
pass expect rejection and get it for the wrong reason.

Requested items and where they are covered: identical duplicate kept once (01); conflicting duplicate
rejects (02, 02b); month-first corrected from Excel (03, 03b, 03c); ambiguous swap detected (04, 04b);
unparseable non-blank date rejects (05 ×4, 05b); NA counted (06, 06b); fewer refs than previous rejects
(07, 07b); ref sets differ rejects (08); column order equals official (09); last record complete (10, 10b,
10c); output byte-stable on round trip (11, 11b).

## 5. Proposed patch (`work8/proposed.patch`)

Unified diff, 858 lines, three files: `scripts/repd_q3_2026_ingest.py` (modified),
`scripts/repd_q3_staging_verify.py` (one hunk), `scripts/repd_date_rule.py` (new, identical to
`work8/repd_date_rule.py`). `git apply --check` passes on a pristine copy of the delivered scripts and the
result equals `work8/patched/scripts`. It has been applied nowhere else.

What it changes in the ingest script:

- removes both ref sets and the `== 25` / `== 5` gates; month-first cells are whatever the rule finds;
- every discovered date column is validated and serialised from the rule's output (fixes H1, M2, L2);
- floor becomes `max(minimum_refs, size of the baseline)`, and the baseline is de-duplicated first (M5);
- chronology is recorded per corrected cell, no longer a gate (L3);
- pins `lineterminator="\n"` (L4), fixes the `"\\n"` (L8), writes `Q3_DATE_PROVENANCE.csv`, and adds
  `date_rule`, flags and non-trivial cells to `Q3_RECONCILIATION.json`.

Effect on the real files: stage unchanged, 25 normalisations, 0 failures, candidate byte-identical to the
delivered script's. The delivered verifier still passes its checks up to the git-blob section against the
patched output (that section needs the repository and was not run here).

Not addressed by the patch, for the other agent or the owner: M1 (`NA` planning references), M3 (38
uncompared columns, coordinates, Offshore Wind Round), M4 (whitespace reporting), M6 (verifier value
comparison and `assert`), M7 (capacity text), L1, L5-L7, L9, L10.

## Files

| Path under `./` | What |
|---|---|
| `REVIEW.md` | this document |
| `repd_date_rule.py` | the general rule |
| `proposed.patch` | diff for the other agent |
| `tests/` | pytest suite |
| `real_run/` | rule output on the real files |
| `patched/scripts/` | delivered scripts with the patch applied |
| `tiproot/` | untouched copy of the delivered tree |
| `run_out/`, `run_out_patched/` | offline runs, delivered and patched |
| `scratch/` | exploration and defect demonstrations |
