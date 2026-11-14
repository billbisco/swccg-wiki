from b3common import *
phase=sys.argv[1];assert phase in['uploads','pages']
plan=read('plan.json');rows=[r for r in plan if(r['kind']=='upload')==(phase=='uploads')];gatephase='uploads-r3'if phase=='uploads'else'pages'
approval=read(gatephase+'-approval.json');assert sha((B/(gatephase+'-manifest.json')).read_bytes())==approval['manifest_sha256'];packet=[]
for row in rows:
 assert read(gatephase+'-'+row['file']+'.report.json')['publication_eligible']
 text=(B/'drafts'/row['file']).read_bytes().decode();sub=next(x['subject']for x in read(gatephase+'-manifest.json')['pages']if x['title']==row['title']);assert sha(text.encode())==sub['content_sha256']
 item={**row,'text':text,'sha256':sha(text.encode())}
 if phase=='uploads':item['data']=base64.b64encode((B/'assets'/row['asset']).read_bytes()).decode()
 packet.append(item)
code="""import pathlib,requests,shlex,json,hashlib,base64
ROOT=pathlib.Path('/mnt/HC_Volume_107153504/work/memorycore-443-settings-correction-20261114');ROOT.mkdir(parents=True,exist_ok=True)
values={}
for line in pathlib.Path('/opt/swccg-wiki/.env').read_text().splitlines():
 if line.startswith('MW_BOT_MEMORY_CORE_PASSWORD='):values['p']=shlex.split(line.split('=',1)[1])[0]
s=requests.Session();URL='https://wiki.swccg.com/api.php'
def api(files=None,**p):
 r=s.post(URL,data=dict(p,format='json',formatversion=2),files=files,timeout=65);r.raise_for_status();v=r.json();assert'error'not in v,v.get('error',{}).get('code');return v
login=api(action='query',meta='tokens',type='login')['query']['tokens']['logintoken'];assert api(action='login',lgname='Memory Core ChatGPT',lgpassword=values['p'],lgtoken=login)['login']['result']=='Success'
assert api(action='query',meta='userinfo')['query']['userinfo']['name']=='Memory Core ChatGPT';token=api(action='query',meta='tokens')['query']['tokens']['csrftoken']
def page(t):return api(action='query',titles=t,prop='revisions|imageinfo|flagged',rvprop='ids|timestamp|content|user',rvslots='main',iiprop='url|timestamp|sha1|size|mime')['query']['pages'][0]
def matches(actual,text):
 if actual is None:return False
 if text.rstrip().endswith('~~~~'):
  prefix=text.rstrip()[:-4];tail=actual[len(prefix):];return actual.startswith(prefix)and len(tail)<500 and'Memory Core ChatGPT'in tail and'(UTC)'in tail
 return actual==text.rstrip()
out=[]
for item in PACKET:
 old=page(item['title']);text=item['text'];assert hashlib.sha256(text.encode()).hexdigest()==item['sha256']
 if PHASE=='uploads':
  binary=base64.b64decode(item['data']);filename=item['title'].removeprefix('File:')
  if old.get('missing'):
   r=api(files={'file':(filename,binary,'image/gif')},action='upload',filename=filename,text=text,comment='Story443: unchanged historical OVS1 full card with direct primary-source credits',token=token);assert r['upload']['result']=='Success'
 else:
  if not matches(old.get('revisions',[{}])[0].get('slots',{}).get('main',{}).get('content'),text):
   assert old.get('revisions',[{}])[0].get('revid')==item['base'],'Revision conflict: '+item['title']
   p={'action':'edit','title':item['title'],'text':text,'summary':'Story443: move saved image default to dedicated Display settings page','bot':1,'token':token}
   if item['base']is None:p['createonly']=1
   else:p.update(baserevid=item['base'],basetimestamp=old['revisions'][0]['timestamp'])
   assert api(**p)['edit']['result']=='Success'
 row=page(item['title']);assert matches(row['revisions'][0]['slots']['main']['content'],text),item['title']
 if row['ns']in[0,4,6,3000]:
  rid=row['revisions'][0]['revid']
  if row.get('flagged',{}).get('stable_revid')!=rid:api(action='review',revid=rid,flag_accuracy=1,comment='Story443 exact-state image/source cohort checked',token=token);row=page(item['title'])
  assert row['flagged']['stable_revid']==rid
 if PHASE=='uploads':
  r=s.get(row['imageinfo'][0]['url'],timeout=40);r.raise_for_status();assert r.content==binary
 out.append(row);(ROOT/(PHASE+'-results.json')).write_text(json.dumps({'pages':out},indent=2))
print(json.dumps({'pages':out}))
""".replace('PACKET',repr(packet)).replace('PHASE',repr(phase))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);(B/(phase+'-publication.stderr')).write_bytes(r.stderr);assert r.returncode==0,r.stderr.decode(errors='replace')[-1800:];save(phase+'-published.json',json.loads(r.stdout));print(json.dumps({'phase':phase,'saved':len(packet),'actor':'Memory Core ChatGPT'}))
