"""Prototype of the drift algorithm: each verified line of Edition 4 (keys.json) against the HEAD of the local
clone of its repository. Reads git objects only (git show HEAD:path); never the working tree. Classes:
SAME      the quoted text is at the same path and line at HEAD
MOVED     the text is in the same file at HEAD but at another line (first occurrence reported)
GONE      the file exists at HEAD but the text is not in it
FILE_GONE the path does not exist at HEAD
UNVERIFIED no clone of the repository on this machine; nothing is claimed"""
import json, os, subprocess, collections
ED = json.load(open('/home/user/estate/kuiper-belt/editions/202611012027/keys.json'))['bodies']
ROOTS = ['/home/user/estate', '/home/user']
def clone(repo):
    for r in ROOTS:
        p = os.path.join(r, repo)
        if os.path.isdir(os.path.join(p, '.git')): return p
    return None
def head(p):
    return subprocess.run(['git', '-C', p, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
out, heads = [], {}
for b in ED:
    p = clone(b['repo']); text = b.get('line_text') or b['quote']
    rec = {'id': b['id'], 'repo': b['repo'], 'path': b['path'], 'line': b['line'], 'key': b.get('key'), 'edition_commit': b['commit']}
    if not p: rec['class'] = 'UNVERIFIED'; rec['reason'] = 'no clone'; out.append(rec); continue
    heads.setdefault(b['repo'], head(p)); rec['head'] = heads[b['repo']]
    r = subprocess.run(['git', '-C', p, 'show', 'HEAD:' + b['path']], capture_output=True)
    if r.returncode != 0: rec['class'] = 'FILE_GONE'; out.append(rec); continue
    lines = r.stdout.decode('utf-8', 'replace').split('\n')
    same = b['line'] - 1 < len(lines) and lines[b['line'] - 1].rstrip('\r') == text
    if same: rec['class'] = 'SAME'
    else:
        hits = [i + 1 for i, l in enumerate(lines) if l.rstrip('\r') == text]
        if hits: rec['class'] = 'MOVED'; rec['head_line'] = hits[0]; rec['delta'] = hits[0] - b['line']
        else: rec['class'] = 'GONE'
    out.append(rec)
c = collections.Counter(r['class'] for r in out)
print('bodies', len(out), dict(c))
per = collections.defaultdict(collections.Counter)
for r in out: per[r['repo']][r['class']] += 1
for repo in sorted(per): print(' ', repo, (heads.get(repo) or 'no clone')[:12], dict(per[repo]))
print('examples MOVED:', [(r['repo'], r['path'], r['line'], '->', r['head_line']) for r in out if r['class'] == 'MOVED'][:5])
print('examples GONE:', [(r['repo'], r['path'], r['line']) for r in out if r['class'] == 'GONE'][:5])
print('examples FILE_GONE:', [(r['repo'], r['path']) for r in out if r['class'] == 'FILE_GONE'][:5])
json.dump({'heads': heads, 'rows': out}, open('drift.json', 'w'), indent=1)
