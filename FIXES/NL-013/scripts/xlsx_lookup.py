import sys, openpyxl
wb=openpyxl.load_workbook(sys.argv[1],read_only=True,data_only=True); ws=wb['REPD']
it=ws.iter_rows(values_only=True); h=[str(x).strip() if x else x for x in next(it)]
want=set(sys.argv[3:]); cols=sys.argv[2].split('|')
ri=h.index('Ref ID')
for r in it:
    if r[ri] is not None and str(int(r[ri]) if isinstance(r[ri],(int,float)) else r[ri]) in want:
        print(r[ri], {c: r[i] for i,c in enumerate(h) if c and any(c.startswith(k) for k in cols)})
