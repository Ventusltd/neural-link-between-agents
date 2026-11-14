import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const outdir = process.argv[2];
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true, args: ['--proxy-server=https=127.0.0.1:9', '--proxy-bypass-list=<-loopback>'] });
for (const rel of ['202609082224', '202611132345']) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto(`http://127.0.0.1:8731/uk_renewables_pipeline/${rel}/`);
  await page.waitForFunction(() => document.querySelector('#tbody')?.dataset.complete === 'true', null, { timeout: 60000 });
  await page.waitForTimeout(1500);
  const t = await page.evaluate(() => {
    const clone = document.body.cloneNode(true);
    clone.querySelector('#tbody')?.remove(); clone.querySelector('#stories')?.remove();
    clone.querySelectorAll('select#county option').forEach(o => o.remove());
    const chrome = clone.innerText;
    const rows = [...document.querySelectorAll('#tbody tr')].map(tr => [...tr.children].map((td,i)=> i===0 ? td.childNodes[0].textContent : td.innerText.replace(/\s+/g,' ')).join(' | '));
    const counties = [...document.querySelectorAll('#county option')].map(o => o.value);
    return { chrome, rows, counties };
  });
  fs.writeFileSync(`${outdir}/${rel}_chrome.txt`, t.chrome);
  fs.writeFileSync(`${outdir}/${rel}_page1_rows.txt`, t.rows.join('\n') + '\n');
  fs.writeFileSync(`${outdir}/${rel}_counties.txt`, t.counties.join('\n') + '\n');
  await page.close();
}
await browser.close();
