const { chromium, devices } = require('playwright');
(async () => {
  const url = 'http://127.0.0.1:8106/editions/202611012027/';
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const out = {};
  for (const dev of (process.argv[2] ? [process.argv[2]] : ['Pixel 7', 'Galaxy S24', 'Pixel 7 landscape'])) {
    const ctx = await browser.newContext({ ...devices[dev] });
    const page = await ctx.newPage();
    const errors = [];
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', e => errors.push('pageerror: ' + e.message));
    await page.goto(url, { waitUntil: 'load' });
    await page.waitForTimeout(7000);
    const m = await page.evaluate(() => {
      const bar = document.getElementById('bar'); const r = bar.getBoundingClientRect();
      const items = [...bar.children].map(el => { const b = el.getBoundingClientRect(); const cs = getComputedStyle(el); return { tag: el.tagName, text: el.textContent.trim(), x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height), font: cs.fontSize, pad: cs.padding, border: cs.borderTopColor, deco: cs.textDecorationLine }; });
      const btnRows = new Set(items.filter(i => i.tag !== 'SPAN').map(i => i.y)).size;
      const a = bar.querySelector('a.gm-title');
      const resolved = new URL(a.getAttribute('href'), location.href).href;
      const pages = new URL(a.getAttribute('href'), 'https://ventusltd.github.io/kuiper-belt/editions/202611012027/').href;
      const pagesFromPointer = new URL(a.getAttribute('href'), 'https://ventusltd.github.io/kuiper-belt/editions/202611019999/index.html').href;
      const ap = [...document.querySelectorAll('#edapps a')].map(x => ({ text: x.textContent, href: x.getAttribute('href'), local: new URL(x.getAttribute('href'), location.href).href, pages: new URL(x.getAttribute('href'), 'https://ventusltd.github.io/kuiper-belt/editions/202611012027/').href }));
      return { vw: innerWidth, vh: innerHeight, barH: Math.round(r.height), btnRows, items, sumW: items.reduce((s, i) => s + i.w, 0) + 4 * (items.length - 1) + 16, seeThrough: { target: a.getAttribute('target'), href: a.getAttribute('href'), resolved, pages, pagesFromPointer }, edapps: ap, edappsText: document.getElementById('edapps').textContent };
    });
    // HEAD the resolved links through the page (same origin)
    m.linkStatus = await page.evaluate(async (urls) => { const o = {}; for (const u of urls) { try { const r = await fetch(u, { method: 'GET', redirect: 'follow' }); o[u] = r.status; } catch (e) { o[u] = String(e); } } return o; }, [m.seeThrough.resolved, ...m.edapps.map(x => x.local)]);
    const safe = dev.replace(/ /g, '_');
    await page.screenshot({ path: `/tmp/nl009/06/after-bar-${safe}.png`, clip: { x: 0, y: 0, width: m.vw, height: Math.min(m.vh, 260) }, timeout: 180000 });
    // open the EDITION panel by touch and record the apps paragraph
    const ed = m.items.find(i => i.text === 'edition');
    await page.touchscreen.tap(ed.x + ed.w / 2, ed.y + ed.h / 2);
    await page.waitForTimeout(800);
    m.panel = await page.evaluate(() => { const t = document.getElementById('top'); const e = document.getElementById('edapps'); const tr = t.getBoundingClientRect(), er = e.getBoundingClientRect(); return { open: t.classList.contains('gm-open'), panel: { y: Math.round(tr.y), h: Math.round(tr.height), scrollH: t.scrollHeight, clientH: t.clientHeight }, edapps: { y: Math.round(er.y), h: Math.round(er.height), bottom: Math.round(er.bottom) }, visibleWithoutScroll: er.bottom <= tr.bottom + 1 }; });
    if (dev === 'Pixel 7') await page.screenshot({ path: `/tmp/nl009/06/after-panel-${safe}.png`, clip: { x: 0, y: 0, width: m.vw, height: Math.min(m.vh, 620) }, timeout: 180000 });
    // the panel must not be toggled by the link; tap SEE THROUGH with the panel open and follow it
    const st = m.items.find(i => i.text === 'see through');
    const nav = page.waitForNavigation({ waitUntil: 'load', timeout: 60000 }).catch(e => 'no navigation: ' + e.message);
    await page.touchscreen.tap(st.x + st.w / 2, st.y + st.h / 2);
    const navRes = await nav;
    await page.waitForTimeout(3000);
    m.afterTap = { navigation: typeof navRes === 'string' ? navRes : 'navigated', href: page.url(), title: await page.title() };
    // and the back gesture (history back) returns to the edition
    await page.goBack({ waitUntil: 'load' }).catch(e => { m.back = 'goBack failed: ' + e.message; });
    await page.waitForTimeout(6000);
    m.back = Object.assign(m.back || {}, await page.evaluate(() => ({ href: location.href, barItems: document.querySelectorAll('#bar .gm-title').length, openPanel: !!document.querySelector('.gm-open'), big: document.getElementById('big').textContent })));
    m.errors = errors;
    out[dev] = m;
    await ctx.close();
  }
  console.log(JSON.stringify(out, null, 1));
  await browser.close();
})();
