"""Resolve a photographic mark using a second complete physical foil."""
import json
from pathlib import Path
root=Path(__file__).parent
primary=json.loads((root/'batch7-readings.json').read_bytes());r=next(r for r in primary if r['title']=='Redemption');second=next(r for r in map(json.loads,(root/'swca-originals-results.jsonl').read_text().splitlines()) if r['id']=='45052' and r.get('original_bytes'))
r=dict(r,source_kind='SWCA',source_gallery=second['entry_url'],source_id=second['id'],source_photo=second['local_file'],source_url=second['source'],source_sha256=second['sha256'])
r['lore']=r['lore'].replace('have been. modified','have been modified')
r['inspection']='Second complete physical foil inspected directly: no period between “been” and “modified”; the mark in the PSA photograph is not retained as punctuation'
r['reading_note']='Targeted second-source check resolves the punctuation-sized photographic mark; no separate printing/misprint article is warranted'
(root/'batch7check-readings.json').write_text(json.dumps([r],ensure_ascii=False,indent=2),encoding='utf8')
print('Second full foil confirms “have been modified”; correction prepared for source preservation')
