"""F1 T17: source discovery and measured existing-factory baseline; no semantic engine."""
import json,sys,time,statistics,copy
from pathlib import Path
from tacit_f1_performance import check,sha,blob,digest
from tacit_c_eighth_peer import pinned
from tacit_c_verify import canonical,ARCHIVE
from tacit_c_seventh import member
G="487ec7bd38dfa5aecb1c75da53b4a866ab2101cb"
GA="afffa9781f6130529ae93052604cd3d98d172a35"
S="665faa0a19ca0a5a19a297e74bc5aae4020e9fd5"
P="preview/9698781539e549deaa6ecaa4a2b34610c1f9fd29/"
# Existing producer IDs only; absence is not a newly issued identity.
SOURCES=[
("nearest-source/v9-geodesy.js","ventus-grid-engine",G,"engine/v9-geodesy.js","14023f06d4ef2ea806437863bd35dee954c46b11",["distanceKm","initialBearingDeg"],"block:Vg","ADMITTED_ORIENT_ONLY",["EARTH_RADIUS_KM"],"WGS84 degrees lon/lat -> km and degrees; sphere 6378.137 km"),
("atlas-geodesy.js","gridatlas",GA,"atlas/modules/202609011950-geodesy.js","bfc364925b05a4295fc916fc6d55ec771b337548",["distanceKm","initialBearingDeg"],None,"SOURCE_LINEAGE_ONLY",["window module registration"],"original Atlas implementation; do not grant admission to alternative copy"),
("vicinity.js","gridatlas",GA,"atlas/modules/202611180026-grid-vicinity.js","419758cc50731538e44cf604067a2ef2ecf67950",["stationRecords","exploreVicinity"],None,"RESEARCH_NOT_ADMITTED",["representativePoint","voltagesKv","distanceKm","normaliseOrigin","radiusKm"],"explicit 132 voltage band, radius, ordered distance/name/id; source geometry/rights and closure still required"),
("nearest-source/v9-nearest-search.js","ventus-grid-engine",G,"engine/v9-nearest-search.js","d2ab3b111eb09f7af3df3a9fce9ad0a9dc1dea99",["normalise","index"],"block:Vn","CANDIDATE_DEFAULT_REFUSED",["./v9-geodesy.js"],"minimumKv is maximum declared voltage threshold, NOT exact 132 kV membership"),
("compass.mjs","satnav",S,P+"nav/compass.mjs","9813532f1df0ee0a6e99ab6952087d64814586ce",["fixQuality","guide"],None,"RESEARCH_NOT_ADMITTED",["../vendor/grid-distance-maths/src/geodesy.mjs","trusted fix time/accuracy"],"straight-line guide; stale >10s, poor >30m; not route/access"),
("satnav-geodesy.mjs","satnav",S,P+"vendor/grid-distance-maths/src/geodesy.mjs","5a0320ca6db05273fae14f786b20223b088bc60b",["distanceKm","initialBearingDeg","distanceEllipsoidalKm"],"block:x776","ALTERNATIVE_COPY_NOT_ADMITTED",["R_ATLAS","WGS84"],"classification link is upstream similarity, not byte identity or authority"),
("electrical/module.mjs","ventus-grid-engine",G,"engine/voltage-drop.js","85f48ecf7effabb47973b0a056f90e82b8196ef2",["voltageDropVolts","dropPercent","lossesWatts","annualLossKwh"],"block:Vd","CANDIDATE_DEFAULT_REFUSED",["explicit current/R/X/length/PF/nominal voltage/loss factor"],"V, %, W, kWh; no cable selection or compliance"),
("current.js","ventus-grid-engine",G,"engine/current-from-power.js","78dc747eff3c8e5d8b756fac1652674dc7c3c320",["currentA","currentFromMvaAtKv"],None,"RESEARCH_NOT_ADMITTED",["apparent power VA or MVA","voltage V or kV","phase"],"implied amperes, not actual load, headroom or rating")
]
def main(root,out):
    raw=(root/"nodes.json").read_bytes();check(sha(raw)=="8467adaf1ac7c77e1a61db5ce0915cbb36f58c950d46735a325433023a90d1c1","GENOME")
    genome=json.loads(raw);ids={x["id"]:i for i,x in enumerate(genome["features"])}
    raw=(root/"edges.json").read_bytes();check(sha(raw)=="ddcc74d2a81936aa0bfb0bd628d4e3246ce08b4fe5a4b3479509ad2e4ed44612","EDGES")
    edges=json.loads(raw)["edges"]
    raw=(root/"topology.json").read_bytes();check(sha(raw)=="968bc7ef6fbfecb8dc6b55bf90a4ce4eb83d8ded86e9af6e0b5929ee6c15737d","PRINTER")
    printer=json.loads(raw);pids={x["id"] for x in printer["nodes"]}
    raw=(root/"periodic.json").read_bytes();check(blob(raw)=="0effdf62ccf1472480464843e8e4b15ec560f1bd","STARS")
    stars={x["id"]:x for x in json.loads(raw)["nodes"]}
    rows=[]
    for local,repo,head,path,b,functions,block,admission,deps,cap in SOURCES:
        source=(root/local).read_bytes();check(blob(source)==b,"SOURCE:"+path)
        lines=source.decode().splitlines()
        positions={f:[i+1 for i,x in enumerate(lines) if "function "+f+"(" in x] for f in functions}
        check(all(positions.values()),"FUNCTION:"+path)
        identity="Ventusltd/"+repo+"::"+path
        n=ids.get(identity)
        if block:check(block in stars,"BLOCK")
        rows.append({"repository":"Ventusltd/"+repo,"commit":head,"path":path,"git_blob":b,"sha256":sha(source),"function_definition_lines":positions,"genome_id":identity if n is not None else None,"genome_repository_present":"Ventusltd/"+repo in ids,"genome_incident_records":sum(a==n or z==n for a,z,_ in edges) if n is not None else None,"printer_repository_present":repo in pids,"printer_url_reference_edges":sum(x["from"]==repo or x["to"]==repo for x in printer["edges"]),"periodic_block":block,"periodic_link":stars[block]["gh"] if block else None,"admission":admission,"dependencies":deps,"capability":cap})
    froot=root/"factory";peer=root/"peer-b";droot=root/"peer-d"
    sys.path[:0]=[str(froot/"tools"),str(peer/"tools"),str(droot/"tools")]
    import package_factory as f
    import typed_package_execution as t
    from kuiper_select import Space
    from tacit_b_patterns import PatternBridge
    from tacit_b_convergence import bind_execution,orient
    raw=member(root,"A-bonds")
    desc=f.strict(f.ADMISSIONS["orient"].read_bytes())
    archive=root/"manual-orient.zip";build=f.build(desc,root/"inputs",archive)
    check(sha(archive.read_bytes())==ARCHIVE,"ARCHIVE")
    bridge=PatternBridge(f,t,Space,raw,archive.read_bytes(),build,root/"nearest",root/"nearest-source",root/"electrical")
    # Actual manual selection of two ORIENT operations; no ranking bypass.
    fixtures=[{"A":(-1.51,52.41),"B":(-2.46,53.11),"C":(0.35,51.21)},{"A":(12.4,48.1),"B":(15.2,47.5),"C":(9.8,50.3)},{"A":(151.1,-33.8),"B":(150.5,-34.4),"C":(153.2,-28.7)}]
    evidence=[]
    for points in fixtures:
        timings=[];receipts=None
        for repeat in range(3):
            start=time.perf_counter_ns();rr=[]
            for j,target in enumerate(("B","C")):
                q=bridge.request_v2("orient",orient(points["A"],points[target]))
                ctx={"generation":j+1,"selection_receipt_sha256":"a"*64,"challenge":str(j+1)*64}
                bound=bind_execution(bridge,q,ctx)
                check(bound["pattern_receipt"]["result"]["state"]=="EXECUTED_INTERNAL","ACTUAL_RUNTIME")
                rr.append({"target":target,"output":bound["pattern_receipt"]["result"]["output"],"request_sha256":bound["pattern_receipt"]["request_sha256"],"receipt_sha256":bound["receipt_sha256"],"pattern_sha256":bound["pattern_receipt"]["pattern_sha256"]})
            timings.append((time.perf_counter_ns()-start)/1e6)
            if receipts is None:receipts=rr
            else:check(receipts==rr,"DETERMINISM")
        evidence.append({"points":points,"manual_commands":2,"coordinate_entries":8,"unique_coordinate_fields":6,"factory_calls":2,"unique_admitted_archive":1,"comparison":"REFUSED_NOT_ADMITTED","results":receipts,"median_ms":statistics.median(timings),"samples_ms":timings})
    prior=json.loads(pinned(root/"B1.zip",("77561125ed5829483f30f84391c9998a21915654737fbfa34ca336b43686dbe5","tacit-b1-patterns.json","a5540a0978117750fd54739e423dbd4e7c0150ce1eba81d5139609ed2db7ee97")))
    for op in ("nearest-orient","electrical"):
        check(bridge.execute_v2(prior["candidate_requests"][op])==prior["refusals"][op],"REFUSAL")
    report={"schema":"tacit-f1.vedic-reuse-evidence.v1","source_rows":rows,"manual_baseline":evidence,"instruction":"Calculate distance and initial bearing from point A to point B and from point A to point C, then identify the nearer destination.","language_target":{"human_instruction_count":1,"factory_calls":2,"unique_archive":1,"comparison":"REFUSED_NOT_ADMITTED","status":"TARGET_NOT_MEASURED"},"open":["actual peer semantic/compound integration requires exact successor pins","authenticated UI timings not yet measured for T17","source discovery is not Kuiper permanent occurrence allocation","dataset rights and exact 132kV membership before nearest admission"],"status":"PASS_BOUNDED"}
    out.write_bytes(canonical(report))
    print(json.dumps({"sha256":sha(out.read_bytes()),"sources":len(rows),"manual":evidence,"graph_coverage":[{k:r[k] for k in ("repository","path","genome_id","printer_repository_present","periodic_block")} for r in rows]},sort_keys=True))
if __name__=="__main__":main(Path(sys.argv[1]),Path(sys.argv[2]))
