#!/usr/bin/env python3
"""Merge coded/SA.tsv, SB.tsv, K.tsv into results/archive_rows.tsv and print counts.
Usage: python3 -I mathas/archives/scripts/merge.py"""
import csv
from collections import Counter
rows, cols = [], None
for part in ("SA", "SB", "K"):
    rd = csv.DictReader((l for l in open(f"mathas/archives/results/coded/{part}.tsv", encoding="utf-8") if not l.startswith("#")), delimiter="\t")
    cols = rd.fieldnames
    rows += list(rd)
csv.DictWriter(open("mathas/archives/results/archive_rows.tsv", "w", encoding="utf-8"), cols, delimiter="\t", lineterminator="\n", extrasaction="ignore").writeheader()
with open("mathas/archives/results/archive_rows.tsv", "a", encoding="utf-8") as f:
    csv.DictWriter(f, cols, delimiter="\t", lineterminator="\n", extrasaction="ignore").writerows(rows)
print(len(rows)); print(Counter(r["matha"] for r in rows)); print(Counter(r["topic"] for r in rows)); print(Counter(r["legibility"] for r in rows))
