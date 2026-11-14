#!/usr/bin/env python3
"""Independent re-derivation of repd-2026q3.csv from the official CSV + XLSX (Team 1, task 1).

Written from the stated policy only (docs/repd/2026q3/CLEANING-LOG.txt header), not from clean.py:
  * drop byte-identical duplicate records (keep first)
  * the 16 date columns: value = Excel typed date as dd/mm/yyyy; blank where Excel is blank
  * non-date cells whose workbook value is a number < 61 shown with a date format: workbook number
  * other cells: strip an edge whitespace run only if it contains TAB/CR/LF; inner line-break runs -> ' '
Then compare with the official CSV (count and classify every changed cell) and with the PR's file.
usage: rederive.py OFFICIAL.csv OFFICIAL.xlsx PR_repd-2026q3.csv OUTDIR
"""
import csv, hashlib, io, json, re, sys
from collections import Counter
from datetime import datetime, date
from pathlib import Path
import openpyxl

csv_p, xlsx_p, pr_p, out = map(Path, sys.argv[1:5])
out.mkdir(parents=True, exist_ok=True)
DATE_COLS = {"Record Last Updated (dd/mm/yyyy)", "Judicial Review", "Planning Application Submitted",
             "Planning Application Withdrawn", "Planning Permission Refused", "Appeal Lodged", "Appeal Withdrawn",
             "Appeal Refused", "Appeal Granted", "Planning Permission Granted", "Secretary of State - Intervened",
             "Secretary of State - Refusal", "Secretary of State - Granted", "Planning Permission Expired",
             "Under Construction", "Operational"}
norm = lambda h: " ".join(str(h).split())

raw = csv_p.read_bytes()
text = raw.decode("cp1252")          # official encoding per log; fail loudly otherwise
rows = list(csv.reader(io.StringIO(text, newline="")))
header, body = rows[0], rows[1:]
assert all(len(r) == len(header) for r in body), "field count"
names = [norm(h) for h in header]
ri = names.index("Ref ID")

wb = openpyxl.load_workbook(xlsx_p, read_only=True, data_only=True)
ws = wb["REPD"] if "REPD" in wb.sheetnames else wb.worksheets[0]
xit = ws.iter_rows()
xh = [norm(c.value) for c in next(xit) if c.value is not None]
assert xh == names, "header mismatch"
xrows = {}
xdup = Counter()
for r in xit:
    vals = [(c.value, getattr(c, "number_format", "General"), getattr(c, "is_date", False)) for c in r[:len(xh)]]
    vals += [(None, "General", False)] * (len(xh) - len(vals))
    if all(v[0] is None for v in vals):
        continue
    ref = vals[ri][0]
    ref = str(int(ref)) if isinstance(ref, (int, float)) else str(ref).strip()
    xdup[ref] += 1
    xrows.setdefault(ref, vals)

EDGE_L, EDGE_R = re.compile(r"^[ \t\r\n]+"), re.compile(r"[ \t\r\n]+$")
BRK = re.compile(r"[ \t]*[\r\n]+[ \t]*")

def clean_text(s):
    m = EDGE_L.match(s)
    if m and re.search(r"[\t\r\n]", m.group()):
        s = s[m.end():]
    m = EDGE_R.search(s)
    if m and re.search(r"[\t\r\n]", m.group()):
        s = s[:m.start()]
    return BRK.sub(" ", s)

def serial(d):
    # Excel 1900 system: before 1 Mar 1900 serial 1 = 1900-01-01 (phantom 29 Feb 1900 comes later)
    return (d - datetime(1899, 12, 31)).total_seconds() / 86400.0

seen, outrows, changes, removed = {}, [], [], []
kinds = Counter()
date_csv_agree = Counter()
for n, r in enumerate(body, 1):
    ref = r[ri].strip()
    if ref in seen:
        assert seen[ref] == r, f"conflicting duplicate {ref}"
        removed.append((ref, n)); continue
    seen[ref] = r
    x = xrows[ref]
    new = []
    for i, (name, before) in enumerate(zip(names, r)):
        xv, fmt, isd = x[i]
        if name in DATE_COLS:
            if isinstance(xv, (datetime, date)):
                d = xv.date() if isinstance(xv, datetime) else xv
                assert not (isinstance(xv, datetime) and xv.time() != datetime.min.time())
                after = d.strftime("%d/%m/%Y")
                cs = before.strip()
                if cs == after: k = "date_same"
                elif cs == d.strftime("%m/%d/%Y") or cs == f"{d.month}/{d.day}/{d.year}": k = "date_month_first"
                else: k = "date_other!"
            else:
                assert xv is None or (isinstance(xv, str) and xv.strip().casefold() in ("", "na", "n/a")), (ref, name, xv)
                after = ""
                cs = before.strip()
                k = "blank_same" if before == "" else ("date_na" if cs.casefold() in ("na", "n/a") else
                                                         ("date_ws" if cs == "" else "csv_date_excel_blank!"))
            date_csv_agree[k] += 1
            if after != before:
                kinds[k] += 1
        elif isinstance(xv, datetime) and xv < datetime(1900, 3, 1):
            s = serial(xv)
            after = str(int(s)) if s == int(s) else repr(s)
            assert before.strip() == xv.strftime("%d/%m/%Y"), (ref, name, before, xv)
            kinds["num_as_date"] += 1
        else:
            after = clean_text(before)
            if after != before:
                kinds["edge_control" if after == before.strip(" \t\r\n") and not BRK.search(before.strip(" \t\r\n")) else "linebreak_or_mixed"] += 1
        if after != before:
            changes.append({"ref": ref, "column": header[i], "before": before, "after": after})
        new.append(after)
    outrows.append(new)

buf = io.StringIO(newline="")
w = csv.writer(buf, lineterminator="\n")
w.writerow(header); w.writerows(outrows)
mine = buf.getvalue().encode("utf-8")
(out / "rederived-repd-2026q3.csv").write_bytes(mine)
pr = pr_p.read_bytes()

# cell-level comparison with the PR file
prrows = list(csv.reader(io.StringIO(pr.decode("utf-8"), newline="")))
cell_diffs = []
for a, b in zip(outrows, prrows[1:]):
    for i, (u, v) in enumerate(zip(a, b)):
        if u != v:
            cell_diffs.append({"ref": a[ri], "column": header[i], "mine": u, "pr": v})
rep = {
    "official_csv_sha256": hashlib.sha256(raw).hexdigest(),
    "official_xlsx_sha256": hashlib.sha256(xlsx_p.read_bytes()).hexdigest(),
    "official_records": len(body), "xlsx_records": sum(xdup.values()),
    "xlsx_duplicates": {k: v for k, v in xdup.items() if v > 1},
    "removed_duplicates": removed,
    "rows_out": len(outrows), "distinct_cells_changed": len(changes),
    "kinds": dict(kinds), "date_cells_by_class": dict(date_csv_agree),
    "mine_sha256": hashlib.sha256(mine).hexdigest(), "mine_bytes": len(mine),
    "pr_sha256": hashlib.sha256(pr).hexdigest(), "pr_bytes": len(pr),
    "byte_identical": mine == pr, "pr_rows": len(prrows) - 1, "cell_diffs_vs_pr": cell_diffs[:50],
    "cell_diff_count_vs_pr": len(cell_diffs),
}
(out / "rederive-report.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False))
(out / "rederive-changes.json").write_text(json.dumps(changes, indent=0, ensure_ascii=False))
print(json.dumps({k: v for k, v in rep.items() if k != "cell_diffs_vs_pr"}, indent=1))
