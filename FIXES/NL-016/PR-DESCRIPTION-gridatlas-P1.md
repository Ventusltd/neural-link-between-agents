# 202611132345-gridatlas-v9.189 preview: REPD search and record snapshot re-pinned to October 2026 (Q3), data-only

Draft preview PR. Nothing in it moves the live route: `atlas/current.json`, `STATE.md`, `atlas/index.html` and
`atlas/releases/**` are byte-identical to main `41729af`. Releasing it needs the owner's `ACCEPT 202611132345` and the usual
`release-accepted.mjs` path (docs/RELEASE.md steps 3 to 5). Agents do not record acceptance.

## What changes
- New records snapshot `data/repd_projects_202611132345.parquet` (sha256 `cc9b7f04…`, 11,329 rows, one per REPD ref) and
  manifest `data/repd_v9_manifest_202611132345.json` (`b90bda5a…`). They are compiled by `compiler/202611132345-compile-atlas-v9.py`,
  which is the 202608290716 compiler with only its pins changed. The input is the cleaned October CSV, `repd-2026q3.csv` on
  globalgrid2050 main (sha256 `d937ae16…`, 14,967 rows, UTF-8, CSV capacity precision; official CSV `48e76c49…`). The browser
  registry is `data/repd_browser_registry_202611132345.json` (9.55 MB, added to the large-files allowlist).
- Under GridAtlas's own filter (active statuses, lon -9..2.5, lat 49..61), 11,329 rows are kept against 11,069 for Q2. The
  incumbent comparison gives +328 refs, −68 refs and 1,166 changed, classified VERIFIED_NO_DATA_REGRESSION.
- Two cartridges are re-cut for the new URL, hashes, closure counts and card wording only:
  - `uk-gazetteer-flyto`: `atlas/cartridges/202611132345-place-global-search-v9-5.js` with its parts manifest and REPD part;
  - `uk-offtakers-overlay`: module `atlas/modules/202611132345-uk-offtakers-overlay.js`, rebuilt byte for byte from
    `tools/offtakers/src`.
- **The lightning overlay is unchanged** (module 202610291043, cartridge identity 202610312138). Its REPD record lookup stays on
  the 202608290716 snapshot until a separate lightning cut (see "Why two steps").
- Test-only: `tools/ci/lightning/overlay-engine.test.mjs`. Tests 80 (H3/I1/J2) and 98 (J3) were clock-dependent and fail on
  main today. 80 used a fixed flash date (2026-10-25) that left the 7D window about 7 days later. 98's collector regex had no
  optional date, so it failed from 00:00 to 00:10 UTC. Both are fixed without weakening the assertions.
  `tools/ci/offtakers/overlay-offtakers.test.mjs` fixtures follow each module's own pinned snapshot (M5-3 expects 10,503 for
  the live module and 10,423 for the new one).

## Gates (local, offline, at this file set)
`node tools/ci/pr-gate.mjs --base HEAD`: **19/19 PASS**. That covers lint, state parity, the compositions 202610312138 and
202611132345, the proofs for the gazetteer, offtakers and both live lightning/offtakers generations, run-current,
verify-compose, loader registry and equivalence, the lightning and offtakers source rebuilds, the lightning suites (207 pass,
10 skipped), the offtakers suites (30/30 for each pair) and release-tools. The data-contract parity proof shows the same three
pre-existing FAIL rows as main and no new ones. Double build A/B is byte-identical. atman verify: VERIFIED. Fly-to contract:
8/8. `atlas/releases` 100/100 and `atlas/v` (52 generations) are unchanged.

Not run here: the rendered browser audits (`atman/*rendered-browser-audit.mjs`, `*.browser.mjs`), the live-bytes and served
checks, and `release-generation.mjs --check`. The last needs this PR on main.

## Why two steps (owner decision)
The single-generation preview (gazetteer + lightning + offtakers, 27 files) fails one gate:
`202611132345-uk-lightning-overlay.proof.mjs`: `uk-gazetteer-flyto differs from 202610291043`. The lightning proof
(`tools/proofs/lightning-cartridge.mjs`) checks arrival parity against a monolithic reference composition. It requires every
script before sld-sandbox to be byte-identical to the reference, and sld(R) + '\n' + overlay(G) to equal the reference
sld-sandbox. A data re-pin breaks both conditions: it changes the gazetteer, which comes before sld-sandbox, and it changes the
lightning module. No monolithic reference with the new gazetteer exists, and `make-generation.mjs` cuts lightning against the
live composition. Two ways forward:
1. **This PR, then a lightning-only cut (recommended).** After 202611132345 is live, cut the lightning re-pin with
   `tools/lightning/make-generation.mjs` (monolithic M + modular G, parity reference M). The proof then passes as designed,
   because the gazetteer in M equals the live one.
2. One generation, with an amended `lightning-cartridge.mjs` that accepts declared co-changed cartridges and a changed module.
   That is a tooling change to a proof, so it needs the owner.

## Capacity precision (settled)
The records join that the lightning and offtakers cards use (point within 1e-6 degrees, same name, same MW, same technology)
matches the drawn register. That register is data-gridatlas `repd_master_v8_oracle`, the same rows as globalgrid2050
`dist/repd_master.json`, 10,784 rows. Its capacities carry at most 3 decimals: 0 dp 4,380, 1 dp 3,527, 2 dp 2,872, 3 dp 5.
Joined rows: Q2 snapshot **10,503**; October at CSV precision **10,423**; October at XLSX full precision **8,973**. XLSX
precision breaks exactly 1,450 of the 10,423 CSV-precision joins (for example 0.384 against 0.38, 24.995 against 25). The
remaining −80 against Q2 is real register change (86 lost, 6 gained): 45 refs left the active statuses, 24 MW changed,
12 points moved, 4 names changed, 1 point and MW. **Rule: compile GridAtlas from the CSV-precision file. Never feed the XLSX or
staged full-precision values.**

## Known limitations carried into this preview (pre-existing on main, not introduced here)
- 36 active records with blank X/Y are converted from BNG (0,0) to the false origin (-7.55716, 49.766807). That point is inside
  the box, so they stay in the snapshot. The gazetteer (`hasSafeMapPoint`), the sld-sandbox arrival
  (PLACEHOLDER_COORDINATES_FALSE_ORIGIN) and the offtakers overlay all refuse that point, so the result is NO MAP, not a false
  location. 15 of the 36 are offshore. 6 of them have a Crown Estate lease point in `atlas/data/offshore-coordinates.json`,
  which still pins the January file. 7 offshore projects new since January (10920, 11613, 13417, 13428, 13432, 13735, 21087)
  have no lease point.
- The compiler rule `biomass > 100 MW → /1000` rescales 7 real plants: Drax units 1 to 4 at 645 MW become 0.645, Lynemouth
  420 → 0.42, Upper Bighouse 260 → 0.26, BAEF 102 → 0.102. The same rule is in globalgrid2050 `scripts/repd_updater.py`, so the
  drawn register agrees and the join still holds. Fixing it means fixing both together.
- Blank capacity is written as `capacity_mw` 0.0 (1,126 rows; the schema has NOT NULL). The cards say "no stated capacity, never
  shown as 0 MW", but the data column cannot tell the two apart.
- The drawn REPD layer stays the April (Q1) data-gridatlas partition, and the card says so. Refs 18561/18562 (Salters Lane,
  Tyne and Wear) sit near High Wycombe in the October source.
