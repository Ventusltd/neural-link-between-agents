# NL-011 brief: six Opus agents study the neural link and reason

Owner's question (2 Nov 2026, overnight): "Is the neural link working well between agents? Can we get 6 additional
opus agents that just study the neural link and reason?"

Study only: read, measure, reason, write. Do not post on GitHub, do not edit anything outside FIXES/NL-011/, do not
commit or push (the harness commits). Every claim carries a key: an issue comment URL or id, a file path:line, a commit
sha, or a count with the command that produced it.

Sources:
- Ventusltd/neural-link-between-agents issues #1–#10 and every comment:
  `gh api "repos/Ventusltd/neural-link-between-agents/issues/<n>/comments?per_page=100" --paginate`
  (fields: id, created_at, body, updated_at). Issues #6 NL-006, #7 NL-007, #8 NL-008, #9 NL-009, #10 NL-010 hold
  tonight's traffic.
- /home/user/neural-link-between-agents: PROTOCOL.md (the envelope and handshake), AGENTS.md, SESSIONS/,
  FIXES/ (NL-007 rounds, NL-009 round1, NL-010 team-1..5, ROADMAP.md, OPUS-BRIEF.md, OVERNIGHT.md log,
  served-check.md, handoff-11/13), and `git log --format='%h %ad %s' --date=iso` of that repo.
- /home/user/estate/kuiper-belt/editions/202611012135/handoff/*/ (PLAN.md, REQUESTS.md, HANDOFF.md, TEST.md,
  EVIDENCE.md, 10-integration/ADMISSIONS.md, GREEN.md, WATCHER-B.md, CONTROLLER.md) and the branch history
  `git log --format='%h %ad %s' --date=iso origin/edition/202611012135`. Much coordination happened through these
  files, not the issues; count both.

Known facts to weigh, not to repeat as findings without checking: nine comments were posted with a literal "@file"
body because a brief said `gh api -f` instead of `-F`, and were repaired; agents overwrote each other's files more than
once (test.cjs, EVIDENCE.md, the loader reference); handoffs were sometimes posted before review; several reports had
times not read from a clock; the harness relayed many messages between agents by direct message rather than through
the link.

Each agent writes FIXES/NL-011/<NN>-<lens>.md: a verdict of three sentences at the top, then numbered findings with
keys and counts, then what to change (concrete, small), then limits. Return a summary of at most 150 words.
Agent 06 waits for 01–05 (poll FIXES/NL-011/ every 3 minutes, up to 45 minutes) and writes FIXES/NL-011/SYNTHESIS.md
and FIXES/NL-011/PROTOCOL-v2-proposal.md.
