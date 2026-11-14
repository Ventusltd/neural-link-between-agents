#!/usr/bin/env python3
"""Gate 3: which workflows a merge of PR #57 to main would trigger (push to main), evaluated with the HEAD versions
of the workflow files (GitHub uses the workflow file at the pushed commit). Read-only."""
import subprocess, yaml, fnmatch, re, sys, json
WT="<workspace>/gg-wt"; BASE="73cbdec10bbd3fe2f8313b60b1acc2d22d31b517"
def git(*a): return subprocess.run(["git","-C",WT,*a],capture_output=True,text=True,check=True).stdout
head=git("rev-parse","HEAD").strip()
changed=git("diff","--name-only",BASE,head).splitlines()
def glob_to_re(p):
    # GitHub filter pattern: ** any incl /, * any except /, ? one char except /, leading ! handled by caller
    i=0; out=""
    while i<len(p):
        if p.startswith("**",i): out+=".*"; i+=2
        elif p[i]=="*": out+="[^/]*"; i+=1
        elif p[i]=="?": out+="[^/]"; i+=1
        else: out+=re.escape(p[i]); i+=1
    return re.compile("^"+out+"$")
def match_paths(pats, files):
    hits=set()
    for f in files:
        ok=False
        for p in pats:
            neg=p.startswith("!"); pp=p[1:] if neg else p
            if glob_to_re(pp).match(f): ok = not neg
        if ok: hits.add(f)
    return hits
def branch_ok(spec):
    br=spec.get("branches"); ign=spec.get("branches-ignore")
    if br is not None:
        ok=False
        for b in br:
            neg=b.startswith("!"); bb=b[1:] if neg else b
            if glob_to_re(bb).match("main"): ok=not neg
        return ok
    if ign is not None: return not any(glob_to_re(b).match("main") for b in ign)
    if spec.get("tags") is not None and br is None: return False
    return True
rows=[]
for wf in sorted(git("ls-tree","--name-only",f"{head}:.github/workflows").split()):
    if not wf.endswith((".yml",".yaml")): continue
    txt=git("show",f"{head}:.github/workflows/{wf}")
    try: y=yaml.safe_load(txt)
    except Exception as e: rows.append((wf,"PARSE-ERROR",str(e)[:80])); continue
    on=y.get(True, y.get("on"))
    if isinstance(on,str): on={on:None}
    if isinstance(on,list): on={k:None for k in on}
    if not isinstance(on,dict) or "push" not in on: continue
    spec=on["push"] or {}
    if not branch_ok(spec): continue
    if "paths" in spec: hits=match_paths(spec["paths"],changed)
    elif "paths-ignore" in spec: hits=set(changed)-match_paths(spec["paths-ignore"],changed)
    else: hits=set(changed)
    if hits: rows.append((wf,len(hits),sorted(hits)[:6]))
json.dump(rows,open("<workspace>/teams/5/g3/triggered.json","w"),indent=1)
print(f"head={head} changed={len(changed)} workflows triggered on push to main: {len(rows)}")
for r in rows: print(" ",r[0],r[1],r[2][:3])
