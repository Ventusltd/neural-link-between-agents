import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const [,, release, outdir, port = '8731'] = process.argv;
const base = `http://127.0.0.1:${port}/uk_renewables_pipeline/${release}/`;
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true, args: ['--proxy-server=https=127.0.0.1:9', '--proxy-bypass-list=<-loopback>'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, acceptDownloads: true });
const page = await ctx.newPage();
const errs = []; page.on('pageerror', e => errs.push(e.message));
const ready = async () => page.waitForFunction(() => document.querySelector('#tbody')?.dataset.complete === 'true' && !/Loading/.test(document.querySelector('#resultsMeta').textContent), null, { timeout: 60000 });
const meta = () => page.evaluate(() => ({ r: document.querySelector('#resultsMeta').textContent, f: document.querySelector('#resultsMeta').dataset.filteredCount, rows: document.querySelectorAll('#tbody tr').length, pager: document.querySelector('#projectPager')?.textContent.trim(), url: location.search }));
const out = {};
await page.goto(base); await ready();
out.initial = await meta();
out.tech = {};
for (const t of ['solar', 'bess', 'wind_onshore', 'wind_offshore', 'interconnector', 'all']) { await page.click(`#tech [data-technology="${t}"]`); await page.waitForTimeout(300); out.tech[t] = await meta(); }
out.status = {};
for (const s of ['Operational', 'Under Construction', 'Awaiting Construction', 'Application Submitted', 'All']) { await page.click(`#status [data-official-status="${s}"]`); await page.waitForTimeout(300); out.status[s] = await meta(); }
out.search = {};
for (const q of ['18561', 'Salters Lane', 'Berwick Bank', 'GG2050-REPD-19459', 'Forsinain', 'zzznotfound']) { await page.fill('#search', q); await page.waitForTimeout(700); out.search[q] = await meta(); out.search[q].first = await page.evaluate(() => document.querySelector('#tbody tr .site')?.childNodes[0]?.textContent || null); }
await page.click('#clearFilters'); await page.waitForTimeout(300);
// pagination: go to page 2 and to last page via repeated next? use dataset: click next once, then jump by evaluating clicks
await page.click('#projectPager [data-page-step="1"]'); await page.waitForTimeout(200); out.page2 = await meta();
const pages = Number(await page.evaluate(() => document.querySelector('#projectPager').dataset.pages));
for (let i = 2; i < pages; i++) await page.evaluate(() => document.querySelector('#projectPager [data-page-step="1"]').click());
await page.waitForTimeout(300); out.lastPage = await meta();
await page.click('#clearFilters'); await page.waitForTimeout(300);
// URL hydration
await page.goto(base + '?status=No%20Application%20Made'); await ready(); out.urlNoAppMade = await meta();
await page.goto(base + '?technology=bess&status=Under%20Construction'); await ready(); out.urlBessUC = await meta();
// county
await page.goto(base); await ready();
await page.selectOption('#county', { index: 5 }); await page.waitForTimeout(300); out.county = { value: await page.$eval('#county', s => s.value), ...(await meta()) };
await page.click('#clearFilters'); await page.waitForTimeout(300);
// exports
async function grab(label, sel) { const [d] = await Promise.all([page.waitForEvent('download'), page.click(sel)]); const p = `${outdir}/${release}_${label}.csv`; await d.saveAs(p); return { file: p, name: d.suggestedFilename(), exportMeta: await page.$eval('#exportMeta', e => e.textContent) }; }
out.exportAll = await grab('export_all', '#exportInline');
await page.click('#status [data-official-status="Under Construction"]'); await page.waitForTimeout(300);
out.exportUC = await grab('export_under_construction', '#export');
out.pageErrors = errs;
fs.writeFileSync(`${outdir}/${release}_interact.json`, JSON.stringify(out, null, 1));
console.log(JSON.stringify(out, null, 1));
await browser.close();
