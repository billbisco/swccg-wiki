import json,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1];product=sys.argv[2] if len(sys.argv)>2 else 'Reflections'
rows=json.loads((root/'psa-originals.json').read_bytes());labels=json.loads((root/(stage+'-labels.json')).read_bytes())
selected=[next(r for r in rows if r['product']==product and r['label']==label) for label in labels]
(root/(stage+'-source-manifest.json')).write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf8');print(len(selected),'originals selected for inspection')
