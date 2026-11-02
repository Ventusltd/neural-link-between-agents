# shift module line refs >= START by D in EVIDENCE.md (module-context only)
import re, sys
p, START, D = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(p).read().split('\n')
def sh(m):
    a = int(m.group(2)); b = m.group(4)
    na = a + D if a >= START else a
    nb = (int(b) + D if int(b) >= START else int(b)) if b else None
    return m.group(1) + str(na) + ('-' + str(nb) if b else '')
NUM = re.compile(r'(:)(\d{2,3})((?:-)(\d{2,3}))?\b')
PROTECT = re.compile(r'(kuiper-shell\.js:\d+|index\.html:\d+|README\.md:\d+|layers\.js:\d+(?:-\d+)?|ED5 :\d+(?:-\d+)?|live :\d+(?:-\d+)?|:710 PANELS)')
def shift_text(t):
    parts = PROTECT.split(t)
    return ''.join(x if PROTECT.fullmatch(x or '') else NUM.sub(sh, x) for x in parts)
# section 1 table rows: last cell only
start1 = next(i for i,l in enumerate(L) if l.startswith('## 1.'))
end1 = next(i for i,l in enumerate(L) if l.startswith('## 2.'))
for i in range(start1, end1):
    l = L[i]
    if l.startswith('|') and l.count('|') >= 4 and not l.startswith('|---') and 'In the Kuiper module' not in l:
        cells = l.split('|'); cells[-2] = shift_text(cells[-2]); L[i] = '|'.join(cells)
# explicit module-context fragments elsewhere
FRAG = [r'resolves \(:\d+\)', r'\(module :\d+-\d+, :\d+\)', r'vs module :\d+', r'pasted link", :\d+, :\d+\)',
        r'module :\d+-\d+ header, :\d+-\d+ registration', r'`wireFind` :\d+-\d+, `openPaste` :\d+-\d+',
        r'`H\.wafer\.then\(readLocation\)` :\d+', r'`Hc\.ov` :\d+-\d+', r'`readout\(\)` :\d+', r'`editionName\(\)` :\d+-\d+',
        r'no shell :\d+', r'\(order 1e9\) :\d+, the readout \(order 40\) :\d+', r'\| :138, :259, :\d+ \|', r'\(:\d+\)\. It is in the 28-hook',
        r"`GEN = '202611012231'` \(:28, :\d+\)", r'module :1, :28, :\d+', r'module :\d+-\d+ \|', r'module :29, :\d+',
        r'module :161, :\d+, :\d+', r'comment at :\d+ and the `utcStamp` comment at :\d+', r'and in the registration \(:\d+\)',
        r'`writeNow` :\d+-\d+', r'hook table; `fmt\(\)` \(:\d+\)']
for i in range(len(L)):
    if start1 <= i < end1: continue
    for f in FRAG:
        L[i] = re.sub(f, lambda m: NUM.sub(sh, m.group(0)), L[i])
open(p, 'w').write('\n'.join(L))
