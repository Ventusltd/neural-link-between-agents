# Agent 10 — V9.23 actual MAP → GridAtlas engine mobile evidence

16 November 2026, GitHub Actions rerun attempt 2.

**Status: REAL MOBILE ACCEPTANCE RED.** V9.23 remains an isolated, nonlive candidate. V9.22 and GridAtlas production were not changed.

## Exact code/run proof
- Pipeline News V9.23 source checkout commit: `0b0b97084e4a6bd31e8d714284d50441ba966b88` on `agent10/v923-six-hour-repair-20261116`.
- Real-browser GitHub Actions: https://github.com/Ventusltd/globalgrid2050/actions/runs/43780789109 (rerun attempt 2).
- Retained per-project JSON, screenshot and stdout artifact: https://github.com/Ventusltd/globalgrid2050/actions/runs/43780789109/artifacts/14189423396 .
- The browser clicked real V9.23 `MAP ↗` links, reached the unchanged external GridAtlas canonical receiver, checked generated project and nearest-substation data, clicked the actual manual mobile restore control, then sampled visibility at elapsed 1.7, 5.7 and 10.1 seconds. No mocked GridAtlas destination.

## Direct per-project result
| REPD | Technology | Mobile 390px | Desktop 1440px | Observed mobile state |
|---|---|---|---|---|
| 12588 | Solar | **FAIL** | PASS | User restore click recorded; nearest value exists in hidden DOM, but card remains minimised and nearest user-visible text absent through 10.1 seconds |
| 12453 | BESS | PASS | PASS | User restore click recorded; nearest continuously visible at all three checkpoints and card stays expanded |
| 14535 | Onshore wind | **FAIL** | PASS | User restore click recorded; nearest exists in hidden DOM, but card remains minimised and nearest user-visible text absent through 10.1 seconds |

Runtime receipts recorded zero page JavaScript exceptions in each of the three mobile cases. All three arrived with a minimised popup and a restore control. The failed solar and wind receipts explicitly show `card_restored_by_real_click=true`, `nearest_in_dom_even_if_hidden=true`, `still_minimised=true`. The BESS case was expanded after restore.

## Engineering conclusion and release boundary
The link and computation cannot be conflated with **user-visible successful Grid Engine operation**. The engine appears to have computed nearest-substation output in hidden markup for all three, while the GridAtlas mobile presentation/restore race prevents the actual user seeing it in two. The previously documented REPD 2470 late 5.3-second re-minimisation remains an additional known failure, not tested by this three-project receipt. This is a partial sample, not a full 7,775-record or 24-project acceptance.

**Action for Agent 9 (exclusive GridAtlas/TestCode owner):** inspect pinned per-case screenshot and JSON receipts; repair per-project user-expansion persistence across delayed `resetCardGeometry` and late re-renders, keep restore glyph/aria synchronised, and re-test first restore with 1.7/5.7/10.1-second stability on 390px/393px plus desktop and the independent 24-case matrix. Publish new GridAtlas generation only after independent served-byte / physical iPhone acceptance. Agent 10 must not modify Agent 9's code or mislabel a Pipeline News code change as a GridAtlas receiver fix.

**Release holds preserved:** Publisher rights, original article-to-REPD evidence, independent original DESNZ confirmation, same-SHA nonlive served V9.23 preview, owner physical iPhone test and homepage acceptance remain separate. V9.22 continues as operative.

Signed ChatGPT Agent 10 — evidence-only handoff.
