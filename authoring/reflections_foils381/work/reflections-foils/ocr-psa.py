"""Source-image OCR for reading assistance only; never publication approval."""
import json,subprocess
from pathlib import Path
root=Path(__file__).parent;rows=[r for r in json.loads((root/'psa-originals.json').read_bytes()) if 'local_file' in r]
code='ROWS='+repr([{k:r[k] for k in ['article','source_url','sha256','local_file']} for r in rows])+'\n'+'''
import csv,hashlib,io,json,os,subprocess,urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image,ImageOps
root=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-reflections381-20261113/ocr');root.mkdir(exist_ok=True)
def one(row):
    try:
        name=Path(row['local_file'].replace('\\\\','/')).name;path=root/name
        if not path.exists():
            with urllib.request.urlopen(row['source_url'],timeout=90) as r:binary=r.read()
            assert hashlib.sha256(binary).hexdigest()==row['sha256'];path.write_bytes(binary)
        assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
        with Image.open(path) as source:
            im=source.convert('RGB');w,h=im.size;crop=(int(w*.1),int(h*.25),int(w*.95),int(h*.95)) if h/w>1.55 and h>=1500 else (0,0,w,h)
            im=ImageOps.autocontrast(ImageOps.grayscale(im.crop(crop)));im=im.resize((im.width*2,im.height*2));analysis=root/(name+'.ocr.png');im.save(analysis)
        task_env=dict(os.environ,OMP_THREAD_LIMIT='1')
        result=subprocess.run(['tesseract',str(analysis),'stdout','--psm','11','-l','eng','tsv'],env=task_env,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,check=True).stdout.decode()
        lines={};words=[]
        for word in csv.DictReader(io.StringIO(result),delimiter='\\t',quoting=csv.QUOTE_NONE):
            if not word.get('text','').strip():continue
            words.append(dict(text=word['text'],confidence=float(word['conf']),left=int(word['left']),top=int(word['top']),width=int(word['width']),height=int(word['height'])))
            key=(word['block_num'],word['par_num'],word['line_num']);lines.setdefault(key,[]).append(word['text'])
        text='\\n'.join(' '.join(v) for v in lines.values())
        return dict(article=row['article'],source_sha256=row['sha256'],source_url=row['source_url'],crop=crop,text=text,words=words,status='reading aid only; physical face not yet approved')
    except Exception as e:return dict(article=row['article'],error=str(e),status='OCR failed; retain original for manual reading')
with ThreadPoolExecutor(max_workers=2) as pool:
    for record in pool.map(one,ROWS):print(json.dumps(record),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close();out=[]
with (root/'psa-ocr.jsonl').open('wb') as log:
    for line in p.stdout:
        log.write(line);log.flush();out.append(json.loads(line))
        if len(out)%25==0:print('Source OCR',len(out),'/',len(rows),flush=True)
print(len(out),'source readings;',sum('error' in r for r in out),'errors; all remain unapproved',flush=True)
raise SystemExit(p.wait())
