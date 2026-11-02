// Unit test of SECTION C (builder) outside the browser: stubs for KY/H, real files, Node webcrypto. No Playwright.
'use strict';
const fs = require('fs'), path = require('path');
const ROOT = '/home/user/estate/kuiper-belt', ED = ROOT + '/editions/202611012135';
const src = fs.readFileSync(ED + '/modules/202611012309-apps.js', 'utf8');
const C0 = src.indexOf('// ======================================================================== SECTION C'), D0 = src.indexOf('// ======================================================================== SECTION D');
const sec = src.slice(C0, D0);
const removeGraphs = process.argv.includes('--no-graphs');
// the wafer, as index.html builds it
const rows = f => fs.readFileSync(ROOT + '/cosmos/' + f, 'utf8').split('\n').filter(l => l && l[0] !== '#').map(l => l.split('\t'));
const repos = rows('repos.tsv').map(p => ({ i: +p[0], name: p[1], lines: +p[2] }));
let k = 0; const commits = rows('wafer.tsv').map(p => { k += +p[4]; const c = { repo: +p[2], sha: p[3], k0: k, lines: +p[1] }; k += c.lines; return c; });
const SPACE = k, R = Math.sqrt(SPACE);
global.fetch = async (file) => { const p = path.join(ED, file); if (removeGraphs && /graphs/.test(file) || !fs.existsSync(p)) return { ok: false, status: 404 };
  const b = fs.readFileSync(p); return { ok: true, status: 200, arrayBuffer: async () => b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength), json: async () => JSON.parse(b) }; };
global.window = { crypto: globalThis.crypto };
global.addEventListener = () => {};
const H = { SPACE, repos, commits, keyPlace: kk => [kk / SPACE * R, 0], fmt: n => n.toLocaleString('en-GB'), o2: { canvas: { width: 400, height: 800 } }, cv: {} };
const regs = [];
const L = { get: id => ({ id, status: id === 'elements' ? 'REFUSED' : 'EMPTY' }), register: l => { regs.push(l); } };
const st = { said: [], spider: { status: 'WAIT', why: '', graphs: {} }, card: null };
let EL = null;
const loadElements = () => Promise.resolve().then(() => { EL = JSON.parse(fs.readFileSync(ED + '/data/elements.json')); return EL; });
const fn = new Function('KY', 'H', 'st', 'loadElements', 'getEL', 'mod', 'fmt', 'openElement', 'ID', 'C_RECORD', 'C_SEL', 'setTimeout',
  sec.replace(/\bEL\b/g, 'getEL()') + '\nreturn { registerLayers, loadSpider, nodeKey, C, GRAPHS };');
const KY = { draw: { add() {} }, redraw() {}, cam: { x: 0, y: 0, zoom: 1 } };
const X = fn(KY, H, st, loadElements, () => EL, () => L, H.fmt, () => true, 'apps', '#c9d3e6', '#ff2bd6', setTimeout);
X.registerLayers();
setTimeout(async () => {
  console.log('registered', regs.map(r => r.id));
  const sp = regs.find(r => r.id === 'spider'), el = regs.find(r => r.id === 'elements');
  try { console.log('elements load', await el.load()); } catch (e) { console.log('elements load FAIL', e.message); }
  try { console.log('spider load', await sp.load()); } catch (e) { console.log('spider load FAIL', e.message); }
  console.log(JSON.stringify(st.spider.graphs, null, 0).slice(0, 900));
  console.log('readout:', st.said);
  console.log('segs', X.C.segs.length, 'rings', X.C.rings.length, 'dots', X.C.dots.length);
}, 400);
