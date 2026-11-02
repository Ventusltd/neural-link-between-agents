# scratch site for OPUS-6: the edition as it will stand at admission 6 (loader 04 patch + layers 03 patch applied in a copy;
# modules kuiper-shell, line-card, layers, file). Nothing in the repository is written.
import os, re, json, hashlib, subprocess, shutil, sys
KB='/home/user/estate/kuiper-belt'; ED=KB+'/editions/202611012135'; S='/tmp/nl010-opus/team-7/tester/site'
mods=sys.argv[1:] or ['modules/202611012143-kuiper-shell.js','modules/202611012143-line-card.js','modules/202611012141-layers.js','modules/202611012231-file.js','modules/202611012141-see-through.js','modules/202611012309-apps.js']
if not os.path.isdir(S):
    os.makedirs(S+'/editions/202611012135')
    for n in os.listdir(KB):
        if n not in ('editions','.git'): os.symlink(KB+'/'+n, S+'/'+n)
    for n in os.listdir(KB+'/editions'):
        if n!='202611012135': os.symlink(KB+'/editions/'+n, S+'/editions/'+n)
d=S+'/editions/202611012135'
for n in os.listdir(ED):
    if n in ('index.html','modules.json','modules'): continue
    if not os.path.lexists(d+'/'+n): os.symlink(ED+'/'+n, d+'/'+n)
if os.path.isdir(d+'/modules'): shutil.rmtree(d+'/modules')
shutil.copytree(ED+'/modules', d+'/modules')
shutil.copy(os.environ.get('KYPAGE','/tmp/nl010-opus/team-7/tester/index.base.html'), d+'/index.html')
for p in ['handoff/04-loader/index.html.patch','handoff/03-layers/index.html.after-04-loader.patch']:
    subprocess.run(['patch','-p3','-s','-d',d,'-i',ED+'/'+p],check=True) if False else None
# patches are written against a/editions/202611012135/index.html: apply from S with -p1
for p in []:
    r=subprocess.run(['patch','-p1','-s','-d',S,'--follow-symlinks','-i',ED+'/'+p],capture_output=True,text=True)
    print(p, 'rc', r.returncode, r.stdout[-300:], r.stderr[-300:])
m=json.load(open(ED+'/handoff/04-loader/modules.json'))
for rel in mods:
    src=open(d+'/'+rel,'rb').read(); t=src.decode()
    h=re.match(r'/\* kuiper module ([a-z0-9-]+), generation (\d{12}) \(UTC\), ([^*\n]*)', t)
    reg=re.search(r"KY\.register\(\{[\s\S]*?requires:\s*(\[[^\]]*\]|REQUIRES)", t)
    lit=reg.group(1)
    if lit=='REQUIRES': lit=re.search(r"var REQUIRES = (\[[^\]]*\])", t).group(1)
    req=re.findall(r"'([^']+)'", lit)
    prov=re.findall(r"'([^']+)'", re.search(r"provides:\s*(\[[^\]]*\])", t[reg.start():]).group(1))
    prov=[x if x!="' + ID + '" else h.group(1) for x in prov]
    if 'ID' in re.search(r"provides:\s*(\[[^\]]*\])", t[reg.start():]).group(1): prov=[h.group(1)]+[p for p in prov]
    rec={'id':h.group(1),'generation':h.group(2),'path':rel,'sha256':hashlib.sha256(src).hexdigest(),'bytes':len(src),'byte_budget':max(len(src),65536),
         'requires':req,'provides':sorted(set(prov+[h.group(1)]),key=lambda x:(x!=h.group(1),x)),'reads':[],'writes':[],'creates_controls':'scratch','licence':h.group(3).strip(),'team':'scratch','step':0,'proof':'scratch'}
    m['modules']=[x for x in m['modules'] if x['id']!=rec['id']]+[rec]
    if rec['id'] not in m['order']: m['order'].append(rec['id'])
m['order']=[x for x in m['order'] if x!='hello']; m['modules']=[x for x in m['modules'] if x['id']!='hello']
json.dump(m, open(d+'/modules.json','w'), indent=1)
print([(x['id'],x['provides'],len(x['requires'])) for x in m['modules']])
