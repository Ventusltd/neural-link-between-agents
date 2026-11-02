// probe: with shell + line-card, tap a LINES row and log what happens to #card
const { chromium, devices } = require('playwright'); const fs = require('fs'); const path = require('path');
const T = '/home/user/estate/kuiper-belt/editions/202611012135/handoff/02-card/test.cjs';
(async () => {
  const report = JSON.parse(fs.readFileSync('/tmp/nl010-opus/team-2/tester/run-shell/report.json', 'utf8'));
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const ctx = await b.newContext({ ...devices['Pixel 7'] });
  // reuse the served html/manifest the test builds: run the test's builder by requiring it is not possible; rebuild here
  const { execFileSync } = require('child_process');
  const ED = '/home/user/estate/kuiper-belt/editions/202611012135';
  const tmp = fs.mkdtempSync('/tmp/nl010-opus/team-2/tester/probe/s-'); fs.mkdirSync(tmp + '/editions/202611012135', { recursive: true });
  fs.copyFileSync(ED + '/index.html', tmp + '/editions/202611012135/index.html'); execFileSync('git', ['init', '-q'], { cwd: tmp });
  execFileSync('git', ['apply', ED + '/handoff/04-loader/index.html.patch'], { cwd: tmp }); execFileSync('git', ['apply', ED + '/handoff/02-card/index.patch'], { cwd: tmp });
  const html = fs.readFileSync(tmp + '/editions/202611012135/index.html', 'utf8');
  const crypto = require('crypto'); const rec = (id, f) => { const buf = fs.readFileSync(ED + '/modules/' + f); return { id, generation: f.slice(0, 12), path: 'modules/' + f, sha256: crypto.createHash('sha256').update(buf).digest('hex'), bytes: buf.length, byte_budget: 131072, requires: (buf.toString().match(/requires\s*:\s*\[([^\]]*)\]/)[1].match(/['"]([^'"]+)['"]/g) || []).map(s => s.slice(1, -1)), provides: [id], licence: 'Apache-2.0' }; };
  const man = { schema: 'kuiper.modules.v1', edition: '202611012135', hooks: 'kuiper.hooks.v1', order: ['kuiper-shell', 'line-card'], modules: [rec('kuiper-shell', '202611012143-kuiper-shell.js'), JSON.parse(fs.readFileSync(ED + '/handoff/02-card/MODULE.json'))] };
  const U = 'http://127.0.0.1:8422/editions/202611012135/';
  await ctx.route(u => u.href === U || u.href === U + 'index.html', r => r.fulfill({ body: html, contentType: 'text/html' }));
  await ctx.route(u => u.href === U + 'modules.json', r => r.fulfill({ body: JSON.stringify(man), contentType: 'application/json' }));
  const p = await ctx.newPage(); const log = []; p.on('console', m => log.push('console ' + m.type() + ' ' + m.text())); p.on('pageerror', e => log.push('pageerror ' + e.message));
  await p.goto(U); await p.waitForFunction(() => window.KY && KY.modules['line-card'] && KY.modules['kuiper-shell'], null, { timeout: 120000 }); await new Promise(r => setTimeout(r, 7000));
  await p.evaluate(() => { window.__log = []; const c = document.getElementById('card');
    new MutationObserver(ms => ms.forEach(m => window.__log.push([Math.round(performance.now()), 'card ' + m.attributeName + '=' + c.getAttribute(m.attributeName), new Error().stack.split('\n').slice(2, 5).join(' | ')]))).observe(c, { attributes: true });
    for (const t of ['pointerdown', 'pointerup', 'click', 'popstate', 'keydown']) addEventListener(t, e => window.__log.push([Math.round(performance.now()), t, (e.target && (e.target.id || e.target.className || e.target.tagName)) + '']), true);
    const lc = KY.modules['line-card'].api; });
  const wafer = await p.evaluate(() => { const t = document.querySelector('[data-menu="wafer"] > .gm-title'); const r = t.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; });
  await p.touchscreen.tap(wafer.x, wafer.y); await new Promise(r => setTimeout(r, 1000));
  const row = await p.evaluate(() => { const e = document.querySelector('#lineslist [data-i]'); const b = e.getBoundingClientRect(); const x = b.left + b.width / 2, y = b.top + Math.min(b.height / 2, 10); const h = document.elementFromPoint(x, y); return { x, y, hit: h && (h.className || h.tagName), inRow: e.contains(h), cls: e.className }; });
  console.log('row', JSON.stringify(row));
  await p.touchscreen.tap(row.x, row.y); await new Promise(r => setTimeout(r, 3000));
  const out = await p.evaluate(() => ({ log: window.__log, card: getComputedStyle(document.getElementById('card')).display, inspect: KY.modules['line-card'].api.inspect ? KY.modules['line-card'].api.inspect() : null, hist: history.length }));
  console.log(JSON.stringify(out, null, 1).slice(0, 4000)); console.log(log.join('\n'));
  await b.close();
})().catch(e => { console.error(e); process.exit(2); });
