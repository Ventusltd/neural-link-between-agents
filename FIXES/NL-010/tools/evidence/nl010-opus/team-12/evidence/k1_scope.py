import io, os, sys, subprocess
ROOT = '/home/user/estate/kuiper-belt'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from check_proof import leaks
files = []
for base in ['see-through', 'editions/202611012135/handoff/12-see-through-reader']:
    for d, _, fs in os.walk(os.path.join(ROOT, base)):
        files += [os.path.join(d, f) for f in fs]
bad = [f for f in files if os.path.getsize(f) <= 3_000_000 and leaks(io.open(f, encoding='utf-8', errors='replace').read())]
print('team-12 scope K1: %d files scanned, %d match a private digest' % (len(files), len(bad)))
for b in bad: print('  ', os.path.relpath(b, ROOT))
