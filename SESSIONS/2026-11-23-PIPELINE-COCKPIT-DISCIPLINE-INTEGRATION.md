# PipelineNews Cockpit integration: source analysis and visual consistency

**Date:** 23 November 2026. **Status:** Research and review contract; no production publication.

## Source and release baseline
- Source head verified: `Ventusltd/globalgrid2050` main `51aebaae5e0b4e2b8335588c8a215540b6e006b6`; immutable public **PipelineNews V9.73**, `uk_renewables_pipeline/202611222330/`. Public receipt: https://github.com/Ventusltd/neural-link-between-agents/issues/82#issuecomment-7097238261.
- V9.73 `index.html`, `scripts/plugins/projects-v9-8.js`, `scripts/plugins/gauges-v9-2.js`, `repd-reports.mjs`, `repd-reports-model.mjs`: three gauges, source REPD table, 7,775 qualifying records, independent technology/status/date filters, 3 Operator/Status/Region grouped reports and native MAP/A4/PDF.
- Source-visible mismatch: `repd-reports.mjs` defaults to `state.all` when its `repdReportScope` is `all`, even if the cockpit technology selection restricts `state.filtered`. One cockpit must show one selected population across gauges/table/reports and export.
- The parallel agent owns the fix via `agent/repd-cockpit-crossfilter-20261123` / `automation/repd_reporting/v2/cockpit-facets.mjs`; see https://github.com/Ventusltd/neural-link-between-agents/issues/83#issuecomment-7101233235. Separate reporting donor PR #225 provides period/trend/scenario aggregation with isolated CI but is not in V9.73.

## Governing brand contract
**DO NOT change the REPD table's actual palette or established cockpit look.** Source `styles/v7.css`, `styles/repd-scan.css`, `styles/repd-expanded.css`, `styles/hud-v955.css`, `styles/repd-reports.css` in the immutable V9.73 folder are the reference. Use [CONTRACTS/repd-cockpit-skin.v1.mjs](../CONTRACTS/repd-cockpit-skin.v1.mjs) to derive/compare role tokens from rendered native REPD colours for new panels, without touching native controls. This MJS is presently a **Neural Link reference**, not an app-mounted module.

Secondary brand reference: live GridAtlas SCADA immutable shell `Ventusltd/gridatlas/atlas/releases/202608300453-atlas-v9/ventusv8.css` and `index.html`, composer `atlas/current.json` observed generation `202611222343`. Existing SCADA uses black `#000`, cyan `#00ffff`, muted white/grey, amber `#ffae00`, monospace, restrained thin borders. This **does not authorise recolouring voltage classes, actual status colours or warning signals**.

Visual invariant: dark background, cyan header accents, green REPD capacity figures, original yellow Solar `#ffff00`, amber BESS `#ffae00`, cyan Onshore `#00ffff`, blue Offshore `#0066ff`, red ticker warning `#ff3038`. Engineering-specific GridAtlas grid-voltage colours remain source-defined, with their own legend. High information density and compact controls should retain original normal/expanded mobile and desktop behaviour.

## Actual divergence identified in current styles (source code inspection, not screenshot/browser approval)

| Panel | Source file | Drift | Safe target |
|---|---|---|---|
| Data Centres | `automation/news/datacentre-ui/styles.css` | yellow `#f4df73` table headings, different teal `#62e7ed`, `#142328` header, different button/selection scheme | scoped adapter that inherits native REPD table header/background/cyan, row colours, input/border/button typography |
| Grid & Offtakers | `uk_renewables_pipeline/202611222330/scripts/layers/pipeline-layers.css` | `#ffd24a` selected buttons and source counts rather than REPD selection colour | match REPD control states and headings; **never change engineering voltage/asset encoding** |
| Prices | `automation/price_daily_ui/78d5360239e1a5fcffa83fcb30d5937c5521acb9/styles.css` | 10px rounded cyan-glow cards, red `#ff5555` ordinary stat labels | scoped, restrained table borders/radii, neutral labels, red reserved for actual alarms/ticker |
| Existing REPD | V9.73 table and HUD CSS | accepted native benchmark | **unchanged; no broad CSS overrides** |

Other disciplines use pinned independent sources and identities: Interconnectors have `IC-` namespace (not REPD records); Grid tracks substations/voltage and source IDs (not available connection capacity); Data Centres distinguish IT load from grid-connection MW; Offtakers are source categories (not assumed development MW); Prices are £/MWh observations (not project capacity); News associations are provisional evidence. A harmonised cockpit **shares skin and interaction contracts**, not fabricated source models or sums mixing MW, MWp, MWh and £.

## Three lanes — exclusive ownership

**A / Functional cockpit owner (first/parallel chat):** `Ventusltd/globalgrid2050` isolated branch `agent/repd-cockpit-crossfilter-20261123`, owns `automation/repd_reporting/v2/cockpit-facets.mjs`, functional tests and successor integration. One source of truth across Solar/BESS/Onshore/Offshore, every official status, operator, region, date, typed capacity; preserve 7,775 REPD refs, MAP/A4/PDF/VICINITY, gauges/ticker, no duplicate report launchers. The earlier `v2/cockpit-skin.*` on A branch are **frozen reference-only donor code**, not dual-owned files.

**B / Visual consistency owner (this chat):** owns Neural Link `CONTRACTS/repd-cockpit-skin.v1.mjs` and this `SESSIONS/...` document, then **separate isolated product branch** `agent/repd-visual-consistency-20261123` with only *new* scoped `automation/repd_brand/v1/*` skin adapter, CSS and visual tests. No editing A's `automation/repd_reporting/v2/*`, current immutable V9.73, GridAtlas or hashed source cartridges. Corrections to Grid/DC/Offtakers/Prices are designed as a scoped host adapter; A imports a reviewed donor only after explicit handoff. No live mutation before owner/QA.

**C / Third chat scope controller:** owns only coordination and separate QA acceptance matrix in Neural Link, source/branch/head and test review, conflict detection, dependent task sequencing and publication gates; no modification of A/B source files and no unilateral release.

**Handshake:** each chat posts `ACK` referencing the exact #83 scope split comment. The comments are polled upon invocation, not guaranteed real-time.

## Acceptance rules
1. Pixel/computed-style parity of existing REPD table before/after on Chromium and WebKit at desktop, 393×852 phone portrait and 852×393 landscape; verify normal/expanded and screen clipping. Match cross-domain panel heading/button/row/scroll/focus palette to native REPD.
2. No global CSS selectors/overrides for `body`, `table`, `.btn` or native REPD IDs. No rewriting accepted source CSS. Scoped new child/adapters only.
3. Preserve existing true technology, voltage, status/warning colours and ticker; readable contrast for disabled and focus states; keyboard/touch controls intact.
4. Production parity source IDs, capacity MW vs MWp, all statuses, normal/expanded MAP/A4/PDF, no truncation, no altered data rights or provenance.
5. Exact-head CI, source hashes, independent reviewer, explicit user publication authorisation, separate homepage owner, public served SHA256 and rollback. Draft/fixture PASS is not evidence of deployed success.

The authoritative work exchange is [Neural Link #83](https://github.com/Ventusltd/neural-link-between-agents/issues/83); update it with commit/PR heads and ACKs.
