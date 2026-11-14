from b2common import *
import re,requests
plan=read('plan.json');changed=[]
for row in plan:
 if row['kind']!='article':continue
 path=B/'drafts'/row['file'];text=path.read_bytes().decode();match=re.search(r'(?ms)^\|sources=(.*?)(?=^\||^}})',text);assert match
 lines=match[1].splitlines();kept=[]
 for line in lines:
  if line.startswith('* Full-card remaster:'):continue
  if line.startswith('* [')and'VirtualCards1.pdf'in line:continue
  kept.append(line)
 new=text[:match.start(1)]+'\n'.join(kept)+'\n'+text[match.end(1):]
 if new!=text:path.write_bytes(new.encode());changed.append(row)
for row in changed:
 text=(B/'drafts'/row['file']).read_bytes().decode();r=requests.post('https://wiki.swccg.com/api.php',data={'action':'parse','format':'json','formatversion':2,'title':row['title'],'text':text,'prop':'text|parsewarnings'},timeout=50);r.raise_for_status();v=r.json();assert not v['parse'].get('parsewarnings')and'mw-ext-cite-error'not in v['parse']['text']
files={'authoring/pilots/443/batch2/drafts/'+r['file']:(B/'drafts'/r['file']).read_bytes()for r in plan};newpin=pin('billbisco/swccg-wiki','deduplicated-drafts',files);save('active-draft-pin.json',newpin)
old=read('active-preflight-registry.json');evidence={'path':read('backup-drafts-sources-r2.json')['repository']+'/blob/'+read('backup-drafts-sources-r2.json')['commit']+'/authoring/pilots/443/batch2/source-accuracy.json','sha256':sha((B/'source-accuracy.json').read_bytes())};requests_list=[]
for row in changed:
 data=(B/'drafts'/row['file']).read_bytes();sub={'kind':'wiki_draft','title':row['title'],'content_sha256':sha(data),'bytes':len(data)};backup=receipt(newpin,'authoring/pilots/443/batch2/drafts/'+row['file'],sub)
 original=[r for r in old['export']['objects']if r['subject']['kind']=='wiki_draft'and r['subject']['title']==row['title']]
 assert len(original)==3
 for r in original:requests_list.append(request(sub,r['source'],backup,r['source_backup_receipt'],evidence))
updates=register('deduplicated-source-bindings',requests_list);old['export']['objects'] += updates['export']['objects'];save('active-preflight-registry.json',old)
print(json.dumps({'canonical_sources_deduplicated':len(changed),'source_bindings':len(requests_list)}))
