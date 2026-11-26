"""C1 independent adversarial review of actual predecessor D browser, loopback only.
Threat model: selected JSON response can be substituted; app code and embedded pins
are intact. Full origin compromise is explicitly outside this guarantee.
No producer edits, no execution/admission claim. Findings are not silently waived.
"""
import copy,json,subprocess,sys,time
from pathlib import Path
from playwright.sync_api import sync_playwright
from tacit_c_browser import D,BASE
from tacit_c_eighth_peer import pinned
from tacit_c_ninth import B_OLD
from tacit_c_seventh import member
from tacit_c_verify import canonical,sha,need

def main():
    root,repo,out=map(Path,sys.argv[1:])
    obs=[];proc=None
    def result(case,ok,**detail):
        obs.append(dict(case=case,result="PASS" if ok else "FAIL",**detail))
    def open_case(case,reason):
        obs.append(dict(case=case,result="OPEN",reason=reason))
    try:
        need(subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()==D,"D_PIN")
        manifest=json.loads(member(root,"A-bonds"))
        original=json.loads(pinned(root/"B-old.zip",B_OLD))
        bykey={str(x["kuiper"]["key"]):x for x in manifest["source_entries"]}
        need(len(bykey)==8,"COHORT")
        import urllib.request
        url=BASE+"/__kuiper/select?mode=machine&family=Vg"
        with (root/"c1-server.log").open("w") as log:
            proc=subprocess.Popen([sys.executable,str(repo/"tools/kuiper_research.py"),str(root/"A-bonds.zip"),"--b-proof",str(root/"B-old.zip"),"--port","8765"],stdout=log,stderr=log)
            for _ in range(80):
                try:
                    with urllib.request.urlopen(url,timeout=2) as f: baseline=json.load(f)
                    break
                except OSError: time.sleep(.25)
            else: raise RuntimeError("SERVER_START")
            expected=sorted((k for k,r in bykey.items() if int(r["meaning_id"][-6:]) in (1,5)),key=int)
            result("independent-exact-occurrence-join", [r["key"] for r in baseline["rows"]]==expected and all(r["source"]==bykey[r["key"]]["source"] and r["meaning"]==bykey[r["key"]]["meaning_id"] and r["module"]==bykey[r["key"]]["module_classification"]["symbol"] for r in baseline["rows"]))
            with sync_playwright() as pw:
                browser=pw.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
                for width,height in ((1280,800),(390,844)):
                    page=browser.new_page(viewport={"width":width,"height":height},has_touch=width<500,is_mobile=width<500)
                    page.route("**/*",lambda route:route.continue_() if route.request.url.startswith(BASE+"/") or route.request.url.startswith("blob:") else route.abort())
                    page.goto(BASE+"/editions/202611021201/",wait_until="domcontentloaded",timeout=60000)
                    page.wait_for_function("window.KY && KY.inspect().done && KY.modules.computation && KY.hooks.SPACE>0",timeout=90000)
                    page.wait_for_function("KY.modules.layers.api.get('computation')?.status === 'OK'",timeout=60000)
                    page.locator('[data-menu="wafer"] button').first.click()
                    panel=page.locator("#ky-computation");panel.wait_for(state="visible")
                    select=panel.get_by_role("button",name="Select",exact=True)
                    stage=panel.get_by_role("button",name="Stage B request")
                    field=panel.locator("textarea").first;preview=panel.locator("textarea[readonly]")
                    inspect=lambda:page.evaluate("KY.modules.computation.api.inspect()")
                    def selected():
                        select.click()
                        page.wait_for_function("!KY.modules.computation.api.inspect().status.startsWith('SELECTING')")
                        return inspect()
                    got=selected()
                    result(f"unmodified-control-{width}",list(map(str,got["keys"]))==expected and not stage.is_disabled())
                    route_pattern="**/__kuiper/select?*"
                    def mutate(case,fn,reseal=False):
                        def handle(route):
                            resp=route.fetch();j=resp.json();fn(j)
                            if reseal:
                                # Producer selection digest is public, not a signature.
                                j["receipt_sha256"]=sha(canonical({k:v for k,v in j.items() if k!="receipt_sha256"}))
                            route.fulfill(response=resp,json=j)
                        page.route(route_pattern,handle)
                        try:
                            state=selected()
                            result(f"{case}-{width}",state["count"]==0 and stage.is_disabled(),observed_count=state["count"],stage_enabled=not stage.is_disabled())
                        finally:page.unroute(route_pattern,handle)
                    mutate("manifest-pin-control",lambda j:j.update(manifest_sha256="0"*64))
                    mutate("authority-control",lambda j:j.update(authority="EXECUTE"))
                    mutate("duplicate-key-control",lambda j:j["rows"].append(copy.deepcopy(j["rows"][0])))
                    mutate("forged-source-path",lambda j:j["rows"][0]["source"].update(path="engine/nonexistent.js"),True)
                    mutate("forged-span",lambda j:j["rows"][0]["source"].update(first=0),True)
                    mutate("forged-blob",lambda j:j["rows"][0]["source"].update(blob="0"*40),True)
                    mutate("forged-meaning",lambda j:j["rows"][0].update(meaning="GG2050-VEDIC-999999"),True)
                    mutate("forged-property-state",lambda j:j["rows"][0].update(evidence="OBSERVED"),True)
                    mutate("forged-bond",lambda j:j["bonds"].append({"from":"forged.out","to":"forged.in","state":"CONDITIONAL","conditions":[]}),True)
                    mutate("forged-selection-digest",lambda j:j.update(receipt_sha256="0"*64))
                    mutate("substituted-stage-operation",lambda j:j.update(stage_operation="electrical"),True)
                    # Change to another real cohort key (not an arbitrary or duplicate key).
                    foreign=next(r for r in manifest["source_entries"] if str(r["kuiper"]["key"]) not in expected)
                    def wrong_key(j):
                        row=j["rows"][0];row.update(key=str(foreign["kuiper"]["key"]),source=foreign["source"],meaning=foreign["meaning_id"],module=foreign["module_classification"]["symbol"])
                    mutate("wrong-exact-cohort-selection",wrong_key,True)
                    # Hold an actual response, then invalidate its generation.
                    held=[]
                    def hold(route):held.append((route,route.fetch()))
                    page.route(route_pattern,hold)
                    select.click()
                    for _ in range(100):
                        if held:break
                        page.wait_for_timeout(50)
                    need(bool(held),"HOLD_SELECTION")
                    panel.get_by_role("button",name="Reset").click()
                    held[0][0].fulfill(response=held[0][1])
                    page.wait_for_timeout(250)
                    result(f"stale-selection-after-reset-{width}",inspect()["count"]==0 and stage.is_disabled())
                    page.unroute(route_pattern,hold)
                    got=selected();need(list(map(str,got["keys"]))==expected,"RESTORE")
                    field.fill(json.dumps(original["requests"]["orient"]["inputs"]))
                    # Substitute only a data response, never executable code.
                    receipt_pattern="**/__kuiper/receipt"
                    def receipt(route):
                        resp=route.fetch();j=resp.json()
                        j.update(scope="HISTORICAL_PINNED_B_EXECUTION_NOT_LIVE",review="INDEPENDENT_PASS",receipt_sha256="0"*64)
                        j["output"]["distance_km"]+=123
                        route.fulfill(response=resp,json=j)
                    page.route(receipt_pattern,receipt)
                    stage.click()
                    page.wait_for_function("document.querySelector('#ky-computation textarea[readonly]').value.length>0 || document.querySelector('#ky-computation').innerText.includes('REFUSED')")
                    result(f"forged-result-and-review-{width}",not preview.input_value())
                    page.unroute(receipt_pattern,receipt)
                    held=[]
                    def hold_receipt(route):held.append((route,route.fetch()))
                    page.route(receipt_pattern,hold_receipt)
                    raw=field.input_value();stage.click()
                    for _ in range(100):
                        if held:break
                        page.wait_for_timeout(50)
                    need(bool(held),"HOLD_RECEIPT")
                    field.fill("{}");field.fill(raw)
                    held[0][0].fulfill(response=held[0][1])
                    page.wait_for_timeout(250)
                    result(f"input-ABA-stale-receipt-{width}",not preview.input_value())
                    page.unroute(receipt_pattern,hold_receipt)
                    page.close()
                browser.close()
        open_case("full-origin-compromise","Client cannot authenticate its own replaced application code or pins.")
        open_case("successor-contracts","A1/B1/D1/E1 exact candidate versions not supplied at test authoring; predecessor only.")
        open_case("physical-handset-production","Headless viewports and loopback only; no public service, physical handset or admission.")
    except Exception as e:obs.append(dict(case="harness",result="FAIL",reason=type(e).__name__+":"+str(e)))
    finally:
        if proc is not None:proc.terminate();proc.wait(timeout=10)
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"tacit-c1.browser-trust-review.v1","D_head":D,"counts":counts,"observations":obs,"threat":"DATA_RESPONSE_SUBSTITUTION_WITH_INTACT_APPLICATION","production":False,"admission_changed":False}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for item in obs:print(json.dumps(item))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
