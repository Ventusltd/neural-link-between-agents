const { chromium, devices } = require('playwright');
const fs = require('fs');
(async () => {
  const V = '20260914T143049Z-v5-linkify-frontdoor-brandfaithful';
  const base = 'http://127.0.0.1:8204/spider/' + V + '/index.html';
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const out = {};
  for (const [name, url] of [['default', base], ['overview', base + '?graph=overview&focus=GLOBALGRID2050%20architecture']]) {
    const ctx = await browser.newContext({ ...devices['Pixel 7'] });
    const page = await ctx.newPage();
    const reqs = [], failed = [], errors = [], consoleErr = [];
    page.on('request', r => reqs.push(r.url()));
    page.on('requestfailed', r => failed.push(r.url() + ' ' + (r.failure() || {}).errorText));
    page.on('response', r => { if (r.status() >= 400) failed.push(r.url() + ' HTTP ' + r.status()); });
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 200)));
    page.on('console', m => { if (m.type() === 'error') consoleErr.push(m.text().slice(0, 200)); });
    const t0 = Date.now();
    await page.goto(url, { waitUntil: 'load', timeout: 120000 });
    await page.waitForTimeout(8000);
    const m = await page.evaluate(() => {
      const q = s => document.querySelector(s);
      const txt = s => (q(s) ? q(s).innerText.trim().slice(0, 300) : null);
      const sel = q('select'); const opts = sel ? [...sel.options].map(o => o.textContent.trim()) : [];
      const vis = [...document.querySelectorAll('button, a, select, input')].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
      const small = vis.filter(e => { const r = e.getBoundingClientRect(); return r.height < 44 || r.width < 44; }).length;
      return { title: document.title, vw: innerWidth, vh: innerHeight, sw: document.documentElement.scrollWidth, sh: document.documentElement.scrollHeight,
        eyebrow: txt('.brand .ey'), h1: txt('.brand h1'), count: txt('.count'), hint: txt('.hint'), crumbs: txt('.crumbs'), srctag: txt('.srctag'),
        graphOptions: opts, cards: document.querySelectorAll('.card, [class*=card]').length, svgs: document.querySelectorAll('svg').length,
        controls: vis.length, controlsUnder44: small, bodyText: document.body.innerText.replace(/\s+/g, ' ').slice(0, 600) };
    });
    await page.screenshot({ path: 'spider-pixel7-' + name + '.png', timeout: 180000 });
    out[name] = { url, loadMs: Date.now() - t0, m, requests: reqs, failed, pageErrors: errors, consoleErrors: consoleErr };
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync('spider-pixel7.json', JSON.stringify(out, null, 1));
  for (const k of Object.keys(out)) { const o = out[k]; console.log('==', k, o.loadMs + 'ms'); console.log(JSON.stringify(o.m, null, 1)); console.log('requests', o.requests.length); o.requests.forEach(r => console.log('  R', r)); console.log('failed', o.failed.length); o.failed.forEach(r => console.log('  F', r)); console.log('pageErrors', o.pageErrors); console.log('consoleErrors', o.consoleErrors.slice(0, 6)); }
})().catch(e => { console.error('ERR', e); process.exit(1); });
