#!/usr/bin/env python3
"""OPUS-9 evidence officer: re-read every key of handoff/09-law/EVIDENCE.md from git objects (never a working tree).
Apache-2.0 (kuiper-belt code). One TSV row per key: section, id, key, PASS/FAIL, lines read (trimmed)."""
import re, subprocess, hashlib
E = '/home/user/estate'
NL = '/home/user/neural-link-between-agents'
def repo_dir(r): return NL if r == 'neural-link' else E + '/' + r
def git(repo, *a, binary=False):
    r = subprocess.run(['git', '-C', repo_dir(repo)] + list(a), capture_output=True)
    return r.returncode, (r.stdout if binary else r.stdout.decode('utf-8', 'replace'))
RL = 'docs/RELEASE.md'; NOTES = 'SESSIONS/202611012145-kuiper-edition-harness-notes.md'
MB = 'atlas/modules/202609031958-menu-bar.js'
K = [  # section, id, repo, sha, path, a, b, regex
 # 1. RELEASE.md: the eight steps and the rules
 ('R', 'step-1-cut', 'gridatlas', '5ec7f62', RL, 38, 38, r'^\| 1 \| cut \|.*make-generation'),
 ('R', 'step-2-preview', 'gridatlas', '5ec7f62', RL, 39, 39, r'^\| 2 \| preview PR \|.*draft PR'),
 ('R', 'step-3-acceptance', 'gridatlas', '5ec7f62', RL, 40, 40, r'^\| 3 \| owner acceptance \|.*ACCEPT G.*first line.*owner login'),
 ('R', 'step-4-release', 'gridatlas', '5ec7f62', RL, 41, 41, r'^\| 4 \| release \|.*owner merges it with \*\*rebase'),
 ('R', 'step-5-live', 'gridatlas', '5ec7f62', RL, 42, 42, r'^\| 5 \| live bytes \|'),
 ('R', 'step-6-homepage', 'gridatlas', '5ec7f62', RL, 43, 43, r'^\| 6 \| homepage \|'),
 ('R', 'step-7-served', 'gridatlas', '5ec7f62', RL, 44, 44, r'^\| 7 \| served \|.*byte for byte'),
 ('R', 'step-8-rollback', 'gridatlas', '5ec7f62', RL, 45, 45, r'^\| 8 \| rollback \|.*route C'),
 ('R', 'eight-steps', 'gridatlas', '5ec7f62', RL, 26, 26, r'Eight steps'),
 ('R', 'pointer-only', 'gridatlas', '5ec7f62', RL, 3, 7, r'Nothing else changes'),
 ('R', 'agents-never-accept', 'gridatlas', '5ec7f62', RL, 49, 53, r'Agents never record acceptance'),
 ('R', 'owner-merges', 'gridatlas', '5ec7f62', RL, 54, 55, r'Only the owner merges a release[\s\S]*rebase, never squash'),
 ('R', 'hash-each-cartridge', 'gridatlas', '5ec7f62', RL, 117, 117, r'hashing to its recorded sha256'),
 ('R', 'tested-preview', 'gridatlas', '5ec7f62', RL, 119, 121, r'tested preview is the release'),
 ('R', 'two-files', 'gridatlas', '5ec7f62', RL, 147, 151, r'revertable, byte for byte'),
 ('R', 'reverse-order', 'gridatlas', '5ec7f62', RL, 264, 264, r'pointer first'),
 ('R', 'route-c-refusals', 'gridatlas', '5ec7f62', RL, 291, 296, r'pointer has moved since'),
 ('R', 'route-c-byte', 'gridatlas', '5ec7f62', RL, 300, 302, r'byte-identical'),
 ('R', 'route-c-gates', 'gridatlas', '5ec7f62', RL, 305, 306, r'runs the gates[\s\S]*rollback/'),
 ('R', 'manifest-arch', 'gridatlas', '5ec7f62', 'atlas/current.json', 5, 5, r'IMMUTABLE_SHELL_PLUS_HASHED_CARTRIDGES'),
 ('R', 'manifest-order', 'gridatlas', '5ec7f62', 'atlas/current.json', 14, 21, r'cartridge_order'),
 ('R', 'manifest-sha', 'gridatlas', '5ec7f62', 'atlas/current.json', 31, 31, r'"sha256": "[0-9a-f]{64}"'),
 ('R', 'pr-gate-sha', 'gridatlas', '5ec7f62', 'tools/ci/pr-gate.mjs', 176, 176, r'SHA-256 mismatch'),
 ('R', 'menu-admission', 'gridatlas', '5ec7f62', MB, 8, 17, r'installs nothing until'),
 ('R', 'menu-no-silent-skip', 'gridatlas', '5ec7f62', MB, 17, 18, r'reachable[\s\S]*instead of being silently skipped'),
 ('R', 'menu-complete', 'gridatlas', '5ec7f62', MB, 122, 124, r'EXPECTED_LAYER_CONTROLS'),
 ('R', 'menu-missing', 'gridatlas', '5ec7f62', MB, 157, 157, r"missing\.push\('63 unique layer controls'\)"),
 ('R', 'ga-root-forward', 'gridatlas', '5ec7f62', 'index.html', 2, 2, r'location\.replace\(target\+window\.location\.search\+window\.location\.hash\)'),
 # 2. LAWS.md L1-L10
 ('L', 'preface', 'kuiper-belt', '018b46a', 'LAWS.md', 3, 4, r'cannot be falsified is not a\s*law|cannot be falsified'),
 ('L', 'L1', 'kuiper-belt', '018b46a', 'LAWS.md', 12, 12, r'^## L1\. The shepherd is computed, never declared'),
 ('L', 'L2', 'kuiper-belt', '018b46a', 'LAWS.md', 26, 26, r'^## L2\. Semi-major axis'),
 ('L', 'L3', 'kuiper-belt', '018b46a', 'LAWS.md', 42, 42, r'^## L3\. Eccentricity'),
 ('L', 'L4', 'kuiper-belt', '018b46a', 'LAWS.md', 57, 57, r'^## L4\. Inclination'),
 ('L', 'L5', 'kuiper-belt', '018b46a', 'LAWS.md', 72, 72, r'^## L5\. Mass'),
 ('L', 'L6', 'kuiper-belt', '018b46a', 'LAWS.md', 82, 82, r'^## L6\. Resonance'),
 ('L', 'L7', 'kuiper-belt', '018b46a', 'LAWS.md', 100, 100, r'^## L7\. Epoch'),
 ('L', 'L8', 'kuiper-belt', '018b46a', 'LAWS.md', 111, 111, r'^## L8\. Openness: the only law that judges'),
 ('L', 'L8-body', 'kuiper-belt', '018b46a', 'LAWS.md', 111, 124, r'licen'),
 ('L', 'L9', 'kuiper-belt', '018b46a', 'LAWS.md', 128, 128, r'^## L9\. Reproducibility'),
 ('L', 'L10', 'kuiper-belt', '018b46a', 'LAWS.md', 139, 139, r'^## L10\. Reconciliation'),
 ('L', 'L10-verdicts', 'kuiper-belt', '018b46a', 'LAWS.md', 152, 157, r'HONOURED[\s\S]*OVERREACHED[\s\S]*NOT EVALUATED[\s\S]*DISCLOSED'),
 ('L', 'L10-not-evaluated', 'kuiper-belt', '018b46a', 'LAWS.md', 156, 156, r'NOT EVALUATED'),
 ('L', 'L10-disclosed', 'kuiper-belt', '018b46a', 'LAWS.md', 157, 157, r'DISCLOSED'),
 # 3. ci_check K1-K4
 ('K', 'K1-def', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 8, 8, r'K1\s+no tracked file'),
 ('K', 'K2-def', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 9, 9, r'K2\s+cosmos/wafer\.tsv'),
 ('K', 'K3-def', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 10, 10, r'K3\s+every tool'),
 ('K', 'K4-def', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 11, 11, r'K4\s+keys are in time order'),
 ('K', 'K1-code', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 37, 48, r"K1 privacy"),
 ('K', 'K2-code', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 50, 60, r"K2 sums"),
 ('K', 'K3-code', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 62, 80, r"K3 syntax"),
 ('K', 'K3-root-only', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 68, 68, r"os\.listdir\(ROOT\)"),
 ('K', 'K4-code', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 82, 93, r"K4 order"),
 ('K', 'result-line', 'kuiper-belt', '018b46a', 'tools/ci_check.py', 97, 97, r"RESULT: "),
 ('K', 'workflow-on', 'kuiper-belt', '018b46a', '.github/workflows/check.yml', 6, 8, r'on:[\s\S]*push'),
 ('K', 'workflow-run', 'kuiper-belt', '018b46a', '.github/workflows/check.yml', 25, 26, r'python tools/ci_check\.py'),
 # 4. pointers
 ('P', 'ed-meta', 'kuiper-belt', '018b46a', 'editions/index.html', 7, 7, r'url=202611012027/"'),
 ('P', 'ed-link', 'kuiper-belt', '018b46a', 'editions/index.html', 11, 11, r'href="202611012027/"'),
 ('P', 'ed-replace', 'kuiper-belt', '018b46a', 'editions/index.html', 12, 12, r"location\.replace\('202611012027/' \+ location\.hash\)"),
 ('P', 'ed-meta-HEAD', 'kuiper-belt', 'HEAD', 'editions/index.html', 7, 7, r'url=202611012027/"'),
 ('P', 'ed-link-HEAD', 'kuiper-belt', 'HEAD', 'editions/index.html', 11, 11, r'href="202611012027/"'),
 ('P', 'ed-replace-HEAD', 'kuiper-belt', 'HEAD', 'editions/index.html', 12, 12, r"location\.replace\('202611012027/' \+ location\.hash\)"),
 ('P', 'st-meta', 'kuiper-belt', '018b46a', 'see-through/index.html', 7, 7, r'url=202610050609/"'),
 ('P', 'st-link', 'kuiper-belt', '018b46a', 'see-through/index.html', 11, 11, r'href="202610050609/"'),
 ('P', 'st-replace', 'kuiper-belt', '018b46a', 'see-through/index.html', 12, 12, r"location\.replace\('202610050609/' \+ location\.hash\)"),
 ('P', 'st-meta-HEAD', 'kuiper-belt', 'HEAD', 'see-through/index.html', 7, 7, r'url=202611020012/"'),
 ('P', 'st-link-HEAD', 'kuiper-belt', 'HEAD', 'see-through/index.html', 11, 11, r'href="202611020012/"'),
 ('P', 'st-replace-HEAD', 'kuiper-belt', 'HEAD', 'see-through/index.html', 12, 12, r"location\.replace\('202611020012/' \+ location\.search \+ location\.hash\)"),
 ('P', 'ed-readme-stamp', 'kuiper-belt', '018b46a', 'editions/README.md', 3, 4, r'the stamp is the key[\s\S]*Kuiper Edition 4'),
 ('P', 'ed-readme-newest', 'kuiper-belt', '018b46a', 'editions/README.md', 9, 10, r'from the pointer, not by sorting'),
 ('P', 'ed4-no-belt', 'kuiper-belt', '018b46a', 'editions/202611012027/README.md', 25, 26, r'/belt/'),
 ('P', 'ed4-keys-sha', 'kuiper-belt', '018b46a', 'editions/202611012027/proof/edition-sha256.txt', 4, 4, r'^1c293c33[0-9a-f]{56}\s+\S*keys\.json'),
 # 5. the harness notes and AGENTS.md (the law's process keys)
 ('N', 'nl008-gap', 'neural-link', '591b57c', NOTES, 19, 20, r'only the owner merges'),
 ('N', 'folder-rule', 'neural-link', '591b57c', NOTES, 39, 41, r'new dated folder[\s\S]*three[\s\S]*no `/belt/`'),
 ('N', 'readme-entries', 'neural-link', '591b57c', NOTES, 42, 43, r'current[\s\S]*edition'),
 ('N', 'folder-files', 'neural-link', '591b57c', NOTES, 44, 46, r'sha256 of every file except itself'),
 ('N', 'ci-before-push', 'neural-link', '591b57c', NOTES, 48, 49, r'RESULT: PASS[\s\S]*merge `--no-ff` into main'),
 ('N', 'android-test', 'neural-link', '591b57c', NOTES, 52, 58, r'Pixel 7[\s\S]*hasTouch'),
 ('N', 'never-accept', 'neural-link', '591b57c', NOTES, 63, 64, r'Agents never post ACCEPT'),
 ('N', 'agents-11', 'neural-link', '591b57c', 'AGENTS.md', 11, 11, r'owner acceptance'),
 ('N', 'agents-18', 'neural-link', '591b57c', 'AGENTS.md', 18, 18, r'declare `ACCEPT <generation>`, merge protected or live release branches'),
 ('N', 'nl009-01-13', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/01-bar.md', 13, 13, r'BLOCKER.*75\.1 px'),
 ('N', 'nl009-01-18', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/01-bar.md', 18, 18, r'MAJOR.*29\.0 px'),
 ('N', 'nl009-01-20', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/01-bar.md', 20, 20, r'MAJOR.*SEE THROUGH'),
 ('N', 'nl009-06-11', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/06-seethrough.md', 11, 11, r'BLOCKER.*unreachable'),
 ('N', 'nl009-06-24', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/06-seethrough.md', 24, 24, r'MAJOR'),
 ('N', 'nl009-09-11', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/09-robust.md', 11, 11, r'MAJOR.*READOUT'),
 ('N', 'nl009-09-18', 'neural-link', 'HEAD', 'FIXES/NL-009/round1/09-robust.md', 18, 18, r'MAJOR.*WebGL'),
]
bad = 0
rows = []
for sec, i, repo, sha, path, a, b, rx in K:
    if sha == 'HEAD':
        sha = git(repo, 'rev-parse', '--short=7', 'HEAD')[1].strip()
    rc, out = git(repo, 'show', '%s:%s' % (sha, path))
    lines = out.split('\n')[a - 1:b] if rc == 0 else []
    ok = rc == 0 and bool(re.search(rx, '\n'.join(lines), re.I | re.M))
    bad += not ok
    print('%s\t%s\t%s@%s %s:%s\t%s\t%s' % (sec, i, repo, sha, path, a if a == b else '%d-%d' % (a, b), 'PASS' if ok else 'FAIL',
          ' / '.join(l.strip() for l in lines if l.strip())[:200]))
# unchanged between the roadmap's head and the branch head
for p in ['LAWS.md', 'tools/ci_check.py', 'editions/index.html', 'LICENSE', 'README.md', 'editions/README.md']:
    rc, d = git('kuiper-belt', 'diff', '--stat', '018b46a', 'HEAD', '--', p)
    print('U\tunchanged:%s\tkuiper-belt 018b46a..HEAD %s\t%s\t%s' % (p, p, 'PASS' if rc == 0 and not d.strip() else 'CHANGED', d.strip()[:120]))
rc, d = git('gridatlas', 'diff', '--stat', '5ec7f62', 'HEAD', '--', RL)
print('U\tunchanged:RELEASE.md\tgridatlas 5ec7f62..HEAD\t%s\t%s' % ('PASS' if not d.strip() else 'CHANGED', d.strip()[:120]))
print('RESULT: %s (%d keys)' % ('PASS' if not bad else 'FAIL (%d)' % bad, len(K)))
