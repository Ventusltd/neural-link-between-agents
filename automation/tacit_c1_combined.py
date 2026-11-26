"""Independent C1 witness: real browser, E1 loopback transport, B1 admitted archive.
A1 evidence only, no simulated execution. Response tampering confined to local test.
"""
import copy,hashlib,json,subprocess,sys,time,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
from tacit_c1_fresh import independent

E="2211b68b9966b5e22abf80a33e41f8c29f3076ac"
D="dd55e05e789f2fdc4163f9a84046a8f71c8f309e"
B="988e2293fd740ca434a9cf087fa873f841b7dc6f"
A="7391b50343b7d7beecb8a32ccd748bfc00c2190b"
PIN="821abf96d3e4c2f42e61d578dcefdfbda366c145b067f9cc9206fdaa91b6cf2d"
ARCH="e83937c040499a7060b03ca2c4969e4414cdca48cb7f28a3ef9039f002486787"
BASE="http://127.0.0.1:8765"
def canonical(x):return json.dumps(x,sort_keys=True,ensure_ascii=True,allow_nan=False,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def bh(x):return sha(canonical(x)+b"\n")
def verify(r):return r["receipt_sha256"]==bh({k:v for k,v in r.items() if k!="receipt_sha256"})
def get(path):return urllib.request.urlopen(BASE+path,timeout=5).read()
def main():
    stage,repo,out=map(Path,sys.argv[1:]);repo=repo.resolve();obs=[]
    def check(case,ok,**kw):obs.append(dict(case=case,result="PASS" if ok else "FAIL",**kw))
    def require(case,ok):
        check(case,ok)
        if not ok:raise ValueError(case)
    proc=None
    try:
        require("E1-exact",subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()==E)
        require("B1-exact",subprocess.check_output(["git","-C",str(stage/"b"),"rev-parse","HEAD"],text=True).strip()==B)
        require("D1-exact-cartridge",subprocess.check_output(["git","hash-object",str(repo/"tools/kuiper-computation/202611261720-computation.js")],text=True).strip()=="26485d0689c6aeccad1c1401243093d9ec47d3a3")
        require("original-archive",sha((stage/"package.zip").read_bytes())==ARCH)
        proc=subprocess.Popen([sys.executable,"-B",str(repo/"tools/kuiper_research.py"),str(stage/"bonds.zip"),"--port","8765","--runtime-stage",str(stage)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        for _ in range(100):
            if proc.poll() is not None:raise RuntimeError("SERVER_EXIT")
            try:raw=get("/__kuiper/manifest");break
            except OSError:time.sleep(.1)
        else:raise RuntimeError("SERVER_START")
        require("manifest-authentication",sha(raw)==PIN)
        m=json.loads(raw);a_raw=(stage/"a1-property-impact.json").read_bytes();a=json.loads(a_raw)
        require("A1-exact-evidence",sha(a_raw)=="1233591210b19b006bb5970ecc85bdf0e5951cc3bef92e5e670871a4da0ca9e3" and a["base_manifest_sha256"]==PIN)
        sources={str(r["kuiper"]["key"]):r for r in m["source_entries"]}
        groups={"Vg":{1,5},"Vn":{15,16},"Vn+Vg":{1,5,15,16},"Vd":{24,25,26,27}}
        expected={fam:sorted((k for k,r in sources.items() if int(r["meaning_id"][-6:]) in ids),key=int) for fam,ids in groups.items()}
        for fam,keys in expected.items():
            for mode in ("machine","vedic"):
                import urllib.parse
                sel=json.loads(get("/__kuiper/select?"+urllib.parse.urlencode(dict(mode=mode,family=fam))))
                check("transport-"+fam+"-"+mode,[r["key"] for r in sel["rows"]]==keys and all(r["source"]==sources[r["key"]]["source"] for r in sel["rows"]) and sel["receipt_sha256"]==sha(canonical({k:v for k,v in sel.items() if k!="receipt_sha256"})))
        require("A1-ORIENT-parity",a["selection_examples"][0]["keys"]==expected["Vg"])
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
            for width,height in ((1280,800),(390,844)):
                suffix=str(width)
                page=browser.new_page(viewport={"width":width,"height":height},is_mobile=width<500,has_touch=width<500)
                page.route("**/*",lambda r:r.continue_() if r.request.url.startswith(BASE+"/") or r.request.url.startswith("blob:") else r.abort())
                errors=[];page.on("pageerror",lambda e:errors.append(str(e)))
                page.goto(BASE+"/editions/202611021201/",wait_until="domcontentloaded",timeout=60000)
                page.wait_for_function("window.KY && KY.inspect().done && KY.modules.computation && KY.hooks.SPACE>0",timeout=90000)
                page.wait_for_function("KY.modules.layers.api.get('computation')?.status === 'OK'",timeout=60000)
                page.locator('[data-menu="wafer"] button').first.click()
                panel=page.locator("#ky-computation");panel.wait_for(state="visible")
                select=panel.get_by_role("button",name="Select",exact=True)
                execute=panel.get_by_role("button",name="Execute ORIENT")
                def inspect():return page.evaluate("KY.modules.computation.api.inspect()")
                def settled():page.wait_for_function("!KY.modules.computation.api.inspect().status.startsWith('SELECTING')",timeout=30000)
                for fam,keys in expected.items():
                    for mode in ("machine","vedic"):
                        panel.get_by_label("Instrument",exact=True).select_option(mode)
                        panel.get_by_label("Family / operation",exact=True).select_option(fam)
                        select.click();settled()
                        state=inspect();check("browser-"+suffix+"-"+fam+"-"+mode,[str(k) for k in state["keys"]]==keys and execute.is_enabled()==(fam=="Vg"))
                panel.get_by_label("Family / operation",exact=True).select_option("Vg")
                panel.get_by_label("Instrument",exact=True).select_option("machine")
                select.click();settled()
                require("ready-"+suffix,execute.is_enabled())
                results=[]
                for i,coords in enumerate(((10,20,13,22),(179,12,-179,13))):
                    for name,value in zip(("A longitude","A latitude","B longitude","B latitude"),coords):
                        panel.get_by_label(name,exact=True).fill(str(value))
                    with page.expect_response(lambda r:r.url==BASE+"/__kuiper/execute",timeout=45000) as event:execute.click()
                    response=event.value;require("actual-http-"+suffix+"-"+str(i),response.status==200)
                    request=response.request.post_data_json;r=response.json();v=r["pattern_receipt"];q=r["pattern_request"];legacy=r["receipt"]
                    inputs=request["request"]["inputs"];actual=r["output"];oracle=independent(inputs["point_a"],inputs["point_b"])
                    check("oracle-"+suffix+"-"+str(i),abs(actual["distance_km"]-oracle["distance_km"])<1e-6 and abs((actual["initial_bearing_deg"]-oracle["initial_bearing_deg"]+180)%360-180)<1e-7,actual=actual,expected=oracle)
                    check("binding-"+suffix+"-"+str(i),request["request"]["keys"]==expected["Vg"] and r["generation"]==request["generation"] and r["selection_receipt_sha256"]==request["selection_receipt_sha256"] and r["request_sha256"]==bh(request["request"]) and v["request_sha256"]==bh(q) and v["pattern_sha256"]==bh(v["pattern"])==q["pattern_sha256"] and v["result_sha256"]==bh(v["result"]) and verify(v) and verify(legacy) and v["legacy_receipt"]==legacy and v["result"]["output"]==actual and r["archive_sha256"]==ARCH)
                    check("authority-"+suffix+"-"+str(i),r["state"]=="EXECUTED_INTERNAL" and r["review"]=="PENDING_EXACT_REQUEST_REVIEW" and r["rights"]=="BLOCKED" and legacy["admission"] is True)
                    page.wait_for_function("KY.modules.computation.api.inspect().execution !== 'EXECUTING'",timeout=10000)
                    preview=panel.locator("textarea[readonly]").input_value()
                    check("UI-"+suffix+"-"+str(i),inspect()["execution"]=="REPORTED EXECUTED" and bool(preview) and json.loads(preview)["receipt"]==legacy and json.loads(preview)["review"]=="PENDING_EXACT_REQUEST_REVIEW")
                    results.append(v)
                check("distinct-request-same-pattern-"+suffix,results[0]["pattern_sha256"]==results[1]["pattern_sha256"] and results[0]["request_sha256"]!=results[1]["request_sha256"] and results[0]["result_sha256"]!=results[1]["result_sha256"])
                # Real delayed response, input A -> B -> A: epoch, not merely value comparison.
                held=[]
                def hold(route):held.append((route,route.fetch(timeout=45000)))
                page.route("**/__kuiper/execute",hold)
                coord=panel.get_by_label("B longitude",exact=True);coord.fill("4");execute.click()
                for _ in range(100):
                    if held:break
                    page.wait_for_timeout(50)
                require("held-real-response-"+suffix,len(held)==1 and held[0][1].status==200)
                coord.fill("5");coord.fill("4")
                with page.expect_response(lambda r:r.url==BASE+"/__kuiper/execute"):held[0][0].fulfill(response=held[0][1])
                page.wait_for_timeout(250)
                check("stale-ABA-"+suffix,inspect()["execution"]=="NOT EXECUTED" and panel.locator("textarea[readonly]").input_value()=="")
                page.unroute("**/__kuiper/execute",hold)
                # Fully rehashed selection cannot supersede independently pinned source facts.
                def corrupt(route):
                    response=route.fetch();body=response.json()
                    body["rows"][0]["source"]["path"]="forged/path.js"
                    body["receipt_sha256"]=sha(canonical({k:v for k,v in body.items() if k!="receipt_sha256"}))
                    route.fulfill(response=response,json=body)
                page.route("**/__kuiper/select?*",corrupt);select.click();settled()
                check("rehashed-source-refused-"+suffix,inspect()["status"].startswith("REFUSED") and inspect()["count"]==0 and not execute.is_enabled())
                page.unroute("**/__kuiper/select?*",corrupt)
                select.click();settled()
                def forged_result(route):
                    response=route.fetch();body=response.json();body["output"]["distance_km"]+=1
                    route.fulfill(response=response,body=canonical(body))
                page.route("**/__kuiper/execute",forged_result)
                execute.click();page.wait_for_function("KY.modules.computation.api.inspect().execution !== 'EXECUTING'",timeout=45000)
                check("unbound-result-refused-"+suffix,inspect()["execution"]=="REFUSED" and not panel.locator("textarea[readonly]").input_value())
                page.unroute("**/__kuiper/execute",forged_result)
                check("no-page-errors-"+suffix,not errors,errors=errors)
                check("no-overflow-"+suffix,page.evaluate("document.documentElement.scrollWidth<=innerWidth"))
                panel.get_by_role("button",name="Reset").click();check("reset-"+suffix,inspect()["count"]==0 and inspect()["execution"]=="NOT EXECUTED")
                page.close()
            browser.close()
        obs.append(dict(case="production-authority-and-distribution",result="OPEN",reason="No publication, ledger or admission change authorised."))
        obs.append(dict(case="runtime-origin-authentication",result="OPEN",reason="Browser reports correlated result pending independent review; hash alone is not a signature or fully compromised-origin guarantee."))
    except Exception as exc:obs.append(dict(case="harness",result="FAIL",reason=type(exc).__name__+":"+str(exc)))
    finally:
        if proc is not None:proc.terminate();proc.wait(timeout=5)
    counts={k:sum(o["result"]==k for o in obs) for k in ("PASS","FAIL","OPEN")}
    report=dict(schema="tacit-c1.combined-independent.v1",A1=A,B1=B,D1=D,E1=E,counts=counts,observations=obs,production=False,admission_changed=False)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report)+b"\n")
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"observations":obs}))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
