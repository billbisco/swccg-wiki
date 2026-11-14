from b3common import *
import requests,importlib.util
from bs4 import BeautifulSoup
spec=importlib.util.spec_from_file_location('lintsettingslive',ROOT/'source/authoring/style_lint.py');lint=importlib.util.module_from_spec(spec);spec.loader.exec_module(lint)
published=read('pages-published.json')['pages'];r=requests.get('https://wiki.swccg.com/api.php',params={'action':'query','format':'json','formatversion':2,'titles':'|'.join(x['title']for x in published),'prop':'revisions|flagged','rvprop':'ids|timestamp|content|user','rvslots':'main'},timeout=45);r.raise_for_status();fresh=r.json()['query']['pages'];files={};proof=[];prefix='authoring/pilots/443/settings-correction/live/'
for row in fresh:
 rev=row['revisions'][0];old=next(x for x in published if x['title']==row['title'])['revisions'][0];assert rev['revid']==old['revid']and rev['slots']['main']['content']==old['slots']['main']['content']and rev['user']=='Memory Core ChatGPT';text=rev['slots']['main']['content'];flags,_=lint.lint(text,row['title']);assert all(f.startswith('ARCHIVE ')for f in flags)
 p=requests.get('https://wiki.swccg.com/api.php',params={'action':'parse','format':'json','formatversion':2,'oldid':rev['revid'],'prop':'text|images|parsewarnings'},timeout=45).json()['parse'];dom=BeautifulSoup(p['text'],'html.parser');assert not p.get('parsewarnings')and not p['images']and not dom.select('.error,.mw-ext-cite-error');required=row['ns']==4
 if required:assert row['flagged']['stable_revid']==rev['revid']
 response=requests.get('https://wiki.swccg.com/wiki/'+row['title'].replace(' ','_'),timeout=45);response.raise_for_status();public=BeautifulSoup(response.content,'html.parser');link=public.select_one('#t-permalink a');assert link and('oldid='+str(rev['revid']))in link['href']
 path=prefix+str(rev['revid'])+'.wiki';files[path]=text.encode();proof.append({'title':row['title'],'revision':rev['revid'],'actor':rev['user'],'sha256':sha(text.encode()),'bytes':len(text.encode()),'review_required':required,'stable_revision':row.get('flagged',{}).get('stable_revid'),'raw_flags':flags,'native_public_qa':'PASS','path':path})
save('live-proof.json',{'pages':proof,'exact_revisions':3,'required_stable_reviews':2,'raw_archive_findings':sum(len(x['raw_flags'])for x in proof),'non_archive_findings':0,'card_article_text_or_image_edits':0,'archive_uploads':0});files[prefix+'live-proof.json']=(B/'live-proof.json').read_bytes()
for row in read('baseline.json')['query']['pages']:
 if row.get('revisions'):files[prefix+'before-'+str(row['revisions'][0]['revid'])+'.wiki']=row['revisions'][0]['slots']['main']['content'].encode()
backup=pin('billbisco/swccg-wiki','exact-live',files);receipts=[]
for row in proof:receipts.append(receipt(backup,row['path'],{'kind':'wiki_revision','title':row['title'],'revision_id':row['revision'],'content_sha256':row['sha256'],'bytes':row['bytes']}))
save('live-backup-receipts.json',{'commit':backup['commit'],'receipts':receipts,'independent_readback':True});print(json.dumps({'live_pages':3,'stable_reviews':2,'raw_archive_findings':sum(len(x['raw_flags'])for x in proof),'non_archive_findings':0,'exact_live_backup':backup['commit']}))
