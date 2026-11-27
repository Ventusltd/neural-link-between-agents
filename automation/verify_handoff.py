"""Compare a handoff receipt with freshly retrieved GitHub data; never grant authority."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from validate_operations import require, strict_object, utc

COMMENT_URL = re.compile(r"https://github\.com/Ventusltd/neural-link-between-agents/issues/[1-9][0-9]*#issuecomment-([1-9][0-9]*)")
SHA = re.compile(r"[a-f0-9]{40}")
DIGEST = re.compile(r"[a-f0-9]{64}")

def verify(receipt, comment, current_head, now):
    require(isinstance(receipt, dict) and isinstance(comment, dict), "invalid receipt or comment")
    require(receipt.get("schema") == "neural.handoff-receipt.v1", "invalid receipt schema")
    url = receipt.get("comment_url")
    require(isinstance(url, str) and COMMENT_URL.fullmatch(url), "invalid comment address")
    require(comment.get("html_url") == url and type(comment.get("id")) is int
            and str(comment["id"]) == COMMENT_URL.fullmatch(url).group(1), "comment identity mismatch")
    created = utc(receipt.get("created_at"))
    updated = utc(receipt.get("updated_at"))
    require(created <= updated <= now, "invalid receipt chronology")
    require(comment.get("created_at") == receipt["created_at"] and
            comment.get("updated_at") == receipt["updated_at"], "comment timestamp changed")
    digest = receipt.get("body_sha256")
    require(isinstance(digest, str) and DIGEST.fullmatch(digest), "invalid body digest")
    require(isinstance(comment.get("body"), str) and
            hashlib.sha256(comment["body"].encode("utf-8")).hexdigest() == digest, "comment body changed")
    head = receipt.get("target_commit")
    require(isinstance(head, str) and SHA.fullmatch(head) and head == current_head, "target head changed")
    require("expires_at_utc" in receipt, "expiry must be explicit")
    if receipt["expires_at_utc"] is not None:
        expiry = utc(receipt["expires_at_utc"])
        require(updated <= expiry and now < expiry, "scope expired or invalid")
    return {"status": "MATCH", "authority_verified": False, "newer_comments_checked": False,
            "retrieval_freshness_verified": False}

def selftest():
    import copy
    comment = {"id": 1, "html_url": "https://github.com/Ventusltd/neural-link-between-agents/issues/87#issuecomment-1",
               "created_at": "2026-11-27T12:00:00Z", "updated_at": "2026-11-27T12:00:00Z",
               "body": "Synthetic fixture — exact body\n"}
    head = "a" * 40
    receipt = {"schema": "neural.handoff-receipt.v1", "comment_url": comment["html_url"],
               "created_at": comment["created_at"], "updated_at": comment["updated_at"],
               "body_sha256": hashlib.sha256(comment["body"].encode("utf-8")).hexdigest(),
               "target_commit": head, "expires_at_utc": "2026-11-27T13:00:00Z"}
    now = utc("2026-11-27T12:30:00Z")
    require(verify(receipt, comment, head, now)["authority_verified"] is False, "false authority")
    no_expiry = dict(receipt, expires_at_utc=None)
    require(verify(no_expiry, comment, head, now)["status"] == "MATCH", "explicit unspecified expiry")
    cases = [
        lambda r,c: c.update(body=c["body"].strip()),
        lambda r,c: c.update(updated_at="2026-11-27T12:01:00Z"),
        lambda r,c: c.update(id=2),
        lambda r,c: c.clear(),
        lambda r,c: r.update(target_commit="b"*40),
        lambda r,c: r.update(target_commit="main"),
        lambda r,c: r.update(expires_at_utc="2026-11-27T12:30:00Z"),
        lambda r,c: r.pop("expires_at_utc"),
        lambda r,c: r.update(comment_url="https://github.com/OtherOwner/repo/issues/87#issuecomment-1"),
        lambda r,c: r.update(updated_at="2026-11-27T12:40:00Z"),
    ]
    for index, change in enumerate(cases, 1):
        r,c = copy.deepcopy(receipt), copy.deepcopy(comment)
        change(r,c)
        try:
            verify(r,c,head,now)
        except ValueError:
            continue
        raise RuntimeError("negative fixture accepted: " + str(index))
    print(json.dumps({"status": "PASS", "healthy_fixtures": 2, "negative_fixtures": len(cases),
                      "coverage": "enumerated receipt integrity fixtures",
                      "miss_probability": "unknown outside fixture domain", "authority_verified": False}))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--receipt", type=Path)
    p.add_argument("--comment", type=Path)
    p.add_argument("--current-head")
    args = p.parse_args()
    if args.selftest:
        selftest()
        return
    if not (args.receipt and args.comment and args.current_head):
        p.error("supply receipt, freshly retrieved comment JSON and exact target HEAD")
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"), object_pairs_hook=strict_object)
        comment = json.loads(args.comment.read_text(encoding="utf-8"), object_pairs_hook=strict_object)
        print(json.dumps(verify(receipt, comment, args.current_head, datetime.now(timezone.utc))))
    except (ValueError, OSError, UnicodeError):
        # Never echo API bodies or private file paths.
        raise SystemExit("BLOCKED: receipt mismatch, invalid input or unavailable evidence") from None

if __name__ == "__main__":
    main()
