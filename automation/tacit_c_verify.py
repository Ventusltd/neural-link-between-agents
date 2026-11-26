#!/usr/bin/env python3
"""TACIT C: independent fourth-turn checks; no new permanent IDs or release authority."""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import zipfile

FACTORY = "2ccc717933f97e7d191dae85360559a12de7ed21"
ARCHIVE = "e83937c040499a7060b03ca2c4969e4414cdca48cb7f28a3ef9039f002486787"
DESCRIPTOR = "b45e61e955e0d0ddde15495f9be7c3fc4943c3193dd8f318a4249524f2fb5f53"
RECEIPT = "83147e90c0f0831ee1f82ce5e721a3521dc843421a96ae9cba3425343d0b3c19"
MODULE = "af9b5a8796b51a1e4368491b98961a197adec539f2fa0f3ed226552a876864bb"
PINS = {
    "printer.json": ("Ventusltd/spiders", "9801c73e8fd290d621bcf980fcc3fd6851229bf0", "spider_printer_v1/data/topology.json", "71e098e5095c444196095080efe74c37df4add25"),
    "genome.json": ("Ventusltd/spiders", "9801c73e8fd290d621bcf980fcc3fd6851229bf0", "species/genome-spider/data/nodes.json", "6fb7867bf6bf3abce14930f72dbfe5f8a323d86c"),
    "periodic.json": ("Ventusltd/stars", "1cf9c7530c7d287ccf9b3cffd70f693fb83c8402", "blocks/graph.json", "0effdf62ccf1472480464843e8e4b15ec560f1bd"),
    "modular.json": ("Ventusltd/stars", "1cf9c7530c7d287ccf9b3cffd70f693fb83c8402", "modular/graph.json", "349478a7fc286b36e6a08c325ce5f1980c2a3bd3"),
    "receiver.json": ("Ventusltd/ventus-grid-engine", "487ec7bd38dfa5aecb1c75da53b4a866ab2101cb", "spider/manifest.json", "79ec584f5040a0002da2a00b06defbeb3b510e03"),
    "maths.json": ("Ventusltd/ventus-grid-engine", "487ec7bd38dfa5aecb1c75da53b4a866ab2101cb", "genome/engine-graph.json", "7a9dd9774f4e4e876c3cd299c397309592860ea2"),
    "mission.json": ("Ventusltd/neural-link-between-agents", "e9ae30bfebc62425e2a1d3e40e0e6643339da03a", ".cvaa/contracts/vedic-core-mission.json", "24010433991b7b65083e710f89667108ae785363"),
    "recovery.json": ("Ventusltd/neural-link-between-agents", "e9ae30bfebc62425e2a1d3e40e0e6643339da03a", ".cvaa/contracts/vedic-third-turn-recovery.json", "fccb8e6220106da016aa482fc414ca37e39342bf"),
}
def need(ok, reason):
    if not ok:
        raise ValueError(reason)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()

def read_pinned(root, name):
    raw = (root / name).read_bytes()
    need(blob(raw) == PINS[name][3], "SOURCE_BLOB_MISMATCH:" + name)
    return json.loads(raw)

def identity_projection(kind, rows):
    """Only existing producer IDs, namespaced by producer; never allocate an ID."""
    ids = [r["id"] for r in rows]
    need(all(isinstance(i, str) and i for i in ids) and len(ids) == len(set(ids)), "INVALID_OR_DUPLICATE_ID")
    return {"producer":kind, "ids":sorted(ids)}

def graph_checks(root, record):
    d = {name:read_pinned(root, name) for name in PINS}
    printer,genome,periodic,modular = [d[x] for x in ("printer.json","genome.json","periodic.json","modular.json")]
    need(printer["schemaVersion"]=="0.2.0" and printer["methodState"]=="screening", "PRINTER_SCHEMA")
    need(genome["type"]=="FeatureCollection", "GENOME_SCHEMA")
    need(periodic["schema"]=="periodic-table-graph.v1" and modular["schema"]=="modular-star-graph.v1", "STARS_SCHEMA")
    for kind, rows in (("spider-printer",printer["nodes"]),("spider-genome",genome["features"]),("periodic-table",periodic["nodes"]),("modular-star",modular["nodes"])):
        baseline = identity_projection(kind, rows)
        changed = copy.deepcopy(rows)
        for row in changed:
            if kind=="spider-genome":
                row["properties"]["rag"]="amber"
                row["geometry"]["coordinates"]=[0,0]
            else:
                row["label"]="presentation change only"
                row["rag"]="amber"
                if kind=="spider-printer": row["x"],row["y"]=0,0
        need(identity_projection(kind, changed)==baseline, "PRESENTATION_CHANGED_ID")
        changed[0]["id"]="tacit-c-synthetic-mutation-not-an-issued-id"
        need(identity_projection(kind, changed)!=baseline, "ID_MUTATION_UNDETECTED")
        record.append({"case":kind+"-property-separation","result":"PASS","count":len(rows),"identity_projection_sha256":sha(canonical(baseline)),"scope":"synthetic mutation of pinned actual graph rows; not cross-version or permanent occurrence proof"})
    pids=set(identity_projection("spider-printer",printer["nodes"])["ids"])
    gids=set(identity_projection("spider-genome",genome["features"])["ids"])
    need(all(e["from"] in pids and e["to"] in pids and e["type"]=="reference" and type(e["references"]) is int and e["references"]>0 for e in printer["edges"]), "PRINTER_EDGE_CONTRACT")
    need(printer["totals"]["nodes"]==len(pids) and printer["totals"]["edges"]==len(printer["edges"]), "PRINTER_TOTALS")
    need(sum(e["references"] for e in printer["edges"])==printer["totals"]["totalReferences"],"REFERENCE_TOTAL")
    # Explicit repository-ID projection; not a function identity join.
    overlap=sorted(n for n in pids if "Ventusltd/"+n in gids)
    required=["vedic-","neural-link-between-agents","spiders","cvaa","ventus-grid-engine","stars"]
    coverage=[{"repository":n,"printer_present":n in pids,"genome_present":"Ventusltd/"+n in gids} for n in required]
    record.append({"case":"printer-coverage","result":"PASS","printer_nodes":len(pids),"printer_edges":len(printer["edges"]),"shared_repository_labels":overlap,"coverage":coverage,"edge_semantics":"URL references only; no inferred executable dependency","missing_nodes":"OPEN; do not silently invent rows"})
    receiver=d["receiver.json"]
    need(receiver["schema_version"]=="receiver-manifest-v1" and {"engine-graph","genome-spider","modular","periodic-table"} <= {g["id"] for g in receiver["graphs"]},"RECEIVER_CONTRACT")
    need(d["maths.json"]["schema"]=="ventus-grid-engine.genome.v1","MATHS_GENOME_SCHEMA")
    mission,recovery=d["mission.json"],d["recovery.json"]
    need(mission["recovery"]["blob"]==PINS["recovery.json"][3] and recovery["resume_policy"]=="read-only-until-revalidated","RECOVERY_PIN")
    need(recovery["totals"]["held"]==7 and recovery["totals"]["resolved"]==0,"RECOVERY_OBLIGATIONS")
    need(recovery["predecessor_ledger_capsule"]["totals"]["disputed"]==1,"HISTORICAL_DISPUTE_LOST")
    record.append({"case":"cold-recovery","result":"PASS","predecessor_ledger":recovery["predecessor_ledger_capsule"],"historical_printer_state":next(c["state"] for c in mission["channels"] if c["id"]=="spider-printer"),"new_observation":"Printer source located; historical contract remains unchanged","receipt_binding":"exact Git blobs"})
    return coverage

def runtime(root, record):
    # Import only exact peer sources, acquired by immutable commit in CI.
    peer=root/"peer"
    need(blob((peer/"tools/package_factory.py").read_bytes())=="23247de65fde04a400bb30874fc7e81cca4b7ebe","FACTORY_BLOB")
    need(blob((peer/"tools/typed_package_execution.py").read_bytes())=="480a0d0d1ee1af0b7a5919e307564cf597b9f8ff","TYPED_CONSUMER_BLOB")
    sys.path.insert(0,str(peer/"tools"))
    import package_factory as factory
    import typed_package_execution as consumer
    # Reuse TACIT9 independent vector oracle, not producer trigonometry.
    sys.path.insert(0,str(root/"oracle"))
    import acceptance as oracle
    inputs=root/"inputs"
    descriptor=json.loads((peer/"packages/factory/admissions/orient.json").read_bytes())
    archive=root/"orient.zip"
    receipt=factory.build(descriptor, inputs, archive)
    raw=archive.read_bytes()
    need(sha(raw)==ARCHIVE and receipt["descriptor_sha256"]==DESCRIPTOR,"ARCHIVE_OR_DESCRIPTOR_PIN")
    with zipfile.ZipFile(archive) as z:
        need(sha(z.read("source-receipt.json"))==RECEIPT and sha(z.read("v9-geodesy.mjs"))==MODULE,"ARCHIVE_SOURCE_PIN")
    q=json.loads((peer/"packages/factory/orient-execution.json").read_bytes())
    cases=oracle.CASES+[("tacit-c-northwest",oracle.pair((0,0),(-1,1))),("tacit-c-polar-destination",oracle.pair((10,80),(10,90))),("tacit-c-wrap",oracle.pair((0,0),(-0.001,1)))]
    for label, x in cases:
        req=copy.deepcopy(q)
        req["input"].update(point_a=x["origin"],point_b=x["destination"])
        expected=oracle.oracle(x)
        try:
            actual=consumer.execute(req,raw,receipt)
            out=actual["pattern"]["output"]
            oracle.close_result(out,expected)
            again=consumer.execute(req,raw,receipt)
            need(actual==again,"NONDETERMINISTIC_RESULT")
            record.append({"case":label,"result":"PASS","expected":expected,"actual":out,"pattern_sha256":actual["pattern_sha256"]})
        except Exception as e:
            record.append({"case":label,"result":"FAIL","expected":expected,"reason":type(e).__name__+":"+str(e)})
    def reject(label, fn):
        try:
            fn()
        except (ValueError,KeyError,TypeError) as e:
            record.append({"case":label,"result":"PASS","observation":"actual peer refusal","reason":type(e).__name__+":"+str(e)})
        except Exception as e:
            record.append({"case":label,"result":"FAIL","reason":"unexpected exception "+type(e).__name__})
        else:
            record.append({"case":label,"result":"FAIL","observation":"peer unexpectedly accepted mutation"})
    for label,x in oracle.negative_inputs():
        req=copy.deepcopy(q)
        if "origin" in x: req["input"]["point_a"]=x["origin"]
        if "destination" in x: req["input"]["point_b"]=x["destination"]
        else: del req["input"]["point_b"]
        if x["unit"]!="degree": req["input"]["unit"]=x["unit"]
        req["input"]["crs"]=x["crs"]
        if "selection_revision" in x: req["input"]["selection_revision"]=x["selection_revision"]
        reject(label,lambda req=req:consumer.execute(req,raw,receipt))
    for label,key,val in [("unknown-source","archive_sha256","0"*64),("forged-descriptor","descriptor_sha256","0"*64),("nearest-not-admitted","family","nearest-substation"),("unknown-export","export","distanceKm"),("unit-mismatch","ports",dict(q["ports"],distance="m"))]:
        m=dict(q,**{key:val})
        reject(label,lambda m=m:consumer.execute(m,raw,receipt))
    reject("archive-byte-tamper",lambda:consumer.execute(q,raw[:-1]+bytes([raw[-1]^1]),receipt))
    reject("receipt-occurrence-tamper",lambda:consumer.execute(q,raw,dict(receipt,input_pins=[])))
    reject("electrical-not-admitted",lambda:factory.admit(json.loads((peer/"packages/factory/pending/electrical.json").read_bytes())))
    reject("unreviewed-closure",lambda:factory.review_receipt("nearest-substation",b"{}",{},b"{}"))
    peer_raw=(inputs/"peer-orient.json").read_bytes()
    original=consumer.execute_peer(peer_raw,raw,receipt)
    oracle.close_result(original["pattern"]["output"],oracle.oracle(oracle.pair((0,0),(1,0))))
    record.append({"case":"actual-peer-plan","result":"PASS","actual":original["pattern"]["output"],"pattern_sha256":original["pattern_sha256"]})
    for label,mutation in [
        ("wrong-source-occurrence",lambda p:p["plan"]["nodes"][0]["source"].update(first=30)),
        ("graph-mutation",lambda p:p["plan"]["nodes"].reverse()),
        ("missing-dependency",lambda p:p["plan"]["dependencies"].pop()),
        ("stale-coordinate",lambda p:p["inputs"]["point_b"].update(longitude=2)),
        ("forged-output",lambda p:p["outputs"].update(distance_km=1)),
    ]:
        p=json.loads(peer_raw);mutation(p)
        reject(label,lambda p=p:consumer.execute_peer(canonical(p),raw,receipt))
    return {"archive_sha256":sha(raw),"descriptor_sha256":DESCRIPTOR,"source_receipt_sha256":RECEIPT,"module_sha256":MODULE}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("mode",choices=("channels","runtime"))
    p.add_argument("root",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    observations=[]
    details={}
    try:
        details = {"coverage":graph_checks(a.root,observations)} if a.mode=="channels" else runtime(a.root,observations)
    except Exception as e:
        observations.append({"case":"apparatus-or-contract","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    result="PASS" if observations and all(x["result"]=="PASS" for x in observations) else "FAIL"
    receipt={"schema":"vedic.independent-observation.v1","principal":"TACIT 1b / existing estate producers","measured_twin":a.mode,"falsifier":"TACIT C; mathematical oracle TACIT 9","witness":"GitHub Actions; exact checked-out verifier head in run context","question":"Do pinned artifacts preserve identity and execute the admitted bounded operation correctly?","apparatus":{"factory_commit":FACTORY,"source_pins":PINS,"oracle_commit":"1aa2b9d1ab3bf9c6963b68b20ea608e826162e15"},"procedure":"Exact digest validation; actual peer consumer and independent vector oracle or data-only graph projection; negative controls retained","observations":observations,"result":result,"details":details,"verdict":{"test":result,"formal_independent_acceptance":"OPEN","rights":"BLOCKED","permanent_identity":"OPEN","nearest_admission":"OPEN","electrical_admission":"OPEN","publication":"NOT_AUTHORISED"},"limitations":["No live producer wiring or permanent ID allocation","No proof of graph edge execution or historical identity across releases","No software or source archive distribution","Historical CVAA registry failure and all prior obligations remain open","No nearest or electrical mathematical acceptance before legitimate admission"]}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_bytes(canonical(receipt))
    print(json.dumps({"mode":a.mode,"result":result,"observations":len(observations),"receipt_sha256":sha(a.out.read_bytes())}))
    return 0 if result=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
