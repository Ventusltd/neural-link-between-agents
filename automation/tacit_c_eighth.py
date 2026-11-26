"""Turn 8 baseline: exercise actual factory and D sparse selection, no new runtime."""
import copy, json, math, sys, zipfile
from pathlib import Path
from tacit_c_verify import sha,blob,canonical,need,DESCRIPTOR
from tacit_c_seventh import member
from tacit_c_fifth import artifact
def run(root,obs):
    sys.path[:0]=[str(root/"factory/tools"),str(root/"kuiper/tools")]
    import package_factory as f
    import kuiper_select as d
    need(blob((root/"factory/tools/package_factory.py").read_bytes())=="23247de65fde04a400bb30874fc7e81cca4b7ebe","FACTORY_PIN")
    need(blob((root/"kuiper/tools/kuiper_select.py").read_bytes())=="409208484604ab88a94b377a009548f2a2b67964","D_PIN")
    def check(label,ok):
        need(ok,label);obs.append({"case":label,"result":"PASS"})
    def refuse(label,func,reason):
        try:func()
        except (ValueError,TypeError) as e:
            need(reason in str(e),"WRONG_REFUSAL:"+label+":"+str(e))
            obs.append({"case":label,"result":"PASS","refusal":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+label)
    c=json.loads(member(root,"C-source"))
    actual=json.loads(member(root,"A-bonds"))
    # Read the actual factory allowlist; candidate evidence does not mutate it.
    orient=f.strict(f.ADMISSIONS["orient"].read_bytes())
    check("existing-ORIENT-only",set(f.ADMISSIONS)=={"orient"} and f.sha(f.canonical(f.admit(orient)))==DESCRIPTOR)
    check("no-reviewed-registry-authority",f.REVIEWED_RECEIPTS=={})
    for family,key,reason in (("nearest","nearest-substation","FAMILY_NOT_ADMITTED"),("electrical","electrical","SOURCE_RECEIPT_PENDING")):
        desc=f.strict(f.PENDING[key].read_bytes())
        refuse(family+"-actual-factory-gate",lambda:f.admit(desc),reason)
        raw=(root/"A-original.zip").read_bytes()
        need(sha(raw)=="c1ea563a7be0c1343d547d5678f46b86952a73bc8d5346d330a0faf8e7667772","A_ZIP")
        with zipfile.ZipFile(root/"A-original.zip") as z:
            sr,cl=[z.read(next(x for x in z.namelist() if x.endswith("family-review/"+family+"-"+k+".json"))) for k in ("source","closure")]
        rev=c["source_and_closure"][family]
        check(family+"-actual-review-pins",sha(sr)==rev["source_candidate_sha256"] and sha(cl)==rev["closure_candidate_sha256"] and rev["source"]["formal_acceptance"]=="OPEN")
        refuse(family+"-real-review-not-authority",lambda:f.review_receipt(key,sr,{},cl),"REVIEWED_RECEIPT_NOT_PINNED")
        forged=f.strict(sr);forged.update(independent_acceptance=True,owner_approval="APPROVED",rights="CLEARED")
        refuse(family+"-rehashed-owner-claim",lambda:f.review_receipt(key,f.canonical(forged),{},cl),"REVIEWED_RECEIPT_NOT_PINNED")
        other="electrical" if key=="nearest-substation" else "nearest-substation"
        refuse(family+"-valid-wrong-family-review",lambda:f.review_receipt(other,sr,{},cl),"REVIEWED_RECEIPT_NOT_PINNED")
        refused=copy.deepcopy(desc);refused["licence"]="CLEARED"
        refuse(family+"-rights-overreach",lambda:f.admit(refused),"LICENCE" if key=="nearest-substation" else reason)
    for label,mut,reason in [
       ("stale-ORIENT-edition",lambda x:x.update(edition="0"*40),"ADMISSION_MISMATCH"),
       ("ORIENT-changed-source-occurrence",lambda x:x["inputs"][0].update(commit="0"*40),"ADMISSION_MISMATCH"),
       ("ORIENT-changed-exports",lambda x:x.update(exports=["arbitrary"]),"ADMISSION_MISMATCH"),
       ("ORIENT-embedded-owner-approval",lambda x:x.update(owner_approval=True),"FIELDS"),
       ("ORIENT-public-rights",lambda x:x.update(licence="CLEARED"),"LICENCE"),
    ]:
        x=copy.deepcopy(orient);mut(x);refuse(label,lambda:f.admit(x),reason)
    # D's actual selection path, independent expected sets from A source rows.
    manifest=d.load(root/"A-bonds.zip")
    check("D-loads-exact-A-manifest",manifest==actual)
    space=d.Space(manifest);rows=manifest["source_entries"]
    properties={tuple(p["source_occurrence"][k] for k in d.FIELDS)+(p["property"],):p for p in manifest["properties"]}
    keys=tuple(sorted(r["kuiper"]["key"] for r in rows))
    def expected(module=None,meaning=None,property_name=None,state=None,key_min=None,key_max=None):
        out=[]
        for r in rows:
            k=r["kuiper"]["key"];src=tuple(r["source"][x] for x in d.FIELDS)
            p=properties.get(src+(property_name,))
            if module is not None and r["module_classification"]["symbol"]!=module:continue
            if meaning is not None and r["meaning_id"]!=meaning:continue
            if key_min is not None and k<key_min:continue
            if key_max is not None and k>key_max:continue
            if property_name is not None and (p is None or state is not None and p["state"]!=state):continue
            out.append(k)
        return tuple(sorted(out))
    queries=[{"module":m} for m in ("Vg","Vn","Vd")]+[{"meaning":r["meaning_id"]} for r in rows]+[
      {"property_name":"runtime_effects","state":"UNKNOWN"},{"property_name":"runtime_effects","state":"OBSERVED"},{"property_name":"typed_ports","state":"DERIVED","module":"Vd"},
      {"key_min":keys[1],"key_max":keys[-2]},{"key_min":0,"key_max":1},{"module":"Vg","meaning":next(r["meaning_id"] for r in rows if r["module_classification"]["symbol"]=="Vd")}]
    for i,q in enumerate(queries):check("D-independent-selection-"+str(i),space.select(**q)==expected(**q))
    for i,p in enumerate(space.project(keys)):
        k=keys[i];m=k*2654435769%2**32;r=math.sqrt(k+.5);theta=math.tau*m/2**32
        check("D-original-law-"+str(i),p["key"]==k and p["m"]==m and math.isclose(p["r"],r,rel_tol=1e-14) and math.isclose(p["x"],r*math.cos(theta),abs_tol=1e-7) and math.isclose(p["y"],r*math.sin(theta),abs_tol=1e-7))
    check("D-selection-not-execution",space.receipt({"module":"Vg"})["authority"]=="SELECTION_ONLY_NO_EXECUTION" and space.receipt({"module":"Vg"})["redistribution"]=="BLOCKED")
    corrupted=root/"mutated.zip";corrupted.write_bytes((root/"A-bonds.zip").read_bytes()+b" ")
    refuse("D-modified-ZIP-digest",lambda:d.load(corrupted),"ZIP_PIN")
    # Trust-boundary probe: direct constructor does not authenticate a raw object.
    # Do not promote this to a public-path vulnerability; actual load() rejects altered bytes.
    changed=copy.deepcopy(manifest);row=changed["source_entries"][0];newkey=row["kuiper"]["key"]+1
    need(newkey not in keys,"MUTATION_COLLISION")
    row["kuiper"]["key"]=newkey
    try:injected=d.Space(changed)
    except ValueError as e:obs.append({"case":"D-direct-object-forgery","result":"PASS","refusal":str(e)})
    else:
        need(newkey in injected.by_key,"CONSTRUCTOR_PROBE")
        obs.append({"case":"D-direct-object-forgery","result":"OPEN","reason":"Direct Space(manifest) accepts a fabricated in-range key with unchanged source. Exact ZIP loader blocks altered bytes. Browser/bridge must pin trusted input, not treat raw constructor as authentication."})
    obs.append({"case":"new-A-B-D-turn-8-artifacts","result":"OPEN","reason":"Baseline is prior actual implementation; new peer candidate/dry-run/overlay reviewed separately when exact evidence available."})
def main():
    root,out=Path(sys.argv[1]),Path(sys.argv[2]);obs=[]
    try:run(root,obs)
    except Exception as e:obs.append({"case":"turn8-baseline","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"vedic.tacit-c.turn8-baseline.v1","observations":obs,"counts":counts,"formal_admission":False,"permanent_allocation":False,"redistribution":"BLOCKED"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report));print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for o in obs:print(json.dumps(o))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
