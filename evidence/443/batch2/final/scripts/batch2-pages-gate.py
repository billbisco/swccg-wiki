from b2common import *
draftpin=read('active-draft-pin.json');proofpin=read('backup-drafts-sources-r2.json');imagepin=read('backup-image-source-assets.json');evidence={'path':proofpin['repository']+'/blob/'+proofpin['commit']+'/authoring/pilots/443/batch2/source-accuracy.json','sha256':sha((B/'source-accuracy.json').read_bytes())};req=[]
for row in read('uploads-published.json')['pages']:
 r=next(x for x in read('plan.json')if x['title']==row['title']);info=row['imageinfo'][0];asset='preservation/443/batch2/assets/'+r['asset'];meta=imagepin['files'][asset]
 sub={'kind':'wiki_file_version','title':row['title'],'upload_timestamp':info['timestamp'],'original_version_url':info['url'],'content_sha256':meta['sha256'],'bytes':meta['bytes']};source={'url':info['url'],'sha256':meta['sha256'],'bytes':meta['bytes']};req.append(request(sub,source,receipt(imagepin,asset,sub),receipt(imagepin,asset,source_backup_subject(source)),evidence))
registered=register('new-upload-originals',req);registry=read('active-preflight-registry.json');ids={x['object_id']for x in registry['export']['objects']};registry['export']['objects'] += [x for x in registered['export']['objects']if x['object_id']not in ids]
originals=[{'object_id':r['object_id'],'subject':r['subject'],'evidence':evidence}for r in registry['export']['objects']if r['subject']['kind']=='wiki_file_version'];assert len(originals)==36
checks={r['title']:r for r in read('preview-checks.json')};pages=[]
for row in read('plan.json'):
 if row['kind']=='upload':continue
 data=(B/'drafts'/row['file']).read_bytes();sub={'kind':'wiki_draft','title':row['title'],'content_sha256':sha(data),'bytes':len(data)}
 pages.append({'title':row['title'],'subject':sub,'backup_receipt':receipt(draftpin,'authoring/pilots/443/batch2/drafts/'+row['file'],sub),'source_accuracy':{'status':'checked','evidence':evidence},'sources':[{'url':r['source']['url'],'object_id':r['object_id'],'evidence':evidence}for r in registry['export']['objects']if r['subject']==sub],'rendered_originals':checks[row['title']]['rendered_originals'],'original_versions':originals})
gate('pages',pages,registry,proofpin);save('combined-registry.json',registry)
