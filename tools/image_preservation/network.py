"""Bounded requests and streaming hashes with no persistent binary cache."""
import hashlib
import json
import re
import urllib.error
import urllib.parse
import urllib.request

UA='SWCCG-ImagePreservation/1.0 (https://github.com/swccg-guild/work/issues/382)'
API='https://wiki.swccg.com/api.php'
class Throttled(RuntimeError):
    def __init__(self,retry_after):
        self.retry_after=retry_after
        super().__init__('Archive service throttled; retry after '+str(retry_after)+' seconds')

def open_url(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA,'Accept-Encoding':'identity'}),timeout=60)
    except urllib.error.HTTPError as e:
        if e.code==429 or e.code>=500:
            try:delay=int(e.headers.get('Retry-After','120'))
            except ValueError:delay=300
            raise Throttled(max(30,delay)) from None
        raise

def api(**params):
    with open_url(API+'?'+urllib.parse.urlencode({'format':'json','formatversion':2,'maxlag':5,**params})) as r:
        data=json.load(r)
    if 'error' in data:raise RuntimeError('MediaWiki API '+data['error']['code'])
    return data

def image_signature(prefix,mime):
    checks={'image/jpeg':lambda:prefix.startswith(b'\xff\xd8\xff'),
      'image/png':lambda:prefix.startswith(b'\x89PNG\r\n\x1a\n'),
      'image/gif':lambda:prefix.startswith((b'GIF87a',b'GIF89a')),
      'image/webp':lambda:prefix[:4]==b'RIFF' and prefix[8:12]==b'WEBP',
      'image/svg+xml':lambda:b'<svg' in prefix.lower() and b'<html' not in prefix.lower(),
      'image/tiff':lambda:prefix[:4] in (b'II*\x00',b'MM\x00*'),
      'image/bmp':lambda:prefix.startswith(b'BM'),
      'image/x-icon':lambda:prefix.startswith(b'\x00\x00\x01\x00'),
      'image/vnd.microsoft.icon':lambda:prefix.startswith(b'\x00\x00\x01\x00')}
    if mime not in checks:raise ValueError('Unsupported image type needs explicit verifier: '+mime)
    return checks[mime]()

def stream_hash(url,mime,expected_bytes,save_to=None):
    sha1=hashlib.sha1();sha256=hashlib.sha256();size=0;prefix=b''
    f=save_to.open('wb') if save_to else None
    try:
        with open_url(url) as r:
            response_mime=r.headers.get_content_type()
            if not response_mime.startswith('image/'):
                raise ValueError('Non-image response: '+response_mime)
            while True:
                chunk=r.read(128*1024)
                if not chunk:break
                size+=len(chunk)
                if size>expected_bytes:raise ValueError('Payload exceeds inventoried original size')
                if len(prefix)<8192:prefix+=chunk[:8192-len(prefix)]
                sha1.update(chunk);sha256.update(chunk)
                if f:f.write(chunk)
        if size!=expected_bytes:raise ValueError('Payload size mismatch')
        if not image_signature(prefix,mime):raise ValueError('Wrong image signature')
        return {'sha1':sha1.hexdigest(),'sha256':sha256.hexdigest(),'bytes':size,'mime':response_mime}
    finally:
        if f:f.close()

def raw_capture(url,original):
    m=re.fullmatch(r'https?://web\.archive\.org/web/(\d{14})(?:id_)?/(.+)',url)
    if not m or m[2]!=original:raise ValueError('Capture does not identify the exact original URL')
    return 'https://web.archive.org/web/'+m[1]+'id_/'+original

def check_hashes(info,source,archived):
    sha=info['sha1']
    # MediaWiki installations return hex or base-36 SHA-1.
    expected=int(sha,16) if re.fullmatch('[0-9a-fA-F]{40}',sha) else int(sha,36)
    if int(source['sha1'],16)!=expected:raise ValueError('Live source changed from inventoried version')
    if source['bytes']!=info['bytes'] or archived['bytes']!=info['bytes']:
        raise ValueError('Original size mismatch')
    if source['sha256']!=archived['sha256']:raise ValueError('Archived original hash mismatch')
