#!/usr/bin/env python3
"""Task 8: hunt source anomalies in the cleaned October file (report only).
usage: anomalies.py CLEANED.csv KNOWN.json PREV_IDENTITY_V6.json OUT.json"""
import csv, json, re, sys
from collections import Counter, defaultdict
from datetime import date, datetime

cl, kn, prev, out = sys.argv[1:5]
rows = list(csv.DictReader(open(cl, encoding="utf-8", newline="")))
rows = [{" ".join(k.split()): v for k, v in r.items()} for r in rows]
known = json.load(open(kn))["known"]
P = {r["repd_ref"]: r for r in json.load(open(prev))["records"]}
refs = {r["Ref ID"] for r in rows}
D = lambda s: datetime.strptime(s, "%d/%m/%Y").date() if s else None
AS_OF = date(2026, 11, 13)
A = defaultdict(list)

def add(kind, r, detail):
    A[kind].append({"ref": r["Ref ID"], "site": r["Site Name"][:60], "detail": detail, "known": r["Ref ID"] in known})

for r in rows:
    sub, gr, ref_, ex = D(r["Planning Application Submitted"]), D(r["Planning Permission Granted"]), D(r["Planning Permission Refused"]), D(r["Planning Permission Expired"])
    uc, op, upd = D(r["Under Construction"]), D(r["Operational"]), D(r["Record Last Updated (dd/mm/yyyy)"])
    st = r["Development Status (short)"].strip()
    for name in ("Planning Application Submitted", "Planning Permission Granted", "Under Construction", "Operational",
                 "Record Last Updated (dd/mm/yyyy)", "Appeal Lodged", "Appeal Granted", "Planning Permission Refused"):
        d = D(r[name])
        if d and d > AS_OF:
            add("FUTURE_EVENT_DATE", r, f"{name} {r[name]}")
        if d and d.year < 1980:
            add("VERY_OLD_DATE", r, f"{name} {r[name]}")
    if upd and upd > AS_OF:
        pass
    if gr and sub and gr < sub:
        add("GRANTED_BEFORE_SUBMITTED", r, f"submitted {sub} granted {gr}")
    if ex and gr and ex < gr:
        add("EXPIRED_BEFORE_GRANTED", r, f"granted {gr} expired {ex}")
    if op and uc and op < uc:
        add("OPERATIONAL_BEFORE_CONSTRUCTION", r, f"uc {uc} op {op}")
    if op and sub and op < sub and (sub - op).days > 365:
        add("OPERATIONAL_LONG_BEFORE_SUBMISSION", r, f"sub {sub} op {op}")
    if st == "Operational" and not op:
        add("STATUS_OPERATIONAL_NO_DATE", r, "")
    if st in ("Application Submitted", "Awaiting Construction") and op:
        add("PRE_OPERATIONAL_STATUS_WITH_OPERATIONAL_DATE", r, f"{st} op {op}")
    cap = r["Installed Capacity (MWelec)"].strip().replace(",", "")
    if cap:
        try:
            c = float(cap)
            if c <= 0:
                add("CAPACITY_NON_POSITIVE", r, cap)
            if c > 4000:
                add("CAPACITY_VERY_LARGE", r, cap)
        except ValueError:
            add("CAPACITY_NON_NUMERIC", r, cap)
    for col in ("Storage Co-location REPD Ref ID", "Are they re-applying (New REPD Ref)", "Are they re-applying (Old REPD Ref)"):
        v = r[col].strip()
        for tok in re.findall(r"\d+", v):
            if tok not in refs and col != "Are they re-applying (Old REPD Ref)":
                add("DANGLING_CROSS_REFERENCE", r, f"{col}={v!r} -> {tok} not in release")
        if v and v == r["Ref ID"]:
            add("SELF_REFERENCE", r, f"{col}={v}")
    for col in ("Site Name", "Address", "Operator (or Applicant)"):
        v = r[col]
        if re.search(r"Ã.|â€", v):
            add("MOJIBAKE_IN_SOURCE", r, f"{col}: {v[:70]!r}")
        if re.search(r"\w\?\w|\s\?\w", v):
            add("QUESTION_MARK_REPLACEMENT_CHAR", r, f"{col}: {v[:70]!r}")
    if r["Technology Type"].strip() == "Solar Photovoltaics" and r["No. of Turbines"].strip() not in ("", "0"):
        add("SOLAR_WITH_TURBINES", r, r["No. of Turbines"])
    # status regressions vs July
    p = P.get(r["Ref ID"])
    if p:
        order = {"Application Submitted": 1, "Awaiting Construction": 2, "Under Construction": 3, "Operational": 4}
        a, b = order.get(p["status"]), order.get(st)
        if a and b and b < a:
            add("STATUS_REGRESSION_VS_JULY", r, f"{p['status']} -> {st}")
        if p.get("planning_authority") and r["Planning Authority"].strip() and p["planning_authority"] != r["Planning Authority"].strip():
            add("PLANNING_AUTHORITY_TEXT_CHANGED_VS_JULY", r, f"{p['planning_authority']!r} -> {r['Planning Authority'].strip()!r}")
        if p.get("site_name") and p["site_name"] != " ".join(r["Site Name"].split()):
            add("SITE_NAME_CHANGED_VS_JULY", r, f"{p['site_name'][:40]!r} -> {r['Site Name'][:40]!r}")
        if p.get("repd_record_updated") and upd and D(p["repd_record_updated_raw"]) and upd < D(p["repd_record_updated_raw"]):
            add("RECORD_LAST_UPDATED_WENT_BACKWARDS", r, f"{p['repd_record_updated_raw']} -> {r['Record Last Updated (dd/mm/yyyy)']}")

# duplicate site name + coordinates across refs
key = defaultdict(list)
for r in rows:
    if r["X-coordinate"].strip() and r["Site Name"].strip():
        key[(r["Site Name"].strip().lower(), r["X-coordinate"].strip(), r["Y-coordinate"].strip(), r["Technology Type"], r["Development Status (short)"])].append(r["Ref ID"])
dups = {"|".join(k[:1] + k[3:]): v for k, v in key.items() if len(v) > 1}
summary = {k: {"count": len(v), "unknown": sum(not x["known"] for x in v)} for k, v in sorted(A.items())}
json.dump({"summary": summary, "same_name_coords_tech_status_groups": len(dups),
           "same_name_examples": dict(list(dups.items())[:15]), "anomalies": A}, open(out, "w"), indent=1, ensure_ascii=False)
print(json.dumps(summary, indent=1)); print("same name+coords+tech+status groups:", len(dups))
