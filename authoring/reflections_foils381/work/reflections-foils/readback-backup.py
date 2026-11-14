"""Independently fetch immutable remote Git blobs into a separate object store."""
import hashlib,json,os,subprocess,sys,threading
from pathlib import Path
root=Path(__file__).parent;mode=sys.argv[1];assert mode in ['wiki','images']
commit=(root/(mode+'-commit.txt')).read_text().strip()
repository='billbisco/swccg-wiki'+('-files' if mode=='images' else '')
independent=root/('remote-readback-'+mode+'.git')
env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):return subprocess.check_output(['git','-C',str(independent),*args],input=data,env=env)
if not independent.exists():subprocess.run(['git','init','--bare',str(independent)],check=True,stdout=subprocess.DEVNULL)
if not git('remote').strip():git('remote','add','origin','https://github.com/'+repository+'.git')
git('config','remote.origin.promisor','true');git('config','remote.origin.partialclonefilter','blob:none')
git('fetch','--filter=blob:none','--depth=1','--no-tags','origin',commit)
entries={}
for record in git('ls-tree','-rz','--full-tree',commit).split(b'\0'):
    if not record:continue
    metadata,path=record.split(b'\t',1);mode_,kind,oid=metadata.decode().split()
    if kind=='blob':entries[path.decode()]=oid
expected={}
if mode=='wiki':
    # The authoritative saved path mapping is independently fetched as a blob.
    git('fetch','--no-tags','origin',entries['pages/INDEX.tsv'])
    index=git('show',commit+':pages/INDEX.tsv').decode()
    paths=dict(line.split('\t',1) for line in index.splitlines() if '\t' in line)
    for title,h in json.loads((root/'published-heads.json').read_bytes()).items():
        data=(h['revisions'][0]['slots']['main']['content'].rstrip()+'\n').encode()
        expected[paths[title]]=dict(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),title=title,revision_id=h['revisions'][0]['revid'])
else:
    for row in json.loads((root/'uploaded-images.json').read_bytes()):
        expected['files/'+row['name']]=dict(sha256=row['sha256'],bytes=(root/row['local_file']).stat().st_size,title=row['title'])
oids=list(dict.fromkeys(entries[path] for path in expected))
checked=git('cat-file','--batch-check=%(objectname) %(objecttype)',data=('\n'.join(oids)+'\n').encode()).decode().splitlines()
missing=[line.split()[0] for line in checked if line.endswith(' missing')]
if missing:git('fetch','--no-tags','origin','--stdin',data=('\n'.join(missing)+'\n').encode())
print(mode,len(expected),'remote paths fetched; checking raw blob SHA-256/bytes',flush=True)
process=subprocess.Popen(['git','-C',str(independent),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,env=env)
def write():
    process.stdin.write(('\n'.join(oids)+'\n').encode());process.stdin.close()
writer=threading.Thread(target=write);writer.start();actual={}
for oid in oids:
    header=process.stdout.readline().decode().split();assert header[0]==oid and header[1]=='blob',header
    size=int(header[2]);remaining=size;digest=hashlib.sha256()
    while remaining:
        chunk=process.stdout.read(min(remaining,1024*1024));assert chunk;digest.update(chunk);remaining-=len(chunk)
    assert process.stdout.read(1)==b'\n'
    actual[oid]=dict(sha256=digest.hexdigest(),bytes=size)
writer.join();assert process.wait()==0
receipts=[]
for path,want in expected.items():
    got=actual[entries[path]];assert got['sha256']==want['sha256'] and got['bytes']==want['bytes'],path
    receipts.append(dict(repository='https://github.com/'+repository,commit=commit,path=path,blob_sha1=entries[path],independently_restored=True,**want))
(root/(mode+'-independent-readback.json')).write_text(json.dumps(dict(method='Independent remote Git fetch into separate bare object store, exact immutable path/blob raw-byte SHA-256 and size comparison; no local alternates',repository=repository,commit=commit,paths=receipts,passed=True),ensure_ascii=False,indent=2),encoding='utf8')
print(mode,len(receipts),'immutable remote payload readbacks match SHA-256 and byte count',flush=True)
