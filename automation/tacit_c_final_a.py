"""TACIT C: reason-coded independent review of A final artifact, not admission."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import zipfile
import tacit_c_peer_verify as old
from tacit_c_verify import blob, sha, need, canonical

A_HEAD="5ae1e8d4d0f5d9f852aa589a0894e52f112eed6e"
A_ART="15137841195"
A_ZIP="c1ea563a7be0c1343d547d5678f46b86952a73bc8d5346d330a0faf8e7667772"
A_JSON="5f5cc4c75515ca0059fb67e2f511c4b22d7e048096916cff569ecd630578a831"
old.PINS["A"]=(A_ART,A_ZIP,"candidate.json",A_JSON)
FAMILIES={"orient":{1,5},"nearest":{1,15,16},"electrical":{24,25,26,27}}
PINS={"producer/tools/edition_keys.py":"2a7144e76c3701372266a79c20ba8a5b6c940a1b","producer/cosmos/wafer.tsv":"54dafc60dbd38ce949c683a3ec21697255e58eb1","producer/cosmos/repos.tsv":"c456212d863b85848f5976278db61648b9cf0269","electrical-parse.mjs":"a3f4cb6a46a64e9f63f44860e1a4374496ca3121","seed-parse.mjs":"74f14940b0e6e33825ed38bda1bc6e7e35b24821","spider_evidence.py":"9d46730b7346b6861a99b961b4ac70ef9e02b18b","identity_bridge.py":"f3e6519aab67d2bc9fbc818318abca478ca2ef7e","nearest-spider.json":"08920eb2138e988248cb7703e20671afe3a82971","translation-geodesy.json":"707a182be358db746c4b944ee6bea1c87ceb07d6"}
def get(root,name):
    return json.loads(old.member(root,"A",name))
def normal(data):
    data=copy.deepcopy(data)
    for k in ("seconds","command"): data["summary"].pop(k,None)
    for row in data["bodies"]: row.pop("line_text",None)
    return json.dumps(data,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
def verify_source(root,a,obs):
    old.verify_a(root,obs)
    sys.path.insert(0,str(root))
    from identity_bridge import kuiper_join,request
    dictionary=json.loads((root/"dictionary.json").read_bytes())
    tr={x["id"]:x["source"] for x in json.loads((root/"translation-geodesy.json").read_bytes())["records"]}
    rows=[request(m.get("source") or tr[m["translation_ref"]],m["gg_id"]) for m in dictionary["entries"] if m["number"] in old.EXPECTED]
    (root/"requests.json").write_bytes(canonical(rows))
    subprocess.run([sys.executable,str(root/"producer/tools/edition_keys.py"),"--bodies",str(root/"requests.json"),"--roots",str(root/"roots"),"--out",str(root/"fresh.json")],check=True,timeout=120)
    fresh=json.loads((root/"fresh.json").read_bytes())
    need(fresh["summary"]["verified"]==fresh["summary"]["keyed"]==fresh["summary"]["bodies"]==8,"FRESH_COHORT")
    need(sha(normal(fresh))==a["fresh_producer_normalized_sha256"],"FRESH_NORMALIZED_MISMATCH")
    need(get(root,"replay-audit.json")["normalized_receipt_sha256"]==sha(normal(fresh)),"AUDIT_PIN")
    for r in a["entries"]:
        need(kuiper_join(r["source"],fresh)==r["kuiper"],"HISTORIC_IDENTITY_CONTRACT")
    obs.append({"case":"fresh-independent-kuiper-replay","result":"PASS","verified":8,"normalized_sha256":sha(normal(fresh))})
def verify_closure(root,a,obs):
    # Old formal parsers and historical TACIT13 endpoint contract; source is parsed, never executed.
    def node(script,source,out=None):
        cmd=["node",str(root/script),str(root/source)]
        if out: subprocess.run(cmd+[str(root/out)],check=True,timeout=30);return json.loads((root/out).read_bytes())
        return json.loads(subprocess.check_output(cmd,timeout=30))
    electrical=node("electrical-parse.mjs","voltage-drop.js","electrical-parsed.json")
    geodesy=node("seed-parse.mjs","v9-geodesy.js")
    nearest=node("seed-parse.mjs","v9-nearest-search.js")
    actual=node("independent-nearest.mjs","v9-nearest-search.js")
    need(electrical["imports"]==geodesy["imports"]==[] and nearest["imports"]==["./v9-geodesy.js"],"STATIC_IMPORT_CLOSURE")
    need(actual["static_import"]==a["nearest_closure"]["static_import"] and actual["nearest"]==a["nearest_closure"]["nearest"] and actual["calls"]==a["nearest_closure"]["calls"],"NESTED_STATIC_CLOSURE")
    deps={k:v["module_dependencies"] for k,v in electrical["functions"].items()}
    need(deps==a["electrical_internal_dependencies"],"ELECTRICAL_DEPENDENCIES")
    for r in a["entries"]:
        s=r["source"];name=r["function"]
        parsed=(electrical["functions"][name] if name in electrical["functions"] else actual["nearest"] if name=="nearest" else next(e for e in (nearest if name=="index" else geodesy)["exports"] if e["name"]==name))
        need((parsed["first"],parsed["last"])==(s["first"],s["last"]),"FORMAL_SPAN")
    sys.path.insert(0,str(root))
    from spider_evidence import validate_named
    graph=a["source_dependency_graph"];validate_named(graph["nodes"],graph["edges"])
    need(graph["execution_edges"]==[] and graph["printer_relationship"]=="URL_REFERENCE_ONLY_NOT_EXECUTABLE" and graph["periodic_membership"]=="UNKNOWN","GRAPH_OVERREACH")
    historical=json.loads((root/"nearest-spider.json").read_bytes())
    expected={(e["from"],e["to"],e["type"]) for e in historical["edges"]}
    expected|={("electrical:"+k,"electrical:"+d,"static_module_reference") for k,ds in deps.items() for d in ds}
    expected.add(("module:nearest","module:geodesy","static_import"))
    actual_edges={(e["from"],e["to"],e["type"]) for e in graph["edges"]}
    need(actual_edges==expected and len(actual_edges)==len(graph["edges"]),"GRAPH_EDGE_CENSUS")
    need(all(e["state"]=="STATIC_NOT_RUNTIME_TRACE" and e["source_sha256"]==(electrical["module_sha256"] if e["from"].startswith("electrical:") else nearest["module_sha256"]) for e in graph["edges"]),"GRAPH_EDGE_PROVENANCE")
    for e in historical["edges"]:
        ev=e["evidence"];raw=(root/Path(ev["path"]).name).read_bytes()
        need(blob(raw)==ev["blob"] and ev["contains"] in b"".join(raw.splitlines(keepends=True)[ev["first"]-1:ev["last"]]).decode(),"HISTORICAL_EDGE_SOURCE")
    obs.append({"case":"static-closure-and-graph","result":"PASS","edge_count":len(expected),"scope":"static dependencies, no runtime trace"})
def projections(root,a):
    manifest=get(root,"family-review/manifest.json")
    need(manifest["status"]=="CANDIDATE_ONLY" and manifest["authority"]=="NO_ADMISSION","MANIFEST_AUTHORITY")
    need(set(manifest["files"])=={f+"-"+k+".json" for f in FAMILIES for k in ("source","closure")},"FAMILY_CENSUS")
    reviewed={}
    for family,ids in FAMILIES.items():
        sname=family+"-source.json";cname=family+"-closure.json"
        sr=old.member(root,"A","family-review/"+sname);cr=old.member(root,"A","family-review/"+cname)
        need(sha(sr)==manifest["files"][sname] and sha(cr)==manifest["files"][cname],"FAMILY_DIGEST")
        source=json.loads(sr);closure=json.loads(cr)
        want=[r for r in a["entries"] if int(r["meaning_id"][-6:]) in ids]
        need(source["entries"]==want and len(want)==len(ids),"FAMILY_SOURCE_PROJECTION")
        modules={r["source"]["path"]:{"blob":r["source"]["blob"],"sha256":r["module_sha256"]} for r in want}
        need(source["modules"]==closure["modules"]==modules and source["source_commit"]==closure["source_commit"]==old.SOURCE_COMMIT,"FAMILY_MODULE_PIN")
        need(source["family"]==closure["family"]==family and source["candidate_state"]==closure["candidate_state"]=="REFUSED_REVIEW_PENDING" and source["identity_complete"] is False and source["independent_acceptance"] is False and closure["independent_acceptance"] is False and source["rights"]=="BLOCKED" and closure["execution_edges"]==[] and closure["runtime_verified"] is False,"FAMILY_AUTHORITY")
        if family=="nearest":
            need(closure["static_imports"]==[a["nearest_closure"]["static_import"]] and closure["internal_dependencies"]==a["nearest_closure"]["calls"] and closure["typed_bonds"]==a["nearest_typed_bond"]["edges"],"NEAREST_PROJECTION")
        elif family=="electrical":
            need(closure["static_imports"]==[] and closure["internal_dependencies"]==a["electrical_internal_dependencies"] and len(closure["typed_bonds"])==2,"ELECTRICAL_PROJECTION")
        else:
            need(closure["static_imports"]==[] and closure["typed_bonds"]==[] and closure["internal_dependencies"] is None,"ORIENT_PROJECTION")
        reviewed[family]={"source_candidate_sha256":sha(sr),"closure_candidate_sha256":sha(cr),"source":{"verdict":"HONOURED","reason":"PINNED_OCCURRENCES_FRESH_BOUNDED_KUIPER_REPLAY","formal_acceptance":"OPEN"},"closure":{"verdict":"HONOURED","reason":"STATIC_IMPORT_AND_GRAPH_EVIDENCE_ONLY","formal_acceptance":"OPEN"},"admission":"UNCHANGED_ORIENT_ONLY" if family=="orient" else "BLOCKED","open":["EXACT_STARS_OCCURRENCE","RIGHTS_CLEARANCE","FORMAL_FACTORY_REVIEW_AUTHORITY"]+([] if family=="orient" else ["RUNTIME_ADMISSION"])+(["NEAREST_RESULT_EXECUTION_BINDING"] if family=="nearest" else [])}
    return reviewed
def main():
    root=Path(sys.argv[1]);out=Path(sys.argv[2]);obs=[];reviewed={}
    try:
        for p,pin in PINS.items():need(blob((root/p).read_bytes())==pin,"PIN:"+p)
        a=json.loads(old.member(root,"A"))
        verify_source(root,a,obs)
        verify_closure(root,a,obs)
        reviewed=projections(root,a)
        obs.append({"case":"six-family-projections","result":"PASS"})
    except Exception as e:
        obs.append({"case":"independent-review","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    failed=any(r["result"]=="FAIL" for r in obs)
    report={"schema":"vedic.tacit-c.independent-source-closure-review.v1","candidate_head":A_HEAD,"candidate_artifact":A_ART,"candidate_zip_sha256":A_ZIP,"candidate_sha256":A_JSON,"reviewer":"TACIT C","result":"FAIL" if failed else "BOUNDED_EVIDENCE_HONOURED","source_and_closure":reviewed if not failed else {},"observations":obs,"formal_factory_admission":False,"publication":False,"limitations":["No impersonation of inactive TACIT10/13; formal review authority remains explicit owner blocker.","No whole-estate wafer replay or runtime admission; no rights grant.","Nearest adapter falsification remains open until actual fixed consumer verified."]}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"result":report["result"],"observations":len(obs),"receipt_sha256":sha(out.read_bytes()),"family_reviews":reviewed},sort_keys=True))
    for x in obs:
        if x["result"]=="FAIL":print(json.dumps(x))
    return int(failed)
if __name__=="__main__":raise SystemExit(main())
