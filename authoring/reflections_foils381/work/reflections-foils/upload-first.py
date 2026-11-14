import base64,gzip,hashlib,json,re,subprocess,sys
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'first-readings.json').read_bytes());archive=json.loads((root/'first-preservation.json').read_bytes());assert archive['verified']
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
files=[];originals=[]
gallery='https://www.psacard.com/psasetregistry/tcg/other-tcg-sets/2000-decipher-star-wars-ccg-reflections-foil/imagegallery/755431'
for row in rows:
    data=(root/row['source_photo']).read_bytes();assert hashlib.sha256(data).hexdigest()==row['source_sha256']
    slug=re.sub(r'[^A-Za-z0-9]+','-',row['printed_title']).strip('-')
    name='Reflections-Foil-'+('L' if row['side']=='Light' else 'D')+'-'+slug+'-PSA-'+row['physical_cert']+'-original.jpg'
    desc='Original physical [[Reflections]] foil face of [['+row['article']+']], '+row['side']+' Side, photographed in PSA holder '+row['physical_cert']+'. Photograph from Robert John’s PSA Set Registry collection. The original JPEG is retained unchanged.<ref name="source">['+gallery+' Robert John’s Reflections foil gallery] · ['+row['source_url']+' Original photograph]. Preserved copy: ['+archive['capture']+' Internet Archive source photographs], including this unchanged JPEG.</ref>\n\n== References ==\n<references />\n\n[[Category:Card images]]'
    assert not lint(desc,'File:'+name)[0],lint(desc,'File:'+name)[0]
    files.append(dict(title='File:'+name,name=name,card_title=row['article'],desc=desc,data=base64.b64encode(data).decode(),sha1=hashlib.sha1(data).hexdigest(),sha256=row['source_sha256'],urls=[gallery,row['source_url']]))
    originals.append(dict(name=name,local_file=row['source_photo'],sha256=row['source_sha256']))
(root/'first-files-payload.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
(root/'uploaded-images.json').write_text(json.dumps(originals,ensure_ascii=False,indent=2),encoding='utf8')
if '--prepare' in sys.argv:print('Ten original File descriptions prepared, lint 0');raise SystemExit(0)
suffix='''
import hashlib
digest=lambda text:hashlib.sha256(text.encode()).hexdigest()
files=json.loads(gzip.decompress(base64.b64decode(PACKET)))
env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig')
credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken']
assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
assert call(action='query',meta='userinfo')['query']['userinfo']['name']==BOT
csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken'];upload_faces(files,csrf)
'''
packet=base64.b64encode(gzip.compress(json.dumps(files).encode())).decode()
code=(root/'api-core.py').read_text(encoding='utf8')+'\n'+(root/'upload-core.py').read_text(encoding='utf8')+'\nPACKET='+repr(packet)+'\n'+suffix
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/'first-upload-receipts.jsonl').open('ab') as log:
    for line in p.stdout:
        log.write(line);log.flush();r=json.loads(line);print(r['title'],r['revid'],flush=True)
raise SystemExit(p.wait())
