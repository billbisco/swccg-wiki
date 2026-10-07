import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "y2025-missing-players.tsv"
tar_path = ROOT / "y2025-missing-players.tar"
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _title, rel = line.split("\t", 1)
        p = ROOT / rel
        if p.exists():
            tar.add(p, arcname=rel.replace("\\", "/"))
print("tar", tar_path, "bytes", tar_path.stat().st_size)
