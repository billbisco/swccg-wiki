import json,subprocess
from pathlib import Path
root=Path(__file__).parent
prefix=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0]
code=prefix+'''
env=Path('/opt/swccg-wiki/.env').read_text(encoding='utf-8-sig')
credential=next(shlex.split(s.split('=',1)[1],comments=True)[0] for s in env.splitlines() if s.strip().startswith('MW_BOT_MEMORY_CORE_PASSWORD='))
login=call(action='query',meta='tokens',type='login')['query']['tokens']['logintoken']
assert call(True,action='login',lgname=BOT,lgpassword=credential,lgtoken=login)['login']['result']=='Success'
info=call(action='query',meta='userinfo',uiprop='rights')['query']['userinfo'];assert info['name']==BOT
assert {'move','movefile'}<=set(info['rights']),'File-move rights are unavailable'
csrf=call(action='query',meta='tokens')['query']['tokens']['csrftoken']
old='File:Japanese-ANH-Evader-PSA-156625016-original.jpg'
new='File:Japanese-ANH-Im-On-The-Leader-PSA-156625016-original.jpg'
source=fetch(old);target=fetch(new)
if target.get('missing'):
    assert current(source)[0]==301619,'Source changed; rebase required'
    result=call(True,action='move',**{'from':old,'to':new},reason='Correct card identity: PSA holder says Evader, but printed face is I am On The Leader (#369)',movetalk=1,assertuser=BOT,token=csrf,maxlag=5)
    assert result.get('move',{}).get('to')==new,result.get('error')
for title in [old,new]:
    page=fetch(title);rev,text=current(page)
    if title==old:
        assert text.startswith('#REDIRECT') and new in text,text
        assert 'review' in call(True,action='review',revid=rev,flag_accuracy=1,comment='Preserve corrected photo filename redirect (#369)',assertuser=BOT,token=csrf,maxlag=5)
    print(json.dumps(dict(title=title,revid=rev,pageid=page['pageid'],redirect=title==old)),flush=True)
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE)
(root/'file-move-receipts.jsonl').write_bytes(result.stdout)
print(result.stdout.decode());raise SystemExit(result.returncode)
