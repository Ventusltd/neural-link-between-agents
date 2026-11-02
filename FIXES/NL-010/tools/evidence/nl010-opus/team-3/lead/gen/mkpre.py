# PRE-INTEGRATION page for test.cjs --index: current base index.html + team 3's deletions + team 4's hook table and
# loader (the reference bytes of modules/202611012145-loader.js between its marker lines) + the wafer promise + refuse().
import re, subprocess
ED='/home/user/estate/kuiper-belt/editions/202611012135/'
OUT='/tmp/nl010-opus/team-3/lead/pre5/'
subprocess.run(['python3','/tmp/nl010-opus/team-3/lead/gen/delete.py',ED+'index.html',OUT+'del.html'],check=True,stderr=subprocess.DEVNULL)
s=open(OUT+'del.html').read()
P=open(ED+'handoff/04-loader/index.html.patch').read().split('\n')
css=[l[1:] for l in P if l.startswith('+  #refuse,noscript .refuse')]
cssmore=[]
for i,l in enumerate(P):
    if l.startswith('+  #refuse,noscript .refuse'):
        j=i+1
        while P[j].startswith('+  ') and not P[j].startswith('+  /*'): cssmore.append(P[j][1:]); j+=1
        break
ref=[]; 
for i,l in enumerate(P):
    if l.startswith('+function refuse(m, slot)'):
        j=i
        while P[j].startswith('+') and not P[j].startswith('+if (!gl)'): ref.append(P[j][1:]); j+=1
        break
assert css and ref, (css, ref)
L=open(ED+'modules/202611012145-loader.js').read().split('\n')
a=[i for i,l in enumerate(L) if 'KUIPER HOOK TABLE AND LOADER kuiper.hooks.v1 · begin' in l][0]
b=[i for i,l in enumerate(L) if 'KUIPER HOOK TABLE AND LOADER kuiper.hooks.v1 · end' in l][0]
loader='\n'.join(L[a:b+1])
def one(old,new):
    global s; assert s.count(old)==1,old; s=s.replace(old,new)
one('</style>','\n'.join(css+cssmore)+'\n</style>')
one("if (!gl) {", '\n'.join(ref)+"\nif (!gl) {")
one("let N = 0, SPACE = 0, repos = [], commits = [];","let N = 0, SPACE = 0, repos = [], commits = [];\nlet kyWaferOk, kyWaferNo; const kyWafer = new Promise((ok, no) => { kyWaferOk = ok; kyWaferNo = no; }); kyWafer.catch(() => {});")
one("the belt says ' + fmt(bad.lines); return; }","the belt says ' + fmt(bad.lines); kyWaferNo(new Error(hud.textContent)); return; }")
one("  N = issued; SPACE = k;","  N = issued; SPACE = k; kyWaferOk({ N, SPACE });")
one("}).catch(() => { hud.textContent = '../../cosmos/wafer.tsv did not load. The wafer will not invent its keys.'; });",
    "}).catch(() => { refuse('../../cosmos/wafer.tsv did not load. The wafer will not invent its keys.'); kyWaferNo(new Error('../../cosmos/wafer.tsv did not load. The wafer will not invent its keys.')); });")
one("\nrequestAnimationFrame(frame);","\n"+loader+"\nrequestAnimationFrame(frame);")
open(OUT+'index.html','w').write(s)
import json, hashlib
f='modules/202611012141-layers.js'; src=open(ED+f).read()
req=[x.strip().strip("'") for x in re.search(r"REQUIRES = \[([^\]]*)\]",src).group(1).split(',')]
json.dump({"schema":"kuiper.modules.v1","edition":"202611012135","hooks":"kuiper.hooks.v1","order":["layers"],"modules":[{"id":"layers","generation":"202611012141","path":f,"sha256":"live","bytes":0,"byte_budget":98304,"requires":req,"provides":["layers"],"licence":"Apache-2.0"}]},open(OUT+'modules.json','w'),indent=1)
print('ok', len(s))
