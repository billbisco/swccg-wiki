#!/usr/bin/env python3
from __future__ import annotations

import zipfile
from pathlib import Path
from urllib.parse import unquote

zpath = Path("wiki/encyclopedia/pc-2014-events/2014MPC_Holotable.zip")
out = Path("wiki/encyclopedia/pc-2014-events/holotable")
out.mkdir(parents=True, exist_ok=True)
zf = zipfile.ZipFile(zpath)
for i in zf.infolist():
    if not i.filename.endswith(".htd") or i.filename.startswith("__"):
        continue
    name = unquote(Path(i.filename).name)
    dest = out / name
    dest.write_bytes(zf.read(i.filename))
    print(dest.name, dest.stat().st_size)
