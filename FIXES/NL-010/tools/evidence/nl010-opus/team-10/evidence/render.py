#!/usr/bin/env python3
"""Render the live sections of handoff/10-integration/EVIDENCE.md from the template. Read-only on every other file."""
import hashlib, json, os, re, glob, datetime, subprocess
ED = '/home/user/estate/kuiper-belt/editions/202611012135'
HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = ('keyPlace address describe findBy flyTo home homeCamera safeBox lightTime showNew goKey fmt words esc cv ov o2 '
         'hud big sub card gbox gin SPACE N repos commits wafer').split()
EXTRA = 'cam lit sel redraw draw panels'.split()
KEYRE = re.compile(r'[A-Za-z0-9_.-]+@[0-9a-f]{7,40}\b[^\n`|]*?[\w./-]+:\d+')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
def reg_requires(src):
    m = re.search(r'register\(\{.*?requires:\s*(\[[^\]]*\]|[A-Z_]+)', src, re.S)
    if not m: return None
    v = m.group(1)
    if not v.startswith('['):
        m2 = re.search(re.escape(v) + r'\s*=\s*(\[[^\]]*\])', src, re.S)
        if not m2: return None
        v = m2.group(1)
    return re.findall(r"['\"]([^'\"]+)['\"]", v)
def header_requires(src, known):
    head = src[:src.find('*/') + 2] if src.startswith('/*') and 0 < src.find('*/') < 6000 else ''
    blob = head + '\n' + '\n'.join(l for l in src.splitlines()[:8] if l.lstrip().startswith('//'))
    m = re.search(r'requires(?: \(C8\))?:\s*(.*?)(?:\n\s*(?:\*\s*)?(?:optional|provides|Public|[A-Z]{2,})|·\s*provides|provides:|\.\s+provides|\*/)', blob, re.S)
    if not m: return None
    return [t for t in dict.fromkeys(re.findall(r'(?<![#\w-])[A-Za-z][A-Za-z0-9-]*', m.group(1))) if t in HOOKS + EXTRA or t in known]
def handoff_dir(team):
    hd = sorted(d for d in os.listdir(os.path.join(ED, 'handoff')) if d.startswith(str(team).zfill(2) + '-'))
    return hd[0] if hd else None
def evidence_keys(hd):
    p = os.path.join(ED, 'handoff', hd, 'EVIDENCE.md') if hd else ''
    if not (p and os.path.exists(p)): return None
    t = open(p, encoding='utf-8').read()
    return (len(KEYRE.findall(t)), len(re.findall(r'(?<![\w@])[\w./-]*[A-Za-z][\w./-]*:\d+(?:-\d+)?\b', t)))
def test_verdict(hd):
    p = os.path.join(ED, 'handoff', hd, 'TEST.md') if hd else ''
    if not (p and os.path.exists(p)): return 'no TEST.md'
    t = open(p, encoding='utf-8').read()
    m = re.search(r'(?im)^\**(?:verdict|status|result)\**\s*:?\s*\**\s*(.{0,90})', t)
    return (m.group(1).strip() if m else 'no verdict line').replace('|', '/')
mp = os.environ.get('MANIFEST') or os.path.join(ED, 'modules.json')
man = json.load(open(mp))
known = set(); out = []
out.append(f'Read {now}: `modules.json` sha256 `{sha(mp)}`, `order` = `{json.dumps(man.get("order"))}`.\n')
recs = {m.get('id'): m for m in man.get('modules', [])}
if not man.get('order'):
    out.append('No module is admitted yet (`order` is empty). The candidates on disk are checked in 2b below.\n')
earlier = set()
for i, oid in enumerate(man.get('order', []), 1):
    m = recs.get(oid)
    if not m:
        out.append(f'### {i}. `{oid}`: IN ORDER BUT NOT IN `modules` (the loader refuses it: `in order but not in modules`)\n'); continue
    p = os.path.join(ED, m['path']); exists = os.path.exists(p)
    act = sha(p) if exists else 'MISSING'; nb = os.path.getsize(p) if exists else -1
    src = open(p, encoding='utf-8').read() if exists else ''
    l1 = src.splitlines()[0] if src else ''
    hm = re.match(r'/\* kuiper module (\S+), generation (\d{12}) \(UTC\), (.*?)(?:\s*\*/)?$', l1)
    fs = re.match(r'(\d{12})-', os.path.basename(m['path']))
    rg = re.search(r'register\(\{.*?generation:\s*([\'"]?[\w]+)', src, re.S)
    rgen = rg.group(1).strip('\'"') if rg else None
    if rgen and not rgen.isdigit():
        mm = re.search(re.escape(rgen) + r"\s*=\s*['\"](\d{12})", src); rgen = mm.group(1) if mm else rgen
    adm = set(HOOKS) | set(EXTRA) | earlier
    req = m.get('requires', []); bad = [r for r in req if r not in adm]
    rr = reg_requires(src); hr = header_requires(src, earlier)
    hd = handoff_dir(m.get('team', '')); ek = evidence_keys(hd)
    ms = os.path.join(ED, 'handoff', hd, 'MODULE.sha256') if hd else ''
    msv = open(ms).read().split()[0] if ms and os.path.exists(ms) and open(ms).read().split() else None
    stamps = [fs and fs.group(1), hm and hm.group(2), m.get('generation'), rgen]
    ok = lambda b: 'PASS' if b else '**FAIL**'
    out.append(f'### {i}. `{oid}` — `{m["path"]}` (team {m.get("team")}, step {m.get("step")})\n')
    out.append('| check | recorded | measured | result |\n|---|---|---|---|')
    out.append(f'| sha256 | `{m["sha256"]}` (modules.json) | `{act}` (sha256sum) | {ok(act == m["sha256"])} |')
    out.append(f'| sha256 in handoff MODULE.sha256 | `{msv}` | `{act}` | {ok(msv == act) if msv else "no MODULE.sha256"} |')
    out.append(f'| bytes / budget | {m.get("bytes")} / {m.get("byte_budget")} | {nb} | {ok(nb == m.get("bytes") and nb <= (m.get("byte_budget") or 0))} |')
    out.append(f'| header licence line (line 1) | record `licence`: {m.get("licence")} | `{(hm.group(3) if hm else l1)}` | {ok(bool(hm) and bool(m.get("licence")) and m.get("licence").split()[0].rstrip(",") in hm.group(3))} |')
    out.append(f'| header id | `{oid}` | `{hm and hm.group(1)}` | {ok(bool(hm) and hm.group(1) == oid)} |')
    out.append(f'| stamp: file / header / record / registration | | {" / ".join(str(s) for s in stamps)} | {ok(len(set(stamps)) == 1 and None not in stamps)} |')
    out.append(f'| requires (record) against HOOKS.md (28 hooks + 6 + earlier provides) | `{" ".join(req)}` | not admissible: {", ".join(bad) if bad else "none"} | {ok(not bad)} |')
    out.append(f'| requires: registration = record | | `{" ".join(rr) if rr is not None else "not found"}` | {ok(rr is not None and set(rr) == set(req))} |')
    out.append(f'| requires: header = record | | `{" ".join(hr) if hr is not None else "not found"}` | {ok(hr is not None and set(hr) == set(req))} |')
    out.append(f'| provides | `{" ".join(m.get("provides", []))}` | id in provides: {oid in m.get("provides", [])} | {ok(oid in m.get("provides", []))} |')
    out.append(f'| team EVIDENCE.md with keys | `handoff/{hd}/EVIDENCE.md` | {"absent" if ek is None else str(ek[0]) + " full keys `repo@sha path:line`; " + str(ek[1]) + " `path:line` references in all (short forms resolve against the file's heads table)"} | {ok(bool(ek) and ek[1] > 0)} |')
    tp = os.path.join(ED, 'handoff', hd, 'TEST.md') if hd else ''
    tt = open(tp, encoding='utf-8').read() if tp and os.path.exists(tp) else ''
    named = [x[:12] for x in set(re.findall(r'\b[0-9a-f]{64}\b', tt))]
    out.append(f'| team TEST.md verdict | | {test_verdict(hd)} | |')
    out.append(f'| TEST.md ran on the admitted bytes (admitted sha256 written in TEST.md) | `{act[:12]}` | {"named" if act in tt else "**not named**"}; 64-hex values in TEST.md: {", ".join("`"+x+"`" for x in sorted(named)[:6]) or "none"} | {"PASS" if act in tt else "**CHECK**"} |')
    out.append(f'| team HANDOFF.md | | {"present" if hd and os.path.exists(os.path.join(ED, "handoff", hd, "HANDOFF.md")) else "absent"} | |\n')
    earlier |= set(m.get('provides', [])) | {oid}
# references (the loader): sha256 and the marker block equal to index.html's (E6)
B = 'KUIPER HOOK TABLE AND LOADER kuiper.hooks.v1'
def block(p):
    L = open(p, encoding='utf-8').read().split('\n'); i = [n for n, l in enumerate(L) if B in l]
    return ('\n'.join(L[i[0]:i[-1] + 1]), i[0] + 1, i[-1] + 1) if len(i) >= 2 else (None, None, None)
for r in man.get('references', []):
    p = os.path.join(ED, r['file']); a = sha(p) if os.path.exists(p) else 'MISSING'
    bi, i0, i1 = block(os.path.join(ED, 'index.html')); bl, j0, j1 = block(p) if os.path.exists(p) else (None, None, None)
    out.append(f'### reference `{r["file"]}` (team {r.get("team")}, never fetched)\n')
    out.append('| check | recorded | measured | result |\n|---|---|---|---|')
    out.append(f'| sha256 | `{r.get("sha256")}` | `{a}` | {"PASS" if a == r.get("sha256") else "**FAIL**"} |')
    out.append(f'| marker block byte-identical to index.html | index.html :{i0}-{i1} | reference :{j0}-{j1}; sha256 of block `{hashlib.sha256(bi.encode()).hexdigest()[:12] if bi else None}` / `{hashlib.sha256(bl.encode()).hexdigest()[:12] if bl else None}` | {"PASS" if bi and bi == bl else "**FAIL** (or not yet patched in)"} |')
    out.append(f'| header line 1 | | `{open(p).readline().strip()}` | |\n')
# 2b: candidates on disk
cand = ['\n| file | sha256 (sha256sum) | bytes | line 1 (licence) | registration requires | handoff MODULE.sha256 | team TEST.md |', '|---|---|---|---|---|---|---|']
for p in sorted(glob.glob(os.path.join(ED, 'modules', '*.js'))):
    s = open(p, encoding='utf-8').read(); l1 = s.splitlines()[0].replace('|', '/')
    hid = re.match(r'/\* kuiper (?:module (\S+),|loader reference)', l1)
    mid = hid.group(1) if hid and hid.group(1) else None
    team = None
    for d in os.listdir(os.path.join(ED, 'handoff')):
        for f in ('MODULE.json',):
            fp = os.path.join(ED, 'handoff', d, f)
            if mid and os.path.exists(fp):
                try:
                    if json.load(open(fp)).get('id') == mid: team = d
                except Exception: pass
    if not team:
        team = {'hello': '04-loader', 'kuiper-shell': '01-shell', 'line-card': '02-card', 'layers': '03-layers',
                'see-through': '05-see-through', 'file': '06-file', 'apps': '07-apps', 'drift': '08-drift'}.get(mid or '', '04-loader' if 'loader' in p else None)
    ms = os.path.join(ED, 'handoff', team, 'MODULE.sha256') if team else ''
    msv = '—'
    if ms and os.path.exists(ms):
        a = sha(p); msv = 'lists it, equal' if a in open(ms).read() else 'present, **this sha256 not in it**'
    rr = reg_requires(s)
    cand.append(f'| `{os.path.basename(p)}` | `{sha(p)}` | {os.path.getsize(p)} | `{l1[:110]}` | {len(rr) if rr else "—"} names | {msv} | {test_verdict(team)[:60] if team else "—"} |')
open(os.path.join(HERE, 'live-modules.md'), 'w').write('\n'.join(out))
open(os.path.join(HERE, 'live-candidates.md'), 'w').write('\n'.join(cand) + '\n')
print('\n'.join(out)); print('\n'.join(cand))
