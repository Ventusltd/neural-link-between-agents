"""Re-read every key row of an EVIDENCE.md: | id | claim | key | `fragment` |.
key = repo@sha path:line[-line]. PASS only if sha is a prefix of a commit that resolves, the path exists at that
commit (or, for sha 'WT', in the working tree), the first line of the range exists and the fragment is on a line
of the range. Usage: python3 -I check_keys.py EVIDENCE.md"""
import re, subprocess, sys, os
EST = '/home/user/estate'
ROW = re.compile(r'^\|\s*([A-Z]+\d+(?:\.\d+)?)\s*\|(.*)\|\s*([\w.-]+)@([0-9a-fA-FWT]+)\s+([^\s:|]+):(\d+)(?:-(\d+))?\s*\|\s*`(.+)`\s*\|\s*$')
ok = bad = 0
cache = {}
def text(repo, sha, path):
    k = (repo, sha, path)
    if k in cache: return cache[k]
    if sha == 'WT':
        p = os.path.join(EST, repo, path)
        t = open(p, encoding='utf-8').read() if os.path.exists(p) else None
    else:
        r = subprocess.run(['git', '-C', os.path.join(EST, repo), 'show', f'{sha}:{path}'], capture_output=True, text=True)
        t = r.stdout if r.returncode == 0 else None
    cache[k] = t
    return t
for n, line in enumerate(open(sys.argv[1], encoding='utf-8'), 1):
    m = ROW.match(line.rstrip('\n'))
    if not m: continue
    rid, _, repo, sha, path, a, b, frag = m.groups()
    frag = frag.replace('\\|', '|')
    t = text(repo, sha, path)
    a = int(a); b = int(b) if b else a
    if t is None: print(f'FAIL {rid} {repo}@{sha} {path}: no such file'); bad += 1; continue
    L = t.split('\n')
    if b > len(L): print(f'FAIL {rid} {path}:{a}-{b}: past end ({len(L)})'); bad += 1; continue
    if any(frag in L[i-1] for i in range(a, b+1)): ok += 1
    else: print(f'FAIL {rid} {path}:{a}-{b}: fragment not found: {frag!r}'); bad += 1
print(f'rows checked {ok+bad}, PASS {ok}, FAIL {bad}')
print('RESULT: ' + ('PASS' if bad == 0 and ok else 'FAIL'))
