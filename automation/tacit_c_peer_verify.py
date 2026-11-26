"""Independent examination of actual A/B evidence and replay of exact B consumer."""
import copy
import json
import math
from pathlib import Path
import subprocess
import sys
import zipfile

from tacit_c_verify import blob, canonical, need, sha, ARCHIVE, DESCRIPTOR, MODULE, RECEIPT

PINS={
"A":("15138765037","0bc8e66ecec5ceba2800201b44b835b6ffe9645fd5959e9307cf23d634b41376","candidate.json","70c91c6013bbd86bfd9f5e2641bd94decc148961c5eb8728fe17547a5dfb7bfe"),
"B":("15138405406","ec237d8e7303871ce2ccc9039cc39e093a363fa5633dfdaca2d823963a0154b7","tacit-b-composition.json","b2cb04e67e3668682400d6767d197612322c9ea4a75fcc765da41f800bafbcbf"),
"identity":("15126683549","c4b7a4d582b56af8380ae33ab0c64782ec33b1e05c99d88af83a3b494eb4ead5","kuiper-producer.json",None)}
A_HEAD="6a3f20588e0d6c5ef6d73698f4abcf27dccaf237"
B_HEAD="6d8dea0f2eefda0f6c0c9116487a40a75df774f3"
SOURCE_COMMIT="487ec7bd38dfa5aecb1c75da53b4a866ab2101cb"
EXPECTED={1:86415575118,5:86415575222,15:86415575280,16:86415575302,24:86415575415,25:86415575455,26:86415575478,27:86415575510}
SOURCE_BLOBS={"engine/v9-geodesy.js":"14023f06d4ef2ea806437863bd35dee954c46b11","engine/v9-nearest-search.js":"d2ab3b111eb09f7af3df3a9fce9ad0a9dc1dea99","engine/voltage-drop.js":"85f48ecf7effabb47973b0a056f90e82b8196ef2"}

def member(root,kind,name=None):
    _,digest,default,pin=PINS[kind]
    filename=root/(kind+".zip")
    need(sha(filename.read_bytes())==digest,"ARTIFACT_PIN:"+kind)
    with zipfile.ZipFile(filename) as z:
        hits=[i for i in z.infolist() if i.filename==(name or default) or i.filename.endswith("/"+(name or default))]
        need(len(hits)==1 and hits[0].file_size<=20_000_000,"ARTIFACT_MEMBER:"+kind)
        raw=z.read(hits[0])
    if not name and pin: need(sha(raw)==pin,"RECEIPT_PIN:"+kind)
    return raw

def verify_a(root,obs):
    a=json.loads(member(root,"A"))
    producer_raw=member(root,"identity")
    producer=json.loads(producer_raw)
    need(a["schema"]=="vedic.tacit-a-candidate-closure.v1" and a["admission"]=="REFUSED_REVIEW_PENDING" and a["runtime_verified"] is False and a["wafer_replayed"] is False,"A_SCOPE")
    need(a["producer_receipt_sha256"]==sha(producer_raw),"A_PRODUCER_RECEIPT")
    dictionary=(root/"dictionary.json").read_bytes()
    need(sha(dictionary)==a["dictionary_sha256"]=="327803457f1528803278959ad7c107caed76489cfb2263db7143973a151b3c96","DICTIONARY_PIN")
    entries={e["gg_id"]:e for e in json.loads(dictionary)["entries"]}
    translations={r["id"]:r["source"] for r in json.loads((root/"translation-geodesy.json").read_bytes())["records"]}
    rows={int(r["meaning_id"].split("-")[-1]):r for r in a["entries"]}
    need(len(a["entries"])==len(rows)==8 and set(rows)==set(EXPECTED),"A_COVERAGE")
    # Independent direct join and physical-span digest, no use of A's validator.
    for number,key in EXPECTED.items():
        row=rows[number];s=row["source"];e=entries[row["meaning_id"]]
        need(s==(e.get("source") or translations[e["translation_ref"]]),"A_DICTIONARY_OCCURRENCE")
        need(s["repo"]=="Ventusltd/ventus-grid-engine" and s["commit"]==SOURCE_COMMIT and SOURCE_BLOBS[s["path"]]==s["blob"],"A_OCCURRENCE_PIN")
        raw=(root/Path(s["path"]).name).read_bytes()
        need(blob(raw)==s["blob"] and sha(raw)==row["module_sha256"],"A_ACTUAL_BYTES")
        lines=raw.splitlines(keepends=True)
        need(1<=s["first"]<=s["last"]<=len(lines),"A_SPAN_BOUNDS")
        need(sha(b"".join(lines[s["first"]-1:s["last"]]))==row["physical_span_sha256"],"A_SPAN_HASH")
        hits=[r for r in producer["bodies"] if (r["repo"],r["commit"],r["path"],r["blob"],r["line"])==(s["repo"].split("/")[1],s["commit"],s["path"],s["blob"],s["first"])]
        need(len(hits)==1,"A_PRODUCER_JOIN")
        p=hits[0]
        need(p["verified"] and p["on_wafer"] and p["blob_matches_body"] and p["blob_at_path"]==s["blob"],"A_PRODUCER_STATE")
        need(p["key"]==p["k0"]+p["lines_before"]+s["first"]-1==key==row["kuiper"]["key"],"A_KEY_ARITHMETIC")
        need(a["reverse_key_to_meaning"][str(key)]==row["meaning_id"],"A_REVERSE")
        obs.append({"case":"A-source-"+str(number),"result":"PASS","meaning_id":row["meaning_id"],"key":key,"occurrence":s,"span_sha256":row["physical_span_sha256"],"scope":"pinned receipt arithmetic and source span only"})
    props=a["properties"]
    need(len(props)==16 and all(p["state"]=="DERIVED" and p["unknown_reason"] is None for p in props),"A_PROPERTY_CONTRACT")
    def identity(p): return tuple(p["source_occurrence"][k] for k in ("repo","commit","path","blob","first","last"))
    mutated=copy.deepcopy(props[0]);mutated["value"]="synthetic changed presentation"
    need(identity(mutated)==identity(props[0]),"PROPERTY_ID_DRIFT")
    mutated["source_occurrence"]["first"]+=1
    need(identity(mutated)!=identity(props[0]),"OCCURRENCE_CHANGE_UNDETECTED")
    obs.append({"case":"A-property-separation","result":"PASS","scope":"existing source occurrence tuple; not new permanent ID or cross-release proof"})

def verify_b(root,obs):
    b=json.loads(member(root,"B"))
    need(b["schema"]=="tacit-b.composition-receipt.v1" and b["nearest"]["state"]=="REFUSED" and b["nearest"]["selected_id"] is None and b["nearest"]["output"] is None and b["electrical"]["state"]=="REFUSED" and b["electrical"]["geodesic_transfer"] is False,"B_ADMISSION")
    need(b["bond_contract"]=="SYNTHETIC_EXPECTED_RESULT_ONLY_NOT_EXECUTED","B_FIXTURE_LABEL")
    froot=root/"factory"
    sys.path.insert(0,str(froot/"tools"))
    need(blob((froot/"tools/package_factory.py").read_bytes())=="23247de65fde04a400bb30874fc7e81cca4b7ebe","FACTORY_SOURCE")
    import package_factory as factory
    descriptor=json.loads((froot/"packages/factory/admissions/orient.json").read_bytes())
    archive=root/"orient.zip"
    receipt=factory.build(descriptor,root/"inputs",archive)
    need(sha(archive.read_bytes())==ARCHIVE and receipt["descriptor_sha256"]==DESCRIPTOR,"B_ARCHIVE")
    (root/"build.json").write_bytes(factory.canonical(receipt))
    script=root/"b.py"
    need(blob(script.read_bytes())=="8d594beb97fe4712e60655835449883dfafdfe6e","B_RUNNER")
    need(blob((root/"app/tools/tacit5b_activation.py").read_bytes())=="eed42663679b2a09227ff1b389643973adcd4bb6","ACTIVATION_SOURCE")
    need(blob((root/"nearest/packages/nearest-candidate/kuiper_bond.py").read_bytes())=="58bf06469a952b663459e9c2e277d93b51058dca","BOND_SOURCE")
    cmd=[sys.executable,str(script),"--factory",str(froot),"--app",str(root/"app"),"--nearest",str(root/"nearest"),"--activation",str(root/"activation"),"--archive",str(archive),"--receipt",str(root/"build.json")]
    for name in ("replay1.json","replay2.json"):
        subprocess.run(cmd+["--out",str(root/name)],check=True,timeout=45)
    raw=(root/"replay1.json").read_bytes()
    need(raw==(root/"replay2.json").read_bytes(),"B_REPLAY_NONDETERMINISTIC")
    replay=json.loads(raw)
    for field in ("nearest","electrical","bond_contract","negative_checks","fixture_sha256","caller_dataset_sha256"):
        need(replay[field]==b[field],"B_REPLAY_DRIFT:"+field)
    x=replay["orient_fallback"];y=b["orient_fallback"]
    for field in ("semantic_plan","source_records","input_provenance"):
        need(x[field]==y[field],"B_REPLAY_DRIFT:"+field)
    output=x["execution"]["pattern"]["output"]
    need(x["execution"]==y["execution"],"B_EXECUTION_DRIFT")
    sys.path.insert(0,str(root/"oracle"))
    import acceptance as oracle
    expected=oracle.oracle(oracle.pair((0,0),(1,0)))
    oracle.close_result(output,expected)
    obs.append({"case":"B-actual-offline-replay","result":"PASS","actual":output,"expected":expected,"negative_checks":len(replay["negative_checks"]),"repeat_sha256":sha(raw),"original_receipt_sha256":PINS["B"][3],"nearest":replay["nearest"],"electrical":replay["electrical"],"scope":"actual B consumer; independently rebuilt archive; not nearest execution"})
    # Falsify a possible overclaim about the *actual* selected_location adapter:
    # it validates shape and membership, not eligibility or computed distance.
    import importlib.util
    spec=importlib.util.spec_from_file_location("bond",root/"nearest/packages/nearest-candidate/kuiper_bond.py")
    bond=importlib.util.module_from_spec(spec);spec.loader.exec_module(bond)
    fixture=json.loads((root/"nearest/packages/nearest-candidate/consumer-fixture.json").read_bytes())
    request=fixture["input"]
    digest=bond.sha(bond.canonical(request))
    forged={"id":"low","distance_km":0}
    try:
        got=bond.selected_location(request,forged,digest)
    except ValueError as e:
        obs.append({"case":"B-bond-untrusted-result","result":"PASS","observation":"refused "+str(e)})
    else:
        obs.append({"case":"B-bond-untrusted-result","result":"OPEN","observation":"actual adapter accepted in-dataset below-threshold ID and arbitrary nonnegative distance","returned":got,"required":"bind output to exact admitted nearest runtime execution receipt; do not treat typed lookup as eligibility proof"})
    obs.append({"case":"nearest-or-electrical-math","result":"OPEN","reason":"actual B refused both; no runtime admission; do not upgrade a fixture to execution"})

def main():
    root=Path(sys.argv[1]);out=Path(sys.argv[2]);obs=[]
    for fn in (verify_a,verify_b):
        try: fn(root,obs)
        except Exception as e: obs.append({"case":fn.__name__,"result":"FAIL","reason":type(e).__name__+":"+str(e)})
    failed=sum(x["result"]=="FAIL" for x in obs)
    passed=sum(x["result"]=="PASS" for x in obs)
    opened=sum(x["result"]=="OPEN" for x in obs)
    report={"schema":"vedic.independent-observation.v1","principal":"TACIT A and B","measured_twin":"actual pinned A and B artifact receipts and B offline replay","falsifier":"TACIT C with TACIT9 oracle","witness":"GitHub Actions","question":"Do candidate source identity and actual bounded execution match their claims?","apparatus":{"A_head":A_HEAD,"B_head":B_HEAD,"artifact_pins":PINS},"procedure":"independent direct joins, physical source spans, actual B consumer repeat and falsification","observations":obs,"result":"FAIL" if failed else "PASS_WITH_OPEN_OBLIGATIONS","verdict":{"formal_independent_acceptance":"OPEN","rights":"BLOCKED","publication":"NOT_AUTHORISED","permanent_identity":"OPEN","nearest_admission":"OPEN","electrical_admission":"OPEN"},"limitations":["Static A receipt independently examined, A validator not re-executed","No wafer replay, no new identity, no nearest or electrical execution, no browser replay","No formal closure or rights grant","Untrusted bond result must be bound to actual nearest execution before admission"]}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"pass":passed,"fail":failed,"open":opened,"receipt_sha256":sha(out.read_bytes())}))
    for row in obs:
        if row["result"]!="PASS": print(json.dumps(row,sort_keys=True))
    return int(bool(failed))
if __name__=="__main__":
    raise SystemExit(main())
