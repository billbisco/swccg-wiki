"""Own-bot guarded publisher for new articles and narrowly scoped repairs."""
import base64,gzip,json,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1];rows=json.loads((root/(stage+'-packet.json')).read_bytes())
sys.path.insert(0,'work/wiki-tools');from publication_policy import lint
for row in rows:
    flags=lint(row['text'],row['title'])[0]
    assert not flags,(row['title'],flags)
if len(sys.argv)>2:rows=rows[int(sys.argv[2]):int(sys.argv[2])+int(sys.argv[3])]
suffix='''
import hashlib
rows=json.loads(gzip.decompress(base64.b64decode(PACKET)))
env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig')
credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken']
assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
info=call(action='query',meta='userinfo',uiprop='rights')['query']['userinfo'];assert info['name']==BOT and {'edit','review','bot'}<=set(info['rights'])
csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken']
def equivalent(row,text):
    if row.get('signed_note'):
        assert row['title'].startswith('Talk:') and row['text'].count('~~~~')==1
        prefix,suffix=row['text'].split('~~~~')
        return text.startswith(prefix) and text.rstrip().endswith(suffix.rstrip()) and 'Memory Core ChatGPT' in text[len(prefix):]
    return text.rstrip()==row['text'].rstrip()
for row in rows:
    title=row['title'];before=call(action='query',titles=title,prop='revisions',rvprop='ids|timestamp|content',rvslots='main',curtimestamp=1)
    page=before['query']['pages'][0];args=dict(action='edit',title=title,text=row.get('section_text',row['text']),summary=row['summary'],bot=1,assertuser=BOT,token=csrf,maxlag=5,starttimestamp=before['curtimestamp'])
    if page.get('missing'):
        assert row.get('new'),(title,'Unexpected missing old page')
        args.update(createonly=1,baserevid=0,section=0)
        edit=call(True,**args)['edit'];assert edit['result']=='Success';revid=edit['newrevid']
    else:
        rev=page['revisions'][0];old=rev['slots']['main']['content']
        if equivalent(row,old):revid=rev['revid']
        else:
            assert not row.get('new'),(title,'New page already exists with different text; reconcile instead')
            assert rev['revid']==row['before_revid'] and hashlib.sha256(old.encode()).hexdigest()==row['before_sha256'],(title,'Concurrent edit; refresh packet')
            section=row.get('section',0)
            if section is not None:
                args['section']=section
                if section=='new':args['sectiontitle']=row['sectiontitle']
                else:
                    lead=call(action='query',titles=title,prop='revisions',rvprop='content',rvslots='main',rvsection=section)['query']['pages'][0]['revisions'][0]['slots']['main']['content']
                    if 'before_section_sha256' in row:assert hashlib.sha256(lead.encode()).hexdigest()==row['before_section_sha256']
                    else:assert section==0 and lead==old,(title,'Need a section-scoped packet')
            args.update(nocreate=1,baserevid=rev['revid'],basetimestamp=rev['timestamp'])
            edit=call(True,**args)['edit'];assert edit['result']=='Success';revid=edit['newrevid']
    reviewable=page.get('ns',0)%2==0
    if reviewable:assert 'review' in call(True,action='review',revid=revid,flag_accuracy=1,comment='Verified historical Reflections foil publication and sources (#381)',assertuser=BOT,token=csrf,maxlag=5)
    call(True,action='purge',titles=title,forcelinkupdate=1)
    final=fetch(title);rid,text=current(final);assert rid==revid,title
    assert equivalent(row,text),title
    print(json.dumps(dict(title=title,revid=revid,pageid=final['pageid'],sha256=hashlib.sha256(text.encode()).hexdigest(),reviewed=True if reviewable else None,review_status='reviewed' if reviewable else 'not applicable: talk namespace')),flush=True)
'''
packet=base64.b64encode(gzip.compress(json.dumps(rows,ensure_ascii=False).encode())).decode()
code=(root/'api-core.py').read_text(encoding='utf8')+'\nPACKET='+repr(packet)+'\n'+suffix
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/(stage+'-receipts.jsonl')).open('ab') as log:
    for line in p.stdout:
        log.write(line);log.flush();r=json.loads(line);print(r['title'],r['revid'],flush=True)
raise SystemExit(p.wait())
