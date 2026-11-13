"""Shared synthetic-release builders.  No network, no real data.

REPD_TEST_TARGET selects the scripts under test:
  patched  (default)  work8/patched/scripts  = commit b967360d + proposed.patch
  original            work8/tiproot/scripts  = commit b967360d as delivered
"""
from __future__ import annotations

import csv
import inspect
import io
import os
import sys
from datetime import date, datetime
from pathlib import Path

import openpyxl
import pytest

WORK = Path(__file__).resolve().parents[1]
TARGET = os.environ.get("REPD_TEST_TARGET", "patched")
SCRIPTS = WORK / {"patched": "patched", "original": "tiproot"}[TARGET] / "scripts"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(WORK))  # standalone repd_date_rule (identical to the patched copy)

# Official header order in miniature, keeping the real quirks: a trailing space
# and a double space inside two headers.
COLUMNS = [
    "Old Ref ID", "Ref ID", "Record Last Updated (dd/mm/yyyy)", "Operator (or Applicant)",
    "Site Name", "Technology Type", "Installed Capacity (MWelec)", "Development Status (short)",
    "Are they re-applying (Old REPD Ref) ", "Planning Authority", "Planning Application Reference",
    "Planning Application Submitted", "Planning Application Withdrawn", "Planning Permission Refused",
    "Appeal Lodged", "Planning Permission  Granted", "Planning Permission Expired",
    "Under Construction", "Operational",
]
LOCALE_SHORT_DATE = "mm-dd-yy"   # built-in format 14: what almost every official date cell carries
MONTH_FIRST = "m/d/yyyy"         # explicit custom format carried by the 25 October cells


def base_rows(n: int = 6) -> list[dict]:
    rows = []
    for i in range(1, n + 1):
        rows.append({
            "Old Ref ID": "", "Ref ID": 100 + i,
            "Record Last Updated (dd/mm/yyyy)": date(2026, 10, 8),
            "Operator (or Applicant)": f"Operator {i} Ltd", "Site Name": f"Site {i}",
            "Technology Type": "Solar Photovoltaics" if i % 2 else "Battery",
            "Installed Capacity (MWelec)": 49.9 if i % 2 else 120,
            "Development Status (short)": "Application Submitted",
            "Are they re-applying (Old REPD Ref) ": "", "Planning Authority": "Shropshire",
            "Planning Application Reference": f"26/0{i}/FUL",
            "Planning Application Submitted": date(2026, 8, 20 + i),
            "Planning Application Withdrawn": None, "Planning Permission Refused": None,
            "Appeal Lodged": date(2026, 9, 13 + i) if i == 2 else None,
            "Planning Permission  Granted": None, "Planning Permission Expired": None,
            "Under Construction": None, "Operational": None,
        })
    return rows


def _csv_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (date, datetime)):
        return value.strftime("%d/%m/%Y")
    return str(value)


def make_csv(rows: list[dict], overrides: dict | None = None, columns: list[str] | None = None,
             newline: str = "\r\n", encoding: str = "cp1252") -> bytes:
    """Official-style CSV: cp1252, CRLF.  overrides[(ref, column)] = literal CSV text."""
    overrides = overrides or {}
    columns = columns or COLUMNS
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator=newline)
    writer.writerow(columns)
    for row in rows:
        writer.writerow([overrides.get((row["Ref ID"], c), _csv_text(row.get(c))) for c in columns])
    return buffer.getvalue().encode(encoding)


def make_xlsx(rows: list[dict], formats: dict | None = None, overrides: dict | None = None,
              columns: list[str] | None = None) -> bytes:
    """Workbook with a notes sheet first and typed date cells.
    formats[(ref, column)] = number format; overrides[(ref, column)] = raw cell value."""
    formats, overrides = formats or {}, overrides or {}
    columns = columns or COLUMNS
    book = openpyxl.Workbook()
    book.active.title = "Definition Sheet"
    book.active.append(["notes"])
    sheet = book.create_sheet("REPD")
    sheet.append(columns)
    for r, row in enumerate(rows, start=2):
        for c, name in enumerate(columns, start=1):
            key = (row["Ref ID"], name)
            value = overrides.get(key, row.get(name))
            if isinstance(value, date) and not isinstance(value, datetime):
                value = datetime(value.year, value.month, value.day)
            if value is None or value == "":
                continue
            cell = sheet.cell(row=r, column=c, value=value)
            if isinstance(value, datetime):
                cell.number_format = formats.get(key, LOCALE_SHORT_DATE)
    out = io.BytesIO()
    book.save(out)
    return out.getvalue()


@pytest.fixture(scope="session")
def ingest():
    import repd_q3_2026_ingest
    return repd_q3_2026_ingest


@pytest.fixture(scope="session")
def q2():
    import repd_sources_v6
    return repd_sources_v6


@pytest.fixture(scope="session")
def rule():
    import repd_date_rule
    return repd_date_rule


@pytest.fixture
def run(ingest):
    """Run reconcile() on synthetic bytes.  previous defaults to a clean six-row release."""
    def _run(csv_bytes: bytes, xlsx_bytes: bytes, previous: bytes | None = None):
        kwargs = {}
        if "minimum_refs" in inspect.signature(ingest.reconcile).parameters:
            kwargs["minimum_refs"] = 0   # the 14,657 floor is a real-release constant
        return ingest.reconcile(csv_bytes, xlsx_bytes, previous if previous is not None else make_csv(base_rows()),
                                "synthetic previous release", True, **kwargs)
    return _run


def candidate_bytes(canonical) -> bytes:
    """Serialise exactly as main() does in the patched script."""
    out = io.BytesIO()
    canonical.to_csv(out, index=False, encoding="utf-8-sig", lineterminator="\n")
    return out.getvalue()
