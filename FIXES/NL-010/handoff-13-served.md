# OPUS-13 hand-off: served check of the Kuiper editions door (NL-010)

Tester OPUS-13, 2026-11-02. Closes the gap in served-check.md ("Not proved"): no check fetched
`www.globalgrid2050.com/kuiper-editions/` or the Kuiper editions pointer.

- Repository: Ventusltd/gridatlas
- Branch: `served-check-kuiper-editions` (from origin/main 41729af), pushed
- Head: `ce1246ea0273d28039eb3c4f9ee03849278117e4` (1 commit, 1 file: tools/release/check-served.mjs, +30 lines)
- `node --check tools/release/check-served.mjs`: OK
- PR not opened and not merged (the harness does that).

## PR title

check-served: report the Kuiper editions door, pointer and homepage row (NL-010)

## PR body

The `served-homepage` mode of `202608301321-verify-live.yml` runs `tools/release/check-served.mjs`. It proved the
homepage bundle and the GridAtlas row but never fetched the Kuiper editions door. This PR adds three report-only
lines to the same script:

1. **`/kuiper-editions/` on the domain**: records the served sha256 and compares it with globalgrid2050 main's
   `kuiper-editions/index.html` (today `2f046fd8dd494502fb8e2bc130af0fe5073e379a827a53ceefc1f3e338f0565e`). It also
   records whether the page forwards (meta refresh and `location.replace`) to
   `https://ventusltd.github.io/kuiper-belt/editions/`.
2. **`https://ventusltd.github.io/kuiper-belt/editions/`**: records which dated folder the pointer names
   (today `202611012027`, Edition 4).
3. **`/` on the domain**: records whether the `<tr data-entity-id="kuiper-editions">` row is present.
   This uses the homepage body the GridAtlas check already fetches.

Rules:
- The door and pointer are fetched once, before the GridAtlas retry loop. The row is read on each loop pass from the
  homepage body that is already fetched. None of these lines are added to `checks`, so they never hold back or
  extend the GridAtlas verdict.
- A mismatch prints `KUIPER NOTE` and the status does not change. Only an **HTTP 404** on a Kuiper line turns a
  PASS into FAIL (exit 1), with a `<path>: HTTP 404` problem.
- Results go to `report.kuiper` in `work/served-homepage.json` (path, http, ok, expected, live, plus `sha256`,
  `forwards` and `folder`). They print before the last line, so `release-status.mjs --served`, which reads only
  the last line, is unchanged.
- The job stays read-only (contents: read). The only new requests are two curl GETs and one `gh api` contents
  read.

Expected log once merged and dispatched (`mode=served-homepage`, ref main):
```
pin 5a4abe41b7a9: GridAtlas 202610312138 "V9.188 - 31 October 2026"
  OK    homepage-shell/data/homepage.json  HTTP 200
  OK    homepage-shell/assets/versioned-homepage.css  HTTP 200
  OK    homepage-shell/assets/versioned-homepage.js  HTTP 200
  OK    /  HTTP 200
  KUIPER OK    /kuiper-editions/  HTTP 200  sha256 2f046fd8…0565e, forwards to https://ventusltd.github.io/kuiper-belt/editions/
  KUIPER OK    https://ventusltd.github.io/kuiper-belt/editions/  HTTP 200  names 202611012027/
  KUIPER OK    / kuiper-editions row  HTTP 200  row present
PASS: https://www.globalgrid2050.com/ serves the pinned homepage with GridAtlas "V9.188 - 31 October 2026"
```

Tested locally against a 127.0.0.1 mirror of the pinned bundle (`--base http://127.0.0.1:8765/`). Result: PASS
with the door at sha256 2f046fd8… and forwarding, and the row present. With the door removed: `KUIPER NOTE
/kuiper-editions/ HTTP 404` and `FAIL: /kuiper-editions/: HTTP 404`, exit 1. The sandbox proxy refuses github.io,
so the pointer line was HTTP 0 (NOTE, not a failure) in that test.

Not changed: the workflow's Summarise step still lists only `.checks`. The Kuiper lines appear in the job log and
the retained JSON, not in the step summary.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_015ELZDBhAFNgtcsrTUSi1vm
