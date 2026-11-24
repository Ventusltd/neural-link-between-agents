# Independent SatNav cartridge and unique-code audit

Owner request: isolate cartridges and verify CVAA, Spiders, Stars and the existing periodic table, without changing public applications. This branch is test-only. No production publish or persistent catalogue write.

## Connected architecture
- [Periodic table](https://ventusltd.github.io/stars/table.html) — existing block selection UI.
- [Stars](https://github.com/Ventusltd/stars/tree/7c90d879688ca80c7ed63982eec0894fe75d67a3) — permanent line / element / family identity; compare actual exact and format-normalised functions, not claimed semantic equivalence.
- [Spider periodic table graph](https://ventusltd.github.io/ventus-grid-engine/?graph=periodic-table) — relationships and source provenance.
- [Code Generator](https://ventusltd.github.io/code-generator/) — existing assembly interface; the substation finder recipe Si,Vn,Ug,Ps,Dt is candidate evidence, not a full runtime.
- [CVAA](https://github.com/Ventusltd/cvaa/tree/b124c39e5343b24dd5b546a0c279a1c06360bdad) — pinned registry and self-tests.
- [SatNav picker](https://github.com/Ventusltd/satnav/tree/5b6988949e5a8b259aec4b8116878d23eed3501a/nav) — fixture-only, no actual satellite map or live gazetteer.
- [GridAtlas composition](https://github.com/Ventusltd/gridatlas/blob/1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779/atlas/current.json) — authoritative active cartridge list.

## Independent audit
Read-only pinned checkouts; no live pointers, release DB or provider queries. Workflow checks exact manifest hashes/syntax for all nine active cartridges, standalone picker confirmation/invalid replacement/reselection, Stars exact duplicate/reformat/change tests and two held-out suspected identity collisions, plus existing Stars/CVAA/Spider tests and actual periodic table/preset/recipe linkage. CVAA consumer result is separate from its self-test. Every failure is retained; no claim of live UI or complete estate coverage. Stars default-branch/history scan omits unmerged work, short functions and certain files by design. Permanent IDs must not be reset or migrated without separate review. Periodic table link here does not change published UI; actual SatNav block registration is a future owner-side task following accepted integration and refresh.

Run `node SESSIONS/AGENT-22/CARTRIDGE-AUDIT/audit.mjs audit-inputs audit-receipts` after pinned inputs and Stars dependencies are prepared. See the one-shot workflow for exact setup.

## Successor audit
Historical red run [45459688676](https://github.com/Ventusltd/neural-link-between-agents/actions/runs/45459688676) remains immutable. This successor fixes the harness assumption that storage order equals cartridge_order, verifies distinct registry membership, declared loader traversal and actual shell/anchor structure separately, records each cartridge hash/syntax individually and checks declared byte metadata independently. Picker invalid replacement now asserts returned invalid status, null pending and refused confirm. Pin script and workflow together to 5b6988949e5a8b259aec4b8116878d23eed3501a. Preserve the Stars identity assertions and CVAA actual exit; red is expected until all substantive findings are resolved. No live changes.
