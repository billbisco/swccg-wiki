import base64,gzip,hashlib,json,re,subprocess
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'recovered-face-manifest.json').read_bytes());archive=json.loads((root/'recovered-preservation.json').read_bytes());assert archive['verified']
slugs=['Hoth-FX-10','Hoth-Echo-Command-Center-Dark','Hoth-EG-4','Hoth-FX-7','Hoth-Echo-Command-Center-Light','ANH-Evader','ANH-R3-T6','ANH-R5-D4','ANH-RA-7']
files=[]
for row,slug in zip(rows,slugs):
    data=(root/row['file']).read_bytes();name='Japanese-'+slug+'-PSA-'+row['url'].split('/cert/')[1].split('/')[0]+'-original.jpg'
    desc='Full original Japanese printed face of [['+row['title']+']], printing ID <code>'+row['uid']+'</code>, in its PSA holder. Original JPEG from PSA Set Registry, retained unchanged.<ref name="source">['+row['gallery']+' PSA Set Registry source gallery] · ['+row['url']+' Original photograph]. Preserved copy: ['+archive['capture']+' Internet Archive source photographs], including this unchanged JPEG.</ref>\n\n== References ==\n<references />\n\n[[Category:Card images]]'
    files.append(dict(title='File:'+name,name=name,card_title=row['title'],desc=desc,data=base64.b64encode(data).decode(),sha1=hashlib.sha1(data).hexdigest(),sha256=hashlib.sha256(data).hexdigest(),urls=[row['gallery'],row['url']],pending_archive_flags=[]))
(root/'recovered-files-payload.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
prefix=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
helpers=Path('work/japanese-complete/upload.py').read_text(encoding='utf8').split('packet=json.loads')[0].replace('Add original Japanese Premiere card face (#172)','Add verified original Japanese card photograph (#369)')
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
    page=imageinfo(item['title']);rev,text=current(page);assert text==item['desc']
    assert 'review' in call(True,action='review',revid=rev,flag_accuracy=1,comment='Verified original Japanese card photograph (#369)',assertuser=BOT,token=csrf,maxlag=5)
'''
packet=base64.b64encode(gzip.compress(json.dumps(files).encode())).decode();code=prefix+'\n'+helpers+'\nPACKET='+repr(packet)+'\n'+suffix
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'recovered-upload-receipts.jsonl').write_bytes(r.stdout)
for r in map(json.loads,r.stdout.splitlines()):print(r['title'],r['revid'])
