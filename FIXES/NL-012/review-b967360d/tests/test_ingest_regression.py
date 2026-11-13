"""End-to-end regression tests: synthetic CSV + XLSX bytes through reconcile().

One test (or group) per item of the owner's list; the numbering matches it.
"""
from __future__ import annotations

import csv
import io
import re
from datetime import date

import pytest

from conftest import (COLUMNS, LOCALE_SHORT_DATE, MONTH_FIRST, base_rows, candidate_bytes,
                      make_csv, make_xlsx)

STAGED = "STAGED_WITH_SOURCE_DATE_LOCALE_NORMALISATIONS"
SUBMITTED = "Planning Application Submitted"


def cell(canonical, ref, column):
    return canonical.loc[canonical["Ref ID"] == str(ref), column].iloc[0]


def test_00_clean_release_is_staged(run):
    rows = base_rows()
    canonical, report = run(make_csv(rows), make_xlsx(rows))
    assert report["failures"] == []
    assert report["stage"] == STAGED
    assert len(canonical) == len(rows)
    assert report["source_locale_date_normalisation_count"] == 0


# 1 ---------------------------------------------------------------------------
def test_01_identical_duplicate_kept_once(run):
    rows = base_rows()
    rows.insert(3, dict(rows[2]))                      # ref 103 twice, byte-identical
    canonical, report = run(make_csv(rows), make_xlsx(rows))
    assert report["failures"] == []
    assert list(canonical["Ref ID"]).count("103") == 1
    assert len(canonical) == 6 and report["original_csv_rows"] == 7
    evidence = report["identical_source_duplicates_quarantined"]
    assert [e["repd_ref"] for e in evidence["csv"]] == ["103"] == [e["repd_ref"] for e in evidence["xlsx"]]
    assert evidence["csv"][0]["exactly_identical"] is True
    assert evidence["source_rows_not_in_candidate"] == 1


def test_01b_previous_release_with_identical_duplicate_is_usable_as_baseline(run):
    """Next quarter the baseline is the October CSV, which contains ref 7679 twice."""
    rows = base_rows()
    previous = base_rows()
    previous.insert(3, dict(previous[2]))
    canonical, report = run(make_csv(rows), make_xlsx(rows), make_csv(previous))
    assert report["failures"] == [] and len(canonical) == 6
    assert report["comparison_baseline_rows"] == 6


# 2 ---------------------------------------------------------------------------
def test_02_conflicting_duplicate_rejects(run):
    rows = base_rows()
    clash = dict(rows[2])
    clash["Site Name"] = "A different site"
    rows.insert(3, clash)
    canonical, report = run(make_csv(rows), make_xlsx(rows))
    assert canonical is None and report["stage"] == "REJECTED"
    assert any("conflicting duplicate" in f.lower() for f in report["failures"])


def test_02b_duplicate_in_one_file_only_rejects(run):
    rows = base_rows()
    doubled = rows[:3] + [dict(rows[2])] + rows[3:]
    canonical, report = run(make_csv(doubled), make_xlsx(rows))
    assert canonical is None and report["stage"] == "REJECTED"


# 3 ---------------------------------------------------------------------------
def test_03_month_first_cell_corrected_from_excel(run):
    rows = base_rows()
    rows[4][SUBMITTED] = date(2026, 9, 14)             # CSV wrote 9/14/2026
    canonical, report = run(make_csv(rows, {(105, SUBMITTED): "9/14/2026"}),
                            make_xlsx(rows, {(105, SUBMITTED): MONTH_FIRST}))
    assert report["failures"] == []
    assert cell(canonical, 105, SUBMITTED) == "14/09/2026"
    events = report["source_locale_date_normalisations"]
    assert [(e["repd_ref"], e["field"], e["official_csv"], e["official_xlsx"], e["candidate_value"])
            for e in events] == [("105", SUBMITTED, "9/14/2026", "2026-09-14", "14/09/2026")]


def test_03b_month_first_cell_that_is_also_a_valid_day_first_date(run):
    """The dangerous five of October: 09/11/2026 parses day-first as 9 November."""
    rows = base_rows()
    rows[4][SUBMITTED] = date(2026, 9, 11)
    canonical, report = run(make_csv(rows, {(105, SUBMITTED): "09/11/2026"}),
                            make_xlsx(rows, {(105, SUBMITTED): MONTH_FIRST}))
    assert report["failures"] == []
    assert cell(canonical, 105, SUBMITTED) == "11/09/2026"
    assert [e["repd_ref"] for e in report["formerly_ambiguous_date_representations"]] == ["105"]


def test_03c_month_first_correction_is_not_limited_to_one_column(run):
    rows = base_rows()
    canonical, report = run(make_csv(rows, {(102, "Appeal Lodged"): "9/15/2026"}),
                            make_xlsx(rows, {(102, "Appeal Lodged"): MONTH_FIRST}))
    assert report["failures"] == []
    assert cell(canonical, 102, "Appeal Lodged") == "15/09/2026"


# 4 ---------------------------------------------------------------------------
def test_04_ambiguous_day_month_swap_detected(run):
    """CSV 09/11/2026 against Excel 11 September under the ordinary locale format."""
    rows = base_rows()
    rows[4][SUBMITTED] = date(2026, 9, 11)
    canonical, report = run(make_csv(rows, {(105, SUBMITTED): "09/11/2026"}),
                            make_xlsx(rows, {(105, SUBMITTED): LOCALE_SHORT_DATE}))
    assert canonical is None and report["stage"] == "REJECTED"
    assert any("105" in f for f in report["failures"])


def test_04b_swap_detected_in_a_date_column_outside_the_original_eight(run):
    rows = base_rows()
    rows[1]["Appeal Lodged"] = date(2026, 9, 11)
    canonical, report = run(make_csv(rows, {(102, "Appeal Lodged"): "09/11/2026"}), make_xlsx(rows))
    assert canonical is None and report["stage"] == "REJECTED"


# 5 ---------------------------------------------------------------------------
@pytest.mark.parametrize("text", ["sometime in 2026", "31/02/2026", "14/09/26", "2026.09.14"])
def test_05_unparseable_non_blank_date_rejects(run, text):
    rows = base_rows()
    canonical, report = run(make_csv(rows, {(104, SUBMITTED): text}), make_xlsx(rows))
    assert canonical is None and report["stage"] == "REJECTED"


def test_05b_unparseable_date_present_in_both_files_rejects(run):
    rows = base_rows()
    canonical, report = run(make_csv(rows, {(104, "Operational"): "Q3 2026"}),
                            make_xlsx(rows, overrides={(104, "Operational"): "Q3 2026"}))
    assert canonical is None and report["stage"] == "REJECTED"


# 6 ---------------------------------------------------------------------------
def test_06_na_is_blanked_and_counted(run):
    rows = base_rows()
    rows[0]["Operational"] = date(2025, 3, 1)
    canonical, report = run(
        make_csv(rows, {(103, "Operational"): "NA", (104, "Operational"): "NA", (105, "Operational"): " "}),
        make_xlsx(rows, overrides={(103, "Operational"): "NA", (104, "Operational"): "NA",
                                   (105, "Operational"): " "}))
    assert report["failures"] == []
    assert [cell(canonical, r, "Operational") for r in (101, 103, 104, 105)] == ["01/03/2025", "", "", ""]
    assert report["date_rule"]["blank_equivalent_counts"]["Operational"] == {"<whitespace>": 1, "NA": 2}


def test_06b_na_in_csv_but_date_in_excel_rejects(run):
    rows = base_rows()
    rows[2]["Operational"] = date(2025, 3, 1)
    canonical, report = run(make_csv(rows, {(103, "Operational"): "NA"}), make_xlsx(rows))
    assert canonical is None and report["stage"] == "REJECTED"


# 7 ---------------------------------------------------------------------------
def test_07_fewer_refs_than_previous_release_rejects(run):
    previous = make_csv(base_rows(6))
    rows = base_rows(5)
    canonical, report = run(make_csv(rows), make_xlsx(rows), previous)
    assert canonical is None and report["stage"] == "REJECTED"
    assert any("floor" in f or "below" in f for f in report["failures"])


def test_07b_same_or_more_refs_than_previous_release_passes(run):
    rows = base_rows(6)
    canonical, report = run(make_csv(rows), make_xlsx(rows), make_csv(base_rows(5)))
    assert report["failures"] == [] and len(canonical) == 6
    assert report["reference_changes_vs_comparison_baseline"]["new_refs"] == 1


# 8 ---------------------------------------------------------------------------
def test_08_csv_and_excel_ref_sets_differing_rejects(run):
    rows = base_rows()
    canonical, report = run(make_csv(rows), make_xlsx(rows[:-1]), make_csv(base_rows(5)))
    assert canonical is None and report["stage"] == "REJECTED"
    assert report["csv_excel_id_sets_match"] is False
    assert "CSV and Excel REPD reference sets differ" in report["failures"]
    assert not any("floor" in f for f in report["failures"])       # rejected for this reason alone


# 9 ---------------------------------------------------------------------------
def test_09_candidate_column_order_equals_official(run):
    rows = base_rows()
    canonical, report = run(make_csv(rows), make_xlsx(rows))
    official = [re.sub(r"\s+", " ", name.strip()) for name in COLUMNS]
    assert list(canonical.columns) == official
    header = next(csv.reader(io.StringIO(candidate_bytes(canonical).decode("utf-8-sig"), newline="")))
    assert header == official


# 10 --------------------------------------------------------------------------
def test_10_last_record_complete(run):
    rows = base_rows()
    source = make_csv(rows)
    canonical, report = run(source, make_xlsx(rows))
    data = candidate_bytes(canonical)
    assert data.endswith(b"\n")
    records = list(csv.reader(io.StringIO(data.decode("utf-8-sig"), newline="")))
    assert len(records[-1]) == len(COLUMNS) and records[-1][1] == "106"
    assert records[-1][COLUMNS.index("Record Last Updated (dd/mm/yyyy)")] == "08/10/2026"
    assert all(len(record) == len(COLUMNS) for record in records)


def test_10b_source_without_final_newline_rejects(run):
    rows = base_rows()
    canonical, report = run(make_csv(rows).rstrip(b"\r\n"), make_xlsx(rows))
    assert canonical is None and "Q3 source CSV has no final newline" in report["failures"]


def test_10c_source_with_truncated_final_record_rejects(run):
    rows = base_rows()
    source = make_csv(rows)
    truncated = source[:source.rstrip(b"\r\n").rindex(b"\n") + 1] + b",106,08/10/2026\r\n"
    try:
        canonical, report = run(truncated, make_xlsx(rows))
    except (ValueError, RuntimeError):
        return                                         # refused outright: acceptable
    assert canonical is None and report["stage"] == "REJECTED"


# 11 --------------------------------------------------------------------------
def test_11_output_round_trips_byte_stable(run, q2):
    rows = base_rows()
    rows[0]["Site Name"] = "Café – “North” Solar, Phase 2"   # non-ASCII, comma, quotes
    rows[1]["Planning Application Reference"] = "007"
    rows[4][SUBMITTED] = date(2026, 9, 14)
    csv_bytes = make_csv(rows, {(105, SUBMITTED): "9/14/2026"})
    xlsx_bytes = make_xlsx(rows, {(105, SUBMITTED): MONTH_FIRST})
    canonical, report = run(csv_bytes, xlsx_bytes)
    assert report["failures"] == []
    first = candidate_bytes(canonical)
    assert first.startswith(b"\xef\xbb\xbf") and b"\r" not in first
    assert candidate_bytes(q2.read_csv(first)) == first            # read back, write again
    again, _ = run(csv_bytes, xlsx_bytes)
    assert candidate_bytes(again) == first                         # deterministic rebuild
    assert cell(canonical, 101, "Site Name") == rows[0]["Site Name"]
    assert cell(canonical, 102, "Planning Application Reference") == "007"


def test_11b_every_date_column_of_the_candidate_is_strict_day_first(run):
    rows = base_rows()
    rows[3]["Planning Permission  Granted"] = date(2026, 12, 15)   # future, like ref 20029: kept, flagged
    canonical, report = run(make_csv(rows), make_xlsx(rows))
    assert report["failures"] == []
    for column in report["date_rule"]["date_columns"]:
        for value in canonical[column]:
            assert value == "" or re.fullmatch(r"\d{2}/\d{2}/\d{4}", value), (column, value)
    assert "Appeal Lodged" in report["date_rule"]["date_columns"]
    assert cell(canonical, 104, "Planning Permission Granted") == "15/12/2026"
    assert [(f["ref"], f["flag"]) for f in report["date_rule_plausibility_flags"]] == [("104", "AFTER_AS_OF_DATE")]
