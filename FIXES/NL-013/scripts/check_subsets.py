#!/usr/bin/env python3
"""Task 4: first-principles subset filters, validated against January (main) and applied to October.
usage: check_subsets.py JAN_ROOT OCT_ROOT"""
import csv, io, json, sys
from collections import Counter
from pathlib import Path

jan, octo = Path(sys.argv[1]), Path(sys.argv[2])
norm = lambda h: " ".join(h.replace("﻿", "").split())


def read(p):
    raw = p.read_bytes()
    for enc in ("utf-8-sig", "cp1252"):
        try:
            t = raw.decode(enc); break
        except UnicodeDecodeError:
            continue
    rows = list(csv.reader(io.StringIO(t, newline="")))
    return rows[0], rows[1:], enc, raw


def cap(s):
    try:
        return float(s.replace(",", "").strip())
    except ValueError:
        return None


def analyse(root, suffix):
    out = {}
    h, body, enc, raw = read(root / f"repd{suffix}.csv")
    n = [norm(x) for x in h]
    I = {k: i for i, k in enumerate(n)}
    out["full"] = {"rows": len(body), "cols": len(h), "enc": enc, "bom": raw.startswith(b"\xef\xbb\xbf"),
                   "crlf": raw.count(b"\r\n")}
    refs = [r[I["Ref ID"]].strip() for r in body]
    tech, stat, capc, mnt = I["Technology Type"], I["Development Status (short)"], I["Installed Capacity (MWelec)"], I["Mounting Type for Solar"]
    for name, fn, hdr in (
        ("repd-grid-batteries", lambda r: r[tech].strip() == "Battery", None),
        ("repd-solar-operational", lambda r: r[tech].strip() == "Solar Photovoltaics" and r[stat].strip() == "Operational"
         and (cap(r[capc]) or 0) > 1 and r[mnt].strip() in ("Ground", "Roof"), None),
        ("repd-solar-operational-over-4mw", lambda r: r[tech].strip() == "Solar Photovoltaics" and r[stat].strip() == "Operational"
         and (cap(r[capc]) or 0) > 4, None)):
        sh, sb, senc, sraw = read(root / f"{name}{suffix}.csv")
        ragged = sum(len(r) != len(sh) for r in sb)
        sb = [r for r in sb if len(r) == len(sh)]
        sn = [norm(x) for x in sh]
        sref = [r[sn.index("Ref ID")].strip() for r in sb]
        cand = [r for r in body if fn(r)]
        info = {"ragged_records_dropped_for_check": ragged, "rows": len(sb), "cols": len(sh), "enc": senc, "bom": sraw.startswith(b"\xef\xbb\xbf"),
                "crlf": sraw.count(b"\r\n"), "dup_refs": len(sref) - len(set(sref)),
                "header_is_subset_of_full_in_order": [x for x in n if x in set(sn)] == sn}
        if name == "repd-grid-batteries":
            st = Counter(r[stat].strip() for r in cand)
            kept = Counter(r[sn.index("Development Status (short)")].strip() for r in sb)
            info["battery_status_all"] = dict(st)
            info["battery_status_kept"] = dict(kept)
            keepset = set(kept)
            cand = [r for r in cand if r[stat].strip() in keepset]
        cref = [r[I["Ref ID"]].strip() for r in cand]
        info["first_principles_rows"] = len(cand)
        info["refs_missing_from_subset"] = sorted(set(cref) - set(sref), key=int)[:20]
        info["refs_extra_in_subset"] = sorted(set(sref) - set(cref), key=lambda x: int(x) if x.isdigit() else 0)[:20]
        info["order_equal"] = cref == sref
        # every cell equal to the full file's cell (by column name)
        byref = {r[I["Ref ID"]].strip(): r for r in body}
        bad = 0
        for r in sb:
            f = byref.get(r[sn.index("Ref ID")].strip())
            if f is None or any(r[j] != f[I[c]] for j, c in enumerate(sn)):
                bad += 1
        info["rows_not_equal_to_full"] = bad
        out[name] = info
    return out


res = {"january_main": analyse(jan, ""), "october_pr": analyse(octo, "-2026q3")}
print(json.dumps(res, indent=1))
