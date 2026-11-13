import base64
import gzip
import json
from pathlib import Path
import subprocess
import sys

root=Path(__file__).parent
stage=sys.argv[1]
rows=json.loads((root/(stage+'-packet.json')).read_bytes())
if len(sys.argv)>2:
    start=int(sys.argv[2]);rows=rows[start:start+int(sys.argv[3])]
prefix=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
packet=base64.b64encode(gzip.compress(json.dumps(rows,ensure_ascii=False).encode())).decode()
suffix='''
import hashlib
rows=json.loads(gzip.decompress(base64.b64decode(PACKET)))
env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig')
credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken']
assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
info=call(action='query',meta='userinfo',uiprop='rights')['query']['userinfo']
assert info['name']==BOT and {'edit','review','bot'}<=set(info['rights'])
csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken']
for row in rows:
    title=row['title']
    before=call(action='query',titles=title,prop='revisions',rvprop='ids|timestamp|content',rvslots='main',curtimestamp=1)
    starttimestamp=before['curtimestamp'];page=before['query']['pages'][0];rev=page['revisions'][0]
    current_text=rev['slots']['main']['content']
    if current_text.rstrip()!=row['text'].rstrip():
        assert rev['revid']==row['before_revid'] and hashlib.sha256(current_text.encode()).hexdigest()==row['before_sha256'],(title,'Concurrent edit; rebase required')
        args={} if row.get('section',0) is None else dict(section=row.get('section',0))
        if 'sectiontitle' in row:args['sectiontitle']=row['sectiontitle']
        if args.get('section')==0:
            lead=call(action='query',titles=title,prop='revisions',rvprop='content',rvslots='main',rvsection=0)['query']['pages'][0]['revisions'][0]['slots']['main']['content']
            if 'section_text' in row:
                assert hashlib.sha256(lead.encode()).hexdigest()==row['before_section_sha256'],(title,'Lead section changed')
            else:assert lead==current_text,(title,'Editable source sections need a narrower packet')
        edit=call(True,action='edit',title=title,text=row.get('section_text',row['text']),summary=row['summary'],
            bot=1,assertuser=BOT,token=csrf,maxlag=5,nocreate=1,baserevid=rev['revid'],basetimestamp=rev['timestamp'],starttimestamp=starttimestamp,**args)['edit']
        assert edit['result']=='Success',title
        revid=edit['newrevid']
    else:revid=rev['revid']
    assert 'review' in call(True,action='review',revid=revid,flag_accuracy=1,comment='Verified Japanese printed fields and translations (#369)',assertuser=BOT,token=csrf,maxlag=5)
    page=fetch(title);final_rev,final_text=current(page)
    assert final_rev==revid and final_text.rstrip()==row['text'].rstrip(),title
    print(json.dumps(dict(title=title,revid=revid,pageid=page['pageid'],sha256=hashlib.sha256(final_text.encode()).hexdigest(),reviewed=True)),flush=True)
'''
code=prefix+'\nPACKET='+repr(packet)+'\n'+suffix
process=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
process.stdin.write(code.encode());process.stdin.close()
with (root/(stage+'-receipts.jsonl')).open('ab') as log:
    for line in process.stdout:
        log.write(line);log.flush();record=json.loads(line);print(record['title'],record['revid'],flush=True)
raise SystemExit(process.wait())
