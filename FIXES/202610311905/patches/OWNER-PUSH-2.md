# OWNER PUSH 2: gridatlas `preview/202610312138-gridatlas-v9.188` (FIX 202610311905, NL-007)

Only the owner runs these commands, after P9-V posts REVIEW PASS and F1 posts "ready for OWNER PUSH 2" on
[NL-007](https://github.com/Ventusltd/neural-link-between-agents/issues/7). The bundle holds the five commits of P5, P6, P7, P8 and P7b
on top of gridatlas `cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e`. That commit is a **prerequisite**, so the clone must contain it.

| | value |
|---|---|
| bundle | `FIXES/202610311905/patches/09-gridatlas.bundle`, sha256 `737f0267753ce3e13ae8015443bda2ec30e64431c20dbe52f899e871936f43e7`, 99,435 B |
| ref in bundle | `refs/heads/preview/202610312138-gridatlas-v9.188` → `5ec7f62f213e2d20a02e86427daa182c0f38e4a4` |
| prerequisite | `cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e` |
| commits | `685b7e8` (P5, workflow), `bf76680` (P6, re-pin + module), `f162c94` (P7, tests + doc), `313d9c6` (P8, the cut), `5ec7f62` (P7b, DC1 derived) |
| files | the 13 files of plan §3.2; none under `atlas/current.json`, `STATE.md`, `atlas/index.html`, `atlas/releases/**` |
| local gate | `FIXES/202610311905/patches/09-pr-gate.log`: 19/19 PASS, exit 0 |
| PR body | `FIXES/202610311905/patches/09-pr-body.md` |

The commands assume that `neural-link-between-agents` and `gridatlas` are side by side, and that neural-link is at a main that contains
the P9 commit. Set `NL` to the patches folder:

```bash
NL="$PWD/neural-link-between-agents/FIXES/202610311905/patches"
sha256sum "$NL/09-gridatlas.bundle"   # must print 737f0267753ce3e13ae8015443bda2ec30e64431c20dbe52f899e871936f43e7

# 1. gridatlas at origin/main (clone, or cd into an existing clone and update main)
git clone https://github.com/Ventusltd/gridatlas.git      # or: cd gridatlas && git fetch origin main
cd gridatlas
git checkout main && git merge --ff-only origin/main
git merge-base --is-ancestor cacb69a7c4abc3b1a90fd75807ce8ef8cbc46d9e origin/main && echo "prerequisite present"

# 2. bring the branch in from the bundle
git bundle verify "$NL/09-gridatlas.bundle"   # "is okay"; requires cacb69a...
git fetch "$NL/09-gridatlas.bundle" preview/202610312138-gridatlas-v9.188:preview/202610312138-gridatlas-v9.188
git rev-parse preview/202610312138-gridatlas-v9.188   # must print 5ec7f62f213e2d20a02e86427daa182c0f38e4a4
git log --format='%h %an <%ae> %s' cacb69a..preview/202610312138-gridatlas-v9.188   # five commits, Claude <noreply@anthropic.com>
git diff --name-only cacb69a..preview/202610312138-gridatlas-v9.188 | wc -l         # 13

# 3. push the branch
git push -u origin preview/202610312138-gridatlas-v9.188

# 4. open the DRAFT PR with the drafted body (REST, because `gh pr create` needs GraphQL; docs/RELEASE.md "Publishing")
gh api -X POST repos/Ventusltd/gridatlas/pulls \
  -f head=preview/202610312138-gridatlas-v9.188 -f base=main -F draft=true \
  -f title='202610312138 preview (v9.188): data-centre baseline 226/225, DCFSHA re-pinned at data-grid-gb 01a4491 (NL-007)' \
  -F body=@"$NL/09-pr-body.md" --jq '.number, .html_url'
PR=<number printed above>
```

5. **No label is needed.** The head ref starts with `preview/`, so `pr-file-size-guard.yml` runs `dc-browser-smoke` on `opened`.
The gate is `if: startsWith(github.event.pull_request.head.ref, 'preview/')`, from P5.

6. Watch the three jobs of "PR file size guard and cartridge gate": `size-guard`, `cartridge-gate` and `dc-browser-smoke`.
`dc-browser-smoke` takes about 15 minutes.

```bash
gh pr checks "$PR" --repo Ventusltd/gridatlas --watch
# REST alternative, no GraphQL:
gh api repos/Ventusltd/gridatlas/commits/5ec7f62f213e2d20a02e86427daa182c0f38e4a4/check-runs \
  --jq '.check_runs[] | [.name, .status, .conclusion, .html_url] | @tsv'
```

7. **Stop here.** Do not merge yet, and do not accept. Post the PR on NL-007, for example:

```bash
gh issue comment 7 --repo Ventusltd/neural-link-between-agents --body "[OWNER → ALL] [NL-007] [$(date -u '+%Y-%m-%d %H:%M UTC')]
TYPE: HANDOFF
IN-REPLY-TO: <F1's 'ready for OWNER PUSH 2' comment URL>
SCOPE: Ventusltd/gridatlas PR #$PR, preview/202610312138-gridatlas-v9.188 (draft)
HEAD: 5ec7f62f213e2d20a02e86427daa182c0f38e4a4
EVIDENCE: https://github.com/Ventusltd/gridatlas/pull/$PR
STATUS: IN-PROGRESS
DETAILS: OWNER PUSH 2 done; draft PR open; size-guard, cartridge-gate and dc-browser-smoke running or finished.
ACTION REQUESTED: P10-I may start."
```

P10 reads the evidence: the three run URLs, the `dc-browser-smoke-<run id>` artifact, `BROWSER DC SMOKE PASS` at [393,852] and
[1280,800], `tabs: 4` and `errors: []`. P10-V then posts REVIEW. Only after that REVIEW PASS does the owner act:

- **Rebase and merge** the PR, never squash (docs/RELEASE.md), so that `atlas/v/202610312138/` is served by Pages.
- Write `ACCEPT 202610312138` as the first line of a comment on the PR (docs/RELEASE.md step 3).

No agent does either. This PR does not move `atlas/current.json` or `STATE.md`; the release is a later phase.

In the following cases, do not force anything. Stop and post a BLOCKER on NL-007:

- `sha256sum` does not print `737f0267…43e7`.
- `git bundle verify` reports a missing prerequisite. Main has been rewritten or the clone is stale: fetch and retry, never force.
- `rev-parse` does not print `5ec7f62…`.
- GitHub reports a merge conflict, because main has moved under any of the 13 files.
- Any of `size-guard`, `cartridge-gate` or `dc-browser-smoke` fails, or `dc-browser-smoke` does not run on the PR.

Never force-push. Never edit the branch by hand.
