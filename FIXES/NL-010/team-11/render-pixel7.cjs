const {chromium,devices}=require('playwright');
const http=require('node:http'),fs=require('node:fs'),path=require('node:path');
const root=process.argv[2], out=process.argv[3];
const server=http.createServer((req,res)=>{let p=new URL(req.url,'http://x').pathname;const f=path.resolve(root,'.'+(p.endsWith('/')?p+'index.html':p));if(!f.startsWith(root)||!fs.existsSync(f)||!fs.statSync(f).isFile()){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));const base='http://127.0.0.1:'+server.address().port+'/';
const browser=await chromium.launch();const ctx=await browser.newContext({...devices['Pixel 7']});const page=await ctx.newPage();
const errors=[];page.on('pageerror',e=>errors.push('pageerror '+e.message));page.on('console',m=>{if(m.type()==='error')errors.push('console '+m.text());});
// external requests (fonts, active pages etc) are blocked: local render only
await page.route(/^https?:\/\/(?!127\.0\.0\.1)/,r=>r.abort());
await page.goto(base);await page.waitForSelector('#searchControls:not([hidden])',{state:'attached',timeout:20000}).catch(()=>{});
await page.waitForTimeout(1500);
const r={device:'Pixel 7',viewport:page.viewportSize()};
await page.locator('#kuiper > summary').tap();await page.waitForTimeout(400);
const card=page.locator('#kuiper-editions');
r.card_count=await card.count();
r.card_visible=await card.isVisible();
r.card_title=(await card.locator(':scope > summary').innerText()).replace(/\s+/g,' ');
await card.locator(':scope > summary').tap();await page.waitForTimeout(400);
r.card_open=await card.evaluate(e=>e.open);
r.launch_href=await card.locator(':scope > .inside > .launch').getAttribute('href');
r.launch_text=await card.locator(':scope > .inside > .launch').innerText();
r.description=await card.locator(':scope > .inside > p').first().innerText();
r.see_through_href=await page.locator('#see-through > .inside > .launch').getAttribute('href');
r.kuiper_children=await page.locator('#kuiper > .inside > details').evaluateAll(es=>es.map(e=>e.id));
r.doc_overflow_px=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
const bb=await card.boundingBox();r.card_box=bb;
await card.scrollIntoViewIfNeeded();await page.waitForTimeout(200);
await page.screenshot({path:out+'/pixel7-kuiper-editions-card.png',timeout:180000});
await page.locator('#catalogueArchive').evaluate(e=>{e.open=true;});
const search=page.locator('#catalogueSearch, input[type=search]').first();
if(await search.count()){await search.fill('kuiper editions');await page.waitForTimeout(400);r.search_rows=await page.locator('#catalogueRows tr:visible').evaluateAll(rs=>rs.map(x=>x.dataset.entityId));
 const row=page.locator('#catalogueRows tr[data-entity-id="kuiper-editions"]');if(await row.count()){await row.scrollIntoViewIfNeeded();await page.screenshot({path:out+'/pixel7-catalogue-row.png',timeout:180000});r.row_versions=await row.locator('.table-versions > summary').innerText();}}
r.errors=errors;
// no-JS fallback
const nojs=await browser.newContext({...devices['Pixel 7'],javaScriptEnabled:false});const p2=await nojs.newPage();await p2.route(/^https?:\/\/(?!127\.0\.0\.1)/,x=>x.abort());await p2.goto(base);
r.nojs_launch=await p2.locator('#kuiper-editions > .inside > .launch').getAttribute('href');
r.nojs_row=await p2.locator('#catalogueRows tr[data-entity-id="kuiper-editions"]').count();
console.log(JSON.stringify(r,null,2));await browser.close();server.close();})().catch(e=>{console.error(e);process.exit(1);});
