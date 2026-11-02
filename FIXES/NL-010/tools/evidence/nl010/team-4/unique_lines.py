"""Distinct line texts against all line occurrences, over the text blobs at HEAD of the 25 local clones
(/home/user/estate/*), by the wafer's binary rule. Distinct = exact bytes of the line without its newline,
CR before LF removed (LF-normalised). Prints per repository and in total; writes unique_lines.json."""
import subprocess, os, json, hashlib
EST = '/home/user/estate'
tot = {'repos': 0, 'files': 0, 'binary': 0, 'lines': 0, 'distinct_in_repo_sum': 0}
seen = set(); per = {}
for repo in sorted(os.listdir(EST)):
    d = os.path.join(EST, repo)
    if not os.path.isdir(os.path.join(d, '.git')): continue
    ls = subprocess.run(['git','-C',d,'ls-tree','-r','-z','HEAD'], capture_output=True).stdout.split(b'\0')
    shas = [e.split(b'\t')[0].split(b' ')[2] for e in ls if e]
    p = subprocess.run(['git','-C',d,'cat-file','--batch'], input=b'\n'.join(shas)+b'\n', capture_output=True).stdout
    i = 0; lines = 0; files = 0; binary = 0; local = set()
    for sha in shas:
        nl = p.index(b'\n', i); hdr = p[i:nl].split(); size = int(hdr[2]); body = p[nl+1:nl+1+size]; i = nl+1+size+1
        files += 1
        if b'\x00' in body[:8000]: binary += 1; continue
        if body.endswith(b'\n'): body = body[:-1]
        for ln in body.split(b'\n'):
            if ln.endswith(b'\r'): ln = ln[:-1]
            lines += 1; h = hashlib.blake2b(ln, digest_size=16).digest(); local.add(h); seen.add(h)
    head = subprocess.run(['git','-C',d,'rev-parse','HEAD'], capture_output=True, text=True).stdout.strip()
    per[repo] = {'head': head, 'files': files, 'binary': binary, 'lines': lines, 'distinct': len(local)}
    tot['repos'] += 1; tot['files'] += files; tot['binary'] += binary; tot['lines'] += lines; tot['distinct_in_repo_sum'] += len(local)
    print(repo, per[repo], flush=True)
tot['distinct_across_estate'] = len(seen)
print('TOTAL', tot)
json.dump({'per_repo': per, 'total': tot, 'rule': 'exact bytes without newline, CR before LF removed; NUL in first 8000 bytes = binary, skipped'}, open('unique_lines.json','w'), indent=1)
