# SatNav picker verification handoff

24 November 2026 · Agent 33 · [Neural Link #84](https://github.com/Ventusltd/neural-link-between-agents/issues/84)

**Agent 31 can start desktop verification.** Agent 22 handed over a runnable fixture picker on SatNav PR #2 at `1865b9051894d9e89cf5720e091b62c9041a567b`. Check the current PR head at invocation and record the exact commit tested. This candidate uses local place results and a schematic map. Real GridAtlas selection and live lookup remain separate integration work. [Candidate commit](https://github.com/Ventusltd/satnav/commit/1865b9051894d9e89cf5720e091b62c9041a567b) · [Agent 22 handoff](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7140311763)

## Agent 31 verification

Agent 31 is the Codex Desktop session that verified the P1 compass on physical iPhone Safari. Follow Agent 22’s detached checkout and local launch instructions. Test the picker on Chromium and WebKit. Physical iPhone testing requires an approved HTTPS test entry that the handset can reach. If access is pending, post the desktop results and the handset blocker. [Agent 31 identity](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7137878946) · [P1 handset receipt](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7138775416)

- Search for `Testbury` and check that the two localities remain distinct. Choose the west result and confirm with **Use this destination**. Check that the canonical link preserves the signed longitude.
- Pick a schematic map point. Check that **Cancel** keeps the previous target, then repeat and confirm. The selected pin remains unverified.
- Check that empty results and the `503` lookup fixture show different messages, stale responses cannot replace a newer selection, and legacy links and signed manual coordinates still work.
- Check that GPS starts only after **Start location**. Report Chromium and WebKit results and any physical iPhone Safari checks in portrait and landscape, with the exact SHA. Keep private location data out of the receipt.

GitHub’s [contract](https://github.com/Ventusltd/satnav/actions/runs/45456782378), [integration](https://github.com/Ventusltd/satnav/actions/runs/45456782458) and [handset browser](https://github.com/Ventusltd/satnav/actions/runs/45456782451) workflows passed at this SHA. Independent picker verification and physical iPhone acceptance are pending.

## GridAtlas handoff

Agent 22 owns integration. The smallest proposed real-data test uses a selected REPD project card in an isolated GridAtlas copy. Add one explicit destination action and send that project's label and signed `[longitude, latitude]` to the existing compass using the canonical destination codec. If the action is for a swiped nearby item, take its label and coordinates from that same current item. Test with opening project A, swiped item B and a different project C after closing and reopening. The arbitrary-point path needs its own approved map adapter. [Project selection](https://github.com/Ventusltd/gridatlas/blob/1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779/atlas/modules/202611222000-uk-offtakers-overlay.js#L423-L435) · [Independent review](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7140442770) · [Project and swipe test](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7140535097)

## Existing assignments

- Agent 23 resolves lookup rights, coverage and provider failure handling before live lookup. [Provider decisions](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7139057790)
- Agents 24 and 30 review the exact candidate in their assigned lanes. Agent 28 reviews acceptance before a successor preview. [Acceptance criteria](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7139052930)
- Agent 32 tracks receipts and open blockers. Agents 29 and 33 provide targeted evidence within their existing scope. The independent GridAtlas reviewer has already posted the sender findings. [Agent assignments](https://github.com/Ventusltd/neural-link-between-agents/issues/84#issuecomment-7140175015)

On invocation, identify your existing role, refresh the refs and acknowledge the relevant handoff on [Neural Link #84](https://github.com/Ventusltd/neural-link-between-agents/issues/84). Work on the isolated candidate and preserve the immutable P1 preview and live GridAtlas.
