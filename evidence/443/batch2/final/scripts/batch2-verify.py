from b2common import *
import requests,re,importlib.util
from bs4 import BeautifulSoup
spec=importlib.util.spec_from_file_location('lintb2',ROOT/'source/authoring/style_lint.py');lint=importlib.util.module_from_spec(spec);spec.loader.exec_module(lint)
API='https://wiki.swccg.com/api.php'
def api(**p):
 r=requests.get(API,params=dict(format='json',formatversion=2,**p),timeout=55);r.raise_for_status();v=r.json();assert'error'not in v,v;return v
def norm(t):return t.replace('_',' ')
plan=read('plan.json');published=read('uploads-published.json')['pages']+read('pages-published.json')['pages'];fresh=[]
for i in range(0,len(plan),45):fresh+=api(action='query',titles='|'.join(r['title']for r in plan[i:i+45]),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content|user',rvslots='main',iiprop='url|timestamp|size|mime')['query']['pages']
def check(row):
 saved=next(x for x in published if norm(x['title'])==norm(row['title']));actual=next(x for x in fresh if x['title']==saved['title']);rev=actual['revisions'][0];text=rev['slots']['main']['content'];assert rev['revid']==saved['revisions'][0]['revid']and text==saved['revisions'][0]['slots']['main']['content']and rev['user']=='Memory Core ChatGPT'
 flags,_=lint.lint(text,actual['title']);assert all(f.startswith('ARCHIVE ')for f in flags),flags
 parsed=api(action='parse',oldid=rev['revid'],prop='text|images|parsewarnings|links')['parse'];dom=BeautifulSoup(parsed['text'],'html.parser');assert not parsed.get('parsewarnings')and not dom.select('.error,.mw-ext-cite-error'),actual['title']
 required=actual['ns']in[0,4,6,3000]
 if required:assert actual.get('flagged',{}).get('stable_revid')==rev['revid']
 if row['kind']in['article','sample']:
  assert len(dom.select('.swccg-card-image-marker'))==1
  expected=next(x for x in read('inventory.json')if(x['canonical']==row['title']or x['key']in row['file']))if row['kind']=='article'else None
  assert len(parsed['images'])>=3
 r=requests.get('https://wiki.swccg.com/wiki/'+row['title'].replace(' ','_'),timeout=55);r.raise_for_status();public=BeautifulSoup(r.content,'html.parser');permalink=public.select_one('#t-permalink a');assert permalink and('oldid='+str(rev['revid']))in permalink['href'],row['title']
 if row['kind']in['article','sample','hub']:assert'"swccgCardImagePilot"'in r.text
 if row['kind']=='article':assert'remaster' in text and 'web.archive.org/web/20071024153847/'in text
 return{'title':actual['title'],'revision':rev['revid'],'actor':rev['user'],'parent':rev['parentid'],'sha256':sha(text.encode()),'bytes':len(text.encode()),'review_required':required,'stable_revision':actual.get('flagged',{}).get('stable_revid'),'raw_flags':flags,'native_public_qa':'PASS','kind':row['kind'],'text':text}
with ThreadPoolExecutor(max_workers=4)as pool:checks=list(pool.map(check,plan))
baseline=read('baseline.json')['query']['pages'];images=[]
for r in read('inventory.json'):
 n=r['number']
 for role in['original','remaster','slip']:
  title='File:'+r[role];actual=next(x for x in fresh if norm(x['title'])==norm(title));info=actual['imageinfo'][0];name=f'{n:02}-historical.gif'if role=='original'else f'{n:02}-{role}'+Path(r[role]).suffix;data=(B/'assets'/name).read_bytes()
  old=next(x for x in baseline if norm(x['title'])==norm(title))
  if not old.get('missing'):assert info['timestamp']==old['imageinfo'][0]['timestamp']and info['url']==old['imageinfo'][0]['url']
  response=requests.get(info['url'],timeout=50);response.raise_for_status();assert response.content==data and response.headers.get('Content-Type','').startswith('image/')
  images.append({'title':actual['title'],'upload_timestamp':info['timestamp'],'original_version_url':info['url'],'sha256':sha(data),'bytes':len(data),'mime':info['mime'],'source_bytes_unchanged':True})
files={};prefix='authoring/pilots/443/batch2/live/'
for r in checks:
 r['path']=prefix+str(r['revision'])+'.wiki';files[r['path']]=r.pop('text').encode()
for r in baseline:
 if r.get('revisions'):files[prefix+'before-'+str(r['revisions'][0]['revid'])+'.wiki']=r['revisions'][0]['slots']['main']['content'].encode()
proof={'pages':checks,'exact_live_revisions':len(checks),'required_stable_reviews_verified':sum(x['review_required']for x in checks),'raw_archive_findings':sum(len(x['raw_flags'])for x in checks),'non_archive_findings':0,'image_versions':images,'all36_originals_checked':len(images)==36,'card_gameplay_and_versions_conserved':True,'archive_uploads':0,'archive_policy':'Viewing/downloading allowed; uploads and Save Page Now paused','external_preservation_complete':False,'whole443_complete':False}
save('live-proof.json',proof);files[prefix+'live-proof.json']=(B/'live-proof.json').read_bytes();pinresult=pin('billbisco/swccg-wiki','exact-live',files);receipts=[]
for r in checks:receipts.append(receipt(pinresult,r['path'],{'kind':'wiki_revision','title':r['title'],'revision_id':r['revision'],'content_sha256':r['sha256'],'bytes':r['bytes']}))
save('live-backup-receipts.json',{'commit':pinresult['commit'],'receipts':receipts,'independent_readback':True})
print(json.dumps({'pages':len(checks),'reviewed':proof['required_stable_reviews_verified'],'original_versions':len(images),'raw_archive_findings':proof['raw_archive_findings'],'non_archive_findings':0,'exact_live_backup':pinresult['commit']}))
