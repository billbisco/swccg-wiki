import base64
import gzip
import json
from pathlib import Path
import subprocess
import sys

root = Path('work/japanese-audit13')
mode = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv)>2 else None
rows = json.loads((root/'payload.json').read_bytes())['rows']
if limit:
    rows = rows[:limit]
packet = base64.b64encode(gzip.compress(json.dumps(rows,ensure_ascii=False).encode())).decode()
prefix = Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
suffix = '''
import hashlib
rows=json.loads(gzip.decompress(base64.b64decode(PACKET)))
if MODE=='apply':
    env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig')
    credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
    login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken']
    assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
    assert call(action='query',meta='userinfo')['query']['userinfo']['name']==BOT
    csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken']
for row in rows:
    title=row['title']
    parsed=call(True,action='parse',title=title,text=row['text'],contentmodel='wikitext',prop='text|images|sections')['parse']
    assert 'cite-error' not in parsed['text'],title
    assert parsed['images'] or title.startswith('File:'),title
    if MODE=='preview':
        print(json.dumps(dict(title=title,preview='pass',images=len(parsed['images']))),flush=True)
        continue
    page=call(action='query',titles=title,prop='info|revisions',rvprop='ids|content|timestamp',rvslots='main',curtimestamp=1)
    start=page['curtimestamp']
    page=page['query']['pages'][0]
    revision=page['revisions'][0]
    rev,text=revision['revid'],revision['slots']['main']['content']
    if text!=row['text']:
        assert rev==row['before_revid'] and hashlib.sha256(text.encode()).hexdigest()==row['before_sha256'],(title,'Concurrent edit; rebase required')
        section_args={'section':row['section']} if 'section' in row else {}
        result=call(True,action='edit',title=title,text=row['text'],summary=row['summary'],bot=1,**section_args,
            assertuser=BOT,token=csrf,maxlag=5,nocreate=1,baserevid=rev,basetimestamp=revision['timestamp'],starttimestamp=start)['edit']
        assert result['result']=='Success',title
        rev=result['newrevid']
    review=call(True,action='review',revid=rev,flag_accuracy=1,comment='Japanese printed-face verification (#361)',assertuser=BOT,token=csrf,maxlag=5)
    assert 'review' in review,(title,review)
    page=fetch(title)
    assert current(page)==(rev,row['text']),title
    print(json.dumps(dict(title=title,revid=rev,pageid=page['pageid'],sha256=hashlib.sha256(row['text'].encode()).hexdigest(),reviewed=True)),flush=True)
'''
code=prefix+'\nPACKET='+repr(packet)+'\nMODE='+repr(mode)+'\n'+suffix
process=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
process.stdin.write(code.encode());process.stdin.close()
path=root/(mode+('-sample' if limit else '')+'-receipts.jsonl')
with path.open('ab' if mode=='apply' else 'wb') as log:
    for binary in process.stdout:
        log.write(binary);log.flush()
        record=json.loads(binary)
        print(record.get('title'),record.get('revid',record.get('preview')),flush=True)
raise SystemExit(process.wait())
