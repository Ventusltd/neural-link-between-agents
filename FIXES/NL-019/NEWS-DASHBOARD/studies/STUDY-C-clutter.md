# STUDY C: clutter on the Pipeline News page

Agent C, 14 November 2026. Page studied: `uk_renewables_pipeline/202611140306/` (V9.20), served locally from a scratch copy and viewed in headless Chrome at 1440x900 and 390x844. Compared with `202611132345` (V9.12) and `202609082224` (V9.10) by the same method. Screenshots and the layout sketch were made locally and are not published here.

Two limits of the local run: the Chart.js CDN and the two `ventusltd.github.io` contract files were unreachable from the sandbox, so the gauge arcs did not draw and I cannot say how they look live. Everything else loaded (7,775 records, 133 stories, 4 data-centre headlines, 12 register changes).

## 1. Diagnosis

The page is cluttered because it explains itself more than it shows news. Measured:

- **Words above the fold, desktop: 531.** Of these 77 are headline words (7 headlines fully visible), 80 are version links in the sidebar, and the rest is labels, release ids, counts and caveats. **Phone: 189 words, 7 of them headline** (one headline visible, starting at y=738 of 844).
- **Headlines are 24% of the newspaper's text** (1,444 of 6,025 words). Each story card is 245 px tall and has five layers: kicker, headline, green project line, source, badge plus caveat.
- **The same caveat is printed 133 times** ("algorithmic and unverified", once per card). "DISCOVERY ONLY · no project signal" appears 88 times, "PRIMARY_MATCH" 65 times, "canonical" 23 times. 22 version labels and 8 release ids are visible on the page.
- **The project table starts 2,735 px down on desktop and 4,821 px down on a phone.** Yesterday it started at 1,521 and 2,528.
- **22 text colours, 11 font sizes (7 px to 24 px), 59 buttons, 30 sidebar links**, 36% of letters upper case, and four different bordered "note" boxes.

Four things look wrong rather than merely busy:

1. **The MAP button is cut off at 1440 px.** The table has a 1,280 px minimum inside a 1,128 px box, so the ACTIONS column sits 152 px past the right edge. It fits only from about 1,592 px wide. This is the same in all three versions, including V9.10, whose title was "the ACTIONS column fits its buttons".
2. **The NEWS SIGNAL column is almost empty and never a link.** 29 of 7,775 rows have a signal (45 matched items in `dist/major_project_news_v9_5_1.json`). Every other row prints "— no exact canonical PRIMARY_MATCH". The cell is a plain `<span>` (`scripts/plugins/projects-v9-8.js:239`); the adjacent NEWS ↗ button is a Google News search, not an article. All 20 rows on the first page are empty.
3. **"ENERGY DAILY" shows nothing newer than 21 August 2026** (file `updated` 2026-08-22), labelled "AUDITED SNAPSHOT". The only dated-this-week items are the four data-centre headlines.
4. **88 "DISCOVERY ONLY" cards still print a green REPD project name, MW and county under the headline**, for example a New Jersey headline labelled with a Cleveland project and an Australian market headline labelled with a Nottinghamshire solar farm. That is name-level matching shown beside the headline, which the owner ruled out.

Smaller faults: the register-changes strap says "308 changes on 274 projects in this list" above a list of 12; the three gauge cards repeat the three numbers already in the results line directly below them; on a phone the five columns restored in September (`styles/v9-6-1.css:126-139`) repeat what is already printed under each site name, and Technology, Status and Capacity are off-screen behind a sideways scroll.

## 2. Inventory, top to bottom

Heights in px. "D" desktop 1440x900, "P" phone 390x844.

| # | Block | What it says | D height | P height | Kind | Verdict |
|---|---|---|---|---|---|---|
| 1 | Sidebar | Brand, "UK RENEWABLES PIPELINE · V9.20", 30 links: 27 old versions back to V1, DIRECTORY, MAP ATLAS, EXPORT CSV | 250 wide, full height, 98 words | 62 (links hidden, so no MAP ATLAS or versions link on a phone) | Navigation, mostly for engineers | **Remove as a sidebar.** Keep three links in the title bar: Map atlas, Export CSV, Versions. The 27 version links already exist on `versions.html`. |
| 2 | Header | "UK RENEWABLES PIPELINE 202611140306" and a pill "● 133 HEADLINES · 45 UK · 19 INTERNATIONAL · FULL ≥1 MW" | 47 | 110 | Title plus status | **Shrink.** Drop the pill (the counts are repeated twice below). |
| 3 | Release strap | "V9.20 · REPD OCTOBER 2026 (Q3) · NO DATA-CENTRE REGISTER CONTENT · RELEASE CANDIDATE · 14 November 2026"; "Canonical DESNZ REPD…7,775…"; "V9.8 interface · V9.1 canonical data spine…"; REPD source link | 80 | 188 | Status text for engineers | **Move to the footer**, behind "Version". One grey line under the title is enough: register date and project count. |
| 4 | Newspaper masthead | "GLOBALGRID2050 ENERGY DAILY"; strap "UK requires canonical REPD binding · International is read from a committed build-time decision ledger…"; counts line | 95 | 145 | Method note | **Shrink to a heading** "Headlines · n · newest date". Method sentence to footer notes. |
| 5 | News filter bar | 11 buttons (ALL, UK, INTERNATIONAL, US, EUROPE, SOLAR, BESS, CONSENT, CONSTRUCTION, OPERATIONAL, FINANCE / M&A) and a search box | 49 | 153 | Controls | **Shrink** to All, UK, International. |
| 6 | Story grid | 133 cards in a 612 px inner scroll box (10,063 px of content; 27,530 on a phone) | 612 | 549 | News | **Keep, restyle** as one line per item: date, headline link, source. Remove the green project line, the percentage badge and the per-card caveat. Show a short list, the rest behind "All headlines". No box that scrolls inside the page. |
| 7 | Data centres: capex and politics | Second masthead, strap, "UPDATED 14 NOV 2026 · 4 HEADLINES · 9 FEEDS OK", two lanes; politics lane holds one pinned opinion item | 330 | 438 | News (the only fresh items) plus feed status | **Keep, shrink** to a plain short list beside the headlines. Drop "9 FEEDS OK". |
| 8 | Register changes | Third masthead, two-line strap, 12 changes each with a SHOW IN TABLE button, footer sentence | 828 | 1,787 | REPD facts, dated Aug to Oct 2026 | **Keep, shrink** to one line each in two columns (about 250 px). Fix the "308 … in this list" wording. |
| 9 | "REPD PIPELINE ANALYTICS" and three gauge cards | Capacity 365,474; projects 7,775; largest 4,100 | 185 | 563 | Decoration; duplicates the results line | **Remove from view.** |
| 10 | Technology, status filters | 6 + 5 buttons | 75 | 155 | Controls | **Shrink** into the control row. |
| 11 | County, sort, search, CLEAR, EXPORT, results line, "CSV contains the current filtered rows only" | Results line: "7,775 of 7,775 records · 365,474 MW · largest 4,100 MW" | 53 | 196 | Controls plus counter | **Keep.** Search first. The results line must stay (the checks read it). |
| 12 | STATUS DISCIPLINE | Four notes: DEFAULT, NEWS, ATLAS, INTERCONNECTORS | 104 | 224 | Method note | **Move behind a link** in the footer ("Notes on the data"). |
| 13 | Project table | 11 columns, 20 rows per page, rows 83 to 153 px (161 to 252 on a phone) | 585 | 4,125 | The product | **Keep, cut columns** (below). |
| 14 | Pager | "1–20 of 7,775 · page 1 of 389" | in 13 | in 13 | Navigation | Keep. |
| 15 | DATA SOURCES AND LICENCES | REPD and OGL v3.0 line; headlines note; "no content from the UK data-centre register" | 104 | 152 | Legal | **Keep at the bottom**, small, as it is. |

Table columns:

| Column | Verdict |
|---|---|
| SITE NAME (with PROJECT RECORD expander) | Keep. Put REPD ref and updated date under the name on desktop as the phone already does. |
| COUNTY, OPERATOR | Merge into one column on desktop; on a phone they are already under the name. |
| TECHNOLOGY, OFFICIAL REPD STATUS, OFFICIAL CAPACITY | Keep. These must be visible on a phone without sideways scrolling. |
| REPD REF | Keep on desktop. It is the key. |
| GLOBALGRID REF | Remove from the table. It is "GG2050-REPD-" plus the REPD ref. Stays in the CSV. |
| REPD UPDATED | Move under the name; the sort stays in the sort menu. |
| NEWS SIGNAL | **Remove from the table.** 29 of 7,775 rows, no link. Stays in the CSV, so the CSV header does not change. |
| ACTIONS | MAP ↗ only, always in view. NEWS ↗ (a web search) and COPY ID move into PROJECT RECORD. The two-sentence coordinate note under MAP moves into PROJECT RECORD. |

## 3. What last night's version train added

| | V9.10 Sept | V9.12 13 Nov | V9.20 14 Nov |
|---|---|---|---|
| Sidebar links | 23 | 24 | 30 |
| Words above fold, desktop / phone | 493 / 183 | 502 / 185 | 531 / 189 |
| First project row, desktop | 1,521 px | 1,521 px | 2,735 px |
| First project row, phone | 2,516 px | 2,528 px | 4,821 px |
| Phone page length | 6,611 px | 6,623 px | 9,086 px |
| Visible buttons, desktop | 47 | 47 | 59 |

September to 13 November changed the register and nothing visible. The eight versions of 14 November added three stacked blocks between the headlines and the table (data-centre panel 330 px, register changes 828 px, data sources 104 px), six sidebar links, and a longer release strap. Each was reasonable alone; together they pushed the table 1,214 px further down on desktop and 2,293 px on a phone, and added a second and third "newspaper" masthead in the same yellow and white. The headlines, the stale August snapshot, the empty signal column and the clipped MAP column were all inherited unchanged.

## 4. Proposed simple layout (six blocks)

1. **Title bar.** One line: page name, and under it "REPD October 2026 · 7,775 projects". Three links on the right: Map atlas, Export CSV, Versions. Phone: same, links wrap under the title.
2. **Headlines.** First thing the user reads, starting about 150 px down on desktop and 200 px on a phone. One line per item: date, headline (the link), source. Renewables on the left, data-centre headlines in a narrow column on the right; on a phone data centres stack under renewables. Short list, then "All headlines".
3. **Register changes.** One line each with "show", two columns on desktop, one on a phone.
4. **Project controls.** Search box first, then technology, status, county, sort; one results line with the CSV link.
5. **Project table.** Desktop: project, technology, status, capacity, county and operator, REPD ref, MAP. Phone: project, technology, status, capacity, MAP, with no sideways scroll. In the sketch the first row is at about 840 px on desktop (now 2,735) and about 1,720 px on a phone (now 4,821).
6. **Footer.** Sources and licences in plain small text (REPD, OGL v3.0, headlines note, the data-centre register sentence). "Notes on the data" and "Version and all versions" each behind one click.

Sketch measurements (placeholder content): desktop 230 words above the fold, phone 120; whole page 1,324 px on desktop and 2,612 px on a phone, no sideways overflow.

## 5. Change list for a new release folder

Cut with `python3 automation/pipeline_release/new_version.py create <stamp> V9.21 "simple layout"`, then `finalize`, then `verify.py --browser --write`. Files to change:

| File | Change |
|---|---|
| `styles/v9-21.css` (new) | All layout: sidebar becomes a title bar showing only `#mapAtlasNav`, `#export` and the versions link; `.gauges` and its heading hidden; release strap and STATUS DISCIPLINE ordered to the bottom; one accent colour; story cards as single lines; table without the 1,280 px minimum; hide GLOBALGRID REF, REPD UPDATED and NEWS SIGNAL cells; phone rule that drops the `v9-6-1.css:135-139` override. |
| `index.html` | Link the new stylesheet. Remove the eight extra news buttons. Shorten the masthead strap. Wrap STATUS DISCIPLINE in `<details>`. No id removed. |
| `scripts/plugins/newspaper-v9-5-1.js` line 94, `newspaper-v9-7.js` line 37 | Story template: date, headline, source only. Do not touch `signalForProjectV9_5_1` (the CSV uses it). |
| `scripts/plugins/datacentre-news.js` | Plain list, no second masthead, no feed count. |
| `scripts/plugins/register-changes.js` | One line per change; correct the "in this list" sentence. |
| `scripts/plugins/projects-v9-8.js` line 239 | Move NEWS ↗, COPY ID and the map note into the PROJECT RECORD block. The MAP anchor and its href are not edited. |
| `CHANGES.md`, `README.md`, `tests/run_v9_21.sh`, `tests/check_v9_21.mjs` | Written by the tool. |

What the checks require to stay the same (read from `verify.py`, `browser_check.mjs`, `check_template.mjs`, `registry.json`):

- **7,775 rows.** `#resultsMeta` must contain "of 7,775 records" at both widths; `data/` byte-identical to the parent.
- **MAP hrefs.** All 7,775 identical to the parent, character for character; drawn rows keep `a.atlaslink` with the contract href. Do not edit `scripts/core/atlas-receiver-v9-7.js` or the href builder.
- **CSV control.** `#exportInline` must exist and export 7,775 rows with the same header hash, so both news-signal columns stay in the CSV.
- **Feature markers in `index.html`:** `<section class="newspaper">`, `id="exportInline"`, `data-technology="interconnector"`, the three plugin script tags, `href="../versions.html"`, the pinned Chart.js tag, `id="dataSources"`. Hiding the gauges by CSS keeps the Chart.js probe passing; removing them would need a declared withdrawal.
- **Probes:** `#dataSources` contains "Open Government Licence v3.0" and "no content from the UK data-centre register"; `#search` works; `details.project-record` contains "PLANNING AUTHORITY"; no `dcuk-` text.
- **Label strings** (`check_template.mjs:97-108`, `new_version.py:49-55`): the `<title>`, `<h1>UK RENEWABLES PIPELINE <id></h1>`, the brand `<small>`, the active nav link, the link to the parent, and "Canonical DESNZ REPD Q3 2026 … 7,775 solar, BESS and wind records" must all remain in the markup. So in this release they are restyled or reordered by CSS, not deleted. Taking the release id out of the visible h1 needs a four-line change to those two tools; do that separately.
- **Ids the scripts bind to** (a missing one throws): `export`, `exportInline`, `mapAtlasNav`, `newsTools`, `newsSearch`, `newsMeta`, `stories`, `releaseMeta`, `v1`–`v3`, `tech`, `status`, `county`, `sortProjects`, `search`, `clearFilters`, `resultsMeta`, `exportMeta`, `sortUpdated`, `repdUpdatedHeader`, `updatedSortIndicator`, `tbody`, `gaStateSummary`.
- **Phone:** no document-level sideways overflow; no uncaught errors; no failed same-origin requests; folder under 17 MB.

One decision for the owner: on 5 September he asked for the five hidden columns back on a phone. This proposal hides them again there because the same values are already printed under each site name. If he still wants the sideways table on a phone, keep that rule and apply everything else.
