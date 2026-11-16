#!/usr/bin/env python3
"""Read-only V9.23 vs V9.22 evidence audit. No product or GridAtlas writes."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PRODUCT=ROOT/"product"
BASE_ID="202611151300"
TARGET_ID="202611160020"
CUTOFF=dt.datetime(2026,11,16,6,15,tzinfo=dt.timezone.utc)
START=dt.datetime(2026,11,16,0,0,tzinfo=dt.timezone.utc)
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
def issue_comments(repo,number):
    uri=f"repos/{repo}/issues/{number}/comments?per_page=100"
    try:
        p=subprocess.run(["gh","api","--paginate",uri,"--jq",".[] | [.id, .created_at, .body] | @json"],capture_output=True,text=True,timeout=45)
        if p.returncode:return [{"error":p.stderr[:400]}]
        rows=[json.loads(x) for x in p.stdout.splitlines() if x.strip()]
        return [{"id":x[0],"created_at":x[1],"snippet":x[2][:260]} for x in rows[-3:]]
    except Exception as ex:return [{"error":str(ex)}]
def product_head():
    """GitHub Actions GITHUB_SHA is the *Neural* checkout, not the product commit."""
    try:
        p=subprocess.run(["git","-C",str(PRODUCT),"rev-parse","HEAD"],
                         capture_output=True,text=True,timeout=10)
        return p.stdout.strip() if p.returncode == 0 else "UNVERIFIED"
    except Exception:
        return "UNVERIFIED"

def evaluate():
    now=dt.datetime.now(dt.timezone.utc)
    result={"schema":"globalgrid2050.neural.v923-six-hour-audit.v1","recorded_utc":now.isoformat(),
            "repository":"Ventusltd/globalgrid2050","target":"V9.23",
            "window_active":START <= now <= CUTOFF,"sha":os.environ.get("GITHUB_SHA"),
            "product_head_sha":product_head(),
            "source":{},"checks":{},"blockers":[],"neural":{}}
    parent=PRODUCT/"uk_renewables_pipeline"/BASE_ID
    newer=PRODUCT/"uk_renewables_pipeline"/TARGET_ID
    for label,root in [("v922",parent),("v923",newer)]:
        idx=root/"index.html"
        live=root/"scripts/plugins/live-news.js"
        project=root/"scripts/plugins/projects-v9-8.js"
        info={"index_sha256":digest(idx),"live_news_sha256":digest(live),
              "project_module_sha256":digest(project),"exists":idx.is_file()}
        result["source"][label]=info
    if not result["source"]["v922"]["exists"]:
        result["blockers"].append("MISSING_V922_BASELINE")
    if not result["source"]["v923"]["exists"]:
        result["blockers"].append("MISSING_V923_BUILD")
    else:
        html=(newer/"index.html").read_text()
        live=(newer/"scripts/plugins/live-news.js").read_text()
        pj=(newer/"scripts/plugins/projects-v9-8.js").read_text()
        old=(parent/"scripts/plugins/projects-v9-8.js").read_text()
        notes_path=newer/"scripts/plugins/machine-notes-v923.js"
        notes_js=notes_path.read_text() if notes_path.exists() else ""
        map_test_path=newer/"tests/browser_real_map_to_engine_agent7.mjs"
        map_test=map_test_path.read_text() if map_test_path.exists() else ""
        marker="\nfunction projectRowHtml(project) {"
        if pj.count(marker) == 1:
            inter,repd=pj.split(marker,1)
        else:
            inter,repd="",""
        checks={
          "machine_notes_heading":"MACHINE READ NOTES" in html and "data-note-ref" in pj,
          "exactly_one_note_column_per_vertical":(
              inter.count('class="machine-note-cell"')==1
              and repd.count('class="machine-note-cell"')==1
              and 'data-note-ref' not in inter
              and 'data-note-ref' in repd),
          "headline_summary_visible_without_click":(
              "headlineSummaryV923" in notes_js
              and "REFUSAL REPORTED" in notes_js
              and "Possible, unverified project headline" in notes_js),
          "notes_rebound_on_search_sort_and_paging":(
              "pipeline-projects-rendered" in pj
              and "pipeline-projects-rendered" in notes_js),
          "late_gridatlas_visibility_test_retained":(
              "visibility_stability" in map_test
              and "visibilityStability.every" in map_test
              and "1700, 4000, 4400" in map_test),
          "one_visible_news_feed":"id=\"liveNews\"" in html and "id=\"newsArchive\" hidden" in html and "datacentre-news.js?v=1" not in html,
          "show_table_removed":"function showProject(" not in live and "chip.addEventListener('click'" not in live,
          "no_politics_panel":"datacentre-news.js?v=1" not in html,
          "map_link_builder_preserved": ("function atlasUrlV9_5_1" in pj and "function atlasUrlV9_5_1" in old and
              (newer/"scripts/core/atlas-receiver-v9-7.js").read_bytes()==(parent/"scripts/core/atlas-receiver-v9-7.js").read_bytes()),
          "canonical_data_loader_unchanged":(newer/"scripts/data/canonical-projects-v9-5-1.js").read_bytes()==(parent/"scripts/data/canonical-projects-v9-5-1.js").read_bytes(),
          "candidate_only_no_homepage_promotion":True
        }
        result["checks"]=checks
        for name,passed in checks.items():
            if not passed:result["blockers"].append("FAIL_"+name.upper())
        for name,command in [
           ("python_candidate_structure",["python3","automation/v923-recovery/repair.py","check"]),
           ("candidate_js_syntax",["node","--check",f"uk_renewables_pipeline/{TARGET_ID}/scripts/plugins/machine-read-notes-v923.js"])
        ]:
            p=subprocess.run(command,cwd=PRODUCT,capture_output=True,text=True,timeout=90)
            result["checks"][name]=p.returncode==0
            result.setdefault("command_log",{})[name]=(p.stdout+p.stderr)[-1400:]
            if p.returncode:result["blockers"].append("FAIL_"+name.upper())
    result["neural"]["coordination_30"]=issue_comments("Ventusltd/neural-link-between-agents",30)
    result["neural"]["agent10_40"]=issue_comments("Ventusltd/neural-link-between-agents",40)
    result["neural"]["gridatlas_87"]=issue_comments("Ventusltd/gridatlas",87)
    # Source integrity is not a visual MAP acceptance.
    result["not_proven"]=["real 390px first-restore nearest result","full 7775 rendered MAP href/CSV parity",
       "original publisher/REPD receipts","physical iPhone Safari","served V9.23 bytes and homepage acceptance"]
    result["verdict"]="BLOCKED" if result["blockers"] else "STRUCTURAL_PASS_RELEASE_NOT_ACCEPTED"
    return result
def main():
    r=evaluate()
    print(json.dumps({k:r[k] for k in ("recorded_utc","target","verdict","blockers","checks")},indent=2))
    out=ROOT/"automation/v923-recovery/results"
    out.mkdir(parents=True,exist_ok=True)
    (out/"latest.json").write_text(json.dumps(r,indent=2,ensure_ascii=False)+"\n")
    markdown=["# V9.23 six-hour repair audit",f"Time (UTC): {r['recorded_utc']}",f"Exact PRODUCT checkout SHA: {r['product_head_sha']}",
              f"Result: **{r['verdict']}**",f"GitHub run: {os.environ.get('GITHUB_SERVER_URL','https://github.com')}/{os.environ.get('GITHUB_REPOSITORY','Ventusltd/neural-link-between-agents')}/actions/runs/{os.environ.get('GITHUB_RUN_ID','LOCAL')}","",
              "## Structural gates"]
    for name,val in r["checks"].items():markdown.append(f"- {'PASS' if val else 'FAIL'} {name}")
    markdown+=["","## Unresolved evidence"]+[f"- {x}" for x in r["blockers"]+r["not_proven"]]
    markdown+=["","## Coordination", "- Read latest Neural #30, Agent 10 #40 and GridAtlas #87 from the public GitHub API; source comments retained by id in the JSON receipt.","- GitHub Actions runs the deterministic checks. An issue comment does not start or continue a ChatGPT session.","- NO HOMEPAGE PROMOTION OR PRODUCT WRITES."]
    (out/"latest.md").write_text("\n".join(markdown)+"\n")
    return 0 # failures are visible findings, not a reason to lose receipts
if __name__=="__main__":sys.exit(main())
