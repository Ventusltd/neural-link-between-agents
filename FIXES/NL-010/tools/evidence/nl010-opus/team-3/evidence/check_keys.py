#!/usr/bin/env python3
"""Re-read every key row of an EVIDENCE.md: | id | claim | key | `fragment` |.
key = repo@sha path:line (estate clone, read with git show sha:path) or
      neural-link-between-agents path:line (working tree, not a git repo) or
      kuiper-belt@WORKTREE path:line (the edition branch's uncommitted files).
PASS only if the sha resolves, the line exists, and the fragment is on that line."""
import re, subprocess, sys, pathlib
EST = pathlib.Path('/home/user/estate'); NL = pathlib.Path('/home/user/neural-link-between-agents')
KEY = re.compile(r'([A-Za-z0-9_.-]+)@([0-9a-f]{7,40}|WORKTREE) ([^\s`|]+):(\d+)')
NLK = re.compile(r'neural-link-between-agents ([^\s`|]+):(\d+)')
cache = {}
def lines(repo, sha, path):
    k = (repo, sha, path)
    if k not in cache:
        if repo == 'NL':
            cache[k] = (NL / path).read_text(errors='replace').split('\n')
        elif sha == 'WORKTREE':
            cache[k] = (EST / repo / path).read_text(errors='replace').split('\n')
        else:
            out = subprocess.run(['git', '-C', str(EST / repo), 'show', f'{sha}:{path}'], capture_output=True)
            if out.returncode: raise FileNotFoundError(out.stderr.decode().strip())
            cache[k] = out.stdout.decode(errors='replace').split('\n')
    return cache[k]
ok = bad = 0
for n, row in enumerate(open(sys.argv[1], encoding='utf-8'), 1):
    if not row.startswith('|') or row.startswith('|---') or row.startswith('| #'): continue
    cells = [c.strip() for c in re.split(r'(?<!\\)\|', row.strip())[1:-1]]
    if len(cells) < 4: continue
    keycell, frag = cells[-2], cells[-1]
    m = KEY.search(keycell); mn = NLK.search(keycell)
    if not (m or mn): continue
    fm = re.fullmatch(r'`+ ?(.*?) ?`+', frag)
    if not fm: print(f'NOFRAG  row {n}: {cells[0]}'); bad += 1; continue
    f = fm.group(1).replace('\\|', '|')
    repo, sha, path, ln = (m.groups() if m else ('NL', '', mn.group(1), mn.group(2)))
    try:
        L = lines(repo, sha, path); ln = int(ln)
        line = L[ln - 1] if 0 < ln <= len(L) else None
    except Exception as e:
        print(f'FAIL    row {n}: {cells[0]} {repo}@{sha} {path}: {e}'); bad += 1; continue
    if line is not None and f in line: ok += 1
    else:
        bad += 1; print(f'FAIL    row {n}: {cells[0]} {repo}@{sha} {path}:{ln} fragment not on line: {f!r}\n        line: {(line or "")[:200]!r}')
print(f'checked {ok + bad} keys: {ok} PASS, {bad} FAIL'); print('RESULT:', 'PASS' if bad == 0 and ok else 'FAIL')
sys.exit(0 if bad == 0 and ok else 1)
