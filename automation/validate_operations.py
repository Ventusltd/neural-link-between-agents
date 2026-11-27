"""Validate coordination index structure and evidence addresses; no network authority."""
import argparse
import copy
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
STATES = {"HISTORICAL_ACCEPTANCE", "REPORTED_DRAFT", "PENDING_OWNER_SCOPE",
          "IN_PROGRESS", "BLOCKED", "RETRYING", "TESTED", "REVIEWED", "MERGED",
          "PUBLICLY_VERIFIED", "COMPLETE"}
UTC = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")
WORK_ID = re.compile(r"[A-Z0-9][A-Z0-9._-]*")
REPO = r"/Ventusltd/[A-Za-z0-9_.-]+"
TARGET = re.compile(REPO + r"/(?:issues/[1-9][0-9]*|pull/[1-9][0-9]*|commit/[a-f0-9]{40}|actions/runs/[1-9][0-9]*(?:/job/[1-9][0-9]*)?)")
COMMENT = re.compile(r"issuecomment-[1-9][0-9]*")
THREAD = re.compile(r"/Ventusltd/neural-link-between-agents/issues/[1-9][0-9]*")

def require(condition, message):
    if not condition:
        raise ValueError(message)

def strict_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON field")
        result[key] = value
    return result

def utc(value):
    require(isinstance(value, str) and UTC.fullmatch(value), "timestamp must be explicit UTC")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def evidence_address(url, channel=False):
    require(isinstance(url, str) and url.isascii() and not any(c.isspace() or ord(c) < 32 for c in url),
            "invalid evidence address")
    parsed = urlsplit(url)
    require(parsed.scheme == "https" and parsed.netloc == "github.com" and not parsed.query,
            "evidence requires canonical credential-free GitHub HTTPS")
    require(TARGET.fullmatch(parsed.path), "evidence must identify a Ventus issue, PR, commit or Actions run")
    require(all(p not in (".", "..") for p in parsed.path.split("/")), "invalid repository path")
    if parsed.fragment:
        require(("/issues/" in parsed.path or "/pull/" in parsed.path) and COMMENT.fullmatch(parsed.fragment),
                "invalid evidence fragment")
    if channel:
        require(THREAD.fullmatch(parsed.path) and not parsed.fragment, "channel must be a Neural Link issue")

def validate(data):
    require(isinstance(data, dict) and type(data.get("schema_version")) is int
            and data["schema_version"] == 1, "unsupported schema")
    stamp = utc(data.get("checked_at_utc"))
    evidence_address(data.get("channel"), channel=True)
    work = data.get("work")
    require(isinstance(work, list) and work, "empty or invalid work register")
    seen = set()
    for item in work:
        require(isinstance(item, dict), "invalid work record")
        for key in ("id", "owner", "state", "evidence", "next_action"):
            require(isinstance(item.get(key), str) and item[key].strip(), "missing or invalid " + key)
        ident = item["id"]
        require(WORK_ID.fullmatch(ident) and ident not in seen, "malformed or duplicate work ID")
        require(item["state"] in STATES, "invalid state")
        seen.add(ident)
        evidence_address(item["evidence"])
    signoff = data.get("owner_signoff")
    if signoff is not None:
        require(isinstance(signoff, dict), "invalid historical signoff")
        require(signoff.get("status") == "SIGNED_IN_CONVERSATION", "unsupported signoff state")
        require(signoff.get("cryptographic_signature") is False, "unverified signature claim")
        require(utc(signoff.get("recorded_at_utc")) <= stamp, "signoff later than index")
        for key in ("exact_quote", "provenance"):
            require(isinstance(signoff.get(key), str) and signoff[key].strip(), "missing signoff provenance")
    return len(seen)

def selftest(data):
    validate(data)
    cases = [
        lambda d: d.update(schema_version=True),
        lambda d: d.update(checked_at_utc="2026-02-30T00:00:00Z"),
        lambda d: d.update(checked_at_utc="2026-11-19T16:34:22+01:00"),
        lambda d: d.update(channel="https://github.com/Ventusltd/gridatlas/issues/1"),
        lambda d: d.update(channel="https://github.com/Ventusltd/neural-link-between-agents/issues/1#issuecomment-1"),
        lambda d: d.update(work=[]),
        lambda d: d["work"].append(copy.deepcopy(d["work"][0])),
        lambda d: d["work"][0].update(id=" " + d["work"][0]["id"]),
        lambda d: d["work"][0].update(state="APPROVED_BY_AGENT"),
        lambda d: d["work"][0].update(evidence="https://github.com/login"),
        lambda d: d["work"][0].update(evidence="https://github.com:443/Ventusltd/gridatlas/issues/1"),
        lambda d: d["work"][0].update(evidence="https://github.com/Ventusltd/gridatlas/issues/1?redirect=other"),
        lambda d: d["work"][0].update(evidence="https://github.com/OtherOwner/gridatlas/issues/1"),
        lambda d: d["work"][0].update(evidence="https://github.com/Ventusltd/gridatlas/commit/main"),
        lambda d: d["work"][0].update(evidence="https://github.com/Ventusltd/gridatlas/issues/1#unknown"),
        lambda d: d["work"][0].update(evidence="https://github.com/Ventusltd/../issues/1"),
        lambda d: d["work"][0].update(evidence="https://github.com/Ventusltd/gridatlas/issues/1\n"),
        lambda d: d["work"][0].update(evidence="https://user@github.com/Ventusltd/gridatlas/issues/1"),
        lambda d: d.update(owner_signoff={"status": "SIGNED_IN_CONVERSATION", "cryptographic_signature": True}),
    ]
    for number, mutate in enumerate(cases, 1):
        candidate = copy.deepcopy(data)
        mutate(candidate)
        try:
            validate(candidate)
        except ValueError:
            continue
        raise RuntimeError("negative fixture accepted: " + str(number))
    try:
        json.loads('{"state":"BLOCKED","state":"COMPLETE"}', object_pairs_hook=strict_object)
    except ValueError:
        pass
    else:
        raise RuntimeError("duplicate-key fixture accepted")
    return len(cases) + 1

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"), object_pairs_hook=strict_object)
    count = validate(data)
    fixtures = selftest(data) if args.selftest else 0
    print(json.dumps({"status": "PASS", "work_records": count, "negative_fixtures": fixtures,
                      "coverage": "all declared index records; enumerated negative fixtures if requested",
                      "miss_probability": "not applicable to exhaustive structural check; unknown for unlisted work or remote claims",
                      "remote_evidence_verified": False, "release_authority": False}))

if __name__ == "__main__":
    main()
