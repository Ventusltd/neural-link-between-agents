# NL-010 served-domain check (OPUS-13, 2026-11-02 ~00:52 UTC)

**Verdict**
1. `www.globalgrid2050.com/kuiper-editions/` serves the R0 door page (sha256 `2f046fd8…0565e`, 1286 bytes). It forwards straight away to `https://ventusltd.github.io/kuiper-belt/editions/`, which forwards to `202611012027/`. So the domain opens **Edition 4**, the pointer, not Edition 5.
2. The homepage card **is in the served bundle**. `www.globalgrid2050.com/homepage-shell/data/homepage.json` is byte-identical to `3460dc92…4624746` (served-homepage run 41369293571, PASS). That file holds the `kuiper-editions` entity (operative Edition 4, linking `globalgrid2050.com/kuiper-editions/`).
3. The Edition 5 preview URL `https://ventusltd.github.io/kuiper-belt/editions/202611012135/` serves the Edition 5 preview page (`index.html` sha256 `418ae14c…64d05`; modules hello + line-card; shell withdrawn). It was deployed by Pages run 41365403840 (success). Neither the homepage nor the editions pointer links to it yet.

How each point was proved: the sandbox proxy blocks globalgrid2050.com and github.io, so every point comes from GitHub. Point 2 was measured on the live domain by a CI run (it fetched the bytes and compared them). Points 1 and 3 rest on the deployed Pages artifact listings, the successful deploy jobs and the bytes at the deployed commit. No CI run fetched those two URLs.

## 1. Ventusltd/globalgrid2050 main — Pages deploy

- main head: `18aa446e978898f73c39399cc070fd1e28722120` ("homepage-owner: re-pin to merged globalgrid2050-homepage main 5a4abe41 (Kuiper editions card); hashes unchanged", 00:38:17Z). Unchanged at 00:52Z.
- Run **41368222618** "Deploy GlobalGrid2050 Pages" (push, head 18aa446e): **completed / success**, 00:38:20Z → 00:45:53Z.

| job id | job | conclusion |
|---|---|---|
| 125032861044 | build | success |
| 125033846156 | deploy | success ("Created deployment for 18aa446e…", "Reported success!" 00:44:03Z) |
| 125034375071 | verify_v9_7_candidate | success |
| 125034834727 | report | success (commit status `globalgrid/pages-deploy` = success, "Pages deployment and V9.7 candidate browser proof passed") |

- Build step 6, **"Import hash-pinned homepage owner bundle"** (`python3 scripts/import_homepage_owner.py`), success. Log line 00:39:10Z:
  `Imported verified homepage 5a4abe41b7a9e19988faaedace252077a1646fc8: 7 files`.
  The script downloads each file from raw.githubusercontent at the pinned commit and refuses to continue on any sha256 mismatch. It writes the six non-index files under `homepage-shell/` and rewrites `index.html` at the site root (three path rewrites: css, js, catalogue fallback).
- Pin `catalogue/homepage-owner.json` at 18aa446e: repository Ventusltd/globalgrid2050-homepage, commit `5a4abe41b7a9e19988faaedace252077a1646fc8`, 7 files (hashes in section 2).
- Files in the uploaded Pages artifact (build log, "Archive artifact"):
  - `./kuiper-editions/index.html` (log line 26572)
  - `./homepage-shell/data/homepage.json`, `active-pages.json`, `entity-types.json`, `presentation.json`
  - `./homepage-shell/assets/versioned-homepage.css`, `versioned-homepage.js`
  - `./index.html` (root, generated from the pinned owner index), `./catalogue/homepage-owner.json`
- `kuiper-editions/index.html` at 18aa446e: sha256 `2f046fd8dd494502fb8e2bc130af0fe5073e379a827a53ceefc1f3e338f0565e`, 1286 bytes. It is a door page: a meta refresh to `https://ventusltd.github.io/kuiper-belt/editions/` plus `location.replace('https://ventusltd.github.io/kuiper-belt/editions/' + location.search + location.hash)`, and a link to See Through.
- `CNAME` at 18aa446e: `globalgrid2050.com`. (The Pages API is blocked by the proxy, so the served host comes from the CNAME file and from the served-homepage run.)

## 2. Ventusltd/globalgrid2050-homepage @ 5a4abe41

- Commit `5a4abe41b7a9e19988faaedace252077a1646fc8` ("homepage: Kuiper editions card sits just above See Through; shorter description"). This is also the current main head.
- I fetched all seven files at that commit and computed sha256. Every hash equals the pin:

| file | sha256 | = pin |
|---|---|---|
| data/homepage.json | `3460dc92164492ecb0d04d1a7d053be7fcc0737f0e4f0fdd24278054a4624746` | yes (= expected) |
| index.html | `9a7e34c7cea0030fcefc9564de43623484dccc9aabf6db6ce37284689e227c77` | yes |
| assets/versioned-homepage.css | `0c405224efa71f262011db49c5c7a559a265801ec98609c8c9b16a5d83df35d2` | yes |
| assets/versioned-homepage.js | `691df697ba930eab95ba67251ca3bee673ebb8c4174e010d8f6bb73ab24ea0f1` | yes |
| data/active-pages.json | `4ee017277a6e0a7a5e92b5320486cdf908300ac34629d71249d53b0e4d31fdeb` | yes |
| data/presentation.json | `66285dafe5369cfb991030e80ffdf8c7893de279efb5aa15a86493434d9fed11` | yes |
| data/entity-types.json | `bbf1e6c692e6d27c95ca4f37a5286e344028e9d794dd3d8abf2c52232d4b9ca0` | yes |

- `data/homepage.json` entities[3] is **`kuiper-editions`**: parent `kuiper`, title "Kuiper editions", launch "Open the Kuiper editions", operative_release_id `202611012027`. It has four releases: Editions 1–3 (github.io archive URLs) and Edition 4, whose url is `https://globalgrid2050.com/kuiper-editions/`. The next entity is `see-through`. The pinned `index.html` also carries a static row `<tr data-entity-id="kuiper-editions">` that links `https://globalgrid2050.com/kuiper-editions/` (summary "Edition 4 - 1 November 2026").

## 3. Ventusltd/kuiper-belt main — Pages

- main head: `e92ad5dde7ccfd28e9b04b63e02499c4fcfb3111` ("Publish Kuiper Edition 5 preview folder (202611012135); pointer stays on Edition 4", 00:05:55Z). Unchanged at 00:52Z.
- Run **41365403840** "pages build and deployment" (head e92ad5dd): **completed / success**. Jobs: build 125024391242 success, report-build-status 125024518508 success, deploy 125024518513 success ("Created deployment for e92ad5dd…", "Reported success!" 00:07:40Z). The build artifact lists `./editions/202611012135/index.html` and `./editions/index.html`.
- Run 41365404779 "checking engineer" (head e92ad5dd): completed / success.
- Files at e92ad5dd:
  - `editions/202611012135/index.html`: exists. 84309 bytes, blob `eff31e6c4bc8d6d0a93a6f5b5e37004286524061`, sha256 `418ae14ca39bc92be028f852825da196fd634ec12bb48f8f538d0cf739564d05`, title "Kuiper Edition 5…". `modules.json` order is [hello, line-card].
  - `editions/index.html`: exists. 466 bytes, blob `cf2d63bf3a490679cd2022f9b110cb06a0277f4d`, sha256 `29d85a1f996d012c5f09f86dd4dc1e1a69a974d739e6d6595b46a3fbce56727c`. This is the pointer: a meta refresh plus `location.replace('202611012027/' + location.hash)`, which goes to **Edition 4**.
- No CNAME in kuiper-belt, so it is served at `https://ventusltd.github.io/kuiper-belt/`.

## 4. Served-bytes check workflow

- globalgrid2050 has no served-bytes workflow. Its only active Pages-related workflows are deploy-pages.yml and the homepage restore point check.
- The earlier GridAtlas cycle's check lives in **Ventusltd/gridatlas**: workflow 345935128 `.github/workflows/202608301321-verify-live.yml`, `workflow_dispatch` input `mode=served-homepage`. That mode is read-only (contents: read) and runs `tools/release/check-served.mjs`. The earlier run was 41252100497, PASS on 31 Oct.
- What it checks: the served `homepage-shell/data/homepage.json`, `versioned-homepage.css` and `versioned-homepage.js` at `https://www.globalgrid2050.com/` must equal the sha256s pinned in globalgrid2050 main's `catalogue/homepage-owner.json`, and `/` must carry the GridAtlas row. It does **not** fetch `/kuiper-editions/` or check the kuiper-editions row on `/`.
- Precondition checked first: gridatlas `atlas/current.json` generation is 202610312138, which is the homepage pin's GridAtlas operative release ("V9.188 - 31 October 2026").
- I dispatched it on gridatlas main (41729af0) at 00:50:20Z with `mode=served-homepage`. Run **41369293571**: **completed / success**. Job served-homepage 125036104666 success; changes success; live-bytes and build-deploy-verify skipped. Log:
  ```
  pin 5a4abe41b7a9: GridAtlas 202610312138 "V9.188 - 31 October 2026"
    OK    homepage-shell/data/homepage.json  HTTP 200
    OK    homepage-shell/assets/versioned-homepage.css  HTTP 200
    OK    homepage-shell/assets/versioned-homepage.js  HTTP 200
    OK    /  HTTP 200
  PASS: https://www.globalgrid2050.com/ serves the pinned homepage with GridAtlas "V9.188 - 31 October 2026"
  ```
  So the domain serves homepage.json `3460dc92…`, which contains the kuiper-editions card.

## Not proved (no check fetched these from the network)

- The served bytes of `www.globalgrid2050.com/kuiper-editions/` and of the two github.io editions URLs. Their deploys succeeded and the artifacts list them, but no check fetched them. A follow-up could extend check-served.mjs, or add a mode, to hash `/kuiper-editions/` against `2f046fd8…` and look for the `kuiper-editions` row on `/`.
- The root `/` is generated from the pinned index (`9a7e34c7…`) and that index carries the kuiper-editions row. The served `/` check confirmed only the GridAtlas row.

Nothing was committed or posted. The only action on GitHub was the read-only workflow dispatch 41369293571 on Ventusltd/gridatlas.
