# Overnight scope for all agents — 18 November 2026

**Cutoff: 08:00 UTC, 18 November 2026.** Deliver ten tracked engineering steps and target **three new Pipeline News versions and two new GridAtlas versions**, all discoverable from the globalgrid2050.com homepage. Each version builds on the accepted predecessor. Keep earlier versions accessible through individually labelled archive links and immutable edition routes. The mobile REPD MAP defect is the first priority.

This copy consolidates the owner's directions for sign-off. Existing authorization to implement, test, review, merge and publish within this scope continues while sign-off is recorded.

## Agents and ownership

| Lead or worker | Responsibility |
|---|---|
| Grid Analyser | Commands Pipeline News, coordinates cross-product dependencies, assesses release evidence and assigns the single homepage publishing turn. |
| Scope controller, reporting to both leads | Tracks the ten steps and five releases, owners, branches, checks, blockers and Deep Research. Posts independent progress commentary every 5–10 minutes in Neural Link #65 and alerts both leads to material blockers. |
| Pipeline mobile and Journey worker | Owns Pipeline MAP handoff and browser Back, then the REPD, data-centre and substation JOURNEY actions. Executes Pipeline publication in the agreed order. |
| Pipeline intelligence worker | Owns news and official-document improvements, Covenant context and links between news and Journey. Can independently review another worker's changes. |
| Train Conductor | Commands GridAtlas and the Journey engine, coordinates acceptance of the two Atlas versions and their homepage listings. |
| GridAtlas mobile and QA worker | Owns the Atlas mobile arrival fix and end-to-end browser diagnosis. Independently reviews other workers' changes. Another worker reviews this worker's changes. |
| Native Journey worker | Owns the native Journey controller, Grid/Layers entry, evidence states and reuse of the existing planner and preview. |
| Vicinity and release integration worker | Owns radius, voltage filters, nearby assets and integration of approved visual reuse. Assembles GridAtlas generations and executes their releases and coordinated homepage updates. |

Two leads and up to six delegated workers, three per lead. Both leads direct and assess evidence. Workers implement, test and execute releases on isolated branches. Use actual available slots. One publisher edits the homepage owner and domain publisher at a time.

## Five release deliverables

| Release | What readers get | Acceptance |
|---|---|---|
| **PN-01 — Pipeline News mobile MAP** | One native tap opens the selected REPD project in the current tab on touch-first devices. Back returns to the Pipeline view with its search and filters. Desktop retains its existing opening behaviour. GridAtlas shows a useful result on arrival. Candidate V9.42. | Real taps on the dated and homepage-linked release, correct REPD identity, receiver boot, visible nearest-grid result or an honest reason it is unavailable, and Back recovery. Requires the corrected Atlas receiver to be served. |
| **GA-01 — GridAtlas mobile arrival and native Journey** | Compact mobile arrival with project, nearest result and a clear Details control. Grid, Layers and direct links open the same Journey controller. Integrate the existing evidence ledger, planner and native preview. Candidate V9.192. | Android first-tap and rotation, visible result, keyboard and touch controls, stable inherited layers, correct deep-link origin, native open/close lifecycle, reduced motion and explicit evidence states. |
| **PN-02 — JOURNEY actions beside MAP** | REPD projects, data centres and substations open the same native GridAtlas feature used by Layers. Each link carries a stable origin identity and documented location. Where a location is unavailable, explain why. | Real mobile and desktop activation from each entry, matching origin after load or retry, preserved MAP and exports, and return navigation. Builds on PN-01 and the accepted Atlas entry contract. |
| **GA-02 — Vicinity and scenarios** | Explore nearby generation, demand, substations and documented upgrades within 1–50 km in 1 km increments. Filter available voltage bands. Give learners an easy first use and let advanced users explore scenarios using supported controls, with user assumptions clearly marked. Optional Kuiper/Vogel Sunflower schematic if licensing, usability and performance checks pass. | Radius boundaries, filters, provenance, correct distances, accessible controls and measured mobile performance. Distinguish nearby assets, documented routes, schematic segments and user assumptions. Keep the geographic map anchored to real locations. Builds on GA-01. |
| **PN-03 — Energy news, official documents and Journey links** | Improve relevant headline discovery, attribution, deduplication and dates. Link eligible news and official upgrade records to well-supported Journey origins. Journey links back to relevant news. Include the UK Data Centre Covenant and clear behind-the-meter versus network-side context where documented. | Pinned real-input tests, independent source/fact review, typed dates, capacity and efficiency values, document provenance and reliable links. Topic context and source-backed asset links are labelled appropriately. Builds on PN-02. |

## Ten tracked steps

1. **S01 — Baseline and ownership.** Verify live editions, source pins and rollback points. Allocate exclusive branches and maintain the common tracker. Use the canonical Vicinity archive in Neural Link PR57.
2. **S02 — Reproduce mobile MAP.** Trace actual taps from open to receiver boot, project identity and visible grid result. Retain first attempts. Test representative REPD projects and technologies, foreground/background, cold/warm, portrait/landscape and Back.
3. **S03 — Repair sender and receiver.** Implement the Pipeline native touch handoff and GridAtlas visible arrival result. Prove the combined public journey, with Android as the main target and WebKit regression for the reported iPhone failure.
4. **S04 — Integrate Journey foundations.** Reuse the reviewed evidence ledger, bounded graph planner and native Journey preview. Verify input identities, transformer handling, parallel edges, cycles, limits and missing evidence.
5. **S05 — Deliver shared entry points.** Use one Journey controller from REPD, data centres, substations and GridAtlas Layers. Preserve selected origin and radius across loading and retries.
6. **S06 — Deliver Vicinity.** Add the radius, voltage, nearby asset and upgrade views. Show source and availability clearly, with usable controls for different experience levels.
7. **S07 — Evaluate and reuse Sunflower.** Reuse the existing Kuiper and Helmut Vogel work with attribution if it passes. Offer a labelled schematic with a static or reduced-motion option. Core mobile and map delivery takes priority.
8. **S08 — Link News and Journeys.** Improve useful headline access and connect relevant source-backed items to asset or vicinity views. Keep topic suggestions distinct from project evidence.
9. **S09 — Improve official intelligence.** Extend the existing Python extraction and GRID/DOCS presentation. Link the official Data Centre Covenant as policy context and qualify national estimates, design expectations and site facts.
10. **S10 — Publish and hand over.** Run independent CI and public readback, verify homepage links and rollback, and update the overnight ledger. Continue useful fixes and verification until cutoff, then preserve unfinished work and publish the handover.

## Publication, evidence and control

- Each publication requires an exact reviewed commit, applicable GitHub Actions checks, a rollback point, actual served verification and successful browser use from globalgrid2050.com. Use hosted Linux for formal checks Windows cannot complete. Record the original result and any bounded retry.
- Publish the corrected Atlas receiver before final PN-01 homepage acceptance. Serialize homepage updates using the dedicated globalgrid2050-homepage owner repo and the domain publisher pin/import. Add current and prior reader-visible links. Verify the real homepage, dated routes and previous-version links after deploy.
- Aim for roughly one publication per development hour where gates permit. Count only verified product publications. Continue work after the fifth publication through 08:00 UTC. Stop launching work at cutoff and record release counts, exact evidence, unresolved failures and the next action for each unfinished item.
- Use Android Chrome for primary touch, portrait/landscape, Back and Journey coverage. Check Safari/WebKit because the reported device was an iPhone. Label emulated and physical device evidence accurately.
- Preserve the 7,775 canonical REPD records, frozen Solar-1000 identities, CSV and MAP contracts, archive bytes and rollback snapshots. Nearby assets, schematic segments, hypothetical scenarios and documented network routes require distinct labels. The train cursor represents exploration. Power flow and capacity claims require qualifying evidence.
- Use **Grid Journeys — exploring the patterns of energy**. Keep language neutral and international. Credit Vogel and reused code according to their licences. Present the Data Centre Covenant as policy context. A project-level compliance claim requires a separate assessment.
- Keep work within the existing tools and authorized source rights. Paid services, GPU setup, restricted NUAR imports, unlicensed publication and a public suggestions backend are outside this run.
- The scope controller reviews both teams every 5–10 minutes in Neural Link #65 and watches the research branch, PR63 and issue64. It checks the report against existing work and routes useful findings and blockers to both leads. The present engineering programme proceeds while research is in progress.

Scope records: [Command and authorization](https://github.com/Ventusltd/neural-link-between-agents/issues/42#issuecomment-6964495738), [scope controller](https://github.com/Ventusltd/neural-link-between-agents/issues/65), [research intake](https://github.com/Ventusltd/neural-link-between-agents/pull/63), [official Data Centre Covenant](https://www.gov.uk/government/publications/data-centre-covenant/the-data-centre-covenant).

## Owner sign-off

**Approved — this is the scope for all agents through 08:00 UTC on 18 November 2026. Deliver three new Pipeline News versions and two new GridAtlas versions on globalgrid2050.com, with history retained and the stated CI and public acceptance checks.**

Signed: ____________________     Date/time (UTC): ____________________
