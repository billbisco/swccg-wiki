import uuid

def imageinfo(title):
    return call(action="query",titles=title,prop="imageinfo|revisions|info",iiprop="sha1|url|size",rvprop="ids|content",rvslots="main")["query"]["pages"][0]

def upload_faces(files, csrf):
    for f in files:
        title=f["title"]
        p=imageinfo(title)
        if p.get("imageinfo"):
            assert p["imageinfo"][0]["sha1"]==f["sha1"],("Different existing image",title)
        else:
            assert p.get("missing"),title
            duplicates=call(action="query",list="allimages",aisha1=f["sha1"])["query"]["allimages"]
            assert not duplicates,("Existing wiki file has same bytes",title,[x["name"] for x in duplicates])
            data=base64.b64decode(f["data"])
            assert hashlib.sha1(data).hexdigest()==f["sha1"]
            fields=dict(action="upload",format="json",formatversion=2,filename=f["name"],
                        text=f["desc"],comment="Add original Japanese Premiere card face (#172)",
                        token=csrf,assertuser=BOT,maxlag=5)
            boundary="----SWCCG"+uuid.uuid4().hex
            body=b"".join((f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n').encode() for k,v in fields.items())
            body+=(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{f["name"]}"\r\nContent-Type: image/jpeg\r\n\r\n').encode()
            body+=data+(f'\r\n--{boundary}--\r\n').encode()
            req=urllib.request.Request(API,data=body,headers={
                "Content-Type":f"multipart/form-data; boundary={boundary}",
                "User-Agent":"SWCCG Japanese Premiere scan publication"})
            with opener.open(req,timeout=65) as response:
                result=json.load(response)
            assert result.get("upload",{}).get("result")=="Success",(title,result.get("error"),result.get("upload",{}).get("warnings"))
            p=imageinfo(title)
        image=p["imageinfo"][0]
        rev,text=current(p)
        assert image["sha1"]==f["sha1"] and text==f["desc"],title
        print(json.dumps(dict(title=title,revid=rev,pageid=p["pageid"],sha256=digest(text),
                              image_sha256=f["sha256"],image_url=image["url"],sources=f["urls"],
                              pending_archives=len(f["pending_archive_flags"]))),flush=True)

packet=json.loads(gzip.decompress(base64.b64decode(PACKED)))
rows,FILES=packet["rows"],packet["files"]
batch_heads(rows)
if MODE=="preview":
    for f in FILES:
        p=imageinfo(f["title"])
        assert p.get("missing") or (p["imageinfo"][0]["sha1"]==f["sha1"] and current(p)[1]==f["desc"]),f["title"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(inspect,rows))
    print(json.dumps(dict(preview="pass",pages=len(rows),files=len(FILES))),flush=True)
elif MODE=="apply":
    publish(rows)
else:
    raise ValueError(MODE)
