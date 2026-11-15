# Agent 9 — GridAtlas mobile result-card repair: 3,000-word TestCode implementation and dual human/AI sanity-check mandate

**Author:** ChatGPT Agent 8, on the owner's instruction, 15 November 2026. **Recipient:** a separately invoked ChatGPT Agent 9. **Status:** proposed work order, not an Agent 9 acknowledgement or a release authorisation. **Canonical coordination:** https://github.com/Ventusltd/neural-link-between-agents/issues/30 and https://github.com/Ventusltd/gridatlas/issues/87.

**Objective:** repair the first mobile GridAtlas result-card restore so a calculated nearest-substation answer stays visible after one real tap, while preserving the owner's map-first default. Agent 9 works in isolated TestCode; a later, separately governed GridAtlas preview enables the owner's actual iPhone Safari test and Agent 8's independent GitHub verification. Only after both pass may the owner explicitly delegate a new-version production release.

## 1. What exists and what is genuinely broken

Current GlobalGrid2050 Agent 8 V9.22 PR #116, source 998c4cddbd78f04bcdd9df2a40026ac91714cd2f, is not merged. V9.21 remains publicly operative; V9.20 is retained. Producer, CSV and most browser gates passed, but actual mobile GridAtlas acceptance failed: https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946/job/132873210740. The REPD extract retains 7,775 original identities.

In that real browser run, REPD 12588, Botley West solar, generated a correct link, opened the GridAtlas composer, loaded six hash-verified cartridges, enabled the expected technology and project layers, and computed the nearest 400 kV Cowley substation, approximately 15.76 km straight-line. The value appeared in hidden DOM. Nevertheless, after an actual automated tap on the restore button, the bottom card was again minimised and the result was not visible. REPD 12453 BESS and REPD 14535 onshore wind passed that particular 390px run; earlier runs failed other samples. Desktop 1440px passed the three-class sample. Therefore the bug is intermittent **result presentation**, not established failure of electrical/geographical calculation, and neither side can honestly claim fleet-wide reliability.

Live GridAtlas generation 202611132345 (v9.189) uses atlas/cartridges/202609241334-sld-sandbox-v9-8.js. Its restore click toggles gridatlas-min while resetCardGeometry can reapply minimisation after late content injection. That is a plausible race, not yet a proven event sequence. Agent 9 must collect old FAIL and new PASS traces.

Reference evidence:
- https://github.com/Ventusltd/gridatlas/issues/87
- https://github.com/Ventusltd/globalgrid2050/actions/runs/43734245946/artifacts/14169423246
- https://github.com/Ventusltd/testcode/pull/12
- https://github.com/Ventusltd/globalgrid2050/pull/116

## 2. Agent 9 identity, limits and exclusive Git write lane

On first invocation, Agent 9 must read the complete Neural Link AGENTS.md, PROTOCOL.md, LINK-RULE.md, all new issue #30 messages and GridAtlas issue #87; explicitly acknowledge this handoff using its exact GitHub comment URL. Then read TestCode README.md, engines.json and run.mjs, GridAtlas AGENTS.md, STATE.md, atlas/current.json, docs/RELEASE.md and the relevant cartridge's actual committed bytes. Re-fetch current HEADs before any implementation. The SHA values here are recovery baselines, not permission to ignore later commits.

Work only on an exclusive TestCode branch qa/agent9-gridatlas-first-restore-20261115, created from fresh main. Keep the draft PR isolated. Do not write to GlobalGrid2050 PR #116, Agent 7 PR #115, GridAtlas live, homepage, REPD or Agent 3 TestCode PR #12; use Agent 3's validator with explicit attribution and exact pin, not an unreviewed branch takeover.

Use sandbox/gridatlas-agent9-first-restore/ for the harness, source manifest, cases, negative tests, actual Playwright receipts, documentation and runner. Add shared drivers only when justified. Do not register a new estate-wide PASS before offline and network behaviour have independently passed.

## 3. Follow TestCode's ordering rule, not a happy-path shortcut

The current TestCode README is explicit: OFFLINE first; NETWORK only if offline is green; PUBLISH never from TestCode. Its runner uses node run.mjs, with --with-network as a deliberate separate step. A missing input is FAIL, not SKIP and certainly not PASS. Tests must inspect the source bytes actually composed and served, not an unexecuted part or an invented fixture labelled as live. Report independent measurements; a GitHub Action green check is meaningful only for the precise code and evidence it executed.

Pin exact source commit, composed generation, cartridge path/SHA256, Pipeline News release, REPD extract, browsers, viewports and test mode. Read only clean, explicit adjacent checkouts; reject drift or missing inputs until consciously repinned.

Reproduce the original red test first, logging card creation, resetCardGeometry calls, injection, user click, CSS changes and timestamps. Preserve screenshot/trace; separately label artificial timing injection versus unmodified live browser observations.

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

Agent 3 PR #12 already includes a fail-closed receipt validator and 15 synthetic negative/control checks. Extend its intent but never call those synthetic selftests actual GridAtlas/browser acceptance.

## 6. What a real browser receipt must prove

Bind every receipt to one Pipeline News Git SHA, one GridAtlas generation/SHA, exact REPD reference and source coordinates, actual MAP href/clicked URL, browser, viewport, local or preview mode, and UTC timestamps. Separate source identity from public served bytes.

The browser must inspect the real destination: canonical receiver path; expected exact repd_ref, technology and coordinates; loaded generation; hash-verified shell and each cartridge; no unhandled JS errors; technology and project layer actually enabled; destination not stuck on a spinner; real nearest-substation data computed. Record the substation name and distance as geographic screening only, never as available grid capacity, permissible cable route or connection offer.

Presentation is a separate PASS. The browser must physically click the visible restore button once, verify the project card is no longer minimised, find nearest text in actually visible rendered content, confirm the card and control are on screen, and observe the result stable for at least 1.5 seconds. Also observe after 5 seconds and after a purposely delayed same-project update. A hidden DOM match is useful to diagnose computation but cannot turn visibility FAIL into PASS. Do not count repeated clicks, retries, a mocked popup, a fake response or text in an offscreen element as successful first interaction.

Save immutable JSON verdicts, screenshots, trace or video, console/network errors and source-versus-served hashes. Without genuine evidence status is UNVERIFIED; retries never erase a first-attempt FAIL.

## 7. Automated sanity-check matrix

Run the following minimum groups; expand beyond three projects once the first defect is fixed:

**A. Deterministic offline state:** initial phone card collapsed, explicit restore expanded, a late same-project measurement keeps it expanded, manual re-minimise stays minimised, switching project resets to intended first-arrival state, stale callback cannot touch a new selection, desktop geometry remains intact, controls and aria attributes track CSS exactly. Deliberately mutate each rule to confirm the suite turns red.

**B. Three historical live cases:** REPD 12588 solar, 12453 BESS, 14535 onshore wind, at 390px Chromium, 393px WebKit and 1440px Chromium. Use correct frozen REPD coordinates from the checked source, never copied or made-up numbers. Compare the unrepaired GridAtlas generation 202611132345 with the test candidate; each case must have a first-attempt verdict, not just a winner among several repeats.

**C. Broader genuine project sample:** add at least 24 independently selected valid-coordinate REPD IDs stratified across solar, BESS, onshore wind, nearshore/offshore where geographically appropriate, regions, statuses, projects close to a substation and projects beyond the displayed draw radius. Document how IDs were sampled; no imaginary all-7,775 runtime claim. Distinct missing-coordinate or distant-offshore exceptions must be explicitly reported, not silently removed.

**D. Mobile adversarial timing:** cold cache, warm cache, three runs with network delay variation, late measurement content refresh before/after user click, first and second project selection, orientation change, landscape, browser back/forward, reload, tab background/foreground, touch target overlap, map pan, and a disabled/no-network case that produces a clear honest error rather than a fake nearest result.

**E. Preservation:** all 7,775 static Pipeline News source MAP hrefs retain their REPD identity, correct canonical receiver and lat/long when present; 7,749 geographically located and 26 missing-coordinate cases remain distinguishable; 16 interconnectors remain outside the 7,775 count. The V9.20/V9.21 trees, article evidence status, source rights wording and immutable GridAtlas cartridge history must be byte-identical before and after TestCode work.

**F. Negative and integrity probes:** kill a cartridge load, mismatched composition SHA, wrong repd_ref, wrong technology, no actual click, collapsed nearest in hidden DOM, a control under 44px, missing accessible label, a visible result disappearing after 0.5 seconds, and a late stale callback. Every such fixture MUST fail. Do not allow skipped dependencies to silently count as a successful run.

## 8. From TestCode proof to a real NON-LIVE GridAtlas preview

Read GridAtlas AGENTS.md and docs/RELEASE.md again at that time. Its live state is assembled from an immutable shell and SHA-pinned cartridges; never edit atlas/cartridges/202609241334-sld-sandbox-v9-8.js in place or replace atlas/current.json merely to preview a change. Build a new successor cartridge and composition from preserved source parts, with a fresh, truthful UTC generation and version, a new hashed manifest, a proof and a versioned preview route under atlas/v/<generation>/. Do not invent a generator command for an unassembled cartridge: inspect the existing source, build-cartridge/recompose tools, a suitable parts manifest or seed, and source-specific gates; report if a safe source rebuild cannot be established.

The preview route must remain distinguishable from https://ventusltd.github.io/gridatlas/atlas/ (LIVE). It must be genuinely reachable over HTTPS from the owner's phone and must contain the candidate cartridge digest actually declared by its preview manifest. GitHub Pages can serve an immutable preview after the additive preview PR passes; do not move the live current.json pointer or homepage. If a test-specific launch page supplies a preview deep link, label that as an emulated source-to-preview test, not proof that an unmodified Pipeline News MAP button already directs users to the new candidate. The live emitter must remain canonical until formal release.

Preview page must say TEST / NOT OPERATIVE, give genuine generation/SHA and project links, and be reachable via HTTPS before asking the owner to test it. Never invent its URL.

## 9. Owner's actual iPhone Safari acceptance

The owner alone performs physical iPhone approval. Agent 9 supplies one actual HTTPS preview URL, source SHA and brief steps; Safari first, other browsers optional.

**Human walk-through:** Open the clearly labelled TEST preview on iPhone portrait. Start with Botley West REPD 12588. Confirm the correct site/map and that a collapsed project card has a comprehensible plus/Show result control. Tap it **once**. The card must expand and visibly show the nearest-substation calculation, not just an opened tab or moving map. Wait at least five seconds and make sure it stays visible while any background data completes. Pan/zoom the map; dismiss and reopen the card. Repeat with Thorpe Marsh BESS 12453 and onshore wind 14535 using the supplied test links. Observe that selecting another project resets its own initial card without closing the previous project's state incorrectly.

Next turn the iPhone landscape, return to portrait, switch to another app for roughly 20 seconds and return, and reload the preview once. Check there is no blank screen, keyboard-focused obstruction, hidden card behind the toolbar, duplicate stacked card, wrong project identity, unresponsive close control or measurement vanishing after a delayed refresh. Repeat in an ordinary Safari tab and, if practical, a fresh Private tab to distinguish cached and cold behaviour. Try opening an actual existing public V9.21 MAP link separately and label its behaviour “OLD LIVE BASELINE”; do not mistake that for the fixed preview.

For each case the owner returns PASS, FAIL or UNCERTAIN, project ref, first-tap result, five-second stability, rough time and optional cropped recording. Never include personal tabs; a screenshot with hidden content is not approval.

**iPhone evidence integrity:** The phone verdict must name the preview generation and visible build SHA. Agent 9 records the owner's dated response, not an agent-authored imitation of human approval. If the browser still holds an earlier cached build, clear that discrepancy and repeat the test. Never combine an iPhone PASS on one preview with GitHub CI from a different source commit.

## 10. Agent 8's independent GitHub/AI acceptance

While the owner performs the iPhone test, Agent 8 separately verifies GitHub rather than adopting Agent 9's claimed results. Fetch the new TestCode PR, GridAtlas preview PR, branch HEADs, actual CI logs, raw artifact receipts, browser traces, source byte hashes and preview manifest. Confirm the clone and tested source match the current PR head; if any commit changed, require a fresh matching run. Check that existing historical GridAtlas and Pipeline News versions remain untouched and that neither PR has secretly modified live pointers, licence statements or homepage data.

Agent 8 will independently run or inspect the same three historical classes and stratified sample at supported Chromium and WebKit widths, including a genuine click-to-receiver proof where possible. Browser simulator/WebKit is not physical iPhone Safari; report those as separate evidence classes. Verify exactly which assets the preview HTTPS endpoint serves, not merely that the source tree includes them. If source and served SHA256 disagree, STOP. Recheck six-cartridge integrity, closest-substation computation, card visibility after first user click, 1.5-second stability, error-free runtime and no false PASS for hidden DOM.

Tabulate old live state, new preview, actual iPhone Safari, AI GitHub checks, served hashes and exceptions. Human and AI acceptance must refer to the same source generation and commit.

## 11. Publication sequence, responsibility and rollback

Only when the TestCode gates, genuine GridAtlas preview browser evidence and owner's physical iPhone test are green does Agent 9 request **fresh, explicit owner approval for the GridAtlas versioned release**. GridAtlas docs/RELEASE.md requires owner acceptance on the preview PR, later governed release branch and rebase merge, live-byte check, homepage label/pin and served verification. Agents must not post an owner-looking “ACCEPT <generation>” instruction themselves or treat a shared GitHub account comment as independently authenticated. The release tooling's acceptance guard and separate owner instruction remain mandatory.

Publish a NEW GridAtlas cartridge and generation, never rewrite the 20260924 file. Before release, record old current.json, STATE.md, seven homepage hashes and rollback URLs; run GridAtlas lint/state checks. A new owner instruction must authorise any Agent 9 merge.

After GridAtlas is live and verified, Agent 8 must re-run GlobalGrid2050 PR #116 strict producer, integrated, 390/393/1440 browser, exact 7,775 CSV/MAP, and live 390 real GridAtlas nearest tests. V9.22 should remain candidate-only for unsupported news; neither a clean GridAtlas result nor a syntactically valid evidence ledger proves publisher rights. If all Pipeline News release gates pass, the owner may separately delegate the V9.22 app publication and homepage promotion to Agent 9, superseding the earlier Agent 8 sole-publication assignment explicitly. Keep the V9.21 operative link until V9.22 served SHA and rollback are independently established.

## 12. Final sanity checklist and stop-ship contract

TestCode IMPLEMENTED means a reproduced old FAIL, candidate model, mutation negatives, exact pins, real browser receipts and limitations. READY FOR IPHONE means a hash-pinned preview genuinely serves over HTTPS and its own browser tests pass. Synthetic-green selftests never certify the product.

**NO-GO:** failed first restore, late re-minimisation, retry-only PASS, wrong REPD/technology, hidden-only result, runtime/hash/served-byte mismatch, inaccessible control, prior-release rewrite, or iPhone failure. Keep every red receipt.

**GO:** same preview SHA passes offline, real-browser and negative checks, physical iPhone test and independent Agent 8 GitHub verification, with safe rollback. New explicit owner approval/delegation remains mandatory.

Agent 9 must post a signed ACK and later exact-SHA evidence to Neural Link issue #30 and GridAtlas #87. GitHub comments do not wake inactive agents; this handoff does not imply Agent 9 has started.

**Signed:** ChatGPT Agent 8 — author of work order and independent GitHub acceptance lead. This document changes no production code, opens no live pointer and grants no present publication approval.

