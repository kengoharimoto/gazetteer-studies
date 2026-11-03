#!/usr/bin/env python3
"""Collect every Śṛṅgeri / Śaṅkarācārya / Smārta-maṭha mention (OCR variants) with context from all downloaded volumes.
Usage (from gazetteer-vedanta/): python3 -I sringeri/scripts/collect_hits.py > sringeri/results/hits.tsv
Columns: hit_id file volume_label line page_guess context
"""
import csv, glob, os, re
PAT = re.compile(r"s[h]?r[iíī]?[nñṅ]?g[eéēè]?[eiéēí]?r[iíī]|s[h]?r[iíī]?[nñṅ]g[aá]-? ?giri|sring[ce]ri|sriugeri|srinjeri|sh?ankar[aáā]?ch[aáā]?r|sankar[aáā]ch|sm[aáā]rt[ah]? ?(math|mutt|monast)", re.I)
labels = {}
for sel in ["data/selection.tsv", "madras/data/selection.tsv", "revised/data/selection.tsv", "sringeri/data/selection.tsv"]:
    for row in csv.reader(open(sel, encoding="utf-8"), delimiter="\t"):
        for cell in row:
            if re.match(r"^[A-Za-z0-9._-]+$", cell or "") and ("." in cell or "goog" in cell or cell.startswith("cu3")):
                labels.setdefault(cell, " | ".join(c for c in row if c and c != cell)[:90])
PAGE = re.compile(r"^\s*(\d{1,4})\s*$")
n = 0
print("hit_id\tfile\tvolume\tline\tpage_guess\tcontext")
for d in ["data/ia_ocr", "madras/data/ia_ocr", "sringeri/data/ia_ocr", "revised/data/ia_ocr"]:
    for f in sorted(glob.glob(d + "/*.txt")):
        lines = open(f, encoding="utf-8", errors="replace").read().split("\n")
        ident = os.path.basename(f)[:-4]
        page = ""
        for i, ln in enumerate(lines):
            m = PAGE.match(ln)
            if m:
                page = m.group(1)
            if PAT.search(ln):
                n += 1
                ctx = " ".join(" ".join(lines[max(0, i - 6): i + 7]).split())
                print(f"S{n:03d}\t{d.split('/data')[0] or 'bombay'}/{ident}\t{labels.get(ident, '?')}\t{i+1}\t{page}\t{ctx}")
