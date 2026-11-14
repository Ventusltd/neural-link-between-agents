# The two procedures, as the repositories define them (TWIN engineer, NL-016)

Read at: Ventusltd/star-quantum-twin 715f19d, Ventusltd/kuiper-belt 02dc6cd, Ventusltd/testcode 21c9255,
neural-link FIXES/NL-010 and NL-011. Quotations are short and exact; nothing here is inferred beyond them.

## 1. Quantum twin (star-quantum-twin)

- `twins/README.md:3-9`: "A rule joins the Quantum Twin Star only with its twins": the **principal** (the rule in one
  statement), the **twin** ("the measured reality that makes it true, with numbers. Agreement between two things built
  here proves consistency, not truth, so at least one twin comes from measurement"), the **positron** ("the observations
  that would make it false. Each one can be tested") and **witnesses** (independent agents asked to refute it).
  "Coupling is measured, not asserted: each clause of the principal names the check that holds it." Worked example:
  `twins/R5-site-tile.json` (schema `quantum-twin.rule-twin.v1`).
- Generations with their own proof: `proof/publish-gen2.mjs:14,19` writes `publication.json` with
  `previous_generation` and "Every shipped file with bytes and sha256"; `PUBLISHED.md` is the same table.
- Pinned sources, refused on mismatch: `README.md:106-107` "a bucket whose hash does not match, or cannot be computed,
  is not used"; sources and outputs with sha256 are in `data/provenance.json` (README "Data sources").
- A "Verified" list and a "Not verified" list close the README, with desktop 1440, phone 430 and rotation runs.

Applied to GridAtlas: principal = "generation G is exactly what its source produces"; twin = a measured second build
from the pinned register that must equal the committed bytes; positron = the mutations that must turn it red (run, see
REPORT); pins refused on mismatch; verified and not-verified lists.

## 2. Kuiper (kuiper-belt, NL-010, NL-011)

- The first law, `README.md:29-40`: "no claim without a key". "A statement **with** a key is a fact: anyone can
  recompute it on any machine and must get the same answer." "A statement **without** a key is a candidate."
  "A check that examines nothing refuses. It does not pass."
- Editions, `editions/README.md:3-9,39`: an edition is "keyed by its cut stamp", each line "keyed by
  `repo@commit path:line` and verified against a clone before it is placed"; the stable link opens the newest;
  "Earlier dated folders are kept unchanged as history. Find the newest edition from the pointer". Each edition holds
  its `README.md`, `register.tsv` ("the evidence") and `proof/` ("the digests": `proof/edition-sha256.txt`,
  `journey-pixel7.json`, `journey-galaxy-s24.json`).
- Journeys replayed on two phones before release: `editions/202611021201/README.md:30` "journey-6, Pixel 7 16/16 and
  Galaxy S24 16/16"; NL-011 `DECISIONS.md` D004: the pointer "will wait for a finished two-phone journey".
- Never edit in place: NL-011 `DECISIONS.md:35` (D005) "A listed file is never edited in place. Rev 5 may come only
  under a new stamped name." Sealed data: `editions/202611021201/README.md:21`.
- The twin register, `SPEC.md:109-121`: "one matching commit certifies every key inside it"; a per-key comparison
  "would be a check that cannot fail".
- The checker is independent of the author: `tools/check_proof.py:2-4`.

Applied to GridAtlas: a generated register of keys per generation (claim, measured value, file:line or command);
preservation of every earlier `atlas/v/<G>/`; refusal instead of a vacuous pass; URLs pinned to a commit.

## 3. Ordering (testcode)

`README.md:11-13`: "1. offline run on the machine, no socket. If any fails, stop. 2. network only after 1 is green.
3. publish only after 2. Nothing here publishes."
