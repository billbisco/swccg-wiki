import uuid

def imageinfo(title):
    return call(action='query',titles=title,prop='imageinfo|revisions|info',iiprop='sha1|url|size',rvprop='ids|content',rvslots='main')['query']['pages'][0]

def multipart(fields,part,data,filename):
    boundary='----SWCCG'+uuid.uuid4().hex
    body=b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n').encode() for k,v in fields.items())
    body+=(f'--{boundary}\r\nContent-Disposition: form-data; name="{part}"; filename="{filename}"\r\nContent-Type: image/jpeg\r\n\r\n').encode()+data+(f'\r\n--{boundary}--\r\n').encode()
    req=urllib.request.Request(API,data=body,headers={'Content-Type':f'multipart/form-data; boundary={boundary}','User-Agent':'SWCCG Wiki original Japanese photo preservation'})
    with opener.open(req,timeout=90) as response:result=json.load(response)
    assert 'error' not in result,result.get('error',{}).get('info')
    return result['upload']

def upload_faces(files,csrf):
    for f in files:
        title=f['title'];page=imageinfo(title)
        if not page.get('imageinfo'):
            assert page.get('missing'),title
            duplicates=call(action='query',list='allimages',aisha1=f['sha1'])['query']['allimages']
            assert not duplicates,('Existing identical file',[x['name'] for x in duplicates])
            data=base64.b64decode(f['data']);assert hashlib.sha1(data).hexdigest()==f['sha1']
            common=dict(action='upload',format='json',formatversion=2,filename=f['name'],token=csrf,assertuser=BOT,maxlag=5)
            if len(data)>1800000:
                offset=0;filekey=None
                while offset<len(data):
                    chunk=data[offset:offset+900000]
                    args=dict(common,stash=1,filesize=len(data),offset=offset)
                    if filekey:args['filekey']=filekey
                    result=multipart(args,'chunk',chunk,f['name'])
                    assert result['result'] in ['Continue','Success'],(title,result['result'])
                    offset+=len(chunk)
                    if 'offset' in result:assert result['offset']==offset
                    filekey=result['filekey']
                result=call(True,action='upload',filename=f['name'],filekey=filekey,text=f['desc'],comment='Preserve original Japanese photograph without recompression (#369)',token=csrf,assertuser=BOT,maxlag=5)['upload']
            else:
                result=multipart(dict(common,text=f['desc'],comment='Preserve original Japanese photograph (#369)'),'file',data,f['name'])
            assert result['result']=='Success',(title,result['result'])
            page=imageinfo(title)
        rev,text=current(page)
        assert page['imageinfo'][0]['sha1']==f['sha1'],(title,'Image mismatch')
        assert text==f['desc'],(title,'Existing description differs; guarded metadata repair required')
        assert 'review' in call(True,action='review',revid=rev,flag_accuracy=1,comment='Verified original Japanese photo identity and source (#369)',assertuser=BOT,token=csrf,maxlag=5)
        print(json.dumps(dict(title=title,revid=rev,pageid=page['pageid'],sha256=digest(text),image_sha256=f['sha256'],image_url=page['imageinfo'][0]['url'],sources=f['urls'],reviewed=True)),flush=True)
