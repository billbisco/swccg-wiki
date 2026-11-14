import json
from pathlib import Path
from publication_identity import publication_id
root=Path(__file__).parent;rows=[];seen={}
for r in json.loads((root/'manifest.json').read_bytes()):
    if r['language']!='English':continue
    pid=publication_id(r['proposed_article'],r['product']);assert pid not in seen,(pid,r['proposed_article'],seen.get(pid));seen[pid]=r['proposed_article']
    rows.append(dict(article=r['proposed_article'],publication_id=pid))
for file in root.glob('*-new-packet.json'):
    for r in json.loads(file.read_bytes()):
        if r['title'] in {x['article'] for x in rows}:
            expected=next(x['publication_id'] for x in rows if x['article']==r['title']);assert '|publication_id='+expected+'\n' in r['text'],(file.name,r['title'],'Existing published identity changed')
(root/'publication-identity-check.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(len(rows),'distinct English publication IDs; existing packet identities retained')
