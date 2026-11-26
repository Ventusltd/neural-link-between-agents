"""F1 performance only: exact producer browser path and read-only graph evidence."""
import json, os, sys, time, statistics, subprocess, resource, platform, urllib.request
from pathlib import Path
from collections import Counter
from tacit_f1_performance import measure, csr, reverse, check, digest
from tacit_c_verify import sha, blob, canonical, ARCHIVE
from tacit_c_eighth_peer import pinned

def now(): return time.perf_counter_ns()
def ms(start): return (now()-start)/1e6
def samples(vals):return {"samples_ms":vals,"median_ms":statistics.median(vals),"range_ms":[min(vals),max(vals)],"first_ms":vals[0]}

def browser(stage,r):
    from playwright.sync_api import sync_playwright
    root=Path.cwd()
    base="http://127.0.0.1:8765"
    check(blob((root/"tools/kuiper_research.py").read_bytes())=="ca74fa6e3a87c6395ebfd32a2d102a4d224ada49","SERVER_PIN")
    check(blob((root/"tools/kuiper_runtime.py").read_bytes())=="ddf7198a12526fa3aaa136737a1367d4f4ecd8a4","RUNTIME_PIN")
    check(blob((root/"tools/kuiper-computation/202611261720-computation.js").read_bytes())=="26485d0689c6aeccad1c1401243093d9ec47d3a3","UI_PIN")
    check(sha((stage/"package.zip").read_bytes())==ARCHIVE,"ARCHIVE")
    raw=(stage/"b1-patterns.json").read_bytes()
    check(sha(raw)=="a5540a0978117750fd54739e423dbd4e7c0150ce1eba81d5139609ed2db7ee97","B1_MEMBER")
    expected=json.loads(raw)["results"]
    r["startup"]=[]
    r["viewports"]=[]
    r["archive_sha256"]=ARCHIVE
    r["build_and_http_suite_ms"]=int((stage/"build-and-http-ns.txt").read_text())/1e6
    for trial in range(3):
        t=now()
        proc=subprocess.Popen([sys.executable,"-B","tools/kuiper_research.py",str(stage/"bonds.zip"),"--port","8765","--runtime-stage",str(stage)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        try:
            for _ in range(200):
                check(proc.poll() is None,"SERVER_EXIT")
                try:
                    with urllib.request.urlopen(base+"/__kuiper/select?mode=machine&family=Vg",timeout=2) as resp:
                        check(resp.status==200,"SERVER_READY");break
                except OSError:time.sleep(.025)
            else:raise ValueError("SERVER_START")
            startup=ms(t)
            with sync_playwright() as p:
                t=now();b=p.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
                r["startup"].append({"server_ready_ms":startup,"browser_launch_ms":ms(t)})
                for width,height in [(1280,800),(390,844)]:
                    page=b.new_page(viewport={"width":width,"height":height},is_mobile=width<500,has_touch=width<500)
                    errors=[];page.on("pageerror",lambda e:errors.append(str(e)))
                    page.route("**/*",lambda route:route.continue_() if route.request.url.startswith(base+"/") or route.request.url.startswith("blob:") else route.abort())
                    t=now();page.goto(base+"/editions/202611021201/",wait_until="domcontentloaded",timeout=60000)
                    page.wait_for_function("window.KY && KY.inspect().done && KY.modules.computation && KY.hooks.SPACE>0",timeout=90000)
                    page.wait_for_function("KY.modules.layers.api.get('computation')?.status === 'OK'",timeout=60000)
                    ready=ms(t)
                    page.locator('[data-menu="wafer"] button').first.click()
                    panel=page.locator("#ky-computation");panel.wait_for(state="visible")
                    t=now();panel.get_by_role("button",name="Select",exact=True).click()
                    page.wait_for_function("KY.modules.computation.api.inspect().count===2",timeout=30000)
                    selection=ms(t);rows=[]
                    for i,(lon,lat) in enumerate(((0,2),(-3,0))):
                        for name,value in zip(("A longitude","A latitude","B longitude","B latitude"),(0,0,lon,lat)):
                            panel.get_by_label(name,exact=True).fill(str(value))
                        t=now()
                        with page.expect_response(lambda v:v.url==base+"/__kuiper/execute",timeout=45000) as event:
                            panel.get_by_role("button",name="Execute ORIENT").click()
                        resp=event.value;check(resp.status==200,"HTTP_EXECUTE")
                        body=resp.json();http=ms(t)
                        check(body["pattern_receipt"]==expected[i],"B1_EXACT_RESULT")
                        page.wait_for_function("KY.modules.computation.api.inspect().execution==='REPORTED EXECUTED'",timeout=10000)
                        total=ms(t)
                        shown=json.loads(panel.locator("textarea[readonly]").input_value())
                        check(shown["receipt"]==body["receipt"],"DISPLAY_RECEIPT")
                        rows.append({"http_body_ms":http,"click_to_visible_receipt_ms":total,"request_sha256":body["pattern_receipt"]["request_sha256"],"result_sha256":body["pattern_receipt"]["result_sha256"],"output":body["output"]})
                    check(not errors,"PAGE_ERRORS")
                    r["viewports"].append({"trial":trial,"viewport":[width,height],"page_ready_ms":ready,"selection_ms":selection,"requests":rows})
                    page.close()
                b.close()
        finally:
            proc.terminate();proc.wait(timeout=10)
    r["summary"]={str(w):{k:samples([v[k] for v in r["viewports"] if v["viewport"][0]==w]) for k in ("page_ready_ms","selection_ms")} for w in (1280,390)}
    for w in (1280,390):
        for i in (0,1):
            r["summary"][str(w)]["request_"+str(i+1)]=samples([v["requests"][i]["click_to_visible_receipt_ms"] for v in r["viewports"] if v["viewport"][0]==w])
    r["server_startup"]=samples([v["server_ready_ms"] for v in r["startup"]])
    r["browser_startup"]=samples([v["browser_launch_ms"] for v in r["startup"]])
    r["checks"]=["three real server/browser launches","12 actual browser requests with exact B1 parity","two desktop/mobile-sized viewports","visible receipt correlation"]
    r["open"]=["new E1 authenticated origin and live invalidation successor not yet supplied","C1 independent acceptance separate","no physical handset or hardware GPU"]

def graph(root,r):
    pins={"nodes.json":"8467adaf1ac7c77e1a61db5ce0915cbb36f58c950d46735a325433023a90d1c1","edges.json":"ddcc74d2a81936aa0bfb0bd628d4e3246ce08b4fe5a4b3479509ad2e4ed44612","topology.json":"968bc7ef6fbfecb8dc6b55bf90a4ce4eb83d8ded86e9af6e0b5929ee6c15737d"}
    data={}
    for name,pin in pins.items():
        raw=(root/name).read_bytes();check(sha(raw)==pin,"PIN:"+name);data[name]=json.loads(raw)
    raw=(root/"periodic.json").read_bytes();check(blob(raw)=="0effdf62ccf1472480464843e8e4b15ec560f1bd","PERIODIC_PIN");periodic=json.loads(raw)
    nodes=data["nodes.json"]["features"];edges=data["edges.json"]["edges"];n=len(nodes)
    check((n,len(edges))==(1379,3249),"GENOME_COHORT")
    pairs=[(a,b) for a,b,_ in edges]
    off,items=csr(n,pairs)
    def allseeds():return [reverse(off,items,s) for s in range(n)]
    result=measure(r,"genome-all-seed-reverse",allseeds,digest(pins),n,3)
    visits=sum(x["record_visits"] for x in result)
    r["genome"]={"nodes":n,"records":len(edges),"seeds":n,"record_visits":visits,"edge_types":dict(Counter(e[2] for e in edges)),"runtime_edges_claimed":0}
    ids={x["id"]:i for i,x in enumerate(data["topology.json"]["nodes"])}
    printer=data["topology.json"]["edges"];check((len(ids),len(printer))==(30,164),"PRINTER_COHORT")
    po,pi=csr(len(ids),[(ids[x["from"]],ids[x["to"]]) for x in printer])
    pr=measure(r,"printer-all-seed-reverse",lambda:[reverse(po,pi,s) for s in range(len(ids))],pins["topology.json"],len(ids),3)
    r["printer"]={"nodes":len(ids),"records":len(printer),"visits":sum(x["record_visits"] for x in pr),"meaning":"URL references, not call graph"}
    r["repository_overlap"]=sorted(set(ids)&{x["id"].split("/",1)[1] for x in nodes if x["id"].startswith("Ventusltd/")})
    a=json.loads(pinned(root/"A1.zip",("5b3dc6d98ea6f3dec757263869d77a6261ce29d57ddce8a8659dfcd633ab1a86","property-impact.json","1233591210b19b006bb5970ecc85bdf0e5951cc3bef92e5e670871a4da0ca9e3")))
    b=json.loads(pinned(root/"B1.zip",("77561125ed5829483f30f84391c9998a21915654737fbfa34ca336b43686dbe5","tacit-b1-patterns.json","a5540a0978117750fd54739e423dbd4e7c0150ce1eba81d5139609ed2db7ee97")))
    pids={x["id"] for x in periodic["nodes"]};check(all(x["from"] in pids and x["to"] in pids for x in periodic["edges"]),"PERIODIC_EDGES")
    patterns=[b["results"][0]["pattern"],*[v["pattern"] for v in b["candidates"].values()]]
    expected={"engine/v9-geodesy.js":["nearest-orient","orient"],"engine/v9-nearest-search.js":["nearest-orient"],"engine/voltage-drop.js":["electrical"]}
    rows=[]
    for event in a["reverse_impacts"]:
        path=event["event"]["source"]["path"]
        affected=sorted(p["operation"] for p in patterns if any(s["source"]["path"]==path for s in p["sources"]))
        check(affected==expected[path]==event["affected_patterns"],"A_B_IMPACT_PARITY")
        rows.append({"path":path,"affected_patterns":affected,"historical_event_sha256":event["receipt_sha256"],"v2_pattern_sha256":[digest(p) for p in patterns if p["operation"] in affected]})
    r["dependency_scorecard"]=rows
    r["periodic"]={"nodes":len(pids),"edges":len(periodic["edges"]),"module_matches":{s:("block:"+s in pids) for s in ("Vg","Vn","Vd")},"scope":"exact existing ID lookup, no allocation"}
    for scale in (2,4,8):
        nn=n*scale;ee=[(x+n*j,y+n*j) for j in range(scale) for x,y in pairs]
        oo,ii=measure(r,"synthetic-"+str(scale)+"-csr",lambda:csr(nn,ee),digest([pins,scale]),nn,3)
        rr=measure(r,"synthetic-"+str(scale)+"-all-seed",lambda:[reverse(oo,ii,s) for s in range(nn)],digest([pins,scale,"all"]),nn,3)
        check(sum(x["record_visits"] for x in rr)==visits*scale,"SCALE_VISIT_PARITY")
    r["checks"]=["all real Genome seeds","all Printer seeds","exact A1/B1 source impact parity","Periodic Table endpoints","bounded replicated workload parity"]
    r["open"]=["static source applicability not live receipt invalidation","no GPU rerun; no estate-scale extrapolation","independent release acceptance separate"]

def main():
    mode,root,out=sys.argv[1],Path(sys.argv[2]),Path(sys.argv[3])
    r={"schema":"tacit-f1.convergence.v1","mode":mode,"stages":{},"production":False,"checks":[],"open":[]}
    try:
        {"graph":graph,"browser":browser}[mode](root,r);r["status"]="PASS_BOUNDED"
    except Exception as e:r["status"]="FAIL";r["failure"]=type(e).__name__+":"+str(e)
    r["environment"]={"python":platform.python_version(),"cpu_count":os.cpu_count(),"parent_peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,"child_peak_rss_kib":resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(r))
    print(json.dumps({"status":r["status"],"failure":r.get("failure"),"checks":len(r["checks"]),"open":len(r["open"]),"sha256":sha(out.read_bytes()),"summary":r.get("summary"),"startup":r.get("server_startup"),"graph":r.get("genome"),"stages":{k:v["median_ms"] for k,v in r["stages"].items()}},sort_keys=True))
    return int(r["status"]=="FAIL")
if __name__=="__main__":raise SystemExit(main())
