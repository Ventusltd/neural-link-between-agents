import json, subprocess, sys, random
d = json.load(open(sys.argv[1])); kp = sys.argv[2]
P = [b for b in d['bodies'] if b.get('on_wafer')]
seven = [b for b in P if 'quote_key' in b]
random.seed(20261101); extra = random.sample([b for b in P if 'quote_key' not in b], 5)
def text(k):
    o = subprocess.run([sys.executable, '-I', kp, str(k)], capture_output=True, text=True, timeout=300).stdout
    ls = [l for l in o.split('\n') if l.startswith('  | ')]
    return ls[0][4:] if ls else ('<<' + o.strip().split('\n')[-1] + '>>')
rows = []
for b in seven + extra:
    t = text(b['key']); ok = t == b['line_text']
    r = {'repo': b['repo'], 'path': b['path'], 'line': b['line'], 'key': b['key'], 'key_py': t, 'line_text_equal': ok}
    if 'quote_key' in b:
        q = text(b['quote_key']); qf = b['quote'].split('\n')[0]
        r.update({'quote_key': b['quote_key'], 'quote_key_py': q, 'quote_check_at_quote_key': q == qf or q.strip() == qf.strip()})
    rows.append(r); print(json.dumps(r, ensure_ascii=False))
print('line_text equal', sum(r['line_text_equal'] for r in rows), 'of', len(rows))
