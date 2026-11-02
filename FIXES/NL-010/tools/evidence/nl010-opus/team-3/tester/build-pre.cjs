// build-pre.cjs: PRE-INTEGRATION shim for test.cjs --index/--manifest. Edition 4 copy + team 4's index.html.patch
// (+ team 3's index.html.patch when it exists), and a manifest listing the named modules in order.
//   node build-pre.cjs layers [kuiper-shell line-card ...]
const fs = require('fs'), path = require('path'), cp = require('child_process'), crypto = require('crypto');
const ED = '/home/user/estate/kuiper-belt/editions/202611012135', OUT = '/tmp/nl010-opus/team-3/tester/pre';
const ids = process.argv.slice(2).length ? process.argv.slice(2) : ['layers'];
const work = path.join(OUT, 'tree'); fs.rmSync(work, { recursive: true, force: true }); fs.mkdirSync(path.join(work, 'editions/202611012135'), { recursive: true });
fs.copyFileSync(path.join(ED, 'index.html'), path.join(work, 'editions/202611012135/index.html'));
const log = [];
const PATCHES = (process.env.PATCHES || '04-loader/index.html.patch,03-layers/index.html.after-04-loader.patch').split(',').map(x => x.split('/'));
for (const [p, name] of PATCHES) { const f = path.join(ED, 'handoff', p, name); if (!fs.existsSync(f)) { log.push(p + ': no ' + name); continue; }
  try { cp.execFileSync('patch', ['-p1', '--dry-run', '-i', f], { cwd: work, encoding: 'utf8' }); log.push(p + ' ' + name + ': ' + cp.execFileSync('patch', ['-p1', '--no-backup-if-mismatch', '-i', f], { cwd: work, encoding: 'utf8' }).trim().replace(/\n/g, ' / ')); }
  catch (e) { log.push(p + ' ' + name + ': DOES NOT APPLY, skipped: ' + String(e.stdout || e.message).replace(/\n/g, ' / ')); } }
fs.copyFileSync(path.join(work, 'editions/202611012135/index.html'), path.join(OUT, 'index.html'));
const files = fs.readdirSync(path.join(ED, 'modules'));
const modules = ids.map(id => { const f = files.filter(x => new RegExp('^\\d{12}-' + id + '\\.js$').test(x)).sort().pop(); if (!f) throw new Error('no module ' + id);
  const b = fs.readFileSync(path.join(ED, 'modules', f)), s = b.toString('utf8');
  const arr = k => { const m = s.match(new RegExp('(?:' + k + '|' + k.toUpperCase() + ')\\s*[:=]\\s*\\[([^\\]]*)\\]')); return m ? m[1].split(',').map(x => x.trim().replace(/^['"]|['"]$/g, '')).filter(Boolean) : []; };
  return { id, generation: f.slice(0, 12), path: 'modules/' + f, sha256: 'live', bytes: b.length, byte_budget: Math.max(65536, b.length * 2),
    requires: arr('requires'), provides: arr('provides').length ? arr('provides') : [id], reads: [], writes: [], creates_controls: 'see module', licence: 'Apache-2.0', team: 'pre', step: 0, proof: 'pre-integration shim' }; });
const man = { schema: 'kuiper.modules.v1', edition: '202611012135', hooks: 'kuiper.hooks.v1', order: ids, modules };
fs.writeFileSync(path.join(OUT, 'modules.json'), JSON.stringify(man, null, 1));
console.log(log.join('\n')); console.log(JSON.stringify(modules.map(m => [m.id, m.path, m.sha256, m.requires.join(' ')])));
