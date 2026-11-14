from b2common import *
draftpin=read('backup-drafts-sources-r2.json');registry=read('active-preflight-registry.json');evidence={'path':draftpin['repository']+'/blob/'+draftpin['commit']+'/authoring/pilots/443/batch2/source-accuracy.json','sha256':sha((B/'source-accuracy.json').read_bytes())};pages=[]
for row in read('plan.json'):
 if row['kind']!='upload':continue
 data=(B/'drafts'/row['file']).read_bytes();sub={'kind':'wiki_draft','title':row['title'],'content_sha256':sha(data),'bytes':len(data)}
 pages.append({'title':row['title'],'subject':sub,'backup_receipt':receipt(draftpin,'authoring/pilots/443/batch2/drafts/'+row['file'],sub),'source_accuracy':{'status':'checked','evidence':evidence},'sources':[{'url':r['source']['url'],'object_id':r['object_id'],'evidence':evidence}for r in registry['export']['objects']if r['subject']==sub],'rendered_originals':[],'original_versions':[{'object_id':r['object_id'],'subject':r['subject'],'evidence':evidence}for r in registry['export']['objects']if r['subject']['kind']=='wiki_file_version']})
gate('uploads-r3',pages,registry,draftpin)
