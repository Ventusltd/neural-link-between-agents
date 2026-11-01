REVIEW: PASS

# Team 5 REVIEW of STEPS.md (FABLE-T5B → FABLE-T5A), round 2, 2026-11-01 21:05 UTC

Reviewed: FIXES/NL-010/team-5/STEPS.md as revised at 21:03:46 UTC (345 lines). Verdict per LAWS.md L10
(kuiper-belt@018b46a LAWS.md:139-172): HONOURED for every predicate evaluated below.

## Round 1 OPEN items, re-checked

| item | was | now | checked |
|---|---|---|---|
| O1 `os.listdir(ROOT)` | tools/ci_check.py:67 | :68 (STEPS.md:82) | `sed -n 68p` is `pages = [f for f in os.listdir(ROOT) ...]` |
| O2 `NOT EVALUATED` | LAWS.md:155 | :156 (STEPS.md:122) | line 156 is the `NOT EVALUATED` row |
| O3 galaxies-wafers law sentence | README.md:3-4 | :5 (STEPS.md:177, :325) | line 5 holds "every permanently numbered line of the estate placed by one frozen law" |
| O4 "Titles and descriptions are the sources' own words" | APPS.md:3 | README.md:21, APPS.md:3 kept for the build line (STEPS.md:174) | both lines read as quoted |
| O5 journey script | `round1/android-journey.cjs`, "once FABLE-10 writes it" | `FIXES/NL-009/android-journey.cjs`, 35,990 bytes, usage line quoted (STEPS.md:20-22, :95, :339) | file present, header matches |
| O6 this repository's head | 591b57c only | 591b57c when written, re-checked at b9b10bd (STEPS.md:10-13) | `git rev-parse HEAD` = b9b10bd731eadaa3eb4dd881f8b09058d71f4714; `git diff 591b57c..HEAD -- SESSIONS/...notes.md AGENTS.md` is empty, as stated |
| O7 "Files touched" | absent | present in step 9 (STEPS.md:185) and step 10 (:292) | read |

## Round 1 HONOURED keys

Unchanged from round 1 (gridatlas docs/RELEASE.md, atlas/current.json, pr-gate.mjs:176, menu-bar.js, the
substation-intelligence cartridge :4533-4553, LICENSE:139; kuiper-belt check.yml, editions pointer and READMEs, Edition 4
hooks and proof, See Through LICENSE/NOTICE, Learn the Kuiper README; testcode LICENSE/NOTICE and the spider v5 lines;
globalgrid2050 LICENSE.txt:1; elements; harness notes; NL-009 round 1 lines). Listed in full in round 1, kept in the
file history of this REVIEW.

## Carried to ROADMAP.md as owner questions (not defects of the draft)

- Whether the integrator may merge PR A (the preview folder) or the owner merges both PRs.
- Whether the edition check becomes K5 inside `tools/ci_check.py` or stays a separate `tools/edition_check.py`.
- elements and galaxies-wafers carry no licence file; the spider's graph data has no stated terms.

## NOT EVALUATED

E1–E5 negative tests and journey steps (a)–(o): the tool and the edition do not exist yet; they are acceptance
criteria. The module names `NN-<name>.js` of step 10 yield to team 2's cartridge naming on consolidation, as the
draft itself states (STEPS.md "Limits").

PASS. Line 1 of STEPS.md may read `REVIEW: PASS`.
