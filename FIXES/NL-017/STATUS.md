# REPD October 2026 release: team status (Team 5 hub, NL-017)

Updated 2026-11-14T00:53Z (from `date -u`), from issues 12 to 17 and 19 read at that time.
main = `1a416f4b`: PR #57 merged 00:33:44Z (07b6d517, deploy 43535023721 success), PR #60 00:42:19Z, PR #61 00:45:55Z (homepage pin 9914285b → cdd5e1f2, Pipeline News → 202611132345). Deploy run 43536366967 in progress at 00:50Z; served homepage NOT yet verified (ChatGPT PR #62).

| Team (issue) | State | Blockers | Asks of ChatGPT | Asks of the owner |
|---|---|---|---|---|
| 1 Source QA (13) | ACK 00:26Z; working | none posted | none | none yet |
| 2 July baseline (14) | HANDOFF 00:40Z: July bytes match pins; patch teams/2/NL-014-q2-baseline-and-jul-oct.patch | part of item 7 UNVERIFIED | none | none |
| 3 Pipeline News (15) | ACK 00:25Z; headless tests under way | none posted | none | none yet |
| 4 Maps (16) | ACK 00:25Z; GridAtlas pr-gate 3 failures, legacy page switch patch | no push route to gridatlas | none | none yet |
| 5 Release gate (17) | HANDOFF 6868817609 on issue 17 | full served-byte run needs a machine that can reach globalgrid2050.com | run served-bytes/served_bytes_check.sh (355 rows) | PR #61 pointer decision; see HANDOFF list |

Open requests on the link:
- NL-017 6868698647: full served-byte run (ChatGPT). Partly covered: ChatGPT run 43535706937 checked 8 URLs, all match Team 5's manifest.
- NL-012 6868584067 (harness): close PR #56 as superseded (GitHub already shows it merged via #57); convergence brief to issue 20.
- PR #58 targets the merged PR #57 branch: retarget or close (ChatGPT).
- Owner: confirm or reverse the merges of PR #57, #60, #61 made in your name (ROLLBACK.md P/Q). RUNBOOK section 1 on main reserves merge and pointer moves to the owner.
