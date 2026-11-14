"""A3: what GridAtlas returns for each MAP link of the operative Pipeline News page (uk_renewables_pipeline/202611132345),
live generation 202610312138 (records parquet 202608290716, Q2) versus the October preview 202611132345.

Offline replica of two receivers, read from the shipped code (not run in a browser):
 - identity card: place-global-search receiveExactRepdDeepLink (atlas/cartridges/202611132345-place-global-search-v9-5.js
   :695-850; the live 202609071213 cartridge has the same branch structure): exact repd_ref in the records parquet ->
   RESOLVED (register point; else Crown Estate lease point from atlas/data/offshore-coordinates.json; else the link's point)
   or RESOLVED_UNMAPPED; no exact ref -> NOT_IN_ACTIVE_REGISTER (no card; link fields kept). hasSafeMapPoint rejects 0,0 and
   the BNG false origin (-7.55716, 49.766807).
 - point and grid maths: sld-sandbox arrival (atlas/cartridges/202609241334-sld-sandbox-v9-8.js :6362-6620) measures from the
   link's latitude/longitude whenever they are usable, independent of the register; refuses the false origin.
Usage: python3 -I a3_map_links.py <pipeline release dir> <gridatlas work dir> <previous operative release dir> <out.json>
"""
import glob, json, math, sys
from collections import Counter
import duckdb

FO = (-7.55716, 49.766807)


def safe(lon, lat):
    if lon is None or lat is None or not (math.isfinite(lon) and math.isfinite(lat)):
        return False
    if abs(lon) < 1e-12 and abs(lat) < 1e-12:
        return False
    if abs(lat - FO[1]) < 1e-9 and abs(lon - FO[0]) < 1e-9:
        return False
    return -180 <= lon <= 180 and -90 <= lat <= 90


def km(a, b):
    R = 6378.137; d = math.pi / 180
    dl, dp = (b[0] - a[0]) * d, (b[1] - a[1]) * d
    h = math.sin(dp / 2) ** 2 + math.cos(a[1] * d) * math.cos(b[1] * d) * math.sin(dl / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(h), math.sqrt(1 - h))


def rows_of(rel):
    out = []
    for f in sorted(glob.glob(f'{rel}/data/v9.1/projects/part-*.json')):
        out += json.load(open(f, encoding='utf-8'))['projects']
    return out


def main(rel, work, prev, outp):
    proj = rows_of(rel)
    prev_refs = {p['repd_ref'] for p in rows_of(prev)} if prev else set()
    lease = {str(c['repd_ref']): c for c in json.load(open(f'{work}/atlas/data/offshore-coordinates.json'))['coordinates']
             if c.get('longitude') is not None}
    regs = {}
    for g, pq in (('live_202610312138', '202608290716'), ('preview_202611132345', '202611132345')):
        regs[g] = {r[0]: r for r in duckdb.connect().execute(
            f"SELECT repd_ref, name, longitude, latitude, capacity_mw, technology FROM read_parquet('{work}/data/repd_projects_{pq}.parquet')").fetchall()}
    res = []
    for p in proj:
        ref = str(p['repd_ref']); lon, lat = p.get('longitude'), p.get('latitude')
        link_ok = safe(lon, lat)
        row = {'repd_ref': ref, 'name': p['name'], 'technology': p.get('technology'), 'new_vs_202609082224': ref not in prev_refs,
               'link_has_point': link_ok, 'arrival_point_and_grid_maths': 'MEASURED_FROM_LINK_POINT' if link_ok else 'NOT_MEASURED'}
        for g, reg in regs.items():
            r = reg.get(ref)
            if r is None:
                st = 'NOT_IN_ACTIVE_REGISTER (no identity card; map point from link only)' if link_ok else 'NOT_IN_ACTIVE_REGISTER and no link point (lands nowhere)'
                extra = None
            else:
                if safe(r[2], r[3]):
                    src = 'register'
                    pt = (r[2], r[3])
                elif ref in lease:
                    src = 'crown_estate_lease'; pt = (lease[ref]['longitude'], lease[ref]['latitude'])
                elif link_ok:
                    src = 'link'; pt = (lon, lat)
                else:
                    src = None; pt = None
                st = f'RESOLVED ({src} point)' if src else 'RESOLVED_UNMAPPED (identity, map not moved)'
                extra = {'register_name_differs': r[1].strip() != (p['name'] or '').strip(),
                         'card_point_vs_link_point_km': round(km(pt, (lon, lat)), 3) if (pt and link_ok) else None}
            row[g] = st
            row[g + '_detail'] = extra
        res.append(row)
    summ = {}
    for subset, flt in (('all_rows', lambda r: True), ('new_vs_202609082224', lambda r: r['new_vs_202609082224'])):
        s = [r for r in res if flt(r)]
        summ[subset] = {'rows': len(s)}
        for g in regs:
            summ[subset][g] = dict(Counter(r[g] for r in s).most_common())
            summ[subset][g + '_card_point_over_1km_from_link'] = sum(1 for r in s if (r[g + '_detail'] or {}).get('card_point_vs_link_point_km') and r[g + '_detail']['card_point_vs_link_point_km'] > 1)
            summ[subset][g + '_register_name_differs'] = sum(1 for r in s if (r[g + '_detail'] or {}).get('register_name_differs'))
        summ[subset]['arrival'] = dict(Counter(r['arrival_point_and_grid_maths'] for r in s))
    gap = [r for r in res if r['live_202610312138'].startswith('NOT_IN') and not r['preview_202611132345'].startswith('NOT_IN')]
    summ['closed_by_preview'] = len(gap)
    summ['still_not_in_preview'] = Counter(r['preview_202611132345'] for r in res if r['preview_202611132345'].startswith('NOT_IN'))
    far = sorted([r for r in res if ((r['preview_202611132345_detail'] or {}).get('card_point_vs_link_point_km') or 0) > 1],
                 key=lambda r: -r['preview_202611132345_detail']['card_point_vs_link_point_km'])
    summ['preview_card_vs_link_over_1km_examples'] = [f"{r['repd_ref']} {r['name']} {r['preview_202611132345_detail']['card_point_vs_link_point_km']} km" for r in far[:10]]
    json.dump({'summary': summ, 'rows': res}, open(outp, 'w'), indent=0, ensure_ascii=False, default=list)
    print(json.dumps(summ, indent=1, default=dict))


if __name__ == '__main__':
    main(*sys.argv[1:5])
