#!/usr/bin/env python3
"""Split the Team 1 patch tree (pt/) into one unified diff per fix, each against <workspace>/gg-wt (wt/ copy).
Every change block (difflib opcode) is assigned to exactly one fix by keyword; unassigned blocks abort."""
import difflib
from collections import defaultdict
from pathlib import Path

T = Path("<workspace>/teams/1")
WT, PT, OUT = T / "wt", T / "pt", T / "patches"
OUT.mkdir(exist_ok=True)

RULES = {
    "automation/repd/run.py": [
        ("0001", ["SystemExit"]),
        ("0004", ["acceptance_waivers", "waive", "waived_cells", "acceptance_waive_cells"]),
        ("0006", ["known_coordinates", "kcoord", "**kw"]),
    ],
    "automation/repd/validate.py": [
        ("0005", ["_MDY_ANY", "_csv_text_is_date", "swap", "different date", "typed XLSX date", "invalid.append", "continue", "resolved.append", "dt = xd"]),
        ("0006", ["known_scope", "known_coordinates", "load_known_coordinates", "coord_anoms"]),
    ],
    "automation/repd/build_root.py": [
        ("0002", ["tempfile", "scratch", "registry", "resolve()", "import os", "chdir"]),
        ("0009", ["normalise_descriptor", "release_id"]),
    ],
}
WHOLE = {  # file -> fix (all changes of the file)
    ".github/workflows/repd-release-candidate.yml": "0003",
    "automation/repd/hashguard.py": "0007",
    "automation/repd/baselines/2026q3_known_anomalies.json": "0008",
    "dist/manifest_v4_2026q3.json": "0010",
    "docs/repd/2026q3/changes-jan-to-oct/changelog.md": "0011",
    "docs/repd/2026q3/changes-jan-to-oct/diff.json": "0011",
    "automation/repd/tests/test_hardening_nl013.py": "0012",
}
NAMES = {
    "0001": "run-stage-catches-systemexit",
    "0002": "build-root-master-in-scratch-dir-no-config-needed",
    "0003": "workflow-sparse-config-and-hidden-path-check",
    "0004": "run-acceptance-waivers-from-known-anomalies",
    "0005": "validate-date-gate-rejects-different-or-unparseable-dates",
    "0006": "validate-coordinate-waivers-scoped-to-known-coordinates",
    "0007": "hashguard-rehash-skip-worktree-and-assume-unchanged",
    "0008": "baseline-known-anomalies-2026q3-coordinates-waiver-observations",
    "0009": "build-root-accepts-v1-descriptor-shape",
    "0010": "data-manifest-v4-2026q3-source-hashes",
    "0011": "data-jan-to-oct-change-report-regenerated-from-shipped-csv",
    "0012": "tests-hardening-nl013",
}


def lines(p):
    return p.read_text(encoding="utf-8").splitlines(keepends=True) if p.exists() else []


def udiff(rel, a, b):
    out = list(difflib.unified_diff(a, b, fromfile=f"a/{rel}" if a else "/dev/null", tofile=f"b/{rel}", n=3))
    fixed = []
    for ln in out:
        fixed.append(ln if ln.endswith("\n") else ln + "\n\\ No newline at end of file\n")
    return "".join(fixed)


per_fix = defaultdict(str)
for rel, rules in RULES.items():
    a, b = lines(WT / rel), lines(PT / rel)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    variants = defaultdict(list)  # fix -> list of opcodes
    for op in sm.get_opcodes():
        tag, i1, i2, j1, j2 = op
        if tag == "equal":
            continue
        text = "".join(a[i1:i2] + b[j1:j2])
        hits = [fix for fix, kws in rules if any(k in text for k in kws)]
        if len(hits) != 1:
            raise SystemExit(f"{rel}: block {op} matched {hits}:\n{text[:400]}")
        variants[hits[0]].append(op)
    for fix, ops in variants.items():
        new, pos = [], 0
        for tag, i1, i2, j1, j2 in ops:
            new += a[pos:i1] + b[j1:j2]
            pos = i2
        new += a[pos:]
        per_fix[fix] += udiff(rel, a, new)
for rel, fix in WHOLE.items():
    per_fix[fix] += udiff(rel, lines(WT / rel), lines(PT / rel))

for fix, text in sorted(per_fix.items()):
    path = OUT / f"{fix}-{NAMES[fix]}.patch"
    path.write_text(text, encoding="utf-8")
    print(path.name, text.count("\n@@"), "hunks", len(text), "bytes")
