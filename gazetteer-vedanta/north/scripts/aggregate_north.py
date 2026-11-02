#!/usr/bin/env python3
"""District tables for the Daśanāmī study (United Provinces).

Usage: python3 -I scripts/aggregate_north.py   (from north/)

Reads results/coded/*.counts.tsv and *.notes.tsv. Writes
  results/gosain_counts.tsv   district x layer: Gosain (incl. Atit/Atith), Sannyasi, Dandi/Paramhans,
                              Bairagi, Jogi head-counts, district scope only, with census year and source
  results/dasnami_notes.tsv   district x note kind: number of DASNAMI notes (MATH, LAND, MILITARY, TRADE, ...)
Cells are keyed by district, layer and census year; several rows in one cell (e.g. Gosain + Atit) are summed.
Layers: AT (Atkinson NWP 1874–86), OU (Oudh 1877–78), UP (Nevill 1903–11).
Rows whose `note` marks them as land/proprietors/villages/acres/percent (not persons) are excluded.
"""
import collections, csv, glob, re

NOTPERSONS = re.compile(r"(?i)\bvillage|acre|proprietor|percent|per cent|%|mahal|estate|lower bound|over \d|threshold")


def num(x):
    d = re.sub(r"[^\d]", "", x or "")
    return int(d) if d else None


def group(r):
    g = (r.get("group_std") or "").strip()
    p = (r.get("group_as_printed") or "").lower()
    if re.search(r"\batith?s?\b|\batit", p):
        return "GOSAIN"
    if g in ("DANDI", "DASNAMI") or "paramhans" in p:
        return "DANDI_PARAMHANS" if g != "DASNAMI" else "GOSAIN"
    return g


cells = collections.defaultdict(lambda: collections.defaultdict(list))
for f in glob.glob("results/coded/*.counts.tsv"):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        if (r.get("scope") or "").strip() != "district":
            continue
        n = num(r.get("count"))
        if n is None or NOTPERSONS.search((r.get("note") or "") + " " + (r.get("group_as_printed") or "")):
            continue
        g = group(r)
        if g not in ("GOSAIN", "SANNYASI", "DANDI_PARAMHANS", "BAIRAGI", "JOGI"):
            continue
        layer = r["vol"][:2]
        dist = (r.get("district") or "").strip().split("(")[0].strip()
        cells[(dist, layer, (r.get("census_year") or "").strip()[:4])][g].append((n, r.get("census_year", ""), r["vol"], r.get("confidence", "")))

with open("results/gosain_counts.tsv", "w", encoding="utf-8") as f:
    f.write("district\tlayer\tyear\tGOSAIN\tSANNYASI\tDANDI_PARAMHANS\tBAIRAGI\tJOGI\tcensus_years\tvols\tlow_conf\n")
    for (d, layer, yr) in sorted(cells):
        c = cells[(d, layer, yr)]
        cell = lambda g: str(sum(x[0] for x in c.get(g, []))) if c.get(g) else ""   # Gosain + Atit summed
        yrs = sorted({x[1] for g in c for x in c[g] if x[1]})
        vols = sorted({x[2] for g in c for x in c[g]})
        low = sum(1 for g in c for x in c[g] if x[3] == "low")
        f.write("\t".join([d, layer, yr, cell("GOSAIN"), cell("SANNYASI"), cell("DANDI_PARAMHANS"), cell("BAIRAGI"),
                           cell("JOGI"), ",".join(yrs), ",".join(vols), str(low)]) + "\n")

notes = collections.defaultdict(collections.Counter)
for f in glob.glob("results/coded/*.notes.tsv"):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        if (r.get("order") or "").strip() == "DASNAMI":
            d = (r.get("district") or "").strip().split("(")[0].strip()
            notes[d][(r.get("kind") or "").strip()] += 1
kinds = ["MATH", "LAND", "MILITARY", "TRADE", "FAIR", "CASTE", "DOCTRINE", "OTHER"]
with open("results/dasnami_notes.tsv", "w", encoding="utf-8") as f:
    f.write("district\ttotal\t" + "\t".join(kinds) + "\n")
    for d in sorted(notes, key=lambda d: -sum(notes[d].values())):
        f.write("\t".join([d, str(sum(notes[d].values()))] + [str(notes[d][k]) for k in kinds]) + "\n")
print(len(cells), "district-layer cells;", len(notes), "districts with Dasnami notes")
