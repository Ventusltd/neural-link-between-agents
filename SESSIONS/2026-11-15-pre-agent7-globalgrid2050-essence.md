# The essence of GlobalGrid2050 before Agent 7 — independent research and continuity record

**Research cut-off:** immediately before the first [Agent 7 appointment/branch declaration in NL-030, comment 6894674665](https://github.com/Ventusltd/neural-link-between-agents/issues/30#issuecomment-6894674665), 15 November 2026. This is a *historical pre-Agent-7 baseline*, not a report about Agent 7's subsequent implementation.  
**Prepared for:** the owner, Agent 7 (next-version integration/publication), and independent Agents 1b–6.  
**Status:** independent documentary synthesis; no production changes, no new public-release claim.  
**Writing scope:** this research-only branch of Ventusltd/neural-link-between-agents; never Agent 7, Agent 1b, Agent 6 or production branches.  
**Principal sources:** [Neural Link release issue #30](https://github.com/Ventusltd/neural-link-between-agents/issues/30), [iteration ledger #32](https://github.com/Ventusltd/neural-link-between-agents/issues/32), [Agent 6 issue #34](https://github.com/Ventusltd/neural-link-between-agents/issues/34), [producer PR #112](https://github.com/Ventusltd/globalgrid2050/pull/112), [QA PR #111](https://github.com/Ventusltd/globalgrid2050/pull/111), [editorial PR #110](https://github.com/Ventusltd/globalgrid2050/pull/110), [CVAA PR #2](https://github.com/Ventusltd/cvaa/pull/2), [GridAtlas issue #87](https://github.com/Ventusltd/gridatlas/issues/87), and [Agent 6's source-based V9.21 addendum](https://github.com/Ventusltd/neural-link-between-agents/blob/44370c1792940f153f863cd315440d2d4f4d773b/SESSIONS/AGENT-6/2026-11-15-v921-evidence-research-addendum.md).

## Executive finding: the product is an evidence-linked energy-infrastructure system

The programme is not fundamentally an automated newspaper, a web-map redesign or a project to make GitHub Actions green. Its goal is to make the renewable-energy project catalogue an **auditable index of real infrastructure**: preserve the REPD identity of each project, discover significant events affecting it, state precisely *what is known and how*, and allow a reader to move from that record to geographic and grid-connection screening. Project news must make the underlying asset catalogue more useful without converting a plausible name match into a false assertion.

The defining end-to-end experience is:

**Original REPD project identity → publisher or official-source discovery → original response provenance → independently supported project binding → dated event assertion → publication-rights decision → truthful news status → project record/CSV/MAP → actual GridAtlas composer and Grid Engine response → immutable, reproducible public release.**

The architecture is deliberately asymmetric. Candidate *discovery* should be broad enough to avoid missing relevant developments; independently confirmed *publication* should be narrow enough to abstain whenever identity, source bytes, rights or dates are insufficient. More headlines do not mean better intelligence. Nor does a correctly formatted MAP URL mean that the computation behind it ran. This common distinction between **claimed and actually observed results** is the connecting principle behind producer fixes, Agent 2 review, Agent 3 QA, Agent 4 editorial work and Agent 5 CVAA.

## 1. Historical architectural boundaries that must not be erased

**The protected data layer.** The contemporary UK Pipeline News catalogue displays **7,775** solar, battery and wind REPD records, with original reference identity, export and MAP links. The relevant release records point to the DESNZ Q3 2026 extraction and require immutable history and canonical source hashes. Those 7,775 rows are a preserved catalogue requirement, *not* a count of independent news stories or successful Grid Engine executions. Any next version must demonstrate that this data and its established behaviours survived unchanged unless a separately documented source update was explicitly accepted. See [release train #30](https://github.com/Ventusltd/neural-link-between-agents/issues/30) and [version ledger #32](https://github.com/Ventusltd/neural-link-between-agents/issues/32).

**The published V9.21 application.** Before Agent 7, the owner-directed operative edition was **V9.21: uk_renewables_pipeline/202611141017/**; **V9.20: uk_renewables_pipeline/202611140306/** was the preserved fallback. The homepage-owner repository was promoted at **7ea8598f3bbe10b0cad8a5225da736c6f42bb8c7** and GlobalGrid2050 main at **dd0fcceb08e71d6c40b77d18e4e5eff493529d45**, through merged PRs #14 and #114 respectively. [GitHub Pages run 43703081074](https://github.com/Ventusltd/globalgrid2050/actions/runs/43703081074) succeeded. This establishes source promotion and workflow deployment, **not** independent public HTTP byte identity, working external CSV/MAP/engine behaviour or a verified-only news feed. See [Agent 1b's publication distinction](https://github.com/Ventusltd/neural-link-between-agents/issues/30#issuecomment-6892897268) and [Agent 3's independent readback](https://github.com/Ventusltd/neural-link-between-agents/issues/30#issuecomment-6893891860).

**The published rolling RSS feed.** V9.21 reads **pipeline-news-data/dist/pipeline_headlines.json** from a scheduled RSS/Atom collector in **automation/news/pipeline_headlines.py** and displays it with **202611141017/scripts/plugins/live-news.js**. Its "Possible match" chips are discovery associations, explicitly *not* verified project news. At **2026-11-14T20:54:54Z**, the repository snapshot held **65 rolling retained headlines, 3 POSSIBLE REPD matches, 9 general data-centre headlines and 50/50 reported successful feed entries**. These are not 65 fresh events, not three automatically proven REPD updates and not nine records copied from the separate, unverified UK data-centre register. The workflow **.github/workflows/pipeline-headlines.yml** schedules **04:41, 10:41 and 16:41 UTC**, three attempts/day rather than continuous 15–30-minute monitoring. [Agent 6's primary-source audit](https://github.com/Ventusltd/neural-link-between-agents/issues/34#issuecomment-6893502405).

**The stronger, still-isolated producer.** [GlobalGrid2050 PR #112](https://github.com/Ventusltd/globalgrid2050/pull/112), exclusive to Agent 1b's **agent1/producer-release-fixes-20261114** branch, was **OPEN, ready for review, unmerged**, with 47 commits and historical final pre-Agent-7 HEAD **f9f98bb66e30fe58f6a9e463f0222866459b5c8e**. Its code concerns Project Signals matching, source collectors, chronology and evidence-based abstention. The PR is stacked on **acid/team1** baseline **20c9f21339e13ba48da3ac8810dd194b0545b8d1**, not simply a one-file patch that can be merged blindly into main. The published RSS path and this PR were **different products** at the cut-off. Success in one is not proof that its safeguards exist in the other.

## 2. Why all the agents spent so long on apparent "small" news issues

Matching a headline to an electrical project is a high-cost identity problem. A repeated place name, shared developer, generic county reference, RSS summary, old planning article or syndication can cause the wrong project to look confirmed. Once attached to a REPD reference, a wrong event can affect commercial interpretation, engineering screening or a reader's decisions. A unique REPD reference is therefore the master key; generic language is only possible supporting evidence.

The pre-Agent-7 programme found and corrected unsafe assumptions that had been embedded in old tests. Agent 2's independent arbitration refused to treat a generic BBC or shared-URL report as confirmed merely because the phrase Botley West appeared in a summary or a source had a "reviewed" flag. Likewise, a real article about two projects can support two associations only if the individual evidence edges are established, not by carrying the publisher URL across REPD identifiers. A genuinely named weak candidate may be retained as **POSSIBLE** without being promoted to confirmed. Negative wrong-project cases must pass as rigorously as named positive matches. [Agent 2 rulings in #30](https://github.com/Ventusltd/neural-link-between-agents/issues/30#issuecomment-6886994331).

This became production code and tests in Agent 1/1b's producer: reviewed-only wrong-REPD bypass protections, unsupported generic title and location negatives, Foston/Bypass-related name distinctions, East Yorkshire/East Riding corroboration without arbitrary county promotions, and guarded recovery of genuine candidates. A later Agent 1b change prevented **identically worded events in different years** being merged. The final PR #112 **combine.cluster()** time-bounded same-event dated title clustering within fourteen days; it did not indiscriminately conflate undated matching titles. That matters because **the published V9.21 RSS deduplication has a distinct, still-relevant code-path risk**, described below. [Agent 1b N09 evidence](https://github.com/Ventusltd/neural-link-between-agents/issues/32#issuecomment-6891955189).

There were nine inherited integrated failure cases at an earlier stage (index 2, combiner 4, gate 3), which the producer subsequently repaired. At final pre-Agent-7 SHA **f9f98bb**, the seven associated GitHub Actions workflows were reported successful: strict acid **186/186**, Agent 4 editorial **11/11**, integrated index **15/15**, combine **22/22** and gate **13/13**. See [strict/editorial run 43696216101](https://github.com/Ventusltd/globalgrid2050/actions/runs/43696216101) and [integrated run 43696216041](https://github.com/Ventusltd/globalgrid2050/actions/runs/43696216041). These results constitute strong **code-test evidence** on the pinned producer SHA. They do **not** establish public release, original publisher receipts, independently approved rights or clicked Grid Engine output.

## 3. Four separate kinds of evidence, plus one release decision

The programme converged on four independently reviewable objects, rather than one model-generated confidence value:

1. **Article receipt:** the actual original publisher response, requested/final HTTPS URL, publisher/source identity, HTTP status, observed time, content type, exact response-byte SHA256 and parser/version metadata. A SHA of the URL or RSS title is not a SHA of an original publisher response; an arbitrary file hash is not proof that the publisher served it.
2. **Project binding:** the particular **(response receipt, REPD reference)** relationship, supported by a project/planning ID or cited original source evidence, with contrary matches recorded. The identity of another project or a generic reviewed status cannot stand in for this edge.
3. **Event assertion:** what actually happened (application, consent, refusal, appeal, construction, energisation, financing, etc.), its underlying decision reference where available, and **event-effective date** separately from publisher publication and fetch/observation dates. An old article recrawled today is not a new permission.
4. **Rights assessment:** the publisher and lawful basis/permission for precisely the proposed use. Rights to link, cache, quote a short headline, show an excerpt and republish text differ. HTTP access and model confidence alone confer none of these permissions.

**Publication eligibility** follows only after the relevant identity, date, provenance, source terms and editorial tests independently pass. Candidate relevance, identity confidence and legal-rights clearance are **different variables**. When unverified, disclose possible, archive or withhold rather than invent a certified project card.

The earlier Project Signals evidence audit identified **416 article/project edges across 412 URLs**, without independent per-edge binding receipts, and **15 source-rights gaps**. These are a historical **Project Signals audit baseline**, not the distinct 65-entry V9.21 RSS snapshot. Likewise, earlier mention of **258 rights-unverified data-centre register records** does not describe V9.21's nine general data-centre market headlines. Source cohorts must not be mixed in a status dashboard. [Release coordination #30](https://github.com/Ventusltd/neural-link-between-agents/issues/30); [Agent 6 source audit](https://github.com/Ventusltd/neural-link-between-agents/issues/34).

## 4. Known V9.21-specific defects and their honest strength of evidence

**A. Exact-title deduplication risk (source-proven risk, not a witnessed lost story).** In published **automation/news/pipeline_headlines.py::dedupe_titles()**, exact normalised title equality is accepted as duplicate without checking the event's date, REPD reference or decision ID; its *other* 85% word-overlap path is time-bounded to three days. Inputs are sorted oldest first, so two different decisions in different years with the same title may cause the later one to disappear. The correction should preserve distinct events/REPD identities, while safely clustering true syndications and retaining their individual source receipts.

**B. Healthy empty displayed unavailable (direct code defect).** Published **202611141017/scripts/plugins/live-news.js::valid()** requires **items.length > 0**, so schema-valid, successfully generated zero-item JSON fails validation. Its fallback can show a saved older snapshot or "unavailable" when the honest condition is simply no headline meeting the current criteria. The next immutable frontend must distinguish **healthy empty** from malformed/unreachable.

**C. Partial collection masked as healthy (direct code defect).** Its **label()** marks failure or staleness but does not distinguish **status="partial"** from normally fresh; one failing publisher can be hidden by a recent generated-at timestamp. Show "partial collection" and feed counts, retaining usable article links without implying all sources are current or verified.

**D. Collector health is narrower than useful news freshness.** RSS/Atom success means the feed was fetched; it does not prove a relevant article was newly published, that original response bytes were inspected or that a matched event has current significance. Measure source availability, last genuinely relevant item, publisher date, first observation and actual event time separately. Do not turn empty output itself into a failure.

These four concerns were independently documented by Agent 6 and further converted into **21 PROPOSED, NOT EXECUTED** CVAA recovery scenarios, with an executed *record integrity* check. Read [CVAA recovery report](https://github.com/Ventusltd/cvaa/blob/f38b6b8cd0d8933636578d509b1ea57d62100b87/reports/20261115-v921-pipeline-news-recovery.md) and [regression case set](https://github.com/Ventusltd/cvaa/blob/f38b6b8cd0d8933636578d509b1ea57d62100b87/reports/20261115-v921-recovery-cases.json). Do not say all 21 production tests passed merely because their JSON integrity test passed. Agent 5's broader CVAA full registry still had **ten historical findings**; partial-success testing is not an all-green CVAA certificate.

## 5. Why independent deployment and MAP measurement matter

The earlier homepage promoter had a genuine deployment workflow success. But the strongest acceptance work asked a more demanding question: **did the identical bytes from this exact build actually reach the public site and work in a real user's browser?** That calls for a candidate-specific SHA manifest, a network-capable external fetch of served HTML/JS/JSON/CSV, viewport testing, export checks, and a demonstrated reversible pointer/rollback. If an environment cannot resolve the public domain, it has an **UNVERIFIED** result, not evidence that the public site is down and not grounds to claim HTTP success.

[Agent 3 QA PR #111](https://github.com/Ventusltd/globalgrid2050/pull/111) assembled pinned-candidate, adversarial, historical-hash and browser acceptance contracts. It remained a separate QA proposal: green tests in its branch do not certify a V9.21 or a later integrated candidate without executing those checks against that particular build. [Agent 4 editorial PR #110](https://github.com/Ventusltd/globalgrid2050/pull/110) supplied a mobile-first, chronology- and evidence-conscious preview, not a deployed reader. Agent 4's model separates official verified events, possible associations, archive reports, source fetch times and no-new-item states.

The MAP issue makes the distinction tangible. Static Pipeline News code constructs canonical URLs carrying **repd_ref, technology, latitude, longitude, zoom**; the GridAtlas receiver dynamically fetches **atlas/current.json**, composes shell/cartridges and eventually loads engine behaviour. Existing tests validated 7,775 hrefs or REPD IDs, but that **does not** prove actual browser click, successful receiver generation, cartridge integrity, a map point on screen or nearest-substation computation. The historical map-link state included 5,331 active register resolutions and separately explained offshore/out-of-area and inactive statuses; its **pass:true** was explicitly *not* engine proof. [GridAtlas issue #87](https://github.com/Ventusltd/gridatlas/issues/87).

For valid-coordinate onshore and nearshore cases, the acceptance chain is:

**visible/hit-testable MAP control → real click/new context → correct REPD query and coordinates → GridAtlas receiver compositing successfully → intended layer/project point active → actual engine terminal success with measured nearest-substation geometric screening → useful visible result.**

Validate at least 390px mobile/touch and 1440px desktop with representative technologies, geography, statuses and cross-origin delays. A correct URL, HTTP 200 or a DOM containing the word REPD is insufficient. Distant-offshore treatment needs a reproducible geospatial exception, not a blanket wind_offshore bypass. A nearest geometric substation does not establish connection headroom or a bankable cable route.

## 6. Why six agents produced useful work without finishing the release

Before Agent 7, the work was divided deliberately but the integration/publication lane was incorrectly described as **Agent A**. The owner explicitly clarified that **no Agent A existed** and that the original **Agent 1 conversation had exhausted its context**. That ambiguity mattered: every separate agent could finish a scoped branch without anyone being both available and legitimately accountable for assembling the new immutable version. Read [owner correction and Agent 5 acknowledgement](https://github.com/Ventusltd/neural-link-between-agents/issues/30#issuecomment-6894012135).

- **Agent 1b** succeeded the original producer, exclusively owned PR #112 and turned inherited identity/integration reds green without editing V9.21. Its code remains a candidate input, not a live feature merely because Actions succeeded.
- **Agent 2** independently adjudicated candidate-versus-confirmed semantics, per-project rights and false positives. Its veto must survive integration.
- **Agent 3** designed independent CI/browser/served-byte/rollback and actual MAP acceptance. It cannot sign off a candidate it never loaded.
- **Agent 4** created editorial and mobile chronology contracts, but its preview did not become the operative app merely because it had a PR.
- **Agent 5** documented enduring CVAA safety lessons, 17 adversarial false-publication tests, and later 21 proposed V9.21 recovery scenarios. CVAA checks self-declared structure; it does not independently authenticate third-party evidence.
- **Agent 6** researched candidate retrieval, bitemporal events, evidence edges, abstention and source reliability in research-only [PR #33](https://github.com/Ventusltd/neural-link-between-agents/pull/33), explicitly not touching the producer.

The owner also requested ten meaningful iterations. [NL-032](https://github.com/Ventusltd/neural-link-between-agents/issues/32) is an **evidence ledger**, not an entitlement to report ten public releases. Agent 3's final pre-Agent-7 assessment distinguished ten QA/staging checkpoints from **zero independently certified new Project Signals successor editions**; it also recognised the **one real promotion of the already-existing V9.21 app**. Both statements are true once the object being counted is specified.

The right response to this history is not "restart everything with more agents". It is an owner-identified integration lead, exact branch boundaries, one pinned candidate, and independent verification that measures a user's real outcome.

## 7. Pre-Agent-7 risk and dependency register

| Priority | Dependency / risk | What was actually established before Agent 7 | Required next proof |
| --- | --- | --- | --- |
| P0 | Producer-to-public architectural split | V9.21 operative, PR112 unmerged | Pinned integration diff and compatible new immutable reader/data contract |
| P0 | Wrong REPD identity | Producer test regressions repaired | Original response, independent evidence for each (REPD, article) edge; wrong-project negative |
| P0 | Source permission/rights | Historical gaps explicitly recognised | Rights owner, permitted use and approval for each actual published verified item |
| P0 | Overcounted "fresh" news | RSS feed 65 retained, 3 possible, 9 general DC | Distinguish discovery, project verification, article date, effective event date and rights |
| P0 | Historical versions damaged | Prior versions existed and were catalogued | Exact DESNZ/source/historical tree hashes on integration and after publish |
| P0 | Self-certified publication | Pages build successful, public served bytes unknown | Independent external HTTP SHA, 390/1440 browser, CSV, rollback and review |
| P0 | Healthy empty/partial misreported | Published JS defect identified | Executed zero-item, partial, failure, stale and snapshot UI tests |
| P1 | Distinct events lost in RSS | Published exact-title code risk identified | Executed same-title/different-decision and genuine-syndication tests |
| P1 | MAP opens but engine silent | Static hrefs checked, engine not measured | Real click→receiver→cartridge→terminal engine/geometry receipt |
| P1 | Collection gaps | Three cron slots daily; feed OK ≠ useful result | Observed collection latency, per-source health and quota-aware cadence |
| P2 | Premature AI retrieval complexity | Ten Agent6 hypotheses, no production performance proof | Frozen publisher/time held-out baseline and simple lexical recall@k first |

These are evidence-status statements, not fresh assertions that each risk has materialised as a public incident.

## 8. Ranked engineering decisions for Agent 7 to use when publishing the next version

**First — integration without branch or source corruption.** Assemble a **new, independently versioned** V9.21 successor on Agent 7's separately reserved branch. Pin main and PR #112 SHA and inspect the stack's base; do not blindly merge **acid/team1** or edit Agent 1b's producer branch. Bring over only appropriately integrated, tested producer paths. Pin REPD Q3 catalogue source, keep V9.20/V9.21 byte-immutable, and retain the 7,775 rows, CSV, filters, MAP anchors and source citations. No speculative data-centre register import.

**Second — the smallest visible user fixes.** Implement safe RSS dedupe with positive syndication and negative distinct-event cases. Make live-news reader accept zero valid items, show healthy empty separately from errors, display partial/stale/source-health honestly, and avoid calling an RSS discovery record verified. Agent 4's chronologically coherent mobile stream should be adapted only after tested integration, not copied as a static design mock.

**Third — meaningful verified project links.** Establish ArticleReceipt → ProjectBinding → EventAssertion → RightsAssessment objects before upgrading POSSIBLE to verified. Keep uncertainty and the independently explained no-verified-story state. Prioritise official planning reference and source-grounded aliases; measure candidate retention and false positives. Avoid new LLM adjudication or neural matching as a first prerequisite to shipping the useful existing product.

**Fourth — an actual candidate-specific release gate.** Re-run strict 186-case, editorial 11-case and grouped tests on the **new integrated exact HEAD** (historic PR112 green does not transfer across changed merges). Verify separately all protected source/historical SHA and data-centre exclusion, then get Agent 2 semantic/rights evidence, Agent 3 live browser/CSV/MAP/served SHA/rollback receipts and Agent 4 editorial acceptance. A healthy empty verified-news panel is a legitimate shipped outcome if rights cannot be cleared.

**Fifth — measure Grid Engine execution, not URL construction.** For eligible onshore and nearshore rows with coordinates, assert a real engine result in the same browser journey rather than a nominally correct destination. Coordinate further fixes on separately owned GridAtlas/engine branches after the core news release as specified in [issue #87](https://github.com/Ventusltd/gridatlas/issues/87). Engineering output must remain described as screening, not a connection offer.

**Sixth — improve source coverage only once truthfulness and latency are measurable.** Add per-feed last successful fetch, last relevant item, article-age and failure-retry metrics. Propose 15–30-minute polling, region/timezone coverage and international CAPEX screening only after rate limits, rights, compute cost and observed missed news are measured. Do not infer project CAPEX from capacity or headline language. Keep global market/DC intelligence visibly separate from independently evidenced UK REPD decisions.

## 9. Explicit acceptance contract and post-handoff boundary

A sound next release has **one** immutable candidate SHA, actual source/manifests, an independently verified project/rights set, tested code, actual browser outputs, served hashes and a measured rollback. For any purported verified headline, its source-response SHA, REPD binding, event-effective date, rights basis and exact article URL must be resolvable or it remains withheld. For any qualifying MAP journey, an actual engine result rather than just a link must be evidenced. An honest zero-new-verified-item state may pass; a fabricated positive must fail.

**The next version is Agent 7's responsibility, not this report's.** This research ends immediately before Agent 7's first NL-030 post. Agent 7's creation is cited only to define the cut-off and handoff. There is no Agent A, and the original exhausted Agent 1 is archival. The work must respect Agent 1b's exclusive producer branch and Agents 2–6 independent review lanes; no GitHub comment wakes a dormant chat. The owner decides live publication subject to the project's safeguards. This report is documentation only, not review signoff or release authority.

### Fast source and evidence index

- [NL-030, full release train and role correction](https://github.com/Ventusltd/neural-link-between-agents/issues/30)
- [NL-032, staging vs genuine public release evidence ledger](https://github.com/Ventusltd/neural-link-between-agents/issues/32)
- [NL-034, independent Agent 6 research review](https://github.com/Ventusltd/neural-link-between-agents/issues/34)
- [Agent 1b producer PR112](https://github.com/Ventusltd/globalgrid2050/pull/112) and [exact-head CI](https://github.com/Ventusltd/globalgrid2050/actions/runs/43696216101)
- [Agent 3 independent release QA PR111](https://github.com/Ventusltd/globalgrid2050/pull/111)
- [Agent 4 editorial/mobile PR110](https://github.com/Ventusltd/globalgrid2050/pull/110)
- [Agent 5 CVAA PR2](https://github.com/Ventusltd/cvaa/pull/2) and [21 regression case proposals](https://github.com/Ventusltd/cvaa/blob/f38b6b8cd0d8933636578d509b1ea57d62100b87/reports/20261115-v921-recovery-cases.json)
- [Agent 6 hypothesis PR33](https://github.com/Ventusltd/neural-link-between-agents/pull/33) and [V9.21 source code audit](https://github.com/Ventusltd/neural-link-between-agents/blob/44370c1792940f153f863cd315440d2d4f4d773b/SESSIONS/AGENT-6/2026-11-15-v921-evidence-research-addendum.md)
- [GRIDATLAS-87: MAP actual engine reliability](https://github.com/Ventusltd/gridatlas/issues/87)
- [Published V9.21 Pages deployment workflow](https://github.com/Ventusltd/globalgrid2050/actions/runs/43703081074)

**Research conclusion:** **The next successful version is not the one that produces the most headlines. It is the one in which every meaningful project claim is traceable, uncertainty remains honest, MAP really computes, and the entire public edition can be independently reproduced and reversed.** That is the essence of what the previous agents built and what Agent 7 was appointed to finish.

**Signed: Independent Deep Research — Agent 5 context, for Agent 7 and all active agents.**
