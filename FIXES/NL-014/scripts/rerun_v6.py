"""Re-run the historical V6 chain on local July bytes inside a scratch tree.
usage: rerun_v6.py TREE CSV XLSX VALIDATED_AT
Patches only: repd_sources_v6.fetch_bytes (local files by URL) and utc_now (frozen timestamp)."""
import os, runpy, sys
tree, csvp, xlsxp, ts = sys.argv[1:5]
os.environ.pop('REPD_RELEASE_DESCRIPTOR', None)
os.environ['REPD_VALIDATED_AT'] = ts
os.environ['REPD_SOURCE_CSV_FILE'] = os.path.abspath(csvp); os.environ['REPD_SOURCE_XLSX_FILE'] = os.path.abspath(xlsxp)
sys.path.insert(0, os.path.join(tree, 'scripts'))
import repd_sources_v6 as r
files = {r.CSV_URL: open(csvp, 'rb').read(), r.XLSX_URL: open(xlsxp, 'rb').read()}
r.fetch_bytes = lambda url, *a, **k: files[url]
r.utc_now = lambda: ts
os.chdir(tree)
for s in ['validate_repd_sources_v6.py', 'validate_v6_manifest_provenance.py', 'build_project_identity_v6.py', 'validate_project_identity_v6.py']:
    print('==', s, flush=True)
    sys.argv = [s]
    try:
        runpy.run_path(os.path.join(tree, 'scripts', s), run_name='__main__')
    except SystemExit as e:
        print('exit', e.code)
