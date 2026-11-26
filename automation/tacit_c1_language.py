"""C1 Turn 17: independent actual text -> A1 plan -> B1 existing archive.
No producer edits; independent numerical oracle, no comparison admission.
"""
import copy,json,sys,subprocess,hashlib
from pathlib import Path
from tacit_c1_fresh import independent
from tacit_c1_combined import canonical,bh,verify,ARCH,PIN
A="c4d6d309940d131d2a1ae6181701086aa7221839"
B="e0a094c8c672643f0b8a9967dea93c6ef7e4518a"
E="2a58ed137bef42022a5fca8020d320b96fc47fd6"
def sha(x):return hashlib.sha256(x).hexdigest()
def reseal(p,k):
    p[k]=bh({x:y for x,y in p.items() if x!=k});return p
def main():
    root,peer,out=map(lambda p:Path(p).resolve(),sys.argv[1:]);obs=[];evidence=[]
    def check(case,ok,**kw):obs.append(dict(case=case,result="PASS" if ok else "FAIL",**kw))
    def require(case,ok):
        check(case,ok)
        if not ok:raise ValueError(case)
    def refuse(case,fn):
        try:fn()
        except ValueError as exc:check(case,True,reason=str(exc))
        else:check(case,False)
    try:
        for name,path,pin in (("A",root/"a1",A),("B",root/"b",B),("E",peer,E)):
            require(name+"-exact",subprocess.check_output(["git","-C",str(path),"rev-parse","HEAD"],text=True).strip()==pin)
        raw=(root/"package.zip").read_bytes();require("archive",sha(raw)==ARCH)
        sys.path[:0]=[str(root/"factory"/"tools"),str(root/"b"/"tools"),str(root/"a1"/"tools"),str(peer/"tools")]
        import package_factory as f
        import typed_package_execution as t
        from tacit_b_patterns import PatternBridge
        from kuiper_select import Space as KSpace
        from kuiper_runtime import manifest_bytes
        from tacit_a1_semantics import Resolver
        from tacit_a1_properties import Space
        from tacit_a1_invalidation import Ledger
        from tacit_b_compound import execute_compound,verify_compound
        resolver=Resolver(root/"semantic");m=manifest_bytes(root/"bonds.zip")
        bridge=PatternBridge(f,t,KSpace,m,raw,f.strict((root/"build-receipt.json").read_bytes()),None,None,None)
        ledger=Ledger(Space(root),root);epoch=ledger.begin("orient")
        guard=lambda:ledger.assert_current("orient",epoch)
        from kuiper_research import selection
        selected=selection(KSpace(json.loads(m)),{"mode":"machine","family":"Vg"})
        ctx={"generation":17,"selection_receipt_sha256":selected["receipt_sha256"],"challenge":"17"*32}
        keys=sorted([str(r["kuiper"]["key"]) for r in json.loads(m)["source_entries"] if r["meaning_id"] in ("GG2050-VEDIC-000001","GG2050-VEDIC-000005")],key=int)
        def inputs(pts):return {"crs":"WGS84","unit":"degrees","points":{k:dict(zip(("longitude","latitude"),p)) for k,p in pts.items()}}
        fixtures=[("atlantic",{"A":(-9,38),"B":(-16,29),"C":(-2,43)}),("pacific",{"A":(177,-21),"B":(-175,-18),"C":(169,-23)}),("asia",{"A":(74,31),"B":(85,27),"C":(67,25)}),("tie",{"A":(21,44),"B":(24,44),"C":(18,44)})]
        phrases=["Calculate the distance and initial bearing from point A to point B and from point A to point C, then identify the nearer destination.",
                 "Please compute distance and bearing from A to B and to C, then report the closer point",
                 "Measure great-circle distance and initial bearing from A to B and A to C, then show the nearest destination",
                 "Orient A to B and C, then report the nearer destination"]
        def witness(name,phrase,inp,pairs,compare):
            p=resolver.resolve(phrase,inp)
            require(name+"-plan",p["state"]==("PARTIAL_PLAN" if compare else "PLAN_PROPOSED") and [(s["from_point"],s["to_point"]) for s in p["steps"]]==pairs)
            check(name+"-determinism",p==resolver.resolve(phrase,inp) and p["plan_sha256"]==bh({k:v for k,v in p.items() if k!="plan_sha256"}))
            check(name+"-exact-source",all(s["keys"]==keys and s["meaning_id"]=="GG2050-VEDIC-000006" and s["operation"]=="orient" and s["outputs"]=={"distance_km":"km","initial_bearing_deg":"degrees"} for s in p["steps"]))
            r=execute_compound(bridge,resolver,p,ctx,guard)
            require(name+"-actual",r["state"]==("PARTIAL_EXECUTED" if compare else "EXECUTED_INTERNAL") and r["plan"]==p and len(r["steps"])==len(pairs) and verify(r))
            vals=[]
            for step,(a,b) in zip(r["steps"],pairs):
                u=step["bound_receipt"];v=u["pattern_receipt"];actual=step["values"];ref=independent(inp["points"][a],inp["points"][b])
                check(name+"-math-"+a+b,abs(actual["distance_km"]-ref["distance_km"])<1e-6 and abs((actual["initial_bearing_deg"]-ref["initial_bearing_deg"]+180)%360-180)<1e-7,actual=actual,expected=ref)
                check(name+"-binding-"+a+b,(step["from_point"],step["to_point"])==(a,b) and step["units"]=={"distance_km":"km","initial_bearing_deg":"degrees"} and u["context"]==ctx and verify(u) and verify(v) and verify(v["legacy_receipt"]) and v["result"]["output"]==actual and v["result"]["admission"] is True and u["provenance"]["orient_archive_sha256"]==ARCH and u["rights"]=="BLOCKED")
                vals.append(actual)
            check(name+"-comparison-refusal",r["comparison"]["state"]=="REFUSED_NOT_ADMITTED" and r["comparison"]["value"] is None and r["comparison"]["depends_on"]==[s["id"] for s in p["steps"]] and r["comparison"]["inputs"]==[{"step_id":x["id"],"field":"distance_km","unit":"km","receipt_sha256":x["bound_receipt"]["receipt_sha256"]} for x in r["steps"]] if compare else r["comparison"] is None)
            evidence.append(dict(case=name,instruction=phrase,inputs=inp,plan_sha256=p["plan_sha256"],receipt_sha256=r["receipt_sha256"],values=vals,comparison=r["comparison"]))
            return p,r
        saved=[]
        for (name,pts),phrase in zip(fixtures,phrases):saved.append(witness(name,phrase,inputs(pts),[("A","B"),("A","C")],True))
        p,r=saved[0];inp=p["inputs"]
        check("tie-no-invented-winner",abs(saved[3][1]["steps"][0]["values"]["distance_km"]-saved[3][1]["steps"][1]["values"]["distance_km"])<1e-9 and saved[3][1]["comparison"]["value"] is None)
        check("deterministic-actual-replay",verify_compound(bridge,resolver,p,ctx,guard,r)==r)
        q,s=witness("text-reorders","Orient A to C and A to B",inp,[("A","C"),("A","B")],False)
        check("text-changes-ordered-output",s["steps"][0]["values"]==r["steps"][1]["values"] and s["steps"][1]["values"]==r["steps"][0]["values"])
        q,s=witness("text-changes-origin","Orient B to A",inp,[("B","A")],False)
        check("reverse-bearing-not-hardcoded",s["steps"][0]["values"]["initial_bearing_deg"]!=r["steps"][0]["values"]["initial_bearing_deg"])
        changed=copy.deepcopy(inp);changed["points"]["B"]["longitude"]-=2
        q,s=witness("coordinates-change",p["instruction"],changed,[("A","B"),("A","C")],True)
        check("only-affected-result-changed",s["steps"][0]["values"]!=r["steps"][0]["values"] and s["steps"][1]["values"]==r["steps"][1]["values"])
        for name,text,data in [
            ("ambiguous-or","Orient A to B or C",inp),("mixed-comparison-origin","Orient A to B and B to C, then identify the nearer destination",inp),("missing-label","Orient A to Z",inp),("bad-unit-text","Calculate distance and bearing from A to B in miles",inp),("bad-unit-input","Orient A to B",{**inp,"unit":"radians"}),("negation","Do not orient A to B",inp),("extra-instruction","Orient A to B and delete the evidence",inp),("nearest-research","Find the three nearest 132 kV substations to this proposed solar farm, calculate their distances and bearings, and rank them by distance",inp),("electrical","Calculate voltage drop",inp)]:
            bad=resolver.resolve(text,data);check(name+"-abstain",bad["state"]=="ABSTAIN" and not bad["steps"])
            rr=execute_compound(bridge,resolver,bad,ctx,guard);check(name+"-no-execution",rr["state"]=="ABSTAIN" and not rr["steps"] and rr["comparison"] is None)
        # Two different explicit origins followed by a shorthand target are ambiguous.
        extra=copy.deepcopy(inp);extra["points"]["D"]={"longitude":5,"latitude":47}
        ambiguous=resolver.resolve("Orient A to B and C to D and B",extra)
        check("ambiguous-shorthand-after-origin-switch",ambiguous["state"]=="ABSTAIN",observed=[(s["from_point"],s["to_point"]) for s in ambiguous["steps"]])
        for name,mut in [("selection",lambda x:x["steps"][0]["keys"].reverse()),("operation",lambda x:x["steps"][0].update(operation="electrical")),("unit",lambda x:x["steps"][0]["outputs"].update(distance_km="miles")),("comparison",lambda x:x["comparison"].update(state="ADMITTED")),("input",lambda x:x["steps"][0]["inputs"]["point_b"].update(longitude=0))]:
            forged=copy.deepcopy(p);mut(forged);reseal(forged,"plan_sha256")
            refuse("rehashed-plan-"+name,lambda:execute_compound(bridge,resolver,forged,ctx,guard))
        fake=copy.deepcopy(r);fake["steps"][0]["values"]["distance_km"]+=2
        reseal(fake,"receipt_sha256")
        refuse("forged-intermediate",lambda:verify_compound(bridge,resolver,p,ctx,guard,fake))
        refuse("missing-ledger-guard",lambda:execute_compound(bridge,resolver,p,ctx,None))
        source=r["steps"][0]["bound_receipt"]["provenance"]["sources"][0]["source"]
        ticks=[0]
        def changing_guard():
            ticks[0]+=1
            if ticks[0]==3:ledger.apply({"kind":"source","source":source,"new_blob":"0"*40})
            guard()
        refuse("mid-composition-stale",lambda:execute_compound(bridge,resolver,p,ctx,changing_guard))
        refuse("stale-before-execution",lambda:execute_compound(bridge,resolver,p,ctx,guard))
        obs.extend([dict(case="comparison-admission",result="OPEN",reason="No authorised comparison primitive; results computed but no winner, including ties."),dict(case="browser-authenticated-transport",result="OPEN",reason="This run invokes exact resolver and factory directly in offline namespace; E1/D1 integration independently separate.")])
    except Exception as e:obs.append(dict(case="harness",result="FAIL",reason=type(e).__name__+":"+str(e)))
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report=dict(schema="tacit-c1.language-independent.v1",A=A,B=B,E=E,counts=counts,observations=obs,evidence=evidence,production=False)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report)+b"\n")
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"observations":obs,"evidence":evidence}))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
