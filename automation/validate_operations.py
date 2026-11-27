"""Fail closed on malformed coordination-index evidence, without network access.

This checks syntax and self-tests the declared rejection contract. A valid URL,
timestamp or recorded sign-off is not authentication, reachability or approval.
"""
import copy
import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = frozenset({
    "HISTORICAL_ACCEPTANCE", "REPORTED_DRAFT", "PENDING_OWNER_SCOPE",
    "IN_PROGRESS", "BLOCKED", "RETRYING", "TESTED", "REVIEWED", "MERGED",
    "PUBLICLY_VERIFIED", "COMPLETE",
})
ID = re.compile(r"[A-Z0-9][A-Z0-9_-]*", re.ASCII)
STAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", re.ASCII)
# Source: GitHub issue, PR, commit and Actions evidence routes used by STATUS.json.
BASE = r"https://github\.com/[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+/"
NUMBER = r"[1-9][0-9]*"
EVIDENCE = re.compile(
    BASE + r"(?:(?:issues|pull)/" + NUMBER
    + r"(?:#(?:issuecomment|discussion_r|pullrequestreview)-?" + NUMBER + r")?"
    + r"|commit/[a-f0-9]{40}"
    + r"|actions/runs/" + NUMBER + r"(?:/(?:job|attempts)/" + NUMBER + r")?)",
    re.ASCII,
)
CHANNEL = re.compile(
    r"https://github\.com/Ventusltd/neural-link-between-agents/issues/" + NUMBER,
    re.ASCII,
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key")
        result[key] = value
    return result


def invalid_constant(_):
    raise ValueError("Non-standard JSON constant")


def load_index(raw):
    return json.loads(raw, object_pairs_hook=no_duplicates, parse_constant=invalid_constant)


def utc_stamp(value):
    require(isinstance(value, str) and STAMP.fullmatch(value), "Expected UTC timestamp ending Z")
    datetime.fromisoformat(value.replace("Z", "+00:00"))


def valid_text(value):
    return (
        isinstance(value, str) and bool(value.strip())
        and value == value.strip()
        and not any(ord(c) < 32 or 127 <= ord(c) <= 159 for c in value)
    )


def evidence_url(value):
    require(isinstance(value, str) and EVIDENCE.fullmatch(value), "Unsupported GitHub evidence route")
    # Forbid dot segments, including the repository segment.
    require(value.split("/")[4] not in {".", ".."}, "Invalid repository segment")


def validate(data):
    require(isinstance(data, dict), "Index must be an object")
    require(type(data.get("schema_version")) is int and data["schema_version"] == 1, "Unsupported schema_version")
    utc_stamp(data.get("checked_at_utc"))
    require(isinstance(data.get("channel"), str) and CHANNEL.fullmatch(data["channel"]), "Invalid Neural issue channel")
    work = data.get("work")
    require(isinstance(work, list) and bool(work), "Work must be a nonempty list")
    seen = set()
    for item in work:
        require(isinstance(item, dict), "Work item must be an object")
        for field in ("id", "owner", "state", "evidence", "next_action"):
            require(valid_text(item.get(field)), "Missing or invalid text field: " + field)
        require(ID.fullmatch(item["id"]) and item["id"] not in seen, "Invalid or duplicate work ID")
        require(item["state"] in STATES, "Invalid work state")
        evidence_url(item["evidence"])
        seen.add(item["id"])
    if "owner_signoff" in data:
        signoff = data["owner_signoff"]
        require(isinstance(signoff, dict), "Recorded sign-off must be an object")
        for field in ("status", "exact_quote", "provenance"):
            require(valid_text(signoff.get(field)), "Invalid sign-off record")
        utc_stamp(signoff.get("recorded_at_utc"))
        # A copied conversation quotation cannot itself be a cryptographic proof.
        require(signoff.get("cryptographic_signature") is False, "Unverified cryptographic signature claim")
    return len(seen)


def selftest():
    """One healthy fixture plus explicit disease cases; no network or live-state mutation."""
    channel = "https://github.com/Ventusltd/neural-link-between-agents/issues/87"
    fixture = {
        "schema_version": 1, "checked_at_utc": "2026-11-27T12:00:00Z",
        "channel": channel,
        "work": [{"id": "TEST-1", "owner": "Reviewer", "state": "TESTED",
                  "evidence": channel + "#issuecomment-123", "next_action": "Review exact head"}],
    }
    require(validate(load_index(json.dumps(fixture))) == 1, "Healthy fixture refused")
    failures = []
    for label, field, value in (
        ("boolean schema", "schema_version", True),
        ("float schema", "schema_version", 1.0),
        ("offset instead of UTC", "checked_at_utc", "2026-11-27T13:00:00+01:00"),
        ("impossible date", "checked_at_utc", "2026-02-30T12:00:00Z"),
        ("wrong channel", "channel", channel.replace("issues/87", "pull/87")),
        ("foreign channel", "channel", channel.replace("Ventusltd/", "other/")),
        ("empty work", "work", []),
        ("object instead of list", "work", {}),
        ("duplicate ID", "work", fixture["work"] * 2),
        ("signature assertion", "owner_signoff", {"status": "SIGNED", "exact_quote": "x",
           "provenance": "x", "recorded_at_utc": "2026-11-27T12:00:00Z", "cryptographic_signature": True}),
    ):
        candidate = copy.deepcopy(fixture)
        candidate[field] = value
        failures.append((label, candidate))
    for label, field, value in (
        ("ambiguous ID", "id", "test-1"), ("unknown state", "state", "GREEN"),
        ("control character", "owner", "Agent\nX"), ("empty action", "next_action", " "),
        ("non-GitHub", "evidence", "https://example.org/issues/1"),
        ("credential URL", "evidence", "https://user:pass@github.com/o/r/issues/1"),
        ("nonstandard port", "evidence", "https://github.com:8443/o/r/issues/1"),
        ("arbitrary path", "evidence", "https://github.com/o/r/settings"),
        ("mutable branch commit", "evidence", "https://github.com/o/r/commit/main"),
        ("tracking or secret query", "evidence", channel + "?token=fixture"),
        ("encoded path", "evidence", "https://github.com/o/r/issues/%31"),
        ("dot segment", "evidence", "https://github.com/o/../issues/1"),
        ("arbitrary fragment", "evidence", channel + "#anything"),
    ):
        candidate = copy.deepcopy(fixture)
        candidate["work"][0][field] = value
        failures.append((label, candidate))
    for label, candidate in failures:
        try:
            validate(candidate)
        except ValueError:
            continue
        raise RuntimeError("Disease accepted: " + label)
    for raw in ('{"schema_version":1,"schema_version":2}', '{"x":NaN}'):
        try:
            load_index(raw)
        except ValueError:
            continue
        raise RuntimeError("Malformed JSON accepted")
    print("PASS: one healthy and " + str(len(failures) + 2)
          + " enumerated negative fixtures; full declared fixture set, unknown miss rate outside it")


def main():
    selftest()
    count = validate(load_index((ROOT / "STATUS.json").read_text(encoding="utf-8")))
    print(f"PASS: all {count} work records checked for unique IDs, UTC timestamps and evidence route syntax; "
          "remote reachability, freshness, identity and approval not verified")


if __name__ == "__main__":
    main()
