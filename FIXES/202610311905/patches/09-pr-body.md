# 202610312138 preview (v9.188): data-centre baseline 226/225, DCFSHA re-pinned at data-grid-gb 01a4491 (NL-007)

Draft preview PR for generation **202610312138** (v9.188), cut by hand under docs/RELEASE.md step 1 and opened under step 2 ("Publishing (a person does this)"). Base: `main` at `cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e`. Head: `preview/202610312138-gridatlas-v9.188` at `5ec7f62f213e2d20a02e86427daa182c0f38e4a4`.

**This PR does not move `atlas/current.json` or `STATE.md`.** Acceptance is the owner's `ACCEPT 202610312138` on this PR, under docs/RELEASE.md step 3, after CI.

## What the generation changes

202610312138 is 202610292044 **re-pinned, otherwise unchanged**. The offtakers overlay now reads the 226-record UK data-centre pipeline file from data-grid-gb main at merge commit `01a4491dc66ec4e6319a05a394926043b9d992f9` ([data-grid-gb PR #7](https://github.com/Ventusltd/data-grid-gb/pull/7)). In that file Wapseys Wood is one site, not two. It has 226 records: 225 have coordinates and are drawn, and one (Ebbsfleet) has no coordinates and is never drawn. The lightning overlay is recomposed with no change in behaviour; its module path stays `atlas/modules/202610291043-uk-lightning-overlay.js`.

The composition note is corrected. It used to say "203 sites from the open UK data-centre pipeline, DC-A7's pinned snapshot". It now says "226 records from the open UK data-centre pipeline (DC-A7's pinned snapshot, Wapseys Wood one site), 225 drawn, one (Ebbsfleet) without coordinates and never drawn". In both the manifest and `atlas/v/202610312138/current.json`, `site_data_sources` reads `features 226` and `drawn 225`, and classes reads "C data centres 225 (226 records, one unplaced)".

## Four equal hashes

`87337db5d3bf7959f7f605d3abd029dd4196ab24a79107ceb95210c5b7751654` (446,550 B, 226 features, 225 with geometry), measured four ways:

1. `sha256sum data/uk_datacentre_pipeline_202610312133.geojson` (S = 202610312133, M's committer UTC minute)
2. the data-grid-gb `datacentres/lanes/MANIFEST.json` pin at `01a4491` (`out/uk_datacentre_pipeline.geojson`)
3. `DCFSHA` in `tools/offtakers/src/01-data.js`
4. `git show 01a4491:datacentres/lanes/dc-a7-merge/out/uk_datacentre_pipeline.geojson | sha256sum`

Module: `atlas/modules/202610312138-uk-offtakers-overlay.js` is 71,191 B (budget 80,000 B), sha256 `1be368f53b04f4f451c0559ca6c534d3f8301ad9df158cc6dd94308517c5cf46`. `node tools/offtakers/build.mjs --check` rebuilds it byte for byte. 202610292044 is marked historical in `tools/offtakers/generations.json`.

## The 13 files

1. `atlas/manifests/202610312138-composition.json`
2. `atlas/v/202610312138/current.json`
3. `atlas/v/202610312138/index.html` (byte copy of `atlas/index.html`, loader v2)
4. `tools/proofs/202610312138-uk-lightning-overlay.proof.mjs`
5. `tools/proofs/202610312138-uk-offtakers-overlay.proof.mjs`
6. `atlas/modules/202610312138-uk-offtakers-overlay.js`
7. `tools/offtakers/generations.json`
8. `data/uk_datacentre_pipeline_202610312133.geojson`
9. `tools/offtakers/src/01-data.js`
10. `tools/ci/offtakers/overlay-offtakers.test.mjs`
11. `tools/ci/offtakers/browser-dc-smoke.mjs`
12. `docs/OFFTAKERS-SOURCE.md`
13. `.github/workflows/pr-file-size-guard.yml`

None of these paths is under `atlas/current.json`, `STATE.md`, `atlas/index.html` or `atlas/releases/**`. `git diff --stat cacb69a..5ec7f62` shows 13 files changed, 2,385 insertions and 12 deletions.

## Commits (rebase-merge; each one is authored `Claude <noreply@anthropic.com>`)

| SHA | subject |
|---|---|
| `685b7e8678f02cc266f2ce65b215df0772b483d4` | ci: run the data-centre Chromium smoke on every preview/ PR, generation 202610312138, upload-artifact pinned (NL-007 P5) |
| `bf766804a7ce13dd799311d96c97ab84e6d9565b` | offtakers: vendor the 226-record data-centre pipeline at data-grid-gb 01a4491 as 202610312133, re-pin DCF/DCFSHA, build module 202610312138 (NL-007 P6) |
| `f162c947fd82851934085cbd5264c2a98fc4bf10` | offtakers tests and source doc: 226 records, one unplaced; smoke default generation 202610312138 (NL-007 P7) |
| `313d9c6714bc364909a02f7be1e433af28104f5e` | 202610312138 preview (v9.188): data-centre baseline 226/225, DCFSHA re-pinned at data-grid-gb 01a4491, composition note corrected (NL-007 P8) |
| `5ec7f62f213e2d20a02e86427daa182c0f38e4a4` | offtakers test DC1: derive the unplaced count from the file the module pins, so the gate holds for 202610292044 and 202610312138 (NL-007 P7b) |

## Local gate: `node tools/ci/pr-gate.mjs --base cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e`

Result: **19/19 checks passed**, exit 0, 146 s, Node v22.23.4. Generations under test: 202610292044 (live) and 202610312138 (touched). The rows:

- lint, state-parity
- composition 202610292044 and its two proofs
- composition 202610312138 and its two proofs: `202610312138-uk-lightning-overlay.proof.mjs` and `202610312138-uk-offtakers-overlay.proof.mjs` (71191 B <= 80000, rebuilt from source, 6 scripts composed)
- run-current, verify-compose, loader-registry (53 loaders), loader-equivalence
- lightning-source, offtakers-source (`ok 202610312138: 71191 B … rebuilt byte for byte`)
- lightning 202610291043: overlay-engine 207 pass / 0 fail / 10 skipped; overlay-latest 8 pass / 0 fail
- **offtakers 202610292044 + lightning 202610291043: 30 pass / 0 fail** (`atlas/current.json`)
- **offtakers 202610312138 + lightning 202610291043: 30 pass / 0 fail** (`atlas/v/202610312138/current.json`)
- release-tools: 16 pass / 0 fail

The full log is `FIXES/202610311905/patches/09-pr-gate.log` in neural-link-between-agents.

## Why P7b (commit 5ec7f62)

The gate runs the offtakers suite on the **live** module (202610292044) as well as on the new one. The live module still loads the 227-record file (`DCFSHA 176c1b2e…2d89`), which has two records without coordinates: Ebbsfleet and Wapseys Wood. P7 had changed DC1's literal from 2 to 1, so the gate's live-pair row failed with 29/30 (`overlay-offtakers.test.mjs:389`, `2 !== 1`). P7b removes the literal. DC1 now:

- takes the expected unplaced count from the `data/*.geojson` file whose sha256 equals the `DCFSHA` of the module under test, by counting its features with null geometry;
- asserts that the module reports that count;
- asserts that Ebbsfleet is among the unplaced records and that none of them is drawn.

The expected count is 2 for 202610292044 and 1 for 202610312138, and the test stays correct for any later re-pin. P8's manifest, proofs and module do not depend on the test file.

## Why the workflow edit (commit 685b7e8)

`pr-file-size-guard.yml` triggers on `on: pull_request:` with no `types`, so a label added after a PR is opened would not fire it. The `dc-browser-smoke` job was gated on `github.event.pull_request.number == 75`, a one-off for issue #73. It now runs on **every `preview/` PR**, on `opened` and `synchronize`, with no label:

- `if: startsWith(github.event.pull_request.head.ref, 'preview/')`
- `DC_SMOKE_GENERATION: '202610312138'` (the G literal)
- `uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02  # v4.6.2`: the only action in the file that was not pinned by SHA. The SHA was resolved with `git ls-remote https://github.com/actions/upload-artifact.git refs/tags/v4.6.2`.

This way a real browser opens this generation on its own PR, instead of the preview relying on PR #75's browser evidence. Each run costs about 15 CI minutes. `on:` is unchanged, and the job does not deploy, change the live pointer or use secrets.

## UNVERIFIED until CI runs on this PR

- `size-guard`
- `cartridge-gate` (the same `pr-gate.mjs`, run on CI)
- `dc-browser-smoke`: should report `BROWSER DC SMOKE PASS` at [393,852] and [1280,800], `tabs: 4`, `errors: []`, two PNGs in the artifact `dc-browser-smoke-<run id>`. No sandbox reaches the MapLibre CDN, so a local pass is not evidence.
- Pages serving `atlas/v/202610312138/`, which happens only after the rebase merge.

## Links

- Channel: [NL-007](https://github.com/Ventusltd/neural-link-between-agents/issues/7)
- Plan: [FIXES/202610311905-datacentre-baseline.md](https://github.com/Ventusltd/neural-link-between-agents/blob/main/FIXES/202610311905-datacentre-baseline.md)
- Data source: [Ventusltd/data-grid-gb PR #7](https://github.com/Ventusltd/data-grid-gb/pull/7), merged as `01a4491dc66ec4e6319a05a394926043b9d992f9`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm
