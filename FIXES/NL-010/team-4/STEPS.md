REVIEW: OPEN

# Team 4 "the OS of the estate, baby steps": steps 7 and 8 (with 8a–8c, Addendum 1) of the NL-010 roadmap

Architect FABLE-T4A. Evidence officer FABLE-T4B (EVIDENCE.md, REVIEW.md beside this file). Channel: issue #10.
Heads this file is keyed to: kuiper-belt `018b46aed50f28f7b1882a0dcaba6593ce522beb`, elements
`f7a92fb085c38dcbbd5cb469a66cd5ca61fb95bf`, testcode `d09c185c8dacbc5c73afb2b0d0d8dad40745a544`, stars
`cbca125bb5eeb7d0ffb02f4546d60eb5d47dadc9`, globalgrid2050 `c66759f0d7ac3489df9158da6eaa1330a37c069f`, galaxies-wafers
`fff6fc6ad4f93a15fe8f6456942a1b44e5547105`, gridatlas `5ec7f62f213e2d20a02e86427daa182c0f38e4a4`,
neural-link-between-agents `56958f2b20ed4c00b16b48ca5332726e25a3e3b8` (this repository moves as the teams write; the nl keys below are against that head). Short form `kb@018b46a` = kuiper-belt at that
head, `el@f7a92fb` = elements, `tc@d09c185` = testcode, `gg@c66759f` = globalgrid2050, `gw@fff6fc6` = galaxies-wafers,
`ga@5ec7f62` = gridatlas, `nl@56958f2` = this repository. Every key is `repo@sha path:line`. No claim without a key.
Every number that is not in a keyed file was measured by a script in `/tmp/nl010/team-4/` named beside it, and is
marked MEASURED; a number nobody has measured is written UNMEASURED, never guessed.

Vocabulary (shared with Team 5's STEPS.md): **the edition** is the next dated folder `kuiper-belt/editions/<stamp>/`;
**a module** is one file `modules/NN-<name>.js` in that folder, admitted by `modules.json`; **a data file** is one JSON
under `data/` in that folder; **the wafer** is the engine `index.html` copies, its keys from `cosmos/wafer.tsv`.
Team 5's Opus plan already reserves `modules/07-apps.js` + `data/apps.json` for step 7 and
`modules/08-<algorithm>.js` + `data/<algorithm>.json` for step 8 (nl@56958f2 FIXES/NL-010/team-5/STEPS.md:233-234,
:268-269; its line 1 reads `REVIEW: PASS`); the names below fill those slots: `08-drift.js`, `data/drift.json`.

**For FABLE-T4B (evidence keys requested, Addendum 1).** Please key in EVIDENCE.md: (a) galaxies-wafers' law and
counts: gw@fff6fc6 wafer.mjs:11-14 (the law), :28 (342,795), :44-49 (`SUBSTRATE` frozen 2026-09-15T15:00:00Z),
gg@c66759f testcode/202609142202/data/all-lines.meta.json:10-16 (250,174 lines, min 1, max 342,795),
gg@c66759f testcode/202609151339/README.md:9-15; (b) the live wafer's totals: kb@018b46a cosmos/wafer-meta.json:2-12
(issued 45,735,836,396; unissued 17,604,284,400; address space 63,340,120,796; 13,344 commits; 98 repositories; the law
line), tools/ci_check.py:9 and :53-60 (K2 re-sums wafer.tsv and equals wafer-meta.json and repos.tsv),
tools/wafer_keys.py:10-11 and :33-34 (600 keys per second, 14-day cap), tools/count_lines.py:14 and :60-61 (the
binary rule), :122 and :151 (`--all`: every ref of the clone); (c) the one-wafer intermediate: kb@018b46a NEXT.md:8-13.
Also re-run `/tmp/nl010/team-4/drift.py`, `elements_on_wafer.py`, `app_sizes.py`, `unique_lines.py` and
`spider-pixel7.cjs` (serve `/home/user/estate/testcode` on port 8204) and key their outputs.

---

## Step 7. The app registry and the launcher: the first baby step of the OS of the estate

**Goal.** One file in the edition folder names every app of the estate with its permanent key, its stable link, its
licence and one line of purpose; the edition opens any of them from the File menu; the periodic table of the estate's
code and the spider sandbox each become an app row and a layer on the wafer. No window manager, no frames, no second
engine: one baby step the owner can see on a phone.

**What "OS of the estate" means in the owner's vocabulary.** The owner's words: "Turn the kuiper into the OS of the
estate in baby steps" (nl@56958f2 FIXES/NL-010/BRIEF.md:8-9). The estate already uses the word: globalgrid2050 calls
itself "a modular operating system built on ventus-core.js, ventus.css, Python ETL scripts, GitHub Actions, feature
manifests, GridBot automation and versioned application cartridges" (gg@c66759f ARCHITECTURE.md:22), its platform
line is "Ventus OS Modular Pipeline" (:9) and its eighth system is "Versioned App Cartridges" (:848); the Kuiper's
own README calls the wafer "a navigation instrument, not a picture. Its destination is the sandboxes: a body you
cannot open is a body that has failed" (kb@018b46a README.md:6-8). So, in the estate's own terms, an OS is: an
**address space** (the wafer: one key per line, kb@018b46a cosmos/wafer-meta.json:2-4), a **registry** of what can be
opened (this step's `data/apps.json`, the homepage's entity table, gg@c66759f homepage_versions/homepage_v134.html:31-56),
a **launcher** (open an app from one menu, same tab), **cartridges** admitted by hash (Team 2, step 4), a **file menu**
(Team 3, step 6), **layers** on the ground (Team 2, step 3), and a **release law** (Team 5, step 9). What it is not,
yet: windows, processes, a kernel. A baby step adds one of these at a time and proves it on Android before the next.

**GridAtlas lesson (with keys).**
- A thing enters the shell only through a registry record with an id, an order and a hash, never by being pasted in:
  ga@5ec7f62 atlas/current.json:5 (`IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES`), :14-21 (`cartridge_order`).
- A module installs nothing until the hooks it needs exist, and counts what it found: ga@5ec7f62
  atlas/modules/202609031958-menu-bar.js:8-17 (the admission rule), :34 (`EXPECTED_LAYER_CONTROLS = 63`), :157
  (`missing.push('63 unique layer controls')`).
- The estate presents its apps as one table with a stable key per row (`data-entity-id`, `entity-key`), a type
  (application, engine, reference, catalogue, drawing), a link and one line of purpose: gg@c66759f
  homepage_versions/homepage_v134.html:31 (the table, "All apps and their current versions. Select an app to open it"),
  :32-56 (25 rows; MEASURED by `/tmp/nl010/team-4/` parse of the row regex `<tr data-entity-id=`). The homepage opens
  every app in the same tab (nl@56958f2 FIXES/NL-009/round1/06-seethrough.md:16-17, "0 `target="_blank"`").
- The periodic table's key grammar is already the estate's: el@f7a92fb README.md:9 ("Every element, app and function
  with more than 10 lines of code has a unique key. Each key is one the estate already uses and never reuses. None is
  invented here"), :13 (`block:<Sym>` element), :14 (app = register block of kind app), :15 (`surface:<url>` = the
  folder of a live address). Counts: 244 elements, 7 apps, 97 surfaces (el@f7a92fb CATALOGUE.md:7-9). The seven apps:
  `block:Ra`, `Cg`, `Sb`, `St`, `Pn`, `Gp`, `Wf` (el@f7a92fb APPS.md:7-13).

**Kuiper hooks (with keys).** The edition page loads two TSVs and refuses if they do not sum (kb@018b46a
editions/202611012027/index.html:201-205); every key resolves to repository, commit, path through `address(k)` (:282)
and places through `keyPlace` (:633); the edition layer is a list of records filtered by the admission predicate
`on_wafer && verified && key < SPACE` (:632-633); a tap within 9 px opens the nearest spark (:685-690); the bar is four
titles and a name (:699-703) and NL-009 measured it already two rows wide on a 412 px phone, 439 px of content against
412 (nl@56958f2 FIXES/NL-009/round1/06-seethrough.md:24-30). So **the launcher adds no bar entry**; it is a panel that
Team 3's File menu opens ("open an app (step 7's registry)", nl@56958f2 FIXES/NL-010/team-5/STEPS.md:267), and Team 3's
own evidence hands the registry to this step (nl@56958f2 FIXES/NL-010/team-3/EVIDENCE.md:246-247).

**Kuiper change.** One baby step, four parts, all data-first.

7.1 **The registry `data/apps.json`.** One JSON array, one record per app, written by a tool (`tools/apps_registry.py`,
    new, in kuiper-belt at the release PR) from two keyed sources and nothing else: el@f7a92fb APPS.md:7-13 (7 rows)
    and gg@c66759f homepage_versions/homepage_v134.html:32-56 (25 rows), plus two rows the owner asked for by name that
    neither source holds yet: the spider sandbox (tc@d09c185 spider/INDEX.md:13, version 5) and the periodic table
    itself (el@f7a92fb CATALOGUE.md:1). 34 rows. Fields, every one with its source:

    | field | rule | source of the value |
    |---|---|---|
    | `key` | a key the estate already uses, never invented here: `block:<Sym>` where the app is a register block (7 rows, el@f7a92fb README.md:13-14); the homepage's own permanent key `data-entity-id` where the app is a homepage entity (25 rows, gg@c66759f homepage_versions/homepage_v134.html:32-56, the `entity-key` the homepage prints beside each name). `surface:<url>` is **not** used: el@f7a92fb README.md:15 defines a surface as a folder the register records, and SURFACES.md records none of the 25 homepage folders except `https://globalgrid2050.com/` (SURFACES.md:7). The two rows neither source holds (the spider, the periodic table) get the ids `spider-sandbox` and `periodic-table`, and the registry says in the record (`issued_by: data/apps.json`) that it is their issuing file; they are candidates until the homepage or the register names them (kb@018b46a README.md:33-36: a statement without a key is a candidate, written as one) | APPS.md column 1; homepage `data-entity-id`; this file for 2 rows |
    | `key_source` | one of `register`, `homepage`, `issued-here`, so a reader never mistakes an issued id for an estate key | the tool writes it |
    | `name` | the source's own title | APPS.md column 2; homepage link text |
    | `kind` | `app` (register) or the homepage type: application, engine, reference, catalogue, drawing | APPS.md column 3; homepage `entity-type` summary |
    | `purpose` | one line, the source's own words, never written here | APPS.md column 7; homepage "Intended purpose" cell |
    | `link` | the stable link: the homepage `href`, except where the target repository keeps a pointer above its dated folders, in which case the pointer is the link and the dated `href` is kept as `source_href` (See Through: `https://ventusltd.github.io/kuiper-belt/see-through/`, source_href `…/see-through/202610050609/`, homepage_v134.html:35; Learn the Kuiper likewise, :34; NL-009's decision 5c, 06-seethrough.md:55-57: the pointer opens the newest, the dated link does not); for register apps the first `live` URL of `catalogue/apps.json`; for the spider the GitHub tree link at tc@d09c185 until a served address is keyed (none is recorded in el@f7a92fb SURFACES.md; UNVERIFIED) | as stated |
    | `licence` | the licence file of the repository the link lands in, quoted by key; `not stated` when no LICENSE, NOTICE or licence sentence exists at that head | see 7.5 |
    | `source` | `repo@sha path:line` of the row this record was built from | the tool writes it |
    | `wafer` | `{repo, commit, path}` of the app's first register file whose commit is a row of `cosmos/wafer.tsv`, or `null` with a reason | `catalogue/apps.json` `files[]` against wafer.tsv `sha12` (MEASURED: all 50 file rows of the 7 apps are on the wafer, `/tmp/nl010/team-4/elements_on_wafer.py`) |

    Rows whose code and page are the same thing cross-reference each other in `same_as` (e.g. `block:Pn` "Pipeline News
    app" and homepage `pipeline-news`); nothing is merged, because a register block is code with a key and a homepage
    entity is a served page with a version, and the owner may open either. The registry carries its own provenance
    header: the two source heads and the sha256 of the two source files, as el@f7a92fb catalogue/provenance.json:10-12
    does for the register.

7.2 **The launcher `modules/07-apps.js`.** A panel, not a bar title: one more entry in the engine's `PANELS`, opened
    by `setPanel('apps')` and placed under the bar by `placePanels()` (kb@018b46a editions/202611012027/index.html:712-714),
    with no `.gm-title` added, because the bar's content already measures 439 px against 412 px on a Pixel 7 and 360 px
    on a Galaxy S24 (nl@56958f2 FIXES/NL-009/round1/06-seethrough.md:24-30; step 1 owns that budget). It registers one
    File-menu entry "open an app" with Team 3's module and one layer record with Team 2's registry, then draws the list from `data/apps.json` only
    after the wafer has admitted its own data (the hook is the `loadEdition()` call site, kb@018b46a
    editions/202611012027/index.html:219). Each row obeys the card law of step 1: **the header of the row is the key
    line** (`block:Pn` / `see-through`), then name, one-line purpose, licence, and the link. A tap on the link
    navigates in the same tab (NL-009's decision, 06-seethrough.md:51-57: on Android Chrome a `_blank` tab is
    invisible and two WebGL pages on one phone evict each other); a tap on the key, when `wafer` is not null, flies the
    camera to the app's first line on the wafer through `keyPlace`/`edFly` and opens the card (:676-680). The GitHub
    link alone keeps `_blank`, as the edition's card does (:662). A row whose `link` fails `fetch(HEAD)` is drawn with
    GridAtlas' `FAIL` state in its label, never hidden (Team 2's review bar, nl@56958f2 FIXES/NL-010/team-2/EVIDENCE.md:316-317).
    Rows are 44 px tall on a phone (NL-009's hit-target dimension: today's buttons are 29 px, 06-seethrough.md:70).
    **No window manager**: the launcher opens exactly one thing, by navigation, and the back gesture is the way home
    (06-seethrough.md:20-21 and :51-54 measured it).

7.3 **The periodic table: a layer and an app.** *Layer:* every element of el@f7a92fb catalogue/elements.json placed at
    its own key on the wafer. The key of an element is the key of line 1 of the first file the register lists for it (`files[0]`), at the
    register's recorded commit; the register lists at most 8 files per block (FABLE-T4B's E8: max 8, 17 blocks at
    exactly 8, 139 at 1), so `files[]` is a sample, a placement seed, and an element's code size is not known from the
    register (8a says what is), computed exactly as `tools/edition_keys.py` computes a verified line's key (kb@018b46a
    editions/202611012027/README.md:28-35: the commit's first key from wafer.tsv, plus the lines of every text blob
    before that file in `git ls-tree -r <commit>` order, plus the line number, refused when the walk does not land where
    the wafer says the commit ends). MEASURED (`/tmp/nl010/team-4/elements_on_wafer.py`, reads only): of 244 elements,
    221 have at least one register file whose commit is a row of `cosmos/wafer.tsv` (all 426 file rows match; 30
    distinct commits; 31 repositories, every one a row of `cosmos/repos.tsv`); 23 have no files and are counted, named
    in `data/elements.json` and not placed (the seventh law, kb@018b46a editions/202611012027/README.md:34-35): 12
    constants, 4 engines, 6 layers, 1 cartridge. Colour by the palette and by nothing else: `UNSETTLED` state in amber
    (attention, kb@018b46a PALETTE.md:12), the rest as the record (grey-blue, :9); the selected element magenta (:13).
    The card of an element: header = the line at its key (card law), then `block:<Sym>`, title, kind, category, state,
    the register description in the source's words, and the GitHub link at the recorded commit. *App:* a row in
    `data/apps.json` with the issued id `periodic-table`, `key_source: issued-here`, its `link` the register folder the
    catalogue was built from, el@f7a92fb catalogue/provenance.json:10, and a panel that lists the 244 elements by
    category and number like el@f7a92fb ELEMENTS.md, each row's header its key, tap = fly to it. The edition folder
    carries its own copy `data/elements.json` (the 244 records with their computed keys and sha256 of the source), so it
    loads offline like `keys.json` does. Precedent on the pre-Kuiper wafer: gw@fff6fc6 iterations/05-periodic-table/
    table.mjs:1-14 (one cell per block of the live register, grouped by category; tapping a cell flies the wafer to the
    block's first line), which this layer repeats on the Kuiper's keys instead of the numbered lines.

    Disclosed, not hidden: the catalogue is pinned to the register of 2026-09-15 (244 blocks, el@f7a92fb
    CATALOGUE.md:3); the live register at stars@cbca125 blocks/blocks.json:2 is generated 2026-10-31T18:45:22.798Z and
    holds 606 blocks, still 7 of kind app (MEASURED, `python3 -c` over that file). The edition places the catalogued
    244 because they are the keyed, checked set (el@f7a92fb README.md:21-23, `tests/check_catalogue.py`); the 362
    newer blocks are a number in the readout ("606 in the live register, 244 catalogued"), and step 8's algorithm is
    exactly the instrument that will say how far the two have drifted.

7.4 **The spider sandbox: an app and a graph layer.** *App:* one row (`id: spider-sandbox`, tc@d09c185
    spider/INDEX.md:13, the v5 folder `20260914T143049Z-v5-linkify-frontdoor-brandfaithful`). MEASURED on a Pixel 7
    emulation served from `/home/user/estate/testcode` on port 8204 (`/tmp/nl010/team-4/spider-pixel7.cjs`, results in
    `spider-pixel7.json`, screenshot `spider-pixel7-default.png`): the page renders its hard-coded Federation snapshot
    (7 cards, "5 dependencies · 1 dependents", tag `SNAPSHOT`), fits the phone (scrollWidth 412 = viewport, scrollHeight
    839 = viewport), 0 page errors; it makes 24 requests of which 21 fail, logged as 21 failure entries: 7 entries for 6 distinct local URLs
    (`./spider/federation_radial.css`, logged twice as `HTTP 404` and `net::ERR_ABORTED`; `./spider/data/nodes.json`,
    `edges.json`, `contents/manifest.json`, `contents/nodes.json`, `contents/edges.json`, which the v5 folder does not
    contain: it holds only `index.html`, `spider/identity.json`, `spider/manifest.json`, `spider/overview-graph.json`)
    and 14 remote fetches (`estate-menu.js` from `ventusltd.github.io/spiders`, and 13 of the 16 graphs of
    `spider/manifest.json`, on `ventusltd.github.io/{ventus-grid-engine,spiders,stars,code-generator}`; `federation`
    and `globalgrid2050-contents` are `BUILT_IN` and read locally, `overview` is local) blocked by the sandbox proxy; the 12 visible controls are all under 44 px. The deep link `?graph=overview&focus=…` did not
    reach the overview within 8 s because the manifest graphs are fetched one after another and each remote fetch had
    to fail first. So: the spider **needs its data beside it** to be an app of an offline-capable edition, exactly as
    the edition needs `keys.json` beside it. *Graph layer:* the spider's graphs are `receiver-graph-v1` node/edge JSON
    (tc@d09c185 spider/…v5…/spider/overview-graph.json:2); a node that names a repository, or a file at a commit, has a
    key on the wafer (a repository: its first commit's `k0`, which is Team 2's repository layer; a block: its element key
    from 7.3), and an edge between two placed nodes is a line on `o2` between their places, the galaxies-wafers
    `LineString` of keys (gw@fff6fc6 README.md:13-16). Baby step: two graphs copied into the edition folder with their
    sha256, `data/graphs/overview.json` (16 nodes, 15 edges, the front door) and `data/graphs/periodic-table.json`
    (stars@cbca125 blocks/graph.json: 663 nodes, 2,481 edges, MEASURED), drawn only between nodes that have keys; nodes
    without a key are counted in the readout and not drawn. The dashboard itself stays where it is and is opened by
    its row; the edition does not copy its UI.

7.5 **Licences in the registry, verified from files.** kuiper-belt code Apache-2.0 (kb@018b46a LICENSE:1-3), text and
    data CC BY 4.0 (editions/202611012027/README.md:64-67); See Through CERN-OHL-S v2 (kb@018b46a
    see-through/202610050609/NOTICE.md:3); globalgrid2050 surfaces CERN-OHL-S v2 (gg@c66759f LICENSE.txt:1); gridatlas
    Apache-2.0 (ga@5ec7f62 LICENSE:1-3); the spider Apache-2.0 under testcode's root licence (tc@d09c185 LICENSE:1-3,
    NOTICE:10-11; the spider folder has no licence file of its own); the periodic table: **`not stated`**, because
    neither el@f7a92fb nor stars@cbca125 tracks a LICENSE or NOTICE file (`git ls-files | grep -i licen` returns nothing
    in both; Team 2 found the same, nl@56958f2 FIXES/NL-010/team-2/EVIDENCE.md:292). The registry writes `not stated`
    and the launcher shows it; Team 5's licence register (step 9) carries the decision to the owner. No row is dropped
    for a missing licence; a missing fact is shown, not filled.

**Module.** `modules/07-apps.js`; `data/apps.json`, `data/elements.json`, `data/graphs/overview.json`,
`data/graphs/periodic-table.json`; `tools/apps_registry.py` and `tools/element_keys.py` (the `edition_keys.py` walk
applied to register files) at the kuiper-belt root in the release PR; entries in `modules.json` with sha256 (Team 5's
9.5); one paragraph in the edition README and the licence lines in NOTICE.md.

**Acceptance test on Android (Pixel 7 and a 360 px device, Playwright touch, served from the kuiper-belt root).**
A1 `data/apps.json` has 34 records; every record has non-empty `name`, `purpose`, `link`, `licence`, `source`,
`key_source`; the provenance rule holds: the 7 keys with `key_source: register` equal el@f7a92fb APPS.md:7-13 exactly,
the 25 with `key_source: homepage` equal the `data-entity-id` set of homepage_v134.html:32-56 exactly, and the only
`issued-here` keys are `spider-sandbox` and `periodic-table` (a script compares, not a reader).
A2 the bar is unchanged in width (no new title; `#bar .gm-title` count equals step 1's); File → "open an app" opens the
launcher panel under the bar; each row ≥ 44 px tall; the first row's header text is a key.
A3 tapping the See Through row navigates in the same tab to `../../see-through/` (HTTP 200, title "See Through");
`goBack()` returns to the edition with no panel open (the NL-009 journey, 06-seethrough.md:18-21).
A4 the periodic table layer: readout says "221 elements placed, 23 counted, not placed"; a tap within 9 px of an element
spark opens a card whose first line is the text at its key and whose second line is `block:<Sym>`;
`python tools/key.py <key>` on three sampled elements returns the recorded repository, commit and path.
A5 the spider row opens the dashboard; the graph layer draws 15 edges for the overview graph and the readout names how
many nodes of the periodic-table graph had no key; with `data/graphs/` removed the layer prints its error in the
readout and the wafer still draws (kb@018b46a editions/202611012027/index.html:631 is the pattern).
A6 offline: with every request to a host other than the served origin blocked, the launcher, both layers and the card
work; nothing in this step fetches off-origin at load.

**Licence note.** Everything this step copies into the edition is data (registry, element records, two graphs) under
CC BY 4.0 as the edition's data; the code is Apache-2.0; each row carries its target's own licence; the periodic
table's licence is `not stated` until the owner states it (7.5).

**Opus team brief (team 7 in Team 5's plan).** Four engineers: one writes `tools/apps_registry.py` and the 34-row
registry with A1 as its test; one writes `tools/element_keys.py` and `data/elements.json` (221 keys, 23 named) with A4;
one writes `modules/07-apps.js` (launcher panel, File entry, two layer records, card) against Team 2's registry probe
and Team 3's File hook, with A2, A3, A5; one owns the Android journey and the offline test A6 and the `handoff/07-apps/`
folder. Touch only the files named under Module. Never a bar title. Never a licence written from memory.

**Baby step 2 (not in this edition).** The apps answer back: each app of the family (See Through, Learn the Kuiper, the
spider, the periodic table) exposes a probe object like GridAtlas' `menuBar.inspect()` (nl@56958f2
FIXES/NL-010/team-2/EVIDENCE.md:49-50, :326) naming its stamp, its licence and the deep-link grammar it accepts; the
launcher reads the probe and shows `WAIT/LOAD/OK/FAIL` per row; and every app links back to the Kuiper at a key
(See Through's `window.KGModules` is the existing hook, team-2/EVIDENCE.md:281). Two-way links, still no windows.
**Baby step 3.** An app runs inside the edition as a cartridge under step 4's law (its own stamp, hash and hooks), and
its code is a per-app Kuiper (8a below). Only when two cartridges run at once does the question of a window manager
arise, and it is asked then, with measurements, not now.

---

## Step 8. The first intelligent algorithm: **the drift**

**Name.** *The drift of an edition from the live heads*, short name **drift**; module `modules/08-drift.js`, data
`data/drift.json`, tool `tools/drift.py`. The word is already the Kuiper's (kb@018b46a DRIFT.md:1-4, host
entanglement drift between GitHub and GitLab heads, reconciled under L10, LAWS.md:139); this step turns it from a
report about repositories into an algorithm about lines.

**The question it answers.** Every verified line of the edition is keyed to a commit (kb@018b46a
editions/202611012027/keys.json `commit`, `path`, `line`, `line_text`). The estate moves on: keys.json keys its 346
lines to 22 repositories (MEASURED, distinct `repo` values) and to commits that are not the heads: the gridatlas rows
alone are keyed to 13 distinct commits (`cacb69a7` among them, proof/keys-summary.json round trip 1) while gridatlas
main is `5ec7f62f`. Is what the edition says about a line
still true at the head? The algorithm answers per line, with a key, and never by plausibility.

**Why this one, of the four candidates.**
- *Nearest verified line to a tap* already exists: kb@018b46a editions/202611012027/index.html:685-690 picks the nearest
  spark within 9 px of a tap. It is a hit test on the screen, not an algorithm over the estate.
- *Pattern density per repository per period* is a picture of the edition's own data (`pattern` × `repo` × the wafer's
  time rings); it needs a period law first and it tells the owner nothing he cannot read in LINES. Second in line.
- *The descent from a spark to a substation* is Team 3's star player (step 5), and its law is See Through's.
- *The drift* is the first algorithm that makes an edition honest over time; it is the GridAtlas lesson of the hashed
  cartridge (a thing is admitted only when its bytes still hash to the record, ga@5ec7f62 atlas/current.json:5) applied
  to every verified line; its inputs are all keys; its refusal rule is the first law itself ("A check that examines
  nothing refuses. It does not pass", kb@018b46a README.md:40); it is what step 9's release gate needs before a
  pointer moves; and it is the algorithm that will run first on a per-app Kuiper (8a). It was prototyped today and it
  returned numbers (below).

**Inputs, with keys.**
1. `editions/<stamp>/keys.json` `bodies[]`: `id`, `repo`, `commit`, `path`, `line`, `line_text`, `key`
   (kb@018b46a editions/202611012027/keys.json; field list MEASURED from the file).
2. The head of each repository: `git rev-parse HEAD` of a clone, or `GET repos/Ventusltd/<repo>/commits/HEAD`; recorded
   as `heads{repo: sha}` with the time of observation and its offset (kb@018b46a README.md:39 "Every time carries its
   offset").
3. The file at the head: `git show <head>:<path>` (git objects, never the working tree).
4. For the moved-line search: the exact bytes of `line_text`, LF-normalised, the wafer's own text rule
   (kb@018b46a tools/count_lines.py:60-61).

**Output `data/drift.json`.** `{edition, cut_at, heads{repo: {sha, observed_at}}, rows[], summary}` where each row is
`{id, key, repo, path, line, edition_commit, head, class, head_line?, delta?}` and `class` is one of:
`SAME` (the text is at the same path and line at the head), `MOVED` (the same text is in the same file at another line;
first occurrence, `delta` = head_line − line), `GONE` (the file exists at the head and the text is not in it),
`FILE_GONE` (the path does not exist at the head), `UNVERIFIED` (no head was observed; nothing is claimed). `summary`
is the count per class and per repository, and the share `SAME / (rows − UNVERIFIED)` with its denominator printed.

**Refusal rule.** A repository whose head was not observed makes every one of its rows `UNVERIFIED`, never `SAME`:
the algorithm may not infer stability from the absence of a fetch (kb@018b46a README.md:40; tools/key.py:49 "Never
trusted blind"). A row whose `line_text` is empty, or whose `key` is not on the wafer (`on_wafer: false`, the two
star-maker lines), is `UNVERIFIED` with its reason. If the heads file is older than the cut by more than the cap the
edition README states, the whole run is refused and `drift.json` is not written: a stale drift is worse than none. The
page module draws nothing when `drift.json` is missing or its `edition` field is not the folder's stamp; it prints why
in the readout, in the engine's own idiom (kb@018b46a editions/202611012027/index.html:207 `REFUSED: …`, :240 `… did
not load. The wafer will not invent its keys.`, :631): `data/drift.json did not load. The wafer will not invent a
head.`; and the tool prints `REFUSED: no head recorded for <repo>; <n> lines UNVERIFIED` per repository it could not
observe, and `REFUSED: heads older than the cut by <h> h; drift.json not written` for the stale case.

**Where it runs.** `tools/drift.py` runs at cut time on the machine that cuts the edition (it needs git or the GitHub
API; the page must stay offline-capable), writes `data/drift.json` and is listed in `proof/edition-sha256.txt`; it is
re-run by `tools/ci_check.py`'s successor in Team 5's E-checks as "drift.json re-computed against the recorded heads is
byte-identical" (the heads are recorded, so the re-run is reproducible without a network when the clones are at those
heads). `modules/08-drift.js` only reads: it colours each verified spark by class, inside the palette (kb@018b46a
PALETTE.md:9-14, :20): `SAME` stays green (the record, lit), `MOVED` amber (attention: a boundary moved), `GONE` and
`FILE_GONE` an amber ring with no fill (attention, and nothing there), `UNVERIFIED` the dim grey-blue of a record not
yet measured; the card gains two lines: `at head <sha7>: SAME` or `MOVED to line N (+d)` or `GONE`, and the LINES
panel gains a filter by class. No new bar title.

**MEASURED today, as a prototype, not as the deliverable** (`/tmp/nl010/team-4/drift.py`, output `drift.json` there;
heads = the local clones at the heads listed at the top of this file, plus pipelinenews at
`2c0c8564532c` on `/home/user/pipelinenews`): 346 bodies → **333 SAME, 10 MOVED, 3 GONE, 0 FILE_GONE, 0 UNVERIFIED**
(all 22 repositories had a clone). The 3 GONE: ga@5ec7f62 `atlas/current.json` lines 14 and 576 (the pointer moved
the pointer now reads generation 202610292044, ga@5ec7f62 atlas/current.json:3; the quoted lines are no longer in it), kb@018b46a
`learn-the-kuiper/202610050144/NOTICE.md:6`. The 10 MOVED: 5 in data-grid-gb `datacentres/lanes/dc-a7-merge/dcmerge.py`
(+6 lines each: the NL-007 `_op_core` patch landed above them), 2 in gridatlas, 1 each in data-centres-gb,
globalgrid2050 (the diary line 89→90) and kuiper-belt. The prototype compares `line_text` (the text at the edition's
commit) and, where `line_text` is empty (6 bodies, MEASURED), falls back to `quote` (`drift.py:20`), which the
deliverable will not do: run strictly (`/tmp/nl010/team-4/drift_strict.py`, output `drift_strict.json`) the result is
**331 SAME, 7 MOVED, 2 GONE, 0 FILE_GONE, 6 UNVERIFIED (reason `empty line_text`)**, and those are the numbers the
rule above produces. Two of the MOVED rows, kuiper-belt README.md 33→34 and globalgrid2050 diary 89→90, are two of
the rows keys.json `quote_not_at_line` flags; they are genuine at head (`line_text` is found one line lower), not an
artefact of that flag. FABLE-T4B re-ran the first run byte-identical (REVIEW.md round 1); the strict numbers stand
once EVIDENCE.md keys them.

**How it is proven.** P1 determinism: two runs against the same recorded heads produce byte-identical `drift.json`.
P2 the refusal: with one clone removed, every row of that repository is `UNVERIFIED` and the summary's denominator
drops by exactly that count; with `heads` emptied, the tool exits non-zero and writes nothing. P3 ground truth: for
every `MOVED` row, `git show <head>:<path>` at `head_line` equals `line_text` byte for byte, and for every `SAME` row
the same at `line`; for every `GONE` row `git grep -F -- '<line_text>' <head> -- <path>` is empty. P4 on the page
(Android journey): the readout prints the five counts; a `MOVED` spark is amber; its card names the head and the new
line; with `data/drift.json` removed the wafer and the green sparks are unchanged and the readout says the drift did
not load. P5 the law: `drift.json` lists no repository that is not in `cosmos/repos.tsv` and no key not in `keys.json`.

**Module.** `tools/drift.py`, `modules/08-drift.js`, `data/drift.json`, the two card lines and the LINES filter, the
`modules.json` entry, a README paragraph "Drift since the cut" with the five counts and the heads.

**Acceptance test on Android.** P4 above on Pixel 7 and a 360 px device, touch; plus: tapping an amber spark opens
its card within 9 px (the existing hit test); the LINES filter "moved" lists exactly the `MOVED` rows; the bar stays
one row (step 1's budget untouched).

**Licence note.** `tools/drift.py` and `08-drift.js` Apache-2.0 as kuiper-belt code; `drift.json` CC BY 4.0 as edition
data; it quotes no line text beyond what `keys.json` already quotes, so it adds no licence.

**Opus team brief (team 8).** Four engineers: one writes `tools/drift.py` with P1–P3 and P5 as its test file; one writes
`modules/08-drift.js` (colours, card lines, filter) against Team 2's layer registry; one runs P4 on Android and owns
`handoff/08-drift/`; one writes the README paragraph and the E-check line for Team 5 and re-runs the tool against the
recorded heads on a second machine. Touch nothing outside these files. The colours are the palette's or the module is
refused.

**The beginning of the intelligent algorithms.** The drift is first because it is the one every later algorithm
needs: a pattern density that counts moved lines as present is wrong; a per-app Kuiper (8a) built from stale keys is
wrong; a release gate that cannot say "nothing drifted" cannot say "ship". Next in order, each with the same shape
(inputs with keys, a refusal rule, a tool that writes a JSON and a module that only reads it): pattern density per
repository per period (over the wafer's time rings); the descent from a spark to a substation (with Team 3, once See
Through's placement law is a module); the register drift (244 catalogued against 606 live blocks, 7.3), which is this
algorithm run over `block:` keys instead of line keys.

---

## Step 8a. Per-app Kuipers: a Kuiper drawn around one actual app (Addendum 1, Phase 2, gated on the owner's acceptance of steps 1–10)

**Goal.** A Kuiper whose address space is the code of one app and nothing else, so an algorithm (the drift first)
runs on that app's code alone, with the same law, and with a provable mapping between the app key and the
overarching key.

**Law.** The app's key space is the subset of the overarching wafer's issued keys whose address (kb@018b46a
editions/202611012027/index.html:282, `address(k)` → commit, repository, and through `tools/key.py` the path) lies in
the app's files. The app's files are: for a register app, its `files[]` at their commits (el@f7a92fb
catalogue/apps.json) **as the seed only**: the register never lists more than 8 files per block (FABLE-T4B's E8: max 8,
17 blocks at exactly 8, 139 at 1, and for `Ra`, `Sb`, `Pn` the `repos` field names repositories the `files` list does
not), so a register app's denominator is the folder set the tool measures from those seeds (the folders of the seed
files at their commits), printed, never the 8 files; for a folder app (See Through, Learn the Kuiper, the spider, an edition), every text blob under
its folder in every commit of its repository that is a row of `cosmos/wafer.tsv`. App keys are issued exactly as the wafer issues its own (kb@018b46a
editions/202611012027/index.html:202-205; tools/wafer_keys.py:10-11, :33-34): the app's commits in wafer order, and
per commit `app_k0 = previous app_k1 + gap_before` (600 keys per second of the gap since the app's previous commit,
capped at 14 days, left unissued) and `app_k1 = app_k0 + lines` (the app's text lines in that commit's tree); a line's
app key is `app_k0 + lines_before + (line − 1)`, the `edition_keys.py` walk restricted to the app's files. So an app's
Kuiper has rings that are its own nights, and "rank" holds only among issued app keys, never across the gaps. The placement law
is the wafer's, unchanged: `r = sqrt(key + 0.5), theta = 2π frac(key × 2654435769 / 2^32)` (kb@018b46a
editions/202611012027/index.html:278 as drawn; cosmos/wafer-meta.json:12 as declared).

**The mapping, written down and provable.** `data/app-keys/<id>.tsv`: rows `wafer_k0  app_k0  run_length  commit_sha12
path` plus one row per app commit `unix  lines  sha12  gap_before` (the app's own `wafer.tsv`) — one row per contiguous run of the app's lines inside one file at one commit (a file's lines are contiguous in
the wafer, README.md:28-35 of the edition). Both directions are a binary search over `wafer_k0` or `app_k0`. Proof:
for 12 sampled app keys, `app → wafer → tools/key.py` returns a path under the app's folder with the same text as
`git show <commit>:<path>` at the computed line; for 12 sampled wafer keys outside the app, `wafer → app` refuses.
The sums must close: Σ run_length = the app's issued keys = the number of app keys, printed, or the file is not written.

**MEASURED today (HEAD only, by the wafer's binary rule, `/tmp/nl010/team-4/app_sizes.py`), so the owner can see the
scale, not the per-app totals, which are UNMEASURED until the tool runs over every commit:** See Through
`see-through/202610050609` 27 files, 3,013 text lines; Learn the Kuiper `202610050609` 27 files (1 binary), 10,387;
Edition 4 folder 9 files (3 binary), 1,217; the spider v5 folder 4 files, 6,539; GridAtlas live shell
`atlas/releases/202608300453-atlas-v9` 23 files, 3,113; GridAtlas `atlas/cartridges` 165 files, 1,088,335 lines (the
61 stamped copies of the substation-intelligence cartridge alone, ga@5ec7f62 atlas/cartridges/, are most of it: a
per-app Kuiper of GridAtlas is dominated by its own history, which is the point of drawing it).

**GridAtlas lesson (with key).** A cartridge is admitted alone, by its own hash, and knows nothing of the others
(ga@5ec7f62 atlas/current.json:5, :14-21; kb@018b46a SPEC.md:3-5 "one small module, its own data, its own proof,
loaded on demand … it does not know about any other cartridge"): a per-app Kuiper is that cartridge idea applied to
an address space. **Opus team brief.** Phase 2: written after the owner's ACCEPT of steps 1–10; one team of four per
app, starting with See Through, owning `tools/app_keys.py` and `apps/<id>/`, with the round trips as the test.

**First algorithm on a per-app Kuiper.** The drift (step 8) over See Through's app keys: how many of its lines at the
edition's cut are `SAME` at `see-through/` head. Then the register drift of the periodic table.

**Module.** `tools/app_keys.py`, `data/app-keys/<id>.tsv`, `apps/<id>/index.html` = the engine with `SPACE`, `N` and
the commit texture built from the app's TSV instead of `cosmos/wafer.tsv` (the three load lines, kb@018b46a
editions/202611012027/index.html:201-208, are the only change), one per app row of `data/apps.json` that has a `wafer`
field. **Acceptance:** the sums close; 12+12 round trips; the Android journey on one per-app Kuiper. **Licence:** as
the app's repository; the TSVs CC BY 4.0.

## Step 8b. The overarching Kuiper that counts EVERYTHING (Addendum 1, Phase 2)

**What the live wafer counts today, exactly (every number keyed).**
- 98 repositories, 13,344 commits, 45,735,836,396 issued keys, 17,604,284,400 unissued, address space 63,340,120,796,
  silence share 0.2779, first commit 1748560273 (2025-05-29), last 1793539112 (2026-11-01): kb@018b46a
  cosmos/wafer-meta.json:2-10. `tools/ci_check.py` K2 re-sums `cosmos/wafer.tsv` and requires it to equal the meta
  file and `cosmos/repos.tsv` (:9, :53-60); re-summed today by `/tmp/nl010/team-4/` (python over the two TSVs): issued
  45,735,836,396, silent 17,604,284,400, commits 13,344, repositories 98, repos.tsv lines sum 45,735,836,396. MEASURED,
  equal.
- What an issued key is: "one per line in every file in every commit" (kb@018b46a tools/wafer_keys.py:10); a
  commit's `lines` are the lines of every text blob in its tree, so **a line that survives n commits holds n keys**,
  one per commit it stands in (keys.json `commit_lines_wafer` 5286 for a 72-line `.gitattributes` commit shows the
  whole tree is counted). This is the overarching count: it is not a count of distinct lines (8c is).
- Which commits: `git rev-list --all` of each public clone (kb@018b46a tools/count_lines.py:151; `log --all` at :122),
  so every ref the clone had at harvest, not only main; which repositories: the public ones of the account as the
  harvest asked GitHub (tools/harvest.py:7-9), with six private names redacted as `unnamed-01…06` in `cosmos/repos.tsv`
  (K1 privacy, tools/ci_check.py:8).
- The binary rule: a blob with a NUL byte in its first 8,000 bytes is binary, "counted as a blob, excluded from line
  totals" (tools/count_lines.py:14, :60-61; the same test in tools/key.py:40). A text blob's lines are newlines plus
  one if it does not end in a newline (:60).
- The silence rule: 600 unissued keys per second between consecutive commits, capped at 14 days
  (tools/wafer_keys.py:33-34).

**GridAtlas lesson (with key).** The register UI counts what it found and publishes the exact counts rather than a
summary (ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:34, :122-124, :157): EVERYTHING is a count with its
denominator printed, never a word. **Opus team brief.** Phase 2, after the owner's ACCEPT of 1–10: one team of four on
`tools/count_lines.py`, `cosmos/binaries.tsv`, `wafer-meta.json` and the K2 sums; the owner decides item 1 first.

**What EVERYTHING adds, each as a denominator the readout must print.**
1. Private repositories: today named by digest only; EVERYTHING counts their lines into the issued total under the same
   redaction (the count is public, the name is not), or states the exact number of repositories left out. Decision for
   the owner.
2. Binaries: today excluded from line totals. EVERYTHING names every binary blob with its byte size in a separate table
   `cosmos/binaries.tsv` (sha, bytes, repo, first commit) and places none of them on the line wafer; a second ring
   outside the rim, keyed by bytes, is a new substrate with a new name (gw@fff6fc6 wafer.mjs:40-43: "If a different
   arrangement is wanted, it is a new substrate with a new name beside this one, never an edit to this one").
3. Data and documents: already counted when they are text (TSV, JSON, Markdown); EVERYTHING states per repository how
   many of its keys are code, data and prose by extension, as a readout, not as a placement change.
4. Branches: already `--all`; EVERYTHING records per commit which refs reached it at harvest, so a count can be
   restricted to main on demand without re-harvesting.
5. The denominator rule: every count in the readout names its denominator — "of 45,735,836,396 issued", "of
   63,340,120,796 addresses", "of 98 repositories", "of 13,344 commits" — never a bare percentage.

**Module.** `tools/count_lines.py` gains `binaries.tsv` and the per-ref record; `cosmos/wafer-meta.json` gains the
counts of 1–4; `ci_check` K2 gains their sums. **Acceptance:** K2 PASS with the new sums; the readout prints the five
denominators on a phone. **Licence:** data CC BY 4.0.

## Step 8c. The unique-lines Kuiper, compared by measurement with the wafer that predates the Kuiper (Addendum 1, Phase 2)

**Definition of distinct.** A line is its exact bytes without its line terminator, with a CR before the LF removed
(LF-normalised) and nothing else trimmed. Why exact: the estate pins LF at the attribute layer (data-centres-gb
`.gitattributes:5`, quoted in kb@018b46a editions/202611012027/keys.json body 1: "Every digest in this repository is
taken over git blob content, which is LF"), so CRLF/LF is a transport difference, not a different line; indentation is
not, because a key must be invertible to the bytes at it (`tools/key.py` returns text that must equal the git line,
proof/keys-summary.json `text_eq_git_line`), and a trimmed key cannot be. The alternative (trimmed) merges more and is
stated here so it can be argued with.

**The wafer that predates the Kuiper (keyed).** gw@fff6fc6 README.md:5: "every permanently numbered line of the
estate placed by one frozen law, `r = sqrt(key)`, `theta = key x golden angle`"; the law in full, wafer.mjs:11-14,
frozen 2026-09-15T15:00:00Z (:44-49), inherited unchanged from gg@c66759f testcode/202609151339 (README.md:5 of gw;
gg README.md:9-15). Its keys are the numbered database: 250,174 distinct lines numbered 1 to 342,795, no duplicate
rows, 128,369 in a function family (gg@c66759f testcode/202609142202/data/all-lines.meta.json:10-16; the source
header, el@f7a92fb catalogue/provenance.json:42, "250,174 unique lines, numbered 1 to 342,795. Generated
2026-09-14T19:56:58.242Z by the modular star"). Extent sqrt(342,795) ≈ 585.5 units. Between it and the live wafer sat
the one-wafer of 19 September: 19,257 bodies (one per distinct blob SHA) from 66 repositories, drawn with the 250,174
numbered lines, 245,170 placed (kb@018b46a NEXT.md:8-13).

**The live wafer against it.** Law: golden angle `theta = key × 2.39996…` (gw) against `theta = 2π frac(key ×
2654435769 / 2^32)` (kb@018b46a cosmos/wafer-meta.json:12, the Knuth multiplier, editions/202611012027/NOTICE.md:12-14): same `r = sqrt(key)`,
different angle, so **no key lands in the same place on the two wafers**, which is why they are two substrates and not
one. Key ranges: 1…342,795 against 0…63,340,120,795. Count: 250,174 distinct lines against 45,735,836,396 line
occurrences, a ratio of about 1.8 × 10⁵, which is the expected effect of counting every line in every commit.
Silence: 92,621 never-issued numbers of 342,795 (27.0 %, from all-lines.meta.json:10 and :14) against 17,604,284,400
of 63,340,120,796 (27.79 %, wafer-meta.json:5). Radius: `sqrt(key)` against `sqrt(key + 0.5)` (gw wafer.mjs:11,
kb index.html:278). The two keys do not share a space: a pre-Kuiper key is one distinct numbered line of a snapshot,
a Kuiper key is one line of one blob in one commit (kb@018b46a tools/key.py:8-9); so "what moved" is **a change of
unit, not a renumbering**, and the comparison file must say so in its first line.

**GridAtlas lesson (with key).** A basemap is never redrawn to suit a layer; a different arrangement is a new
substrate beside the old one (gw@fff6fc6 wafer.mjs:3-7, :40-43, GridAtlas' Carto basemap as the precedent): the
unique-lines wafer is a second substrate with a second name, compared, never merged. **Opus team brief.** Phase 2,
after the owner's ACCEPT of 1–10: one team of four on `tools/unique_lines.py`, `cosmos/unique.tsv`, `unique.html` and
`proof/unique-vs-numbered.json`, run on the harvest machine, with K2u as the test.

**The unique-lines Kuiper.** `tools/unique_lines.py` walks every text blob of every commit the wafer holds (the same
`rev-list --all` set), hashes each LF-normalised line, and issues one key per distinct line in the order of its
**first** appearance in wafer order (so radius is still time: the time the line was first written); silence by the
same 600/s rule between first appearances. Output `cosmos/unique.tsv` (one row per commit: unix, new_distinct_lines,
repo_index, sha12, gap_before) and `cosmos/unique-meta.json` with `distinct_lines`, `occurrences` (= the wafer's
issued), the ratio, and the rule. The same engine draws it from the second TSV. **The comparison, measured, in
`proof/unique-vs-numbered.json`:** (i) how many of the 250,174 numbered lines appear among the distinct lines (the
numbered database's lines were taken from 66 repositories on 14 September; a line can be absent only if its repository
is not public or its text was normalised differently, and each absence is listed with its number); (ii) the first-key
of each in both spaces; (iii) the law constants side by side; (iv) what moved and why: every numbered line's place on
the old wafer and on the unique wafer, with the reason "different angle law" or "different key".

**MEASURED today as a lower-bound prototype, HEAD only, 25 local clones, not the wafer's 98 repositories and not all
commits (`/tmp/nl010/team-4/unique_lines.py`, output `unique_lines.json`):** the run is **partial**: 8 of 25 repositories done
when this revision was written (it stalls on globalgrid2050's tree), the per-repository rows as they stand are in
"Measurements appended" below, copied from `/tmp/nl010/team-4/unique_lines.log`; no total is claimed; FABLE-T4B's
re-run (`unique_lines.rerun.log`) will be keyed in EVIDENCE.md E11 if it completes. The number the owner asked for, distinct lines across all
commits of all 98 repositories, is UNMEASURED until the tool runs on the harvest machine.

**Module.** `tools/unique_lines.py`, `cosmos/unique.tsv`, `cosmos/unique-meta.json`, `proof/unique-vs-numbered.json`,
a `unique.html` at the kuiper-belt root (the engine reading the second TSV), one ci_check line "K2u: unique.tsv
re-sums to unique-meta.json and distinct ≤ issued". **Acceptance:** K2u PASS; (i)–(iv) written with keys; on a phone
the readout says "N distinct lines of M occurrences, first written between <date> and <date>". **Licence:** CC BY 4.0
data; the pre-Kuiper wafer's code is gw@fff6fc6 with no LICENSE file (same finding as the elements: `git ls-files`
shows none), disclosed to Team 5.

---

## Limits of this file

- The 34-row registry, the 221/23 element placement, the spider's 24/21 request count, the drift's 331/7/2/6 (strict) and
  333/10/3 (with the quote fallback) and the HEAD line counts were measured on this machine against the heads at the top; FABLE-T4B re-runs them, and only the
  keyed re-run counts. None of them is a number about the live GitHub Pages site, which this sandbox cannot fetch.
- Served addresses for the spider and the periodic table are not recorded in el@f7a92fb SURFACES.md; the registry
  carries GitHub links until a surface is keyed.
- The drift prototype treats the local clones as "the live heads"; the deliverable records heads with an observation
  time and refuses when none is recorded.
- 8a–8c are Phase 2, gated on the owner's acceptance of steps 1–10 (BRIEF.md Addendum 1); their counts marked
  UNMEASURED are left so, by the law.

## Measurements appended

Partial output of `/tmp/nl010/team-4/unique_lines.py` (HEAD of the local clones, by the wafer's binary rule; distinct =
exact LF-normalised bytes within that repository). 8 of 25 repositories done; the remaining 17 (globalgrid2050,
grid-distance-maths, gridatlas, gridmachine1, kuiper-belt, kuiper-drawing-engine, kuiper-ship, maths,
particle-physics-drawing-engine, star-maker, stars, substations, testcode, time-stone, trillion-loop, ventus-grid-engine,
worlds-) are UNMEASURED here. No estate-wide distinct count is claimed from this table.

| repository | head | files | binary | text lines | distinct lines | distinct / lines |
|---|---|---|---|---|---|---|
| code-generator | `857ea8124484` | 59 | 0 | 43,201 | 17,045 | 0.395 |
| cvaa | `877bf380202b` | 77 | 0 | 8,846 | 5,183 | 0.586 |
| data-centres-gb | `f9f47286fae6` | 33 | 0 | 5,286 | 3,442 | 0.651 |
| data-grid-gb | `75ab8ae54e95` | 102 | 0 | 364,592 | 90,702 | 0.249 |
| data-gridatlas | `8bf88da9e210` | 133 | 65 | 24,140 | 9,081 | 0.376 |
| elements | `f7a92fb085c3` | 25 | 0 | 129,931 | 39,177 | 0.302 |
| energy-transition-simulator | `a6b5ae63cc0e` | 156 | 38 | 27,537 | 23,314 | 0.847 |
| galaxies-wafers | `fff6fc6ad4f9` | 735 | 0 | 114,966 | 27,849 | 0.242 |

The row for `elements` (129,931 lines, 39,177 distinct) is the catalogue's own JSON and Markdown, where the same line
recurs across `ELEMENTS.md`, `catalogue/*.json` and `inputs/`; `data-grid-gb` (364,592 lines, 90,702 distinct) is data.
Both are what 8c's per-repository code/data/prose readout (8b item 3) exists to separate.
