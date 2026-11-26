"""Independent B1 successor v2 review, with existing admitted software only."""
import copy,json,subprocess,sys
from pathlib import Path
from tacit_c_verify import canonical,sha,blob,need,ARCHIVE,DESCRIPTOR
from tacit_c_eighth_peer import pinned
from tacit_c_seventh import member
from tacit_c1_fresh import independent
from tacit_c_fifth import expected_rank,fixtures
from tacit_c_sixth import reference,near

HEAD="988e2293fd740ca434a9cf087fa873f841b7dc6f"
PROOF=("77561125ed5829483f30f84391c9998a21915654737fbfa34ca336b43686dbe5","tacit-b1-patterns.json","a5540a0978117750fd54739e423dbd4e7c0150ce1eba81d5139609ed2db7ee97")
DECISION=(PROOF[0],"tacit-b-admission.json","79ca2bf68b94c2c06c4d21063cc1a4acd4442acc43bb9630f8cd32a7d01daa2a")

def main():
    root,out=map(Path,sys.argv[1:]);obs=[]
    def check(case,ok,**detail):obs.append(dict(case=case,result="PASS" if ok else "FAIL",**detail))
    def refuse(case,fn):
        try:fn()
        except (ValueError,TypeError,KeyError) as e:check(case,True,refusal=str(e))
        else:check(case,False)
    try:
        peer=root/"peer-b1";froot=root/"factory";droot=root/"peer-d"
        need(subprocess.check_output(["git","-C",str(peer),"rev-parse","HEAD"],text=True).strip()==HEAD,"B1_CHECKOUT")
        need(blob((peer/"tools/tacit_b_patterns.py").read_bytes())=="f231fdc7014491cb63e5824f09f90d7a62c8f5fb","B1_BLOB")
        sys.path[:0]=[str(froot/"tools"),str(peer/"tools"),str(droot/"tools"),str(root/"oracle")]
        import package_factory as f
        import typed_package_execution as t
        import acceptance as oracle
        from tacit_b_patterns import PatternBridge
        from kuiper_select import Space
        raw=member(root,"A-bonds");manifest=json.loads(raw)
        pin=pinned(root/"B1.zip",PROOF);producer=json.loads(pin)
        decision=pinned(root/"B1.zip",DECISION);(root/"decision.json").write_bytes(decision)
        for label in ("first","second"):
            dest=root/f"b1-{label}.json"
            cmd=[sys.executable,str(peer/"tools/tacit_b_patterns.py"),"--factory",str(froot),"--d",str(droot),"--bonds",str(root/"A-bonds.zip"),"--nearest",str(root/"nearest"),"--nsources",str(root/"nearest-source"),"--esources",str(root/"electrical"),"--archive",str(root/"orient.zip"),"--build",str(root/"build.json"),"--electrical",str(root/"electrical.json"),"--decision",str(root/"decision.json"),"--out",str(dest)]
            subprocess.run(cmd,check=True,timeout=90)
            check("actual-B1-producer-repeat-"+label,dest.read_bytes()==pin)
        b=PatternBridge(f,t,Space,raw,(root/"orient.zip").read_bytes(),f.strict((root/"build.json").read_bytes()),root/"nearest",root/"nearest-source",root/"electrical")
        canon=lambda x:(json.dumps(x,sort_keys=True,ensure_ascii=True,allow_nan=False,separators=(",",":"))+"\n").encode()
        hash_=lambda x:sha(canon(x))
        rows={str(x["kuiper"]["key"]):x for x in manifest["source_entries"]}
        ids={"orient":{1,5},"nearest-orient":{1,5,15,16},"electrical":{24,25,26,27}}
        for op,meaning in ids.items():
            p=b.pattern(op);keys=sorted((k for k,r in rows.items() if int(r["meaning_id"][-6:]) in meaning),key=int)
            check("exact-pattern-source-"+op,p["keys"]==keys and p["sources"]==[dict(key=k,meaning_id=rows[k]["meaning_id"],source=rows[k]["source"]) for k in keys] and p["closure_sha256"]==hash_(p["closure"]))
            want=0 if op=="orient" else 3 if op=="nearest-orient" else 2
            edges=p["typed_graph"]["conditional_bonds"]
            check("exact-typed-bonds-"+op,len(edges)==want and all(e in manifest["typed_bonds"] for e in edges))
        rs=[];qs=[]
        def verify_orient(case,inputs):
            q=b.request_v2("orient",inputs);r=b.execute_raw(canon(q));o=r["result"]["output"]
            ref=independent(inputs["point_a"],inputs["point_b"])
            check(case+"-math",abs(o["distance_km"]-ref["distance_km"])<1e-6 and abs((o["initial_bearing_deg"]-ref["initial_bearing_deg"]+180)%360-180)<1e-7,actual=o,expected=ref)
            check(case+"-binding",r["request_sha256"]==hash_(q) and r["pattern_sha256"]==hash_(r["pattern"])==q["pattern_sha256"] and r["result_sha256"]==hash_(r["result"]) and r["receipt_sha256"]==hash_({k:v for k,v in r.items() if k!="receipt_sha256"}) and r["legacy_receipt"]["archive_sha256"]==ARCHIVE and r["pattern"]["descriptor_sha256"]==DESCRIPTOR and r["rights"]=="BLOCKED")
            check(case+"-authority",r["result"]["admission"] is True and r["result"]["state"]=="EXECUTED_INTERNAL" and r["independent_verification"]=="PENDING_EXACT_REQUEST_REVIEW")
            check(case+"-repeat",b.execute_raw(canon(q))==r)
            qs.append(q);rs.append(r)
        for i,q in enumerate(producer["requests"]):verify_orient("producer-fixture-"+str(i),q["inputs"])
        for i,(a,z) in enumerate((((-0.1276,51.5072),(2.3522,48.8566)),((179.8,12.3),(-179.4,12.7)))):
            point=lambda x:dict(longitude=x[0],latitude=x[1])
            verify_orient("independent-fixture-"+str(i),dict(crs="WGS84",unit="degrees",point_a=point(a),point_b=point(z)))
        check("pattern-stable-fresh-requests",len({r["pattern_sha256"] for r in rs})==1 and len({r["request_sha256"] for r in rs})==4 and len({r["result_sha256"] for r in rs})==4)
        for label,mut in (("wrong-manifest",lambda q:q.update(manifest_sha256="0"*64)),("wrong-key",lambda q:q["keys"].reverse()),("wrong-pattern",lambda q:q.update(pattern_sha256="0"*64)),("caller-experiment",lambda q:q.update(experiment=True)),("wrong-unit",lambda q:q["inputs"].update(unit="radians"))):
            q=copy.deepcopy(qs[0]);mut(q);refuse(label,lambda:b.execute_raw(canon(q)))
        refuse("duplicate-wire-field",lambda:b.execute_raw(b'{"schema":1,"schema":2}'))
        refuse("cross-request-replay",lambda:b.replay_v2(qs[1],rs[0]))
        for label,mut in (("forged-result",lambda r:r["result"]["output"].update(distance_km=0)),("forged-review",lambda r:r.update(independent_verification="PASS")),("forged-rights",lambda r:r.update(rights="CLEARED")),("forged-source",lambda r:r["pattern"]["sources"][0]["source"].update(first=0)),("forged-closure",lambda r:r["pattern"].update(closure_sha256="0"*64))):
            fake=copy.deepcopy(rs[0]);mut(fake);fake["pattern_sha256"]=hash_(fake["pattern"]);fake["result_sha256"]=hash_(fake["result"]);fake["receipt_sha256"]=hash_({k:v for k,v in fake.items() if k!="receipt_sha256"})
            refuse(label+"-rehashed",lambda:b.replay_v2(qs[0],fake))
        for op,q in producer["candidate_requests"].items():
            r=b.execute_raw(canon(q));check(op+"-default-refusal",r["result"]["state"]=="REFUSED" and r["result"]["output"] is None and not r["result"]["admission"] and r["rights"]=="BLOCKED")
        for label,x in fixtures():
            if label=="coincident-distance-only":continue
            q=b.request_v2("nearest-orient",x);r=b.execute_v2(q,experiment=True);ref=expected_rank(oracle,x)
            if ref:check("nearest-"+label,r["result"]["state"]=="PRE_ADMISSION_EXECUTED" and r["result"]["output"]["id"]==ref[0]["id"] and not r["result"]["admission"])
            else:check("nearest-"+label,r["result"]["state"]=="NO_ELIGIBLE_RECORD" and r["result"]["output"] is None)
        for label,length in (("base",1000),("half",500),("fractional",125.5)):
            x=copy.deepcopy(producer["candidate_requests"]["electrical"]["inputs"]);x["route"]["value"]=length
            r=b.execute_v2(b.request_v2("electrical",x),experiment=True);ref,_,_=reference(x)
            check("electrical-"+label,r["result"]["state"]=="PRE_ADMISSION_EXECUTED" and not r["result"]["admission"] and all(near(r["result"]["output"][k],v) for k,v in ref.items()))
        check("registry-and-rights-unchanged",set(f.ADMISSIONS)=={"orient"} and not f.REVIEWED_RECEIPTS)
        obs.append(dict(case="combined-E1-D1-v2-execution",result="OPEN",reason="Independent B1 v2 runtime only; require exact combined candidate. Existing v1 bridge compatible."))
    except Exception as e:obs.append(dict(case="harness",result="FAIL",reason=type(e).__name__+":"+str(e)))
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report=dict(schema="tacit-c1.b1-independent.v1",B1_head=HEAD,counts=counts,observations=obs,production=False,admission_changed=False)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for item in obs:
        if item["result"]!="PASS" or "actual" in item:print(json.dumps(item))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
