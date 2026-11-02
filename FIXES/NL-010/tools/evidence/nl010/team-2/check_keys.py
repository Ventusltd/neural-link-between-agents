#!/usr/bin/env python3
"""Verify every `repo@sha path:line` key in an EVIDENCE/STEPS file against the clones under /home/user/estate.
A row passes when the clone's HEAD starts with the sha, the file has that line, and the backticked fragment
(last table cell) is on that line (or, if the row has a range a-b, within it). Prints PASS/FAIL per row and a total."""
import re, subprocess, sys, os
ESTATE = '/home/user/estate'
KEY = re.compile(r'([\w.-]+)@([0-9a-f]{7,40}) (\S+?):(\d+)(?:-(\d+))?')
heads = {}
def head(repo):
    if repo not in heads:
        try: heads[repo] = subprocess.check_output(['git', '-C', f'{ESTATE}/{repo}', 'rev-parse', 'HEAD'], text=True).strip()
        except Exception: heads[repo] = ''
    return heads[repo]
files = {}
def lines(repo, path):
    p = f'{ESTATE}/{repo}/{path}'
    if p not in files:
        try: files[p] = open(p, 'rb').read().decode('utf-8', 'replace').split('\n')
        except Exception: files[p] = None
    return files[p]
ok = bad = 0
for ln in open(sys.argv[1], encoding='utf-8'):
    if not ln.startswith('|'): continue
    cells = [c.strip() for c in ln.strip().strip('|').split('|')]
    if len(cells) < 4: continue
    m = KEY.search(cells[2])
    if not m: continue
    repo, sha, path, a, b = m.group(1), m.group(2), m.group(3), int(m.group(4)), m.group(5)
    b = int(b) if b else a
    frag = cells[-1]
    fm = re.match(r'^``\s?(.*?)\s?``$|^`(.*)`$', frag)
    frag = (fm.group(1) if fm and fm.group(1) is not None else (fm.group(2) if fm else frag))
    frag = frag.replace('\\|', '|')
    why = []
    h = head(repo)
    if not h.startswith(sha): why.append(f'HEAD {h[:12]} != {sha}')
    L = lines(repo, path)
    if L is None: why.append('no such file')
    elif b > len(L): why.append(f'only {len(L)} lines')
    else:
        text = '\n'.join(L[a-1:b])
        if frag and frag not in text: why.append(f'fragment not on line: {L[a-1][:100]!r}')
    tag = cells[0]
    if why: bad += 1; print(f'FAIL {tag} {repo}@{sha} {path}:{a} :: ' + '; '.join(why))
    else: ok += 1
print(f'RESULT: {"PASS" if not bad else "FAIL"} ({ok} keys verified, {bad} failed)')
sys.exit(1 if bad else 0)
