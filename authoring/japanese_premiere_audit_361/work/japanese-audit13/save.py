from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys

root=Path('work/japanese-audit13')
kind=sys.argv[1]
repo={'wiki':'work/wiki-source','images':'work/japanese-files-backup.git','evidence':'work/japanese-preservation/evidence-repo'}[kind]
env=dict(os.environ,GIT_INDEX_FILE=str((root/(kind+'-backup.index')).resolve()),GIT_NO_LAZY_FETCH='1')
def git(*args,data=None):
    return subprocess.check_output(['git','-C',repo,'-c','core.protectNTFS=false',*args],input=data,env=env)
def save(parent,files):
    git('read-tree',parent)
    updates=[]
    for path,binary in files.items():
        oid=git('hash-object','-w','--stdin',data=binary).decode().strip()
        updates.append(f'100644 {oid}\t{path}\0')
    git('update-index','--info-only','-z','--index-info',data=''.join(updates).encode())
    tree=git('write-tree','--missing-ok').decode().strip()
    commit=git('commit-tree',tree,'-p',parent,'-m',f'Complete Japanese Premiere verified content audit and integration findings (#361; {kind})').decode().strip()
    changes=git('diff-tree','--no-commit-id','--name-only','-r',commit).decode().splitlines()
    assert set(changes)<=set(files),changes
    return commit,changes

for attempt in range(3):
    git('fetch','origin','main')
    parent=git('rev-parse','FETCH_HEAD').decode().strip()
    files={}
    if kind=='images':
        for record in json.loads((root/'better-faces.json').read_bytes()):
            n=185 if record['id']=='12508' else 25
            files[f'files/Japanese-Premiere-1301-{n}o-SWCA.jpg']=(root/('original-'+record['id']+'.jpg')).read_bytes()
    elif kind=='wiki':
        sys.path.insert(0,'work/wiki-tools')
        from dump_live import wiki_fname
        index=dict(line.split('\t',1) for line in git('show',parent+':pages/INDEX.tsv').decode().splitlines() if '\t' in line)
        heads=json.loads((root/'checked-heads.json').read_bytes())
        titles=[r['title'] for r in json.loads((root/'payload.json').read_bytes())['rows']]
        for title in titles:
            path=index.get(title,'pages/'+wiki_fname(title))
            assert not any(other!=title and target.casefold()==path.casefold() for other,target in index.items()),title
            index[title]=path
            files[path]=(heads[title]['revisions'][0]['slots']['main']['content'].rstrip('\n')+'\n').encode()
        files['pages/INDEX.tsv']=''.join(f'{title}\t{path}\n' for title,path in sorted(index.items(),key=lambda x:(x[0].casefold(),x[0]))).encode()
        done=json.loads(git('show',parent+':ops/wayback/done.json'))
        video=json.loads((root/'video-capture.json').read_bytes())
        source=next(r for r in map(json.loads,(root/'preservation-receipts.jsonl').read_text().splitlines()) if r['kind']=='source_snapshot')
        captures=list(map(json.loads,(root/'image-captures.jsonl').read_text().splitlines()))+[source]
        now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        for capture in captures:
            assert capture['verified']
            verify=dict(at=now,method='sha256',sha256=capture['sha256'],capture_id=re.sub(r'(/web/\d{14})/',r'\1id_/',capture['capture'],count=1))
            if 'bytes' in capture:verify['bytes']=capture['bytes']
            done[capture['url']]=dict(done.get(capture['url'],{}),status='verified',capture=capture['capture'],last=now,verify=verify,note='Original Japanese Premiere JPEG/snapshot replay byte-checked by MemoryCoreChatGPT (#361)')
        video_url='https://www.youtube.com/watch?v=qqdS5JpNPiE'
        done[video_url]=dict(done.get(video_url,{}),status='verified',capture=video['capture'],last=now,verify=dict(at=now,method='html-content',decoded_sha256=video['sha256'],bytes=video['bytes'],capture_id=video['capture'].replace('164955/','164955id_/')),note='Opened on VPS; decompressed archived watch page matches video ID, title and channel. Card frames cited separately (#361).')
        files['ops/wayback/done.json']=(json.dumps(done,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
        scripts=['build.py','build-phase2.py','build-phase3.py','census.py','final-audit.py','publish.py','verify.py','seek-faces.py','get-better-faces.py','preserve.py','check-video.py','upload-faces.py','archive-uploaded.py','capture-local.py','save.py','report.py']
        data=['README.md','story.md','live.json','census.json','set-head.json','images.json','readings.json','observations.json','phase1-payload.json','phase2-payload.json','phase3-payload.json','phase4-payload.json','payload.json','files-payload.json','better-faces.json','checked-heads.json','final-manifest.json','coverage.csv','remaining-field-gaps.json','remaining-evidence.md','recommendations.md','video-capture.json','preservation-receipts.jsonl','image-captures.jsonl','upload-receipts.jsonl','verification.json','apply-receipts.jsonl','changes.diff','phase2.diff','phase3.diff','phase4.diff','navigation-check.json','section-boundaries.json']
        base='authoring/japanese_premiere_audit_361/'
        for name in scripts+data:files[base+'work/japanese-audit13/'+name]=(root/name).read_bytes()
        for name,path in [('audit_wiki_card_titles.py','work/audit_wiki_card_titles.py'),('wiki-tools/style_lint.py','work/wiki-tools/style_lint.py')]:files[base+'work/'+name]=Path(path).read_bytes()
        files[base+'work/wiki_title_publish.py']=Path('work/wiki_title_publish.py').read_text(encoding='utf8').split('def main(payload):')[0].encode()
        files[base+'README.md']=(root/'README.md').read_bytes()
    else:
        names=['README.md','story.md','final-manifest.json','coverage.csv','remaining-field-gaps.json','remaining-evidence.md','recommendations.md','verification.json','apply-receipts.jsonl','upload-receipts.jsonl','video-capture.json','preservation-receipts.jsonl','image-captures.jsonl','changes.diff','phase2.diff','phase3.diff','phase4.diff','payload.json','readings.json','observations.json','navigation-check.json','section-boundaries.json','before.webp','after.webp','diff.webp','location.webp','translation.webp','mobile.webp','mobile-lower.webp','pass-report.md','wiki-backup-commit.txt','images-backup-commit.txt']
        for name in names:
            binary=(root/name).read_bytes()
            if name.endswith('.webp'):assert len(binary)<500000
            files['evidence/361/'+name]=binary
        files['docs/design-log/361-japanese-premiere-audit.md']=(root/'design-log.md').read_bytes()
    commit,changes=save(parent,files)
    try:
        git('push','origin',commit+':refs/heads/main')
    except subprocess.CalledProcessError:
        if attempt==2:raise
        continue
    (root/(kind+'-backup-commit.txt')).write_text(commit+'\n',encoding='utf8')
    print(kind,commit,len(changes),'paths saved')
    break
