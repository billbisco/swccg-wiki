# SWCCG Wiki

Preservation copy of [wiki.swccg.com](https://wiki.swccg.com).

The live wiki is the encyclopedia people read. This repository is a public backup of its wikitext so the site can be rebuilt if the server or domain goes away, and so history is not trapped on one VPS.

## License

Fan encyclopedia. Respective rights belong to their owners.

Star Wars, Star Wars Customizable Card Game, card names, card text, and related marks remain with Lucasfilm Ltd., Disney, Decipher, and/or the Players Committee. This project claims none of those rights. Original arrangement, generators, and documentation in this repository may be copied to preserve and rebuild the encyclopedia.

See `LICENSE` and `NOTICE`.

## Layout

| Path | What it is |
| --- | --- |
| `pages/` | Encyclopedia wikitext (the backup) |
| `tools/dump_live.py` | Pulls current article text from wiki.swccg.com |
| `.github/workflows/sync-from-live.yml` | Weekly (and on-demand) dump → commit |
| `chrome/` | Shared site header/footer |
| `encyclopedia/` | Championship 60 transcribes (sheet emails redacted) |
| `authoring/` | Generators and apply helpers used to *build* the live wiki |

Card scans, PDFs, and extract rasters stay on the live wiki (size). Dump those separately with MediaWiki `dumpBackup.php` plus an image dump, or Internet Archive.

## Update GitHub from the live wiki

```text
python tools/dump_live.py
```

Writes each article under `pages/` and `pages/INDEX.tsv` (`title<TAB>path`). A GitHub Action runs that dump weekly and on **Actions → Sync from live wiki → Run workflow**.

## Rebuild a wiki from this repo

1. Install MediaWiki (FlaggedRevs optional; the live site uses it).
2. Import wikitext from `pages/INDEX.tsv`:

```bash
python tools/import_pages.py --pages pages --index pages/INDEX.tsv
```

`import_pages.py` prints MediaWiki `edit` / `importTextFiles` commands. On the live VPS the existing apply path is `apply-tsv.sh` in `authoring/`.

3. Copy `chrome/` into the site skin/header as on wiki.swccg.com.
4. Import images from a separate dump (not in this repo).

## What this is not

This is a fan encyclopedia. It is not Lucasfilm, Disney, Decipher, or the Players Committee.
