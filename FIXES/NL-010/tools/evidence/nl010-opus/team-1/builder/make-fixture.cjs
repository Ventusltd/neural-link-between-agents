// Builds a GridAtlas wordmark fixture from the real bytes: ventusv8.css (whole file) + the menu-bar module's
// installStyle() CSS array (gridatlas@5ec7f62 atlas/modules/202609031958-menu-bar.js:164-384), and the shell's
// .hud-header markup (atlas/releases/202608300453-atlas-v9/index.html:23-33) inside a .gm-brand-slot between two
// side groups of the six titles (buildBar :481-545).
const fs = require('fs');
const G = '/home/user/estate/gridatlas/';
const mod = fs.readFileSync(G + 'atlas/modules/202609031958-menu-bar.js', 'utf8').split('\n');
const start = mod.findIndex(l => l.includes('style.textContent = ['));
const end = mod.findIndex((l, i) => i > start && l.includes("].join('');"));
const BAR_ID = 'gridatlas-menu-bar';
const css = eval('[' + mod.slice(start + 1, end).join('\n') + ']').join('');
const v8 = fs.readFileSync(G + 'atlas/releases/202608300453-atlas-v9/ventusv8.css', 'utf8');
const shell = fs.readFileSync(G + 'atlas/releases/202608300453-atlas-v9/index.html', 'utf8').split('\n');
const hud = shell.slice(22, 34).join('\n');   // :23-34
const t = n => `<div class="gm-menu"><button class="gm-title">${n}</button></div>`;
const html = `<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>${v8}</style><style>${css}</style></head><body><div class="dashboard"><div class="map-container" style="flex:1">
<nav id="gridatlas-menu-bar"><div class="gm-side gm-side-left">${t('File')}${t('Edit')}${t('View')}</div>
<div class="gm-brand-slot">${hud}</div><div class="gm-side gm-side-right">${t('Scope')}${t('Grid')}${t('About')}</div></nav>
</div></div><script>(function t(){const now=new Date(),target=new Date(Date.UTC(2050,0,1,0,0,0));document.getElementById('clock').innerText=now.toLocaleTimeString('en-GB');document.getElementById('date').innerText=now.toLocaleDateString('en-GB');document.getElementById('days').innerText=Math.floor((target-now)/86400000)+' DAYS';setTimeout(t,1000)})()</script></body></html>`;
fs.writeFileSync(__dirname + '/ga-fixture/index.html', html);
console.log('lines', start + 1, end + 1, 'css bytes', css.length);
