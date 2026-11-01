# NL-010 Team 1 — REVIEW of STEPS.md by FABLE-T1B (evidence officer)

REVIEW: PASS (round 3, 21:19 UTC, FABLE-T1B; rounds 1–2 below for the record)
PASS given on the revision of 21:18:35 UTC (40,013 bytes), which closes the two round-2 points: line 107 now cites
`:1662-1669` (module) and `:6017-6023` (cartridge), both verified by `sed -n`; the star-slot rule is now one breakpoint,
`max-width:380px` strip / `min-width:381px` seventh title, with the slack 79 / 91 / 110 px at 381 / 393 / 412 re-done
by me from the measured 302 px (six titles 224.4 + slot 77.6). Every claim in STEPS.md that carries a key was checked
against the file at that key; every measured number was reproduced by my own run (EVIDENCE A9, B6) or recounted (B3).

Round 2 (superseded) reviewed: `FIXES/NL-010/team-1/STEPS.md` as revised at 21:15:01 UTC on 2026-11-01 (39,954 bytes),
diffed against the 21:08 revision and re-checked against `EVIDENCE.md`, the owner's words (`FIXES/NL-010/BRIEF.md:5-11`)
and NL-009 round 1 (`01-bar.md`, `06-seethrough.md`, `09-robust.md`). Round 1 (21:13 UTC, ten points) is superseded by
this file; its text is in the issue comment
https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6563980345.

## Round 1 points, as they stand at 21:15

| # | point | state | checked how |
|---|---|---|---|
| 1 | keys that do not land | mostly closed: `:31`, `:107-124`, `:141-160`, `:220-225`, `:554-583`, `:1-21`, `:30-35` land | `sed -n` on `gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js` |
| 2 | branch, live generation, NOTICE.md | closed: header names `preview/202610312138-gridatlas-v9.188`, `cacb69a`, `41729af`, 202610312138; licence now `LICENSE:1-3`, `README.md:150-160` | file read; `git` facts as in EVIDENCE header |
| 3 | the C5 "holds there" column | closed: every GridAtlas cell carries its key and the measured count; the live cartridge's search rule (`:6010-6016`) is stated; the find box stays on the wafer under the bar (C6) and FILE carries it as a row only; EDIT re-derived from Status Colours (colour meaning, legend, lit state) | against EVIDENCE A3/A9 and the cartridge diff (`install()` module `:1647-1746` vs cartridge `:5996-6105`: the search move is the only difference) |
| 4 | desktop lockup, "exactly" | closed: above 700 px the whole lockup is copied, SYSTEM TIME and 2050 TARGET included, the engine's arithmetic keyed (`ventus-corev8engine.js:604-607` verified: `Date.UTC(2050,0,1)`, `toLocaleTimeString('en-GB')`, `DAYS`), `.hud-header` CSS `:195-202` verified, flanks hidden at `:375-376` verified | `sed -n` |
| 5 | the star slot and A2 | closed in substance (a width rule the shell owns; ≤ 380 px the 44 px bottom-left strip as GridAtlas's chips, measured (15,697) 65.7×44 by me) — one gap remains, see point B | arithmetic re-done: 393 − 302 = 91 ≥ 72; 381 − 302 = 79 ≥ 72 |
| 6 | `::after` over an open panel | closed: removed under `[data-open]`; A6 tests both states | text |
| 7 | what the module removes | closed: `:697-703`, `:704-708`, `:710-723` superseded; `:726` kept and re-pointed; `:728-749` kept for team 2 — matches EVIDENCE B2 | line ranges verified |
| 8 | asynchronous hooks | closed: `keys.json` (`loadEdition :628-631`) and the wafer waited for on GridAtlas's 250 ms × 160 clock (`:35`, `:1770-1797`), "waiting for keys.json" on the strip, `edMeta.error` words after | keys verified |
| 9 | B1 arithmetic | closed: 216 = 212 + 4, 7 with `quote_key`, the 344 decomposition quoted | matches my recount (EVIDENCE B3) |
| 10 | 1.3× font scale | closed: A2 runs at 1.3× with the expected result stated | text |

## Round-2 points (closed at 21:18)

A. **One key still does not land.** Lesson 1.5 (STEPS.md line 107) cites `:1658-1667` for the moves of the commands into
   the panels; `:1658-1660` are `installStyle / bar = buildBar / buildLayerControls`, and the moves are `:1662-1669` in
   the module and `:6017-6023` in the live cartridge (EVIDENCE A4). Replace the range.
B. **The star-slot width rule has a hole from 381 to 392 px.** "from 393 px up … the seventh title" and "at
   `max-width:380px` … the strip" leave twelve widths with no rule, and A2 runs at 393 but a Pixel 5 is 393 and a
   Galaxy A-series is 384. Since the seventh title already fits from 381 px (381 − 302 = 79 ≥ 72), write one
   breakpoint: `max-width:380px` → strip, `min-width:381px` → title (or whichever single number you choose, with its
   slack), so that every width has exactly one answer.

Everything else PASSES against the evidence and the owner's four instructions for the shell (logo exactly as GridAtlas:
C3 with the flanks; labels and commands like GridAtlas: C4–C7 and the corrected C5; consistent UI built around the
wafer: C1, C6, C8 and the unchanged `safeBox`/`edFly` law; the line of code is the header, written in the page, the
README and LAWS.md: step 2 K1–K6). Both closed at 21:18:35; `REVIEW: PASS`.
