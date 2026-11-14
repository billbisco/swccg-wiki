from b3common import *
import requests,importlib.util
from bs4 import BeautifulSoup
spec=importlib.util.spec_from_file_location('lintsettings',ROOT/'source/authoring/style_lint.py');lint=importlib.util.module_from_spec(spec);spec.loader.exec_module(lint);checks=[]
for row in read('plan.json'):
 text=(B/'drafts'/row['file']).read_bytes().decode();flags,_=lint.lint(text,row['title']);assert all(f.startswith('ARCHIVE ')for f in flags),flags
 r=requests.post('https://wiki.swccg.com/api.php',data={'action':'parse','format':'json','formatversion':2,'title':row['title'],'text':text,'contentmodel':'wikitext','prop':'text|images|parsewarnings'},timeout=50);r.raise_for_status();v=r.json()['parse'];dom=BeautifulSoup(v['text'],'html.parser');assert not v.get('parsewarnings')and not dom.select('.error,.mw-ext-cite-error')and not v['images'];checks.append({'title':row['title'],'raw_flags':flags,'native_preview':'PASS','rendered_originals':[]})
save('preview-checks.json',checks)
files={'authoring/pilots/443/settings-correction/drafts/'+r['file']:(B/'drafts'/r['file']).read_bytes()for r in read('plan.json')}
for n in['source-accuracy.json','issue.json','preview-checks.json']:files['authoring/pilots/443/settings-correction/'+n]=(B/n).read_bytes()
dp=pin('billbisco/swccg-wiki','drafts',files);evidence={'path':dp['repository']+'/blob/'+dp['commit']+'/authoring/pilots/443/settings-correction/source-accuracy.json','sha256':sha((B/'source-accuracy.json').read_bytes())};req=[];pages=[]
for row in read('plan.json'):
 data=(B/'drafts'/row['file']).read_bytes();sub={'kind':'wiki_draft','title':row['title'],'content_sha256':sha(data),'bytes':len(data)};back=receipt(dp,'authoring/pilots/443/settings-correction/drafts/'+row['file'],sub)
 if row['file']=='talk-hub.wiki':
  data=(B/'issue.json').read_bytes();source={'url':'https://github.com/swccg-guild/work/issues/443','sha256':sha(data),'bytes':len(data)};req.append(request(sub,source,back,receipt(dp,'authoring/pilots/443/settings-correction/issue.json',source_backup_subject(source)),evidence))
 pages.append({'title':row['title'],'subject':sub,'backup_receipt':back,'source_accuracy':{'status':'checked','evidence':evidence},'sources':[],'rendered_originals':[],'original_versions':[]})
reg=register('sources',req)
for page in pages:page['sources']=[{'url':r['source']['url'],'object_id':r['object_id'],'evidence':evidence}for r in reg['export']['objects']if r['subject']==page['subject']]
gate('pages',pages,reg,dp)
