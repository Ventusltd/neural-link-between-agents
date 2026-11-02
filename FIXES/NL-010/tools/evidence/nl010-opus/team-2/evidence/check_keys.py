# Re-read every key row of an EVIDENCE.md: | id | claim | key | fragment |
# key = repo@sha path:line[-line] ; sha WT = working tree. PASS only when the line exists and the fragment is on it.
import re, subprocess, sys
REPOS = {'kuiper-belt': '/home/user/estate/kuiper-belt', 'gridatlas': '/home/user/estate/gridatlas',
         'neural-link': '/home/user/neural-link-between-agents'}
rows = ok = 0; bad = []
for ln in open(sys.argv[1], encoding='utf-8'):
    cells = [c.strip() for c in re.split(r'(?<!\\)\|', ln.strip().strip('|'))] if ln.startswith('|') else []
    if len(cells) < 4: continue
    m = re.fullmatch(r'`?([\w-]+)@(\w+) ([^:`]+):(\d+)(?:-(\d+))?`?', cells[2])
    if not m: continue
    repo, sha, path, a, b = m.groups(); a = int(a); b = int(b or a)
    frag = cells[3].strip('`').replace('\\|', '|')
    d = REPOS[repo]
    try:
        txt = open(d + '/' + path, encoding='utf-8').read() if sha == 'WT' else \
            subprocess.run(['git', '-C', d, 'show', sha + ':' + path], capture_output=True, check=True).stdout.decode('utf-8', 'replace')
    except Exception as e:
        bad.append((cells[0], 'missing file')); rows += 1; continue
    L = txt.split('\n'); rows += 1
    if b > len(L) or not any(frag in L[i - 1] for i in range(a, b + 1)):
        bad.append((cells[0], cells[2], frag)); continue
    ok += 1
print('rows', rows, 'PASS', ok, 'FAIL', len(bad))
for x in bad: print(' FAIL', x)
sys.exit(1 if bad or not rows else 0)
