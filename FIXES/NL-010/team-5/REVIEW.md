REVIEW: OPEN

# Team 5 REVIEW of STEPS.md (FABLE-T5B → FABLE-T5A), round 1, 2026-11-01 21:02 UTC

Reviewed: FIXES/NL-010/team-5/STEPS.md as on disk at 21:00 UTC (line 1 `REVIEW: OPEN`, 320 lines). Every key was
re-read at the heads named in EVIDENCE.md. Verdict per LAWS.md L10 (kuiper-belt@018b46a LAWS.md:139-172).

## HONOURED (keys that resolve to the text claimed)

gridatlas@5ec7f62 docs/RELEASE.md:3-7, :38-45, :40, :41, :49-55, :117-118, :119-121, :139-151, :264, :283-306,
:291-296, :300-302; atlas/current.json:5, :14-21, :31, :566-573 (sha256 `d94b0de5…`); tools/ci/pr-gate.mjs:176
(`SHA-256 mismatch for`); atlas/modules/202609031958-menu-bar.js:8-17, :122-124, :157;
atlas/cartridges/202609062358-substation-intelligence-v9-63.js:4533-4553 (the fused masthead, "The VENTUS logo is the
best part", `.ventus-main` 14 px 800); LICENSE:139 (Trademarks). kuiper-belt@018b46a .github/workflows/check.yml:6-8,
:25-26; editions/index.html:7, :11, :12; editions/README.md:3-4, :9-10, :12-15, :27; editions/202611012027/README.md:16-19,
:25-26; editions/202611012027/proof/edition-sha256.txt:4 (`1c293c33…  ./keys.json`); editions/202611012027/index.html:628,
:640, :655, :676, :682, :712, :714; see-through/index.html:7, :12; see-through/202610050609/LICENSE.md:1-9, NOTICE.md:3,
:8-18, :16, :22-25, :28-34, :38-39; learn-the-kuiper/README.md:34-37; LAWS.md:111-124. testcode@d09c185 LICENSE:1-3,
NOTICE:1-11, :26-33; spider/INDEX.md:3-5; spider v5 index.html:108, :239, :244. globalgrid2050@c66759f LICENSE.txt:1.
elements@f7a92fb README.md:1-20 (no licence line). Harness notes :19-20, :39-46, :48-49, :51, :53-58, :64, :80-81.
NL-009 round1 01-bar.md:13, :18, :20, :27, :33, :135; 06-seethrough.md:11, :24, :33, :154; 09-robust.md:11, :18, :23,
:36, :221; BRIEF.md:11-20. The register's conclusions (elements: no licence file; spider data terms not stated; See
Through CERN-OHL-S v2 by copying, nothing by linking; the mark is not licensed by Apache-2.0 §6) match EVIDENCE.md §5.

## OPEN (must change before PASS)

O1 STEPS.md:77 cites `tools/ci_check.py:67` for `os.listdir(ROOT)`. That statement is line 68 (line 67 is the K3
   `fails.append` for a tool that does not parse). Write `:68`.
O2 STEPS.md:112 cites `LAWS.md:155` for `NOT EVALUATED`. Line 155 is `OVERREACHED`; `NOT EVALUATED` is line 156.
O3 STEPS.md:165 and :301 cite `galaxies-wafers@fff6fc6 README.md:3-4` for "every permanently numbered line of the
   estate placed by one frozen law". Lines 3-4 are "Code galaxies with layers, in the manner of Grid Atlas." and a
   blank; the quoted sentence is line 5. Write `README.md:5` in both places.
O4 STEPS.md:162 attributes "Titles and descriptions are the sources' own words" to `elements APPS.md:3`. APPS.md:3 is
   the build line (register sha256 `d356562b2e8f`, 250,174 lines). The quoted sentence is `elements README.md:21`.
O5 STEPS.md:17-18 and :252 name the journey script `FIXES/NL-009/round1/android-journey.cjs` "once FABLE-10 writes
   it". It exists now at `FIXES/NL-009/android-journey.cjs` (35,990 bytes, written 20:59 UTC, header "the Android
   end-to-end journey of a Kuiper edition, measured, not eyeballed", usage `node android-journey.cjs <url> <outdir>
   [--device "Pixel 7"] [--all]`). Name that path and drop "once FABLE-10 writes it"; 9.4 may now say the journey
   script is this file, extended by the integrator.
O6 STEPS.md:9-10 keys this repository to `591b57c`. `git rev-parse HEAD` in /home/user/neural-link-between-agents at
   21:00 UTC is `1976a4981159968606262f4ce17402a985fe4247` (the harness commits as teams write). Every harness-notes
   line cited verifies at the current head, so the keys hold; state the head you re-checked against, or state that
   the notes file is unchanged between the two.
O7 Format. The consolidated ROADMAP format carries, per step: goal, GridAtlas lesson with key, Kuiper change, module
   name, files touched, acceptance test on Android, licence note, Opus team brief. Step 9 and step 10 have no
   explicit "Files touched" line (step 10 carries it inside the table's "may touch" column; step 9 only inside
   "Module"). Add one line `**Files touched.**` to each step so the consolidator does not have to infer it.

Nothing else is open. The substance of 9.1–9.8 and of step 10 is HONOURED against EVIDENCE.md; the two owner
questions the draft raises (PR A merged by the integrator versus the owner; a K5 in ci_check.py versus a separate
tool) are carried to ROADMAP.md's open questions, not resolved here.

## NOT EVALUATED

The negative tests of `tools/edition_check.py` (E1–E5) and the journey steps (a)–(o) cannot be run: the tool and the
edition do not exist yet. They are acceptance criteria, listed as such.
