# P4-I: merge evidence for data-grid-gb PR #7 (NL-007)

Measured 2026-10-31 from the clone after `git fetch origin main`. The data-grid-gb `origin/main` is M.

## The merge commit M

| key | value |
|---|---|
| M | `01a4491dc66ec4e6319a05a394926043b9d992f9` ("Merge pull request #7 from Ventusltd/fix/nl007-operator-canon", committer GitHub <noreply@github.com>) |
| parent 1 (base) | `b57c94d4e964df2de0dea2786781c6d07a967ea1` |
| parent 2 (branch tip) | `75ab8ae54e95b90bb59e306b4ca3a08042430ce5` |
| committer date | `2026-10-31T21:33:27+00:00` |
| **S** (committer UTC minute) | **`202610312133`** (`TZ=UTC git log -1 --format=%cd --date=format-local:%Y%m%d%H%M 01a4491`) |
| tree of M vs 75ab8ae | `git diff --stat 75ab8ae 01a4491` is empty: the merge brings in exactly the branch tree |
| PR | https://github.com/Ventusltd/data-grid-gb/pull/7 (merged 2026-10-31T21:33:28Z, base `b57c94d`, head `75ab8ae`, 2 commits, 4 files) |

## The file at M

`datacentres/lanes/dc-a7-merge/out/uk_datacentre_pipeline.geojson`

| check | command | measured | plan (§2, §7 P2) |
|---|---|---|---|
| sha256 | `git show 01a4491…:<path> \| sha256sum` | `87337db5d3bf7959f7f605d3abd029dd4196ab24a79107ceb95210c5b7751654` | same: PASS |
| bytes | `git show 01a4491…:<path> \| wc -c` | 446,550 | 446,550: PASS |
| features | `jq '.features\|length'` | 226 | 226: PASS |
| with geometry | `jq '[.features[]\|select(.geometry!=null)]\|length'` | 225 | 225: PASS |
| git blob | `git rev-parse 01a4491:<path>` | `2b62e7ae829743e5271881864d8e60a754abd6c7` (the same blob as at `75ab8ae`) | n/a |

Raw file at M:
https://raw.githubusercontent.com/Ventusltd/data-grid-gb/01a4491dc66ec4e6319a05a394926043b9d992f9/datacentres/lanes/dc-a7-merge/out/uk_datacentre_pipeline.geojson

## CI: `test-assets.yml` ("Test the asset pipelines")

These are the check runs on the PR head `75ab8ae`, read through the GitHub API (`pull_request_read get_check_runs`; `actions_get get_workflow_job`/`get_workflow_run`).

Pull-request run 41244063192 (run #51, event `pull_request`, conclusion `success`): https://github.com/Ventusltd/data-grid-gb/actions/runs/41244063192

| leg | job | conclusion | started → completed (UTC) |
|---|---|---|---|
| test (requirements) | https://github.com/Ventusltd/data-grid-gb/actions/runs/41244063192/job/124663718734 | **success** (steps 1–10 success) | 21:32:28 → 21:32:40 |
| test (bare) | https://github.com/Ventusltd/data-grid-gb/actions/runs/41244063192/job/124663718827 | **success** (steps 4 and 9 skipped by design, the rest success) | 21:32:28 → 21:32:43 |

Push run 41244000905 (run #50, event `push`, same head `75ab8ae`, conclusion `success`): test (bare) job 124663539518 success; test (requirements) job 124663539258 success.

Both legs were green before the merge at 21:33:28Z.

## Hand-on to P6

gridatlas will vendor this exact blob (sha256 `87337db5…1654`, 446,550 B, at M `01a4491`) as
`data/uk_datacentre_pipeline_202610312133.geojson` (`data/uk_datacentre_pipeline_<S>.geojson`, S = `202610312133`). The `DCFSHA`, the MANIFEST
pin and the vendored file must all carry `87337db5d3bf7959f7f605d3abd029dd4196ab24a79107ceb95210c5b7751654` (plan §6 risk 2). G must be later than S.
