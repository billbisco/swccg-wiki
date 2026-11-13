"""Preserve the independently identified card's printed uniqueness marker."""
import hashlib,json
from pathlib import Path
import requests
root=Path(__file__).parent
title="I'm On The Leader (Japanese)"
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=title,prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status()
p=r.json()['query']['pages'][0];rev=p['revisions'][0];old=rev['slots']['main']['content']
needle='|printed_title=<span lang="ja">先頭機は任せろ</span>'
assert old.count(needle)==1
new=old.replace(needle,'|printed_title=<span lang="ja">＊先頭機は任せろ</span><ref name="jp-original-369">[[:File:Japanese-ANH-Im-On-The-Leader-PSA-156625016-original.jpg|Original Japanese printed face]]. The printed face identifies this as I’m On The Leader; the holder’s Evader label is incorrect.</ref>')
(root/'phase4-heads.json').write_text(json.dumps({title:p},ensure_ascii=False,indent=2),encoding='utf8')
packet=[dict(title=title,text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Restore the printed unique-title marker from the correctly identified Japanese face (#369)')]
(root/'phase4-packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2),encoding='utf8')
