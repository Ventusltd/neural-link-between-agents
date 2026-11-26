"""C1 fresh ORIENT independent numerical verification of inherited B actual bridge.
Run only after successful inherited ninth-turn runtime staging and falsifiers.
This is not the combined successor or a browser-to-runtime test.
"""
import copy,json,math,sys
from pathlib import Path
from tacit_c_verify import canonical,sha,need,ARCHIVE,DESCRIPTOR
from tacit_c_seventh import member
from tacit_c_ninth import B_HEAD,B_PIN
from tacit_c_eighth_peer import pinned

def independent(a,b):
    # Vector central angle and local tangent direction; no producer imports.
    def xyz(p):
        lo,la=map(math.radians,(p["longitude"],p["latitude"]))
        return (math.cos(la)*math.cos(lo),math.cos(la)*math.sin(lo),math.sin(la))
    x,y=xyz(a),xyz(b)
    cross=(x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
    dot=lambda u,v:sum(i*j for i,j in zip(u,v))
    angle=math.atan2(math.sqrt(dot(cross,cross)),dot(x,y))
    lo,la=map(math.radians,(a["longitude"],a["latitude"]))
    east=(-math.sin(lo),math.cos(lo),0)
    north=(-math.sin(la)*math.cos(lo),-math.sin(la)*math.sin(lo),math.cos(la))
    return {"distance_km":6378.137*angle,"initial_bearing_deg":math.degrees(math.atan2(dot(y,east),dot(y,north)))%360}

def main():
    root,out=map(Path,sys.argv[1:]);obs=[]
    def check(case,ok,**detail):
        obs.append(dict(case=case,result="PASS" if ok else "FAIL",**detail))
    try:
        froot=root/"factory";peer=root/"peer-b";droot=root/"peer-d"
        sys.path[:0]=[str(froot/"tools"),str(peer/"tools"),str(droot/"tools")]
        import package_factory as f
        import typed_package_execution as t
        from tacit_b_kuiper import Bridge
        from kuiper_select import Space
        raw=member(root,"A-bonds")
        old=json.loads(pinned(root/"B-bridge.zip",B_PIN))
        archive=(root/"orient.zip").read_bytes()
        build=f.strict((root/"build.json").read_bytes())
        need(sha(archive)==ARCHIVE and build["descriptor_sha256"]==DESCRIPTOR,"ARCHIVE_PIN")
        check("original-archive-and-descriptor",True,archive_sha256=ARCHIVE,descriptor_sha256=DESCRIPTOR)
        b=Bridge(f,t,Space,raw,archive,build,root/"nearest",root/"nearest-source",root/"electrical")
        requests=[];receipts=[]
        pairs=[((-0.1276,51.5072),(2.3522,48.8566)),((179.8,12.3),(-179.4,12.7))]
        for idx,(a,z) in enumerate(pairs):
            point=lambda v:dict(longitude=v[0],latitude=v[1])
            inputs={"crs":"WGS84","unit":"degrees","point_a":point(a),"point_b":point(z)}
            req=b.request("orient",inputs);r=b.execute(req);again=b.execute(req)
            expect=independent(inputs["point_a"],inputs["point_b"]);actual=r["output"]
            check(f"fresh-{idx}-math",abs(actual["distance_km"]-expect["distance_km"])<=1e-6 and abs((actual["initial_bearing_deg"]-expect["initial_bearing_deg"]+180)%360-180)<=1e-7,expected=expect,actual=actual)
            check(f"fresh-{idx}-authority",r["admission"] is True and r["state"]=="EXECUTED_INTERNAL" and r["rights"]=="BLOCKED" and r["archive_sha256"]==ARCHIVE)
            check(f"fresh-{idx}-binding",r["request_sha256"]==f.sha(f.canonical(req)) and r["pattern_sha256"]==f.sha(f.canonical(r["pattern"])) and r["receipt_sha256"]==f.sha(f.canonical({k:v for k,v in r.items() if k!="receipt_sha256"})) and req["keys"]==old["requests"]["orient"]["keys"])
            check(f"fresh-{idx}-repeat",f.canonical(r)==f.canonical(again))
            requests.append(req);receipts.append(r)
        r,s=receipts
        check("same-pattern-different-requests-results",r["pattern_sha256"]==s["pattern_sha256"] and r["request_sha256"]!=s["request_sha256"] and r["receipt_sha256"]!=s["receipt_sha256"] and r["output"]!=s["output"] and all(x["request_sha256"]!=old["results"]["orient"]["request_sha256"] for x in receipts))
        def refused(label,fn):
            try:fn()
            except (ValueError,TypeError) as e:check(label,True,refusal=str(e))
            else:check(label,False)
        refused("cross-request-stale-receipt",lambda:b.replay(requests[1],r))
        fake=copy.deepcopy(r);fake["output"]["distance_km"]+=1;fake=b.seal({k:v for k,v in fake.items() if k!="receipt_sha256"})
        refused("rehashed-forged-result",lambda:b.replay(requests[0],fake))
        bad=copy.deepcopy(requests[0]);bad["inputs"]["unit"]="radians"
        refused("wrong-unit",lambda:b.execute(bad))
        for op in ("nearest-orient","electrical"):
            x=b.execute(old["requests"][op])
            check("default-refusal-"+op,x["state"]=="REFUSED" and x["output"] is None and x["admission"] is False)
        obs.append(dict(case="E1-D1-combined-replay",result="OPEN",reason="Predecessor B actual runtime only, not a browser-initiated fresh call. Exact combined candidate required."))
    except Exception as e:obs.append(dict(case="harness",result="FAIL",reason=type(e).__name__+":"+str(e)))
    counts={k:sum(x["result"]==k for x in obs) for k in ("PASS","FAIL","OPEN")}
    report=dict(schema="tacit-c1.fresh-orient-review.v1",B_head=B_HEAD,counts=counts,observations=obs,production=False,admission_changed=False)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for item in obs:print(json.dumps(item))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
