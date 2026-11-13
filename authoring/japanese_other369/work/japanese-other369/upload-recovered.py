import base64,gzip,hashlib,json,re,subprocess,sys
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'recovered-face-manifest.json').read_bytes());archive=json.loads((root/'recovered-preservation.json').read_bytes());assert archive['verified']
slugs=['Hoth-FX-10','Hoth-Echo-Command-Center-Dark','Hoth-EG-4','Hoth-FX-7','Hoth-Echo-Command-Center-Light','ANH-Im-On-The-Leader','ANH-R3-T6','ANH-R5-D4','ANH-RA-7']
files=[]
for row,slug in zip(rows,slugs):
    data=(root/row['file']).read_bytes();name='Japanese-'+slug+'-PSA-'+row['url'].split('/cert/')[1].split('/')[0]+'-original.jpg'
    mismatch=' The PSA label says “Evader”; the printed title 先頭機は任せろ, destiny 3, unique marker and game text identify [[I\'m On The Leader (Japanese)]].' if row.get('rejected_catalog_assignment') else ''
    desc='Full original Japanese printed face of [['+row['title']+']], printing ID <code>'+row['uid']+'</code>, in its PSA holder. Original JPEG from PSA Set Registry, retained unchanged.'+mismatch+'<ref name="source">['+row['gallery']+' PSA Set Registry source gallery] · ['+row['url']+' Original photograph]. Preserved copy: ['+archive['capture']+' Internet Archive source photographs], including this unchanged JPEG.</ref>\n\n== References ==\n<references />\n\n[[Category:Card images]]'
    files.append(dict(title='File:'+name,name=name,card_title=row['title'],desc=desc,data=base64.b64encode(data).decode(),sha1=hashlib.sha1(data).hexdigest(),sha256=hashlib.sha256(data).hexdigest(),urls=[row['gallery'],row['url']],pending_archive_flags=[]))
(root/'recovered-files-payload.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
if '--prepare' in sys.argv:print('Prepared',len(files),'correctly identified original File descriptions');raise SystemExit(0)
prefix=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
helpers=(root/'upload-core.py').read_text(encoding='utf8')
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
process=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE)
(root/'recovered-upload-receipts.jsonl').write_bytes(process.stdout)
for record in map(json.loads,process.stdout.splitlines()):print(record['title'],record['revid'])
if process.returncode:raise SystemExit(process.returncode)
