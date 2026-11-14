# NL-019 NEWS-DASHBOARD: audit trail

Audit trail for the Pipeline News fix of 14 November 2026, kept by Auditor B (Claude Fable) for Agent A (ChatGPT)
and the Claude harness. Issue: [#19](https://github.com/Ventusltd/neural-link-between-agents/issues/19).
Site: globalgrid2050.com, page `uk_renewables_pipeline/<release>/` in `Ventusltd/globalgrid2050`
(operative release V9.20, folder `202611140306`).

## What the owner said (14 November 2026, morning)

> "Improve the news dashboard it's bad. It's stuck on the same news article. Study the relevant news algorithms.
> For example Botley West was refused planning. Use 3 fable agents and 10 opus agents to fix and leave an audit
> trail for ChatGPT via agents repo."

Also: "Keep it as it is" (read as: do not remove or restructure the project table and its columns; fix the news),
"Simple don't over complicate", and "solve problems and publish".

The Botley West statement is treated as the owner's claim, to be checked against sources. The outcome of that check
is recorded in `GROUND-TRUTH.json` and in `AUDIT-LOG.md` when the review is done.

## Diagnosis (from the three studies in `studies/`)

1. The page's main news reads `dist/major_project_news_v9_5_1.json`; its `updated` field is 22 August 2026 and its
   newest article is 21 August 2026 (STUDY U, sources table).
2. Nothing writes that file: commit `3bcb1252` set the V4, V5 and V6 crawler workflows to manual on 23 August; the
   last scheduled V5 and V6 runs (`32621092076`, `32621379438`) failed (STUDY U, root cause 2).
3. Every release pins the file's SHA-256 (`tests/check_v9_20.mjs` line 80, "must not be rebuilt by this release"),
   so a refresh would fail the release checks (STUDY U, root cause 1).
4. The page hides the age: the header count "133 HEADLINES · 45 UK · 19 INTERNATIONAL" is typed into `index.html`
   line 79 and the dated line is replaced by "audited snapshot" (STUDY U, root cause 3; STUDY C, fault 3).
5. The NEWS SIGNAL column is computed from the same August file: 29 of 7,775 rows carry a badge, none carries a
   link (STUDY S, counts table).
6. All 45 bound articles are tied by project name; none by REPD Ref ID or planning reference; 20 of the 29 rows are
   name-only, and several are wrong on their face (STUDY S).
7. The newer feed files from PRs #66 and #67 are on main but no page script reads them, and they hold the same
   August articles (STUDY U, root cause 4; STUDY S, "not wired in" table).
8. Only the data-centre panel is built to refresh (data branch read through raw.githubusercontent.com); its four
   runs were all manual and its first scheduled slot produced no run (STUDY U, root cause 5).
9. Headlines are 24% of the newspaper's text; the same caveat is printed 133 times; 88 "DISCOVERY ONLY" cards
   still print a REPD project name under an unrelated headline (STUDY C, diagnosis).
10. Consequence: a real, recent story about a named REPD project cannot appear, whatever happens in the world.

## Plan

1. A fetcher reads a fixed list of tested public RSS/Atom feeds, filters for UK renewables and grid events
   (planning decisions, consents, refusals, DCO decisions, financial close, construction start, energisation, grid
   connection, plus data-centre capex and politics), and writes one small file of headlines and links.
2. A scheduled workflow runs it several times a day and publishes the file to a data branch; no release folder
   and no pinned file is rewritten.
3. One page release (V9.21) reads that file, falls back to a snapshot if it cannot, and prints an honest
   "updated" label computed from the file's own timestamp. The project table and MAP links stay as they are.
4. Ground-truth events gathered by scouts (1 August 2026 to today) are the test: the algorithm must keep them.
5. Independent review of both pull requests, then publication, then live checks.

## Who does what

| Role | Work | Writes where |
|---|---|---|
| Fable A | fetcher, algorithm, headlines contract, workflow | pull request in `Ventusltd/globalgrid2050` |
| Engineer guardian | the V9.21 page release that reads the contract | pull request in `Ventusltd/globalgrid2050` |
| Ten Opus scouts | feed lanes (find and test feeds) and event lanes (ground-truth events); read-only | scratch files, reviewed by the auditor |
| Auditor B (Fable) | this audit trail; review of scouts' output, of the algorithm and of V9.21 | this folder and issue #19 only |
| Agent A (ChatGPT) | requested: independent review of both pull requests; live checks after publication | issue #19 |

## Rules in force

- REPD Ref ID is the only authoritative project key.
- A headline may be linked to a REPD project only as a labelled "possible match", and only when the project name
  in the headline matches a REPD site name exactly AND something else agrees (developer, local authority or
  technology). Otherwise it is shown as a headline with no project.
- Headlines and links only: no article text stored or shown beyond the title, source and date.
- Sponsored items are dropped.
- No data-centre register content (licence hold).
- MAP links, the Offtakers layer and existing release folders are not touched.
- Neutral, professional public wording. Nothing private in any output.
- The auditor changes nothing outside this folder; the auditor's reviews are findings, not edits.

## Files

| File | What |
|---|---|
| `README.md` | this page |
| `AUDIT-LOG.md` | UTC-timestamped entries, newest last |
| `studies/STUDY-U-updates.md` | why the news does not update, and the smallest fix |
| `studies/STUDY-S-signal.md` | the NEWS SIGNAL column |
| `studies/STUDY-C-clutter.md` | clutter on the page |
| `FEEDS.json` | reviewed feed list (added when the scouts finish) |
| `GROUND-TRUTH.json` | reviewed ground-truth events (added when the scouts finish) |

The studies are copies with local references removed; screenshots are not published.
