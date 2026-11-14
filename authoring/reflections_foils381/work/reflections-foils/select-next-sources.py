"""Select uncovered collected originals, retaining immutable source-ledger names."""
import json,sys
from pathlib import Path
root=Path(__file__).parent;stage,product,kind=sys.argv[1:4];count=int(sys.argv[4]) if len(sys.argv)>4 else 10
manifest=json.loads((root/'manifest.json').read_bytes());by={r['proposed_article']:r for r in manifest};renames={r['before']:r['after'] for r in json.loads((root/'unpublished-title-normalizations.json').read_bytes())}
covered={r['article'] for f in root.glob('*-readings.json') for r in json.loads(f.read_bytes())}
raw=json.loads((root/'psa-originals.json').read_bytes()) if kind=='PSA' else list(map(json.loads,(root/'swca-originals-results.jsonl').read_text().splitlines()));selected=[]
for source in raw:
    article=renames.get(source.get('article'),source.get('article'));m=by.get(article)
    if not m or m['product']!=product or article in covered:continue
    selected.append(dict(source,article=article,source_ledger_article=source.get('article'),product=product,label=m['label'],side=m['side'],alternate_image=m.get('alternate_image',False)))
print(len(selected),'unread originals in selected source collection')
selected=selected[:count];(root/(stage+'-source-manifest.json')).write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf8');print([r['label'] for r in selected])
