#!/usr/bin/env python3
"""Build FIXES/NL-011/KUIPER-MAP.md: the neural link keyed the way the Kuiper keys lines.

One row per key. A file key is `nl@<commit> <path>:<line>`: the commit is the one that wrote the line (git blame),
the line number is the line's number in that commit's version of the file, and the text is re-read from that commit
with `git show` and compared to the working tree before the row is written (a row whose text differs is marked).
A comment key is `#<issue>/c<id>` (GitHub issue comment id); its time is GitHub's created_at.

Usage (from the repository root):
    python3 FIXES/NL-011/build_kuiper_map.py --comments-dir <dir with c9.json c10-*.json c11.json> [--out FIXES/NL-011/KUIPER-MAP.md]
Without --comments-dir the comments are fetched with `gh api` (REST, paged by &page=N).

Written by FABLE-FIN-3, 2 Nov 2026. Types: RULE, RULING, DECISION, HANDOFF, REVISION, REVIEW, FINDING, and the
envelope's own REQUEST, ACK, BLOCKER where a comment carries them (DECISION-PROPOSAL is written DECISION).
"""
import argparse, glob, json, os, re, subprocess, sys, datetime, collections

REPO = 'Ventusltd/neural-link-between-agents'
ISSUES = (9, 10, 11)

def sh(*cmd, text=True):
    return subprocess.run(cmd, check=True, capture_output=True, text=text).stdout

def utc(ts):
    return datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ')

# ---------------------------------------------------------------------------------------------------------------
# 1. File rows: which lines of which files are keys, and how they are typed.
#    (path, selector, type, who, note). selector: list of line numbers, or a regex matched against the line text,
#    or ('range', a, b). type may be a callable(line_text) -> type.
# ---------------------------------------------------------------------------------------------------------------
def overnight_type(t):
    s = t.lower()
    if 'correction' in s: return 'REVISION'
    if 'rule from now' in s or 'ruling' in s or 'rulings' in s: return 'RULING'
    if re.search(r'shipped|published|merged|done\.|merge|moved to', s): return 'HANDOFF'
    return 'FINDING'

def overnight_who(t):
    if 'Watcher A' in t: return 'WATCHER-A (Fable)'
    if t.startswith('- 2026-11-01 23:3') or t.startswith('- 2026-11-01 23:5') or t.startswith('- 2026-11-02 00:05 UTC · (Watcher A') or t.startswith('- 2026-11-02 00:07 UTC · Watcher A'):
        return 'WATCHER-A (Fable)'
    return 'HARNESS'

def decisions_row(t):
    # | D001 | time | who | authority | what | key | link | status |
    cells = [c.strip() for c in t.strip().strip('|').split('|')]
    if len(cells) < 8: return None
    what = cells[4]
    w = what.lower()
    typ = 'DECISION'
    if w.startswith('ruling') or 'ruling:' in w[:40]: typ = 'RULING'
    elif w.startswith('refuses') or w.startswith('"verdict: fail') or w.startswith('fail:'): typ = 'REVIEW'
    elif w.startswith('hands off') or w.startswith('handoff'): typ = 'HANDOFF'
    elif w.startswith('revision'): typ = 'REVISION'
    elif w.startswith('admits'): typ = 'REVIEW'
    elif w.startswith('discloses') or w.startswith('finding'): typ = 'FINDING'
    status = cells[7]
    sup = ''
    m = re.search(r'(superseded by|resolved by|overrides|supersedes|replaces) (D\d+[a-z]?(?:[,/ ]+D\d+[a-z]?)*)', status + ' ' + what, re.I)
    if m: sup = m.group(0)
    return dict(id=cells[0], when=cells[1], who=cells[2], typ=typ, summary=what[:160], superseded=sup)

FILE_SPECS = [
    ('LINK-RULE.md', re.compile(r'^\d\. '), 'RULE', 'OWNER (relayed by HARNESS)', 'the link is the medium of exchange'),
    ('LINK-RULE.md', [1], 'RULE', 'OWNER (relayed by HARNESS)', 'title and date of the rule'),
    ('PROTOCOL.md', [5, 7, 15, 16, 20, 25, 30, 31, 33, 37, 41, 45, 47], 'RULE', 'Agent F (protocol v1 author)', 'protocol v1'),
    ('AGENTS.md', re.compile(r'^(\d\. |- )'), 'RULE', 'Agent F (protocol v1 author)', 'mailbox rules'),
    ('SESSIONS/202611012145-kuiper-edition-harness-notes.md', ('range', 39, 66, re.compile(r'^- ')), 'RULE', 'HARNESS', 'rules that bind every edition'),
    ('FIXES/NL-010/BRIEF.md', [5, 72], 'DECISION', 'OWNER (quoted by HARNESS)', "owner's words: the roadmap brief and Addendum 1"),
    ('FIXES/NL-010/OVERNIGHT.md', [3], 'DECISION', 'OWNER (quoted by HARNESS)', "owner's ACCEPT and overnight instruction"),
    ('FIXES/NL-010/OVERNIGHT.md', ('range', 13, 22, re.compile(r'^- R')), 'DECISION', 'HARNESS', 'the small steps R0-R4'),
    ('FIXES/NL-010/OVERNIGHT.md', ('range', 36, 400, re.compile(r'^- ')), overnight_type, overnight_who, 'overnight log entry'),
    ('FIXES/NL-010/ROADMAP.md', ('range', 27, 39, re.compile(r'^\d\. ')), 'RULE', 'FABLE-T5B (consolidator)', 'the law the roadmap is written under'),
    ('FIXES/NL-010/ROADMAP.md', re.compile(r'^### Step \d+\.'), 'DECISION', 'FABLE-T5B (consolidator)', 'a roadmap step'),
    ('FIXES/NL-010/ROADMAP.md', re.compile(r'^- \*\*Q\d '), 'DECISION', 'FABLE-T5B (consolidator) to OWNER', 'open question for the owner (OPEN)'),
    ('FIXES/NL-010/ROADMAP.md', re.compile(r'^## Phase 2'), 'DECISION', 'FABLE-T5B (consolidator)', 'Phase 2 gated on owner acceptance of steps 1-10'),
    ('FIXES/NL-010/OPUS-BRIEF.md', re.compile(r'ACCEPT|-F body=@file|may touch|REQUEST comment'), 'RULE', 'HARNESS', 'Opus team rule'),
    ('FIXES/NL-011/DECISIONS.md', re.compile(r'^\| D\d'), None, None, 'NL-011 decision log row (LINK-09)'),
    ('FIXES/NL-011/PROTOCOL-v2-proposal.md', re.compile(r'^\| \d+ \| \*\*'), 'DECISION', 'NL-011 STUDY-06 (proposal to OWNER, NOT ADOPTED)', 'protocol v2 hunk (OPEN)'),
    ('FIXES/NL-011/LEDGER.md', re.compile(r'^\| (Q\d|OW-)'), 'DECISION', 'OPUS LINK-08 (ledger) to OWNER', 'owner ask in the ledger'),
    ('FIXES/NL-011/SYNTHESIS.md', ('range', 11, 15, re.compile(r'^\d\. ')), 'FINDING', 'NL-011 STUDY-06', 'the synthesis answer, five sentences'),
]

def blame(path):
    """Return {final_line: (sha, orig_line, author, committer_time)}."""
    out = sh('git', 'blame', '--line-porcelain', '--', path)
    res = {}
    sha = orig = final = None; author = ''; ctime = 0
    for ln in out.splitlines():
        m = re.match(r'^([0-9a-f]{40}) (\d+) (\d+)(?: (\d+))?$', ln)
        if m:
            sha, orig, final = m.group(1), int(m.group(2)), int(m.group(3)); continue
        if ln.startswith('author '): author = ln[7:]
        elif ln.startswith('committer-time '): ctime = int(ln[15:])
        elif ln.startswith('\t'):
            res[final] = (sha, orig, author, ctime)
    return res

_show_cache = {}
def line_at(sha, path, n):
    key = (sha, path)
    if key not in _show_cache:
        _show_cache[key] = sh('git', 'show', f'{sha}:{path}').splitlines()
    lines = _show_cache[key]
    return lines[n - 1] if 0 < n <= len(lines) else None

def select_lines(lines, selector):
    if isinstance(selector, list): return [n for n in selector if n <= len(lines)]
    if isinstance(selector, tuple):
        _, a, b, rx = selector
        return [n for n in range(a, min(b, len(lines)) + 1) if rx.search(lines[n - 1])]
    return [n for n, t in enumerate(lines, 1) if selector.search(t)]

def file_rows():
    rows = []
    for path, selector, typ, who, note in FILE_SPECS:
        if not os.path.exists(path): continue
        lines = open(path, encoding='utf-8').read().split('\n')
        bl = blame(path)
        for n in select_lines(lines, selector):
            text = lines[n - 1]
            sha, orig, author, ctime = bl[n]
            at_commit = line_at(sha, path, orig)
            verified = (at_commit is not None and at_commit.rstrip() == text.rstrip())
            row_typ = typ(text) if callable(typ) else typ
            row_who = who(text) if callable(who) else who
            summary = re.sub(r'\s+', ' ', text.strip())[:170]
            sup = ''
            if path.endswith('DECISIONS.md'):
                d = decisions_row(text)
                if d is None: continue
                row_typ, row_who, summary, sup = d['typ'], d['who'], f"{d['id']} ({d['when']}): {d['summary']}", d['superseded']
            if 'CORRECTION of times' in text: sup = 'corrects the three log stamps above it (01:05Z, 01:12Z, 01:25Z)'
            if 'CORRECTION SHIPPED' in text: sup = 'supersedes the Edition 5 release a432b43 (OVERNIGHT.md R2 entry)'
            rows.append(dict(key=f'nl@{sha[:7]} {path}:{orig}', when=utc(ctime), who=row_who, typ=row_typ, note=note,
                             summary=summary, superseded=sup, verified=verified, cur_line=n, path=path, sha=sha[:7]))
    return rows

# ---------------------------------------------------------------------------------------------------------------
# 2. Comment rows.
# ---------------------------------------------------------------------------------------------------------------
# Curated supersession: new comment id -> (old comment id, why). Everything else is derived from TYPE/IN-REPLY-TO.
SUPERSEDES = {
    6567437030: (6566796733, 'delegation renewed and widened to See Through folders'),
    6567953002: (6567194090, 'Edition 5 manifest corrected: be99c8a1 restored in place of 4e6b4031'),
    6568373074: (6567953002, 'the pointer moved from Edition 5 to Edition 6'),
    6569312507: (6568373074, 'the pointer moved from Edition 6 to Edition 7'),
    6569860419: (6569312507, 'the pointer moved from Edition 7 to Edition 8'),
    6570717660: (6569860419, 'the pointer moved from Edition 8 to Edition 9'),
    6572568222: (6570717660, 'the pointer moved from Edition 9 to Edition 10'),
    6574744989: (6572568222, 'the pointer moved from Edition 10 to Edition 11'),
    6566485658: (6565195261, 'kuiper-shell rev 2 replaces rev 1 (refused 6565858587)'),
    6568299280: (6566485658, 'kuiper-shell rev 3 (2045c51a) replaces rev 2 (withdrawn 6567109868)'),
    6567112212: (6565667126, 'layers re-handed off with the four behaviours'),
    6568555984: (6567112212, 'layers revision 202611020304 (b16716bd)'),
    6571928537: (6568555984, 'layers revision 202611020637 (c8fccccf) after b16716bd was refused 6569024455'),
    6566504289: (6565879640, 'drift revision 49/49'),
    6568883224: (6566504289, 'drift revision 202611020240 (f03b7835) after the withdrawal 6567584787'),
    6573876435: (6568231803, 'File revision 202611020832 (5fc4e307) replaces 3ae05df7'),
    6567574981: (6565550370, 'line-card landscape revision 8ec117f9 replaces e2baeaaa'),
    6566812411: (6565556866, 'POINTER-READY redefined without layers; admission order 5, 8, 6, 7, 3, 9'),
    6566977283: (6566873489, 'D020 answered on the link: K1 blobs stay in branch history, main never carried them'),
    6568437190: (6568425579, 'whole-wafer HARNESS-LIMITED ruling; controller 2 takes over from controller 1'),
    6570675769: (6568425579, 'controller 2 hands over the queue; controller 1 handover superseded'),
    6568425579: (6566567995, 'controller 1 end-of-run handover replaces its running REVIEW state'),
}
ADMIT_WORDS = re.compile(r'\bADMITTED\b|\badmitted\b', re.I)
REFUSE_WORDS = re.compile(r'\bREFUSED\b|\bwithdrawn\b|\bwithdraws\b', re.I)

def load_comments(cdir):
    rows = []
    if cdir:
        files = sorted(glob.glob(os.path.join(cdir, 'c*.json')))
        for f in files:
            n = int(re.search(r'c(\d+)', os.path.basename(f)).group(1))
            for r in json.load(open(f)):
                r['_issue'] = n; rows.append(r)
    else:
        for n in ISSUES:
            page = 1
            while True:
                data = json.loads(sh('gh', 'api', f'repos/{REPO}/issues/{n}/comments?per_page=100&page={page}'))
                for r in data: r['_issue'] = n; rows.append(r)
                if len(data) < 100: break
                page += 1
    seen = set(); out = []
    for r in rows:
        if r['id'] in seen: continue
        seen.add(r['id']); out.append(r)
    return sorted(out, key=lambda r: (r['_issue'], r['created_at']))

def parse_comment(r):
    body = r['body'] or ''
    first = body.strip().splitlines()[0] if body.strip() else ''
    m = re.match(r'\s*\[([^\]]+?)\s*(?:→|->)\s*([^\]]*)\]\s*\[([^\]]*)\]\s*\[([^\]]*)\]', body)
    if m:
        frm, to, stamp = m.group(1).strip(), m.group(2).strip(), m.group(4).strip()
    else:
        m2 = re.match(r'\s*(\w[\w\-]*) · (\w+) · (\S+) ·', body)
        frm = (m2.group(2).upper() if m2 else 'unknown'); to = 'ALL'; stamp = (m2.group(3) if m2 else '')
    t = re.search(r'TYPE:\s*([A-Z][A-Z\-]+)', body)
    typ = t.group(1) if t else (re.match(r'\s*([A-Z]+) ·', body).group(1) if re.match(r'\s*([A-Z]+) ·', body) else '?')
    if typ == 'DECISION-PROPOSAL': typ = 'DECISION'
    irt = re.search(r'IN-REPLY-TO:\s*(\S+)', body)
    irt_id = None
    if irt:
        mm = re.search(r'issuecomment-(\d+)', irt.group(1))
        irt_id = int(mm.group(1)) if mm else None
    scope = re.search(r'SCOPE:\s*(.+)', body)
    status = re.search(r'STATUS:\s*(.+)', body)
    summary = (scope.group(1) if scope else first.split('·', 3)[-1] if '·' in first else first)
    summary = re.sub(r'\s+', ' ', summary.strip())[:150]
    corrected = 'time corrected' in first
    return dict(id=r['id'], issue=r['_issue'], when=r['created_at'].replace('T', ' ').replace('Z', 'Z'), who=frm, to=to,
                typ=typ, irt=irt_id, status=(status.group(1).strip()[:60] if status else ''), summary=summary,
                stamp=stamp, corrected=corrected, updated=r['updated_at'] != r['created_at'], body=body)

def comment_rows(raw):
    parsed = [parse_comment(r) for r in raw]
    by = {p['id']: p for p in parsed}
    for p in parsed:
        sup = ''
        if p['id'] in SUPERSEDES:
            old, why = SUPERSEDES[p['id']]
            sup = f'#{by[old]["issue"] if old in by else "?"}/c{old}: {why}'
        elif p['typ'] == 'REVISION' and p['irt'] in by:
            sup = f'#{by[p["irt"]]["issue"]}/c{p["irt"]}: revision of that hand-off'
        if p['corrected']:
            sup = (sup + '; ' if sup else '') + 'its own envelope time, corrected in place to GitHub\'s'
        p['superseded'] = sup
        rel = ''
        if p['typ'] == 'REVIEW' and p['irt'] in by:
            if REFUSE_WORDS.search(p['status']) or REFUSE_WORDS.search(p['body'][:600]): rel = 'refused'
            if ADMIT_WORDS.search(p['status']): rel = 'admitted'
        p['relation'] = rel
    return parsed

# ---------------------------------------------------------------------------------------------------------------
# 3. Write the map.
# ---------------------------------------------------------------------------------------------------------------
def model_of(label):
    u = label.upper()
    if u.startswith('FABLE') or u.startswith('WATCHER'): return 'Fable'
    if u.startswith('OPUS') or 'LINK-' in u: return 'Opus'
    if u.startswith('HARNESS'): return 'harness (Fable session)'
    if u.startswith('NL-011'): return 'Opus'
    return 'unstated'

def norm_label(label):
    s = re.sub(r'\s*\(.*?\)\s*', ' ', label).strip()
    s = re.sub(r'\s+(lead|builder|tester|evidence|architect|consolidator|integrator).*$', '', s, flags=re.I)
    s = re.sub(r'\s+(shell/evidence|layers|law-and-proof|bar|card|camera|touch|lines|seethrough|perf|type|robust|journey|index|persistence|decision log|resume kit|live reviewer|integration controller)$', '', s, flags=re.I)
    return s.strip() or label

def esc(s):
    return str(s).replace('|', '\\|')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--comments-dir')
    ap.add_argument('--out', default='FIXES/NL-011/KUIPER-MAP.md')
    a = ap.parse_args()
    head = sh('git', 'rev-parse', '--short', 'HEAD').strip()
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    frows = file_rows()
    crows = comment_rows(load_comments(a.comments_dir))
    unverified = [r for r in frows if not r['verified']]

    agents = collections.OrderedDict()
    for p in crows:
        k = norm_label(p['who'])
        a_ = agents.setdefault(k, dict(model=model_of(k), n=0, roles=set(), first=p['when'], last=p['when'], issues=set()))
        a_['n'] += 1; a_['last'] = max(a_['last'], p['when']); a_['first'] = min(a_['first'], p['when']); a_['issues'].add(p['issue'])
        role = re.search(r'\b(lead|builder|tester|evidence|architect|consolidator)\b', p['who'], re.I)
        if role: a_['roles'].add(role.group(1).lower())

    L = []
    L.append('# KUIPER-MAP: the neural link keyed the way the Kuiper keys lines')
    L.append('')
    L.append(f'Built by FIXES/NL-011/build_kuiper_map.py at {now} (clock read with `date -u`) on neural-link-between-agents '
             f'`{head}`. One row per key. A file key `nl@<commit> <path>:<line>` names the commit that wrote the line '
             f'(git blame) and the line number in that commit\'s version of the file; each line was re-read from that commit '
             f'with `git show` and compared with the working tree ({len(frows) - len(unverified)} of {len(frows)} equal; '
             f'a row marked `~` differs in whitespace only or has moved). A comment key `#<issue>/c<id>` is the GitHub issue '
             f'comment; its time is GitHub\'s `created_at`, never the self-written stamp. "Supersedes" names the key a row '
             f'replaced, from the envelope (REVISION, IN-REPLY-TO) or the builder\'s curated list, which is itself in the script.')
    L.append('')
    L.append('Types: RULE (binds agents), RULING (a harness or controller decision on a case), DECISION (a proposal, a plan or an '
             'owner question; DECISION-PROPOSAL envelopes are written DECISION), HANDOFF, REVISION, REVIEW, FINDING; the envelope\'s '
             'REQUEST, ACK and BLOCKER are kept where a comment carries them.')
    L.append('')
    L.append(f'Counts: {len(frows)} file keys, {len(crows)} comment keys (#9 {sum(1 for p in crows if p["issue"]==9)}, '
             f'#10 {sum(1 for p in crows if p["issue"]==10)}, #11 {sum(1 for p in crows if p["issue"]==11)}), {len(agents)} agent labels.')
    L.append('')
    # agents
    L.append('## A. Agents (every FROM label on #9, #10, #11, normalised to the agent; role words kept in the comment rows)')
    L.append('')
    L.append('| agent | model | comments | issues | first (UTC) | last (UTC) |')
    L.append('|---|---|---|---|---|---|')
    for k, v in sorted(agents.items(), key=lambda kv: (kv[1]['model'], kv[0])):
        L.append(f'| {esc(k)} | {v["model"]} | {v["n"]} | {", ".join("#"+str(i) for i in sorted(v["issues"]))} | {v["first"]} | {v["last"]} |')
    by_model = collections.Counter(v['model'] for v in agents.values())
    L.append('')
    L.append('Distinct labels by model: ' + ', '.join(f'{m} {n}' for m, n in sorted(by_model.items())) + '.')
    L.append('')
    # file rows
    L.append('## B. Rules, rulings and decisions written in this repository (keyed by the commit that wrote the line)')
    L.append('')
    L.append('| key | written (UTC, commit time) | who | type | supersedes | text (first 170 chars) |')
    L.append('|---|---|---|---|---|---|')
    for r in frows:
        mark = '' if r['verified'] else ' ~'
        L.append(f'| `{r["key"]}`{mark} | {r["when"]} | {esc(r["who"])} | {r["typ"]} | {esc(r["superseded"])} | {esc(r["summary"])} |')
    L.append('')
    # comments
    for n in ISSUES:
        L.append(f'## C{n}. Issue #{n} comments')
        L.append('')
        L.append('| key | created (UTC) | from | to | type | in reply to | supersedes | relation | scope / first line |')
        L.append('|---|---|---|---|---|---|---|---|---|')
        for p in crows:
            if p['issue'] != n: continue
            irt = f'c{p["irt"]}' if p['irt'] else ('NEW' if 'IN-REPLY-TO: NEW' in p['body'] else '')
            L.append(f'| `#{n}/c{p["id"]}` | {p["when"]} | {esc(p["who"])} | {esc(p["to"][:60])} | {p["typ"]} | {irt} | {esc(p["superseded"])} | {p["relation"]} | {esc(p["summary"])} |')
        L.append('')
    L.append('## Limits')
    L.append('')
    L.append('- A file key is only as fine as a line: a decision spread over several lines is keyed by its first line.')
    L.append('- The "supersedes" column is complete for the chains the builder lists (editions, delegation, module revisions, '
             'controller handovers) and for REVISION envelopes; other supersessions live in the DECISIONS.md rows\' status column.')
    L.append('- "relation" is read from a REVIEW\'s STATUS line and first 600 characters (admitted / refused); a REVIEW that '
             'both refuses one module and admits another is written by its STATUS word.')
    L.append('- Comment bodies are not copied; the row keeps the SCOPE line (or the first line) only, so the K1 check runs on less text.')
    L.append('')
    L.append('---')
    L.append('_Generated by [Claude Code](https://claude.ai/code)_')
    open(a.out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(f'wrote {a.out}: {len(frows)} file keys ({len(unverified)} unverified), {len(crows)} comment keys, {len(agents)} agents')

if __name__ == '__main__':
    main()
