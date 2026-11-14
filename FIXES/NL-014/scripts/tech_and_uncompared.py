"""Pieces 5 and 6. usage: tech_and_uncompared.py PREV_clean.csv NEW_clean.csv OLD_diff.json INDEP.json OUTDIR
Blank capacity is unknown, never zero."""
import csv, json, math, sys, collections, datetime
prevp, newp, olddiff, indep, out = sys.argv[1:6]
def load(p):
    rows = list(csv.DictReader(open(p, encoding='utf-8-sig', newline='')))
    return {r['Ref ID'].strip(): r for r in rows}
P, N = load(prevp), load(newp)
CAP, T, S = 'Installed Capacity (MWelec)', 'Technology Type', 'Development Status (short)'
def mw(r):
    try: return float(r[CAP])
    except (ValueError, TypeError): return None
def agg(recs):
    n = len(recs); k = [mw(r) for r in recs]
    return n, sum(x for x in k if x is not None), sum(1 for x in k if x is None)
techs = sorted(set(r[T] for r in P.values()) | set(r[T] for r in N.values()))
added = set(N) - set(P); removed = set(P) - set(N); kept = set(P) & set(N)
LIVE = ['Application Submitted', 'Awaiting Construction', 'Under Construction', 'Operational']
md = ['# Per-technology quarter-on-quarter tables: July 2026 (Q2) -> October 2026 (Q3)', '',
      f'Inputs: {prevp.split("/")[-1]} ({len(P)} refs), {newp.split("/")[-1]} ({len(N)} refs). MW sums known capacities only; blank capacity is unknown, never zero.', '',
      '## Records and capacity by technology', '',
      '| Technology | Jul n | Oct n | Added | Removed | Jul MW | Oct MW | Delta MW | Unknown cap. Jul | Unknown cap. Oct | Status changes |', '|---|---|---|---|---|---|---|---|---|---|---|']
res = {}
for t in techs:
    p = [r for r in P.values() if r[T] == t]; n = [r for r in N.values() if r[T] == t]
    pn, pm, pu = agg(p); nn, nm, nu = agg(n)
    a = sum(1 for x in added if N[x][T] == t); rm = sum(1 for x in removed if P[x][T] == t)
    sc = sum(1 for x in kept if N[x][T] == t and P[x][S] != N[x][S])
    res[t] = dict(jul_n=pn, oct_n=nn, added=a, removed=rm, jul_mw=round(pm, 3), oct_mw=round(nm, 3), jul_unknown=pu, oct_unknown=nu, status_changes=sc)
    md.append(f'| {t} | {pn:,} | {nn:,} | {a} | {rm} | {pm:,.1f} | {nm:,.1f} | {nm-pm:+,.1f} | {pu} | {nu} | {sc} |')
tot = lambda d, k: sum(v[k] for v in res.values())
md.append(f'| **All** | {tot(res,"jul_n"):,} | {tot(res,"oct_n"):,} | {tot(res,"added")} | {tot(res,"removed")} | {tot(res,"jul_mw"):,.1f} | {tot(res,"oct_mw"):,.1f} | {tot(res,"oct_mw")-tot(res,"jul_mw"):+,.1f} | {tot(res,"jul_unknown")} | {tot(res,"oct_unknown")} | {tot(res,"status_changes")} |')
md += ['', '## Pipeline stage by technology (count / known MW), July -> October', '',
       '| Technology | ' + ' | '.join(LIVE) + ' |', '|---|' + '---|' * len(LIVE)]
stage = {}
for t in ['Solar Photovoltaics', 'Battery', 'Wind Onshore', 'Wind Offshore', 'Hydrogen', 'Pumped Storage Hydroelectricity']:
    cells = []
    for s in LIVE:
        a = agg([r for r in P.values() if r[T] == t and r[S] == s]); b = agg([r for r in N.values() if r[T] == t and r[S] == s])
        stage[f'{t}|{s}'] = dict(jul=[a[0], round(a[1], 1)], oct=[b[0], round(b[1], 1)])
        cells.append(f'{a[0]:,} / {a[1]:,.0f} -> {b[0]:,} / {b[1]:,.0f}')
    md.append(f'| {t} | ' + ' | '.join(cells) + ' |')
md += ['', '## Status transitions on retained records, by technology (top transitions)', '', '| Technology | From | To | n | MW (Oct capacity) |', '|---|---|---|---|---|']
tr = collections.Counter(); trmw = collections.Counter()
for x in kept:
    if P[x][S] != N[x][S]:
        k = (N[x][T], P[x][S], N[x][S]); tr[k] += 1; trmw[k] += mw(N[x]) or 0
for k, v in tr.most_common(25):
    md.append(f'| {k[0]} | {k[1]} | {k[2]} | {v} | {trmw[k]:,.1f} |')
open(f'{out}/../w5/TECH_TABLES.md', 'w').write('\n'.join(md) + '\n')
json.dump({'by_technology': res, 'stage': stage, 'transitions': [[*k, v, round(trmw[k], 3)] for k, v in tr.most_common()]}, open(f'{out}/../w5/tech_tables.json', 'w'), indent=1)
# ---- piece 6
old = json.load(open(olddiff)); unc = old['conventions']['columns_only_in_new']
ind = json.load(open(indep))
md = ['# Changes in the columns the earlier July->October report never compared', '',
      f'The earlier report (docs/repd/2026q3/changes-jul-to-oct, previous = derived project_identity_v6.json) compared 19 columns; {len(unc)} official columns were not compared. Counts below are retained refs (14,648) whose value changed, from clean.py output July vs clean.py output October, classified by scripts/indep_diff.py.', '',
      '| Column | Real change | of which filled (blank->value) | blanked (value->blank) | Formatting only (whitespace/spacing/separator/numeric form) |', '|---|---|---|---|---|']
for c in unc:
    d = ind['columns'].get(c, {})
    m = sum(v for k, v in d.items() if k.startswith('material'))
    f = sum(v for k, v in d.items() if not k.startswith('material'))
    md.append(f'| {c} | {m} | {d.get("material_filled",0)} | {d.get("material_blanked",0)} | {f} |')
# coordinates
X, Y = 'X-coordinate', 'Y-coordinate'
moves = []
for x in kept:
    a, b = P[x], N[x]
    if (a[X].strip(), a[Y].strip()) != (b[X].strip(), b[Y].strip()):
        try: d = math.hypot(float(b[X]) - float(a[X]), float(b[Y]) - float(a[Y]))
        except ValueError: d = None
        moves.append((x, a[T], a[X], a[Y], b[X], b[Y], d))
bands = collections.Counter()
for m in moves:
    d = m[6]
    bands['unparseable/blank' if d is None else '<100 m' if d < 100 else '100 m-1 km' if d < 1000 else '1-10 km' if d < 10000 else '10-100 km' if d < 100000 else '>100 km'] += 1
md += ['', f'## Coordinates (British National Grid easting/northing)', '', f'{len(moves)} retained records changed X and/or Y. Distance moved:', '']
for k in ['<100 m', '100 m-1 km', '1-10 km', '10-100 km', '>100 km', 'unparseable/blank']:
    md.append(f'- {k}: {bands[k]}')
big = [m for m in moves if m[6] and m[6] >= 10000]
md += ['', 'Moves of 10 km or more (open REPD data; likely corrections of misplaced points):', '', '| Ref | Technology | Jul X,Y | Oct X,Y | km |', '|---|---|---|---|---|']
for m in sorted(big, key=lambda m: -m[6]):
    md.append(f'| {m[0]} | {m[1]} | {m[2]},{m[3]} | {m[4]},{m[5]} | {m[6]/1000:,.1f} |')
# dates & refs detail
def detail(col):
    rows = [(x, P[x][col], N[x][col]) for x in sorted(kept, key=int) if P[x][col].strip() != N[x][col].strip()]
    return rows
for col in ['Appeal Lodged', 'Appeal Withdrawn', 'Appeal Refused', 'Appeal Granted', 'Secretary of State - Intervened', 'Secretary of State - Refusal', 'Secretary of State - Granted', 'Judicial Review', 'Appeal Reference', 'Secretary of State Reference', 'Type of Secretary of State Intervention']:
    r = detail(col)
    md += ['', f'### {col}: {len(r)} changed', '']
    for x, a, b in r[:20]:
        md.append(f'- ref {x}: "{a}" -> "{b}"')
md += ['', '### Planning Application Reference (compared earlier too; listed for completeness)', '']
for x, a, b in detail('Planning Application Reference'):
    if ' '.join(a.split()) != ' '.join(b.split()): md.append(f'- ref {x}: "{a.strip()}" -> "{b.strip()}"')
md += ['', '### Address: real changes after removing line breaks and spacing', '']
ad = [(x, a, b) for x, a, b in detail('Address') if ''.join(a.split()).casefold() != ''.join(b.split()).casefold()]
md.append(f'{len(ad)} retained records have a substantive address change (all other address differences are line-break/spacing removal by DESNZ).')
for x, a, b in ad[:20]: md.append(f'- ref {x}: "{" ".join(a.split())}" -> "{" ".join(b.split())}"')
open(f'{out}/UNCOMPARED_COLUMNS.md', 'w').write('\n'.join(md) + '\n')
json.dump({'uncompared_columns': unc, 'coordinate_moves': moves, 'bands': bands}, open(f'{out}/uncompared_columns.json', 'w'), indent=1)
print('ok', len(moves), dict(bands))
