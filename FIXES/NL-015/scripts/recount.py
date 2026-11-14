# Independent recount of the pinned figures from the October CSV (repd-2026q3.csv) and the official CSV.
import csv, collections, json, sys, hashlib
def load(p):
    return list(csv.DictReader(open(p, encoding='utf-8-sig', newline='')))
src = sys.argv[1]
R = load(src)
print('rows', len(R), 'unique refs', len({r['Ref ID'] for r in R}))
print('tech types', collections.Counter(r['Technology Type'] for r in R).most_common())
TECH = {'Solar Photovoltaics': 'solar', 'Battery': 'bess', 'Wind Onshore': 'wind_onshore', 'Wind Offshore': 'wind_offshore'}
seen = {}; 
for r in R: seen.setdefault(r['Ref ID'], r)
inscope = []; blank = collections.Counter(); sub1 = collections.Counter()
for ref, r in seen.items():
    t = TECH.get(r['Technology Type'].strip())
    if not t: continue
    c = r['Installed Capacity (MWelec)'].strip().replace(',', '')
    if c == '': blank[t] += 1; continue
    c = float(c)
    if c < 1.0: sub1[t] += 1; continue
    inscope.append((ref, t, c, r))
cnt = collections.Counter(t for _, t, _, _ in inscope)
cap = round(sum(c for _, _, c, _ in inscope), 2)
largest = max(c for _, _, c, _ in inscope)
def coord(r):
    try: x = float(r['X-coordinate']); y = float(r['Y-coordinate']); return x, y
    except: return None
nocoord = sum(1 for *_, r in inscope if coord(r) is None)
out = dict(project_count=len(inscope), capacity_mw=cap, displayed=round(cap), largest_mw=largest, by_tech=dict(cnt),
           blank_capacity_in_4_techs=dict(blank), blank_total=sum(blank.values()), below_1mw=dict(sub1),
           no_xy_in_scope=nocoord,
           statuses=collections.Counter(r['Development Status (short)'] for *_, r in inscope).most_common(),
           status_long=collections.Counter(r['Development Status'] for *_, r in inscope).most_common(),
           no_application_made_all=sum(1 for r in R if 'no application made' in (r['Development Status']+r['Development Status (short)']).lower()),
           no_application_made_by_tech=collections.Counter(r['Technology Type'] for r in R if 'no application made' in (r['Development Status']+r['Development Status (short)']).lower()),
           no_application_made_inscope=[(ref, t, c) for ref, t, c, r in inscope if 'no application made' in (r['Development Status']+r['Development Status (short)']).lower()])
print(json.dumps(out, indent=1, default=str))
