"""Fifth turn independent producer witnesses; not a new runtime, classifier or admission gate."""
import copy
import json
import math
from pathlib import Path
import sqlite3
import subprocess
import sys
import zipfile
from tacit_c_verify import sha,blob,canonical,need
PINS={"v9-nearest-search.js":"d2ab3b111eb09f7af3df3a9fce9ad0a9dc1dea99","v9-geodesy.js":"14023f06d4ef2ea806437863bd35dee954c46b11","voltage-drop.js":"85f48ecf7effabb47973b0a056f90e82b8196ef2","table.json":"aaa1f27d2d4acf372c8c6868987072779bb90d8a","catalogue.json":"38e0fbb0ead2d21467889563d31a1cbf0b306ac1"}
ARTIFACTS={"A":("c1ea563a7be0c1343d547d5678f46b86952a73bc8d5346d330a0faf8e7667772","candidate.json","5f5cc4c75515ca0059fb67e2f511c4b22d7e048096916cff569ecd630578a831"),"crosswalk":("2ae770734cdfe12d307e8fc3a3bd063fac172d0c7964a7f743efecc49024eddc","crosswalk.json","cb496073d32a84d1d4dc8ff73d75552eaf05867b3186f0d19aea9db8f7bd1d7f"),"classification":("9eda93c93072930348d0c3a07fb7a23c50d826769005debb5fbf3bb07927d4ab","classification.json","7ead5adf6049c4bc606b993ba17e97a08530b77a65156188b5ded1ec43e35655"),"previous":("8469f9457a73e24a484beff998a386b591089dc35147176b39b26f842b69dcf9","b-corrective-review.json","dd95231390005a7e72ae85b03bb203ad5afaa7b29d9492972f4ff6403c30dc74")}
def artifact(root,key):
    zpin,name,pin=ARTIFACTS[key]
    p=root/(key+".zip");need(sha(p.read_bytes())==zpin,"ZIP_PIN:"+key)
    with zipfile.ZipFile(p) as z:
        members=[m for m in z.infolist() if m.filename==name or m.filename.endswith("/"+name)]
        need(len(members)==1 and members[0].file_size<4_000_000,"MEMBER")
        raw=z.read(members[0])
    need(sha(raw)==pin,"CONTENT_PIN:"+key)
    return json.loads(raw)
def distance(oracle,origin,loc):
    a=oracle.vector(origin["longitude"],origin["latitude"]);b=oracle.vector(loc["longitude"],loc["latitude"])
    return oracle.R*math.atan2(math.hypot(*oracle.cross(a,b)),oracle.dot(a,b))
def expected_rank(oracle,q):
    # Stable sorting by physical spherical distance; no new production search.
    return sorted([{"id":r["id"],"distance_km":distance(oracle,q["query"],r["location"])} for r in q["records"] if r["voltages_kv"] and max(r["voltages_kv"])>=q["minimumKv"]],key=lambda x:x["distance_km"])
def fixtures():
    def r(i,lon,lat,vs):return {"id":i,"name":"Synthetic "+i,"location":{"longitude":lon,"latitude":lat},"voltages_kv":vs}
    def q(records,lon=0,lat=0,minimum=132):return {"crs":"EPSG:4326","query":{"longitude":lon,"latitude":lat},"minimumKv":minimum,"records":records}
    base=q([r("low",.1,0,[33]),r("eligible",1,0,[132]),r("far",2,0,[275])])
    return [("baseline",base),("permutation",q(list(reversed(base["records"])))),("threshold-inclusive",q(base["records"],minimum=275)),("threshold-none",q(base["records"],minimum=400)),("empty",q([])),("unknown-voltage",q([r("unknown",.01,0,[]),r("eligible",1,0,[132])])),("tie-first",q([r("east",1,0,[132]),r("west",-1,0,[132])])),("tie-reversed",q([r("west",-1,0,[132]),r("east",1,0,[132])])),("antimeridian",q([r("across",-179.8,0,[132]),r("same",178,0,[132])],179.9)),("north-high-lat",q([r("east",1,80,[132]),r("north",0,81,[132])],0,80)),("coincident-distance-only",q([r("same",0,0,[132]),r("east",1,0,[132])])),("multi-voltage",q([r("multi",.5,0,[33,132]),r("far",2,0,[275])]))]
def runtime(root,obs):
    sys.path.insert(0,str(root));import acceptance as oracle
    for name in ("v9-nearest-search.js","v9-geodesy.js","voltage-drop.js"):
        need(blob((root/name).read_bytes())==PINS[name],"SOURCE_PIN:"+name)
    previous=artifact(root,"previous")
    need(previous["counts"]=={"PASS":9,"FAIL":0,"OPEN":1},"PRIOR_REGRESSION_LOST")
    need(any(o["case"]=="eligible-but-not-nearest" and o["result"]=="OPEN" for o in previous["observations"]),"PRIOR_FALSIFIER_LOST")
    cases=fixtures()
    runner=root/"rank-witness.mjs"
    runner.write_text("""import {index} from './v9-nearest-search.js';
import fs from 'node:fs';
const rows=JSON.parse(fs.readFileSync(0,'utf8'));
const map=x=>({id:x.point.id,distance_km:x.km});
const out=rows.map(q=>{const ix=index(q.records.map(r=>({...r,location:{lon:r.location.longitude,lat:r.location.latitude}})));const a=ix.nearest(q.query.longitude,q.query.latitude,{minimumKv:q.minimumKv,limit:1});const all=ix.nearest(q.query.longitude,q.query.latitude,{minimumKv:q.minimumKv,limit:Math.max(2,q.records.length+1)});return {selected:a?map(a):null,ranking:all.map(map)}});
process.stdout.write(JSON.stringify(out));
""")
    (root/"package.json").write_text('{"type":"module"}')
    actual=json.loads(subprocess.check_output(["node",str(runner)],input=canonical([q for _,q in cases]),timeout=30))
    for (label,q),out in zip(cases,actual,strict=True):
        expected=expected_rank(oracle,q)
        need([x["id"] for x in out["ranking"]]==[x["id"] for x in expected],"RANK:"+label)
        need(all(abs(x["distance_km"]-y["distance_km"])<=1e-8 for x,y in zip(out["ranking"],expected,strict=True)),"DISTANCE:"+label)
        need(out["selected"]==(out["ranking"][0] if expected else None),"FIRST:"+label)
        obs.append({"case":label,"result":"PASS","witness":"actual pinned producer index().nearest() compared with independent vector oracle","input_sha256":sha(canonical(q)),"actual":out,"reference":expected})
    need(actual[0]["selected"]["id"]=="eligible" and actual[0]["ranking"][1]["id"]=="far","FAR_FALSIFIER")
    need(actual[6]["selected"]["id"]=="east" and actual[7]["selected"]["id"]=="west","TIE_ORDER")
    obs.append({"case":"farther-eligible-original-falsifier","result":"OPEN","reason":"Pinned producer ranks eligible before far; previous B adapter accepts far. No new B ranking receipt acquired yet.","previous_receipt_sha256":ARTIFACTS["previous"][2]})
    obs.append({"case":"runtime-admission","result":"OPEN","reason":"Direct source witness only; no package admission or redistribution."})
def identities(root,obs):
    for name in ("table.json","catalogue.json","v9-geodesy.js","v9-nearest-search.js","voltage-drop.js"):
        need(blob((root/name).read_bytes())==PINS[name],"SOURCE_PIN:"+name)
    a=artifact(root,"A");x=artifact(root,"crosswalk");c=artifact(root,"classification")
    table=json.loads((root/"table.json").read_bytes());cat=json.loads((root/"catalogue.json").read_bytes())
    by={r["meaning_id"]:r for r in a["entries"]};cross={r["meaning_id"]:r for r in x["entries"]};classed={r["meaning_id"]:r for r in c["entries"]}
    need(set(by)==set(cross)==set(classed) and len(by)==8,"CENSUS")
    db=root/"modular.sqlite";hash_before=sha_file(db)
    need(hash_before==x["snapshot"]["database_sha256"],"ACTUAL_DB_PIN")
    with sqlite3.connect(db.resolve().as_uri()+"?mode=ro&immutable=1",uri=True) as conn:
        conn.execute("PRAGMA query_only=ON")
        for mid,r in by.items():
            s=r["source"];cx=cross[mid];cl=classed[mid]
            need({k:cx["source"][k] for k in s}==s and cl["source"]==cx["source"] and cl["kuiper"]==cx["kuiper"]==r["kuiper"],"IDENTITY_JOIN:"+mid)
            exact=conn.execute("SELECT o.tablet,t.git_blob FROM occurrence o JOIN tablet t ON t.n=o.tablet WHERE o.repo=? AND o.commit_sha=? AND o.path=?",(s["repo"],s["commit"],s["path"])).fetchall()
            need(exact==[] and cx["current_stars"]["tablet_id"] is None and cx["current_stars"]["element_id"] is None and cx["periodic"]["number"] is None,"STARS_ABSENCE:"+mid)
            scans=conn.execute("SELECT repo,commit_sha,issue FROM scan WHERE lower(repo)=lower(?) ORDER BY repo,commit_sha",(s["repo"],)).fetchall()
            same=conn.execute("SELECT n FROM tablet WHERE git_blob=?",(s["blob"],)).fetchall()
            same_occ=conn.execute("SELECT o.repo,o.commit_sha,o.path FROM occurrence o JOIN tablet t ON t.n=o.tablet WHERE t.git_blob=? ORDER BY o.repo,o.commit_sha,o.path LIMIT 10",(s["blob"],)).fetchall()
            mod=[e for e in table["elements"] if e["key"]=="engine:"+s["path"]]
            need(len(mod)==1,"MODULE_KEY:"+mid);e=mod[0]
            m=cl["module_classification"];category=cat["engine_categories"][e["name"]]
            need((m["number"],m["symbol"],m["category"],m["table_identity"],m["key"])==(e["number"],e["symbol"],category,e["identity"],e["key"]),"CLASSIFICATION:"+mid)
            need(cl["exact_function_family_membership"]["number"] is None and cl["admission"]=="REFUSED_REVIEW_PENDING","NO_PROMOTION")
            obs.append({"case":mid,"result":"PASS","kuiper":r["kuiper"]["key"],"module":{"number":e["number"],"symbol":e["symbol"],"category":category},"exact_function_occurrence":None,"diagnostic":{"exact_revision_scanned":any(y[1]==s["commit"] for y in scans),"repo_scan_rows":scans,"same_blob_tablet_count":len(same),"same_blob_other_occurrences":same_occ}})
    need(sha_file(db)==hash_before,"DB_MUTATED")
    obs.append({"case":"exact-function-identity","result":"OPEN","reason":"No matching repo/commit/path occurrence in exact producer DB; no module-classification promotion."})
def sha_file(p):
    import hashlib
    with p.open("rb") as f:return hashlib.file_digest(f,"sha256").hexdigest()
def main():
    mode,root,out=sys.argv[1],Path(sys.argv[2]),Path(sys.argv[3]);obs=[]
    try:{"runtime":runtime,"identities":identities}[mode](root,obs)
    except Exception as e:obs.append({"case":"fifth-turn-"+mode,"result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(o["result"]==k for o in obs) for k in ("PASS","FAIL","OPEN")}
    report={"schema":"vedic.tacit-c.fifth-turn-witness.v1","mode":mode,"observations":obs,"counts":counts,"producer_pins":PINS,"artifact_pins":ARTIFACTS,"formal_admission":False,"redistribution":"BLOCKED","scope":"independent bounded producer witness, not peer runtime acceptance"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(report))
    print(json.dumps({"mode":mode,"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for o in obs:print(json.dumps(o))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
