#!/bin/bash
# rebuild the scratch edition: live modules + data, patched index.html, manifest with fresh sha256s
B=/tmp/nl010-opus/team-5/builder; KB=/home/user/estate/kuiper-belt; E=$B/site/editions/202611012135
rm -rf $E; mkdir -p $E; cp -r $KB/editions/202611012135/{index.html,keys.json,data,modules} $E/
cd $E && patch -s -p3 < $KB/editions/202611012135/handoff/04-loader/index.html.patch || exit 1
python3 - "$E" "$@" <<'PY'
import sys, json, hashlib, os
E = sys.argv[1]; ids = sys.argv[2:] or ['line-card', 'see-through']
mods = []
for f in sorted(os.listdir(E + '/modules')):
    stamp, name = f[:12], f[13:-3]
    if name not in ids: continue
    b = open(E + '/modules/' + f, 'rb').read()
    import subprocess
    reg = json.loads(subprocess.check_output(['node', '-e', 'let r;global.window={KY:{register:x=>r=x}};global.document={};require(process.argv[1]);console.log(JSON.stringify({q:r.requires,p:r.provides}))', E + '/modules/' + f]))
    mods.append({'id': name, 'generation': stamp, 'path': 'modules/' + f, 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b),
                 'byte_budget': 65536, 'requires': reg['q'], 'provides': reg['p'], 'reads': [], 'writes': [], 'creates_controls': 'none', 'licence': 'Apache-2.0'})
order = [i for i in ids if any(m['id'] == i for m in mods)]
json.dump({'schema': 'kuiper.modules.v1', 'edition': '202611012135', 'hooks': 'kuiper.hooks.v1', 'order': order, 'modules': mods}, open(E + '/modules.json', 'w'), indent=1)
print('order', order)
PY
