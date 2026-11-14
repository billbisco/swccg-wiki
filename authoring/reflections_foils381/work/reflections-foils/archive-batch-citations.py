"""Reuse verified receipts, then preserve exact primary resources still needed."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1]
urls=json.loads((root/(stage+'-citation-urls.json')).read_bytes())
known=json.loads((root/'old-citation-final.json').read_bytes())
for p in root.glob('batch*-citation-final.json'):known.update(json.loads(p.read_bytes()))
if (root/(stage+'-citation-captures.jsonl')).exists():known.update({r['url']:r for r in map(json.loads,(root/(stage+'-citation-captures.jsonl')).read_text().splitlines()) if r.get('status')=='verified'})
rows=[dict(url=u,known=known.get(u)) for u in urls]
code='ROWS='+repr(rows)+'\n'+'''
import json,sys
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
done=json.loads(Path('/opt/swccg-ops/repos/swccg-wiki/ops/wayback/done.json').read_text())
for row in ROWS:
    original=row['url'];url=original.split('#')[0]
    known=row.get('known') or done.get(url) or done.get(original) or {}
    try:
        if known.get('status')=='verified':
            print(json.dumps(dict(known,url=original)),flush=True);continue
        if '/blob/' in url and 'github.com/' in url:url=url.replace('https://github.com/','https://raw.githubusercontent.com/').replace('/blob/','/')
        capture=worker.latest_capture(url) or worker.save_anon(url)
        status,info=worker.verify(url,capture)
        print(json.dumps(dict(url=original,preserved_url=url,capture=capture,status=status,verify=info)),flush=True)
    except Exception as e:print(json.dumps(dict(url=original,preserved_url=url,status='unverified',error=str(e))),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/(stage+'-citation-captures.jsonl')).open('ab') as log:
    for line in p.stdout:
        log.write(line);log.flush();r=json.loads(line);print(r['status'],r['url'],flush=True)
raise SystemExit(p.wait())
