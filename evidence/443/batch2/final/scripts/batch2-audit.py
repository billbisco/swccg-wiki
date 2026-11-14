from pilotlib import *
import requests,re,shutil
B=P/'batch2';B.mkdir(exist_ok=True);A=B/'assets';A.mkdir(exist_ok=True)
API='https://wiki.swccg.com/api.php'
def get(**kw):
 r=requests.get(API,params=dict(format='json',formatversion=2,**kw),timeout=45);r.raise_for_status();return r.json()
def put(n,v):(B/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for n in[443,382,445]:
 put(f'issue{n}.json',gh(f'repos/swccg-guild/work/issues/{n}'));put(f'comments{n}.json',gh(f'repos/swccg-guild/work/issues/{n}/comments?per_page=100'))
setpage=get(action='query',titles='Virtual Set 1: Legacy',prop='revisions',rvprop='ids|timestamp|content',rvslots='main')['query']['pages'][0];put('set.json',setpage)
rows=[]
for line in setpage['revisions'][0]['slots']['main']['content'].splitlines():
 m=re.match(r'^\|\s*(\d\d)\s*\|\|',line)
 if not m:continue
 files=re.findall(r'\[\[File:([^|\]]+)',line)
 if not files or not files[0].startswith('VS1O-'):continue
 target=re.search(r'\|link=([^\]]+)',line)[1]
 rows.append({'number':int(m[1]),'slip':files[0],'remaster':files[1],'target':target})
assert len(rows)==12
pages=get(action='query',titles='|'.join(r['target']for r in rows),redirects=1,prop='revisions',rvprop='ids|timestamp|content',rvslots='main');put('cards.json',pages)
files=get(action='query',titles='|'.join('File:'+r[k]for r in rows for k in['slip','remaster']),prop='imageinfo|revisions',iiprop='url|timestamp|size|mime|sha1',rvprop='ids|timestamp|content',rvslots='main');put('files.json',files)
hist=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-e-block-4/work/holotable/preservation-repo/historical-recovery/419')
names=['boshek','fusiongeneratorsupplytanks','gold1','hansheavyblasterpistol','lukeskywalker','saitorrkalfas','assaultrifle','black2','blasterrack','darthvader','fusiongeneratorsupplytanks','prophetess']
for row in rows:
 n=row['number'];row['slug']=names[n-1];side='Light'if n<=6 else'Dark';row['historical_member']=f'cards/starwars/Virtual1-{side}/large/{row["slug"]}.gif'
 src=hist/'large-v17'/row['historical_member'];dest=A/f'{n:02}-historical.gif';shutil.copyfile(src,dest);row['original_sha256']=sha(dest.read_bytes())
 for role in['slip','remaster']:
  f=next(x for x in files['query']['pages']if x['title'].replace(' ','_')==('File:'+row[role]).replace(' ','_'));info=f['imageinfo'][0];dest=A/f'{n:02}-{role}'+Path(row[role]).suffix if False else A/(f'{n:02}-{role}'+Path(row[role]).suffix)
  if not dest.exists():
   r=requests.get(info['url'],timeout=45);r.raise_for_status();dest.write_bytes(r.content)
  row[role+'_metadata']={**info,'sha256':sha(dest.read_bytes()),'file_revision':f['revisions'][0]['revid']}
 redirects={r['from']:r['to']for r in pages['query'].get('redirects',[])};title=redirects.get(row['target'],row['target']);page=next(x for x in pages['query']['pages']if x['title']==title);t=page['revisions'][0]['slots']['main']['content'];row['canonical']=title;row['revision']=page['revisions'][0]['revid'];row['fields']={m[1]:m[2]for m in re.finditer(r'^\|([a-z_0-9]+)=([^\n]*)',t,re.M)}
put('inventory.json',rows)
print(json.dumps({'cards':len(rows),'source_revision':setpage['revisions'][0]['revid'],'downloaded_images':24,'cards_brief':[{'n':x['number'],'title':x['canonical'],'uid':x['fields'].get('card_uid'),'text':x['fields'].get('game_text')}for x in rows]},ensure_ascii=True))
