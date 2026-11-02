// OPUS-2 evidence: the cost of the 1,240,449-character header (kuiper-belt estate-network.json:1, key 63013167769)
const { chromium, devices } = require('playwright'); const fs = require('fs'), crypto = require('crypto');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const U = 'http://127.0.0.1:8423/editions/202611012135/', ED = '/home/user/estate/kuiper-belt/editions/202611012135';
const IDX = '/tmp/nl010-opus/team-2/evidence/apply/editions/202611012135/index.html';
const MOD = fs.readdirSync(ED + '/modules').find(f => /^\d{12}-line-card\.js$/.test(f));
(async () => {
  const bytes = fs.readFileSync(ED + '/modules/' + MOD), sha = crypto.createHash('sha256').update(bytes).digest('hex');
  const manifest = { schema:'kuiper.modules.v1', edition:'202611012135', hooks:'kuiper.hooks.v1', order:['line-card'], modules:[{ id:'line-card',
    generation: MOD.slice(0,12), path:'modules/' + MOD, sha256: sha, bytes: bytes.length, byte_budget: 32768,
    requires:['card','esc','fmt','address','describe','sel','lit','redraw','gbox'], provides:['line-card'], reads:[], writes:['#card'],
    creates_controls:'none', licence:'Apache-2.0', team:'02', step:2, proof:'handoff/02-card/' }], contracts:{} };
  const browser = await chromium.launch({ args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const out = { module: MOD, sha256: sha, devices: {} };
  for (const name of ["Pixel 7", "Galaxy S24"]) {
    const ctx = await browser.newContext({ ...devices[name] });
    await ctx.route(U, r => r.fulfill({ body: fs.readFileSync(IDX), contentType:'text/html' }));
    await ctx.route(U + 'modules.json', r => r.fulfill({ body: JSON.stringify(manifest), contentType:'application/json' }));
    const page = await ctx.newPage(); const errs = [];
    page.on('pageerror', e => errs.push('pageerror ' + e.message)); page.on('console', m => { if (m.type() === 'error') errs.push('console ' + m.text()); });
    await page.goto(U, { waitUntil:'load' }); await sleep(8000);
    const r = await page.evaluate(async () => {
      const j = await (await fetch('keys.json')).json(), api = KY.modules['line-card'].api, card = KY.hooks.card;
      const time = async (b) => { const t0 = performance.now(); api.show(b, { index:0, of:344 }); const rc = card.getBoundingClientRect();
        const t1 = performance.now(); await new Promise(res => requestAnimationFrame(() => requestAnimationFrame(res))); const t2 = performance.now();
        const code = card.querySelector('header.lc-h > code'), h = card.querySelector('header.lc-h').getBoundingClientRect();
        return { show_layout_ms: +(t1 - t0).toFixed(1), to_second_frame_ms: +(t2 - t0).toFixed(1), header_equal: code.textContent === b.line_text,
          chars: b.line_text.length, card_share: +(rc.height / innerHeight).toFixed(3), header_h: Math.round(h.height), code_scrollH: code.scrollHeight, code_rect_h: Math.round(code.getBoundingClientRect().height), code_w: Math.round(code.getBoundingClientRect().width), hdr_scrollW: card.querySelector("header.lc-h").scrollWidth, hdr_scrollH: card.querySelector("header.lc-h").scrollHeight }; };
      const big = j.bodies.find(b => b.key === 63013167769), small = j.bodies.find(b => b.key === 36064705400);
      const res = { small: await time(small), big: await time(big), small2: await time(small), big2: await time(big), sha: 0 }; return res; });
    await page.screenshot({ path: "/tmp/nl010-opus/team-2/evidence/t/big-" + name.replace(/ /g, "-") + ".png", timeout: 180000 });
    const _x = await page.evaluate(() => { KY.modules["line-card"].api.close(); return 1;
      api.close(); return res; });
    out.devices[name] = { ...r, errors: errs }; console.error(name, JSON.stringify(out.devices[name])); await ctx.close();
  }
  await browser.close(); fs.writeFileSync('/tmp/nl010-opus/team-2/evidence/t/bigline.json', JSON.stringify(out, null, 1));
})().catch(e => { console.error(e); process.exit(1); });
