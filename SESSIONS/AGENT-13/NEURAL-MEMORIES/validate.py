"""Validate this declared build handoff. No network, Git writes or command execution."""
import json
from pathlib import Path
import re
import sys


SHA = re.compile(r"[0-9a-f]{40}\Z")
DIGEST = re.compile(r"[0-9a-f]{64}\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def acyclic(rows, key, dependencies):
    nodes = {row[key]: row for row in rows}
    require(len(nodes) == len(rows), f"duplicate {key}")
    active, done, ordered = set(), set(), []

    def visit(name):
        require(name in nodes, f"missing dependency: {name}")
        require(name not in active, f"dependency cycle: {name}")
        if name in done:
            return
        active.add(name)
        for child in nodes[name][dependencies]:
            visit(child)
        active.remove(name)
        done.add(name)
        ordered.append(name)

    for name in nodes:
        visit(name)
    return ordered


def check_ci(row):
    ci = row["ci"]
    require(ci["status"] in {"observed_pass", "pending", "failed"}, "unknown CI status")
    if ci["status"] == "observed_pass":
        require(bool(SHA.fullmatch(row["head"] or "")), "CI has no exact head")
        require(ci["tested_head"] == row["head"], "stale CI head")
        require(bool(ci["urls"]), "passing CI has no receipt")
    for url in ci["urls"]:
        require(url.startswith("https://github.com/") and "/actions/runs/" in url, "invalid CI receipt URL")


def validate(doc):
    require(doc["schema"] == "globalgrid2050.neural-build-ledger.v1", "unknown ledger schema")
    require(doc["coverage"]["complete_transcript"] is False, "transcript completeness is not measured")
    inv = doc["invariants"]
    require((inv["repd_records"], inv["solar_records"], inv["solar1000_count"]) == (7775, 3604, 1000), "baseline counts changed")
    require(inv["automatic_verified"] is False, "machine verification forbidden")
    require(inv["critical_evidence_failure_blocks_publication"] is True, "critical source/schema gate removed")
    require(bool(DIGEST.fullmatch(inv["solar1000_sha256"])), "missing pilot digest")
    require(bool(SHA.fullmatch(doc["protocol_sources"]["commit"])), "protocol source is not pinned")

    components = doc["components"]
    require(bool(components), "empty component inventory")
    ordered = acyclic(components, "id", "code_requires")
    for row in components:
        require(bool(row["authored_commits"]), "component lacks authored commits")
        require(len(set(row["authored_commits"])) == len(row["authored_commits"]), "duplicate authored commit")
        for sha in row["authored_commits"] + row["integrated_as"]:
            require(bool(SHA.fullmatch(sha)), "short or invalid source commit")
        require(bool(row["owned_paths"]), "component lacks file scope")
        for path in row["owned_paths"]:
            require(not path.startswith(("/", "\\")) and ".." not in path.split("/") and ":" not in path, "non-relative file scope")
        require(row["checks"]["status"] in {"reported_pass", "observed_pass", "pending", "failed", "unavailable"}, "unknown component check status")
        require(row["checks"]["evidence_url"].startswith("https://github.com/"), "missing handoff evidence")
        if row["integration"] == "transplant_required":
            require(row["next_action"]["kind"] == "transplant", "old release delta must be transplanted")
            require(not (row["next_action"]["command"] or "").startswith("git cherry-pick"), "unsafe historical-path cherry-pick")
        if row["integration"] == "candidate_integrated":
            require(bool(row["integrated_as"]), "integrated component lacks resulting commit")

    milestones = doc["milestones"]
    acyclic(milestones, "version", "requires_release")
    ids = set(ordered)
    count = 0
    for row in milestones:
        require(set(row["components"]) <= ids, "milestone references missing component")
        check_ci(row)
        require(type(row["published"]) is bool, "published must be boolean")
        if row["published"]:
            require(row["ci"]["status"] == "observed_pass", "publication lacks passing exact-head CI")
            require(bool(row["public_receipts"]), "publication lacks public receipt")
            for receipt in row["public_receipts"]:
                require(receipt["url"].startswith("https://"), "public URL must be HTTPS")
                require(bool(SHA.fullmatch(receipt["deployment_sha"])), "missing deployed commit")
                require(bool(DIGEST.fullmatch(receipt["html_sha256"])), "missing served-byte digest")
                require(receipt["browser_receipt_url"].startswith("https://"), "missing actual browser receipt")
            count += 1
    require(type(doc["public_pipeline_count"]) is int and doc["public_pipeline_count"] == count, "public release count differs from receipts")
    for row in doc["prerequisite_releases"]:
        check_ci(row)

    # The ledger is public. These checks are only obvious-leak checks, not a security certification.
    text = json.dumps(doc, ensure_ascii=False)
    require(not re.search(r"(?i)(?<![A-Za-z])[A-Z]:[\\/]|/Users/|/home/|session_id\s*[\":]|threadId", text), "private path or session identifier in public ledger")
    return {"status": "PASS", "components": len(components), "milestones": len(milestones), "public_pipeline_count": count, "code_dependency_order": ordered}


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("20261116-build-ledger.json")
    try:
        doc = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)
        print(json.dumps(validate(doc), sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc) if not isinstance(exc, OSError) else "ledger unavailable"}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
