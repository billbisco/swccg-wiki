import json,os,sys,base64,urllib.request,urllib.error
T=os.environ["GH_TOKEN"]; repo,branch,msg=sys.argv[1],sys.argv[2],sys.argv[3]; files=sys.argv[4:]  # local=remote/path
R="https://api.github.com/repos/"+repo
def gh(m,p,d=None):
    r=urllib.request.Request(R+p,json.dumps(d).encode() if d is not None else None,{"Authorization":"token "+T,"Content-Type":"application/json"},method=m)
    try: return json.loads(urllib.request.urlopen(r,timeout=180).read())
    except urllib.error.HTTPError as e: sys.exit(f"{m} {p} -> {e.code} {e.read()[:300]!r}")
head=gh("GET",f"/git/ref/heads/{branch}")["object"]["sha"]; base=gh("GET",f"/git/commits/{head}")["tree"]["sha"]
tree=[]
for f in files:
    loc,rem=f.split("=",1)
    b=gh("POST","/git/blobs",{"content":base64.b64encode(open(loc,"rb").read()).decode(),"encoding":"base64"})["sha"]
    tree.append({"path":rem,"mode":"100644","type":"blob","sha":b})
nt=gh("POST","/git/trees",{"base_tree":base,"tree":tree})["sha"]
me={"name":"billbisco","email":"billbisco@users.noreply.github.com"}
c=gh("POST","/git/commits",{"message":msg,"tree":nt,"parents":[head],"author":me,"committer":me})["sha"]
gh("PATCH",f"/git/refs/heads/{branch}",{"sha":c}); print("committed",repo,c)
