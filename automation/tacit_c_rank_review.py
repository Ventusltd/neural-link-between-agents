"""Replay exact B fifth-turn ranking, preserving earlier falsification. No new producer."""
import copy,json,sys,subprocess
from pathlib import Path
import tacit_c_peer_verify as old
from tacit_c_verify import sha,blob,canonical,need,ARCHIVE,DESCRIPTOR
from tacit_c_fifth import fixtures,expected_rank
HEAD="b4108fd17686f05c13326efdfaa8fd29c893b532"
old.PINS["B"]=("15138469041","6c316fd5eda0b5df597049666244251339a306577a9145c0c997c3e1fe3d638b","tacit-b-ranking.json","5c71125c76e2495f88d447f60f2f93d13f36198641e8bb4379964c45e7e2be51")
def verify(root,obs):
    for p,pin in {"tacit_b_ranking.py":"8a3932e42a426cbae8dcc958e4673644615e2d44","tacit_b_composition.py":"a97a9c4297e45b6befbff1cc4130c395a831332a","factory/tools/package_factory.py":"23247de65fde04a400bb30874fc7e81cca4b7ebe","factory/tools/typed_package_execution.py":"480a0d0d1ee1af0b7a5919e307564cf597b9f8ff","nearest-source/adapter.mjs":"4f31929dab709d22eea053c474616f72ee4f4153","nearest-source/v9-nearest-search.js":"d2ab3b111eb09f7af3df3a9fce9ad0a9dc1dea99","nearest-source/v9-geodesy.js":"14023f06d4ef2ea806437863bd35dee954c46b11","nearest/packages/nearest-candidate/kuiper_bond.py":"58bf06469a952b663459e9c2e277d93b51058dca"}.items():
        need(blob((root/p).read_bytes())==pin,"PIN:"+p)
    original=old.member(root,"B");report=json.loads(original)
    froot=root/"factory";sys.path[:0]=[str(froot/"tools"),str(root),str(root/"oracle")]
    import package_factory as f
    import typed_package_execution as t
    import acceptance as oracle
    from tacit_b_ranking import Ranking
    from tacit_b_composition import load_bond,validate_selected_contract
    d=f.strict((froot/"packages/factory/admissions/orient.json").read_bytes())
    pending=f.strict((froot/"packages/factory/pending/nearest-substation.json").read_bytes())
    archive=root/"orient.zip";receipt=f.build(d,root/"inputs",archive);raw=archive.read_bytes()
    need(sha(raw)==ARCHIVE and receipt["descriptor_sha256"]==DESCRIPTOR,"ARCHIVE_PIN")
    receipt_path=root/"build.json";receipt_path.write_bytes(f.canonical(receipt))
    cmd=[sys.executable,str(root/"tacit_b_ranking.py"),"--factory",str(froot),"--nearest",str(root/"nearest"),"--sources",str(root/"nearest-source"),"--archive",str(archive),"--receipt",str(receipt_path)]
    for name in ("rank1.json","rank2.json"):
        subprocess.run(cmd+["--out",str(root/name)],check=True,timeout=60)
        need((root/name).read_bytes()==original,"ACTUAL_B_RECEIPT_REPLAY")
    need(report["factory_admission"]=="FAMILY_NOT_ADMITTED" and report["nearest_archive"] is None and report["rights"]=="BLOCKED" and report["independent_acceptance"] is False,"REPORT_SCOPE")
    obs.append({"case":"B-actual-CLI-byte-parity","result":"PASS","receipt_sha256":sha(original),"archive_sha256":sha(raw)})
    rank=Ranking(f,pending,root/"nearest-source")
    bond=load_bond(root/"nearest/packages/nearest-candidate/kuiper_bond.py")
    def orient(points):
        q={"schema":t.SCHEMA,"family":"orient","export":"orient","descriptor_sha256":t.DESCRIPTOR,"archive_sha256":t.ARCHIVE,"ports":dict(t.PORTS),"input":points}
        return t.execute(q,raw,receipt)["pattern"]["output"]
    def compose(req,rc):
        result=rank.replay(req,rc)
        if result is None:return None
        pts=validate_selected_contract(bond,req,result,bond.sha(bond.canonical(req)),orient)
        return orient(pts)
    def refusal(label,fn,why):
        try:fn()
        except (ValueError,TypeError) as e:
            need(why in str(e),"WRONG_REFUSAL:"+label+":"+str(e))
            obs.append({"case":label,"result":"PASS","reason":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+label)
    for label,q in fixtures():
        reference=expected_rank(oracle,q);rc=rank.run(q);actual=rank.replay(q,rc)
        need(rc["request_sha256"]==f.sha(f.canonical(q)) and rc["request"]==q and rc["admission"] is False and rc["redistribution"]=="BLOCKED" and rc["descriptor_sha256"]==f.sha(f.canonical(pending)),"RECEIPT_BINDING:"+label)
        if reference:
            expected=reference[0]
            need(actual["id"]==expected["id"] and abs(actual["distance_km"]-expected["distance_km"])<=1e-8,"RANK_ORACLE:"+label)
            if label=="coincident-distance-only":
                try:compose(q,rc)
                except ValueError as e:obs.append({"case":"coincident-bearing-refused","result":"PASS","reason":str(e)})
                else:raise ValueError("UNDEFINED_BEARING_ACCEPTED")
            else:
                loc=next(r["location"] for r in q["records"] if r["id"]==actual["id"])
                ref=oracle.oracle({"crs":"WGS84","unit":"degree","origin":q["query"],"destination":loc})
                out=compose(q,rc)
                need(abs(out["distance_km"]-ref["distance_km"])<=1e-8 and abs((out["initial_bearing_deg"]-ref["initial_bearing_deg"]+180)%360-180)<=1e-8,"ORIENT_ORACLE:"+label)
        else:
            need(actual is None and compose(q,rc) is None,"EMPTY_REFUSAL:"+label);out=None
        obs.append({"case":label,"result":"PASS","request_sha256":rc["request_sha256"],"ranking_receipt_sha256":rc["receipt_sha256"],"actual":actual,"expected":reference[0] if reference else None})
    request=fixtures()[0][1];good=rank.run(request)
    def rehash(rc):
        rc["receipt_sha256"]=f.sha(f.canonical({k:v for k,v in rc.items() if k!="receipt_sha256"}));return rc
    for label,mut in [
        ("farther-eligible-rehashed",lambda rc:rc.update(result={"id":"far","distance_km":222.63898158654712},selected_location={"longitude":2,"latitude":0})),
        ("correct-id-false-distance",lambda rc:rc["result"].update(distance_km=0)),
        ("false-source-pin",lambda rc:rc["source_pins"]["index.mjs"].update(sha256="0"*64)),
        ("false-admission-true-maths",lambda rc:rc.update(admission=True,redistribution="CLEARED")),
        ("false-coordinate",lambda rc:rc["selected_location"].update(longitude=2)),
        ("false-descriptor",lambda rc:rc.update(descriptor_sha256="0"*64)),
        ("wrong-distance-unit",lambda rc:rc.update(distance_unit="m")),
    ]:
        rc=copy.deepcopy(good);mut(rc);refusal(label,lambda rc=rc:compose(request,rehash(rc)),"RANKING_REPLAY_MISMATCH")
    for label,mut in [
        ("permuted-stale",lambda q:q["records"].reverse()),
        ("changed-threshold",lambda q:q.update(minimumKv=275)),
        ("changed-dataset",lambda q:q["records"][1]["location"].update(longitude=1.1)),
    ]:
        q=copy.deepcopy(request);mut(q);refusal(label,lambda q=q:compose(q,good),"RANKING_REPLAY_MISMATCH")
    for label,mut in [
        ("duplicate-id",lambda q:q["records"].append(q["records"][0])),
        ("boolean-voltage",lambda q:q["records"][1].update(voltages_kv=[True,132])),
        ("boolean-threshold",lambda q:q.update(minimumKv=True)),
        ("out-of-range-coordinate",lambda q:q["records"][1]["location"].update(latitude=91)),
        ("invalid-crs",lambda q:q.update(crs="EPSG:27700")),
        ("negative-voltage",lambda q:q["records"][1].update(voltages_kv=[-132])),
        ("wrong-coordinate-label",lambda q:q.update(query={"lon":0,"lat":0})),
    ]:
        q=copy.deepcopy(request);mut(q);refusal(label,lambda q=q:rank.run(q),"PRODUCER_INPUT_REFUSED")
    source=root/"nearest-source/v9-nearest-search.js";original_source=source.read_bytes()
    try:
        source.write_bytes(original_source+b"\n");refusal("source-byte-mutation",lambda:Ranking(f,pending,root/"nearest-source"),"SOURCE_PIN")
    finally:source.write_bytes(original_source)
    refusal("factory-nearest-formal-admission",lambda:f.admit(pending),"FAMILY_NOT_ADMITTED")
    obs.append({"case":"formal-runtime-admission","result":"OPEN","reason":"Actual pre-admission chain verified; factory and rights remain blocked."})
def main():
    root=Path(sys.argv[1]);out=Path(sys.argv[2]);obs=[]
    try:verify(root,obs)
    except Exception as e:obs.append({"case":"actual-ranking-review","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"vedic.tacit-c.ranking-review.v1","B_head":HEAD,"B_artifact":old.PINS["B"],"observations":obs,"counts":counts,"verdict":"FAIL" if counts["FAIL"] else "PRE_ADMISSION_RANKING_INDEPENDENTLY_VERIFIED","formal_admission":False,"redistribution":"BLOCKED"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"verdict":report["verdict"]}))
    for o in obs:print(json.dumps(o))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
