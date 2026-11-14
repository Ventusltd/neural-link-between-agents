# Owner's instructions, night of 13 to 14 November 2026, consolidated and compared with progress

Maintained by the coordinator from the harness's compilation (the harness's working copy is its private brief; changes it makes there are merged here, not copied over). Compiled by the Claude harness at 00:50 UTC on 14 November 2026 from the owner's messages to Claude (complete) and
from what is visible of his messages to ChatGPT (screenshots he sent to Claude, and ChatGPT's own posts on the
coordination repository that quote or report him). His long explanation to ChatGPT of the REPD and data-centre
convergence is NOT visible to Claude and is marked as missing below. Wording is lightly cleaned; meaning is not changed.
Times are UK time, which equals UTC.

This document is the reference for the Fable reasoner: every lane's scope should trace back to a line here, and every
line here should have an owner, a state and evidence.

## Part 1. What the owner asked for, in order

### To ChatGPT (as far as visible)

| When | Instruction | Source |
|---|---|---|
| before 21:11 | Find the Pipeline News and REPD repositories in the Ventus GitHub account and bring in the October 2026 REPD release from the government page, preserving existing data and site structure. | ChatGPT screenshot sent to Claude at 21:11 |
| before 21:13 | Back up the old files, with a text log, then start the new data ingestion through GitHub. | owner to Claude, 21:13 |
| about 21:36 | Have Claude check ChatGPT's work and take a more active, collaborative role. | ChatGPT comment 6865514827 on issue 12 |
| about 21:55 | Prepare all specialist work and deploy when verifiable CI/CD and product acceptance gates pass. | ChatGPT comment 6865883681 (ChatGPT's wording) |
| about 22:20 | Leave an audit trail, commit everything as soon as possible, get Claude's sign-off. | ChatGPT screenshot sent to Claude at 22:25 |
| about 23:45 | Keep coordination practical: short notes on the link for material commits, finished CI, findings, blockers and reviewer decisions only; no repeated unchanged-status messages; alert the owner only for a real change, failure or approval decision. | ChatGPT comment 6867837465 (ChatGPT's wording) |
| about 23:55 | The updater may already exist: look at the existing REPD sync workflow before writing new code. | ChatGPT comment 6867976784 ("Owner pointed out we may already have the necessary updater") |
| about 00:25 | Finish October REPD with Claude without requesting additional routine approval. As relayed, this is conditional: it applies after acceptance, CI, browser, rollback and served-byte gates pass, and is not permission to ignore a failed test, edit legacy files silently or claim an unverified deployment. | ChatGPT comment 6868443782 |
| about 00:27 | Phase two: improve the Pipeline News article and relevance algorithm, and bring UK data-centre projects directly into Pipeline News, reusing the established GridAtlas data-centre layers and data federation, not inventing a new source. | ChatGPT issue 19 |
| about 00:36 | Convergence, as written up by ChatGPT: keep it separate from the October ingest; reuse the pinned October REPD and the existing GridAtlas, data-centres-gb and data-grid-gb sources; never mix data-centre demand MW with generation MW, or proximity with a connection; unknown stays unknown; 5/10/25/50 km straight-line screening with source hashes; news scoring separates official facts, attributed journalism and speculative leads; Data Centres a distinct category with no invented REPD id; no MAP without geometry; delivery as versioned files, tests with negative cases, a draft pull request and reviewed browser tests. | ChatGPT comment 6868599730 on issue 20 (ChatGPT's wording, not a quotation) |
| about 00:59 | News specification, as relayed by ChatGPT: public copy professional and neutral; the REPD Ref ID is the only authoritative key for a UK renewable project, with no name or proximity guessing, and data-centre ids kept separate; the lead page puts UK REPD and data-centre-linked investment news first, then major international projects, AI capital expenditure, cybersecurity, ethics; six-market 24-hour watches (London, New York, San Francisco, Hong Kong, Tokyo, Sydney); a project headline qualifies at 50 MW or more, or a separately evidenced commitment of 25 million US dollars or more; never infer cost per MW or convert currency. | ChatGPT comment 6868955209 on issue 19 (ChatGPT's wording; compare the owner's 00:56 words to Claude: "Simple. Do not over-complicate.") |
| unknown | The owner's own long explanation of the convergence of REPD and data centres. | STILL MISSING in his words: only in the ChatGPT conversation |

### To Claude

| When | Instruction |
|---|---|
| 21:11 | Do you have access to my GitHub? (with the government REPD quarterly extract page) |
| 21:14 | ChatGPT is already doing the ingestion. Monitor it so it does not truncate anything. |
| 21:26 | Set up a communication file for today between Claude and ChatGPT in the neural-link-between-agents repository, using the patterns used before. |
| 21:44 | Bring three more Fable agents to compare the current REPD release with older ones and prepare a report of the differences and main highlights. Not on the website: for our own context first. (Sent with two slides: top-50 solar NSIP pipeline and who owns it.) |
| 21:46 | Ask ChatGPT to provide copies of the files. Work aggressively. |
| 22:25 | ChatGPT is sending you messages (it had been told to get Claude's sign-off). |
| 22:31 | Increase the agent count to ten. |
| 23:25 | Just get it done. I will refine later. |
| 23:26 | "Get it done" means: use the current format, ingest the new REPD data, inspect and clean the data with Python. All the past work is in globalgrid2050 and related repositories. |
| 23:27 | Bring fifty Opus agents to crawl all REPD and Pipeline News work, and automate. |
| 23:27 | Tell ChatGPT to help, working through the agents repository. |
| 23:28 | Lots of Python, YAML and workflows already exist in pipelinenews and gridatlas. This is just an update. Use hash keys so months of previous work are not truncated. Take risks: we have git if it goes wrong. |
| 00:23 | Keep the Opus agent harness active, with master agents in teams of ten, five teams, talking to Claude and ChatGPT, progressing autonomously through the agents repository. |
| 00:25 | I want finished, audited CI/CD work. Mistakes are acceptable because git can undo them. Work all night. Two teams of ten is also fine. Use your initiative, talk to ChatGPT, use past patterns for safeguards. After REPD is ingested, work on the news algorithms too. |
| 00:29 | No delays. I want convergence of REPD and data centres; I have explained it at length to ChatGPT. (Sent with a note on big-technology job cuts alongside about 190 billion dollars committed to AI and cloud infrastructure.) |
| 00:30 | ChatGPT has plenty of unused capacity. Work hard, save regularly, make checkpoints, back up old work so it is easy to restore. Use the testcode repository for backups. Work live. Do not wait for approvals. |
| 00:31 | Sent an Excel file named REPD_Publication_Q3_2026.xlsx, for information. |
| 00:41 | Go to automatic mode; stop asking for trivial permissions. I am going to sleep. |
| 00:44 | Run a Fable-quality agent to tie it all together and orchestrate the agents repository with Claude and ChatGPT, as traffic coordinator and reasoner. Work without restraint: it is a public-good repository. |
| 00:45 | Correction: the Fable agent just reads the scopes and improves them. |
| 00:56 | I want REPD to be updated every month. |
| 00:56 | I want data-centre capital-expenditure news and politics in the REPD pipeline (Pipeline News). |
| 00:56 | Simple. Do not over-complicate. |
| 00:56 | GridAtlas already has a lot of data: use a headless Chrome browser and look at it through its offtakers and other layers. |
| 00:56 | Experiment, explore, do not freeze. |
| between 00:56 and 01:18 | Make sure the Compare the Cloud article is there (in the data-centre news feed) and also link it to the cyber-resilience site, using hashes so nothing is truncated; get ChatGPT to check it and publish. (As quoted by the harness in issue 12 comment 6869302028.) |
| between 00:56 and 01:18 | Get versions of Pipeline News published every 30 minutes even if broken, then use CI/CD against earlier versions to deliver a final release. The map and the Ventus Grid Engine deep link are the star feature. Prepare a Fable engineer guardian for that CI integration and keep old versions. (Same source.) |
| 01:26 | The map link already has a very advanced grid engine, as does the offtakers layer. I just don't want this broken, but adapted and flexible to the new REPD additions. (As quoted by the harness in issue 16 comment 6869603567.) |
| 01:52 and 01:53 | Just build a new GridAtlas, bypass the rule, preserving the older one as it is as a version on the website; publish the new one and have CI/CD runs verify it, using the star quantum twin and Kuiper inspired procedures to replicate the new GridAtlas. Don't worry about the rule. (As quoted by the harness in issue 16 comment 6869802620.) |
| 00:47 | First consolidate everything I have said tonight to ChatGPT and to you in a coherent order, and compare it with progress. That is the DNA of the reasoner and quality Fable. |

## Part 2. The same instructions as one coherent brief

1. Protect what exists. Back up old files with a text log before anything changes. Nothing is truncated. Use hashes to
   prove it. Save often, checkpoint before each step, keep backups in the testcode repository, make restore easy.
2. Ingest the October 2026 REPD release. Use the current formats and the existing Python, YAML and workflows in
   globalgrid2050, pipelinenews and gridatlas: it is an update, not a rebuild. Inspect and clean the data with Python.
3. Work as two agents through the agents repository. ChatGPT implements and Claude checks, then Claude also builds.
   Leave an audit trail, commit everything, get Claude's sign-off, keep ChatGPT informed and use its capacity.
4. Understand the release privately first. A comparison of the new release with older ones, highlights, and how it
   bears on the solar pipeline and its owners. Not on the website.
5. Scale and speed. More agents (3, then 10, then 50, then teams with masters), autonomous overnight, live, no waiting
   for approvals, initiative expected, mistakes tolerated because git can undo them, past patterns as safeguards.
6. Finish it properly. Audited CI/CD, automated so the next quarter is routine.
7. Then the news algorithms: Pipeline News article discovery and relevance.
8. Converge REPD with data centres, and bring data-centre projects into Pipeline News from the existing GridAtlas and
   data-centre layers. (Requirements in ChatGPT's wording are on issue 20, comment 6868599730, and in the body of
   issue 19; the owner's own explanation is still missing.)
9. A Fable reasoner whose job is to read every lane's scope and improve it, with this document as its reference.
10. REPD refreshes monthly without anyone asking: a scheduled check that, when the government file has changed, runs the
    existing pipeline and opens the update. (By the owner's direct word this overrides the repository's "all workflows
    manual" freeze for this one workflow.)
11. Pipeline News carries data-centre capital-expenditure news and the politics around it, next to the REPD projects.
    A small, readable feed and a panel, not a platform.
12. Use what GridAtlas already holds (offtakers, data-centre layer, substations): look at it in a headless browser
    before building anything new.
13. Working style: simple, exploratory, keep moving. Simplicity is a criterion for every lane: anything a lane builds
    that the owner did not ask for is cut.
14. The Compare the Cloud article appears in the data-centre news feed and is linked from the cyber-resilience site,
    added without truncating anything there (hash-checked); ChatGPT checks and publishes it.
15. Pipeline News is released as a train: a new version about every 30 minutes, published even if broken, each compared
    by CI with earlier versions, old versions kept, converging on a final release. The star feature is the map and the
    Ventus Grid Engine deep link. A Fable engineer guardian runs the train.
16. The map link, its grid engine and the offtakers layer are not to be broken: they are adapted so that the October
    REPD additions work in them.
17. A new GridAtlas on the October register is published; the older one stays on the website as a version; the
    acceptance rule is set aside for this release by the owner's word; CI verifies the new GridAtlas by replication, in
    the manner of the star quantum twin and Kuiper procedures.

## Part 3. Progress against each point

Kept current by the coordinator (Claude Fable). Last pass: 2026-11-14T02:51Z. Each line names its one owning lane; scopes are in
`SCOPES.md` in this folder. globalgrid2050 main at this pass: `3f136bfa` (PRs #57, #60, #61, #63, #64, #66 to #71
merged; #72 open; #65 draft). Rows 2c, 2d, 8b, 11, 15 and 16 were brought up to 01:50Z (main `3d679cdb`, PRs #72 and #74 merged, #75 open; gridatlas main `41f3f2aa`).

| # | Asked | Owning lane | State | Evidence | Gap |
|---|---|---|---|---|---|
| 1 | Back up, no truncation, hashes, checkpoints, testcode, easy restore | Team 5 (handed off); the harness makes checkpoints | DONE for the first merge; a second checkpoint is reported for the legacy-page switch | Restore branch and testcode backup of 00:31Z; Team 5 gate table (6868817609); harness 6869302028 ("checkpointed in testcode backups/") | No no-truncation restatement for main after PRs #63 to #71. Pointer and full rollback written, not rehearsed. Successor lane S-B still unowned |
| 2a | October datasets | Team 1 (handed off) | DONE, reproduced byte for byte; fixes merged (PR #64) | 6868919369 | D9, D10 for the owner |
| 2b | July baseline and comparison | Team 2 (handed off) | DONE (PR #60) | 6868663705 | Workbook 99ec4d05; July originals into main |
| 2c | Pipeline News on October data | Team 3 (handed off); from 01:24Z the guardian (line 15) | LIVE: 202611132345 operative. On main, not promoted: 202611140058 (V9.13) and 202611140128 (V9.14, with the data-centre news panel); V9.15 in PR #75 | 6869028602; 6869067985 | Second pointer promotion (ChatGPT). Three files of 202611132345 differ from the bytes ChatGPT verified until patch S2 restores them. ChatGPT's live checks unanswered |
| 2d | GridAtlas and legacy maps | Team 4 (handed off 01:20Z) | Legacy: seven current pages now read the October files (PR #71), historical pages left. GridAtlas: patch-0 (two clock-dependent tests) and P1 (22 files, pr-gate 19 of 19) ready; since 01:44Z the preview generation 202611132345 (11,329 rows, October register) is merged in gridatlas beside the live one (PR #84, main 41f3f2aa); and since 01:58Z it is the live generation (gridatlas main b0a3a938; previous 202610312138 kept as a version) | 6869215161, 6869257356; harness 6869603567, 6869802620; FIXES/NL-016 | Live map in a real browser UNVERIFIED (ChatGPT asked). docs/RELEASE.md steps 6 and 7 (homepage label and pin for GridAtlas V9.189, served check) not done. Until then the live map is on the July register: of 7,775 MAP links, 5,246 resolve, 97 active rows get no identity card, 12 resolve to a point that moved. Legacy pages on the live site UNVERIFIED (ChatGPT asked) |
| 3 | Two agents through the repository, audit trail, sign-off | The harness with ChatGPT | WORKING | Issue 12 | ChatGPT's draft pull requests #58, #59, #62 open |
| 4 | Private report | The harness (private) | DONE | Private | |
| 5 | Scale, autonomy, live | The harness | WORKING | 14 lanes started, all but the guardian handed off | |
| 6 | Finished, audited CI/CD | Team 5 (handed off); S-B unowned | NOT FINISHED | Release-folder CI on pull requests (PR #63, #68); monthly workflow (PR #71) | Public language gate has not run on any pull request tonight. Rollback rehearsal, Jekyll exclusion of rendered .md pages, `--news-review-expected`, pruning of one-off workflows and evidence branches |
| 7a | News: existing builders | N1 (handed off) | ON MAIN (PR #66) | 6868976118 | Live crawl UNVERIFIED |
| 7b | News: discovery | N2 (handed off); P1 (handed off 02:28Z) for the pipelinenews release | pipelinenews PR #3 merged as 35c7507f: October release 202611132345-pipelinenews, source only, live pointers unchanged | 6869000917, 6869003251; P1 HANDOFF 6870215097; ChatGPT readback 6870323478 | Not deployed (the release manifest says deployment not authorised) |
| 7c | News: relevance | N3 (handed off) | ON MAIN (PR #67) | 6869000209 | No page reads the events feed yet; ChatGPT proposes a lane for it on its Energy24 page |
| 8a | Convergence join | Team 6 (handed off) | ON MAIN (PR #63) | 6868817840 | Six questions answered by ChatGPT from the owner's standing brief (6870009456). New hold: all 258 source entries of the 226-site register carry licence_status "unverified", and the derived files drop attribution (ChatGPT 6870023614; accepted by the harness, 6870155339) |
| 8b | Data centres beside the REPD pipeline | G1's page (PR #72, merged 01:27Z) | One new page listing the 226 sites with October REPD capacity within 10 km, MAP links and news links | G1 HANDOFF 6869332568 | ChatGPT's answer 4 (6870009456): keep the page and also add a Data Centres category inside a new Pipeline News version. The harness has since stopped adding data-centre content until the licence hold is cleared; the guardian added attribution and a "screening only" note in V9.18. The data-centres page itself (PR #72) still shows no attribution and is in no lane |
| 9 | Fable reasoner | Coordinator | Revision 3 | SCOPES.md | |
| 10 | REPD every month | M1 (handed off) | ON MAIN (PR #71): repd-monthly.yml, 3rd of each month, pull request only when published hashes differ | Run 43540253203 on main: success | After its pull request, a release folder build and a pointer move are still by hand |
| 11 | Data-centre capex news and politics in Pipeline News | N4 (handed off) | Feed ON MAIN (PR #69, #70), daily; panel in version 202611140128 (V9.14, PR #74), which is not the operative release | 6869147650; runs 43539485129, 43539808173 | A reader arriving from the homepage does not see the panel until a version carrying it is promoted. ChatGPT read the live feed file (6870122616, 6870104588): 5 items, one titled "Sponsored", one an investment fund filed as capex, operator-only matches attach sites the headline does not name, no age limit. N4 has handed off: these four fixes have no lane. ChatGPT's Energy24 (PR #65) fetches separately: one fetcher still to be agreed |
| 12 | Use what GridAtlas already holds | G1 (handed off 01:26Z) | DONE: GridAtlas already shows, per data centre, the nearest 30 substations, 30 REPD sites and 30 plants with MW within 5, 10, 20 km; Offtakers is off by default and no URL parameter turns it on | 6869332568; FIXES/NL-016/G1 | GridAtlas counts all technologies from the July register; the new page counts solar, battery and wind from October: the two numbers differ for the same site (Bedford 403.3 against 303.8 MW) |
| 13 | Simple | Every lane | See SCOPES.md section 2c | | Two fetchers; two binders on main |
| 14 | Compare the Cloud article in the feed and on the cyber-resilience site | The harness (feed, PR #70; cyber-resilience PR #1); ChatGPT checks and publishes | Feed: ON MAIN. Cyber-resilience: pull request open | 6869302028 | ChatGPT's check and merge |
| 15 | Pipeline News version train, every 30 minutes, final release with the map and Grid Engine deep link as the star | Guardian (Fable engineer; reports on issue 15) | RELEASE CANDIDATE NAMED 02:46Z: V9.18 = 202611140223 (main 244cb1f8), answering ChatGPT's V9.16 review point by point; V9.14 to V9.17 kept; none promoted | Guardian ACK 6869481646; FIXES/NL-015/VERSIONS.md; run 43541314987 | End stated: five hours from 01:23Z, or on the harness's word, or on-change after promotion (guardian 6870049208). Against the released October register 5,331 of 5,334 active rows resolve; the 3 that do not are Norfolk Vanguard East and West and Norfolk Boreas (refs 2484, 20218, 6483; 4,160 MW together) at 2.55 E, outside the compiler's 2.5 E bound: no lane owns that fix. Guardian HANDOFF 6870447086: attribution block, precision labels, location-only link wording and feature probes in CI. Left: live browser and served-byte checks and the promotion (ChatGPT); the licence hold decides whether the candidate may carry data-centre content. The post-deploy browser proof job failed on the deploy of 896e7f4b (run 43546300437, job verify_v9_7_candidate; build and deploy jobs succeeded): no lane has looked at it |
| 16 | Do not break the map link, grid engine or offtakers; adapt them to the October additions | The harness (gridatlas PR #84, from Team 4's P1); the guardian holds the MAP contract on the page side | RELEASED 01:58Z on the owner's direct instruction to the harness (line 17) | 6869802620; guardian rule: every MAP href identical to its parent's, 7,775 of 7,775 | Browser checks of the live route and of the preserved version (ChatGPT) |
| 17 | New GridAtlas published, old one kept as a version, CI verifies by replication (star quantum twin, Kuiper procedures) | Harness (release, done); Twin Engineer (issue 16, handed off 02:13Z) | RELEASED; twin, preservation and keys checks reported running on gridatlas main 4c52780c (harness 6870155339) | 6869802620: release gates PASS, live-bytes run 43543524737 success, rollback command recorded; Twin ACK 6869802670 | Twin HANDOFF 6870008257: rebuild byte for byte, 224 pins of 53 generations hold, eight mutations caught; pre-existing: 175 part files and 3 old manifests no longer match hashes recorded by older manifests. Homepage label: draft homepage PR #10, made with --skip-acceptance and disclosed. Live browser checks outstanding (ChatGPT says it has not verified them: 6870007228) |

## Part 4. Open points that need the owner or ChatGPT

Only the owner:
- Acceptance of the release; Team 5's seven decisions (6868817609); Team 6's six questions (6868809262); N2's decisions (6869000917 section 6).
- (Done by his instruction at 01:52Z: the GridAtlas release; the acceptance line on PR #84 was posted by the harness and says so.)
- The language-gate runner or a waiver. Which scheduled workflows stand: monthly REPD (his word), daily data-centre news (on main), hourly Energy24 (ChatGPT's draft).
- Whether a data-centres page beside Pipeline News (PR #72) is what he meant by convergence in Pipeline News.

Only ChatGPT:
- Second pointer promotion to 202611140058, and later to the guardian's release candidate; gates on each.
- cyber-resilience PR #1: check and publish.
- Live checks: Team 3's three (6868808787), G1's two (6869332568), the seven legacy pages after deploy of 3f136bfa, Team 5's 355-row manifest.
- One fetcher with N4's feed; PR #58, #59, #62.

The harness:
- S-B; PR #72; N4's panel patch 0003; the guardian's ACK on issue 15.

Resolved since revision 2: S-A (successor on main); M1 on main; legacy pages switched; G1's inventory; N4's feed.

## Corrections and extensions by the coordinator (each with its source)

- 00:51Z Part 1, to ChatGPT: added the 23:45 working instruction (comment 6867837465) and the 23:55 remark that an updater may already exist (comment 6867976784).
- 00:51Z Part 1: the 00:25 instruction as relayed is conditional on gates passing (comment 6868443782); the condition was missing.
- 00:51Z Part 1 and Part 2 line 8: the convergence intent is not wholly missing; ChatGPT wrote requirements on issue 20 (comment 6868599730) and in the body of issue 19. The owner's own words remain missing.
- 00:51Z Part 3 line 2: "homepage still opens the September Pipeline News" and "live site not checked by anyone" were out of date (comments 6868684475 and 6868763314; globalgrid2050 PR #61, main 1a416f4b).
- 00:51Z Part 3 line 3: "PR #56 still open" was wrong (pull request API: merged_at 2026-11-14T00:33:46Z); "served-byte check not yet answered" and "brief not yet posted" were out of date.
- 00:51Z Part 3: lines 2, 7 and 8 split so that each line has one owning lane; line 8b has none.
- 00:51Z Part 3 line 1: gap restated after the pointer move (PR #61 diff of catalogue/homepage-owner.json; FIXES/NL-017/ROLLBACK.md covers the PR #57 merge only).
- 00:53Z Part 3 lines 1, 2c, 6, 8a, 8b and Part 4 updated from the HANDOFFs of Teams 3, 5 and 6 (issue 15 comment 6868814345, issue 17 comment 6868817609, issue 20 comment 6868817840).
- 01:06Z The harness replaced this file with its own copy plus the 00:56 addendum, which removed the corrections above. Restored; the five 00:56 instructions are now in Part 1, lines 10 to 13 in Part 2, and Part 3 is rewritten for the state at 01:06Z (globalgrid2050 main 10cc4b40; HANDOFFs on issues 13, 15, 19).
- 01:06Z Part 1: added ChatGPT's relay of a news specification (issue 19 comment 6868955209). It is wider than the owner's 00:56 words to Claude; both are recorded, neither is edited.
- 01:28Z Part 1 and Part 2: the owner's two instructions given between 00:56 and 01:18 added as lines 14 and 15, from the harness's quotation in issue 12 comment 6869302028 (they were not yet in this file). Part 3 rewritten: every Claude lane started before 01:20Z has handed off.
- 01:50Z Part 1 and Part 2: the owner's 01:26 instruction on the map link, grid engine and offtakers added as line 16, from the harness's quotation in issue 16 comment 6869603567. Part 3 rows 2c, 2d, 8b, 11, 15 updated; row 16 added.
- 02:10Z Part 1 and Part 2: the owner's 01:52 and 01:53 instruction added as line 17, from the harness's quotation in issue 16 comment 6869802620. Part 3 rows 2d, 15, 16 updated; row 17 added. Part 4: the ACCEPT item is closed by that instruction.
- 02:31Z Part 3 rows 7b, 8a, 8b, 11, 15, 17 updated from issue 15 (6870006766, 6870049208), issue 16 (6870008257), issue 19 (6870104588, 6870122616, 6870215097), issue 20 (6870009456, 6870023614) and issue 12 (6870155339).
- 02:51Z Part 3 rows 7b, 8b, 15 updated from issue 15 (6870447086), issue 19 (6870323478) and Actions run 43546300437.
