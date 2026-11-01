# NL-010 Team 1 — REVIEW of STEPS.md by FABLE-T1B (evidence officer)

REVIEW: OPEN

Reviewed: `FIXES/NL-010/team-1/STEPS.md` as revised at 21:08:43 UTC on 2026-11-01 (36,115 bytes, line 1 `REVIEW: OPEN`;
the 21:05 draft was read first and the 21:08 revision re-checked point by point),
against `FIXES/NL-010/team-1/EVIDENCE.md` (my keys and my own measurements, `/tmp/nl010/team-1/B/`), the owner's words
in `FIXES/NL-010/BRIEF.md:5-11`, and the three NL-009 round-1 files present (`01-bar.md`, `06-seethrough.md`,
`09-robust.md`). Round 1 of the review.

## What holds (checked, not just read)

- The measured shell agrees with my independent run number for number: bar (5,5) 1270×36 at 1280 px, 350×34 at 360 px,
  402×34 on Pixel 7; six titles one row at every width (widths 50.7/57.9 desktop, 34.6/40.2 phone, sum 218.8 px at
  9 px); brand slot 247×35 / 77.6×33; `.ventus-main` 14 px/800/.2em (measured 76×15 at 1280) and 11 px/.14em
  (55.5×11.5) on a phone; `.ventus-sub` 5.5 px / 4.5 px; the wordmark inside no `<a>`; no logo file exists; `#fs-letterhead`
  `display:none`; GRID/SUBS chips 65.7×44 bottom-left on a phone (EVIDENCE A9).
- The seven ROADMAP fields are present for both steps (goal, lesson with keys, Kuiper change, module, Android acceptance,
  licence, Opus brief). Line 1 carries the review state.
- Step 2's numbers over `keys.json` reproduce exactly: 344 placed bodies all carry `line_text`; 4 empty; `quote ==
  line_text` for 128; 212 differ, of which 147 only in surrounding whitespace, 31 fragment, 31 quote marks/whitespace;
  `quote_check` and `summary.quote_not_at_line` (7) exist; `tools/edition_keys.py:251` writes `line_text`
  (EVIDENCE B3; my recount in the same session). The L11 text is in LAWS.md's own shape (statement + **Falsified by:**).
- The NL-009 fold-in table maps every finding of the three files that touches the shell.

## OPEN points (numbered; 1–5 must change before PASS, 6–10 must be answered in the text or the tests)

1. **Keys that do not land (the law).** Most of the 21:05 draft's slips are already fixed at 21:08 (`:31`, `:107-124`,
   `:141-160`, `:220-225`, `:554-583`, `:1-21` now land). Still wrong: the admission-rule row of the measured table
   (line 57) cites `:30` (`FAILURE_ID`) for the inventory numbers → `:32-35` (`EXPECTED_ENGINE_LAYERS 60`,
   `EXPECTED_PIPELINE_LAYERS 3`, `EXPECTED_LAYER_CONTROLS 63`, `MAX_TRIES 160`); lesson 1.5 cites `:1658-1667` for the
   moves → the moves are `:1662-1669` in the module and `:6017-6023` in the cartridge (`:1658-1660` are
   `installStyle/buildBar/buildLayerControls`). Verified by `sed -n` on `gridatlas@5ec7f62
   atlas/modules/202609031958-menu-bar.js` (EVIDENCE A3, A4, A6).
2. **The repository facts in the header.** `gridatlas@5ec7f62` is not "main": the clone is checked out on
   `preview/202610312138-gridatlas-v9.188`; the shell files are byte-identical on local `main` `cacb69a` (`git diff
   main --stat` empty), and the live pointer on `origin/main` `41729af` names generation **202610312138**, not
   `202610292044` (the clone's `atlas/current.json:3`). Say both, because the step quotes the generation (EVIDENCE
   header table and C5). And `kuiper-belt@018b46a NOTICE.md` does not exist at the repository root (`ls` →
   no such file); the licence lives at `README.md:150-160` ("Code is licensed under Apache-2.0 … documentation and
   generated data under CC BY 4.0") and `LICENSE:1-3`; the edition's `editions/202611012027/NOTICE.md:1-10` is the
   per-edition notice.
3. **The C5 mapping table's "holds there" column is wrong against the code and the measurement, and the Kuiper
   mapping is derived from it.** Measured panels at 1280 (EVIDENCE A9) and the moves in the LIVE cartridge
   (`:6017-6023`, `adoptLate :5903-5995`; module `:1662-1669`, `:1554-1645`): FILE = Export CSV (`:1663`), the Export
   group print/PDF/image/source (`appendExport :1350`), the engine-module group (`appendEngineModules :641`, fetched from
   github.io, 0 rows here) — and NOT the search bar, which the live cartridge deliberately leaves in `.map-container`
   (`:6011-6016`, as your own note under the table now says: the two statements in the file disagree); EDIT = **Status
   Colours only** (`:1664`; measured 1 row "◑ Status Colours"), not the search box; VIEW = fullscreen, Exit full screen,
   GB conditions, **Studies** (`:1665`, `:1556-1558`, `:1588 appendStudies(panels.View)`), not "status, measure, the SLD
   sandbox"; SCOPE = Radius Search, Radius Area, Poly Zone, **Measure**, Grid Finding Scope (`:1666-1669`, `:1578`) plus
   the tray's clear/scope chips on a phone (measured 7 on Pixel 7), not "clear"; ABOUT = Versions ledger, disclaimer,
   shout-out, Estate links, attribution last (`:1557`, `:1580-1583`, `:605-613`, `:1590-1611`). Rewrite the column from
   these keys (one key per cell) and re-derive the Kuiper column from the corrected facts. In particular: GridAtlas keeps
   its search ON the map under the bar and in no menu, so "like the gridatlas" puts the Kuiper's find box (`/`) on the
   map under the bar as C6 already draws it, and the FILE and EDIT rows should not both claim it; EDIT then needs a
   reason from GridAtlas's EDIT (one control that changes how things are coloured) or a stated departure.
4. **"Exactly like GridAtlas" and the desktop lockup.** On every width above 700 px GridAtlas's brand slot is the
   whole `.hud-header`: SYSTEM TIME clock | VENTUS / CABLES & CONNECTIVITY® | 2050 TARGET countdown (measured slot
   247×35 with children 66×35 / 90×20.5 / 57×23; screenshot `ga-desktop1280.png`); the phone rule alone hides the
   two flanks (`:372-376`). C3 drops the flanks at every width. The reasoning is stated, but the owner's word is
   "exactly", so the step must name this as a deviation for the owner to accept in the DECISION-PROPOSAL (one
   sentence: what GridAtlas shows on a desktop, what the Kuiper will show, why), or keep the flanks above 700 px with the
   Kuiper's own two numbers in the same slots (for example the edition stamp and "344 lines lit"), which is the same
   lockup with the Kuiper's content. Either is acceptable; silence is not.
5. **The star slot leaves acceptance A2 unrunnable.** C5 "reserves the first position of the left group" for See Through
   as a title, C9 shows a seventh title in GridAtlas's face does not fit at 360 px (≈ 72–74 px against 58 px of slack;
   my recount at 9 px DejaVu mono: 11 × 5.42 + 12 = 71.6 px), and the decision is deferred to step 5. A2 ("every title
   on one row at 360") cannot be run against a contract with an open slot. State the shell's own width rule now, so
   step 5 chooses within it: for example, at ≤ 360 px the star entry takes the bottom-left 44 px strip that GridAtlas
   itself uses for its two most-used controls (GRID/SUBS chips measured (15,697) 65.7×44 at 360, `chipStaysOnMap
   :1521-1552`), and from 393 px up it is the seventh title (slack 393 − 302 = 91 px ≥ 72). Any rule will do if it is
   measured and keeps one row at 360.
6. **C4's hidden 44 px hit box (`::after` below the bar) overlaps an open panel.** Panels hang from the bar's bottom
   (GridAtlas `top:100%`; Edition 4 `placePanels` = bar height + 2). A 10 px extension below a 34 px bar covers the
   first 10 px of the open panel's first row, so a tap there resolves to the title and closes the menu. Either disable the
   extension while a panel is open, or add to A6: `elementFromPoint` at the open panel's first row's top + 4 px resolves
   to the row, not the title. Also note that GridAtlas's own accepted phone bar is 34 px with no extension; the step
   should say it departs from GridAtlas here on NL-009 01-bar F2's measurement, so the departure is on the record.
7. **What the Module section removes.** "removal of the Edition 3 bar block `:693-726`" is not the block: `:697-703` is
   the bar, `:704-708` the LINES panel, `:710-723` `PANELS/placePanels/setPanel` and the closers, `:726` the `safeBox`
   wrap (keep), `:728-749` the layer switches, `fillLines` and the draw/step wrappers (team 2's material, keep). Name
   exactly which lines the shell module supersedes and which stay (EVIDENCE B2).
8. **C8's hook list and the asynchronous ones.** `keys.json` arrives by `fetch` (`loadEdition :628-639`) and the wafer
   by `cosmos/wafer.tsv`; GridAtlas waits up to 40 s (160 × 250 ms, `:35`, `:1770-1797`) because its register is built
   after map load. Add the bounded retry and the two asynchronous conditions (`edPlaced.length > 0` or `edMeta.error`
   named on the strip, as 09-robust F4 asks) to C8, so the refusal is "waiting for keys.json" and not a false
   "missing hook" during the first second.
9. **Step 2 arithmetic in B1.** The 7 `quote_not_at_line` bodies include the 4 with empty `line_text` (my recount:
   quote_check exact 128 + trimmed 147 + fragment 31 + quote-marks 31 + not-at-line 7 = 344; the 212 differing
   non-empty = 147 + 31 + 31 + 3). If K1 gives the 4 empty bodies a "register quote" row too, B1's count of
   `.cq` rows is 216 (212 + 4), 7 of them with `quote_key`; if not, say the 4 show no quote. Write the number the test
   will assert.
10. **A2 at a system font scale.** 01-bar measured the bar at 1.3×; at 9 px × 1.3 the six titles plus the slot are
    ≈ 393 px, over 360, so C9's `overflow-x:auto` is the path taken. Add the 1.3× run to A2 and state the expected
    result (one row, horizontal scroll, last title reachable), as 01-bar did.

Not blocking, for the record: the clamp rule 01-bar proposes (`clamp(10px,2.75vw,12px)`) is a different answer from
GridAtlas's fixed 9 px; the step chooses GridAtlas's number, which is the owner's instruction, and says so (C9). Agreed.

Next: FABLE-T1A revises STEPS.md; I re-read it on the next poll and write round 2 here.
