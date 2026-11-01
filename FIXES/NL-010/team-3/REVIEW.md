REVIEW: OPEN

# NL-010 Team 3 review of STEPS.md (round 1)

Reviewer FABLE-T3B, 2026-11-01 ~21:35 UTC. Reviewed: `FIXES/NL-010/team-3/STEPS.md` (474 lines, "REVIEW: OPEN",
committed at neural-link 51ac5b8) against `EVIDENCE.md` (E1–E12) and the owner's words (BRIEF.md:6-7, "See Through
to be the star player"). Every key the draft cites that I had not already measured was opened on the clones at
kb@018b46a, ga@5ec7f62, gg@c66759f; the draft's own measurements were recomputed where a script could do it.

## Verified (no action)

- M3 recomputed: 344 placed bodies, keys min 36,064,705,400, max 63,035,688,574, 278 at or beyond 59,637,070,538;
  `cosmos/wafer.tsv` re-summed (lines + gap_before over 13,344 rows) = 63,340,120,796 = `wafer-meta.json` address_space;
  `wafer.tsv` 535,037 B, `repos.tsv` 2,467 B. `keys.json` bodies carry `line_text` (A2 of step 6 is testable).
- `KGGridData.substations.names['1182'] === 'Drax'` (so `find('drax')` → 1182 holds). No `<a>`, `el('a')` or
  `createElement('a')` in descent.js, see3d.js, model.js: the "no link out" claim of 5.8 holds.
- Keys opened and found exact: descent.js :15, :19-22, :35-36, :101, :159-160, :346, :389-425, :427-435, :442-446,
  :592, :818-822, :848-849, :855-860, :862-863, :872-874, :907, :917, :926-936, :954-955, :962-967, :1034-1050,
  :1052-1057, :1072-1073; kuiper-law.js :35-36, :113; menu-bar.js :1-3, :31, :141-157, :177-178, :221, :481-503,
  :584, :616-621, :629-632, :707-733, :737-762, :794-811, :1082, :1120, :1206, :1350-1389, :1392-1407, :1490,
  :1499-1575, :1586-1588, :1662-1669; substation-intelligence-v9-63.js :6010-6016; place-postcode-search.js :206-209,
  :294-298; deep-link-receiver-manifest.json :4-5; gridatlas index.html:2; lesson.js :320-336 (hashText :333 writes
  `k=&n=&s=&g=&w=&r=&o=&p=`), play.js :736-752, one.js :468; Edition 4 :92, :203-208, :219, :278-286, :604-611,
  :628-638, :651-664, :676-680, :688-695, :696-703, :714-724, :726; editions/README.md :12-24, :27-28; Edition 4
  NOTICE.md :7-11; PALETTE.md :9-14; gridatlas and kuiper-belt LICENSE both Apache-2.0; team-1 STEPS :51, :156,
  :191-195 (224.4 + 77.6 = 302.0; 5.64 px per character at 9 px, so SEE THROUGH 74.2 px follows); team-2 3.6 and the
  `see-through` row :212; team-4 7.2 (launcher is a panel, no bar entry); team-5 :168; NL-009 01-bar :43-45,
  05-lines :31-36 and :40-44, 06-seethrough :11-60, :126-173, 09-robust :25-29.
- The structure the brief asks for is present in both steps: goal, GridAtlas lesson with keys, Kuiper change, module,
  Android acceptance test with numbers, licence note, Opus team brief. See Through is first and largest (5.1), on a
  phone (5.1b, 5.3), the descent is named by key (5.4), deep links in and out exist (5.5, 5.7, 5.8), the stars gather
  by the same law as a layer (5.6); the File menu is an OS File menu (6.1) with one hash grammar (6.3) and a
  round-trip law (6.4). The departure from GridAtlas's `?repd_ref=` to the hash is argued with keys (6.3).

## OPEN points (fix all; 1–3 are substance, 4–7 are keys and words)

1. **5.5 `sub` contradicts the box's own law and the draft's own example.** `bestMatch()` (ST descent.js:404-408)
   returns the exact lower-case match if any, else `mIdx[0]`, the first substring match; so GO flies whenever there
   is at least one match. The table says "an exact lower-case match, or exactly one substring match, flies; otherwise
   no flight". Measured in grid-data.js names: `cowley` matches 'Cowley Substation' (201) and 'Cowley Road Substation'
   (4275) and no name equals 'cowley'; so the draft's example `…/see-through/#sub=Cowley&view=3d` (5.5) would not fly
   under its own rule, while typing cowley and GO flies to 201 (and the diary's worked example is "Try: cowley",
   kb@018b46a diary/20261005.html). Likewise `hinkley` → 1892 'Hinkley Point A Substation', 1893 'Hinkley Point B
   Substation'. Choose one and write it with its key: (a) the link is exactly "the typed name plus GO" (bestMatch
   byte for byte; then A3's `#sub=Hinkley` expects `T === 1892`, not −1), or (b) the stricter rule, stated as a
   departure from the box with the reason, with the Cowley example changed to a name that is exact or unique and A3
   kept. (a) is the smaller claim and the one the owner's "Try: cowley" already teaches.
2. **`sub` is a search, not an identity; say so against 5.L4.** `KGGridData.substations.names` has 4,460 entries for
   5,800 substations (1,340 have no name, `nameOf` :100 says so); 4,338 distinct lower-case names; 91 names are used
   more than once ('Drax' is 1182 and 1368). GridAtlas's lesson 5.L4 is one exact identity parameter. The step must
   state: `key` (the star key, `subKey[j]`, one per substation, 5,800 of 5,800) is the identity field; `sub` is a
   convenience that reaches only named substations and lands on the first of a duplicate; A3's `T === 1182` holds
   because 1182 precedes 1368 in the file, written down as such. The README sentence of 5.8(d) carries the same.
3. **5.6: state the rule for the day the wafer is re-measured.** `cosmos/wafer-meta.json` `last_unix` is 1793539112
   (2026-11-01) and `address_space` grows with the estate (ci_check K2, kb@018b46a tools/ci_check.py:9, 56-60). The
   draft re-lifts `SPACE` into the See Through folder and makes the Kuiper layer `FAIL … draw nothing` when the
   folder's `SPACE` ≠ the wafer's (5.6, A4). That is correct the day the edition is cut and FAIL the day after the
   next cosmos re-measure, and every `#key=<subKey>` link between the two pages changes meaning with each re-lift.
   Write the rule, one of: (a) See Through reads `SPACE` at run time from `../../cosmos/wafer-meta.json` (address_space)
   with the folder's frozen constant as the offline/file:// fallback, and the layer compares the value See Through
   actually used; or (b) the folder stays frozen (the law file's own instruction, kuiper-law.js:38), the edition pins
   `see_through: "<stamp>", space: <n>` (already in the feature properties, 5.6) and the row shows the mismatch with
   both numbers as a measured state (`STALE · See Through <stamp> SPACE <a> · wafer <b>`), drawing the stars at the
   pinned `SPACE` because that is what See Through will do when tapped, and the release law (team 5 step 9) requires a
   new See Through folder whenever cosmos changes. Either is acceptable; the draft today implies they agree forever.
4. **Keys that do not land (all verified; move them):** `CHOOSE A SUBSTATION FIRST` is ST descent.js:364, not :362
   (:362 is `function enter3d`); `lit` is :871, not :870; the WebGL context is Edition 4 index.html:122
   (`getContext('webgl2', { antialias:false, alpha:false, powerPreference:'high-performance' })`, no
   `preserveDrawingBuffer`, which supports 6.1 EXPORT as written), not :121; `lightTime` in the find grammar is
   :607-608, not :604-605; the `visibilitychange` handler is :1020-1024, not :1019-1022; Edition 1's `belt/` is
   editions/README.md:22, not :21; "Do not edit it; edit the live page and re-lift" is kuiper-law.js:38, not :37;
   the repd regex `^[A-Za-z0-9-]{1,40}$` needs its path: ga@5ec7f62 atlas/releases/202608300453-atlas-v9/
   ventus-corev8engine.js:799-801 (verified there; the same test is at :821 of the substation-intelligence cartridges).
5. **`nl@…` keys have a sha now.** This checkout is a git repository at 51ac5b8 ("NL-009/NL-010: agent files as they
   land"); EVIDENCE.md, this file's target STEPS.md and the NL-009 round-1 files are committed there. Write
   `nl@51ac5b8 FIXES/NL-009/round1/06-seethrough.md:11-23` and so on (team 4 already writes `nl@<sha>`), and name any
   file read uncommitted.
6. **Phone words in A3.** `caption()` shortens on a phone (SHORT map, `DOWN TO THE SUBSTATION`, ST descent.js:818-822)
   while `S.note` does not. 5.5 puts the `sub` and `key` words in the note and the `repo` words in the caption, and A3
   asserts exact text on Pixel 7. State for each new string whether it is a note or a caption and, for captions, the
   phone form (or add them to SHORT), so A3 is testable byte for byte as the Opus brief demands.
7. **5.1(b) and the owner's bar law.** The strip form moves the star entry out of the bar below 377 px. The owner's
   words are "star player" and (team 1) "the bar on one row on a 360 px phone". The decision is measured and
   acceptable, but add one sentence to 5.1(c) and the README table naming the alternative that NL-009 01 measured and
   rejected or accepted (five titles in one row at 360 with 10 px titles, 01-bar.md "Design"), and why the 9 px
   GridAtlas face is kept instead (the owner's "exactly like GridAtlas"). The reader of the README should not have to
   find 01-bar.md to know the strip was a choice.

Nothing else blocks. On the next draft I will re-open every changed key, re-run the Python checks above, and if
1–7 are closed write `REVIEW: PASS` here and post it on issue #10.
