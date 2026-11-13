import base64
import gzip
import hashlib
import json
from pathlib import Path
import subprocess

root=Path('work/japanese-audit13')
capture=next(x for x in map(json.loads,(root/'preservation-receipts.jsonl').read_text().splitlines()) if x['kind']=='source_snapshot')
assert capture['verified'] and capture['staging_removed']
files=[]
for source in json.loads((root/'better-faces.json').read_bytes()):
    number,label=(185,'Lieutenant Tanbris') if source['id']=='12508' else (25,'R4-E1 (Arfour-Eeone)')
    binary=(root/('original-'+source['id']+'.jpg')).read_bytes()
    assert hashlib.sha256(binary).hexdigest()==source['sha256']
    name=f'Japanese-Premiere-1301-{number}o-SWCA.jpg'
    record='https://theswca.com/index.php?action=disp_item&item_id='+source['id']
    desc=(f'Complete Japanese [[Premiere (Japanese)]] face of [[{label} (Japanese)]], printing ID <code>1301_{number}o</code>. Photograph by Duncan Jenkins, Star Wars Collectors Archive. Original JPEG, with the full printed card area visible.'
          f'<ref name="source">[{record} Star Wars Collectors Archive record] · [{source["source"]} Original photograph]. Preserved copy: [{capture["capture"]} Internet Archive source photographs], including both original JPEGs and source attribution.</ref>\n\n== References ==\n<references />\n\n[[Category:Card images]]')
    files.append(dict(title='File:'+name,name=name,desc=desc,data=base64.b64encode(binary).decode(),sha1=hashlib.sha1(binary).hexdigest(),sha256=source['sha256'],urls=[record,source['source']],pending_archive_flags=[]))
(root/'files-payload.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
prefix=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
helpers=Path('work/japanese-complete/upload.py').read_text(encoding='utf8').split('packet=json.loads')[0]
helpers=helpers.replace('Add original Japanese Premiere card face (#172)','Add complete original Japanese Premiere card face (#361)')
suffix='''
import hashlib
digest=lambda text:hashlib.sha256(text.encode()).hexdigest()
files=json.loads(gzip.decompress(base64.b64decode(PACKET)))
env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig')
credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken']
assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
assert call(action='query',meta='userinfo')['query']['userinfo']['name']==BOT
csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken']
upload_faces(files,csrf)
for item in files:
    page=imageinfo(item['title'])
    rev,text=current(page)
    assert text==item['desc']
    assert 'review' in call(True,action='review',revid=rev,flag_accuracy=1,comment='Verified original Japanese Premiere source photo (#361)',assertuser=BOT,token=csrf,maxlag=5)
'''
packet=base64.b64encode(gzip.compress(json.dumps(files).encode())).decode()
code=prefix+'\n'+helpers+'\nPACKET='+repr(packet)+'\n'+suffix
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'upload-receipts.jsonl').write_bytes(result.stdout)
for row in map(json.loads,result.stdout.splitlines()):print(row['title'],row['revid'])
