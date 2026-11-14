# NL-019 NEWS-DASHBOARD audit log (append-only, newest last; times from `date -u`; GitHub's timestamp wins)

## 2026-11-14T10:18Z  AUDITOR B  SETUP  audit trail opened

STATUS: OPEN.
- Owner's instruction of this morning recorded in README.md, with the diagnosis, plan, roles and rules.
- Three studies copied into `studies/` (U updates, S signal, C clutter). Removed before publication: references to
  local screenshot and sketch files. No email addresses, local paths or private-repository content found in them.
- Baseline at opening: operative release V9.20 (`202611140306`); main news file `updated` 22 August 2026.
- Not yet available: scouts' feed and event files, the headlines contract, the algorithm note, either pull request.
- Botley West: the owner's statement ("was refused planning") is unverified at this time; to be checked against
  primary sources and recorded here.

## 2026-11-14T10:19Z  AUDITOR B  FINDING  Botley West: what was decided, by whom, when

STATUS: VERIFIED against the official record. The owner's statement is accurate in substance.
- Decision: development consent REFUSED for Botley West Solar Farm (Planning Inspectorate reference EN010147), an
  application under the Planning Act 2008 by Photovolt Development Partners (PVDP) on behalf of SolarFive Ltd.
- Decision maker: Baroness Curran, Parliamentary Under-Secretary of State, on behalf of the Secretary of State for
  Energy Security and Net Zero.
- Date: 10 November 2026.
- Sources opened by the auditor today:
  1. Planning Inspectorate project page, https://national-infrastructure-consenting.planninginspectorate.gov.uk/projects/EN010147
     (stage: post-decision; states that development consent was refused on 10 November 2026).
  2. GOV.UK, Department for Energy Security and Net Zero, "Botley West Solar Farm: development consent order,
     Planning Act 2008", published 10 November 2026,
     https://www.gov.uk/government/publications/botley-west-solar-farm-development-consent-order-planning-act-2008
     (names the decision maker; the page itself does not state the outcome).
  3. ITV News Meridian, 10 November 2026, "Planned solar farm in Oxfordshire scrapped as government rejects
     application", https://www.itv.com/news/meridian/2026-11-10/planned-solar-farm-in-oxfordshire-scrapped
  4. Solar Power Portal, 11 November 2026, "UK government refuses 840MW Botley West Solar Farm in first-ever solar
     NSIP no", https://www.solarpowerportal.co.uk/solar-planning/uk-government-refuses-840mw-botley-west-solar-farm-in-first-ever-solar-nsip-no
     (reports that the refusal followed the Examining Authority's recommendation, and that a six-week period for
     legal challenge applies; no challenge is reported).
- Precision: the owner said "refused planning". The decision is a refusal of development consent for a nationally
  significant infrastructure project by a minister, not a refusal of planning permission by a local planning
  authority. For the page, "development consent refused" is the accurate short wording.
- REPD (October 2026 release): Ref ID 12588, site name "Botley West, Botley - Botley West Solar Project", applicant
  "Photovolt Development Partners & SolarFive", solar photovoltaics, 840 MW, status "Planning Application
  Submitted", planning authority "The Planning Inspectorate - National Infrastructure". The register predates the
  decision, so its status does not yet show the refusal.
- Consequence for the matching rule: the headlines say "Botley West Solar Farm"; the REPD site name is a different
  string. Under the rule in force (exact site name plus one agreeing field) these headlines carry NO project and
  must still be shown as headlines. This is the first test the algorithm has to pass: the story appears, labelled
  as a refusal, without a project link presented as fact.
- Unverified: the decision letter itself was not opened (document host not reachable by the auditor); the reasons
  are known only from the two press reports.

## 2026-11-14T10:19Z  AUDITOR B  NOTE  headlines contract received (not yet reviewed in full)

- Fable A wrote the data contract at 10:17Z: branch `pipeline-news-data`, file `dist/pipeline_headlines.json`, schema
  `globalgrid2050.news.pipeline-headlines.v1`. Review follows with the algorithm note and the pull request.

## 2026-11-14T10:32Z  AUDITOR B  REVIEW  scouts done: feeds and ground-truth events reviewed; FEEDS.json and GROUND-TRUTH.json published

STATUS: PASS with limits stated below.
- Input: six feed lanes (58 distinct feed URLs after de-duplication) and four event lanes (37 events). All ten files
  parse as JSON.
- Feeds, what the auditor opened directly today (4): Solar Power Portal (RSS, 50 items, newest 13 Nov 2026; it
  contains the Botley West refusal headline dated 11 Nov); Lincolnshire County Council news (RSS, 20 items, newest
  13 Nov); DataCentreNews UK (RSS, 10 items, newest 13 Nov, no UK site in the newest titles); Energy Global wind
  (RSS, newest 8 May 2026: stale, rejection confirmed).
- Feeds, limit: the auditor's fetch tool refused 14 other feed URLs it tried (GOV.UK atom feeds, BBC, Guardian,
  offshoreWIND.biz, reNEWS, Ofgem, Energy-Storage.news, Construction Enquirer, Data Centre Review). The scouts met
  the same limit and often read a third-party mirror or the publisher's HTML page instead. FEEDS.json therefore
  marks only 5 feeds "use" and 28 "test": the first workflow run's per-feed table is the real test. 25 rejected.
- Events, what the auditor opened (17 source pages across the four lanes; at least three per lane): E1 Botley West
  (four sources), Great North Road, Steeple, Beacon Fen (GOV.UK press releases); E2 Hams Hall, Hunterston, High
  Marnham (Solar Power Portal); E3 Llŷr (Welsh Government), Morgan and Morecambe transmission assets (GOV.UK),
  Vanguard West and East financial close (RWE); E4 Trerice appeal, Wheatenhurst appeal, Bonnyknox (Solar Power
  Portal), Brecks construction start (Renewable Energy Magazine). In every case the headline, date and event were
  as the scout recorded.
- Corrections made: the GOV.UK "development consent decision announced" releases are published by the Planning
  Inspectorate, not DESNZ (publisher label corrected); Bonnyknox: the source does not name the deciding authority
  (changed to "not named in the source"); the TotalEnergies/Steeple item now links the original publisher, not a
  republication.
- Thrown out: 2 events (Carrick Forest: single source is a court opinion, not a headline; Beacon Fen in lane E2:
  duplicate, merged) and 5 sources (two 2025 Gazette application notices, one campaign-site repost, one aggregator
  copy, one republication). 35 events remain; 15 have at least one source opened by the auditor.
- REPD: every Ref ID the scouts gave exists in the October 2026 register with the stated site name. Applying the
  rule in force to the headlines alone: 2 events qualify for a "possible match" (Inch Cape, REPD 2527; Brecks Solar
  Farm, REPD 10087); 1 is ambiguous (Beacon Fen Energy Park: exact name, two REPD rows, 13599 and 13600); 32,
  including Botley West, qualify for none and must be shown as headlines with no project.
- Consequence: under the rule a project link will be rare (2 of 35). That is the rule working, not a fault. The
  test of the fix is that the headlines appear, are fresh and are correctly labelled, not that they are tied to
  rows.
- Fable A reported pull request #95 in Ventusltd/globalgrid2050 (branch `news/pipeline-headlines`) opened at
  10:30Z. Review follows.

## 2026-11-14T10:35Z  AUDITOR B  REVIEW  globalgrid2050 PR #95 (fetcher and algorithm), head `9fa42037`

STATUS: CHANGES REQUESTED (three blocking findings); otherwise sound.
- PR #95 "Pipeline headlines: fresh UK renewables and grid headlines three times a day (data branch)", 13 files,
  opened 10:30Z. Its probe job (run 43585625813) passed: 46 offline tests; 37 feeds fetched from the hosted runner,
  32 ok, 5 failed, 80 headlines kept, newest 13 November 2026.
- This settles most of the "test" feeds in FEEDS.json: the GOV.UK, BBC, Guardian, offshoreWIND.biz, reNEWS,
  Energy-Storage.news, PV Tech, Planning Resource and Construction Enquirer feeds loaded from the runner. Failed:
  news.gov.scot (404), Current News (rejected by the parser), Energy Voice (403), DataCentreNews UK (406), and a
  second Energy-Storage.news URL (403). Ofgem returned no entries.
- Method: the auditor ran the PR's labelling and matching code against the 63 source headlines in GROUND-TRUTH.json
  and against trap titles, using the October 2026 REPD.
- Pass: all 27 ground-truth headlines that come from listed feeds are kept; the Botley West refusal is kept and
  labelled as a refusal; only title, link, source, date and derived labels are stored; one failing feed does not
  stop the run (five failed in the probe and the run completed); sponsored titles are dropped by prefix; the cron
  line is present (`41 4,10,16 * * *`); name-only traps (The Grange, Hill Solar Farm, Kells, Gedling, Rigifa)
  produce no match.
- Blocking B1: a single distinctive word plus a technology word can select the wrong register row. "Revera's
  Hunterston battery storage project starts construction" returns REPD 412 "Hunterston" (5 MW, Abandoned), not
  REPD 10535 (Revera Energy, 400 MW).
- Blocking B2: the contract says the headline must contain the REPD site name exactly; the code accepts a segment
  of the name. In the live probe 4 of 7 possible matches are not the full site name (including Botley West,
  REPD 12588), and all 7 rest on technology alone. They are the right projects, but the rule as written in the
  brief is stricter. A ruling is needed: tighten the code, or accept segments and correct the contract.
- Blocking B3: a failed court challenge is labelled a refusal. Live example, BBC, 12 November: "Challenge to UK's
  largest solar farm plan rejected" is given `refusal` although the consent stands.
- Non-blocking: about 9 of 80 kept headlines are not UK stories ("New South Wales" matches "Wales"); "Branded
  content" is not caught by the sponsored filter; the job timeout is shorter than the worst-case fetch time; the
  failing feeds remain in the list, so the file's status would read "partial" every run; the shared merge function
  is being changed by draft PR #93.
- Full findings with file and line were given to the harness. The auditor made no change to the pull request.
- Also at this time: the engineer guardian reports PR #94 (V9.21, folder `202611141017`) open with CI green.
  Review follows.

## 2026-11-14T10:37Z  AUDITOR B  REVIEW  globalgrid2050 PR #94 (V9.21 page, folder `202611141017`), merged 10:31:13Z as `7067570b`

STATUS: PASS, no blocking finding. The review was made after the merge (the pull request was merged three minutes
after it opened).
- Merged by the repository owner's account at 10:31:13Z; head `dd705a55`; the guardian reports CI run 43585387654
  green. The auditor did not run the browser checks; it compared the folder with its parent `202611140306`.
- The page reads the contract: same URL and schema name; a wrong schema or an empty list is refused.
- Fallback: live file, then the copy saved in the folder, then the sentence "Live headlines are not available at
  the moment." The August list opens only as a labelled archive ("ARCHIVE ... NOT UPDATED").
- Updated label: computed in the browser from the file's `generated_at`; "Stale since ..." after 36 hours or after
  a failed refresh. The typed-in counts and the words "audited snapshot" are removed.
- Possible match: always under the words "Possible match"; never written into the project table. Titles are drawn
  as text.
- Table and MAP: the table script is byte-identical to the parent, `data/` is identical, the column headers are
  the same twelve, and the all-rows MAP link check is part of the release run.
- Notes, none blocking: (1) the homepage still opens V9.20; V9.21 is a candidate, and until PR #95 is merged and its
  workflow has run once V9.21 shows "not available" and the August archive, so the homepage should not move first;
  (2) the stylesheet pins the ACTIONS column at every width to stop the MAP button being cut off at 1440 px; no
  column is added or removed, but two columns now pass under it until the table is scrolled, which is a visible
  change to a table the owner asked to keep as it is; (3) the saved copy in the folder is empty, so in this release
  the fallback is the plain sentence, not cached headlines; (4) archive cards with a name-only match are now
  labelled "possible match", and the NEWS SIGNAL column is unchanged.
- State of the fix at this time: page merged, not yet what the homepage opens; fetcher (PR #95) open with three
  blocking findings; no data file exists yet; the live site is unchanged for a visitor.

## 2026-11-14T10:46Z  AUDITOR B  REVIEW  globalgrid2050 PR #95 re-reviewed at head `0539a68c`; algorithm note and corrected contract read

STATUS: no blocking defect remains; one ruling is open; not yet merged.
- Fable A pushed four further heads between 10:35Z and 10:44Z and wrote an algorithm note. Probe and size-guard are
  green on `0539a68c`; a check named "gate" is still queued.
- Fixed since the first review: B1 (a one-word name now needs developer, planning authority or county; both
  Hunterston test titles give no match); B3 (a legal challenge is now `planning_decision`, not `refusal`); the UK
  word must be in the title (the foreign items are gone); "branded content" is dropped; job timeout 25 minutes;
  the five failing feeds are removed from the list.
- B2, restated: the contract now says what the code does (a whole comma or dash part of the REPD Site Name plus a
  second agreeing thing). That is wider than the brief's wording, "matches a REPD site name exactly". Under the
  code as it stands the Botley West refusal headline carries "Possible match: Botley West, Botley - Botley West
  Solar Project (REPD 12588)"; under the strict reading it would be shown with no project. Both are honest while
  the words "possible match" stay. The choice is the harness's or the owner's; the algorithm note gives the
  one-line change.
- Auditor's re-run: 27 of 27 ground-truth headlines from listed feeds are kept. Fable A's own figures on the
  scouts' full set: 64 of 70 headlines and 36 of 37 events kept; the misses are document titles, not news headlines.
- New since the first review, and outside what the auditor was shown: the feed list is now 50 feeds (30 BBC), with a
  BBC keywords lane and two world-news lanes (data-centre money from Bloomberg and trade titles; China solar from
  pv magazine), each capped at ten items. The code comments attribute these to further owner instructions; the
  auditor has not seen those instructions and records them as reported. These two lanes are not UK news and are
  labelled as such in the file's scope sentence. Bloomberg's feed terms were not checked by any scout.
- Open, non-blocking: the shared merge function is imported from the data-centre feed, which draft PR #93 would
  change; "BBC first" is fetch order only, the V9.21 page orders by date; exact name plus technology is in effect
  name-only when the technology word is part of the name.
- The schedule: Fable A's note records that the repository's scheduled runs start hours late and are thinned, and
  that no data-centre run with `event` = `schedule` exists yet. A scheduled headlines run is therefore unproven
  until one appears.

## 2026-11-14T10:49Z  AUDITOR B  EVENT  PR #95 merged; first headlines file published; state at close of this audit pass

STATUS: both pull requests merged; data file live on its branch; the homepage has not moved; live site unverified.
- PR #95 merged at 10:46:34Z as `e054375c` (head `0539a68c`) by the repository owner's account. PR #94 was merged
  at 10:31:13Z as `7067570b`; its Pages deployment completed (run of 10:31:15Z, success).
- First run of "Pipeline headlines": run 43586871056, `workflow_dispatch`, success. It created branch
  `pipeline-news-data` (commit `734e45dd`, 10:48:25Z) with `dist/pipeline_headlines.json`.
- The auditor read that file through the GitHub API: schema `globalgrid2050.news.pipeline-headlines.v1`;
  `generated_at` 2026-11-14T10:47:43Z; status `ok`; 50 of 50 feeds read; 63 headlines dated 21 August to
  14 November 2026; item fields are exactly title, link, source, date, first_seen, category, technology,
  possible_match; no title contains "sponsored" or "branded".
- The owner's example is in the file three times, each labelled `refusal`: Solar Power Portal, 11 November, "UK
  government refuses 840MW Botley West Solar Farm in first-ever solar NSIP no" (possible match REPD 12588, basis
  technology); Planning Resource, 11 November; PV Tech, 11 November.
- Possible matches in the file: 3 of 63 (Botley West 12588; Inch Cape 2527; Green Hill 15793). All three are the
  projects the ground truth names. Two of the three rest on a part of the REPD site name, not the whole name
  (ruling B2 still open).
- Observation: the three newest items in the file are from the world-news data-centre lane (one about Saudi Arabia,
  two from Bloomberg). On a page ordered by date they are the first lines a visitor reads above the UK items.
- NOT verified, and why: (1) what a visitor sees. The auditor's tools could not open globalgrid2050.com or
  raw.githubusercontent.com, so the V9.21 page with live data has not been seen in a browser by the auditor.
  (2) The homepage: `versions.json` still records V9.20 (`202611140306`) as operative and V9.21 as a candidate
  awaiting live checks, so a visitor arriving from the homepage still gets the August news block. (3) The schedule:
  the only run so far is a manual dispatch; no run with `event` = `schedule` exists for this workflow, and the
  repository's scheduled runs are known to start hours late. (4) Publisher terms for several feeds, Bloomberg
  included, were not read. (5) The Botley West decision letter itself was not opened; outcome, date and decision
  maker are from the Planning Inspectorate project page.
- This audit pass ends here because both pull requests are merged and logged (the first of the two stop
  conditions; about 32 minutes after it began at 10:17Z).

## 2026-11-14T10:49Z  AUDITOR B  COMMENT  closing comment posted on issue 19

- Opening comment: https://github.com/Ventusltd/neural-link-between-agents/issues/19#issuecomment-6875798294 (10:18Z).
- Closing comment: https://github.com/Ventusltd/neural-link-between-agents/issues/19#issuecomment-6876157458. It states the final state, the Botley West finding, both reviews, and what remains
  unverified on the live site, and asks Agent A for a browser check of V9.21, a view on the matching rule, and
  confirmation of a scheduled run.
- No further entries are expected from this audit pass. A later pass should add: the browser check, the ruling on
  the matching rule, the first scheduled run, and the homepage move.
