from pilotlib import *
import requests,re,shutil
B=P/'batch2';D=B/'drafts';D.mkdir(exist_ok=True);A=B/'assets';API='https://wiki.swccg.com/api.php'
def put(n,v):(B/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def get(**kw):
 r=requests.get(API,params=dict(format='json',formatversion=2,**kw),timeout=50);r.raise_for_status();return r.json()
rows=json.loads((B/'inventory.json').read_bytes());recipes=json.loads((B/'recipes.json').read_bytes());H=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-e-block-4/work/holotable/preservation-repo/historical-recovery/419');cdx=json.loads((H/'metadata/archive-original-virtual-cdx.json').read_bytes())
oldsource=Path('C:/Users/gythe/Documents/Codex/2026-10-27/wher/work/set1-history-implementation/source-accuracy.json');pdf=next(x for x in json.loads(oldsource.read_bytes())['sources']if x['key']=='pc2006');shutil.copyfile(pdf['local_source'],A/'PC-VirtualCards1-20071024153847.pdf');assert sha((A/'PC-VirtualCards1-20071024153847.pdf').read_bytes())==pdf['subject']['content_sha256']
PDF=pdf['url'];PCPDF=PDF+'#page='
keys=['boshek','fusion-light','gold1','hans-pistol','luke','saitorr','assault-rifle','black2','blaster-rack','vader','fusion-dark','prophetess']
labels=['BoShek','Fusion Generator Supply Tanks (Light)','Gold 1',"Han's Heavy Blaster Pistol",'Luke Skywalker',"Sai'torr Kal Fas",'Assault Rifle','Black 2','Blaster Rack','Darth Vader','Fusion Generator Supply Tanks (Dark)','Prophetess']
filelabels=['BoShek','Fusion-Generator-Supply-Tanks-Light','Gold-1','Hans-Heavy-Blaster-Pistol','Luke-Skywalker','Saitorr-Kal-Fas','Assault-Rifle','Black-2','Blaster-Rack','Darth-Vader','Fusion-Generator-Supply-Tanks-Dark','Prophetess']
manifest=json.loads((P/'source/chrome/card-image-pilot.json').read_bytes());manifest['cards']={}
proof=[];plan=[];targets=[]
for r,label,key,fl in zip(rows,labels,keys,filelabels):
 n=r['number'];r.update(key=key,label=label,original='Holotable-OVS1-'+fl+'-v17.gif');data=(A/f'{n:02}-historical.gif').read_bytes();digest=base64.b32encode(hashlib.sha1(data).digest()).decode();match=next((x for x in cdx if x[5]==digest),None)
 r['archive_source']=('https://web.archive.org/web/'+match[1]+'/'+match[2])if match else None;r['pc_original_url']=match[2]if match else None;r['recipe_url']=recipes[n-1]['url'];r['pdf_page']=2
 manifest['pages'][r['canonical']]=True;state=r['fields']['card_uid']+':PC-E2';manifest['cards'][key]={'label':label,'state':state,'language':'en','slip':r['slip'],'renditions':[{'kind':'original','state':state,'language':'en','file':r['original'],'sha256':r['original_sha256']},{'kind':'remastered','state':state,'language':'en','file':r['remaster'],'sha256':r['remaster_metadata']['sha256']}]}
 targets+=['File:'+r['original'],'File:'+r['remaster'],'File:'+r['slip'],r['canonical']]
 matchnote='Original/remaster/slip title, game text, printed symbols and supported stats checked visually. All agree; artwork/typography variation is presentation only.'
 proof.append({'number':n,'card':r['canonical'],'state':state,'language':'en','result':'PASS','original_sha256':r['original_sha256'],'remaster_sha256':r['remaster_metadata']['sha256'],'slip_sha256':r['slip_metadata']['sha256'],'literal_game_text':recipes[n-1]['recipe']['game_text'],'lore':recipes[n-1]['recipe']['lore'],'stats':recipes[n-1]['recipe']['stats'],'icons':recipes[n-1]['recipe']['icons'],'checked':matchnote,'archive_source':r['archive_source'],'archive_cdx_sha1_matches_payload':bool(match),'archive_replay_verification':'Separate archive-checks.json; indexed digest equality is not replay verification','recipe':r['recipe_url'],'pdf_source':PDF,'original_package_member':r['historical_member']})
samples={1:'SWCCG Wiki:Samples/Original Virtual BoShek card images',9:'SWCCG Wiki:Samples/Original Virtual Blaster Rack card images',10:'SWCCG Wiki:Samples/Original Virtual Darth Vader image viewer'}
hub='SWCCG Wiki:Samples/Original Virtual card images';talk='SWCCG Wiki talk:Samples/Original Virtual card images';targets+=list(samples.values())+[hub,talk]
baseline=[]
for i in range(0,len(targets),45):baseline+=get(action='query',titles='|'.join(targets[i:i+45]),prop='revisions|imageinfo|flagged',rvprop='ids|timestamp|content',rvslots='main',iiprop='url|timestamp|size|sha1|mime')['query']['pages']
put('baseline.json',{'query':{'pages':baseline}})
def page(t):return next(x for x in baseline if x['title'].replace(' ','_')==t.replace(' ','_'))
def oldtext(t):return page(t).get('revisions',[{}])[0].get('slots',{}).get('main',{}).get('content','')
def draft(title,name,text,kind,asset=None):
 (D/name).write_bytes((text.rstrip()+'\n').encode());plan.append({'title':title,'file':name,'kind':kind,'asset':asset,'base':page(title).get('revisions',[{}])[0].get('revid')})
def origin(r):
 return (f"* Historical PC full-card image: [{r['archive_source']} {r['label']}], swccgpc.com (Internet Archive, 18 December 2007).\n"if r['archive_source']else '* Recovered Holotable image: [https://raw.githubusercontent.com/billbisco/swccg-holotable/033d17f68e6ac51848323d353216a685f920f575/historical-recovery/419/large-v17/cards/starwars/Virtual1-Light/large/saitorrkalfas.gif exact distribution member].\n')+f"* Publisher slip and card text: [{PCPDF+str(r['pdf_page'])} VirtualCards1.pdf, page {r['pdf_page']}, card {r['number']:02}], Players Committee; official text as of 4 December 2006 (Internet Archive, 24 October 2007)."
for r in rows:
 n=r['number'];source=origin(r);recipe=f"* CardMaker reconstruction recipe: [{r['recipe_url']} card {n:02}], billbisco/swccg-cardmaker."
 title='File:'+r['original'];old=oldtext(title);new=f"Historical full-card image of [[{r['canonical']}|{r['label']}]], matching the later [[Virtual Set 1: Legacy]] publisher slip. It combines the underlying Decipher card and the Virtual slip. The same image was recovered unchanged from the Holotable large-image distribution through Virtual Set 17.\n\n== Source ==\n{source}\n* Distribution member: <code>{r['historical_member']}</code>.\n"
 # Keep independent source/preservation notes already placed by other work.
 if old:
  tail=re.search(r'(?ms)^== Preservation ==.*',old)
  if tail:new+='\n'+tail[0]
 new+='\n== Related images ==\n'+f"* Publisher slip: [[:File:{r['slip']}]].\n* Later CardMaker reconstruction: [[:File:{r['remaster']}]].\n"
 draft(title,f'{n:02}-original.wiki',new,'file'if not page(title).get('missing')else'upload',f'{n:02}-historical.gif')
 for role in['remaster','slip']:
  title='File:'+r[role];old=oldtext(title)
  addition=('\n\n== Source ==\n'+source+'\n'+recipe+'\n* Reconstruction of the underlying Decipher card and the PC slip; generated with [[Making Custom SWCCG Cards|CardMaker]].\n')if role=='remaster'else'\n\n== Source ==\n'+f"* [{PCPDF+str(r['pdf_page'])} VirtualCards1.pdf, page {r['pdf_page']}, card {n:02}], Players Committee; official text as of 4 December 2006 (Internet Archive, 24 October 2007).\n"
  assert not re.search(r'^== Source ==',old,re.M),'Concurrent source section needs explicit merge'
  draft(title,f'{n:02}-{role}.wiki',old.rstrip()+addition,'file')
 for title in [r['canonical']]+([samples[n]]if n in samples else[]):
  old=oldtext(title);new=old
  if title==r['canonical']:
   new=re.sub(r'^\|image=.*$',lambda m:'|image='+r['original'],new,flags=re.M);new=re.sub(r'^\|image2=.*$',lambda m:'|image2='+r['remaster'],new,flags=re.M)
   assert not re.search(r'^\|image3=',new,re.M)
   new=new.replace('|image2='+r['remaster'],'|image2='+r['remaster']+'\n|image3='+r['slip']+'\n|image_note=<span class="swccg-card-image-marker" data-card-image-key="'+r['key']+'">Original and Remastered images of the same English publication; matching publisher slip.</span>')
  # Add primary inputs before existing sources without deleting historical citations.
  assert '|sources='in new
  new=new.replace('|sources=', '|sources='+source+'\n'+recipe+'\n',1)
  draft(title,f'{n:02}-'+('article'if title==r['canonical']else'sample')+'.wiki',new,'article'if title==r['canonical']else'sample')
text=oldtext(hub);text=text.replace('== Examples ==','== Review examples ==');text+='\n\n== Original Virtual Set 1 ==\nThe matching Original and Remastered images are available on each of the twelve later card publications:\n\n'+ '\n'.join(f"* [[{r['canonical']}|{r['number']:02} — {r['label']}]]"for r in rows)+'\n'
draft(hub,'hub.wiki',text,'hub')
note='\n\n== Original Virtual Set 1 expansion and primary image sources ==\n\nAll twelve later English PC-E2 card publications have matching historical full-card images, CardMaker reconstructions and publisher slips. The nine newly audited pairs agree on printed game text and symbols. Existing publication histories and Versions navigation are retained. Source sections now identify the historical PC image capture, original PC sheet and reconstruction recipe separately from wiki copies. Eleven historical payloads match the archived PC image index digests; this alone does not establish replay verification. See the exact checks and any rate-limited replay results in [[github:swccg-guild/work/issues/443|Story 443]]. Archive.org viewing and downloads are allowed; uploads and Save Page Now remain paused. Source credit and wiki-original preservation are separate records. ~~~~\n'
note=note.replace('[[github:swccg-guild/work/issues/443|Story 443]]','[https://github.com/swccg-guild/work/issues/443 Story 443]')
draft(talk,'talk-hub.wiki',oldtext(talk).rstrip()+note,'talk')
put('plan.json',plan);put('inventory.json',rows);put('source-accuracy.json',{'ticket':443,'cohort':'Twelve Original Virtual Set1 PC-E2 articles, plus retained three review samples','cards':proof,'publisher_pdf':pdf,'source_index':str(H/'metadata/archive-original-virtual-cdx.json'),'archive_policy':'Read/download allowed; uploads, Save Page Now and saver/timer restart paused','preservation_complete':False,'canonical_gameplay_text_and_versions_unchanged':True})
(P/'source/chrome/card-image-pilot.json').write_bytes((json.dumps(manifest,indent=2,ensure_ascii=False)+'\n').encode())
print(json.dumps({'drafts':len(plan),'uploads':sum(x['kind']=='upload'for x in plan),'canonical_articles':12,'existing_samples':3,'activated_titles':len(manifest['pages']),'source_pdf_sha256':pdf['subject']['content_sha256']}))
