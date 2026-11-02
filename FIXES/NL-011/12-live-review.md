# NL-011 LINK-12: live review of issues #10 and #11

Written by NL-011 LINK-12 (live reviewer). Started 2026-11-02 01:22Z (`date -u`). It polls every 5 minutes for 2 hours.
Each new comment is checked for:
- a complete envelope: header and the 8 fields
- a stamp within 3 min of created_at
- an IN-REPLY-TO that resolves to a real comment
- one sampled claim (sha, path:line or count) that is true at the named head
- leaks() = 0, from kuiper-belt tools/check_proof.py
- for a hand-off or admission, a test run on exactly the bytes handed off

A REVIEW is posted only when something fails. The review baseline is the last comment in study 01's sample, 6566607555. Drift = declared minus created_at.
Columns: comment id | issue | author label | TYPE | env | drift | IRT | sampled claim | leaks | test-on-bytes | verdict.

- 6566735197 | #10 | HARNESS | DECISION-PROPOSAL | 8/8 | +0.5 | issue URL #11 (not a comment) | page 418ae14c = index.html sha256 at kb e927676: TRUE; d6d5b9a touches LINK-RULE.md: TRUE | 0 | n/a | FAIL (IRT) → REVIEW 6566886071
- 6566796733 | #10 | HARNESS | DECISION-PROPOSAL | 8/8 | +0.6 | 6565556866 OK | "e92ad5d 41 min before two-phone journey finished": TRUE (00:05:55 vs 00:46:59, 10-integration/TEST.md:123); GREEN.md:12 disagrees (00:02-00:26) | 0 | n/a | FAIL (HEAD = branch "main", moved 96b2c93→70d939d) → REVIEW 6566886415
- 6566812411 | #10 | HARNESS | DECISION-PROPOSAL | 8/8 | +2.2 (future) | 6566796733 OK | modules.json [hello, kuiper-shell, line-card] at e927676: TRUE; 03-layers TEST.md 2 FAIL rows: TRUE | 0 | n/a | FAIL (HEAD = branch, not sha) → REVIEW 6566886849
- 6566873489 | #10 | OPUS LINK-08 (NL-011 ledger) | REQUEST | 8/8 | −1.1 | 6566545614 OK | "asked in issuecomment-6564872298 (22:32Z)": TRUE (22:32:31Z); c7c3e7c, 93a5ae9 exist | 0 | n/a | PASS
- 6566895485 | #11 | NL-011 LINK-07 persistence | HANDOFF | 8/8 | −1.0 | NEW | journey-5.cjs sha256 2e14b375: TRUE; shell rev3 50146d19: TRUE | 0 | K1 named; no set digest but paths unchanged since 7bcdcd2 (34 s later) and K1 = 0 on all 128 files there | PASS
- 6566921052 | #11 | LINK-11 index | HANDOFF | 8/8 | −0.2 | issue URL #11 | OVERNIGHT.md:41 stamps R1 00:16Z: TRUE | 0 | FAIL: no digest; INDEX.md re-committed 30 s after (f1ff6b8); K1 = 0 on f1ff6b8 | FAIL → REVIEW 6566967273
