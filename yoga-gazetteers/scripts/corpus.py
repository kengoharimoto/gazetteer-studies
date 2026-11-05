#!/usr/bin/env python3
"""Catalogue the gazetteer OCR already downloaded for gazetteer-vedanta.

Writes data/corpus.tsv: one row per OCR file, with region, vol code, district, year,
kind (gazetteer / glossary / census / other) and generation:
  G1 = up to 1890 (first gazetteers, Hunter, Atkinson, Campbell)
  G2 = 1891-1935 (district gazetteers, Imperial Gazetteer era, glossaries)
  G3 = 1950 onward (revised state gazetteers)
If a scan is both primary and backup for the same volume, only the primary is kept
(`dup` column = primary identifier for backups that are also present).

Usage (from research/): python3 -I yoga-gazetteers/scripts/corpus.py
"""
import csv, glob, os, re

GV = "gazetteer-vedanta"
REGION = {"data": "Bombay", "madras": "Madras", "north": "UP", "bengal": "Bengal",
          "punjab": "Punjab", "cp": "CP", "revised": "Revised", "sringeri": "Mysore/Kanara",
          "rivals": "rivals", "census-images": "census"}

meta = {}  # identifier -> dict
for sel in glob.glob(f"{GV}/**/selection*.tsv", recursive=True):
    top = sel.split("/")[1]
    for r in csv.DictReader(open(sel, encoding="utf-8"), delimiter="\t"):
        if "primary" in r:
            ids = [(r["primary"], "primary"), (r.get("backup") or "", "backup")]
            vol, dist, note = r["vol"], r["district"], r.get("note", "")
        else:  # sringeri layout
            ids = [(r["ia"], "primary")]
            vol, dist, note = r["id"], r["volume"], r.get("note", "")
        for ident, role in ids:
            if not ident:
                continue
            d = dict(region=REGION.get(top, top), vol=vol, district=dist, year=r["year"],
                     note=note, role=role, primary=r.get("primary") or ident, sel=sel)
            if ident not in meta or meta[ident]["role"] == "backup":
                meta[ident] = d

cands = {}
for c in glob.glob(f"{GV}/**/ia_candidates.tsv", recursive=True):
    for r in csv.DictReader(open(c, encoding="utf-8"), delimiter="\t"):
        cands.setdefault(r["identifier"], (r.get("year", ""), r.get("title", "")))


def kind(m, path):
    s = (m.get("vol", "") + " " + m.get("note", "") + " " + m.get("district", "") + " " + path).lower()
    if "census" in s or m.get("vol", "").startswith("C1"):
        return "census"
    if re.search(r"rose|russell|rus\d|thurston|glossary|castes", s):
        return "glossary"
    return "gazetteer"


def gen(y):
    try:
        y = int(str(y)[:4])
    except ValueError:
        return "?"
    return "G1" if y <= 1890 else "G2" if y <= 1935 else "G3"


files = sorted(glob.glob(f"{GV}/**/*.txt", recursive=True))
files = [f for f in files if re.search(r"/(ia_ocr|census|thurston)/", f) and "/archives/" not in f
         and os.path.getsize(f) > 100_000]
present = {os.path.basename(f)[:-4] for f in files}
out = []
for f in files:
    ident = os.path.basename(f)[:-4]
    m = meta.get(ident)
    if f.split("/")[-2] == "thurston":
        m = dict(region="Madras", vol="THU" + ident[-1], district="Madras (all)", year="1909",
                 note="Thurston & Rangachari, Castes and Tribes", role="primary", primary=ident)
    if not m:
        y, t = cands.get(ident, ("", ""))
        top = f.split("/")[1]
        m = dict(region=REGION.get(top, top), vol="", district="", year=y, note=t[:80],
                 role="unselected", primary=ident)
    dup = m["primary"] if m["role"] == "backup" and m["primary"] in present else ""
    out.append(dict(path=f, ident=ident, region=m["region"], vol=m["vol"], district=m["district"],
                    year=m["year"], gen=gen(m["year"]), kind=kind(m, f), role=m["role"], dup=dup,
                    note=m["note"], bytes=os.path.getsize(f)))

cols = list(out[0])
with open("yoga-gazetteers/data/corpus.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, cols, delimiter="\t")
    w.writeheader()
    w.writerows(out)
print(len(out), "files;", sum(1 for r in out if not r["dup"]), "after dropping duplicate scans")
