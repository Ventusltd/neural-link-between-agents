import sys, io, re, json
sys.path.insert(0, '../globalgrid2050/scripts')
import pandas as pd
import repd_sources_v6 as q2
from datetime import datetime
print("== 1 norm_date edge cases")
for v in ["07/03/2026","2026-03-07","03/25/2026","31/02/2026","7 March 2026","07/03/26","n/a","", pd.Timestamp("2026-07-03"), 46000]:
    print("  %r -> %r" % (v, q2.norm_date(v)))
print("  unparseable pair equal?", q2.norm_date("7 March 2026")==q2.norm_date("9 May 2025"), "| unparseable vs blank equal?", q2.norm_date("07/03/26")==q2.norm_date(""))
print("== 2 Excel round trip")
buf=io.BytesIO()
df=pd.DataFrame({"Ref ID":[1,2,3],"Site Name":["a","b","c"],"Technology Type":["x"]*3,"Installed Capacity (MWelec)":[1.005,2,3],
  "Planning Application Submitted":[pd.Timestamp("2026-07-03"),"07/03/2026","03/25/2026"]})
df.to_excel(buf,index=False); fr,_=q2.read_xlsx(buf.getvalue())
for r,v in zip(fr["Ref ID"],fr["Planning Application Submitted"]): print("  ref",r,type(v).__name__,repr(v),"->",q2.norm_date(v))
print("  csv '07/03/2026' ->",q2.norm_date("07/03/2026"),"vs true-date cell 3 Jul 2026 ->",q2.norm_date(pd.Timestamp("2026-07-03")),"(day/month swap shows as a conflict)")
print("== 3 historical repd.csv through the same reader")
raw=open('../globalgrid2050/repd.csv','rb').read()
f=q2.read_csv(raw); print("  rows",len(f),"cols",len(f.columns),"unique refs",f["Ref ID"].map(q2.clean_ref).nunique(), "ends with newline",raw.endswith(b"\n"))
print("  last row ref",f["Ref ID"].iloc[-1],"| non-empty cells in last row",int((f.iloc[-1]!="").sum()))
lead=0; ex=[]
for c in f.columns:
    m=f[c].astype(str).str.match(r'^[=+\-@\t\r]')
    # ignore plain negative/positive numbers
    m&=~f[c].astype(str).str.match(r'^[+\-]?\d+(\.\d+)?$')
    if m.any():
        lead+=int(m.sum()); ex.append((c,int(m.sum()),f.loc[m,c].iloc[0][:40]))
print("  cells starting with = + - @ (formula risk if opened in Excel):",lead); [print("    ",e) for e in ex[:8]]
nl=sum(int(f[c].astype(str).str.contains(r'[\r\n]').sum()) for c in f.columns); print("  cells containing line breaks (collapse() flattens these in the canonical):",nl)
bad={}
for c in q2.OFFICIAL_DATE_FIELDS:
    if c in f.columns:
        s=f[c].astype(str); nb=s[(s.str.strip()!="")]; u=nb[nb.map(q2.norm_date)==""]
        us=nb[nb.map(lambda t: bool(re.fullmatch(r'\d{1,2}/\d{1,2}/\d{4}',t.strip())) and int(t.split('/')[1])>12)]
        if len(u) or len(us): bad[c]=(len(u),list(u[:3]),len(us))
print("  date fields with non-blank values norm_date turns into '' (count, examples, mm/dd-only count):",bad or "none")
print("== 4 truncation guard: cut the file at a row boundary")
lines=raw.split(b"\n"); cut=b"\n".join(lines[:12600])+b"\n"
try:
    g=q2.read_csv(cut); print("  truncated copy parses cleanly:",len(g),"rows; passes the >=12,000 floor:",len(g)>=12000,"; below last validated 14,657:",len(g)<14657)
except Exception as e: print("  truncated copy rejected:",str(e)[:120])
