import json,subprocess
from pathlib import Path
root=Path(__file__).parent
latest={r['url']:r for r in map(json.loads,(root/'old-citation-archives.jsonl').read_text().splitlines())}
rows=[r for r in latest.values() if r['status']!='verified']
code='ROWS='+repr(rows)+'\n'+'''
import json,re,sys
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
for row in ROWS:
    original=row['url'];url=original
    if '/blob/' in url:url=url.replace('https://github.com/','https://raw.githubusercontent.com/').replace('/blob/','/')
    try:
        capture=row.get('capture') if url==original else None
        capture=capture or worker.latest_capture(url) or worker.save_anon(url)
        status,info=worker.verify(url,capture)
        print(json.dumps(dict(url=original,preserved_url=url,capture=capture,status=status,verify=info)),flush=True)
    except Exception as e:print(json.dumps(dict(url=original,preserved_url=url,status='unverified',error=str(e))),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/'old-citation-archives.jsonl').open('ab') as log:
    for line in p.stdout:log.write(line);log.flush();print(line.decode().strip(),flush=True)
raise SystemExit(p.wait())
