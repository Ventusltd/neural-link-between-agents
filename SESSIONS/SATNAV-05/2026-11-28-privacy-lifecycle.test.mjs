// SATNAV-05 independent test receipt. Node 22; no dependencies.
 // Prepare a temporary directory containing this file and nav/app.mjs from:
 // https://github.com/Ventusltd/satnav/blob/9698781539e549deaa6ecaa4a2b34610c1f9fd29/nav/app.mjs
 // Verify git hash-object nav/app.mjs = 9ae118926d62b1bc8741ae73235e79a9e29378d1.
 // In that temporary directory ONLY, stub nav/place.mjs:
 // export function parseDestination(){return null;}
 // and nav/compass.mjs:
 // export function fixQuality(fix){return fix?'usable':'missing';}
 // export function guide(){return null;}
 // Run node 2026-11-28-privacy-lifecycle.test.mjs
 // Result 28 Nov: 8/8. Mock DOM, mock geolocation, synthetic (0,0).
 // Not a browser, real GPS, routing, geodesy, network privacy or handset test.
import assert from 'node:assert/strict';
const elements=new Map(), docEvents={},winEvents={},watchers=[],cleared=[];
const el=id=>{if(!elements.has(id))elements.set(id,{style:{},addEventListener(){}});return elements.get(id);};
globalThis.document={getElementById:el,addEventListener:(n,f)=>docEvents[n]=f,hidden:false};
globalThis.window={addEventListener:(n,f)=>winEvents[n]=f};
globalThis.location={search:''};globalThis.isSecureContext=true;
Object.defineProperty(globalThis,'navigator',{value:{geolocation:{watchPosition(ok,err){watchers.push({ok,err});return watchers.length-1;},clearWatch(i){cleared.push(i);}}},configurable:true});
globalThis.setInterval=()=>0;
await import('./nav/app.mjs');
const fix={coords:{longitude:0,latitude:0,accuracy:5,heading:null,speed:null},timestamp:Date.now()};
let count=0;function test(name,fn){try{fn();console.log('PASS',name);count++;}catch(e){console.log('FAIL',name,e.message);process.exitCode=1;}}
test('No watch on module initialization',()=>assert.equal(watchers.length,0));
el('start').onclick();test('Explicit Start opens one watch',()=>assert.equal(watchers.length,1));
el('start').onclick();test('Repeated Start does not open a second watch',()=>assert.equal(watchers.length,1));
watchers[0].ok(fix);test('Simulated position appears after opt-in',()=>assert.match(el('position').textContent,/Position 0\.00000, 0\.00000/));
el('stop').onclick();test('Stop clears watch and displayed position',()=>{assert.deepEqual(cleared,[0]);assert.equal(el('position').textContent,'Position unavailable');assert.equal(el('stop').disabled,true);});
watchers[0].ok(fix);test('Late callback after Stop cannot restore position',()=>assert.equal(el('position').textContent,'Position unavailable'));
el('start').onclick();watchers[1].err({code:1});test('Permission denial clears watch and resets controls',()=>{assert.deepEqual(cleared,[0,1]);assert.equal(el('status').textContent,'Location permission denied');assert.equal(el('start').disabled,false);});
el('start').onclick();watchers[2].ok(fix);winEvents.pagehide();test('Pagehide clears watch and displayed position',()=>{assert.deepEqual(cleared,[0,1,2]);assert.equal(el('position').textContent,'Position unavailable');});
console.log(count+'/8 passed');
