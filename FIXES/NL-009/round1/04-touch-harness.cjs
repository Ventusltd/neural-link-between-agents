// FABLE-04 touch harness. node touch.cjs <before|after> [device]
const { chromium, devices } = require('playwright');
const fs = require('fs');
const S = __dirname;
const mode = process.argv[2] || 'before', devName = process.argv[3] || 'Pixel 7';
const htmlPath = mode === 'before' ? S + '/index.orig.html' : S + '/index.html';
const HOOK = `
window.__k = { get:()=>({cx,cy,zoom,moved,openPanel,card:card.style.display,cardOpen:card.classList.contains('open'),pts:pts.size,edSel,edN:edPlaced.length,drag:!!drag,pinch:!!pinch,W:innerWidth,H:innerHeight}),
  set:(o)=>{ if ('cx' in o) cx=o.cx; if ('cy' in o) cy=o.cy; if ('zoom' in o) zoom=o.zoom; tween=null; atHome=false; dirty=true; draw(); },
  spark:(i)=>({x:edPlaced[i].x,y:edPlaced[i].y,s:edScreen(edPlaced[i])}), toWorld, key:(k)=>dispatchEvent(new KeyboardEvent('keydown',{key:k})), draw:()=>{dirty=true;draw();} };
window.edCard = (i)=>edCard(i); Object.defineProperty(window,'edSel',{set:v=>{edSel=v;},get:()=>edSel}); Object.defineProperty(window,'litRepo',{set:v=>{litRepo=v;},get:()=>litRepo});
window.__ev = { cancel:0, ctx:0, ctxPrevented:0, ups:[], clicks:[] };
addEventListener('pointercancel', ()=>__ev.cancel++, true);
addEventListener('contextmenu', e=>{ __ev.ctx++; setTimeout(()=>{ if (e.defaultPrevented) __ev.ctxPrevented++; },0); }, true);
addEventListener('pointerup', e=>__ev.ups.push([performance.now(), e.target.id||e.target.tagName]), true);
addEventListener('click', e=>__ev.clicks.push([performance.now(), e.target.id||e.target.tagName]), true);
requestAnimationFrame(frame);
</script>`;
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const html = fs.readFileSync(htmlPath, 'utf8').replace('requestAnimationFrame(frame);\n</script>', HOOK);
  if (!html.includes('window.__k')) throw new Error('hook not injected');
  const browser = await chromium.launch({ args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
  const ctx = await browser.newContext({ ...devices[devName] });
  const page = await ctx.newPage();
  const errors = []; page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); }); page.on('pageerror', e => errors.push(String(e)));
  await page.route('**/editions/202611012027/', r => r.fulfill({ status:200, contentType:'text/html', body:html }));
  const cdp = await ctx.newCDPSession(page);
  const touch = (type, pts) => cdp.send('Input.dispatchTouchEvent', { type, touchPoints: pts.map((p, i) => ({ x:p[0], y:p[1], id:i, radiusX:8, radiusY:8 })) });
  const touchT = (type, pts, t) => cdp.send('Input.dispatchTouchEvent', { type, timestamp:t, touchPoints: pts.map((p, i) => ({ x:p[0], y:p[1], id:i, radiusX:8, radiusY:8 })) });
  const seq = async (steps) => { const t0 = Date.now()/1000; for (const [type, pts, dt] of steps) await touchT(type, pts, t0 + dt/1000); };
  const R = { mode, device:devName, results:{} };
  const rec = (k, v) => { R.results[k] = v; console.log(k, JSON.stringify(v)); };
  await page.goto('about:blank'); await page.goto('http://127.0.0.1:8104/editions/202611012027/');
  await page.waitForFunction(() => window.__k && window.__k.get().edN > 0, null, { timeout:60000 }); await sleep(7000);
  const G = () => page.evaluate(() => window.__k.get());
  const settle = async () => { const fr = () => page.evaluate(() => new Promise(r => requestAnimationFrame(t0 => requestAnimationFrame(t1 => r(t1 - t0)))));
    for (let i = 0; i < 60; i++) { if (await fr() < 120 && await fr() < 120) return i; } return -1; };
  const VV = () => page.evaluate(() => ({ scale:visualViewport.scale, pageTop:visualViewport.pageTop, offsetTop:visualViewport.offsetTop, scrollY:scrollY, scrollX:scrollX }));
  const st = await G(); const W = st.W, H = st.H;
  rec('viewport', { W, H, meta: await page.evaluate(() => document.querySelector('meta[name=viewport]').content) });
  rec('touch_action', await page.evaluate(() => { const g = s => { const el = document.querySelector(s); return el ? getComputedStyle(el).touchAction + ' | user-select=' + getComputedStyle(el).userSelect : 'n/a'; };
    return { canvas:g('#c'), overlay:g('#o'), bar:g('#bar'), barBtn:g('#bar .gm-title'), lines:g('#lines'), top:g('#top'), card:g('#card'), html:g('html') }; }));
  // ---- T1 one finger drag
  { const a = await G(), v0 = await VV(); const x0 = Math.round(W*0.5), y0 = Math.round(H*0.55);
    await touch('touchStart', [[x0, y0]]); for (let i = 1; i <= 10; i++) { await touch('touchMove', [[x0 + 10*i, y0 + 6*i]]); await sleep(16); } await touch('touchEnd', []); await sleep(300);
    const b = await G(), v1 = await VV();
    rec('T1_drag', { dcx_px: +((a.cx - b.cx)*a.zoom).toFixed(2), dcy_px: +((b.cy - a.cy)*a.zoom).toFixed(2), expected:[100, 60], cancel: await page.evaluate(() => __ev.cancel), vv_before:v0, vv_after:v1, card_after:b.card, pts:b.pts }); }
  // ---- T2 pinch on canvas
  { const a = await G(); const cxs = Math.round(W*0.5), cys = Math.round(H*0.55); const w0 = await page.evaluate(([x,y]) => window.__k.toWorld(x,y), [cxs, cys]);
    await touch('touchStart', [[cxs-50, cys]]); await touch('touchStart', [[cxs-50, cys],[cxs+50, cys]]);
    for (let i = 1; i <= 10; i++) { await touch('touchMove', [[cxs-50-5*i, cys],[cxs+50+5*i, cys]]); await sleep(16); }
    await touch('touchEnd', [[cxs+100, cys]]); await touch('touchEnd', []); await sleep(300);
    const b = await G(); const w1 = await page.evaluate(([x,y]) => window.__k.toWorld(x,y), [cxs, cys]);
    rec('T2_pinch_canvas', { zoom_ratio:+(b.zoom/a.zoom).toFixed(3), expected:2, centre_world_drift:+Math.hypot(w1[0]-w0[0], w1[1]-w0[1]).toFixed(6), vv: await VV(), pts:b.pts, pinch:b.pinch }); }
  // ---- T2b pinch on the bar and on an open panel (page zoom?)
  { const br = await page.$eval('#bar', e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; });
    const y = Math.round(br[1] + br[3]/2), x = Math.round(W*0.5);
    await touch('touchStart', [[x-40, y]]); await touch('touchStart', [[x-40, y],[x+40, y]]);
    for (let i = 1; i <= 10; i++) { await touch('touchMove', [[x-40-8*i, y],[x+40+8*i, y]]); await sleep(16); }
    await touch('touchEnd', []); await sleep(400);
    rec('T2b_pinch_bar', { vv: await VV(), state:(await G()).zoom });
    await page.evaluate(() => { if (visualViewport.scale !== 1) {} });
    await page.evaluate(() => window.__k.key('Escape'));
    await page.$eval('#bar [data-panel=lines]', b => b.click()); await sleep(300);
    const lr = await page.$eval('#lines', e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; });
    const py = Math.round(lr[1] + Math.min(lr[3]/2, 200)), px = Math.round(W*0.5);
    await touch('touchStart', [[px-40, py]]); await touch('touchStart', [[px-40, py],[px+40, py]]);
    for (let i = 1; i <= 10; i++) { await touch('touchMove', [[px-40-8*i, py],[px+40+8*i, py]]); await sleep(16); }
    await touch('touchEnd', []); await sleep(400);
    rec('T2c_pinch_lines_panel', { lines_rect:lr.map(Math.round), vv: await VV(), openPanel:(await G()).openPanel });
    await page.screenshot({ path:S + '/img/' + mode + '-T2c.png', scale:'css', timeout:180000 });
    await cdp.send('Emulation.setPageScaleFactor', { pageScaleFactor:1 }).catch(()=>{});
    await page.evaluate(() => window.__k.key('Escape')); }
  // ---- T3 tap discrimination
  { const clear = async () => { await page.evaluate(() => { card.style.display = 'none'; __k.key('Backspace'); }); await sleep(1500); await settle(); };
    await page.evaluate(() => { __ev.t = []; addEventListener('pointerdown', e => __ev.t.push(['d', e.timeStamp]), true); addEventListener('pointerup', e => __ev.t.push(['u', e.timeStamp]), true); });
    const dtLast = () => page.evaluate(() => { const t = __ev.t; const u = t.filter(v => v[0] === 'u').pop(), d = t.filter(v => v[0] === 'd').pop(); return u && d ? +(u[1] - d[1]).toFixed(1) : null; });
    await clear();
    const x = Math.round(W*0.5), y = Math.round(H*0.5);
    await seq([['touchStart', [[x, y]], 0], ['touchEnd', [], 60]]); await sleep(200);
    const clean = (await G()).card, cleanDt = await dtLast();
    await clear();
    await seq([['touchStart', [[x, y]], 0], ['touchEnd', [], 900]]); await sleep(200);
    const held = (await G()).card, heldDt = await dtLast();
    await clear();
    await seq([['touchStart', [[x, y]], 0], ['touchMove', [[x+3, y+2]], 20], ['touchMove', [[x+5, y+5]], 40], ['touchMove', [[x+6, y+6]], 60], ['touchEnd', [], 80]]); await sleep(200);
    const jitter = await G(); const jitterDt = await dtLast();
    await clear();
    await seq([['touchStart', [[x, y]], 0], ...[1,2,3,4,5,6].map(i => ['touchMove', [[x+5*i, y]], 16*i]), ['touchEnd', [], 120]]); await sleep(200);
    const drag30 = await G();
    rec('T3_tap_vs_drag', { clean_tap_opens_card: clean === 'block', clean_down_to_up_ms:cleanDt, held_900ms_opens_card: held === 'block', held_down_to_up_ms:heldDt, jittered_tap_6px_opens_card: jitter.card === 'block', jitter_moved:+jitter.moved.toFixed(2), jitter_down_to_up_ms:jitterDt, drag_30px_opens_card: drag30.card === 'block', drag_moved:+drag30.moved.toFixed(2) }); }
  // ---- T4 double tap: page zoom and click delay
  { await page.evaluate(() => { card.style.display = 'none'; }); const x = Math.round(W*0.5), y = Math.round(H*0.6);
    await touch('touchStart', [[x, y]]); await sleep(50); await touch('touchEnd', []); await sleep(120); await touch('touchStart', [[x, y]]); await sleep(50); await touch('touchEnd', []); await sleep(600);
    const vvc = await VV();
    await page.$eval('#bar [data-panel=top]', b => b.click()); await sleep(200);
    const tr = await page.$eval('#top', e => { const r = e.getBoundingClientRect(); return [r.left + r.width/2, r.top + Math.min(r.height/2, 80)]; });
    await touch('touchStart', [[tr[0], tr[1]]]); await sleep(50); await touch('touchEnd', []); await sleep(120); await touch('touchStart', [[tr[0], tr[1]]]); await sleep(50); await touch('touchEnd', []); await sleep(600);
    const vvp = await VV();
    await cdp.send('Emulation.setPageScaleFactor', { pageScaleFactor:1 }).catch(()=>{});
    await page.evaluate(() => { __ev.ups = []; __ev.clicks = []; });
    const b = await page.$('#bar [data-panel=hud]'); const bb = await b.boundingBox();
    await page.touchscreen.tap(bb.x + bb.width/2, bb.y + bb.height/2); await sleep(500);
    const lat = await page.evaluate(() => ({ ups:__ev.ups, clicks:__ev.clicks, delay_ms: __ev.clicks.length && __ev.ups.length ? +(__ev.clicks[0][0] - __ev.ups[0][0]).toFixed(1) : null }));
    rec('T4_double_tap', { vv_after_double_tap_canvas:vvc, vv_after_double_tap_panel:vvp, pointerup_to_click_ms:lat.delay_ms, targets:{ up:lat.ups[0], click:lat.clicks[0] }, openPanel:(await G()).openPanel });
    await page.evaluate(() => window.__k.key('Escape')); }
  // ---- T5 a tap on the bar / the card's x / the wafer-with-panel-open reaching the canvas
  { const put = async (i, sx, sy) => page.evaluate(([i, sx, sy]) => { const b = __k.spark(i), g = __k.get(); __k.set({ zoom:14, cx: b.x - (sx - g.W/2)/14, cy: b.y + (sy - g.H/2)/14 }); return __k.spark(i).s; }, [i, sx, sy]);
    await page.evaluate(() => { card.style.display = 'none'; edSel = -1; });
    const bb = await (await page.$('#bar [data-panel=lines]')).boundingBox(); const bx = bb.x + bb.width/2, by = bb.y + bb.height/2;
    const s = await put(5, bx, by); await sleep(300); await settle();
    await page.touchscreen.tap(bx, by); await sleep(1500);
    const g1 = await G();
    rec('T5a_tap_bar_button_over_spark', { spark_screen:s.map(v => +v.toFixed(1)), button_centre:[+bx.toFixed(1), +by.toFixed(1)], panel_opened:g1.openPanel, card_opened_by_spark: g1.card === 'block', edSel:g1.edSel, verdict: g1.edSel === 5 ? 'BUG: bar tap reached the canvas' : 'ok' });
    await page.screenshot({ path:S + '/img/' + mode + '-T5a.png', scale:'css', timeout:180000 });
    if (g1.openPanel) await page.evaluate(() => window.__k.key('Escape'));
    // the card's x
    await page.evaluate(() => { card.style.display = 'none'; edSel = -1; }); await page.evaluate(() => { edCard(3); }); await sleep(300);
    const xb = await (await page.$('#card .cx')).boundingBox(); const xx = xb.x + xb.width/2, xy = xb.y + xb.height/2;
    const s2 = await put(7, xx, xy); await sleep(300); await settle();
    await page.touchscreen.tap(xx, xy); await sleep(1500);
    const g2 = await G();
    rec('T5b_tap_card_close_over_spark', { spark_screen:s2.map(v => +v.toFixed(1)), x_centre:[+xx.toFixed(1), +xy.toFixed(1)], card_after:g2.card, edSel_after:g2.edSel, verdict: g2.card === 'block' ? 'BUG: x close reopened another line' : 'ok' });
    await page.screenshot({ path:S + '/img/' + mode + '-T5b.png', scale:'css', timeout:180000 });
    // details toggle on the card: does the card survive?
    await page.evaluate(() => { card.style.display = 'none'; edSel = -1; edCard(9); }); await sleep(300);
    const db = await (await page.$('#card .ct')).boundingBox(); await page.touchscreen.tap(db.x + db.width/2, db.y + db.height/2); await sleep(400);
    const g3 = await G();
    rec('T5c_tap_details', { card_after:g3.card, details_open:g3.cardOpen, verdict: g3.card === 'block' && g3.cardOpen ? 'ok' : 'BUG: details tap closed the card' });
    // tap on the card body
    await page.evaluate(() => { card.style.display = 'none'; edSel = -1; edCard(9); }); await sleep(300);
    const cb = await (await page.$('#card .cq')).boundingBox(); await page.touchscreen.tap(cb.x + 20, cb.y + 8); await sleep(400);
    rec('T5d_tap_card_body', { card_after:(await G()).card });
    // tap on the card's own padding (target is #card itself)
    await page.evaluate(() => { card.style.display = 'none'; edSel = -1; edCard(9); }); await sleep(300);
    const cr = await (await page.$('#card')).boundingBox(); await page.touchscreen.tap(cr.x + cr.width - 12, cr.y + cr.height - 6); await sleep(400);
    rec('T5f_tap_card_padding', { card_after:(await G()).card, verdict:(await G()).card === 'block' ? 'ok' : 'BUG: tap on the card padding closed the card' });
    // wafer tap with a panel open: closes the panel; does it also act on the wafer?
    await page.evaluate(() => { card.style.display = 'none'; edSel = -1; litRepo = -1; }); await page.$eval('#bar [data-panel=hud]', b => b.click()); await sleep(300);
    await page.touchscreen.tap(Math.round(W*0.5), Math.round(H*0.75)); await sleep(500);
    const g5 = await G();
    rec('T5e_tap_wafer_with_panel_open', { panel_after:g5.openPanel, card_after:g5.card, verdict: g5.openPanel ? 'BUG: panel stayed open' : (g5.card === 'block' ? 'tap also acted on the wafer (card opened)' : 'ok: dismiss only') }); }
  // ---- T6 back gesture and Escape
  { await page.evaluate(() => { card.style.display = 'none'; }); const len0 = await page.evaluate(() => history.length);
    await page.$eval('#bar [data-panel=lines]', b => b.click()); await sleep(300);
    const len1 = await page.evaluate(() => history.length);
    await page.goBack({ waitUntil:'commit' }).catch(e => rec('T6_goback_error', String(e))); await sleep(800);
    const url = page.url(); const alive = await page.evaluate(() => !!window.__k).catch(() => false);
    const after = alive ? await G() : null;
    rec('T6a_back_with_panel_open', { history_before:len0, history_after_open:len1, url_after_back:url, page_alive:alive, openPanel_after:after && after.openPanel, verdict: alive && !after.openPanel ? 'ok: back closed the panel' : 'BUG: back left the page' });
    if (!alive) { await page.goForward({ waitUntil:'commit' }).catch(()=>{}); await page.waitForFunction(() => window.__k && window.__k.get().edN > 0, null, { timeout:60000 }); await sleep(6000); }
    // back with the card open
    await page.evaluate(() => { edCard(2); }); await sleep(200); await page.goBack({ waitUntil:'commit' }).catch(()=>{}); await sleep(800);
    const alive2 = await page.evaluate(() => !!window.__k).catch(() => false); const g6 = alive2 ? await G() : null;
    rec('T6b_back_with_card_open', { page_alive:alive2, card_after:g6 && g6.card, verdict: alive2 && g6.card !== 'block' ? 'ok' : 'BUG' });
    if (!alive2) { await page.goForward({ waitUntil:'commit' }).catch(()=>{}); await page.waitForFunction(() => window.__k && window.__k.get().edN > 0, null, { timeout:60000 }); await sleep(6000); }
    // back with nothing open leaves the page (must still work)
    const g6c0 = await G(); await page.goBack({ waitUntil:'commit' }).catch(()=>{}); await sleep(800); const alive3 = await page.evaluate(() => !!window.__k).catch(() => false);
    rec('T6c_back_with_nothing_open', { openPanel:g6c0.openPanel, card:g6c0.card, page_left:!alive3, verdict: !alive3 ? 'ok: back leaves the page' : 'BUG: back trapped' });
    if (!alive3) { await page.goForward({ waitUntil:'commit' }).catch(()=>{}); await page.waitForFunction(() => window.__k && window.__k.get().edN > 0, null, { timeout:60000 }); await sleep(6000); }
    await page.evaluate(() => { edCard(4); }); await sleep(200); await page.keyboard.press('Escape'); await sleep(200);
    const g7 = await G(); rec('T6d_escape_with_card_open', { card_after:g7.card, verdict: g7.card === 'block' ? 'BUG: Escape does not close the card' : 'ok' });
    await page.evaluate(() => { card.style.display = 'none'; }); await page.$eval('#bar [data-panel=foot]', b => b.click()); await sleep(200); await page.keyboard.press('Escape'); await sleep(200);
    rec('T6e_escape_with_panel_open', { openPanel_after:(await G()).openPanel }); }
  // ---- T7 long press
  { await page.evaluate(() => { card.style.display = 'none'; __ev.ctx = 0; __ev.ctxPrevented = 0; }); await settle();
    const x = Math.round(W*0.5), y = Math.round(H*0.65);
    await touch('touchStart', [[x, y]]); await sleep(900); await touch('touchEnd', []); await sleep(300);
    const c1 = await page.evaluate(() => ({ ctx:__ev.ctx, prevented:__ev.ctxPrevented, sel:getSelection().toString().length, card:__k.get().card }));
    const bb = await (await page.$('#bar [data-panel=top]')).boundingBox(); await page.evaluate(() => { __ev.ctx = 0; __ev.ctxPrevented = 0; });
    await touch('touchStart', [[bb.x + bb.width/2, bb.y + bb.height/2]]); await sleep(900); await touch('touchEnd', []); await sleep(300);
    const c2 = await page.evaluate(() => ({ ctx:__ev.ctx, prevented:__ev.ctxPrevented, sel:getSelection().toString().length, openPanel:__k.get().openPanel }));
    const synth = await page.evaluate(() => { const ev = new MouseEvent('contextmenu', { bubbles:true, cancelable:true, clientX:200, clientY:500 }); return { canvas_contextmenu_prevented: !document.getElementById('c').dispatchEvent(ev),
      bar_contextmenu_prevented: !document.querySelector('#bar .gm-title').dispatchEvent(new MouseEvent('contextmenu', { bubbles:true, cancelable:true })) }; });
    rec('T7_long_press', { canvas:c1, bar_button:c2, synthetic:synth }); }
  rec('console_errors', errors);
  await page.evaluate(() => { card.style.display = 'none'; if (__k.get().openPanel) __k.key('Escape'); });
  fs.writeFileSync(S + '/results-' + mode + '-' + devName.replace(/\s+/g, '_') + '.json', JSON.stringify(R, null, 1));
  await browser.close();
})().catch(e => { console.error('HARNESS ERROR', e); process.exit(1); });
