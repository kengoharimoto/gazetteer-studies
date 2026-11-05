#!/usr/bin/env python3
"""Merge coded batches with passage metadata, check every quote verbatim against its passage, and tabulate.

Reads data/passages.tsv and results/coded/*.coded.tsv. Writes
  results/coded_all.tsv        passage metadata + codes + quote_ok (1/0/'' when no quote)
  results/sense_by_gen.tsv     counts of sense by generation x term family group
  results/tags_by_gen.tsv      counts of tags by generation x term group (relevant senses only)
and prints missing ids, bad codes and unverified quotes.
Usage (from research/): python3 -I yoga-gazetteers/scripts/merge.py
"""
import csv, glob, re, collections

norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
P = {p["id"]: p for p in csv.DictReader(open("yoga-gazetteers/data/passages.tsv", encoding="utf-8"), delimiter="\t")}
SENSES = {"PHIL", "DISCIPLINE", "MODERN", "ASCETIC", "MENDICANT", "CASTE", "SAINT", "PRACTICE_OTHER",
          "NAME", "ASTRO", "OTHER", "JUNK"}
IRRELEVANT = {"NAME", "ASTRO", "OTHER", "JUNK", "PRACTICE_OTHER"}

def group(fams):
    f = set(fams.split(","))
    if f & {"yoga", "yogasutra", "patanjali"}: return "yoga"
    if "yogi" in f: return "yogi"
    if f & {"jogi", "nath_kanphata"}: return "jogi/nath"
    if "modern" in f: return "modern"
    return "practice"

rows, seen = [], set()
for path in sorted(glob.glob("yoga-gazetteers/results/coded/*.coded.tsv")):
    for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE):
        i = (r.get("id") or "").strip()
        if i not in P:
            print("UNKNOWN ID", path, i); continue
        if i in seen:
            print("DUPLICATE", i); continue
        seen.add(i)
        p = P[i]
        sense = (r.get("sense") or "").strip().upper()
        if sense not in SENSES:
            print("BAD SENSE", i, sense)
        q = (r.get("quote") or "").strip().strip('"“”')
        ok = ""
        if q:
            parts = [x for x in re.split(r"\s*(?:…|\.\.\.)\s*", norm(q)) if len(x) > 8]
            ok = int(bool(parts) and all(x in norm(p["text"]) for x in parts))
        rows.append(dict(id=i, ident=p["ident"], region=p["region"], vol=p["vol"], district=p["district"],
                         year=p["year"], gen=p["gen"], kind=p["kind"], families=p["families"],
                         group=group(p["families"]), terms=p["terms"], sense=sense,
                         sense2=(r.get("sense2") or "").strip().upper(), attitude=(r.get("attitude") or "").strip(),
                         tags=(r.get("tags") or "").strip(), page=(r.get("page") or "").strip(), quote=q,
                         quote_ok=ok, note=(r.get("note") or "").strip()))

todo = {i for i, p in P.items() if p["index"] == "0"}
miss = sorted(todo - seen)
print(len(rows), "coded;", len(miss), "missing", miss[:10])
bad = [r for r in rows if r["quote_ok"] == 0]
print("quotes checked", sum(r["quote_ok"] != "" for r in rows), "not verbatim", len(bad))
for r in bad[:15]:
    print("  NOT VERBATIM", r["id"], r["quote"][:90])

rows.sort(key=lambda r: r["id"])
# Unidentified Cornell scans that are other copies of Atkinson volumes already counted
# (6-word shingle overlap 0.20-0.22 with one volume, <=0.02 with any other; checked 2026-11-05).
DUP_SCANS = {"cu31924023947736": "AT01", "cu31924023947744": "AT02", "cu31924023947751": "AT11"}
key = lambda q: re.sub(r"[^a-z]", "", q.lower())[:80]
first = {}
for r in rows:
    r["exclude"] = f"duplicate scan of {DUP_SCANS[r['ident']]}" if r["ident"] in DUP_SCANS else ""
    r["copy_of"] = ""
    if r["quote"] and not r["exclude"]:
        k = key(r["quote"])
        if k in first:
            f = first[k]
            if f["gen"] == r["gen"]:
                r["exclude"] = f"same passage as {f['id']}"
            else:
                r["copy_of"] = f"{f['id']} ({f['vol']} {f['year']})"
        else:
            first[k] = r
print("excluded", sum(bool(r["exclude"]) for r in rows), "; later copies of earlier text",
      sum(bool(r["copy_of"]) for r in rows))
with open("yoga-gazetteers/results/coded_all.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, list(rows[0]), delimiter="\t"); w.writeheader(); w.writerows(rows)

GENS = ["G1", "G2", "G3"]
rows = [r for r in rows if not r["exclude"]]
c = collections.Counter((r["group"], r["sense"], r["gen"]) for r in rows)
with open("yoga-gazetteers/results/sense_by_gen.tsv", "w", encoding="utf-8") as fh:
    fh.write("group\tsense\t" + "\t".join(GENS) + "\n")
    for g, s in sorted({(g, s) for g, s, _ in c}):
        fh.write(f"{g}\t{s}\t" + "\t".join(str(c[(g, s, x)]) for x in GENS) + "\n")
t = collections.Counter()
for r in rows:
    if r["sense"] in IRRELEVANT: continue
    t[("ALL", "attitude:" + r["attitude"], r["gen"])] += 1
    for tag in filter(None, (x.strip() for x in r["tags"].split(","))):
        t[(r["group"], tag, r["gen"])] += 1
with open("yoga-gazetteers/results/tags_by_gen.tsv", "w", encoding="utf-8") as fh:
    fh.write("group\ttag\t" + "\t".join(GENS) + "\n")
    for g, s in sorted({(g, s) for g, s, _ in t}):
        fh.write(f"{g}\t{s}\t" + "\t".join(str(t[(g, s, x)]) for x in GENS) + "\n")
