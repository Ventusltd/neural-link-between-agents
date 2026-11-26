"""Independent replay of B corrective implementation, with explicit residual ranking gap."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tacit_c_peer_verify as old
from tacit_c_verify import blob, sha, canonical, need, ARCHIVE, DESCRIPTOR
HEAD="9431c1c704d7812b67eb85963a8310a86350ee87"
old.PINS["B"]=("15137938108","2b5cb2535974c3ab9b4cccd3bf84f7859dd5c775de8e708edfb0b66f6408e332","tacit-b-composition.json","e358464b75d37cb507c49a6f5969c365b8d800c52e146ae5c3c515c4284973b8")
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def verify(root,obs):
    for p,pin in {"b.py":"a97a9c4297e45b6befbff1cc4130c395a831332a","intake.py":"af5ed846d93192f047a37c1044a28a7884285e50","factory/tools/package_factory.py":"23247de65fde04a400bb30874fc7e81cca4b7ebe","factory/tools/typed_package_execution.py":"480a0d0d1ee1af0b7a5919e307564cf597b9f8ff","nearest/packages/nearest-candidate/kuiper_bond.py":"58bf06469a952b663459e9c2e277d93b51058dca","app/tools/tacit5b_activation.py":"eed42663679b2a09227ff1b389643973adcd4bb6"}.items():need(blob((root/p).read_bytes())==pin,"PIN:"+p)
    original=old.member(root,"B")
    b=json.loads(original)
    froot=root/"factory";sys.path.insert(0,str(froot/"tools"))
    import package_factory as f
    import typed_package_execution as t
    d=json.loads((froot/"packages/factory/admissions/orient.json").read_bytes())
    archive=root/"orient.zip";receipt=f.build(d,root/"inputs",archive);raw=archive.read_bytes()
    need(sha(raw)==ARCHIVE and receipt["descriptor_sha256"]==DESCRIPTOR,"ARCHIVE_PIN")
    (root/"build.json").write_bytes(f.canonical(receipt))
    cmd=[sys.executable,str(root/"b.py"),"--factory",str(froot),"--app",str(root/"app"),"--nearest",str(root/"nearest"),"--activation",str(root/"activation"),"--archive",str(archive),"--receipt",str(root/"build.json")]
    for name in ("replay1.json","replay2.json"):
        subprocess.run(cmd+["--out",str(root/name)],check=True,timeout=45)
    need((root/"replay1.json").read_bytes()==(root/"replay2.json").read_bytes()==original,"B_RECEIPT_REPLAY")
    need(b["schema"]=="tacit-b.composition-receipt.v2" and len(b["negative_checks"])==16 and b["nearest"]["state"]==b["electrical"]["state"]=="REFUSED" and b["nearest"]["selected_id"] is None and b["nearest"]["output"] is None and b["bond_validation"]["nearest_ranking_verified"] is False and b["bond_validation"]["admitted_nearest_runtime_receipt"] is None,"B_SCOPE")
    obs.append({"case":"actual-B-replay","result":"PASS","receipt_sha256":sha(original),"negative_checks":16})
    intake_cmd=[sys.executable,str(root/"intake.py"),"--factory",str(froot),"--archive",str(root/"A.zip"),"--out",str(root/"intake.json")]
    subprocess.run(intake_cmd,check=True,timeout=30)
    intake=json.loads((root/"intake.json").read_bytes())
    need(set(intake["families"])=={"nearest-substation","electrical"} and all(x["factory_review"]=="REVIEWED_RECEIPT_NOT_PINNED" and x["admission"] is False for x in intake["families"].values()),"INTAKE_OVERREACH")
    obs.append({"case":"actual-candidate-intake","result":"PASS","receipt_sha256":sha((root/"intake.json").read_bytes()),"families":intake["families"]})
    consumer=load(root/"b.py","b_corrected")
    bond=consumer.load_bond(root/"nearest/packages/nearest-candidate/kuiper_bond.py")
    sys.path.insert(0,str(root/"oracle"))
    import acceptance as oracle
    fixture=json.loads((root/"nearest/packages/nearest-candidate/consumer-fixture.json").read_bytes())
    request=fixture["input"];expected=fixture["expected"]
    q=b["orient_fallback"]["execution"]["pattern"]["request"]
    def actual_orient(inputs):
        result=t.execute(dict(q,input=inputs),raw,receipt)["pattern"]["output"]
        p=inputs["point_a"];z=inputs["point_b"]
        oracle.close_result(result,oracle.oracle(oracle.pair((p["longitude"],p["latitude"]),(z["longitude"],z["latitude"]))))
        return result
    def execute(req,res,digest=None):
        return consumer.validate_selected_contract(bond,req,res,digest or bond.sha(bond.canonical(req)),actual_orient)
    need(execute(request,expected)["point_b"]=={"longitude":1,"latitude":0},"CORRECT_SELECTION")
    obs.append({"case":"eligible-correct-distance","result":"PASS"})
    def refuse(name,req,res,reason,digest=None):
        try: execute(req,res,digest)
        except ValueError as e:need(str(e)==reason,"WRONG_REFUSAL:"+name+":"+str(e));obs.append({"case":name,"result":"PASS","reason":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+name)
    refuse("original-falsifier",request,{"id":"low","distance_km":0},"SELECTED_BELOW_THRESHOLD_OR_UNKNOWN")
    refuse("eligible-forged-distance",request,dict(expected,distance_km=0),"SELECTED_DISTANCE_MISMATCH")
    changed=copy.deepcopy(request);changed["records"][1]["voltages_kv"]=[]
    refuse("unknown-voltage",changed,expected,"SELECTED_BELOW_THRESHOLD_OR_UNKNOWN")
    changed=copy.deepcopy(request);changed["minimumKv"]=True
    refuse("boolean-threshold",changed,expected,"INVALID_VOLTAGE_THRESHOLD")
    changed=copy.deepcopy(request);changed["records"][1]["voltages_kv"]=[True,132]
    refuse("boolean-voltage",changed,expected,"INVALID_VOLTAGE_METADATA")
    changed=copy.deepcopy(request);changed["records"][1]["location"]["longitude"]=1.1
    refuse("stale-dataset",changed,expected,"INPUT_DIGEST_MISMATCH",bond.sha(bond.canonical(request)))
    # The candidate contract checks selection eligibility and distance, not ranking.
    far=oracle.oracle(oracle.pair((0,0),(2,0)))["distance_km"]
    got=execute(request,{"id":"far","distance_km":far})
    need(got["point_b"]["longitude"]==2,"RANKING_SCOPE_CHANGED")
    obs.append({"case":"eligible-but-not-nearest","result":"OPEN","observation":"actual hardened B contract accepts a farther eligible substation with correct distance; ranking remains unverified as declared","distance_km":far,"required":"exact admitted nearest ranking and runtime receipt"})
def main():
    root=Path(sys.argv[1]);out=Path(sys.argv[2]);obs=[]
    try:verify(root,obs)
    except Exception as e:obs.append({"case":"actual-review","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"vedic.tacit-c.hardened-b-review.v1","B_head":HEAD,"B_artifact":old.PINS["B"],"observations":obs,"counts":counts,"result":"FAIL" if counts["FAIL"] else "CORRECTION_HONOURED_RANKING_OPEN","admission":"BLOCKED","formal_factory_authority":"OPEN","publication":False}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"result":report["result"]}))
    for x in obs:
        if x["result"]!="PASS":print(json.dumps(x))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
