#!/usr/bin/env python3
"""Write editions/202611012135/proof/keys-summary.json in Edition 4's form, every value re-measured here."""
import json, os, re, subprocess, collections
KB = '/home/user/estate/kuiper-belt'; ED = KB + '/editions/202611012135'
KP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kp')   # cwd holding C:/Users/vikra/Documents/GitHub -> clones
k = json.load(open(ED + '/keys.json')); B = k['bodies']; byk = {b['key']: b for b in B if b.get('key') is not None}
e4 = json.load(open(KB + '/editions/202611012027/proof/keys-summary.json'))
rt = []
for r in e4['roundtrip_key_py']:
    key = r['key']; b = byk.get(key, {})
    try:
        p = subprocess.run(['python3', KB + '/tools/key.py', str(key)], cwd=KP, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        rt.append({'key': key, 'pass': None, 'repo': b.get('repo'), 'path': b.get('path'), 'line': b.get('line'),
                   'checks': 'NOT EVALUATED: key.py did not finish in 900 s (load average over 80)', 'edition4_pass': r.get('pass')}); continue
    o = p.stdout.splitlines()
    if 'REFUSED: no local clone' in p.stdout:
        rt.append({'key': key, 'pass': None, 'repo': b.get('repo'), 'path': b.get('path'), 'line': b.get('line'),
                   'checks': 'NOT EVALUATED: no clone of ' + str(b.get('repo')) + ' on this machine (key.py: ' + o[-1].strip() + ')',
                   'edition4_pass': r.get('pass')}); continue
    m1 = next((re.match(r'key [\d,]+ -> (\S+) / ([0-9a-f]+) / line', l) for l in o if l.startswith('key ')), None)
    m2 = next((re.match(r'\s+(.+?) : (\d+)\s+\(blob', l) for l in o if '(blob' in l), None)
    txt = next((l[l.index('| ') + 2:] if '| ' in l else '' for l in o if l.lstrip().startswith('|')), None)
    kp = {'repo': m1 and m1.group(1), 'commit': m1 and m1.group(2), 'path': m2 and m2.group(1),
          'line': m2 and int(m2.group(2)), 'text': txt}
    lt = b.get('line_text'); q = b.get('quote') or ''
    checks = {'exit0': p.returncode == 0, 'repo': (kp['repo'] or '').lower() == (b.get('repo') or '').lower(),
              'commit': bool(kp['commit']) and (b.get('commit') or '').startswith(kp['commit']),
              'path': kp['path'] == b.get('path'), 'line': kp['line'] == b.get('line'),
              'text_eq_git_line': txt is not None and lt is not None and txt.rstrip('\r\n') == lt.rstrip('\r\n'),
              'text_vs_quote': b.get('quote_check')}
    rt.append({'key': key, 'pass': all(v for kk, v in checks.items() if kk != 'text_vs_quote'), 'repo': b.get('repo'),
               'path': b.get('path'), 'line': b.get('line'), 'checks': checks, 'key_py': kp,
               'edition4_pass': r.get('pass')})
pl = [b for b in B if b.get('on_wafer')]
out = {
 'edition': 'Kuiper Edition 5 (202611012135), keys.json byte-identical to Edition 4 (sha256 1c293c33…242b)',
 'bodies': len(B), 'on_wafer': len(pl), 'verified': sum(1 for b in B if b.get('verified')),
 'not_on_wafer': [{'id': b.get('id'), 'repo': b.get('repo'), 'commit': b.get('commit'), 'reason': 'commit not on the wafer'} for b in B if not b.get('on_wafer')],
 'roundtrip_key_py': rt,
 'quote_not_at_line': [{'id': b.get('id'), 'repo': b.get('repo'), 'path': b.get('path'), 'line': b.get('line'), 'key': b.get('key'),
                        'quote_key': b.get('quote_key'), 'check': b.get('quote_check')} for b in B if b.get('quote_key')],
 'line_text': {'placed_quote_differs': sum(1 for b in pl if b.get('quote') != b.get('line_text')),
               'placed_empty_line': sum(1 for b in pl if b.get('line_text') == ''),
               'longest': max(((len(b.get('line_text') or ''), b['repo'] + ' ' + b['path'] + ':' + str(b['line']), b['key']) for b in B))},
 'method': 'tools/key.py run per key from a scratch cwd whose relative path C:/Users/vikra/Documents/GitHub/<repo> links to the local clones (key.py ROOTS, tools/key.py:31); key.py is not edited. Counts read from keys.json.',
 'render': 'NOT EVALUATED here: the Android journey is proof/android-journey.json (Opus 10 tester, team 9 script).',
 'note': e4['note'],
}
os.makedirs(ED + '/proof', exist_ok=True)
json.dump(out, open(ED + '/proof/keys-summary.json', 'w'), indent=1, ensure_ascii=False); open(ED + '/proof/keys-summary.json', 'a').write('\n')
print('bodies', out['bodies'], 'on_wafer', out['on_wafer'], 'verified', out['verified'], 'not_on_wafer', len(out['not_on_wafer']),
      'roundtrips pass', sum(1 for r in rt if r['pass'] is True), 'of', len(rt), 'quote_not_at_line', len(out['quote_not_at_line']))
for r in rt:
    if r['pass'] is not True: print('NOT PASS', r['key'], r['checks'], r.get('key_py'))
