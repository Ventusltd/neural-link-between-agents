# OWNER PUSH 1: data-grid-gb `fix/nl007-operator-canon` (FIX 202610311905, NL-007)

Only the owner runs these commands, after P3-V's REVIEW PASS and F1's "ready for OWNER PUSH 1" on
[NL-007](https://github.com/Ventusltd/neural-link-between-agents/issues/7). The bundle holds the two commits of P1 and P2
on top of data-grid-gb `b57c94d4e964df2de0dea2786781c6d07a967ea1`. That commit is a **prerequisite**, so the clone must contain it.

| | value |
|---|---|
| bundle | `FIXES/202610311905/patches/03-data-grid-gb.bundle`, sha256 `928e291ee02dff345ef326a4e02966a51f29c82fe4b82bfe084abf3da936b4c6`, 4,985 B |
| ref in bundle | `refs/heads/fix/nl007-operator-canon` → `75ab8ae54e95b90bb59e306b4ca3a08042430ce5` |
| prerequisite | `b57c94d4e964df2de0dea2786781c6d07a967ea1` |
| commits | `f8258a0` (P1, dcmerge + test), `75ab8ae` (P2, rebuild + MANIFEST) |
| PR body | `FIXES/202610311905/patches/03-pr-body.md` |

The commands assume `neural-link-between-agents` and `data-grid-gb` sit side by side, with neural-link at a main that contains
the P3 commit. Set `NL` to the patches folder:

```bash
NL="$PWD/neural-link-between-agents/FIXES/202610311905/patches"
sha256sum "$NL/03-data-grid-gb.bundle"   # must print 928e291ee02dff345ef326a4e02966a51f29c82fe4b82bfe084abf3da936b4c6

# 1. data-grid-gb at origin/main (clone, or cd into an existing clone and update main)
git clone https://github.com/Ventusltd/data-grid-gb.git      # or: cd data-grid-gb && git fetch origin main
cd data-grid-gb
git checkout main && git merge --ff-only origin/main
git merge-base --is-ancestor b57c94d4e964df2de0dea2786781c6d07a967ea1 origin/main && echo "prerequisite present"

# 2. bring the branch in from the bundle
git bundle verify "$NL/03-data-grid-gb.bundle"   # "is okay"; requires b57c94d...
git fetch "$NL/03-data-grid-gb.bundle" fix/nl007-operator-canon:fix/nl007-operator-canon
git rev-parse fix/nl007-operator-canon           # must print 75ab8ae54e95b90bb59e306b4ca3a08042430ce5
git log --format='%h %an <%ae> %s' b57c94d..fix/nl007-operator-canon   # two commits, Claude <noreply@anthropic.com>

# 3. push the branch
git push -u origin fix/nl007-operator-canon

# 4. open the PR with the drafted body
gh api -X POST repos/Ventusltd/data-grid-gb/pulls \
  -f head=fix/nl007-operator-canon -f base=main \
  -f title='dc-a7: Wapseys Wood is one site; merged pipeline 226 records, 225 with geometry (NL-007)' \
  -F body=@"$NL/03-pr-body.md" --jq '.number, .html_url'
PR=<number printed above>

# 5. wait for both legs of test-assets.yml: "test (requirements)" and "test (bare)"
gh pr checks "$PR" --repo Ventusltd/data-grid-gb --watch

# 6. merge (a merge commit keeps both commits and their authorship, owner decision 6)
gh pr merge "$PR" --repo Ventusltd/data-grid-gb --merge

# 7. read the merged commit M
M=$(gh pr view "$PR" --repo Ventusltd/data-grid-gb --json mergeCommit --jq .mergeCommit.oid); echo "$M"
git fetch origin main && git show "$M:datacentres/lanes/dc-a7-merge/out/uk_datacentre_pipeline.geojson" | sha256sum
#   must print 87337db5d3bf7959f7f605d3abd029dd4196ab24a79107ceb95210c5b7751654
```

8. Post M on NL-007, for example:

```bash
gh issue comment 7 --repo Ventusltd/neural-link-between-agents --body "[OWNER → ALL] [NL-007] [$(date -u '+%Y-%m-%d %H:%M UTC')]
TYPE: HANDOFF
IN-REPLY-TO: <F1's 'ready for OWNER PUSH 1' comment URL>
SCOPE: Ventusltd/data-grid-gb PR #$PR, fix/nl007-operator-canon merged to main
HEAD: $M
EVIDENCE: https://github.com/Ventusltd/data-grid-gb/pull/$PR
STATUS: PASS
DETAILS: OWNER PUSH 1 done; merged commit M = $M; both test-assets.yml legs green.
ACTION REQUESTED: P4-I may start."
```

Stop and post a BLOCKER on NL-007 instead of forcing anything in these cases:

- `git bundle verify` reports a missing prerequisite.
- `rev-parse` does not print `75ab8ae…`.
- GitHub reports a merge conflict, because main has moved under `datacentres/lanes/`.
- Either `test-assets.yml` leg fails.

Never force-push. Never edit the branch by hand.
