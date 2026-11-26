"""Independent exact signed browser-to-runtime witness, trusted local launcher only.
No production authority; producer code is unmodified; host changes disposable.
"""
import copy,hashlib,json,os,secrets,subprocess,sys,tempfile,time,urllib.request,urllib.error
from pathlib import Path
from playwright.sync_api import sync_playwright
from tacit_c1_combined import canonical,bh,verify,ARCH,PIN,BASE
from tacit_c1_fresh import independent
E="2a58ed137bef42022a5fca8020d320b96fc47fd6"
D="af78cdec7a3adbcf13f742f80d7b654abff0f7ce"
A="46d21c7ef45c1133d1ef24039a79b8dd9978d667"
B="3c921cb913d35ad8bd8a0cf94fe9ede55fa0e529"
def sha(raw):return hashlib.sha256(raw).hexdigest()
def openssl(*args):return subprocess.check_output(["openssl",*args],timeout=10,stderr=subprocess.DEVNULL)
def raw_to_der(raw):
    # Independent P1363-to-ASN.1 encoding for OpenSSL verification.
    if len(raw)!=64:raise ValueError("SIGNATURE_SIZE")
    def integer(v):
        x=v.lstrip(b"\x00") or b"\x00"
        if x[0]&128:x=b"\x00"+x
        return b"\x02"+bytes([len(x)])+x
    body=integer(raw[:32])+integer(raw[32:])
    return b"\x30"+bytes([len(body)])+body
def get(path):return urllib.request.urlopen(BASE+path,timeout=5).read()
def post(path,obj,origin=BASE,raw=None):
    req=urllib.request.Request(BASE+path,data=canonical(obj) if raw is None else raw,headers={"Content-Type":"application/json","Origin":origin})
    try:
        with urllib.request.urlopen(req,timeout=45) as r:return r.status,json.load(r)
    except urllib.error.HTTPError as ex:
        try:return ex.code,json.load(ex)
        except ValueError:return ex.code,{}
def main():
    stage,repo,out=map(lambda x:Path(x).resolve(),sys.argv[1:]);obs=[]
    def check(case,ok,**kw):obs.append(dict(case=case,result="PASS" if ok else "FAIL",**kw))
    def require(case,ok):
        check(case,ok)
        if not ok:raise ValueError(case)
    proc=None
    try:
        for name,path,pin in (("E1",repo,E),("A1",stage/"a1",A),("B1",stage/"b",B)):
            require(name+"-exact",subprocess.check_output(["git","-C",str(path),"rev-parse","HEAD"],text=True).strip()==pin)
        require("D1-exact",subprocess.check_output(["git","hash-object",str(repo/"tools/kuiper-computation/202611261720-computation.js")],text=True).strip()=="e470d8041b9be7760cc525197b4a3c2901592665")
        require("original-archive",sha((stage/"package.zip").read_bytes())==ARCH)
        with tempfile.TemporaryDirectory(prefix="c1-trusted-",dir=stage) as t:
            t=Path(t);key=t/"private.pem";pub=t/"public.der";events=t/"events.json";rows=[]
            openssl("genpkey","-algorithm","EC","-pkeyopt","ec_paramgen_curve:prime256v1","-out",str(key));key.chmod(0o600)
            pub.write_bytes(openssl("pkey","-in",str(key),"-pubout","-outform","DER"))
            trust={"algorithm":"ECDSA-P256-SHA256","spki_hex":pub.read_bytes().hex(),"key_id":sha(pub.read_bytes())}
            def write_events():
                tmp=t/"next";tmp.write_bytes(canonical({"schema":"kuiper.local-source-events.v1","events":rows}));tmp.chmod(0o600);tmp.replace(events)
            write_events()
            proc=subprocess.Popen([sys.executable,"-B",str(repo/"tools/kuiper_research.py"),str(stage/"bonds.zip"),"--runtime-stage",str(stage),"--origin-key",str(key),"--source-events",str(events)],stdout=subprocess.DEVNULL,stderr=None)
            for _ in range(100):
                if proc.poll() is not None:raise RuntimeError("SERVER_EXIT")
                try:raw=get("/__kuiper/manifest");break
                except OSError:time.sleep(.1)
            else:raise RuntimeError("SERVER_START")
            require("manifest",sha(raw)==PIN);m=json.loads(raw)
            sources={str(x["kuiper"]["key"]):x for x in m["source_entries"]}
            def signed(w,q):
                if set(w)!={"payload","signature","key_id"} or w["key_id"]!=trust["key_id"]:raise ValueError("WRAPPER")
                f=t/"message";sig=t/"signature";f.write_bytes(w["payload"].encode("utf-8"));sig.write_bytes(raw_to_der(bytes.fromhex(w["signature"])))
                openssl("dgst","-sha256","-verify",str(pub),"-keyform","DER","-signature",str(sig),str(f))
                r=json.loads(w["payload"])
                if r["challenge"]!=q["challenge"] or r["generation"]!=q["generation"] or r["auth_schema"]!="kuiper.runtime-origin.p256.v1":raise ValueError("CHALLENGE_BINDING")
                return r
            def envelope(family,op,inputs,generation):
                import urllib.parse
                s=json.loads(get("/__kuiper/select?"+urllib.parse.urlencode({"family":family,"mode":"machine"})))
                return {"challenge":secrets.token_hex(32),"generation":generation,"query":s["query"],"selection_receipt_sha256":s["receipt_sha256"],"request":{"schema":"tacit-b.kuiper-request.v1","operation":op,"manifest_sha256":PIN,"keys":[r["key"] for r in s["rows"]],"inputs":inputs}}
            all_receipts=[];all_challenges=set();last_q=None;last_w=None
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
                for width,height in ((1280,800),(390,844)):
                    page=browser.new_page(viewport={"width":width,"height":height},has_touch=width<500,is_mobile=width<500)
                    page.add_init_script("window.__KUIPER_RUNTIME_TRUST__="+json.dumps(trust))
                    page.route("**/*",lambda r:r.continue_() if r.request.url.startswith(BASE+"/") or r.request.url.startswith("blob:") else r.abort())
                    errors=[];page.on("pageerror",lambda err:errors.append(str(err)))
                    page.goto(BASE+"/editions/202611021201/",wait_until="domcontentloaded",timeout=60000)
                    page.wait_for_function("window.KY && KY.inspect().done && KY.modules.computation && KY.hooks.SPACE>0",timeout=90000)
                    page.wait_for_function("KY.modules.layers.api.get('computation')?.status === 'OK'",timeout=60000)
                    page.locator('[data-menu="wafer"] button').first.click()
                    panel=page.locator("#ky-computation");panel.wait_for(state="visible")
                    state=lambda:page.evaluate("KY.modules.computation.api.inspect()")
                    select=panel.get_by_role("button",name="Select",exact=True);execute=panel.get_by_role("button",name="Execute ORIENT");preview=panel.locator("textarea[readonly]")
                    for label in ("Instrument","Family / operation","A longitude","A latitude","B longitude","B latitude"):
                        require(f"exact-label-{width}-{label}",panel.get_by_label(label,exact=True).count()==1)
                    select.click();page.wait_for_function("!KY.modules.computation.api.inspect().status.startsWith('SELECTING')")
                    require(f"ready-{width}",execute.is_enabled())
                    receipts=[]
                    for i,coords in enumerate(((10,20,13,22),(179,12,-179,13),(10,20,13,22))):
                        for label,val in zip(("A longitude","A latitude","B longitude","B latitude"),coords):panel.get_by_label(label,exact=True).fill(str(val))
                        with page.expect_response(lambda r:r.url==BASE+"/__kuiper/execute-auth",timeout=45000) as ev:execute.click()
                        resp=ev.value;require(f"signed-http-{width}-{i}",resp.status==200)
                        q=resp.request.post_data_json;w=resp.json();r=signed(w,q);v=r["pattern_receipt"];legacy=r["receipt"];inputs=q["request"]["inputs"]
                        require(f"challenge-unique-{width}-{i}",q["challenge"] not in all_challenges);all_challenges.add(q["challenge"])
                        oracle=independent(inputs["point_a"],inputs["point_b"]);actual=r["output"]
                        check(f"oracle-{width}-{i}",abs(actual["distance_km"]-oracle["distance_km"])<1e-6 and abs((actual["initial_bearing_deg"]-oracle["initial_bearing_deg"]+180)%360-180)<1e-7,actual=actual)
                        check(f"binding-{width}-{i}",r["request_sha256"]==bh(q["request"]) and v["request_sha256"]==bh(r["pattern_request"]) and v["pattern_sha256"]==bh(v["pattern"]) and v["result_sha256"]==bh(v["result"]) and verify(v) and verify(legacy) and v["legacy_receipt"]==legacy and v["result"]["output"]==actual and r["archive_sha256"]==ARCH and r["rights"]=="BLOCKED" and r["selection_receipt_sha256"]==q["selection_receipt_sha256"] and r["dependency_epoch"]==0)
                        bound=r["bound_receipt"];prov=bound["provenance"]
                        check(f"bound-context-{width}-{i}",verify(bound) and bound["schema"]=="tacit-b.execution-context.v1" and bound["context"]=={k:q[k] for k in ("challenge","generation","selection_receipt_sha256")} and bound["request"]==r["pattern_request"] and bound["pattern_receipt"]==v and bound["rights"]=="BLOCKED" and bound["origin_authentication"]=="HOST_REQUIRED" and prov["orient_archive_sha256"]==ARCH and prov["descriptor_sha256"]==v["pattern"]["descriptor_sha256"] and prov["closure_sha256"]==v["pattern"]["closure_sha256"] and prov["sources"]==v["pattern"]["sources"] and prov["manifest_sha256"]==PIN and prov["earth_model"]["model"]=="sphere" and prov["earth_model"]["radius_km"]==6378.137)
                        page.wait_for_function("KY.modules.computation.api.inspect().execution !== 'EXECUTING'",timeout=10000)
                        pv=json.loads(preview.input_value()) if preview.input_value() else {}
                        check(f"UI-auth-{width}-{i}",state()["execution"]=="REPORTED EXECUTED" and state()["originState"]=="SIGNATURE VERIFIED" and pv.get("runtime_origin",{}).get("payload")==w["payload"] and pv.get("review")=="PENDING_EXACT_REQUEST_REVIEW")
                        receipts.append(v);last_q=q;last_w=w;all_receipts.append(v)
                    check(f"repeat-semantic-{width}",receipts[0]==receipts[2] and receipts[0]["pattern_sha256"]==receipts[1]["pattern_sha256"] and receipts[0]["result_sha256"]!=receipts[1]["result_sha256"])
                    status_button=panel.get_by_role("button",name="Check receipt status")
                    with page.expect_response(lambda r:r.url==BASE+"/__kuiper/status-auth",timeout=45000) as ev:status_button.click()
                    sr=ev.value;require(f"signed-status-{width}",sr.status==200 and signed(sr.json(),sr.request.post_data_json)["state"]=="CURRENT_FOR_PINNED_INPUT")
                    page.wait_for_function("KY.modules.computation.api.inspect().originState === 'CURRENT_FOR_PINNED_INPUT'")
                    check(f"UI-current-{width}",json.loads(preview.input_value())["latest_status"]["state"]=="CURRENT_FOR_PINNED_INPUT")
                    path="**/__kuiper/execute-auth"
                    def attack(kind):
                        def tamper(route):
                            resp=route.fetch(timeout=45000);w=resp.json()
                            if kind=="signature":w["signature"]="0"*128
                            elif kind=="key":w["key_id"]="0"*64
                            elif kind=="signed-replay":w=last_w
                            elif kind=="unsigned":w=json.loads(w["payload"])
                            elif kind=="rehash":
                                r=json.loads(w["payload"]);r["output"]["distance_km"]+=10
                                old=r["receipt"];old["output"]=r["output"];old["receipt_sha256"]=bh({k:v for k,v in old.items() if k!="receipt_sha256"})
                                v=r["pattern_receipt"];v["legacy_receipt"]=old;v["result"]["output"]=r["output"];v["result_sha256"]=bh(v["result"]);v["receipt_sha256"]=bh({k:x for k,x in v.items() if k!="receipt_sha256"})
                                bound=r["bound_receipt"];bound["pattern_receipt"]=v;bound["receipt_sha256"]=bh({k:x for k,x in bound.items() if k!="receipt_sha256"})
                                w["payload"]=(canonical(r)+b"\n").decode("ascii")
                            route.fulfill(response=resp,json=w)
                        page.route(path,tamper)
                        try:
                            execute.click();page.wait_for_function("KY.modules.computation.api.inspect().execution !== 'EXECUTING'",timeout=45000)
                            check(f"refused-{width}-{kind}",state()["execution"]=="REFUSED" and not preview.input_value())
                        finally:page.unroute(path,tamper)
                    for kind in ("signature","key","signed-replay","unsigned","rehash"):attack(kind)
                    held=[]
                    def hold(route):held.append((route,route.fetch(timeout=45000)))
                    page.route(path,hold);coord=panel.get_by_label("B longitude",exact=True);coord.fill("4");execute.click()
                    for _ in range(100):
                        if held:break
                        page.wait_for_timeout(50)
                    require(f"held-{width}",len(held)==1 and held[0][1].status==200)
                    coord.fill("5");coord.fill("4")
                    held[0][0].fulfill(response=held[0][1]);page.wait_for_timeout(300)
                    check(f"ABA-{width}",state()["execution"]=="NOT EXECUTED" and not preview.input_value())
                    page.unroute(path,hold);check(f"page-errors-{width}",not errors)
                    if width==390:
                        coord.fill("13")
                        with page.expect_response(lambda r:r.url==BASE+"/__kuiper/execute-auth",timeout=45000) as ev:execute.click()
                        rr=ev.value;require("status-rehearsal-real-execution",rr.status==200 and signed(rr.json(),rr.request.post_data_json)["pattern_receipt"]==all_receipts[0])
                        page.wait_for_function("KY.modules.computation.api.inspect().originState === 'SIGNATURE VERIFIED'")
                        saved=json.loads(preview.input_value())["runtime_origin"]["payload"]
                    else:page.close()
                check("same-semantics-cross-viewport",all_receipts[:3]==all_receipts[3:])
                check("challenge-replay-server",post("/__kuiper/execute-auth",last_q)[0]==400)
                check("unsigned-downgrade-server",post("/__kuiper/execute",{k:v for k,v in last_q.items() if k!="challenge"})[0]==403)
                check("cross-origin-server",post("/__kuiper/execute-auth",last_q,"https://invalid.example")[0]==403)
                check("duplicate-json-server",post("/__kuiper/execute-auth",{},raw=b'{"challenge":"a","challenge":"b"}')[0]==400)
                bsrc=all_receipts[0]["pattern"]["sources"][0]["source"]
                esrc=next(v["source"] for v in sources.values() if v["module_classification"]["symbol"]=="Vd")
                rid=all_receipts[0]["receipt_sha256"]
                def status(n):
                    q={"challenge":secrets.token_hex(32),"generation":n,"operation":"orient","receipt_sha256":rid};c,w=post("/__kuiper/status-auth",q);require("status-http-"+str(n),c==200);return signed(w,q)
                rows.append({"kind":"presentation","source":bsrc,"field":"display_colour"});write_events()
                r=status(101);check("presentation-stable",r["state"]=="CURRENT_FOR_PINNED_INPUT" and not r["stale_operations"])
                rows.append({"kind":"source","source":esrc,"new_blob":"0"*40});write_events()
                r=status(102);check("electrical-only",r["state"]=="CURRENT_FOR_PINNED_INPUT" and r["stale_operations"]==["electrical"])
                q=envelope("Vg","orient",last_q["request"]["inputs"],103);c,w=post("/__kuiper/execute-auth",q)
                require("unaffected-HTTP",c==200);r=signed(w,q);check("unaffected-real-receipt",r["pattern_receipt"]==all_receipts[0])
                q=envelope("Vd","electrical",{},104);c,w=post("/__kuiper/execute-auth",q);check("affected-electrical-refused",c==409 and signed(w,q)["receipt"] is None)
                rows.append({"kind":"source","source":bsrc,"new_blob":"0"*40});write_events()
                r=status(105);check("geodesy-stale-historical",r["state"]=="STALE_HISTORICAL_PRESERVED" and r["stale_operations"]==["electrical","nearest-orient","orient"])
                with page.expect_response(lambda r:r.url==BASE+"/__kuiper/status-auth",timeout=45000) as ev:status_button.click()
                sr=ev.value;require("UI-stale-signed-HTTP",sr.status==200 and signed(sr.json(),sr.request.post_data_json)["state"]=="STALE_HISTORICAL_PRESERVED")
                page.wait_for_function("KY.modules.computation.api.inspect().execution === 'STALE HISTORICAL'")
                historic=json.loads(preview.input_value());check("UI-historical-preserved",historic["runtime_origin"]["payload"]==saved and historic["latest_status"]["state"]=="STALE_HISTORICAL_PRESERVED")
                q=envelope("Vg","orient",last_q["request"]["inputs"],106);c,w=post("/__kuiper/execute-auth",q);check("affected-orient-refused",c==409 and signed(w,q)["receipt"] is None and not any(k in signed(w,q) for k in ("bound_receipt","pattern_receipt","output")))
                rows.pop();write_events();q=envelope("Vg","orient",last_q["request"]["inputs"],107);check("event-rollback-refused",post("/__kuiper/execute-auth",q)[0]==400)
                browser.close()
            proc.terminate();proc.wait(timeout=5);proc=None
        obs.extend([dict(case="full-origin-replacement",result="OPEN",reason="Trusted launcher and client intact; no protection if they are replaced."),dict(case="continuous-browser-invalidation",result="OPEN",reason="Explicit live authenticated browser status and host event rehearsal, not continuous polling or real source observation."),dict(case="production-and-handset",result="OPEN",reason="Isolated hosted Chromium only; no release or permanent writes.")])
    except Exception as exc:obs.append(dict(case="harness",result="FAIL",reason=type(exc).__name__+":"+str(exc)))
    finally:
        if proc is not None:proc.terminate();proc.wait(timeout=5)
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(dict(schema="tacit-c1.authenticated-independent.v1",E1=E,D1=D,A1=A,B1=B,counts=counts,observations=obs,production=False))+b"\n")
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes()),"observations":obs}));return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
