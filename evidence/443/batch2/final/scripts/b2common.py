import pilotlib as lib
from pilotlib import *
from concurrent.futures import ThreadPoolExecutor
ROOT=P;B=P/'batch2';lib.P=B;P=B
def request(subject,source,backup,source_backup,evidence):
 r=lib.request(subject,source,backup,source_backup,evidence)
 r['readiness']['reason']='Exact source/version and independent GitHub readback checked; Archive.org uploads and Save Page Now remain paused; reading/downloading allowed'
 r['continuation']='Story443: Bill explicitly allows Archive.org reads/downloads. Keep uploads, Save Page Now and saver/timer restarts paused. Existing central owner completes original-image replay verification and File Preservation links under the applicable read policy; submits preservation writes only after explicit resumption. No client staging/promotion.'
 r['approval_scope']['approval']='Bill approved the remaining nine OVS1 cards with exact text checks and repaired primary source references; viewing/downloading Archive.org explicitly allowed; preservation uploads remain paused'
 return r
def pin(repo,phase,files):
 checkpoint='backup-'+phase+'.json';R='repos/'+repo;ref=R+'/git/ref/heads/main'
 if(B/checkpoint).exists():result=read(checkpoint)
 else:
  def blob(item):
   name,data=item;r=gh(R+'/git/blobs','POST',{'encoding':'base64','content':base64.b64encode(data).decode()});return{'path':name,'mode':'100644','type':'blob','sha':r['sha']}
  with ThreadPoolExecutor(max_workers=4)as pool:entries=list(pool.map(blob,files.items()))
  for attempt in range(4):
   base=gh(ref)['object']['sha'];tree=gh(R+'/git/commits/'+base)['tree']['sha'];nt=gh(R+'/git/trees','POST',{'base_tree':tree,'tree':entries});head=gh(R+'/git/commits','POST',{'parents':[base],'tree':nt['sha'],'message':'Preserve exact OVS1 nine-card rollout '+phase+' (Refs swccg-guild/work#443)'})['sha']
   if gh(ref)['object']['sha']!=base:continue
   try:gh(R+'/git/refs/heads/main','PATCH',{'sha':head,'force':False})
   except RuntimeError:
    if gh(ref)['object']['sha']!=base:continue
    raise
   break
  else:raise RuntimeError('Concurrent backup movement; no force push')
  result={'repository':'https://github.com/'+repo,'commit':head,'files':{e['path']:{'blob':e['sha'],'sha256':sha(files[e['path']]),'bytes':len(files[e['path']])}for e in entries}}
 def restore(item):
  name,data=item;info=result['files'][name];blob=gh(R+'/git/blobs/'+info['blob']);assert base64.b64decode(blob['content'])==data,name
 with ThreadPoolExecutor(max_workers=4)as pool:list(pool.map(restore,files.items()))
 result.update(independent_readback=True,verified_at=now());save(checkpoint,result);return result

def gate(phase,pages,registry,proofpin):
 exportpath=phase+'-registry-export.json';save(exportpath,registry['export']);prefix='evidence/443/batch2/'+phase+'/'
 pinned=pin('billbisco/swccg-wiki',phase+'-registry',{prefix+exportpath:(B/exportpath).read_bytes()})
 proofpath='authoring/pilots/443/batch2/source-accuracy.json';uri=proofpin['repository']+'/blob/'+proofpin['commit']+'/'+proofpath;evidence={'path':uri,'sha256':sha((B/'source-accuracy.json').read_bytes())}
 manifest={'schema_version':1,'approval_scope':{'ticket':443,'approval':'Bill explicitly approved remaining nine OVS1 cards, matching exact text and repairing old/new image sources; existing publication workflow authorized; Archive.org uploads held'},'registry_export':{'path':exportpath,'sha256':sha((B/exportpath).read_bytes()),'storage':{'kind':'git','repository':pinned['repository'],'commit':pinned['commit'],'path':prefix+exportpath}},'evidence_files':[{'uri':uri,'sha256':evidence['sha256'],'path':'source-accuracy.json'}],'pages':pages}
 save(phase+'-manifest.json',manifest);mh=sha((B/(phase+'-manifest.json')).read_bytes());save(phase+'-approval.json',{'approved':True,'manifest_sha256':mh,'scope':'Bill-authorized exact OVS1 rollout, primary credits and pending external preservation'})
 def check(page):
  row=next(r for r in read('plan.json')if r['title']==page['title']);name=row['file'];cmd=['python',str(ROOT/'source/authoring/style_lint.py'),str(B/'drafts'/name),'--title',row['title'],'--publication-manifest',str(B/(phase+'-manifest.json')),'--approved-manifest-sha256',mh,'--report-json',str(B/(phase+'-'+name+'.report.json'))];r=subprocess.run(cmd,capture_output=True);(B/(phase+'-'+name+'.log')).write_bytes(r.stdout+r.stderr);assert r.returncode==0,(name,(r.stdout+r.stderr).decode(errors='replace')[-1600:]);return name
 with ThreadPoolExecutor(max_workers=4)as pool:list(pool.map(check,pages))
 print(json.dumps({'phase':phase,'gates':'PASS','pages':len(pages)}),flush=True);return mh
