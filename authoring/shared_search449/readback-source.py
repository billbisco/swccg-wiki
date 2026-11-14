import base64,hashlib,io,json,subprocess,tarfile
from pathlib import Path
p=Path(__file__).parent;commit=(p/'wiki-commit.txt').read_text().strip();path='authoring/shared_search449/source-data.tar.xz'
j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/contents/'+path+'?ref='+commit]))
if not j.get('content'):j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/git/blobs/'+j['sha']]))
raw=base64.b64decode(j['content']);assert raw==(p/'source-data.tar.xz').read_bytes();proof=[]
with tarfile.open(fileobj=io.BytesIO(raw),mode='r:xz') as archive:
    total=sum(m.size for m in archive if m.isfile())
    for member in archive:
        if not member.isfile():continue
        data=archive.extractfile(member).read();local=p/member.name
        if member.name.startswith('story-updates/'):local=p/Path(member.name).name
        assert local.read_bytes()==data,member.name
        proof.append(dict(member=member.name,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data)))
(p/'source-readback.json').write_text(json.dumps(dict(repository='https://github.com/billbisco/swccg-wiki',commit=commit,path=path,artifact_sha256=hashlib.sha256(raw).hexdigest(),artifact_bytes=len(raw),uncompressed_bytes=total,independent_remote_readback=True,members=proof),ensure_ascii=False,indent=2),encoding='utf8');print(len(proof),'exact source/data members independently restored before publication')
