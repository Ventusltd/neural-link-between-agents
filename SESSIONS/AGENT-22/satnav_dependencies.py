#!/usr/bin/env python3
"""Read-only estate census and explicit, immutable SatNav dependency materialisation.
No source repo writes. Run census in CI; materialise into a NEW directory only.
"""
import argparse, base64, hashlib, json, os, re, tempfile
from pathlib import Path, PurePosixPath
from urllib.request import Request, urlopen
from urllib.parse import quote

OWNER = 'Ventusltd'
API = 'https://api.github.com'
SHA = re.compile(r'^[0-9a-f]{40}$')
KEYWORDS = re.compile(r'geodes|bearing|geolocat|compass|gps|maplibre|basemap|satellite|lidar|terrain|slope|offline|service.worker|deeplink|deep.link|vicinity|route|routing|overpass|scada|tile|cache|licen[cs]e|notice', re.I)

def get(path):
    headers = {'Accept':'application/vnd.github+json','User-Agent':'satnav-dependency-audit/1','X-GitHub-Api-Version':'2022-11-28'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token: headers['Authorization'] = 'Bearer ' + token
    with urlopen(Request(API + path, headers=headers), timeout=30) as r:
        return json.load(r)

def blob_oid(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()

def safe_path(path):
    p = PurePosixPath(path)
    if not path or p.is_absolute() or '..' in p.parts or '\\' in path or ':' in path or str(p) != path or path == '.':
        raise ValueError('unsafe path: ' + path)
    return p

def census(shard=0, shards=1, fetch=get):
    if not 0 <= shard < shards: raise ValueError('invalid shard')
    repos = []
    for page in range(1, 1000):
        batch = fetch(f'/users/{OWNER}/repos?per_page=100&page={page}&sort=full_name')
        repos.extend(r for r in batch if not r.get('private') and r['owner']['login'].lower()==OWNER.lower())
        if len(batch) < 100: break
    else: raise RuntimeError('pagination limit reached')
    names = sorted({r['full_name']:r for r in repos}.values(), key=lambda r:r['full_name'].lower())
    out = {'public_repo_count':len(names),'shard':shard,'shards':shards,'repositories':[]}
    for r in names:
        repo = r['full_name']
        if int(hashlib.sha256(repo.lower().encode()).hexdigest(),16)%shards != shard: continue
        item = {'repo':repo,'branch':r['default_branch']}
        try:
            head = fetch(f'/repos/{repo}/commits/{quote(r["default_branch"],safe="")}')
            tree = fetch(f'/repos/{repo}/git/trees/{head["commit"]["tree"]["sha"]}?recursive=1')
            item.update(commit=head['sha'], truncated=bool(tree.get('truncated')), file_count=sum(x['type']=='blob' for x in tree['tree']), candidates=[{'path':x['path'],'blob':x['sha'],'bytes':x.get('size')} for x in tree['tree'] if x['type']=='blob' and KEYWORDS.search(x['path'])])
            item['status'] = 'INCOMPLETE' if item['truncated'] else 'INDEXED'
        except Exception as e:
            item.update(status='INCOMPLETE',error=type(e).__name__)
        out['repositories'].append(item)
    return out

def materialise(lock, dest, fetch=get):
    dest=Path(dest)
    if dest.exists(): raise FileExistsError(dest)
    entries=lock['files']
    if lock.get('schema_version')!=1 or not entries: raise ValueError('invalid lock')
    paths=set()
    for e in entries:
        src=safe_path(e['path']); target=safe_path(e['target'])
        if str(target) in paths or not str(target).startswith('vendor/') or not re.fullmatch(r'Ventusltd/[A-Za-z0-9_.-]+',e['repo']) or not SHA.fullmatch(e['commit']) or not SHA.fullmatch(e['blob']) or e.get('licence')!='Apache-2.0': raise ValueError('invalid entry: '+str(target))
        paths.add(str(target))
    for e in entries:
        for legal in ('LICENSE','NOTICE'):
            if not any(x['repo']==e['repo'] and x['commit']==e['commit'] and x['path']==legal for x in entries): raise ValueError('missing legal file: '+legal)
    dest.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=dest.parent,prefix='.satnav-stage-') as tmp:
        stage=Path(tmp)/'pack';stage.mkdir(); receipt=[]
        for e in entries:
            info=fetch(f'/repos/{e["repo"]}/contents/{quote(e["path"],safe="/")}?ref={e["commit"]}')
            if info.get('type')!='file' or info.get('sha')!=e['blob'] or info.get('encoding')!='base64': raise ValueError('source identity mismatch: '+e['path'])
            data=base64.b64decode(info['content'].replace('\n',''),validate=True)
            if blob_oid(data)!=e['blob'] or len(data)!=info.get('size'): raise ValueError('source bytes mismatch: '+e['path'])
            if 'sha256' in e and hashlib.sha256(data).hexdigest()!=e['sha256']: raise ValueError('sha256 mismatch')
            p=stage/e['target'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
            receipt.append({**e,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        (stage/'receipt.json').write_text(json.dumps({'schema_version':1,'files':receipt},indent=2)+'\n',encoding='utf-8')
        if dest.exists(): raise FileExistsError(dest)
        stage.rename(dest)
    return receipt

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    c=sub.add_parser('census');c.add_argument('--shard',type=int,default=0);c.add_argument('--shards',type=int,default=1);c.add_argument('--out',type=Path,required=True)
    m=sub.add_parser('materialise');m.add_argument('--lock',type=Path,required=True);m.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.cmd=='census':
        result=census(a.shard,a.shards);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');return int(any(x['status']!='INDEXED' for x in result['repositories']))
    materialise(json.loads(a.lock.read_text(encoding='utf-8')),a.out);return 0
if __name__=='__main__': raise SystemExit(main())
