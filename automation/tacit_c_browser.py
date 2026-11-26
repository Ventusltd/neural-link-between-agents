"""Independent browser and loopback request review of pinned D, no publication."""
import copy,json,math,sys,time,subprocess,urllib.request,urllib.parse,urllib.error
from pathlib import Path
from playwright.sync_api import sync_playwright
from tacit_c_verify import need,sha,canonical
from tacit_c_eighth_peer import pinned
from tacit_c_ninth import B_OLD,B_PIN
from tacit_c_seventh import member
D="e625da97e76a7d3b99361e01767e0fef0984c445"
BASE="http://127.0.0.1:8765"
FAMILIES={"Vg":"orient","Vn+Vg":"nearest-orient","Vd":"electrical"}
def main():
    root,repo,out=map(Path,sys.argv[1:]);obs=[]
    def check(name,ok,**extra):
        need(ok,name);obs.append(dict(case=name,result="PASS",**extra))
    def call(path,body=None,origin=BASE):
        headers={} if body is None else {"Content-Type":"application/json","Origin":origin}
        req=urllib.request.Request(BASE+path,data=None if body is None else json.dumps(body).encode(),headers=headers)
        try:
            with urllib.request.urlopen(req,timeout=8) as f:return f.status,json.loads(f.read())
        except urllib.error.HTTPError as e:return e.code,None
    def select(q):
        code,res=call("/__kuiper/select?"+urllib.parse.urlencode(q));need(code==200,"SELECT_HTTP");return res
    proc=None
    try:
        check("exact-D-checkout",subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()==D)
        old=json.loads(pinned(root/"B-old.zip",B_OLD));final=json.loads(pinned(root/"B-final.zip",B_PIN))
        check("D-pinned-B-results-still-current",all(old[k]==final[k] for k in ("requests","results","refusals")))
        manifest=json.loads(member(root,"A-bonds"))
        check("cohort-8",len(manifest["source_entries"])==8)
        with (root/"server.log").open("w") as log:
            proc=subprocess.Popen([sys.executable,str(repo/"tools/kuiper_research.py"),str(root/"A-bonds.zip"),"--b-proof",str(root/"B-old.zip"),"--port","8765"],stdout=log,stderr=log)
            for i in range(60):
                try:
                    if call("/__kuiper/select?mode=machine&family=Vg")[0]==200:break
                except OSError:time.sleep(.25)
            else:raise RuntimeError("D_SERVER_START")
            for fam,op in FAMILIES.items():
                q={"mode":"machine","family":fam};s=select(q);t=select({**q,"mode":"vedic"})
                expected=old["requests"][op]["keys"]
                check("http-parity-"+op,s["rows"]==t["rows"] and [r["key"] for r in s["rows"]]==expected and s["execution"]=="NOT_EXECUTED")
                req={"request":old["requests"][op],"query":q,"selection_receipt_sha256":s["receipt_sha256"]}
                code,receipt=call("/__kuiper/receipt",req);ref=old["results"][op]
                check("http-exact-historical-"+op,code==200 and receipt["output"]==ref["output"] and receipt["receipt_sha256"]==ref["receipt_sha256"] and receipt["scope"]=="HISTORICAL_PINNED_B_EXECUTION_NOT_LIVE" and receipt["admission"]==ref["admission"] and receipt["rights"]=="BLOCKED")
                changed=copy.deepcopy(req);changed["request"]["inputs"]["C_test_changed"]=True
                c,x=call("/__kuiper/receipt",changed)
                check("http-changed-input-"+op,c==200 and x["state"]=="NOT EXECUTED" and "output" not in x)
                forged=copy.deepcopy(req);forged["request"]["keys"][0]=str(int(forged["request"]["keys"][0])+1)
                check("http-forged-key-"+op,call("/__kuiper/receipt",forged)[0]==400)
                stale=copy.deepcopy(req);stale["selection_receipt_sha256"]="0"*64
                check("http-stale-selection-"+op,call("/__kuiper/receipt",stale)[0]==400)
                check("http-origin-"+op,call("/__kuiper/receipt",req,"http://example.invalid")[0]==403)
            check("http-unknown-not-observed",len(select({"mode":"machine","family":"Vd","property_name":"runtime_effects","state":"UNKNOWN"})["rows"])==4 and not select({"mode":"machine","family":"Vd","property_name":"runtime_effects","state":"OBSERVED"})["rows"])
            check("http-duplicate-query",call("/__kuiper/select?mode=machine&mode=vedic&family=Vg")[0]==400)
            with sync_playwright() as pw:
                b=pw.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
                for width,height in ((1280,800),(390,844)):
                    p=b.new_page(viewport={"width":width,"height":height},has_touch=width<500,is_mobile=width<500)
                    errors=[];p.on("pageerror",lambda e:errors.append(str(e)))
                    p.route("**/*",lambda route:route.continue_() if route.request.url.startswith(BASE+"/") or route.request.url.startswith("blob:") else route.abort())
                    p.goto(BASE+"/editions/202611021201/",wait_until="domcontentloaded",timeout=60000)
                    p.wait_for_function("window.KY && KY.inspect().done && KY.modules.computation && KY.hooks.SPACE>0",timeout=90000)
                    p.wait_for_function("KY.modules.layers.api.get('computation')?.status === 'OK'",timeout=60000)
                    check(f"browser-original-edition-{width}",p.evaluate("KY.inspect().refused.length===0 && !!KY.hooks.cv.getContext('webgl2')"))
                    p.locator('[data-menu="wafer"] button').first.click()
                    panel=p.locator("#ky-computation");panel.wait_for(state="visible")
                    select_btn=panel.get_by_role("button",name="Select",exact=True);stage=panel.get_by_role("button",name="Stage B request")
                    field=panel.locator("textarea").first;preview=panel.locator("textarea[readonly]")
                    for fam,op in FAMILIES.items():
                        panel.locator("select").nth(1).select_option(fam)
                        panel.locator("select").nth(0).select_option("machine")
                        select_btn.click();keys=old["requests"][op]["keys"]
                        p.wait_for_function("n=>KY.modules.computation.api.inspect().count===n",arg=len(keys))
                        actual=p.evaluate("KY.modules.computation.api.inspect()")
                        check(f"browser-machine-{op}-{width}",list(map(str,actual["keys"]))==keys)
                        for key in map(int,keys):
                            xy=p.evaluate("k=>KY.hooks.keyPlace(k)",key);theta=2*math.pi*((key*2654435769)%2**32)/2**32;rr=math.sqrt(key+.5)
                            need(math.hypot(xy[0]-rr*math.cos(theta),xy[1]-rr*math.sin(theta))<1e-6,"PLACEMENT_LAW")
                        check(f"browser-placement-{op}-{width}",True)
                        panel.locator("select").nth(0).select_option("vedic")
                        check(f"browser-mode-invalidates-{op}-{width}",preview.input_value()=="" and stage.is_disabled())
                        select_btn.click();p.wait_for_function("n=>KY.modules.computation.api.inspect().count===n",arg=len(keys))
                        check(f"browser-vedic-{op}-{width}",list(map(str,p.evaluate("KY.modules.computation.api.inspect().keys")))==keys)
                        field.fill(json.dumps(old["requests"][op]["inputs"]));stage.click()
                        p.wait_for_function("document.querySelector('#ky-computation textarea[readonly]').value.includes('tacit-b.kuiper-request.v1')")
                        value=json.loads(preview.input_value());ref=old["results"][op]
                        check(f"browser-pinned-receipt-{op}-{width}",value["observation"]["scope"]=="HISTORICAL_PINNED_B_EXECUTION_NOT_LIVE" and value["observation"]["output"]==ref["output"] and value["observation"]["receipt_sha256"]==ref["receipt_sha256"] and value["observation"]["rights"]=="BLOCKED")
                        altered=copy.deepcopy(old["requests"][op]["inputs"]);altered["C_test_changed"]=True
                        field.fill(json.dumps(altered));check(f"browser-input-invalidates-{op}-{width}",preview.input_value()=="")
                        stage.click();p.wait_for_function("document.querySelector('#ky-computation textarea[readonly]').value.includes('tacit-b.kuiper-request.v1')")
                        value=json.loads(preview.input_value())
                        check(f"browser-staged-not-executed-{op}-{width}",value["execution"]=="NOT EXECUTED" and "output" not in value["observation"])
                    panel.locator("select").nth(2).select_option("runtime_effects");panel.locator("select").nth(3).select_option("OBSERVED")
                    select_btn.click();p.wait_for_function("KY.modules.computation.api.inspect().status.startsWith('SELECTED')")
                    check(f"browser-no-fabricated-observed-{width}",p.evaluate("KY.modules.computation.api.inspect().count===0") and stage.is_disabled())
                    check(f"browser-layout-{width}",p.evaluate("document.documentElement.scrollWidth<=innerWidth && document.getElementById('ky-computation').scrollWidth<=document.getElementById('ky-computation').clientWidth+2"))
                    panel.get_by_role("button",name="Reset").click();check(f"browser-reset-{width}",p.evaluate("KY.modules.computation.api.inspect().count===0") and preview.input_value()=="" and not errors)
                    p.close()
                b.close()
        obs.append({"case":"D-browser-trust-boundary","result":"OPEN","reason":"Local server authenticates exact ZIP and recomputes request, but raw Space and same-origin browser response are trusted internal objects; no independent browser-side exact occurrence authentication or compromised-origin guarantee."})
        obs.append({"case":"physical-handset-and-public-release","result":"OPEN","reason":"Headless Chromium desktop/mobile viewports; local-only research server, no live runtime execution in UI or release."})
    except Exception as e:obs.append({"case":"independent-browser","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    finally:
        if proc is not None:proc.terminate();proc.wait(timeout=10)
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"tacit-c.independent-kuiper-browser.v1","D_head":D,"B_pinned_proof":B_OLD[2],"B_latest_proof":B_PIN[2],"counts":counts,"observations":obs,"redistribution":"BLOCKED","live_execution":False,"physical_handset":False}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report));print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}));print(json.dumps(obs[-3:]))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
