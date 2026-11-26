"""Seventh-turn append-only CVAA/Quantum Twin candidate witness, not a new ledger."""
import copy,json,sys,subprocess,zipfile
from pathlib import Path
from tacit_c_verify import sha,blob,canonical,need,graph_checks,ARCHIVE,MODULE
A_HEAD="bb637d3a32173de8b3892380af4c6166f969412c"
B_HEAD="827dc15ffebc236954ee4aa40ba0141cd7c23fa4"
ART={
"A-final":("9340883f8719d73ba1da7251ee8e360a5a0436c5b4ed1bdf8c02580a35e0dfe9","capsule.json","ae4ef39ac1886e2b1eadd57ffeebe7d08099efa38d3f6594ed1dcfd4a771bf7d"),
"A-bonds":("649209e8723af1efd4c73f85ebd90b524a2312907d8a5e24759c8bf72ad1f72a","bonds.json","821abf96d3e4c2f42e61d578dcefdfbda366c145b067f9cc9206fdaa91b6cf2d"),
"B-final":("73aa6fd35d71cefb9f60148bc14a5105ab35bbf013c48b6bf555002a0c1d7158","tacit-b-abc-bonds.json","536358fe3271c87fcd13118b9f467415509a6af1b6a998437925846b8a6f7fe1"),
"C-source":("8d48284a1ed870d16d99504707c81e0650a23c24693a1e491a787e809bb08ffa","a-review.json","76080746a09f0c3fa6693211147acfa98716be50caeb766f4ee01a68fc9ac303"),
"C-rank":("c5b746fa68438f43c7b96ac062604db9955152584d904ef1994cd4e92657f7f2","ranking-review.json","f73a064c910e69334a4b1a2c57f1cb86642b51843d6a59ff149c4a9c561b1e90"),
"C-electrical":("22f5266e2fb2d7a014231befa31251c611301e9e6abd463d9aab8b5ee8143cd4","sixth-review.json","20d577d7b4e74cbdc0059dd3ea4950ecc3c0e11ed1c0cafe0b328dfdce5b1e67"),
"C-prior-falsifier":("8469f9457a73e24a484beff998a386b591089dc35147176b39b26f842b69dcf9","b-corrective-review.json","dd95231390005a7e72ae85b03bb203ad5afaa7b29d9492972f4ff6403c30dc74")}
B_MEMBERS={"ranking":("tacit-b-ranking.json","5c71125c76e2495f88d447f60f2f93d13f36198641e8bb4379964c45e7e2be51"),"electrical":("tacit-b-electrical.json","c8598fb9719ca84f8e36fdab24eee4b3c45ffc1e489527a3661b2fbfad307b47"),"reviewed":("tacit-b-reviewed-intake.json","3bbc8f816deb978e338287ae4b33a365d3c1cb0f37a8d073dbd96eacc548fd41"),"unreviewed":("tacit-b-candidate-intake.json","62704c84e7b242312772311f5dae9f8f25107d92c4bd30a6c4dfe101000349f0")}
def member(root,key,name=None,pin=None):
    zpin,default,dpin=ART[key];p=root/(key+".zip")
    need(sha(p.read_bytes())==zpin,"ZIP_PIN:"+key)
    name=name or default;pin=pin or dpin
    with zipfile.ZipFile(p) as z:
        hits=[x for x in z.infolist() if x.filename==name or x.filename.endswith("/"+name)]
        need(len(hits)==1 and hits[0].file_size<=4_000_000,"MEMBER:"+name)
        raw=z.read(hits[0])
    need(sha(raw)==pin,"CONTENT:"+name);return raw
def verdict(root,obs):
    for p,pin in {"ledger.json":"6589d29acd37b812949f0fe07906da59c19b5074","ledger.md":"5e57840cc24f831508047e169d398480cb53edd8","quantum.md":"54294722a577111799e43f1a7bf15b170415de73"}.items():
        need(blob((root/p).read_bytes())==pin,"CONTRACT_PIN:"+p)
    need(blob((root/"laws.md").read_bytes())=="79dae2440dc083b4b34b4fa572bf137e58f5e501","LAW_PIN")
    ledger=json.loads((root/"ledger.json").read_bytes())
    need(ledger["resume_policy"]=="read-only-until-revalidated" and ledger["totals"]=={"whole":6,"resolved":0,"held":6,"outside":0,"open":1,"partial":4,"disputed":1,"settled":0},"PREDECESSOR_LEDGER")
    fail=json.loads((root/"cvaa-job.json").read_bytes())
    need(fail["id"]==139949829074 and fail["run_id"]==45831696890 and fail["conclusion"]=="failure" and ledger["checkpoint_evidence"]["cvaa"]["registry_selfaudit"]=="FAIL","HISTORICAL_FAILURE_ERASED")
    for text,words in [((root/"quantum.md").read_text(),("principal","twin","positron","witnesses")),((root/"laws.md").read_text(),("HONOURED","OVERREACHED","NOT EVALUATED","DISCLOSED"))]:
        need(all(w in text for w in words),"EXISTING_EVIDENCE_VOCABULARY")
    obs.append({"case":"predecessor-ledger-conservation","result":"PASS","historical_totals":ledger["totals"],"cvaa_failure_run":45831696890,"cvaa_job":139949829074,"authority":"read-only; no settlement"})
    graph_checks(root,obs)
    a_raw=member(root,"A-final");a=json.loads(a_raw);b_raw=member(root,"B-final");b=json.loads(b_raw)
    bonds=json.loads(member(root,"A-bonds"));c=json.loads(member(root,"C-source"));cr=json.loads(member(root,"C-rank"));ce=json.loads(member(root,"C-electrical"));old=json.loads(member(root,"C-prior-falsifier"))
    need((root/"a-cold.json").read_bytes()==(root/"a-repeat.json").read_bytes()==a_raw,"A_FINAL_COLD_PARITY")
    need(a["schema"]=="vedic.tacit-a.cold-recovery.v1" and a["typed_bonds"]==bonds["typed_bonds"] and a["properties"]==bonds["properties"] and len(a["source_entries"])==8 and a["live_integration"] is False and a["rights"]=="BLOCKED","A_CAPSULE_SCOPE")
    need(a["spider_channels"]["execution_edges"]==0 and a["spider_channels"]["printer_nodes"]==30 and a["spider_channels"]["printer_edges"]==164 and a["periodic_state"]=="PRODUCER_MODULE_CLASSIFICATION_ONLY","A_CHANNEL_SCOPE")
    obs.append({"case":"actual-A-final-recovery","result":"PASS","receipt_sha256":sha(a_raw),"replays":2,"graph_scope":"historical read-only"})
    pins={"tacit_b_ranking.py":"8a3932e42a426cbae8dcc958e4673644615e2d44","tacit_b_electrical.py":"1d8875227690e5d2c5dc1d78c36e8fc4faf2055e","tacit_b_composition.py":"a97a9c4297e45b6befbff1cc4130c395a831332a","tacit_b_candidate_intake.py":"85503fd264c7160aaa0982f47f6e466c6611896d","tacit_b_bond_intake.py":"d8e5639e00d0bb2dee42075bac23695ca4df3d27","factory/tools/package_factory.py":"23247de65fde04a400bb30874fc7e81cca4b7ebe"}
    for p,pin in pins.items():need(blob((root/p).read_bytes())==pin,"FINAL_B_CODE_PIN:"+p)
    for k,(name,pin) in B_MEMBERS.items():(root/(k+".json")).write_bytes(member(root,"B-final",name,pin))
    ranking=json.loads((root/"ranking.json").read_bytes());elec=json.loads((root/"electrical.json").read_bytes());review=json.loads((root/"reviewed.json").read_bytes())
    cmd=[sys.executable,str(root/"tacit_b_bond_intake.py"),"--factory",str(root/"factory"),"--archive",str(root/"A-bonds.zip"),"--ranking",str(root/"ranking.json"),"--review",str(root/"reviewed.json"),"--electrical",str(root/"electrical.json")]
    for name in ("b-cold.json","b-repeat.json"):
        subprocess.run(cmd+["--out",str(root/name)],check=True,timeout=30)
        need((root/name).read_bytes()==b_raw,"B_FINAL_BOND_REPLAY")
    need(cr["counts"]=={"PASS":33,"FAIL":0,"OPEN":1} and ce["counts"]=={"PASS":28,"FAIL":0,"OPEN":2} and old["counts"]=={"PASS":9,"FAIL":0,"OPEN":1},"C_PREDECESSORS")
    need(any(x["case"]=="farther-eligible-rehashed" and x["result"]=="PASS" for x in cr["observations"]) and any(x["case"]=="eligible-but-not-nearest" and x["result"]=="OPEN" for x in old["observations"]),"FALSIFIER_HISTORY")
    need(cr["B_artifact"][3]==B_MEMBERS["ranking"][1] and ce["artifact_pins"]["B"][2]==B_MEMBERS["electrical"][1] and b["b_ranking_sha256"]==B_MEMBERS["ranking"][1] and b["b_electrical_sha256"]==B_MEMBERS["electrical"][1],"FINAL_B_PREVIOUS_REPLAY_DIGESTS")
    need(b["c_review_sha256"]==ART["C-source"][2] and b["a_manifest_sha256"]==ART["A-bonds"][2] and c["formal_factory_admission"] is False and review["independent_review"]=="BOUNDED_EVIDENCE_HONOURED_FORMAL_AUTHORITY_OPEN","REVIEW_BOUNDARY")
    need(ranking["nearest_archive"] is None and elec["archive"] is None and ranking["factory_admission"]=="FAMILY_NOT_ADMITTED" and elec["admission"]=="SOURCE_RECEIPT_PENDING" and b["admission"]=="UNCHANGED" and b["redistribution"]=="BLOCKED","AUTHORITY_BOUNDARY")
    obs.append({"case":"actual-B-final-bond-replay","result":"PASS","receipt_sha256":sha(b_raw),"replays":2,"runtime_receipt_digests_unchanged":True,"source_code_unchanged":True})
    for x in a["source_entries"]:
        src=x["source"];raw=(root/Path(src["path"]).name).read_bytes();need(blob(raw)==src["blob"],"SOURCE_PIN")
        q=copy.deepcopy(x);q["module_classification"]={"symbol":"presentation mutation"}
        need((q["source"],q["kuiper"])==(x["source"],x["kuiper"]) and blob(raw+b" ")!=src["blob"],"SOURCE_OR_PROPERTY_MUTATION")
    rr=ranking["ranking"];q=copy.deepcopy(rr["request"]);q["records"].reverse()
    need(sha(canonical(q))!=rr["request_sha256"] and sha(canonical(rr["request"]))==rr["request_sha256"],"DATASET_MUTATION")
    obs.append({"case":"source-identity-versus-property-dataset","result":"PASS","addresses":8,"mutations":"classification stable; source byte and ordered dataset invalidated"})
    # Independently inspect B's actual browser receipt, not a claim of independent browser execution.
    raw=(root/"browser.zip").read_bytes();need(sha(raw)=="f57b97ac16afbb29751b26d86fde42559d22ad394e9c12e23f23cc9560bd80d5","BROWSER_ZIP")
    reports=[]
    with zipfile.ZipFile(root/"browser.zip") as z:
        for info in z.infolist():
            if not info.filename.endswith(".json") or info.file_size>4_000_000:continue
            doc=json.loads(z.read(info))
            if isinstance(doc,dict) and "browser_cases" in doc:reports.append(doc)
    need(len(reports)==2,"BROWSER_RECEIPT_CENSUS")
    for r in reports:
        need(r["state"]=="BROWSER_DEVELOPMENT_PASS" and r["independent_acceptance"] is False and r["redistribution"]=="BLOCKED","BROWSER_AUTHORITY")
        cases=r["browser_cases"];need(len(cases)==4 and {(x["browser"],tuple(x["viewport"])) for x in cases}=={(name,vp) for name in ("chromium","webkit") for vp in ((1280,800),(390,844))},"BROWSER_MATRIX")
        for x in cases:
            need(x["state"]=="PASS" and x["electrical_refusal"] and x["import_sha256"]["package/v9-geodesy.mjs"]==MODULE and all(l["document_width"]<=l["viewport_width"] for l in x["layout_checks"]),"BROWSER_REGRESSION")
        if r["package_sha256"]==ARCHIVE:need(all(x["semantic_activation_tested"] for x in cases),"SEMANTIC_BROWSER")
    need({r["package_sha256"] for r in reports}=={ARCHIVE,"ad4d0daa6cef5b30756184f44726b8a750e6a6d0eb31e2fea7fe6886a6b8669c"},"BROWSER_ARCHIVES")
    obs.append({"case":"final-B-browser-artifact-observed","result":"PASS","configurations":8,"independent_replay":False,"physical_handset":False})
    # Historical ledger is untouched. This scorecard has non-fungible obligations for the new principal.
    families={
      "ORIENT":{"source":"PASS","closure":"PASS","archive":"PASS","runtime":"PASS","math":"PASS","independent":"PASS","admission":"EXISTING_INTERNAL_ONLY","rights":"OPEN_BLOCKED"},
      "nearest-to-ORIENT":{"source":"PASS","closure":"PASS_STATIC","archive":"OPEN_NOT_PRODUCED","runtime":"PASS_PRE_ADMISSION","math":"PASS","independent":"PASS_BOUNDED","admission":"OPEN_FAMILY_NOT_ADMITTED","rights":"OPEN_BLOCKED"},
      "electrical":{"source":"PASS","closure":"PASS_STATIC","archive":"OPEN_NOT_PRODUCED","runtime":"PASS_PRE_ADMISSION","math":"PASS_SYNTHETIC","independent":"PASS_BOUNDED","admission":"OPEN_SOURCE_RECEIPT_PENDING","rights":"OPEN_BLOCKED"}}
    obligations=[
      {"obligation_id":"C-5-7-KUIPER","principal":"8 exact source keys, not Stars membership","twin":"fresh producer 8/8 and exact A recovery","positron":"same blob other occurrence or source bytes change","witness":"C","state":"PARTIAL","verdict":"HONOURED","open":"exact Stars 0/8"},
      {"obligation_id":"C-5-7-RANK","principal":"actual pre-admission ranking chain","twin":ART["C-rank"][2],"positron":"farther eligible correctly rehashed rejected","witness":"C","state":"PARTIAL","verdict":"HONOURED","open":"formal admission and rights"},
      {"obligation_id":"C-5-7-ELECTRICAL","principal":"actual synthetic typed electrical chain","twin":ART["C-electrical"][2],"positron":"geodesic route, mean current, incompatible units refused","witness":"C","state":"PARTIAL","verdict":"HONOURED","open":"admitted archive and real engineering inputs"},
      {"obligation_id":"C-5-7-CONTEXT","principal":"read-only recovery and channel evidence","twin":ART["A-final"][2],"positron":"unknown promotion or URL reference as runtime","witness":"C","state":"PARTIAL","verdict":"HONOURED","open":"live CVAA/Spider/Stars consumption and registry failure"},
      {"obligation_id":"C-5-7-BROWSER","principal":"actual B browser regression report observed","twin":"artifact 15139381570","positron":"missing matrix, overflow, unsupported admission","witness":"C receipt check only","state":"PARTIAL","verdict":"HONOURED","open":"independent browser replay and physical handset"},
      {"obligation_id":"C-5-7-AUTHORITY","principal":"formal factory registry and public rights","twin":None,"positron":"valid review digest treated as admission","witness":"C","state":"OPEN","verdict":"NOT EVALUATED","open":"owner-authorized exact registry/handler/admission process and rights clearance"}]
    obs.extend({"case":x["obligation_id"],"result":"OPEN","reason":x["open"]} for x in obligations)
    return families,obligations,ledger["totals"]
def main():
    root,out=Path(sys.argv[1]),Path(sys.argv[2]);obs=[];families={};obligations=[];totals={}
    try:families,obligations,totals=verdict(root,obs)
    except Exception as e:obs.append({"case":"seventh-reconciliation","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"vedic.tacit-c.candidate-quantum-twin-witness.v1","A_head":A_HEAD,"B_head":B_HEAD,"artifact_pins":ART,"observations":obs,"counts":counts,"families":families,"obligations":obligations,"historical_ledger_totals":totals,"ledger_mutated":False,"live_channel_integration":False,"formal_admission_changed":False,"redistribution":"BLOCKED","resume_policy":"read-only-until-revalidated","next":"Owner authorize exact formal admission review/registry handler and resolve rights separately; no new ID allocation without approved producer ingest."}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"families":families,"historical_ledger_totals":totals}))
    for x in obs:
        if x["result"]!="PASS":print(json.dumps(x))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
