import base64,gzip,hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).parent
source=json.loads((root/'new-source.json').read_bytes());capture=json.loads((root/'preservation.json').read_bytes());assert capture['verified']
data=(root/source['file']).read_bytes();name='Japanese-Hoth-2-1B-PSA-175224368.jpg'
desc='Original Japanese [[Hoth (Japanese)]] face of [[2-1B (Too-Onebee) (Japanese)]], printing ID <code>1303_1o</code>, in its PSA holder. The label identifies the 1998 Japanese Light Side printing, certification 108070289. Image from StarWarsCollector_#1’s PSA Set Registry gallery.<ref name="source">['+source['gallery']+' PSA Set Registry image gallery] · ['+source['image']+' Original photograph]. Preserved copy: ['+capture['capture']+' Internet Archive source photograph], retaining the original JPEG unchanged.</ref>\n\n== References ==\n<references />\n\n[[Category:Card images]]'
files=[dict(title='File:'+name,name=name,desc=desc,data=base64.b64encode(data).decode(),sha1=hashlib.sha1(data).hexdigest(),sha256=hashlib.sha256(data).hexdigest(),urls=[source['gallery'],source['image']],pending_archive_flags=[])]
(root/'files-payload.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf8')
prefix=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
helpers=Path('work/japanese-complete/upload.py').read_text(encoding='utf8').split('packet=json.loads')[0].replace('Add original Japanese Premiere card face (#172)','Add original Japanese Hoth 2-1B photograph (#369)')
suffix='''
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
    assert 'review' in call(True,action='review',revid=rev,flag_accuracy=1,comment='Verified original Japanese Hoth card photograph (#369)',assertuser=BOT,token=csrf,maxlag=5)
'''
packet=base64.b64encode(gzip.compress(json.dumps(files).encode())).decode()
code=prefix+'\n'+helpers+'\nPACKET='+repr(packet)+'\n'+suffix
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'upload-receipts.jsonl').write_bytes(r.stdout)
for row in map(json.loads,r.stdout.splitlines()):print(row['title'],row['revid'])
