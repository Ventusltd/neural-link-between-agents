"""Read-only exhaustive command/sense audit; no package execution.
Usage: python audit_resolution.py /path/to/vedic-checkout --out receipt.json
Use --projection only for a reduced fixture; never confuse it with full checkout.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re


def audit(root, output, projection=False):
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()
    compiler = root / 'tools/semantic_compiler.py'
    dictionary = root / 'data/dictionary.json'
    registry = root / 'data/command-execution-bindings.json'
    report = {'schema': 'satnav02.vedic-resolution-audit.v1',
              'mode': 'PROJECTED_FIXTURE' if projection else 'CHECKOUT',
              'sha256': {str(p.relative_to(root)): digest(p) for p in (compiler, dictionary, registry)},
              'stages': {}, 'failures': []}
    def save():
        tmp = output.with_suffix(output.suffix + '.tmp')
        tmp.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        tmp.replace(output)
    save()
    spec = importlib.util.spec_from_file_location('semantic_compiler', compiler)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rows = json.loads(dictionary.read_text(encoding='utf-8'))
    reg = json.loads(registry.read_text(encoding='utf-8'))
    ids = [r['gg_id'] for r in rows['entries']]
    if len(set(ids)) != len(ids) or not set(reg['bindings']) <= set(ids):
        raise ValueError('Invalid input identities')
    # Independent oracle: index declared names, not compiler matching logic.
    names = {}
    for row in rows['entries']:
        ident = row['gg_id']
        for name in [row['word'], *row.get('aliases', []), *reg['bindings'].get(ident, {}).get('aliases', [])]:
            key = ' '.join(name.lower().split())
            names.setdefault(key, set()).add(ident)
    report['entries'] = len(ids)
    report['unique_phrases'] = len(names)
    report['bindings'] = len(reg['bindings'])
    report['ambiguities'] = {k: sorted(v) for k, v in names.items() if len(v) > 1}
    report['stages']['index'] = 'PASS'
    save()
    counts = {'pass': 0, 'fail': 0, 'expected_resolution': 0, 'expected_refusal': 0}
    for key in sorted(names):
        for phrase in (key, '  ' + '   '.join(key.upper().split()) + '  '):
            for sense in [None, *ids]:
                eligible = names[key] if sense is None else names[key] & {sense}
                if len(eligible) == 1:
                    expected = next(iter(eligible))
                    counts['expected_resolution'] += 1
                else:
                    expected = 'AMBIGUOUS_COMMAND' if eligible else 'UNKNOWN_COMMAND'
                    counts['expected_refusal'] += 1
                try:
                    actual = mod.resolve(phrase, rows, reg, sense)['command_id']
                except mod.Refusal as exc:
                    actual = str(exc)
                if expected == actual:
                    counts['pass'] += 1
                else:
                    counts['fail'] += 1
                    report['failures'].append({'phrase': phrase, 'sense': sense, 'expected': expected, 'actual': actual})
        report['stages']['matrix'] = dict(counts, last_phrase=key)
        save()
    report['status'] = 'PASS' if counts['fail'] == 0 else 'FAIL'
    save()
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('root', type=Path)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--projection', action='store_true')
    args = p.parse_args()
    result = audit(args.root, args.out, args.projection)
    print(json.dumps({k: v for k, v in result.items() if k != 'failures'}, indent=2))
    raise SystemExit(result['status'] != 'PASS')
