import importlib.util, json, sys, hashlib
from pathlib import Path
mod_path, identity, xlsx, out, existing = sys.argv[1:6]
spec = importlib.util.spec_from_file_location('spine', mod_path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ident = json.load(open(identity))['records']
p = m.build_coordinate_fixture(Path(xlsx), ident, Path(out))
e = json.load(open(existing))
print('rebuilt meta', {k: v for k, v in p.items() if k != 'records'})
print('existing meta', {k: v for k, v in e.items() if k != 'records'})
print('records equal:', p['records'] == e['records'])
diff = [(a, b) for a, b in zip(p['records'], e['records']) if a != b]
print('differing records', len(diff), diff[:5])
pe = dict(p); pe['source_workbook'] = e['source_workbook']; pe['source_workbook_sha256'] = e['source_workbook_sha256']
print('payload equal apart from workbook name/hash:', pe == e)
