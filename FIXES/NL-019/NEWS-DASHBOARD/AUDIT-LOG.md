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
