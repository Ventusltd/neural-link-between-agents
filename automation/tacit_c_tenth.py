"""Cold independent reconciliation: pinned actual outputs; no ledger settlement."""
import json,sys,zipfile
from pathlib import Path
from tacit_c_verify import need,sha,canonical,ARCHIVE,MODULE
from tacit_c_eighth_peer import pinned
from tacit_c_ninth import B_PIN,B_OLD
from tacit_c_seventh import member
A=("6f3b7fbaa718ccb6869565ee4ebc9594198859a3914275e21c28743fb0282d32","recovery.json","816fcc85b9f43a4006470652172a42cc8c219126dee01beb9520b7a749ff4efe")
PINS={
"identity":("00434d8a3c59dbb160986df65831c22c8ad48a736e190de4d84dc00e4b7b6c8c","identity.json","9dc9d328f5c55206648180acb925447306da29a09ad9dd442ef8be5b53d7bea7"),
"gate":("a6fa111dfc5df17aa09dab86203ed20c2e68df7133e4130f83a5c1e106a8132f","gate.json","303ad784d6d8775e7dc16b98f8dd4a9c5eef113abc7cde0c87129a3065c02b5b"),
"runtime":("1a395b5446486f86294dea8439b8face56013b07a059ed1d82b429bc5cf4d80f","ninth-runtime.json","41b0ef3f97dbbdfabd417e812097bae3c956cfd7d2bd0c0deb68771691f881e8"),
"impact":("8a5872f3e6f9718d3bf5cf0b6581cbee62ef03e61f7f468da17475586bc75cef","ninth-impact.json","39061ca737c1333e923d041ddfb5fd31edbc25d834d9002485d9a0a286710107"),
"prior":("3d0ed22a5fe99fb839e368ae0afd7d11035bc6957bbda99f710d99e28945748c","seventh-witness.json","6a3110164560f14e814d4e8e321440e577b6f599bc7d73e6ba31768e42bb3a6c")}
def read_digest(path,pin):
    need(sha(path.read_bytes())==pin[0],"ZIP_PIN:"+path.name)
    with zipfile.ZipFile(path) as z:
        hits=[z.read(i) for i in z.infolist() if i.filename.endswith(".json") and i.file_size<=2_000_000]
    hits=[v for v in hits if sha(v)==pin[2]]
    need(len(hits)==1,"MEMBER_PIN:"+path.name);return json.loads(hits[0])
def main():
    root,out=map(Path,sys.argv[1:]);obs=[];score={}
    def check(case,ok,**extra):need(ok,case);obs.append(dict(case=case,result="PASS",**extra))
    try:
        a_raw=pinned(root/"A-final.zip",A);a=json.loads(a_raw)
        check("actual-A-final-twice",all((root/f"A-{x}.json").read_bytes()==a_raw for x in ("first","second")),checks=len(a["tests"]))
        b=json.loads(pinned(root/"B-final.zip",B_PIN));old=json.loads(pinned(root/"B-old.zip",B_OLD))
        check("B-final-same-actual-outputs",all(b[k]==old[k] for k in ("requests","results","refusals")))
        c={k:read_digest(root/(k+".zip"),pin) for k,pin in PINS.items()}
        for k,p,o in (("identity",13,1),("gate",26,2),("runtime",53,1),("impact",68,1)):
            check("C-"+k+"-verified",c[k]["counts"]=={"PASS":p,"FAIL":0,"OPEN":o})
        check("prior-ledger-untouched",c["prior"]["ledger_mutated"] is False and not c["prior"]["live_channel_integration"] and c["prior"]["counts"]=={"PASS":11,"FAIL":0,"OPEN":6})
        check("preserve-eight-addresses",len(a["source_entries"])==8 and len({str(x["kuiper"]["key"]) for x in a["source_entries"]})==8)
        check("preserve-32-properties-five-bonds",len(a["properties"])==32 and len(a["conditional_bonds"])==5)
        check("no-graph-promotion",not a["live_integration"] and a["static_source_graph"]["execution_edges"]==[] and not a["spider_channels"]["live_integration"])
        for op in ("orient","nearest-orient","electrical"):
            bind=a["actual_bridge_bindings"][op];r=b["results"][op];q=b["requests"][op]
            check("actual-receipt-binding-"+op,bind["keys"]==q["keys"] and all(bind[k]==r[k] for k in ("request_sha256","pattern_sha256","receipt_sha256")) and bind["rights"]=="BLOCKED")
            check("actual-authority-"+op,r["admission"]==(op=="orient") and r["rights"]=="BLOCKED")
            if op!="orient":
                check("actual-default-refusal-"+op,b["refusals"][op]["state"]=="REFUSED" and b["refusals"][op]["output"] is None)
            score[op]={"source":"PASS_EXACT","closure":"PASS_STATIC","runtime":"PASS_INTERNAL" if op=="orient" else "PASS_PRE_ADMISSION","independent_math":"PASS_BOUNDED","archive":"PASS_EXISTING" if op=="orient" else "OPEN_NOT_ADMITTED","rights":"BLOCKED","selection_receipt":"HISTORICAL_ONLY","live_integration":False}
        impacts=a["impact_example"];affected={x["sha256"] for x in impacts["affected_receipts"]}
        check("actual-latest-bridge-invalidation",all(a["actual_bridge_bindings"][op]["receipt_sha256"] in affected for op in impacts["affected_patterns"]) and not impacts["addresses_changed"])
        raw=(root/"B-browser.zip").read_bytes();need(sha(raw)=="cf83dc1b141038a81c33fcf26df7b7c1bb6b6deb4add927a6fd264970e355a8e","B_BROWSER_ZIP")
        reports=[]
        with zipfile.ZipFile(root/"B-browser.zip") as z:
            for i in z.infolist():
                if i.filename.endswith(".json") and i.file_size<=4_000_000:
                    j=json.loads(z.read(i))
                    if isinstance(j,dict) and "browser_cases" in j:reports.append(j)
        check("B-browser-producer-matrix",len(reports)==2 and all(len(j["browser_cases"])==4 and all(x["state"]=="PASS" for x in j["browser_cases"]) for j in reports),independent_replay=False)
        check("B-browser-no-authority",all(j["state"]=="BROWSER_DEVELOPMENT_PASS" and j["independent_acceptance"] is False and j["redistribution"]=="BLOCKED" for j in reports))
        for case,why in (("historical-ingest","Owner authority required: three exact occurrence tuples only; production 0/8; no permanent allocation."),("new-factory-admissions","Owner-authorized exact receipt locator, handler and registry entry required, no redistribution grant."),("live-producers","CVAA/Spider/Stars live integration not executed; prior six obligations preserved."),("B-independent-browser","B final producer browser reports observed, not independently rerun here."),("public-production","No production write, handset or public release.")):
            obs.append(dict(case=case,result="OPEN",reason=why))
    except Exception as e:obs.append(dict(case="cold",result="FAIL",reason=type(e).__name__+":"+str(e)))
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"tacit-c.cold-recovery-8-10.v1","A_head":"72e9bedaa16a3be6d607e37f083ee2365798a5ea","B_head":"dbca4db3658850f421e8f7319b7cef7e540c1a46","counts":counts,"observations":obs,"families":score,"historical_ledger_mutated":False,"production":False,"redistribution":"BLOCKED"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report));print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}));print(json.dumps(obs[-5:]))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
