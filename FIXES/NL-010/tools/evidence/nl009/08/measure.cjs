// FABLE-08 type audit: measure text sizes, line lengths, panel rects on Android emulation.
// usage: node measure.cjs <variant orig|patched> <device pixel7|s360> [shots-prefix]
const { chromium, devices } = require('playwright');
const fs = require('fs');
const variant = process.argv[2] || 'orig', dev = process.argv[3] || 'pixel7', shots = process.argv[4] || '';
const URL = 'http://127.0.0.1:8108/editions/' + variant + '/';
const ctxOpts = dev === 'pixel7' ? { ...devices['Pixel 7'] }
  : { viewport: { width: 360, height: 640 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true,
      userAgent: devices['Pixel 7'].userAgent };
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const ctx = await browser.newContext(ctxOpts);
  const page = await ctx.newPage();
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push('pageerror ' + e.message));
  await page.goto(URL, { waitUntil: 'load', timeout: 180000 });
  await sleep(8000);
  const out = { variant, dev, viewport: ctxOpts.viewport, dsf: ctxOpts.deviceScaleFactor, errors };

  // generic measurer, run in page
  const measure = await page.evaluateHandle(() => {
    const dsf = devicePixelRatio;
    function charW(el) { const cs = getComputedStyle(el); const c = document.createElement('canvas').getContext('2d'); c.font = cs.fontWeight + ' ' + cs.fontSize + ' ' + cs.fontFamily; return c.measureText('x'.repeat(100)).width / 100; }
    function sizes(root) {
      const seen = new Map();
      const walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = walk.nextNode())) { if (!n.textContent.trim()) continue; const el = n.parentElement; const cs = getComputedStyle(el);
        if (cs.display === 'none') continue; const r = el.getBoundingClientRect(); if (!r.width && !r.height) continue;
        const key = el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ').filter(Boolean).join('.') : '');
        const fs = parseFloat(cs.fontSize);
        const rec = seen.get(key) || { sel: key, fontPx: fs, devPx: +(fs * dsf).toFixed(1), lineH: cs.lineHeight, color: cs.color, chars: 0, sample: n.textContent.trim().slice(0, 40) };
        rec.chars += n.textContent.trim().length; seen.set(key, rec); }
      return [...seen.values()];
    }
    function panel(sel) { const el = document.querySelector(sel); const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
      const cw = r.width - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight); const ch = charW(el);
      const text = el.innerText || el.textContent;
      return { sel, rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) }, pctOfScreen: +(100 * r.height / innerHeight).toFixed(1),
        fontPx: parseFloat(cs.fontSize), devPx: +(parseFloat(cs.fontSize) * dsf).toFixed(1), lineHeight: cs.lineHeight, charWidthPx: +ch.toFixed(2), charsPerLine: Math.floor(cw / ch),
        textChars: text.replace(/\s+/g, ' ').trim().length, words: text.trim().split(/\s+/).length, scrollH: el.scrollHeight, clientH: el.clientHeight, overflow: el.scrollHeight > el.clientHeight + 1,
        fontFamily: cs.fontFamily, textSizeAdjust: cs.webkitTextSizeAdjust || cs.textSizeAdjust, sizes: sizes(el) }; }
    return { panel, sizes, charW };
  });
  const P = async sel => page.evaluate(([m, s]) => m.panel(s), [measure, sel]);
  out.html = await page.evaluate(() => ({ fontSize: getComputedStyle(document.documentElement).fontSize, bodyFont: getComputedStyle(document.body).font,
    textSizeAdjust: getComputedStyle(document.documentElement).webkitTextSizeAdjust, inner: [innerWidth, innerHeight], dsf: devicePixelRatio }));

  // the bar
  out.bar = await P('#bar');
  out.bar.buttons = await page.evaluate(() => [...document.querySelectorAll('#bar .gm-title, #barname')].map(b => { const r = b.getBoundingClientRect(); const cs = getComputedStyle(b); return { t: b.textContent, x: +r.x.toFixed(0), y: +r.y.toFixed(0), w: +r.width.toFixed(0), h: +r.height.toFixed(0), fontPx: parseFloat(cs.fontSize), color: cs.color }; }));
  out.bar.rows = new Set(out.bar.buttons.map(b => b.y)).size;
  const tapBar = async name => { const r = await page.evaluate(n => { const b = document.querySelector('#bar [data-panel=' + n + ']'); const q = b.getBoundingClientRect(); return [q.x + q.width / 2, q.y + q.height / 2]; }, name); await page.touchscreen.tap(r[0], r[1]); await sleep(400); };
  const shot = async (name, clip) => { if (!shots) return; await page.screenshot({ path: shots + '-' + name + '.png', timeout: 180000, clip }); };

  // panels
  const map = { top: 'edition', hud: 'readout', lines: 'lines', foot: 'commands' };
  out.panels = {};
  for (const [id, name] of Object.entries(map)) {
    await tapBar(id); const p = await P('#' + id); p.open = await page.evaluate(i => document.getElementById(i).classList.contains('gm-open'), id);
    if (id === 'lines') { p.rows = await page.evaluate(() => { const rows = [...document.querySelectorAll('#lineslist .ln')]; const r0 = rows[0] && rows[0].getBoundingClientRect(); return { count: rows.length, firstRowH: r0 && +r0.height.toFixed(1), rowText: rows[0] && rows[0].innerText.slice(0, 80) }; }); }
    out.panels[name] = p;
    await shot(name);
    await tapBar(id);
  }
  // the card after "next verified line"
  await page.keyboard.press('e'); await sleep(7000);
  out.card = await P('#card');
  out.card.link = await page.evaluate(() => { const a = document.querySelector('#card a'); const r = a.getBoundingClientRect(); const cs = getComputedStyle(a); return { h: +r.height.toFixed(1), fontPx: parseFloat(cs.fontSize), color: cs.color }; });
const sparkPos = () => page.evaluate(() => { const o = document.getElementById('o'); const g = o.getContext('2d'); const d = g.getImageData(0, 0, o.width, o.height).data; let sx = 0, sy = 0, n = 0;
    for (let i = 0; i < d.length; i += 4) { if (d[i] > 200 && d[i + 1] < 90 && d[i + 2] > 170 && d[i + 3] > 80) { const p = i / 4; sx += p % o.width; sy += Math.floor(p / o.width); n++; } }
    const k = innerWidth / o.width; const c = document.getElementById('card').getBoundingClientRect(); const bar = document.getElementById('bar').getBoundingClientRect();
    if (!n) return { found: false }; const x = sx / n * k, y = sy / n * k; return { found: true, x: +x.toFixed(0), y: +y.toFixed(0), underCard: y > c.top, underBar: y < bar.bottom }; });
  out.card.spark = await sparkPos();
  await shot('card');
  // details open
  await page.evaluate(() => document.querySelector('#card .ct').dispatchEvent(new MouseEvent('click', { bubbles: true })));
  await sleep(300);
  out.cardDetails = await P('#card');
  await shot('card-details');
  // platform fonts actually used (this Linux Chromium; Android reasoning in the report)
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  const doc = await cdp.send('DOM.getDocument', { depth: -1 });
  const q = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '#barname' });
  out.platformFonts = (await cdp.send('CSS.getPlatformFontsForNode', { nodeId: q.nodeId })).fonts;

  // font scaling: 125 % via text-size-adjust (needs Blink's text autosizer) and via zoom on the text containers
  const probe = () => page.evaluate(() => { const b = document.querySelector('#bar .gm-title'); const c = document.getElementById('card'); const bar = document.getElementById('bar').getBoundingClientRect(); return { btnH: +b.getBoundingClientRect().height.toFixed(1), barH: +bar.height.toFixed(1), barRows: new Set([...document.querySelectorAll('#bar .gm-title, #barname')].map(x => Math.round(x.getBoundingClientRect().y))).size, cardH: +c.getBoundingClientRect().height.toFixed(1), cardPct: +(100 * c.getBoundingClientRect().height / innerHeight).toFixed(1), cardOverflow: c.scrollHeight > c.clientHeight + 1 }; });
  out.scale100 = await probe();
  await page.addStyleTag({ content: 'html{-webkit-text-size-adjust:125%!important;text-size-adjust:125%!important}' });
  await sleep(500); out.scaleTSA125 = await probe();
  await page.addStyleTag({ content: '#bar,#top,#hud,#foot,#lines,#card{zoom:1.25}' });
  await sleep(500); out.scaleZoom125 = await probe();
  out.scaleZoom125.spark = await sparkPos();
  await shot('card-125');
  await page.evaluate(() => document.querySelector('#card .cx').dispatchEvent(new MouseEvent('click', { bubbles: true })));
  await tapBar('top'); await sleep(300);
  out.scaleZoom125.edition = await P('#top');
  await shot('edition-125');
  await browser.close();
  fs.writeFileSync('/tmp/nl009/08/measure-' + variant + '-' + dev + '.json', JSON.stringify(out, null, 1));
  console.log(JSON.stringify(out, null, 1));
})().catch(e => { console.error(e); process.exit(1); });
