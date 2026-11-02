import subprocess,sys,re,hashlib
sys.path.insert(0,'tools')
from check_proof import leaks
def g(*a): return subprocess.run(['git',*a],capture_output=True).stdout
commits=g('rev-list','--reverse','96736f5..origin/edition/202611012135').decode().split()
state={}
for c in commits:
    t=g('log','-1','--format=%ad','--date=format:%H:%M:%S',c).decode().strip()
    for line in g('diff-tree','-r','--no-commit-id','--name-status',c).decode().splitlines():
        st,*p=line.split('\t'); path=p[-1]
        if st.startswith('D'):
            if state.get(path): print(t,c[:7],'REMOVED',path); state[path]=False
            continue
        b=g('show',f'{c}:{path}')
        n=leaks(b.decode('utf-8','replace'))
        if n and not state.get(path): print(t,c[:7],'K1 IN',path,n)
        if not n and state.get(path): print(t,c[:7],'K1 CLEARED',path)
        state[path]=bool(n)
