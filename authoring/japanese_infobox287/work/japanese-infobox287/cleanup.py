import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint
root=Path(__file__).parent
row=next(r for r in json.loads((root/'drafts.json').read_bytes()) if 'Japanese' not in r['title'])
text=row['text'];receipt=next(r for r in map(json.loads,(root/'cards-receipts.jsonl').read_text(encoding='utf8').splitlines()) if r['title']==row['title'])
archive=json.loads((root/'bgg-preservation.json').read_bytes());assert archive['verified']
preserved=' Preserved copy: ['+archive['capture']+' Internet Archive].'
text=text.replace('The 5×7 signed by Baksa, Michael A. Stackpole, and Timothy Zahn.','Signed by Baksa, Stackpole, and Zahn.')
text=text.replace('BoardGameGeek (22 August 2012).</ref>','BoardGameGeek (22 August 2012).'+preserved+'</ref>')
text=text.replace('BoardGameGeek (22 August 2012)\n','BoardGameGeek (22 August 2012).'+preserved+'\n')
assert not lint(text,row['title'])[0],lint(text,row['title'])
packet=dict(title=row['title'],text=text,before_revid=receipt['revid'],before_sha256=receipt['sha256'],section=0,summary='Preserve the card-list citation and shorten the signed-card caption (#366; #287)')
(root/'cleanup-packet.json').write_text(json.dumps([packet],ensure_ascii=False,indent=2),encoding='utf8')
print('Promo citation/caption cleanup lint 0; original source URL and citation date preserved')
