import hashlib,json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from PIL import Image
root=Path(__file__).parent;rows=json.loads((root/'selected-photo-leads.json').read_bytes());manifest=json.loads((root/'manifest.json').read_bytes())
complete={r['proposed_article'] for r in manifest if r['status'] in ['existing','created']}
rows=[r for r in rows if r['article'] not in complete]
def one(row):
    name={'Reflections':'ri','Reflections II: Expanding the Galaxy':'rii','Reflections III':'riii'}[row['product']]+'-'+str(row['number']).zfill(3)+'-psa.jpg'
    file=root/'photos'/name
    try:
        if not file.exists():
            r=requests.get(row['candidate']['url'],timeout=90);r.raise_for_status();file.write_bytes(r.content)
        binary=file.read_bytes();assert binary.startswith(b'\xff\xd8')
        with Image.open(file) as im:w,h=im.size
        return dict(row,local_file=str(file.relative_to(root)),source_url=row['candidate']['url'],sha256=hashlib.sha256(binary).hexdigest(),width=w,height=h,original_bytes=True)
    except Exception as e:return dict(article=row['article'],source_url=row['candidate']['url'],error=str(e))
out=[]
with ThreadPoolExecutor(max_workers=3) as pool:
    for r in pool.map(one,rows):
        out.append(r)
        if len(out)%25==0:print('Original PSA photos',len(out),'/',len(rows),flush=True)
(root/'psa-originals.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(len(out),'processed;',sum('error' in r for r in out),'errors',flush=True)
