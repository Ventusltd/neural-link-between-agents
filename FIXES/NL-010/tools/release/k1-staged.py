import sys, subprocess
sys.path.insert(0, '/home/user/estate/kuiper-belt/tools')
from check_proof import leaks
files = subprocess.run(['git', 'diff', '--cached', '--name-only', '--diff-filter=AM'], capture_output=True, text=True).stdout.split()
bad = []
for f in files:
    try:
        b = open(f, 'rb').read()
    except OSError:
        continue
    if len(b) <= 3_000_000 and leaks(b.decode('utf-8', 'replace')):
        bad.append(f)
print('K1-STAGED', len(files), 'files,', len(bad), 'leak:', ' '.join(bad))
sys.exit(1 if bad else 0)
