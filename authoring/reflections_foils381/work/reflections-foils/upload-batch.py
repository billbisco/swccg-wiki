import base64,gzip,hashlib,json,re,subprocess,sys,unicodedata
from pathlib import Path
from source_registry import provenance
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent;stage=sys.argv[1]
rows=json.loads((root/(stage+'-readings.json')).read_bytes());archive=json.loads((root/(stage+'-preservation.json')).read_bytes());assert archive['verified']
files=[];originals=[]
for row in rows:
    data=(root/row['source_photo']).read_bytes();assert hashlib.sha256(data).hexdigest()==row['source_sha256'];p=provenance(row)
    code={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections-II','Reflections III':'Reflections-III'}[row['product']]
    slug=re.sub(r'[^A-Za-z0-9]+','-',unicodedata.normalize('NFKD',row['printed_title']).encode('ascii','ignore').decode()).strip('-')
    name=code+'-Foil-'+('L' if row['side']=='Light' else 'D')+'-'+slug+'-'+p['kind']+'-photo-'+p['photo_id']+'-original.jpg'
    desc='Original physical [['+row['product']+']] foil face of [['+row['article']+']], '+row['side']+' Side. Photograph from '+p['credit']+'. Original JPEG retained unchanged.<ref name="source">['+p['url']+' Source collection entry] · ['+row['source_url']+' Original photograph]. Preserved copy: ['+archive['capture']+' Internet Archive source photographs], including this unchanged JPEG.</ref>\n\n== References ==\n<references />\n\n[[Category:Card images]]'
    assert not lint(desc,'File:'+name)[0],lint(desc,'File:'+name)[0]
    files.append(dict(title='File:'+name,name=name,card_title=row['article'],desc=desc,data=base64.b64encode(data).decode(),sha1=hashlib.sha1(data).hexdigest(),sha256=row['source_sha256'],urls=[p['url'],row['source_url']]))
    originals.append(dict(name=name,local_file=row['source_photo'],sha256=row['source_sha256']))
(root/(stage+'-files-payload.json')).write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
alloriginals=json.loads((root/'uploaded-images.json').read_bytes()) if (root/'uploaded-images.json').exists() else []
alloriginals={r['name']:r for r in alloriginals};alloriginals.update({r['name']:r for r in originals});(root/'uploaded-images.json').write_text(json.dumps(list(alloriginals.values()),ensure_ascii=False,indent=2),encoding='utf8')
if '--prepare' in sys.argv:print(len(files),'File descriptions prepared, lint 0');raise SystemExit(0)
suffix='''
import hashlib
digest=lambda text:hashlib.sha256(text.encode()).hexdigest()
files=json.loads(gzip.decompress(base64.b64decode(PACKET)))
env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig');credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken'];assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
assert call(action='query',meta='userinfo')['query']['userinfo']['name']==BOT
csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken'];upload_faces(files,csrf)
'''
packet=base64.b64encode(gzip.compress(json.dumps(files).encode())).decode();code=(root/'api-core.py').read_text(encoding='utf8')+'\n'+(root/'upload-core.py').read_text(encoding='utf8')+'\nPACKET='+repr(packet)+'\n'+suffix
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/(stage+'-upload-receipts.jsonl')).open('ab') as log:
    for line in p.stdout:log.write(line);log.flush();r=json.loads(line);print(r['title'],r['revid'],flush=True)
raise SystemExit(p.wait())
