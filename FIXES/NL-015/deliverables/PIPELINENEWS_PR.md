# PR description: Ventusltd/pipelinenews: REPD October 2026 (Q3) register release 202611132345-pipelinenews

Title: `release(intelligence): 202611132345-pipelinenews — REPD October 2026 (Q3) register refresh (not promoted)`

Base: `main` (built against clone head 67aa2eb). Branch: one new branch chosen by the harness. Open it as a **draft**.

## What this adds
- `releases/202611132345-pipelinenews/` (89 files). This is a new immutable release whose parent is
  `202609060232-pipelinenews`. It was cut by the repo's own `tools/intelligence/release_builder.py
  --from 202609060232-pipelinenews --cartridge repd-2026q3-register --gen 202611132345`.
- `tools/intelligence/cartridges/repd-2026q3-register/`: cartridge.json plus 18 data files (16 spine partitions of
  15 x 500 + 275, and the fast projects and search indexes).
- `tools/intelligence/register_refresh.py` (new). It ports `compileProjects`/`searchText` from
  `index/202608270055-compile-v8-fast.mjs`, because that script hard-asserts 7680/14657/16 and cannot be rerun.
  `--prove-q2` recompiles the shipped Q2 indexes byte for byte.
- `tools/intelligence/release_builder.py` (modified). Adds a `registry_core` cartridge block. All five keys (totals,
  source, assets.projects, assets.search, detail_partitions) must be replaced together, and any other key is refused.
  sha256, bytes and record_count are derived from the files. Totals are recomputed from the partitions and must equal
  the declaration. The old and new digests are recorded in `registry_core_replaced`.
- `tools/intelligence/release_hash_guard.py` (new): proves that no existing release byte changed.
- `tools/publication/test_register_refresh.py` (new, 18 tests).

Full list, 112 paths: `pipelinenews_pr_file_list.txt` (the `{GEN}` placeholder in the cartridge file names is literal;
the builder substitutes it).

## Figures (DESNZ REPD Q3 2026, October 2026)
- 14,967 unique Ref IDs. The official CSV has 14,968 rows: ref 7679 appears twice, identical, and is removed once.
- Spine at >=1 MW, solar/BESS/onshore/offshore: **7,775 records, 365,474.49 MW**, largest 4,100 MW.
- Split: 3,604 solar, 1,644 BESS, 2,417 onshore, 110 offshore. 7,749 valid geometry, 26 missing.
- Against Q2: 101 new refs and 6 dropped (5 absent from October, 1 now blank capacity), net +95.
- Capacity precision is the official XLSX value, as in Q2. 23 solar sites published as "1" in the CSV are 0.996 to
  0.99975 MW in the workbook. They stay outside the >=1 MW scope and are recorded as `candidate_delta`
  (held, fail-closed).
- Independently verified by NL-015 Team 3: the 16 partitions hold 7,775 unique refs and 365,474.49 MW, and they are
  field-for-field identical to the globalgrid2050 candidate spine `uk_renewables_pipeline/202611132345/data/v9.1`
  (0 differing fields).

## Tests
- `sha256sum -c sha256sums.txt` inside the release: OK (re-run by Team 3).
- `release_builder.py --check 202611132345-pipelinenews`: 36 PASS, 0 FAIL (re-run by Team 3).
- `pytest tools/publication/test_register_refresh.py`: 18 passed (re-run by Team 3).
- Other suite results reported by the builder (not re-run here):
  - `pytest tools/publication`: 75 passed. The 2 failures need git history and are pre-existing.
  - atlas selfTest 16/16, render_proof 26/26, sector_render_proof 11/11, surface_truth_proof 8/8,
    v6_deep_link_cartridge 29/29.
  - `v8_neutral_surface.py` crashes on parent and child alike (pre-existing).
- Headless Chrome on localhost (Team 3), desktop 1440 and mobile 390:
  - shows "7,775 of 7,775 records" with the Q3 text;
  - `?repd_ref=21073` (new in Q3) shows "1 of 7,775 records";
  - the parent shows "7,680 of 7,680" with the same console profile.
  - The only failed requests were external, because this workspace has no outbound browser access.
- `release_hash_guard.py --verify`: 2,618 existing release files unchanged; 89 new files, all inside the new folder.

## Not done, and why it matters
- **Not promoted.** `releases/current-v4.json` and `state/live-set.json` still point at 202609040144.
  `deployment: not-authorised`.
- Pages classifies this as `source-only`: additive-cartridge releases are not published by pipelinenews Pages.
  Publishing means a separate globalgrid2050 PR that copies the folder to `pipelinenews_intelligence/202611132345/`.
  That PR is not part of this one.
- **Carried over from Q2:** grid proximity and distance, locality, substation, project intelligence, wider fleet and
  provisional projects. The page says so. 14 carried grid measurements belong to refs whose coordinates moved
  between Q2 and Q3, so they are stale.
- **REPD 18561/18562** (Salters Lane, Tyne and Wear) have published coordinates near High Wycombe. They are kept as
  published.
- **The existing workflow `202608311458-build-intelligence-release.yml` defaults to `push: true`** and runs
  `git push origin HEAD:main`. Do not dispatch it for this release with push enabled.

Nothing in this PR changes an existing release, pointer, homepage or the globalgrid2050 repository.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015ELZDCCoxh5As4wURAS8rx
