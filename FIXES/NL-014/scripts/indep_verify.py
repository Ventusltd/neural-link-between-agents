"""Independent structure check of a raw REPD CSV + XLSX (no automation/repd code)."""
import csv, hashlib, io, json, sys, collections, datetime
import openpyxl
csvp, xlsxp, outp = sys.argv[1:4]
res = {}
raw = open(csvp, 'rb').read()
res['csv_bytes'] = len(raw); res['csv_sha256'] = hashlib.sha256(raw).hexdigest()
try: raw.decode('utf-8'); enc = 'utf-8'
except UnicodeDecodeError: enc = 'cp1252'
res['csv_encoding'] = enc
rows = list(csv.reader(io.StringIO(raw.decode(enc), newline='')))
hdr, body = rows[0], rows[1:]
res['csv_header'] = hdr; res['csv_columns'] = len(hdr); res['csv_records'] = len(body)
res['csv_field_counts'] = dict(collections.Counter(len(r) for r in body))
refs = [r[1].strip() for r in body]
res['csv_unique_refs'] = len(set(refs))
res['csv_dup_refs'] = sorted(k for k, v in collections.Counter(refs).items() if v > 1)
res['csv_blank_cells_total'] = sum(1 for r in body for c in r if c.strip() == '')
res['csv_NA_cells'] = {hdr[i]: n for i, n in collections.Counter(i for r in body for i, c in enumerate(r) if c.strip() == 'NA').items()}
# month-first / non dd/mm/yyyy date strings
datecols = [2] + list(range(37, 51))
odd = collections.defaultdict(list)
for r in body:
    for i in datecols:
        v = r[i].strip()
        if not v: continue
        try:
            d = datetime.datetime.strptime(v, '%d/%m/%Y')
            if len(v) != 10: odd[hdr[i]].append((r[1], v))
        except ValueError:
            odd[hdr[i]].append((r[1], v))
res['csv_nonconforming_dates'] = {k: v for k, v in odd.items()}
wb = openpyxl.load_workbook(xlsxp, read_only=True, data_only=True)
res['xlsx_sheets'] = wb.sheetnames
ws = wb['REPD']
xr = list(ws.iter_rows(values_only=True))
xh = [str(c) if c is not None else '' for c in xr[0]]
xb = [r for r in xr[1:] if any(c not in (None, '') for c in r)]
res['xlsx_header_equals_csv_header'] = xh == hdr
res['xlsx_records'] = len(xb)
xrefs = [str(int(r[1])) if isinstance(r[1], (int, float)) else str(r[1]).strip() for r in xb]
res['xlsx_unique_refs'] = len(set(xrefs))
res['ref_sets_equal'] = set(xrefs) == set(refs)
res['same_order'] = xrefs == refs
raw2 = open(xlsxp, 'rb').read()
res['xlsx_bytes'] = len(raw2); res['xlsx_sha256'] = hashlib.sha256(raw2).hexdigest()
json.dump(res, open(outp, 'w'), indent=1, default=str)
print(json.dumps({k: v for k, v in res.items() if k not in ('csv_header',)}, default=str, indent=1))
