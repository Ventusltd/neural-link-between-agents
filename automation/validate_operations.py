"""Validate the compact coordination index without network or dependencies."""
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'STATUS.json').read_text(encoding='utf-8'))
if data['schema_version'] != 1:
    raise SystemExit('Unsupported schema_version')
stamp = datetime.fromisoformat(data['checked_at_utc'].replace('Z', '+00:00'))
if stamp.tzinfo is None:
    raise SystemExit('checked_at_utc requires timezone')
states = {'HISTORICAL_ACCEPTANCE', 'REPORTED_DRAFT', 'PENDING_OWNER_SCOPE',
          'IN_PROGRESS', 'BLOCKED', 'RETRYING', 'TESTED', 'REVIEWED', 'MERGED',
          'PUBLICLY_VERIFIED', 'COMPLETE'}
seen = set()
for item in data['work']:
    for field in ('id', 'owner', 'state', 'evidence', 'next_action'):
        if not isinstance(item.get(field), str) or not item[field].strip():
            raise SystemExit(f'Missing/non-text {field}')
    if item['id'] in seen or item['state'] not in states:
        raise SystemExit(f'Duplicate ID or invalid state: {item["id"]}')
    seen.add(item['id'])
for url in [data['channel']] + [item['evidence'] for item in data['work']]:
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname != 'github.com' or parsed.username or parsed.password:
        raise SystemExit('Evidence must use credential-free GitHub HTTPS links')
print(f'PASS: {len(seen)} unique work IDs; valid states, timestamp and evidence links')
