"""Evidence for the capacity-precision question of the M5 REPD record join (offline replica of
tools/lightning/src/11b-repd-records.js RpQ/RpZ/RpJ, same rules as <workspace>/auto/gridatlas/scripts/m5_join_rate.py).

For every drawn-register row (globalgrid2050 dist/repd_master.json, 10,784 rows, no ref) it records which record
it joins in Q2 (202608290716) and in the October preview (202611132345, CSV precision), then:
 1. classifies the rows that joined in Q2 but not in October (why the 80 are lost: ref no longer active, MW,
    name, point or technology changed in REPD, or a new same-point twin made it ambiguous);
 2. measures what Excel full precision would do: for each October join, the ref's capacity in the staged file
    (Q3_CANONICAL_STAGED.csv, XLSX precision) versus the CSV value; any difference breaks the exact MW match;
 3. reports the register's own capacity precision (decimal places), which decides which source precision can match.
Usage: python3 -I m5_precision_evidence.py <register.json> <q2.parquet> <oct.parquet> <staged_xlsx_precision.csv> <out.json> <oct_csv_precision.csv>
Excel effect is measured raw-against-raw (staged XLSX value vs the CSV-precision input value for the same ref), because the
compiler rescales biomass >100 MW and solar_roof >50 MW by /1000 before writing capacity_mw.
"""
import csv, json, re, sys, unicodedata
from collections import defaultdict, Counter
import duckdb

EPS = 1.000001e-6


def rpz(s):
    s = '' if s is None else str(s)
    s = re.sub(r'[\x80-\x9f]', lambda m: bytes([ord(m.group())]).decode('cp1252', errors='replace'), s)
    return ' '.join(unicodedata.normalize('NFC', s).split())


def n(v):
    try:
        v = float(v)
    except (TypeError, ValueError):
        return 0.0
    return v if v > 0 else 0.0


def load(parquet):
    rows = duckdb.connect().execute(
        f"SELECT repd_ref, name, capacity_mw, repd_technology, longitude, latitude, status FROM read_parquet('{parquet}')").fetchall()
    grid = defaultdict(list)
    for r in rows:
        grid[(round(r[4], 4), round(r[5], 4))].append(r)
    return rows, grid


def cands_at(grid, x, y):
    out = {}
    for dx in (-1e-4, 0, 1e-4):
        for dy in (-1e-4, 0, 1e-4):
            for r in grid.get((round(x + dx, 4), round(y + dy, 4)), []):
                if abs(r[4] - x) <= EPS and abs(r[5] - y) <= EPS:
                    out[r[0]] = r
    return list(out.values())


def join(grid, f):
    x, y = f['geometry']['coordinates'][:2]
    p = f['properties']
    c = [r for r in cands_at(grid, x, y)
         if rpz(r[1]) == rpz(p.get('name')) and abs(n(r[2]) - n(p.get('capacity'))) < 1e-6 and r[3] == p.get('raw_tech')]
    return c


def decimals(v):
    s = repr(float(v)) if v not in (None, '') else ''
    return len(s.split('.')[1].rstrip('0')) if '.' in s else 0


def main(reg, q2p, octp, staged, out, csvp):
    feats = json.load(open(reg, encoding='utf-8'))['features']
    q2rows, q2 = load(q2p)
    octrows, oc = load(octp)
    octby = {r[0]: r for r in octrows}
    xl = {}
    with open(staged, encoding='utf-8-sig', newline='') as fh:
        for row in csv.DictReader(fh):
            ref = (row.get('Ref ID') or '').strip()
            xl[ref] = (row.get('Installed Capacity (MWelec)') or '').strip()
    cs = {}
    with open(csvp, encoding='utf-8-sig', newline='') as fh:
        for row in csv.DictReader(fh):
            cs[(row.get('Ref ID') or '').strip()] = (row.get('Installed Capacity (MWelec)') or '').strip()
    res = Counter(); lost = Counter(); lost_ex = defaultdict(list)
    xl_break = 0; xl_ex = []; reg_dec = Counter()
    for f in feats:
        p = f['properties']
        reg_dec[decimals(p.get('capacity') or 0)] += 1
        a, b = join(q2, f), join(oc, f)
        ka = 'one' if len(a) == 1 else ('none' if not a else 'multi')
        kb = 'one' if len(b) == 1 else ('none' if not b else 'multi')
        res[(ka, kb)] += 1
        if ka == 'one' and kb != 'one':
            ref = a[0][0]; o = octby.get(ref)
            if kb == 'multi':
                why = 'ambiguous in October (a second record now shares point, name, MW and technology)'
            elif o is None:
                why = 'ref not in the October snapshot (left the active statuses, outside bbox or withdrawn)'
            else:
                d = []
                if abs(o[4] - a[0][4]) > EPS or abs(o[5] - a[0][5]) > EPS: d.append('point')
                if rpz(o[1]) != rpz(a[0][1]): d.append('name')
                if abs(n(o[2]) - n(a[0][2])) >= 1e-6: d.append('MW')
                if o[3] != a[0][3]: d.append('technology')
                why = 'October record changed: ' + ('+'.join(d) or 'other')
            lost[why] += 1
            if len(lost_ex[why]) < 6:
                lost_ex[why].append({'ref': ref, 'register_name': p.get('name'), 'q2': [a[0][1], a[0][2], a[0][6]],
                                     'oct': None if o is None else [o[1], o[2], o[6], round(o[4], 6), round(o[5], 6)]})
        if kb == 'one':
            ref = b[0][0]; v = xl.get(ref, ''); c0 = cs.get(ref, '')
            if v != c0 and abs(n(v) - n(c0)) >= 1e-6:
                xl_break += 1
                if len(xl_ex) < 10:
                    xl_ex.append({'ref': ref, 'name': b[0][1], 'csv_mw': c0, 'parquet_mw': b[0][2], 'xlsx_mw': v, 'register_mw': p.get('capacity')})
    q2_one = sum(v for (a, b), v in res.items() if a == 'one')
    oct_one = sum(v for (a, b), v in res.items() if b == 'one')
    rep = {
        'register_rows': len(feats),
        'joined_q2_202608290716': q2_one,
        'joined_oct_csv_precision_202611132345': oct_one,
        'transition_q2_to_oct': {f'{a}->{b}': v for (a, b), v in sorted(res.items())},
        'lost_q2_to_oct_by_reason': dict(lost.most_common()),
        'lost_examples': lost_ex,
        'oct_joins_broken_by_xlsx_precision': xl_break,
        'oct_joined_with_xlsx_precision_upper_bound': oct_one - xl_break,
        'xlsx_break_examples': xl_ex,
        'register_capacity_decimal_places': dict(sorted(reg_dec.items())),
    }
    json.dump(rep, open(out, 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in rep.items() if not k.endswith('examples')}, indent=1))


if __name__ == '__main__':
    main(*sys.argv[1:7])
