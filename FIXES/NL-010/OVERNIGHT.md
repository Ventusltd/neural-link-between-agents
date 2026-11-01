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

## Log

- 2026-11-01 23:34 UTC · Watcher A "release" started (session_015ELZDBhAFNgtcsrTUSi1vm). Read OVERNIGHT, OPUS-BRIEF, ROADMAP step 9, harness notes. kuiper-belt origin/main is now b9901d4 (the engine's own Actions commit, cosmos/*.tsv, 22:09 UTC), ahead of the 018b46a the notes record; the edition branch tip is febdd99. `python3 tools/ci_check.py` on the edition working tree: RESULT: PASS (K1 649 files, 0 private digests). `tools/edition_check.py` and `editions/LAW.md` do not exist yet (team 5's to deliver).
- 2026-11-01 23:36 UTC · State read from handoff/10-integration: ADMISSIONS rows 1-3 admitted (hello+loader 23:19, kuiper-shell 23:21, line-card 23:35); TEST.md Run 1 INTERIM (Pixel 7, 23:35): the shell admission turns `lines-pick` and `card-details` RED (shell `closeAll(false)` → `history.back()` taken by the loader's ANDROID BACK popstate listener). R1 condition (journey green on Pixel 7 and Galaxy S24 with base + loader + shell) NOT met. Polling every 5 minutes; nothing merged.
- 2026-11-01 23:50 UTC · Watcher A returning early (the run ended when its turn ended; relaunch needed). Nothing merged, nothing posted. Ready-made scripts in the session scratchpad (/tmp/claude-0/-home-user/e5bfe783-54ef-5c7a-8d30-0a492af18594/scratchpad/release/r1_squash.sh and merge_watch.sh; squash is done in a separate worktree so the Opus working tree on edition/202611012135 is untouched). R1 blocked only by the journey: TEST.md Run 1 INTERIM (Pixel 7) `lines-pick` and `card-details` red under the shell (shell `closeAll(false)` → `history.back()` vs the loader's ANDROID BACK popstate listener); no Galaxy S24 run on the assembled edition yet. Team 3 posted its layers HANDOFF on #10 at 23:44 UTC. Files on the branch for the squash: editions/202611012135, tools/build_layers.py, edition_min.py, apps_registry.py, element_keys.py, drift.py; absent: tools/edition_check.py, editions/LAW.md; check.yml identical to main. Note origin/main is b9901d4 (engine Actions commit, cosmos/*.tsv), so the squash onto main carries the newer cosmos files.
- 2026-11-01T23:58Z harness: R0 merged. globalgrid2050 PR #50 (kuiper-editions door) merged 3248bf7; deploy-pages.yml did not fire because the folder was not in its allow-list, so the deploy was dispatched by hand (run 41364141297); PR #51 (0b3369d) lists kuiper-editions/** for next time. Opus teams 1, 2 handed off; loader, shell and card admitted by the integrator; journey red on lines-pick/card-details until the shell/loader back-gesture owner is agreed (teams 1 and 4 told).
