#!/usr/bin/env node
// Independent held-out checks; scratch databases and pinned read-only source inputs.
import assert from 'node:assert/strict';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
const root=resolve(process.argv[2]||'audit-inputs'), out=resolve(process.argv[3]||'audit-receipts');
mkdirSync(out,{recursive:true});
const read=(repo,path)=>readFileSync(resolve(root,repo,path));
const json=(repo,path)=>JSON.parse(read(repo,path));
const load=(repo,path)=>import(pathToFileURL(resolve(root,repo,path)).href);
const pins={"satnav":"1865b9051894d9e89cf5720e091b62c9041a567b","gridatlas":"1c9ed251ea31de67cc9d7e3b3d7908ea6aa39779","stars":"7c90d879688ca80c7ed63982eec0894fe75d67a3","cvaa":"b124c39e5343b24dd5b546a0c279a1c06360bdad","spiders":"c6fccc802c3534286c167bb7e96bbf5f4962f6bd","code-generator":"857ea81244848b1da8fe21fffaed74cab568a3b4"};
const receipt={schema:'satnav.independent-cartridge-audit.v1',pins,checks:[],scope:'isolated fixtures, not deployment or operational navigation'};
let bad=0;
async function check(name,fn){
  try{const detail=await fn();receipt.checks.push({name,status:'PASS',detail});console.log('PASS',name);}
  catch(e){bad++;receipt.checks.push({name,status:'FAIL',detail:String(e.message)});console.error('FAIL',name,e.message);}
}
await check('exact source checkout pins',()=>{for(const [repo,sha] of Object.entries(pins))assert.equal(execFileSync('git',['-C',resolve(root,repo),'rev-parse','HEAD'],{encoding:'utf8'}).trim(),sha);});
await check('all active GridAtlas cartridge bytes match composition',()=>{
  const manifest=json('gridatlas','atlas/current.json');
  assert.equal(manifest.generation,'202611222343');
  assert.equal(manifest.cartridges.length,9);
  assert.deepEqual(manifest.cartridges.map(x=>x.id),manifest.cartridge_order);
  const selected=manifest.cartridges.map(c=>{
    assert.match(c.path,/^\.\/(?:cartridges|modules)\/[A-Za-z0-9._-]+\.js$/);
    const bytes=read('gridatlas','atlas/'+c.path.slice(2));
    assert.equal(createHash('sha256').update(bytes).digest('hex'),c.sha256,c.id);
    execFileSync(process.execPath,['--check',resolve(root,'gridatlas','atlas',c.path)]);
    return {id:c.id,path:c.path,sha256:c.sha256,bytes:bytes.length};
  });
  return selected;
});
await check('current manifest does not activate historical vicinity or newer resolver by assumption',()=>{
  const m=json('gridatlas','atlas/current.json');
  const paths=m.cartridges.map(x=>x.path);
  assert.ok(paths.includes('./cartridges/202611132345-place-global-search-v9-5.js'));
  assert.ok(!paths.some(x=>x.includes('202611180026-place-global-search')));
  assert.ok(paths.includes('./modules/202611222000-uk-offtakers-overlay.js'));
  return 'Use the active native map/card surface; successor resolver is a separate candidate.';
});
await check('picker explicit confirmation and no mode promotion',async()=>{
  const {createPicker}=await load('satnav','nav/picker.mjs');
  const sent=[];const p=createPicker({onConfirm:x=>sent.push(x)});
  await p.search('Testbury');assert.equal(p.snapshot().results.length,2);
  p.chooseResult(1);assert.equal(sent.length,0);p.cancel();assert.equal(sent.length,0);
  p.chooseMapPoint({at:[-2.1,53.4],label:'Test',mode:'road_to_field',asset:{source:'bad',id:'bad'}});
  const x=p.confirm();assert.deepEqual(x.coordinates,[-2.1,53.4]);assert.equal(x.mode,'compass');assert.equal(x.asset,null);assert.equal(x.accessStatus,'unverified');assert.equal(sent.length,1);
});
await check('picker invalid map replacement cannot leave previous pending confirmation',async()=>{
  const {createPicker}=await load('satnav','nav/picker.mjs');
  const p=createPicker();p.chooseMapPoint({at:[-2,53],label:'old'});
  assert.throws(()=>p.chooseMapPoint({at:[999,53],label:'invalid'}));
  assert.equal(p.snapshot().pending,null,'invalid replacement retains a stale pending point');
  assert.throws(()=>p.confirm());
});
await check('picker selecting a different visible search result before confirmation',async()=>{
  const {createPicker}=await load('satnav','nav/picker.mjs');
  const p=createPicker();await p.search('Testbury');p.chooseResult(0);p.chooseResult(1);
  assert.deepEqual(p.snapshot().pending.coordinates,[-2.1,53.4]);
});
await check('Stars exact duplicates do not allocate new lines/elements; reformat same family',async()=>{
  const {openDb,ingestFile,rebuildTablet}=await load('stars','modular-star/lib.mjs');
  const ctx=openDb(':memory:');
  const a=Buffer.from('function add(a,b) {\n  return a + b;\n}\n');
  const b=Buffer.from('function add(a,b){\n return a+b; // format\n}\n');
  const c=Buffer.from('function add(a,b){\n return a-b;\n}\n');
  const put=(path,bytes)=>ingestFile(ctx,{repo:'fixture',commit:'synthetic',path,bytes});
  const count=table=>ctx.db.prepare('SELECT count(*) n FROM '+table).get().n;
  const id=put('a.js',a), before=['line','tablet','element','family'].map(count);
  assert.equal(put('copy.js',a),id);assert.deepEqual(['line','tablet','element','family'].map(count),before);
  assert.equal(count('occurrence'),2);assert.deepEqual(rebuildTablet(ctx,id),a);
  put('b.js',b);assert.equal(count('family'),1);assert.equal(count('element'),2);
  put('c.js',c);assert.equal(count('family'),2);ctx.db.close();
});
await check('Stars semantically different ASI return functions have different families',async()=>{
  const {extractJs}=await load('stars','modular-star/lib.mjs');
  const a='function f(){\n return 1\n}\n', b='function f(){\n return\n 1\n}\n';
  assert.notEqual(extractJs(a)[0].family.toString('hex'),extractJs(b)[0].family.toString('hex'),'token-only family conflates return 1 and return newline 1');
});
await check('Stars distinct nested function spans sharing physical lines remain distinct elements',async()=>{
  const {openDb,ingestFile,extractJs}=await load('stars','modular-star/lib.mjs');
  const src='function outer(){ return function inner(){\n return 1;\n}; }\n';
  assert.equal(extractJs(src).length,2);
  const ctx=openDb(':memory:');
  ingestFile(ctx,{repo:'fixture',commit:'synthetic',path:'nested.js',bytes:Buffer.from(src)});
  const n=ctx.db.prepare('SELECT count(*) n FROM element').get().n;
  ctx.db.close();assert.equal(n,2,'whole-line element hash conflates nested spans');
});
await check('periodic table and code generator links and relevant named block identities',()=>{
  const page=read('stars','table.html').toString('utf8');
  assert.match(page,/graph=periodic-table/);assert.match(page,/ventusltd\.github\.io\/code-generator\//);
  assert.match(page,/blocks\/blocks\.json/);
  const presets=json('stars','blocks/presets.json').presets;
  const p=presets.find(x=>x.id==='substation-finder');assert.deepEqual(p.blocks,['Si','Vn','Ug','Ps','Dt']);
  const blocks=json('stars','blocks/blocks.json').blocks;
  for(const symbol of p.blocks){const b=blocks.find(x=>x.symbol===symbol);assert.ok(b,'missing block '+symbol);}
  const recipe=json('code-generator','apps/substation-finder/parts.json');assert.deepEqual(recipe.blocks,p.blocks);
  return {table:'https://ventusltd.github.io/stars/table.html',generator:'https://ventusltd.github.io/code-generator/',blocks:p.blocks,scope:'pinned data links; not live-browser test'};
});
writeFileSync(resolve(out,'independent.json'),JSON.stringify(receipt,null,2)+'\n');
process.exitCode=bad?1:0;
