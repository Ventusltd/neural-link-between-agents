# dc-a7: Wapseys Wood is one site; merged pipeline 226 records, 225 with geometry (NL-007)

Wapseys Wood (PINS EN0110030) appeared twice in `datacentres/lanes/dc-a7-merge/out/uk_datacentre_pipeline.geojson`. This
PR merges it into one record. The published baseline goes from 227 records to 226, and 225 of them have geometry (unchanged). The one record without geometry is Ebbsfleet.

Channel: [NL-007](https://github.com/Ventusltd/neural-link-between-agents/issues/7).
Plan: [neural-link `FIXES/202610311905-datacentre-baseline.md`](https://github.com/Ventusltd/neural-link-between-agents/blob/main/FIXES/202610311905-datacentre-baseline.md) (§3.1, §4.1, §7 P1–P3).

## Cause

The cause is that the operator comparison in `operator_match` was exact on `norm_operator`. A parenthesised gloss was therefore treated as a different operator. Line numbers are in `datacentres/lanes/dc-a7-merge/dcmerge.py` at b57c94d:

- `:87-88` `norm_operator` keeps the tokens of "(SDC Capital Partners)".
- `:122-128` `operator_match` is exact equality on `norm_operator`, so "Slough Holdings UK Limited (SDC Capital Partners)" and
  "Slough Holdings UK Limited" were two operators.
- `:262-267` `cannot_link` treats `operator_match(...) is False` as a hard, cluster-wide split before the URL and name rules run.
  The dc-a3 record and the dc-a2 s35 record of the same site therefore never linked.

## Change

- `dcmerge.py`: a new `_op_core(s)` (`:122-125` after the change) replaces `\([^)]*\)` with a space. `operator_match` (`:128-129`) now compares
  `norm_operator(_op_core(a))` with `norm_operator(_op_core(b))`. Equality stays exact. The canonicalisation is in
  `operator_match` only: `norm_operator`, `geo_key` (`:228-232`, which embeds `norm_operator`), `site_key` and every other site id
  are untouched.
- `test_dcmerge.py`: the new test `test_parenthesised_operator_gloss_is_not_a_split` checks that one operator, with and without a gloss, merges
  in both input orders: one site, two sources, exact_site, 300 MW counted once, no `operator_disagreement`. It also checks that
  `operator_match("Digital Realty", "Global Technical Realty")` stays `False`. `test_operator_match` and the three
  cross-operator tests are unchanged.
- Rebuild: `python3 pipelines/run_lanes.py build datacentres --lane dc-a7-merge`, run twice; the two outputs are `cmp`-identical.

## Measured

- `cd datacentres/lanes/dc-a7-merge && python3 -m unittest test_dcmerge`: **Ran 53 tests, OK** (52 at b57c94d). Measured by P1-I
  and re-run by P1-V on NL-007.
- `out/uk_datacentre_pipeline.geojson`: sha256 `87337db5d3bf7959f7f605d3abd029dd4196ab24a79107ceb95210c5b7751654`,
  **446,550 B** (was `176c1b2e…2d89`, 447,511 B).
- **226 features, 225 with geometry, 1 unplaced** (Ebbsfleet, status `unknown`).
- Ids compared with the 227-record file at b57c94d: **gone {`dcuk-bf4650ea1c4a8a0b`}, new {}**. No other id moves.
- `dcuk-4ad498e7880d6ba4` (Wapseys Wood) keeps its id, its point (exact_site, [-0.59697, 51.58696]) and its operator string
  "Slough Holdings UK Limited (SDC Capital Partners)". Its `location.source_id` is
  `dc-a3-gov:MHCLG; Planning Inspectorate:gov-s35-wapseys-wood`. It now has 2 sources: it gains `out:s35-seed:dc-a2:s35:EN0110030` by
  rule `evidence_document`. Its conflicts are `[]`.
- metadata.summary changes, each caused by this one merge: sites 227→226; in_planning 8→7; it_load_mw_known 5→4;
  sum_it_load_mw_known 1632→1332; OGL-UK-3.0 29→28; sites_from_several_lanes 2→3.
- `out/uk_datacentre_pipeline.rejects.json` is **unchanged** (`dcf72c03…211f`, 2,117 B) and is not in the diff.
- `datacentres/lanes/MANIFEST.json`, as `run_lanes.py build` writes it in the tool's canonical two-space form: the raw diff
  is 236 lines and `git diff -w` shows 6 insertions and 6 deletions, which are the three pins:
  - `:99-100` `dcmerge.py` 22,845 B `f63ac9e2c29f4268d98b1488b47a2af5da5d36ef20b0299c0062e19c634c7c60`
  - `:107-108` `out/uk_datacentre_pipeline.geojson` 446,550 B `87337db5d3bf7959f7f605d3abd029dd4196ab24a79107ceb95210c5b7751654`
  - `:115-116` `test_dcmerge.py` 29,292 B `08c21f2fa094fa6a442018b63ae9173d9457ac45c8a53feeb0be813d893d77a1`
  - `:111-112` (rejects) unchanged.
- `python3 reproduce.py check --json r.json`: exit 0, `mismatches: []`, lanes dc-a2, dc-a3, dc-a4 and dc-a7 `rebuilt=identical`,
  **summary_sha256 `720a435c23ac7302e0952452a2575f7e684aad4432544b69d8899f48dad1168e`**. This was measured locally with Python 3.13.18. Lane dc-a6 is
  `skipped_missing_input` locally. CI's `requirements` leg downloads its inputs, so that leg's digest can differ from this one.

## Checks run on this branch (HEAD `75ab8ae`)

| command | result |
|---|---|
| `python3 ci/verify.py` | exit 0, 8 `ok` lines incl. `lanes ok (6 vendored lanes, every file pinned)` |
| `python3 -m unittest discover -s tests` | `Ran 35 tests`, `OK` |
| `python3 reproduce.py check --json r.json` | exit 0, `summary_sha256 720a435c…168e` |
| `git bundle verify 03-data-grid-gb.bundle` | `is okay`; contains `75ab8ae…` `refs/heads/fix/nl007-operator-canon`; requires `b57c94d…` |

The full outputs are in neural-link
[`FIXES/202610311905/patches/03-checks.txt`](https://github.com/Ventusltd/neural-link-between-agents/blob/main/FIXES/202610311905/patches/03-checks.txt).
Each step was independently re-run by a verifier on NL-007: P1-V and P2-V PASS, and P3-V re-runs these checks from a fresh clone and the bundle.

## Commits

1. `f8258a01978a4b6f29dd2a248864a6283f18c02a` dcmerge: canonicalise operator inside operator_match only (NL-007 P1)
2. `75ab8ae54e95b90bb59e306b4ca3a08042430ce5` dc-a7: rebuild merged pipeline, 226 records 225 with geometry (NL-007 P2)

## Out of scope (separate issues; not changed here)

- `docs/METHODS.md:118` says 190 and `counts.json` says 212. This is a documentation issue and touches no pinned byte.
- Lane id "out": `dcingest.py:398` takes `basename(dir)`, so lanes passed as `…/out` are recorded as lane "out" (231 of 258 source
  entries). Fixing it rewrites 231 source ids and needs its own reviewable change.
- `licence_status: unverified` on all 258 source entries (`dcingest.py:260-267`, declared as a caveat). Fixing it needs a lane-level verification pass, not a merge change.
- The Cowley pin: gridatlas's substation-intelligence cartridge is pinned at data-grid-gb `1c9909d`. Moving that pin is a later generation (G2) with its own plan,
  and it first needs a deterministic network writer here.

After this merges, gridatlas vendors the file at the merge commit, re-pins `DCF`/`DCFSHA` and cuts its preview generation
(plan steps P4–P10). Nothing in gridatlas changes in this PR.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm
