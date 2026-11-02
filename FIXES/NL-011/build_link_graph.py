#!/usr/bin/env python3
"""Build FIXES/NL-011/link-graph.json from FIXES/NL-011/KUIPER-MAP.md, in the ventus-grid-engine genome graph format.

Format followed: ventus-grid-engine commit 96a800eb01825748936b5a193ce396a960f9302f, genome/engine-graph.json as written
by genome/build-graph.mjs: a JSON object {schema, label, generated_utc, note, focus_default, kind_labels, nodes,
node_ids, edges, edge_kind_counts}; nodes are {label, type, rag, reason, gh}; node_ids is the parallel list of stable
ids; edges are {from, to, type, evidence:{file, lines, method}} with from/to as indices into nodes. The spider
receiver (spider-sandbox.html, normaliseGenericGraph) reads exactly these fields: label, type, rag, reason, gh, and
edges by index or id, so this file can be listed in spider/manifest.json and drawn with no change to the page.

Nodes: the three issues, every agent label, every file key and every comment key of the map.
Edges: wrote (agent -> comment), on (comment -> issue), replied_to (comment -> the comment its IN-REPLY-TO names),
superseded (new -> old, from the map's supersedes column), admitted / refused (a controller REVIEW -> the hand-off it
judged), governs (a RULE -> the issues it binds).

Usage: python3 FIXES/NL-011/build_link_graph.py [--map FIXES/NL-011/KUIPER-MAP.md] [--out FIXES/NL-011/link-graph.json]
Written by FABLE-FIN-3, 2 Nov 2026.
"""
import argparse, collections, datetime, json, re

NL = 'https://github.com/Ventusltd/neural-link-between-agents'
KIND_LABELS = collections.OrderedDict([
    ('wrote', 'wrote'), ('on', 'posted on'), ('replied_to', 'replied to'), ('superseded', 'superseded'),
    ('admitted', 'admitted'), ('refused', 'refused'), ('governs', 'governs'),
])

def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

def unesc(s):
    return s.replace('\\|', '|')

def parse_map(path):
    text = open(path, encoding='utf-8').read().split('\n')
    section = None
    agents, files, comments = [], [], []
    for ln in text:
        if ln.startswith('## A.'): section = 'A'; continue
        if ln.startswith('## B.'): section = 'B'; continue
        m = re.match(r'## C(\d+)\.', ln)
        if m: section = 'C' + m.group(1); continue
        if ln.startswith('## Limits'): section = None; continue
        if not ln.startswith('| ') or ln.startswith('|---') or ln.startswith('| key') or ln.startswith('| agent'): continue
        c = [unesc(x) for x in cells(ln)]
        if section == 'A' and len(c) >= 6:
            agents.append(dict(label=c[0], model=c[1], n=int(c[2]), issues=c[3], first=c[4], last=c[5]))
        elif section == 'B' and len(c) >= 6:
            key = c[0].strip('`').replace('` ~', '').strip()
            m2 = re.match(r'nl@([0-9a-f]+) (\S+):(\d+)', key)
            if not m2: continue
            files.append(dict(key=key, sha=m2.group(1), path=m2.group(2), line=int(m2.group(3)), when=c[1], who=c[2], typ=c[3], superseded=c[4], text=c[5]))
        elif section and section.startswith('C') and len(c) >= 9:
            key = c[0].strip('`')
            m2 = re.match(r'#(\d+)/c(\d+)', key)
            if not m2: continue
            comments.append(dict(key=key, issue=int(m2.group(1)), id=int(m2.group(2)), when=c[1], frm=c[2], to=c[3], typ=c[4],
                                 irt=c[5], superseded=c[6], relation=c[7], summary=c[8]))
    return agents, files, comments

def norm_label(label):
    s = re.sub(r'\s*\(.*?\)\s*', ' ', label).strip()
    s = re.sub(r'\s+(lead|builder|tester|evidence|architect|consolidator|integrator).*$', '', s, flags=re.I)
    s = re.sub(r'\s+(shell/evidence|layers|law-and-proof|bar|card|camera|touch|lines|seethrough|perf|type|robust|journey|index|persistence|decision log|resume kit|live reviewer|integration controller)$', '', s, flags=re.I)
    return s.strip() or label

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--map', default='FIXES/NL-011/KUIPER-MAP.md')
    ap.add_argument('--out', default='FIXES/NL-011/link-graph.json')
    a = ap.parse_args()
    agents, files, comments = parse_map(a.map)

    nodes, node_ids, index = [], [], {}
    def add(nid, label, typ, rag, reason, gh):
        if nid in index: return index[nid]
        index[nid] = len(nodes); nodes.append(dict(label=label, type=typ, rag=rag, reason=reason, gh=gh)); node_ids.append(nid); return index[nid]

    titles = {9: 'NL-009: Kuiper Edition 5, mobile UI fixed by ten Fable agents, See Through as a button (Android)',
              10: 'NL-010: the ten-step roadmap, GridAtlas lessons into the Kuiper (OS of the estate), See Through the star player',
              11: 'NL-011: twelve Opus agents study and run the neural link; the link is the medium of exchange'}
    for n in (9, 10, 11):
        add(f'issue-{n}', f'issue #{n}', 'issue', 'green', titles[n], f'{NL}/issues/{n}')
    for ag in agents:
        add('agent:' + ag['label'], ag['label'], 'agent', 'green',
            f"{ag['model']}; {ag['n']} comment(s) on {ag['issues']}; first {ag['first']}, last {ag['last']}", None)

    comment_by_id = {c['id']: c for c in comments}
    superseded_ids = set()
    for c in comments:
        m = re.match(r'#\d+/c(\d+)', c['superseded'])
        if m: superseded_ids.add(int(m.group(1)))
    for c in comments:
        rag = 'green'
        if c['id'] in superseded_ids: rag = 'grey'
        elif c['relation'] == 'refused': rag = 'red'
        elif c['typ'] == 'DECISION' and 'OWNER' in c['to'].upper(): rag = 'amber'
        elif c['typ'] in ('REQUEST', 'BLOCKER'): rag = 'amber'
        add(c['key'], f"{c['typ']} {c['key']}", c['typ'].lower(), rag,
            f"{c['when']} · {c['frm']} → {c['to']} · {c['summary']}", f"{NL}/issues/{c['issue']}#issuecomment-{c['id']}")
    for f in files:
        rag = 'green'
        if f['typ'] == 'DECISION' and ('OPEN' in f['text'].upper()[:10] or 'to OWNER' in f['who'] or 'NOT ADOPTED' in f['who']): rag = 'amber'
        if re.search(r'superseded by', f['superseded'], re.I): rag = 'grey'
        if f['typ'] == 'REVIEW': rag = 'red' if re.search(r'refus|fail', f['text'], re.I) else 'green'
        add(f['key'], f"{f['typ']} {f['path']}:{f['line']}", f['typ'].lower(), rag,
            f"{f['when']} · {f['who']} · {f['text']}", f'{NL}/blob/{f["sha"]}/{f["path"]}#L{f["line"]}')

    edges = []
    def edge(src, dst, typ, file, lines, method):
        if src in index and dst in index:
            edges.append(dict(**{'from': index[src], 'to': index[dst]}, type=typ, evidence=dict(file=file, lines=lines, method=method)))
    for c in comments:
        edge('agent:' + norm_label(c['frm']), c['key'], 'wrote', 'FIXES/NL-011/KUIPER-MAP.md', c['key'], 'FROM label of the envelope, normalised to the agent')
        edge(c['key'], f"issue-{c['issue']}", 'on', 'FIXES/NL-011/KUIPER-MAP.md', c['key'], 'the issue the comment is on')
        m = re.match(r'c(\d+)', c['irt'])
        if m and int(m.group(1)) in comment_by_id:
            t = comment_by_id[int(m.group(1))]
            edge(c['key'], t['key'], 'replied_to', 'FIXES/NL-011/KUIPER-MAP.md', c['key'], 'IN-REPLY-TO field of the envelope')
            if c['relation'] in ('admitted', 'refused'):
                edge(c['key'], t['key'], c['relation'], 'FIXES/NL-011/KUIPER-MAP.md', c['key'], "REVIEW's STATUS line (admitted / refused)")
        m = re.match(r'#\d+/c(\d+)', c['superseded'])
        if m and int(m.group(1)) in comment_by_id:
            edge(c['key'], comment_by_id[int(m.group(1))]['key'], 'superseded', 'FIXES/NL-011/KUIPER-MAP.md', c['key'], c['superseded'])
    for f in files:
        if f['typ'] == 'RULE':
            targets = {'LINK-RULE.md': (10, 11), 'PROTOCOL.md': (9, 10, 11), 'AGENTS.md': (9, 10, 11),
                       'SESSIONS/202611012145-kuiper-edition-harness-notes.md': (9, 10), 'FIXES/NL-010/ROADMAP.md': (10,),
                       'FIXES/NL-010/OPUS-BRIEF.md': (10,)}.get(f['path'], ())
            for n in targets:
                edge(f['key'], f'issue-{n}', 'governs', 'FIXES/NL-011/KUIPER-MAP.md', f['key'], 'the rule binds the agents of that issue (LINK-RULE.md:1, BRIEF/OPUS-BRIEF channel lines)')
        m = re.search(r'(D\d+[a-z]?)', f['superseded'])
        if m and re.search(r'superseded by|resolved by', f['superseded'], re.I):
            # D-row to D-row: find the row whose text starts with that D id
            for g in files:
                if g['path'].endswith('DECISIONS.md') and g['text'].startswith(m.group(1) + ' '):
                    edge(g['key'], f['key'], 'superseded', 'FIXES/NL-011/KUIPER-MAP.md', f['key'], f"DECISIONS.md status column: {f['superseded']}")
                    break
    counts = collections.Counter(e['type'] for e in edges)
    graph = collections.OrderedDict([
        ('schema', 'neural-link.kuiper-map.v1'),
        ('label', 'neural link between agents · agents, issues, rules and hand-offs keyed as the Kuiper keys lines'),
        ('generated_utc', datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')),
        ('note', 'Same shape as ventus-grid-engine genome/engine-graph.json (ventus-grid-engine@96a800eb01825748936b5a193ce396a960f9302f, '
                 'written by genome/build-graph.mjs): nodes {label,type,rag,reason,gh}, node_ids parallel to nodes, edges {from,to,type,evidence} '
                 'by index, kind_labels and edge_kind_counts. Read by spider-sandbox.html normaliseGenericGraph() unchanged. Built from '
                 'FIXES/NL-011/KUIPER-MAP.md by FIXES/NL-011/build_link_graph.py. rag: green in force, grey superseded, amber open or asked, red refused.'),
        ('focus_default', index.get('issue-10', 0)),
        ('kind_labels', KIND_LABELS),
        ('nodes', nodes), ('node_ids', node_ids), ('edges', edges),
        ('edge_kind_counts', dict(counts)),
    ])
    json.dump(graph, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'wrote {a.out}: {len(nodes)} nodes, {len(edges)} edges, kinds {dict(counts)}')

if __name__ == '__main__':
    main()
