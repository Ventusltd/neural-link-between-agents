# OPUS-11b hand-off: the homepage See Through link opens the new See Through (202611020012)

Lead: OPUS-11b, 2026-11-02 ~02:25 UTC (times from `date -u`). Follows team 11's pattern
(FIXES/NL-010/handoff-11-homepage.md). One branch pushed in globalgrid2050-homepage; no PR opened or merged;
(b) in globalgrid2050 is written here as steps only, because its pin must be cut from the merged main.

## What ships

Today the `see-through` entity's operative release `20261005-0609` launches the dated folder
https://ventusltd.github.io/kuiper-belt/see-through/202610050609/, so the homepage still opens the old See Through
although the pointer moved (kuiper-belt main 7110022, HARNESS HANDOFF issuecomment-6567465379, pages build and
deployment run 41376685032 success).

Change, in `data/homepage.json` only (plus the regenerated fallback `index.html`):

- New release on `see-through`, appended after the existing one (catalogue order is oldest first):
  `id` 202611020012, `label` "2 November 2026", `url` https://ventusltd.github.io/kuiper-belt/see-through/ (the
  stable pointer: kuiper-belt@7110022 see-through/index.html forwards to 202611020012/ with search and hash, and will
  follow future versions), `published_at` 2026-11-02T02:14:48Z (the commit time of 7110022), `status` available,
  `source_ref` https://github.com/Ventusltd/kuiper-belt/commit/7110022668eb4f8bd8d4dcfce87fd3c2fb315bfd,
  `archive_url` https://ventusltd.github.io/kuiper-belt/see-through/202611020012/, `archive_kind` app (the GridAtlas
  and Kuiper editions shape: mutable url + immutable dated archive).
- Promoted with the repo's tooling: `python3 scripts/releases.py promote see-through 202611020012 --reason "..."`,
  which set `operative_release_id` and appended the audit entry to `promotions` (promoted_at 2026-11-02T02:19:08Z).
- `20261005-0609` (dated folder 202610050609/) is unchanged and is now shown as Archived (an available non-operative
  release is archived implicitly; nothing removed).
- Entity description: one sentence added before "Needs the internet.": "It now also opens from a Kuiper card's link,
  straight to the right star." (Releases have no description field in the schema, so the note sits on the entity.)
- No other entity, release, view item, highlight or promotion changed. Title, subtitle and launch label unchanged.

Fallback after the change: nest launch and table row link https://ventusltd.github.io/kuiper-belt/see-through/;
versions summary "2 November 2026"; the table lists 2 November 2026 (Operative, link see-through/) and 5 October 2026
(Archived, link see-through/202610050609/).

## Branch (a)

Ventusltd/globalgrid2050-homepage `see-through-202611020012`, head **36b65cd80120d785e8caf1d6c8373995fe566ed0**,
base main 5a4abe41b7a9e19988faaedace252077a1646fc8, 1 commit. Files: data/homepage.json (+19 -2), index.html
(2 lines, regenerated).

Checks run locally on the branch (the same commands as .github/workflows/pr-checks.yml):

- `python3 scripts/releases.py validate`: Valid: 27 entities, 52 releases, 9 root view items; duplicate keys and broken
  references: 0.
- `python3 scripts/build_homepage_fallback.py && git diff --exit-code -- index.html`: Built 9 pinned nests and 25
  catalogue rows; index.html reproduced byte for byte (exit 0, after commit).
- `python3 -m unittest discover -s tests`: Ran 19 tests, OK.
- `node --check assets/versioned-homepage.js`: OK.
- `python3 scripts/fetch_active_pages.py --check`: offline ticker schema/key checks passed.
- `PLAYWRIGHT_MODULE=/opt/node22/lib/node_modules/playwright node tests/homepage-browser.cjs`: status pass (desktop
  and 390 px, all listed checks including "no browser runtime errors").
- Public language rules (globalgrid2050 scripts/check_public_language.py RULES): the added sentence and label carry no
  reserved, maker/site, dev-diary, path or assistant word.
- K1 (`leaks()` from kuiper-belt tools/check_proof.py): the changed lines (diff `+` and `-` lines of both files) = 0.
  Whole files print 1 for data/homepage.json and 1 for index.html, and print the same 1 on main 5a4abe4 before this
  change: the match is pre-existing, in the `cable-selection` entity, which this branch does not touch. Not fixed here
  (out of scope); flagged for the owner.
- Not checked: served bytes of the kuiper-belt pages (this sandbox's proxy refuses ventusltd.github.io and
  globalgrid2050.com); the pointer's content was read from git at 7110022 and the Pages run for 7110022 succeeded.

## PR (a) title and body

Title: homepage: See Through opens the new See Through (202611020012, stable pointer)

Body:
Adds release `202611020012` "2 November 2026" to the `see-through` entity in `data/homepage.json` and promotes it with
`scripts/releases.py promote` (audit entry appended), then rebuilds the no-JavaScript fallback with
`scripts/build_homepage_fallback.py`.

The launch link is the stable pointer https://ventusltd.github.io/kuiper-belt/see-through/, which opens 202611020012
today (kuiper-belt 7110022, see-through/index.html forwards search and hash) and follows future versions; the
immutable dated folder https://ventusltd.github.io/kuiper-belt/see-through/202611020012/ is the `archive_url`
(archive_kind app, the GridAtlas shape); `source_ref` is kuiper-belt 7110022668eb4f8bd8d4dcfce87fd3c2fb315bfd,
`published_at` its commit time. The previous operative release `20261005-0609` (dated folder 202610050609/) stays as an
archived release. The description gains one sentence: See Through now also opens from a Kuiper card's link, straight to
the right star. No other entity, release, view item, highlight or promotion changes.

Checks run locally: `releases.py validate` (27 entities, 52 releases), fallback reproduces `index.html`, unittest OK
(19), `node --check`, `fetch_active_pages.py --check`, `tests/homepage-browser.cjs` status pass. The added text carries
none of the domain's public-language words.

After merge: pin the merged main into Ventusltd/globalgrid2050 (`python scripts/release_gridatlas.py pin origin/main`),
with restore point homepage_v137 first.

Context: https://github.com/Ventusltd/neural-link-between-agents/issues/10 (NL-010, See Through 202611020012 on the
homepage)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm

## (b) Steps for the harness, after PR (a) merges

State when written: globalgrid2050 origin/main 18aa446e978898f73c39399cc070fd1e28722120, whose
catalogue/homepage-owner.json pins globalgrid2050-homepage 5a4abe41 (index.html 9a7e34c7…, data/homepage.json
3460dc92…). homepage_versions/ has 233 entries; highest restore point is v136, so the next is **v137**.

1. Cut the pin from the merged main (globalgrid2050-homepage):

       cd /home/user/globalgrid2050-homepage
       git fetch origin && git checkout main && git pull
       python3 scripts/releases.py validate
       python3 scripts/release_gridatlas.py pin origin/main > /tmp/pin.json

   Expected, if main was still 5a4abe4 when (a) merged (squash, rebase or merge commit all give the same tree):
   `commit` = the merged main sha, and these seven hashes (the pin printed for head 36b65cd):

       index.html                    3285399327d9be98bc99b6a9c0fbe5b1b2d1406d766ffc25ca05e48d2c7aa7a6
       assets/versioned-homepage.css 0c405224efa71f262011db49c5c7a559a265801ec98609c8c9b16a5d83df35d2
       assets/versioned-homepage.js  691df697ba930eab95ba67251ca3bee673ebb8c4174e010d8f6bb73ab24ea0f1
       data/homepage.json            4aed72cc055ac006bd6a5f894a57a9fd8558709696a96f0e523a5a825daf697a
       data/active-pages.json        4ee017277a6e0a7a5e92b5320486cdf908300ac34629d71249d53b0e4d31fdeb
       data/presentation.json        66285dafe5369cfb991030e80ffdf8c7893de279efb5aa15a86493434d9fed11
       data/entity-types.json        bbf1e6c692e6d27c95ca4f37a5286e344028e9d794dd3d8abf2c52232d4b9ca0

   Only index.html and data/homepage.json differ from the current pin. If any other hash differs, or these two
   differ, stop: main moved; re-run the (a) checks on main and recompute.

2. Branch in globalgrid2050 from origin/main:

       cd /home/user/estate/globalgrid2050
       git fetch origin main
       git checkout -b see-through-202611020012 origin/main     # expect 18aa446e; if main moved, re-check step 3

3. Restore point v137 = the homepage served today (import output of the current pin 5a4abe41, before the edit):

       python3 scripts/import_homepage_owner.py                 # "Imported verified homepage 5a4abe41…: 7 files"
       cp index.html homepage_versions/homepage_v137.html
       git checkout -- index.html homepage-shell                # generated output discarded (both are tracked, stale)

   (If raw.githubusercontent.com is unreachable, the same bytes come from globalgrid2050-homepage
   `git show 5a4abe41:index.html` with the three replacements import_homepage_owner.py makes:
   `./assets/versioned-homepage.css|js` -> `./homepage-shell/assets/…`, `href="data/homepage.json"` ->
   `href="./homepage-shell/data/homepage.json"`, then rstrip + "\n". This method reproduces v136's sha256 c85ca230…e7df
   exactly for 30470e1.)

   Expected metrics (computed by that method; must match): **68 lines, 3454 words, 52107 characters, 52111 bytes,
   SHA-256 77a5739de17180dd16c6cdf44c053af079aad8588618ee5d8e43ba4fe163b138**.

   Write homepage_versions/homepage_v137-metrics.json in v136's shape:

       {
         "file": "homepage_v137.html",
         "source": "Currently served homepage: scripts/import_homepage_owner.py output for the pre-edit pin (owner commit 5a4abe41b7a9e19988faaedace252077a1646fc8) on globalgrid2050 main 18aa446e978898f73c39399cc070fd1e28722120. Deploy-pages assembles index.html this way during the build, so these are the served bytes; the committed root index.html is stale and is overwritten at build.",
         "homepage_versions_entries_before": 233,
         "lines": 68,
         "words": 3454,
         "characters": 52107,
         "bytes": 52111,
         "sha256": "77a5739de17180dd16c6cdf44c053af079aad8588618ee5d8e43ba4fe163b138",
         "intention": "Promote the owner bundle at globalgrid2050-homepage <merged sha> (branch see-through-202611020012) so the See Through entry in the Kuiper nest opens the new See Through: release 202611020012 (2 November 2026) launching the stable pointer https://ventusltd.github.io/kuiper-belt/see-through/, with its dated folder see-through/202611020012/ as the archive, and 5 October 2026 (202610050609) kept as an archived release. All other entries and links retained.",
         "measurement_workflow": "Passed <run URL> at main 18aa446e978898f73c39399cc070fd1e28722120",
         "numbering": "Checked remote main: v136 was highest; v137 created without overwriting history."
       }

   Append to homepage_versions/README.md:

       ## Version 137

       Pre-edit restore point: `homepage_v137.html`; measurements: `homepage_v137-metrics.json`. Source: the currently served homepage, rebuilt byte-for-byte by `scripts/import_homepage_owner.py` from the pre-edit pin (owner `5a4abe41b7a9e19988faaedace252077a1646fc8`) at main `18aa446e978898f73c39399cc070fd1e28722120`; the committed root `index.html` is stale and replaced at build.

       Intention: <the same intention sentence as the metrics file>

       Measurement: restore-point workflow [<run id>](<run URL>) passed. 233 entries before adding v137 and its metrics.

       Metrics: 68 lines, 3454 words, 52107 characters, 52111 bytes; SHA-256 `77a5739de17180dd16c6cdf44c053af079aad8588618ee5d8e43ba4fe163b138`.

   Measurement run: `gh api -X POST repos/Ventusltd/globalgrid2050/actions/workflows/homepage-restore-point-check.yml/dispatches -f ref=main`
   (team 11 used run 41366798722 at main; it measures the committed files and does not change the site), then put its
   run URL in both places.

4. The pin: `cp /tmp/pin.json catalogue/homepage-owner.json` (the exact output of step 1; keep the file's trailing
   newline as the current file has it). Optional local proof: `python3 scripts/import_homepage_owner.py` must print
   "Imported verified homepage <merged sha>: 7 files"; then `git checkout -- index.html homepage-shell` again.
   `python3 scripts/check_public_language.py` should show only the two pre-existing "measured" findings
   (globalgrid2050-homepage #5).

5. K1 on every changed file (`leaks()` must print 0): homepage_v137.html will print the same pre-existing 1 as the
   owner bundle (the `cable-selection` entity text, served today and already in v136); check that v136 prints the
   same and say so in the PR; the metrics json, README and homepage-owner.json must print 0.

6. Commit (trailers "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" and "Claude-Session: https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm"),
   push `see-through-202611020012`, open PR (b):

   Title: homepage: promote owner bundle with See Through 202611020012 (globalgrid2050-homepage <merged sha short>)

   Body:
   Replaces `catalogue/homepage-owner.json` with the pin printed by `python scripts/release_gridatlas.py pin origin/main`
   in globalgrid2050-homepage (commit plus seven SHA-256; only `index.html` and `data/homepage.json` change in the
   bundle). The See Through entry in the Kuiper nest now opens the new See Through: release 202611020012
   (2 November 2026) launches the stable pointer https://ventusltd.github.io/kuiper-belt/see-through/, with the dated
   folder see-through/202611020012/ as its archive; 5 October 2026 (202610050609) stays as an archived release.

   Restore point first, per `homepage_versions/README.md`: `homepage_v137.html` is the currently served homepage
   (`import_homepage_owner.py` output for the pre-edit pin 5a4abe41 at main 18aa446e), with `homepage_v137-metrics.json`
   and a README entry; restore-point workflow <run URL> passed.

   Merging pushes `catalogue/**` to main, which is in `deploy-pages.yml`'s push paths, so the deploy imports the pinned
   bundle. If it does not start: `gh api -X POST repos/Ventusltd/globalgrid2050/actions/workflows/deploy-pages.yml/dispatches -f ref=main`.
   Restore: revert this PR (the previous pin 5a4abe41 returns; v137 is that page byte for byte).

   Context: https://github.com/Ventusltd/neural-link-between-agents/issues/10

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm

## Deploy expectations

1. Merging (a) runs the owner repo's own pages.yml (owner Pages site); the domain does not use it. Nothing on
   globalgrid2050.com changes until (b) merges.
2. Merging (b) pushes `catalogue/homepage-owner.json`; deploy-pages.yml `on.push.paths` lists `catalogue/**`, so
   "Deploy GlobalGrid2050 Pages" starts and runs `python3 scripts/import_homepage_owner.py`. Watch
   `gh api "repos/Ventusltd/globalgrid2050/actions/runs?head_sha=<merge sha>&per_page=10"` for completed success.
   homepage-catalogue.yml also starts on the same push and fails on main today with 4 pre-existing barcode findings; it
   is not a deploy gate. PR checks on (b): "PR file size guard" (passes at this size) and "Public language gate"
   (self-hosted runner, offline since 29 Oct; expect queued).
3. Served-byte checks (from a machine that reaches the domain):
   - sha256 of https://www.globalgrid2050.com/homepage-shell/data/homepage.json = 4aed72cc055ac006bd6a5f894a57a9fd8558709696a96f0e523a5a825daf697a
   - the served root index.html = the import of the new pin; expected (same method as v137): 68 lines, 3474 words,
     52358 characters, 52362 bytes, sha256 5ea40cc002a30fea21f8abca6804f239cebf4cb3b506254410cefbae36faee57
   - Kuiper nest, See Through: "Open See Through" href https://ventusltd.github.io/kuiper-belt/see-through/, which
     lands on see-through/202611020012/ (the pointer is a meta refresh plus location.replace that keeps search and
     hash); catalogue row versions summary "2 November 2026", with 5 October 2026 listed as Archived at
     see-through/202610050609/.
4. Browser caches: the shell fetches data/homepage.json; a hard reload may be needed to see the new release.

## Posted

HANDOFF: https://github.com/Ventusltd/neural-link-between-agents/issues/10#issuecomment-6567576912 (02:25:18Z)

## Limits

- K1 whole-file result is 1 (pre-existing, `cable-selection` entity), not 0; changed lines are 0.
- No phone render run for this change (the launch href change is covered by the fallback diff and homepage-browser.cjs;
  See Through itself was tested by team 12, Pixel 7 only, Galaxy S24 not run, as LINK-12 recorded).
- Served bytes not checked from this sandbox (proxy refuses ventusltd.github.io and globalgrid2050.com).
