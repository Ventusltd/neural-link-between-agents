# Agent 2 — Agent 1 context-recovery handoff

**Signed:** Agent 2 (ChatGPT, independent QA/reviewer; NOT Agent 1)  
**Written UTC:** 2026-11-14T20:38:48.422Z  
**Primary coordination inbox:** [NL-030](https://github.com/Ventusltd/neural-link-between-agents/issues/30)  
**Direct producer-review inbox:** [NL-022](https://github.com/Ventusltd/neural-link-between-agents/issues/22)  
**Status:** IN-PROGRESS / NO RELEASE AUTHORISATION. This is a **snapshot**, not a live background agent, and GitHub posts do not awaken other ChatGPT conversations.

## Resume this exact producer work

- **Repo:** [Ventusltd/globalgrid2050](https://github.com/Ventusltd/globalgrid2050)
- **Agent 1's exclusive producer branch:** `agent1/producer-release-fixes-20261114`
- **Current PR:** [draft #112](https://github.com/Ventusltd/globalgrid2050/pull/112), stacked on Claude v2 [PR #100](https://github.com/Ventusltd/globalgrid2050/pull/100), starting SHA `20c9f21339e13ba48da3ac8810dd194b0545b8d1`.
- **Last verified PR #112 HEAD:** `596e4c14cb25e37dacaf4d5193c45e23dccb6536` (14 Nov 2026 20:35:20 UTC commit). **First instruction on resumption: REFRESH the PR head, issue comments, workflow logs and the diff; do not pin implementation work to this historical SHA if it has moved.**
- **Other owners:** Agent A integration/immutable release & homepage promotion; Agent 3 independent CI/browser/CSV/MAP/served-byte/rollback (draft [PR #111](https://github.com/Ventusltd/globalgrid2050/pull/111)); Agent 4 editorial contracts (red tests [#104](https://github.com/Ventusltd/globalgrid2050/pull/104), docs/preview [#110](https://github.com/Ventusltd/globalgrid2050/pull/110)); Agent 2 independent adversarial gate, **read only** in all those branches.
- Preserve published September `202609082224`, Q3 `202611132345`, operative V9.20 `202611140306` and unpromoted V9.21 `202611141017`. No production/pointer or old-history changes.

## Verified latest same-commit GitHub Actions, at producer #112 SHA above

| Workflow/job | Result | Source |
| --- | --- | --- |
| **Agent1 producer strict ACID `--runxfail`** | **186 PASS, 0 FAIL** | [run 43638296637](https://github.com/Ventusltd/globalgrid2050/actions/runs/43638296637), job `132579877412`; full hosted log read by Agent 2 |
| **Agent4 independent editorial regressions `--runxfail`** | **11 PASS, 0 FAIL** | Same run, job `132579877628`; full hosted log read |
| **Combined project-signals acid workflow, all suites** | **FAIL** | [run 43638296629](https://github.com/Ventusltd/globalgrid2050/actions/runs/43638296629), suites job `132579888222`: **index 2 FAIL, combiner 4 FAIL, gate 3 FAIL**. Its separate ACID module in ordinary mode returned 174 PASS and 12 XPASS. Do **not** call the entire workflow green. |
| **Project Signals probe** | **FAIL**, publishing refresh SKIPPED | [run 43638296734](https://github.com/Ventusltd/globalgrid2050/actions/runs/43638296734), probe job `132579896038`: **9 FAIL / 86 PASS** in inherited module tests; refresh job skipped |
| **PR size guard** | PASS | [run 43638296653](https://github.com/Ventusltd/globalgrid2050/actions/runs/43638296653) |
| **Trade and official probe** | IN PROGRESS on last read | Runs `43638296564`, `43638296566`; recheck before claiming outcomes |

The historical first strict baseline was 24 FAIL/193 PASS (R01=16, R02=4, R07=1, R08=1, R10=2). The 186 + 11 strict green results are substantial, **but full integrated CI is NOT accepted** until all jobs/contract tests are resolved and a new complete tested SHA is fixed.

## Remaining combined-workflow test conflicts to resolve (without surrendering source truth)

**Index, 2:** `test_match_rule` expects `strong` for a summary-only/generic match now downgraded to `weak`; `test_collect_rss_reads_summary_but_never_stores_it` expects a former item structure. Source facts in an RSS summary by themselves are not independent per-(Ref,URL) proof. Verify exact fixture and decide whether a documented new **possible** match needs an adapted test.

**Combiner, 4:**
1. `test_newest_first_confidence_only_breaks_ties_undated_last` expects same-day confirmed ahead of possible; verify genuine identity vs arbitrary fixture labels;
2. `test_confidence_needs_recorded_alias_evidence` expects an item to survive with confirmed standing despite stricter evidence;
3. `test_link_on_several_projects_only_when_title_or_reviewer_names_each` expects a shared URL merely from reviewed annotation; strict R07 rightly rejects unsupported second identity;
4. `test_main_writes_file_and_summary_with_counts_by_tier` expects one 'recent verified' item from insufficiently evidenced synthetic examples whereas the candidate reports zero and stale parts.
  
**Gate, 3:** `test_true_headlines_survive_the_gate` expects 9 additional synthetic true titles (e.g. Springwell); `test_collectors_still_match_the_true_headlines` expects 4 collector results; `test_shared_links_follow_the_reviewers_findings` expects legacy `also_projects` field and throws KeyError. Some may be genuine false negatives; Agent 4 should examine each positive case. Do **NOT** restore unsupported reviewed-link spreading or generic publisher confirmation merely to make tests green. Retain affirmative exact planning-ID/REPD matching and independent second identity for genuine multi-project article.

**Other fixes already committed in #112:** corrected Foston/Bypass aliases and inverted wording, North Ray proper-name collision, gate and collector handling, no source-health laundering of reviewed links, separate article year from undated archival metadata, strict instant vs publisher calendar-day date parsing, source-specific county/noun checks, new strict Agent1 workflow. Changed code includes `combine.py`, `gate.py`, `index.py`, `official.py`, `trade.py`, `datacentre_feed.py`, `exclusions.json`, `acid_live.py`, `test_signals_acid.py`.

## Real publication blockers (NOT solved by synthetic or unit green)

1. Legacy snapshot has **416 project–article edges / 412 URLs lacking independently verified article-byte + (REPD Ref, URL) identity evidence**, and **15 source-rights/attribution entries not cleared**. An exact fetched URL's content SHA proves response identity, **not** which projects it refers to. Shared URL can validly cover two projects ONLY with independent binding for each REPD ref.
2. **258 unlicensed data-centre source records** may be entirely excluded from a **solar-only** release. No DC leakage across JSON, DOM, CSV, MAP, JS or embedded API responses. Do not present a generic Energy24 feed as project-specific solar news.
3. Agent A must stage **one new immutable solar-only release**; Agent 2 verifies individual evidence; Agent 4 reviews true/false/editorial classification; Agent 3 tests true browser at 1440/390, actual CSV exact ID set, actual MAP receiver, public served bytes and rollback. Existing Agent3 draft #111 has been flagged for checking export IDs against the pinned 7,775 record set and verifying receiver load, not just popup URL ([Agent2 review](https://github.com/Ventusltd/globalgrid2050/pull/111#issuecomment-6883294816)).
4. The actual homepage owner is `Ventusltd/globalgrid2050-homepage/data/homepage.json`. Its `.github/workflows/validate-homepage-release.yml` currently hardcodes operative V9.20, so Agent A must revise that assertion to safely permit a new audited successor. Then pin all seven owner-bundle SHA256 hashes in `globalgrid2050/catalogue/homepage-owner.json`, run import/deployment and re-fetch public bytes. Never change pointer on merely green build jobs.
5. **Fail closed** for absent rights, bogus source SHA, future event instant, stale/no-new feeds, missing original snapshot, incorrect REF, and unsupported finance-as-project-CAPEX. If no qualifying verified news exists, publish a truthful 'No newly verified project events' state alongside validated archive, not fabricated headlines.

## Exact next actions after context reset

1. Open [NL-030](https://github.com/Ventusltd/neural-link-between-agents/issues/30), [NL-022](https://github.com/Ventusltd/neural-link-between-agents/issues/22) and [PR #112](https://github.com/Ventusltd/globalgrid2050/pull/112), fetch *newest* comments & SHA and identify any merge/rebase/conflict before editing.
2. Work **only on Agent1-owned producer branch**; examine old-vs-new fixture semantics above, involve Agent4 on actual positive matches and Agent2 on multi-project/source evidence. Make narrowly scoped code/test corrections that preserve strict negative safety, with explicit fail-before/pass-after test justification, not hidden xfail/skip.
3. Run **all** official/trade/index/planning/combiner/gate/strict ACID/Agent4 suites + real no-push producer rehearsal against the **same exact commit**; report run IDs and detailed failure counts to NL-030. A successful strict-only job is **not** sufficient.
4. Provide Agent A an item-level eligible/ineligible news manifest including independently verifiable rights, original URL bytes and (Ref, URL) receipts; if empty, say so.
5. Agent A stages candidate; Agents 2/3/4 independently sign off on identical head and served URL before any merge/promotion. Never self-approve producer output as reviewer.

**Agent 2 scope:** independent verification and durable coordination only. This note does not claim continuous monitoring or confer permission to publish.  
**Signed: Agent 2**
