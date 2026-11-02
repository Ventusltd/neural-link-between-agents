#!/usr/bin/env python3
"""Re-read every key of the LICENCES.md register from git objects at the named heads (never a working tree).
Apache-2.0 (kuiper-belt code). Prints one TSV row per key: id, key, PASS/FAIL, the lines read (trimmed)."""
import re, subprocess, sys
E = '/home/user/estate'
ST = 'see-through/202610050609/'
K = [  # id, repo, sha, path, first, last, regex that must match the lines read
 ('kb-licence', 'kuiper-belt', '018b46a', 'LICENSE', 1, 3, r'Apache License'),
 ('kb-readme', 'kuiper-belt', '018b46a', 'README.md', 156, 157, r'Apache-2\.0[\s\S]*CC BY 4\.0'),
 ('kb-editions-readme', 'kuiper-belt', '018b46a', 'editions/README.md', 27, 27, r'Apache-2\.0'),
 ('kb-ed4-notice-code', 'kuiper-belt', '018b46a', 'editions/202611012027/NOTICE.md', 3, 5, r'Apache License 2\.0'),
 ('kb-ed4-notice-quotes', 'kuiper-belt', '018b46a', 'editions/202611012027/NOTICE.md', 7, 10, r'ODbL[\s\S]*(OGL|Open Government)'),
 ('kb-laws-l8', 'kuiper-belt', '018b46a', 'LAWS.md', 111, 124, r'licen'),
 ('kb-laws-disclosed', 'kuiper-belt', '018b46a', 'LAWS.md', 156, 156, r'NOT EVALUATED|DISCLOSED|examine'),
 ('ga-licence', 'gridatlas', '5ec7f62', 'LICENSE', 1, 4, r'Apache License'),
 ('ga-notice', 'gridatlas', '5ec7f62', 'NOTICE', 1, 12, r'Ventus[\s\S]*Apache'),
 ('ga-notice-thirdparty', 'gridatlas', '5ec7f62', 'NOTICE', 25, 32, r'(third|data)'),
 ('ga-trademarks', 'gridatlas', '5ec7f62', 'LICENSE', 139, 142, r'Trademarks'),
 ('ga-ventus-css', 'gridatlas', '5ec7f62', 'atlas/modules/202609031958-menu-bar.js', 184, 205, r'ventus'),
 ('st-licence', 'kuiper-belt', '018b46a', ST + 'LICENSE.md', 1, 10, r'CERN'),
 ('st-notice-head', 'kuiper-belt', '018b46a', ST + 'NOTICE.md', 3, 3, r'CERN|licen'),
 ('st-notice-files', 'kuiper-belt', '018b46a', ST + 'NOTICE.md', 8, 16, r'CERN|ODbL'),
 ('st-notice-odbl', 'kuiper-belt', '018b46a', ST + 'NOTICE.md', 22, 27, r'OpenStreetMap[\s\S]*ODbL|Open Database'),
 ('st-notice-services', 'kuiper-belt', '018b46a', ST + 'NOTICE.md', 28, 34, r'CARTO[\s\S]*Esri'),
 ('st-notice-maplibre', 'kuiper-belt', '018b46a', ST + 'NOTICE.md', 38, 39, r'MapLibre|BSD'),
 ('st-maplibre-licence', 'kuiper-belt', '018b46a', ST + 'vendor/MAPLIBRE-LICENSE.txt', 1, 1, r'.'),
 ('st-cern-text', 'kuiper-belt', '018b46a', ST + 'licences/globalgrid2050-CERN-OHL-S-2.0.txt', 1, 1, r'CERN'),
 ('st-pointer', 'kuiper-belt', '018b46a', 'see-through/index.html', 12, 12, r'202610050609/'),
 ('gg-licence', 'globalgrid2050', 'c66759f', 'LICENSE.txt', 1, 5, r'CERN'),
 ('lk-readme', 'kuiper-belt', '018b46a', 'learn-the-kuiper/README.md', 34, 37, r'licen|Apache|CC BY|CERN'),
 ('lk-notice', 'kuiper-belt', '018b46a', 'learn-the-kuiper/202610050609/NOTICE.md', 7, 11, r'CERN'),
 ('tc-licence', 'testcode', 'd09c185', 'LICENSE', 2, 4, r'Apache'),
 ('tc-notice', 'testcode', 'd09c185', 'NOTICE', 1, 12, r'Apache'),
 ('tc-notice-thirdparty', 'testcode', 'd09c185', 'NOTICE', 26, 33, r'.'),
]
NONE = [('elements', 'f7a92fb'), ('galaxies-wafers', 'fff6fc6'), ('stars', 'cbca125'), ('code-generator', '857ea81')]

def git(repo, *a):
    r = subprocess.run(['git', '-C', E + '/' + repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace')

bad = 0
for i, repo, sha, path, a, b, rx in K:
    rc, out = git(repo, 'show', '%s:%s' % (sha, path))
    lines = out.split('\n')[a - 1:b] if rc == 0 else []
    txt = '\n'.join(lines)
    ok = rc == 0 and bool(re.search(rx, txt, re.I))
    bad += not ok
    print('%s\t%s@%s %s:%s\t%s\t%s' % (i, repo, sha, path, a if a == b else '%d-%d' % (a, b), 'PASS' if ok else 'FAIL', ' / '.join(l.strip() for l in lines if l.strip())[:220]))
for repo, sha in NONE:
    rc, files = git(repo, 'ls-tree', '-r', '--name-only', sha)
    fl = [f for f in files.split('\n') if f]
    lic = [f for f in fl if re.search(r'licen|notice|copying', f.split('/')[-1], re.I)]
    rc2, g = git(repo, 'grep', '-n', '-i', '-I', 'licen', sha)
    hits = [l for l in g.split('\n') if l]
    print('none-%s\t%s@%s (tree)\t%s\t%d tracked files; licence/notice/copying files: %s; `git grep -i licen`: %d line(s)%s' % (
        repo, repo, sha, 'PASS' if rc == 0 else 'FAIL', len(fl), lic or 'none', len(hits), (' e.g. ' + hits[0][:120]) if hits else ''))
    bad += rc != 0
print('RESULT: %s' % ('PASS' if not bad else 'FAIL (%d)' % bad))
