const N=20000, NSUB=5800, F=63340120796, W=63363988142, OLD=59637070538;
const key=(j,s)=>Math.floor((j+0.5)*s/N);
let bad=0, bad2=0;
for (const [a,b] of [[F,W],[W,F],[OLD,F],[F,OLD]]) for (let j=0;j<NSUB;j++){ const k=key(j,a); const jj=Math.floor(k*N/a);
  if (jj!==j || key(jj,a)!==k) bad++; // STEPS formula, no +-1 needed?
  let hit=-1; for (let d=-1;d<=1;d++) if (j+d>=0&&j+d<NSUB&&key(j+d,a)===k) hit=j+d; if (hit!==j) bad2++; }
console.log('STEPS j=floor(k*N/space) recovers j for all 4x5800:', bad===0, ' code +-1 window recovers j:', bad2===0);
console.log('subKey[1182] frozen', key(1182,F), ' main-sky', key(1182,W), ' 7a65dd3-sky', key(1182,OLD));
const k0=36064705400; console.log('36064705400 / frozen: j', Math.floor(k0*N/F), 'is star key?', key(Math.floor(k0*N/F),F)===k0, ' < SPACE', k0<F);
// false-positive remap: a non-star key that passes the check?
let fp=0; for (let t=0;t<200000;t++){ const k=Math.floor(Math.random()*F); const j=Math.floor(k*N/F); if (j<NSUB && key(j,F)===k) fp++; } console.log('random keys that pass the star-key check:', fp,'/200000');
