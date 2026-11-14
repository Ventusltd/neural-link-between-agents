"""Independent 53-column Ref-ID diff of two official-layout REPD CSVs (no automation/repd code).
usage: indep_diff.py PREV.csv NEW.csv OUT.json
Each changed cell on a retained ref is classified:
  whitespace   equal after collapsing whitespace (incl. NBSP, CR/LF, zero-width)
  case         equal after whitespace collapse + casefold
  spacing      equal after deleting all whitespace (line-break removal such as 'Road\n, Town' -> 'Road, Town')
  separator_slash_to_ampersand  equal after mapping '/' to '&' (October joint-operator style)
  numeric      both parse as numbers and are equal within 0.0051
  date         both parse as dd/mm/yyyy (or d/m/yyyy, ISO) to the same date
  material     anything else (blank<->value counts here, split out as filled/blanked)"""
import csv, io, json, re, sys, collections, datetime
def load(p):
    raw = open(p, 'rb').read()
    for enc in ('utf-8-sig', 'cp1252'):
        try: txt = raw.decode(enc); break
        except UnicodeDecodeError: pass
    rows = list(csv.reader(io.StringIO(txt, newline='')))
    hdr = [' '.join(h.split()) for h in rows[0]]
    recs, dups = {}, []
    for r in rows[1:]:
        if not any(c.strip() for c in r): continue
        ref = r[1].strip()
        if ref in recs:
            dups.append([ref, recs[ref] == r]); continue
        recs[ref] = r
    return hdr, recs, dups, enc
WS = re.compile(r'[\s ​‌‍﻿]+')
def ws(s): return WS.sub(' ', s).strip()
def num(s):
    try: return float(ws(s).replace(',', ''))
    except ValueError: return None
def dt(s):
    s = ws(s)
    for f in ('%d/%m/%Y', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S'):
        try: return datetime.datetime.strptime(s, f).date()
        except ValueError: pass
    return None
def classify(a, b):
    if ws(a) == ws(b): return 'whitespace'
    if ws(a).casefold() == ws(b).casefold(): return 'case'
    if WS.sub('', a).casefold() == WS.sub('', b).casefold(): return 'spacing'
    if WS.sub('', a.replace('/', '&')).casefold() == WS.sub('', b.replace('/', '&')).casefold(): return 'separator_slash_to_ampersand'
    if not ws(a): return 'material_filled'
    if not ws(b): return 'material_blanked'
    na, nb = num(a), num(b)
    if na is not None and nb is not None and abs(na - nb) <= 0.0051: return 'numeric'
    da, db = dt(a), dt(b)
    if da and db and da == db: return 'date'
    return 'material_changed'
ph, P, pd_, pe = load(sys.argv[1]); nh, N, nd, ne = load(sys.argv[2])
assert ph == nh, 'headers differ'
added = sorted(set(N) - set(P), key=int); removed = sorted(set(P) - set(N), key=int)
kept = sorted(set(P) & set(N), key=int)
cols = collections.OrderedDict((h, collections.Counter()) for h in ph)
examples = collections.defaultdict(list)
refs_material = set()
for ref in kept:
    a, b = P[ref], N[ref]
    for i, h in enumerate(ph):
        if a[i] == b[i]: continue
        c = classify(a[i], b[i])
        cols[h][c] += 1
        if c.startswith('material'):
            refs_material.add(ref)
            if len(examples[h]) < 5: examples[h].append([ref, a[i], b[i]])
out = {'previous': {'file': sys.argv[1].split('/')[-1], 'encoding': pe, 'refs': len(P), 'duplicate_rows': pd_},
       'new': {'file': sys.argv[2].split('/')[-1], 'encoding': ne, 'refs': len(N), 'duplicate_rows': nd},
       'added': len(added), 'removed': len(removed), 'retained': len(kept),
       'removed_refs': removed, 'added_refs': added,
       'retained_refs_with_material_change': len(refs_material),
       'columns': {h: dict(c) for h, c in cols.items()},
       'material_by_column': {h: sum(v for k, v in c.items() if k.startswith('material')) for h, c in cols.items()},
       'examples': examples}
json.dump(out, open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
print('added', len(added), 'removed', len(removed), 'retained', len(kept), 'refs w/ material change', len(refs_material))
for h, c in cols.items():
    if c: print(f'  {h:45s} {dict(c)}')
