"""F1: hosted CPU evidence, not an execution engine or admission mechanism."""
import copy, hashlib, json, math, os, platform, resource, statistics, sys, time
from collections import deque
from pathlib import Path
from tacit_c_verify import sha, blob, canonical, need, ARCHIVE, DESCRIPTOR
from tacit_c_ninth import B_PIN, A_PIN
from tacit_c_eighth_peer import pinned
from tacit_c_seventh import member

LAB_BLOB = "4273eb3d4e0715f12cce22a5ac5030cb579addcd"
REPEATS = 5
def check(ok, label):
    need(ok, label)
def digest(x):
    return sha(canonical(x))
def measure(report, label, fn, input_sha, cohort, n=REPEATS):
    samples = []
    cpu = []
    first = None
    expected = None
    for i in range(n):
        start = time.perf_counter_ns()
        c = time.process_time_ns()
        value = fn()
        cpu.append((time.process_time_ns()-c)/1e6)
        samples.append((time.perf_counter_ns()-start)/1e6)
        d = digest(value)
        if i == 0:
            first, expected = value, d
        check(d == expected, "NONDETERMINISTIC:"+label)
    report["stages"][label] = {"input_sha256":input_sha,"cohort":cohort,
        "samples_ms":samples,"first_ms":samples[0],"warm_median_ms":statistics.median(samples[1:]),
        "median_ms":statistics.median(samples),"range_ms":[min(samples),max(samples)],
        "parent_cpu_ms":cpu,"repeats":n,"output_sha256":expected,
        "memory_scope":"process-wide peak RSS; see environment, not per-stage"}
    return first

def csr(n, edges):
    # Convert actual published index-array records into incoming CSR, retaining duplicates.
    buckets = [[] for _ in range(n)]
    for a,b in edges:
        check(type(a) is int and type(b) is int and 0 <= a < n and 0 <= b < n, "EDGE_RANGE")
        buckets[b].append(a)
    offsets, items = [0], []
    for b in buckets:
        items.extend(b); offsets.append(len(items))
    return offsets,items

def reverse(offsets,items,seed):
    seen={seed:0}; queue=deque([seed]); visits=0
    while queue:
        target=queue.popleft()
        for j in range(offsets[target],offsets[target+1]):
            source=items[j]; visits+=1
            if source not in seen:
                seen[source]=seen[target]+1; queue.append(source)
    return {"depths":sorted(seen.items()),"record_visits":visits}

def graph(report, label, n, edges, input_sha, synthetic=False):
    check(0<n<=12000 and len(edges)<=30000,"GRAPH_BOUND")
    offsets, items=measure(report,label+"-csr",lambda:csr(n,edges),input_sha,n)
    check(offsets[-1]==len(edges),"CSR_RECORD_COUNT")
    # Fixed seeds across index domain, not a claim to scan all of the estate.
    seeds=sorted(set([0,n//4,n//2,3*n//4,n-1]))
    result=measure(report,label+"-reverse",lambda:[reverse(offsets,items,s) for s in seeds],
        digest([input_sha,seeds]),n)
    visits=sum(r["record_visits"] for r in result)
    report["graphs"][label]={"nodes":n,"records":len(edges),"seeds":seeds,"record_visits":visits,
        "synthetic":synthetic,"interpretation":"static records, not execution or runtime call edges",
        "visits_per_second":visits/(report["stages"][label+"-reverse"]["median_ms"]/1000)
        if report["stages"][label+"-reverse"]["median_ms"] else None}

def runtime(root,report):
    raw_lab=(root/"lab.json").read_bytes()
    check(blob(raw_lab)==LAB_BLOB,"LAB_PIN")
    lab=json.loads(raw_lab)
    report["historical_cuda"]={"source_git_blob":LAB_BLOB,"sha256":sha(raw_lab),
        "status":"PRODUCER_REPORTED_NOT_REPEATED","baseline":lab["baseline"],
        "graph_summary":lab["spider"]["graphs"],"failed_local_receipts":lab["local_failure_receipts"],
        "raw_local_receipts":"OPEN_UNAVAILABLE","gpu_acceptance":False}
    pins=lab["spider"]["input_sha256"]
    data={}
    for path in ("species/genome-spider/data/nodes.json","species/genome-spider/data/edges.json","spider_printer_v1/data/topology.json"):
        file=root/Path(path).name
        b=measure(report,"read-"+file.name,lambda:{"sha256":sha(file.read_bytes())},pins[path],1)
        check(b["sha256"]==pins[path],"SPIDER_INPUT_PIN")
        data[file.name]=json.loads(file.read_bytes())
    n=len(data["nodes.json"]["features"])
    edges=[(a,b) for a,b,_ in data["edges.json"]["edges"]]
    check((n,len(edges))==(1379,3249),"GENOME_COHORT")
    graph(report,"genome",n,edges,digest([pins["species/genome-spider/data/nodes.json"],pins["species/genome-spider/data/edges.json"]]))
    printer=data["topology.json"]
    ids={x["id"]:i for i,x in enumerate(printer["nodes"])}
    pe=[(ids[x["from"]],ids[x["to"]]) for x in printer["edges"]]
    check((len(ids),len(pe))==(30,164),"PRINTER_COHORT")
    graph(report,"printer",len(ids),pe,pins["spider_printer_v1/data/topology.json"])
    for scale in (2,4,8):
        se=[(a+k*n,b+k*n) for k in range(scale) for a,b in edges]
        graph(report,"synthetic-genome-"+str(scale),n*scale,se,digest([pins["species/genome-spider/data/edges.json"],scale]),True)
    # All producer acquisitions inherited from C's previously verified staging.
    froot=root/"factory"; peer=root/"peer-b"; droot=root/"peer-d"
    sys.path[:0]=[str(froot/"tools"),str(peer/"tools"),str(droot/"tools")]
    import package_factory as f
    import typed_package_execution as t
    from tacit_b_kuiper import Bridge
    from kuiper_select import Space, load
    zip_path=root/"A-bonds.zip"
    manifest=measure(report,"authenticated-manifest-load",lambda:load(zip_path),sha(zip_path.read_bytes()),8)
    raw=member(root,"A-bonds")
    check(json.loads(raw)==manifest,"MANIFEST_PARITY")
    mhash=sha(raw)
    space=Space(manifest)
    measure(report,"property-validation",lambda:sorted(Space(manifest).by_key),mhash,8)
    keys=measure(report,"property-selection",lambda:space.select(module="Vg",property_name="runtime_effects",state="UNKNOWN"),mhash,8)
    check(len(keys)==2,"PROPERTY_SELECTION")
    check(tuple(sorted(k for i in (1,5) for k in space.select(meaning="GG2050-VEDIC-%06d"%i)))==keys,"MEANING_MACHINE_PARITY")
    positions=measure(report,"original-js-projection",lambda:space.project(tuple(sorted(space.by_key))),mhash,8)
    check(len(positions)==8 and all(p["m"]==(p["key"]*2654435769)%2**32 for p in positions),"PLACEMENT_MOD")
    check(all(abs(p["r"]-math.sqrt(p["key"]+0.5))<1e-9 for p in positions),"PLACEMENT_RADIUS")
    # Cache is disposable, content-addressed, never an execution-result cache.
    cache={}
    def lookup(payload):
        key=sha(payload)
        if key not in cache:
            check(key==mhash,"CACHE_UNAUTHENTICATED")
            cache[key]=Space(json.loads(payload))
        return cache[key]
    def cold():
        cache.clear();return sorted(lookup(raw).by_key)
    measure(report,"selection-cache-empty",cold,mhash,8)
    measure(report,"selection-cache-warm",lambda:sorted(lookup(raw).by_key),mhash,8)
    try: lookup(raw+b" ")
    except ValueError: pass
    else: raise ValueError("CACHE_INVALIDATION_FAILED")
    check(len(cache)==1,"CACHE_MUTATION")
    archive=root/"orient.zip"
    desc=f.strict(f.ADMISSIONS["orient"].read_bytes())
    build=measure(report,"factory-build",lambda:f.build(desc,root/"inputs",archive),digest(desc),1,3)
    ar=archive.read_bytes()
    check(sha(ar)==ARCHIVE and build["descriptor_sha256"]==DESCRIPTOR,"ORIENT_ARCHIVE_PIN")
    b=Bridge(f,t,Space,raw,ar,build,root/"nearest",root/"nearest-source",root/"electrical")
    rep=json.loads(pinned(root/"B-bridge.zip",B_PIN))
    q1=rep["requests"]["orient"]; q2=copy.deepcopy(q1)
    q2["inputs"]["point_b"]["longitude"]=2
    rc=[]
    for i,q in enumerate((q1,q2)):
        r=measure(report,"actual-orient-"+str(i+1),lambda q=q:b.execute(q),digest(q),2,3)
        check(r["state"]=="EXECUTED_INTERNAL" and r["archive_sha256"]==ARCHIVE and r["request_sha256"]==digest(q),"RUNTIME_RECEIPT")
        check(r["receipt_sha256"]==digest({k:v for k,v in r.items() if k!="receipt_sha256"}),"RECEIPT_HASH")
        rc.append(r)
    check(rc[0]["request_sha256"]!=rc[1]["request_sha256"] and rc[0]["output"]!=rc[1]["output"],"FRESH_REQUEST")
    check(rc[0]["pattern_sha256"]==rc[1]["pattern_sha256"],"STABLE_PATTERN")
    report["runtime"]=[{k:r[k] for k in ("request_sha256","pattern_sha256","receipt_sha256","output","state","archive_sha256")} for r in rc]
    for op in ("nearest-orient","electrical"):
        r=b.execute(rep["requests"][op])
        check(r["state"]=="REFUSED" and r["output"] is None and r["nodes"]==[],"DEFAULT_REFUSAL:"+op)
    report["checks"] += ["authenticated eight-key cohort","machine/meaning parity","original projection MOD/radius","cache tamper refusal","actual ORIENT archive","two distinct fresh requests","stable pattern","nearest and electrical refused"]
    report["open"] += ["A1/B1/D1/E1 successor candidate not staged","independent oracle remains C1 scope","no physical GPU or handset replay","cold OS cache not controlled; cold means empty application cache","CPU scaling measured only on disjoint synthetic copies; not estate scaling"]

def impact(root,report):
    raw=pinned(root/"A-impact.zip",A_PIN)
    m=json.loads(raw)
    check((root/"impact-first.json").read_bytes()==(root/"impact-second.json").read_bytes()==raw,"ACTUAL_IMPACT_REPLAY")
    sys.path.insert(0,str(root/"peer-a"/"tools"))
    import tacit_a_impact as a
    expect={"engine/v9-geodesy.js":["nearest-orient","orient"],"engine/v9-nearest-search.js":["nearest-orient"],"engine/voltage-drop.js":["electrical"]}
    events=[]
    for r in m["source_entries"]:
        s=r["source"]
        events.extend([({"kind":"source","source":s,"new_blob":"0"*40},expect[s["path"]]),
                       ({"kind":"source","source":s,"new_blob":s["blob"]},[]),
                       ({"kind":"presentation","source":s,"field":"display_colour"},[]),
                       ({"kind":"presentation","source":s,"field":"classification_description"},[])])
    for family,row in m["family_reviews"].items():
        events.append(({"kind":"closure","family":family,"old_sha256":row["closure_sha256"],"new_sha256":"0"*64},sorted(p["operation"] for p in m["patterns"] if family in p["families"])))
    for p in m["properties"]:
        s=p["source_occurrence"]
        events.append(({"kind":"property","source":s,"property":p["property"],"old_sha256":a.sha(a.canonical(p)),"new_sha256":"0"*64},sorted(x["operation"] for x in m["patterns"] if any(z["source"]==s for z in x["sources"]))))
    before=sha(a.canonical(m))
    got=measure(report,"actual-reverse-impact-batch",lambda:[a.impact(m,e) for e,_ in events],digest([sha(raw),[e for e,_ in events]]),len(events))
    rows=[]
    for i,((e,want),r) in enumerate(zip(events,got)):
        check(r["affected_patterns"]==want and not r["addresses_changed"],"IMPACT_"+str(i))
        expected=sorted({d for p in m["patterns"] if p["operation"] in want for d in p["receipts"]})
        check([x["sha256"] for x in r["affected_receipts"]]==expected and all(x["state"]=="STALE_FOR_NEW_INPUT_HISTORICAL_PRESERVED" for x in r["affected_receipts"]),"RECEIPT_STALE_"+str(i))
        rows.append({"case":i,"kind":e["kind"],"event_sha256":digest(e),"affected_patterns":want,"stale_receipt_count":len(expected),"state":r["state"]})
    check(sha(a.canonical(m))==before and sha(raw)==A_PIN[2],"HISTORICAL_BYTES")
    check(len(m["bond_details"])==5 and all(x["relationship_state"]=="CONDITIONAL_CANDIDATE" for x in m["bond_details"]),"CONDITIONAL")
    report["impact"]={"rows":rows,"manifest_sha256":sha(raw),"actual_producer_replay":True,
        "conditional_bonds":5,"historical_receipts_unchanged":True,"live_consumer":False}
    report["checks"] += ["producer cold replay byte-identical","all "+str(len(rows))+" source/closure/property/presentation events","historical bytes unchanged","conditional bonds preserved"]
    report["open"] += ["A1 successor contract and E1 integrated runtime not yet staged","live receipt invalidation unverified","CVAA/Faraday/Quantum Twin inherited evidence only; no live wiring"]

def main():
    mode,root,out=sys.argv[1],Path(sys.argv[2]),Path(sys.argv[3])
    report={"schema":"tacit-f1.performance-regression.v1","mode":mode,"stages":{},"graphs":{},"checks":[],"open":[],
      "acquisition":{"staged_network_wall_ms":int((root/"acquisition-ns.txt").read_text())/1e6,"repeats":1,"scope":"network setup in workflow; no cold/warm network claim"},
      "environment":{"python":platform.python_version(),"platform":platform.platform(),"logical_cpus":os.cpu_count()},
      "authority":"RESEARCH_ONLY","production":False,"redistribution":"BLOCKED"}
    try:
        {"runtime":runtime,"impact":impact}[mode](root,report)
        report["status"]="PASS_BOUNDED"
    except Exception as e:
        report["status"]="FAIL"; report["failure"]=type(e).__name__+":"+str(e)
    report["environment"].update(parent_peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                                  child_peak_rss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes(canonical(report))
    print(json.dumps({"status":report["status"],"checks":len(report["checks"]),"open":len(report["open"]),
      "sha256":sha(out.read_bytes()),"stages":{k:round(v["median_ms"],4) for k,v in report["stages"].items()},
      "failure":report.get("failure")},sort_keys=True))
    return int(report["status"]=="FAIL")

if __name__=="__main__":
    raise SystemExit(main())
