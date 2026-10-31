# Steps 5–7 evidence, generation 202610312138 (v9.188)

All times UTC, 2026-10-31.

| step | what | evidence | result |
|---|---|---|---|
| 3 | owner acceptance | https://github.com/Ventusltd/gridatlas/pull/80#issuecomment-6550183092 (owner login, 22:48:55) ; `acceptance.mjs` → `ACCEPTED` | PASS |
| 2 close | preview PR rebase-merged | https://github.com/Ventusltd/gridatlas/pull/80 → main 285148aa (22:50:04) | PASS |
| 4 | release-accepted.mjs → release PR | https://github.com/Ventusltd/gridatlas/pull/81 ; 8/8 gates (11-release-gates.log) ; rebase-merged → main 41729af0b49dcfbe8f2a3ebc485eff217a61b84d | PASS |
| 5 | check-live --wait (live-bytes) | https://github.com/Ventusltd/gridatlas/actions/runs/41250154007/job/124681813343 | PASS |
| 6a | homepage label | https://github.com/Ventusltd/globalgrid2050-homepage/pull/4 → main 30470e127ab6359957cefd7cbf6919574f192f2e ("V9.188 - 31 October 2026") | PASS (checks job success) |
| 6b | catalogue pin + restore point v135 | https://github.com/Ventusltd/globalgrid2050/pull/49 → main 35b5be2fa44603defb47a924f611a748b2db29c7 ; restore-point run https://github.com/Ventusltd/globalgrid2050/actions/runs/41250539956 | PASS (size-guard success; language gate not runnable: MSI runner offline; local run FAIL with two pre-existing findings identical on main; owner chose to merge; wording issue https://github.com/Ventusltd/globalgrid2050-homepage/issues/5) |
| 6c | deploy-pages | https://github.com/Ventusltd/globalgrid2050/actions/runs/41251556591 (build, deploy, verify_v9_7_candidate, report) | PASS |
| 7 | served-homepage (verify-live, dispatch) | https://github.com/Ventusltd/gridatlas/actions/runs/41252100497/job/124687567204 | PASS |

Out of scope, recorded: METHODS.md 190 vs 212, lane id "out", licence_status unverified (data-grid-gb); the Cowley pin (gridatlas G2, needs a sorted node_names writer first); the two "measured" sentences on the homepage (globalgrid2050-homepage issue #5); the MSI runner offline since 2026-10-29.
