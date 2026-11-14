# REPD October 2026 release: team status (Team 5 hub, NL-017)

Updated: 2026-11-14T00:33Z (read from `date -u`). Source: issues 12 to 17 read at that time, plus the teams' working folders.
PR under test: Ventusltd/globalgrid2050 draft PR #57, head `f9ccd703`. Nothing merged, nothing promoted.

| Team (issue) | State | Blockers | Asks of ChatGPT | Asks of the owner |
|---|---|---|---|---|
| 1 Source QA (13) | ACK 00:26Z; working (re-derive 832 cell changes, gate audits, test suite) | none posted | none yet | none yet |
| 2 July baseline and delta (14) | working (folders q2/, q3/, w1-w4 active); no ACK on issue 14 yet | none posted | none yet | none yet |
| 3 Pipeline News (15) | ACK 00:25Z; headless browser runs under way | none posted | none yet | none yet |
| 4 Maps (16) | ACK 00:25Z; GridAtlas 3 failing pr-gate checks, legacy atlas switch patch | no push route to gridatlas (patch only) | none yet | none yet |
| 5 Release gate (17) | ACK 00:27Z; gates 1 to 4 done locally, see below | see open items | served-byte check after any merge (script to follow) | see open items |

Open requests still unanswered on the link (oldest first):
- NL-012 6868339699 (Claude harness to ChatGPT, 00:19Z): review PR #57; say whether #56 closes; browser-test candidate page; gov.uk publication-page check. Unanswered.
- NL-012 6868447347 (harness, 00:25Z): ChatGPT asked to answer team requests, run gov.uk check and live baseline, say if it objects to the arrangement. Unanswered.
- NL-012 6868443782 (ChatGPT, 00:25Z): asks Claude to resolve the one acceptance-harness failure (Ref 15915 Address) under a strict evidence policy and name the SHA for browser/MAP tests. Owner-of-reply: harness / Team 1.

Team 5 interim results (head f9ccd703, local evidence in the team folder; to be published in REPORT.md):
- No truncation: 316 added, 5 modified, 0 deleted; 63 of 64 RUNBOOK section 2 pins identical. The one change is `.github/large-files-allowlist.txt`, append-only (+7 lines, 0 removed), which RUNBOOK 2.1 lists as "byte-identical" and as "append only, owner approval".
- Rollback rehearsed locally: revert of a simulated merge restores main's tree exactly (0 paths differ), 0.3 s plumbing, 2.2 s porcelain.
- CI on PR branch: size guard success (321 files, 4 allowlisted), source intake success; public-language gate QUEUED (self-hosted runner offline); one failed push run 43533133319 at 0c78c8c1 (invalid workflow file, fixed by f9ccd703).
