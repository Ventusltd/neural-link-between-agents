const { chromium, devices } = require('playwright');
const fs = require('fs');
const OUT = '/tmp/nl010/team-1';
const URL = 'http://127.0.0.1:8201/atlas/';
const args = ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'];


const VENDOR = '/home/user/estate/kuiper-belt/see-through/202610050513/vendor/';
const BLOCKED = [];
async function wire(page, tag) {
  await page.route('**/*', async (route) => {
    const u = route.request().url();
    if (u.startsWith('http://127.0.0.1:8201/')) return route.continue();
    if (u.includes('maplibre-gl@3.6.2/dist/maplibre-gl.js')) return route.fulfill({ status: 200, contentType: 'application/javascript', body: fs.readFileSync(VENDOR + 'maplibre-gl.js') });
    if (u.includes('maplibre-gl@3.6.2/dist/maplibre-gl.css')) return route.fulfill({ status: 200, contentType: 'text/css', body: fs.readFileSync(VENDOR + 'maplibre-gl.css') });
    if (u.includes('basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json')) return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ version: 8, name: 'stub-dark', sources: {}, layers: [{ id: 'bg', type: 'background', paint: { 'background-color': '#0b0e14' } }] }) });
    BLOCKED.push(tag + ' ' + u.slice(0, 140));
    return route.abort('blockedbyclient');
  });
}

async function measure(page, tag) {
  // wait for the menu bar to install (max 60 s)
  let installed = false;
  for (let i = 0; i < 60; i++) {
    installed = await page.evaluate(() => !!document.getElementById('gridatlas-menu-bar'));
    if (installed) break;
    await page.waitForTimeout(1000);
  }
  await page.waitForTimeout(4000);
  const data = await page.evaluate(() => {
    const r = (el) => { if (!el) return null; const b = el.getBoundingClientRect(); return { x: +b.x.toFixed(1), y: +b.y.toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1) }; };
    const cs = (el, props) => { if (!el) return null; const s = getComputedStyle(el); const o = {}; props.forEach(p => o[p] = s.getPropertyValue(p)); return o; };
    const bar = document.getElementById('gridatlas-menu-bar');
    const out = { viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio }, title: document.title, href: location.href };
    out.menuBarState = window.__GRIDATLAS_MODULES__ && window.__GRIDATLAS_MODULES__.menuBar ? JSON.parse(JSON.stringify(window.__GRIDATLAS_MODULES__.menuBar, (k, v) => typeof v === 'function' ? undefined : v)) : null;
    out.bar = { rect: r(bar), style: cs(bar, ['position','top','left','right','height','z-index','background-color','border-bottom','font-family','font-size','line-height','backdrop-filter','display']) };
    out.titles = bar ? Array.from(bar.querySelectorAll('.gm-title')).map(t => ({ text: t.textContent, rect: r(t), side: t.closest('.gm-side') ? t.closest('.gm-side').className : null, style: cs(t, ['font-family','font-size','letter-spacing','text-transform','color','padding','min-height','background-color']) })) : [];
    const brand = bar ? bar.querySelector('.gm-brand-slot') : null;
    out.brandSlot = brand ? { rect: r(brand), style: cs(brand, ['max-width','padding','display','justify-content']), html: brand.innerHTML.slice(0, 3000) } : null;
    const hh = document.querySelector('.hud-header');
    out.hudHeader = hh ? { rect: r(hh), parent: hh.parentElement && hh.parentElement.className, children: Array.from(hh.children).map(c => ({ tag: c.tagName, cls: c.className, text: c.textContent.replace(/\s+/g,' ').trim(), rect: r(c), display: getComputedStyle(c).display })), style: cs(hh, ['display','gap','font-family']) } : null;
    const vm = document.querySelector('.ventus-main');
    const vs = document.querySelector('.ventus-sub');
    out.ventusMain = vm ? { tag: vm.tagName, text: vm.textContent.trim(), rect: r(vm), style: cs(vm, ['font-family','font-size','font-weight','letter-spacing','color','text-shadow','line-height','margin']), link: (vm.closest('a') || {}).href || null, parentTag: vm.parentElement.tagName, parentCls: vm.parentElement.className } : null;
    out.ventusSub = vs ? { tag: vs.tagName, text: vs.textContent.trim(), rect: r(vs), style: cs(vs, ['font-family','font-size','font-weight','letter-spacing','color','text-transform']) } : null;
    out.images = Array.from(document.querySelectorAll('img, svg, [style*="background-image"]')).filter(e => /ventus|logo|brand/i.test((e.outerHTML||'').slice(0,400)) || (e.closest && e.closest('#gridatlas-menu-bar'))).slice(0,20).map(e => ({ tag: e.tagName, src: e.currentSrc || e.src || null, natural: e.naturalWidth ? { w: e.naturalWidth, h: e.naturalHeight } : null, rect: r(e), cls: e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className, bg: getComputedStyle(e).backgroundImage }));
    out.anchorsInBar = bar ? Array.from(bar.querySelectorAll('a')).slice(0, 30).map(a => ({ text: a.textContent.replace(/\s+/g,' ').trim().slice(0,60), href: a.href, target: a.target, hidden: a.offsetParent === null })) : [];
    const sel = {
      mapContainer: '.map-container', map: '#map, .maplibregl-map', mapControls: '.map-controls', search: '.search-bar-wrapper', attrib: '.custom-map-attrib', scada: '#scada-ui-container', scadaBrand: '.scada-brand', statusLegend: '.status-legend', fsLetterhead: '#fs-letterhead', btnExport: '#btn-export', btnStatus: '#btn-status', btnFullscreen: '#btn-fullscreen', btnRadius: '#btn-radius', btnZone: '#btn-zonedraw', btnMeasure: '#btn-measure', disclaimer: '.disclaimer-box', podcast: '.podcast-shoutout', maplibreCtrlTL: '.maplibregl-ctrl-top-left', maplibreCtrlTR: '.maplibregl-ctrl-top-right', maplibreCtrlBL: '.maplibregl-ctrl-bottom-left', maplibreCtrlBR: '.maplibregl-ctrl-bottom-right'
    };
    out.landmarks = {};
    for (const k in sel) { const el = document.querySelector(sel[k]); out.landmarks[k] = el ? { rect: r(el), visible: !!(el.offsetParent || el.getClientRects().length), inBar: !!el.closest('#gridatlas-menu-bar'), parentCls: el.parentElement && (el.parentElement.className || el.parentElement.id), display: getComputedStyle(el).display, position: getComputedStyle(el).position, zIndex: getComputedStyle(el).zIndex } : null; }
    // visible elements that sit over the map outside the bar: anything absolutely/fixed positioned with text, top-level
    out.overlays = Array.from(document.body.querySelectorAll('*')).filter(e => { const s = getComputedStyle(e); if (!(s.position === 'absolute' || s.position === 'fixed')) return false; if (e.closest('#gridatlas-menu-bar')) return false; if (e.closest('.maplibregl-canvas-container')) return false; const b = e.getBoundingClientRect(); return b.width > 0 && b.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && e.textContent.trim().length > 0 && b.width < innerWidth; }).slice(0, 40).map(e => ({ tag: e.tagName, id: e.id, cls: String(e.className).slice(0,60), text: e.textContent.replace(/\s+/g,' ').trim().slice(0, 50), rect: r(e) }));
    out.brandChain = (function(){ const vm = document.querySelector('#gridatlas-menu-bar .ventus-main'); const chain = []; let e = vm; while (e && e.id !== 'gridatlas-menu-bar') { chain.push(e.tagName + (e.id ? '#' + e.id : '') + (e.className ? '.' + String(e.className).split(' ').join('.') : '')); e = e.parentElement; } return chain; })();
    out.rootVars = { clear: getComputedStyle(document.documentElement).getPropertyValue('--gridatlas-menu-bar-clear') };
    out.bodyFont = cs(document.body, ['font-family','font-size','background-color','color']);
    return out;
  });
  fs.writeFileSync(`${OUT}/measure-${tag}.json`, JSON.stringify(data, null, 1));
  await page.screenshot({ path: `${OUT}/shell-${tag}.png`, timeout: 180000 });
  // open each menu and measure its panel
  const names = ['File','Edit','View','Scope','Grid','About'];
  const panels = {};
  for (const n of names) {
    try {
      const t = page.locator(`#gridatlas-menu-bar .gm-title:has-text("${n}")`).first();
      await t.click({ timeout: 5000 });
      await page.waitForTimeout(600);
      panels[n] = await page.evaluate((n) => {
        const bar = document.getElementById('gridatlas-menu-bar');
        const p = Array.from(bar.querySelectorAll('.gm-panel')).find(p => !p.hidden);
        if (!p) return null;
        const b = p.getBoundingClientRect();
        const items = Array.from(p.querySelectorAll('button,[role="button"],a,.gm-layer-group,label')).filter(e => e.getClientRects().length).slice(0, 80).map(e => ({ tag: e.tagName, text: e.textContent.replace(/\s+/g,' ').trim().slice(0, 70), href: e.href || null, h: +e.getBoundingClientRect().height.toFixed(0) }));
        return { rect: { x: +b.x.toFixed(1), y: +b.y.toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1) }, position: getComputedStyle(p).position, count: items.length, items };
      }, n);
      await page.screenshot({ path: `${OUT}/menu-${n.toLowerCase()}-${tag}.png`, timeout: 180000 });
      await page.keyboard.press('Escape');
      await page.waitForTimeout(300);
    } catch (e) { panels[n] = { error: String(e).slice(0, 200) }; }
  }
  fs.writeFileSync(`${OUT}/panels-${tag}.json`, JSON.stringify(panels, null, 1));
  console.log(tag, 'installed', installed, 'bar', JSON.stringify(data.bar.rect), 'titles', data.titles.map(t => t.text + '@' + t.rect.x + ',' + t.rect.y + ' ' + t.rect.w + 'x' + t.rect.h).join(' | '));
}

(async () => {
  const browser = await chromium.launch({ args });
  const consoleLog = [];
  // desktop
  {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const page = await ctx.newPage(); await wire(page, 'desk');
    page.on('console', m => consoleLog.push('[desk] ' + m.type() + ' ' + m.text().slice(0, 200)));
    page.on('requestfailed', rq => consoleLog.push('[desk] FAIL ' + rq.url().slice(0, 160)));
    await page.goto(URL, { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(8000);
    await measure(page, 'desktop-1280x800');
    await ctx.close();
  }
  {
    const ctx = await browser.newContext({ ...devices['Pixel 7'] });
    const page = await ctx.newPage(); await wire(page, 'px7');
    page.on('console', m => consoleLog.push('[px7] ' + m.type() + ' ' + m.text().slice(0, 200)));
    page.on('requestfailed', rq => consoleLog.push('[px7] FAIL ' + rq.url().slice(0, 160)));
    await page.goto(URL, { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(8000);
    await measure(page, 'pixel7');
    await ctx.close();
  }
  {
    const ctx = await browser.newContext({ ...devices['Pixel 7'], viewport: { width: 360, height: 740 } });
    const page = await ctx.newPage(); await wire(page, '360');
    await page.goto(URL, { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(8000);
    await measure(page, '360x740');
    await ctx.close();
  }
  fs.writeFileSync(`${OUT}/console.log`, consoleLog.join('\n'));
  fs.writeFileSync(`${OUT}/blocked-requests.log`, Array.from(new Set(BLOCKED)).join('\n'));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
