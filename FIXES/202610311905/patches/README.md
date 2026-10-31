# Patches and bundles for FIX 202610311905

The implementers of NL-007 have no push access to `Ventusltd/data-grid-gb` or `Ventusltd/gridatlas`. Each step of
`../202610311905-datacentre-baseline.md` therefore ends as a local commit on a named branch plus a file here, committed to
this repository's main, one commit per step (`P<n>: <artefact>`). The owner applies them and pushes. Nothing here is a
secret or a credential; every file is a plain-text diff, a git bundle or a text report.

## Files, in step order

| file | step | kind | applies on |
|---|---|---|---|
| `01-dcmerge.patch` | P1 | `git format-patch` | data-grid-gb `b57c94d` |
| `02-rebuild.patch` | P2 | `git format-patch` | after 01 |
| `03-checks.txt`, `03-data-grid-gb.bundle`, `03-pr-body.md` | P3 | report, `git bundle`, PR body | data-grid-gb `b57c94d` (the bundle holds commits 01+02) |
| `04-merge-evidence.md` | P4 | report (M, S, sha256, bytes, CI run URLs) | — |
| `05-workflow.patch` | P5 | `git format-patch` | gridatlas `cacb69a` |
| `06-repin.patch` | P6 | `git format-patch` | after 05 |
| `07-tests.patch` | P7 | `git format-patch` | after 06 |
| `08-cut.patch` | P8 | `git format-patch` | after 07 |
| `09-pr-gate.log`, `09-gridatlas.bundle`, `09-pr-body.md` | P9 | log, `git bundle`, PR body | gridatlas `cacb69a` (the bundle holds 05–08) |
| `10-ci-evidence.md` | P10 | report (run URLs, viewports, artifact names) | — |

## Applying a patch series (owner, or a verifier)

```bash
git clone https://github.com/Ventusltd/data-grid-gb.git && cd data-grid-gb
git checkout -b fix/nl007-operator-canon b57c94d4e964df2de0dea2786781c6d07a967ea1
git am --3way ../neural-link-between-agents/FIXES/202610311905/patches/01-dcmerge.patch \
              ../neural-link-between-agents/FIXES/202610311905/patches/02-rebuild.patch
git log --oneline b57c94d..HEAD          # two commits, authorship preserved
```

`git am` keeps the implementer's author line, date and message (and the `Co-Authored-By` and `Claude-Session` trailers).
`--3way` lets a patch apply if main has moved under it; if it still fails, stop and post a BLOCKER on NL-007 with both refs
rather than resolving by hand.

## Applying a bundle (owner, for OWNER PUSH 1 and 2)

```bash
# data-grid-gb, OWNER PUSH 1
cd data-grid-gb && git fetch origin main
git bundle verify ../neural-link-between-agents/FIXES/202610311905/patches/03-data-grid-gb.bundle
git fetch ../neural-link-between-agents/FIXES/202610311905/patches/03-data-grid-gb.bundle fix/nl007-operator-canon:fix/nl007-operator-canon
git rev-parse fix/nl007-operator-canon    # must equal the HEAD posted in P3's HANDOFF
git push -u origin fix/nl007-operator-canon
gh api -X POST repos/Ventusltd/data-grid-gb/pulls -f head=fix/nl007-operator-canon -f base=main \
  -f title='Merge Wapseys Wood: canonicalise operator glosses in operator_match; 226-record baseline' \
  -F body=@../neural-link-between-agents/FIXES/202610311905/patches/03-pr-body.md
# wait for both test-assets.yml legs, merge, then post the merged SHA M on NL-007

# gridatlas, OWNER PUSH 2
cd gridatlas && git fetch origin main
git bundle verify ../neural-link-between-agents/FIXES/202610311905/patches/09-gridatlas.bundle
git fetch ../neural-link-between-agents/FIXES/202610311905/patches/09-gridatlas.bundle 'refs/heads/preview/*:refs/heads/preview/*'
git push -u origin preview/<G>-gridatlas-v9.188
gh api -X POST repos/Ventusltd/gridatlas/pulls -f head=preview/<G>-gridatlas-v9.188 -f base=main -F draft=true \
  -f title='<G> preview (v9.188): data-centre baseline 226/225, DCFSHA re-pin' \
  -F body=@../neural-link-between-agents/FIXES/202610311905/patches/09-pr-body.md
# the preview/ head ref makes pr-file-size-guard.yml run dc-browser-smoke; no label needed
```

A bundle is self-contained: `git bundle verify` checks that the clone holds the bundle's prerequisite commit
(`b57c94d…` or `cacb69a…`). If it reports a missing prerequisite, main has been re-written or the clone is stale; fetch
and retry, never force.

## What the owner never does from here

No file here moves `atlas/current.json`, `STATE.md`, `atlas/index.html` or `atlas/releases/**`, and none records
acceptance. `ACCEPT <G>` is a first-line comment by the owner on the gridatlas preview PR, after P10's REVIEW PASS, and
is outside this phase (docs/RELEASE.md step 3).
