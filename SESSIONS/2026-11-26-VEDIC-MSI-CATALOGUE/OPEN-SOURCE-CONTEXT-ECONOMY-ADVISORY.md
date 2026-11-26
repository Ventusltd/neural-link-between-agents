# VEDIC — Open-source research advisory for MSI Terminals 1, 2 and 3
26 November 2026 — TACIT b t b a

## Authority
Advisory only. Do not interrupt running work, reopen settled roles, create agents, or replace the authoritative three-terminal mandate:
https://raw.githubusercontent.com/Ventusltd/neural-link-between-agents/2cadb145a64910beac02bd21c43bd5af0cfe1426/SESSIONS/2026-11-26-VEDIC-MSI-CATALOGUE/MSI-THREE-TERMINAL-MASTER-MANDATE.md

Owner objective: use existing Blackwell GPU, Python, NumPy, CuPy and CUDA to offload repetitive computational work from the Codex context window. Store computational memory locally in Parquet and DuckDB. Produce continuous, natural, source-grounded English prose sufficient to understand software and, where tested, reconstruct equivalent behavior. No Ollama, new AI platform, model downloads or paid API calls. Reuse techniques rather than installing frameworks.

## Research references and lessons
1. Google DeepMind — Unsupervised Evaluation of Code LLMs with Round-Trip Correctness, ICML 2024.
Paper: https://proceedings.mlr.press/v235/allamanis24a.html
Implementation: https://github.com/google-deepmind/icml2024-roundtrip-correctness
Software Apache-2.0; other materials CC BY 4.0 as specified upstream. Code -> natural-language description -> independently reconstructed code -> executable equivalence tests. This is the closest published analogue to VEDIC's reconstruction experiment. Use original software as independently held oracle. Do not give reconstruction implementer original source or implementation-revealing tests. A passing sample is not proof of whole application equivalence. Record failures and improve prose without overwriting initial evidence. Existing T2 geodesy experiment follows this principle.

2. CodeWiki — https://github.com/FSoft-AI4Code/CodeWiki
MIT. Dependency-aware documentation for large repositories. Published benchmark includes Wazuh (1,446,730 lines), OpenHands (229,909), Electron (184,234), Puppeteer (136,302), Svelte (124,576). These are benchmark repository sizes, not proof of VEDIC-level complete reconstruction or verified exhaustive prose coverage. Use hierarchical component decomposition, bottom-up summaries and dependency context. Read connected source units, not isolated lines. Reassemble ordered, continuous passages at application/module level. Cache exact source and contextual hashes. Keep provenance.

3. Aider — https://github.com/Aider-AI/aider
Apache-2.0. Repository mapping using syntax extraction, dependency/reference graphs and graph ranking within a bounded token budget. Study its repo map documentation: https://aider.chat/docs/repomap.html . Adopt algorithmic principle rather than requiring Aider installation. T1 can build symbol/reference adjacency tables, sparse graph representation and seed ranking around the target function; T2 receives relevant source spans and minimal dependency context rather than entire repository. Preserve essential dependencies, conditions and precision even if rank is low. Measure recall and completeness as well as token economy.

4. Microsoft TokenEconomizer — https://github.com/microsoft/TokenEconomizer
MIT as reported in public repository research; verify pinned licence before reuse. Study mechanisms for avoiding repeated information discovery and unproductive loops. Reported mean cost reductions 18.4–30.9% across five agent-model combinations are benchmark results, not guaranteed savings on MSI. Store durable facts, processed hashes, failed attempts and verified results outside the conversation. Do not blindly retry unsuccessful commands or reload already completed source batches.

5. RepoDoc — https://github.com/SYSUSELab/RepoDoc
Licence not confirmed. Treat as research reference only until pinned licence and rights are checked. Study incremental graph-based documentation: recompute changed source and context-dependent passages, preserve unchanged records. Do not import or redistribute code until permission is established.

All upstream licences and third-party dependency/data rights must be verified at the exact selected revisions before copying, redistribution or commercial deployment. Preserve attribution and required notices. No external code has been installed, audited, or benchmarked on MSI by this advisory.

## Practical MSI application (incremental improvements, not a new scope)
T1 engineering: use existing source inventory and parser output to build sparse directed dependency graph. Establish a CPU reference implementation using installed NumPy/Python; if installed CuPy sparse capabilities permit, benchmark Blackwell acceleration for adjacency construction, graph ranking, neighborhood selection and batched numerical verification. Include host/device transfer time, memory, correctness parity, and end-to-end benefit. Use CPU where faster. Do not install additional dependencies without owner permission. Persist ranked context packets, relevant source spans and dependency identifiers locally. No GPU contention with existing tasks.

T2 semantic translation: consume bounded context packets in coherent operational order. Include target source, essential definitions, relevant dependent behavior, exact constants/units, state changes, exceptions and prior validated terminology. Retrieve only needed earlier passages/facts. Record method and source/context hash; do not request another translation for unchanged inputs. Emit detailed continuous prose, not keywords or generic summaries. Do not treat graph ranking as proof that a dependency may be omitted. Distinguish deterministic structural narration from Codex semantic candidates and independently reviewed meanings. Existing Codex is connected; CuPy performs numerical computation, not language inference. Do not circumvent Codex context/usage limits or send unauthorized source. Save checkpoints and continue offline work when semantic allowance is exhausted.

T3 integration: maintain single DuckDB writer and immutable Parquet manifests. Track source revision, source/context hashes, dependency graph version, prose order, evidence, actual work queue, errors and last completed checkpoint. Maintain explicit local handover summaries allowing context compaction or new Codex sessions without re-reading estate. Invalidation must include changed dependencies, not only edited line hashes. Keep separate counts of unique lines, contextual occurrences, structurally narrated lines, semantic candidates, independently reviewed passages and reconstruction-tested components. Retain source provenance and rights restrictions. No production publication or new admissions without approval.

## Measure, do not assume, context economy
For a small representative pilot, compare existing approach against bounded ranked retrieval with persistent local facts:
- Actual input/output token counts where exposed; otherwise explicitly labeled estimates using one consistent method. Do not invent telemetry.
- Number of repeated source reads and semantic requests; cache hits and misses; context packet size; percentage of essential dependencies included.
- CPU/GPU wall time including transfers, actual GPU utilization/VRAM when measurable, total end-to-end throughput and failures.
- Translation accuracy, omissions, semantic review coverage and prose-only reconstruction test results.
- Same pinned source, same semantic task and equivalent quality gates. A smaller context that loses behavior is not a success.
Report through normal Neural Link handoff, not per-batch chat. No new workload that disrupts the current overnight run. Adopt improvements only where measurements justify them.

## Core distinction
CuPy and NumPy can perform millions of repetitive mathematical/structural operations outside Codex context. They do not independently generate natural English without semantic intelligence. The goal is to reserve Codex context for genuinely novel interpretation and let local scripts, indexed facts, graphs and persistent storage carry everything else. The complete conversational digital twin and its reconstructability remain empirical objectives.

References are research leads, not mandates to install five platforms. Current MSI roles and owner restrictions remain unchanged.
— TACIT b t b a