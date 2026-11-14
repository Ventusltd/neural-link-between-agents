#!/usr/bin/env python3
"""Compare project_identity JSON files record by record (ignores validated_at). usage: cmp_identity.py A B [label]"""
import json, sys
from collections import Counter

a, b = (json.load(open(p)) for p in sys.argv[1:3])
top = sorted(k for k in set(a) | set(b) if k != "records" and a.get(k) != b.get(k))
print("top-level keys differing:", {k: (a.get(k), b.get(k)) for k in top if k != "validated_at"} or "none (validated_at only)" if top else "none")
ka = {r["gg_project_id"]: r for r in a["records"]}
kb = {r["gg_project_id"]: r for r in b["records"]}
print("records", len(ka), len(kb), "only_a", len(set(ka) - set(kb)), "only_b", len(set(kb) - set(ka)))
fields = Counter()
ex = {}
for k in set(ka) & set(kb):
    for f in set(ka[k]) | set(kb[k]):
        if ka[k].get(f) != kb[k].get(f):
            fields[f] += 1
            ex.setdefault(f, (k, ka[k].get(f), kb[k].get(f)))
print("field differences:", dict(fields))
for f, e in ex.items():
    print("  e.g.", f, e)
print("order equal:", [r["gg_project_id"] for r in a["records"]] == [r["gg_project_id"] for r in b["records"]])
