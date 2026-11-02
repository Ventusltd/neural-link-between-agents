const { chromium, devices } = require('playwright');
const fs = require('fs');
const PORT = 8413, BASE = `http://127.0.0.1:${PORT}/editions/202611012135/`;
const MOD = 'modules/202611012143-kuiper-shell.js';
const VP = [
  ['Galaxy S24', devices['Galaxy S24']],
  ['Pixel 7', devices['Pixel 7']],
  ['393', { ...devices['Pixel 7'], viewport: { width: 393, height: 852 } }],
  ['430', { ...devices['Pixel 7'], viewport: { width: 430, height: 932 } }],
  ['434', { ...devices['Pixel 7'], viewport: { width: 434, height: 932 } }],
  ['Pixel 7 landscape', devices['Pixel 7 landscape']],
  ['1280x800', { viewport: { width: 1280, height: 800 } }],
];
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const out = {};
  for (const [name, dev] of VP) {
    const ctx = await browser.newContext(dev); const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push('pageerror ' + e.message));
    page.on('console', m => { if (m.type() === 'error') errs.push('console ' + m.text()); });
    await page.route(BASE, async r => { const res = await r.fetch(); let b = await res.text();
      b = b.replace('</body>', `<script src="${MOD}"></script></body>`); r.fulfill({ response: res, body: b }); });
    console.error('start', name, Date.now()); await page.goto(BASE, { waitUntil: 'domcontentloaded', timeout: 60000 }); await page.waitForTimeout(7000); console.error('loaded', name, Date.now());
    out[name] = await page.evaluate(() => {
      const R = e => { if (!e) return null; const r = e.getBoundingClientRect(); return [+r.x.toFixed(1), +r.y.toFixed(1), +r.width.toFixed(1), +r.height.toFixed(1)]; };
      const bar = document.getElementById('kuiper-menu-bar'); const cs = e => getComputedStyle(e);
      const vm = bar && bar.querySelector('.ventus-main'), vs = bar && bar.querySelector('.ventus-sub'), hh = bar && bar.querySelector('.hud-header'), vb = bar && bar.querySelector('.ventus-brand');
      const titles = bar ? [...bar.querySelectorAll('.gm-title')].map(t => [t.textContent, ...R(t)]) : [];
      const left = bar && bar.querySelector('.gm-side-left');
      return { state: window.__KUIPER_SHELL__ ? window.__KUIPER_SHELL__.inspect() : (window.__KUIPER_MODULES__||{}).menuBar,
        bar: R(bar), barBg: bar && cs(bar).backgroundColor, barBorder: bar && cs(bar).borderBottom, barFont: bar && cs(bar).font, pos: bar && cs(bar).position,
        scroll: bar && [bar.scrollWidth, bar.clientWidth], titles,
        titleStyle: titles.length && (s => [s.fontSize, s.letterSpacing, s.color, s.textTransform, s.paddingLeft])(cs(bar.querySelector('.gm-menu>.gm-title'))),
        leftSide: R(left), leftContent: left && left.scrollWidth,
        hudHeader: R(hh), brand: R(vb), brandCentre: vb && +((vb.getBoundingClientRect().x + vb.getBoundingClientRect().width/2) - innerWidth/2).toFixed(2),
        vm: vm && [R(vm), cs(vm).fontSize, cs(vm).fontWeight, cs(vm).letterSpacing, cs(vm).color, cs(vm).textTransform, cs(vm).fontFamily, !!vm.closest('a')],
        vs: vs && [R(vs), cs(vs).fontSize, cs(vs).letterSpacing, cs(vs).color],
        flanks: hh && [...hh.children].map(c => cs(c).display),
        strip: R(document.getElementById('kuiper-star-strip')), starIds: document.querySelectorAll('#kuiper-star-strip').length,
        oldBar: (b => b && [cs(b).visibility, R(b)])(document.getElementById('bar')),
        safeTop: null, iw: innerWidth };
    });
    out[name].errors = errs;
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync(__dirname + '/measure.json', JSON.stringify(out, null, 1));
  console.log(JSON.stringify(out, null, 0));
})();
