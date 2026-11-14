#!/usr/bin/env python3
"""Local dry run of .github/workflows/repd-monthly.yml: executes the YAML's own `run:` blocks in order.

`uses:` steps are emulated (checkout = git clone of a local bare "origin" at main; upload/download
artifact = copy of the listed paths). Two substitutions only, both printed:
  * the monthly.py call gets --api-file/--files-dir (offline: GOV.UK unreachable here);
  * `git push` and `gh pr create` are replaced by stubs that record what would be pushed/opened.
Usage: dryrun_workflow.py <workflow.yml> <repo dir to serve as main> <api json> <files dir> <work dir> [release_folder]
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

wf_path, repo, api, files, work = map(lambda p: Path(p).resolve(), sys.argv[1:6])
folder = sys.argv[6] if len(sys.argv) > 6 else ""
wf = yaml.safe_load(wf_path.read_text())
if work.exists():
    shutil.rmtree(work)
work.mkdir(parents=True)
for p in ("/tmp/repd-monthly", "/tmp/repd-monthly-artifact"):
    shutil.rmtree(p, ignore_errors=True)

origin = work / "origin.git"
subprocess.run(["git", "init", "-q", "-b", "main", str(work / "seed")], check=True)
shutil.copytree(repo, work / "seed", dirs_exist_ok=True)
git_id = ["-c", "user.name=dryrun", "-c", "user.email=dryrun@localhost"]
subprocess.run(["git", "-C", str(work / "seed"), "add", "-A"], check=True)
subprocess.run(["git", *git_id, "-C", str(work / "seed"), "commit", "-qm", "main"], check=True)
subprocess.run(["git", "clone", "-q", "--bare", str(work / "seed"), str(origin)], check=True)

stub = work / "stubbin"
stub.mkdir()
(stub / "gh").write_text('#!/bin/bash\necho "STUB gh $*"; for ((i=1;i<=$#;i++)); do [[ "${!i}" == --body-file ]] && j=$((i+1)) && cp "${!j}" "$DRYRUN_WORK/pr_body.md"; done; echo "$*" > "$DRYRUN_WORK/gh_args.txt"\n')
(stub / "gh").chmod(0o755)


def run_job(name, outputs_in, inputs):
    job = wf["jobs"][name]
    ws = work / f"ws-{name}"
    subprocess.run(["git", "clone", "-q", "-b", "main", str(origin), str(ws)], check=True)
    gh_out, summary = work / f"{name}.GITHUB_OUTPUT", work / f"{name}.STEP_SUMMARY"
    gh_out.touch(); summary.touch()
    step_outputs = {}

    def expr(s):
        if not isinstance(s, str):
            return s
        s = s.replace("${{ inputs.release_folder }}", inputs.get("release_folder", ""))
        s = s.replace("${{ github.token }}", "dummy").replace("${{ github.run_number }}", "1")
        for k, v in outputs_in.items():
            s = s.replace("${{ needs.check.outputs.%s }}" % k, v)
        for sid, outs in step_outputs.items():
            for k, v in outs.items():
                s = s.replace("${{ steps.%s.outputs.%s }}" % (sid, k), v)
        return s

    env = dict(os.environ, GITHUB_OUTPUT=str(gh_out), GITHUB_STEP_SUMMARY=str(summary), GITHUB_RUN_ID="0",
               GITHUB_SERVER_URL="https://github.com", GITHUB_REPOSITORY="OWNER/REPO", RUNNER_TEMP=str(work / "tmp"),
               DRYRUN_WORK=str(work), PATH=f"{stub}:{os.environ['PATH']}")
    (work / "tmp").mkdir(exist_ok=True)
    env.update({k: expr(str(v)) for k, v in (job.get("env") or {}).items()})
    for step in job["steps"]:
        sid, title = step.get("id"), step.get("name")
        cond = step.get("if")
        if cond:
            c = cond
            for sid2, outs in step_outputs.items():
                for k, v in outs.items():
                    c = c.replace(f"steps.{sid2}.outputs.{k}", repr(v))
            c = c.replace("always() && ", "").replace("==", "==").replace("!=", "!=")
            import re
            c = re.sub(r"steps\.\w+\.outputs\.\w+", "''", c)
            if not eval(c):  # noqa: S307 - our own YAML, simple comparisons only
                print(f"[{name}] SKIP  {title}  (if: {cond})")
                continue
        if "uses" in step:
            u = step["uses"]
            if u.startswith("actions/upload-artifact"):
                dest = work / "artifact"
                for p in step["with"]["path"].split():
                    p = Path(p)
                    if p.exists():
                        rel = p.relative_to("/tmp/repd-monthly")
                        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
                        (shutil.copytree if p.is_dir() else shutil.copy2)(p, dest / rel)
            elif u.startswith("actions/download-artifact"):
                shutil.copytree(work / "artifact", env["ART"])
            print(f"[{name}] EMUL  {title}  ({u})")
            continue
        script = expr(step["run"])
        script = script.replace('python -m automation.repd.monthly "${args[@]}"',
                                f'python -m automation.repd.monthly "${{args[@]}}" --api-file {api} --files-dir {files}')
        script = script.replace('git push origin "HEAD:refs/heads/$BRANCH"',
                                'echo "WOULD PUSH $(git rev-parse HEAD) to refs/heads/$BRANCH"; '
                                'git diff --name-status HEAD~1 HEAD > "$DRYRUN_WORK/commit_files.txt"')
        step_env = dict(env)
        step_env.update({k: expr(str(v)) for k, v in (step.get("env") or {}).items()})
        before = gh_out.read_text()
        print(f"[{name}] RUN   {title}")
        proc = subprocess.run(["bash", "-e", "-c", script] if "set -" not in script else ["bash", "-c", script],
                              cwd=ws, env=step_env, capture_output=True, text=True)
        tail = (proc.stdout + proc.stderr).strip().splitlines()[-6:]
        for line in tail:
            print(f"        | {line[:220]}")
        new = gh_out.read_text()[len(before):]
        if sid:
            step_outputs[sid] = dict(l.split("=", 1) for l in new.splitlines() if "=" in l)
            print(f"        outputs: {step_outputs[sid]}")
        if proc.returncode != 0:
            print(f"[{name}] FAILED step {title!r} exit {proc.returncode}")
            return step_outputs, False
    return step_outputs, True


outs, ok = run_job("check", {}, {"release_folder": folder})
job_out = {"status": outs.get("check", {}).get("status", ""), "release_id": outs.get("check", {}).get("release_id", ""),
           "overall": outs.get("build", {}).get("overall", "")}
print(f"check job: {'green' if ok else 'RED'}; outputs {job_out}")
if ok and job_out["status"] == "new" and job_out["overall"] == "ok":
    _, ok2 = run_job("open-pr", job_out, {})
    print(f"open-pr job: {'green' if ok2 else 'RED'}")
else:
    print("open-pr job: SKIPPED (if: status == 'new' && overall == 'ok')")
