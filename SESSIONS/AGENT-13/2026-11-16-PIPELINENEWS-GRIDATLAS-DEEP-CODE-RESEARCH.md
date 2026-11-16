# Pipeline News × GridAtlas — source-pinned computer-science research for live Codex agents
**Observation window:** 16 November 2026, GitHub API and source inspection at approximately 18:44–19:00 UTC.  
**Type:** Independent **repository read-only** research; this note alone changes no product code or publication state.  
**Audience:** COMMAND/root release integrator, MODULE ARCHITECT, news/REPD/data-centre/UI owners, QA and up to 16 owner-reported local Windows PowerShell Codex workers.  
**Provenance:** Direct connected-GitHub API/source-file inspection (not a locally executed test suite). GitHub CI status is indicated as *reported by GitHub*, and owner/agent browser claims as *reported by those agents*. Local PowerShell process count, native-device state and public origin bytes were **not** independently observed. External public-page reader returned inaccessible for tested origin URLs.  
**Relationship to other notes:** Complements [preliminary live research index](./2026-11-16-PIPELINENEWS-GRIDATLAS-LIVE-RESEARCH-NOTES.md), [COMMAND checkpoint](./2026-11-16-CODEX-COMMAND-STATE.md), and [coordination issue #42](https://github.com/Ventusltd/neural-link-between-agents/issues/42). Does **not** override newer owner instructions or authorize releases.

## 1. Decision for agents already writing code

**Do not restart V9.25, fork a new UI framework, invent a second feed collector or rewrite immutable releases.** Extract the good existing contracts; build the corrected next edition through the sole COMMAND integrator. Most consequential unresolved business deliverable is **approved real source rights plus useful, independently reviewable project-linked evidence**, not another synthetic test count or editorial score.

At inspection, GitHub reports:
- [Pipeline News PR #125](https://github.com/Ventusltd/globalgrid2050/pull/125) V9.25 merged **18:02:24Z**, merge SHA \`60c778d9789b88ce6a803ac84bff9099e423eec2\`, release folder \`uk_renewables_pipeline/202611161630\`.
- [PR #126](https://github.com/Ventusltd/globalgrid2050/pull/126) V9.26 merged **18:06:51Z**, SHA \`53c437fa23debe16036b87ba3d59cfaca3900105\`, folder \`202611161734\`.
- [PR #127](https://github.com/Ventusltd/globalgrid2050/pull/127) V9.27 merged **18:07:04Z**, SHA \`fb4bd1baaa50c5102a791cf88b9ef23f3fc89a67\`, folder \`202611161747\`.
- Inspected \`globalgrid2050\` **main \`65bcc01e0d7e4dc073e759345727e53cf7a95752\`**, catalogue regeneration at 18:17:59Z. Revalidate on handoff.
- [GridAtlas PR #92](https://github.com/Ventusltd/gridatlas/pull/92) V9.191 merged **17:50:09Z**, main \`1de35f9eca360a5d80d81542230fef546917f5c5\`, generation \`202611161720\`.
- [Homepage-owner PR #20](https://github.com/Ventusltd/globalgrid2050-homepage/pull/20) **OPEN DRAFT / OWNER HOLD**, head \`498f4b6317d5a5a07793619e67d375eda087262f\`. Homepage-owner \`data/homepage.json\` pins Pipeline News operative **V9.24 / \`202611161244\`**, not V9.27. \`globalgrid2050/catalogue/homepage-owner.json\` pins homepage-owner commit \`1a343b8d8e70b4f9e2298e7870f129cbd32db896\`.
- GitHub Actions latest inspected \`v924-public-readback\` run [43927519211](https://github.com/Ventusltd/globalgrid2050/actions/runs/43927519211) returned **success**; [43925459267](https://github.com/Ventusltd/globalgrid2050/actions/runs/43925459267) earlier **failed**. A deploy [43927365188](https://github.com/Ventusltd/globalgrid2050/actions/runs/43927365188) returned **success**. These reports are not a replacement for exact release-version and origin-byte receipts.
- \`v9.28-codex-integration\` and \`v9.29-third-context-ui\` branches exist, but their unmerged working state must **not** be called a release. The owner-command checkpoint reports V9.28's proposed 100 global DC leads/22 countries and V9.29 context work; treat those as branch-specific claims until exact heads/tests are checked.
- The canonical issue contains the user's later **UNFREEZE DEVELOPMENT** message, [comment 6925813697](https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6925813697): resume assigned development/research/testing, **not** unrestricted homepage promotion.

**Source-of-truth hierarchy:** owner instruction in latest #42 comment → production repository \`AGENTS.md\` and authoritative owner manifests → exact branch/commit and CI receipts → current live public readback. \`neural-link-between-agents/CURRENT_PIPELINE_NEWS_VERSION.md\` still describes V9.22/V9.23; it is **historically stale** and should not defeat the newer command checkpoint, homepage owner or commits.

## 2. Owner's current UI acceptance contract: preserve appearance, modularise behavior

The owner explicitly rejected V9.25–V9.27's blue-grey/sans-serif, high-ceremony hero and visible Priority N scoring. The next edition must preserve the **V9.24 black/monospace/cyan-yellow compact style**, with exactly:
1. **GLOBALGRID2050 HEADLINES** — one original headline feed, publisher/date/original link; relevance may sort internally but no visible ranking numbers, explanations or duplicate summary panels.
2. **REPD PIPELINE ANALYTICS** — one principal pipeline region; UK projects, Global Data Centres and later categories live under tabs/search/scroll. No separate Register Changes or Solar-1000 Evidence Pilot panels. Preserve all underlying data.

**Architecture directive:** GridAtlas's stable shell + bounded, versioned, hashed modules is the preferred model. Do not reproduce GridAtlas's unrelated geographic drawing system inside Pipeline News. The specific existing \`Ventusltd/pipelinenews\` repository already contains \`data/\`, \`ui/\`, \`index/\`, \`releases/\` and build/manifest assets. Inspect its real contracts and owner status before authorising a new Ventus News Engine repository/scheduler. [Existing repository README](https://github.com/Ventusltd/pipelinenews/blob/35c7507fe4c164/README.md).

## 3. Best code: cross-repository reuse matrix

| Discipline | Strongest verified source implementation | What to adopt | What **not** to transplant |
|---|---|---|---|
| Immutable official population | [Pipeline Solar-1000 queue](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/research_queue.py#L17-L49): hashes original seed, build manifest and every partition; checks 7,775 total, 3,604 solar, exact first 1,000 numeric IDs | **KEEP** official \`repd_ref\` and pinned population; separate research cohort | No re-sort by file order, reselect, synthetic coordinates or assigning REPD IDs to global DCs |
| Smallest safe source fetcher | [Pipeline fetch](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/fetch.py#L28-L180): one DNS resolution for connect and public-IP veto, HTTPS allowlist, 4MiB/200-entry caps, max four redirects, ETag, strict RSS; [normalise](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/normalise.py#L31-L69) sanitises titles and does not persist bodies | **KEEP/EXTEND** narrowly for approved sources only; add tests for DNS/redirect and feed errors before every new adapter | Do not turn a \`--probe\` into rights grant, build a general web crawler, or bypass paywalls |
| Project association | [Pipeline strict match](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/match.py#L9-L37): explicit “REPD Ref ID” or full unique name; no inferred events; output \`PROVISIONAL\` | **KEEP** false-positive-resistant baseline and full-population name-ambiguity veto | Do not equate name string hit, article count, or high score with independent confirmation |
| Transactional evidence state | [Pipeline SQLite store](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/evidence_store.py#L112-L254): FK enforcement, schema version, article URL PK, project/article association uniqueness, partial unique NULL index, transactional run; immutable first-observed article metadata | **KEEP** separate immutable article facts, provisional matches and run receipts; retain honest nulls | Do not treat a headline scan as individual planning authority research or promote all no-hits to “no evidence exists” |
| Canonical projection / reproducibility | [Pipeline analytics](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/analytics.py#L41-L171): typed DuckDB/Parquet, one-thread sorted ZSTD, schema/hash, every-row readback, orphan checks, runtime pin \`duckdb==1.3.2\` | **KEEP** one SQLite operational store + optional Parquet read model; full-row readback if sizes manageable | No GPU/second DB required for 1,000–7,775 rows; do not confuse analytical readback with factual verification |
| More complete upstream provenance | [Data GridAtlas compiler](https://github.com/Ventusltd/data-gridatlas/blob/8bf88da9e210ce9f61dc0398869d3369f3fa2445/compiler/202608291015-build-v8-transplant.py#L86-L154): source bytes, SHA256, Git blob OID, run/compute identity and source plan; [merge closure](https://github.com/Ventusltd/data-gridatlas/blob/8bf88da9e210ce9f61dc0398869d3369f3fa2445/compiler/202608291015-build-v8-transplant.py#L448-L488) checks exactly 56 source partitions and membership count | **ADAPT** complete-source closure manifest, byte/row/schema checks, signed review receipt association per input | Do not copy large layer-specific V8 geometry compiler, its fixed 56-source counts or topology logic into the news engine |
| Modular UI substrate | [GridAtlas current.json](https://github.com/Ventusltd/gridatlas/blob/1de35f9eca360a5d80d81542230fef546917f5c5/atlas/current.json) declares \`IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES\`, module order, slots, expected hashes, previous generation and fixed live route; [scope contract](https://github.com/Ventusltd/gridatlas/blob/1de35f9eca360a5d80d81542230fef546917f5c5/AGENTS.md) | **ADAPT** small module manifests (\`id,version,sha256,slot,input_schema,output_schema,fallback\`) to existing Pipeline plugin host | Do not create another frontend framework or copy 300 generated files to implement a two-block visual change |
| News discovery ranking | [Pipeline V9.26 algorithm](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/news_algorithm.py#L165-L232), [SHA-bound priority spec](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/NEWS_PRIORITY.md) | **KEEP BACKEND ONLY** exact-original headline, original publisher/link, freshness fallback and content-addressed ranking sidecar | Do not render visible ranks/points; do not call publisher variety “independent corroboration” |
| Research priority without truth inflation | [Pipeline prospecting](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/prospecting.py#L139-L151): UNKNOWN corporate eligibility/heat, event_at NULL; [strict input review](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/prospecting.py#L174-L218) for rights/access and [ID separation](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/prospecting.py#L254-L317) for \`DC-WD-Q...\` | **KEEP as triage hint**, preserve \`UNKNOWN\`, \`PROVISIONAL\`, null MW; separate Global DC and REPD identity namespaces | Do not turn provisional research score into a project event, finance claim, verified lead or scored public UI |
| Map/identity bridge | [Pipeline canonical deep-link builder](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/uk_renewables_pipeline/202611161747/scripts/core/atlas-receiver-v9-7.js#L280-L313) uses \`repd_ref\`, technology, coordinates only if valid; [interconnector map link](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/uk_renewables_pipeline/202611161747/scripts/core/atlas-interconnector-link-v9-8.js) uses separate identity | **KEEP** different technology IDs and graceful unavailable reason; test the receiver itself, not just HTTP 200 | Do not use REPD ID for interconnector/DC, assume offshore equals mainland point, or call loaded page proof grid-engine fired |
| State + release correctness | [GridAtlas deterministic state](https://github.com/Ventusltd/gridatlas/blob/1de35f9eca360a5d80d81542230fef546917f5c5/tools/scope/loop.mjs#L30-L44) pins LF published bytes (important on Windows); [full local promotion rehearsal](https://github.com/Ventusltd/gridatlas/blob/1de35f9eca360a5d80d81542230fef546917f5c5/tools/release/map-promotion-rehearsal.mjs); [Pipeline inherited feature contract](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/pipeline_release/feature_contracts.py) permits **explicit** presentation migrations | **COMBINE** GridAtlas stable shell/manifest and local promotion rehearsal with Pipeline feature-withdrawal receipts and homepage served-byte transformation audit | Never treat \`sha256(index-source)\` as equal to post-import homepage root hash; never edit dated published trees |

**Engineering distinction:** Data GridAtlas is best as an example of **compiled data closure and hash-pinned analytical artifacts**. GridAtlas itself is best as **a stable map substrate and cartridge composition release discipline**. Pipeline News already has strong **provisional evidence and link contracts**. These are compatible patterns, not one codebase to overwrite the other.

## 4. Findings: verified source behavior vs targeted hypotheses

### F1 — P0, source-verified semantic risk: “research attempted” overclaim
[EvidenceStore.record_run lines 208–223](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/evidence_store.py#L208-L223) writes \`researched_at=fetched_at\` for **all 1,000** seed projects and \`RESEARCH_ATTEMPTED_NO_EVIDENCE\` when no strict article match. But [run.collect lines 17–29](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/run.py#L17-L29) only scans the bounded RSS feed, not each project or local authority. The serialized [snapshot](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/evidence_store.py#L226-L253) **does** say explicitly “not independent project-first research; no match is not proof no evidence exists”, so the storage is more qualified than the row status name.

**Decision:** Treat current status as “no match in the bounded source window”, not “the project's external evidence has been exhaustively researched”. Before any UI reuse, create an explicit \`search_method=NEWS_FEED_SCAN\`, per-project scope/attempt receipt, and display text that preserves this limitation. Implement genuine project-first research separately. Test that zero hits and blocked source do not silently become completed independent project investigation. This is a **semantics risk established by reading code**, not a claim that an observed public UI already made a false statement.

### F2 — P0, verified policy gate: no accepted real solar evidence published
[Actual sources.yaml](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/sources.yaml) says PV Magazine \`enabled:false\`, \`rights_status:unknown\`. [Acquisition README](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/README.md) reports one **probe**, HTTP 200, 10 articles, zero strict Solar-1000 matches at 16:27:39Z; earlier 403; **no accepted real evidence snapshot**. [fetch.py](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/fetch.py#L123-L177) rejects production fetches when rights are not accepted.

**Decision:** Do not set \`enabled:true\` merely to make a green run or invent a finding. Resolve rights/licensing/source approval through responsible human review, or add a genuinely permitted official source adapter with exact identity. A transport probe is not a legal licence, project match, or fresh event.

### F3 — P0, independently confirmed owner gate: interface promotion blocked
[Issue #42 owner direction](https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6925200793) and [COMMAND checkpoint](./2026-11-16-CODEX-COMMAND-STATE.md) reject the new style and visible scores. [Homepage PR20](https://github.com/Ventusltd/globalgrid2050-homepage/pull/20) is **draft**. Current homepage-owner entry has \`pipeline-news.operative_release_id=202611161244\`; \`versions.json\` on producer main similarly records V9.25 as evidence-disabled software candidate and V9.24 operative.

**Decision:** Root only: preserve already merged dated version URLs, rebuild presentation in a **new** edition, rerun a visual-contract Chrome comparison to V9.24, and leave homepage-owner PR20 on HOLD until accepted. The subsequent user “Unfreeze” removes the broad development pause, **not** a precise publication gate.

### F4 — P0, verified release interface: safe CAS is not all-workflow serialization
[Pipeline publish.py](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/publish.py#L9-L22) checks that the candidate HEAD has the expected parent, then pushes \`HEAD:refs/heads/pipeline-evidence-data\` with **\`--force-with-lease=<ref>:<expected_sha>\`**. This is a conditional compare-and-swap-style remote ref update, **not** an unconditional force push. It protects against a stale expected head, but does not make a transaction across homepage repo, multiple branches, data services or a browser CDN.

**Decision:** Retain exact expected SHA check, fail on mismatch, no force retry; one designated evidence-data writer per branch and one root publisher. Integrate snapshot directory and its latest pointer into **one commit**. Test two writers started from the same parent: exactly one should win; loser must fetch new head, inspect conflict and rebuild, not reset another agent. Inspect branch protection and workflow permissions before modifying push strategy.

### F5 — P1, code-inspected scaling hypothesis: editorial rank O(n²)
[news_algorithm.py lines 215–228](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/news_algorithm.py#L215-L228) repeatedly runs \`min(candidates,key=...)\` and \`candidates.remove(picked)\` while publisher penalty changes. That is quadratic in headline count. The function caps input at 10,000, whereas current normal daily headline feeds are tens, so **no measured production bottleneck is established**.

**Decision:** Keep current semantics. If a benchmark demonstrates unacceptable growth at 2,000–10,000 items, optimise the grouped priority queues and prove exactly identical ordered output/credits on fixed and random fixtures. Do not install CuPy for text parsing, HTTP or a small greedy ranking loop.

### F6 — P1, targeted identity regression surface
[match.py](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/match.py#L13-L37) requires full unique names or explicit IDs and marks every association provisional. [normalise_article](https://github.com/Ventusltd/globalgrid2050/blob/65bcc01e0d7e4dc073e759345727e53cf7a95752/automation/news/acquisition/normalise.py#L47-L69) retains query parameters in canonical article URL, so different tracking URLs could remain distinct article identities. This is an **adversarial test opportunity**, not evidence of a present production duplicate.

**Decision:** Add metamorphic fixtures: names reordered/Unicode-normalised, shared names, fake REPD numbers in unrelated paragraphs, same article with tracking query variants, one URL associated to two projects, same URL changed title/date, invalid future source timestamp. Reject or quarantine uncertain merges rather than masking conflict with count deduplication.

### F7 — P1, full release-tree duplication vs durable modular shell
The three merged Pipeline PRs touched **307**, **269**, and **290** files respectively, dominated by immutable copied dated release trees (not 866 independent source-code modules). GridAtlas [AGENTS.md](https://github.com/Ventusltd/gridatlas/blob/1de35f9eca360a5d80d81542230fef546917f5c5/AGENTS.md) instead mandates immutable app shell, cartridges, ordered manifest and atomic composition pointer.

**Decision:** Propose a small Pipeline plugin boundary \`id/version/input_schema/output_schema/slot/sha256/fallback/owner\` in the **existing** plugin host/manifest, with a validator and two-block visual-contract fixture. Do not retrofit historical release directories or introduce live dynamic imports from unreviewed origins. Preserve a flat export for browsers that cannot load optional modules.

### F8 — P1, CI/operational evidence vs unsupported live claim
GitHub shows successful recent runs for deploy, public-readback, release ledger and PR test workflows; [COMMAND checkpoint](./2026-11-16-CODEX-COMMAND-STATE.md) reports Chrome 375/768/1440 origin tests and dated version URLs served. The independent public reader for three tested origin URLs returned inaccessible in **this** research context, so we did **not** collect raw origin bytes or rerun Chrome. The **homepage operative V9.24** is nevertheless independently confirmed from the owner repository configuration.

**Decision:** Every promotion must attach (a) exact head SHA, (b) CI run ID and green check list, (c) source output SHA, (d) homepage-import-transformed bytes SHA where relevant, (e) served-root SHA and HTTP readback, (f) actual browser MAP/engine observation, (g) immutable rollback ref. Do not use “HTTP 200 on GridAtlas shell” as proof that the grid engine accepted a project.

## 5. GridAtlas–Pipeline boundary: formal invariants

**Identity.** REPD solar/BESS/wind = \`repd_ref\` from official partition. Interconnector identity is independent. Data centres are \`DC-WD-Q...\` (Wikidata source indexed, not REPD). GridAtlas receiving URL may use \`repd_ref\`, \`technology\`, and optional valid lat/lon. No invented 0,0 coordinates; null geometry must remain null.

**Population.** Frozen original selected Pipeline population: 7,775 rows; 3,604 solar; exactly 1,000 Solar-1000 in ascending numeric REPD references from immutable V9.24. GridAtlas register has a different population: prior \`versions.json\` MAP contract reported 11,329 registry records, 5,334 active Pipeline rows, 5,331 active resolved and 3 geographically outside its register. This is an **older pinned measured contract** and should be rerun against V9.191; it is not proof every Pipeline row receives an identity card. Rows outside active statuses still need a usable MAP/point or a truthful unavailable reason.

**Provenance.** Separate times: \`published_at\` (publisher), \`observed_at\` (collector), \`last_seen\` (collector), \`event_at\` (only independently evidenced event), \`generation_at\` (build), \`released_at\` (deployment). Unknown event dates stay null. Never use snapshot generation time as project event time.

**Evidence state machine.** \`SOURCE_DISCOVERY\` → \`FETCHED_AND_RIGHTS_ELIGIBLE\` → \`NORMALISED\` → \`PROVISIONAL_ASSOCIATION\` → \`INDEPENDENT_REVIEW\` → \`ACCEPTED/REJECTED\`. Only reviewer-authored provenance supports accepted project assertions. Discoveries (including permitted paywalled headline/link metadata) may drive research but never authenticate underlying financing or MW facts.

**Deterministic computation.** Same pinned input files, schema, profile, UTC clock and runtime ⇒ same canonical logical output and hashes. \`duckdb==1.3.2\` and \`threads=1\` are already documented for the analytical projection. Run every-row Parquet readback and content closure. Record runtime versions. Metadata clocks must be explicit inputs in test fixtures.

**Publication.** Immutable version directories remain immutable. Git data-branch pointer and evidence snapshots must be committed in one ref update; homepage-owner promotion is a separate authorised step with exact expected owner pin and rollback. GitHub Actions \`concurrency\` group names do not, by themselves, confer transaction isolation across unrelated workflows and repositories. Release control belongs to COMMAND.

**Presentation.** Stable V9.24 visual shell and two-block vocabulary. Optional plugins cannot change colour/typography/panel count. Rank stays internal. Article/publisher HTML is escaped and the original source link retained. The existing GridAtlas MAP button must fire the actual receiver and show identity or a reason, not merely open a 200 page.

## 6. Fifteen-minute actionable QA/reuse checkpoints (research suggestions, NOT reassignment)

Each ticket is owner-dependent. File scope and actual PR owner must be ACKed in issue #42 before anyone edits; if a worker already owns the path, that worker takes the fixture or declines it.

- [ ] **QA-01** Pin \`globalgrid2050\` current main, \`gridatlas\` current main, \`data-gridatlas\` main and homepage-owner main SHAs. Capture one-page version/owner/branch matrix with UTC.
- [ ] **QA-02** Read current #42 owner thread tail and \`SESSIONS/AGENT-13/2026-11-16-CODEX-COMMAND-STATE.md\`. Record the single root/UI/DC/context/news ownership boundaries; no duplicate writer.
- [ ] **QA-03** Assert \`load_seed_projects()\` returns exactly the original 1,000 numeric IDs and total source REPD 7,775/solar 3,604, with hash-mismatched part negative fixture.
- [ ] **QA-04** Add failing semantic fixture if UI calls a feed-only no-hit “independent project research completed”; separate actual attempted searches from news source coverage.
- [ ] **QA-05** Test fetch \`timeout,403,429,500,304-no-cache,ETag-mismatch,redirect-private-IP,DNS-private-address,oversized XML,malformed XML\`: no state update on critical failure.
- [ ] **QA-06** Verify \`sources.yaml\` disabled/rights-unknown gate. No automated production activation or fabricated project match.
- [ ] **QA-07** Test provisional matching for shared names, exact REPD IDs, NFKC, duplicate URLs, different trackers and changed metadata.
- [ ] **QA-08** Test repeated SQLite successful run and exported identity checksum, one no-evidence marker per project and zero \`VERIFIED\`.
- [ ] **QA-09** Test \`analytics.py\` immutable target collision, typed schema, ZSTD, full-row Parquet equality, orphan rejection, null coords.
- [ ] **QA-10** Inject two concurrent Git evidence branch publishers from the same expected head: exactly one remote update; no overwrite.
- [ ] **QA-11** Tamper \`pipeline_headlines.rank.json\` digest/profile/rank/identity/clock; client must display original source/date order, not fabricated replacement.
- [ ] **QA-12** Compare exact V9.24 screenshots to candidate at 375, 768, 1440px: colours/font/row density/two panel count; no visible Priority N.
- [ ] **QA-13** Test Pipeline MAP URLs for active onshore REPD, near-shore, no-geometry, inactive, interconnector and distant offshore; verify actual GridAtlas receiver/engine behavior.
- [ ] **QA-14** Check existing \`Ventusltd/pipelinenews\` and its collector ownership before adding Ventus News Engine; no second schedule.
- [ ] **QA-15** Record exact-source vs post-homepage-import vs public-served SHA stages and accepted rollback, using an independently run browser receipt.
- [ ] **QA-16** Update stale coordination version text only as a separately owned documentation change with approval; preserve historic narrative.

### Suggested commands (run ONLY in your own clean isolated Windows PowerShell worktree)
\`\`\`powershell
git status --short --branch
git fetch origin
git rev-parse HEAD
py -m pytest -q automation/news/tests/test_acquisition.py automation/news/tests/test_evidence_store.py automation/news/tests/test_acquisition_analytics.py automation/news/tests/test_news_algorithm.py automation/news/tests/test_prospecting.py
py -m automation.news.acquisition.research_queue
py -m automation.news.acquisition.run --probe --report tmp/source-probe.json
\`\`\`
The probe contacts the currently disabled **explicit health endpoint**; coordinate source access policy and do **not** publish probe results as evidence. For browser tests, use a separate port per worker:
\`\`\`powershell
Push-Location automation/news/acquisition/browser
npm ci --ignore-scripts
$env:EVIDENCE_TEST_PORT = "45431"
npx playwright test --config news-priority.config.mjs
Pop-Location
\`\`\`
For GridAtlas **in its separate clone/worktree**, not the Pipeline repository:
\`\`\`powershell
node tools/scope/loop.mjs lint
node tools/scope/loop.mjs state --stdout
\`\`\`
These are **reproduction instructions**, not claims that this research session executed them. Do not run a destructive release rehearsal in another agent's checkout.

## 7. Agent integration protocol for 16 concurrent local sessions

The number 16 is **owner-reported**; GitHub shows branches/PRs, not running PowerShell processes. Each agent should publish:
\`\`\`text
[NL-042][CODEX]
agent / owner:
repo / branch / HEAD:
base main SHA:
owned paths (exclusive):
dependency PRs:
schema/contract versions:
one next <=15min check:
test command + result:
commits + PR:
blocker / reviewer:
release write authority: NO (unless COMMAND)
\`\`\`
Recommended PR order: **contracts and baseline gates → isolated source/data and algorithm changes → stable visual shell contract → distinct plugin consumers → root integration → full test suite and exact-head release receipt → owner homepage approval**. Never merge two branches with conflicting generated dated directories by blind cherry-pick. Never run two workers against one mutable PowerShell worktree, shared npm install directory, SQLite DB or test server port. Detached worktrees, per-agent cache/test dirs and branch-specific ports are mandatory. A branch existing is **not** evidence a worker is still alive or ready.

**Minimal success report, rather than test-count theatre:** \`<SHA, input digest, code contract, test result, negative fixture, output digest, CI URL, actual browser/served receipt, rights state, rollback ref>\`. If a field is unknown, write UNKNOWN and retain the reason. Separate a software PASS from an evidence ACCEPTED and publication PASS.

## 8. Priority and disposition

**P0 NOW:** owner-approved V9.24 two-block visual shell; no live homepage promotion until accepted; source-rights and actual evidence gating; source/REPD identity invariants; no mislabelled “researched” state; preserve GridAtlas deep-link engine; exclusive publication lock and browser/served checks.

**P1 NEXT:** reuse one manifest-driven modular shell and adapter interfaces; optimize only proven hot loops; add project-first official source receipts; integrate real approved evidence review into concise REPD row remarks; improve branch ownership index and stale coordination docs.

**P2 LATER:** worldwide source spiders, GPU/CuPy, massive backfills, new analytics engines, full cross-category graph, second platform frontend. CPU DuckDB/SQLite is already demonstrably the correct complexity level for this size.

### Reliability caveat
This note is a **static source audit** at a stated observation time. It verifies repository file content, GitHub merge records, homepage configuration, source adapter disabled state, and code-level contracts. It **does not** independently validate every README test claim, install Chrome locally, inspect the user's 16 PowerShell sessions, confirm source-rights acceptance, fetch the origin's exact bytes, or authorise release. Root integrator should report newer contrary evidence, not silently overwrite this audit.