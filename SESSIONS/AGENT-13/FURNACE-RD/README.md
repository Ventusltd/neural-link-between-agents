# Offline Furnace research

Canonical discussion: [Neural Link 51](https://github.com/Ventusltd/neural-link-between-agents/issues/51). Coordination and producer ownership: [Neural Link 42](https://github.com/Ventusltd/neural-link-between-agents/issues/42). [Research index](../../../RESEARCH.md).

This lane supplies bounded numerical experiments and reproducible evidence to existing producers. It does not own the product shell, collectors, matching semantics or publication. Current owner direction keeps ranking mechanics behind the interface; these experiments do not introduce visible scores or UI changes. HELMUT/Furnace and other assigned producers retain their own scopes.

## Reuse the tested pilot

The [portable prospecting pilot](experiments/prospecting/furnace_pilot.py) uses actual SHA-pinned `official_candidate` and relevance functions from [globalgrid2050 commit 0cb4f71e](https://github.com/Ventusltd/globalgrid2050/commit/0cb4f71e948df23e2985f189a5a1d77e88d332b2) on explicitly synthetic records. Its two source snapshots are byte-pinned; private inputs are absent. With Python, NumPy and a compatible existing CuPy/CUDA environment, run from this directory:

```text
python -B experiments/prospecting/furnace_pilot.py --cases 7775 --output YOUR_NEW_OUTPUT_DIRECTORY/receipt.json
python -B experiments/prospecting/verify_pilot.py
python -B experiments/prospecting/furnace_pilot.py --cases 32 --inject-failure --output YOUR_NEW_OUTPUT_DIRECTORY/rejected.json
```

The deliberate-failure invocation must exit **1** with `accepted: false`. A normal accepted run exits **0**. Use a new owned output directory, preserving earlier receipts. No source acquisition occurs. GPU unavailable, changed source pins or contradictory output must fail closed.

CPU code extracts features and independently witnesses every synthetic score and string-ID order. Raw CUDA branches and a CuPy expression graph independently express additive scoring. Both GPU channels share CuPy sorting, checked against independent Python sorting; they are not two independent sorting algorithms. Twelve boundary rows cover unknown versus zero capacity, caps, freshness and ties. Case count is capped at 262,144; GPU allocations are bounded. Repeated timings do not increase unique coverage.

The [six negative/reproducibility controls](experiments/prospecting/verify_pilot.py) cover case/repeat caps, source mutation, unavailable GPU, deterministic seed and deliberately corrupted output. [Pins](experiments/prospecting/source-pins.json) identify the carried producer bytes. The snapshots are the project's existing source, included to reproduce this bounded experiment, not a competing producer implementation.

## Executed findings

The following are one-host local results, not hardware guarantees or CI results. GPU timings include synchronization, transfers and complete ordering; CPU feature extraction and compilation are separate.

| Synthetic rows | CPU NumPy median ms | Raw CUDA median ms | CuPy graph median ms | Saved receipt |
| ---: | ---: | ---: | ---: | --- |
| 69 | 0.0121 | 0.2785 | 0.3715 | [receipt](experiments/prospecting/receipt-69.json) |
| 7,775 | 0.2286 | 0.3617 | 0.4861 | [receipt](experiments/prospecting/receipt-7775.json) |
| 262,144 | 10.9054 | 1.8835 | 1.9476 | [receipt](experiments/prospecting/receipt-262144.json) |

All saved successful receipts report zero numerical differences. [Injected corruption](experiments/prospecting/receipt-injected-failure.json) was rejected. Small current-size scoring favors CPU; larger arithmetic batches merit measurement. CPU feature extraction/oracle time dominates the larger synthetic runs, so this does not establish end-to-end acceleration.

A separate existing Pipeline preflight was freshly replayed on its **old 7,680-record snapshot**. All sixteen source partition hashes matched its historical inputs. Across 1,024 query executions, full masks/counts/sums, sixteen original-record scalar witnesses, sixteen top-20 order comparisons and nonfinite thresholds passed. There are **514 distinct queries / 3,947,520 unique record-query states**; 7,864,320 pairs per pass and eleven timed passes are repeated evaluations. Latest warm resident-array filtering/count/sum medians were 39.7545 ms NumPy and 0.480600 ms GPU wall. Loading, preparation, transfers, ranking and browser work were excluded from that warm comparison. The CPU reference is not an indexed database. See the [source-linked handoff](https://github.com/Ventusltd/neural-link-between-agents/issues/51#issuecomment-6925126331). This old snapshot does not certify the current 7,775-row inventory or Solar-1000.

The complete offline solar implementation also passed a fresh 256-case scalar/NumPy/CuPy sample across ten numeric fields and verdict/packed-design/cell comparisons. Its repository copy lacks a dependency present in the offline package; those source versions were not silently equated. Earlier million/billion-case and coordinate receipts were studied as historical evidence, not rerun at their original scale.

## Twelve-hour review window

The owner requested hourly reviews for twelve hours, using a local R&D lab. The configured task reads current public coordination and bounded linked Git references, runs required offline checks, rehashes an allowlist of historical inputs, attempts four independent Astra reviews and posts a compact note to NL-051. It requires an awake machine and logged-in user. An end boundary and wrapper deadline enforce the window. An issue comment alone does not schedule or wake agents.

Two initial scheduled runs completed local checks but only 1/4 and 2/4 model reviewers connected. Their notes correctly remain incomplete. Transport retries are bounded; no complete unattended four-review success is claimed. Subsequent notes carry the actual outcome. The existing ten-minute reader is separate and was preserved.

Numeric parity does not prove rights, source truth, independent corroboration, matching legitimacy, browser behavior, database durability or deployment. Preserve the complete official inventory, exact Solar-1000 and typed unknowns. Recheck current producer commits and inputs before applying any result.
