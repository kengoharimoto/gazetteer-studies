#!/usr/bin/env python3
"""Merge coded/W.tsv, N.tsv, S.tsv into results/mathas.tsv.
Drops rows from ATcu3 (a second scan of Atkinson vol XI = AT11) and relabels the 'CP12' row,
whose source file (dli.ministry.07863) is the revised Thane gazetteer of 1982, not Nagpur 1908."""
import csv
out, cols = [], None
for part in ("W", "N", "S"):
    rd = csv.DictReader((l for l in open(f"mathas/results/coded/{part}.tsv", encoding="utf-8") if not l.startswith("#")), delimiter="\t")
    cols = rd.fieldnames
    for r in rd:
        if r["volume"].startswith("ATcu3"): continue
        if r["id"] == "N30":
            r["volume"], r["year"], r["district"] = "Thane (revised) | 1982 [IA dli.ministry.07863, catalogued as Nagpur 1908]", "1982", "Thane"
        out.append(r)
w = csv.DictWriter(open("mathas/results/mathas.tsv", "w", encoding="utf-8"), cols, delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out), Counter(r["seat"] for r in out).most_common())
