import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const [,, release, outdir] = process.argv;
const url = `http://127.0.0.1:8731/uk_renewables_pipeline/${release}/`;
const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY, bypass: '<-loopback>' } : undefined;
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true, args: ['--ignore-certificate-errors', `--proxy-server=https=${process.env.HTTPS_PROXY.replace(/^https?:\/\//,'')}`, '--proxy-bypass-list=<-loopback>'] });
const result = {};
for (const [name, vp, mobile] of [['desktop', { width: 1440, height: 900 }, false], ['mobile', { width: 390, height: 844 }, true]]) {
  const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile, ignoreHTTPSErrors: true, acceptDownloads: true });
  const page = await ctx.newPage();
  const consoleMsgs = [], failed = [], bad = [], reqs = [];
  page.on('console', m => { if (['error', 'warning'].includes(m.type())) consoleMsgs.push(`${m.type()}: ${m.text()}`); });
  page.on('pageerror', e => consoleMsgs.push(`pageerror: ${e.message}`));
  page.on('requestfailed', r => failed.push(`${r.url()} :: ${r.failure()?.errorText}`));
  page.on('response', r => { reqs.push(`${r.status()} ${r.url()}`); if (r.status() >= 400) bad.push(`${r.status()} ${r.url()}`); });
  const t0 = Date.now();
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  try { await page.waitForFunction(() => /\d/.test(document.querySelector('#resultsMeta')?.textContent || '') && !/Loading/i.test(document.querySelector('#resultsMeta').textContent), null, { timeout: 60000 }); } catch (e) { consoleMsgs.push('TIMEOUT waiting resultsMeta'); }
  await page.waitForTimeout(4000);
  const info = await page.evaluate(() => {
    const t = s => document.querySelector(s)?.textContent.trim().replace(/\s+/g, ' ');
    return { title: document.title, h1: t('h1'), status: t('.header .status'), meta: t('.meta strong'), metaSpan: t('.meta span'),
      releaseMeta: t('#releaseMeta'), newsMeta: t('#newsMeta'), resultsMeta: t('#resultsMeta'), v1: t('#v1'), v2: t('#v2'), v3: t('#v3'),
      rows: document.querySelectorAll('#tbody tr').length, stories: document.querySelectorAll('#stories > *').length,
      firstRow: t('#tbody tr'), mapNav: document.querySelector('#mapAtlasNav')?.href,
      statusButtons: [...document.querySelectorAll('#status button')].map(b => b.textContent.trim()),
      counties: document.querySelectorAll('#county option').length,
      scrollW: document.documentElement.scrollWidth, clientW: document.documentElement.clientWidth };
  });
  info.loadMs = Date.now() - t0;
  await page.screenshot({ path: `${outdir}/${release}_${name}_top.png` });
  await page.screenshot({ path: `${outdir}/${release}_${name}_full.png`, fullPage: false, clip: undefined });
  await page.evaluate(()=>document.querySelector('#tbody')?.scrollIntoView()); await page.waitForTimeout(500);
  await page.screenshot({ path: `${outdir}/${release}_${name}_table.png` });
  result[name] = { info, console: consoleMsgs, failed, bad, requestCount: reqs.length, requests: reqs };
  await ctx.close();
}
await browser.close();
fs.writeFileSync(`${outdir}/${release}_load.json`, JSON.stringify(result, null, 1));
for (const k of Object.keys(result)) { const r = result[k]; console.log(k, JSON.stringify(r.info), '\nconsole:', r.console.length, r.console.slice(0, 8), '\nfailed:', r.failed, '\nbad:', r.bad); }
