"""Turn 8 independent review of actual A repair and B candidate, on disposable inputs."""
import ast,copy,json,sqlite3,sys,subprocess,zipfile
from pathlib import Path
from tacit_c_verify import sha,blob,canonical,need,DESCRIPTOR
from tacit_c_seventh import member
A_HEAD="98d1c4580f307c6db40d511ab8d86f1ec692aaa1"
B_HEAD="e273402c75e99438b31b37c9a2ff73a24c0f7fe0"
AP=("f2a66617149a4b51e95dbdc908dd78ea9ff5db94e9946e259ad297888d46d04f","repair.json","e76464f5f4c70f25cf24b42ffa2ac199d5b8b3eced4189484fe5af159b1a211c")
BP=("c3e60f000426ea09d3f012a2ff9bc808ec1cbc0da601751f95f00d283ec157a2","tacit-b-admission.json","79ca2bf68b94c2c06c4d21063cc1a4acd4442acc43bb9630f8cd32a7d01daa2a")
def pinned(path,pins):
    zpin,name,pin=pins
    need(sha(path.read_bytes())==zpin,"ZIP_PIN")
    with zipfile.ZipFile(path) as z:
        hits=[i for i in z.infolist() if i.filename==name or i.filename.endswith("/"+name)]
        need(len(hits)==1 and hits[0].file_size<=2_000_000,"MEMBER")
        raw=z.read(hits[0])
    need(sha(raw)==pin,"MEMBER_PIN")
    return raw
def verify_a(root,obs):
    raw=pinned(root/"A-repair.zip",AP);r=json.loads(raw)
    need((root/"a-first.json").read_bytes()==(root/"a-second.json").read_bytes()==raw,"A_REPLAY_BYTES")
    obs.append({"case":"actual-A-repair-CLI-repeat","result":"PASS","checks_replayed":len(r["tests"]),"receipt_sha256":sha(raw)})
    src=root/"repair";db=src/"modular.sqlite";snapshot=json.loads((src/"snapshot.json").read_bytes())
    from tacit_c_fifth import sha_file
    before=sha_file(db)
    need(before==snapshot["database_sha256"]==r["producer_snapshot"]["database_sha256"],"A_DB_PIN")
    need(r["namespace_restored"] and r["permanent_allocations"]==0 and r["mode"]=="DISPOSABLE_TRANSACTION_ROLLED_BACK","NO_ALLOCATION")
    need(r["temporary_count_delta"]=={"line":0,"tablet":0,"element":0,"family":0,"tablet_element":0,"occurrence":3,"scan":0,"commit_info":0},"TEMPORARY_DELTAS")
    target=r["source_commit"];parent=r["source_parent"];repo=r["source_repo"]
    def git(*args):return subprocess.check_output(["git","-C",str(src/"git"),*args],text=True,timeout=30).strip()
    need(git("rev-parse",target+"^")==parent,"PARENT")
    counts={}
    with sqlite3.connect(db.resolve().as_uri()+"?mode=ro&immutable=1",uri=True) as conn:
        conn.execute("PRAGMA query_only=ON")
        need(conn.execute("SELECT count(*) FROM commit_info WHERE repo=? AND sha=?",(repo,target)).fetchone()[0]==0,"HISTORICAL_REVISION_PRESENT")
        for tab,v in r["namespace_before"].items():
            need(tab in ("line","tablet","element","family","tablet_element","occurrence","scan","commit_info"),"TABLE")
            need(conn.execute("SELECT count(*) FROM "+tab).fetchone()[0]==v,"NAMESPACE:"+tab)
        parser=json.loads((src/"producer-ast.json").read_bytes())
        for item in r["files"]:
            s=item["input"];path=s["path"];b=(src/Path(path).name).read_bytes()
            need(s["commit"]==target and s["parent"]==parent and s["repo"]==repo and blob(b)==s["blob"]==git("rev-parse",target+":"+path)==git("rev-parse",parent+":"+path),"GIT_OCCURRENCE")
            exact=conn.execute("SELECT tablet FROM occurrence WHERE repo=? AND commit_sha=? AND path=?",(repo,target,path)).fetchall()
            need(not exact,"EXACT_OCCURRENCE_ALREADY_PRESENT")
            tablet=conn.execute("SELECT n FROM tablet WHERE git_blob=?",(s["blob"],)).fetchall()
            need(len(tablet)==1,"CONTENT_TABLET")
            num=conn.execute("SELECT count(*) FROM tablet_element WHERE tablet=?",(tablet[0][0],)).fetchone()[0]
            fs=parser[path]["functions"]
            need(num==item["temporary_indexed_element_count"] and len(fs)==item["original_parser_callable_count"],"PARSER_COUNT")
            counts[path]=len(fs)
            obs.append({"case":"exact-missing-path:"+path,"result":"PASS","parser_callable_count":len(fs),"existing_tablet_element_count":num})
        need(sum(counts.values())==16 and len(r["rows"])==8,"COHORT")
        for i,row in enumerate(r["rows"]):
            s=row["source"];p=row["producer_ast"]
            match=conn.execute("SELECT count(*) FROM tablet_element te JOIN tablet t ON te.tablet=t.n WHERE t.git_blob=? AND te.first=? AND te.last=? AND te.col0=? AND te.col1=? AND te.name=?",(s["blob"],s["first"],s["last"],p["col0"],p["col1"],p["name"])).fetchone()[0]
            need(match==1==row["temporary_ast_match_count"] and row["exact_occurrence_status"]=="MISSING_IN_PINNED_PRODUCER" and row["permanent_ids_allocated"] is False,"EXACT_AST_SPAN")
            wrong=conn.execute("SELECT count(*) FROM tablet_element te JOIN tablet t ON te.tablet=t.n WHERE t.git_blob=? AND te.first=? AND te.last=? AND te.col0=? AND te.col1=? AND te.name=?",(s["blob"],s["first"],s["last"],p["col0"]+1,p["col1"],p["name"])).fetchone()[0]
            need(wrong==0,"STALE_AST_OFFSET")
            obs.append({"case":"exact-tablet-AST-"+str(i),"result":"PASS","temporary_join_match_count":match,"exact_historical_membership":"MISSING"})
    need(sha_file(db)==before,"ORIGINAL_DB_MUTATION")
    obs.append({"case":"namespace-conserved","result":"PASS","temporary_occurrence_delta":3,"permanent_allocations":0,"original_db_unchanged":True})
    obs.append({"case":"production-occurrence-repair","result":"OPEN","reason":"Owner-authorised original producer ingest of exactly three tuples plus new immutable readback required; do not mark revision fully scanned."})
def verify_b(root,obs):
    raw=pinned(root/"B-admission.zip",BP);report=json.loads(raw)
    froot=root/"factory";peer=root/"peer-b";sys.path[:0]=[str(froot/"tools"),str(peer/"tools")]
    import package_factory as f
    import tacit_b_admission as b
    for path,pin in (("tacit_b_admission.py","0100840db47f006b748064a84f46a4a1b628afae"),("tacit_b_stage_factory.py","fbde3fd2f80448cb796a3b19c66337b4571b1014")):
        need(blob((peer/"tools"/path).read_bytes())==pin,"B_PIN")
    orig=(root/"factory-original.py").read_bytes()
    need(blob(orig)=="23247de65fde04a400bb30874fc7e81cca4b7ebe","FACTORY_ORIGINAL")
    def funcs(raw):return {node.name:ast.dump(node,include_attributes=False) for node in ast.parse(raw).body if isinstance(node,ast.FunctionDef)}
    before=funcs(orig);after=funcs((froot/"tools/package_factory.py").read_bytes())
    need(all(before[x]==after[x] for x in ("admit","validate","assemble","electrical_adapter","nearest_adapter","build")),"FACTORY_GATE_MUTATED")
    need(set(f.ADMISSIONS)=={"orient"} and f.REVIEWED_RECEIPTS=={},"REGISTRY")
    obs.append({"case":"actual-factory-authority-preserved","result":"PASS"})
    cmd=[sys.executable,str(peer/"tools/tacit_b_admission.py"),"--factory",str(froot),"--a",str(root/"A-original.zip"),"--c",str(root/"C-source.zip"),"--nearest",str(root/"nearest"),"--electrical",str(root/"electrical")]
    for name in ("b-first.json","b-second.json"):
        subprocess.run(cmd+["--out",str(root/name)],check=True,timeout=30)
        need((root/name).read_bytes()==raw,"B_CANDIDATE_REPLAY_BYTES")
    obs.append({"case":"actual-B-admission-CLI-repeat","result":"PASS","receipt_sha256":sha(raw)})
    review=b.member(f,root/"C-source.zip",b.C,"a-review.json",b.C_JSON)
    def refuse(label,fn,reason):
        try:fn()
        except (ValueError,TypeError) as e:
            need(str(e)==reason,"WRONG_REFUSAL:"+label+":"+str(e))
            obs.append({"case":label,"result":"PASS","refusal":str(e)})
        else:raise ValueError("UNEXPECTED_ACCEPT:"+label)
    for family,(sd,cd) in b.PINS.items():
        short="nearest" if family=="nearest-substation" else family
        sr=b.member(f,root/"A-original.zip",b.A,"family-review/"+short+"-source.json",sd)
        cl=b.member(f,root/"A-original.zip",b.A,"family-review/"+short+"-closure.json",cd)
        d=f.strict(f.PENDING[family].read_bytes())
        inp=root/short
        mods={x["path"]:(inp/x["filename"]).read_bytes() for x in d["inputs"] if x["role"] in ("module","local_dependency")}
        def call(ds=d,s=sr,c=cl,rv=review,m=mods):return b.candidate(f,family,ds,s,c,rv,m)
        row=call();need(row==report["families"][family] and row["archive"] is None and row["rights"]=="BLOCKED","CANDIDATE_ROW")
        desc=row["descriptor"];need(f.sha(f.canonical(f.validate(desc)))==row["descriptor_sha256"],"VALIDATOR")
        obs.append({"case":family+"-exact-reviewed-candidate","result":"PASS","descriptor_sha256":row["descriptor_sha256"],"formal_gate":row["formal_gate"],"review_gate":row["formal_review_gate"]})
        forged=f.strict(review);forged.update(formal_factory_admission=True,publication=True,owner_approval="APPROVED")
        refuse(family+"-rehashed-false-review",lambda:call(rv=f.canonical(forged)),"INDEPENDENT_REVIEW_PIN")
        other="nearest" if short=="electrical" else "electrical";op="nearest-substation" if other=="nearest" else other
        other_src=b.member(f,root/"A-original.zip",b.A,"family-review/"+other+"-source.json",b.PINS[op][0])
        refuse(family+"-valid-wrong-family-source",lambda:call(s=other_src),"RECEIPT_DIGEST")
        other_cl=b.member(f,root/"A-original.zip",b.A,"family-review/"+other+"-closure.json",b.PINS[op][1])
        refuse(family+"-valid-wrong-family-closure",lambda:call(c=other_cl),"CLOSURE_DIGEST")
        for label,mut in (("stale-descriptor",lambda x:x.update(version="9.9.9")),("different-occurrence",lambda x:x["inputs"][0].update(commit="0"*40)),("embedded-owner-approval",lambda x:x.update(owner_approval=True)),("wrong-units",lambda x:x["ports"]["input"].update(forged="km")),("rights-escalation",lambda x:x.update(licence="CLEARED"))):
            x=copy.deepcopy(d);mut(x);refuse(family+"-"+label,lambda:call(ds=x),"PENDING_DESCRIPTOR_PIN")
        m=dict(mods);key=next(iter(m));m[key]+=b" ";refuse(family+"-changed-module",lambda:call(m=m),"MODULE_PIN")
        refuse(family+"-actual-assembly-gate",lambda:f.assemble(desc,inp),row["formal_gate"])
        refuse(family+"-actual-registry-gate",lambda:f.review_receipt(family,sr,mods,cl),"REVIEWED_RECEIPT_NOT_PINNED")
        obs.append({"case":family+"-formal-admission","result":"OPEN","reason":"Candidate artifact member locator is not a Git tree file. Owner must approve exact family registration/handler and artifact acquisition pin; runtime closure and redistribution remain separate."})
    need(set(f.ADMISSIONS)=={"orient"} and f.REVIEWED_RECEIPTS=={} and f.sha(f.canonical(f.strict(f.ADMISSIONS["orient"].read_bytes())))==DESCRIPTOR,"REGISTRY_CHANGED")
def main():
    mode,root,out=sys.argv[1],Path(sys.argv[2]),Path(sys.argv[3]);obs=[]
    try:{"identity":verify_a,"gate":verify_b}[mode](root,obs)
    except Exception as e:obs.append({"case":mode+"-review","result":"FAIL","reason":type(e).__name__+":"+str(e)})
    counts={k:sum(o["result"]==k for o in obs) for k in ("PASS","FAIL","OPEN")}
    result={"schema":"vedic.tacit-c.eighth-peer-review.v1","mode":mode,"A_head":A_HEAD,"B_head":B_HEAD,"A_pins":AP,"B_pins":BP,"observations":obs,"counts":counts,"formal_admission":False,"permanent_allocations":0,"redistribution":"BLOCKED"}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(canonical(result));print(json.dumps({"counts":counts,"receipt_sha256":sha(out.read_bytes())}))
    for o in obs:print(json.dumps(o))
    return int(bool(counts["FAIL"]))
if __name__=="__main__":raise SystemExit(main())
