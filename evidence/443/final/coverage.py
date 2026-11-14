from pilotlib import *
import requests,re
API='https://wiki.swccg.com/api.php'
v=requests.get(API,params={'action':'query','format':'json','formatversion':2,'titles':'Virtual Set 1: Legacy','prop':'revisions','rvprop':'ids|content','rvslots':'main'},timeout=40).json()['query']['pages'][0];text=v['revisions'][0]['slots']['main']['content'];rows=[]
names={1:'boshek',2:'fusiongeneratorsupplytanks',3:'gold1',4:'hansheavyblasterpistol',5:'lukeskywalker',6:'saitorrkalfas',7:'assaultrifle',8:'black2',9:'blasterrack',10:'darthvader',11:'fusiongeneratorsupplytanks',12:'prophetess'}
root=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-e-block-4/work/holotable/preservation-repo/historical-recovery/419/large-v17/cards/starwars')
for line in text.splitlines():
 m=re.match(r'^\|\s*(\d\d)\s*\|\|',line)
 if not m:continue
 n=int(m[1]);files=re.findall(r'\[\[File:([^|\]]+)',line);
 if not files or not files[0].startswith('VS1O-'):continue
 assert len(files)==2
 historical=root/f'Virtual1-{"Light"if n<=6 else"Dark"}/large/{names[n]}.gif'
 rows.append({'number':n,'publisher_slip':files[0],'remaster':files[1],'historical_distribution_payload_locally_available':historical.is_file(),'exact_state_compatibility_checked_for443':n in[1,9,10],'pilot_activated':n in[1,9,10],'disposition':'Verified review example'if n in[1,9,10]else'Candidate only: audit exact publication/text state and language before enabling; no rollout authorized by filename availability'})
assert len(rows)==12
titles=['File:'+r[k]for r in rows for k in ['publisher_slip','remaster']];metadata=requests.get(API,params={'action':'query','format':'json','formatversion':2,'titles':'|'.join(titles),'prop':'imageinfo','iiprop':'url|timestamp|size|mime'},timeout=40).json()['query']['pages'];bytitle={r['title'].replace(' ','_'):r for r in metadata}
for r in rows:
 for role in ['publisher_slip','remaster']:
  info=bytitle[('File:'+r[role]).replace(' ','_')];r[role+'_exists']=not info.get('missing',False)
boundary=[]
for title in ['Darth Vader (V) (Virtual Set 1) (Errata 2)','Virtual Set 1: Legacy','Darth Vader','SWCCG Wiki:Samples/Original Virtual Luke Skywalker image viewer']:
 response=requests.get('https://wiki.swccg.com/wiki/'+title.replace(' ','_'),timeout=40);response.raise_for_status();assert'"swccgCardImagePilot"'not in response.text
 boundary.append({'title':title,'http':response.status_code,'new_viewer_activated':False})
report={'cohort':'Original Virtual Set1 pilot','set_revision':v['revisions'][0]['revid'],'set_cards':len(rows),'activated_review_examples':3,'other_candidates_not_activated':9,'raw_source_payload_availability_not_eligibility':True,'rows':rows,'shared_consumers':[{'consumer':'Template:Card','observed_revision':306969,'change':'No template edit; existing three portrait slots plus explicit scoped marker'},{'consumer':'MediaWiki:Common.js portrait/thumbnail hover','observed_revision':210284,'change':'Unchanged; hover resolves the visible source image via existing File links'},{'consumer':'MediaWiki:Common.css card rails/tables','observed_revision':261879,'change':'Unchanged; new styling limited to viewer class and allowlisted pages'},{'consumer':'Set-table card thumbnails','change':'Not activated; resolver integration remains future rollout'},{'consumer':'Existing Luke review sample','change':'Legacy hook retained; not activated by the new viewer'}],'boundaries':boundary,'whole_wiki_inventory_complete':False,'all443_acceptance_criteria_complete':False,'archive_org_requests':0}
save('coverage.json',report);print(json.dumps({'set_cards':len(rows),'pilot':3,'candidate_only':9,'unaffected_boundaries_checked':len(boundary)}))
