# For WT rows whose fragment moved: find the unique line now holding the fragment and rewrite the key's line number.
import re, sys
p = sys.argv[1]; R = {'kuiper-belt': '/home/user/estate/kuiper-belt'}
out = []; changed = []
for ln in open(p, encoding='utf-8'):
    cells = re.split(r'(?<!\\)\|', ln.strip().strip('|')) if ln.startswith('|') else []
    if len(cells) >= 4:
        key = cells[2].strip(); frag = cells[3].strip().strip('`').replace('\\|', '|')
        m = re.fullmatch(r'kuiper-belt@WT ([^:]+):(\d+)', key)
        if m:
            L = open(R['kuiper-belt'] + '/' + m.group(1), encoding='utf-8').read().split('\n'); n = int(m.group(2))
            if not (n <= len(L) and frag in L[n - 1]):
                hits = [i + 1 for i, l in enumerate(L) if frag in l]
                if len(hits) == 1:
                    ln = ln.replace(key, 'kuiper-belt@WT %s:%d' % (m.group(1), hits[0]), 1); changed.append((cells[0].strip(), n, hits[0]))
                else: changed.append((cells[0].strip(), n, 'hits=%s' % hits))
    out.append(ln)
open(p, 'w', encoding='utf-8').write(''.join(out)); print(changed)
