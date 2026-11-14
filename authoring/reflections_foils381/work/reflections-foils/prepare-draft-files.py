"""Names for offline article drafts only; never upload or claim preservation."""
import hashlib,json,re,sys,unicodedata
from pathlib import Path
from source_registry import provenance
root=Path(__file__).parent;stage=sys.argv[1];rows=json.loads((root/(stage+'-readings.json')).read_bytes());files=[]
assert not (root/(stage+'-upload-receipts.jsonl')).exists(),'Never replace a published file payload'
for row in rows:
    data=(root/row['source_photo']).read_bytes();assert hashlib.sha256(data).hexdigest()==row['source_sha256'];p=provenance(row)
    code={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections-II','Reflections III':'Reflections-III'}[row['product']]
    slug=re.sub(r'[^A-Za-z0-9]+','-',unicodedata.normalize('NFKD',row['printed_title']).encode('ascii','ignore').decode()).strip('-')
    name=code+'-Foil-'+('L' if row['side']=='Light' else 'D')+'-'+slug+'-'+p['kind']+'-photo-'+p['photo_id']+'-original.jpg'
    files.append(dict(title='File:'+name,name=name,card_title=row['article'],sha1=hashlib.sha1(data).hexdigest(),sha256=row['source_sha256'],draft_only=True,preservation_status='pending; no verified snapshot asserted; regenerate complete upload packet after archive recovery'))
(root/(stage+'-files-payload.json')).write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
print(len(files),'offline draft image identities; no uploads or archive claims')
