#!/usr/bin/env python3
"""Build the served-byte manifest for main 07b6d517 (PR #57 merge). Columns: expect, path, sha256, bytes.
expect = NEW (added by PR #57), MOD (modified by PR #57), PIN (unchanged, hash-pinned by RUNBOOK 2.1),
         JEKYLL (has front matter: Jekyll may transform it, check status only), SKIP (Jekyll excludes _/. paths)."""
import subprocess, hashlib, csv, sys
WT="<workspace>/gg-wt"; BASE="73cbdec10bbd3fe2f8313b60b1acc2d22d31b517"; MERGE_TREE_REV="f9ccd703"
def git(*a): return subprocess.run(["git","-C",WT,*a],capture_output=True,check=True).stdout
rows=[]
for line in git("diff","--name-status","--no-renames",BASE,MERGE_TREE_REV).decode().splitlines():
    st,p=line.split("\t",1); rows.append(("NEW" if st=="A" else "MOD",p))
for r in csv.DictReader(open("<workspace>/teams/5/g1/runbook-pins.tsv"),delimiter="\t"):
    if r["kind"]=="FILE" and r["path"]!=".github/large-files-allowlist.txt": rows.append(("PIN",r["path"]))
rows.append(("PIN","uk_renewables_pipeline/202609082224/index.html"))
out=[]
for exp,p in rows:
    data=git("cat-file","blob",f"{MERGE_TREE_REV}:{p}")
    parts=p.split("/")
    if any(x.startswith(("_",".")) for x in parts): exp2="SKIP"
    elif data[:4] in (b"---\n",b"---\r") or p.endswith(".md"): exp2="JEKYLL"
    else: exp2=exp
    out.append((exp2 if exp2 in ("SKIP","JEKYLL") else exp,p,hashlib.sha256(data).hexdigest(),len(data),exp))
w=csv.writer(open("<workspace>/teams/5/g8/served-manifest.tsv","w"),delimiter="\t",lineterminator="\n")
w.writerow(["expect","path","sha256","bytes","origin"]); w.writerows(out)
from collections import Counter; print(Counter(o[0] for o in out), len(out))
