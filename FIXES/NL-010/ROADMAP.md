# NL-010 ROADMAP: the ten steps that bring the GridAtlas lessons into the Kuiper

Consolidated by FABLE-T5B (team 5, evidence officer) from the five teams' STEPS.md and EVIDENCE.md under
`FIXES/NL-010/team-1..5/`. Channel: https://github.com/Ventusltd/neural-link-between-agents/issues/10. Owner: Vikram
Kumar, Ventus Ltd. Heads every key is written against: gridatlas `5ec7f62f213e2d20a02e86427daa182c0f38e4a4`, kuiper-belt
`018b46aed50f28f7b1882a0dcaba6593ce522beb`, elements `f7a92fb085c38dcbbd5cb469a66cd5ca61fb95bf`, testcode
`d09c185c8dacbc5c73afb2b0d0d8dad40745a544`, globalgrid2050 `c66759f0d7ac3489df9158da6eaa1330a37c069f`, galaxies-wafers
`fff6fc6ad4f93a15fe8f6456942a1b44e5547105`. `repo@sha path:line` is the key; a short sha means that head. All five teams' STEPS.md read `REVIEW: PASS` on line 1
when this file was assembled (21:32 UTC); each team's EVIDENCE.md and REVIEW.md sit beside its STEPS.md.

## Preface: the owner's words and the law

The owner's instruction of 1 Nov 2026, binding (FIXES/NL-010/BRIEF.md:5-11): "establish a fable x 10 agents (teams of 2
so 5 teams) the 10 steps road map governing lessons from gridatlas into Kuiper ref layer management and file menu etc.
Further I want see through to be the star player. I want the ventus logo exactly like gridatlas on the top of Kuiper.
This is just the beginning of the intelligent algorithms. Also bring in periodic table and spider sandbox. Turn the
kuiper into the OS of the estate in baby steps. Further the line code is the header have that clearly written. The
labels and commands must be like the gridatlas not near the top copy the gridatlas UI keep it consistent and build it
around the kuiper. Use 40 opus agents, teams of 4."

Addendum 1 (BRIEF.md:72-74), conditional on the roadmap passing: "If passed then Kuiper paradigms (Kuiper drawn around
actual apps so we can run algorithms on the code of various apps) and of course an overarching Kuiper that counts
EVERYTHING. And have a unique lines Kuiper separately and compare it to the wafer that predates the Kuiper."

The law this roadmap is written under:

1. No claim without a key. Every number, every GridAtlas lesson and every Kuiper hook below carries `repo@sha path:line`
   (harness notes, "Mission so far", item 1; kuiper-belt@018b46a LAWS.md:3-4 "A law that cannot be falsified is not a
   law"). Where a file does not exist, the gap is written `DISCLOSED` (LAWS.md:157), never filled in.
2. The line of code is the header. Every card the Kuiper shows for a keyed line opens with the line itself, verbatim;
   the key follows; the names come after. Written in the page, the README and LAWS.md (step 2).
3. See Through is the star player: the first and largest entry of the shell, reachable in one tap from every edition,
   the descent from the wafer's stars to one substation, a deep link in and out (step 5).
4. The Kuiper becomes the OS of the estate in baby steps: a launcher that opens one app at a time and returns to the
   wafer, no window manager (steps 7-8); the first intelligent algorithm runs over keys and refuses without them.
5. The GridAtlas UI is copied, not imitated: the bar, the Ventus wordmark, the six menus, the layer grammar and the
   release law are measured from the live shell at gridatlas@5ec7f62 and built around the wafer (steps 1, 3, 4, 9).
6. Editions ship by the folder rule: a new dated folder, a pointer that moves in three places, `ci_check` PASS, the
   Android journey PASS, the owner's `ACCEPT <stamp>` before the pointer moves; agents never post ACCEPT (step 9).

Each step below has the same eight fields: goal; GridAtlas lesson with key; Kuiper change; module name; files touched;
acceptance test on Android; licence note; Opus team brief. Where two teams disagreed, both are cited and the choice is
given with its reason, in the "Resolved between teams" section before the Opus table.
## Phase 1: the ten steps

### Step 1. The shell contract: the GridAtlas bar, the Ventus wordmark and the six menus, built around the wafer (team 1)

**Goal.** The next edition opens under the same shell as the live GridAtlas: one 36 px bar (34 px on a phone) across
the top of the instrument, the VENTUS wordmark fused into its centre exactly as GridAtlas renders it, three titles left
and three right in GridAtlas's face, colour and spacing, every panel closed at rest and dropped from its title, every
label and command inside a panel row and nothing floating over the wafer, one row on a 360 px Android phone. "Exactly as
GridAtlas" is defined by team 1's measured table (team-1/STEPS.md:32-82), not by resemblance.

**GridAtlas lesson (with key).** The bar is one 36 px strip, `rgba(4,10,13,.95)`, 1 px `rgba(80,220,240,.3)` rule, mono
11 px, titles uppercase `.05em` `#cfeef6` (gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:167-181); the six
menus `['File', 'Edit', 'View', 'Scope', 'Grid', 'About']` (menu-bar.js:31); the VENTUS masthead fused into the centre of
the same strip "rather than a second row, so it costs no map height on a phone" and "the hero of this strip" (menu-bar.js:
184-191; the live cartridge atlas/cartridges/202609062358-substation-intelligence-v9-63.js:4533-4553, admitted by
atlas/current.json:566-573, sha256 `d94b0de5…`); `.gm-brand-slot` max-width 64 %, `.ventus-main` 14 px weight 800
letter-spacing .2em `#fff`, `.ventus-sub` 5.5 px (menu-bar.js:192-205), phone 11 px / 4.5 px (:377-378). The wordmark is
text, not an image: `.scada-brand-main` "Ventus", `.scada-brand-sub` "Cables &amp; Connectivity&reg;"
(atlas/releases/202608300453-atlas-v9/index.html:113-118); no logo file exists in gridatlas (`find -iname "*logo*"`
empty outside node_modules). The admission rule: install nothing until the 63 controls are present and unique, leave
the old interface reachable and publish the failure (menu-bar.js:8-17, :34, :157).

**Kuiper change.** A shell module replaces Edition 4's `#bar` and `#keys` strip (editions/202611012027/index.html:699-
703); the wafer engine and its placement law are untouched. Team 1's contract C1–C10 (team-1/STEPS.md:115-199): the
brand slot holds `div.hud-header > div.ventus-brand > div.ventus-main` "Ventus" + `div.ventus-sub` "Cables &
Connectivity®" with GridAtlas's classes and CSS copied verbatim, centred, not a link (C3); titles are
`button.gm-title[aria-haspopup=menu]`, 44 px hit box on a coarse pointer by an invisible `::after` so the visible strip
stays 34 px (C4); the six names mapped (C5): FILE → FILE (open a key, an edition, an app, copy a link: step 6); EDIT →
EDIT (the find box `/`, the LINES filter, clear the selection); VIEW → VIEW (readout, whole wafer, `r`, `n`, `e`/`E`,
reduced motion); SCOPE → SCOPE (the focus: all / gridatlas + data centres / one repository / one period / one commit);
GRID → WAFER (the layer registry, step 3); ABOUT → ABOUT (the edition's name and stamp, the laws, the licences, the
estate links). The star slot, one width rule fixed by the shell so step 5 chooses the content within it: at `min-width:381px` the
star entry is the seventh title, first in the left group before FILE, `a.gm-title[href="../../see-through/"]` in the
same face (the six titles and the slot measure 302 px, so the slack is 79 px at 381, 91 at 393, 110 at 412, against the
72 px the entry needs); at `max-width:380px` it leaves the bar and takes the bottom-left 44 px strip that GridAtlas
itself gives its two most-used controls on a phone (the GRID/SUBS chips, `chipStaysOnMap :1521-1552`, 65.7×44 px at
360 px), same face, same colours; step 5 may change the words and the target, not the rule; one row at 360 px is never
traded (team-1/STEPS.md:156-161). Every
command is a 44 px row inside a panel; at rest nothing is drawn over the wafer but the bar; `safeBox()` starts under
the bar (Edition 4 :726) and `edFly` is unchanged (C6). Panels at `top:100%`, one open at a time, closed by the same
title, Escape, a wafer tap and the Android back gesture via `history.pushState` (C7). The shell is a cartridge in step
4's sense: it installs nothing until `#c`, `#o`, `#top`, `#hud`, `#foot`, `#keys`, `#lines`, `#card`, `safeBox`,
`draw`, `edCard`, `edFly`, `edNext`, `setPanel` exist and are unique, and a missing hook writes
`#kuiper-menu-bar-failure` (`role=alert`) and leaves Edition 4's bar reachable (C8). One row at 360, 393, 412 and 430 px
and in landscape (C9). The contract is written at the head of the module with its keys and the date measured (C10).

**Module name.** `editions/<stamp>/modules/<module-stamp>-kuiper-shell.js`, schema `kuiper.menu-bar.v1`, probe
`window.__KUIPER_MODULES__.menuBar` = `{schema, installed, controls_moved, failure, panel_counts}`.

**Files touched.** The module; one script tag in `editions/<stamp>/index.html` and the removal of the Edition 4 bar block
(`:693-726`, team-1/STEPS.md:200-207) once the module has installed; `proof/accept-shell.cjs` and its JSON output. Nothing in `cosmos/`,
`keys.json`, `tools/key.py` or the placement law.

**Acceptance test on Android.** `proof/accept-shell.cjs`, Playwright Chromium with the harness flags, `devices['Pixel 7']`,
Galaxy S24 (360×780), Pixel 7 at 393 and 430 px, Pixel 7 landscape, 1280×800; served from the kuiper-belt root; 8 s
settle. A1 `#kuiper-menu-bar` at `y=0`, full width, height 34/36, `installed:true`, `failure:null`. A2 six `.gm-title`
(plus the star entry if step 5 makes it a title) FILE EDIT VIEW SCOPE WAFER ABOUT on one rounded `y`,
`scrollWidth === clientWidth` at 360. A3 the wordmark's computed style (11/14 px, 800, `rgb(255,255,255)`, uppercase;
sub 4.5/5.5 px `rgb(136,136,136)`), centred within 1 px, `closest('a')` null, box within 1 px of GridAtlas's measured
box (73.6×16.3 on Pixel 7 and at 360 px; 90.0×20.5 at 1280×800). A4 at rest only `#c`, `#o` (and after a pick `#card`)
have a client rect over the wafer. A5 every panel row ≥ 44 px; tap opens one panel under the bar, second tap, Escape and
`goBack()` close it; "next verified line" lands the spark between the bar and the card. A6 `elementFromPoint(x, 40)` is
the title on a coarse pointer. A7 zero `pageerror`, zero console errors, `node --check` of the module. A8 with `#keys`
removed before load: `installed:false`, the failure strip names `#keys`, Edition 4's bar still clickable. A9 the same
script against GridAtlas at `/atlas/` prints the same table for `#gridatlas-menu-bar`, so the two shells are compared
number to number in one run (team-1/STEPS.md:209-236).

**Licence note.** GridAtlas is Apache-2.0 (gridatlas@5ec7f62 LICENSE:1-4, NOTICE:1-12); the CSS values and the menu
module's structure copied into the Kuiper carry GridAtlas's NOTICE line in the module header and the edition's
`NOTICE.md` (Apache-2.0 §4(d)). "Ventus" and "Cables & Connectivity®" are the owner's mark: Apache-2.0 §6 grants no
trademark right (LICENSE:139), so the mark is used by the owner's instruction of 1 Nov 2026, and `NOTICE.md` says so
(team-5/STEPS.md register row "the Ventus logo"). No third-party asset is added.

**Opus team brief (team 1).** Build `<module-stamp>-kuiper-shell.js` to C1–C10; do not edit the engine above the
Edition 2 marker (`index.html:620`) or any file under `cosmos/`; copy every CSS value from the keys in this step and
cite the key beside it; run A1–A9 on the six viewports and paste the numbers into the edition README under "The shell,
measured"; FAIL loudly on any missing hook; do not decide the star slot (team 5 of the Opus plan, Fable team 3) or the
WAFER rows (Opus team 3, Fable team 2): leave a named, empty group for each with its owner's schema name; hand the
measured widths at 360 px to the layer and See Through teams on issue #10 before they add rows or titles.

### Step 2. The card law: the line of code is the header (team 1)

**Goal.** Every card the Kuiper shows for a keyed line opens with the line of code itself, verbatim, as its header; the
key follows; every human name for the line comes after. The law is written in three places with one wording: the page,
the edition README, and `LAWS.md` as law L11.

**GridAtlas lesson (with key).** GridAtlas's menu shows the engine's own live text, WAIT/LOAD/OK/FAIL suffix included,
never a cleaned label, because a stripped label made a success and a failure indistinguishable on a phone
(gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:92-100). The Kuiper's own first law: a statement with a key is a
fact, without one a candidate (kuiper-belt@018b46a README.md:29-40). Measured in Edition 4's `keys.json`: all 344 placed
bodies carry `line_text` (the bytes at the key, `tools/edition_keys.py:251`); the register's `quote`, which the card
shows today (`index.html:661`), equals `line_text` byte for byte for 128 of 340 non-empty lines and differs for 212
(team-1/STEPS.md:261-273). The law makes it 344 of 344.

**Kuiper change.** K1 the card (`#card`, Edition 4 `index.html:655-666`) is rebuilt in this order and no other: row 1
the header `<header class="ch"><code>` = `line_text` escaped, `white-space:pre-wrap`, mono, `#fff`, 600; row 2 the key
`repo@commit path:line`; then the names. K0 `keys.json` unchanged; a body without `line_text` (the two star-maker
bodies, never placed) refuses with "no text at key". K2 `aria-label` = the header, `aria-live=polite`. K3 the sentence in
the page (ABOUT panel, first paragraph): "The line of code is the header. Every card opens with the line itself,
verbatim from the key; the key is the second row; every name a person gave the line comes after." K4 the edition
README section "The card law" with the same sentence, one rendered example and the falsification test. K5 `LAWS.md`
L11 after L10 (LAWS.md:139), in the file's own form, with "Falsified by: a card whose first visible row differs from the
text at its key; a card that shows a line without its key on the next row; or a quote shown as the header when the
quote is not the line at the key." K6 the LINES rows (`fillLines`, `:737-744`) follow the same order
(team-1/STEPS.md:274-311).

**Module name.** `editions/<stamp>/modules/<module-stamp>-line-card.js`, schema `kuiper.card.v1`, wrapping `edCard` and
`fillLines` through the hook table of step 4.

**Files touched.** The module; one script tag in `index.html`; the edition `README.md` (the section); root `LAWS.md`
(L11, carried as `handoff/02-card/LAWS-L11.patch` into PR B, never edited on the edition branch: team-5/STEPS.md step
10); `NOTICE.md` (nothing new to license). `keys.json` stays byte-identical to Edition 2's.

**Acceptance test on Android.** `proof/accept-card.cjs`: Pixel 7 and 360×780, touch; after `touchscreen.tap` on a spark,
on a LINES row and on `e`: B1 the card's first visible text node equals `bodies[i].line_text` byte for byte for all 344
placed bodies (scripted over every body); B2 the second row is the key; B3 the card is capped as Edition 4 caps it
(34 % on a phone, editions/202611012027/README.md:16-19) and the spark stays in the clear space after `edFly`; B4 the
sentence of K3 is in the ABOUT panel, the README and the LAWS patch, identical (diff empty); B5 a body without
`line_text` shows "no text at key"; B6 LINES rows read text, key, title in that order; B7 zero page errors and `tools/ci_check.py` `RESULT: PASS`
(team-1/STEPS.md:316-332).

**Licence note.** The quoted lines keep their repositories' licences as Edition 4's `NOTICE.md:7-10` states (Apache-2.0,
CERN-OHL-S v2, CC BY 4.0, ODbL 1.0, OGL v3); "A quote here is a citation with its key, not a relicensing." The module
is Apache-2.0 kuiper-belt code; L11's text is CC BY 4.0.

**Opus team brief (team 2).** Build `<module-stamp>-line-card.js` to K0–K6 against step 4's hook table; write the
LAWS-L11 patch and the README paragraph with the one wording; prove B1–B7 on both devices, scripted over all 344
bodies; hand the three wordings to the evidence officer, who confirms them identical before the hand-off.

### Step 3. The Kuiper layer registry: reference layers as records, one original, proxied everywhere (team 2)

**Goal.** One registry, `data/layers.json` plus the layers module, holds every reference layer of the wafer as a record
with a key, a label, a group, a colour with a stated meaning, an order, a source with a sha256, a licence and a live
state; one panel under the WAFER title shows one row per layer with an on/off control that is the only original; every
other surface (keys, readout, URL, File menu, the apps) proxies that original; a layer whose data is missing, wrong or
unlicensed is listed and says why, draws nothing, and the wafer underneath keeps drawing. The first seven layers:
verified lines, repositories, periods, editions, See Through stars, elements, spider graphs.

**GridAtlas lesson (with key).** A layer is a record, not a code path: the shell declares 60 layers as data (`ukConfig`,
11 groups, 60 ids, gridatlas@5ec7f62 atlas/releases/202608300453-atlas-v9/index.html:142-264); the Grid menu drives the
SAME 63 original inputs through proxies that mirror checked, disabled and label (menu-bar.js:12, :34, :421-426, :1442);
the label carries the live state WAIT/LOAD/OK/FAIL (menu-bar.js:92-100); the inventory must be complete or the module
publishes the failure (:122-124, :157). galaxies-wafers inherited the same states from GridAtlas
(galaxies-wafers@fff6fc6 README.md:7) and its builder "refuses to write a key the numbered database does not contain"
(README.md:18). Full key list: team-2/EVIDENCE.md A1–A3, B1–B6.

**Kuiper change.** The registry record schema `layer:<id>` with id, label, group, colour (PALETTE.md), order, source
{path, sha256, bytes, features}, licence, state {WAIT, LOAD, OK, EMPTY, FAIL, REFUSED} and `why`; the verified-lines
layer's draw, card, list, filter and `e`/`E` move out of the page (`index.html:626-692, :705-709, :728-749`) into the
module; `lyOn`/`lyFocus`/`lyQuery` stop being bare lets: the registry is the original and the bar proxies it; the
registry owns one wrap of `draw` through `KY.draw.add` in registry order (the Kuiper's `cartridge_order`); a layer's
data loads only after the wafer admitted its own (`index.html:201-240`), a failed load is printed in the row, the
heading and `#refuse[role=alert]`; a body enters a layer only by the admission predicate (verified, keyed, inside
`SPACE`, placed by `keyPlace`); the ticked layers are written to the URL with `history.replaceState` as team 2's `layers` parameter, carried in the
hash grammar of step 6 (R3) (team-2/STEPS.md:99-239). The see-through, elements and spider rows are present from day one with `EMPTY` or `REFUSED` and a
non-empty `why` until steps 5 and 7 fill them; the see-through row is the first of THE APPS and the largest label.

**Module name.** `editions/<stamp>/modules/<module-stamp>-layers.js` (id `layers`, provides `layers`, requires
`keyPlace, address, o2, card, flyTo, safeBox, panels, draw, redraw, lit`).

**Files touched.** The module; `editions/<stamp>/data/layers.json`, `data/editions.json`; `tools/build_layers.py` (writes
`bytes`, `features`, `sha256`, refuses a key outside `SPACE` or a colour outside PALETTE.md); `index.html` only to
delete what was moved; `tools/edition_check.py` E2/E6 extended to `data/*.json` hashes.

**Acceptance test on Android.** Pixel 7 and Galaxy S24, touch, harness flags, served from the root: 1 `KY.layers.inspect()`
→ `layers: 7, unique: 7, complete: true`, 7 `input[data-ky-layer]`, no `[data-layer-id]`; 2 the WAFER panel opens under
the bar, rows ≥ 44 px, the `lines` row reads `OK · 344 of 346`; 3 a tap on the row turns the layer off (overlay pixel at
`edScreen(edPlaced[0])` no longer green) and on again; 4 `keys.json` as 404 → row `FAIL · keys.json HTTP 404`,
`#refuse[role=alert]` visible, wafer still drawn, `pageerror` 0, `e` does not fly; 5 one byte changed in `keys.json` →
`FAIL · sha256 mismatch`, zero sparks; 6 a link with `layers=lines,periods` round-trips through `history.replaceState` and through the pointer; 7
`KY.layers.set('repos', true)` after `/gridatlas` keeps `?selftest=repo:gridatlas` PASS; 8 the see-through, elements and
spider rows show `EMPTY`/`REFUSED` with a `why`, see-through first and largest; 9 `ci_check.py` PASS, `node --check`
on the module, every `data/*.json` hashes to its record; test 6 opens through the pointer `editions/`, not only the
dated folder (team-2/STEPS.md:248-287).

**Licence note.** The module Apache-2.0, `layers.json`/`editions.json` CC BY 4.0 (kuiper-belt@018b46a README.md:156-157);
each record carries its own `licence`, verified by step 9's register; a record with an unsettled licence is listed
`REFUSED · licence unsettled` and places nothing (elements, until the owner settles Q1); See Through's row names
CERN-OHL-S v2 and ODbL; the spider's names Apache-2.0 and the licences of the graphs it draws.

**Opus team brief (team 3).** Own the module, `layers.json`, `editions.json`, `tools/build_layers.py`, and the move of
the verified-lines code from the page into the module, keeping every behaviour NL-009 patched; touch `index.html` only
to delete what you moved; file a REQUEST on #10 for any hook the table lacks; do not touch `keys.json`, `cosmos/`, the
placement law, the bar's titles, the link grammar beyond `?layers=`, or any app's data; prove tests 1–9 on both
devices with screenshots of WAIT, OK, FAIL and REFUSED; your `requires` list is exactly the hooks you call.

### Step 4. The Kuiper cartridge: a stamped, hashed module admitted only when its hooks exist (team 2)

**Goal.** Every feature the Opus teams build is one stamped file under `editions/<stamp>/modules/`, listed with its
sha256 in `editions/<stamp>/modules.json`, admitted by the page in manifest order only after its bytes hash as recorded
and every hook it requires exists, isolated in its own script element, registering itself through one call, and refused
in words (readout and alert) for a missing file, a hash mismatch, a stamp mismatch, a missing hook, no registration or
an install that throws. The page without any module is a whole, working wafer.

**GridAtlas lesson (with key).** The composer fetches `current.json` with `cache: 'no-store'`, checks schema and
architecture (gridatlas@5ec7f62 atlas/index.html:39-44), composes in `cartridge_order`, refuses a missing id (:65-67),
hashes the fetched bytes in the browser and refuses a mismatch (:78-81), injects a blob-URL script per cartridge
(:82-83), publishes `window.__GRIDATLAS_ATLAS__` (:104-114), and on any failure shows one screen "The immutable shell
was not changed" (:32-36). The record carries `id, generation, version, type, slot, path, sha256, contract,
capabilities` (atlas/current.json:24-41), later `reads_at_runtime`, `writes`, `isolation` (:650-660). A late module
installs nothing until its dependencies exist and publishes a loud failure after a bounded retry (menu-bar.js:35,
:1647-1656, :1752-1768); the lightning overlay publishes one frozen API under one namespace
(atlas/modules/202610291043-uk-lightning-overlay.js:7-8, :393-400). A cartridge is a new timestamped file beside the
previous one, never rewritten (atlas/cartridges/README.md:3-7; tools/build-cartridge.mjs:1-14). The PR gate re-hashes
every cartridge (tools/ci/pr-gate.mjs:170-179) and the release re-hashes before the pointer moves (docs/RELEASE.md:117).
The boundary: "One module, one responsibility, one proof, one public surface"
(governance/202609011940-modular-architecture-and-domain-map.md:26-49). The anti-lesson in the Kuiper's own family:
Learn the Kuiper skips a missing module silently (`onerror="this.remove()"`,
kuiper-belt@018b46a learn-the-kuiper/202610050609/modes.html:16-24); the edition does the opposite. FINDING carried:
the live substation-intelligence cartridge's header says generation `202609060259` while its file name and
`current.json` say `202609062358` (team-2/EVIDENCE.md A4.32-A4.33); a stamp written twice drifts, so the Kuiper writes it
once in the file name and once in the registration and refuses when they differ.

**Kuiper change.** 4.1 The edition layer today reaches the engine by wrapping its functions and writing its module-level
variables (`index.html:620-749`); a separate file cannot, so the hook table is the precondition of modules. 4.2
`window.KY`, built by the page after the engine's definitions, frozen: `schema 'kuiper.hooks.v1'`, `hooks` (`keyPlace`
:278, `address` :282, `describe` :284, `findBy` :280, `flyTo` :253, `home` :277, `homeCamera` :272, `safeBox` :262,
`lightTime` :554, `showNew` :420, `goKey` :416, `fmt`/`words` :126, `esc` :681, `cv`/`ov`/`o2` :121, `hud`/`big`/`sub`
:123, `card`, `gbox`/`gin` :604, `SPACE`, `N`, `repos`, `commits`), `cam`, `lit`, `sel`, `redraw()`, `draw.add(fn, order)`
(the one wrap of `draw`), `panels.add/set/place` (`setPanel` :714, `placePanels` :712), `register(module)`, `modules`,
`inspect()`. 4.3 The file `modules/<module-stamp>-<name>.js`: a classic script in one IIFE, first line
`/* kuiper module <name>, generation <module-stamp> (UTC), <licence> */`, never edited after publication, carried
byte-identical across editions as GridAtlas carries a cartridge of `202609241251` in generation `202610292044`
(atlas/current.json:3, :25). 4.4 `KY.register({schema:'kuiper.module.v1', id, generation, requires, provides,
install(KY), inspect()})` records against `KY.admitting`; the loader checks id, stamp, `requires` ⊆ hooks ∪ earlier
`provides`, calls `install` in `try`, freezes `KY.modules[id]`, prints `<id> admitted · <sha256 first 12>`. 4.5
`modules.json` = `{schema 'kuiper.modules.v1', edition, hooks, order[], modules[{id, file, generation, path, sha256,
bytes, byte_budget, requires, provides, reads, writes, creates_controls, licence, team, step, proof}], contracts}`.
4.6 The loader starts as soon as `window.KY` is built, before the `cosmos` fetch returns, so the shell and the card
are admitted and visible while the 535,037-byte `wafer.tsv` loads and stay when it refuses; a module that needs the
wafer lists `wafer` in `requires` and awaits that promise in its own `install` (GridAtlas composes every cartridge first
and each module waits for its own inventory, menu-bar.js:1647-1656): fetch `modules.json` no-store,
refuse the whole set on a wrong schema (`#refuse` strip, "the wafer is unchanged"), per module fetch, digest, budget,
blob-URL `<script data-ky-module>` per module, registration checks, publish `window.__KUIPER_EDITION__ = {admitted,
refused}`, never admit twice, never fetch outside `order`. 4.7/4.8 what a module may and may not touch (`KY.*` only, its
own `#ky-<id>` host, its `reads` and `writes`; never wrap an engine function, never a `.gm-title`, never
`target="_blank"` on the same host, never a colour outside PALETTE.md, never `keys.json`, `cosmos/`, the pointer or
`index.html`). 4.9 checks E6–E8 (stamp = header = manifest; `reads`/`writes` matched by literals; `node --check` and
exactly one `KY.register(`) folded into `tools/edition_check.py` (team-2/STEPS.md:364-531).

**Module name.** The hook table and the loader live in `editions/<stamp>/index.html` (integrator); the reviewable
reference is `modules/<module-stamp>-loader.js`; a twenty-line `modules/<module-stamp>-hello.js` proves the loader and
is removed from `order` before PR A.

**Files touched.** `index.html` (the hook table patch and the loader, applied by the integrator); `modules.json` schema
and first record set; `tools/edition_check.py` E6–E8; the hello module; `proof/handoff/04-loader/`.

**Acceptance test on Android.** Pixel 7 and Galaxy S24: 1 every `order` entry admitted in order with the manifest's
sha256, `refused` empty, `pageerror` 0; 2 one byte changed in a served module → `refused: sha256 mismatch`, all others
admitted, `#refuse[role=alert]` inside the viewport at 360 px, wafer drawn; 3 `requires: ['noSuchHook']` → `missing hook`;
4 renamed stamp → `refused … stamp`; 5 `install` throws → `install threw test`; 6 file deleted → `HTTP 404`; 7
`modules.json` emptied → wafer and bar present, `admitted: []`, `Object.isFrozen(window.KY)`; 8 `edition_check.py`
E1–E8 PASS on the committed folder and FAIL on each mutation applied to a copy; 9 load-to-last-admitted time and
Σ `bytes` against Σ `byte_budget` recorded, no threshold (team-2/STEPS.md:539-566).

**Licence note.** Loader, hook table and modules Apache-2.0 (kuiper-belt@018b46a README.md:157); `modules.json` and
`proof/` CC BY 4.0; every record carries its own `licence` (SPDX or the exact name, `CERN-OHL-S-2.0` for code taken from
See Through); an empty `licence` fails E6 and is refused at run time (`refused: no licence`). Code copied from GridAtlas's
modules is Apache-2.0 under gridatlas's LICENSE and cited `repo@sha path:line` in the module header.

**Opus team brief (team 4).** Own the hook table (as a patch to `index.html`), the loader reference, `modules.json`'s
schema and the first record set, E6–E8, the hello module, tests 1–9 with screenshots of 1, 2 and 7; do not touch the
engine below the hook table, `keys.json`, `cosmos/`, the bar's titles, any layer or the link grammar; you are admitted
first in the integrator's order, so publish the hook-table key list on #10 as a FINDING before any other team's module
is cut, and add a key only by a new FINDING naming the engine line it exposes.
### Step 5. See Through, the star player (team 3)

**Goal.** See Through is the first thing a person can open from the Kuiper and the largest entry in its bar; on a phone
it is one tap away and never wraps the bar; a tap takes the person from the wafer's stars down to one real substation;
a spark, a repository or a substation name on the Kuiper is a link into See Through with one written grammar; See
Through's stars gather on the wafer by the same placement law and are a layer of the Kuiper; and See Through's own
page links back to the Kuiper by key. "Star player" has one source, the owner's words (BRIEF.md:6-7): no Kuiper
document names See Through today (team-3/EVIDENCE.md E6: README, LAWS, SPEC, NEXT, PALETTE, the editions' READMEs, 0
hits), and NL-009 found it unreachable from Edition 4 (06-seethrough.md:11, BLOCKER).

**GridAtlas lesson (with key).** A control a person needs before they know which menu to open stays on the surface: the
live cartridge keeps the search box on the map (gridatlas@5ec7f62 atlas/cartridges/202609062358-substation-intelligence-
v9-63.js:6010-6016) and the phone keeps its GRID and SUBS chips on the map, "one tap on a phone, not two"
(atlas/modules/202609031958-menu-bar.js:1521-1552); See Through's own phone layout is that lesson applied (GRID SUBS
SPIDER bottom-left, see-through/202610050609/descent.js:926-930). The first title of the left group is the first thing
read (menu-bar.js:481-503). A link to another surface is an `<a role="button">` in the bar's own face, and a surface
that cannot be reached is a stated failure (menu-bar.js:737-754, :1392-1407, :757-762). Identity is resolved by one exact
parameter, never manufactured from a name: `repd_ref`, `EXACT_REPD_REF_ONLY` (atlas/releases/202608300453-atlas-v9/
deep-link-receiver-manifest.json:4-5; ventus-corev8engine.js:799-801), written on selection with `history.replaceState`
(202608291818-place-postcode-search.js:206-209), absent → `status:'ABSENT'` (:294-298). See Through has none of this
today: zero readers of `location.hash|search|URLSearchParams` in its seven scripts (team-3/EVIDENCE.md E2). NL-009's
measured decisions for the button: the stable pointer `../../see-through/`, the same tab, `goBack()` returns with 0
errors (06-seethrough.md:11-23, :51-60).

**Kuiper change.** 5.1 The entry, two forms, one node: `a#kuiper-star.gm-title[href="../../see-through/"]`, text SEE
THROUGH, first child of `.gm-side-left` before FILE, in the shell's face, drawn at rest in the shell's own lit state
(`rgba(80,220,240,.16)`, `#fff`, menu-bar.js:177-178) so it is the star without a second look, and the largest entry by
its own length (74.2 px against 34.6–40.2 px for the six titles at 9 px; 100.9 against 50.7–57.9 at 11 px); no font
size or weight is changed. Where the bar is too narrow for it (the 360 px class), the same node is moved (GridAtlas's
`move` idiom, menu-bar.js:1490) into `div#kuiper-star-strip`, `position:fixed; left:8px; bottom:calc(8px +
env(safe-area-inset-bottom))`, 44 px tall, the lit face with See Through's chip border (descent.js:862-863), ≈107 px
wide; the card's `bottom` and `safeBox().y1` move up by 52 px so Edition 4's clear-space camera law holds; never a
second row, never two copies; the README states which form each tested width got. The width rule itself is the
shell's (step 1, team-1/STEPS.md:156-161: `min-width:381px` title, `max-width:380px` strip; see R7). 5.2 The entry's
`title`/`aria-label` is the homepage's own sentence, "See Through: from the stars to one substation in 3D"
(homepage_v134.html:35); the ABOUT panel lists See Through first with that sentence, its licence and the pointer; the
edition README gets "The apps" (06-seethrough.md:126-152); the Kuiper's documents name See Through from this edition
on. 5.3 See Through's first screen is kept as measured (caption, name box and GO at y 56, the porthole of 12,900 stars,
KUIPER MAP SAT 3D, GRID SUBS SPIDER, the ODbL credit); the additions (5.5, 5.6, 5.8) go in a new dated folder
`see-through/<stamp>/` with the pointer moved in its three places (see-through/index.html:7, :11, :12), never in
`202610050609/`. 5.4 The descent, as it is, named: `flyTo(i)` (descent.js:417-425), `flightDepth` (:427-435: stars 1 s,
gather 1.2–3.3 s, zoom 9 by 4 s, `DMAX = 8` at 8 s), `arrive()` (:855-860), a star tap (`pick`, :872-882, 34 px on a
phone); measured `D` 1.84 at 3.5 s, 8 at 12.5 s under SwiftShader; the Opus team changes none of it. 5.5 The deep link
into See Through, read from `location.hash` once after the names are loaded (descent.js:1051-1057) and on `hashchange`;
fields `sub` (a name ≤ 80 chars: exact lower-case match or exactly one substring match flies; the existing refusal
words `NO SUBSTATION NAME HERE CONTAINS THAT` and the `MATCHES` note otherwise), `key` (`^\d{1,15}$`: an amber ring at
`KuiperLaw.place(key)` among the stars, "A LINE OF CODE, NOT A SUBSTATION", or the star that lands on a substation, or
`IS BEYOND THIS SKY`), `repo` (a `cosmos/repos.tsv` name: its key ranges computed as the engine does, caption
`<REPO> · n OF 12,900 STARS`), `view` (`kuiper|map|sat|3d`); order `repo`, `key`, `sub`, `view`; written on arrival as
`#sub=<name>` by `history.replaceState`; `window.__descent.link()` for the tests; examples
`see-through/#sub=Drax`, `#key=36064705400`, `#repo=gridatlas`, `#sub=Cowley&view=3d`. 5.6 The stars gather by the
same law and the sky reaches the rim: `kuiper-law.js` is lifted verbatim from the live page (kuiper-law.js:1-3, :37);
the law is unchanged at HEAD (`keyPlace`, index.html:92, :250) but `SPACE` is 59,637,070,538 (:36) against
63,340,120,796 today (cosmos/wafer-meta.json:4), so 278 of 344 verified lines are beyond See Through's rim; the new
folder re-lifts the law with the live `address_space`, and the Kuiper draws the same 5,800 star keys
(`floor((j + 0.5) · SPACE / 20000)`) as its `see-through` layer from `data/see-through.json` (5,800 Point features,
built by `tools/see_through_keys.py`, hashed into `layers.json`), registered through `KY.layers.register` and drawn
through `KY.draw.add` with `KY.hooks.keyPlace` and nothing else; the row shows `OK · 5,800 of 5,800 · See Through
<stamp> · SPACE <n>` or `FAIL · SPACE <a> ≠ wafer <b>` and draws nothing: the sky and the wafer must agree. 5.7 Deep
links out of the Kuiper: from a spark's card "see this line among the stars" → `../../see-through/#key=<key>` (no
mapping to a substation is invented); from a repository row or find result → `#repo=<name>`; from the find box's
unmatched text via FILE → open an app → See Through as `#sub=<text>`; all same-origin, same tab, through the pointer.
5.8 See Through links back: the X at the stars stage goes home (`history.back()` when the referrer is same-origin,
else `../../editions/`); a 44 px row `STAR KEY <k> · OPEN IT ON THE KUIPER` → `../../editions/#key=<k>` once a
substation is chosen; the credit line names the Kuiper law with its sha; `#key=` round-trips (team-3/STEPS.md:88-220).

**Module name.** `editions/<stamp>/modules/<module-stamp>-see-through.js` (id `see-through`, requires `keyPlace,
address, o2, card, flyTo, safeBox, panels, draw, redraw, layers, menuBar`, provides `see-through`); plus the new See
Through folder `see-through/<stamp>/`.

**Files touched.** The module; `editions/<stamp>/data/see-through.json`; `tools/see_through_keys.py`; the new folder
`see-through/<stamp>/` (descent.js with 5.5 and 5.8, kuiper-law.js re-lifted per 5.6, README.md; NOTICE.md, LICENSE.md,
licences/, plain.css, see3d.js, model.js, pf.js, grid-data.js, data/, vendor/ carried byte-identical); the pointer
`see-through/index.html` in three places; `see-through/README.md` entry; the ABOUT sentence and README "The apps".
Nothing in `cosmos/`, `202610050609/`, the engine above the edition layer or `keys.json`. The homepage's dated link
(homepage_v134.html:35) will be one stamp behind: a `REQUESTS.md` line for the homepage owner, not this team's file.

**Acceptance test on Android.** `proof/accept-see-through.cjs`, six viewports (Pixel 7, Galaxy S24 360×780, Pixel 7 at
393 and 430, landscape, 1280×800), real touch, 8 s settle: A1 `#kuiper-star` exists once; at 393 and wider it is the
first child of `.gm-side-left`, on the titles' `y`, `scrollWidth === clientWidth`, the widest `.gm-title`, lit at rest;
at 360 the same node is in `#kuiper-star-strip` at `x = 8`, bottom 8 px above the safe inset, 44 px tall, and the bar's
titles still share one `y`; A2 a tap on the entry (both forms) navigates in the same tab to `see-through/<stamp>/`
through the pointer and `goBack()` returns with the bar intact, no panel, 0 errors; A3 in See Through on Pixel 7: 13
controls ≥ 44 px; `#sub=Drax` → `T === 1182`, `D === 8` within 14 s; `#sub=xyzzy` → the existing refusal note;
`#sub=Hinkley` → the `MATCHES` note; `#key=36064705400` → one amber ring within 1 px of `KuiperLaw.place(k)`;
`#key=<SPACE>` → `IS BEYOND THIS SKY`; `#repo=gridatlas` → the caption count equals the Python count from `wafer.tsv`;
after `fly(1182)` `location.hash === '#sub=Drax'`; A4 `KuiperLaw.constants.SPACE` in the shipped folder equals
`cosmos/wafer-meta.json` `address_space`, `data/see-through.json` has 5,800 features recomputed by the test, the layer
row `OK`; with `SPACE` patched the row reads `FAIL` and nothing is drawn; A5 the pointer's three stamps equal the
shipped folder, every link of 5.7 is same-origin and 200, the card of `keys.json` bodies[0] carries
`/see-through/#key=36064705400`; A6 the round trip by key (Drax → STAR KEY row → the edition at that key with the line
of code as the card header → back to See Through showing "Drax"); A7 the X at the stars stage returns to the edition;
A8 zero `pageerror`, `node --check`, `ci_check` PASS, the module's sha256 in `modules.json` equals
`edition-sha256.txt`'s (team-3/STEPS.md:232-269).

**Licence note.** See Through is CERN-OHL-S v2 (see-through/202610050609/LICENSE.md:3-6; full text
`licences/globalgrid2050-CERN-OHL-S-2.0.txt`); the new folder is the same licence and carries LICENSE.md, NOTICE.md
and `licences/` byte-identical; the hash reader and the way home are additions to `descent.js` under that licence;
`kuiper-law.js` keeps its header. The substation names in `data/see-through.json` are © OpenStreetMap contributors,
ODbL 1.0 (NOTICE.md:22-25; grid-data.js:8), carried in the file's header and shown on the row. The Kuiper module is
Apache-2.0 and copies no See Through code: it links, which is not a relicensing (step 9's register). Nothing
third-party is added.

**Opus team brief (team 5).** Agent 1: the See Through folder `see-through/<stamp>/`: copy `202610050609/` whole, add
5.5 and 5.8, re-lift `kuiper-law.js` per 5.6 with a note naming `cosmos/wafer-meta.json:4`, move the pointer in three
places, never touch `202610050609/`. Agent 2: `tools/see_through_keys.py`, `data/see-through.json`, the layer record,
`drawStars` through `KY.layers.register` and `KY.draw.add` only. Agent 3: the bar entry and its two forms, the ABOUT
sentence, README "The apps", the card rows of 5.7 through the card module's row hook. Agent 4: `proof/accept-see-
through.cjs` A1–A8 on the six viewports, the README table of forms, `proof/handoff/05-see-through/` with screenshots.
Rules: every refusal string byte for byte; no mapping from a spark to a substation; no change to `flyTo`, `flightDepth`,
`arrive` or the 13 controls; no `target="_blank"` except the GitHub link; every number in the README from the test's JSON.

### Step 6. The File menu of an OS, and the hash deep-link grammar (team 3)

**Goal.** The Kuiper's FILE menu does what a File menu does in an operating system and nothing decorative: open a key,
open an edition, open an app, copy a link, download the evidence, export the view; the link it copies is one written
hash grammar that every surface of the Kuiper reads and writes, that the pointers forward, and that round-trips a spark
from the card to the same spark; EDIT and VIEW are named for what they hold.

**GridAtlas lesson (with key).** The File menu is the start of "a grid OS in our website … it should allow AI and humans
to develop and use" (the architect, 2026-09-05, gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:616-621); it
lists the mathematics the application runs on and opens each one (:614-632); its one runnable command is offered as a
copy with `navigator.clipboard.writeText` and a fallback that shows the command in full, "a control that silently does
nothing is worse than one that shows its own payload" (:707-733). File holds what leaves the building: "Export this
view", the image checked for blankness before it is offered (:794-811, `looksBlank` :1082, capture inside a render frame
:1120-1137), the credit travelling with the artefact (:813-834), each export control named by `id` and `data-gm-export`
(:1354-1365). Rows ≥ 44 px (:221); a fetch that fails adds no row and no error (:757-762). The deep link is one exact
parameter written on selection and read on arrival (202608291818-place-postcode-search.js:206-209, :294-298), and the
repository root forwards `search + hash` to the live route (gridatlas index.html:2). The Kuiper's own find grammar is
the seed: a period `YYYY[-MM[-DD]]` → `lightTime`, `new …` → `showNew`, digits → `goKey`, else a repository
(editions/202611012027/index.html:604-611; `goKey` :416, `address` :282, `describe` :284); Learn the Kuiper writes its
state into the hash with `history.replaceState`, 400 ms debounced (learn-the-kuiper/202610050609/lesson.js:336).

**Kuiper change.** 6.1 FILE's rows, each 44 px in the shell's face, grouped: OPEN — `Open a key…` (a numeric field and
GO; `0 ≤ k < SPACE` → `goKey(k)` and the card; outside → `key <k> is not on this wafer (SPACE <n>)`; second line
`python tools/key.py <k>` with a copy), `Open a line…` (the `line=<id>` of the hash, `keys.json bodies[].id`), `Open an
edition ▸` (one row per edition from `data/editions.json`, newest first, the current one inert; a tap goes to
`../<stamp>/` carrying the hash; Edition 1 opens `../202610311905/belt/`; the pointer `editions/` last), `Open an app ▸`
(step 7's launcher panel, See Through first and lit; the find box's unmatched text travels as `#sub=<text>`); LINK —
`Copy a link to this view` (`location.origin + pathname + '#' + hashText()`; `✓ Copied` for 4 s; on refusal the link in a
selected read-only field, never silent), `Copy the key`, `Copy python tools/key.py <k>`; EVIDENCE — `<a download>` rows
for `keys.json`, `proof/edition-sha256.txt`, `proof/keys-summary.json`, `modules.json`, `LICENCES.md`,
`proof/android-journey.json`, `README.md`, each with its byte count so a missing file is a test FAIL, not a silent 404
(09-robust.md:25-29); EXPORT — `Save an image of this view` (captured inside the page's own draw via `KY.draw.add`,
GridAtlas's blank test, stamped with the edition, the UTC time and "code Apache-2.0, text and data CC BY 4.0"; a blank
capture refused in words) and `Print` (the same image in a print stylesheet; no PDF writer copied, the browser's
print-to-PDF gives the same artefact). 6.2 FILE holds no fetched list at install, no layer switches, no bar title beyond
FILE, no new window. 6.3 The hash grammar, read and written by `KY.link`: the hash, not GridAtlas's query, because the
three pointers forward only `location.hash` (editions/index.html:12, see-through/index.html:12,
learn-the-kuiper/index.html:12) and drop the query, Learn the Kuiper already uses the hash, and a hash change does not
reload a WebGL page with 535 KB of wafer data in memory; the departure is stated in the README; the reader merges
`location.search.slice(1) + '&' + location.hash.slice(1)` (Learn the Kuiper one.js:468) and the hash wins on a
duplicate; the writer writes only the hash. Fields: `key` (`^\d{1,15}$`, `< SPACE`), `line` (`^[0-9a-f]{40}:\d+$`),
`repo`, `period` (`^20\d\d(-\d\d){0,2}$`), `layers` (ids of `layers.json`, comma-joined: team 2's `?layers=` adopted as
this field, read from either place, written in the hash), `edition` (navigate to `../<stamp>/` with the rest of the
hash), `app` (navigate to the app's link with the carried fields mapped), `sub` (carried to See Through only). Order on
arrival after the wafer admitted its data: `edition`, `app`, `layers`, `period`, `repo`, `line`, `key`; `hashchange`
runs the same reader; writing by `history.replaceState`, 400 ms debounced; Backspace clears every field but `layers`;
a field that fails its rule is ignored and named once in the readout, never an error. Examples:
`#key=36064705400` · `#line=0048802883266c68d5bdb6f5add0074e8b5b729d:5` · `#repo=gridatlas&period=2026-07` ·
`#layers=lines,see-through&key=63035688574` · `#edition=202611010114&key=36064705400` · `#app=see-through&sub=Drax`.
6.4 The round trip is the law of the grammar: `Copy a link` on a card writes `line=<id>&key=<key>`; opened fresh
through the pointer it selects the same body, lands it in the clear space, and the header is the same line of code;
written in the README under "Links" and in ABOUT as one sentence: "A link to this page is its hash: key, line, repo,
period, layers; copy it from File, paste it in Edit; the pointer keeps it." 6.5 EDIT holds what a person types (the
find box, now also accepting a pasted Kuiper or See Through link via `KY.link.read(text)`, `Paste a link…`, the LINES
filter with a clear control, `Clear the selection`); VIEW holds what a person looks at (readout, whole wafer, `r`, `n`,
`e`/`E`, reduced motion) and writes the hash on every change; VIEW does not export and does not switch layers
(team-3/STEPS.md:327-432).

**Module name.** `editions/<stamp>/modules/<module-stamp>-file.js` (id `file`; provides `file`, `link`; requires
`keyPlace, address, describe, goKey, lightTime, home, flyTo, safeBox, edCard, edFly, card, gbox, gin, panels, draw,
redraw, layers, menuBar`).

**Files touched.** The module; the README sections "File" and "Links"; one `NOTICE.md` line for GridAtlas's clipboard
and export method. `data/editions.json` is step 3's, `data/apps.json` step 7's; `index.html` only through
`modules.json`. Nothing in `cosmos/`, `keys.json`, `tools/key.py` or the law.

**Acceptance test on Android.** `proof/accept-file.cjs`, Pixel 7, Galaxy S24, Pixel 7 landscape, 1280×800, real touch:
A1 FILE opens one panel under the bar, every row ≥ 44 px, the rows in 6.1's order with four group headings, See Through
first and lit under `Open an app`, every edition stamp listed plus the pointer; A2 `Open a key` 36064705400 → the hash
holds it, the card header equals `keys.json` bodies[0].`line_text`, zoom 14 on the key within 1 px of the clear-space
centre; `SPACE` → the refusal words, camera unchanged; the copy command lands in the clipboard or, denied, in a selected
field; A3 every EVIDENCE download is 200 with `content-length` equal to the row's byte count and `keys.json`'s sha256
equals `edition-sha256.txt`'s; A4 the six example links opened through the pointer and directly do what the table says
(`edition=` asserts the URL only, Edition 2 ignores the hash today); A5 the round trip for three random `edPlaced[i]`;
A6 `Save an image` yields a PNG that is not one colour, `innerWidth × min(dpr, 2)` wide, with the stamp strip, and a
cleared `#c` yields the refusal and no file; A7 EDIT: a pasted Kuiper link → the `line` behaviour, a pasted See Through
link → navigation, Backspace → no `key/line/repo/period`, `layers` kept; A8 the back gesture after three link changes
leaves the page in one step, after a panel closes the panel; zero `pageerror`; `node --check`; `ci_check` PASS; the
module's sha256 matches (team-3/STEPS.md:440-470).

**Licence note.** The clipboard pattern, the export's blank check and the stamp travel are GridAtlas's method
(Apache-2.0, gridatlas@5ec7f62 LICENSE, NOTICE), credited in the module header and `NOTICE.md`; no GridAtlas bytes are
copied verbatim except the two words of the row labels. The evidence files are the edition's own (code Apache-2.0, text
and data CC BY 4.0, editions/README.md:27); offering `keys.json` for download is the same publication as serving the
page (its quotes keep their repositories' licences, Edition 4 NOTICE.md:7-10). The exported image carries the
attribution line. Nothing third-party is added.

**Opus team brief (team 6).** Agent 1: `KY.link` (reader with the merge rule, the field table byte for byte, the
resolution order, `read(text)`, the debounced writer, `hashText()`, `KY.link.inspect()`). Agent 2: the FILE rows (OPEN,
LINK, EVIDENCE with byte counts from the build) through `KY.panels`. Agent 3: EXPORT (in-draw capture, blank check,
stamp), the EDIT paste field and the Backspace rule. Agent 4: `proof/accept-file.cjs` A1–A8 on the four viewports, the
README sections with the six examples and measured numbers, `proof/handoff/06-file/`. Rules: every refusal string and
field rule byte for byte; no fetch at install; no `target="_blank"`; no new bar title; nothing in the hash that is not
in the table; do not touch the layer switches, the app registry or the placement law; when the clipboard refuses,
show, never swallow.
### Step 7. The OS of the estate, baby step one: the app registry, the launcher, the periodic table and the spider sandbox (team 4)

**Goal.** One file in the edition folder names every app of the estate with its permanent key, its stable link, its
licence and one line of purpose; the edition opens any of them from the File menu; the periodic table of the estate's
code and the spider sandbox each become an app row and a layer on the wafer. No window manager, no frames, no second
engine: one baby step the owner can see on a phone. In the estate's own terms an OS is an address space (the wafer),
a registry of what can be opened, a launcher, cartridges admitted by hash (step 4), a file menu (step 6), layers (step
3) and a release law (step 9); not yet windows, processes or a kernel (team-4/STEPS.md:43-54; globalgrid2050@c66759f
ARCHITECTURE.md:22, :9, :848; kuiper-belt@018b46a README.md:6-8).

**GridAtlas lesson (with key).** A thing enters the shell only through a registry record with an id, an order and a hash
(gridatlas@5ec7f62 atlas/current.json:5, :14-21); a module installs nothing until its hooks exist and counts what it
found (menu-bar.js:8-17, :34, :157); the homepage presents the estate's apps as an entity table with a key, a type,
a purpose and an operative version (globalgrid2050@c66759f homepage_versions/homepage_v134.html:31-56; See Through at
:18 and :35, type `application`).

**Kuiper change.** 7.1 `data/apps.json`, written by `tools/apps_registry.py` from two keyed sources and nothing else:
elements@f7a92fb APPS.md:7-13 (7 `block:<Sym>` rows: Ra, Cg, Sb, St, Pn, Gp, Wf) and homepage_v134.html:32-56 (25
`data-entity-id` rows), plus the spider sandbox (testcode@d09c185 spider/INDEX.md:13, v5) and the periodic table
itself (elements CATALOGUE.md:1): 34 rows; fields `key` (the estate's grammar: `block:<Sym>` or `surface:<url>`), `id`,
`name`, `kind`, `purpose` (the source's own words), `link`, `licence` (quoted by key, `not stated` where no file
exists), `source` (`repo@sha path:line` of the row), `wafer` (`{repo, commit, path}` of the app's first register file on
`cosmos/wafer.tsv`, or null with a reason); `same_as` cross-references, never merges; a provenance header as
elements catalogue/provenance.json:10-12. 7.2 The launcher is a panel, not a bar title (the bar already measures 439 px
against 412 px, NL-009 06-seethrough.md:24-30): one File entry "open an app" (step 6) and one layer record (step 3); each
row's header is the key line (the card law), then name, purpose, licence, link; same-tab navigation (06-seethrough.md:
51-57); the back gesture is the way home; a row whose link fails `fetch(HEAD)` shows `FAIL`, never hidden; rows 44 px.
7.3 The periodic table as a layer: every element of elements catalogue/elements.json at the key of line 1 of its first
register file at the recorded commit, computed as `tools/edition_keys.py` computes a verified line's key
(editions/202611012027/README.md:28-35); MEASURED: 221 of 244 elements have a register file whose commit is a row of
`cosmos/wafer.tsv`, 23 have no files and are counted, named in `data/elements.json`, not placed (12 constants, 4
engines, 6 layers, 1 cartridge); colours from PALETTE.md:9-13 only; the card: header = the line at its key, then
`block:<Sym>`, title, kind, category, state, description, GitHub link; as an app: key `surface:https://ventusltd.github.io/stars/blocks/`
and a panel by category and number like ELEMENTS.md. Disclosed: the catalogue is pinned to the register of 2026-09-15
(244 blocks); the live register holds 606 (stars@cbca125 blocks/blocks.json:2); the readout says "606 in the live
register, 244 catalogued". Precedent on the pre-Kuiper wafer: galaxies-wafers@fff6fc6 iterations/05-periodic-table/
table.mjs:1-14. 7.4 The spider sandbox as an app (row `spider-sandbox`, v5) and a graph layer: MEASURED on Pixel 7, the
v5 page renders its snapshot, 0 page errors, 24 requests of which 21 fail (6 local 404s for files the v5 folder does not
hold, 15 remote fetches blocked by the proxy), 12 controls under 44 px, so the spider needs its data beside it; the
layer copies two graphs into the edition with their sha256, `data/graphs/overview.json` (16 nodes, 15 edges, the front
door) and `data/graphs/periodic-table.json` (stars@cbca125 blocks/graph.json: 663 nodes, 2,481 edges), drawn only
between nodes that have keys (a repository: its first commit's `k0`; a block: its element key); the dashboard itself
stays where it is. 7.5 Licences in the registry verified from files (team-4/STEPS.md:184-188; step 9's register).

**Module name.** `editions/<stamp>/modules/<module-stamp>-apps.js` (id `apps`).

**Files touched.** The module; `data/apps.json`, `data/elements.json`, `data/graphs/overview.json`,
`data/graphs/periodic-table.json`; `tools/apps_registry.py` and `tools/element_keys.py` at the kuiper-belt root in the
release PR; the `modules.json` records; one README paragraph; the licence lines in `NOTICE.md`. Never a bar title.

**Acceptance test on Android.** Pixel 7 and a 360 px device, touch, served from the root: A1 `apps.json` has 34 records,
every `key` matches `^(block:[A-Za-z0-9]+|surface:https://)`, the 7 `block:` keys equal APPS.md:7-13 and the 25 ids equal
the homepage's `data-entity-id` set (a script compares); A2 the bar's `.gm-title` count equals step 1's; File → "open an
app" opens the launcher under the bar, rows ≥ 44 px, the first row's header is a key; A3 the See Through row navigates
in the same tab to `../../see-through/` (200, title "See Through") and `goBack()` returns with no panel open; A4 the
readout says "221 elements placed, 23 counted, not placed"; a tap within 9 px of an element spark opens a card whose
first line is the text at its key and second `block:<Sym>`; `python tools/key.py <key>` on three sampled elements returns
the recorded repository, commit and path; A5 the spider row opens the dashboard; the graph layer draws 15 edges for the
overview graph and the readout names how many periodic-table nodes had no key; with `data/graphs/` removed the layer
prints its error and the wafer still draws; A6 offline (every off-origin request blocked) the launcher, both layers and
the card work (team-4/STEPS.md:194-211).

**Licence note.** Everything this step copies is data under CC BY 4.0 as the edition's data; the code is Apache-2.0;
each row carries its target's own licence; the periodic table's licence is `not stated` until the owner states it
(Q1); the spider's graph data has no stated terms at its sources (stars has no LICENSE file: team-4/EVIDENCE.md E4), so
the two copied graphs are listed `DISCLOSED` in `LICENCES.md` and the owner is asked (Q5) before PR A.

**Opus team brief (team 7).** One writes `tools/apps_registry.py` and the 34-row registry with A1 as its test; one
writes `tools/element_keys.py` and `data/elements.json` (221 keys, 23 named) with A4; one writes the module (launcher
panel, File entry, two layer records, card) against step 3's registry probe and step 6's File hook, with A2, A3, A5;
one owns the Android journey, the offline test A6 and `handoff/07-apps/`. Touch only the files named. Never a bar
title. Never a licence written from memory.

### Step 8. The first intelligent algorithm: the drift of an edition from the live heads (team 4)

**Goal.** Every verified line of the edition is keyed to a commit; the estate moves on (23 repositories have moved since
Edition 1 was cut, gridatlas from `cacb69a7` to `5ec7f62f`). The drift answers, per line, with a key and never by
plausibility: is what the edition says about a line still true at the head? It is first because every later algorithm
needs it (a density that counts moved lines as present is wrong; a per-app Kuiper built from stale keys is wrong; a
release gate that cannot say "nothing drifted" cannot say "ship").

**GridAtlas lesson (with key).** The hashed cartridge: a thing is admitted only when its bytes still hash to the record
(gridatlas@5ec7f62 atlas/current.json:5, :31; tools/ci/pr-gate.mjs:176), applied to every verified line. The word is
already the Kuiper's: kuiper-belt@018b46a DRIFT.md:1-4 (host drift reconciled under L10, LAWS.md:139).

**Kuiper change.** Inputs with keys: `keys.json` `bodies[]` (`id, repo, commit, path, line, line_text, key`); the head of
each repository (`git rev-parse HEAD` or `GET repos/Ventusltd/<repo>/commits/HEAD`) recorded with its observation time
and offset (README.md:40); the file at the head by `git show <head>:<path>`; the exact bytes of `line_text`
LF-normalised (tools/count_lines.py:60-61). Output `data/drift.json` = `{edition, cut_at, heads, rows[], summary}`; each
row `{id, key, repo, path, line, edition_commit, head, class, head_line?, delta?}` with class `SAME`, `MOVED` (same text
in the same file at another line), `GONE`, `FILE_GONE`, `UNVERIFIED` (no head observed; nothing is claimed); the
summary's share is `SAME / (rows − UNVERIFIED)` with its denominator printed. Refusal rule: an unobserved head makes
every row of that repository `UNVERIFIED`, never `SAME` (README.md:46-47; tools/key.py:49 "Never trusted blind"); an
empty `line_text` or a key not on the wafer is `UNVERIFIED` with its reason; heads older than the cut by more than the
README's cap refuse the whole run and write nothing; the page module draws nothing when `drift.json` is missing or its
`edition` is not the folder's stamp and prints why (the `keys.json did not load` pattern, index.html:631). Where it
runs: `tools/drift.py` at cut time on the cutting machine; re-run by `tools/edition_check.py` as E9, "drift.json
re-computed against the recorded heads is byte-identical". The module only reads: `SAME` green, `MOVED` amber, `GONE`
and `FILE_GONE` an amber ring, `UNVERIFIED` grey-blue (PALETTE.md:9-14, :20); the card gains `at head <sha7>: SAME` /
`MOVED to line N (+d)` / `GONE`; LINES gains a filter by class; no new bar title. MEASURED as a prototype
(`/tmp/nl010/team-4/drift.py`, local clones at the heads above plus pipelinenews `2c0c8564532c`): 346 bodies → 333
SAME, 10 MOVED, 3 GONE, 0 FILE_GONE, 0 UNVERIFIED; the 3 GONE are gridatlas `atlas/current.json` lines 14 and 576
(the pointer moved) and kuiper-belt `learn-the-kuiper/202610050144/NOTICE.md:6`; the 10 MOVED include 5 in
data-grid-gb `dcmerge.py` (+6, the NL-007 `_op_core` patch landed above them). The numbers stand only once team 4's
evidence officer keys them; team 4's REVIEW passed at 21:28 UTC (team-4/STEPS.md:233-327).

**Module name.** `editions/<stamp>/modules/<module-stamp>-drift.js` (id `drift`), with `tools/drift.py` and
`data/drift.json`.

**Files touched.** The tool, the module, `data/drift.json`, the two card lines and the LINES filter (through the card
and layers APIs), the `modules.json` record, a README paragraph "Drift since the cut" with the five counts and the heads.

**Acceptance test on Android.** P1 determinism: two runs against the same recorded heads give byte-identical
`drift.json`. P2 refusal: one clone removed → every row of that repository `UNVERIFIED` and the denominator drops by
that count; `heads` emptied → exit non-zero, nothing written. P3 ground truth: every `MOVED` row's `git show
<head>:<path>` at `head_line` equals `line_text`; every `SAME` row the same at `line`; every `GONE` row's `git grep -F`
is empty. P4 on Pixel 7 and a 360 px device: the readout prints the five counts; a `MOVED` spark is amber; its card names
the head and the new line; with `drift.json` removed the wafer and the green sparks are unchanged and the readout says
the drift did not load; tapping an amber spark opens its card within 9 px; the LINES filter "moved" lists exactly the
`MOVED` rows; the bar stays one row. P5 the law: `drift.json` lists no repository outside `cosmos/repos.tsv` and no key
outside `keys.json`.

**Licence note.** `tools/drift.py` and the module Apache-2.0 as kuiper-belt code; `drift.json` CC BY 4.0; it quotes no
line text beyond what `keys.json` already quotes, so it adds no licence.

**Opus team brief (team 8).** One writes `tools/drift.py` with P1–P3 and P5 as its test file; one writes the module
(colours, card lines, filter) against step 3's layer registry; one runs P4 on Android and owns `handoff/08-drift/`; one
writes the README paragraph and the E9 line for step 9 and re-runs the tool against the recorded heads on a second
machine. Touch nothing outside these files. The colours are the palette's or the module is refused. Next algorithms,
in order, each with the same shape (inputs with keys, a refusal rule, a tool that writes JSON, a module that only
reads it): pattern density per repository per period; the descent from a spark to a substation (with step 5); the
register drift (244 catalogued against 606 live blocks).

### Step 9. The release law for editions, and the licence register (team 5)

**Goal.** Every Kuiper edition from Edition 5 onwards ships by one written law: a new dated folder, a pointer that
moves in three places and nowhere else, `ci_check` green, the Android journey green, every module hashed in a manifest,
the owner's `ACCEPT <stamp>` on a served preview before the pointer moves, the owner merging the pointer, and rollback
that is the pointer moving back, byte-exact, with no folder ever deleted. Every licence of everything the edition
brings in is verified from the files and written in one register in the edition folder.

**GridAtlas lesson (with key).** A release is a pointer move and nothing else (gridatlas@5ec7f62 docs/RELEASE.md:3-7,
:139-151); the eight steps cut, preview PR, owner acceptance, release, live bytes, homepage, served, rollback
(docs/RELEASE.md:38-45); the tested preview is the release (:119-121); the owner accepts in writing, first line, by an
owner login, and agents never record acceptance (:40, :49-53); only the owner merges, every PR a draft, rebase never
squash (:41, :54-55); cartridges hashed in the manifest and refused on mismatch (atlas/current.json:5, :14-21, :31;
tools/ci/pr-gate.mjs:176; docs/RELEASE.md:117); a module installs nothing until its hooks exist and publishes a missing
hook (menu-bar.js:8-17, :122-124, :157); rollback is a revert of the pointer commit, byte-exact, gates re-run, refused
if the pointer has moved since (docs/RELEASE.md:264, :283-306, :291-296, :300-302). The NL-008 finding closed here: a
harness merged release PRs on chat authorisation against "only the owner merges" (harness notes :19-20).

**Kuiper change.** The law `editions/LAW.md` (root-level, delivered in the release PR so the owner merges it), repeated
in short in each edition's README (team-5/STEPS.md:58-200): 9.1 the folder rule (harness notes :39-46; editions/README.md:
3-4, :9-10); each folder holds `index.html`, `keys.json`, `modules.json`, `modules/`, `README.md` ("What changed from
Edition N"), `NOTICE.md`, `LICENCES.md`, `proof/edition-sha256.txt`, `proof/keys-summary.json`, `proof/render-*.png`,
and from Edition 5 `proof/android-journey.json` and `proof/ci_check.log`. 9.2 the pointer `editions/index.html` in
exactly three places (:7, :11, :12), `<stamp>/` with no `/belt/`, and from Edition 5 the `location.replace` forwards
`location.search + location.hash` as GridAtlas's root does (gridatlas@5ec7f62 index.html:2), because today it forwards
only the hash and `editions/?layers=…` opens with no layers (team-2/STEPS.md 3.6); the same forwarding is asked of
`see-through/index.html:12` when step 5 cuts its folder; the release PR also adds the `editions/README.md` entry
and the root README entry. 9.3 `ci_check` PASS, extended: today K3 parses root pages only (tools/ci_check.py:68) so
edition pages and modules are unchecked by CI; `tools/edition_check.py` adds E1 every `editions/*/index.html` script and
every `modules/*.js` pass `node --check`; E2 every module in `modules.json` exists and hashes as recorded, no stray
file; E3 `proof/edition-sha256.txt` matches every file; E4 the pointer's three stamps agree and name a folder with a
proof; E5 `keys.json` byte-identical to the previous edition unless the README names a change (Edition 4's is
`1c293c33…`, proof/edition-sha256.txt:4); E6–E8 from step 4 (stamp = header = manifest; `reads`/`writes` literal; one
`KY.register`); E9 from step 8 (drift re-computed byte-identical). Output saved as `proof/ci_check.log`; wired into
`.github/workflows/check.yml` (:6-8, :25-26) in the same PR. 9.4 the Android journey gate: `FIXES/NL-009/android-journey.cjs`
(35,990 bytes; `node android-journey.cjs <url> <outdir> --all`) on Pixel 7 with real touch, SwiftShader flags, served
from the root; steps (a)–(o): load with zero console errors; bar one row at 360 and 393 px with the Ventus lockup at the
top; each title opens, closes on the same tap, a wafer tap and the back gesture; SEE THROUGH opens `../../see-through/`
on the same host; LINES pick closes the panel, the card's header is the line of code, the spark is in clear space; NEXT
three times; pinch zooms the wafer not the page, drag pans not scrolls; a 4 px spark is hit or the page says what it
hit; landscape and font scale 1.3; every module `admitted`; plus every NL-009 BLOCKER and MAJOR as a step (01-bar.md:13,
:18, :20; 06-seethrough.md:11, :24; 09-robust.md:11, :18) and every MINOR measured and reported without blocking ACCEPT.
A step that cannot be run is `NOT EVALUATED` with the reason (LAWS.md:156) and the preview goes to the owner only with
that list in the PR body. 9.5 `modules.json` hashes and the loader's refusals (step 4). 9.6 two draft PRs from
`edition/<stamp>`: PR A the preview adds `editions/<stamp>/` and nothing else, is merged so Pages serves the folder, and
the owner tests it on the phone and posts `ACCEPT <stamp>` as the first line of a comment on PR A (or `REJECT <stamp>`);
PR B the release changes only the pointer (three places), `editions/README.md`, the root README Editions section and,
the first time, `editions/LAW.md`; gate: the owner's ACCEPT on PR A after the folder's cut time, 9.3 PASS on the PR
head, the pointer naming the folder the owner tested byte for byte; only the owner merges PR B, with rebase. Who merges
PR A is Q6 for the owner. 9.7 rollback by `git revert` of PR B's pointer commit on `rollback/<stamp>-to-<previous>`,
refused unless the pointer has not moved since, `editions/index.html` byte-identical to the commit's parent, 9.3 re-run,
a draft PR only the owner merges; no folder deleted or edited. 9.8 the licence register `LICENCES.md` in the edition
folder, verified from the files at the heads above (team-5/STEPS.md:151-180 and team-5/EVIDENCE.md §5): kuiper-belt
Apache-2.0 code / CC BY 4.0 text and data (LICENSE:1-3; README.md:156-157; editions/README.md:27; Edition 4
NOTICE.md:3-5); GridAtlas Apache-2.0 (LICENSE:2-4; NOTICE:1-12), its third-party data excluded by its own NOTICE
(:25-32); the Ventus wordmark not licensed by Apache-2.0 §6 (LICENSE:139), used by the owner's instruction; See Through
CERN-OHL-S v2 for its code (see-through/202610050609/LICENSE.md:1-10; NOTICE.md:3, :8-16;
licences/globalgrid2050-CERN-OHL-S-2.0.txt:1; origin globalgrid2050@c66759f LICENSE.txt:1-5), ODbL 1.0 for its
substations and the GridAtlas line files (NOTICE.md:16, :22-27), CARTO/Esri/AWS terms (:28-34), MapLibre BSD-3
(:38-39; vendor/MAPLIBRE-LICENSE.txt:1); Learn the Kuiper Apache-2.0 / CC BY 4.0 / CERN-OHL-S v2 parts
(learn-the-kuiper/202610050609/NOTICE.md:7-11); testcode and its spider Apache-2.0 (testcode@d09c185 LICENSE:2-4,
NOTICE:1-12, :26-33), the spider's graph data not stated; elements: none in repository (`DISCLOSED`; Q1);
galaxies-wafers: none in repository (`DISCLOSED`; Q2); OSM-derived quotations ODbL 1.0 and DESNZ/DUKES OGL v3 (Edition
4 NOTICE.md:7-10). Rule: a row with `DISCLOSED` or `NOT EVALUATED` blocks copying, not linking (L8, LAWS.md:111-124).
Linking to See Through brings in no licence duty; copying `kuiper-law.js` or `descent.js` into a module makes that
module CERN-OHL-S v2 and it cannot be relicensed Apache-2.0: keep See Through code in its own module so the reciprocity
stops at that file.

**Module name.** `editions/LAW.md`; `tools/edition_check.py` (E1–E9); `editions/<stamp>/modules.json`;
`editions/<stamp>/LICENCES.md`; `proof/android-journey.json`; `proof/ci_check.log`.

**Files touched.** New: `kuiper-belt/editions/LAW.md`, `kuiper-belt/tools/edition_check.py`,
`editions/<stamp>/modules.json`, `editions/<stamp>/LICENCES.md`, `editions/<stamp>/proof/android-journey.json`,
`editions/<stamp>/proof/ci_check.log`. Changed, in PR B only: `editions/index.html` (three places),
`editions/README.md`, root `README.md` (Editions section), `.github/workflows/check.yml` (one `run:` line).

**Acceptance test on Android.** The journey of 9.4 passes on Pixel 7 against the served preview folder, and again
against the pointer `editions/` after PR B lands on the same stamp (`location.replace` resolves to `<stamp>/`). On a
desktop shell: `tools/edition_check.py` prints `RESULT: PASS` with E1–E9 each PASS; one altered byte in a module makes
E2 FAIL and the page print `<id> refused: sha256 mismatch`; a `requires` name that does not exist prints `refused:
missing hook`; the revert of 9.7 restores `editions/index.html` byte-identical to its parent (`git diff --exit-code
<parent> -- editions/index.html`).

**Licence note.** The law and the register are CC BY 4.0 text of kuiper-belt; `tools/edition_check.py` is Apache-2.0
code. Gaps the owner must close before their steps ship: elements has no licence file (step 7); the spider's graph
data has no stated terms (step 7); galaxies-wafers has no licence file (Phase 2, numbers only). Neither is invented.

**Opus team brief (team 9).** Write `tools/edition_check.py` with E1–E9 and a negative test for each; write
`editions/LAW.md` from 9.1–9.8 without softening a word; build `LICENCES.md` from the register, re-verifying every key at
the heads the integrator names; wire `edition_check.py` into `check.yml`; keep the journey script
(`FIXES/NL-009/android-journey.cjs`) as the gate and extend it from the NL-009 FINDINGS the integrator names; never
post ACCEPT.

### Step 10. The Opus plan: ten teams of four, one step each, integrated in a proven order (team 5)

**Goal.** Forty Opus agents build the edition as ten modules, one per step of this roadmap, each team inside its own
files, each module proven on Android before it is handed to the integrator, integrated in an order where every
admission leaves the journey green.

**GridAtlas lesson (with key).** One module, one slot, one hash, one proof per cartridge (gridatlas@5ec7f62
atlas/current.json:14-21, :31; docs/RELEASE.md:117-118); admitted only when its hooks exist and the inventory is complete
(menu-bar.js:8-17, :122-124); the preview is additive and never touches the pointer, the loader or the release folders
(docs/RELEASE.md:39); only the owner merges (:54-55); "shared modules are shared, not copied"
(governance/202609011940-modular-architecture-and-domain-map.md:26-49).

**Kuiper change.** The edition folder laid out for ten teams (team-5/STEPS.md step 10, module names reconciled to step
4's `<module-stamp>-<name>.js`): `index.html`, `keys.json`, `modules.json` integrator only; `modules/` one file per
team; `data/` one JSON per team that needs one; `handoff/NN-<name>/` per team (`MODULE.sha256`, `test.cjs`, `img/`,
`EVIDENCE.md` with every key, `LICENCE.txt`, `REQUESTS.md`), moved to `proof/handoff/` before PR A; `README.md`,
`NOTICE.md`, `LICENCES.md`, `proof/` integrator with team 9's register. Root-level files any team may change, and only
these: team 9 `tools/edition_check.py`, `.github/workflows/check.yml`, `editions/LAW.md`; team 3 `tools/build_layers.py`;
team 7 `tools/apps_registry.py`, `tools/element_keys.py`; team 8 `tools/drift.py`; team 2 proposes L11 as
`handoff/02-card/LAWS-L11.patch` (carried into PR B). The pointer, `editions/README.md` and the root `README.md` change
only in PR B. `cosmos/`, `tools/key.py`, `tools/edition_keys.py`, `see-through/`, `learn-the-kuiper/` and every earlier
edition folder are untouchable by every team. Each team of four: a lead (owns the module and the hand-off), a builder
(same file, never a second), a tester (`test.cjs` in the journey's Playwright form, screenshots), an evidence officer
(keys for every lesson and hook, the `LICENCES.md` row, the header's licence line). A change needed elsewhere is a
REQUEST on issue #10, not an edit.

**Module name.** The ten modules of the table below and `modules.json`.

**Files touched.** Per team, exactly the "may touch" column of the Opus table.

**Acceptance test on Android.** Every row's test, then the whole journey of 9.4 on the assembled edition, then the
same journey through the pointer after PR B.

**Licence note.** Each module header states its licence: Apache-2.0 for kuiper-belt code; CERN-OHL-S v2 for the See
Through module wherever See Through code is copied; team 7 copies no elements catalogue text and no spider graph JSON
beyond the two `DISCLOSED` graphs until their sources carry a licence.

**Opus team brief (team 10, the integrator).** Open the branch `edition/<stamp>` on day one with the Edition 4 copy, the
hook table and an empty `modules.json`; publish the loader stub in `handoff/00-stub/`; admit in the integration order
below, running the journey after each; a module that turns a step red is not admitted and the integrator posts a REVIEW
on #10 naming the step and the measurement; write the README "What changed from Edition 4" naming every module and
every NL-009 finding folded in; open PR A and PR B; never post ACCEPT; never merge PR B.
## Phase 2: Kuiper paradigms (gated on the owner's acceptance of steps 1–10)

Owner's words (BRIEF.md:72-74): "If passed then Kuiper paradigms (Kuiper drawn around actual apps so we can run
algorithms on the code of various apps) and of course an overarching Kuiper that counts EVERYTHING. And have a unique
lines Kuiper separately and compare it to the wafer that predates the Kuiper." Written by team 4 as steps 8a–8c
(team-4/STEPS.md:354-533) with keys from team 4's and team 5's evidence officers; nothing here is built until the owner
has accepted steps 1–10. The release law of step 9 applies unchanged to any folder Phase 2 publishes.

### 8a. Per-app Kuipers: a Kuiper drawn around one actual app

**Law.** The app's key space is the subset of the overarching wafer's issued keys whose address (`address(k)`,
kuiper-belt@018b46a editions/202611012027/index.html:282, and through `tools/key.py` the path) lies in the app's files:
for a register app its `files[]` at their commits (elements@f7a92fb catalogue/apps.json); for a folder app (See Through,
GridAtlas, the spider, the periodic table, Learn the Kuiper, an edition) every text blob under its folder in every
commit of its repository that is a row of `cosmos/wafer.tsv`. The app key is the rank of the overarching key among the
app's keys in wafer order (dense, from 0); silence between the app's commits is left unissued by the wafer's own rule,
600 keys per second capped at 14 days (tools/wafer_keys.py:10-11, constants at :33-34); the placement law is the
wafer's unchanged, `r = sqrt(key), theta = 2π frac(key × 2654435769 / 2^32)` (cosmos/wafer-meta.json:12).

**The mapping, provable.** `data/app-keys/<id>.tsv`: one row per contiguous run of the app's lines inside one file at
one commit, `wafer_k0  app_k0  run_length  commit_sha12  path`; both directions a binary search; proof: 12 sampled app
keys round-trip `app → wafer → tools/key.py` to a path under the app's folder with the text of `git show
<commit>:<path>` at the computed line, and 12 sampled wafer keys outside the app refuse; Σ run_length = the app's issued
keys, printed, or the file is not written.

**MEASURED today at HEAD only, by the wafer's binary rule (`/tmp/nl010/team-4/app_sizes.py`), for scale, not the
per-app totals (UNMEASURED until the tool runs over every commit):** See Through `see-through/202610050609` 27 files,
3,013 text lines; Learn the Kuiper `202610050609` 27 files (1 binary), 10,387; Edition 4 folder 9 files (3 binary),
1,217; the spider v5 folder 4 files, 6,539; the GridAtlas live shell `atlas/releases/202608300453-atlas-v9` 23 files,
3,113; `atlas/cartridges` 165 files, 1,088,335 lines (61 stamped copies of the substation-intelligence cartridge are
most of it: a per-app Kuiper of GridAtlas is dominated by its own history, which is the point of drawing it).

**First algorithm on a per-app Kuiper.** The drift (step 8) over See Through's app keys; then the register drift of the
periodic table.

**Module.** `tools/app_keys.py`; `data/app-keys/<id>.tsv`; `apps/<id>/index.html` = the engine with `SPACE`, `N` and the
commit texture built from the app's TSV instead of `cosmos/wafer.tsv` (the three load lines, index.html:201-208, the
only change), one per app row of `data/apps.json` that has a `wafer` field. **Acceptance:** the sums close; 12 + 12 round
trips; the Android journey on one per-app Kuiper. **Licence:** as the app's repository; the TSVs CC BY 4.0.

### 8b. The overarching Kuiper that counts EVERYTHING

**What the live wafer counts today, exactly.** 98 repositories, 13,344 commits, 45,735,836,396 issued keys,
17,604,284,400 unissued, address space 63,340,120,796, silence share 0.2779, first commit 1748560273, last 1793539112,
600 keys per second of gap capped at 1,209,600 s (kuiper-belt@018b46a cosmos/wafer-meta.json:2-11); `cosmos/wafer.tsv`
13,344 data rows, `cosmos/repos.tsv` 98 data rows, six of them redacted `unnamed-01…06`; `ci_check` K2 re-sums and
agrees (tools/ci_check.py:50-60; measured by both teams, `RESULT: PASS`). An issued key is "one per line in every file
in every commit" (tools/wafer_keys.py:10): a line that survives n commits holds n keys; this is a count of line
occurrences, not of distinct lines (8c is). Which commits: `git rev-list --all` of each public clone
(tools/count_lines.py:151; `log --all` at :122), every ref the clone had at harvest, not only main. Which repositories:
the public ones of the account as the harvest asked GitHub (tools/harvest.py:7-9), private names redacted (K1,
tools/ci_check.py:8). The binary rule: a blob with a NUL byte in its first 8,000 bytes is binary, counted as a blob,
excluded from line totals (tools/count_lines.py:14, :60-61; tools/harvest.py:77-78); a text blob's lines are newlines
plus one if it does not end in a newline (:80).

**What EVERYTHING adds, each as a denominator the readout must print.** (1) Private repositories: count their lines
into the issued total under the same redaction, or state the exact number left out: Q4 for the owner. (2) Binaries:
name every binary blob with its byte size in `cosmos/binaries.tsv` (sha, bytes, repo, first commit) and place none on
the line wafer; a second ring keyed by bytes is a new substrate with a new name (galaxies-wafers@fff6fc6 wafer.mjs:40-
43 "a new substrate with a new name beside this one, never an edit to this one"). (3) Data and documents: already
counted when text; state per repository how many keys are code, data and prose by extension, as a readout. (4)
Branches: already `--all`; record per commit which refs reached it at harvest so a count can be restricted to main on
demand. (5) Every count names its denominator: "of 45,735,836,396 issued", "of 63,340,120,796 addresses", "of 98
repositories", "of 13,344 commits"; never a bare percentage.

**Module.** `tools/count_lines.py` gains `binaries.tsv` and the per-ref record; `cosmos/wafer-meta.json` gains the counts
of (1)–(4); `ci_check` K2 gains their sums. **Acceptance:** K2 PASS with the new sums; the readout prints the five
denominators on a phone. **Licence:** data CC BY 4.0.

### 8c. The unique-lines Kuiper, compared by measurement with the wafer that predates the Kuiper

**Distinct, defined.** A line is its exact bytes without its terminator, CR before LF removed, nothing else trimmed:
the estate pins LF at the attribute layer (data-centres-gb `.gitattributes:5`, quoted in Edition 4 keys.json body 1),
so CRLF/LF is transport; indentation is not, because a key must be invertible to the bytes at it
(proof/keys-summary.json `text_eq_git_line`). The alternative (trimmed) merges more and is stated so it can be argued with.

**The wafer that predates the Kuiper, keyed.** galaxies-wafers@fff6fc6 README.md:5 ("every permanently numbered line of
the estate placed by one frozen law, `r = sqrt(key)`, `theta = key x golden angle` ... inherited unchanged from
testcode/202609151339"); the law wafer.mjs:43 (`GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5))`), :44-49 (`wafer.v1`,
frozen 2026-09-15T15:00:00Z), :52-54 (`place`), :69 (`extent = sqrt(max)`); the counts app.mjs:4-5 ("250,174 ... numbered
1 to 342,795"), :12 (`r = SPACING * sqrt(key)  theta = key * GOLDEN`), :59 (the numbered database at
`globalgrid2050.com/testcode/202609142202/data/`); the parent globalgrid2050@c66759f testcode/202609151339/README.md:9;
the same 250,174 is the denominator of elements (elements@f7a92fb APPS.md:3); 128,369 lines in a function family
(testcode/202609142202/data/all-lines.meta.json:11-16 per team 4). Between it and the live wafer sat the one-wafer of 19
September: 19,257 bodies from 66 repositories, 250,174 numbered lines, 245,170 placed (kuiper-belt NEXT.md:11-13).
Layers already on the old wafer for the comparison: `layers/manifest.json:2-3` (substrate `wafer.v1`, built
2026-09-15T16:17:31Z), `layers/periodic-table.json`, `layers/spider.json`, `layers/blocks.json` among 16; 42 iterations
(`iterations/index.json:3`). The development environment: globalgrid2050@c66759f testcode/wafer-development-environment/
(40 dated folders from `202609162333-estate` to `202609191355-proof-8`).

**The live wafer against it.** Same radius `sqrt(key)`; different angle: the old wafer multiplies the key by the golden
angle (wafer.mjs:46), the Kuiper takes `2π frac(key × 2654435769 / 2^32)` (wafer-meta.json:12; Knuth, Edition 4
NOTICE.md:13), so no key lands in the same place on the two wafers, which is why they are two substrates and not one.
Key ranges 1…342,795 against 0…63,340,120,795. Units differ: a pre-Kuiper key is one distinct numbered line of a
snapshot; a Kuiper key is one line of one blob in one commit (tools/key.py:39-42). Count: 250,174 distinct lines against
45,735,836,396 occurrences, about 1.8 × 10⁵, the expected effect of counting every line in every commit. "What moved"
is a change of unit, not a renumbering, and the comparison report says so first.

**The unique-lines Kuiper.** `tools/unique_lines.py` walks every text blob of every commit the wafer holds (the same
`rev-list --all` set), hashes each LF-normalised line, issues one key per distinct line at its first appearance in
wafer order (radius is still time: when the line was first written), silence by the same 600/s rule between first
appearances; writes `cosmos/unique.tsv` (unix, new_distinct_lines, repo_index, sha12, gap_before) and
`cosmos/unique-meta.json` (`distinct_lines`, `occurrences` = the wafer's issued, the ratio, the rule); the same engine
draws it from the second TSV as `unique.html` at the kuiper-belt root. The comparison in `proof/unique-vs-numbered.json`:
(i) how many of the 250,174 numbered lines appear among the distinct lines, each absence listed with its number and
reason; (ii) the first key of each in both spaces; (iii) the law constants side by side; (iv) what moved and why. The
number the owner asked for, distinct lines across all commits of all 98 repositories, is UNMEASURED until the tool runs
on the harvest machine; team 4's HEAD-only prototype over the local clones finished 8 of 25 repositories before both runs were killed out
of memory (exit 137) while reading globalgrid2050's HEAD tree (team-4/STEPS.md:534-559: e.g. data-grid-gb 364,592 text
lines, 90,702 distinct, 0.249; elements 129,931 lines, 39,177 distinct, 0.302); no estate-wide distinct count is claimed
from it, and the deliverable streams instead of holding a repository in memory.

**Module.** `tools/unique_lines.py`, `cosmos/unique.tsv`, `cosmos/unique-meta.json`, `proof/unique-vs-numbered.json`,
`unique.html`, one `ci_check` line "K2u: unique.tsv re-sums to unique-meta.json and distinct ≤ issued". **Acceptance:**
K2u PASS; (i)–(iv) written with keys; on a phone the readout says "N distinct lines of M occurrences, first written
between <date> and <date>". **Licence:** CC BY 4.0 data; galaxies-wafers' code has no LICENSE file (Q2), so Phase 2
compares its numbers and constants and copies none of its code.

### What Phase 2 needs from the Opus teams (separate from Phase 1's ten teams; not assigned)

| Phase 2 work | tool / folder | acceptance | needs from Phase 1 | licence |
|---|---|---|---|---|
| 8a per-app Kuipers | `tools/app_keys.py`, `data/app-keys/<id>.tsv`, `apps/<id>/index.html` per app with a `wafer` field in `data/apps.json` (step 7) | Σ run_length closes; 12 + 12 round trips through `tools/key.py`; the Android journey on one per-app Kuiper; the drift (step 8) run over See Through's app keys | step 4's loader, step 7's registry, step 8's drift, step 9's law | as the app's repository; TSVs CC BY 4.0 |
| 8b the all-counting Kuiper | `tools/count_lines.py` (+ `cosmos/binaries.tsv`, per-ref record), `cosmos/wafer-meta.json` new counts, `ci_check` K2 sums | K2 PASS with the new sums; five denominators printed on a phone; owner's answer to Q4 recorded in the README | step 9's law; the owner's Q4 | data CC BY 4.0 |
| 8c the unique-lines Kuiper and the comparison | `tools/unique_lines.py`, `cosmos/unique.tsv`, `cosmos/unique-meta.json`, `unique.html`, `proof/unique-vs-numbered.json` | K2u PASS; (i)–(iv) with keys for every number; run on the harvest machine over all 98 repositories, not a HEAD-only lower bound | step 9's law; galaxies-wafers read-only | data CC BY 4.0; no galaxies-wafers code copied (Q2) |
## Resolved between teams (both cited, one chosen, with the reason)

R1 **Module file names.** Team 5 drafted `modules/NN-<name>.js` (team-5/STEPS.md step 10); team 2 asks for
`modules/<module-stamp>-<name>.js` with the step number as the manifest fields `team` and `step` and the order in
`modules.json` (team-2/STEPS.md 4.3), because a module carried byte-identical into a later edition keeps its identity by
its stamp, not by one edition's order, as GridAtlas carries a cartridge of generation `202609241251` inside generation
`202610292044` (gridatlas@5ec7f62 atlas/current.json:3, :25). Teams 1 and 4 already name their files by stamp
(`<stamp>-kuiper-shell.js`, team-1/STEPS.md:165) or accept the reconciliation (team-4/STEPS.md step 7 "Module").
**Chosen: team 2's.** The brief gives team 2 the module boundary (BRIEF.md:41-44); the stamp is the identity and the
manifest carries the order. Every `NN-<name>.js` in this roadmap reads `<module-stamp>-<name>.js`; the `handoff/NN-<name>/`
folders keep the step number because they are one edition's working folders, not modules.

R2 **The name of the layers' title.** Team 1 maps GRID → WAFER (team-1/STEPS.md C5, measured: WAFER is five letters like
SCOPE, 40.2 px, the six titles 224.4 px plus the brand slot 77.6 px fit a 360 px bar with 58.0 px slack); team 2 proposes
LAYERS (team-2/STEPS.md "Open items", handed to team 1). **Chosen: WAFER.** Team 1 owns the menu names (BRIEF.md:34-39)
and measured the budget; LAYERS is six letters and was not measured against 360 px. The panel under WAFER is the layer
registry of step 3 in full.

R3 **The link grammar: query or hash.** Team 2's registry writes the ticked layers as the query parameter
`?layers=a,b` (galaxies-wafers' grammar, layers-panel.mjs:508-522; GridAtlas's deep links are queries) and finds that the
Kuiper's pointer drops the query (`location.replace('202611012027/' + location.hash)`, editions/index.html:12) while
GridAtlas's root forwards both (`search + hash`, gridatlas@5ec7f62 index.html:2), so it asks step 9's pointer law to
forward `location.search + location.hash` (team-2/STEPS.md 3.6). Team 3, which owns the grammar (BRIEF.md:45-48), chose
the hash: the pointers forward it today, Learn the Kuiper already uses it, and a hash change does not reload a WebGL
page; its reader merges `search` and `hash` (hash wins) and its writer writes only the hash, with `layers` adopted as a
hash field (team-3/STEPS.md 6.3). **Chosen: both, each in its own place.** The grammar is team 3's: every link the Kuiper
writes is a hash, `#key=…&line=…&repo=…&period=…&layers=…`, and `?layers=` is read as a courtesy. The pointer fix is team
2's: from Edition 5 `editions/index.html` and the new `see-through/index.html` forward `location.search +
location.hash` (step 9, 9.2), so a GridAtlas-style query link and a hash link both survive the pointer. Step 3's test 6
therefore passes through the pointer with either spelling; the one sentence for the README is 6.4's.

R7 **The star entry at 360 px: a fixed breakpoint or a measured overflow.** Team 1 fixes one rule in the shell,
`min-width:381px` seventh title / `max-width:380px` bottom-left 44 px strip, "step 5 may change the words and the target,
not the rule" (team-1/STEPS.md:156-161); team 3 moves the same node whenever `bar.scrollWidth > bar.clientWidth`
(by its budget, portrait phones narrower than 377 px) and specifies the strip's form (team-3/STEPS.md 5.1 (b)). The two
agree on every tested width (title at 393, 412, 430, landscape, desktop; strip at 360). **Chosen: team 1's breakpoint as
the rule, team 3's node-move and strip form as the content**, because a fixed breakpoint is what A2 of step 1 can test at
fixed widths and the shell owns the bar's budget; the one-row-at-360 law is never traded (both say so).

R4 **Who merges PR A.** Team 5's law lets the integrator merge PR A (the preview folder, pointer untouched) so that Pages
serves it for the owner's phone test, and keeps PR B (the pointer) for the owner alone (team-5/STEPS.md 9.6); the
GridAtlas law has the owner merge the release and the preview PR rebase-merged after CI (docs/RELEASE.md:39, :41). The
Edition 2–4 practice was the harness merging and pushing main itself (harness notes :48-49), which NL-008 recorded as a
gap (:19-20). **Not chosen here: Q6 for the owner**, with the law written so that either answer is one line in
`editions/LAW.md`.

R5 **The edition check: inside `ci_check.py` or beside it.** Team 5 writes `tools/edition_check.py` and wires it into
`check.yml`; team 2 and team 4 add E6–E9 to it; nobody proposes editing K1–K4. **Chosen: a separate tool, wired into the
same workflow**, so `ci_check.py` (K1–K4) stays byte-identical and the notes' rule "ci_check must print RESULT: PASS"
keeps its meaning; Q3 asks the owner whether a K5 line in `ci_check.py` is preferred instead.

R6 **One key corrected during review.** Team 4's draft cited `tools/wafer_keys.py:37-38` for the constants 600 keys
per second and 14 days; the consolidator's check found them at `tools/wafer_keys.py:33-34` (`GAP_KEYS_PER_SECOND = 600`,
`CAP_SECONDS = 14 * 86400`; team-5/EVIDENCE.md §7), and team 4's final text cites :33-34 (team-4/STEPS.md:427). No
disagreement remains; recorded so the correction is traceable.

## The ten Opus teams

Four agents per team: lead (owns the module and the hand-off), builder (same file), tester (`test.cjs` in the journey's
Playwright form, screenshots, Pixel 7 and Galaxy S24, real touch, zero console errors), evidence officer (keys, the
`LICENCES.md` row, the header's licence line). A hand-off without keys or without a passing `test.cjs` is returned.

| Opus team | step | module (file in `editions/<stamp>/modules/`) | may touch (and nothing else) | acceptance on Android (short; the full test is in the step) | hand-off |
|---|---|---|---|---|---|
| 1 | 1 the shell | `<module-stamp>-kuiper-shell.js` | its module; one script tag; `proof/accept-shell.cjs`; `handoff/01-shell/` | A1–A9: one row at 360/393/412/430 px and landscape; the wordmark within 1 px of GridAtlas's box; FILE EDIT VIEW · VENTUS · SCOPE WAFER ABOUT; 44 px hit boxes; back gesture closes; A9 the same script against GridAtlas | module + sha256; test; 4 screenshots; measured GridAtlas values with keys; `requires` list |
| 2 | 2 the card law | `<module-stamp>-line-card.js` | its module; script tag; README section; `handoff/02-card/` incl. `LAWS-L11.patch` | B1–B7: the first visible text node of every card equals `line_text` for all 344 placed bodies; key second; three wordings identical | module + sha256; test; before/after screenshots; the patch; the paragraph |
| 3 | 3 the layer registry | `<module-stamp>-layers.js` | its module; `data/layers.json`, `data/editions.json`; `tools/build_layers.py`; deletions in `index.html` of what moved; `handoff/03-layers/` | tests 1–9: 7 records, one original per layer, WAIT/LOAD/OK/EMPTY/FAIL/REFUSED in the row, `keys.json` 404 and tampering refused loudly, wafer still draws | module + data + sha256s; test; screenshots of WAIT, OK, FAIL, REFUSED; the record schema with keys |
| 4 | 4 the cartridge law | hook table + loader (patch to `index.html`; reference `<module-stamp>-loader.js`); `<module-stamp>-hello.js` | the patch; `modules.json` schema and first records; `tools/edition_check.py` E6–E8; `handoff/04-loader/` | tests 1–9: all admitted in order; sha256 mismatch, missing hook, stamp mismatch, install throw, 404 each refused in words with the rest running; empty manifest leaves a whole wafer; `KY` frozen | loader + sha256; test with the negative cases; the hook-table key list (published on #10 first); the manifest schema |
| 5 | 5 See Through, the star player | `<module-stamp>-see-through.js` | its module; `data/see-through.json`; `handoff/05-see-through/` | the step 5 test: first and largest entry; `../../see-through/` opens on the same host; a deep link from a spark or a repository lands on the named substation; the stars gather by the same law; CERN-OHL-S v2 code kept inside this module | module + sha256; test; screenshots (the entry, the landing); the header naming the licence |
| 6 | 6 the File menu | `<module-stamp>-file.js` | its module; `handoff/06-file/` | the step 6 test: open a key, open an edition, open an app, copy a link; the hash grammar round-trips through the pointer; clipboard or selectable fallback on Pixel 7 | module + sha256; test; the grammar with examples; screenshots |
| 7 | 7 the OS, baby step one | `<module-stamp>-apps.js` | its module; `data/apps.json`, `data/elements.json`, `data/graphs/*.json`; `tools/apps_registry.py`, `tools/element_keys.py`; `handoff/07-apps/` | A1–A6: 34 registry rows keyed and compared by script; launcher under the bar, rows 44 px, key as header; 221 elements placed, 23 named; 15 overview edges; offline works | module + data + sha256s; test; screenshots (launcher, table layer, spider layer); copied-versus-linked list per the register |
| 8 | 8 the drift | `<module-stamp>-drift.js` | its module; `tools/drift.py`; `data/drift.json`; README paragraph; `handoff/08-drift/` | P1–P5: determinism, refusal, ground truth by `git show`, the five counts on the page, amber MOVED sparks, nothing outside `repos.tsv` and `keys.json` | module + tool + data + sha256s; test; the algorithm's law in LAWS.md form |
| 9 | 9 law and register | `tools/edition_check.py` (E1–E9), `editions/LAW.md`, `LICENCES.md`, `.github/workflows/check.yml` | these; `handoff/09-law/` | E1–E9 PASS on the assembled folder, each with a negative test that FAILs; `LICENCES.md` every key re-verified at the integrator's heads; the journey script writes `proof/android-journey.json` | the tool + tests; `LAW.md`; `LICENCES.md`; the journey script |
| 10 | 10 integration and proof | `index.html`, `keys.json`, `modules.json`, `README.md`, `NOTICE.md`, `proof/`, the branch, PR A, PR B | these | the full journey of 9.4 PASS on the served preview; `ci_check.py` and `edition_check.py` PASS; `proof/edition-sha256.txt` complete; the README names every module and every NL-009 finding folded in | PR A with the journey table and the `NOT EVALUATED` list; PR B; the request for `ACCEPT <stamp>` |

## Integration order

The integrator (Opus team 10) opens `edition/<stamp>` on day one with the Edition 4 copy, the hook table and an empty
`modules.json`, publishes the loader stub in `handoff/00-stub/`, and admits in this order, running the journey after
each admission (team-5/STEPS.md step 10 "Order of integration"; team-2/STEPS.md brief "admitted first"):

1. **Opus 4, the loader and hook table**: nothing else can be admitted without it; its hook-table key list is a FINDING on
   #10 before any other module is cut.
2. **Opus 1, the shell**: the bar, the wordmark and the six names every later module hangs from; the star slot left
   empty with its owner's schema name.
3. **Opus 2, the card law**: the header of every card and LINES row.
4. **Opus 3, the layer registry**: the WAFER panel the See Through stars, the elements and the spider graphs register into.
5. **Opus 6, the File menu and the hash grammar**: the entries See Through and the apps add to.
6. **Opus 5, See Through**: the star player goes in before the other apps so its entry is first and largest by
   construction.
7. **Opus 7, the apps, the periodic table and the spider**.
8. **Opus 8, the drift**: the last layer, run over everything above.
9. **Opus 9, the law, the tool and the register**: it checks everything above, so it lands when there is everything to
   check; `edition_check.py` E1–E9 and `LICENCES.md` against the assembled folder.
10. **Opus 10, proof, README, NOTICE, PR A**, then the owner's phone test and `ACCEPT <stamp>`, then PR B.

`modules.json` `order` is this list, so the page loads in the order it was proven in. A module that turns a journey step
red is not admitted; the integrator posts a REVIEW on #10 naming the step and the measurement, and the team revises.
Phase 2 (8a–8c) starts only after the owner's ACCEPT of the edition that carries steps 1–10.

## Open questions for the owner

- **Q1 elements' licence.** `elements@f7a92fb` has no LICENSE or NOTICE file and no licence sentence in any of its 25
  tracked files. Which licence? Every sibling repository is Apache-2.0 code and CC BY 4.0 text. Until answered, step 7
  links to the catalogue and copies only keys (`block:<Sym>`), never its descriptions, and the elements layer row reads
  `REFUSED · licence unsettled`.
- **Q2 galaxies-wafers' licence.** `galaxies-wafers@fff6fc6` has no LICENSE or NOTICE file. Needed only if Phase 2 copies
  its code; the comparison of 8c uses its numbers and constants only.
- **Q3 K5 or a separate tool.** CI's K3 parses root pages only (tools/ci_check.py:68), so edition pages are unchecked
  today. The roadmap adds `tools/edition_check.py` (E1–E9) beside `ci_check.py` and wires it into `check.yml`. May the
  checks instead become a K5 line inside `ci_check.py`?
- **Q4 EVERYTHING's denominators (Phase 2, 8b).** Count private repositories' lines under the same redaction, or state
  the number left out? Binaries named and not placed (as today, count_lines.py:14) or a second ring keyed by bytes? Every
  ref (as today, `rev-list --all`) or main only on demand?
- **Q5 the spider's graph data.** The two graphs step 7 copies into the edition (`overview.json`, `periodic-table.json`)
  come from repositories whose licence is not stated at their source (stars has no LICENSE file). Copy them as
  `DISCLOSED` with the source address, or draw them live only and copy nothing?
- **Q6 who merges PR A.** The preview folder must be on main for Pages to serve it for the phone test. The integrator
  merges PR A (pointer untouched) and the owner alone merges PR B, as drafted; or the owner merges both, as
  GridAtlas's law reads for the release.
- **Q7 the star slot on your phone.** The shell fixes one rule (team-1/STEPS.md:156-161): at 381 px and wider SEE
  THROUGH is the seventh bar title, first on the left; at 380 px and narrower it is the bottom-left 44 px chip GridAtlas
  itself uses on a phone. A Pixel 7 (393 px) shows the title; a Galaxy S24 (360 px) shows the chip. Confirm on your
  phone that the chip is "the star player" enough at 360 px, or ask for the title at every width at the cost of
  GridAtlas's face (a smaller font or less tracking).
- **Q8 the mark.** "Ventus" and "Cables & Connectivity®" are used by your instruction; Apache-2.0 §6 licenses no
  trademark (gridatlas LICENSE:139). Confirm the wording `NOTICE.md` carries: "The VENTUS mark is used by Ventus Ltd,
  its owner. The Apache-2.0 licence of this code does not license the mark."

## Limits of this consolidation

- Written from the five teams' files as on disk at 21:32 UTC on 1 Nov 2026, when all five STEPS.md read `REVIEW: PASS`
  on line 1 (team 1 at 21:18:55, team 2 at 21:31:53, team 3 at 21:31:33, team 4 at 21:28:00, team 5 at 21:05:11; the
  consolidator's start was 20:45 UTC, so the 50-minute limit was met with three minutes to spare). No step is marked
  OPEN.
- NL-009 round 1 held `01-bar.md`, `06-seethrough.md`, `09-robust.md` and `android-journey.cjs` when this was written;
  the other seven auditors' findings are folded in by the integrator the same way (step 9, 9.4).
- No number here was computed by the consolidator except the `ci_check.py` run on a copy of kuiper-belt at 018b46a
  (`RESULT: PASS`) and the line counts of `cosmos/*.tsv`; every other number is a team's, with its key.
