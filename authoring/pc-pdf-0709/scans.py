"""scans.py <final_dir> : scan PNG per deck into final/media (130 dpi gray, stacked pages, upright)."""
import json, sys, subprocess, tempfile, os, pathlib
sys.argv=[sys.argv[0]]+sys.argv[1:]
final = pathlib.Path(sys.argv[1]); media = pathlib.Path(__file__).parent / "media"; media.mkdir(exist_ok=True)
sys.path.insert(0, "/home/claude/sw2/authoring/pc-pdf-scans")
from PIL import Image
src = open("/home/claude/sw2/authoring/pc-pdf-scans/make_scans.py").read()
upright_src = src[src.index("def upright"):src.index("tsv, pdfdir, outd")]
ns = {}; exec("import subprocess, re\nfrom PIL import Image, ImageStat\n" + upright_src, ns); upright = ns["upright"]
canon = json.load(open(final / "decks-canon.json"))
here = pathlib.Path(__file__).parent
for d in canon:
    dst = media / d["scan"]
    if dst.exists(): continue
    ims = []
    with tempfile.TemporaryDirectory() as td:
        for p in d["pages"]:
            full = here / "img" / (d["pdf"] + "_full") / f"p-{int(p):02d}.png"
            if full.exists():
                im = Image.open(full).convert("L"); im = im.resize((int(im.width * 130 / 200), int(im.height * 130 / 200)))
                f = full
            else:
                subprocess.run(["pdftoppm", "-r", "130", "-gray", "-f", str(p), "-l", str(p), "-png", str(here / "pdf" / (d["pdf"] + ".pdf")), f"{td}/x{p}"], check=True, stderr=subprocess.DEVNULL)
                f = sorted(pathlib.Path(td).glob(f"x{p}*.png"))[0]; im = Image.open(f).convert("L")
            ims.append(upright(im, f))
        w = max(i.width for i in ims); h = sum(i.height for i in ims)
        c = Image.new("L", (w, h), 255); y = 0
        for i in ims: c.paste(i, (0, y)); y += i.height
        c.save(dst, optimize=True)
print(len(list(media.iterdir())), "scans")
