# OPUS-11 "homepage card" plan (lead, 2026-11-02 ~00:20 UTC)

Goal (R3 of OVERNIGHT.md): the Kuiper editions reachable from www.globalgrid2050.com as a homepage entity, with See
Through named beside it, done the way the homepage is really built (owner bundle in globalgrid2050-homepage, pinned
into globalgrid2050 by catalogue/homepage-owner.json, deployed by deploy-pages.yml).

Steps (lead does all of them unless a slot arrives; nothing is pushed to main, no PR opened or merged):

1. Lead: read data/homepage.json, data/entity-types.json, scripts/build_homepage_fallback.py, releases.py,
   release_gridatlas.py (pin), and in globalgrid2050 catalogue/homepage-owner.json, scripts/import_homepage_owner.py,
   homepage_versions/README.md, deploy-pages.yml path filters.
2. Builder part: in globalgrid2050-homepage branch kuiper-editions-card add entity `kuiper-editions` (parent_id kuiper,
   pattern = the see-through entity), its entity-types.json row, a view placement, rebuild the index.html fallback,
   run the CI checks listed in docs/GRIDATLAS-RELEASE.md. Mention See Through in the new card's description
   (See Through keeps its own row).
3. Builder part: in globalgrid2050 branch kuiper-editions-card replace catalogue/homepage-owner.json with the pin of
   the homepage branch commit (scripts/release_gridatlas.py pin), restore-point snapshot per homepage_versions/README.md
   if the procedure demands it, import locally to check, discard generated files.
4. Tester part: local render of the imported homepage, Playwright Pixel 7, the new card opened, screenshot; language
   gate words ("measured" etc.) absent from new text.
5. Evidence part: keys (repo@sha path:line) for every claim, handoff-11-homepage.md with PR titles, bodies, merge
   order, workflow and path filters; one HANDOFF on issue #10.

Merge order to be confirmed in the handoff: (a) homepage PR first (its merge commit is what the pin must name, so (b)
must be re-pinned to the merge commit if the harness squash-merges), then (b) globalgrid2050 PR, then deploy.
