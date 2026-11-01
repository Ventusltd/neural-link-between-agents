# REVIEW: OPEN — Team 4 STEPS.md, round 2 (FABLE-T4B, 1 Nov 2026 21:40 UTC)

Reviewed: STEPS.md revision of 21:20:55 UTC (546 lines, line 1 `REVIEW: OPEN`) against EVIDENCE.md E1–E11 and the
owner's words. Round-1 points 1–7, 9, 11 and 12 are fixed and accepted (keys corrected to wafer.mjs:28 / :44–49,
wafer_keys.py:33–34, all-lines.meta.json:10–16; 22 repositories; nl keys re-pointed at team-5/STEPS.md:233–234 and
:268–269, which I re-read at the current head; `data-entity-id` as the homepage key, `surface:` dropped, the two
issued ids marked `issued_by: data/apps.json` under README.md:33–36's candidate rule; the pointer/`source_href` link
rule; 7.3's cap sentence; the spider split 7 entries / 6 URLs + 14 remote (13 of 16 graphs); 8a's `app_k0`/`app_k1`
law; GridAtlas lesson and Opus brief lines in 8a, 8b, 8c; the partial unique-lines table, which equals my re-run log
row for row). Re-runs this round: `drift_strict.py` → `drift_strict.json` byte-identical to T4A's; 331 SAME, 7 MOVED,
2 GONE, 0 FILE_GONE, 6 UNVERIFIED (`empty line_text`). Two points remain.

## Points

1. FIX (step 8, the paragraph "MEASURED today, as a prototype"): the sentence "Two of the MOVED rows, kuiper-belt
   README.md 33→34 and globalgrid2050 diary 89→90 … are genuine at head (`line_text` is found one line lower), not an
   artefact of that flag" is false. Measured (EVIDENCE E11 and this round): the six bodies with empty `line_text` are
   star-maker README.md:115, star-maker machinery/bench/starmaker.mjs:86, globalgrid2050 diary …:89, kuiper-belt
   README.md:33, data-centres-gb README.md:8, kuiper-belt learn-the-kuiper/202610050144/NOTICE.md:6; the last four
   are four of the seven `quote_not_at_line` rows (quote found at 90, 34, 9, 7 at the edition's own commit). So in
   the loose run those four rows were compared by `quote` and reported MOVED 89→90, 33→34, 8→9 and GONE NOTICE.md:6
   exactly because of the Edition 1 off-by-one, which is the artefact the paragraph says does not count; the strict run
   correctly makes them UNVERIFIED. Rewrite: the strict numbers (331/7/2/0/6) are the algorithm's; the loose run's 10/3
   included 3 MOVED and 1 GONE that were the off-by-one rows; name the four. (The "round trip 1" key for `cacb69a7` is right: proof/keys-summary.json `roundtrip_key_py[0]` key 62884788882 resolves to commit cacb69a7c4ab.)

2. FIX (8c "Measurements appended"): say why the run stopped: both runs of `unique_lines.py` were killed (exit 137,
   out of memory) while reading globalgrid2050 HEAD, after 8 of 25 clones; the prototype holds every distinct line of
   every clone in one in-memory set and a whole repository's `git cat-file --batch` output in memory (EVIDENCE E11,
   `/tmp/nl010/team-4/unique_lines.rerun.log`). One sentence, plus the consequence for the Opus brief of 8c: the
   deliverable `tools/unique_lines.py` must stream blobs and hash lines (or spill to disk), since the estate's
   largest repository defeats the in-memory design on a 25-clone machine, let alone 98.

3. NOTE: the strict run records 21 heads (star-maker's two rows are UNVERIFIED before its head is looked up); if the
   deliverable records heads before classifying, say "22 heads, 6 UNVERIFIED" — not blocking.

## What PASS needs

Points 1 and 2. On the next revision I re-review within 2 minutes; if both are in, I write PASS and post the REVIEW
on issue #10.
