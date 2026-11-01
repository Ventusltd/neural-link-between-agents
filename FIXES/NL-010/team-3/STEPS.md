REVIEW: OPEN

# NL-010 team 3 ("See Through and File"): steps 5 and 6

Architect FABLE-T3A; evidence officer FABLE-T3B (`EVIDENCE.md`, `REVIEW.md` beside this file; rows cited as E2, E8 etc.
are sections of that file). Channel: issue #10. Heads: `kb@018b46a` = `/home/user/estate/kuiper-belt` at
018b46aed50f28f7b1882a0dcaba6593ce522beb (main, Edition 4); `ga@5ec7f62` = `/home/user/estate/gridatlas` at
5ec7f62f213e2d20a02e86427daa182c0f38e4a4; `gg@c66759f` = globalgrid2050 at c66759f0d7ac3489df9158da6eaa1330a37c069f;
`ST` = `see-through/202610050609/` inside kuiper-belt (the newest dated folder, the one the pointer opens:
kb@018b46a see-through/index.html:7, :11, :12). `nl@…` keys are files of this repository, read on 1 Nov 2026 between
20:50 and 21:15 UTC (NL-009 round 1: `01-bar.md`, `05-lines.md`, `06-seethrough.md`, `09-robust.md`; the other teams'
STEPS.md). No claim without a key; a measured absence is written as such.

Vocabulary shared with teams 1, 2, 4 and 5: **the edition** is the next dated folder `editions/<stamp>/`; **the page**
is its `index.html`; **a module** is one file under `editions/<stamp>/modules/`, admitted by `modules.json` with a
sha256 (team 2 step 4; team 5 step 9); **the hook table** is `window.KY` (team 2, 4.2); **the shell** is team 1's bar
(`nav#kuiper-menu-bar`, six titles FILE EDIT VIEW · VENTUS · SCOPE WAFER ABOUT, team-1/STEPS.md C1–C10); **the layer
registry** is team 2's `data/layers.json` + `KY.layers` (team-2/STEPS.md 3.1–3.8); **the app registry** is team 4's
`data/apps.json` and launcher panel (team-4/STEPS.md 7.1–7.2). Module names follow team 2's `<module-stamp>-<name>.js`
(team-2/STEPS.md 4.3); team 5 writes `NN-<name>.js` (team-5/STEPS.md:235, :266-267); the difference is for team 5B to
consolidate and changes nothing below but a file name.

## What was measured for these two steps (the keys behind the numbers)

Served `/home/user/estate/kuiper-belt` on `127.0.0.1:8203`; Playwright Chromium with the harness flags,
`devices['Pixel 7']` (412×839 CSS px, dpr 2.625, touch). Script and raw JSON: `/tmp/nl010/team-3/shots.cjs`,
`/tmp/nl010/team-3/shots-report.json`; copies in `FIXES/NL-010/team-3/img/` (`pixel7-measurements.json`,
`see-through-pixel7-arrived.png`, `edition4-pixel7-first.png`). Limitation, stated: the sandbox proxy refuses
`basemaps.cartocdn.com`, so MapLibre never finished loading (`mapState:'loading'`, `tileErr:1`, caption `MAP LOADING`
at the bottom of the fall); every number below about the stars, the controls and the flight is independent of a tile.
SwiftShader renders See Through's canvases slowly; captures were taken with the page told it was hidden (descent.js
pauses its frame loop on `visibilitychange`, kb@018b46a ST descent.js:1020-1023) and told it was visible again after.

See Through, first screen on Pixel 7 (M1): title "See Through"; caption `SEE THROUGH`; 12,900 stars (`NP`, the phone
rule of ST descent.js:954-955); porthole radius `Rpx` 193.64 px, centre `cy = 148 + (839 − 312)/2 = 411.5` (ST
descent.js:159-160); thirteen controls, all 44 px tall: name input (8,56) 332×44 placeholder "Substation name", GO
(348,56) 56×44, ♪ (308,8) 44×44, X (360,8) 44×44, KUIPER (71,713) 89×44, MAP (166,713) 63×44, SAT (235,713) 56×44,
3D (297,713) 45×44, GRID (8,761) 66×44, SUBS (78,761) 72×44, SPIDER (153,761) 88×44, ▲ (312,761) 44×44, ▼ (360,761)
44×44; no `<a>` element anywhere on the page (`links: []`); `window.KuiperLaw.constants.SPACE` = 59,637,070,538.
Arriving with `#sub=Drax` changed nothing: `state().T === -1`, `location.hash` still `#sub=Drax` (E2: no reader).
`window.__descent.find('drax')` → 1182, `sub(1182)` → `{Drax, 53.73622, −0.99249, 400 kV, National Grid}`.
`fly(1182)`: at 3.5 s `D` 1.84, caption `DOWN TO THE SUBSTATION`, flight `down`; at 12.5 s `D` 8, zoom 16, view
`sat`, card `Drax · 400 kV`; `view('kuiper')` → caption `THE STARS ONLY`. Page errors: none but the blocked tunnel.
Edition 4 on the same device (M2): `#bar` (0,0) 412×75, two rows: EDITION (147,6) 71×29, READOUT (221,6) 71×29,
LINES (296,6) 56×29, COMMANDS (8,39) 78×29; `#big` "Kuiper Edition 4 · 344 verified lines lit"; `location.hash` empty.

The wafer versus See Through's sky (M3): the live wafer's address space is 63,340,120,796 keys (kb@018b46a
cosmos/wafer-meta.json:4; re-summed from `cosmos/wafer.tsv` lines + gap_before over 13,344 rows = 63,340,120,796).
See Through's `SPACE` is 59,637,070,538, frozen at kuiper-belt commit 7a65dd3 (ST kuiper-law.js:35-36, :113). Of the
344 verified lines Edition 4 places, 278 have keys at or beyond 59,637,070,538 (`python3` over
`editions/202611012027/keys.json`, bodies with `on_wafer`; min 36,064,705,400, max 63,035,688,574). So today 278 of 344
sparks lie outside See Through's sky, and a star for them cannot be lit there until the constant is re-lifted (5.6).

---

## Step 5 — See Through, the star player

**Goal.** See Through is the first thing a person can open from the Kuiper and the largest entry in its bar; on a
phone it is one tap away and never wraps the bar; a tap takes the person from the wafer's stars down to one real
substation; a spark, a repository or a substation name on the Kuiper is a link into See Through with one written
grammar; the stars of See Through gather on the wafer by the same placement law and are a layer of the Kuiper; and
See Through's own page links back to the Kuiper by key. "Star player" has one source, the owner's words (BRIEF.md:6-7);
no Kuiper document names See Through today (E6 gap: README, LAWS, SPEC, NEXT, PALETTE, the editions' READMEs, 0 hits).

**GridAtlas lesson (with keys).**
5.L1 A control a person needs before they know which menu to open stays on the surface, not in a panel: the live
cartridge keeps the search box on the map for that reason (ga@5ec7f62
atlas/cartridges/202609062358-substation-intelligence-v9-63.js:6010-6016, quoted in team-1/STEPS.md "Note on the search
box"), and on a phone GridAtlas keeps its GRID and SUBS chips on the map, "one tap on a phone, not two"
(ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:1521-1552, E8). See Through's own phone layout is that lesson
applied: GRID SUBS SPIDER bottom-left, "GridAtlas mobile chips" (ST descent.js:926-930; measured at y 761, M1).
5.L2 The bar is three zones with the brand centred, and "the architect's complaint was that the VENTUS identity had
been torn out of view" (menu-bar.js:481-503); the first title of the left group is the first thing read.
5.L3 A link to another surface of the estate is an `<a role="button">` in the bar's own face, never a second look
(menu-bar.js:737-754 engine modules; :1392-1407 estate links), and a surface that cannot be reached is a stated
failure, not a silent gap (:757-762; the admission rule :1-21).
5.L4 Identity is resolved by one exact parameter and never manufactured from a name: `repd_ref`,
`EXACT_REPD_REF_ONLY` (ga@5ec7f62 atlas/releases/202608300453-atlas-v9/deep-link-receiver-manifest.json:4-5; the
engine's regex `^[A-Za-z0-9-]{1,40}$`, ventus-corev8engine.js:799-801); the link is written on selection with
`history.replaceState` (202608291818-place-postcode-search.js:206-209); absent → `status:'ABSENT'` (:294-298). See
Through has none of this today: zero readers of `location.hash|search|URLSearchParams` in its seven scripts (E2).
5.L5 The Pipeline News MAP arrival that See Through already copies, "on the point, then the card, then the lines" (ST
descent.js:855), and NL-009's measured decisions for the See Through button: the stable pointer `../../see-through/`,
not the dated folder; the same tab, because the back gesture is the way home and two WebGL pages on one phone evict
each other; `goBack()` measured to return to the edition with 0 errors (nl@FIXES/NL-009/round1/06-seethrough.md:11-23,
:51-60; E12).

**Kuiper change.**

5.1 **The entry, two forms, one node, measured not argued.** The shell (team 1) reserves the first position of the
left group for the star entry; whether a seventh title fits at 360 px is step 5's measured decision (team-1/STEPS.md
C5 "The star slot", C9). The budget, from team 1's measurements of GridAtlas's own face: six titles at 9 px 224.4 px +
the brand slot 77.6 px = 302.0 px; `SEE THROUGH` in that face is 11 × 5.65 + 12 = 74.2 px; total 376.2 px. At 360 px it
does not fit by 16.2 px; at 393 px the slack is 16.8 px, at 412 px 35.8 px, at 430 px 53.8 px, in landscape (863 px,
11 px titles: 11 × 7.175 + 22 = 100.9 px) and on a desktop it fits with room. So:
  (a) The entry is `a#kuiper-star.gm-title[href="../../see-through/"]` (the pointer, 06's decision), text
  `SEE THROUGH`, same tab, `rel` unset, first child of `.gm-side-left`, before FILE, in the shell's face (team 1 C4),
  with one difference that makes it the star without a second look: it is drawn at rest in the shell's own *lit*
  state, `background:rgba(80,220,240,.16); color:#fff` (menu-bar.js:177-178, the open-title look; See Through lights
  its own on-chips the same way, ST descent.js:871). It is the largest entry of the bar by its own length: 74.2 px
  against 34.6–40.2 px for the six titles at 9 px, 100.9 px against 50.7–57.9 px at 11 px; no font size or weight is
  changed to make it so (the owner's "exactly like GridAtlas" binds the face).
  (b) On install and on every resize the shell measures: if, with the star title present, `bar.scrollWidth >
  bar.clientWidth` (by the budget above, portrait phones narrower than 377 px: the 360 px Galaxy S24 class), the same
  node is moved (GridAtlas's `move` idiom, menu-bar.js:1490: the same DOM node, listeners kept) into
  `div#kuiper-star-strip`, `position:fixed; left:8px; bottom:calc(8px + env(safe-area-inset-bottom))`, the place
  GridAtlas and See Through keep their phone chips (5.L1); the strip is 44 px tall, `padding:0 14px`, 11 px, uppercase,
  the lit face plus `border:1px solid rgba(80,220,240,.5)` (See Through's chip border, ST descent.js:862-863), ≈107 px
  wide; `html` gets class `kuiper-star-strip`; the card's `bottom` becomes `calc(60px + env(safe-area-inset-bottom))`
  and `safeBox().y1` is reduced by 52 px so Edition 4's clear-space camera law (`edFly`, kb@018b46a
  editions/202611012027/index.html:676-680, `safeBox` wrap :726) keeps the spark above both. When the bar widens again
  the node moves back. There is never a second row (NL-009 01 F1: 75 px two-row bar, nl@FIXES/NL-009/round1/01-bar.md:
  43-45; M2) and never two copies of the entry.
  (c) The README of the edition states which form each tested width got, with the numbers (A1 below).
5.2 **What the entry says, on the phone and in the panel.** The entry's `title` and `aria-label` are "See Through:
from the stars to one substation in 3D" (the homepage's own sentence for it, gg@c66759f
homepage_versions/homepage_v134.html:35, E6). The ABOUT panel's estate group (team 1 C5) lists See Through first with
that sentence, its licence (CERN-OHL-S v2, ST LICENSE.md:3-6) and the pointer link, the two sentences NL-009 06 wrote as
`#edapps` (06-seethrough.md PATCH hunk `@@ -718,10`), carried into the edition's README section "The apps"
(06-seethrough.md:126-152) and the repository README's Editions entry. The Kuiper's own documents name See Through from
this edition on (closes the E6 gap).
5.3 **The hero on a phone (what the tap opens).** See Through's first screen is kept as measured (M1; NL-009 06 F4
"fits the phone", nl@FIXES/NL-009/round1/06-seethrough.md:39-50): caption `SEE THROUGH` top-left, ♪ and X top-right,
the name box and GO at y 56, the porthole of 12,900 stars (desktop 20,000, ST descent.js:19, :954-955) centred at
y 411.5 with radius 193.6 px, KUIPER MAP SAT 3D at y 713, GRID SUBS SPIDER and ▲ ▼ at y 761, the ODbL credit at the
foot. This step changes nothing in that layout; it adds the hash reader (5.5), the way back (5.7) and the re-lifted
`SPACE` (5.6), each in a **new dated folder** `see-through/<stamp>/` with the pointer moved in its three places
(see-through/index.html:7, :11, :12; the folder rule, see-through/README.md:23-25), never in `202610050609/`.
5.4 **The descent, as it is, named.** From the stars to a substation is one flight: `flyTo(i)` (ST descent.js:417-425)
sets phase `up` or `down`, `setView('map')`, `loadMap()`; `flightDepth(seconds)` (:427-435) holds the stars for 1 s,
gathers them into the grid from 1.2 s to 3.3 s (D 1→2), falls to zoom 9 by 4 s, holds the town labels two seconds,
and reaches `DMAX = 8` (MapLibre zoom `ZEND = 16`, :21-22) at 8 s; `arrive()` (:855-860) pings, captions `ONE SUBSTATION:
<NAME>` (`ONE SUBSTATION` on a phone, :818-822) and, when `see3d.js` is present and the person has not touched a view,
rises into 3D after 1.4 s. A tap on a star at the stars stage (`pick`, :872-882, 34 px radius on a phone) is the same
`flyTo`. Measured: `D` 1.84 at 3.5 s, `D` 8 at 12.5 s under SwiftShader (M1). The Kuiper documents this in the edition
README under "See Through" with these keys; the Opus team changes none of it.
5.5 **The deep link into See Through: the exact grammar.** Read from `location.hash` (the pointer forwards the hash and
drops the query, see-through/index.html:12; Learn the Kuiper's modules already read `#k=…&n=…` this way, kb@018b46a
learn-the-kuiper/202610050609/lesson.js:320-336, play.js:736-752; GridAtlas's departure to `?repd_ref=` is stated in
6.3). Fields `name=value`, joined by `&`, values `encodeURIComponent`-encoded, decoded in `try/catch` (play.js:741).
Read once at the end of the `ensureGridData` callback, after the names are in `D0.low` (ST descent.js:1051-1057; a link
arriving before that has nothing to search, E11 item 4), and again on `hashchange`. Unknown fields are ignored and named
once in the caption line (`LINK FIELD <name> NOT UNDERSTOOD`), never an error.

| field | value | what See Through does | refusal words (existing words where they exist) |
|---|---|---|---|
| `sub` | a substation name, ≤ 80 chars (the box's own `maxLength`, :907) | the name goes into the box; `doSearch()` (:389-403) runs; an exact lower-case match, or exactly one substring match, flies (`flyTo`, :417); otherwise no flight | 0 matches: `NO SUBSTATION NAME HERE CONTAINS THAT` (:400); many: `N MATCHES, n LIT. KEEP TYPING` (:402); the person finishes the search by hand |
| `key` | an integer `^\d{1,15}$` | at the stars stage (`D = 0`) one amber ring (`C.amber`, attention, kb@018b46a PALETTE.md:9-14) is drawn at `KuiperLaw.place(key)` projected exactly as every star is, `cx + x·ks, cy − y·ks` (:592), nothing else moves; if `key` equals `subKey[j]` for some `j < 5800` (:101, :965: the star that lands on substation j) the box is pre-filled with `nameOf(j)` and the note reads `THE STAR THAT LANDS ON <NAME>. PRESS GO`; otherwise the note reads `KEY <k> · A LINE OF CODE, NOT A SUBSTATION` (the module's own law, :11) | `key ≥ SPACE`: `KEY <k> IS BEYOND THIS SKY (SPACE <SPACE>)`; not an integer: ignored and named |
| `repo` | a repository name as `cosmos/repos.tsv` spells it | fetches `../../cosmos/wafer.tsv` and `repos.tsv` once (535,037 + 2,467 bytes, `wc -c`), computes the repository's key ranges exactly as the engine does (`k += gap_before; k0 = k; k += lines`, kb@018b46a editions/202611012027/index.html:203-208), and lights every star whose key falls in a range of that repository (the 20,000 DRAW THE GRID keys, :962-966), in the instrument's cyan; the caption reads `<NAME> · <n> OF <NP> STARS`; the name match is the engine's: exact lower-case, then `includes` (:612-613) | fetch fails: `REPOSITORY RANGES NEED ../../cosmos/wafer.tsv`; no such name: `NO REPOSITORY CALLED <name>`; 0 stars in range: `NO STAR OF THIS SKY FALLS IN <NAME>` |
| `view` | `kuiper` \| `map` \| `sat` \| `3d` | `setView(v, true)` after the flight (:346-358); `3d` before a target is chosen is the existing `CHOOSE A SUBSTATION FIRST` (:364) | other values ignored and named |

Order on arrival: `repo`, then `key`, then `sub` (a flight wins the camera), then `view`. Written on the way out, as
GridAtlas writes `repd_ref` on selection: `arrive()` does `history.replaceState(null, '', '#sub=' +
encodeURIComponent(nameOf(S.T)))`; `back()` to the stars (standalone branch, :442-446) clears the hash. Examples:
`https://ventusltd.github.io/kuiper-belt/see-through/#sub=Drax`, `…/see-through/#key=36064705400`,
`…/see-through/#repo=gridatlas`, `…/see-through/#sub=Cowley&view=3d`. `window.__descent.link()` returns the hash text the
page would write, for the tests (added beside `find`/`fly`, :1034-1050).
5.6 **The stars gather by the same placement law, and the sky reaches the rim.** `kuiper-law.js` is lifted verbatim
from the live page and says "Do not edit it; edit the live page and re-lift" (ST kuiper-law.js:1-3, :37). The law is
unchanged at HEAD (`G32`, `keyPlace` at kb@018b46a index.html:92, :250; E3), but the sky is not: `SPACE` 59,637,070,538
(:36) against 63,340,120,796 today (M3), so 278 of 344 verified lines are beyond the rim (M3). The new See Through folder
re-lifts `kuiper-law.js` at the edition's head: `source:` names the new commit (:113), `SPACE` becomes the live
`address_space`, and a comment beside it names `cosmos/wafer-meta.json:4` and the stamp. The 20,000 DRAW THE GRID keys
(`floor((ki + 0.5) · SPACE / NRULE)`, :962-963) and therefore the 5,800 star keys change with `SPACE`; that is the
design (a star for every 1/20,000th of the whole wafer), stated in the README. The Kuiper draws the same 5,800 star
keys as its `see-through` layer: `data/see-through.json`, `code-feature-collection.v1` (team 2, 3.2), 5,800 Point
features `{"type":"Point","key":subKey[j]}` with `properties: {sub: j, name: nameOf(j), see_through: "<stamp>",
space: <SPACE>}`, built by `tools/see_through_keys.py` from the same formula and the folder's `SPACE`, hashed into
`layers.json` and `proof/edition-sha256.txt`; a layer record `id: see-through, key: layer:see-through, group: THE APPS,
colour: cyan (the instrument), draws: points, module: <module-stamp>-see-through.js, licence: "CERN-OHL-S v2 (See
Through); names © OpenStreetMap contributors, ODbL"` (team-2/STEPS.md 3.1, 3.7 row `see-through`). The module calls
`KY.layers.register(record)` (3.3) and `KY.draw.add(drawStars)`; `drawStars` places each key with `KY.hooks.keyPlace`
and nothing else (3.8, the only placement). A tap within 9 px of a star (Edition 4's spark rule, :688-693) opens the
card with the line of code at that key as its header (team 1 step 2, L11), the key, the substation name under it, and
the row "see this star fall to <NAME>" → `../../see-through/#key=<k>`. The registry row's suffix shows `OK · 5,800 of
5,800 · See Through <stamp> · SPACE <n>`; when the folder's `SPACE` differs from the wafer's it shows `FAIL · SPACE <a>
≠ wafer <b>` and draws nothing (team 2's refuse discipline, 3.4-3.5): the sky and the wafer must agree.
5.7 **Deep links out of the Kuiper into See Through.** (a) From a spark: the card (team 1 step 2) gets a row "see this
line among the stars" → `../../see-through/#key=<key>` for any placed body (`keys.json bodies[].key`); no mapping to a
substation is invented (:11). (b) From a repository: the REPOS layer row and the find box result (`/` with a name,
:612-613) get "its stars in See Through" → `../../see-through/#repo=<name>`. (c) From a substation name: FILE → open an
app → See Through (step 6, 6.2) carries the find box's text as `#sub=<text>` when the text matched no key, period or
repository. (d) From a See Through star of the layer: 5.6. Every link is same-origin, same tab, through the pointer;
the See Through folder shipped with the edition is the one the pointer names (checked, A5).
5.8 **How See Through links back to the Kuiper.** Today it has no link out at all (`links: []`, M1; `ATLAS_URL` and
`SIM_URL` are declared and unused, ST descent.js:35-36). In the new folder: (a) the X at the stars stage, when there is
nothing to undo (`S.T < 0 && S.D === 0`, the standalone branch of `back()`, :442-446), goes home: `history.back()` when
`document.referrer` is same-origin and `history.length > 1`, else `location.href = '../../editions/'` (the pointer,
kb@018b46a editions/index.html:7, :11, :12); its `aria-label` becomes "back to the Kuiper" at that stage; (b) a
44 px row `STAR KEY <k> · OPEN IT ON THE KUIPER` appears in the card area once a substation is chosen (`showCard`,
:848-853), an `<a>` to `../../editions/#key=<keyOfSub(S.T)>`, the first `<a>` the page has; (c) the credit line gains
"Stars placed by the Kuiper law (kuiper-belt@<sha>)" with the same link; (d) the See Through README's first paragraph
names the Kuiper edition as its home and gives the grammar of 5.5 with the four examples. The two apps then link both
ways by key, and `#key=` round-trips (A6).

**Module.** `editions/<stamp>/modules/<module-stamp>-see-through.js` (the bar entry and its two forms, the layer
registration, the card rows of 5.7; registered with `requires: ['keyPlace','address','o2','card','flyTo','safeBox',
'panels','draw','redraw','layers','menuBar']`, `provides: ['see-through']`, team 2 4.4), `editions/<stamp>/data/see-
through.json`, `tools/see_through_keys.py`; and the new See Through folder `see-through/<stamp>/` (descent.js with
5.5 and 5.8, kuiper-law.js re-lifted per 5.6, README.md, NOTICE.md, LICENSE.md carried byte-identical, plain.css,
see3d.js, model.js, pf.js, grid-data.js, data/, vendor/ carried byte-identical), the pointer `see-through/index.html`
moved in three places, `see-through/README.md` entry. Touches nothing in `cosmos/`, nothing in `202610050609/`,
nothing in the engine above the edition layer, nothing in `keys.json`. The homepage registry row (gg@c66759f
homepage_v134.html:35) links the dated folder and will be one stamp behind; a `REQUESTS.md` line asks the homepage
owner to point it at the pointer (E11 item 5); not this team's file.

**Acceptance test on Android** (`proof/accept-see-through.cjs`; Pixel 7, Galaxy S24 360×780, Pixel 7 at 393 and 430,
Pixel 7 landscape, 1280×800; harness flags; serve the kuiper-belt root; real touch; 8 s settle):
A1 `#kuiper-star` exists once; at 393, 412, 430, landscape and desktop it is the first child of `.gm-side-left`, its
`y` equals every other title's `y`, `bar.scrollWidth === bar.clientWidth`, its width is the largest of all `.gm-title`
(≥ 74 px at 9 px, ≥ 100 px at 11 px), computed background `rgba(80,220,240,0.16)` and colour `rgb(255,255,255)` at
rest; at 360 the same node is inside `#kuiper-star-strip`, rect `x = 8`, `bottom = innerHeight − 8 − safe inset`,
height 44, width ≥ 100, and the bar's titles still share one `y`; the README table of forms matches these numbers.
A2 `touchscreen.tap` on the entry's centre (both forms) navigates in the same tab to `…/see-through/<stamp>/`, title
"See Through", through the pointer; `page.goBack()` returns to the edition with the bar intact, no panel open, 0
errors (06's test, 06-seethrough.md:154-173, re-run).
A3 In See Through on Pixel 7: 13 controls ≥ 44 px tall as M1; `#sub=Drax` → within 14 s `__descent.state().T === 1182`,
`name === 'Drax'`, `D === 8`; `#sub=xyzzy` → `T === −1`, note `NO SUBSTATION NAME HERE CONTAINS THAT`; `#sub=Hinkley`
(many) → `T === −1`, note matches `/MATCHES/`, box holds "Hinkley"; `#key=36064705400` → `T === −1`, `D === 0`, note
`KEY 36,064,705,400 · A LINE OF CODE, NOT A SUBSTATION`, one amber ring within 1 px of the projection of
`KuiperLaw.place(36064705400)`; `#key=<subKey[1182]>` → box text "Drax", note starts `THE STAR THAT LANDS ON DRAX`;
`#key=<SPACE>` → note `KEY … IS BEYOND THIS SKY`; `#repo=gridatlas` → caption matches `/^GRIDATLAS · \d[\d,]* OF 12,900
STARS$/` and the count equals the Python count of DRAW THE GRID keys inside gridatlas's ranges from `wafer.tsv`;
`#repo=nosuchrepo` → `NO REPOSITORY CALLED NOSUCHREPO`; after `fly(1182)` `location.hash === '#sub=Drax'`;
`__descent.link()` equals it.
A4 `KuiperLaw.constants.SPACE` in the shipped See Through folder equals `cosmos/wafer-meta.json` `address_space`, and
`data/see-through.json` has 5,800 features whose keys equal `floor((j + 0.5) · SPACE / 20000)` for `j < 5800`
(recomputed in the test), all `< SPACE`; `KY.layers.inspect().states['see-through'] === 'OK'`; with `SPACE` patched
in a copy to the old constant the row reads `FAIL · SPACE …` and `drawStars` draws nothing (count of cyan pixels in
`#o` unchanged).
A5 The pointer's three stamps equal the shipped folder; every link of 5.7 resolves with `new URL(href, base)` to the
same origin and `fetch(HEAD)` 200; the card of body `0048802883266c68d5bdb6f5add0074e8b5b729d:5` (keys.json bodies[0])
carries an `<a>` whose `href` ends `/see-through/#key=36064705400`.
A6 Round trip by key: in See Through choose Drax, tap `STAR KEY … OPEN IT ON THE KUIPER`; the edition opens with
`location.hash` `#key=<subKey[1182]>`, the camera at zoom 14 on that key and the card header the line of code at that
key (step 6 reader, 6.3); its row "see this star fall to DRAX" leads back to `…/see-through/#key=<same>`; the See
Through page then shows "Drax" in the box.
A7 The X at the stars stage with a same-origin referrer returns to the edition (`page.url()` is the edition folder);
opened directly, it navigates to `editions/`; `aria-label` "back to the Kuiper" at that stage, "back" otherwise.
A8 Zero `pageerror` on both pages; `node --check` on the module; `python3 tools/ci_check.py` → `RESULT: PASS`; the
module's sha256 in `modules.json` equals `proof/edition-sha256.txt`'s.

**Licence note.** See Through is CERN-OHL-S v2 (ST LICENSE.md:3-6; full text `licences/globalgrid2050-CERN-OHL-S-2.0.txt`,
:7); the new folder is the same licence and carries LICENSE.md, NOTICE.md and the licences folder byte-identical; the
hash reader and the way home are additions to `descent.js` under that licence; `kuiper-law.js` stays as it is headed
(E3, E4). The substation names in `data/see-through.json` are © OpenStreetMap contributors, ODbL 1.0 (ST NOTICE.md:22-25,
grid-data.js:8); the layer file carries that attribution in its header and the row shows it (team 2 3.7); the Kuiper
module is Apache-2.0 (kuiper-belt code) and copies no See Through code: it links to it, which is not a relicensing
(team 5's register row "See Through (the star player)", team-5/STEPS.md:168). The homepage sentence quoted in 5.2 is
Ventus Ltd's own text. Nothing third-party is added.

**Opus team brief (team 5 of 10, four agents).** Agent 1: the See Through folder `see-through/<stamp>/`: copy
`202610050609/` whole, add 5.5 (reader, writer, `link()`), 5.8 (X home, STAR KEY row, credit, README), re-lift
`kuiper-law.js` per 5.6 with the new `source:` line and a note naming `cosmos/wafer-meta.json:4`; move the pointer in
three places; never touch `202610050609/`. Agent 2: `tools/see_through_keys.py` and `data/see-through.json`, the layer
record for `layers.json` (hand it to the integrator, team 2's builder hashes it), and `drawStars` through
`KY.layers.register` and `KY.draw.add` only. Agent 3: the bar entry and its two forms in the module (5.1), the ABOUT
sentence and README "The apps" (5.2), the card rows of 5.7 through the card module's row hook (team 1 step 2). Agent 4:
`proof/accept-see-through.cjs` A1–A8 on the six viewports, the README table of forms with numbers, the handoff folder
`proof/handoff/05-see-through/` with screenshots of the entry (both forms) and the landing. Rules: every string in the
refusal column is used byte for byte; no mapping from a spark to a substation; no change to `flyTo`, `flightDepth`,
`arrive` or the 13 controls; no `target="_blank"` except the GitHub link; every number you cite in the README comes
from the test's JSON. Done when A1–A8 PASS on all six viewports and the evidence officer reproduces them from the
committed script.

---

## Step 6 — The File menu of an OS

**Goal.** The Kuiper's FILE menu does what a File menu does in an operating system and nothing decorative: open a key,
open an edition, open an app, copy a link, download the evidence, export the view; the link it copies is one written
hash grammar that every surface of the Kuiper reads and writes, that the pointers forward, and that round-trips a spark
from the card to the same spark; EDIT and VIEW are named for what they hold.

**GridAtlas lesson (with keys).**
6.L1 The File menu is the start of "a grid OS in our website … it should allow AI and humans to develop and use" (the
architect, 2026-09-05, quoted at ga@5ec7f62 atlas/modules/202609031958-menu-bar.js:616-621): it lists the mathematics
the application runs on and opens each one (:614-632), and its one runnable command is offered as a copy, `git clone …
&& node verify.mjs`, with `navigator.clipboard.writeText` and a fallback that shows the command in full because "a
control that silently does nothing is worse than one that shows its own payload" (:707-733).
6.L2 File holds what leaves the building: "Export this view" — print, PDF, image — and the image is checked for
blankness before it is offered ("Handing someone an empty PNG that looks like a successful save is worse than
refusing", :796-810, `looksBlank` :1082, capture inside a render frame :1120-1137), and the credit travels with the
artefact (`exportStamp`, `attributionText`, :813-834). Each export control is named by `id` and `data-gm-export`
"because its label is not a name" (:1354-1365).
6.L3 What else File, Edit and View hold in the live page: File ← the engine's Export button (:1663) and the engine
modules and export groups (:1586-1587); Edit ← the status button (:1664); View ← fullscreen (:1665) and Studies
(:1588, :777-792); group headings by `appendGroup` (:584); rows ≥ 44 px (:221); a fetch that fails adds no row and no
error (:757-762).
6.L4 The deep link is a query parameter written on selection and read on arrival, identity exact
(202608291818-place-postcode-search.js:206-209, :294-298; receiver manifest :4-5), and the repository root forwards
`search + hash` to the live route (ga@5ec7f62 index.html:2).
6.L5 The Kuiper's own find grammar already exists and is the seed of the link grammar: on Enter, a period
`YYYY[-MM[-DD]]` → `lightTime`, `new [code] [N h]` → `showNew`, digits → `goKey(min(SPACE−1, n))`, else a repository by
exact lower-case name then `includes` (kb@018b46a editions/202611012027/index.html:605-614; `goKey` :416, `address`
:282, `describe` :284 ends with "the text itself: python tools/key.py <k>"; the placeholder "a key, or a repository name
to send light through" :92). Learn the Kuiper writes its state into the hash with `history.replaceState`, 400 ms
debounced (kb@018b46a learn-the-kuiper/202610050609/lesson.js:336).

**Kuiper change.**

6.1 **FILE's rows, in this order, each a 44 px row in the shell's face, grouped by `appendGroup` headings:**

  OPEN
  - `Open a key…` — a row with a 44 px numeric field (`inputmode=numeric`, `enterkeyhint=go`, NL-009 05 F3) and GO;
    digits only; `0 ≤ k < SPACE` → `goKey(k)` and the card (header: the line at the key, step 2; silence → `describe`'s
    "key <k> was never issued", :285-286); outside → the row's own words `key <k> is not on this wafer (SPACE <n>)`
    and nothing moves. The row's second line is the command GridAtlas-style: `python tools/key.py <k>` with a ⧉ copy
    (6.L1), so a person can get the bytes from a clone.
  - `Open a line…` — the LINES filter is EDIT's (team 1 C5); this row opens the `line=<id>` of the hash (6.3) typed or
    pasted as `blob:line` (`keys.json bodies[].id`, e.g. `0048802883266c68d5bdb6f5add0074e8b5b729d:5`).
  - `Open an edition ▸` — one row per edition from `data/editions.json` (team 2 3.7, built from editions/README.md:12-24
    and the pointer), newest first: "Kuiper Edition 4 · 202611012027", the current one marked and inert; a tap goes to
    `../<stamp>/` carrying the current hash (`location.href = '../' + stamp + '/' + location.hash`), same tab, so the
    same key is looked at in another edition; Edition 1 opens `../202610311905/belt/` as its README says (editions/
    README.md:22). The pointer `editions/` is the last row, "the newest edition".
  - `Open an app ▸` — the launcher panel of team 4 (`setPanel('apps')`, team-4/STEPS.md 7.2), the rows drawn from
    `data/apps.json`; See Through first and lit (5.1's face), then Learn the Kuiper, GridAtlas, the periodic table,
    the spider sandbox, the homepage; this step adds nothing to the registry and defines no app key; when the find
    box holds text that matched no key, period or repository, the See Through row carries it as `#sub=<text>` (5.7c).

  LINK
  - `Copy a link to this view` — writes `location.origin + location.pathname + '#' + hashText()` (6.3) with
    `navigator.clipboard.writeText`; on success the row reads `✓ Copied` for 4 s; on refusal or absence of the API the
    row shows the link in full in a read-only 44 px field, selected, as GridAtlas shows its command (6.L1); never silent.
  - `Copy the key` — the selected key as digits; `Copy python tools/key.py <k>` — the command; both the same way.
  - `Paste a link…` is EDIT's (6.5).

  EVIDENCE (every row an `<a download>` to a file of the edition folder, same origin, no fetch at install)
  - `keys.json` (the register of verified lines; 346 bodies), `proof/edition-sha256.txt` (sha256 of every file but
    itself), `proof/keys-summary.json` (the 12 key.py round trips), `modules.json` (the admitted modules and their
    hashes, team 2 4.5), `LICENCES.md` (team 5 9.8), `proof/android-journey.json` (team 5 9.4), `README.md`; each row's
    second line is the file's byte count from `edition-sha256.txt`'s companion list, written by the build, so a row
    whose file is missing at test time is a FAIL of A3, not a silent 404 (NL-009 09: keys.json 404 shown only in a
    hidden readout, nl@FIXES/NL-009/round1/09-robust.md:25-29).

  EXPORT (GridAtlas's "Export this view", 6.L2)
  - `⤓ Save an image of this view` (`id=kuiper-export-image`, `data-ky-export="image"`): the WebGL wafer is drawn with
    `{antialias:false, alpha:false}` and no `preserveDrawingBuffer` (kb@018b46a editions/202611012027/index.html:122),
    so the capture is taken inside the page's own draw (`KY.draw.add` with the highest order, reading `#c` then `#o`
    onto one offscreen canvas), checked with GridAtlas's blank test, and stamped at the foot with the edition's name,
    the stamp, the UTC time and the licence line "code Apache-2.0, text and data CC BY 4.0" (editions/README.md:27);
    a blank capture is refused with "the image came back blank; try again after the wafer has drawn".
  - `⎙ Print` (`data-ky-export="print"`): the same image in a print stylesheet with the same foot. No PDF writer is
    copied from GridAtlas in this step (its `buildMapPdf` is 80 lines of JPEG-in-PDF for a raster map, :1206-1285;
    the browser's print-to-PDF gives the Kuiper the same artefact), stated in the README.

6.2 **What FILE does not hold.** No fetched list at install (GridAtlas's File fetches the engine graph; the Kuiper's
rows are its own files, so nothing can fail silently); no layer switches (WAFER, team 2); no bar title of its own beyond
FILE; no new window (one thing opens by navigation; the back gesture is the way home, team 4 7.2, NL-009 06:51-57).

6.3 **The hash deep-link grammar of the Kuiper page.** One grammar, read and written by `KY.link` (this module), used
by every row above, by the card, by the layers and by the apps.

  Why the hash and not GridAtlas's query: the three pointers of the family forward only `location.hash`
  (kb@018b46a editions/index.html:12, see-through/index.html:12, learn-the-kuiper/index.html:12) and drop the query, so
  a link through `editions/` keeps a hash and loses a `?`; Learn the Kuiper's modules already use the hash for the same
  purpose (6.L5); and a hash change does not reload a page whose WebGL context and 535 KB of wafer data are already in
  memory. The departure from GridAtlas is stated here and in the README. Courtesy to GridAtlas-style links: the reader
  merges `location.search.slice(1) + '&' + location.hash.slice(1)` (Learn the Kuiper one.js:468 does exactly this) and the
  hash wins on a duplicate field; the writer writes only the hash. Team 2 named `?layers=` as a query parameter
  (team-2/STEPS.md 3.6) and asked this step to adopt it: it is adopted as the field `layers`, read from either place by
  the merge above and written in the hash; team 5B consolidates the one sentence.

  Fields (`name=value`, `&`-joined, `encodeURIComponent`, order free; a field that fails its rule is ignored and named
  once in the readout line `link: <field> not understood`, never an error):

| field | value | reads as | writes when |
|---|---|---|---|
| `key` | `^\d{1,15}$`, `< SPACE` | `goKey(k)`: camera to the key at zoom 14, the card with the line at the key (step 2) or `describe`'s silence words | a key is opened by any means (`r`, `/`, a tap on the wafer that opens a card, `Open a key`) |
| `line` | `^[0-9a-f]{40}:\d+$` (`keys.json bodies[].id`) | the verified line: `edCard(i)` + `edFly` for the body with that id; unknown id → `line <id> is not in this edition's keys.json` | `e`/`E`, a spark tap, a LINES row, `Open a line` (and `key=` is written beside it with the body's key) |
| `repo` | a name of `cosmos/repos.tsv` | lit repository, exact lower-case then `includes` (:612-613), `home()`; none → `no repository called <name>` | the find box lights a repository; the REPOS layer row |
| `period` | `^20\d\d(-\d\d){0,2}$` | `lightTime(y, m, d)` (:607-608) | the find box lights a period; the PERIODS layer row |
| `layers` | ids of `layers.json`, comma-joined | `KY.layers.set(id, true)` for each, others off (team 2 3.6) | any layer change (team 2 writes through `KY.link.set('layers', …)`) |
| `edition` | a stamp of `data/editions.json` | handled by `Open an edition`: navigation to `../<stamp>/` with the rest of the hash; never kept in this page's hash | never written by this page |
| `app` | an id of `data/apps.json` | navigation to the app's `link` with the carried fields mapped (See Through gets `key`, `repo`, `sub`), same tab; unknown → `no app called <id>` | never written by this page |
| `sub` | a substation name | carried only: with `app=see-through` it becomes See Through's `#sub=` | written by `Open an app → See Through` from the find box |

  Resolution order on arrival, after the wafer admitted its data (`N > 0`, the `loadEdition()` call site, :219) and,
  for `line`, after `keys.json` loaded: `edition` (navigate, stop), `app` (navigate, stop), `layers`, `period`, `repo`,
  `line`, `key` (the last camera wins). `hashchange` runs the same reader. Writing: `history.replaceState(null, '', '#'
  + hashText())`, 400 ms debounced (6.L5); `hashText()` emits only fields with a value, in the table's order; Backspace
  (whole wafer) clears every field but `layers`. The Android back gesture pops one open panel (team 1 C7); it never
  pops a `replaceState`, so a link never traps a person on the page. Examples, each a test in A4:
  `editions/202611012027/#key=36064705400` · `#line=0048802883266c68d5bdb6f5add0074e8b5b729d:5` · `#repo=gridatlas&
  period=2026-07` · `#layers=lines,see-through&key=63035688574` · `#edition=202611010114&key=36064705400` ·
  `#app=see-through&sub=Drax`.

6.4 **The round trip, the law of the grammar.** A link copied from a card reopens the same spark: `Copy a link` on a
card writes `line=<id>&key=<key>`; opening it in a fresh page (through the pointer `editions/`, which forwards the
hash) selects the same body, the camera lands it in the clear space (`edFly`), and the card header is the same line of
code. Written in the README under "Links" with the six examples, and in the page's ABOUT panel as one sentence: "A link
to this page is its hash: key, line, repo, period, layers; copy it from File, paste it in Edit; the pointer keeps it."

6.5 **What EDIT and VIEW become** (team 1 C5 named them; this step fixes their rows that touch links):
  EDIT holds the things a person types: the find box (`/`: a key, a repository, a period — the grammar of 6.L5, now also
  accepting a whole Kuiper link or a See Through link pasted in, parsed by `KY.link.read(text)`), `Paste a link…` (the
  same field, named), the LINES filter (`#lyFind`, with the clear control NL-009 05 F4 asks for, nl@FIXES/NL-009/round1/
  05-lines.md:40-44), `Clear the selection` (Backspace: clears the hash fields as 6.3 says). Edit never navigates.
  VIEW holds the things a person looks at and the keys that step through them: readout on/off, whole wafer, random
  line `r`, new code `n`, next/previous verified line `e`/`E`, reduced motion; every VIEW action that changes what is
  looked at writes the hash (`key`, `line`, `period`), so `Copy a link` after any VIEW action copies that view. VIEW
  does not export (FILE does, as in GridAtlas, 6.L2) and does not switch layers (WAFER does).

**Module.** `editions/<stamp>/modules/<module-stamp>-file.js` (`KY.link` reader/writer, the FILE panel rows, the EDIT
paste field, the export; `requires: ['keyPlace','address','describe','goKey','lightTime','home','flyTo','safeBox',
'edCard','edFly','card','gbox','gin','panels','draw','redraw','layers','menuBar']`, `provides: ['file','link']`);
`data/editions.json` is team 2's; `data/apps.json` team 4's. Touches `index.html` only through `modules.json`; the
README sections "File", "Links"; `NOTICE.md` one line for GridAtlas's clipboard and export method (Apache-2.0).
Nothing in `cosmos/`, `keys.json`, `tools/key.py` or the law.

**Acceptance test on Android** (`proof/accept-file.cjs`; Pixel 7, Galaxy S24, Pixel 7 landscape, 1280×800; harness
flags; real touch; serve the root; 8 s settle):
A1 `touchscreen.tap` FILE: one panel, `top ≥` bar bottom, every row `height ≥ 44`; the rows in 6.1's order with the
four group headings; `Open an app` first row is See Through with the lit face; `Open an edition` lists every stamp of
`editions/README.md` plus the pointer, the current one inert.
A2 `Open a key`: type `36064705400`, GO → `location.hash` contains `key=36064705400`, the card header equals
`keys.json` bodies[0].`line_text`, camera zoom 14 on `keyPlace(36064705400)` within 1 px of the clear-space centre;
type `SPACE` → the words `key … is not on this wafer`, camera unchanged; `Copy python tools/key.py 36064705400` →
clipboard (granted) text equals that command; with the clipboard permission denied, the row shows the command in a
selected field.
A3 EVIDENCE: every `<a download>` resolves 200 with `content-length` equal to the row's byte count; `edition-sha256.txt`'s
hash of `keys.json` equals the served bytes' sha256.
A4 The six example links of 6.3 opened through `editions/` (the pointer) and directly: `key` → zoom 14 at the key and
the card; `line` → `edSel` is that body, the spark between the bar's bottom and the card's top (Edition 4's law);
`repo&period` → `litRepo` is gridatlas and `litK` spans July 2026; `layers=lines,see-through&key=…` →
`KY.layers.inspect().on` equals `['lines','see-through']` and the camera at the key; `edition=…&key=…` → `page.url()` is
`editions/202611010114/#key=36064705400` (Edition 2 ignores the hash today; the test asserts the URL only); `app=see-
through&sub=Drax` → `page.url()` ends `/see-through/<stamp>/#sub=Drax` and See Through lands on Drax (5.5).
A5 Round trip: tap `e`, tap `Copy a link`, read the clipboard, open it in a new page through the pointer: same body
id selected, same header bytes, `edSel` equal; repeat for three random `edPlaced[i]`.
A6 `Save an image`: the download is a PNG whose decoded pixels are not all one colour (GridAtlas's `looksBlank` test
applied by the test itself), width = `innerWidth × min(dpr, 2)`, with the stamp text present (asserted by drawing the
same foot into a reference canvas and comparing the strip's non-background pixel count within 5 %); with `#c` cleared
before the tap the row reads `the image came back blank…` and no file is offered.
A7 EDIT: paste `https://ventusltd.github.io/kuiper-belt/editions/202611012027/#line=0048802883266c68d5bdb6f5add0074e8b5b729d:5`
into the find box, Enter → the same as A4 `line`; paste a See Through link `…/see-through/#sub=Drax`, Enter →
navigation to See Through; Backspace → hash has no `key`, `line`, `repo` or `period`, `layers` kept.
A8 The Android back gesture (`page.goBack()`) after three link changes on one page leaves the page (one history
entry), and after opening a panel closes the panel (team 1 A5); zero `pageerror`; `node --check`; `ci_check` PASS;
the module's sha256 in `modules.json` equals `edition-sha256.txt`'s.

**Licence note.** The clipboard pattern, the export's blank check and the stamp travel are GridAtlas's method
(Apache-2.0, ga@5ec7f62 LICENSE, NOTICE; team-1/STEPS.md licence note), credited in the module header and in the
edition's `NOTICE.md`; no GridAtlas bytes are copied verbatim except the two words of the row labels. The evidence
files offered for download are the edition's own (code Apache-2.0, text and data CC BY 4.0, editions/README.md:27);
`keys.json` quotes lines that keep their repositories' licences (editions/202611012027/NOTICE.md:7-11); offering the
file is the same publication as serving the page. The exported image carries the attribution line. Nothing
third-party is added.

**Opus team brief (team 6 of 10, four agents).** Agent 1: `KY.link` (6.3, 6.4): reader with the merge rule, the field
table byte for byte, the resolution order, `read(text)` for pasted links, the debounced writer, `hashText()`; publish
`KY.link.inspect()` → `{fields, last_read, last_written, refused:[…]}`. Agent 2: the FILE panel rows (6.1) in the shell's
face through `KY.panels`, the OPEN and LINK groups, the EVIDENCE rows with byte counts from the build. Agent 3: the
EXPORT group (6.1) with the in-draw capture, the blank check and the stamp; the EDIT paste field and Backspace rule
(6.5). Agent 4: `proof/accept-file.cjs` A1–A8 on the four viewports, the README sections "File" and "Links" with the six
examples and the measured numbers, `proof/handoff/06-file/` with screenshots (the panel, a copied link, the image).
Rules: every refusal string and every field rule is used byte for byte; no fetch at install; no `target="_blank"`; no
new bar title; write nothing into the hash that is not in the table; do not touch the layer switches, the app registry
or the placement law; when the clipboard refuses, show, never swallow. Done when A1–A8 PASS on all four viewports and
the evidence officer reproduces them from the committed script.

---

## Open items for other teams (stated, not resolved here)

1. Module file naming: team 2 `<module-stamp>-<name>.js` vs team 5 `NN-<name>.js` (team 5B consolidates; this file
   uses team 2's).
2. `layers` as a query (team 2 3.6) vs a hash field (6.3): the reader accepts both, the writer writes the hash; one
   sentence for team 5B.
3. The homepage's dated See Through link (gg@c66759f homepage_v134.html:35) will be one stamp behind the new folder; a
   `REQUESTS.md` line for the homepage owner.
4. The star entry's strip form at 360 px takes the bottom-left 44 px; team 1's card and team 4's launcher must not
   place anything there on a phone (team 1 C6 already reserves it for the star entry).
