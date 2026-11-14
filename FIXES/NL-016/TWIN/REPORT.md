# TWIN engineer report: GridAtlas 202611132345 (v9.189), NL-016

Base: Ventusltd/gridatlas main b0a3a938. Nothing was pushed, merged or dispatched. Patches only.

## Result
**202611132345 is reproducible byte for byte from repd-2026q3.csv** (sha256 d937ae16…e4b9, 5,201,029 B), both from the
local file and from the commit-pinned URL (globalgrid2050 07b6d517). Two builds in empty directories agreed with each
other and with the committed files (duckdb 1.3.2, pyproj 3.7.2, Node 22.23.4):

| file | bytes | sha256 |
|---|---|---|
| data/repd_projects_202611132345.parquet | 1,488,420 | cc9b7f04…d789 |
| data/repd_browser_registry_202611132345.json | 9,551,352 | fdda9b6e…8f58 |
| data/repd_v9_manifest_202611132345.json | 4,572 | b90bda5a…f3fb |
| atlas/cartridges/202611132345-place-global-search-v9-5.js (+ parts manifest) | 41,115 | a27a11c4…a619 |
| atlas/modules/202611132345-uk-offtakers-overlay.js | 71,191 | eee30014…fdb6 |

Evidence: `local-runs.log` (network twin 11/11, network keys 10/10), `pr-gate.log` (18/18 with the patches applied).

## Patches (apply in order to main b0a3a938; `git apply --check` clean on a fresh worktree; 12 files, additive apart from 4 edits)
- `patches/0001-twin-preservation-keys-tools.patch`: `tools/twin/` (replicate-generation.mjs, preserve.mjs, keys.mjs,
  lib.mjs, sources.json, keys/202611132345.json, .txt, -pipeline-news-refs.tsv) and a section in docs/CI.md.
- `patches/0002-twin-ci-wiring.patch`: tools/ci/pr-gate.mjs (three offline checks when a PR touches atlas/, data/,
  compiler/ or tools/), a `twin` job in pr-file-size-guard.yml (`needs: cartridge-gate`, then network), and
  `mode=twin` in 202608301321-verify-live.yml (dispatch). **No new workflow file**; ACTIVE_WORKFLOWS, STATE.md,
  atlas/current.json, the loader, every cartridge and every data file are untouched (`loop.mjs lint` PASS, state parity).

## Checks, run locally
- Preservation: 224 cartridge pins of 53 generations hold; 63 files of 3 release sha256sums verify; both data
  manifests hold; 116 assembled cartridges hold; 202610312138 is published and composes through its own loader
  (6 cartridges hash-verified); nothing under the published roots changed against origin/main.
- Keys: 10 of 10 claims hold (`keys-202611132345.txt`).
- Mutations that must turn it red, and did (exit 1, file named): wrong source byte (refused, "Not used"); one byte in
  the committed parquet; registry and manifest edited together; an old cartridge edited; atlas/v/202610312138 removed;
  offtakers source edited (differs at byte 33450); a ref dropped from the list; compiler constant edited (registry
  differs at byte 9551242, manifest at byte 118).

## Two claims do not hold as worded; the register states what is true
- "Nearest-substation results unchanged for retained refs": true for 10,982 of 11,001 retained refs (identical
  coordinate, and the engine files are identical: sld-sandbox 78129536…, substations 87976435…). 19 refs were moved by
  the register (12 by more than 5 km) and now measure to a different point; they are listed in K08.
- "Every October Pipeline News ref resolves": 5,331 of 7,775 resolve by exact ref. 2,444 do not because the snapshot
  keeps the four active statuses; 3 of those are active in Pipeline News and still have no record (2484, 6483, 20218:
  longitude beyond the compiler's 2.5 E limit).

## Pre-existing, reported and not failed
175 part or module files no longer hash to what older parts manifests recorded, and 3 composition manifests from
before atlas/v/ existed name a cartridge that changed. The assembled cartridges and all published pointers hold.

## Not verified
- The two workflow changes have never run on GitHub (runner pip wheels, proxy-free curl). YAML parses; steps were run by hand.
- The live site and any real phone or desktop journey: unreachable here. Requests to ChatGPT are in the HANDOFF.
- The lightning overlay still reads the Q2 records (by design of the release); the twin does not cover it.
- A later generation that marks 202611132345 "historical" in tools/offtakers/generations.json will be held by hash
  only: the twin then says so in a note rather than rebuilding it.
