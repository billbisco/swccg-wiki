from pilotlib import *
import requests,time,io
from PIL import Image
B=P/'batch2';A=B/'assets';commit='ed271e5000117b80af36bd28e3987c5c34af3ec4';recipes=[]
for n in range(1,13):
 url=f'https://raw.githubusercontent.com/billbisco/swccg-cardmaker/{commit}/cards/vs1/{n:02}.json';dest=A/f'{n:02}-recipe.json'
 if not dest.exists():
  r=requests.get(url,timeout=40);r.raise_for_status();dest.write_bytes(r.content)
 recipes.append({'number':n,'url':url,'sha256':sha(dest.read_bytes()),'bytes':dest.stat().st_size,'recipe':json.loads(dest.read_bytes())})
(B/'recipes.json').write_text(json.dumps(recipes,indent=2)+'\n',encoding='utf-8');print('12 immutable CardMaker recipes checked',flush=True)
url='https://web.archive.org/web/20071024153847id_/http://www.swccgpc.com/Resources/VirtualCards1.pdf';dest=A/'PC-VirtualCards1-20071024153847.pdf'
if not dest.exists():
 r=requests.get(url,timeout=40)
 if r.status_code==200 and r.content.startswith(b'%PDF'):dest.write_bytes(r.content);print('Publisher source PDF downloaded',flush=True)
 else:print('Source PDF response '+str(r.status_code),flush=True)
checks=json.loads((B/'archive-checks.json').read_bytes())
for rec in checks:
 if rec['status']=='checked':continue
 # Read-only recovery; stop at rate limiting rather than cycling providers/hosts.
 time.sleep(12);dest=A/('archive-'+rec['relative_path'].replace('/','__'))
 r=requests.get(rec['archive_url'],timeout=30)
 if r.status_code==429:print('Read cooldown: 429; remaining image replays retained as unresolved',flush=True);break
 if r.status_code!=200:continue
 try:Image.open(io.BytesIO(r.content)).verify()
 except Exception:continue
 assert base64.b32encode(hashlib.sha1(r.content).digest()).decode()==rec['cdx_digest'];dest.write_bytes(r.content);rec.update(status='checked',sha256=sha(r.content),bytes=len(r.content),asset=dest.name,checked_at=now(),final_url=r.url,mime=r.headers.get('content-type'));print(rec['relative_path']+' replay checked',flush=True)
 (B/'archive-checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
