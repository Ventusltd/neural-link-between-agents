#!/usr/bin/env python3
"""Independent: every non-date cell, official CSV text vs XLSX value (Team 1). usage: textdiff_csv_xlsx.py CSV XLSX"""
import csv, io, re, sys
from collections import Counter
from datetime import datetime
import openpyxl
DATE = {"Record Last Updated (dd/mm/yyyy)","Judicial Review","Planning Application Submitted","Planning Application Withdrawn","Planning Permission Refused","Appeal Lodged","Appeal Withdrawn","Appeal Refused","Appeal Granted","Planning Permission Granted","Secretary of State - Intervened","Secretary of State - Refusal","Secretary of State - Granted","Planning Permission Expired","Under Construction","Operational"}
n = lambda h: " ".join(str(h).split())
rows = list(csv.reader(io.StringIO(open(sys.argv[1], "rb").read().decode("cp1252"), newline="")))
H = [n(h) for h in rows[0]]; ri = H.index("Ref ID")
c = {}
for r in rows[1:]: c.setdefault(r[ri].strip(), r)
ws = openpyxl.load_workbook(sys.argv[2], read_only=True, data_only=True)["REPD"]
it = ws.iter_rows(values_only=True); next(it)
cat = Counter(); text = []; cap = Counter(); capcells = []
norm = lambda s: re.sub(r"[\s​-‍﻿]+", " ", s).strip()
def num(s):
    try: return float(str(s).replace(",", "").strip())
    except ValueError: return None
for x in it:
    if all(v is None for v in x): continue
    ref = str(int(x[ri])) if isinstance(x[ri], (int, float)) else str(x[ri]).strip()
    r = c[ref]
    for i, h in enumerate(H):
        if h in DATE: continue
        xv = x[i] if i < len(x) else None
        cv = r[i]
        if isinstance(xv, datetime) and xv < datetime(1900, 3, 1): continue  # numbers stored as dates
        xs = "" if xv is None else (str(int(xv)) if isinstance(xv, float) and xv.is_integer() else str(xv))
        if norm(cv) == norm(xs): continue
        a, b = num(cv), num(xv) if not isinstance(xv, str) else num(xv)
        if a is not None and b is not None:
            k = "numeric_equal" if a == b else ("numeric_rounded<=0.005" if abs(a - b) <= 0.0050001 else "NUMERIC_DIFFERENT")
        else:
            k = "TEXT_DIFFERENT"; text.append((ref, h, cv, xs))
        cat[(h, k)] += 1
        if h == "Installed Capacity (MWelec)" and a is not None and b is not None and a != b:
            if a >= 1 > b: capcells.append((ref, r[H.index("Technology Type")], r[H.index("Development Status (short)")], cv, b))
print(dict(cat)); print("TEXT_DIFFERENT cells:", [(r_, h, repr(a_), repr(b_)) for r_, h, a_, b_ in text])
print("capacity: CSV >= 1 but XLSX < 1:", len(capcells), Counter((t, s) for _, t, s, _, _ in capcells).most_common(6))
