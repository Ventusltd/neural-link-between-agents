REVIEW: PASS

# NL-010 Team 3 review of STEPS.md (round 2, PASS)

Reviewer FABLE-T3B, 2026-11-01 ~21:50 UTC. Reviewed: `FIXES/NL-010/team-3/STEPS.md` as revised by FABLE-T3A (504 lines,
revision after neural-link d9a57af) against `EVIDENCE.md` (E1–E12) and the owner's words (BRIEF.md:6-7). Round 1
(seven OPEN points) is below for the record; every point is closed with a key I re-opened.

## Closure of round 1

1. `sub` now means "exactly the typed name plus GO": `goSearch` :409-415 → `doSearch` :389-403 → `bestMatch` :404-408
   (exact lower-case match, else the first substring match in file order) → `flyTo` :417; the examples agree with the
   file (`#sub=Cowley` → 201 'Cowley Substation', `#sub=Hinkley` → 1892 'Hinkley Point A Substation'; recomputed from
   grid-data.js names) and A3 asserts those indices. Closed.
2. Identity stated against 5.L4: `key` (with `space`) is the identity field, one star key per substation (5,800 of
   5,800, :965); `sub` is a search over 4,460 names, 4,338 distinct, 91 duplicates ('Drax' 1182 and 1368), landing on
   the first; the writer now writes `#key=<subKey>&space=<SPACE>&sub=<name>`. Closed.
3. The rule for a re-measured wafer: See Through reads `SPACE` at run time from `../../cosmos/wafer-meta.json`
   (address_space) with the folder's frozen constant as the offline fallback, `state().spaceSource` says which; every
   written `key` carries `space`; a key from an older sky is remapped by `j = floor(key·20000/space)` checked by
   `floor((j+0.5)·space/20000) === key`; the Kuiper layer shows `STALE · layer SPACE a · wafer b` and still draws, and
   team 5's `edition_check` gets one line. I checked the remap: for all 5,800 star keys under SPACE 59,637,070,538,
   63,340,120,796, 63,340,120,797 and 70,000,000,001 the round trip is exact (0 failures) and a non-star key
   (36,064,705,400) is correctly rejected. Closed.
4. Keys moved: `CHOOSE A SUBSTATION FIRST` :364, `lit` :871, WebGL context Edition 4 :122, `lightTime` :607-608,
   `visibilitychange` :1020-1024, Edition 1 `belt/` editions/README.md:22, "re-lift" kuiper-law.js:38, the repd regex
   at ga@5ec7f62 atlas/releases/202608300453-atlas-v9/ventus-corev8engine.js:799-801. All verified. Closed.
5. `nl@d9a57af` is a commit of this repository (`git cat-file -t` → commit) and the cited files are in it. Closed.
6. Every new string of 5.5 is named as a note (`S.note`, never shortened on a phone) and A3 reads notes; the unknown
   field message is a note. Closed.
7. 5.1(c) names the alternative NL-009 01 measured (10 px titles, `KE4` mark, 347.9 px at 360, SEE THROUGH 80.4 px;
   nl@d9a57af FIXES/NL-009/round1/01-bar.md:43-50, :64) and why the 9 px GridAtlas face is kept ("exactly like
   gridatlas"). Closed.

## Verdict

PASS. Both steps carry goal, GridAtlas lesson with keys, Kuiper change, module, Android acceptance test with numbers,
licence note (CERN-OHL-S v2 for See Through, ODbL for the names, Apache-2.0 for the Kuiper module and GridAtlas's
method) and the Opus team brief. See Through is the first and largest entry and has a measured place on a 360 px phone,
a deep link in (`#key&space`, `#sub`, `#repo`, `#view`) and out (`../../editions/#key=`), its stars gather on the
wafer by the one law as a layer, and the File menu is an OS File menu with one hash grammar that the pointers forward
and that round-trips a spark. Remaining limitations, stated in the draft and agreed: the sandbox proxy blocks the map
tiles, so the descent's map stages were not rendered here; the homepage's dated See Through link is a request to its
owner; team 5B consolidates the module-name and `layers` sentences (Open items 1–2, 5).

Line 1 of STEPS.md set to `REVIEW: PASS` by the reviewer on this verdict so team 5B's poll sees it; the text of
STEPS.md is otherwise FABLE-T3A's. Posted on issue #10 as the team's REVIEW comment.

## Round 1 (2026-11-01 ~21:35 UTC), for the record: REVIEW: OPEN, seven points

1 `sub` rule contradicted `bestMatch` and the Cowley example; 2 `sub` is not an identity (4,460 names / 5,800, 91
duplicates); 3 no rule for the day the wafer is re-measured (SPACE re-lift → FAIL forever after); 4 eight keys off by
one to three lines or missing a path; 5 `nl@…` keys without a sha; 6 note vs caption on a phone; 7 the 360 px strip
decision not named against NL-009 01's alternative.
