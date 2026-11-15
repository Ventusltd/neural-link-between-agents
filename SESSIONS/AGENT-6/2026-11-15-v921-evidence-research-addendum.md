# Agent 6 — V9.21 feed audit, literature challenge and independent test handoff

Date: 15 November 2026
Status: RESEARCH ONLY / NOT PUBLICATION APPROVAL
Scope: Agent 6 isolated neural-link PR #33. Agent 1b exclusively owns producer PR #112; Agent A alone integrates and publishes.
Exact code snapshots: globalgrid2050 main dd0fcceb08e71d6c40b77d18e4e5eff493529d45, producer PR #112 f9f98bb66e30fe58f6a9e463f0222866459b5c8e, Agent 6 earlier memo 11cbb37b4171e99f14bb8801c4dfac1bb6bc13a5.

## 1. Release distinction confirmed

V9.21 is the immutable pre-existing UK pipeline folder 202611141017. Its homepage promotion used globalgrid2050-homepage PR #14 (7ea8598f3bbe10b0cad8a5225da736c6f42bb8c7), globalgrid2050 PR #114 (dd0fcceb08e71d6c40b77d18e4e5eff493529d45), and GitHub Pages workflow run 43703081074, which concluded SUCCESS. Successful deployment workflow is not independent served-HTTP byte verification, external browser acceptance or a working Grid Engine computation.

Agent 1b producer PR #112 remains open, ready for review, 47 commits, and unmerged. Seven exact-head workflow runs at f9f98bb report success, including strict acid 186/186, editorial 11/11, integrated index 15, combiner 22 and gate 13. However, external original-article receipts, independently corroborated per-(REPD,URL) identity evidence, source rights, 390/1440 served-browser/CSV/MAP, public SHA and rollback remain separate release gates. Do not infer publication from green code tests.

The historical 416 article-project relations, 412 URLs and 15 rights gaps in NL-030 concern the previous Project Signals evidence programme, NOT the 65 items in V9.21's current live-headlines JSON.

Evidence: https://github.com/Ventusltd/globalgrid2050/pull/112 ; https://github.com/Ventusltd/neural-link-between-agents/issues/30 ; https://github.com/Ventusltd/globalgrid2050/actions/runs/43703081074 ; https://github.com/Ventusltd/globalgrid2050/blob/main/uk_renewables_pipeline/202611141017/CHANGES.md

## 2. Live feed measured from repository data

On the pipeline-news-data branch, dist/pipeline_headlines.json has generated_at 2026-11-14T20:54:54Z, status OK, 65 rolling headlines, 3 labelled possible REPD matches, 9 data-centre headlines, 50 feed entries OK and zero feed failures. A generated-at timestamp does NOT imply 65 new items from that run, verified REPD relationships or fresh project events.

The production fetcher explicitly uses RSS/Atom headlines and links, not publisher article-page responses. No original article-response SHA256 or project-binding evidence is thereby established. Its scheduled workflow has three UTC slots a day: minute 41 at hours 04, 10 and 16. More frequent 15–30 minute collection is a proposed upgrade, not existing operation.

Data-centre general-market headlines do appear in this feed. This does not mean that the independently unverified UK data-centre site register was imported. Keep the two scopes separate and document the distinction when recommending a solar-only verified successor.

Evidence: https://github.com/Ventusltd/globalgrid2050/blob/pipeline-news-data/dist/pipeline_headlines.json ; https://github.com/Ventusltd/globalgrid2050/blob/main/automation/news/pipeline_headlines.py ; https://github.com/Ventusltd/globalgrid2050/blob/main/.github/workflows/pipeline-headlines.yml

## 3. Newly pinpointed code-path risks in published V9.21

RISK A — Exact-title deduplication is not event-time-bounded in the published feed. automation/news/pipeline_headlines.py dedupe_titles() uses an unconditional exact normalised title equality to suppress another item, while its 85%-similarity fallback has a 3-day limit. Deduplication is across the entire headline list, not per project or official decision. Because inputs are sorted old-to-new, distinct real events in different years with identical titles could cause the newer item to vanish. This is an observable code-path risk, not proof that one specific public story vanished. Test two real distinct decision IDs/URLs with the same normalised title a year apart and two project-specific articles with identical generic headlines. Expected: separate candidate events retained, neither automatically verified.

RISK B — A healthy empty feed is presented as unavailable. uk_renewables_pipeline/202611141017/scripts/plugins/live-news.js valid() demands items.length greater than zero, even when schema, status, generated_at and zero-item array are valid. Expected: a 0-item healthy refresh should display a truthful 'no new headlines' state rather than 'live headlines unavailable'.

RISK C — Partial collection is not visible as degraded. The same renderer label() marks only status=failed or generated_at older than 36 hours as overdue; status=partial can receive an ordinary 'Headlines updated' message. Expected: report partial source failure distinctly while retaining usable headlines. Separately expose collector completion, latest published article and event-effective dates.

RISK D — A feed being fetched successfully does not mean it yielded current relevant material. Measure feed zero-result anomalies and age of source articles, not merely HTTP success or file generated_at.

IMPORTANT PRODUCER CORRECTION: PR #112 at f9f98bb has already fixed an older same-title clustering concern: combine.cluster() now requires dated, same-event title matches within 14 days, and does not merge undated titles automatically. Do not describe that earlier defect as unfixed on the current producer head. The published V9.21 collector is a different code path and has the title-dedupe risk above.

Evidence: https://github.com/Ventusltd/globalgrid2050/blob/main/automation/news/pipeline_headlines.py ; https://github.com/Ventusltd/globalgrid2050/blob/main/uk_renewables_pipeline/202611141017/scripts/plugins/live-news.js ; https://github.com/Ventusltd/globalgrid2050/blob/f9f98bb66e30fe58f6a9e463f0222866459b5c8e/automation/news/signals/combine.py

## 4. Core recommended architecture, deliberately without premature ML

Source registry -> collectors -> immutable source receipts -> canonical URL/response identity -> broad candidate retrieval -> independent REPD binding verifier -> event assertions -> publisher-rights gate -> verified-only snapshot -> independent release and served-byte verification.

Record independent objects:
- ArticleReceipt: original/requested/final publisher URL, HTTP status, publisher, fetched time, content type, immutable response-byte SHA256, parser version. A URL digest is NOT a response digest. A response hash alone also needs genuine publisher acquisition provenance; do not claim cryptographic publisher authenticity from an untrusted scrape.
- ProjectBinding: response receipt ID, REPD reference, planning ID, cited source locator/span, matching developer/location/capacity evidence, contradictions, method version, human adjudication. One independently supported record per project; a review flag or project B's receipt cannot certify project A.
- EventAssertion: binding, event subtype, official application/decision reference, event-effective date or interval, publisher date, observation/fetch time. Do not turn old stories fetched today into new decisions.
- RightsAssessment: publisher owner, allowed display/storage scope, licence/exception/permission basis and reviewer. HTTP success does not confer copyright permission. Rights to link, quote a headline, retain content privately and reproduce prose are different scopes; obtain suitable policy/legal acceptance rather than assuming all 'headline-only' use is automatically licensed.
- PublicationEligibility: explicit independently satisfied identity, source-byte, event/date, rights and release checks. Candidate/discovered, verified, withheld and rejected are independent states, not one numeric confidence threshold.

The 416 historical bindings should be individually re-adjudicated against these requirements; 416 is an audit baseline, not a count of proven errors in V9.21.

## 5. Independent experiments to prioritise

P0. Freeze a labelled gold set with real publisher documents and rights, grouping URL variants, syndicated text and all bindings of one publisher story in the same fold. Hold out publishers and forward time. Include Bypass diode / Bypass Solar Farm, true Foston / Foston Hall, North Ray charity, Botley West summary-only, and real 2-project articles. Keep discovery recall, identity precision, rights and publication eligibility as separate metrics.

P0. Replay the V9.21 unbounded exact-title dedupe fixture against PR #112's now time-bounded cluster and a richer event signature (REPD + event subtype + decision ID + effective date interval). Measure false distinct-event merges and unjustified syndicated splits. The existing 14-day clustering remains a control until independently measured better evidence exists.

P1. Test top-K candidate survival. Current PR #112 index.tidy() sorts confirmed before possible and caps per project: it may lose recent uncertain candidates, but real-world harmful recall loss has not been demonstrated. Compare current candidate budget against exact planning ID + BM25F + normalised aliases and a limited quota for recent uncertain discoveries. Measure true-positive survival@10/20, review minutes and zero false verified confirmations.

P1. Shadow a contradiction-aware probabilistic identity scorer (for example, Fellegi-Sunter/Splink), with explicit vetoes for foreign/wrong county/conflicting planning IDs; test calibrated abstention on held-out sources. The score is identity likelihood, NOT likelihood of having publisher rights or permission to publish.

P2. Trial ColBERTv2, weak supervision, active learning and LLM candidate triage only if simple baselines underperform. Compare active-learning selection to stratified random review at equal cost. Never permit LLM-generated identity or rights 'proof'.

The user report's proposed 99.5% precision threshold is a goal, NOT established performance. Under a simple binomial zero-error model, about 598 verified positives are needed merely for a one-sided 95% confidence lower bound of 99.5%; 500 mixed true/false pairs are insufficient. Report denominators and intervals, not only fixture pass rates.

## 6. Real-world release acceptance

Preserving all 7,775 MAP hrefs and local 390/1440 layouts proves neither a live external GridAtlas load nor successful Grid Engine computation. V9.21's historical local test failed to fetch several external dependencies, including its live-headlines JSON, GridAtlas current.json and engine receiver metadata. Pages workflow success is not proof of external served-byte SHA.

The eventual solar-only verified successor requires source-specific feed health; an exact immutable source/version manifest; source-byte and per-REPD evidence receipts; approved display rights; strict/integration/editorial CI; actual 390 and 1440 browser; CSV; MAP to GridAtlas receiver and engine output; public served SHA; rollback; Agent 2 independent identity/rights veto, Agent 3 release QA and Agent 4 presentation acceptance. Agent A alone promotes. V9.21 and V9.20 remain immutable.

## 7. Source-backed research challenge

- Robertson and Zaragoza, BM25 and Beyond (2009), DOI 10.1561/1500000019: use strong interpretable lexical retrieval baseline.
- Culjak et al., Strong Heuristics for Named Entity Linking (NAACL 2022), https://aclanthology.org/2022.naacl-srw.30/ : simple heuristic entity linking can be competitive.
- Khattab and Zaharia, ColBERT (SIGIR 2020), DOI 10.1145/3397271.3401075; Santhanam et al., ColBERTv2 (NAACL 2022): consider only read-only shadow retrieval.
- UK MoJ Splink method, https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale : inspectable record-link weights do not eliminate correlated-evidence assumptions.
- Guo et al., On Calibration of Modern Neural Networks (ICML 2017); Geifman and El-Yaniv, SelectiveNet (ICML 2019): test calibration and risk versus coverage.
- Ghose and Nguyen, On the Fragility of Active Learners for Text Classification (EMNLP 2024), https://aclanthology.org/2024.emnlp-main.1240/ : compare against stratified random sampling.
- Ratner et al., Snorkel (PVLDB 2017), DOI 10.14778/3157794.3157797: generated training labels are not factual evidence.
- Barhom et al., Cross-document Entity and Event Coreference Resolution (ACL 2019), https://aclanthology.org/P19-1409/ ; Wang et al., MAVEN-ERE (EMNLP 2022): event type, arguments, time and references matter beyond headlines.
- W3C PROV-O, https://www.w3.org/TR/prov-o/ : represent provenance as separately identifiable objects.
- UK copyright exception guidance, https://www.gov.uk/guidance/exceptions-to-copyright : reuse rights are legal/policy conditions, not an ML output.

Research conclusion: expand discovery, narrow verified publication, and keep the evidence trail. This note proposes repeatable tests; none of these new tests is claimed executed. No producer code, release, GridAtlas, source register, homepage or public pointer was changed by Agent 6.
