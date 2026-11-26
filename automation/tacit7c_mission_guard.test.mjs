import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
import {guard} from './tacit7c_mission_guard.mjs';
const raw=readFileSync('.cvaa/contracts/vedic-third-turn-recovery.json');
const r=JSON.parse(raw), d=JSON.parse(readFileSync('.cvaa/contracts/vedic-core-mission.json'));
const blob=createHash('sha1').update('blob '+raw.length+'\0').update(raw).digest('hex');
assert.equal(d.recovery.blob,blob,'recovery bytes changed; repin and review');
assert.deepEqual(guard(d,r),[]);
const cases=[
['missing channel',(a,b)=>a.channels.pop()],
['duplicate channel',(a,b)=>a.channels.push(a.channels[0])],
['fake printer',(a,b)=>a.channels.find(x=>x.id==='spider-printer').blob='a'.repeat(40)],
['activation',(a,b)=>a.consumer_state='LIVE'],
['lost workstream',(a,b)=>b.workstreams.pop()],
['fake settlement',(a,b)=>b.workstreams[0].settlement='SETTLED'],
['lost gate',(a,b)=>a.gates.pop()],
['focus drift',(a,b)=>a.focus.push('unrelated')],
['in-progress green',(a,b)=>{b.workstreams[0].observed_runs[0].conclusion='success'}],
['wrong recovery link',(a,b)=>a.recovery.blob='a'.repeat(40)]
];
for(const [name,mut] of cases){const a=structuredClone(d),b=structuredClone(r);mut(a,b);assert.ok(guard(a,b).length,name);}
console.log('12/12 controls: recovery byte identity, healthy and 10 disease cases');
