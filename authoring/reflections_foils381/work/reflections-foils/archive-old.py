import base64,json,subprocess
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'old-citation-queue.json').read_bytes())
code='ROWS='+repr(rows)+'\n'+'''
import json,sys
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
for r in ROWS:
    url=r['url'];known=r.get('known') or {}
    try:
        if known.get('status')=='verified':
            print(json.dumps(dict(url=url,capture=known['capture'],status='verified',method='existing verified shared preservation record')),flush=True);continue
        capture=worker.latest_capture(url) or worker.save_anon(url)
        status,info=worker.verify(url,capture)
        print(json.dumps(dict(url=url,capture=capture,status=status,verify=info)),flush=True)
    except Exception as e:print(json.dumps(dict(url=url,status='unverified',error=str(e))),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/'old-citation-archives.jsonl').open('ab') as log:
    for line in p.stdout:log.write(line);log.flush();print(line.decode().strip(),flush=True)
raise SystemExit(p.wait())
