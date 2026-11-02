import sys
sys.path.insert(0, '/home/user/estate/kuiper-belt/tools')
from check_proof import leaks
bad=[f for f in sys.argv[1:] if leaks(open(f,encoding='utf-8',errors='replace').read())]
print('K1', len(sys.argv)-1, 'files,', len(bad), 'leak:', ' '.join(bad)); sys.exit(1 if bad else 0)
