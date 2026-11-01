# NL-010 overnight plan (owner ACCEPT, 1 Nov 2026 late evening)

Owner's words, binding: "ACCEPT. Reduce to 2 table watchers. Use 40 opus agents. Work overnight. Focus on CI CD
merging and publishing in small steps. Have work to show for by morning: deliver updates to Kuiper and make it work
from www.globalgrid2050.com. Don't overthink. Execute small steps."

Reading of ACCEPT: authority for the harness to merge and publish Kuiper editions in small steps tonight (as with the
owner's earlier "Accept" on NL-007), each step recorded here and on issue #10; the owner can reverse any step by the
pointer. Governance note for NL-008's record: this is chat authorisation, not an ACCEPT comment on a preview PR.

## Small steps (each: branch → ci_check PASS → merge to main → Pages deploy watched → recorded)

- R0 (done tonight): globalgrid2050.com/kuiper-editions/ is a door page forwarding to the editions pointer
  (branch kuiper-editions-door on Ventusltd/globalgrid2050; /kuiper/ was already taken by the kuiper-grid composer).
- R1: merge edition/202611012135 to kuiper-belt main as a PREVIEW (pointer unchanged) as soon as the base plus the
  admitted modules pass the journey on Pixel 7 and Galaxy S24; squash to one K1-clean commit first.
- R2: move the pointer to 202611012135 when the journey is green with the shell, card, layers and loader admitted;
  README and editions/README entries; Pages deploy watched; screenshots to the owner.
- R3: homepage card on globalgrid2050.com for the Kuiper editions and See Through (catalogue entry, label → pin →
  deploy cycle as for GridAtlas v9.188), so the Kuiper is reachable from the homepage, not only the door.
- R4…: each later module set (See Through, File, apps, drift, law) admitted and green → a new dated edition folder
  (6, 7, …), pointer moved, recorded. Earlier folders never edited.

## Watchers (two Fable agents, long loops)

- Watcher A "release": CI/CD. Runs ci_check and edition_check, squashes and merges, watches Pages runs, moves pointers,
  posts each step on #10 with the run ids; refuses to merge anything red.
- Watcher B "integration": keeps the Opus admission loop moving: polls handoff folders, re-runs the Android journey on
  the assembled edition, routes blockers to teams, decides refusals with measurements.

The harness wakes every ~40 minutes to commit landed files, relaunch watchers that ended, and start queued Opus agents
(20 concurrent cap).
