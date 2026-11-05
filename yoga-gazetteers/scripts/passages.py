#!/usr/bin/env python3
"""Merge the core hits of results/kwic.tsv into passages for coding.

Hits in the same volume less than 500 characters apart form one passage; the passage text runs
from 450 characters before the first hit to 450 after the last. Passages that look like an index
(many bare numbers) are kept but flagged index=1 and not sent to coders.
Writes data/passages.tsv (id, ident, region, vol, district, year, gen, kind, families, terms, index, text)
and data/batches/batch_NN.tsv (non-index passages, ~150 per batch, grouped by region).
Usage (from research/): python3 -I yoga-gazetteers/scripts/passages.py
"""
import csv, os, re, collections

K = list(csv.DictReader(open("yoga-gazetteers/results/kwic.tsv", encoding="utf-8"), delimiter="\t"))
corp = {r["ident"]: r for r in csv.DictReader(open("yoga-gazetteers/data/corpus.tsv", encoding="utf-8"), delimiter="\t")}
by = collections.defaultdict(list)
for k in K:
    by[k["ident"]].append(k)

out, n = [], 0
for ident, hits in by.items():
    c = corp[ident]
    t = re.sub(r"\s+", " ", open(c["path"], encoding="utf-8", errors="replace").read())
    hits.sort(key=lambda k: int(k["pos"]))
    groups = []
    for h in hits:
        p = int(h["pos"])
        if groups and p - groups[-1]["end"] < 500:
            groups[-1]["end"] = p + len(h["term"]); groups[-1]["hits"].append(h)
        else:
            groups.append(dict(start=p, end=p + len(h["term"]), hits=[h]))
    for g in groups:
        n += 1
        text = t[max(0, g["start"] - 450):g["end"] + 450]
        toks = text.split()
        nums = sum(bool(re.fullmatch(r"[\d,;:.\-—\[\]()]+", x)) for x in toks)
        out.append(dict(id=f"P{n:05d}", ident=ident, region=c["region"], vol=c["vol"], district=c["district"],
                        year=c["year"], gen=c["gen"], kind=c["kind"],
                        families=",".join(sorted({h["family"] for h in g["hits"]})),
                        terms=",".join(sorted({h["term"] for h in g["hits"]})),
                        index=int(nums / max(1, len(toks)) > 0.18), text=text))

cols = list(out[0])
with open("yoga-gazetteers/data/passages.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, cols, delimiter="\t"); w.writeheader(); w.writerows(out)

todo = sorted((p for p in out if not p["index"]), key=lambda p: (p["region"], p["year"], p["id"]))
os.makedirs("yoga-gazetteers/data/batches", exist_ok=True)
size = 150
for i in range(0, len(todo), size):
    with open(f"yoga-gazetteers/data/batches/batch_{i // size + 1:02d}.tsv", "w", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t"); w.writeheader(); w.writerows(todo[i:i + size])
print(len(out), "passages;", sum(p["index"] for p in out), "index-like;", len(todo), "to code in",
      -(-len(todo) // size), "batches")
print(collections.Counter(p["families"] for p in todo).most_common(12))
