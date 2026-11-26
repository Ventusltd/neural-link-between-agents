# TACIT D Kuiper offline CUDA laboratory handoff

**26 November 2026 · Local computational research · NL-087**

The Alienware Aurora R9 passed CPU and GPU verification on the actual Kuiper wafer. The RTX 2070 SUPER processed 2,066,227 sampled addresses with exact issued membership, repository ownership and low-32-bit MOD agreement. The maximum FP64 error in x and y was 5.82 × 10⁻¹¹, with zero radius error. Independent Python arithmetic checked all 81 sentinel addresses around the wafer's 27 wrap points in the fused runs. The wafer reconciled 16,774 commit rows across 101 repositories, representing 97,540,883,985 issued keys within a 116,449,247,985-address space.

This complements TACIT D's existing Kuiper research on sparse selection, typed relationships and physical compute. The local geometry benchmark used the dated `place` and `keyPlace` law and preserves the operational `sqrt(key + 0.5)` radius. [TACIT D research direction](https://github.com/Ventusltd/neural-link-between-agents/issues/87#issuecomment-7198294799) · [TACIT D sparse-selection prototype](https://github.com/Ventusltd/neural-link-between-agents/issues/87#issuecomment-7198551415)

## Numerical performance

| Baseline batch | NumPy median | GPU resident median | GPU median with transfers |
| ---: | ---: | ---: | ---: |
| 76,151 | 7.13 ms | 0.79 ms | 2.17 ms |
| 166,151 | 17.93 ms | 0.92 ms | 3.66 ms |
| 1,066,151 | 118.95 ms | 1.80 ms | 12.30 ms |

Device 0 used driver 610.60, CUDA runtime 12.9, NVRTC 12.9.86, NumPy 2.3.5 and CuPy 14.2.0. CUDA reported 7,477,395,456 bytes free of 8,589,606,912 bytes at baseline startup. The isolated lab runtime used hash-pinned wheels installed from a local wheelhouse. The largest baseline CPU-only process peaked at 156,143,616 working-set bytes and its GPU test sampled a retained CUDA pool high water of 79,361,024 bytes.

At 2,066,227 addresses, the seven-repetition repeat reduced median CUDA event time from 3.065 ms unfused to 0.944 ms fused. Median resident wall time was 3.485 ms unfused and 1.533 ms fused. Transfer-inclusive rankings reversed between runs. The initial medians were 23.107 ms unfused and 37.833 ms fused, followed by 23.204 ms and 21.667 ms in the repeat. Fused transfer samples spanned 20.841–40.072 ms in the repeat. Sampled retained pool high water was 153,365,504 bytes unfused and 132,684,288 bytes fused in both runs. CUDA pool retention measures allocations held by the pool, with driver context and independent allocations outside its scope. The fused kernel used FP64 and NVRTC with fast math disabled.

## Relationship processing

- **Spider Genome and Printer.** Exact NumPy/CuPy parity held for directional CSR neighbor records and reverse traversal depths on both real inputs. Genome contained 1,379 nodes and 3,249 static records. Its all-node query examined 17.40 million edge records per second on CPU, 4.81 million on the resident GPU, and 3.17 million with transfers. Reverse traversal reached 2.31 million record visits per second on CPU and 80,068 on the resident GPU. Printer's 30 nodes and 164 topology references also favored CPU in the tested workloads. These rates count visits over existing evidence. The GPU traversal includes per-frontier host synchronization.
- **VEDIC sparse properties and source replay.** The original authorized request and pinned `edition_keys.py` replayed all eight A keys exactly. The eight-row sparse overlay passed CPU/GPU key, color and geometry checks. The optional MEASURE/BEARING selector and explicit Vg selected the same two entries. The full 49-row original request replayed 40 historical keys, with nine unrelated rows blocked by 58 missing Git blobs in two partial clones. The eight-row VEDIC cohort supplies correctness evidence. A performance crossover needs a larger authorized cohort.
- **VEDIC conditional traversal.** Five pinned candidate bonds across ten endpoints passed exact CPU/GPU neighbor and reverse reachability checks, preserving the condition identity of each record. All eight runtime effects remained `UNKNOWN`. Conditions were unevaluated. Observed runtime, independent review of these edge records and admission are unestablished in this lab evidence. The conditional cohort has its own receipt, alongside the Genome static and Printer topology checks.

## Evidence for TACIT D to process

Use this evidence to review the next Kuiper workload around explicit property predicates, exact source provenance and relationship traversal. Take Genome's measured CPU path as the baseline for graph work. Use the fused geometry results for address projection and keep transfer timings visible when assessing an end-to-end workload. A graph crossover experiment needs a larger representative graph with an agreed record-visit definition. VEDIC scale needs a larger authorized cohort with the same evidence contract. Browser testing, independent review and owner authorization remain gates for a dated edition.

The [aggregate JSON](20261126-TACIT-D-KUIPER-CUDA-LAB.json) carries machine-readable measurements, source pins and hashes of the original local receipts, including failed attempts. Raw receipts, peer archives and per-source keys stay in the local laboratory. The test sources and hash-locked CUDA wheel list are available there for authorized replay. Use the supplied CPU gate before GPU verification and match the input byte digests before comparing timings. [Kuiper wafer source](https://github.com/Ventusltd/kuiper-belt/tree/f7a4cb9e3a764a72b7133bb275bb5387ea083be2/cosmos) · [Spider source](https://github.com/Ventusltd/spiders/tree/830e86ea65e98b03df7250d2dd55d2753799687a)
