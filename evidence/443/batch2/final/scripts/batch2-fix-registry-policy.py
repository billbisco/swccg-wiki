from b2common import *
prior=read('preflight-r2-registry.json');requests=[]
for row in prior['export']['objects']:
 requests.append(request(row['subject'],row['source'],row['backup_receipt'],row['source_backup_receipt'],row['source']['checked_evidence']))
result=register('policy-corrected',requests);save('active-preflight-registry.json',result)
print(json.dumps({'registered_policy_corrections':len(requests),'reads_allowed':True,'uploads_paused':True}))
