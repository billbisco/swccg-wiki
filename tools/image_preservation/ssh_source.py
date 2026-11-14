"""Read-only SSH stream of inventoried public Wiki originals; no server staging or HTTP."""
import base64,json,re,subprocess,urllib.parse
from pathlib import Path
from .offline_backup import wiki_image_url
PUBLIC_ROOT='/var/lib/docker/volumes/swccg-wiki_wiki_images/_data'
REMOTE_CODE=r'''
import json,os,pathlib,re,sys
os.nice(10)
root=pathlib.Path('/var/lib/docker/volumes/swccg-wiki_wiki_images/_data').resolve()
items=json.load(sys.stdin)
if len(items)>500:raise ValueError('Read-only batch exceeds500 originals')
out=sys.stdout.buffer
for item in items:
    name=item['relative_path'];ident=item['id']
    if not re.fullmatch(r'(?:archive/)?[0-9a-f]/[0-9a-f]{2}/[^/\\\x00]+',name):raise ValueError('Non-public original path')
    path=(root/name).resolve()
    if not path.is_relative_to(root):raise ValueError('Path escapes public image root')
    try:
        f=path.open('rb');size=os.fstat(f.fileno()).st_size
        if size!=item['bytes']:f.close();raise ValueError('Original size differs from inventory')
    except (OSError,ValueError) as error:
        out.write((json.dumps({'id':ident,'bytes':0,'error':str(error)[:180]})+'\n').encode());out.flush();continue
    with f:
        out.write((json.dumps({'id':ident,'bytes':size})+'\n').encode());out.flush()
        remaining=size
        while remaining:
            chunk=f.read(min(128*1024,remaining))
            if not chunk:raise OSError('Original truncated during read')
            out.write(chunk);remaining-=len(chunk)
        out.flush()
'''
def request_item(info):
    wiki_image_url(info['url'])
    path=urllib.parse.unquote(urllib.parse.urlsplit(info['url']).path.removeprefix('/images/'))
    if not re.fullmatch(r'(?:archive/)?[0-9a-f]/[0-9a-f]{2}/[^/\\\x00]+',path):raise ValueError('Not an inventoried public original path')
    if not isinstance(info['bytes'],int) or info['bytes']<0:raise ValueError('Invalid expected byte count')
    if not re.fullmatch('[0-9a-f]{64}',info['id']):raise ValueError('Invalid version identity')
    return {'id':info['id'],'relative_path':path,'bytes':info['bytes']}
def start(items,stderr):
    if len(items)>500:raise ValueError('At most500 originals per read-only source stream')
    request=[request_item(x) for x in items]
    encoded=base64.b64encode(REMOTE_CODE.encode()).decode()
    command="python3 -c \"import base64;exec(base64.b64decode('"+encoded+"'))\""
    proc=subprocess.Popen(['ssh','-T','gemp',command],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=stderr)
    try:proc.stdin.write(json.dumps(request).encode());proc.stdin.close()
    except BaseException:proc.kill();proc.wait();raise
    return proc

def receive(proc,info,part):
    line=proc.stdout.readline(4097)
    if not line or len(line)>4096:raise RuntimeError('Invalid source stream header')
    header=json.loads(line)
    if header.get('id')!=info['id']:raise RuntimeError('Source stream version order differs')
    if header.get('error'):return header['error']
    if header.get('bytes')!=info['bytes']:raise RuntimeError('Source stream byte count differs')
    remaining=info['bytes']
    read_bytes=0
    with part.open('wb') as output:
        while remaining:
            chunk=proc.stdout.read(min(128*1024,remaining))
            if not chunk:raise RuntimeError('Truncated source stream')
            read_bytes+=len(chunk)
            if read_bytes%(8*1024**2)<len(chunk):
                from .store import ensure_space
                ensure_space(part.parent)
            output.write(chunk);remaining-=len(chunk)
        output.flush()
        import os
        os.fsync(output.fileno())
    return None
