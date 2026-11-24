import { createHash } from 'node:crypto';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { createPreviewServer } from './host/tools/journey/serve.mjs';
import { rerootForPreview } from './host/tools/release/lib.mjs';

const root = new URL('./host/', import.meta.url);
const preview = new URL('atlas/v/agent33-satnav-demo/', root);
const source = await readFile(new URL('./satnav-handoff.js', import.meta.url));
const digest = createHash('sha256').update(source).digest('hex');
const composition = JSON.parse(await readFile(new URL('atlas/current.json', root), 'utf8'));
const id = 'agent33-satnav-handoff-demo';
if (composition.generation !== '202611222343' || composition.cartridge_order.at(-1) !== 'vicinity-controls-rescue') {
  throw new Error('The demo expects the pinned GridAtlas V9.197 composition.');
}
composition.cartridge_order.push(id);
composition.cartridges.push({ id, type: 'script', slot: 'after-cartridge', after: 'vicinity-controls-rescue', path: `./modules/${id}.js`, sha256: digest, preview_only: true });
await mkdir(preview, { recursive: true });
await writeFile(new URL(`atlas/modules/${id}.js`, root), source);
await writeFile(new URL('index.html', preview), await readFile(new URL('atlas/index.html', root)));
await writeFile(new URL('current.json', preview), rerootForPreview(JSON.stringify(composition, null, 2)) + '\n');

console.log(`Demo cartridge SHA256 ${digest}`);
if (process.argv[2] !== '--stage-only') {
  const port = Number(process.argv[2] ?? 8767);
  const server = await createPreviewServer(port);
  const serve = server.listeners('request')[0];
  server.removeListener('request', serve);
  server.on('request', (request, response) => {
    if (request.url.startsWith('/gridatlas/')) request.url = request.url.slice('/gridatlas'.length);
    serve(request, response);
  });
  console.log(`Demo http://127.0.0.1:${server.address().port}/gridatlas/atlas/v/agent33-satnav-demo/`);
}
