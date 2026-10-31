# FIXES/202610311905/patches — how the owner (or anyone) replays the fix

Every implementation step of plan `FIXES/202610311905-datacentre-baseline.md` (revision 2) left an artefact here,
committed on main one step at a time. Authors of every patch are `Claude <noreply@anthropic.com>`; every patch carries
`Co-Authored-By` and `Claude-Session` trailers (verifiers grep the `From:` and trailer lines for no-reply addresses).

| file | step | what |
|---|---|---|
| `01-dcmerge.patch` | P1 | data-grid-gb: `_op_core` + `operator_match` canonicalisation and the false-split test (53 tests OK) |
| `02-rebuild.patch` | P2 | data-grid-gb: dc-a7 rebuilt, 226 records / 225 with geometry, MANIFEST pins, rejects unchanged |
| `03-checks.txt`, `03-data-grid-gb.bundle`, `03-pr-body.md`, `OWNER-PUSH-1.md` | P3 | verify 8 ok, 35 tests OK, reproduce digest; the bundle (tip 75ab8ae, requires b57c94d); PR body and push instructions |
| `04-merge-evidence.md` | P4 | M = 01a4491dc66ec4e6319a05a394926043b9d992f9, S = 202610312133, geojson 87337db5…1654 / 446,550 B |
| `05-workflow.patch`, `05-G.txt` | P5 | gridatlas: `pr-file-size-guard.yml` runs the Chromium smoke on every `preview/` PR, G = 202610312138, upload-artifact pinned |
| `06-repin.patch` | P6 | gridatlas: vendored data file, DCF/DCFSHA, generations.json, module 202610312138 (71,191 B) |
| `07-tests.patch` | P7 | gridatlas: test and doc edits for 226/225 |
| `07b-dc1-derived.patch`, `09a-pr-gate-blocked.log` | P7b | re-plan after P9's blocker: DC1 derives the unplaced count from the pinned file; the blocked gate log kept as evidence |
| `08-cut.patch` | P8 | gridatlas: the hand cut of generation 202610312138 (manifest, route pointer, loader copy, two proofs) |
| `09-pr-gate.log`, `09-gridatlas.bundle`, `09-pr-body.md`, `OWNER-PUSH-2.md` | P9 | gate 19/19 PASS; the bundle (tip 5ec7f62, requires cacb69a, five commits incl. P7b); PR body and push instructions |
| `10-ci-evidence.md` | P10 | PR #80 CI: size-guard, cartridge-gate, dc-browser-smoke PASS at [393,852] and [1280,800] |
| `11-release-report.json`, `11-release-gates.log` | step 4 | release-accepted.mjs: 8/8 gates, release commit ddbf51d → main 41729af0 |
| `12-steps-5-7-evidence.md` | steps 5–7 | live-bytes, homepage label and pin, deploy, served check |

Machine paths in the logs are replaced by `<clone>`, `<scratch>`, `<local>`; the content is otherwise as run.

## Applying a patch

```bash
git -C <clone> checkout -b <branch> <base-sha>      # base per the plan: b57c94d (data-grid-gb) or cacb69a (gridatlas)
git -C <clone> am <neural-link>/FIXES/202610311905/patches/NN-*.patch
git -C <clone> log --format='%h %an <%ae> %s' <base-sha>..HEAD   # authors must be noreply
```

## Fetching from a bundle

```bash
git bundle verify <bundle>                                   # prints the prerequisite; it must be in the clone
git fetch <bundle> <branch>:<branch>
git rev-parse <branch>                                       # must equal the tip named in the step's HANDOFF
git push -u origin <branch>
```

Then open the PR with the step's `*-pr-body.md` and its title as the HANDOFF states; `OWNER-PUSH-1.md` and `OWNER-PUSH-2.md`
give the exact commands. In this run the owner authorised the harness in chat to perform both pushes and the merges;
that authorisation and its limits are discussed in the NL-008 QA finding Q4.
