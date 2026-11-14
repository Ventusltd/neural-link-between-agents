# Acid scorecard: top-200 solar project signals

Test lead: Claude Fable. 14 November 2026. Repository Ventusltd/globalgrid2050.

The acid suite is `automation/news/tests/test_signals_acid.py` (pull request 101: tests and CI only). It is written against contract version 2 (`project-signals.v2`). It runs the combiner as a program on fixtures, the collectors' own matchers and date readers on the reported cases, and a checker on the real published file. "Passes" means every test of the rule passes. A test that fails on main is recorded in the suite as a strict known failure naming the review finding it covers; on code that declares version 2 the marker is not applied, so the test must pass there.

Summary

| | tests | pass | fail | known failing | open recommendations |
|---|---|---|---|---|---|
| main, 91727c22 (six suites together) | 259 | 169 | 0 | 78 | 12 |
| fixer's branch, ab6fe337, pull request 100 (seven suites: its new gate suite is discovered and run) | 281 | 264 | 13 | 0 | 4 |
| earlier head of the same branch, 481388b6, for the record | 270 | 236 | 23 | 0 | 11 |

On main all thirteen product rules (R01 to R13) fail; R14 and R15 are the integrated run and the live checker themselves, added by pull request 101. On the fixer's branch eleven of the thirteen pass in full; two still have failing tests: false matches (R01, 12 tests) and one multi-project case (R07, 1 test).

## 1. Main (commit 91727c22, schema project-signals.v1)

### Offline acid suite on main at 91727c22

186 tests: 96 pass, 78 known failing (strict xfail, each naming the finding it covers), 12 open recommendations, 0 failed.

| rule | what it checks | passes | evidence |
|---|---|---|---|
| R01 | False matches: REPD 9050 and bypass diodes; the testers' 239 wrong headlines; confidence earned, not inherited | no | 49 tests: 17 pass, 31 known failing, 1 open recommendation. REPD 9050 shows ['Hot spots: why bypass diodes fail in solar modules', 'New bypass diode design cuts shading losses in PV modules', 'Solar panel bypass diodes explained', 'Heart bypass patient backs hospital solar panels', 'Town b // the bypass-diode headline came back from the previous file // trade.py ties 'Town bypass to get solar-powered road signs' to REPD 9050 as a confident match: ("alias phrase 'Bypass' in title with solar or energy word directly after it", 'confirmed') |
| R02 | Calendar and dates: day-month swap, two-digit year, no time zone, impossible and future dates, 90-day boundary | no | 79 tests: 57 pass, 11 known failing, 11 open recommendation. '2026-02-30' became '2026-02-30' (30 February does not exist) // official.parse_day('1/2/0026') gave '0026-02-01' (acid tester 2: an implausible year must not become a date) // first shown: 'Alderwick Solar Farm to open' dated '2027-06-01' |
| R03 | Stale feed: same items, old dates, new run | no | 3 tests: 0 pass, 3 known failing. version 1 output: one mixed 'signals' list per project, no recent_news / official / archive // generated_at moved from 2026-11-14T12:00:00Z to 2026-11-15T12:00:00Z with nothing collected // version 1 output: one mixed 'signals' list per project, no recent_news / official / archive |
| R04 | Source failure: a part missing, unreadable, raising, of the wrong schema, or with every source failed | no | 8 tests: 1 pass, 7 known failing. parts.trade.status is 'absent' after a failed collection (missing) // the withdrawn reviewed entry is still published |
| R05 | An undated item never outranks a dated one; newest first; a fresh possible item is not hidden | no | 3 tests: 0 pass, 3 known failing. shown in the order ['old', 'undated', 'fresh'] // version 1 output: one mixed 'signals' list per project, no recent_news / official / archive // the newest item is missing or not first |
| R06 | A reviewed item duplicated by a fetched one is shown once; reviewed items follow their dates | no | 6 tests: 5 pass, 1 known failing. version 1 output: one mixed 'signals' list per project, no recent_news / official / archive |
| R07 | Multi-project articles handled deliberately | no | 4 tests: 0 pass, 4 known failing. the article is shown as fact on a project its title does not name // 4 link(s) on more than one project without also_projects: ['https://morpethherald.co.uk/business/new-solar-farms-on-150-hectares-of-northumberland-farmland-is-given-the-go-ahead-3905725', 'https://www.inkl.com/news/welsh-governmen |
| R08 | A sharp drop in the counts is not published | no | 2 tests: 1 pass, 1 known failing. published with 1 of 6 projects and 2 of 8 items left |
| R09 | generated_at does not advance when collection fails | no | 4 tests: 0 pass, 4 known failing. generated_at is '2026-11-14T12:00:00Z' though nothing was ever collected // generated_at went from 2026-11-14T12:00:00Z to 2026-11-15T12:00:00Z although every collection failed (missing) |
| R10 | Counts by tier, never mixing recent news with archive | no | 3 tests: 0 pass, 3 known failing. {'schema': ["schema is 'project-signals.v1', not 'project-signals.v2'"], 'tier-counts': ['version 1 counts one mixed f...earch are not separated'], 'tier-purity': ['version 1 has one list per project; items carry no tier and no fr // 'headline' // {'schema': ["schema is 'project-signals.v1', not 'project-signals.v2'"], 'tier-counts': ['version 1 counts one mixed f...earch are not separated'], 'tier-purity': ['version 1 has one list per project; items carry no tier and no fr |
| R11 | A register search is not labelled as a planning file | no | 1 tests: 0 pass, 1 known failing. REPD 90001: label 'planning file' |
| R12 | Event type recorded; one event shown once with its sources | no | 8 tests: 0 pass, 8 known failing. version 1 output: one mixed 'signals' list per project, no recent_news / official / archive // event None for 'Alderwick Solar Farm granted development consent' |
| R13 | Provenance on every item (source, how obtained, when) | no | 1 tests: 0 pass, 1 known failing. ["schema is 'project-signals.v1', not 'project-signals.v2'"] |
| R14 | One integrated CI run of all signals suites with one table | no on main today; yes with pull request 101 | 2 tests: 2 pass with the new workflow |
| R15 | Live checker of the published file names the rule that fails | yes (new in pull request 101) | 13 tests: 13 pass |

### Live check of the published file

dist/project_signals.json on project-signals-data: schema `project-signals.v1`, generated_at `2026-11-14T12:46:07Z`.

| rule | passes | evidence |
|---|---|---|
| live: schema | no | schema is 'project-signals.v1', not 'project-signals.v2' |
| live: nothing | yes |  |
| live: repd-9050 | yes |  |
| live: undated-order | no | project 10914 signals: 2024-09-06 at place 5 is below the older 2024-09-04 (and 10 more) |
| live: tier-counts | no | version 1 counts one mixed figure (with_signal 162, with_confirmed_signal 158): recent news, old articles, official notices and reviewed research are not separated |
| live: tier-purity | no | version 1 has one list per project; items carry no tier and no freshness |
| live: dates | yes |  |
| live: generated-at | yes |  |

Notes on reading this honestly:

- R14 and R15 pass with pull request 101 applied. On main as it stands there is no integrated run: `project-signals.yml` runs two of the five existing suites (NL-019 finding 4).
- The live file passes "repd-9050" today only because no collector happened to fetch a bypass-diode headline in the single run so far; rule R01 shows the code would publish one.
- The live file passes "generated-at" because its only run succeeded on 14 November; rule R09 shows the stamp would advance on a failed run too.
- "live: undated-order" fails on the real file: in 11 places version 1 puts an older or undated item above a newer one (confirmed first, then date).
- Open recommendations are tester proposals outside contract version 2: one test for the eight aliases acid tester 3 would downgrade, and eleven date-reader cases from acid tester 2 where a date is lost rather than wrong. They are reported, never failures.

## 2. The fixer's branch (acid/team1 at ab6fe337, pull request 100, schema project-signals.v2)

The same suite, with the known-failing markers switched off by the code's own version. The branch moved during the cycle (481388b6, then ab6fe337: a shared title gate and date reader in the collectors, standings, more exclusions); the contract was amended at 13:20 UTC and the suite follows the amendments (an undated item may carry a year alone; a fetched headline must name the project in its title).

### Offline acid suite on the fixer's branch at ab6fe337 (pull request 100)

186 tests: 169 pass, 0 known failing (strict xfail, each naming the finding it covers), 4 open recommendations, 13 failed.

| rule | what it checks | passes | evidence |
|---|---|---|---|
| R01 | False matches: REPD 9050 and bypass diodes; the testers' 239 wrong headlines; confidence earned, not inherited | no | 49 tests: 37 pass, 12 FAILED. class ADJ (trade ADJACENT allows up to two arbitrary words between the core and 'solar'/'energy', so ): 7 confident wrong matches in 48 cases, e.g. trade REPD 15149 'GNR solar timetable chaos hits Great Northern commuters'; trade  // class DEV: 1 of 18 wrong headlines are published as confirmed, e.g. REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor' |
| R02 | Calendar and dates: day-month swap, two-digit year, no time zone, impossible and future dates, 90-day boundary | yes | 79 tests: 75 pass, 4 open recommendation |
| R03 | Stale feed: same items, old dates, new run | yes | 3 tests: 3 pass |
| R04 | Source failure: a part missing, unreadable, raising, of the wrong schema, or with every source failed | yes | 8 tests: 8 pass |
| R05 | An undated item never outranks a dated one; newest first; a fresh possible item is not hidden | yes | 3 tests: 3 pass |
| R06 | A reviewed item duplicated by a fetched one is shown once; reviewed items follow their dates | yes | 6 tests: 6 pass |
| R07 | Multi-project articles handled deliberately | no | 4 tests: 3 pass, 1 FAILED. also_projects is only for an article that names each project |
| R08 | A sharp drop in the counts is not published | yes | 2 tests: 2 pass |
| R09 | generated_at does not advance when collection fails | yes | 4 tests: 4 pass |
| R10 | Counts by tier, never mixing recent news with archive | yes | 3 tests: 3 pass |
| R11 | A register search is not labelled as a planning file | yes | 1 tests: 1 pass |
| R12 | Event type recorded; one event shown once with its sources | yes | 8 tests: 8 pass |
| R13 | Provenance on every item (source, how obtained, when) | yes | 1 tests: 1 pass |
| R14 | One integrated CI run of all signals suites with one table | yes (with pull request 101) | 2 tests: 2 pass with the new workflow |
| R15 | Live checker of the published file names the rule that fails | yes (new in pull request 101) | 13 tests: 13 pass |


The 13 tests that fail on the fixer's branch:

| test | what fails on the fixer's branch |
|---|---|
| `test_R01_tester_false_matches_no_collector_is_confident[ADJ]` | class ADJ (trade ADJACENT allows up to two arbitrary words between the core and 'solar'/'energy', so ): 7 confident wrong matches in 48 cases, e.g. trade REPD 15149 'GNR solar timetable chaos hits Great Northern commuters'; trade REPD 14543 'Tealing solar and battery hub plan near Dundee substation'; index REPD 14543 'Tealing so |
| `test_R01_tester_false_matches_no_collector_is_confident[CTY]` | class CTY (one-word core (weakness 1) accepted with the county or planning-authority word anywhere in): 1 confident wrong matches in 47 cases, e.g. official REPD 14096 'Frodsham solar panels on Cheshire school roof' |
| `test_R01_tester_false_matches_no_collector_is_confident[DEV]` | class DEV (the agreeing 'developer' term is the first operator token outside OPERATOR_STOP, here an e): 6 confident wrong matches in 18 cases, e.g. trade REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor'; index REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor';  |
| `test_R01_tester_false_matches_no_collector_is_confident[DUP]` | class DUP (two of the 200 projects share this core, so one headline attaches to both): 3 confident wrong matches in 11 cases, e.g. official REPD 7191 'Wentlooge solar farm second phase approved'; trade REPD 1980 'Solar Planning firm wins Defford Aerodrome bid'; official REPD 1980 'Solar Planning firm wins Defford Aerodrome bid' |
| `test_R01_tester_false_matches_no_collector_is_confident[GEN]` | class GEN (the alias is a generic farm/lane/place name followed by 'Solar Farm'; the full alias in th): 21 confident wrong matches in 45 cases, e.g. official REPD 15866 'Meridian Solar wins contract for school rooftop arrays'; trade REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor'; index REPD 1 |
| `test_R01_tester_false_matches_no_collector_is_confident[IDXADJ]` | class IDXADJ (index adjacency rule: core directly followed by 'solar' counts as strong even when the nex): 7 confident wrong matches in 22 cases, e.g. trade REPD 14543 'Tealing solar and battery hub plan near Dundee substation'; index REPD 14543 'Tealing solar and battery hub plan near Dundee substation'; trade REPD 9815 'Bumble |
| `test_R01_tester_false_matches_no_collector_is_confident[IDXW]` | class IDXW (index weak rule: core and 'solar' anywhere in the title, kept as weak (uncertain) but stil): 2 confident wrong matches in 32 cases, e.g. trade REPD 1980 'Solar Planning firm wins Defford Aerodrome bid'; official REPD 1980 'Solar Planning firm wins Defford Aerodrome bid' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[DEV]` | class DEV: 1 of 18 wrong headlines are published as confirmed, e.g. REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[GEN]` | class GEN: 4 of 45 wrong headlines are published as confirmed, e.g. REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor'; REPD 19975 'North Ray of Light charity solar donation'; REPD 12822 'Kirkton solar farm plan near Inverurie' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[IDXADJ]` | class IDXADJ: 1 of 22 wrong headlines are published as confirmed, e.g. REPD 9456 'Coldharbour solar farm in Surrey approved' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[IDXW]` | class IDXW: 1 of 32 wrong headlines are published as confirmed, e.g. REPD 19975 'North Ray of Light charity solar donation' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[W0]` | class W0: 1 of 89 wrong headlines are published as confirmed, e.g. REPD 19975 'North Ray of Light charity solar donation' |
| `test_R07_an_article_naming_one_project_is_not_listed_on_another[reviewed]` | also_projects is only for an article that names each project |

What this means:

- Fixed and proven by test: tiers and counts by tier, ordering (dated before undated, newest first), impossible and future dates, the collectors' date readers, stale feed, every source-failure case, generated_at on failure, the sharp-drop refusal (exit 3, file untouched, reason given), a withdrawn reviewed entry no longer carried, a published false match purged on the next run, reviewed duplicates, planning file labels, event types and clusters, provenance, the REPD 9050 rule, and confidence for aliases without evidence.
- Not yet fixed: of the 239 wrong headlines acid tester 1 reported, a few dozen still pass a collector's matcher as a confident match (seven of nine rule classes still have at least one), and eight are still published as confirmed by the combiner (for example REPD 17560, 19975, 12822, 9456). An article that names one project, when the reviewed file lists it under two, is downgraded on the second but still carries also_projects.
- Open recommendations: eight of the twelve are now met by the branch; four date-reader cases remain (feed dates without a usable time zone).
- The published file is still version 1 until pull request 100 is merged and a refresh runs; the live check will be red on the daily schedule until then, naming schema, undated-order, tier-counts and tier-purity.
- If both pull requests are merged as they stand, the `suites` job of the acid workflow fails on main with these 13 tests listed. That is the intended signal, not an accident of the test.
