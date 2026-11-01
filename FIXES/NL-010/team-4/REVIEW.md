# REVIEW: OPEN — Team 4 STEPS.md, round 1 (FABLE-T4B, 1 Nov 2026 21:25 UTC)

Reviewed: FIXES/NL-010/team-4/STEPS.md as found at 21:08 UTC (480 lines, line 1 `REVIEW: OPEN`) against
FIXES/NL-010/team-4/EVIDENCE.md (E1–E10) and the owner's words (BRIEF.md and Addendum 1). Every number T4A marked
MEASURED was re-run by me from T4A's scripts in /tmp/nl010/team-4/ (reads only). Verdict per point: FIX = blocks
PASS; NOTE = accepted, recorded for the ROADMAP.

## Re-runs (what stands)

- `drift.py` re-run 21:14 UTC: `drift.json` byte-identical to T4A's (`cmp` → identical). 346 rows: 333 SAME, 10 MOVED,
  3 GONE, 0 FILE_GONE, 0 UNVERIFIED; heads recorded for 22 repositories; GONE = gridatlas atlas/current.json:576 and :14,
  kuiper-belt learn-the-kuiper/202610050144/NOTICE.md:6; the 10 MOVED as listed in STEPS.md (5 × dcmerge.py +6, gridatlas
  tools/ci/202609012200-local-ci.mjs 351→367 and atlas/parts/202609012045-sld-sandbox-body.js 409→751, kuiper-belt
  README.md 33→34, data-centres-gb README.md 8→9, globalgrid2050 diary 89→90). STANDS.
- `elements_on_wafer.py` re-run: 244 elements, 221 placeable, 23 not (12 constant, 4 engine, 6 layer, 1 cartridge),
  426 of 426 file rows on the wafer, 30 distinct commits, 31 repositories all in repos.tsv. STANDS (EVIDENCE E8 agrees
  for the 7 apps: 50 of 50 files).
- `app_sizes.py` re-run: See Through 27 files / 3,013 lines; Learn the Kuiper 27 (1 binary) / 10,387; Edition 4 folder
  9 (3 binary) / 1,217; spider v5 4 / 6,539; GridAtlas atlas-v9 shell 23 / 3,113; atlas/cartridges 165 / 1,088,335. STANDS.
- `spider-pixel7.json` read: default load 24 requests, 21 failures, srctag SNAPSHOT, 7 cards, 12 controls all under
  44 px; overview deep link: crumbs still "Federation". STANDS, but the split of the 21 is wrong (point 5).
- Live register: stars@cbca125b blocks/blocks.json 606 blocks, 7 of kind app, the same seven symbols. STANDS.
- `unique_lines.py`: T4A's run wrote no `unique_lines.json` (log stops at galaxies-wafers). My re-run is in progress
  (`/tmp/nl010/team-4/unique_lines.rerun.log`); see point 12.

## Points

1. FIX (keys off by one or more, EVIDENCE E7/E6b): `gw@fff6fc6 wafer.mjs:27` → the 342,795 sentence is **:28**;
   `wafer.mjs:46-51` (SUBSTRATE) → **:44-49**; `kb@018b46a tools/wafer_keys.py:37-38` (600/s, 14-day cap) → the
   constants are **:33-34** (`GAP_KEYS_PER_SECOND = 600`, `CAP_SECONDS = 14 * 86400`; :37-38 is `def rows`);
   `gg@c66759f testcode/202609142202/data/all-lines.meta.json:11-16` → **:10-16** (`"lines": 250174` is :10,
   `distinct` :11, `duplicate_rows` :12, `min` :13, `max` :14, `in_a_family` :15). All other kuiper-belt, gridatlas,
   globalgrid2050, elements, PALETTE, NOTICE, NEXT, LAWS, README and NL-009 keys I checked are right.

2. FIX (count): "23 repositories have moved since Edition 1 was cut" and "all 23 repositories had a clone" → keys.json
   holds **22** distinct repositories (measured; drift.json `heads` has 22). Also "gridatlas alone from `cacb69a7` to
   `5ec7f62f`": cacb69a7 is one of 13 gridatlas commits in keys.json, not a keyed "cut head" of Edition 1; key the
   claim (Edition 1's README or keys.json rows) or write "gridatlas rows are keyed to 13 commits, cacb69a7 among them".

3. FIX (this repository moved): STEPS.md is keyed to `nl@7f7f49d`; HEAD is now `d837d9772c16d9cc4ffedb9f929f4c907f9444f6`
   and team-5/STEPS.md has moved: the `07-apps.js`/`08-<algorithm>.js` slot lines are now **:233-234** and the step
   table rows **:267-269** (not :218, :249-251). team-5/STEPS.md line 1 reads `REVIEW: PASS` already. Re-key, and
   state the nl head once at the top.

4. FIX (the key grammar, 7.1): `surface:<url>` for the 25 homepage rows and `surface:https://ventusltd.github.io/stars/blocks/`
   for the periodic table are **not keys the estate already uses**. elements README.md:15 defines a surface as "the
   folders of the live addresses the register records", and SURFACES.md holds none of these 26 folders except
   `surface:https://globalgrid2050.com/` (SURFACES.md:7, block:Ra). README.md:9 says "None is invented here". Either
   (a) write that the registry **issues** these keys under the estate's grammar and is their issuing file (so
   `source` for them is `data/apps.json` itself, and SURFACES.md is not claimed), or (b) use the homepage's own
   permanent key, `data-entity-id` (homepage_v134.html:32–56, E1c), as the key of a homepage row, with `block:` for
   the seven register apps. Say which and why; A1's regex passes either, so A1 must also assert the provenance rule.

5. FIX (numbers, 7.4): the 21 failures are **7 failure entries for 6 distinct local URLs** (federation_radial.css is
   logged twice: `HTTP 404` and `net::ERR_ABORTED`; then data/nodes.json, data/edges.json, contents/manifest.json,
   contents/nodes.json, contents/edges.json) **plus 14 remote** (estate-menu.js and **13** manifest graphs:
   federation and globalgrid2050-contents are `BUILT_IN` and read locally, overview is local, so 16 − 3 = 13;
   measured list in spider-pixel7.json). The draft says "6 local 404s … and 15 remote fetches … the 14 graphs".

6. FIX (7.1 link of the See Through row): the homepage `href` is the dated folder `…/see-through/202610050609/`
   (E1c line 35) while 7.2/A3 navigate to the pointer `../../see-through/` (NL-009 decision 5c). State which the
   registry carries as `link` and that it differs from the source row (the pointer, with the dated folder recorded
   as `source_href`), or A1's "link = homepage href" and A3 disagree.

7. FIX (7.3, the denominator): the register's `files[]` is capped at **8 per block** (E8: max 8; 17 blocks have
   exactly 8; for Ra, Sb and Pn the `repos` field names repositories the `files` list does not). "The key of line 1
   of its first register file" is fine as a placement rule, but write that "first" means the register's first listed
   file, that the list is a sample, and that an element's code size is therefore not known from the register (8a
   depends on this: a per-app Kuiper of a register app cannot take `files[]` as its file set).

8. FIX (step 8 refusal rule vs the prototype): the rule says a row whose `line_text` is empty is UNVERIFIED; keys.json
   has **6** bodies with empty `line_text`, and `drift.py:20` falls back to `quote` (`text = b.get('line_text') or
   b['quote']`), which is why the prototype reports 0 UNVERIFIED. Either state the fallback and that the deliverable
   will not have it (6 rows will be UNVERIFIED), or change the rule. Also say plainly that the two MOVED rows
   kuiper-belt README.md 33→34 and globalgrid2050 diary 89→90 are the same two rows keys.json `quote_not_at_line`
   flags, and that they are genuine at head (line_text found one line lower), so a reader does not take the
   coincidence for a bug. (The GONE sentence "generation 202610292044's predecessor" is keyed: current.json:3.)

9. FIX (8a, the law): "the app key is the rank of the overarching key among the app's keys … dense, from 0" and
   "silence between the app's commits is left unissued by the same rule" contradict each other: with gaps issued, the
   app key is not a dense rank. Write it as the wafer does (index.html:202–205, E5): per app commit in wafer order,
   `app_k0 = previous app_k1 + gap_before`, `app_k1 = app_k0 + lines`; an app key is `app_k0 + lines_before + (line−1)`;
   "rank" then holds only among issued app keys.

10. NOTE (8a sizes, 8b counts): all re-measured numbers stand; the six private repositories are `unnamed-01…06` at
    repos.tsv:8, 10, 26, 28, 66, 67; keys.json body 1 `blob_lines` 72 confirms the ".gitattributes 72-line" sentence.

11. FIX (format): 8a, 8b and 8c carry no "GridAtlas lesson (with key)" and no "Opus team brief"; BRIEF.md's ROADMAP
    format lists both for every step. One line each is enough (the lesson may be the hashed-cartridge one or
    `current.json:5`; the brief may read "Phase 2: written after the owner's ACCEPT of 1–10").

12. FIX (8c, the appended measurement): the "Measurements appended" section is a placeholder ("FABLE-T4A appends …")
    and 8c says "see the table FABLE-T4B keys from that file", but `unique_lines.json` was never written: the log ends
    after galaxies-wafers (8 of 25 repositories; partial totals in `/tmp/nl010/team-4/unique_lines.log`). Either carry
    the partial per-repository table as it stands, marked partial with the repositories done and not done, or wait
    for my re-run and carry its JSON (I will key it in EVIDENCE.md E11 when it completes). A step may not point at a
    number that no file holds.

13. NOTE (accepted as written, with keys checked): the "OS" definition from ARCHITECTURE.md:9/:22/:848 and README.md:6–8;
    the launcher as a File-menu panel and no bar title (NL-009 06-seethrough.md:24–30, :51–57); 44 px rows (:70);
    same-tab navigation; PALETTE colours :9/:12/:13; the periodic-table drift disclosure (244 vs 606); licences in 7.5
    (elements and stars `not stated`, gw no licence file: confirmed by `git ls-files`); the choice of the drift over
    the other three candidates, its inputs by key, its refusal rule, P1–P5; 8b's five denominators; 8c's definition of
    distinct and the unit-change comparison (ratio 45,735,836,396 / 250,174 ≈ 1.83 × 10⁵; extent √342,795 ≈ 585.5).

## What PASS needs

Points 1–9, 11 and 12 fixed in STEPS.md (line 1 may stay `REVIEW: OPEN` until I write PASS). I poll STEPS.md every
2 minutes and re-review on change.
