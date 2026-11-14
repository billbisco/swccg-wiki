import hashlib,json,sys
from pathlib import Path
import requests
root=Path(__file__).parent;stage=sys.argv[1]
captures={r['title']:r for r in map(json.loads,(root/(stage+'-image-captures.jsonl')).read_text().splitlines())};assert captures and all(r['verified'] for r in captures.values())
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(captures),prop='revisions|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='url|timestamp|sha1|size|mime'),timeout=60);r.raise_for_status()
heads={p['title']:p for p in r.json()['query']['pages']};rows=[]
for title,p in heads.items():
    rev=p['revisions'][0];old=rev['slots']['main']['content'];cap=captures[title];version=p['imageinfo'][0]
    assert version['timestamp']==cap['version'] and version['sha1']==cap['sha1'] and version['url']==cap['url'],title
    if cap['capture'] in old:continue
    assert '== Preservation ==' not in old,(title,'Concurrent preservation section; merge required')
    section='* ['+cap['capture']+' Full-resolution original image]. Upload version: <code>'+cap['version']+'</code> (UTC). Verified SHA-256: <code>'+cap['sha256']+'</code>.\n'
    text=old.rstrip()+'\n\n== Preservation ==\n\n'+section.rstrip()
    rows.append(dict(title=title,text=text,section='new',sectiontitle='Preservation',section_text=section,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),summary='Link the byte-verified archive of this exact original image version (#381)'))
(root/(stage+'-file-preservation-heads.json')).write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
(root/(stage+'-file-preservation-packet.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'version-specific original-image preservation links prepared')
