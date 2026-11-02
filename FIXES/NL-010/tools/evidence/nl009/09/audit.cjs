// FABLE-09 robust audit of Kuiper Edition 4 on Pixel 7. Usage: node audit.cjs <orig|patched> [outdir]
const { chromium, devices } = require('playwright');
const fs = require('fs');
const variant = process.argv[2] || 'orig';
const out = process.argv[3] || ('/tmp/nl009/09/out-' + variant);
fs.mkdirSync(out, { recursive: true });
const PAGE = fs.readFileSync(variant === 'orig' ? '/tmp/nl009/09/index.orig.html' : '/tmp/nl009/09/index.html', 'utf8');
const URL = 'http://127.0.0.1:8109/editions/202611012027/';
const ARGS = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'];
const sleep = ms => new Promise(r => setTimeout(r, ms));
const R = { variant, scenarios: {} };
const note = (k, v) => { R.scenarios[k] = v; console.log(k, JSON.stringify(v)); };

async function serve(ctx, opts = {}) {
  await ctx.route(u => /editions\/202611012027\/(index\.html)?$/.test(u.pathname), r => r.fulfill({ status: 200, contentType: 'text/html', body: PAGE }));
  if (opts.keys404) await ctx.route(/keys\.json$/, r => r.fulfill({ status: 404, contentType: 'text/plain', body: 'not here' }));
}
function wire(page, log) {
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') log.push(m.type() + ': ' + m.text().slice(0, 160)); });
  page.on('pageerror', e => log.push('pageerror: ' + String(e && e.message || e).slice(0, 160)));
}
// what the browser laid out: rectangles, the magenta spark on the overlay, the panel and bar
const MEASURE = () => {
  const q = s => document.querySelector(s);
  const rect = el => { if (!el) return null; const r = el.getBoundingClientRect(); return { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1), vis: getComputedStyle(el).display !== 'none' && r.width > 0 && r.height > 0 }; };
  const cv = q('#c'), ov = q('#o');
  let spark = null; try {
    const ctx = ov.getContext('2d'); const d = ctx.getImageData(0, 0, ov.width, ov.height).data; let n = 0, sx = 0, sy = 0;
    for (let i = 0; i < d.length; i += 4) { if (d[i] > 200 && d[i + 1] < 90 && d[i + 2] > 170 && d[i + 3] > 150) { const p = i / 4; sx += p % ov.width; sy += Math.floor(p / ov.width); n++; } }
    if (n) spark = { x: +(sx / n).toFixed(1), y: +(sy / n).toFixed(1), px: n };
  } catch (e) { spark = { err: String(e) }; }
  const open = document.querySelector('.gm-open');
  return { inner: [innerWidth, innerHeight], cvBuf: [cv.width, cv.height], cvCss: rect(cv), bar: rect(q('#bar')), card: rect(q('#card')),
    openPanel: open ? open.id : null, panelRect: rect(open), panelTop: open ? open.style.top : null, spark,
    big: (q('#big') || {}).textContent, hudLines: (q('#hud') || {}).textContent.split('\n').filter(l => /EDITION|keys\.json|WebGL|CONTEXT|did not load/.test(l)) };
};
function clear(m) { // is the spark in the clear space: under the bar, above the card, inside the screen
  if (!m.spark || m.spark.err) return 'no spark pixels on the overlay';
  const top = m.bar ? m.bar.y + m.bar.h : 0, bot = m.card && m.card.vis ? m.card.y : m.inner[1];
  const ok = m.spark.x > 0 && m.spark.x < m.inner[0] && m.spark.y > top && m.spark.y < bot;
  return (ok ? 'IN CLEAR' : 'NOT CLEAR') + ' spark(' + m.spark.x + ',' + m.spark.y + ') bar.bottom=' + top.toFixed(0) + ' card.top=' + (m.card && m.card.vis ? m.card.y : 'none') + ' inner=' + m.inner.join('x');
}
async function tapButton(page, sel) { const b = await page.$(sel); const r = await b.boundingBox(); await page.touchscreen.tap(r.x + r.width / 2, r.y + r.height / 2); }

(async () => {
  const browser = await chromium.launch({ args: ARGS });
  // ---------------------------------------------------------------- 1. portrait, panel + card, rotate, toolbar
  {
    const log = []; const ctx = await browser.newContext({ ...devices['Pixel 7'] }); await serve(ctx);
    const page = await ctx.newPage(); wire(page, log);
    await page.goto(URL); await sleep(8000);
    // aria and structure
    const aria = await page.evaluate(() => {
      const q = s => document.querySelector(s), qa = s => [...document.querySelectorAll(s)];
      const at = el => el ? Object.fromEntries([...el.attributes].filter(a => /^(role|aria-|id$|tabindex|type)/.test(a.name)).map(a => [a.name, a.value])) : null;
      return { noscript: !!q('noscript'), bar: at(q('#bar')), barButtons: qa('#bar .gm-title').map(b => ({ text: b.textContent, ...at(b) })),
        panels: ['#top', '#hud', '#lines', '#foot'].map(s => ({ s, ...at(q(s)) })), card: at(q('#card')), lyFind: at(q('#lyFind')),
        detailsToggle: (() => { const t = q('#card .ct'); return t ? { tag: t.tagName, ...at(t) } : 'card closed'; })(),
        linesRowsFocusable: qa('#lineslist [data-i]').filter(r => r.tabIndex >= 0).length, linesRows: qa('#lineslist [data-i]').length,
        barDomIndex: [...document.body.children].findIndex(e => e.id === 'bar'), bodyChildren: [...document.body.children].map(e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '')) };
    });
    note('aria_rest', aria);
    // focus order: Tab from the document
    const order = []; for (let i = 0; i < 7; i++) { await page.keyboard.press('Tab'); order.push(await page.evaluate(() => { const a = document.activeElement; if (!a || a === document.body) return 'body'; const cs = getComputedStyle(a); return (a.tagName.toLowerCase() + (a.id ? '#' + a.id : '') + (a.className ? '.' + String(a.className).split(' ')[0] : '') + '[' + (a.textContent || '').trim().slice(0, 14) + '] outline=' + cs.outlineStyle + '/' + cs.outlineWidth + ' fv=' + a.matches(':focus-visible')); })); }
    note('focus_order', order);
    await page.evaluate(() => document.activeElement && document.activeElement.blur());
    // open READOUT and pick a line
    await tapButton(page, '#bar [data-panel="hud"]'); await sleep(300);
    await page.keyboard.press('e'); await sleep(7000);
    const m0 = await page.evaluate(MEASURE); note('portrait_panel_card', { ...m0, clear: clear(m0) });
    const ariaOpen = await page.evaluate(() => { const b = document.querySelector('#bar .gm-on'); const t = document.querySelector('#card .ct'), x = document.querySelector('#card .cx');
      return { onButton: b ? Object.fromEntries([...b.attributes].map(a => [a.name, a.value])) : null, details: t ? { tag: t.tagName, tabIndex: t.tabIndex, role: t.getAttribute('role'), expanded: t.getAttribute('aria-expanded') } : null,
        close: x ? { tag: x.tagName, label: x.getAttribute('aria-label'), w: x.getBoundingClientRect().width, h: x.getBoundingClientRect().height } : null,
        cardAttrs: Object.fromEntries([...document.getElementById('card').attributes].map(a => [a.name, a.value])) }; });
    note('aria_open', ariaOpen);
    await page.screenshot({ path: out + '/portrait.png', scale: 'css', timeout: 180000 });
    // rotate to landscape (same device, swapped)
    await page.setViewportSize({ width: 839, height: 412 }); await sleep(6000);
    const m1 = await page.evaluate(MEASURE); note('landscape', { ...m1, clear: clear(m1) });
    await page.screenshot({ path: out + '/landscape.png', scale: 'css', timeout: 180000 });
    // back to portrait
    await page.setViewportSize({ width: 412, height: 839 }); await sleep(6000);
    const m2 = await page.evaluate(MEASURE); note('portrait_again', { ...m2, clear: clear(m2) });
    // Android dynamic toolbar: the viewport loses 56 px
    await page.setViewportSize({ width: 412, height: 783 }); await sleep(6000);
    const m3 = await page.evaluate(MEASURE); note('toolbar_minus56', { ...m3, clear: clear(m3) });
    await page.setViewportSize({ width: 412, height: 839 }); await sleep(4000);
    // Escape: first closes the panel, then (patched) the card
    await page.keyboard.press('Escape'); await sleep(300);
    const e1 = await page.evaluate(() => ({ panel: !!document.querySelector('.gm-open'), card: getComputedStyle(document.getElementById('card')).display }));
    await page.keyboard.press('Escape'); await sleep(300);
    const e2 = await page.evaluate(() => ({ panel: !!document.querySelector('.gm-open'), card: getComputedStyle(document.getElementById('card')).display }));
    note('escape', { afterFirst: e1, afterSecond: e2 });
    // hash deep link (does the engine read location.hash at all?)
    note('console_main', log);
    await ctx.close();
  }
  // ---------------------------------------------------------------- 2. reduced motion: is the fly instant?
  {
    const log = []; const ctx = await browser.newContext({ ...devices['Pixel 7'], reducedMotion: 'reduce' }); await serve(ctx);
    const page = await ctx.newPage(); wire(page, log);
    await page.goto(URL); await sleep(8000);
    await page.evaluate(() => { window.__zooms = []; const h = document.getElementById('hud'); new MutationObserver(() => { const m = h.textContent.match(/zoom ([\d.]+) px per key|zoom 1 px = ([^\n]+)/); if (m) { const v = m[1] ? +m[1] : ('1px=' + m[2]); if (window.__zooms[window.__zooms.length - 1] !== v) window.__zooms.push(v); } }).observe(h, { childList: true, characterData: true, subtree: true }); });
    await page.keyboard.press('e'); await sleep(7000);
    const z = await page.evaluate(() => ({ matches: matchMedia('(prefers-reduced-motion: reduce)').matches, zooms: window.__zooms.slice(0, 12), n: window.__zooms.length }));
    note('reduced_motion', { ...z, console: log });
    await ctx.close();
  }
  // ---------------------------------------------------------------- 3. keys.json 404
  {
    const log = []; const ctx = await browser.newContext({ ...devices['Pixel 7'] }); await serve(ctx, { keys404: true });
    const page = await ctx.newPage(); wire(page, log);
    await page.goto(URL); await sleep(8000);
    await tapButton(page, '#bar [data-panel="hud"]'); await sleep(500);
    const hud = await page.evaluate(() => document.getElementById('hud').innerText);
    await tapButton(page, '#bar [data-panel="top"]'); await sleep(500);
    const top = await page.evaluate(() => document.getElementById('top').innerText.slice(0, 200));
    await tapButton(page, '#bar [data-panel="lines"]'); await sleep(500);
    const lines = await page.evaluate(() => document.getElementById('lineslist').innerText.slice(0, 200));
    await page.keyboard.press('Escape'); await page.keyboard.press('e'); await sleep(500);
    const card = await page.evaluate(() => getComputedStyle(document.getElementById('card')).display);
    note('keys404', { hudEditionLines: hud.split('\n').filter(l => /EDITION|keys/.test(l)), editionPanel: top, linesPanel: lines, cardAfterE: card, console: log });
    await ctx.close();
  }
  // ---------------------------------------------------------------- 4. no JavaScript
  {
    const ctx = await browser.newContext({ ...devices['Pixel 7'], javaScriptEnabled: false }); await serve(ctx);
    const page = await ctx.newPage(); await page.goto(URL); await sleep(1500);
    const t = await page.evaluate(() => ({ text: document.body.innerText.trim().slice(0, 300), visible: [...document.body.querySelectorAll('*')].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && e.textContent.trim() && getComputedStyle(e).display !== 'none' && e.children.length === 0; }).map(e => e.tagName + ':' + e.textContent.trim().slice(0, 60)).slice(0, 6) })).catch(e => ({ err: String(e) }));
    // evaluate needs JS; fall back to content()
    const html = await page.content();
    note('no_js', { evaluated: t, noscriptInHtml: /<noscript/i.test(html) });
    await ctx.close();
  }
  // ---------------------------------------------------------------- 5. hash deep link
  {
    const log = []; const ctx = await browser.newContext({ ...devices['Pixel 7'] }); await serve(ctx);
    const page = await ctx.newPage(); wire(page, log);
    await page.goto(URL + '#1000000'); await sleep(8000);
    const h = await page.evaluate(() => ({ hash: location.hash, card: getComputedStyle(document.getElementById('card')).display, hud: document.getElementById('hud').textContent.split('\n')[0].slice(0, 80), big: document.getElementById('big').textContent, bar: !!document.getElementById('bar') }));
    note('hash', { ...h, engineReadsHash: /location\.hash/.test(PAGE), console: log });
    await ctx.close();
  }
  await browser.close();
  // ---------------------------------------------------------------- 6. WebGL unavailable
  {
    const b2 = await chromium.launch({ args: [...ARGS, '--disable-webgl', '--disable-webgl2', '--disable-3d-apis'] });
    const log = []; const ctx = await b2.newContext({ ...devices['Pixel 7'] }); await serve(ctx);
    const page = await ctx.newPage(); wire(page, log);
    await page.goto(URL); await sleep(3000);
    const t = await page.evaluate(() => ({ gl2: !!document.createElement('canvas').getContext('webgl2'), bar: !!document.getElementById('bar'),
      visibleText: [...document.body.querySelectorAll('*')].filter(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden' && e.children.length === 0 && e.textContent.trim(); }).map(e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ':' + e.textContent.trim().slice(0, 90)).slice(0, 8),
      hudText: document.getElementById('hud').textContent, hudDisplay: getComputedStyle(document.getElementById('hud')).display }));
    note('no_webgl', { ...t, console: log });
    await page.screenshot({ path: out + '/nowebgl.png', scale: 'css', timeout: 180000 });
    await ctx.close(); await b2.close();
  }
  fs.writeFileSync(out + '/result.json', JSON.stringify(R, null, 1));
  console.log('written', out + '/result.json');
})().catch(e => { console.error('FATAL', e); process.exit(1); });
