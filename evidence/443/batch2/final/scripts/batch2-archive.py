from pilotlib import *
import requests,io
from PIL import Image
B=P/'batch2';A=B/'assets';H=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-e-block-4/work/holotable/preservation-repo/historical-recovery/419')
ledger=json.loads((H/'metadata/archive-recovered-all-manifest.json').read_bytes());out=[]
for src in ledger:
 if not src.get('relative_path','').startswith('v1/'):continue
 rec={k:src[k]for k in['source_url','capture_timestamp','archive_url','relative_path','cdx_digest']};dest=A/('archive-'+src['relative_path'].replace('/','__'))
 try:
  if not dest.exists():
   r=requests.get(src['archive_url'],timeout=25);r.raise_for_status();Image.open(io.BytesIO(r.content)).verify();dest.write_bytes(r.content);rec['final_url']=r.url;rec['mime']=r.headers.get('content-type')
  data=dest.read_bytes();rec.update(sha256=sha(data),bytes=len(data),sha1_base32=base64.b32encode(hashlib.sha1(data).digest()).decode(),checked_at=now(),asset=dest.name,status='checked');assert rec['sha1_base32']==src['cdx_digest']
 except Exception as e:rec['status']='unavailable';rec['error']=str(e)[:300]
 out.append(rec);(B/'archive-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'file':rec['relative_path'],'status':rec['status'],'sha256':rec.get('sha256')}),flush=True)
