from pathlib import Path
import json,sys,base64,hashlib,datetime
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent.parent/'wiki-tcgmix-expanded'))
from backup import gh
R='repos/billbisco/swccg-wiki-files';REF=R+'/git/ref/heads/main';PREFIX='preservation/issue-382-offline-historical-sample-20261114/'
def save(n,v):(P/n).write_bytes((json.dumps(v,indent=2)+'\n').encode())
def read(n):return json.loads((P/n).read_bytes())
report=read('restore-report.json');assert report['archive_org_requests']==0 and report['sample_versions']==10
if (P/'sample-backup-receipts.json').exists():print(json.dumps({'existing_commit':read('sample-backup-receipts.json')['commit']}));raise SystemExit(0)
assert gh('user')['login']=='billbisco'
files={PREFIX+'restore-report.json':(P/'restore-report.json').read_bytes()}
for row in report['rows']:
 data=(P/row['isolated_path']).read_bytes();assert hashlib.sha256(data).hexdigest()==row['sha256']and len(data)==row['bytes']
 files[PREFIX+'objects/'+row['sha256']]=data
if(P/'sample-prepared-blobs.json').exists():prepared=read('sample-prepared-blobs.json')
else:
 prepared={}
 for path,data in files.items():prepared[path]=gh(R+'/git/blobs','POST',{'encoding':'base64','content':base64.b64encode(data).decode()})['sha']
 save('sample-prepared-blobs.json',prepared)
for attempt in range(3):
 base=gh(REF)['object']['sha'];tree=gh(R+'/git/commits/'+base)['tree']['sha']
 nt=gh(R+'/git/trees','POST',{'base_tree':tree,'tree':[{'path':path,'mode':'100644','type':'blob','sha':prepared[path]}for path in files]});head=gh(R+'/git/commits','POST',{'parents':[base],'tree':nt['sha'],'message':'Preserve and independently restore bounded historical image sample (Refs swccg-guild/work#382)'})['sha']
 if gh(REF)['object']['sha']!=base:continue
 gh(R+'/git/refs/heads/main','PATCH',{'sha':head,'force':False});break
else:raise RuntimeError('Repeated concurrent image-backup head movement; no force write')
for path,data in files.items():
 info=gh(R+'/contents/'+path+'?ref='+head);assert info['sha']==prepared[path];blob=gh(R+'/git/blobs/'+info['sha']);restored=base64.b64decode(blob['content']);assert restored==data
now=datetime.datetime.now(datetime.timezone.utc).isoformat();receipts=[]
for row in report['rows']:
 receipts.append({'schema_version':1,'subject':{'kind':'wiki_file_version','title':row['title'],'content_sha256':row['sha256'],'bytes':row['bytes'],'upload_timestamp':row['timestamp'],'original_version_url':row['url']},'storage':{'kind':'git','repository':'https://github.com/billbisco/swccg-wiki-files','commit':head,'path':PREFIX+'objects/'+row['sha256']},'verification':{'status':'verified','independent':True,'restored_sha256':row['sha256'],'restored_bytes':row['bytes'],'verified_at':now},'inventory_version_id':row['id']})
out={'commit':'https://github.com/billbisco/swccg-wiki-files/commit/'+head,'github_main_verified':True,'files_read_back':len(files),'image_versions':len(receipts),'unique_image_payloads':len(files)-1,'archive_org_requests':0,'receipts':receipts}
save('sample-backup-receipts.json',out);print(json.dumps({k:v for k,v in out.items()if k!='receipts'}))
