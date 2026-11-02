#!/usr/bin/env python3
"""Existence check of every fully-qualified key `repo@sha path:line[-line]` in a STEPS file (no fragment column):
HEAD must start with sha, file must exist, last line of the range must exist. Also checks `team-N/STEPS.md:line`
and `neural-link path:line` keys against this repository's working tree."""
import re, subprocess, sys
ESTATE='/home/user/estate'; NL='/home/user/neural-link-between-agents'
txt=open(sys.argv[1],encoding='utf-8').read()
heads={}
def head(r):
    if r not in heads:
        try: heads[r]=subprocess.check_output(['git','-C',f'{ESTATE}/{r}','rev-parse','HEAD'],text=True).strip()
        except Exception: heads[r]=''
    return heads[r]
def nlines(p):
    try: return len(open(p,'rb').read().split(b'\n'))
    except Exception: return -1
bad=0; n=0
for m in re.finditer(r'([\w-]+)@([0-9a-f]{7,40}) ([\w./-]+?):(\d+)(?:-(\d+))?', txt):
    r,s,p,a,b=m.groups(); b=int(b or a); n+=1
    why=[]
    if not head(r).startswith(s): why.append(f'HEAD {head(r)[:12]}')
    L=nlines(f'{ESTATE}/{r}/{p}')
    if L<0: why.append('no file')
    elif b>L: why.append(f'only {L} lines')
    if why: bad+=1; print('FAIL',m.group(0),';'.join(why))
for m in re.finditer(r'(?:neural-link|team-5/|team-3/|team-1/|team-4/)\s?([\w./-]+?):(\d+)(?:-(\d+))?', txt):
    p,a,b=m.groups(); b=int(b or a); n+=1
    full = p if p.startswith('FIXES') or p.startswith('SESSIONS') else ('FIXES/NL-010/'+m.group(0).split()[0].rstrip('/') + '/' + p if m.group(0).startswith('team-') else p)
    if m.group(0).startswith('team-'): full='FIXES/NL-010/'+m.group(0).split(':')[0]
    L=nlines(f'{NL}/{full}')
    if L<0 or b>L: bad+=1; print('FAIL',m.group(0),'->',full,f'lines={L}')
print(f'RESULT: {"PASS" if not bad else "FAIL"} ({n} keys, {bad} failed)')
