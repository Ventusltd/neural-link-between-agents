const { chromium, devices } = require('playwright'); const fs = require('fs'), crypto = require('crypto');
const ED = '/home/user/estate/kuiper-belt/editions/202611012135/', BASE = 'http://127.0.0.1:8410/editions/202611012135/';
const FILE = ED + 'modules/202611012143-kuiper-shell.js', buf = fs.readFileSync(FILE), sha = crypto.createHash('sha256').update(buf).digest('hex');
const man = JSON.parse(fs.readFileSync(ED + 'modules.json', 'utf8')); let rec = man.modules.find(m => m.id === 'kuiper-shell'); if (!rec) { rec = JSON.parse(fs.readFileSync('/tmp/nl010-opus/team-1/lead/shell-record.json', 'utf8')); man.modules.splice(1, 0, rec); } if (!man.order.includes('kuiper-shell')) man.order.splice(man.order.indexOf('hello') + 1, 0, 'kuiper-shell'); rec.sha256 = sha; rec.bytes = buf.length;
(async () => {
  const browser = await chromium.launch({ args: ['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  for (const dn of (process.argv[2] || 'Pixel 7,Galaxy S24').split(',')) {
    const page = await (await browser.newContext(devices[dn])).newPage(); const errs = [];
    page.on('pageerror', e => errs.push(e.message)); page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await page.route(BASE + 'modules.json', r => r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(man) }));
    await page.goto(BASE, { waitUntil: 'load' }); await page.waitForFunction(() => window.__KUIPER_EDITION__ && __KUIPER_EDITION__.done !== false && document.getElementById('kuiper-menu-bar'), null, { timeout: 60000 }).catch(() => {}); await page.waitForTimeout(6000);
    const tapSel = async sel => { if (!(await page.locator(sel).count())) return false; const b = await page.locator(sel).first().boundingBox(); if (!b) return false; await page.touchscreen.tap(b.x + b.width / 2, b.y + b.height / 2); return true; };
    const card = () => page.evaluate(() => { const c = document.getElementById('card'); return getComputedStyle(c).display !== 'none' && c.getBoundingClientRect().height > 0; });
    const st = () => page.evaluate(() => ({ open: window.__KUIPER_SHELL__ ? __KUIPER_SHELL__.inspect().open : (KY.modules['kuiper-shell'] && KY.modules['kuiper-shell'].inspect().open), hs: JSON.stringify(history.state), hl: history.length }));
    const out = { admitted: await page.evaluate(() => window.__KUIPER_EDITION__ && __KUIPER_EDITION__.admitted.map(a => a.id).join(',') + ' | refused ' + JSON.stringify(__KUIPER_EDITION__.refused)) };
    // 1 VIEW > next verified line
    await tapSel('#kmb-title-view'); await page.waitForTimeout(500); await tapSel('#kmb-panel-view [data-k="e"]'); await page.waitForTimeout(2500);
    out.nextCard = await card(); out.afterNext = await st();
    // 2 card details
    const det = await tapSel('#card .lc-t, #card .ct'); await page.waitForTimeout(1500); out.details = det; out.detailsCard = await card();
    // 3 WAFER > pick a row
    await tapSel('#kmb-title-wafer'); await page.waitForTimeout(800);
    const row = await tapSel('#kmb-panel-wafer #lineslist [data-i]'); await page.waitForTimeout(2500);
    out.pickRow = row; out.pickCard = await card(); out.afterPick = await st();
    const det2 = await tapSel('#card .lc-t, #card .ct'); await page.waitForTimeout(1500); out.details2Card = await card();
    // 4 back gesture closes the card and stays
    await page.goBack({ waitUntil: 'commit', timeout: 5000 }).catch(e => out.backErr = e.message.split('\n')[0]); await page.waitForTimeout(1200); out.backCard = await card(); out.url = page.url().replace(BASE, '.../'); out.afterBack = await st();
    // 5 open a panel while... ABOUT then back closes panel only
    await tapSel('#kmb-title-about'); await page.waitForTimeout(500); await page.goBack({ waitUntil: 'commit', timeout: 5000 }).catch(e => out.backErr2 = e.message.split('\n')[0]); await page.waitForTimeout(1000); out.aboutAfterBack = await st(); out.url2 = page.url().replace(BASE, '.../');
    out.errs = errs;
    console.log(dn, JSON.stringify(out));
    await page.context().close();
  }
  await browser.close();
})();
