"""Independent A1 exact property/impact review; producer code executed, no writes."""
import copy,json,subprocess,sys
from pathlib import Path
from tacit_c_verify import canonical,sha,blob,need
from tacit_c_eighth_peer import pinned
from tacit_c_ninth import B_PIN

HEAD="7391b50343b7d7beecb8a32ccd748bfc00c2190b"
SOURCE="de46c88c993a18f3c8a17ea289c936e2cd42e316"
BONDS=("649209e8723af1efd4c73f85ebd90b524a2312907d8a5e24759c8bf72ad1f72a","bonds.json","821abf96d3e4c2f42e61d578dcefdfbda366c145b067f9cc9206fdaa91b6cf2d")
IMPACT=("ab7f89fb7b93a96db3a3d4c0dd0273dd41f17f11c641ba58dcbf258101aff5d0","impact.json","b49b0cbf518a7b9095339871fad585958640003e860053cfcc03562150fa2592")
PRODUCER=("5b3dc6d98ea6f3dec757263869d77a6261ce29d57ddce8a8659dfcd633ab1a86","property-impact.json","1233591210b19b006bb5970ecc85bdf0e5951cc3bef92e5e670871a4da0ca9e3")

def main():
    root,peer,out=map(Path,sys.argv[1:]);obs=[]
    def check(case,ok,**detail):obs.append(dict(case=case,result="PASS" if ok else "FAIL",**detail))
    def refuse(case,fn):
        try:fn()
        except (ValueError,TypeError,KeyError) as e:check(case,True,refusal=str(e))
        else:check(case,False)
    def digest(j):return sha(json.dumps(j,sort_keys=True,separators=(",",":"),allow_nan=False).encode())
    def seal(j):return {**j,"receipt_sha256":digest({k:v for k,v in j.items() if k!="receipt_sha256"})}
    try:
        need(subprocess.check_output(["git","-C",str(peer),"rev-parse","HEAD"],text=True).strip()==HEAD,"A1_CHECKOUT")
        need(blob((peer/"tools/tacit_a1_properties.py").read_bytes())==SOURCE,"A1_SOURCE_PIN")
        raw=pinned(root/"producer.zip",PRODUCER);producer=json.loads(raw)
        check("actual-producer-cli-reproduced-twice",all((root/f"{x}.json").read_bytes()==raw for x in ("first","second")),producer_checks=producer["counts"])
        b=json.loads(pinned(root/"bonds.zip",BONDS));m=json.loads(pinned(root/"impact.zip",IMPACT));br=json.loads(pinned(root/"b-final.zip",B_PIN))
        rows={str(r["kuiper"]["key"]):r for r in b["source_entries"]};keys=sorted(rows,key=int)
        need(len(rows)==8 and len(b["properties"])==32 and len(m["bond_details"])==5,"COHORT")
        props={(next(k for k,r in rows.items() if r["source"]==p["source_occurrence"]),p["property"]):p for p in b["properties"]}
        sys.path.insert(0,str(peer/"tools"))
        from tacit_a1_properties import Space
        s=Space(root)
        expr=lambda a=(),n=():{"all":list(a),"none":list(n)}
        pred=lambda field,value:dict(field=field,value=value)
        prop=lambda name,state,**kw:dict(field="property",name=name,state=state,**kw)
        def eval_pred(k,p):
            r=rows[k];f=p["field"]
            if f=="module":return r["module_classification"]["symbol"]==p["value"]
            if f=="meaning":return r["meaning_id"]==p["value"]
            if f=="key":return k==p["value"]
            if f=="depends_on":
                # Independent transitive closure by fixed-point iteration.
                targets={rows[p["value"]]["source"]["path"]}
                found=set()
                while True:
                    new={e["source"] for e in m["module_dependencies"] if e["target"] in targets|found}
                    if new<=found:break
                    found|=new
                return r["source"]["path"] in found
            v=props.get((k,p["name"]))
            if v is None or (v["state"]=="UNKNOWN" and p["state"]!="UNKNOWN"):return None
            return v["state"]==p["state"] and ("value" not in p or digest(v["value"])==digest(p["value"]))
        def expected(q):
            y=[];u=[]
            for k in keys:
                yes=[eval_pred(k,p) for p in q["all"]]
                no=[eval_pred(k,p) for p in q["none"]]
                if any(v is False for v in yes) or any(v is True for v in no):continue
                (u if None in yes or None in no else y).append(k)
            return y,u
        def verify(case,q):
            got=s.select(q);y,u=expected(q)
            check(case,got["keys"]==y and got["unknown_keys"]==u and got["occurrences"]==[dict(key=k,meaning_id=rows[k]["meaning_id"],source=rows[k]["source"]) for k in y] and got["receipt_sha256"]==seal(got)["receipt_sha256"] and got["authority"]=="SELECTION_ONLY" and s.verify_selection(got))
            return got
        for fam in ("Vg","Vn","Vd"):
            verify("module-"+fam,expr([pred("module",fam)]))
        for k in keys:
            verify("key-"+k,expr([pred("key",k)]))
            verify("meaning-"+k,expr([pred("meaning",rows[k]["meaning_id"])]))
            verify("reverse-dependency-"+k,expr([pred("depends_on",k)]))
            verify("all-but-key-"+k,expr(n=[pred("key",k)]))
        for name in sorted({p["property"] for p in b["properties"]}):
            for state in ("DECLARED","DERIVED","OBSERVED","UNKNOWN"):
                q=prop(name,state)
                verify("positive-"+name+"-"+state,expr([q]))
                verify("negative-"+name+"-"+state,expr(n=[q]))
                for fam in ("Vg","Vn","Vd"):
                    verify("intersection-"+fam+"-"+name+"-"+state,expr([pred("module",fam),q]))
                    verify("exclusion-"+fam+"-"+name+"-"+state,expr([pred("module",fam)],[q]))
        vg=verify("true-and-unknown",expr([pred("module","Vg"),prop("runtime_effects","OBSERVED")]))
        verify("false-dominates-unknown",expr([pred("module","Vg"),pred("module","Vd"),prop("runtime_effects","OBSERVED")]))
        good=s.select(expr([pred("module","Vg")]))
        for case,alter in (
          ("forged-key",lambda j:j["keys"].__setitem__(0,str(int(j["keys"][0])+1))),
          ("forged-occurrence",lambda j:j["occurrences"][0]["source"].update(path="engine/not-real.js")),
          ("forged-authority",lambda j:j.update(authority="EXECUTE")),
          ("forged-unknown",lambda j:j.update(unknown_keys=keys)),
          ("forged-manifest",lambda j:j.update(base_manifest_sha256="0"*64)),
          ("forged-expression",lambda j:j.update(expression=expr([pred("module","Vd")])))):
            fake=copy.deepcopy(good);alter(fake);refuse("rehashed-"+case,lambda:s.verify_selection(seal(fake)))
        refuse("wrong-exact-source-join",lambda:s.exact_join(good["keys"][0],rows[next(k for k in keys if k not in good["keys"])]["source"]))
        refuse("unknown-value-is-not-false",lambda:s.select(expr([prop("runtime_effects","UNKNOWN",value=False)])))
        refuse("unknown-state-rejected",lambda:s.select(expr([prop("typed_ports","VERIFIED")])))
        refuse("no-implicit-cohort-expansion",lambda:s.select(expr()))
        refuse("forged-key-in-predicate",lambda:s.select(expr([pred("key","1")])))
        for k,name in sorted(props):
            r=s.property_receipt(k,name)
            check("property-receipt-"+k+"-"+name,r["evidence"]==props[k,name] and r["key"]==k and r["receipt_sha256"]==seal(r)["receipt_sha256"])
        for i,e in enumerate(m["bond_details"]):
            actual=s.bond_receipt(e)
            check("exact-bond-"+str(i),all(actual[k]==v for k,v in e.items()) and actual["receipt_sha256"]==seal(actual)["receipt_sha256"])
            for field,value in (("source_port",{}),("target_endpoint",{}),("required_data",[]),("direction","reverse"),("formal_admission","GRANTED"),("family_receipts",{})):
                changed=copy.deepcopy(e);changed[field]=value
                refuse("altered-bond-"+str(i)+"-"+field,lambda:s.bond_receipt(changed))
        families={"Vg":["nearest-orient","orient"],"Vn":["nearest-orient"],"Vd":["electrical"]}
        for k,r in rows.items():
            src=r["source"];ops=families[r["module_classification"]["symbol"]]
            q={"kind":"source","source":src,"new_blob":"0"*40}
            got=s.reverse_impact(q);ids={x["sha256"] for x in got["affected_receipts"]}
            check("reverse-impact-"+k,got["affected_patterns"]==ops and all(br["results"][op]["receipt_sha256"] in ids for op in ops) and all(x["state"]=="STALE_FOR_NEW_INPUT_HISTORICAL_PRESERVED" for x in got["affected_receipts"]) and not got["addresses_changed"] and got["receipt_sha256"]==seal(got)["receipt_sha256"])
            check("display-stable-"+k,not s.reverse_impact({"kind":"presentation","source":src,"field":"display_colour"})["affected_patterns"])
        check("pinned-peer-bytes-preserved",sha(pinned(root/"b-final.zip",B_PIN))==B_PIN[2])
        obs.extend([dict(case="fresh-B1-receipt-impact",result="OPEN",reason="A1 exact first candidate binds predecessor B only."),dict(case="production-ledger-and-occurrence-repair",result="OPEN",reason="Owner authority not granted; no permanent writes."),dict(case="combined-browser-runtime",result="OPEN",reason="Peer integration separate.")])
    except Exception as e:obs.append(dict(case="harness",result="FAIL",reason=type(e).__name__+":"+str(e)))
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report=dict(schema="tacit-c1.a1-independent.v1",A1_head=HEAD,counts=counts,observations=obs,production=False,admission_changed=False)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for item in obs:
        if item["result"]!="PASS":print(json.dumps(item))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
