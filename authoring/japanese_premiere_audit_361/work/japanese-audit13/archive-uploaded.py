import base64
import json
from pathlib import Path
import subprocess

root=Path('work/japanese-audit13')
rows=list(map(json.loads,(root/'upload-receipts.jsonl').read_text().splitlines()))
code='ROWS='+repr(base64.b64encode(json.dumps(rows).encode()).decode())+'\n'+'''
import base64,hashlib,json,re,sys,urllib.request
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import wayback_worker as worker
for row in json.loads(base64.b64decode(ROWS)):
    url=row['image_url']
    try:
        capture=worker.latest_capture(url) or worker.save_anon(url)
        replay=re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1)
        with urllib.request.urlopen(replay,timeout=45) as response:data=response.read()
        digest=hashlib.sha256(data).hexdigest()
        assert digest==row['image_sha256']
        print(json.dumps(dict(title=row['title'],url=url,capture=capture,verified=True,sha256=digest,bytes=len(data))),flush=True)
    except Exception as error:
        print(json.dumps(dict(title=row['title'],url=url,verified=False,error=str(error))),flush=True)
'''
process=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
process.stdin.write(code.encode());process.stdin.close()
with (root/'image-captures.jsonl').open('wb') as log:
    for line in process.stdout:
        log.write(line);log.flush();print(line.decode().strip(),flush=True)
raise SystemExit(process.wait())
