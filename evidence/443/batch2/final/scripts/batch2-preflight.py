from b2common import *
import requests,importlib.util,re
from bs4 import BeautifulSoup
spec=importlib.util.spec_from_file_location('lint2',ROOT/'source/authoring/style_lint.py');lint=importlib.util.module_from_spec(spec);spec.loader.exec_module(lint)
plan=read('plan.json');baseline=read('baseline.json')['query']['pages'];checks=[]
def preview(row):
 text=(B/'drafts'/row['file']).read_text(encoding='utf-8');flags,_=lint.lint(text,row['title']);assert all(f.startswith('ARCHIVE ')for f in flags),(row['title'],flags)
 r=requests.post('https://wiki.swccg.com/api.php',data={'action':'parse','format':'json','formatversion':2,'title':row['title'],'text':text,'contentmodel':'wikitext','prop':'text|images|links|parsewarnings'},timeout=60);r.raise_for_status();v=r.json();assert'error'not in v,v;parsed=v['parse'];dom=BeautifulSoup(parsed['text'],'html.parser');assert not parsed.get('parsewarnings')and not dom.select('.error,.mw-ext-cite-error'),row['title'];(B/(row['file']+'.preview.html')).write_text(parsed['text'],encoding='utf-8')
 if row['kind']=='article':
  old=next(x for x in baseline if x['title']==row['title'])['revisions'][0]['slots']['main']['content']
  def keep(t):
   t=re.sub(r'^\|image(?:2|3|_note)?=.*\n','',t,flags=re.M);t=re.sub(r'(?ms)^\|sources=.*?(?=^\||^}})','',t);return t.strip()
  assert keep(old)==keep(text),(row['title'],'Nonimage/nonsource card content changed')
 return{'title':row['title'],'raw_flags':flags,'native_preview':'PASS','rendered_originals':['File:'+n for n in parsed['images']]}
with ThreadPoolExecutor(max_workers=4)as pool:checks=list(pool.map(preview,plan))
save('preview-checks.json',checks);print(json.dumps({'previews':len(checks),'non_archive_flags':0,'raw_archive_flags':sum(len(x['raw_flags'])for x in checks)}),flush=True)
assets={'preservation/443/batch2/assets/'+x.name:x.read_bytes()for x in(B/'assets').iterdir()if x.is_file()}
imagepin=pin('billbisco/swccg-wiki-files','image-source-assets',assets)
files={'authoring/pilots/443/batch2/drafts/'+r['file']:(B/'drafts'/r['file']).read_bytes()for r in plan}
for n in['source-accuracy.json','inventory.json','recipes.json','archive-checks.json','preview-checks.json']:files['authoring/pilots/443/batch2/'+n]=(B/n).read_bytes()
draftpin=pin('billbisco/swccg-wiki','drafts-sources-r2',files)
evidence={'path':draftpin['repository']+'/blob/'+draftpin['commit']+'/authoring/pilots/443/batch2/source-accuracy.json','sha256':sha((B/'source-accuracy.json').read_bytes())}
requests_list=[];source_defs={};rows=read('inventory.json')
for r in rows:
 n=r['number'];source_defs[r['recipe_url']]=f'{n:02}-recipe.json'
 if r['archive_source']:source_defs[r['archive_source']]=f'{n:02}-historical.gif'
source_defs[read('source-accuracy.json')['publisher_pdf']['url']]='PC-VirtualCards1-20071024153847.pdf'
source_defs['https://raw.githubusercontent.com/billbisco/swccg-holotable/033d17f68e6ac51848323d353216a685f920f575/historical-recovery/419/large-v17/cards/starwars/Virtual1-Light/large/saitorrkalfas.gif']='06-historical.gif'
source_defs['https://github.com/swccg-guild/work/issues/443']=None
for row in plan:
 data=(B/'drafts'/row['file']).read_bytes();sub={'kind':'wiki_draft','title':row['title'],'content_sha256':sha(data),'bytes':len(data)};backup=receipt(draftpin,'authoring/pilots/443/batch2/drafts/'+row['file'],sub)
 urls=re.findall(r'https?://[^\s\]<>]+',data.decode());urls=sorted({u.split('#')[0]for u in urls})
 for url in urls:
  if url in source_defs and source_defs[url]:
   asset='preservation/443/batch2/assets/'+source_defs[url];meta=imagepin['files'][asset];source={'url':url,'sha256':meta['sha256'],'bytes':meta['bytes']};requests_list.append(request(sub,source,backup,receipt(imagepin,asset,source_backup_subject(source)),evidence))
  elif url=='https://github.com/swccg-guild/work/issues/443':
   # Talk's internal work reference is not an external factual citation; retain a checked issue snapshot.
   asset='authoring/pilots/443/batch2/issue443.json'
   if not(B/'backup-work-issue.json').exists():pin('billbisco/swccg-wiki','work-issue',{asset:(B/'issue443.json').read_bytes()})
   ip=read('backup-work-issue.json');meta=ip['files'][asset];source={'url':url,'sha256':meta['sha256'],'bytes':meta['bytes']};requests_list.append(request(sub,source,backup,receipt(ip,asset,source_backup_subject(source)),evidence))
  else:raise AssertionError(('Uninventoried external source',row['title'],url))
# Public originals already present: remasters/slips plus the four historical GIFs from the pilot/Versions work.
for row in rows:
 n=row['number']
 for role in['original','slip','remaster']:
  title='File:'+row[role];old=next(x for x in baseline if x['title'].replace(' ','_')==title.replace(' ','_'))
  if old.get('missing'):continue
  info=old['imageinfo'][0];asset=f'{n:02}-historical.gif'if role=='original'else f'{n:02}-{role}'+Path(row[role]).suffix;data=(B/'assets'/asset).read_bytes()
  r=requests.get(info['url'],timeout=45);r.raise_for_status();assert r.content==data
  sub={'kind':'wiki_file_version','title':old['title'],'upload_timestamp':info['timestamp'],'original_version_url':info['url'],'content_sha256':sha(data),'bytes':len(data)};source={'url':info['url'],'sha256':sha(data),'bytes':len(data)};ap='preservation/443/batch2/assets/'+asset
  requests_list.append(request(sub,source,receipt(imagepin,ap,sub),receipt(imagepin,ap,source_backup_subject(source)),evidence))
registry=register('preflight-r2',requests_list);save('source-definitions.json',source_defs)
pages=[]
for row in plan:
 if row['kind']!='upload':continue
 data=(B/'drafts'/row['file']).read_bytes();sub={'kind':'wiki_draft','title':row['title'],'content_sha256':sha(data),'bytes':len(data)}
 pages.append({'title':row['title'],'subject':sub,'backup_receipt':receipt(draftpin,'authoring/pilots/443/batch2/drafts/'+row['file'],sub),'source_accuracy':{'status':'checked','evidence':evidence},'sources':[{'url':r['source']['url'],'object_id':r['object_id'],'evidence':evidence}for r in registry['export']['objects']if r['subject']==sub],'rendered_originals':[],'original_versions':[{'object_id':r['object_id'],'subject':r['subject'],'evidence':evidence}for r in registry['export']['objects']if r['subject']['kind']=='wiki_file_version']})
gate('uploads',pages,registry,draftpin)
