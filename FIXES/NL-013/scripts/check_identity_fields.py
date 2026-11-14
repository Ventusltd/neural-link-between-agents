#!/usr/bin/env python3
"""Task 5: identity + major projects, field by field against the cleaned CSV; stability vs July.
usage: check_identity_fields.py CLEANED.csv IDENTITY_Q3.json MAJOR_Q3.json IDENTITY_JUL.json MAJOR_JUL.json"""
import csv, json, sys
from collections import Counter
from datetime import datetime

cl, idq, mpq, idj, mpj = sys.argv[1:6]
rows = list(csv.DictReader(open(cl, encoding="utf-8", newline="")))
norm = lambda h: " ".join(h.split())
rows = [{norm(k): v for k, v in r.items()} for r in rows]
by = {r["Ref ID"]: r for r in rows}
iso = lambda s: datetime.strptime(s, "%d/%m/%Y").date().isoformat() if s.strip() else None
txt = lambda s: (" ".join(s.split()) or None)

MAP = {"site_name": "Site Name", "technology": "Technology Type", "status": "Development Status (short)",
       "operator": "Operator (or Applicant)", "county": "County", "region": "Region", "country": "Country",
       "planning_authority": "Planning Authority", "planning_application_reference": "Planning Application Reference"}
DATES = {"planning_application_submitted": "Planning Application Submitted",
         "planning_application_withdrawn": "Planning Application Withdrawn",
         "planning_permission_refused": "Planning Permission Refused",
         "planning_permission_granted": "Planning Permission Granted",
         "planning_permission_expired": "Planning Permission Expired",
         "under_construction": "Under Construction", "operational": "Operational",
         "repd_record_updated": "Record Last Updated (dd/mm/yyyy)"}

I = json.load(open(idq))
mism = Counter(); ex = {}
cap_diff = Counter()
for r in I["records"]:
    c = by.get(r["repd_ref"])
    if c is None:
        mism["ref_missing_in_cleaned"] += 1; continue
    for f, col in MAP.items():
        if (r.get(f) or None) != txt(c[col]) and (r.get(f) or "").strip() != c[col].strip():
            mism[f] += 1; ex.setdefault(f, (r["repd_ref"], r.get(f), c[col]))
    for f, col in DATES.items():
        if r.get(f) != iso(c[col]):
            mism[f] += 1; ex.setdefault(f, (r["repd_ref"], r.get(f), c[col]))
    raw = c["Installed Capacity (MWelec)"].strip().replace(",", "")
    try:
        cv = float(raw) if raw else None
    except ValueError:
        cv = "NONNUM"
    if cv is None or cv == "NONNUM":
        if r["capacity_known"] or r["capacity_mw"] not in (None,):
            mism["capacity_blank_but_known"] += 1; ex.setdefault("capacity_blank_but_known", (r["repd_ref"], r["capacity_mw"], raw))
    else:
        d = abs((r["capacity_mw"] or 0) - cv)
        cap_diff["exact" if d == 0 else ("<=0.005" if d <= 0.0050001 else ">0.005")] += 1
        if d > 0.0050001:
            ex.setdefault("capacity_gt_tol", (r["repd_ref"], r["capacity_mw"], raw))
    if (r.get("repd_old_ref") or None) != (c["Old Ref ID"].strip() or None):
        mism["repd_old_ref"] += 1; ex.setdefault("repd_old_ref", (r["repd_ref"], r.get("repd_old_ref"), c["Old Ref ID"]))
print("identity records", len(I["records"]), "cleaned rows", len(rows), "refs equal", {r["repd_ref"] for r in I["records"]} == set(by))
print("identity field mismatches:", dict(mism) or "none"); [print("  e.g.", k, v) for k, v in ex.items()]
print("capacity vs cleaned CSV text:", dict(cap_diff))

# major projects selection from first principles (identity capacity, all statuses?)
M = json.load(open(mpq))
sel = {r["repd_ref"] for r in I["records"] if r["capacity_known"] and (
    (r["technology"] == "Solar Photovoltaics" and r["capacity_mw"] > 1.0) or
    (r["technology"] == "Battery" and r["capacity_mw"] > 100.0))}
got = {p["repd_ref"] for p in M["projects"]}
print("major projects", len(got), "first-principles", len(sel), "missing", sorted(sel - got)[:10], "extra", sorted(got - sel)[:10])
idx = {r["repd_ref"]: r for r in I["records"]}
pm = Counter()
for p in M["projects"]:
    r = idx[p["repd_ref"]]
    for f in set(p) & set(r):
        if p[f] != r[f]:
            pm[f] += 1
print("major vs identity shared-field mismatches:", dict(pm) or "none")

# stability vs July
J = json.load(open(idj))
jj = {r["repd_ref"]: r for r in J["records"]}
qq = idx
both = set(jj) & set(qq)
pid = sum(jj[k]["gg_project_id"] != qq[k]["gg_project_id"] for k in both)
dev = sum(jj[k]["gg_development_id"] != qq[k]["gg_development_id"] for k in both)
print(f"stability: July {len(jj)} Oct {len(qq)} shared {len(both)} removed {len(set(jj)-set(qq))} added {len(set(qq)-set(jj))}; "
      f"gg_project_id changed {pid}; gg_development_id changed {dev}")
devchg = [k for k in both if jj[k]["gg_development_id"] != qq[k]["gg_development_id"]]
print("  development id changes e.g.", sorted(devchg, key=int)[:15])
MJ = json.load(open(mpj))
print("major July", len(MJ["projects"]), "Oct", len(M["projects"]), "dropped refs", len({p['repd_ref'] for p in MJ['projects']} - got),
      "added", len(got - {p['repd_ref'] for p in MJ['projects']}))
