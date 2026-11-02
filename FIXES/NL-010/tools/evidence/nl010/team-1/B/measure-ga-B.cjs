const { chromium, devices } = require('playwright');
const fs = require('fs');
const ML = fs.readFileSync('/home/user/estate/kuiper-belt/see-through/202610050609/vendor/maplibre-gl.js');
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const out = {};
  for (const [name, ctxOpts] of [['desktop1280', { viewport: { width: 1280, height: 800 } }], ['pixel7', { ...devices['Pixel 7'] }], ['w360', { viewport: { width: 360, height: 780 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true }]]) {
    const ctx = await browser.newContext(ctxOpts);
    await ctx.route(/^https?:\/\/(?!127\.0\.0\.1)/, route => {
      const u = route.request().url();
      if (/maplibre-gl.*\.js$/.test(u)) return route.fulfill({ status: 200, contentType: 'text/javascript', body: ML });
      if (/maplibre-gl.*\.css$/.test(u)) return route.fulfill({ status: 200, contentType: 'text/css', body: '' });
      if (/style\.json/.test(u)) return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ version: 8, name: 'stub', sources: {}, layers: [{ id: 'bg', type: 'background', paint: { 'background-color': '#000' } }] }) });
      return route.abort();
    });
    const page = await ctx.newPage();
    const errs = []; page.on('pageerror', e => errs.push(String(e).slice(0, 200)));
    await page.goto('http://127.0.0.1:8772/atlas/', { waitUntil: 'load', timeout: 120000 });
    let installed = false;
    try { await page.waitForSelector('#gridatlas-menu-bar', { timeout: 60000 }); installed = true; } catch (e) {}
    await page.waitForTimeout(3000);
    const m = await page.evaluate(() => {
      const rr = e => { if (!e) return null; const b = e.getBoundingClientRect(); return { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height) }; };
      const cs = (e, props) => { if (!e) return null; const s = getComputedStyle(e); const o = {}; for (const p of props) o[p] = s[p]; return o; };
      const bar = document.getElementById('gridatlas-menu-bar');
      const titles = [...document.querySelectorAll('#gridatlas-menu-bar .gm-title')].map(b => ({ text: b.textContent, rect: rr(b), style: cs(b, ['fontSize','fontFamily','letterSpacing','textTransform','color']) }));
      const brand = document.querySelector('#gridatlas-menu-bar .gm-brand-slot');
      const main = document.querySelector('#gridatlas-menu-bar .ventus-main');
      const sub = document.querySelector('#gridatlas-menu-bar .ventus-sub');
      const state = window.__GRIDATLAS_MODULES__ && window.__GRIDATLAS_MODULES__.menuBar;
      return {
        vw: innerWidth, vh: innerHeight, gen: document.documentElement.dataset.gridatlasGeneration,
        bar: rr(bar), barStyle: cs(bar, ['position','height','font','backgroundColor','borderBottom','zIndex']),
        titles, brand: rr(brand), main: { rect: rr(main), text: main && main.textContent, style: cs(main, ['fontSize','fontWeight','fontFamily','letterSpacing','color','textTransform']), insideAnchor: !!(main && main.closest('a')), onclick: !!(main && (main.onclick || main.closest('[onclick]'))) },
        sub: { rect: rr(sub), text: sub && sub.textContent, style: cs(sub, ['fontSize','letterSpacing','color']) },
        mapContainer: rr(document.querySelector('.map-container')), map: rr(document.getElementById('map')),
        hudHeaderParent: document.querySelector('.hud-header') && document.querySelector('.hud-header').parentElement.className,
        letterhead: cs(document.getElementById('fs-letterhead'), ['display']),
        panelCounts: state && state.panel_counts, installedState: state && state.installed, layer_controls: state && state.layer_controls, failure: state && state.failure, waiting: state && state.waiting_for,
        gridChips: [...document.querySelectorAll('#gridatlas-mobile-tray button')].filter(b => !b.hidden).map(b => ({ text: b.textContent.trim(), rect: rr(b) }))
      };
    });
    out[name] = { installed, ...m, errors: errs.slice(0, 5) };
    await page.screenshot({ path: `/tmp/nl010/team-1/B/ga-${name}.png`, timeout: 180000 }); fs.writeFileSync('/tmp/nl010/team-1/B/ga-' + name + '.json', JSON.stringify(out[name], null, 1));
    if (installed) {
      // open each menu and measure its panel
      const panels = {};
      for (let i = 0; i < 6; i++) {
        await page.click(`#gridatlas-menu-bar-title-${i}`);
        await page.waitForTimeout(400);
        panels[await page.textContent(`#gridatlas-menu-bar-title-${i}`)] = await page.evaluate((i) => { const p = document.getElementById('gridatlas-menu-bar-panel-' + i); const b = p.getBoundingClientRect(); return { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height), items: [...p.querySelectorAll('button,a,label,.gm-layer-group')].slice(0, 40).map(e => e.textContent.replace(/\s+/g, ' ').trim().slice(0, 60)) }; }, i);
        if (name === 'desktop1280') await page.screenshot({ path: `/tmp/nl010/team-1/B/ga-${name}-menu${i}.png`, timeout: 180000 });
        await page.keyboard.press('Escape');
      }
      out[name].panels = panels; fs.writeFileSync('/tmp/nl010/team-1/B/ga-' + name + '.json', JSON.stringify(out[name], null, 1));
    }
    await ctx.close();
  }
  console.log(JSON.stringify(out, null, 1));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
