from pilotlib import *
import requests,importlib.util,re
from bs4 import BeautifulSoup
API='https://wiki.swccg.com/api.php';ACTOR='Memory Core ChatGPT'
def api(**params):
 r=requests.get(API,params={'format':'json','formatversion':2,**params},timeout=45);r.raise_for_status();v=r.json();assert'error'not in v,v;return v
spec=importlib.util.spec_from_file_location('style443',P/'source/authoring/style_lint.py');lint=importlib.util.module_from_spec(spec);spec.loader.exec_module(lint)
published=[r for phase in ['upload','pages','notes']for r in read(phase+'-published.json')['pages']]
fresh=api(action='query',titles='|'.join(r['title']for r in published),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content|user',rvslots='main',iiprop='url|timestamp|sha1|size|mime')['query']['pages'];rows=[];files={};prefix='authoring/pilots/443/live/'
plan=read('page-plan.json')
for expected in published:
 row=next(r for r in fresh if r['title']==expected['title']);rev=row['revisions'][0];text=rev['slots']['main']['content'];old=expected['revisions'][0]
 assert rev['revid']==old['revid']and text==old['slots']['main']['content']and rev['user']==ACTOR
 flags,_=lint.lint(text,row['title']);assert all(f.startswith('ARCHIVE ')for f in flags),flags
 parsed=api(action='parse',oldid=rev['revid'],prop='text|images|links|parsewarnings')['parse'];dom=BeautifulSoup(parsed['text'],'html.parser');assert not parsed.get('parsewarnings')and not dom.select('.error,.mw-ext-cite-error')
 entry=next(r for r in plan if r['title']==row['title']);required=row['ns']in[0,4,6,3000]
 if required:assert row.get('flagged',{}).get('stable_revid')==rev['revid']
 if entry['kind']in('sample','hub'):
  assert not [l['title']for l in parsed['links']if not l.get('exists')],row['title']
  response=requests.get('https://wiki.swccg.com/wiki/'+row['title'].replace(' ','_'),timeout=40);response.raise_for_status();public=BeautifulSoup(response.content,'html.parser');permalink=public.select_one('#t-permalink a');assert permalink and('oldid='+str(rev['revid']))in permalink['href']
  assert'"swccgCardImagePilot"'in response.text and'else (root.RLQ'in response.text
  if entry['kind']=='sample':assert len(parsed['images'])==3 and len(dom.select('.swccg-card-image-marker'))==1
  files[prefix+'public-'+entry['file']+'.html']=response.content
 path=prefix+str(rev['revid'])+'-'+entry['file'];data=text.encode();files[path]=data
 rows.append({'title':row['title'],'revision':rev['revid'],'parent':rev['parentid'],'actor':rev['user'],'sha256':sha(data),'bytes':len(data),'path':path,'review_required':required,'stable_revision':row.get('flagged',{}).get('stable_revid'),'raw_flags':flags,'native_parse':'PASS','kind':entry['kind']})
baseline=read('publication-baseline.json')['query']['pages']
for row in baseline:
 if row['title']not in{r['title']for r in published}or not row.get('revisions'):continue
 rev=row['revisions'][0];files[prefix+'before-'+str(rev['revid'])+'.wiki']=rev['slots']['main']['content'].encode()
manifest=read(read('active-sample-phase.json')['phase']+'-manifest.json');originals={r['subject']['title']:r['subject']for page in manifest['pages']for r in page['original_versions']}
image_checks=[]
for sub in originals.values():
 row=api(action='query',titles=sub['title'],prop='imageinfo',iiprop='url|timestamp|size')['query']['pages'][0];info=row['imageinfo'][0];assert info['timestamp']==sub['upload_timestamp']and info['url']==sub['original_version_url']
 r=requests.get(info['url'],timeout=40);r.raise_for_status();assert r.headers.get('Content-Type','').startswith('image/')and len(r.content)==sub['bytes']and sha(r.content)==sub['content_sha256'];image_checks.append(sub)
proof={'pages':rows,'exact_live_revisions':len(rows),'review_required':sum(r['review_required']for r in rows),'actual_required_reviews_verified':sum(r['review_required']for r in rows),'strict_archive_findings':sum(len(r['raw_flags'])for r in rows),'non_archive_findings':0,'exact_original_image_versions_rechecked':len(image_checks),'image_checks':image_checks,'source_payload_changes':False,'canonical_card_edits_by_this_publisher':False,'archive_org_requests':0,'external_preservation_complete':False,'whole443_complete':False}
save('live-proof.json',proof);files[prefix+'live-proof.json']=(P/'live-proof.json').read_bytes();livepin=pin('billbisco/swccg-wiki','exact-live',files)
receipts=[]
for row in rows:
 sub={'kind':'wiki_revision','title':row['title'],'revision_id':row['revision'],'content_sha256':row['sha256'],'bytes':row['bytes']};receipts.append(receipt(livepin,row['path'],sub))
save('live-backup-receipts.json',{'commit':livepin['repository']+'/commit/'+livepin['commit'],'receipts':receipts,'independent_readback':True})
print(json.dumps({k:v for k,v in proof.items()if k not in('pages','image_checks')}|{'backup_commit':livepin['commit']}))
