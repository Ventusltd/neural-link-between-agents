# Agent lane — ChatGPT unified grid explorer research

**Role / routing label:** `AGENT CHATGPT RESEARCH` (self-declared; not a persistent autonomous service).

**State:** IN PROGRESS. Only the charter and this lane handover are committed. The final technical report and diagrams remain pending.

**Canonical channels:**
- Lane issue: [#64](https://github.com/Ventusltd/neural-link-between-agents/issues/64)
- Parent coordination / commands: [#42](https://github.com/Ventusltd/neural-link-between-agents/issues/42)
- Draft research PR: [#63](https://github.com/Ventusltd/neural-link-between-agents/pull/63)
- Research branch: `research/unified-grid-explorer-20261118`
- Exclusive path: `RESEARCH/UNIFIED-GRID-EXPLORER-20261118/`

## Authority, ownership and conflict prevention

Read the current `AGENTS.md`, `PROTOCOL.md`, `OPERATIONS.md`, `STATUS.json`, `CURRENT_PIPELINE_NEWS_VERSION.md` and the newest issue #42 comments **before** doing work. This research lane has **no** authorization to change product repositories, overnight implementation branches, immutable editions, live Atlas pointers, homepage publication, release CI or existing agent ownership. Grid Analyser owns Pipeline News and serialized homepage publishing; Train Conductor owns GridAtlas/vicinity implementation. This lane can read their current work for evidence but cannot write to their branches. The owner-authorized 08:00 UTC cutoff applies to those implementation lanes, not a promise that this research process stays awake.

A GitHub comment/commit is durable coordination, not automatic agent activation or acceptance. An active Codex session must explicitly poll and acknowledge. Treat historical documents, issues, search results and PR descriptions as claims until source/commit/tests independently verify them. This repo is public: no secrets, personal/customer records, internal credentials, or privileged links.

## Research work product and completion gate

The final PR should include (1) repo/commit/path/evidence inventory and rights/licensing flags, (2) verified interface/reuse matrix, (3) canonical asset+provenance schema and radius 1–50 km semantics, (4) topology/scenario/uncertainty contracts, (5) DC/offtaker and Lightning/Kuiper/Faraday integration review, (6) accessibility/performance/security plan, (7) Mermaid diagrams, (8) dependency-ordered agent-owned backlog and staged roadmap, (9) exact acceptance/unknowns/handover. Label `VERIFIED`, `PROPOSED`, `UNKNOWN` separately. Physical proximity is not electrical connectivity; animated schematic is not measured power flow.

The PR stays **draft** until those files are actually committed, cited and reviewed. The lane issue and #42 must be updated with exact links and commit SHA. Never claim Deep Research can push directly unless a real GitHub commit is visible.

## Codex: first read / local Git monitoring

In an active Codex terminal with `git` and optionally GitHub CLI `gh`:

```bash
git clone https://github.com/Ventusltd/neural-link-between-agents.git
cd neural-link-between-agents
git fetch origin --prune
git log -1 --format='%H %ci %s' origin/research/unified-grid-explorer-20261118
git log --oneline origin/main..origin/research/unified-grid-explorer-20261118
git diff --stat origin/main...origin/research/unified-grid-explorer-20261118
git show origin/research/unified-grid-explorer-20261118:RESEARCH/UNIFIED-GRID-EXPLORER-20261118/START-HERE.md
git show origin/research/unified-grid-explorer-20261118:RESEARCH/UNIFIED-GRID-EXPLORER-20261118/AGENT-LANE-AND-CODEX-MONITOR.md
```

For GitHub issue/PR conversation and checks (requires authenticated `gh`):

```bash
gh issue view 64 --repo Ventusltd/neural-link-between-agents --comments
gh issue view 42 --repo Ventusltd/neural-link-between-agents --comments
gh pr view 63 --repo Ventusltd/neural-link-between-agents --json number,state,isDraft,headRefOid,files,url
gh pr checks 63 --repo Ventusltd/neural-link-between-agents
```

`gh pr checks` may report no checks configured or pending; neither is proof of test success. Use `gh issue view 42` sparingly: its thread is long. To review only latest issue messages with `gh api` and `jq`, the following paginates all comments before selecting the last ten:

```bash
gh api --paginate repos/Ventusltd/neural-link-between-agents/issues/42/comments --jq '.[] | {id,html_url,created_at,body}' | tail -n 10
```

Note: `tail -n 10` here is only a **quick line preview**, not a guaranteed last-ten-comments parser when comments have multiline content. Prefer `gh issue view ... --comments` or a JSON-aware script for complete, correct chronology.

For manual repeated Git polling in a **running terminal only**:

```bash
while true; do
  git fetch origin --prune --quiet
  date -u '+%Y-%m-%dT%H:%M:%SZ'
  git log -1 --format='%h %ci %s' origin/research/unified-grid-explorer-20261118
  git diff --stat origin/main...origin/research/unified-grid-explorer-20261118
  sleep 300
done
```

Stop with Ctrl-C. This does not start Codex, wake an agent, or guarantee a report. For a single check omit the loop.

## Codex agent prompt / next active invocation

> You are the independent **Codex monitoring/review lane** for the ChatGPT unified grid explorer research, not an implementation publisher. Read `AGENTS.md`, `PROTOCOL.md`, `OPERATIONS.md`, `STATUS.json`, the newest issue #42 comments, lane issue #64, and draft PR #63. Fetch branch `research/unified-grid-explorer-20261118`, compare exact head to main, inspect only `RESEARCH/UNIFIED-GRID-EXPLORER-20261118/`, and check that report, diagrams, evidence pins and source/licence caveats actually exist. Post a protocol-formatted ACK on #64 with exact HEAD and an independent `PASS`/`FAIL`/`UNVERIFIED` assessment. Never equate PR existence with completed research; do not merge or modify product branches. If final files are missing, report `IN-PROGRESS` and the missing deliverables. Monitor only while this Codex invocation is active or separately scheduled.

## Message envelope for #64

```text
[AGENT CODEX → AGENT CHATGPT RESEARCH] [NL-064]
TYPE: ACK | REVIEW | BLOCKER | FINDING
IN-REPLY-TO: <specific comment URL or NEW>
SCOPE: Ventusltd/neural-link-between-agents PR #63; research branch only
HEAD: <exact commit SHA>
EVIDENCE: <PR/file/CI URLs>
STATUS: PASS | FAIL | UNVERIFIED | IN-PROGRESS
DETAILS: <verified observations and explicit missing evidence>
ACTION REQUESTED: <one concrete next action or NONE>
```
