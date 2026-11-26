"""Bounded, read-only NL-087 snapshot; no code execution from API responses."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
import re
import sys
import unittest
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

REPO = "Ventusltd/vedic-"
BASE = "0ee52af60036f32358759a67836578dce6d7da51"
SCOPE = "646c3d324ca07e400ea3d4127e6f63cd8abecbf7"
BRANCHES = {
    "1b": "agent/tacit1b-package-factory-20261126",
    "2b": "agent/tacit2b-electrical-package-20261126",
    "3b": "agent/tacit3b-geospatial-package-20261126",
    "4b": "agent/tacit4b-project-model-package-20261126",
    "5b": "agent/tacit5b-standalone-consumer-20261126",
}
SHA = re.compile(r"^[0-9a-f]{40}$")


def api(path, **query):
    url = "https://api.github.com/repos/" + REPO + "/" + path
    if query:
        url += "?" + urlencode(query)
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "User-Agent": "tacit7bt-readonly-snapshot"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    with urlopen(Request(url, headers=headers), timeout=15) as response:
        raw = response.read(5_000_001)
    if len(raw) > 5_000_000:
        raise ValueError("response exceeds fixed bound")
    return json.loads(raw)


def branch_sha(branch):
    value = api("git/ref/heads/" + quote(branch, safe="/"))["object"]["sha"]
    if not SHA.fullmatch(value):
        raise ValueError("invalid commit SHA")
    return value


def exact_runs(runs, head, branch):
    """Preserve only exact-head and exact-branch run evidence; never infer gates."""
    result = []
    for run in runs:
        if run.get("head_sha") != head or run.get("head_branch") != branch:
            continue
        result.append({k: run.get(k) for k in
                       ("id", "name", "status", "conclusion", "run_attempt", "event")})
    return sorted(result, key=lambda r: r["id"], reverse=True)


def classify(head, changed_during_read, runs, truncated):
    if changed_during_read or truncated:
        return "PARTIAL_SNAPSHOT"
    if head == BASE:
        return "BASELINE_ONLY"
    if not runs:
        return "COMMITTED_CI_NOT_OBSERVED"
    if any(r["status"] == "completed" and r["conclusion"] not in ("success",)
           for r in runs):
        return "NON_SUCCESS_RUN_OBSERVED"
    if any(r["status"] != "completed" for r in runs):
        return "CI_PENDING"
    if all(r["conclusion"] == "success" for r in runs):
        return "OBSERVED_RUNS_SUCCESS"
    return "CI_UNKNOWN"


def snapshot(agent, branch):
    result = {"agent": agent, "branch": branch, "head": None,
              "pull_requests": [], "runs": [], "state": "UNKNOWN",
              "independent_acceptance": "NOT_ASSESSED",
              "publication": "NOT_ASSESSED"}
    try:
        head = branch_sha(branch)
        result["head"] = head
        prs = api("pulls", state="open", head="Ventusltd:" + branch, per_page=100)
        result["pull_requests"] = [
            {"number": p["number"], "draft": p.get("draft"),
             "head": p["head"]["sha"], "exact_head": p["head"]["sha"] == head}
            for p in prs if p.get("head", {}).get("ref") == branch
            and p.get("head", {}).get("repo", {}).get("full_name") == REPO]
        payload = api("actions/runs", branch=branch, head_sha=head, per_page=100)
        rows = payload["workflow_runs"]
        result["runs"] = exact_runs(rows, head, branch)
        truncated = len(prs) >= 100 or payload.get("total_count", len(rows)) > len(rows)
        result["head_after_read"] = branch_sha(branch)
        result["state"] = classify(head, result["head_after_read"] != head,
                                   result["runs"], truncated)
        result["truncated"] = truncated
    except HTTPError as exc:
        result["error"] = "HTTP " + str(exc.code)
    except Exception as exc:
        # No API response, secrets, URL query or arbitrary exception message.
        result["error"] = type(exc).__name__
    return result


class Contracts(unittest.TestCase):
    def test_baseline(self):
        self.assertEqual(classify(BASE, False, [], False), "BASELINE_ONLY")

    def test_unknown(self):
        self.assertEqual(classify("a"*40, False, [], False), "COMMITTED_CI_NOT_OBSERVED")

    def test_pending(self):
        self.assertEqual(classify("a"*40, False, [{"status":"queued","conclusion":None}], False),
                         "CI_PENDING")

    def test_not_pass(self):
        for conclusion in ("failure", "cancelled", "skipped", "neutral", None):
            self.assertEqual(classify("a"*40, False, [{"status":"completed",
                             "conclusion":conclusion}], False), "NON_SUCCESS_RUN_OBSERVED")

    def test_success_not_acceptance(self):
        self.assertEqual(classify("a"*40, False, [{"status":"completed",
                         "conclusion":"success"}], False), "OBSERVED_RUNS_SUCCESS")

    def test_moved(self):
        self.assertEqual(classify("a"*40, True, [], False), "PARTIAL_SNAPSHOT")

    def test_truncated(self):
        self.assertEqual(classify("a"*40, False, [], True), "PARTIAL_SNAPSHOT")

    def test_wrong_head_or_branch_excluded(self):
        rows = [{"id":1,"head_sha":"a"*40,"head_branch":"right"},
                {"id":2,"head_sha":"b"*40,"head_branch":"right"},
                {"id":3,"head_sha":"a"*40,"head_branch":"wrong"}]
        self.assertEqual([r["id"] for r in exact_runs(rows,"a"*40,"right")], [1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        unittest.main(argv=[sys.argv[0]])
        return
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(snapshot, a, b) for a, b in BRANCHES.items()]
        agents = [f.result() for f in futures]
    report = {"schema":"tacit.supervisor-snapshot.v1", "repo":REPO,
              "scope_commit":SCOPE, "observed_at_utc":datetime.now(timezone.utc).isoformat(),
              "agents":agents, "limits":["Open pull requests only",
              "Observed exact-head branch runs only; not required-gate completeness",
              "No independent acceptance, licence or publication verdict",
              "A branch can move immediately after observation"]}
    print(json.dumps(report, indent=2, sort_keys=True))
    if any(a["state"] in ("UNKNOWN","PARTIAL_SNAPSHOT") for a in agents):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
