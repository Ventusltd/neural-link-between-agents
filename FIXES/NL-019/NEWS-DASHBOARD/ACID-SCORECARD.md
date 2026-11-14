# Acid scorecard: top-200 solar project signals

Test lead: Claude Fable. 14 November 2026. Repository Ventusltd/globalgrid2050.

The acid suite is `automation/news/tests/test_signals_acid.py` (pull request 101: tests and CI only). It is written against contract version 2 (`project-signals.v2`). It runs the combiner as a program on fixtures, the collectors' own matchers and date readers on the reported cases, and a checker on the real published file. "Passes" means every test of the rule passes. A test that fails on main is recorded in the suite as a strict known failure naming the review finding it covers; on code that declares version 2 the marker is not applied, so the test must pass there.

Summary

| | tests | pass | fail | known failing | open recommendations |
|---|---|---|---|---|---|
| main, 91727c22 (six suites together) | 259 | 169 | 0 | 78 | 12 |
| fixer's branch, 481388b6, pull request 100 (six suites together) | 270 | 236 | 23 | 0 | 11 |

On main all thirteen product rules (R01 to R13) fail; R14 and R15 are the integrated run and the live checker themselves, added by pull request 101. On the fixer's branch ten of the thirteen pass in full and three still have failing tests: false matches (R01, 21 tests), one date reader (R02, 1 test) and one multi-project case (R07, 1 test).

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
| R07 | Multi-project articles handled deliberately | no | 4 tests: 0 pass, 4 known failing. the article is also listed on a project its title does not name // 4 link(s) on more than one project without also_projects: ['https://morpethherald.co.uk/business/new-solar-farms-on-150-hectares-of-northumberland-farmland-is-given-the-go-ahead-3905725', 'https://www.inkl.com/news/welsh-governmen |
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

## 2. The fixer's branch (acid/team1 at 481388b6, pull request 100, schema project-signals.v2)

The same suite, unchanged, with the known-failing markers switched off by the code's own version.

### Offline acid suite on the fixer's branch at 481388b6 (pull request 100)

186 tests: 152 pass, 0 known failing (strict xfail, each naming the finding it covers), 11 open recommendations, 23 failed.

| rule | what it checks | passes | evidence |
|---|---|---|---|
| R01 | False matches: REPD 9050 and bypass diodes; the testers' 239 wrong headlines; confidence earned, not inherited | no | 49 tests: 28 pass, 21 FAILED. trade.py ties 'Town bypass to get solar-powered road signs' to REPD 9050 as a confident match: ("alias phrase 'Bypass' in title with solar or energy word directly after it", 'confirmed') // class ADJ (trade ADJACENT allows up to two arbitrary words between the core and 'solar'/'energy', so ): 59 confident wrong matches in 48 cases, e.g. trade REPD 15149 'Great North Road solar canopy planned for motorway services'; o // class ADJ: 5 of 48 wrong headlines are published as confirmed, e.g. REPD 15252 'Steeple Morden solar farm plan in Cambridgeshire'; REPD 11476 'Helios Towers plans renewable energy park for masts'; REPD 8479 'Council probes breach  |
| R02 | Calendar and dates: day-month swap, two-digit year, no time zone, impossible and future dates, 90-day boundary | no | 79 tests: 67 pass, 1 FAILED, 11 open recommendation. official.parse_day('1/2/0026') gave '0026-02-01' (acid tester 2: an implausible year must not become a date) |
| R03 | Stale feed: same items, old dates, new run | yes | 3 tests: 3 pass |
| R04 | Source failure: a part missing, unreadable, raising, of the wrong schema, or with every source failed | yes | 8 tests: 8 pass |
| R05 | An undated item never outranks a dated one; newest first; a fresh possible item is not hidden | yes | 3 tests: 3 pass |
| R06 | A reviewed item duplicated by a fetched one is shown once; reviewed items follow their dates | yes | 6 tests: 6 pass |
| R07 | Multi-project articles handled deliberately | no | 4 tests: 3 pass, 1 FAILED. the article is also listed on a project its title does not name |
| R08 | A sharp drop in the counts is not published | yes | 2 tests: 2 pass |
| R09 | generated_at does not advance when collection fails | yes | 4 tests: 4 pass |
| R10 | Counts by tier, never mixing recent news with archive | yes | 3 tests: 3 pass |
| R11 | A register search is not labelled as a planning file | yes | 1 tests: 1 pass |
| R12 | Event type recorded; one event shown once with its sources | yes | 8 tests: 8 pass |
| R13 | Provenance on every item (source, how obtained, when) | yes | 1 tests: 1 pass |
| R14 | One integrated CI run of all signals suites with one table | yes (with pull request 101) | 2 tests: 2 pass with the new workflow |
| R15 | Live checker of the published file names the rule that fails | yes (new in pull request 101) | 13 tests: 13 pass |


The 23 tests that fail on the fixer's branch:

| test | what fails on the fixer's branch |
|---|---|
| `test_R01_no_collector_attaches_a_reported_false_match_as_a_confident_match[trade-9050-Town-bypass-to-get-solar-powered]` | trade.py ties 'Town bypass to get solar-powered road signs' to REPD 9050 as a confident match: ("alias phrase 'Bypass' in title with solar or energy word directly after it", 'confirmed') |
| `test_R01_no_collector_attaches_a_reported_false_match_as_a_confident_match[trade-11678-Boom-Power-secures-planning-perm]` | trade.py ties 'Boom Power secures planning permission for 49.99MW Drove Lane solar PV plant in East Yorkshire' to REPD 11678 as a confident match: ("alias phrase 'East Yorkshire' in title with developer 'Boom'", 'confirmed') |
| `test_R01_no_collector_attaches_a_reported_false_match_as_a_confident_match[official-11678-Boom-Power-secures-planning-perm]` | official.py ties 'Boom Power secures planning permission for 49.99MW Drove Lane solar PV plant in East Yorkshire' to REPD 11678 as a confident match: ("alias 'East Yorkshire Solar Farm' (as 'East Yorkshire') in the title with a solar or energy term", 'confirmed') |
| `test_R01_tester_false_matches_no_collector_is_confident[ADJ]` | class ADJ (trade ADJACENT allows up to two arbitrary words between the core and 'solar'/'energy', so ): 59 confident wrong matches in 48 cases, e.g. trade REPD 15149 'Great North Road solar canopy planned for motorway services'; official REPD 15149 'Great North Road solar canopy planned for motorway services'; trade REPD 15149 ' |
| `test_R01_tester_false_matches_no_collector_is_confident[CTY]` | class CTY (one-word core (weakness 1) accepted with the county or planning-authority word anywhere in): 45 confident wrong matches in 47 cases, e.g. trade REPD 9050 'Contractor named for £60m Lincolnshire bypass'; trade REPD 9050 'By-pass farm shop plan refused in Lincolnshire'; trade REPD 12281 'Tillbridge Lane closure for cabl |
| `test_R01_tester_false_matches_no_collector_is_confident[DEV]` | class DEV (the agreeing 'developer' term is the first operator token outside OPERATOR_STOP, here an e): 17 confident wrong matches in 18 cases, e.g. trade REPD 17699 'Whitestone homes development hits net zero target'; trade REPD 10914 'Island Green Power appoints new site manager at Cottam data hub'; trade REPD 17560 'Island Gr |
| `test_R01_tester_false_matches_no_collector_is_confident[DUP]` | class DUP (two of the 200 projects share this core, so one headline attaches to both): 16 confident wrong matches in 11 cases, e.g. trade REPD 9546 'Pancross & Oaklands Solar Farm approved in Vale of Glamorgan'; index REPD 9546 'Pancross & Oaklands Solar Farm approved in Vale of Glamorgan'; official REPD 9546 'Pancross & Oakland |
| `test_R01_tester_false_matches_no_collector_is_confident[FOREIGN]` | class FOREIGN (the full alias contains 'solar', so official.match and index.match_item accept it anywhere): 13 confident wrong matches in 7 cases, e.g. index REPD 11476 'Helios Solar Farm reaches financial close in Spain'; official REPD 11476 'Helios Solar Farm reaches financial close in Spain'; trade REPD 11476 'Helios solar-pl |
| `test_R01_tester_false_matches_no_collector_is_confident[GEN]` | class GEN (the alias is a generic farm/lane/place name followed by 'Solar Farm'; the full alias in th): 97 confident wrong matches in 45 cases, e.g. trade REPD 15149 'Great North Road solar canopy planned for motorway services'; official REPD 15149 'Great North Road solar canopy planned for motorway services'; trade REPD 15866 ' |
| `test_R01_tester_false_matches_no_collector_is_confident[IDXADJ]` | class IDXADJ (index adjacency rule: core directly followed by 'solar' counts as strong even when the nex): 37 confident wrong matches in 22 cases, e.g. trade REPD 13043 'Springwell solar panels fitted at Gateshead school'; index REPD 13043 'Springwell solar panels fitted at Gateshead school'; trade REPD 14098 'Fenwick solar pane |
| `test_R01_tester_false_matches_no_collector_is_confident[IDXW]` | class IDXW (index weak rule: core and 'solar' anywhere in the title, kept as weak (uncertain) but stil): 21 confident wrong matches in 32 cases, e.g. trade REPD 10914 'Cottam residents fear solar panels on Preston new homes'; trade REPD 14851 'Rosefield care home solar panels approved'; trade REPD 15252 'Steeple Morden solar far |
| `test_R01_tester_false_matches_no_collector_is_confident[W0]` | class W0 (core scored weakness 0 by trade.weakness() (two or more words, not all in COMMON), so the ): 65 confident wrong matches in 89 cases, e.g. trade REPD 14806 'One Earth climate fund backs community energy projects'; official REPD 14806 'One Earth climate fund backs community energy projects'; trade REPD 17701 'Light Valle |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[ADJ]` | class ADJ: 5 of 48 wrong headlines are published as confirmed, e.g. REPD 15252 'Steeple Morden solar farm plan in Cambridgeshire'; REPD 11476 'Helios Towers plans renewable energy park for masts'; REPD 8479 'Council probes breach of solar farm planning conditions' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[CTY]` | class CTY: 30 of 47 wrong headlines are published as confirmed, e.g. REPD 12281 'Tillbridge Lane closure for cable works in Lincolnshire'; REPD 16063 'Lime Down quarry restoration plan in Wiltshire'; REPD 17560 'The Droves nature reserve in Norfolk wins lottery cash' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[DEV]` | class DEV: 11 of 18 wrong headlines are published as confirmed, e.g. REPD 17699 'Whitestone homes development hits net zero target'; REPD 10914 'Island Green Power appoints new site manager at Cottam data hub'; REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[DUP]` | class DUP: 3 of 11 wrong headlines are published as confirmed, e.g. REPD 14100 'Fosse Way solar farm plan refused in Somerset'; REPD 11278 'Wentlooge Levels flood defence scheme in Gwent'; REPD 17429 'Fosse Way solar farm in Somerset approved' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[FOREIGN]` | class FOREIGN: 4 of 7 wrong headlines are published as confirmed, e.g. REPD 11476 'Helios Solar Farm reaches financial close in Spain'; REPD 19016 'Springfield Solar Farm in Missouri switches on'; REPD 6012 'Kells solar farm plan in County Meath' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[GEN]` | class GEN: 26 of 45 wrong headlines are published as confirmed, e.g. REPD 17699 'Whitestone solar farm plan for Herefordshire village'; REPD 14806 'One Earth climate fund backs community energy projects'; REPD 17560 'Island Green Power: what the droves of solar applications mean for Nor' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[IDXADJ]` | class IDXADJ: 2 of 22 wrong headlines are published as confirmed, e.g. REPD 9456 'Coldharbour solar farm in Surrey approved'; REPD 8494 'Warren solar panels in Doncaster' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[IDXW]` | class IDXW: 10 of 32 wrong headlines are published as confirmed, e.g. REPD 9050 'Bypass plan would cut through proposed solar farm site near Grantham'; REPD 15252 'Steeple Morden solar farm plan in Cambridgeshire'; REPD 14100 'Fosse Way solar farm plan refused in Somerset' |
| `test_R01_tester_false_matches_are_never_published_as_confirmed[W0]` | class W0: 51 of 89 wrong headlines are published as confirmed, e.g. REPD 14806 'One Earth climate fund backs community energy projects'; REPD 17701 'Light Valley festival lights up Calderdale'; REPD 10916 'West Burton village in Wensleydale gets community energy grant' |
| `test_R02_collector_date_readers_never_swap_day_and_month_or_invent_a_date[official.parse_day-year-0026]` | official.parse_day('1/2/0026') gave '0026-02-01' (acid tester 2: an implausible year must not become a date) |
| `test_R07_an_article_naming_one_project_is_not_listed_on_another[reviewed]` | the article is also listed on a project its title does not name |

What this means:

- Fixed and proven by test: tiers and counts by tier, ordering (dated before undated, newest first), impossible and future dates in the combiner, stale feed, every source-failure case, generated_at on failure, the sharp-drop refusal (exit 3, file untouched, reason given), a withdrawn reviewed entry no longer carried, reviewed duplicates, planning file labels, event types and clusters, provenance, the REPD 9050 rule, and confidence for aliases without evidence.
- Not yet fixed: the collectors' matchers are unchanged, so the 239 wrong headlines acid tester 1 reported still pass them, and the combiner's second-term rule lets many through as confirmed (for example a county name next to a road name). `official.parse_day` still reads `1/2/0026` as the year 26. A reviewed link is kept on a second project whose title it does not name, because being in the reviewed file is taken as the reviewer's evidence.
- The published file is still version 1 until pull request 100 is merged and a refresh runs; the live check will be red on the daily schedule until then, naming schema, undated-order, tier-counts and tier-purity.
- If both pull requests are merged as they stand, the `suites` job of the acid workflow fails on main with these 23 tests listed. That is the intended signal, not an accident of the test.
