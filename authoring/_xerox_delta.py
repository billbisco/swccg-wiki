#!/usr/bin/env python3
"""Leftover Xerox incremental TSV + media pack.

Generate still walks every transcribe_*.py (hub needs all rows). Apply ships
only titles not yet in the applied snapshot, plus the event hub, plus new PNGs.
Already-applied PDFs stay off the pack; a new event-day PDF still ships.

  python _xerox_delta.py write-delta --full y2012-nats-xerox-titles.tsv \\
      --applied y2012-nats-xerox-applied.tsv --delta y2012-nats-xerox-delta.tsv \\
      --always "2012 US Nationals"
  python _xerox_delta.py pack --delta y2012-nats-xerox-delta.tsv \\
      --media y2012-nats-media --applied-media y2012-nats-media-applied.txt \\
      --out y2012-nats-xerox.tgz --apply-sh apply-2012-nats-xerox.sh
  python _xerox_delta.py mark --delta y2012-nats-xerox-delta.tsv \\
      --applied y2012-nats-xerox-applied.tsv \\
      --media-dir y2012-nats-media-delta \\
      --applied-media y2012-nats-media-applied.txt
"""
from __future__ import annotations

import argparse
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_tsv(path: Path) -> list[tuple[str, str]]:
    if not path.exists():
        return []
    rows: list[tuple[str, str]] = []
    seen: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        title, rel = line.split("\t", 1)
        title, rel = title.strip(), rel.strip().replace("\\", "/")
        if title in seen:
            rows[seen[title]] = (title, rel)
        else:
            seen[title] = len(rows)
            rows.append((title, rel))
    return rows


def write_tsv(path: Path, rows: list[tuple[str, str]]) -> None:
    path.write_text(
        "".join(f"{t}\t{r}\n" for t, r in rows), encoding="utf-8", newline="\n"
    )


def load_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}


def write_names(path: Path, names: set[str]) -> None:
    path.write_text(
        "".join(f"{n}\n" for n in sorted(names)), encoding="utf-8", newline="\n"
    )


def delta_rows(
    full: list[tuple[str, str]],
    applied: list[tuple[str, str]],
    always: set[str],
) -> list[tuple[str, str]]:
    applied_titles = {t for t, _ in applied}
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for title, rel in full:
        if title in seen:
            continue
        if title in always or title not in applied_titles:
            out.append((title, rel))
            seen.add(title)
    return out


def write_delta_tsv(
    full: list[tuple[str, str]],
    applied_path: Path,
    delta_path: Path,
    always: set[str],
) -> list[tuple[str, str]]:
    applied = load_tsv(applied_path)
    rows = delta_rows(full, applied, always)
    write_tsv(delta_path, rows)
    print("xerox delta tsv", delta_path, "n", len(rows), "applied", len(applied))
    return rows


def new_media(media_dir: Path, applied_names: set[str]) -> list[Path]:
    if not media_dir.exists():
        return []
    out: list[Path] = []
    for p in sorted(media_dir.iterdir()):
        suf = p.suffix.lower()
        if suf not in (".png", ".pdf") or not p.is_file():
            continue
        if p.name in applied_names:
            continue
        out.append(p)
    return out


def pack(
    delta_path: Path,
    media_dir: Path,
    applied_media_path: Path,
    out_tgz: Path,
    apply_sh: str,
    media_arc: str,
) -> None:
    rows = load_tsv(delta_path)
    missing = [f"{t}\t{r}" for t, r in rows if not (ROOT / r).exists()]
    ok = [(t, r) for t, r in rows if (ROOT / r).exists()]
    write_tsv(delta_path, ok)
    print("delta tsv", delta_path, "n", len(ok), "missing", len(missing))
    for m in missing:
        print("MISSING", m)
    media = new_media(media_dir, load_names(applied_media_path))
    delta_media = ROOT / media_arc
    if delta_media.exists() and delta_media.resolve() != media_dir.resolve():
        for old in delta_media.iterdir():
            if old.is_file():
                old.unlink()
    else:
        delta_media.mkdir(parents=True, exist_ok=True)
    packed_media: list[Path] = []
    if delta_media.resolve() == media_dir.resolve():
        packed_media = media
    else:
        import shutil

        delta_media.mkdir(parents=True, exist_ok=True)
        for p in media:
            dest = delta_media / p.name
            shutil.copy2(p, dest)
            packed_media.append(dest)
    with tarfile.open(out_tgz, "w:gz") as tar:
        for _title, rel in ok:
            tar.add(ROOT / rel, arcname=rel)
        tar.add(delta_path, arcname=delta_path.name)
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(ROOT / apply_sh, arcname=apply_sh)
        tar.add(ROOT / "_xerox_delta.py", arcname="_xerox_delta.py")
        for p in packed_media:
            tar.add(p, arcname=f"{media_arc}/{p.name}")
    print(
        "packed",
        out_tgz,
        "bytes",
        out_tgz.stat().st_size,
        "wiki",
        len(ok),
        "media",
        len(packed_media),
    )


def mark_applied(
    delta_path: Path,
    applied_path: Path,
    media_dir: Path,
    applied_media_path: Path,
) -> None:
    merged = load_tsv(applied_path)
    seen = {t: i for i, (t, _) in enumerate(merged)}
    for title, rel in load_tsv(delta_path):
        if title in seen:
            merged[seen[title]] = (title, rel)
        else:
            seen[title] = len(merged)
            merged.append((title, rel))
    write_tsv(applied_path, merged)
    names = load_names(applied_media_path)
    if media_dir.exists():
        for p in media_dir.iterdir():
            if p.is_file() and p.suffix.lower() in (".png", ".pdf"):
                names.add(p.name)
    write_names(applied_media_path, names)
    print("marked applied titles", len(merged), "media", len(names))


def seed_from_full(
    full_path: Path,
    applied_path: Path,
    media_dir: Path,
    applied_media_path: Path,
    drop_titles: set[str],
) -> None:
    rows = [(t, r) for t, r in load_tsv(full_path) if t not in drop_titles]
    write_tsv(applied_path, rows)
    names: set[str] = set()
    if media_dir.exists():
        for p in media_dir.iterdir():
            if p.is_file() and p.suffix.lower() in (".png", ".pdf"):
                names.add(p.name)
    write_names(applied_media_path, names)
    print("seeded applied", applied_path, "n", len(rows), "media", len(names))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("write-delta")
    s.add_argument("--full", required=True)
    s.add_argument("--applied", required=True)
    s.add_argument("--delta", required=True)
    s.add_argument("--always", action="append", default=[])

    s = sub.add_parser("pack")
    s.add_argument("--delta", required=True)
    s.add_argument("--media", required=True)
    s.add_argument("--applied-media", required=True)
    s.add_argument("--out", required=True)
    s.add_argument("--apply-sh", required=True)
    s.add_argument("--media-arc", default="y2012-nats-media-delta")

    s = sub.add_parser("mark")
    s.add_argument("--delta", required=True)
    s.add_argument("--applied", required=True)
    s.add_argument("--media-dir", required=True)
    s.add_argument("--applied-media", required=True)

    s = sub.add_parser("seed")
    s.add_argument("--full", required=True)
    s.add_argument("--applied", required=True)
    s.add_argument("--media", required=True)
    s.add_argument("--applied-media", required=True)
    s.add_argument("--drop", action="append", default=["List of SWCCG tournaments"])

    args = ap.parse_args()
    if args.cmd == "write-delta":
        write_delta_tsv(
            load_tsv(ROOT / args.full),
            ROOT / args.applied,
            ROOT / args.delta,
            set(args.always),
        )
    elif args.cmd == "pack":
        pack(
            ROOT / args.delta,
            ROOT / args.media,
            ROOT / args.applied_media,
            ROOT / args.out,
            args.apply_sh,
            args.media_arc,
        )
    elif args.cmd == "mark":
        mark_applied(
            ROOT / args.delta,
            ROOT / args.applied,
            ROOT / args.media_dir,
            ROOT / args.applied_media,
        )
    elif args.cmd == "seed":
        seed_from_full(
            ROOT / args.full,
            ROOT / args.applied,
            ROOT / args.media,
            ROOT / args.applied_media,
            set(args.drop),
        )


if __name__ == "__main__":
    main()
