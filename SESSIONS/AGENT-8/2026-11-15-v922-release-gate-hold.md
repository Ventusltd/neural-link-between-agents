# Agent 8 V9.22 final exact-head acceptance blocker — 15 Nov 2026

**Decision: PUBLICATION HOLD.** Agent8, sole owner by the user's Agent7 signed handover, will not merge PR116 or move the owner/homepage pointer while an exact-head required browser test is red. V9.21 remains operative and V9.20 remains the frozen rollback. The V9.22 candidate is source-committed, tested and registered, **not publicly deployed**.

## Exact final release source

- Repo: Ventusltd/globalgrid2050 PR116, branch `release/agent8-v922-20261115`, final observed HEAD `998c4cddbd78f04bcdd9df2a40026ac91714cd2f`.
- Source inherited from Agent7 PR115 exact `5f0cadd2f8c0a9b5f44ec46fbf582ff27210b8d1` without touching donor, plus Agent8 repairs, 390/393/1440 cross-browser, source/served Pages post-deploy gate, and generated official eleven-version registry.
- Git tree for immutable V9.22 folder `uk_renewables_pipeline/202611151300`: `301e163ccacf274bbb780688e12258b0aed3dbdd`. The ten preceding release folders retain their exact Git trees.
- [Official 11-version generator run 43733775181](https://github.com/Ventusltd/globalgrid2050/actions/runs/43733775181) PASSED; `versions.json` and `versions.html` generated on branch with first V9.22 marked **SOURCE CANDIDATE — NOT YET PUBLISHED** and all 11 verdicts PASS. Temporary generator workflow removed before any merge. [Source PR116](https://github.com/Ventusltd/globalgrid2050/pull/116) ready for review but explicitly merge-blocked pending real mobile output.

## Exact source acceptance (final head, not donor's historic green)

- [Strict producer run 43734245941](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245941): **SUCCESS**, strict and inherited Agent4 editorial jobs.
- [Integrated run 43734245996](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245996): **SUCCESS**, both suite and live jobs.
- [Versions check 43734246059](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734246059): **SUCCESS**, all eleven registered versions.
- [News reader run 43734245929](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245929), [file size guard 43734246007](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734246007): **SUCCESS**.
- [V9.22 six-job stage 43734245946](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946): **FAIL**. Offline V9.22, immutable source manifest, V9.21/V9.20 public SHA readback and actual 1440 real MAP→engine all PASS; Chromium390/WebKit393/Chromium1440 stage UI/CSV PASS; 390 REAL MAP→GridAtlas **FAIL for solar only**. Do not call this run “six jobs passed”.
- Live source probes official, trade and top200 were still in progress; self-hosted MSI public-language gate queued at last observation. They are not a pass, nor independently identified errors. That public-language gate omits Pipeline News from its SURFACE allow-list and cannot substitute for V9.22 source-specific strict editorial tests.

## Exact real 390 failure forensic proof (downloaded and inspected, not an inferred root cause)

- Failing job [132873210740](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946/job/132873210740), [artifact 14169423246](https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946/artifacts/14169423246).
- REPD **12588 Botley West solar**: actual MAP anchor click physically opened `https://ventusltd.github.io/gridatlas/atlas/`, composed generation **202611132345** with **6** cartridges; solar/project layers enabled, `runtime.failures=[]`, page-errors empty; actual nearest **Cowley 400 kV 15.76km straight** exists in hidden DOM.
- Initial mobile popup `minimised=true`, restore control exists; real restore click performed. Subsequent screenshot and JSON show **`still_minimised=true`**, visible nearest output **missing**. This is a genuine visible UX failure, not a broken nearest calculation; cannot count as mobile first-restored success.
- REPD12453 Thorpe Marsh BESS **PASS** 390, unnamed 400kV 0.31km; REPD14535 onshore wind **PASS** 390, Whitehillock 400kV 23.69km; desktop 1440 **all 3 PASS**. Global fleet 7,775 source link checks are NOT 7,775 executed engines.
- Source of likely race: `Ventusltd/gridatlas:atlas/cartridges/202609241334-sld-sandbox-v9-8.js` user restore control toggles `gridatlas-min` ~L3975; a later `resetCardGeometry` ~L4067–4109 unconditionally re-adds class on phone when `injectIntoCard` ~L4114 rerenders. Human first-restore action can be overruled by a later content update. The old screenshot literally shows the computed map with minimised bottom card.
- Reproduced and posted to [GridAtlas issue #87 comment 6897504870](https://github.com/Ventusltd/gridatlas/issues/87#issuecomment-6897504870).

## Why release has not been forced

- User explicitly instructed no concealing failing tests or unsupported news evidence. We are respecting this; this is not an indefinite editorial research cycle.
- We did not disable/xfail the red 390 test, replace real GridAtlas calculation with synthetic data, claim the known false-negative is an engine outage, or silently re-label project news as verified.
- A GridAtlas fix must be a *new hashed cartridge and preview generation*, not an in-place change to immutable live cartridge. GridAtlas AGENTS.md and docs/RELEASE.md expressly require its own release gates and owner `ACCEPT <generation>` at a preview PR before pointer movement; an agent's GitHub comment cannot impersonate owner acceptance. No unilateral GridAtlas live pointer mutation was made.
- Three candidate headline project links (Green Hill15793, Botley West12588, Inch Cape2527) remain **POSSIBLE**, externally attributed headline links only. Actual original publisher raw response bytes/rights/individual signed event not established; do not alter Q3 status or copy copyrighted article text. No unlicensed data-centre register imported.
- Independent owner homepage [draft PR15](https://github.com/Ventusltd/globalgrid2050-homepage/pull/15) has corrective CI and fallback builder but **no V9.22 operative pointer movement**. Its two initial CI jobs PASS; existing owner V9.21 and old links preserved.

## Restart and next specific action

A fresh Agent8 session must start at this file; fetch live PR116 exact HEAD and latest GridAtlas #87 comments. The single critical gate is *first-restore mobile card stability while preserving map-first default*. Implement/test in isolated GridAtlas versioned preview under its governing release guide; do not edit live `current.json` or immutable cartridge directly. After genuine new GridAtlas preview acceptance, run same exact 390/393 mobile and 1440 desktop real click/engine test on V9.22, then all source gates, publish source through PR116, verify public HTTPS hashes, advance owner PR15 and its seven-owner-file pin, and demonstrate V9.21/V9.20 rollback. Old GitHub comments do not awaken any inactive agent.

**No asynchronous Agent8 watch exists:** extra hourly automation attempt returned five-task limit; existing previously scheduled other-agent tasks do not authorise Agent8 publication. This is a durable audit, not a promise of background execution.

Signed ChatGPT Agent8 — 15 November 2026. Status: source candidate complete, **PUBLICATION HOLD** on reproduced 390px real mobile result-card regression.
