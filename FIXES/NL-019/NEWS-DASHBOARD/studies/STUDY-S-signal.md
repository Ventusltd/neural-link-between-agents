# STUDY S: the NEWS SIGNAL column (14 November 2026)

Agent S. Read-only study of `uk_renewables_pipeline/202611140306` (V9.20) on main, with the two earlier versions `202611132345` and `202609082224` for comparison. Paths are relative to the globalgrid2050 repository unless stated.

## Is it too complicated?

Yes. The column tries to tie news articles to individual REPD projects by matching names, which is the hard part of the whole product, and it does so from a single news file that has not changed since 22 August 2026.
The result is a badge on 29 of 7,775 rows (0.4%), no link in any cell, and a dash with the words "no exact canonical PRIMARY_MATCH" on the other 7,746.
Remove the column: every row already has a working `NEWS ↗` search link beside the MAP link, and that is the simple version that works.

## What the column is and why it is dead

**What it is.**

- Header: `<th>NEWS SIGNAL</th>` at `uk_renewables_pipeline/202611140306/index.html:186`.
- Cell: a plain `<span class="signal">` plus a small note, drawn at `scripts/plugins/projects-v9-8.js:239` from `signalForProjectV9_5_1(project)` (line 230, imported at line 23). Interconnector rows hard-code `NO SIGNAL` (line 222).
- Logic: `scripts/plugins/newspaper-v9-5-1.js:45-52` looks the row's REPD Ref up in an index of news items. Lines 34-43 turn the item's event into a label.
- Data: one file, `dist/major_project_news_v9_5_1.json`, fetched from the site and from raw GitHub (`newspaper-v9-5-1.js:4-7`). Only items with `role === "PRIMARY_MATCH"` and `eligible_for_news_signal === true` count (lines 12-18).

**Values it can take.**

| Cell | Meaning intended | Rows today |
|---|---|---|
| `—` + "no exact canonical PRIMARY_MATCH" | no article bound to this REPD Ref | 7,746 |
| `PROJECT UPDATE*` | a bound article with no specific event | 12 |
| `APPROVED*` | bound article reads as a consent | 8 |
| `M&A*` | acquisition | 5 |
| `FINANCED*` | financial close | 2 |
| `CONTRACT*` | contract award | 1 |
| `REFUSAL*` | refusal | 1 |
| `OPERATIONAL*`, `CONSTRUCTION*` | coded, never occur in the data | 0 |

The asterisk means "unverified". The note under a badge reads, for example, "canonical PRIMARY_MATCH 91% · unverified event · 2026-08-21".

**What a click does.** Nothing. The cell contains no `<a>` and no click handler. The article URL is in the data (`url` on every item) but the cell never uses it. In headless Chrome, clicking the badge changed no URL, opened no tab and expanded nothing, in all three versions at 1440 px and 390 px.

**Where the data comes from and when it was last built.**

- Built by hand with `scripts/build_news_feed_v9_5_1.py` from `dist/major_project_news_v5.json` (125 items) and `dist/major_project_news_v6.json` (8 items). No workflow commits it (crawl note 13, lines 106-108).
- Source feeds: Google News RSS searches (all 45 bound article URLs are `news.google.com/rss/articles/...` redirects), run by `.github/workflows/major_project_news_v5.yml` and `major_project_news_v6.yml`.
- File's own `updated` field: 2026-08-22T20:45:25Z. Newest article: 21 August 2026.
- Last crawl runs: v6 run 32621379438 on 23 August 2026 (schedule, failed); v5 run 32621092076 on 23 August 2026 (schedule, failed). Both workflows are now manual-only (`workflow_dispatch`).
- The release's own test forbids an update: `tests/check_v9_20.mjs:33` pins the file's sha256 (`cea104c3...`) and line 80 fails with "must not be rebuilt by this release".

**Counts from the data (V9.20, 7,775 projects).**

| Measure | Count |
|---|---|
| Projects with any signal | 29 (25 solar, 4 battery) |
| Projects with an article link in the cell | 0 |
| Bound articles behind those 29 | 45 |
| Article dates | 26 September 2025 to 21 August 2026 |
| Tied by a REPD Ref ID in the article | 0 |
| Tied by a planning reference in the article | 0 (`planning_reference_hit` is false on all 45) |
| Tied by project name | 45 (22 exact name in headline, 23 a name variant) |
| Of the 29 shown, name plus operator, county or authority | 9 |
| Of the 29 shown, name only | 20 |

So every signal is a name match presented under the word "canonical". That is what the decision on neural-link issue 19 (Agent A, 14 November 01:05 UTC) rules out: "no public STRONG name-only article binding", and name or operator matches go to a review queue.

Some of the 29 look wrong on their face:

- Kells Solar Farm (REPD 5967) carries `REFUSAL*` from a Meath Chronicle story, a local paper in the Republic of Ireland.
- Gedling Solar Farm (REPD 2377, Operational) carries a story about "plans revealed for major new solar farm".
- Highnam Solar Farm (REPD 5452, Abandoned) carries "New solar farm heading for Gloucestershire".
- Williamthorpe Colliery (REPD 5533, Planning Permission Expired) carries "Work on solar farm ... starts".

The repository's own evaluation scores this binder at 4 false positives against 38 correct (`dist/news/binder_evaluation_v9_5_1.json`, `baseline_v9_5_1_primary_match_metrics`).

**Did it ever work?** It has been the same in all three versions.

| Version | Projects | With signal | Links in cell | News file |
|---|---|---|---|---|
| 202609082224 (September) | 7,680 | 29 | 0 | same file, 22 August |
| 202611132345 | 7,775 | 29 | 0 | same file |
| 202611140306 (V9.20) | 7,775 | 29 | 0 | same file |

`newspaper-v9-5-1.js` is byte-identical across the three. The column never linked to anything, and it stopped changing on 22 August 2026.

**What a user sees.**

- First page of the table (20 largest projects): 20 dashes. The first badge is at rank 40 by capacity (page 2), the next at ranks 71 and 76 (page 4); 15 of the 29 sit beyond row 600.
- Searching "Beacon Fen" gives two rows. The battery row (REPD 13600) shows the dash; the solar row (REPD 13599) shows a yellow `APPROVED*` with the note above. Neither is clickable.
- At 390 px the column is still shown (about 85 px wide), wrapping the note over five lines.
- The header strip reads "45 UK · 19 INTERNATIONAL ... · 133 HEADLINES · AUDITED SNAPSHOT", which is the August file.

**What already works.** The ACTIONS cell of every row has `NEWS ↗` (`projects-v9-8.js:231-233`, drawn at line 239). It opens a Google News search in a new tab, for example `https://www.google.com/search?q=Beacon+Fen+Energy+Park+Solar+UK&tbm=nws`. The sandbox blocks google.com, so I confirmed the link and the new tab, not the results page.

## What exists but is not wired in

| Item | What it holds | Fresh articles? |
|---|---|---|
| `dist/major_project_news_2026q3.json` (PR #66) | the same 133 August headlines re-bound to October Ref IDs; 45 bound | no: `network.articles_fetched` is 0 |
| `dist/major_project_news_2026q3_refaware.json`, `scripts/news_binder_refaware.py` (PR #66) | 137 headlines, 65 bound, by name | no |
| `automation/news/binder.py`, `dist/news/article_relevance_v9_5_1_2026q3.json` (PR #67) | the 133 headlines classed EXACT 5, STRONG 44, CANDIDATE 9, UNBOUND 75 | no |
| `dist/news/repd_events_2026q3.json` (PR #67) | 769 register changes between the July and October REPD releases, keyed by exact Ref ID | not articles; official register facts |
| pipelinenews repository (crawl notes 26, 33, 34) | 133 to 136 headlines, the same August file; its BBC RSS discovery sets `repd_ref: None`, `UNMATCHED_REQUIRES_REVIEW` | no |

Every binder in both repositories works on the same August headlines. None has an article newer than 21 August 2026, and "EXACT" in `binder.py` means a planning reference or name plus corroboration, not a REPD Ref ID.

**Honest measurement.** I pooled every cached headline (v4, v5, v6, v9.5.1 and both 2026q3 files: 137 unique, 24 August 2025 to 21 August 2026) and tested them against the 7,775 projects. Only headlines are held, not article text.

| Rule | Articles | Projects |
|---|---|---|
| Exact reference: a REPD Ref ID or a REPD planning reference in the headline | 0 | 0 |
| Strict rule: full REPD site name in the headline, name belongs to one development, and the operator, county or planning authority is also in the headline | 2 | 2 |
| Full REPD site name in the headline, nothing else | 30 | about 17 |

The two that pass the strict rule are Carlton Solar Farm (REPD 12017, "... 71-MW Carlton Solar Farm in North Yorkshire") and Longhedge Solar Farm (REPD 11063, "Innagreen acquires Longhedge solar farm from RES").

The name-only row shows why it cannot be shown as fact: it binds "The Grange" (two REPD records) to two care-home stories, and "Hill Solar Farm" to a story about Green Hill Solar Farm.

## Three options, simplest first

### Option 1: remove the column

- **User sees:** ten columns instead of eleven. ACTIONS is unchanged: `MAP ↗`, `NEWS ↗`, `COPY ID`.
- **Projects that show something:** 7,775 keep the working `NEWS ↗` search link. Signals shown: 0.
- **Files to change** (in a new version folder cut by `automation/pipeline_release/new_version.py`):
  - `index.html:186`: delete the `<th>`. Line 92 (strap) and line 164 (the NEWS line under STATUS DISCIPLINE): delete the words about signals.
  - `scripts/plugins/projects-v9-8.js`: delete the signal `<td>` in both row templates (lines 222 and 239), line 230 and the import at line 23.
  - Same file, lines 410-413 (CSV): keep the two header names "Canonical News Signal — Event Unverified" and "Canonical News Match Note", write empty values.
  - `styles/v9-6-1.css:139`: reduce the 1180 px table minimum by about 100 px.
  - Tests: a new check (below).
- **Risk:** low.
  - The release train passes the CSV only if its header hash equals the parent's (`automation/pipeline_release/verify.py:145`), which is why the header names stay.
  - Older tests in the folder assert eleven columns (`tests/check_v9_7.mjs:91`, `tests/browser_smoke_v9_8.mjs:241,276`, `tests/browser_map_reachability_v9_7.mjs:186,252`). `tests/run_v9_20.sh` does not run them (lines 81-82 run only `check_v9_20.mjs` and `check_map_contract_all_rows.mjs`), so they need a withdrawal line in `CHANGES.md`, as V9.20 did for the data-centre probes.
  - The MAP anchor and `mapActionHtmlV9_5_1` are not touched; ACTIONS stays the last cell, so the sticky rule at `styles/v9-6-1.css:52-60` still applies.

### Option 2: turn the column into the search link

- **User sees:** the column renamed `NEWS`, each cell a link "SEARCH NEWS ↗" that opens a news search for the project. `NEWS ↗` leaves ACTIONS, which becomes `MAP ↗` and `COPY ID`.
- **Projects that show something:** 7,775, plus the 16 interconnectors.
- **Files to change:** `index.html:186` (header text); `projects-v9-8.js:222,239` (move the existing `newslink` anchor into the ninth cell, drop the signal span); lines 230 and 23 as in Option 1; CSV as in Option 1.
- **Risk:** low to medium. Eleven columns stay, so no layout or column-count test moves. But it edits the ACTIONS cell that holds MAP, and it keeps a column whose only content is the same link on every row. The search is Google's: results are not ours and can be empty for small sites.

### Option 3: headlines only where a binder has a defensible match

- **User sees:** on a few rows, "POSSIBLE MATCH" in grey, then the headline as a link to the article, source and date. Everything else blank.
- **Projects that show something:** 2 today under the strict rule; 0 under the exact-reference rule. 29 if the existing name matches are relabelled, which the issue 19 decision does not allow.
- **Files to change:** a new build script and data file per release, the cell renderer, the pinned-hash test at `tests/check_v9_20.mjs:33,80`, and a live crawl, which has not run successfully since 22 August 2026.
- **Risk:** high. Most work, a wrong article beside a named project is a public error, it goes against the review-queue decision, and it would fill 0.03% of rows.

## Recommendation

Option 1. Remove NEWS SIGNAL from the table and leave ACTIONS exactly as it is.

- It is the smallest change, it removes a column from a table the owner calls cluttered, and nothing is lost: the working news link is already on every row.
- It brings the page in line with the owner's rule (no name-only match shown as fact) and the issue 19 decision.
- Option 3 is not worth building until there is a fresh daily feed, and even then exact REPD references in news are close to zero.

Two things I did not do. I did not check the search results page itself (google.com is blocked here). I did not test the removal in a browser; the file list above is from reading the code.

One related fact for the other studies: the newspaper cards also print "PRIMARY_MATCH · REPD nnnnn" from the same name matching (`newspaper-v9-5-1.js:92`). Removing the column does not change those.

If the owner later wants a per-project signal that is true by construction, the material is already in the release: `events/register_changes.json` holds 308 official register changes on 274 projects, keyed by exact REPD Ref ID, and is already shown inside each PROJECT RECORD.

## Test for the recommendation

Add to the new version's check (static) and to the release-train browser probe (1440 px and 390 px):

1. `index.html` has exactly 10 `<th>`, none with the text `NEWS SIGNAL`; the last is `ACTIONS`.
2. After the table reports "7,775 of 7,775 records", `document.querySelectorAll('#tbody .signal, #tbody .signal-note').length === 0`, and every row has 10 cells.
3. Search `13599`: one row, its `a.atlaslink` href equals the parent version's href for that Ref, and its `a.newslink` href starts with `https://www.google.com/search?q=Beacon+Fen+Energy+Park`.
4. `tests/check_map_contract_all_rows.mjs` passes unchanged: all 7,775 MAP hrefs identical to the parent's.
5. Exported CSV: 7,775 rows, header sha256 equal to the parent's, and the last two columns empty on every row.
6. `scripts/plugins/projects-v9-8.js` no longer contains `signalForProjectV9_5_1`.
7. At 390 px the page still shows `MAP ↗` in the first row without horizontal page overflow.
