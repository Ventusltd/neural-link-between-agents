# REPD October 2026 job: improved scopes for every lane

Written by the coordinator (Claude Fable), first pass 2026-11-14T00:48Z (clock read with `date -u`).
Reference: `OWNER-INSTRUCTIONS.md` in this folder (the owner's instructions of the night in order, as one brief, and
progress against each line). Every lane below traces to a line of its Part 2; every line of Part 2 has one owning lane.
Basis: opening posts and ACKs on issues 12 to 20, the team brief, each lane's working folder and public folder
`FIXES/NL-0xx/`, and globalgrid2050 main at `1a416f4b`. This file states scope only. It approves nothing, and it does
not widen any lane's permissions: the harness and the owner decide what is applied, merged or promoted.
Revised only when a lane's findings or ChatGPT's posts change what a lane should be doing; revisions are listed at the end.

## 0. Trace: the owner's brief (Part 2) to lanes

| Line | Owner's brief | One owning lane | Done when | Evidence expected |
|---|---|---|---|---|
| 1 | Protect what exists: backup, text log, no truncation, hashes, checkpoints, testcode, easy restore | Team 5 (NL-017); checkpoints are made by the harness | Every pre-existing file on main is shown byte-identical or listed with its reason; a rehearsed rollback exists for each live step taken, in the right order | Changed-files table against `73cbdec1`; rehearsal log; checkpoint ids |
| 2a | Ingest October REPD, current formats, cleaned with Python: datasets | Team 1 (NL-013) | Independent re-derivation matches; gates fail on bad input | Re-derivation log, defect table, patches |
| 2b | July baseline and true comparison | Team 2 (NL-014) | Finished | Comment 6868663705, PR #60 |
| 2c | Pipeline News on October data | Team 3 (NL-015) | The operative page is tested beyond load and paging; defects ranked | Headless logs, recounts, patches P1 and P2 |
| 2d | GridAtlas and legacy maps on October data | Team 4 (NL-016) | Preview package ready to push; per-page evidence for the legacy switch; new-ref MAP behaviour known | Gate log, per-page table, patches |
| 3 | Two agents through the agents repository; audit trail; sign-off; use ChatGPT | Harness with ChatGPT (NL-012) | Each live step has a note on the link before or at the time, and a check by the other agent | Issue 12 comments, `LOG.md` |
| 4 | Private understanding of the release | Harness, privately. No lane; never on the link | n/a here | n/a here |
| 5 | Scale and speed, live, no waiting | Harness | n/a (working arrangement) | Issue 12 |
| 6 | Finished, audited CI/CD; next quarter routine | Team 5 (NL-017); Team 1 contributes the gate attack | Gate table complete; the release workflow has run once on GitHub or the reason is stated; a written procedure for the January 2027 release that a new agent can follow | Gate table, workflow run id, RUNBOOK patch |
| 7a | News: existing builders on October data | N1 (NL-019) | October-bound feed under a new name; hard-coded counts located | Feed file, counts, patch |
| 7b | News: discovery | N2 (NL-019) | Chain mapped; new-quarter pickup patched and tested | Map, bind rates, patch |
| 7c | News: relevance | N3 (NL-019) | Explainable score with evidence tiers; shared binder and labelled set | Module, tests, evaluation numbers |
| 8a | Converge REPD with data centres: the join | Team 6 (NL-020) | Deterministic files with manifest, negative tests | Files, manifest, test log |
| 8b | Data-centre projects inside Pipeline News as their own category | **No lane** (see G13) | A new release folder shows Data Centres as a separate category from Team 6's file, with no REPD id and no MAP without geometry | not started |
| 9 | Fable reasoner: read scopes, improve them | Coordinator (NL-012) | This file, one comment per issue, Part 3 kept current | this folder |
| 10 | REPD refreshed every month | M1 (public folder `FIXES/NL-012/M1`) | One scheduled workflow that does nothing when the published files are unchanged and opens a pull request when they changed | Workflow file, one recorded "no change" run on GitHub, a simulated-change test |
| 11 | Data-centre capex news and politics in Pipeline News | N4 (NL-019) | One feed file and one panel on the operative page, hidden when the file is absent | Feed schema, fixture tests, headless screenshot |
| 12 | Use what GridAtlas already holds, through a headless browser | G1 (NL-016) | An inventory of GridAtlas layers with counts, ids and screenshots, and a list of what other lanes can reuse instead of building | Inventory file, screenshots |
| 13 | Simple, exploratory, keep moving | Every lane; the coordinator names the cuts (section 2b) | Each duplicate in section 2b has one owner or is removed | section 2b |
| 14 | Compare the Cloud article in the feed and linked from the cyber-resilience site, nothing truncated | Harness (both pull requests); ChatGPT checks and publishes | Article in the feed file; cyber-resilience entry merged with the earlier entry, note and stylesheet byte-identical | PR #70; cyber-resilience PR #1 and the hashes in its text |
| 15 | Pipeline News version train every 30 minutes, converging on a final release; map and Grid Engine deep link the star; old versions kept | Guardian (reports on NL-015) | See section 2c | versions page, CI workflow, release-candidate post |

## 1. The whole job in one picture

| Stage | What it is | State at 00:48Z | Lane that owns it |
|---|---|---|---|
| S1 Source | Official October CSV `48e76c49…` (5,219,160 bytes) and XLSX `87811e24…` (5,378,656 bytes): 14,968 rows, 14,967 refs, 53 columns | Pinned; 43-check acceptance run 43535583260 with one waived cell (ref 15915 Address) | Team 1 (QA); ChatGPT (gov.uk reach) |
| S2 Baseline | July originals CSV `84c1b5f9…`, XLSX `624a0a97…` (14,657 rows); July to October +319 / −9 / 14,648 retained | On archive branch `d015479f`; baseline patch merged as PR #60 (`67635070`) | Team 2 (finished) |
| S3 Datasets | `repd-2026q3.csv` `d937ae16…` (14,967), subsets 2,181 / 1,229 / 940, `dist/repd_master_2026q3.json` `3ffe6c5c…` (11,293 features), identity 14,967, major projects 3,765 | On main since `07b6d517`; served bytes reported equal to Git by run 43535706937 | Team 1 (QA) |
| S4 Pipeline News | Release folder `uk_renewables_pipeline/202611132345/` (7,775 records) | Served. Homepage pointer moved to it: homepage PR #9 (`cdd5e1f2`), pin PR #61 (`1a416f4b`, merged 00:45:55Z); deploy run 43536366967 in progress at 00:47Z | Team 3 (QA); ChatGPT made the pointer change |
| S5 Maps | GridAtlas (live generation 202610312138, built on older REPD) and globalgrid2050 legacy atlas pages (January files) | Unchanged. GridAtlas preview 202611132345 exists offline only | Team 4 |
| S6 Convergence | REPD × data-centre register (226 records, `87337db5…`) | Building offline; 20 tests pass locally | Team 6 |
| S7 News | Legacy signal builders, discovery tooling, relevance model | Three agents working offline | N1, N2, N3 |
| S8 CI/CD and rollback | Gates, deploy impact, restore points, runbook | Rollback written for the PR #57 merge only | Team 5 |

Order of dependence: S1 → S3 → S4 → (S5, S6) → S7. S2 feeds every change report and N3's events. S8 wraps all stages.

Rules common to every lane (from AGENTS.md, PROTOCOL.md, the team brief): additive files only; existing files stay
byte-identical; blank capacity is unknown, never zero; patches are delivered to the harness, not pushed; nothing private
on the link; a claim carries evidence or the word UNVERIFIED; only the owner accepts a release.

## 2. Gaps that no lane owns (proposed owner in brackets; the harness decides)

G1. **Check of the homepage after the pointer move.** PR #61 changed `catalogue/homepage-owner.json` (owner commit
`9914285b` → `cdd5e1f2`; `index.html` and `data/homepage.json` hashes changed). No Claude lane has the promoted homepage
in scope: Team 3's scope was written when the pointer was unmoved, and Team 5's manifest treats the homepage as a PIN
row that must not change. [Team 5 for the manifest and byte expectations; Team 3 for the page as the operative release;
ChatGPT for the live fetch, which only it can do.]

G2. **Rollback now has two layers and an order.** `FIXES/NL-017/ROLLBACK.md` section A reverts merge `07b6d517`, which
deletes `uk_renewables_pipeline/202611132345/`. Since 00:45:55Z the homepage links to that folder. Reverting the data
merge alone would leave the homepage pointing at a removed page. The pointer rollback (pin back to `9914285b`, which is
a revert of `92d784f4`, plus the homepage repository's own revert of `cdd5e1f2`) is described only in PR #61's text and
has not been rehearsed by anyone. Main has also moved past the rehearsed tree (PR #60, PR #61). [Team 5.]

G3. **Public language gate never ran.** It was queued on PR #57 (43533485421), PR #60 (43535848245), PR #59 and PR #61
(43536298310); it needs a self-hosted runner that is offline. Three merges went in without it. [Owner: start the runner
or state that the gate is waived. Team 5: run the same check locally if the script is in the repository and report.]

G4. **Record of owner acceptance.** PR #61's title says "accepted". The link carries relays of the owner's working
instruction but no acceptance statement by the owner for release 202611132345. [Owner only. No lane writes it.]

G5. **GridAtlas knows only the old register.** The promoted page's MAP links go to the live GridAtlas generation
202610312138. Whether the 319 refs added in October resolve there, and what a reader sees when they do not, sits between
Team 3 (links on the page) and Team 4 (GridAtlas side). The GridAtlas preview has no push route. [Team 4 owns the
answer; Team 3 supplies the list of hrefs. Push to gridatlas: owner.]

G6. **Draft QA pull requests.** PR #58 targets the merged branch of PR #57; PR #59 holds the served-byte and 43-check
workflows as a draft. Neither has an owner for "merge, retarget or close". [ChatGPT, who opened them.]

G7. **Jekyll publishes 32 rendered `.md` pages**, one of them a test fixture (Team 5 finding, issue 17 comment
6868698647). Nobody has the exclusion patch. [Team 5.]

G8. **Pipeline News repository release** (built offline for Ventusltd/pipelinenews) is reviewed by Team 3 but nobody
owns pushing it or deciding whether it is needed now that the page is served from globalgrid2050. [Owner decision;
Team 3 states the consequence of not pushing it.]

G9. **Three binders and two event generators in the news lanes** (see section 3, NL-019). [N3 owns the shared ones.]

G10. **The owner's own words on news and convergence.** ChatGPT's brief on issue 20 (comment 6868599730) and the body of
issue 19 give requirements in ChatGPT's wording. The owner's direct explanation is still not on the link. Lanes work to
the posted wording; anything further is [ChatGPT to post, or the owner].

G11. **Stale status file.** `FIXES/NL-017/STATUS.md` (00:33Z) says nothing is merged. [Team 5, or retire it in favour
of this file plus the lane handoffs.]

G13. **Brief line 8b has no lane.** "Bring data-centre projects directly into Pipeline News" needs a page build: Team 6
delivers data and a field proposal, N2 binds a news topic, nobody builds or tests the category on a release folder.
[Proposed: Team 3, after its QA handoff, as a new release folder beside 202611132345; the harness decides and starts it.]

G14. **Checkpoint for the later live steps.** The testcode checkpoint and restore branch were made before PR #57. No
checkpoint covering main at `1a416f4b` and the previous homepage pin `9914285b` is recorded on the link. [Harness.]

G15. **Next quarter.** Nothing detects a new REPD release; the release workflow is manual and has not run on GitHub.
[Team 5 writes the procedure and names the trigger options; whether a scheduled detector is allowed under the
repository's freeze rule is the owner's decision.]

G12. **Issue 18** (activity index) has no agent and is outside this job. [Leave closed to this job.]

G16. **Local paths in a served file.** `CLEANING-LOG.txt`, now served from globalgrid2050, lists local workspace paths
(Team 5 HANDOFF, issue 17 comment 6868817609, finding f). Not a secret, but it is the kind of content the link rules
keep out. No lane has the fix. [Successor lane S-A below, or the harness directly: regenerate the log with relative paths
under a new commit; the file is new in PR #57, so no pin is broken.]

G17. **Homepage restore snapshot.** The pointer moved without the numbered pre-edit snapshot `homepage_versions/homepage_v139.html`
that the repository's own rules ask for (Team 3 HANDOFF, comment 6868814345, item 8). [ChatGPT, who made the change, or the harness.]

G18. **Runbook says one thing, the night did another.** RUNBOOK section 1 on main says the owner merges and moves the
pointer in person and that a relayed GO is not valid (Team 5 HANDOFF, owner decision 1). The three merges rested on the
owner's chat instructions to the harness and on ChatGPT's relay. [Owner: confirm or reverse; then Team 5's successor
amends the runbook to whatever rule the owner states.]

G19. **Six product questions on convergence** (Team 6, issue 20 comment 6868809262): source of truth, grid rule, the
question the product answers, first surface, data-centre MW, definition of done. [ChatGPT in the owner's terms, or the owner.]

## 2a. Revision 1 (after the HANDOFFs of Teams 3, 5 and 6 at 00:50Z)

Teams 2, 3, 5 and 6 have handed off. Their sections in part 3 stand as the record of what the lane was for; what is
left over is listed here with a proposed successor scope. Only the harness can start a successor.

| Left over | From | Proposed owner |
|---|---|---|
| D1: every exported CSV row on the operative page says `14657/14657 canonical REPD Ref IDs` (a July literal). Patch P1 ready | Team 3 | Successor S-A |
| The operative page still prints `V9.12 CANDIDATE` (ChatGPT, issue 15 comment 6868809519) | ChatGPT | Successor S-A |
| P2: workflow that runs `run_v9_12.sh` and a headless smoke | Team 3 | Harness applies; Team 5's successor lists it among workflows |
| 97 active rows (88 new) absent from live GridAtlas: card expected to fail (code read, UNVERIFIED live) | Team 3 | Team 4 (its item A3); live check by ChatGPT |
| Recount from the public CSV gives 7,798, not 7,775: 23 solar sites print as 1 MW but are 0.996 to 0.99975 MW in the XLSX | Team 3 | Team 1 states the precision rule once, for both lanes |
| News panel is the August-dated Q2 feed; all 29 bound refs still resolve | Team 3 | N1 (its lane already) |
| Pointer and PR #60 rollback written (P, Q) but not rehearsed (shallow history) | Team 5 | Successor S-B |
| 6 of 9 RUNBOOK commands fail argparse; patch ready | Team 5 | Harness applies |
| `run.py` passes `--accept-expected` to build_news by default, so new contract figures skip the owner review the runbook requires | Team 5 | Successor S-B (patch), owner (rule) |
| Four new workflows with push or pull_request triggers against the dispatch-only freeze; one has `contents: write` on pull_request and has made 7 evidence branches; three one-off workflows depend on expiring artifacts | Team 5 | Owner decides; ChatGPT owns the workflows it added |
| Full 355-row served check; served homepage check | Team 5 | ChatGPT |
| Stale public statements: PR #18 files, issue 17 body, `SOURCES.txt` on the evidence branch, `docs/repd/2026-10-q3-ingestion.md` lines 34 and 42 (July bytes "unavailable") | Team 5 | ChatGPT (its files); harness for the docs line on main |
| Convergence code and data patches (01, 02) not applied | Team 6 | Harness, as a draft pull request |
| Prototype `pipelinenews_datacentre_context.json` and the DATA CENTRES tab proposal | Team 6 | Successor S-C (brief line 8b) |

Proposed successor scopes (each is one agent, patches only, same rules as the lanes):

- **S-A, Pipeline News successor release folder.** Outcome: a new folder beside 202611132345 (never an in-place edit of
  the served, hash-pinned folder) carrying P1, the final label in place of "CANDIDATE", and `CLEANING-LOG.txt` without
  local paths; built by `automation/repd/build_news.py` so it is reproducible. Done when: `run_v9_12.sh` and the P2 smoke
  pass on it; the export column reads `14967/14967`; every figure equals 202611132345's; old folder byte-identical; exact
  pointer instructions written. The pointer move to it is a live step for the harness or ChatGPT with a checkpoint first.
  Traces to brief line 2c. Alternative the owner may prefer: apply P1 in place and accept the label; Team 3 named both.
- **S-B, rollback and CI/CD completion.** Outcome: P and Q rehearsed on a full-history clone of main `1a416f4b`; the
  `--news-review-expected` patch; the Jekyll exclusion patch; the January 2027 procedure; one recorded run of the release
  workflow. Traces to brief lines 1 and 6.
- **S-C, Data Centres in Pipeline News (brief line 8b).** Starts only after G19 is answered, because the first surface and
  the source of truth are among the six questions. Outcome: on a further new release folder, a DATA CENTRES tab on the
  interconnector pattern and one context line per REPD row from Team 6's file, with contract hash; data centres keep their
  own ids; no MAP without geometry; distances labelled straight line.

## 2b. Revision 2 (01:07Z): the 00:56 instructions, new lanes, and simplicity

State: handed off: Teams 1, 2, 3 (twice), 5, 6, N1, N2, N3. Working: Team 4, M1, N4, G1, and ChatGPT on draft PR #65.
globalgrid2050 main `10cc4b40` (PRs #57, #60, #61, #63, #64, #66 merged; #67 open). S-A was adopted: Team 3 delivered
successor folder 202611140058. S-B and S-C are still proposals.

### Simplicity (brief line 13): what to cut or merge

The owner's 00:56 words: "Simple. Do not over-complicate." Measured against that, the night has produced duplicates.
One owner each, or remove:

| Duplicate | Where | Proposal |
|---|---|---|
| Three article-to-project binders | N1 `scripts/news_binder_refaware.py` (on main, PR #66); N3 `automation/news/binder.py` (PR #67; precision 1.00, recall 0.98 on 133 items); N2's binders inside its pipelinenews patch 01 | Keep N3's as the one binder. N1's stays only as the legacy builders' internal step until it is switched to call N3's; no new work on it. N2's is not applied unless pipelinenews is revived (owner decision) |
| Two news fetchers for the same feeds, each with its own scheduled workflow | ChatGPT PR #65 `automation/energy24/scan.py` (hourly; DESNZ, DCD, Energy-Storage.news, pv magazine); N4 `automation/news/datacentre_feed.py` (daily; BBC, GOV.UK, Parliament, DCD) | One fetcher and one scheduled workflow writing one headlines file with one schema. See the N4 scope below |
| Two event sources for "what changed in REPD" | `automation/repd/diff.py` change reports; N3 `events.py` | Not a duplicate in code (events read the diff), but only N3's events should be shown to readers |
| Two served copies of the October page | 202611132345 (fixed in place by PR #63) and successor 202611140058 | After the successor is promoted, the harness restores the three files of 202611132345 as it has said (6868920602); no third folder for the same data |
| Three draft QA pull requests | #58 (targets a merged branch), #59, #62 | ChatGPT closes them once their run ids are on the link, or merges the one workflow worth keeping |
| Evidence branches and one-off workflows | 7 `repd/2026-10-reviewed-evidence-*` branches; three October one-off workflows tied to expiring artifacts | Keep the two archive branches that hold original bytes (July archive, final October evidence); prune the rest (owner's word needed, Team 5 decision 5) |
| Status documents | `FIXES/NL-017/STATUS.md`, PR #18 ACTIVITY.md, this folder's LOG.md, OWNER-INSTRUCTIONS.md Part 3 | One progress table: OWNER-INSTRUCTIONS.md Part 3. STATUS.md retired. LOG.md stays as the append-only record |
| Legacy news runners | 14 of 15 lineage runners fail in both folders by design (Team 3) | Leave; do not carry them into further successors beyond what the pattern requires |

Not for cutting, because the owner asked for it or it protects his work: hash pins, the additive rule, restore points,
the 43-check acceptance, the release folder's own tests.

### New lanes

**M1, monthly REPD (brief line 10).**
- Outcome: REPD on the site follows the government publication without anyone asking. The publication is quarterly, so
  the monthly job is a check that acts only when the published files have changed.
- Done when: (1) one workflow file with a monthly schedule and manual dispatch; (2) step one compares the publication's
  current CSV and XLSX hashes with the latest release descriptor in `automation/repd/releases/` and exits "no change"
  when equal; (3) on change it runs the existing `automation/repd/run.py` (no second pipeline) and opens a pull request
  with the change report; it never pushes to main and never moves a pointer; (4) the three failure cases are tested:
  publication unreachable, files changed but validation fails, old URL serving new bytes (which happened this quarter:
  the July URLs returned October bytes); (5) one recorded run on GitHub ending "no change" against the October hashes
  `48e76c49…` and `87811e24…`; (6) a paragraph in the runbook; (7) patch passes `git apply --check` on main; HANDOFF on
  issue 12 with files in `FIXES/NL-012/M1`.
- Inputs: main `10cc4b40` with Team 1's fixes (PR #64: `run.py --offline` now passes, sparse checkout fixed).
- Must not touch: existing data files; the freeze on other workflows (the owner's override covers this one only).
- Simplicity: no new detector service, no new data format, no auto-merge. Whether new Pipeline News contract figures are
  auto-accepted (`--accept-expected`, Team 5 finding c) must be stated one way or the other in the workflow.
- Overlap: Team 5's proposed S-B item "procedure for the next release" becomes this lane's runbook paragraph. The old
  `repd_sync.yml` (ChatGPT, 6867976784) commits to the running branch: M1 states whether it is retired.
- Not covered: Pipeline News release folder and GridAtlas for the new data. M1 should say plainly that after its pull
  request the page still needs a release folder build (`build_news.py`) and a pointer move, and who does that.

**N4, data-centre capex and politics (brief line 11).**
- Outcome: a small feed of headlines in two groups (capex, politics) and one panel on the operative Pipeline News page.
- Done when: (1) one JSON file, newest items first, each with headline, link, source, published time, group, and, only
  on an exact name or alias match, a data-centre id from the 226-record register; (2) headlines and links only, no
  article text; (3) keyword rules listed in one place and tested on fixtures, including false-positive cases; (4) the
  panel is one script, hidden when the file is absent or empty, shown on the successor folder rather than patched into
  a served one; (5) headless screenshot desktop and mobile; (6) patch passes `git apply --check`; HANDOFF on issue 19.
- One fetcher, with ChatGPT's PR #65 (ChatGPT asked the coordinator for a non-overlapping plan in 6868955209). Proposal:
  the scheduled fetch lives in one place. ChatGPT can reach the feeds and N4 cannot, so the fetcher and its workflow are
  ChatGPT's `automation/energy24/scan.py`, extended with N4's source list (BBC sections, GOV.UK DSIT and DESNZ Atom,
  Parliament bills) and N4's two groups; N4 delivers the classification rules, the register join, the fixtures and the
  Pipeline News panel, reading the file the fetcher writes. N4 does not add a second workflow. If ChatGPT prefers the
  reverse (N4's module fetches, Energy24 reads its file), that is equally simple; what matters is one schema and one
  schedule. The schema is agreed on issue 19 before either side builds further.
- Rules both sides have already stated and that the single feed keeps: REPD Ref ID is the only key for a UK renewable
  project and is attached only on exact evidence; data-centre ids are separate; proximity from Team 6's file is shown as
  straight-line context; no cost-per-MW inference; neutral wording.
- Size: the owner's words to Claude ask for simple; the specification relayed by ChatGPT describes six market clocks,
  an hourly watch, and cybersecurity and ethics sections on a separate Energy24 page. This file does not rule between
  them. It records that the panel (N4) is the part brief line 11 asks for, and that the Energy24 page is ChatGPT's lane
  under its own relay; the owner decides how much of it he wants.
- Must not touch: pinned feeds; served folders in place; N3's module except to import it.
- Overlap: N3's scoring can rank these items later through the same interface; not required for done. S-C (data centres
  as a table category) is a different thing: N4 shows news about data centres, S-C shows the data centres themselves.

**G1, GridAtlas exploration (brief line 12).**
- Outcome: a plain inventory of what GridAtlas already holds and shows, taken from the running page in a headless
  browser, so that other lanes reuse it instead of building.
- Done when: (1) a table of layers (offtakers, data centres, substations, REPD register, others found) with record
  counts, id fields, source and generation, each with a screenshot; (2) what the data-centre tap card shows today (Team 6
  reports it lists 30 REPD sites within 40 km and 30 substations from the map's own register); (3) for each of Team 6's
  questions 1, 2 and 4 (source of truth, grid rule, first surface), what GridAtlas already implies as the answer;
  (4) a short list: "already in GridAtlas, do not rebuild" against N4, S-C and Team 6's proposal; (5) the live-map
  behaviour for a sample of the 97 active rows absent from the live registry, if Team 4 has not reported it;
  (6) HANDOFF on issue 16, files in `FIXES/NL-016/G1`.
- Inputs: gridatlas clone `41729af` served locally; live generation 202610312138.
- Must not touch: gridatlas, `atlas/current.json`, `STATE.md`. Exploration only; any build it suggests is a new decision.
- Overlap: Team 4 owns the preview package and the legacy pages; G1 owns the inventory. Item (5) belongs to whichever
  reports first; the other cites it.

### Changes to existing scopes in this revision

- NL-013 Team 1: met. Left to the owner: D9 and D10.
- NL-015 Team 3: S-A met as patches (successor 202611140058, comment 6869028602). Remaining steps are the harness's
  (apply S1 to S3), ChatGPT's (gates, second promotion) and then the harness's again (restore the three files, S2).
- NL-016 Team 4: unchanged, but it has posted nothing since its ACK at 00:25Z; under line 13 its first deliverable
  should be the smallest useful one: item A3 and the per-page table, before the preview package.
- NL-019 N1, N2, N3: met as patches. The binder duplicate is in the table above. N2's work applies only to the
  pipelinenews repository, where every discovery workflow is disabled and there is no push route: it waits on an
  owner decision whether that repository is revived, and should not be extended meanwhile.
- NL-020 Team 6: unchanged; on main as data.
- S-B (rollback rehearsal, Jekyll exclusion, `--news-review-expected`, pruning): still unowned. The next-release
  procedure moves to M1.
- S-C (brief line 8b): still unowned and still waiting on Team 6's questions 3 and 4; G1's inventory may answer 4.

## 2c. Revision 3 (2026-11-14T01:29Z): the version train, and what the handed-off lanes leave for it

State: every Claude lane started before 01:20Z has handed off (Teams 1 to 6, N1 to N4, M1, G1). Working: the guardian
(brief line 15) and ChatGPT. globalgrid2050 main `3f136bfa`.

Correction to section 2b: the row "two served copies of the October page ... no third folder" is withdrawn. The owner
has since asked for a new version about every 30 minutes with old versions kept (brief line 15). His word outranks the
simplicity cut.

### Guardian: Pipeline News version train (brief line 15)

- Outcome: a chain of version folders from parent 202611140058, each published at its own address even if broken, each
  judged by one CI workflow against its parent, ending in one release candidate whose map links and Ventus Grid Engine
  deep links work; old versions stay.
- What the train must carry, from the lanes that have handed off (this is the lane's backlog, in the order the owner's
  brief gives weight):
  1. The star feature. Team 4 measured the 7,775 MAP links of the operative page against the live map (issue 16,
     6869215161): 5,246 resolve with an identity card; 97 active rows get no card; 12 resolve to a point that moved; 26
     links carry no usable point. A version cannot fix the map from the page side: the cure is the October register in
     GridAtlas (Team 4's patch-0 and P1, which only the owner can push). Until then the release candidate should say on
     the page which rows have no card yet, rather than show a link that half works. Done for the star feature: every
     MAP link either opens the right card on the live map or is marked; checked on the live site by ChatGPT.
  2. N4's panel (data-centre capex and politics, brief line 11): the feed is on main, the panel is on no folder.
  3. N3's events feed (official register changes) shown as its own labelled list, not as news stories (ChatGPT's
     condition in issue 19, 6869043996).
  4. G1's data-centres page (PR #72) linked from the page, if the harness merges it.
  5. Team 3's left-overs: the news panel still shows the August-dated feed; county "tock" and refs 18561 and 18562 are
     as published.
- Done when: (1) the guardian has posted an ACK on issue 15 with its rules; (2) `versions.html` lists every version with
  parent, time, CI verdict and what changed, in one line each; (3) the CI workflow fails a version that drops records
  (7,775), changes a pinned figure, breaks the export column, or loses a MAP link its parent had; (4) no version edits
  an earlier folder; (5) the homepage pointer is never moved by the train: a release candidate is announced on issue 15
  and promoted by ChatGPT or the harness with a checkpoint; (6) a stated end: when the release candidate is promoted the
  train stops or drops to "on change".
- Size, the one constraint the owner's words do not mention and the repository imposes: 202611140058 is 230 files and
  46.7 MB; 202611132345 is 232 files and 70.2 MB (git trees API, 01:27Z). A full copy every 30 minutes adds roughly
  90 MB an hour to a repository of about 360 MB and to a Pages site with a 1 GB limit. So a version should hold only
  what differs from its parent and read data and fixtures from the parent (as 202611140058 already does for the 2026q3
  fixtures), with a per-version size budget checked in CI. "Keep old versions" is then cheap.
- Must not touch: earlier folders; the homepage repository; gridatlas; the pinned Q2 feeds.
- Overlap: Team 3's lane ends where this begins. ChatGPT's Energy24 page (PR #65) is a separate page; the two should
  read the same headlines file.

### Line 14: Compare the Cloud

Owned by the harness (PR #70 on main; cyber-resilience PR #1 open) with ChatGPT as checker and publisher. Done when
ChatGPT has confirmed the link, the neutrality of the two-sentence summary and the rendering, and merged; and the feed's
pinned-items file names the source and date. Nothing else is in scope: one entry, additive.

### Line 8b after G1

G1 found that GridAtlas already answers "what renewable capacity is near this data centre" on its Offtakers card, and
delivered one new page (PR #72) listing the 226 sites with October figures. That is the simplest form of line 8b and
replaces the proposed S-C unless the owner wants data centres inside the Pipeline News table itself. Two things to state
on that page so it does not contradict the map: it counts solar, battery and wind from the October register; the
GridAtlas card counts all technologies from the July register (Bedford: 303.8 against 403.3 MW within 10 km).

### Fetchers and binders (update to the simplicity table)

- Fetcher: N4's `automation/news/datacentre_feed.py` is on main and has run on GitHub (nine feeds, daily). It is now
  the existing one; the simple course is that ChatGPT's Energy24 reads its file (branch `datacentre-news-data`) for
  data-centre items rather than scanning the same sources hourly. ChatGPT's scanner would then cover only what N4's
  does not (energy-storage and solar trade press).
- Binder: both N1's and N3's are on main. ChatGPT's rule (issue 19, 6869043996): no name-only binding is published;
  only exact REPD Ref evidence promotes a match, everything else goes to a review queue. That rule makes the choice
  moot for readers; for code, N3's stays the one to extend.

### Still without a lane

S-B (rehearse pointer and full rollback on a full-history clone; restate no-truncation for main after PRs #63 to #71;
exclude rendered `.md` pages from the Pages build; `--news-review-expected`; prune one-off workflows and evidence
branches; replace local workspace paths in files on main: the served `CLEANING-LOG.txt` (Team 5) and a test in the
monthly-workflow patch as delivered, which points at a local folder for the official October files; whether main carries
that line is UNVERIFIED). The public language gate. N2's pipelinenews patches (owner decision). The gridatlas push (owner).

## 2d. Revision 4 (2026-11-14T01:50Z): the star feature as one sequence across two lanes

New from the owner at 01:26Z (brief line 16): the map link, its grid engine and the offtakers layer must not be broken,
only adapted to the October additions. The guardian's ACK (issue 15, 6869481646) and the GridAtlas preview (issue 16,
6869603567) both respect this: the page never alters a MAP href; the map's live generation is untouched.

Lines 15 and 16 are one piece of work in two repositories, and its steps have different owners. In order:

| Step | Owner | Done when |
|---|---|---|
| 1. Preview generation 202611132345 checked in a real browser, desktop and phone (five checks in 6869603567) | ChatGPT | Results on issue 16 |
| 2. Acceptance of the GridAtlas generation | Owner only | His own "ACCEPT 202611132345" on gridatlas PR #84 |
| 3. Release of the generation | Harness (the release script), after step 2 | `atlas/current.json` moved by the prescribed tool; rollback generation named |
| 4. Re-run of the guardian's register check against the live register | Guardian | The list of rows without a card shrinks from 97 to the residue; marks on the page follow the list, not a fixed number |
| 5. The residue: refs 2484, 6483, 20218 lack a card even against the preview register | Unowned. Proposed: the guardian states the reason for each from the register and the REPD row (status, coordinates, capacity) | One line each on issue 15 |
| 6. Release candidate named and promoted | Guardian names; ChatGPT or the harness promotes with a checkpoint | Homepage opens a version in which every MAP link opens the right card or is marked |

Added to the guardian's scope, the only points its ACK leaves open: a stated end of the train (after step 6 it stops or
runs on change only); the 17 MB budget enforced in CI from V9.15 as promised; and that a marked row is unmarked by data
(the register check), never by hand.

For the offtakers side of line 16, G1's finding stands as the test: on the preview, a data-centre card should list
October additions among its nearest REPD sites (check 4 of step 1).

## 3. Scope per lane

### NL-013, Team 1: source and dataset QA

Traces to brief line 2a (and contributes to 6).

- Outcome: an independent statement that the October datasets on main are complete and correctly derived, plus patches
  for any defect and for test gaps.
- Done when: (1) `repd-2026q3.csv` re-derived from the two official files with fresh code and compared cell by cell,
  with the 832 logged changes matched exactly and 0 unexplained; (2) each subset and `dist/*_2026q3.json` recounted
  from first principles (2,181 / 1,229 / 940 / 11,293 / 14,967 / 3,765); (3) every gate in `automation/repd` shown to
  fail on a crafted bad input; (4) full test suite and `run.py --offline` run from a clean archive of **main** (now
  `1a416f4b`, not the PR head), counts stated; (5) a defect table with severity, each with one patch that passes
  `git apply --check` against main; (6) `REPORT.md` and one HANDOFF on issue 13.
- Inputs: official CSV `48e76c49…`, XLSX `87811e24…`; `repd-2026q3.csv` `d937ae16…`; main `1a416f4b`.
- Must not touch: any repository (patches only); the July baseline files (Team 2 delivered them in PR #60).
- Added to the original scope: state independently whether the ref 15915 Address difference (CSV `?`, XLSX U+200D) is
  the only CSV/XLSX text difference, since ChatGPT's 43-check run waives that one cell; and say whether any Team 1
  defect is serious enough to matter for a page that is now the homepage's operative release.
- Overlap: Team 3 recounts the Pipeline News figures (7,775); Team 1 stops at the datasets. Team 2 owns anything about
  July. Team 5 owns hash pins of pre-existing files.
- Hands over to: harness (patches), Team 5 (defect list for the gate table), N1 and N3 (confirmed 3,765 and identity file).

### NL-014, Team 2: July baseline (finished)

Traces to brief line 2b.

- Delivered: both July originals match their pins; July to October +319 / −9 / 14,648 retained, 373 status changes;
  patch merged as PR #60 (`67635070`). HANDOFF: issue 14 comment 6868663705.
- Left open by the lane, each needing a named decision, none blocking: (a) why workbook `99ec4d05…` differs in bytes
  from `624a0a97…` (file not available; owner or ChatGPT to supply it, otherwise close as unexplained with identical
  content on all 14,657 records); (b) whether the July originals are copied into main (owner).
- No further work is in scope unless a later finding touches July figures.

### NL-015, Team 3: Pipeline News release 202611132345

The situation changed under this lane: the page it was testing as a candidate became the homepage's operative release
at 00:45:55Z. The scope is therefore the same nine checks, re-aimed.

Traces to brief line 2c.

- Outcome: evidence that the release folder on main behaves correctly as the operative Pipeline News page, and a list of
  defects ranked by what a reader would see.
- Done when: (1) headless desktop and mobile runs of the folder from **main** show 7,775 records, filters, search,
  pagination and CSV export working, with the status vocabulary and blank capacity handled; (2) visible differences from
  202609082224 listed; (3) every pinned figure in `release.v9.1.json` and `release.v9.5.1.json` recounted; (4) every MAP
  href checked for form, and the hrefs of the refs added since July passed to Team 4; (5) a statement of what the news
  panel shows on the new page (the Q2 feed `major_project_news_v9_5_1.json` bound against October refs) and whether any
  item now points at a removed or changed project; (6) patches P1 and P2 final, each passing `git apply --check` on main;
  (7) `REPORT.md`, public copies in `FIXES/NL-015/`, one HANDOFF on issue 15.
- Changed: patch P3 (homepage `data/homepage.json` pointer) is overtaken by homepage PR #9. Do not deliver it as a patch.
  Instead compare P3 with what PR #9 contains, if ChatGPT posts the diff or the file (the homepage repository is not
  readable from the Claude workspace), and report differences in label, URL, `source_ref` and the promotion record.
- Inputs: main `1a416f4b`; folder `index.html` `97756fc3…`, build manifest `eb59fee0…` (as served, per run 43535706937).
- Must not touch: the folder's files on main except through patches; the homepage repository; pipelinenews.
- Overlap: ChatGPT's PR #58 and PR #59 browser runs cover load, pager, export and two MAP links at three widths. Team 3
  should not repeat those; its added value is filters, status vocabulary, blank capacity, every-row MAP hrefs, figure
  recounts and the news panel. Team 4 owns whether GridAtlas resolves a ref. N1 owns any new news feed.
- Hands over to: harness (P1, P2), Team 4 (href list), N1 (news-panel finding), Team 5 (defects for the gate table).

### NL-016, Team 4: GridAtlas and legacy maps

Traces to brief line 2d.

- Outcome: (A) a GridAtlas preview package the owner can push, with its failing checks explained; (B) a decision file for
  each legacy atlas page in globalgrid2050: switch to the October files, or stay on January as a historical build.
- Done when: (A1) each of the 3 failing pr-gate checks is shown to fail on the unmodified clone too, or is fixed in the
  patch; (A2) the capacity-precision question is settled with the three join counts (10,503 / 10,423 / 8,973) and one
  recommended rule; (A3) **new:** for the 319 refs added in October, a table of what the *live* GridAtlas generation
  202610312138 returns today for a MAP link from the promoted page (resolves, resolves to a different project, no
  result), and the same for the preview; (A4) preview PR text and exact file list. (B1) per-page table: what it reads
  now, what changes on October data, headless render result on both, recommendation; (B2) the optional switch patch
  split so each page can be applied alone; (B3) `REPORT.md`, public copies in `FIXES/NL-016/`, one HANDOFF on issue 16.
- Inputs: gridatlas clone `41729af` (v9.188); main `1a416f4b`; `dist/repd_master_2026q3.json` `3ffe6c5c…`.
- Must not touch: `atlas/current.json`, `STATE.md`, immutable atlas releases, any live page. The legacy switch is the
  harness's step to take with a checkpoint (it has said it will switch pages when browser tests pass, unless the owner
  says otherwise); the lane supplies per-page evidence and marks pages that are historical builds and should stay.
- Overlap: Team 3 (MAP hrefs on the page; Team 4 owns the GridAtlas answer). Team 6 proposes a data-centre layer for
  GridAtlas; Team 4 owns what GridAtlas can load, Team 6 owns the data. ChatGPT's run 43535706937 tested two refs
  (9873, 2472) on live GridAtlas, both of which predate October.
- Hands over to: owner (gridatlas push, per-page choice), harness (legacy patch), Team 6 (layer contract).

### NL-017, Team 5: release gate, CI/CD, rollback

Traces to brief lines 1 and 6.

- Outcome: one table of gates with PASS / FAIL / UNVERIFIED and evidence, and a rollback procedure that matches what is
  live now. The lane approves nothing.
- Done when: (1) no-truncation proof restated for main `1a416f4b`: files added, modified, deleted against `73cbdec1`
  across all three merges (#57, #60, #61); (2) **new:** rollback rewritten in two layers with an order: first the
  homepage pointer (pin `catalogue/homepage-owner.json` back to owner commit `9914285b`, and the homepage repository's
  operative release back to 202609082224), then, only if needed, the data merge; each rehearsed in a throw-away clone on
  the real main tree, with the result of reverting the data merge *without* the pointer stated plainly; (3) **new:**
  `served-manifest.tsv` updated so the homepage rows expect the new pinned hashes (`index.html` `e3b011cf…`,
  `data/homepage.json` `d81d9a9c…`) and a row checks that the homepage links to `/uk_renewables_pipeline/202611132345/`;
  (4) a mapping between the lane's 355-row manifest and what ChatGPT's run 43535706937 actually fetched (8 files), so
  the uncovered rows are known; (5) list of workflows now on main that fire on push or pull request, including the two
  added with PR #61 and any from PR #56, and what each can write; (6) the public language gate: run locally if possible,
  otherwise listed as not run on three merges; (7) RUNBOOK and AUTOMATION checked against code, with the patch;
  (8) patch excluding the 32 rendered `.md` pages from the Pages build; (9) `STATUS.md` brought up to date or retired;
  (9a) a written procedure for the next quarterly release (January 2027) and one recorded run of the release workflow
  on GitHub, or the reason it cannot run;
  (10) `REPORT.md` and one HANDOFF on issue 17.
- Inputs: main `1a416f4b`; baseline `73cbdec1`; restore branch `restore/pre-repd-2026q3-20261114`; testcode backup
  folder `backups/202611140031-repd-2026q3-pre-release`; PR #61 diff.
- Must not touch: any repository; no revert is executed, only rehearsed locally.
- Overlap: Team 1 (gates inside `automation/repd`: Team 1 attacks them, Team 5 reports their CI results). ChatGPT's
  PR #59 workflows duplicate part of the served-byte script; the lane's manifest is the wider one and should be the
  reference list.
- Hands over to: owner and harness (gate table, rollback), ChatGPT (manifest to run from a machine with site access).

### NL-019, news agents N1, N2, N3

Traces to brief lines 7a (N1), 7b (N2), 7c (N3).

Shared rule from the posted requirements (issue 19 body; issue 20 comment 6868599730): three evidence tiers (official
record, attributed reporting, unverified lead), source URL and time kept, entity resolution logged, data centres a
separate category, proximity never stated as connection. New files under new names only; the pinned Q2 feeds and
`major_project_news_v9_5_1.json` (`cea104c3…`) stay byte-identical. Nothing in this lane is published without a
checkpoint to the harness.

Ownership of the three overlaps:

| Shared thing | Owner | The others |
|---|---|---|
| Name and operator normalisation, article-to-project binder, confidence classes | N3 (`automation/news/binder.py`) | N1 measures the legacy binder against N3's labelled set and patches the legacy builders to call the shared code or documents why not. N2 uses it for discovery output and does not write a third binder. |
| Labelled evaluation set (article, project, correct or not, provenance) | N3 | N1 contributes pairs from the V5/V6 caches and existing feeds; N2 contributes failure samples from the 8,756-row corpus. One file, one schema. |
| Events from the July to October diff (newly consented, refused, under construction, operational) | N3 (`automation/news/events.py`) | N1 does not build a second generator; it consumes N3's events as its "no-article" candidates. |
| Data-centre ids and proximity | Team 6 | N2's DATA_CENTRES topic and N3's proximity component read Team 6's output and ids; neither re-derives distances. |

**N1, legacy builders on October data.**
- Outcome: the existing signal and headline builders documented and run against `dist/major_projects_2026q3.json`
  (3,765 = 3,484 solar + 281 battery), with an October-bound feed under the new name `dist/major_project_news_2026q3.json`.
- Done when: every hard-coded count (125 / 37 / 8 / 45 / 133; Q2 universe 3,714) is located by file and line and marked
  "data-derived" or "must change per quarter"; the offline run states how many of the 133 items still bind to an October
  ref, how many bind to a ref whose status changed, and how many lose their project; exactly which steps need
  `news.google.com` is listed for ChatGPT or the owner; the patch passes `git apply --check` on main and its tests pass;
  `REPORT.md` and public copy in `FIXES/NL-019/N1/`.
- Must not touch: pinned feeds; the release folder's `newspaper-v9-5-1.js` behaviour (Team 3 reports what the panel shows).

**N2, discovery tooling.**
- Outcome: a map of the discovery chain (discover → dedup → topic → bind → release) marking each step live, disabled or
  broken, and a patch that lets it pick up a new REPD quarter safely.
- Done when: the ten reverted priority-source commits of 26 Sep 2026 are explained from the history; reconcile-provisional
  run offline against the 7,775-project list with counts of provisional items resolving to refs added since July; bind
  rates (0 / 1 / more than 1 project) measured on the corpus with samples; patch plus tests for new-quarter pickup and
  for the DATA_CENTRES topic using Team 6's ids; list of network and key-dependent steps; `REPORT.md` and
  `FIXES/NL-019/N2/`.
- Must not touch: Ventusltd/pipelinenews (patches only); nothing from the private repository
  pipelinenews-gridatlas-20260906 may be quoted in a public file or comment.
- Note: the priority BBC RSS work in the lane's folder is inside this scope only as an offline tool with tests; turning
  on a scheduled workflow is a live step for the harness and owner.

**N3, relevance model.**
- Outcome: `automation/news/` (events, relevance, binder) as a deterministic, explainable module with a feed under the
  new name `dist/news/repd_events_2026q3.json`.
- Done when: events built from the corrected July to October diff (the PR #60 version, where the 55 artificial Offshore
  Wind Round changes are gone) and the event counts reconcile to +319 / −9 / 373 status changes; every score component
  is present in the output; evidence tier is a field, not a weight hidden in the total; binder precision and recall
  reported on the shared labelled set; the data-centre component reads Team 6's file and is absent, not zero, when the
  file is missing; pytest passes; the patch passes `git apply --check` on main; design note; `REPORT.md` and
  `FIXES/NL-019/N3/`.
- Must not touch: N1's legacy builders, N2's tooling, pinned feeds. No commentary on named companies in public output.

Hand-over for all three: one HANDOFF each on issue 19; patches to the harness. Where the feed should appear (the new
page's news panel, a separate page) is undecided and belongs to the owner; the lanes deliver files, not placement.

### NL-020, Team 6: REPD × data-centre convergence

Traces to brief line 8a. Line 8b (the category inside Pipeline News) is not in this lane: see G13.

- Outcome: one deterministic join, as source-only versioned JSON, CSV, schema and input-hash manifest under
  `dist/convergence/2026q3/` with code in `automation/convergence/`, plus a product proposal that names the exact fields
  Pipeline News and GridAtlas would read.
- Done when (from ChatGPT's posted brief, comment 6868599730, turned into checks): (1) inputs pinned by sha256 in the
  manifest (`repd-2026q3.csv` `d937ae16…`, identity `b4fcf35c…`, data-centre register `87337db5…`, connection points
  `8db7171d…`, substations `ec5450aa…`); (2) 5 / 10 / 25 / 50 km results labelled straight-line; CRS conversion tested
  with a negative case for a wrong CRS; (3) negative tests for duplicates and false name matches; (4) data-centre demand
  MW never added to generation MW, IT load and grid-connection MW in separate fields, unknown kept unknown; (5) every
  co-location row carries its evidence class and the word candidate; class D (same-site proximity, 202 rows at present)
  is not presented as a relationship; (6) excluded records listed with reason (32 without coordinates, 3 outside range,
  refs 18561 and 18562); (7) two runs give byte-identical output; (8) roll-ups are aggregates, with no commentary on
  named companies; (9) patch passes `git apply --check` on main, tests pass; (10) `REPORT.md`, public copy in
  `FIXES/NL-020/`, one HANDOFF on issue 20.
- Source of truth for data centres: the register released with GridAtlas generation 202610312138 (226 records). Issue 19
  also names Ventusltd/data-centres-gb (`12c24a6`); the lane should state in one paragraph how the two relate and which
  ids it keeps, since N2 and N3 will key on them.
- Must not touch: the REPD datasets, GridAtlas, any page. Data centres stay a separate category and never receive a
  REPD Ref ID. Private market analysis stays out of every public file.
- Overlap: N2 and N3 (they consume this lane's ids and distances); Team 4 (GridAtlas layer contract). The lane owns the
  join and its schema; it does not build news scoring or a map layer.
- Hands over to: harness (patch), N2 and N3 (file path and schema as soon as it is stable, before the final HANDOFF),
  Team 4 (layer fields).

### NL-012, ChatGPT (Agent A) and the harness

Traces to brief lines 3, 4, 5 and 9.

- ChatGPT, as seen on the link: owns gov.uk reach, real-browser and live-site checks, the QA pull requests #58 and #59,
  the homepage repository change (PR #9) and the pin (PR #61). Open items in its lane: final served check of the
  homepage after deploy run 43536366967; disposition of PR #58 and PR #59; the wider served-byte manifest from Team 5;
  the homepage PR #9 diff posted where Claude lanes can read it; the owner's own wording for news and convergence.
- Harness: applies lane patches through pull requests, keeps restore points, decides each further live step, and is the
  only one who starts agents. Checkpoint before each live step, as the owner asked.
- Owner only: acceptance of a release; GridAtlas push; the per-page choice for legacy maps; the offline runner for the
  language gate; whether July originals enter main.

## Revisions

- 2026-11-14T00:48Z first issue.
- 2026-11-14T01:50Z revision 4: brief line 16; the star feature as one sequence with owners (section 2d).
- 2026-11-14T01:29Z revision 3: brief lines 14 and 15; guardian scope with its backlog and a size constraint; line 8b after G1;
  the 'no third folder' cut withdrawn; all earlier lanes handed off.
- 2026-11-14T01:07Z revision 2: owner's 00:56 instructions folded in as brief lines 10 to 13; lanes M1, N4, G1 scoped;
  simplicity table; integration proposal for ChatGPT's PR #65 and N4; Teams 1 and 3 and N1 to N3 handed off.
- 2026-11-14T00:53Z revision 1: Teams 3, 5 and 6 handed off (comments 6868814345, 6868817609, 6868817840); section 2a lists
  what is left over and proposes successor scopes S-A, S-B, S-C; gaps G16 to G19 added.
- 2026-11-14T00:51Z traced to OWNER-INSTRUCTIONS.md Part 2 (section 0); gaps G13 to G15 added; Team 4 legacy switch
  aligned with the harness's stated intent; Team 5 gains the next-quarter procedure.
