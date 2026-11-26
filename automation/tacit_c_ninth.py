"""Ninth-turn independent actual bridge and impact review; reuse producer code and oracles."""
import copy,json,math,subprocess,sys
from pathlib import Path
from tacit_c_verify import sha,blob,canonical,need,ARCHIVE,DESCRIPTOR
from tacit_c_eighth_peer import pinned
from tacit_c_seventh import member
from tacit_c_fifth import fixtures,expected_rank
from tacit_c_sixth import reference,near
B_HEAD="dbca4db3658850f421e8f7319b7cef7e540c1a46"
B_PIN=("79a5bf16c0e2a8676af99df14a462f4c76d68952c518540a8e2ed638d716612a","tacit-b-kuiper.json","3dd66b31abeb7ccf1734da8d2719a16be7d77bd5731a41096f4b9307f4a18e24")
B_OLD=("74fe853f050765545dfeb6404c8c84c9d9413754c0d8ec38131182544c7a4149","tacit-b-kuiper.json","7bb9e81ca066cafbaeae75a358da42768bb9db6a63746710025d88b7e0701796")
A_HEAD="c6ded836fa9d88c9bcb3d779401aa4c6c0373876"
A_PIN=("ab7f89fb7b93a96db3a3d4c0dd0273dd41f17f11c641ba58dcbf258101aff5d0","impact.json","b49b0cbf518a7b9095339871fad585958640003e860053cfcc03562150fa2592")
def runtime(root,obs):
    raw=pinned(root/"B-bridge.zip",B_PIN);rep=json.loads(raw)
    old=json.loads(pinned(root/"B-old.zip",B_OLD))
    froot=root/"factory";peer=root/"peer-b";droot=root/"peer-d"
    sys.path[:0]=[str(froot/"tools"),str(peer/"tools"),str(droot/"tools"),str(root/"oracle")]
    import package_factory as f
    import typed_package_execution as t
    from tacit_b_kuiper import Bridge
    from kuiper_select import Space
    import acceptance as oracle
    for p,pin in {"factory/tools/package_factory.py":"23247de65fde04a400bb30874fc7e81cca4b7ebe","factory/tools/typed_package_execution.py":"480a0d0d1ee1af0b7a5919e307564cf597b9f8ff","peer-b/tools/tacit_b_kuiper.py":"f0762d6974c266d8cf97d3647b483aa18ee4eb02","peer-b/tools/tacit_b_ranking.py":"8a3932e42a426cbae8dcc958e4673644615e2d44","peer-b/tools/tacit_b_electrical.py":"1d8875227690e5d2c5dc1d78c36e8fc4faf2055e","peer-b/tools/tacit_b_composition.py":"a97a9c4297e45b6befbff1cc4130c395a831332a","peer-d/tools/kuiper_select.py":"409208484604ab88a94b377a009548f2a2b67964","oracle/acceptance.py":"5101334d63b48d473e2123c13022d77fe32994a2","nearest/packages/nearest-candidate/kuiper_bond.py":"58bf06469a952b663459e9c2e277d93b51058dca"}.items():
        need(blob((root/p).read_bytes())==pin,"SOURCE_PIN:"+p)
    a_raw=member(root,"A-bonds");manifest=json.loads(a_raw)
    electrical=pinned(root/"B-bridge.zip",(B_PIN[0],"tacit-b-electrical.json","c8598fb9719ca84f8e36fdab24eee4b3c45ffc1e489527a3661b2fbfad307b47"))
    (root/"electrical.json").write_bytes(electrical)
    archive=root/"orient.zip";desc=f.strict(f.ADMISSIONS["orient"].read_bytes());build=f.build(desc,root/"inputs",archive)
    ar=archive.read_bytes()
    need(sha(ar)==ARCHIVE and build["descriptor_sha256"]==DESCRIPTOR,"IMMUTABLE_ORIENT")
    build_path=root/"build.json";build_path.write_bytes(f.canonical(build))
    cmd=[sys.executable,str(peer/"tools/tacit_b_kuiper.py"),"--factory",str(froot),"--d",str(droot),"--bonds",str(root/"A-bonds.zip"),"--nearest",str(root/"nearest"),"--nsources",str(root/"nearest-source"),"--esources",str(root/"electrical"),"--archive",str(archive),"--build",str(build_path),"--electrical",str(root/"electrical.json")]
    for name in ("bridge-first.json","bridge-second.json"):
        subprocess.run(cmd+["--out",str(root/name)],check=True,timeout=90)
        need((root/name).read_bytes()==raw,"FINAL_BRIDGE_REPLAY")
    need(all(rep[k]==old[k] for k in ("requests","results","refusals")) and len(rep["checks"])==17,"CORRECTIVE_RUNTIME_PARITY")
    obs.append({"case":"actual-final-B-bridge-CLI-repeat","result":"PASS","receipt_sha256":sha(raw),"archive_sha256":ARCHIVE,"prior_results_unchanged":True})
    def create(m=a_raw,a=ar):return Bridge(f,t,Space,m,a,build,root/"nearest",root/"nearest-source",root/"electrical")
    b=create()
    def check(label,ok,**kw):
        need(ok,label);obs.append({"case":label,"result":"PASS",**kw})
    def refuse(label,fn,reason):
        try:fn()
        except (ValueError,TypeError) as e:
            need(reason in str(e),"WRONG_REFUSAL:"+label+":"+str(e));obs.append({"case":label,"result":"PASS","refusal":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+label)
    for field,mut in (("key",lambda m:m["source_entries"][0]["kuiper"].update(key=m["source_entries"][0]["kuiper"]["key"]+1)),("source",lambda m:m["source_entries"][0]["source"].update(first=0)),("property",lambda m:m["properties"][0].update(state="OBSERVED")),("bond",lambda m:m["typed_bonds"][0].update(type="runtime_verified"))):
        m=copy.deepcopy(manifest);mut(m);refuse("authenticated-manifest-"+field,lambda:create(f.canonical(m)),"MANIFEST_AUTHENTICATION")
    refuse("raw-manifest-object",lambda:create(manifest),"MANIFEST_AUTHENTICATION")
    wanted={"orient":{1,5},"nearest-orient":{1,5,15,16},"electrical":{24,25,26,27}}
    for op,ids in wanted.items():
        expected=[str(k) for k in sorted(r["kuiper"]["key"] for r in manifest["source_entries"] if int(r["meaning_id"][-6:]) in ids)]
        q=rep["requests"][op];rc=rep["results"][op]
        check(op+"-source-key-selection",q["keys"]==b.keys(op)==expected)
        check(op+"-receipt-binding",rc["request_sha256"]==f.sha(f.canonical(q)) and rc["pattern_sha256"]==f.sha(f.canonical(rc["pattern"])) and rc["receipt_sha256"]==f.sha(f.canonical({k:v for k,v in rc.items() if k!="receipt_sha256"})) and rc["rights"]=="BLOCKED")
        if op!="orient":
            default=b.execute(q);check(op+"-formal-refusal",default==rep["refusals"][op] and default["state"]=="REFUSED" and default["nodes"]==[] and default["output"] is None and default["archive_sha256"] is None)
    for label,q in fixtures():
        req=b.request("nearest-orient",q);ref=expected_rank(oracle,q)
        if label=="coincident-distance-only":
            try:b.execute(req,experiment=True)
            except ValueError as e:obs.append({"case":"coincident-bearing-refused","result":"PASS","refusal":str(e)})
            else:raise ValueError("UNDEFINED_BEARING_ACCEPTED")
            continue
        rc=b.execute(req,experiment=True)
        if ref:
            p=next(x["location"] for x in q["records"] if x["id"]==ref[0]["id"])
            expected=oracle.oracle({"crs":"WGS84","unit":"degree","origin":q["query"],"destination":p})
            out=rc["output"]
            check("nearest-"+label,rc["state"]=="PRE_ADMISSION_EXECUTED" and rc["admission"] is False and out["id"]==ref[0]["id"] and near(out["distance_km"],expected["distance_km"]) and abs((out["initial_bearing_deg"]-expected["initial_bearing_deg"]+180)%360-180)<=1e-8)
        else:check("nearest-"+label,rc["state"]=="NO_ELIGIBLE_RECORD" and rc["output"] is None)
    nq=rep["requests"]["nearest-orient"];nr=rep["results"]["nearest-orient"]
    for label,mut in (("farther-eligible",lambda r:r["output"].update(id="far",distance_km=222.63898158654712)),("forged-admission",lambda r:r.update(admission=True,rights="CLEARED")),("forged-pattern",lambda r:r["pattern"]["keys"].reverse()),("wrong-receipt-result",lambda r:r["output"].update(initial_bearing_deg=0))):
        fake=copy.deepcopy(nr);mut(fake);fake=b.seal({k:v for k,v in fake.items() if k!="receipt_sha256"})
        refuse(label+"-rehashed",lambda:b.replay(nq,fake,experiment=True),"EXECUTION_REPLAY_MISMATCH")
    for label,mut in (("duplicate",lambda q:q["inputs"]["records"].append(q["inputs"]["records"][0])),("bad-coordinate",lambda q:q["inputs"]["query"].update(latitude=91)),("boolean-kV",lambda q:q["inputs"].update(minimumKv=True))):
        q=copy.deepcopy(nq);mut(q);refuse("nearest-"+label,lambda:b.execute(q,experiment=True),"PRODUCER_INPUT_REFUSED")
    for label,mut in (("changed-threshold",lambda q:q["inputs"].update(minimumKv=275)),("permuted-records",lambda q:q["inputs"]["records"].reverse()),("moved-location",lambda q:q["inputs"]["records"][1]["location"].update(longitude=1.1))):
        q=copy.deepcopy(nq);mut(q);refuse(label+"-stale-receipt",lambda:b.replay(q,nr,experiment=True),"EXECUTION_REPLAY_MISMATCH")
    eq=rep["requests"]["electrical"]
    for label,mut in (("baseline",lambda q:None),("single",lambda q:q.update(phases="single",nominalVoltageBasis="across-supply",nominalVolts=230)),("reactive",lambda q:q.update(powerFactor=.8,reactanceOhmPerKm=.1)),("fractional-route",lambda q:q["route"].update(value=125.5)),("leap-year",lambda q:q.update(hours=8784))):
        q=copy.deepcopy(eq);mut(q["inputs"]);rc=b.execute(q,experiment=True);want,_,_=reference(q["inputs"])
        check("electrical-"+label,rc["state"]=="PRE_ADMISSION_EXECUTED" and rc["archive_sha256"] is None and all(near(rc["output"][k],v) for k,v in want.items()))
    for label,mut,reason in (("geodesic",lambda q:q["route"].update(quantity="spherical_geographical_distance"),"NOT_ROUTE_LENGTH"),("km",lambda q:q["route"].update(unit="km"),"NOT_ROUTE_LENGTH"),("mean-current",lambda q:q["current"].update(context="mean_current"),"PEAK_CONTEXT_REQUIRED"),("ordinary-factor",lambda q:q.update(factorBasis="ordinary-load-factor"),"FACTOR_BASIS_MISMATCH"),("wrong-voltage-basis",lambda q:q.update(nominalVoltageBasis="across-supply"),"ELECTRICAL_INPUT_REFUSED"),("pf",lambda q:q.update(powerFactor=1.01),"ELECTRICAL_INPUT_REFUSED")):
        q=copy.deepcopy(eq);mut(q["inputs"]);refuse("electrical-"+label,lambda:b.execute(q,experiment=True),reason)
    oq=rep["requests"]["orient"]
    for label,mut,reason in (("keys",lambda q:q["keys"].reverse(),"SELECTION_KEYS"),("forged-key",lambda q:q["keys"].__setitem__(0,str(int(q["keys"][0])+1)),"SELECTION_KEYS"),("caller-experiment",lambda q:q.update(experiment=True),"FIELDS"),("unknown-op",lambda q:q.update(operation="eval"),"UNKNOWN_OPERATION"),("manifest",lambda q:q.update(manifest_sha256="0"*64),"REQUEST_PIN")):
        q=copy.deepcopy(oq);mut(q);refuse(label,lambda:b.execute(q),reason)
    refuse("tampered-archive",lambda:create(a=ar+b" ").execute(oq),"ARCHIVE_PIN")
    obs.append({"case":"new-package-authority","result":"OPEN","reason":"Only ORIENT archive admitted internally; nearest/electrical verified offline pre-admission, no redistribution."})
def impact(root,obs):
    raw=pinned(root/"A-impact.zip",A_PIN);m=json.loads(raw)
    need((root/"impact-first.json").read_bytes()==(root/"impact-second.json").read_bytes()==raw,"ACTUAL_IMPACT_REPLAY")
    peer=root/"peer-a";sys.path.insert(0,str(peer/"tools"))
    import tacit_a_impact as a
    need(blob((peer/"tools/tacit_a_impact.py").read_bytes())=="1fdb974e0bc363bc4f20d8e0eccd023d8d717a40","A_IMPACT_PIN")
    old=json.loads(member(root,"A-bonds"));need(m["source_entries"]==old["source_entries"] and m["properties"]==old["properties"] and m["base_manifest_sha256"]==a.BOND_SHA and m["live_consumer"] is False,"IMPACT_BASE")
    check=lambda label,ok: (need(ok,label),obs.append({"case":label,"result":"PASS"}))
    def refusal(label,fn,why):
        try:fn()
        except ValueError as e:need(why in str(e),"WRONG_REFUSAL:"+label);obs.append({"case":label,"result":"PASS","refusal":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+label)
    check("actual-A-impact-CLI-repeat",True)
    expected={"engine/v9-geodesy.js":["nearest-orient","orient"],"engine/v9-nearest-search.js":["nearest-orient"],"engine/voltage-drop.js":["electrical"]}
    for i,r in enumerate(m["source_entries"]):
        s=r["source"];e={"kind":"source","source":s,"new_blob":"0"*40};got=a.impact(m,e);want=expected[s["path"]]
        rs=sorted({x for p in m["patterns"] if p["operation"] in want for x in p["receipts"]})
        check("actual-source-impact-"+str(i),got["affected_patterns"]==want and [x["sha256"] for x in got["affected_receipts"]]==rs and all(x["state"]=="STALE_FOR_NEW_INPUT_HISTORICAL_PRESERVED" for x in got["affected_receipts"]) and not got["addresses_changed"])
        check("unchanged-source-"+str(i),a.impact(m,{**e,"new_blob":s["blob"]})["affected_patterns"]==[])
        check("display-colour-"+str(i),a.impact(m,{"kind":"presentation","source":s,"field":"display_colour"})["affected_receipts"]==[])
    for family,row in m["family_reviews"].items():
        q={"kind":"closure","family":family,"old_sha256":row["closure_sha256"],"new_sha256":"0"*64};got=a.impact(m,q)
        want=sorted(p["operation"] for p in m["patterns"] if family in p["families"])
        check("closure-impact-"+family,got["affected_patterns"]==want)
        refusal("stale-closure-"+family,lambda:a.impact(m,{**q,"old_sha256":"1"*64}),"STALE_CLOSURE_EVENT")
    for i,p in enumerate(m["properties"]):
        q={"kind":"property","source":p["source_occurrence"],"property":p["property"],"old_sha256":a.sha(a.canonical(p)),"new_sha256":"0"*64}
        want=sorted(x["operation"] for x in m["patterns"] if any(s["source"]==p["source_occurrence"] for s in x["sources"]))
        got=a.impact(m,q);check("property-impact-"+str(i),got["affected_patterns"]==want and not got["addresses_changed"])
    s=m["source_entries"][0]["source"]
    for field,val in (("path","engine/elsewhere.js"),("commit","0"*40),("first",0)):
        q={"kind":"source","source":{**s,field:val},"new_blob":"0"*40}
        refusal("wrong-source-"+field,lambda:a.impact(m,q),"UNKNOWN_OR_STALE_OCCURRENCE")
    check("five-bonds-remain-conditional",len(m["bond_details"])==5 and all(x["relationship_state"]=="CONDITIONAL_CANDIDATE" and x["formal_admission"]=="UNCHANGED" for x in m["bond_details"]) and len(m["incompatible_bonds"])==6)
    b=json.loads(pinned(root/"B-bridge.zip",B_PIN))
    check("A-patterns-match-B-actual-requests",all(p["keys"]==b["requests"][p["operation"]]["keys"] for p in m["patterns"]))
    obs.append({"case":"live-receipt-invalidation","result":"OPEN","reason":"A v1 sidecar models prior pinned receipts; actual B bridge receipt invalidation requires final A recovery sidecar and consuming live integration. Raw impact(m,event) is an internal trusted function."})
def main():
    mode,root,out=sys.argv[1],Path(sys.argv[2]),Path(sys.argv[3]);obs=[]
    try:{"runtime":runtime,"impact":impact}[mode](root,obs)
    except Exception as e:obs.append({"case":mode+"-review","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(o["result"]==k for o in obs) for k in ("PASS","FAIL","OPEN")}
    r={"schema":"vedic.tacit-c.ninth-turn.v1","mode":mode,"A_head":A_HEAD,"B_head":B_HEAD,"artifact_pins":{"A":A_PIN,"B":B_PIN},"observations":obs,"counts":counts,"formal_admission_changed":False,"redistribution":"BLOCKED"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(r));print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for o in obs:print(json.dumps(o))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
