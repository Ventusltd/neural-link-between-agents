REVIEW: OPEN

# Team 5 "law and proof": steps 9 and 10 of the NL-010 roadmap

Architect FABLE-T5A. Evidence officer FABLE-T5B (EVIDENCE.md, REVIEW.md beside this file). Channel: issue #10.
Heads this file is keyed to: gridatlas `5ec7f62f213e2d20a02e86427daa182c0f38e4a4`, kuiper-belt
`018b46aed50f28f7b1882a0dcaba6593ce522beb`, elements `f7a92fb085c38dcbbd5cb469a66cd5ca61fb95bf`, testcode
`d09c185c8dacbc5c73afb2b0d0d8dad40745a544`, globalgrid2050 `c66759f0d7ac3489df9158da6eaa1330a37c069f`,
galaxies-wafers `fff6fc6ad4f93a15fe8f6456942a1b44e5547105`, neural-link-between-agents
`591b57cfa0a6446f332ea30ed69a7747f4f05562`. Every key below is `repo@sha path:line` against those heads; the short
form `gridatlas@5ec7f62` means that head. No claim without a key; where a file does not exist the gap is written as
`DISCLOSED` in the sense of kuiper-belt@018b46a LAWS.md:139-170 (L10), never papered over.

Vocabulary used in both steps: **the edition** is the next dated folder `kuiper-belt/editions/<stamp>/` (Edition 5 or
later, the stamp cut in UTC when the integrator cuts it); **a module** is one file `modules/NN-<name>.js` inside that
folder, admitted by the edition's `modules.json` manifest; **the pointer** is `kuiper-belt/editions/index.html`;
**the journey** is the Android acceptance script of NL-009 (`FIXES/NL-009/round1/android-journey.cjs` once
FABLE-10 writes it; until then the method in neural-link@591b57c FIXES/NL-009/round1/BRIEF.md:11-20).

---

## Step 9. The release law for editions, and the licence register

**Goal.** Every Kuiper edition from Edition 5 onwards ships by one written law: a new dated folder, a pointer that
moves in three places and nowhere else, `ci_check` green, the Android journey green, every module hashed in a
manifest, the owner's `ACCEPT <stamp>` on a served preview before the pointer moves, the owner merging the pointer,
and rollback that is the pointer moving back, byte-exact, with no folder ever deleted. Every licence of everything
the edition brings in is verified from the files and written in one register in the edition folder.

**GridAtlas lesson (with keys).**
- A release is a pointer move and nothing else. gridatlas@5ec7f62 docs/RELEASE.md:3-7 ("A release moves
  `atlas/current.json` ... Nothing else changes: the cartridges, manifest, proof and preview loader are already on main
  from the preview PR"); :139-151 (only the pointer and `STATE.md` are in the release commit, "That is what keeps the
  release separately revertable, byte for byte").
- The tested preview is the release. docs/RELEASE.md:119-121 ("`atlas/v/<G>/current.json` must equal the pointer
  about to be written ... If anyone edited one and not the other, it stops").
- The owner accepts on the preview, in writing, first line. docs/RELEASE.md:40 ("the owner comments `ACCEPT G` (first
  line) on the preview PR ... by an owner login ... no agent signature, after G's `cut_at_utc`; a later `REJECT G` ...
  withdraws it"); :49-53 ("Agents never record acceptance ... No script writes an `ACCEPT` line").
- Only the owner merges a release; every PR the flow opens is a draft. docs/RELEASE.md:54-55 and :41 (merge with
  rebase, never squash, so the revert is clean).
- Modules are hashed in the manifest and refused on mismatch. gridatlas@5ec7f62 atlas/current.json:5
  (`IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES`), :14-21 (`cartridge_order`), :31 and :573 (`sha256` per cartridge);
  tools/ci/pr-gate.mjs:176 (`SHA-256 mismatch for <file>` is a gate failure); docs/RELEASE.md:116-117 ("every
  cartridge the manifest names, each hashing to its recorded sha256").
- A module installs nothing until its hooks exist, and a missing hook is published as a failure. gridatlas@5ec7f62
  atlas/modules/202609031958-menu-bar.js:8-17 (the admission rule), :122-124 (`complete:` the exact counts), :157
  (`missing.push('63 unique layer controls')`).
- Rollback is a revert of the pointer commit, proven byte-exact against the commit's parent, gates re-run, published
  like a release. docs/RELEASE.md:283-306 (route C) and :264 ("Rollback is in the reverse order").
- The NL-008 finding: a harness merged release PRs on chat authorisation against "only the owner merges".
  neural-link@591b57c SESSIONS/202611012145-kuiper-edition-harness-notes.md:19-20. The law below closes that gap for
  the Kuiper.

**Kuiper change.** The law, written as `editions/LAW.md` in kuiper-belt (a root-level file, delivered in the release PR
so the owner merges it) and repeated in short in each edition's README:

9.1 **Folder rule.** Every change is a new dated folder `editions/YYYYMMDDHHMM/` (UTC cut stamp); earlier folders are
never edited, never deleted. Version number = order of publication. Source: harness notes :39-41 and kuiper-belt@018b46a
editions/README.md:3-4, :9-10 ("Earlier dated folders are kept unchanged as history. Find the newest edition from the
pointer, not by sorting folder names"). Each folder holds at least `index.html`, `keys.json`, `modules.json`,
`modules/`, `README.md` (with "What changed from Edition N"), `NOTICE.md`, `LICENCES.md` (the register of 9.8),
`proof/edition-sha256.txt` (sha256 of every file but itself: notes :44-46, as Edition 4 does,
kuiper-belt@018b46a editions/202611012027/proof/edition-sha256.txt, 8 rows), `proof/keys-summary.json`,
`proof/render-*.png`, and new from Edition 5: `proof/android-journey.json` and `proof/ci_check.log`.

9.2 **Pointer in three places.** `editions/index.html` names the stamp in exactly three places: the meta refresh
(kuiper-belt@018b46a editions/index.html:7), the link (:11) and `location.replace` (:12), each as `<stamp>/` with no
`/belt/` (notes :41, the Edition 4 correction at editions/202611012027/README.md:25-26). The release PR also adds the
edition's entry to `editions/README.md` and updates its "current edition" sentence (editions/README.md:4, :12-15 is
the shape) and adds the entry to the Editions section of the root README (notes :42-43). A pointer whose three stamps
disagree, or that names a folder without `proof/edition-sha256.txt`, is refused by the check of 9.3.

9.3 **`ci_check` PASS, extended to editions.** Before any push, `python3 tools/ci_check.py` must print
`RESULT: PASS` (notes :48; kuiper-belt@018b46a tools/ci_check.py:97). On GitHub it runs on every push
(.github/workflows/check.yml:6-8, :25-26). Today K3 parses only pages in the repository root
(tools/ci_check.py:67, `os.listdir(ROOT)`), so an edition's `index.html` and its modules are not parsed by CI. The
law adds `tools/edition_check.py` (Opus team 9, step 10) with checks E1–E5, run locally before the preview PR and
wired into `check.yml` in the same PR: E1 every `editions/*/index.html` module script and every `modules/*.js` pass
`node --check`; E2 every module named in `modules.json` exists and hashes to its recorded sha256, and no file in
`modules/` is absent from the manifest; E3 `proof/edition-sha256.txt` matches every file in the folder; E4 the
pointer's three stamps agree and name an existing folder with a proof; E5 `keys.json` of the new edition is
byte-identical to the previous edition's unless the README's "What changed" names a change to the findings (Edition
4's is `1c293c33…`, proof/edition-sha256.txt:4). Its output is saved as `proof/ci_check.log` in the edition folder.

9.4 **The Android journey gate.** The preview is not ready for the owner until the journey passes on
Playwright `devices['Pixel 7']` with `hasTouch`, `isMobile` and `deviceScaleFactor`, real touch only, SwiftShader
flags, served from the repository root (NL-009 BRIEF.md:11-20; notes :53-58). The journey, in order, each step
measured and written to `proof/android-journey.json` with its rectangle, timing or hit-test result: (a) load
`editions/<stamp>/` with zero console errors; (b) the bar is one row at 360 px and 393 px wide (the Edition 3/4
failure, notes :80-81) and the Ventus lockup is at the top; (c) tap each menu title: it opens, the same tap closes it,
a tap on the wafer closes it, the back gesture closes it; (d) tap SEE THROUGH: `../../see-through/` opens on the same
host; (e) open LINES, pick a row: the panel closes, the card appears with the line of code as its header, the spark
is in clear space between bar and card; (f) NEXT VERIFIED LINE three times: the same holds each time; (g) pinch on
the wafer zooms the wafer and not the page; a drag pans and does not scroll; (h) tap a spark of 4 px: it is hit or the
page says what it hit instead; (i) landscape and a font scale of 1.3: the bar is still one row or wraps by design and
says so; (j) every module of `modules.json` reports `admitted` in the page's readout, none `refused`. Every finding of
NL-009 round 1 (FIXES/NL-009/round1/NN-*.md, FINDINGS sections) that is a BLOCKER or MAJOR becomes a journey step
when the integrator folds them in; at the time of writing that folder holds only BRIEF.md, so the list above is the
floor, not the ceiling. The gate is PASS only when every step is PASS; a step that cannot be run (no script yet, a
device profile missing) is written `NOT EVALUATED` with the reason (LAWS.md:153-154), and the preview goes to the
owner only with the `NOT EVALUATED` list in the PR body.

9.5 **Module manifest hashes.** `modules.json` is the edition's `current.json`: `{"edition": "<stamp>", "order":
[...], "modules": [{"id", "path", "sha256", "requires": ["<hook>", ...], "licence": "<SPDX>", "team": "<NN>"}]}`,
mirroring gridatlas@5ec7f62 atlas/current.json:14-21 and :31. The loader in `index.html` (Opus team 4) fetches each
module in `order`, computes its sha256 (`crypto.subtle.digest`), refuses the module when the digest differs or when
any name in `requires` is not a function on the edition's hook table (`loadEdition`, `setPanel`, `edCard`, `edFly`,
`edNext`, `placePanels`, `drawEdition` at kuiper-belt@018b46a editions/202611012027/index.html:628, :714, :655, :676,
:682, :712, :640; and the hooks Team 2 adds in step 4), and prints the refusal in the readout: `<id> refused:
sha256 mismatch` or `<id> refused: missing hook <name>`, never a silent skip (menu-bar.js:15-17). The edition stays
usable without any refused module, as GridAtlas keeps the old interface reachable (menu-bar.js:16).

9.6 **Owner ACCEPT on the preview; who merges.** Two PRs per edition, both drafts, both from branch
`edition/<stamp>`:
- PR A, the preview: adds `editions/<stamp>/` and nothing else (no pointer, no README entries, no root file). Gate:
  9.3 and 9.4 PASS, `proof/` complete, the PR body carrying the journey table and the `NOT EVALUATED` list. Because
  Pages serves main only, PR A is merged so the folder is served at `editions/<stamp>/`; the integrator may merge PR A
  (it changes nothing the stable link shows: the pointer is untouched). The owner tests the served folder on the
  phone and posts `ACCEPT <stamp>` as the first line of a comment on PR A (or `REJECT <stamp>`, which withdraws it),
  the shape of docs/RELEASE.md:40. Agents never post ACCEPT (notes :64; RELEASE.md:49-53).
- PR B, the release: changes only `editions/index.html` (three places), `editions/README.md`, the root `README.md`
  Editions section, and `editions/LAW.md` the first time. Gate: `ACCEPT <stamp>` exists on PR A, by the owner, after
  the folder's cut time; 9.3 PASS on the PR head; the pointer names the folder the owner tested, byte for byte the
  one in main (RELEASE.md:119-121). **Only the owner merges PR B**, with rebase (RELEASE.md:41, :54-55). This tightens
  the Edition 2–4 procedure, where the harness merged and pushed main itself (notes :48-49): that is the NL-008 gap
  (notes :19-20), and the owner is asked in the DECISION-PROPOSAL to confirm the tightening or keep the old path.

9.7 **Rollback by pointer.** A rollback is `git revert` of PR B's pointer commit on a branch `rollback/<stamp>-to-
<previous>`, refused unless the pointer has not moved since (RELEASE.md:291-296), proven by `editions/index.html`
being byte-identical to the commit's parent (:300-302), with 9.3 re-run, published as a draft PR that only the owner
merges. No folder is deleted or edited; the rolled-back edition stays served at its own stamp and its README entry
gains one line "rolled back on <date>, <reason>" in a later PR. A rollback of an older edition (the pointer has moved
since) is a new release of the earlier stamp through PR B, with the owner's ACCEPT of that stamp quoted.

9.8 **The licence register (`LICENCES.md` in the edition folder).** Verified from the files at the heads above. SPDX
where the file names one; "none in repository" where no LICENSE, NOTICE or licence sentence exists, found by
`grep -rni licen <repo>/` returning nothing.

| brought in | what the edition takes | licence as the files state it | key | note for the edition |
|---|---|---|---|---|
| kuiper-belt engine, edition layer, modules | the page and every module | code Apache-2.0; text and data CC BY 4.0 | kuiper-belt@018b46a LICENSE:1-3; README.md:156-157; editions/README.md:27; editions/202611012027/NOTICE.md:3-5 | every module carries the header `// Apache-2.0, kuiper-belt` and `NOTICE.md` lists it |
| GridAtlas UI contract (menu bar, admission rule, manifest shape, release law) | method, names, CSS values measured from the live shell; no GridAtlas file is copied | Apache-2.0 | gridatlas@5ec7f62 LICENSE:1-3; NOTICE:1-2, :10-12 | if any line of gridatlas code is copied (Team 1 decides), it keeps the Apache-2.0 header and NOTICE attribution (Apache-2.0 §4(d)); a measurement is not a copy |
| the Ventus logo as GridAtlas shows it | the wordmark lockup `.ventus-main` / `.ventus-sub`, a typographic mark, not an image file | the brand is Ventus Ltd's own; Apache-2.0 §6 grants no trademark right, so its use rests on the owner's instruction of 1 Nov 2026, not on the licence | gridatlas@5ec7f62 atlas/cartridges/202609062358-substation-intelligence-v9-63.js:4533-4553 (the fused masthead, "The VENTUS logo is the best part"); atlas/current.json:566-573 (that cartridge is live, sha256 `d94b0de5…`); LICENSE:139 (Trademarks) | `NOTICE.md`: "The VENTUS mark is used by Ventus Ltd, its owner. The Apache-2.0 licence of this code does not license the mark." |
| See Through (the star player) | a button, a deep link, later the descent and the stars' placement law (`kuiper-law.js`) | CERN-OHL-S v2 (strongly reciprocal) for the app's code; the pointer is `202610050609/` | kuiper-belt@018b46a see-through/index.html:7, :12; see-through/202610050609/LICENSE.md:1-9; NOTICE.md:3, :10-18 (per-file table); licences/globalgrid2050-CERN-OHL-S-2.0.txt (full text present) | linking to See Through brings in no licence duty. Copying `kuiper-law.js` or `descent.js` into a module makes that module CERN-OHL-S v2, its source published with the edition (it is) and the module header saying so; it cannot be relicensed Apache-2.0. Keep See Through code in its own module (`05-see-through.js`) so the reciprocity stops at that file |
| See Through data: substation footprints | only if a module draws them | ODbL 1.0 (OpenStreetMap) | see-through/202610050609/NOTICE.md:16, :22-25 | on-screen credit "Substations and lines © OpenStreetMap contributors, ODbL" wherever drawn; derived data stays ODbL |
| See Through runtime services | none copied; reached only through See Through itself | CARTO, Esri World Imagery, AWS Terrain Tiles: their terms as written | NOTICE.md:28-34 | nothing to do in the edition unless a module fetches them directly, which no step asks |
| MapLibre GL JS 4.7.1 | not brought into the edition (the wafer is canvas) | BSD-3-Clause | NOTICE.md:38-39; vendor/MAPLIBRE-LICENSE.txt | register only; no duty unless a module loads it |
| globalgrid2050 (ancestor of See Through's simulator code) | nothing directly | CERN-OHL-S v2 | globalgrid2050@c66759f LICENSE.txt:1 | the reason See Through is CERN-OHL-S v2 (LICENSE.md:1-5) |
| Learn the Kuiper (LEARN button, if Team 1 adds it) | a link | code Apache-2.0, docs CC BY 4.0, globalgrid2050-derived parts CERN-OHL-S v2 | kuiper-belt@018b46a learn-the-kuiper/README.md:34-37 | link only |
| elements (the periodic table: APPS.md, CATALOGUE.md, `catalogue/*.json`) | the app registry (step 7), the `block:<Sym>` keys, titles and descriptions | **none in repository**: no LICENSE, NOTICE or licence sentence in any file (`grep -rni licen` over the clone returns nothing); GitHub's licence detection could not be read from this session (403) | elements@f7a92fb README.md:1-20 (no licence line); APPS.md:3 ("Titles and descriptions are the sources' own words") | `DISCLOSED`. Until the owner adds a LICENSE (the estate's convention is Apache-2.0 code, CC BY 4.0 data, as kuiper-belt README.md:156-157; the choice is the owner's), the edition may link to elements pages and may copy the **keys** (`block:<Sym>`, facts, not expression) but may not vendor `catalogue/*.json` or the descriptions into the edition folder. Step 7's Opus team reads the catalogue at run time from its published address or ships keys only. Ask: owner to add LICENSE and NOTICE to elements before step 7 ships |
| testcode/spider (the spider sandbox v5) | a launcher entry and a graph layer; the dashboard itself stays where it is | Apache-2.0 (repository LICENSE; the spider folder has no licence file of its own, the root one covers it); its data is read live over https from the served GlobalGrid2050 site, and `./spider/data/` is not in the clone | testcode@d09c185 LICENSE:1-3; NOTICE:1-11, :26-33 (third-party data not covered); spider/INDEX.md:3-5; spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful/index.html:239, :244 (`DATA_BASE="./spider/data/"`), :108 (loads `estate-menu.js` from `ventusltd.github.io/spiders`) | copying spider code into a module is Apache-2.0 with attribution. The graph data's terms are **not stated** in the clone (`DISCLOSED`): the spider-graph layer of step 7 draws only what it fetches from the served site at run time, names the source address on the layer, and copies no graph JSON into the edition until the data's licence is written at its source. The `spiders` repository is not in the estate clone; its licence is `NOT EVALUATED` |
| OpenStreetMap-derived material quoted by the verified lines | quotations with keys, as Editions 1–4 | ODbL 1.0; OGL v3 for DESNZ/DUKES material | editions/202611012027/NOTICE.md:7-10 | unchanged: "A quote here is a citation with its key, not a relicensing" |
| galaxies-wafers (Phase 2 comparison only) | nothing in steps 1–10 | to verify at Phase 2 | galaxies-wafers@fff6fc6 README.md:1-4 | register entry opened, not evaluated |

Rule of the register: a row with `DISCLOSED` or `NOT EVALUATED` blocks copying, not linking; L8 (LAWS.md:111-124)
already makes "a dataset carrying a licence" the test of openness, and the edition applies the same test to itself.

**Module.** `editions/LAW.md` (the text of 9.1–9.7), `tools/edition_check.py` (E1–E5, 9.3), `modules.json` (9.5),
`LICENCES.md` (9.8), `proof/android-journey.json` (9.4). Built by Opus team 9 (tooling and register) and team 10
(integration and the gate), step 10 below.

**Acceptance test on Android.** The journey of 9.4 passes on Pixel 7 against the served preview folder, and the
same run against the pointer `editions/` after PR B lands on the same stamp (`location.replace` resolves to
`<stamp>/`, step (a) again). Plus, on a desktop shell: `tools/edition_check.py` prints `RESULT: PASS` with E1–E5 each
PASS; a deliberately altered byte in one module makes E2 FAIL and makes the page print `<id> refused: sha256
mismatch`; a module with a `requires` name that does not exist prints `refused: missing hook`; the revert of 9.7
restores `editions/index.html` byte-identical to its parent (checked with `git diff --exit-code <parent> --
editions/index.html`).

**Licence note.** The law itself and this register are CC BY 4.0 text of kuiper-belt; `tools/edition_check.py` is
Apache-2.0 code. Two gaps the owner must close before their steps ship: elements has no licence file; the spider's
graph data has no stated terms. Neither is invented here.

**Opus team brief (teams 9 and 10, detail in step 10).** Team 9: write `tools/edition_check.py` with E1–E5 and a
negative test for each; write `editions/LAW.md` from 9.1–9.7 without softening a word; build `LICENCES.md` from the
table above, re-verifying every key at the heads the integrator names; wire `edition_check.py` into `check.yml`.
Team 10: the integrator. Cut the stamp, own `index.html`, `modules.json`, `README.md`, `NOTICE.md`, `proof/`;
admit modules in the order of step 10; run the journey after every admission; open PR A and PR B; never post ACCEPT;
never merge PR B.

---

## Step 10. The Opus plan: ten teams of four, one step each

**Goal.** Forty Opus agents build the edition as ten modules, one per step of this roadmap, each team inside its own
files, each module proven on Android before it is handed to the integrator, integrated in an order where every
admission leaves the journey green.

**GridAtlas lesson (with keys).** One module, one slot, one hash, one proof per cartridge (gridatlas@5ec7f62
atlas/current.json:14-21, :31; docs/RELEASE.md:116-118 "`tools/proofs/<G>-<id>.proof.mjs` for every cartridge cut
at G"). A cartridge is admitted only when its hooks exist and the inventory is complete (menu-bar.js:8-17,
:122-124). The preview is additive and never touches the pointer, the loader or the release folders
(docs/RELEASE.md:39). Only the owner merges (:54-55).

**Kuiper change.** The edition folder is laid out for ten teams:

```
editions/<stamp>/
  index.html          integrator only: the engine copy, the edition layer, the hook table, the module loader
  keys.json           integrator only: byte-identical to Edition 4 unless the findings change (E5)
  modules.json        integrator only: order, path, sha256, requires, licence, team
  modules/
    01-shell.js       team 1   04-loader.js     team 4   07-apps.js        team 7
    02-card.js        team 2   05-see-through.js team 5  08-<algorithm>.js team 8
    03-layers.js      team 3   06-file.js       team 6
  data/               one JSON per team that needs one: layers.json (3), apps.json (7), <algorithm>.json (8)
  handoff/NN-<name>/  each team's hand-off (below); removed from the folder before PR A, kept in proof/handoff/
  README.md NOTICE.md LICENCES.md   integrator (10) with team 9's register
  proof/              integrator: edition-sha256.txt, keys-summary.json, ci_check.log, android-journey.json,
                      render-*.png, handoff/ (every team's tests and screenshots)
```

Root-level files any team may change, and only these: team 4 none (the loader lives in the module and in
`index.html` through the integrator); team 9 `tools/edition_check.py`, `.github/workflows/check.yml`,
`editions/LAW.md`; team 2 proposes the card law for the root `LAWS.md` as `handoff/02-card/LAWS-L11.patch` (the
integrator carries it into PR B; nobody edits root `LAWS.md` on the edition branch). The pointer, `editions/README.md`
and the root `README.md` change only in PR B. `cosmos/`, `tools/key.py`, `tools/edition_keys.py`, `see-through/`,
`learn-the-kuiper/` and every earlier edition folder are untouchable by every team.

Each team of four: a **lead** (owns the module file and the hand-off), a **builder** (the second pair of hands in the
same file, never a second file), a **tester** (writes `handoff/NN-<name>/test.cjs`, the team's Android steps in the
journey's own Playwright form, and the screenshots) and an **evidence officer** (the keys for every GridAtlas lesson
and Kuiper hook the module relies on, the module's row of `LICENCES.md`, and the module header's licence line). A team
touches nothing outside its module, its `data/` file and its `handoff/` folder; a change needed elsewhere is a
REQUEST to the integrator on issue #10, not an edit.

The table: step, team, module, files it may touch, acceptance on Android (Pixel 7, real touch, zero console errors
in every case), hand-off.

| step | team | module | may touch | acceptance test on Android | hand-off to the integrator |
|---|---|---|---|---|---|
| 1 the shell (Team 1 Fable, steps 1–2 STEPS.md) | 1 | `modules/01-shell.js` | its module; `handoff/01-shell/` | the bar is one row at 360 px and 393 px (measured `getBoundingClientRect().height` of `#bar` equals one line of its font); the Ventus lockup sits at the top with the face, weight, tracking and two-line form Team 1 measured from gridatlas@5ec7f62 atlas/cartridges/202609062358-substation-intelligence-v9-63.js:4533-4553; the menu titles are the mapped names Team 1 fixes for File, Edit, View, Scope, Grid, About; each opens on tap, closes on the same tap, on a wafer tap and on the back gesture; the labels and commands sit where GridAtlas puts them, not "near the top" | module + sha256; `test.cjs`; 4 screenshots (360, 393, landscape, font scale 1.3); the measured GridAtlas values with keys; `requires` list |
| 2 the card law | 2 | `modules/02-card.js` | its module; `handoff/02-card/` incl. `LAWS-L11.patch` and the README paragraph | after a pick, the card's first visible text node is the line of code itself (the quoted line), rendered as the header; the title, repository and `path:line` come after; the card is capped as Edition 4 caps it (editions/202611012027/README.md:16-19); the spark stays in the clear space after `edFly`; the law sentence "the line of code is the header" is in the page (the EDITION panel), in the README paragraph and in the LAWS patch | module + sha256; `test.cjs`; before/after screenshots; the patch; the paragraph |
| 3 layer registry | 3 | `modules/03-layers.js`, `data/layers.json` | both; `handoff/03-layers/` | the layer registry lists the layers Team 2 Fable names (verified lines, repositories, periods, editions, See Through stars, elements, spider graphs) with GridAtlas's states `WAIT LOAD OK EMPTY FAIL` (the vocabulary galaxies-wafers@fff6fc6 README.md:7-8 inherited from GridAtlas); toggling a layer on a phone changes what is drawn within one frame and the readout names the count; a layer whose source fails says `FAIL` and the reason, never blank | module + data + sha256s; `test.cjs`; screenshots of the registry open and of one FAIL state; the registry schema with keys |
| 4 the loader (cartridge law) | 4 | `modules/04-loader.js` (the reference loader the integrator moves into `index.html`), `handoff/04-loader/` | both | with `modules.json` intact every module shows `admitted` in the readout; with one byte changed in any module that module shows `refused: sha256 mismatch` and the rest still run; with a `requires` entry naming a hook that does not exist the module shows `refused: missing hook <name>`; the page is usable with every module refused (the Edition 4 behaviour remains); load time to first wafer frame on Pixel 7 under SwiftShader is recorded, not promised | loader + sha256; `test.cjs` with the three negative cases; the hook table (name → index.html line at the integrator's copy); the `modules.json` schema |
| 5 See Through, the star player | 5 | `modules/05-see-through.js`, `handoff/05-see-through/` | both | SEE THROUGH is the first and largest entry Team 3 Fable specifies; tap opens `../../see-through/` on the same host (URL checked); a deep link from a spark or a repository to See Through carries the hash grammar of step 6 and lands on the named substation (one named test site, checked by the See Through page's own title); the stars gather by the same placement law (`kuiper-law.js`, CERN-OHL-S v2: kept inside this module and so headed) | module + sha256; `test.cjs`; screenshots (the entry, the landing); the module header naming CERN-OHL-S v2 where code is copied, Apache-2.0 where it is not |
| 6 the File menu | 6 | `modules/06-file.js`, `handoff/06-file/` | both | File offers: open a key (`python tools/key.py` grammar, resolved in page), open an edition (the pointer's list), open an app (step 7's registry), copy a link (the hash deep link); on Pixel 7 "copy a link" writes to the clipboard or shows the link selectable when the clipboard API refuses; the hash grammar round-trips: a link copied from the card reopens the same spark (`location.hash` preserved by the pointer, editions/index.html:12) | module + sha256; `test.cjs`; the grammar written with examples; screenshots |
| 7 the OS, baby steps: apps, periodic table, spider | 7 | `modules/07-apps.js`, `data/apps.json`, `handoff/07-apps/` | all three | the launcher lists apps by `block:<Sym>` key from elements@f7a92fb APPS.md (keys only until elements carries a licence, step 9 register); the periodic table opens as a layer and as an app; the spider sandbox opens as an app (`testcode/spider` v5 served address) and as a graph layer fetched live, with its source address on the layer; no window manager: one app at a time, back returns to the wafer | module + data + sha256s; `test.cjs`; screenshots (launcher, table layer, spider layer); the list of what was copied versus linked, per the register |
| 8 the first intelligent algorithm | 8 | `modules/08-<algorithm>.js` (name from Team 4 Fable's step 8), `data/<algorithm>.json`, `handoff/08-<algorithm>/` | all three | the algorithm runs over the estate's keys with the inputs Team 4 names, prints its key and its result in the readout, and refuses (its refusal rule) with a sentence when an input is missing; on Pixel 7 it completes or reports progress within the time Team 4 bounds; its output carries keys for every number | module + data + sha256s; `test.cjs`; the algorithm's law in the form of LAWS.md (what is measured, how computed, falsified by) |
| 9 law and register | 9 | `tools/edition_check.py`, `.github/workflows/check.yml`, `editions/LAW.md`, `LICENCES.md`, `handoff/09-law/` | these | `edition_check.py` E1–E5 PASS on the assembled folder and each has a negative test that FAILs; the journey script of 9.4 exists in the handoff (taking `FIXES/NL-009/round1/android-journey.cjs` as its base when present) and writes `proof/android-journey.json`; `LICENCES.md` every key re-verified at the integrator's heads | the tool + tests; `LAW.md`; `LICENCES.md`; the journey script |
| 10 integration and proof | 10 | `index.html`, `keys.json`, `modules.json`, `README.md`, `NOTICE.md`, `proof/`, the branch, PR A and PR B | these | the full journey of 9.4 PASS on the served preview; `tools/ci_check.py` and `tools/edition_check.py` PASS; `proof/edition-sha256.txt` complete; the README "What changed from Edition 4" names every module and every NL-009 finding folded in | the PRs, the journey table in PR A's body, the `NOT EVALUATED` list, the request for `ACCEPT <stamp>` |

**Order of integration.** The integrator (team 10) opens the branch on day one with the Edition 4 copy, the hook
table and an empty `modules.json`, and admits in this order, running the journey after each: **4** (the loader: nothing
else can be admitted without it; until it lands, teams test their modules through a copy of the loader stub the
integrator publishes in `handoff/00-stub/`), **1** (shell: the bar, the logo, the menu names every later module hangs
from), **2** (card law), **3** (layer registry, which 5, 7 and 8 register into), **6** (File, which 5 and 7 add entries
to), **5** (See Through: the star player goes in before the other apps so its entry is first and largest by
construction, not by later reordering), **7** (apps, periodic table, spider), **8** (the algorithm, the last layer),
**9** (the tool, the law, the register: it checks everything above, so it lands when there is everything to check),
**10** (proof, README, NOTICE, PR A). A module that turns a journey step red is not admitted; the integrator posts a
REVIEW on issue #10 naming the step and the measurement, and the team revises. `modules.json` `order` is this list,
so the page loads in the same order it was proven in.

**Hand-off form.** `handoff/NN-<name>/` holds `MODULE.sha256` (the digest the integrator must find), `test.cjs`,
`img/`, `EVIDENCE.md` (every key the module relies on, `repo@sha path:line`), `LICENCE.txt` (the module's row for
`LICENCES.md`) and `REQUESTS.md` (anything the team needs changed outside its files, for the integrator, never done
by the team). A hand-off without `EVIDENCE.md` keys or without a passing `test.cjs` on Pixel 7 is returned.

**Module.** The ten modules above and `modules.json`.

**Acceptance test on Android.** Every row's test, then the whole journey of 9.4 on the assembled edition, then the
same journey through the pointer after PR B.

**Licence note.** Each module header states its licence: Apache-2.0 for kuiper-belt code; CERN-OHL-S v2 for
`05-see-through.js` wherever See Through code is copied; team 7 copies no elements catalogue text and no spider graph
JSON until their sources carry a licence (step 9 register).

**Opus team brief.** Four agents per team, roles as above. Read, in order: this ROADMAP, your Fable team's STEPS.md
and EVIDENCE.md, `editions/LAW.md` when it exists, Edition 4's `index.html` edition layer (lines 627–720), the
harness notes. Write only inside your files. Measure, do not guess. Post one FINDING on issue #10 with the PROTOCOL
envelope when your hand-off is complete. Never post ACCEPT. Never merge.

**Phase 2 teams (not assigned; gated on the owner's acceptance of steps 1–10, BRIEF Addendum 1).** When the owner
says steps 1–10 pass, three further bodies of work open, each needing the same shape: a `tools/` script per wafer, a
`cosmos`-like folder per app, and a comparison report whose every number carries a key.
- Per-app Kuipers: one `tools/app_wafer.py <app>` that restricts the walk of `tools/wafer_keys.py` to one app's files
  and commits (See Through, GridAtlas, the spider, the periodic table, Learn the Kuiper, each `block:<Sym>` app in
  elements APPS.md), writing `cosmos-<app>/repos.tsv`, `wafer.tsv`, `wafer-meta.json` in the shape of
  kuiper-belt@018b46a cosmos/wafer-meta.json:1-13, plus `map.tsv` from the overarching key to the app key, checked both
  ways by `tools/key.py`; the K2 sums of `ci_check.py` (tools/ci_check.py:49-60) run per app folder.
- The all-counting Kuiper: a report that first states what the live wafer counts today with keys (wafer-meta.json:2-7:
  issued 45,735,836,396, unissued 17,604,284,400, address space 63,340,120,796, 13,344 commits, 98 repositories at this
  head) and then what EVERYTHING adds (every repository, data and documents, branches or main only, binaries by bytes
  or named and not placed, the denominator), each addition as a measured delta with its own script run, never a
  guess.
- The unique-lines Kuiper: `tools/unique_wafer.py` defining "distinct" in one sentence (exact bytes or trimmed, and
  why), writing a second `cosmos-unique/` folder and `proof/unique-vs-all.json` (distinct count against the all-lines
  count); and the comparison with the wafer that predates the Kuiper, galaxies-wafers@fff6fc6 README.md:3-4
  ("every permanently numbered line of the estate placed by one frozen law, `r = sqrt(key)`, `theta = key x golden
  angle`", `wafer.mjs`, inherited from `testcode/202609151339`) and `globalgrid2050/testcode/wafer-development-
  environment/`: counts, law constants (the Kuiper's `r = sqrt(key), theta = 2 pi frac(key x 2654435769 / 2^32)`,
  wafer-meta.json:12, against galaxies-wafers' golden angle), key ranges, what moved and why, every number keyed.
Teams for Phase 2 are not assigned here; the owner gates it. The release law of step 9 applies to any folder Phase 2
publishes unchanged.

---

## Limits of this file

- `FIXES/NL-009/round1/` held only `BRIEF.md` and an empty `img/` when this was written; the journey of 9.4 is the
  floor and will be extended by the integrator from the auditors' FINDINGS. `android-journey.cjs` did not yet exist.
- Teams 1–4's STEPS.md were not yet on disk; the module names and hook names of steps 1–8 above are proposals in the
  shape Team 2 Fable owns (step 4, the module boundary) and yield to Team 2's names on consolidation.
- GitHub's licence detection for elements and testcode could not be read from this session (HTTP 403 on
  `repos/Ventusltd/elements`); the register relies on the files in the clones.
- The sandbox cannot fetch `github.io` pages (notes :51-52), so "served" is proven by the Pages run, not by a fetch.
