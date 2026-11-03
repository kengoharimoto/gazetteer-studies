#!/usr/bin/env python3
"""Attach volume labels from every selection*.tsv and drop hits from backup scans of a volume already hit.
Usage: python3 -I mathas/scripts/dedupe.py mathas/results/hits.tsv > mathas/results/hits_dedup.tsv"""
import csv, glob, re, sys
lab, prim = {}, {}
for sel in sorted(glob.glob("*/data/selection*.tsv") + glob.glob("data/selection*.tsv")):
    region = sel.split("/data")[0] if not sel.startswith("data/") else "bombay"
    for row in csv.reader(open(sel, encoding="utf-8"), delimiter="\t"):
        if not row or row[0] in ("vol", "id", "code"): continue
        key = region + ":" + row[0]
        label = " | ".join(c for c in row[:3] if c)
        for c in row[1:]:
            for tok in re.split(r"[;, ]+", c):
                if re.match(r"^[A-Za-z0-9._-]{6,}$", tok) and not tok.isdigit():
                    lab.setdefault(tok, (key, label))
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
first = {}
for r in rows:
    ident = r["file"].split("/")[-1]
    key, label = lab.get(ident, (ident, "?"))
    r["volkey"], r["volume"] = key, label
    first.setdefault(key, ident)
w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
cols = ["hit_id", "seat", "volume", "file", "line", "page_guess", "match", "context"]
w.writerow(cols)
for r in rows:
    if first[r["volkey"]] == r["file"].split("/")[-1]:
        w.writerow([r[c] for c in cols])
