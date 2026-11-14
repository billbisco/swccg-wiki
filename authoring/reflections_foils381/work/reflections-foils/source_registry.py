"""Source provenance helpers; never infer card identity from captions."""
import json
from pathlib import Path
ROOT=Path(__file__).parent
def provenance(row):
    if row.get('source_kind')=='SWCA':return dict(url=row['source_gallery'],credit='Duncan Jenkins, Star Wars Collectors Archive',kind='SWCA',photo_id=row['source_id'])
    key=Path(row['source_gallery']).stem
    requests=[]
    for name in ['source-probe.json','gallery-requests.json','all-gallery-requests.json']:
        if (ROOT/name).exists():requests.extend(json.loads((ROOT/name).read_bytes()))
    url=next(r['url'] for r in requests if r['name']==key)
    credit={'ri-robert':'Robert John','ri-collector':'StarWarsCollector_#1','ri-adam':'Adam182R','ri-niclas':'NiclasW','rii-gallery':'NiclasW'}.get(key,'PSA Set Registry source collection')
    return dict(url=url,credit=credit,kind='PSA',photo_id=row['registry_key'])
