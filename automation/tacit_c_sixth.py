"""TACIT C sixth: actual B electrical replay, independent engineering oracle and reviewed bonds."""
import copy, json, math, subprocess, sys, zipfile
from pathlib import Path
from tacit_c_verify import sha,blob,canonical,need
B_HEAD="d59d62f0d29ba830cf0baa6e773ff053a86a94a2"
A_HEAD="ab9584fe564ee59ce7618769be00d54887b4fa4b"
PINS={"B":("c08e4299cff9e16023c24305fa4a02109ec8e13b19277e31b7d701f9135f099b","tacit-b-electrical.json","c8598fb9719ca84f8e36fdab24eee4b3c45ffc1e489527a3661b2fbfad307b47"),"A":("649209e8723af1efd4c73f85ebd90b524a2312907d8a5e24759c8bf72ad1f72a","bonds.json","821abf96d3e4c2f42e61d578dcefdfbda366c145b067f9cc9206fdaa91b6cf2d"),"C":("8d48284a1ed870d16d99504707c81e0650a23c24693a1e491a787e809bb08ffa","a-review.json","76080746a09f0c3fa6693211147acfa98716be50caeb766f4ee01a68fc9ac303")}
def member(root,key,name=None,pin=None):
    zpin,default,dpin=PINS[key];p=root/(key+".zip")
    need(sha(p.read_bytes())==zpin,"ZIP_PIN:"+key)
    name=name or default;pin=pin or dpin
    with zipfile.ZipFile(p) as z:
        hits=[x for x in z.infolist() if x.filename==name or x.filename.endswith("/"+name)]
        need(len(hits)==1 and hits[0].file_size<=4_000_000,"MEMBER:"+name)
        raw=z.read(hits[0])
    need(sha(raw)==pin,"CONTENT:"+name)
    return raw
def reference(q):
    # Independently express the balanced sinusoidal voltage-drop approximation and conductor I²R losses.
    i=q["current"]["value"];l=q["route"]["value"]/1000
    r=q["resistanceOhmPerKm"];x=q["reactanceOhmPerKm"];pf=q["powerFactor"]
    n=3 if q["phases"]=="three" else 2
    multiplier=math.sqrt(3) if n==3 else 2
    phi=math.acos(pf)
    resistive=multiplier*i*l*r*math.cos(phi)
    reactive=multiplier*i*l*x*math.sin(phi)
    drop=resistive+reactive
    loss=n*i*i*l*r
    return {"drop":drop,"percent":drop/q["nominalVolts"]*100,"loss":loss,"energy":loss*q["lossLoadFactor"]*q["hours"]/1000},resistive,reactive
def near(a,b):
    return type(a) in (int,float) and math.isfinite(a) and math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-9)
def verify(root,obs):
    for p,pin in {"factory/tools/package_factory.py":"23247de65fde04a400bb30874fc7e81cca4b7ebe","tacit_b_electrical.py":"1d8875227690e5d2c5dc1d78c36e8fc4faf2055e","tacit_b_composition.py":"a97a9c4297e45b6befbff1cc4130c395a831332a","tacit_b_candidate_intake.py":"85503fd264c7160aaa0982f47f6e466c6611896d","electrical/module.mjs":"85f48ecf7effabb47973b0a056f90e82b8196ef2","electrical/adapter.mjs":"e554f03e6b1d1e7ab2d522e0d3bd4cc43da2bbc6","ports.json":"d90c557d09ce06564abab45718aeea21dd03c7b3"}.items():need(blob((root/p).read_bytes())==pin,"SOURCE:"+p)
    froot=root/"factory";sys.path[:0]=[str(froot/"tools"),str(root)]
    import package_factory as f
    import tacit_b_electrical as peer
    original=member(root,"B");b=json.loads(original)
    a=json.loads(member(root,"A"));c=json.loads(member(root,"C"))
    intake_raw=member(root,"B","tacit-b-reviewed-intake.json","3bbc8f816deb978e338287ae4b33a365d3c1cb0f37a8d073dbd96eacc548fd41")
    desc=f.strict((froot/"packages/factory/pending/electrical.json").read_bytes())
    input_root=root/"electrical"
    def refuse(label,fn,reason):
        try:fn()
        except (ValueError,TypeError) as e:
            need(reason in str(e),"WRONG_REFUSAL:"+label+":"+str(e));obs.append({"case":label,"result":"PASS","reason":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+label)
    for name in ("electrical-1.json","electrical-2.json"):
        p=root/name
        subprocess.run([sys.executable,str(root/"tacit_b_electrical.py"),"--factory",str(froot),"--inputs",str(input_root),"--out",str(p)],check=True,timeout=60)
        need(p.read_bytes()==original,"B_ELECTRICAL_REPLAY")
    need(b["archive"] is None and b["admission"]=="SOURCE_RECEIPT_PENDING" and b["redistribution"]=="BLOCKED" and b["independent_acceptance"] is False,"B_SCOPE")
    obs.append({"case":"actual-B-electrical-CLI-replay","result":"PASS","receipt_sha256":sha(original),"archive":None})
    p=root/"intake-replay.json"
    subprocess.run([sys.executable,str(root/"tacit_b_candidate_intake.py"),"--factory",str(froot),"--archive",str(root/"A-original.zip"),"--review",str(root/"C.zip"),"--out",str(p)],check=True,timeout=30)
    need(p.read_bytes()==intake_raw,"ACTUAL_INTAKE_PARITY")
    intake=json.loads(intake_raw)
    for name,registered in (("electrical","electrical"),("nearest","nearest-substation")):
        row=intake["families"][registered];cr=c["source_and_closure"][name];ar=a["family_reviews"][name]
        need(row["review"]==cr and row["source_sha256"]==ar["source_sha256"]==cr["source_candidate_sha256"] and row["closure_sha256"]==ar["closure_sha256"]==cr["closure_candidate_sha256"] and row["factory_review"]=="REVIEWED_RECEIPT_NOT_PINNED" and row["admission"] is False,"REVIEW_BINDING")
    obs.append({"case":"actual-A-C-B-review-intake","result":"PASS","receipt_sha256":sha(intake_raw),"factory_gate":"REVIEWED_RECEIPT_NOT_PINNED"})
    ports=json.loads((root/"ports.json").read_bytes())
    need(a["electrical"]==ports["functions"] and len(a["source_entries"])==8 and len(a["typed_bonds"])==5 and len(a["incompatible_bonds"])==6 and a["static_source_graph"]["execution_edges"]==[] and len(a["properties"])==32 and a["admission"]=="UNCHANGED" and a["redistribution"]=="BLOCKED","A_TYPED_MANIFEST")
    source={(r["meaning_id"],r["kuiper"]["key"]):r["source"] for r in a["source_entries"]}
    need(len(source)==8 and all(len(p)==10 for p in a["properties"]),"A_PROPERTIES")
    for item in a["properties"]:need(item["source_occurrence"] in source.values() and item["state"] in ("OBSERVED","DERIVED","UNKNOWN"),"PROPERTY_BINDING")
    for r in a["source_entries"]:
        clone=copy.deepcopy(r);clone["module_classification"]={"symbol":"synthetic mutation"};need((clone["source"],clone["kuiper"])==(r["source"],r["kuiper"]),"PRESENTATION_ID_MUTATION")
    need(any("distance is not route length"==x["reason"] for x in a["incompatible_bonds"]),"ROUTE_BOUNDARY")
    obs.append({"case":"A-typed-port-and-bond-evidence","result":"PASS","receipt_sha256":PINS["A"][2],"source_entries":8,"typed_bonds":5,"incompatible_bonds":6,"properties":32,"runtime_trace":False})
    request=b["request"];cases=[("reference",request)]
    for label,mut in [
      ("single-phase",lambda q:q.update(phases="single",nominalVoltageBasis="across-supply",nominalVolts=230)),
      ("lagging-reactive",lambda q:q.update(powerFactor=.8,reactanceOhmPerKm=.1)),
      ("fractional-route",lambda q:q["route"].update(value=125.5)),
      ("leap-year-bound",lambda q:q.update(hours=8784)),
      ("unity-loss-load-factor",lambda q:q.update(lossLoadFactor=1)),
      ("small-positive-current",lambda q:q["current"].update(value=.01)),
    ]:
        q=copy.deepcopy(request);mut(q);cases.append((label,q))
    for label,q in cases:
        got=peer.execute(f,desc,input_root,q);ref,rv,xv=reference(q);out=got["outputs"]
        need(got["request_sha256"]==f.sha(f.canonical(q)) and got["descriptor_sha256"]==f.sha(f.canonical(desc)) and got["admission"]=="SOURCE_RECEIPT_PENDING" and got["archive"] is None,"EXECUTION_BINDING")
        need(all(near(out[k]["value"],v) for k,v in ref.items()),"ORACLE:"+label)
        need([out[k]["unit"] for k in ("drop","percent","loss","energy")]==["V","%","W","kWh"] and near(out["drop"]["resistiveVolts"],rv) and near(out["drop"]["reactiveVolts"],xv),"UNITS_COMPONENTS:"+label)
        obs.append({"case":label,"result":"PASS","actual":{k:v["value"] for k,v in out.items()},"reference":ref,"request_sha256":got["request_sha256"]})
    for label,mut,why in [
       ("geodesic-substituted",lambda q:q["route"].update(quantity="spherical_geographical_distance"),"NOT_ROUTE_LENGTH"),
       ("route-origin-inferred",lambda q:q["route"].update(origin="nearest-result"),"NOT_ROUTE_LENGTH"),
       ("route-unit-km",lambda q:q["route"].update(unit="km"),"NOT_ROUTE_LENGTH"),
       ("mean-current",lambda q:q["current"].update(context="mean_current"),"PEAK_CONTEXT_REQUIRED"),
       ("energy-as-power",lambda q:q["current"].update(quantity="annual_energy_loss",unit="kWh"),"PEAK_CONTEXT_REQUIRED"),
       ("ordinary-load-factor",lambda q:q.update(factorBasis="ordinary-load-factor"),"FACTOR_BASIS_MISMATCH"),
       ("wrong-phase-basis",lambda q:q.update(phases="single"),"ELECTRICAL_INPUT_REFUSED"),
       ("bad-phase",lambda q:q.update(phases="dc"),"ELECTRICAL_INPUT_REFUSED"),
       ("zero-pf",lambda q:q.update(powerFactor=0),"ELECTRICAL_INPUT_REFUSED"),
       ("over-unity-pf",lambda q:q.update(powerFactor=1.01),"ELECTRICAL_INPUT_REFUSED"),
       ("negative-reactance",lambda q:q.update(reactanceOhmPerKm=-.1),"ELECTRICAL_INPUT_REFUSED"),
       ("zero-route",lambda q:q["route"].update(value=0),"ELECTRICAL_INPUT_REFUSED"),
       ("boolean-current",lambda q:q["current"].update(value=True),"ELECTRICAL_INPUT_REFUSED"),
       ("excess-hours",lambda q:q.update(hours=8785),"ELECTRICAL_INPUT_REFUSED"),
       ("invalid-loss-factor",lambda q:q.update(lossLoadFactor=0),"ELECTRICAL_INPUT_REFUSED"),
       ("overflow",lambda q:q["current"].update(value=1e200),"ELECTRICAL_INPUT_REFUSED"),
    ]:
        q=copy.deepcopy(request);mut(q);refuse(label,lambda q=q:peer.execute(f,desc,input_root,q),why)
    refuse("electrical-factory-gate",lambda:f.admit(desc),"SOURCE_RECEIPT_PENDING")
    refuse("review-digest-not-authority",lambda:f.review_receipt("electrical",b"{}",{},b"{}"),"REVIEWED_RECEIPT_NOT_PINNED")
    # Caller provenance is declared, not independently measured; leading PF is outside the implemented lagging/unity model.
    obs.append({"case":"formal-electrical-admission","result":"OPEN","reason":"No admitted electrical archive; exact reviewed registry/handler/owner authority and rights remain open."})
    obs.append({"case":"engineering-model-boundary","result":"OPEN","reason":"Synthetic arithmetic only; actual route, operating resistance and peak current are caller declarations; balanced AC lagging or unity model, no cable selection or certified design."})
def main():
    root=Path(sys.argv[1]);out=Path(sys.argv[2]);obs=[]
    try:verify(root,obs)
    except Exception as e:obs.append({"case":"actual-sixth-review","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"vedic.tacit-c.sixth-turn.v1","A_head":A_HEAD,"B_head":B_HEAD,"artifact_pins":PINS,"observations":obs,"counts":counts,"verdict":"FAIL" if counts["FAIL"] else "ELECTRICAL_PRE_ADMISSION_INDEPENDENTLY_VERIFIED","formal_admission":False,"redistribution":"BLOCKED"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report));print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"verdict":report["verdict"]}))
    for o in obs:print(json.dumps(o))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
