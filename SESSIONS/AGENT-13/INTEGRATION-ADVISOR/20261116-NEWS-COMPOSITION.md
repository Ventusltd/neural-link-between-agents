# V9.26 integration recipe — actual producer/consumer boundary

INTEGRATION ADVISOR, owner-requested role46. This note is a tested integration
finding and implementation recipe, not publication approval. COMMAND alone
finalizes versions and promotes products. No product source was changed here.

## Pinned evidence and delivered lab

- Ranking producer: GlobalGrid2050 `c2b89326ab55424c4ea10ff5921d9c2bf31073dd`,
  `automation/news/news_algorithm.py::rank_headlines`.
- Current consumer: GlobalGrid2050 `e2568fa9b818d39e28b106bbe49c3a53d0ad4fc2`,
  `uk_renewables_pipeline/202611161630/scripts/plugins/live-news.js`.
- Existing source schema: `automation/news/schema/pipeline-headlines.v1.schema.json`.
- Existing collector: `automation/news/pipeline_headlines.py::build/merge/main`;
  existing publication workflow `.github/workflows/pipeline-headlines.yml`.
- Reproducible TestCode lab: branch `integration/news-ranking-20261116`, commit
  `b3e8423`, path `sandbox/news-ranking-integration/`.

Actual Python producer plus actual existing JavaScript renderer in a Node VM:
**12/12 observations passed**. The report explicitly says `release_compatible:false`.
These results reproduce the gap, not certify its repair. Missing input exits1
with zero executed checks. Six producer/package files and two consumer/schema
files are hash checked; source text CRLF is normalised to committed LF bytes.
No publisher article bodies, real-source assertions or private paths are stored.
No live collection, browser, CI or deployment claim is made by this lab.

Observed failure chain:

1. `rank_headlines` returns `globalgrid2050.news.editorial-priority.v1`, while
   the existing client accepts only `globalgrid2050.news.pipeline-headlines.v1`.
2. The existing v1 JSON Schema sets `additionalProperties:false` both at root
   and item level. Adding `editorial` fields to that file violates its contract.
3. A naive v1 envelope with ranked items passes the client's shallow validation
   but drops every `category=policy` item, then sorts by publisher date OR
   first_seen. In the synthetic case, an undated newly collected item moves
   ahead of the government policy that the producer ranked first.
4. Collection labels still correctly distinguish snapshot and failed status;
   preserve these semantics. Collection time must never become publisher date.
5. `pipeline_headlines.merge/dedupe_titles` reconstructs `ITEM_FIELDS` and sorts
   the result. Ranking before merge would lose editorial metadata and order.

## Smallest compatible production composition

Use the **existing collector and data branch**. Do not change the v1 headline
file or old clients. Add one sidecar generated after collection/merge/dedupe:

```json
{
  "schema": "globalgrid2050.news.pipeline-editorial.v1",
  "input": {
    "sha256": "SHA256_OF_EXACT_PIPELINE_HEADLINES_JSON_BYTES",
    "schema": "globalgrid2050.news.pipeline-headlines.v1",
    "generated_at": "ORIGINAL_COLLECTION_TIMESTAMP",
    "item_count": 69
  },
  "ranking": {
    "schema": "globalgrid2050.news.editorial-priority.v1",
    "as_of": "SAME_ORIGINAL_COLLECTION_TIMESTAMP",
    "profile_id": "uk-transition-global-context.v1",
    "profile_sha256": "ACTUAL_PRODUCER_PROFILE_HASH",
    "input_count": 69,
    "items": []
  }
}
```

The abbreviated ranking object above is illustrative, not a valid fabricated
result: preserve the producer's complete actual return value. Producer call:

```python
raw = input_path.read_bytes()
doc = json.loads(raw)
ranked = rank_headlines(doc["items"], as_of=doc["generated_at"])
```

Generate `dist/pipeline_headlines.rank.json` (final name owned by implementation)
from exact bytes. Validate source contract, matching counts, bounded unique
URLs, contiguous ranks and original publisher/possible-match identity. Do not
replace collection timestamp with build time, treat source success as article
freshness, or supply invented source-policy/originality reviews. Null/future
publisher dates retain the producer's unknown/future state.

Add a step to the existing headline workflow after the existing collector.
Publish both files in the **same data-branch commit** with normal non-force push;
rank/schema failure prevents that commit. Add new producer/test paths to its PR
path trigger and execute producer/export tests in both probe and refresh lanes.
Keep existing schedule/collector owner/branch/concurrency. No second scheduler.
The legacy feed's already documented partial-source behavior is separate from
the fail-closed project-evidence pipeline; do not silently conflate the two.

The NEW formal V9.26 consumer loads raw headline bytes and sidecar, verifies
SHA256, source schema/timestamp/count, ranking schema/profile, item identities
and rank continuity before displaying rank order. It must not apply the old
latest-first sort afterward. Include relevant energy policy and preserve source
credit. Show compact priority/reason/access context as editorial research order,
never source verification or a project fact. Existing status labels remain
driven by the source headline document, not sidecar generation.

The two HTTP reads can race with a data-branch update despite one Git commit:
hash mismatch must be handled. On absent/malformed/stale/mismatched sidecar,
display the usable headline document with explicit priority-unavailable state;
do not silently show a stale rank against a newer feed. The saved headline
snapshot needs its own matching saved sidecar. If the live file is unavailable,
saved content stays labelled snapshot. Unknown publisher date stays unknown.

## Ownership and executable gates

Root reports scaffold branch `v9.26-codex-integration` at
`16d96a9bfa79f045fbda66cee2f40a1e24322ef2`, new folder `202611161734`,
parent V9.25 `063adcae`; producer integrated as `8aef1d14`. Recheck these before
merging. Root NEWS_UI_V926 now owns the actual new-folder consumer, bounded
`build_news_priority.py`/export tests and additive existing-workflow wiring.
THIRD's earlier reusable consumer request had no ACK at this checkpoint; avoid
two implementations. Advisor owns only this note and the separate TestCode lab.

Reproduce the observation (Python3.12, Node20+):

```sh
python sandbox/news-ranking-integration/check.py \
  --producer-root "$PINNED_PRODUCER_CHECKOUT" \
  --consumer-root "$PINNED_CONSUMER_CHECKOUT"
```

Run new export tests plus existing `test_news_algorithm.py` and
`test_pipeline_headlines.py`. Required acceptance scenarios for the NEW consumer:

- Older official policy can appear ahead of a newer discovery headline; all
  permitted headlines and publisher credit remain reachable through Show More.
- A real original reporting receipt can affect order; publisher brand alone
  does not become an originality/verification assertion.
- Wrong SHA, stale sidecar, duplicate/missing ranks, changed publisher identity,
  malformed profile and unsafe URLs do not yield trusted priority display.
- Empty healthy feed, partial/failed collection, saved fallback and unknown
  dates retain distinct truthful labels; failed sidecar cannot freshen them.
- Source text remains text; links safe; existing search, CSV, tabs and MAP work.
- Run actual Chrome/Playwright widths375/768/1440 on the new formal folder;
  inspect first page, Show More, labels, console and network failures. The lab
  VM is not a substitute for those browser checks or actual Android evidence.

Do not finalize before adding actual meaningful feature markers and faults.
`new_version.py finalize` defaults to `published`; explicitly pass the intended
candidate state until acceptance. It computes candidate tree and runner deltas;
editing the folder afterward invalidates that receipt. `create` selects the
registry tail as parent; check dry-run parent and source tree first. Published
and non-tail historical entries must stay unchanged.

## Next two composition boundaries

V9.27: integrate prospecting authored commits in listed order, then reusable
UI `fb7dc561...`; consume current feed/evidence with explicit observation dates.
Keep synthetic fixtures out of live project remarks. Exact7775 rows and ordered
Solar1000 remain the identity spine. Test feed-fresh/article-old, no-evidence,
unknown capacity and wrong project ID before adding a visible priority column.
The global news editorial score is not a project priority score.

V9.28: **transplant** only the DC expansion delta from `35facd949...` into the
new formal version; do not cherry-pick its old V9.25 folder edits. Preserve the
original12 IDs and their semantic data.100 source leads/22countries and38
quarantined candidates are not100 verified operating facilities. Integrate
official UK/US `034be1d...` as source records at its own grain, not three new
verified facilities. Parent-group links `6a198894...` remain provisional with
dated scope; capacity/geometry remain null where absent. FIGURES contract
`e0deabac...` precedes Grid/Solar/DC typed context consumers. Test real UI counts,
null maps/geometry, source detail and unchanged official REPD export separately.

Every release retains a prior tested route, meaningful change, exact-head CI,
homepage-owner pin/transform checks and public readback. No sidecar/schema or
component unit test alone increments the public release counter.
