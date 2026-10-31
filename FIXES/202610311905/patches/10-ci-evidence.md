# P10-I: CI evidence for gridatlas PR #80 (NL-007)

Read on 2026-10-31 at about 22:27 UTC through the GitHub API (`pull_request_read get` and `get_check_runs`, `get_job_logs`, `actions_list list_workflow_run_artifacts`, `gh api .../actions/runs/41247942683`). Generation G = `202610312138`.

## PR and run

| key | value |
|---|---|
| PR | https://github.com/Ventusltd/gridatlas/pull/80 (open, **draft**, mergeable_state `clean`, 13 files, +2,385 / -12, 5 commits) |
| head | `preview/202610312138-gridatlas-v9.188` at **`5ec7f62f213e2d20a02e86427daa182c0f38e4a4`** |
| base | `main` at `cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e` |
| run | https://github.com/Ventusltd/gridatlas/actions/runs/41247942683 ("PR file size guard and cartridge gate", run #175, event `pull_request`, head_sha `5ec7f62…`, status `completed`, conclusion **success**, 22:23:05Z → 22:25:32Z) |

## The three jobs

| job | URL | conclusion | started → completed (UTC) |
|---|---|---|---|
| size-guard | https://github.com/Ventusltd/gridatlas/actions/runs/41247942683/job/124675181094 | **success** | 22:23:08 → 22:23:17 |
| cartridge-gate | https://github.com/Ventusltd/gridatlas/actions/runs/41247942683/job/124675181125 | **success** | 22:23:08 → 22:25:31 |
| dc-browser-smoke | https://github.com/Ventusltd/gridatlas/actions/runs/41247942683/job/124675180840 | **success** | 22:23:08 → 22:24:17 |

## Quoted log lines

### size-guard

```text
2026-10-31T22:23:11.3735991Z   BASE_SHA: cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e
2026-10-31T22:23:14.4345283Z checked 13 added/modified files against a 5 MB limit
2026-10-31T22:23:14.4346195Z All files within budget.
```

### cartridge-gate

```text
2026-10-31T22:23:14.2131303Z ok   202610312138: 71191 B sha256 1be368f53b04f4f451c0559ca6c534d3f8301ad9df158cc6dd94308517c5cf46 rebuilt byte for byte
2026-10-31T22:24:43.7755469Z PASS offtakers 202610292044 + lightning 202610291043 overlay-offtakers.test.mjs  pass 30 fail 0 skipped 0 40.3 s; atlas/current.json
2026-10-31T22:25:24.0128406Z PASS offtakers 202610312138 + lightning 202610291043 overlay-offtakers.test.mjs  pass 30 fail 0 skipped 0 40.2 s; atlas/v/202610312138/current.json
2026-10-31T22:25:28.9145072Z 19/19 checks passed
2026-10-31T22:25:28.9169326Z ##[notice]19/19 passed; generations 202610292044, 202610312138; ...
```

Other rows in the same log: lightning 202610291043 overlay-engine `pass 207 fail 0 skipped 10`, overlay-latest `pass 8 fail 0`, release-tools `pass 16 fail 0`, loader-registry `53 served loader(s)`. These are the same numbers as the local gate in `09-pr-gate.log`.

### dc-browser-smoke

The run step and the generation it opened:

```text
2026-10-31T22:23:37.1727431Z ##[group]Run node tools/ci/offtakers/browser-dc-smoke.mjs
2026-10-31T22:23:37.1750305Z   DC_SMOKE_GENERATION: 202610312138
```

One `BROWSER DC SMOKE PASS` line at 22:24:12.5634705Z covers both viewports. Here are the parts that matter, quoted from the line (each site/tab text field shortened to `…`):

```text
BROWSER DC SMOKE PASS {"observations":[
  {"viewport":[393,852],"site":"Data centre (screening)…Digital Realty LHR26 · Digital Realty…Nearest 400 kV 8.86 km · Iver","tabs":4,"initial":{"errors":[]},…,"csv_bytes":19008,
   "additional_taps":[{"name":"Court Lane Industrial Estate, Iver (SL0 9HL)","tab_count":4,"has_unknown_statement":true},{"name":"Cobalt Park Data Centres","tab_count":4,"has_unknown_statement":true}]},
  {"viewport":[1280,800],"site":"…Digital Realty LHR26…","tabs":4,"initial":{"errors":[]},…,"csv_bytes":19008,
   "additional_taps":[…same two sites, tab_count 4…]}],
 "errors":[]}
```

So: viewports `[393,852]` and `[1280,800]`, `"tabs":4` at both, `"initial":{"errors":[]}` at both, and top-level `"errors":[]`.

Artifact upload:

```text
2026-10-31T22:24:12.6650149Z   name: dc-browser-smoke-41247942683
2026-10-31T22:24:12.6650483Z   path: /home/runner/work/_temp/gridatlas-dc-browser/
2026-10-31T22:24:12.8572414Z With the provided path, there will be 2 files uploaded
2026-10-31T22:24:13.9135615Z SHA256 digest of uploaded artifact zip is bd488435e9faffc178dc58a38549d5b3238bee4fd2381f4b723d2881901295bc
2026-10-31T22:24:14.3386287Z Artifact dc-browser-smoke-41247942683 has been successfully uploaded! Final size is 337251 bytes. Artifact ID is 13060655237
2026-10-31T22:24:14.3393909Z Artifact download URL: https://github.com/Ventusltd/gridatlas/actions/runs/41247942683/artifacts/13060655237
```

## Artifact

| key | value |
|---|---|
| name | `dc-browser-smoke-41247942683` (id 13060655237) |
| size | 337,251 B |
| digest | `sha256:bd488435e9faffc178dc58a38549d5b3238bee4fd2381f4b723d2881901295bc` (the API's listing matches the log) |
| expires | 2027-01-29T22:23:05Z |
| files | 2 (log: "there will be 2 files uploaded") |
| PNG names | `dc-393x852.png` and `dc-1280x800.png`. The log does not list file names. The names come from the source at `5ec7f62`: `tools/ci/offtakers/browser-dc-smoke.mjs:98` writes `page.screenshot({path:path.join(OUT,\`dc-${width}x${height}.png\`)})` with `OUT = $RUNNER_TEMP/gridatlas-dc-browser` (line 17), which is the uploaded path. |

**Download not possible from this session.** `actions_get download_workflow_run_artifact` returned a signed URL on `productionresultssa4.blob.core.windows.net`. Both `curl` and `gh run download` got `403 Forbidden` from the session's egress proxy (`CONNECT tunnel failed, response 403`). The file list and PNG contents are therefore **UNVERIFIED** by inspection. The two names above come from the source, and the file count of 2 comes from the log. The owner or P10-V can check them at https://github.com/Ventusltd/gridatlas/actions/runs/41247942683/artifacts/13060655237.

## Result

All three jobs are green on head `5ec7f62f213e2d20a02e86427daa182c0f38e4a4`. `BROWSER DC SMOKE PASS` is reported at [393,852] and [1280,800] with `tabs: 4` and `errors: []`, for generation 202610312138. cartridge-gate reports `19/19 checks passed` with both offtakers rows at 30/30. size-guard reports 13 files within budget. STATUS: **PASS**. The only UNVERIFIED items are the PNG contents.

## What remains

Nothing else remains for agents. P10-V does its independent read and REVIEW, then stops. The next steps are the owner's:

1. **RELEASE.md step 3**: the owner writes `ACCEPT 202610312138` as the first line of a comment on PR #80, from the owner login. No agent writes it.
2. **RELEASE.md step 4**: the owner rebase-merges PR #80, so that `atlas/v/202610312138/` is on Pages.
3. **RELEASE.md steps 5-7**, a later phase: the check-live, homepage and served checks.

No agent comments on PR #80, records ACCEPT, or adds an `accepted:` label.
