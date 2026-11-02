# NL-011 launch queue (kept on the link so it survives the session)

Launched: 01–06 (study), 07 persistence. Waiting for free slots (20 concurrent cap), in this order:

- 08 open-request ledger: keep FIXES/NL-011/LEDGER.md (every open REQUEST/BLOCKER/question from #10, #11 and
  kuiper-belt handoff/*/REQUESTS.md; owner Q1–Q8 as a section), refresh every 10 min for 2 h, nudge on #10 once per
  refresh for rows open over 30 min.
- 09 decision log: FIXES/NL-011/DECISIONS.md, every ruling, refusal, admission and owner instruction since NL-006 with
  its key (comment URL, commit, file:line), who made it and on what authority.
- 10 resume kit: SESSIONS/RESUME.md, the steps a brand-new session takes to pick up the overnight work from the link
  alone (repos to clone, branches, the state files, the tools, the open steps R2/R4, the controller duties), checked by
  reading it cold against the repos.
- 11 index: FIXES/INDEX.md, every NL issue and FIXES folder with one line each, newest first, and where each team's
  hand-off and evidence live.
- 
  short REVIEW only when something is wrong.

Every agent: read LINK-RULE.md first; write files only under the paths named; run the K1 check before leaving a file;
post with `gh api ... -F body=@file`; the harness commits.
