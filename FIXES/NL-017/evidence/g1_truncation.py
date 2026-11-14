#!/usr/bin/env python3
"""Gate 1: no-truncation proof for PR #57 head vs main baseline and RUNBOOK pins. Read-only."""
import subprocess, re, sys, hashlib, csv
WT="<workspace>/gg-wt"; BASE="73cbdec10bbd3fe2f8313b60b1acc2d22d31b517"; OUTD="<workspace>/teams/5/g1"
def git(*a, text=True): return subprocess.run(["git","-C",WT,*a],capture_output=True,text=text,check=True).stdout
head=git("rev-parse","HEAD").strip()
def tree(rev):
    d={}
    for line in git("ls-tree","-r","-l","--full-tree",rev).splitlines():
        meta,path=line.split("\t",1); mode,typ,blob,size=meta.split()
        d[path]=(blob,int(size) if size!='-' else -1,mode)
    return d
B=tree(BASE); H=tree(head)
# baseline manifest
M={}
for row in open("<workspace>/monitor/globalgrid2050.blobmanifest.tsv"):
    b,s,p=row.rstrip("\n").split("\t",2); M[p]=(b,int(s))
man_vs_base = sum(1 for p in B if p not in M or M[p][0]!=B[p][0]) + sum(1 for p in M if p not in B)
added=[p for p in H if p not in B]; deleted=[p for p in B if p not in H]
modified=[p for p in H if p in B and H[p][0]!=B[p][0]]
modechg=[p for p in H if p in B and H[p][0]==B[p][0] and H[p][2]!=B[p][2]]
with open(f"{OUTD}/changed-files.tsv","w") as f:
    f.write("status\tpath\tbase_blob\tbase_size\thead_blob\thead_size\thead_sha256\n")
    for st,lst in (("A",added),("M",modified),("D",deleted)):
        for p in sorted(lst):
            bb,bs=(B[p][0],B[p][1]) if p in B else ("","")
            hb,hs=(H[p][0],H[p][1]) if p in H else ("","")
            sha=hashlib.sha256(subprocess.run(["git","-C",WT,"cat-file","blob",hb],capture_output=True,check=True).stdout).hexdigest() if hb else ""
            f.write(f"{st}\t{p}\t{bb}\t{bs}\t{hb}\t{hs}\t{sha}\n")
print(f"head={head} base={BASE}")
print(f"baseline manifest entries={len(M)} base tree entries={len(B)} manifest-vs-base mismatches={man_vs_base}")
print(f"added={len(added)} modified={len(modified)} deleted={len(deleted)} mode-only-changes={len(modechg)}")
for p in sorted(modified): print(f"  M {p}: {B[p][1]} -> {H[p][1]} bytes")
big=[(p,H[p][1]) for p in added+modified if H[p][1]>5242880]
print(f"added/modified files over 5 MiB: {len(big)}"); [print("  ",p,s) for p,s in big]
# RUNBOOK pins
rb=open(f"{WT}/docs/repd/RUNBOOK.md").read().splitlines()
start=next(i for i,l in enumerate(rb) if l.startswith("## 2. Paths"))
end=next(i for i,l in enumerate(rb) if l.startswith("## 3."))
res=[]
for l in rb[start:end]:
    if not l.startswith("| `"): continue
    cells=[c.strip() for c in l.strip("|").split("|")]
    paths=re.findall(r"`([^`]+)`",cells[0])
    hexes=re.findall(r"`([0-9a-f]{7,64})(?:\.\.\.[0-9a-f]+)?`",cells[1]+" "+(cells[2] if len(cells)>2 else ""))
    full_sha=[h for h in re.findall(r"`([0-9a-f]{64})`",cells[1])]
    blobs=re.findall(r"`([0-9a-f]{8,40})`",cells[2]) if len(cells)>2 else []
    treeids=re.findall(r"`([0-9a-f]{8,40})(?:\.\.\.)?`",cells[1])
    is_tree = "Tree" not in cells[1] and rb.index(l) > next(i for i,x in enumerate(rb) if x.startswith("### 2.2"))
    # expand shorthand v9.5 etc relative to first path dir
    exp=[]
    for p in paths:
        if "/" not in p and exp and "/" in exp[0]: p=exp[0].rsplit("/",1)[0]+"/"+p
        exp.append(p)
    if exp and exp[0].startswith("uk_renewables_pipeline/v9.4"): exp=[exp[0]]+["uk_renewables_pipeline/"+x for x in paths[1:]]
    if exp and exp[0].startswith("repd_grid_atlasv3"): exp=["repd_grid_atlasv3","repd_grid_atlasv4","repd_grid_atlasv5","repd_grid_atlasv6","repd_grid_atlasv7","repd_grid_atlasv8","202608300453-atlas-v9","restore_points"]
    if exp and exp[0].startswith("GridAtlas"): continue
    for idx,p in enumerate(exp):
        if is_tree:
            want=treeids[idx] if idx<len(treeids) else None
            try: b=git("rev-parse",f"{BASE}:{p}").strip(); h=git("rev-parse",f"{head}:{p}").strip()
            except subprocess.CalledProcessError: res.append(("TREE",p,want,"MISSING","")); continue
            ok = b==h and (want is None or b.startswith(want))
            res.append(("TREE",p,want,"PASS" if ok else "FAIL",f"base={b[:12]} head={h[:12]}"))
        else:
            if p not in B: res.append(("FILE",p,"","NOT-IN-BASE","")); continue
            hb=H.get(p,("DELETED",))[0]; bb=B[p][0]
            data=subprocess.run(["git","-C",WT,"cat-file","blob",hb],capture_output=True).stdout if hb!="DELETED" else b""
            sha=hashlib.sha256(data).hexdigest()
            wsha=full_sha[idx] if idx<len(full_sha) else None
            wbl=blobs[idx] if idx<len(blobs) else None
            ok = hb==bb and (wsha is None or sha==wsha) and (wbl is None or bb.startswith(wbl))
            note=f"blob={hb[:12]} sha256={sha[:16]}"
            if hb!=bb: note+=f" CHANGED from {bb[:12]}"
            if wsha and sha!=wsha: note+=f" PIN-MISMATCH want {wsha[:16]}"
            if wbl and not bb.startswith(wbl): note+=f" BLOB-PIN-MISMATCH want {wbl}"
            res.append(("FILE",p,wsha or wbl or "","PASS" if ok else "FAIL",note))
with open(f"{OUTD}/runbook-pins.tsv","w") as f:
    f.write("kind\tpath\tpinned\tresult\tnote\n")
    for r in res: f.write("\t".join(str(x) for x in r)+"\n")
from collections import Counter
print("RUNBOOK section 2 pins:",dict(Counter(r[3] for r in res)), "checked",len(res))
for r in res:
    if r[3]!="PASS": print("  ",r)
