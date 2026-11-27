# VEDIC accelerator round 2 process log

Recorded 27 November 2026 UTC for Neural Link #87. The VEDIC coordinator ran the hosted loop. Four reviewers checked the prior hosted state, Neural Link placement, the offline GPU path, and the round 2 receipt.

## Hosted run

GitHub Actions ran Python 3.12, NumPy 2.4.6 and PyArrow 25.0.1 from 00:25:32 to 00:26:27 UTC. Snapshot and proposal jobs passed. The isolated workflow pinned the successful round 1 receipt by SHA-256, verified the same scoring method, and selected its next slice of hypotheses. The VEDIC scorer files match main `fbd591a9059b383b9cc5cb0ff772123546c062ee`. [Round 2 workflow commit](https://github.com/Ventusltd/vedic-/commit/e502828dd01c59f2133fae48234c6a20781db6d5) · [Round 2 run](https://github.com/Ventusltd/vedic-/actions/runs/45916636705) · [Round 1 run](https://github.com/Ventusltd/vedic-/actions/runs/45913405432)

Both runs verified Stars release 388112262, asset 796582323, and reconstructed the same element features. Round 2 used element seed 193909 and domain review-sampling seed 20261132. It processed 478,800 distinct line IDs, 34,370 elements and 33,221 indexed families. Each round evaluated 17,597,440 element–hypothesis pairs and 21,067,200 line–domain pairs. [Stars producer release](https://github.com/Ventusltd/stars/releases/tag/modular-star)

| Measure | Round 1 | Round 2 |
| --- | ---: | ---: |
| Fresh configured hypotheses tested | 512 | 504 |
| Cumulative hypotheses tested out of 4,683 | 512 | 1,016 |
| Elements with one proposed command group | 5,962 | 5,876 |
| Line IDs with a domain association | 219,113 | 219,113 |
| Distinct line IDs with one proposed group or a domain association | 255,229 | 253,173 |

The domain table matched round 1 byte for byte. The new probe slice changed the element assignments, reducing this round's line-association count by 2,056. Hypothesis coverage accumulates across rounds. Per-round associations are leads. The scan bounded the lexical input for 222 lines and the extracted features for 5,308 elements. This run made zero dictionary admissions. The public release serves 93 commands. [Live VEDIC](https://ventusltd.github.io/vedic-/)

## Evidence pins

| Evidence | SHA-256 |
| --- | --- |
| Round 1 JSON receipt | `26297f8c7a173191db18f79a2dd4d1e7998e40a0c78442fe77fe9a6c94eafd24` |
| Round 2 JSON receipt | `c78b3ddd286194ff53660b9812b20de7a3948cbab976c10f5ef415491aac6175` |
| Round 2 artifact ZIP | `973b45d1d349bdcd6069610f3df60757c1ae9faa18583a33da5435794c2a6987` |
| Scoring method | `4a78d882c882563336a76c3b659a241430fa2c7f6700f99e46ed83a3a8ee105e` |
| Compressed Stars asset | `2379a68bd54096b94efcb13fb557aa8eaad68c756b5b3fdf09a64a51da5414c1` |
| Unpacked Stars SQLite | `bc4d7ddde0e60743508bbe473ec91662f6ed26d602751c2b2738f8c2b5f66462` |
| Reconstructed feature Parquet | `d7fbf1c9d0c8d4f1a7e6f74b2f0e757af2cdc2915d420e32b5201feee3ffa371` |
| Round 2 element Parquet | `e0a07eac6052965efdff8e6b0f4f631b276187a776648a152d0228b70f102533` |
| Domain Parquet | `a5b47a6a4b963ff1867f7e60fbf598f700d99f9331f98606520262ec6da3d48b` |

Independent verification checked the two ZIP digests, the pinned source input, stable method, per-group probe counts and the one-file artifact boundary. Round 2 artifact 15162786406 contains one 25,738-byte JSON receipt. [Round 2 artifact](https://github.com/Ventusltd/vedic-/actions/runs/45916636705/artifacts/15162786406)

## Resume and offline fallback

Use the hosted NumPy workflow first. The two manual rounds form a separate reproducible evidence sequence. The scheduled state writer skipped both. At verification the durable state ref was absent, and the first new scheduled run was due at 03:37 UTC. Check the next scheduled run and its checkpoint before planning another continuation. [Nightly workflow](https://github.com/Ventusltd/vedic-/actions/workflows/modular-consumer.yml) · [Operating notes](https://github.com/Ventusltd/vedic-/blob/fbd591a9059b383b9cc5cb0ff772123546c062ee/docs/MODULAR-CONSUMER.md)

When hosted CPU is unavailable and the local GPU is free, verify the same-method checkpoint and the saved SQLite and feature digests. The MSI's installed CuPy and CUDA environment was confirmed available. To replay this round, use `estate_crib_search.search` with `backend="cupy"`, seed 193909 and `campaign=(int(method_sha256, 16), 1)`. Use `estate_domain_scan.scan_estate` with `backend="cupy"` and seed 20261132. The CuPy paths check their output against NumPy. Keep intermediate artifacts local. The hosted round 2 records GPU parity as untested. [Element scorer](https://github.com/Ventusltd/vedic-/blob/fbd591a9059b383b9cc5cb0ff772123546c062ee/tools/estate_crib_search.py) · [Domain scorer](https://github.com/Ventusltd/vedic-/blob/fbd591a9059b383b9cc5cb0ff772123546c062ee/tools/estate_domain_scan.py)
