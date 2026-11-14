# Homepage pointer change for Pipeline News 202611132345 (exact instructions; do only AFTER owner acceptance)

The repository Ventusltd/globalgrid2050-homepage is not cloned here. I read its two data files read-only at the
pinned commit `9914285b691766c8f20b25fc83147f59c0389938` (raw.githubusercontent.com). Their sha256 values match
`catalogue/homepage-owner.json`:
- data/homepage.json: 3226e596a8c998b461a13a09773fe5fe7938fc14123807ef294e2d8c9f8c7917
- data/active-pages.json: 4ee017277a6e0a7a5e92b5320486cdf908300ac34629d71249d53b0e4d31fdeb

The owner repository's main may have moved past the pin. Apply the change to its current main and re-check the
context lines below.

Preconditions:
1. globalgrid2050 PR #57 is merged, so `uk_renewables_pipeline/202611132345/` is on main.
2. Pages has deployed it.
3. The owner has checked `https://globalgrid2050.com/uk_renewables_pipeline/202611132345/` in a browser (desktop and mobile).

A pointer change does not accept the application (AGENTS.md).

## Step 1: owner repository (globalgrid2050-homepage), `data/homepage.json`
Exact diff against the pinned bytes: `patches/P3-homepage-owner-data-homepage.json.diff`.
- In entity `"id": "pipeline-news"`:
  - set `"operative_release_id": "202611132345"`;
  - insert this as the FIRST element of `releases` (newest first, as in entity `kuiper`), keeping the
    202609082224 element unchanged after it:
  ```json
  {
    "id": "202611132345",
    "label": "13 November 2026 · REPD October 2026",
    "url": "https://globalgrid2050.com/uk_renewables_pipeline/202611132345/",
    "published_at": "2026-11-13T23:45:00Z",
    "status": "available",
    "source_ref": "https://github.com/Ventusltd/globalgrid2050/tree/<MAIN_MERGE_SHA>"
  }
  ```
  `<MAIN_MERGE_SHA>` is the globalgrid2050 main commit that contains the folder, as the existing entry uses
  `7c64560d…`.
- Append to `promotions`:
  `{"entity_id":"pipeline-news","from_release_id":"202609082224","to_release_id":"202611132345","reason":"<owner's words>","promoted_at":"<UTC>"}`.
- `data/active-pages.json`: lines 17 and 163 carry the 202609082224 URL. This file is owner-generated (an activity
  feed), so regenerate it with the owner's own tool rather than editing it by hand. It does not promote anything
  (AGENTS.md).
- Run the owner's `scripts/releases.py` validation (UNVERIFIED here: not cloned). Merge, and record the new owner
  commit SHA.

## Step 2: this repository (globalgrid2050), restore point v139
- The highest existing restore point is `homepage_versions/homepage_v138.html` (`ls homepage_versions`). The next
  number is **v139**; confirm it is still the highest at edit time.
- Create `homepage_versions/homepage_v139.html` as the currently served homepage, assembled by
  `scripts/import_homepage_owner.py` from the CURRENT pin 9914285b…, before any change. Also create
  `homepage_v139-metrics.json` (entries_before, lines, words, characters, bytes, sha256, intention) with
  `scripts/measure_homepage_version.py`, and add a `## Version 139` README section.
- Run `homepage-restore-point-check.yml` (workflow_dispatch) or record why not, as v138 did.
- Never rewrite v001–v138, homepage_v127.html or homepage-before-four-nests-20260925.html.

## Step 3: pinned manifest `catalogue/homepage-owner.json`
- `"commit"`: the new owner commit SHA.
- `"files"`: replace the sha256 of every file that changed at that commit. Normally that is `data/homepage.json`,
  plus `data/active-pages.json` if it was regenerated. Compute each with
  `curl -sSf https://raw.githubusercontent.com/Ventusltd/globalgrid2050-homepage/<sha>/<file> | sha256sum`.
  Leave the other five values untouched if their bytes did not change.

## Step 4: deploy and served-byte verification
- deploy-pages.yml runs the importer on push to main. Afterwards compare sha256 of
  `https://globalgrid2050.com/homepage-shell/data/homepage.json` with the new pinned value, and check that the
  served `https://globalgrid2050.com/` "Open Pipeline News" href is `…/uk_renewables_pipeline/202611132345/`.

## Rollback
Revert `catalogue/homepage-owner.json` to commit 9914285b… and its seven hashes. The operative folder 202609082224
is unchanged and stays served.

## Optional, not required
Append 202609082224 (and the other missing September releases) to `historical_builds.html`. Append only; never
rewrite rows.
