# PRE-INTEGRATION on the integrator's base (hook table + loader already in index.html): our deletions by content, and
# the integrator's modules.json with layers appended. kuiper-shell is left out: it still REQUIREs #lines #lyAll
# #lyFocus #lyFind, which step 3 deletes (REQUEST to Opus 1, issue #10).
import json, subprocess
ED='/home/user/estate/kuiper-belt/editions/202611012135/'; OUT='/tmp/nl010-opus/team-3/lead/pre6/'
subprocess.run(['python3', ED+'handoff/03-layers/delete-moved.py', ED+'index.html', OUT+'index.html'], check=True, stderr=subprocess.DEVNULL)
import sys
SKIP=('layers',) + tuple(sys.argv[1:])
m=json.load(open(ED+'modules.json')); rec=json.load(open(ED+'handoff/03-layers/MODULE.json'))
m['modules']=[x for x in m['modules'] if x['id'] not in SKIP]
m['order']=[x for x in m['order'] if x not in SKIP]
rec=dict(rec); rec['sha256']='live'
m['modules'].append(rec); m['order'].append('layers')
json.dump(m, open(OUT+'modules.json','w'), indent=1); print(m['order'])
