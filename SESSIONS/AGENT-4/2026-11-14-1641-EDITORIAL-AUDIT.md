# Agent 4 — independent editorial audit checkpoint

**Date:** 14 November 2026, approximately 16:41 UTC; GitHub commit and issue-comment timestamps are authoritative.

**Role:** ChatGPT Agent 4, owner-authorised independent Pipeline News algorithm research, editorial relevance, verified identity, false-match/freshness source audit. Read [AGENTS.md](../../AGENTS.md), [PROTOCOL.md](../../PROTOCOL.md), [LINK-RULE.md](../../LINK-RULE.md), NL-024, NL-019, NL-022, producer and controller handoffs.

## Existing scope, ACKs, no overlap
- Agent A: release integration. Agent 1: PR #99 and TestCode #9. Agent 2: independent read-only challenge. Agent 3: independent reproducibility/release QA.
- ACK Agent 1 [6880309723](https://github.com/Ventusltd/neural-link-between-agents/issues/24#issuecomment-6880309723), Agent 3 correction [6880425282](https://github.com/Ventusltd/neural-link-between-agents/issues/24#issuecomment-6880425282); earlier Agent 4 follow-up [6880519952](https://github.com/Ventusltd/neural-link-between-agents/issues/24#issuecomment-6880519952).
- New owner directive explicitly grants separate algorithm-design and synthetic QA experiments; Agent 4 reserved exclusive branch `qa/agent4-editorial-regressions-20261114` on globalgrid2050, created from the then-current #100 exact head `20c9f21339e13ba48da3ac8810dd194b0545b8d1`, and did NOT edit #100, #99, #102, Agent 3 or production.

## Delivered
- [globalgrid2050 draft PR #104](https://github.com/Ventusltd/globalgrid2050/pull/104) **head `dc0166cf9ec57e3bfb3d56b070d1b8b52ebaad2f`**, base `acid/team1` (PR #100 feature branch, NOT main).
- Five strictly additive files: `agent4/editorial_acid_cases.json`, `agent4/audit_sources.py`, `agent4/IMPROVEMENT-PROPOSAL.md`, `tests/test_agent4_editorial_regressions.py` and branch-only `.github/workflows/agent4-editorial-acid.yml`.
- Repro counterexamples: REPD 9050 synthetic false Foston Hall acceptance, genuine Foston & Bypass dropped/downgraded, North Ray phrase collision, future UTC timestamp, manually reviewed Bypass link wrongly retained against Frodsham 14096; plus positive exact planning-ref, bypass-diode rejection, 2019 archive and correctly explicit two-project article.
- Ten ranked algorithm interventions, per-event ranking gate, six IANA cycles, official/publisher/history/candidate/search tiers, rights and DC category veto.
- Offline deterministic SHA256 input audit with 200 distinct REPD refs, alias evidence URL gaps and seven *unverified* sweep contradictions (Byers Gill, Grimsby, Mere Flats, Wentlooge, Frodsham, Craig y Perthi, Hedgehog Grove).
- At check-in creation: PR #104 file guard [43616923653](https://github.com/Ventusltd/globalgrid2050/actions/runs/43616923653) SUCCESS. Own offline ACID workflow [43616906097](https://github.com/Ventusltd/globalgrid2050/actions/runs/43616906097), integrated PR #100 acid [43616923704](https://github.com/Ventusltd/globalgrid2050/actions/runs/43616923704) and project-signals [43616923614](https://github.com/Ventusltd/globalgrid2050/actions/runs/43616923614) were RUNNING, NOT CERTIFIED. The tests intentionally assert desired behaviour and **should be RED against the existing broken baseline**; never disguise fail as xfail.

## Next
Read issue #24/#19/#22 latest comments on next invocation, obtain hosted job logs/artifact SHA, post exact reproducible failures; ask Agent 2 to challenge whether false-match rules hide genuine news and Agent 3 to verify QA artifact hashes and TestCode integration. Agent A and Agent 1 can optionally cherry-pick tests after independent review, without treating them as a producer patch. No publication and no assumption that GitHub comments wake agents.
