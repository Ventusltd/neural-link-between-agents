"""Defects of the scripts AS DELIVERED at b967360d (work8/tiproot/scripts).

Each test asserts the defective behaviour, so a PASS here means "defect
reproduced".  They always load the unpatched copy, whatever REPD_TEST_TARGET is.
"""
from __future__ import annotations

import importlib.util
import inspect
from datetime import date, datetime
from pathlib import Path

import pytest

from conftest import MONTH_FIRST, base_rows, make_csv, make_xlsx

ORIGINAL = Path(__file__).resolve().parents[1] / "tiproot" / "scripts"


def _load(name):
    spec = importlib.util.spec_from_file_location(f"unpatched_{name}", ORIGINAL / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def original():
    return _load("repd_q3_2026_ingest")


@pytest.fixture(scope="module")
def original_q2():
    return _load("repd_sources_v6")


def test_unpatched_rejects_every_release_that_lacks_the_25_hard_coded_refs(original):
    rows = base_rows()
    canonical, report = original.reconcile(make_csv(rows), make_xlsx(rows), make_csv(rows), "synthetic", True)
    assert canonical is None
    assert sum("Expected month-first Q3 date ref is missing" in f for f in report["failures"]) == 25
    assert any("14,657" in f for f in report["failures"])          # hard-coded floor, not the baseline


def test_unpatched_floor_and_allow_list_are_not_parameters(original):
    assert set(inspect.signature(original.reconcile).parameters) == {
        "csv_data", "xlsx_data", "old_data", "baseline_name", "baseline_is_q2"}


def test_unpatched_read_xlsx_turns_the_text_NA_into_missing(original_q2):
    rows = base_rows()
    frame, _ = original_q2.read_xlsx(make_xlsx(rows, overrides={(101, "Planning Application Reference"): "NA"}))
    assert original_q2.collapse(frame.loc[0, "Planning Application Reference"]) == ""   # official text was "NA"


def test_unpatched_build_canonical_blanks_a_planning_reference_of_NA(original_q2):
    rows = base_rows()
    key = (101, "Planning Application Reference")
    csv_frame = original_q2.read_csv(make_csv(rows, {key: "NA"}))
    xlsx_frame, _ = original_q2.read_xlsx(make_xlsx(rows, overrides={key: "NA"}))
    canonical = original_q2.build_canonical(csv_frame, xlsx_frame)
    assert canonical["Planning Application Reference"].iloc[0] == ""                     # both files say "NA"


def test_unpatched_read_csv_pads_a_truncated_record_instead_of_refusing(original_q2):
    frame = original_q2.read_csv(make_csv(base_rows()) + b",107,08/10/2026\r\n")
    assert len(frame) == 7 and frame.iloc[-1].isna().sum() == 16


def test_unpatched_strict_date_iso_drops_a_time_of_day_silently(original):
    assert original.strict_date_iso(datetime(1900, 1, 2, 12, 0)) == "1900-01-02"


def test_unpatched_shared_norm_date_still_guesses_month_first(original_q2):
    assert original_q2.norm_date("9/14/2026") == "2026-09-14"       # used by the Q2 reconcile path


def test_unpatched_baseline_with_an_identical_duplicate_raises(original):
    """The October CSV (ref 7679 twice) cannot be next quarter's baseline."""
    rows = base_rows()
    previous = rows[:3] + [dict(rows[2])] + rows[3:]
    with pytest.raises(RuntimeError, match="duplicates=1"):
        original.reconcile(make_csv(rows), make_xlsx(rows), make_csv(previous), "synthetic", True)


def test_unpatched_collapse_rewrites_nbsp_tabs_and_line_breaks(original_q2):
    assert original_q2.collapse("12 High  St\r\nLydney\t") == "12 High St Lydney"
