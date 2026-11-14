"""Reuse the proven SWCA original-byte browser fetch, scoped to an owned session."""
import base64,hashlib,json,re,subprocess,sys
from pathlib import Path
from PIL import Image
root=Path(__file__).parent
allrows=[]
for file in sorted(root.glob('swca-probe-*.json')):
    allrows.extend(r for r in json.loads(file.read_bytes()) if r.get('assets'))
done={r['id'] for r in map(json.loads,(root/'swca-originals-results.jsonl').read_text().splitlines()) if r.get('local_file')} if (root/'swca-originals-results.jsonl').exists() else set()
rows=[];seen=set()
for r in allrows:
    key=r['name'].split('-')[1]
    if key not in seen and key not in done:rows.append(r);seen.add(key)
if len(sys.argv)>1:rows=rows[:int(sys.argv[1])]
assert rows,'No pending sources'
sources={r['name'].split('-')[1]:r['assets'][0].split('theswca.com/',1)[1] for r in rows}
byid={r['name'].split('-')[1]:r for r in rows}
template=(root/'swca-browser-core.py').read_text(encoding='utf8').replace('SOURCE_MAP',repr(sources))
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','docker','exec','-i','flaresolverr','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(template.encode());p.stdin.close()
with (root/'swca-originals-results.jsonl').open('ab') as log:
    for line in p.stdout:
        r=json.loads(line);meta=byid[r['id']];r.update(article=meta['article'],entry_url=meta['url'])
        if r.get('data'):
            data=base64.b64decode(r.pop('data'));assert data.startswith((b'\xff\xd8',b'\x89PNG',b'GIF')),r['id']
            ext='.png' if data.startswith(b'\x89PNG') else '.gif' if data.startswith(b'GIF') else '.jpg'
            file=root/'photos'/('swca-'+r['id']+ext);file.write_bytes(data)
            with Image.open(file) as im:w,h=im.size
            r.update(local_file=str(file.relative_to(root)),sha256=hashlib.sha256(data).hexdigest(),width=w,height=h,original_bytes=True)
        if r.get('rendered_png'):
            r.pop('rendered_png');r['screenshot_fallback_rejected_as_original']=True
        log.write((json.dumps(r,ensure_ascii=False)+'\n').encode());log.flush();print(r,flush=True)
raise SystemExit(p.wait())
