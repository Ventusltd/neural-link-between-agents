"""Which catalogued elements can be placed on the live wafer at a key of their own?
An element is placeable when at least one of its register files names a commit that is a row of
cosmos/wafer.tsv (sha12 match) in a repository the wafer names. Reads only; prints counts."""
import json, collections
E = json.load(open('/home/user/estate/elements/catalogue/elements.json'))
W = [l.rstrip('\n').split('\t') for l in open('/home/user/estate/kuiper-belt/cosmos/wafer.tsv') if l.strip() and l[0] != '#']
R = {int(p[0]): p[1] for p in (l.rstrip('\n').split('\t') for l in open('/home/user/estate/kuiper-belt/cosmos/repos.tsv') if l.strip() and l[0] != '#')}
sha12 = {w[3]: (R[int(w[2])], int(w[0]), int(w[1])) for w in W}
with_files = [e for e in E if e['files']]
placeable, by_app, commits_used = [], {}, set()
for e in E:
    hits = [(f['repo'], f['path'], f['commit']) for f in e['files'] if f['commit'][:12] in sha12]
    if hits: placeable.append(e['key']); commits_used.update(h[2][:12] for h in hits)
    if e['kind'] == 'app': by_app[e['key']] = (len(e['files']), len(hits), sorted(set(h[2][:7] for h in hits)))
print('elements', len(E), 'with files', len(with_files), 'placeable (a file commit is a wafer row)', len(placeable),
      'not placeable', len(E) - len(placeable), 'distinct commits used', len(commits_used))
print('by kind placeable:', collections.Counter(next(x['kind'] for x in E if x['key'] == k) for k in placeable))
print('by kind all:', collections.Counter(e['kind'] for e in E))
print('apps: key -> (files, files on wafer, commits)', by_app)
allc = collections.Counter(f['commit'][:12] in sha12 for e in E for f in e['files'])
print('file rows total/on wafer:', sum(allc.values()), allc[True])
repos_named = collections.Counter(f['repo'].split('/')[-1] for e in E for f in e['files'])
print('repos named by element files:', dict(repos_named))
print('of which not on the wafer:', [r for r in repos_named if r not in set(R.values())])
