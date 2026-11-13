import base64
import hashlib
import html
import json
from pathlib import Path
import subprocess

root=Path('work/japanese-audit13')
records=json.loads((root/'better-faces.json').read_bytes())
body='<!doctype html><html><meta charset="utf-8"><title>Preserved Japanese Premiere faces, story 361</title><style>body{max-width:52rem;margin:2rem auto;font:1rem system-ui}img{max-width:100%}header{background:#fff3c2;padding:1rem}</style><header>Preserved source photographs, retrieved 13 November 2026. Photos by Duncan Jenkins, Star Wars Collectors Archive.</header><h1>Two Japanese Premiere complete card faces</h1>'
for row in records:
    source=root/('original-'+row['id']+'.jpg')
    binary=source.read_bytes()
    row['sha256']=hashlib.sha256(binary).hexdigest()
    label='Lieutenant Tanbris' if row['id']=='12508' else 'R4-E1 (Arfour-Eeone)'
    body+='<section><h2>'+label+'</h2><p><a href="https://theswca.com/index.php?action=disp_item&amp;item_id='+row['id']+'">Source record</a> · <a href="'+html.escape(row['source'])+'">Original photograph</a></p><img alt="'+label+'" src="data:image/jpeg;base64,'+base64.b64encode(binary).decode()+'"></section>'
body+='</html>'
(root/'two-complete-faces.html').write_text(body,encoding='utf8')
(root/'better-faces.json').write_text(json.dumps(records,indent=2),encoding='utf8')
suffix='''
import base64,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import wayback_worker as worker
def fetch(url):
    request=urllib.request.Request(url,headers={'User-Agent':worker.UA})
    with urllib.request.urlopen(request,timeout=45) as response:return response.read()
video='https://web.archive.org/web/20261106164955id_/https://www.youtube.com/watch?v=qqdS5JpNPiE'
try:
    replay=fetch(video)
    text=replay.decode('utf8')
    assert all(x in text for x in ['qqdS5JpNPiE','Star Wars CCG Japanese Premiere Complete Set','swccgBoosterBreaks'])
    print(json.dumps(dict(kind='video_page',capture=video.replace('id_/','/'),verified=True,sha256=hashlib.sha256(replay).hexdigest(),bytes=len(replay))),flush=True)
except Exception as error:
    print(json.dumps(dict(kind='video_page',verified=False,error=str(error))),flush=True)
path=Path('/opt/swccg-res/snapshots/theswca/japanese-premiere-two-complete-faces-361.html')
binary=base64.b64decode(BODY)
path.write_bytes(binary);path.chmod(0o644)
url='https://swccg.com/snapshots/theswca/'+path.name
assert fetch(url)==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url)
    replay=fetch(re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1))
    assert replay==binary
    embedded=re.findall(b'data:image/jpeg;base64,([A-Za-z0-9+/=]+)',replay)
    assert len(embedded)==2
    result=dict(kind='source_snapshot',url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),image_hashes=[hashlib.sha256(base64.b64decode(x)).hexdigest() for x in embedded])
    path.unlink()
    result['staging_removed']=not path.exists()
    print(json.dumps(result),flush=True)
except Exception as error:
    print(json.dumps(dict(kind='source_snapshot',url=url,verified=False,error=str(error))),flush=True)
'''
code='BODY='+repr(base64.b64encode(body.encode()).decode())+'\n'+suffix
process=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
process.stdin.write(code.encode());process.stdin.close()
with (root/'preservation-receipts.jsonl').open('wb') as log:
    for line in process.stdout:
        log.write(line);log.flush();print(line.decode().strip(),flush=True)
raise SystemExit(process.wait())
