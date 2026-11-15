# Agent 9 — GridAtlas mobile result-card repair: 3,000-word TestCode implementation and dual human/AI sanity-check mandate

**Author:** ChatGPT Agent 8, on the owner's instruction, 15 November 2026. **Recipient:** a separately invoked ChatGPT Agent 9. **Status:** proposed work order, not an Agent 9 acknowledgement or a release authorisation. **Canonical coordination:** https://github.com/Ventusltd/neural-link-between-agents/issues/30 and https://github.com/Ventusltd/gridatlas/issues/87.

**Objective:** make the genuine nearest-substation result visible after a user's first attempt to restore the mobile GridAtlas project card, without losing the intentionally map-first collapsed arrival design. Prove it first inside TestCode, then on an immutable, publicly accessible but NON-LIVE GridAtlas preview so the owner can inspect it in Safari on an actual iPhone and Agent 8 can independently interrogate source, CI and served bytes. Only after both accept should the owner separately authorise Agent 9 to perform a governed next-version publication. Nothing in this assignment authorises a live pointer change today.

## 1. What exists and what is genuinely broken

At the inspected GitHub state, GlobalGrid2050 Agent 8 Pipeline News PR #116 is open, not merged. The candidate V9.22 directory is uk_renewables_pipeline/202611151300, with its main release-source HEAD 998c4cddbd78f04bcdd9df2a40026ac91714cd2f. V9.21 (202611141017) is the homepage's operative public edition and V9.20 (202611140306) remains rollback. The 7,775 canonical DESNZ October 2026/Q3 REPD identifiers are intact. The new edition's strict producer, historical-version, CSV and several browser suites passed, but the actual 390px real-MAP GridAtlas acceptance job failed: https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946/job/132873210740.

In that real browser run, REPD 12588, Botley West solar, generated a correct link, opened the GridAtlas composer, loaded six hash-verified cartridges, enabled the expected technology and project layers, and computed the nearest 400 kV Cowley substation, approximately 15.76 km straight-line. The value appeared in hidden DOM. Nevertheless, after an actual automated tap on the restore button, the bottom card was again minimised and the result was not visible. REPD 12453 BESS and REPD 14535 onshore wind passed that particular 390px run; earlier runs failed other samples. Desktop 1440px passed the three-class sample. Therefore the bug is intermittent **result presentation**, not established failure of electrical/geographical calculation, and neither side can honestly claim fleet-wide reliability.

The live GridAtlas composition is generation 202611132345, version v9.189. Its SLD sandbox points to atlas/cartridges/202609241334-sld-sandbox-v9-8.js. The observed code's card-bar click handler toggles the gridatlas-min class; resetCardGeometry independently re-adds that class when the screen qualifies for a mobile sheet. injectIntoCard and a declared-connection path call resetCardGeometry. A late measurement or content refresh can therefore plausibly undo an intentional user expansion. This is a concrete source-level **hypothesis**, not an experimentally established call sequence. Agent 9 must capture the event order and demonstrate both a failing old state and corrected new state.

Reference evidence:
- https://github.com/Ventusltd/gridatlas/issues/87
- https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946/artifacts/14169423246
- https://github.com/Ventusltd/testcode/pull/12
- https://github.com/Ventusltd/globalgrid2050/pull/116

## 2. Agent 9 identity, limits and exclusive Git write lane

On first invocation, Agent 9 must read the complete Neural Link AGENTS.md, PROTOCOL.md, LINK-RULE.md, all new issue #30 messages and GridAtlas issue #87; explicitly acknowledge this handoff using its exact GitHub comment URL. Then read TestCode README.md, engines.json and run.mjs, GridAtlas AGENTS.md, STATE.md, atlas/current.json, docs/RELEASE.md and the relevant cartridge's actual committed bytes. Re-fetch current HEADs before any implementation. The SHA values here are recovery baselines, not permission to ignore later commits.

Agent 9 shall begin with ONE isolated TestCode branch, proposed name qa/agent9-gridatlas-first-restore-20261115, off a freshly checked TestCode main. Its draft PR must remain read-only with respect to GlobalGrid2050, GridAtlas, Pipeline News, homepage catalogues, source data and deployed Pages. No edit to TestCode main, no manual overwriting of existing Agent 3 PR #12, no silent merge or copying of another agent's branch. Agent 3's receipt validator is relevant independent prior art, not an approved production repair; either use it as a pinned read-only reference or propose a properly reviewed integration, while keeping authorship and exact SHAs clear.

Proposed new TestCode location: sandbox/gridatlas-agent9-first-restore/. Place the test harness, deliberately failing original fixture, patched-candidate model, browser runner, expected case matrix, synthetic mutation tests, result-schema documentation, source-input manifest and a README there. Place reusable proof tooling in drivers/ only if genuinely shared with other checks. Avoid globally registering a new success gate in engines.json until the offline and genuine network phases have each been proven on fixed inputs. No TestCode tool may publish or rewrite product repositories.

**Authority split:** Agent 9 designs and measures; the owner personally tests iPhone; Agent 8 independently verifies GitHub and published evidence. Agent 9 may subsequently prepare a separate GridAtlas preview branch after TestCode tests pass, but the later *live* release requires a new explicit owner acceptance and publication delegation. Agent 8's current V9.22 release PR is not a free-for-all merge target.

## 3. Follow TestCode's ordering rule, not a happy-path shortcut

The current TestCode README is explicit: OFFLINE first; NETWORK only if offline is green; PUBLISH never from TestCode. Its runner uses node run.mjs, with --with-network as a deliberate separate step. A missing input is FAIL, not SKIP and certainly not PASS. Tests must inspect the source bytes actually composed and served, not an unexecuted part or an invented fixture labelled as live. Report independent measurements; a GitHub Action green check is meaningful only for the precise code and evidence it executed.

Begin with a hard input manifest capturing source repository, commit SHA, existing composed generation, cartridge path and SHA256, Pipeline News release source SHA, official REPD extract identity, browser/Playwright version, OS, viewport, URL, time and execution mode. If any pinned input has moved, require a deliberate repin and explain why. The harness should consume an adjacent, read-only clone of GridAtlas, and a read-only GlobalGrid2050 PR #116 checkout. Never infer its source from an arbitrary local dirty working tree.

First prove the historical fault. Capture raw timestamps of card creation, resetCardGeometry invocation, late project injection, minimise-class mutations and user click; record screenshot, video or Playwright trace. Do not change application code during this first run. Reproduce with deliberate slow loading and a delayed measurement update when appropriate, but clearly mark synthetic timing injection and separately repeat against unmodified live behaviour. A source-level explanation without a failing browser receipt is not an accepted reproduction.

## 4. Proposed repair semantics: user action outranks a late refresh

Treat each project card selection as a finite-state machine rather than an uncoordinated CSS class. The conceptual state is: selection token, project REPD reference, popup instance, intended initial visibility, last explicit user visibility choice, and most recent measurement version. The owner deliberately wants the card minimised on first mobile arrival to expose the map and drawn network. Preserve that default. The first deliberate restore tap, however, must become an explicit choice that late updates for the SAME selection cannot override.

Implement the following behavioural rules in the TestCode candidate model, then port them into an immutable GridAtlas successor only after proof:

1. On a new selection token, clear the previous project's user-choice state; decide initial minimised/open state from current viewport and map-first rules. Do not inherit stale popup geometry or drag offsets from a previous selection.
2. The restore button must update state before drawing: userChoice = expanded. The opposite deliberate tap sets userChoice = minimised. The resulting CSS class and geometry must derive from that state, not from a second independent heuristic.
3. On same-project asynchronous content injection, recalculate card dimensions and measured text while preserving the explicit userChoice. A late network response cannot silently reapply gridatlas-min to the previously restored card.
4. An async callback from an obsolete selection token must not rewrite the visible state of a newer selected project. Reject stale callbacks or scope their work to the correct card instance.
5. If no user action occurred, preserve the initial map-first collapse. For a new project, reset again as the original design intends. The fix is not simply to remove every minimisation call.
6. Update the visible plus/minus glyph, title, accessible label, aria-expanded and hit-area dimensions from the actual final state in ONE synchronisation routine. Collapsed means a clear “Show/expand project measurements” control; expanded means “Hide/minimise measurements”. Minimum interactive hit area: 44 by 44 CSS pixels.
7. Handle touch and pointer events without the click propagating into the map behind the card. Preserve drag, close, scroll, safe-area bounds, map interaction and layer-menu access. Any exception or hidden measurement must fail its test.

The proposed mechanism could be a per-popup keyed state object or carefully scoped metadata on the existing popup; Agent 9 should choose the minimum invasive implementation supported by source and browser traces. Do not introduce global “always expanded” flags, mutable state shared between unrelated projects, a timer that repeatedly forces visibility or a test that presses restore repeatedly until it passes. Those would hide rather than repair the race.

## 5. TestCode modules and deliverables

Build a small, clear harness rather than another wholesale application clone. Recommended components are:

- README.md — scope, commands, exact source pins, known historical red evidence, nonpublishing guarantee, and reproduction steps.
- input-manifest.json — committed source identifiers, expected composition and allowed test-only URLs; no credentials or unverified private paths.
- cases.json — genuine known REPD cases, expected technology and conditional geometry, and stratification rules for additional projects.
- state-contract.test.mjs — deterministic state-machine tests that distinguish first arrival, user tap, same-project refresh and new-project reset.
- mutation-selftest.mjs — adversarial changes that MUST make the checker fail; test the checker, not GridAtlas.
- browser-real-map.mjs — actual browser source MAP click, popup event, external composer, real nearest result, screenshots and traces, with no stubs for GridAtlas receiver, cartridges, basemap or calculation.
- result-contract.mjs — produce separate, fail-closed source, navigation, composer, calculation, visibility, accessibility and stability verdicts.
- receipts/README.md — field schema and actual artifact locations; never commit a screenshot that includes confidential browser tabs or personal information.
- run.sh or run.mjs — reproducible local command that first runs offline tests and only then permits explicit network checks.

The existing Agent 3 validator in PR #12 already rejects forged easy greens: correct URL with no visible result, correct hidden DOM with re-minimisation, missing actual click, fewer than six verified cartridges, wrong REPD ID, an inaccessible restore control, and a visible result lasting less than 1,500 milliseconds. Reuse those concepts; do not claim the 15 successful synthetic mutations in Agent 3's CI constitute a real mobile fix.

## 6. What a real browser receipt must prove

Every browser receipt must bind one test to one exact Pipeline News source SHA and one exact GridAtlas composition SHA/generation. It must record original REPD reference, project technology, official source latitude/longitude where available, emitted MAP href, actual clicked destination URL, tab or popup arrival, viewport size, browser engine, local versus public/preview mode and complete ISO UTC timestamps. Distinguish the author's source commit from the public website's *served* bytes.

The browser must inspect the real destination: canonical receiver path; expected exact repd_ref, technology and coordinates; loaded generation; hash-verified shell and each cartridge; no unhandled JS errors; technology and project layer actually enabled; destination not stuck on a spinner; real nearest-substation data computed. Record the substation name and distance as geographic screening only, never as available grid capacity, permissible cable route or connection offer.

Presentation is a separate PASS. The browser must physically click the visible restore button once, verify the project card is no longer minimised, find nearest text in actually visible rendered content, confirm the card and control are on screen, and observe the result stable for at least 1.5 seconds. Also observe after 5 seconds and after a purposely delayed same-project update. A hidden DOM match is useful to diagnose computation but cannot turn visibility FAIL into PASS. Do not count repeated clicks, retries, a mocked popup, a fake response or text in an offscreen element as successful first interaction.

Persist an immutable JSON verdict, screenshots for before/after and failure, Playwright trace or video where available, network error summary, browser console report and a source-versus-served SHA256 table. A PASS without attached raw real-browser evidence is UNVERIFIED. A pass achieved only on retry is FLAKY, with first-attempt failure retained.

## 7. Automated sanity-check matrix

Run the following minimum groups; expand beyond three projects once the first defect is fixed:

**A. Deterministic offline state:** initial phone card collapsed, explicit restore expanded, a late same-project measurement keeps it expanded, manual re-minimise stays minimised, switching project resets to intended first-arrival state, stale callback cannot touch a new selection, desktop geometry remains intact, controls and aria attributes track CSS exactly. Deliberately mutate each rule to confirm the suite turns red.

**B. Three historical live cases:** REPD 12588 solar, 12453 BESS, 14535 onshore wind, at 390px Chromium, 393px WebKit and 1440px Chromium. Use correct frozen REPD coordinates from the checked source, never copied or made-up numbers. Compare the unrepaired GridAtlas generation 202611132345 with the test candidate; each case must have a first-attempt verdict, not just a winner among several repeats.

**C. Broader genuine project sample:** add at least 24 independently selected valid-coordinate REPD IDs stratified across solar, BESS, onshore wind, nearshore/offshore where geographically appropriate, regions, statuses, projects close to a substation and projects beyond the displayed draw radius. Document how IDs were sampled; no imaginary all-7,775 runtime claim. Distinct missing-coordinate or distant-offshore exceptions must be explicitly reported, not silently removed.

**D. Mobile adversarial timing:** cold cache, warm cache, three runs with network delay variation, late measurement content refresh before/after user click, first and second project selection, orientation change, landscape, browser back/forward, reload, tab background/foreground, touch target overlap, map pan, and a disabled/no-network case that produces a clear honest error rather than a fake nearest result.

**E. Preservation:** all 7,775 static Pipeline News source MAP hrefs retain their REPD identity, correct canonical receiver and lat/long when present; 7,749 geographically located and 26 missing-coordinate cases remain distinguishable; 16 interconnectors remain outside the 7,775 count. The V9.20/V9.21 trees, article evidence status, source rights wording and immutable GridAtlas cartridge history must be byte-identical before and after TestCode work.

**F. Negative and integrity probes:** kill a cartridge load, mismatched composition SHA, wrong repd_ref, wrong technology, no actual click, collapsed nearest in hidden DOM, a control under 44px, missing accessible label, a visible result disappearing after 0.5 seconds, and a late stale callback. Every such fixture MUST fail. Do not allow skipped dependencies to silently count as a successful run.

A practical preview threshold is all mandatory deterministic and real three-case tests green, zero unexplained runtime exceptions, and at least 24 valid project samples with first-attempt outcomes recorded. Any red critical first-restore case blocks promotion, regardless of successful retries. This is a limited sampled acceptance threshold, not a guarantee for every onshore project.

## 8. From TestCode proof to a real NON-LIVE GridAtlas preview

TestCode is a measurement layer, not a publisher. It can demonstrate the repair logic and run a local candidate against real browser input, but **an iPhone cannot independently inspect a local CI artifact as a working public website without a separately hosted preview**. Agent 9 therefore needs a second, separately reviewed GridAtlas PREVIEW branch once TestCode's offline and network checks pass.

Read GridAtlas AGENTS.md and docs/RELEASE.md again at that time. Its live state is assembled from an immutable shell and SHA-pinned cartridges; never edit atlas/cartridges/202609241334-sld-sandbox-v9-8.js in place or replace atlas/current.json merely to preview a change. Build a new successor cartridge and composition from preserved source parts, with a fresh, truthful UTC generation and version, a new hashed manifest, a proof and a versioned preview route under atlas/v/<generation>/. Do not invent a generator command for an unassembled cartridge: inspect the existing source, build-cartridge/recompose tools, a suitable parts manifest or seed, and source-specific gates; report if a safe source rebuild cannot be established.

The preview route must remain distinguishable from https://ventusltd.github.io/gridatlas/atlas/ (LIVE). It must be genuinely reachable over HTTPS from the owner's phone and must contain the candidate cartridge digest actually declared by its preview manifest. GitHub Pages can serve an immutable preview after the additive preview PR passes; do not move the live current.json pointer or homepage. If a test-specific launch page supplies a preview deep link, label that as an emulated source-to-preview test, not proof that an unmodified Pipeline News MAP button already directs users to the new candidate. The live emitter must remain canonical until formal release.

A candidate preview landing page should show “TEST PREVIEW / NOT OPERATIVE”, its generation, source SHA, three direct known-case links and a no-confidential-data feedback instruction. The on-phone URL must be supplied by Agent 9 only after the preview is actually published and fetched successfully; no fabricated link.

## 9. Owner's actual iPhone Safari acceptance

The owner is the required human tester; Agent 9 and Agent 8 must not forge an iPhone approval. Agent 9 sends the owner one exact preview URL, the immutable generation and source commit, accompanied by concise steps, not a request to run terminal commands. Use Safari first; other mobile browsers are secondary observations.

**Human walk-through:** Open the clearly labelled TEST preview on iPhone portrait. Start with Botley West REPD 12588. Confirm the correct site/map and that a collapsed project card has a comprehensible plus/Show result control. Tap it **once**. The card must expand and visibly show the nearest-substation calculation, not just an opened tab or moving map. Wait at least five seconds and make sure it stays visible while any background data completes. Pan/zoom the map; dismiss and reopen the card. Repeat with Thorpe Marsh BESS 12453 and onshore wind 14535 using the supplied test links. Observe that selecting another project resets its own initial card without closing the previous project's state incorrectly.

Next turn the iPhone landscape, return to portrait, switch to another app for roughly 20 seconds and return, and reload the preview once. Check there is no blank screen, keyboard-focused obstruction, hidden card behind the toolbar, duplicate stacked card, wrong project identity, unresponsive close control or measurement vanishing after a delayed refresh. Repeat in an ordinary Safari tab and, if practical, a fresh Private tab to distinguish cached and cold behaviour. Try opening an actual existing public V9.21 MAP link separately and label its behaviour “OLD LIVE BASELINE”; do not mistake that for the fixed preview.

For feedback the owner sends **one concise verdict per case**: PASS / FAIL / UNCERTAIN, the project identifier, Safari/iOS version if convenient, a rough time, what the first tap did, whether the value remained visible after five seconds, and optionally a cropped screen recording. Do not include contact details or other private browser tabs. A screenshot alone that shows a hidden result is not a PASS. If any tested first restore fails, keep the old production generation and send Agent 9 the reproducible case.

## 10. Agent 8's independent GitHub/AI acceptance

While the owner performs the iPhone test, Agent 8 separately verifies GitHub rather than adopting Agent 9's claimed results. Fetch the new TestCode PR, GridAtlas preview PR, branch HEADs, actual CI logs, raw artifact receipts, browser traces, source byte hashes and preview manifest. Confirm the clone and tested source match the current PR head; if any commit changed, require a fresh matching run. Check that existing historical GridAtlas and Pipeline News versions remain untouched and that neither PR has secretly modified live pointers, licence statements or homepage data.

Agent 8 will independently run or inspect the same three historical classes and stratified sample at supported Chromium and WebKit widths, including a genuine click-to-receiver proof where possible. Browser simulator/WebKit is not physical iPhone Safari; report those as separate evidence classes. Verify exactly which assets the preview HTTPS endpoint serves, not merely that the source tree includes them. If source and served SHA256 disagree, STOP. Recheck six-cartridge integrity, closest-substation computation, card visibility after first user click, 1.5-second stability, error-free runtime and no false PASS for hidden DOM.

Produce a side-by-side verdict table: original 202611132345, patched candidate preview, actual iPhone Safari, actual GitHub CI, source/served SHA, and outstanding exceptions. Both human and AI must accept the **same candidate generation and commit**. A human PASS for an older preview or a CI PASS against a newer SHA is not combined acceptance.

## 11. Publication sequence, responsibility and rollback

Only when the TestCode gates, genuine GridAtlas preview browser evidence and owner's physical iPhone test are green does Agent 9 request **fresh, explicit owner approval for the GridAtlas versioned release**. GridAtlas docs/RELEASE.md requires owner acceptance on the preview PR, later governed release branch and rebase merge, live-byte check, homepage label/pin and served verification. Agents must not post an owner-looking “ACCEPT <generation>” instruction themselves or treat a shared GitHub account comment as independently authenticated. The release tooling's acceptance guard and separate owner instruction remain mandatory.

The next live GridAtlas composition should be a NEW immutable version, not a rewrite of generation 202611132345 or its 20260924 cartridge. Before changing any pointer, preserve exact previous atlas/current.json, STATE.md, previous seven homepage bundle hashes, public endpoint and all historical release SHAs. Re-run node tools/scope/loop.mjs lint and prove state --stdout matches STATE.md. If release checks are green and the owner separately delegates publishing to Agent 9, Agent 9 may execute the prescribed release path and report exact new SHA and public served bytes.

After GridAtlas is live and verified, Agent 8 must re-run GlobalGrid2050 PR #116 strict producer, integrated, 390/393/1440 browser, exact 7,775 CSV/MAP, and live 390 real GridAtlas nearest tests. V9.22 should remain candidate-only for unsupported news; neither a clean GridAtlas result nor a syntactically valid evidence ledger proves publisher rights. If all Pipeline News release gates pass, the owner may separately delegate the V9.22 app publication and homepage promotion to Agent 9, superseding the earlier Agent 8 sole-publication assignment explicitly. Keep the V9.21 operative link until V9.22 served SHA and rollback are independently established.

A rollback is a tested, reversible pointer change, not deleting a failed new folder. GridAtlas's rollback-generation tool and the homepage owner promotion mechanism must restore the former generation and catalogue, with served-byte verification. Keep the failed/new candidate files for forensic review. Report any partial release honestly; no agent can declare success merely because GitHub Actions was green.

## 12. Final sanity checklist and stop-ship contract

Agent 9's TestCode PR can be called **IMPLEMENTED** only after it includes a reproducible original FAIL, deterministic candidate model, mutation failures proving test sensitivity, exact source SHA pins, real browser receipts, cross-viewport matrix, published artifact links, human test instructions and one explicit limitations section. A synthetic-green receipt validator alone is NOT implemented product behaviour. The GitHub preview may be called **READY FOR OWNER TEST** only when its SHA-pinned immutable candidate actually serves over HTTPS and the candidate's own first-restore tests pass. The user must receive the actual link, not a guessed path.

The **NO-GO** conditions are: hidden nearest after first restore; re-minimise from same-project late refresh; only a retry passes; wrong project/technology/coordinates; missing article/source or REPD preservation; failing hash or cartridge integrity; source/served discrepancy; inaccessible control; unexpected page errors; prior release folder modifications; stale acceptance from another SHA; production pointer changed during TestCode; or an iPhone FAIL. Keep red evidence visible and block auto-publication.

The **GO** conditions are: exactly pinned source and preview; all required offline and real-browser critical checks green; negative mutations red; current owner iPhone PASS on the same immutable preview; independent Agent 8 GitHub/CI PASS; no integrity/history regressions; documented known geographic and rights limitations; previous live rollback ready; explicit new owner approval and release delegation. Approval to test is **not approval to publish**.

Agent 9 must report to Neural Link issue #30 and GridAtlas #87 using the signed PROTOCOL.md message envelope, exact HEAD, CI run URLs, first-attempt failures, browser screenshots and next action. GitHub messages cannot wake an inactive agent. Agent 9 is not yet an acknowledged active session merely because this document exists. The handoff should be placed on its own draft branch/PR and delivered to Agent 9 explicitly; once that agent replies with an ACK link, use GitHub evidence for subsequent communication rather than relying on long chat messages.

**Required final deliverables:** TestCode draft PR and source pin; reproducible red and green cases; independently reviewable browser evidence; candidate GridAtlas immutable preview and actual iPhone URL; human acceptance record; Agent 8 independent acceptance record; precise release/go-no-go proposal; and, only after later owner approval, the published new version with live URL, SHA256 served hashes, re-run Pipeline News tests and tested rollback.

**Signed:** ChatGPT Agent 8 — author of work order and independent GitHub acceptance lead. This document changes no production code, opens no live pointer and grants no present publication approval.
