#!/usr/bin/env python3
"""Merge the round-two (fakir/sadhu) coded batches, check quotes verbatim, tabulate.

Reads data/fakir_passages.tsv and results/fakir_coded/*.coded.tsv. Writes
  results/fakir_coded_all.tsv          metadata + codes + quote_ok + exclude (repeat of an earlier passage
                                        in the same generation)
  results/fakir_referent_by_gen.tsv    referent x religion x generation
  results/fakir_tags_by_gen.tsv        attitude, practice and tags by generation (relevant referents only)
Usage (from research/): python3 -I yoga-gazetteers/scripts/fakir_merge.py
"""
import csv, glob, re, collections

norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
P = {p["id"]: p for p in csv.DictReader(open("yoga-gazetteers/data/fakir_passages.tsv", encoding="utf-8"), delimiter="\t")}
REFS = {"MUSLIM_RELIGIOUS", "HINDU_ASCETIC", "GENERIC_MENDICANT", "CENSUS_CATEGORY", "SAINT_SHRINE", "NAME", "OTHER", "JUNK"}
IRRELEVANT = {"NAME", "OTHER", "JUNK"}
rows, seen = [], set()
for path in sorted(glob.glob("yoga-gazetteers/results/fakir_coded/*.coded.tsv")):
    for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE):
        i = (r.get("id") or "").strip()
        if i not in P or i in seen:
            print("UNKNOWN OR DUPLICATE ID", path, i); continue
        seen.add(i); p = P[i]
        ref = (r.get("referent") or "").strip().upper()
        if ref not in REFS: print("BAD REFERENT", i, ref)
        q = (r.get("quote") or "").strip().strip('"“”')
        ok = ""
        if q:
            parts = [x for x in re.split(r"\s*(?:…|\.\.\.)\s*", norm(q)) if len(x) > 8]
            ok = int(bool(parts) and all(x in norm(p["text"]) for x in parts))
        rows.append(dict(id=i, ident=p["ident"], region=p["region"], vol=p["vol"], district=p["district"],
                         year=p["year"], gen=p["gen"], kind=p["kind"], terms=p["terms"], referent=ref,
                         religion=(r.get("religion") or "").strip().lower(),
                         attitude=(r.get("attitude") or "").strip().lower(),
                         practice=(r.get("practice") or "").strip().lower(), tags=(r.get("tags") or "").strip(),
                         page=(r.get("page") or "").strip(), quote=q, quote_ok=ok, note=(r.get("note") or "").strip()))
todo = {i for i, p in P.items() if p["index"] == "0"}
print(len(rows), "coded;", len(todo - seen), "missing", sorted(todo - seen)[:10])
bad = [r for r in rows if r["quote_ok"] == 0]
print("quotes checked", sum(r["quote_ok"] != "" for r in rows), "not verbatim", len(bad))
for r in bad[:15]: print("  NOT VERBATIM", r["id"], r["quote"][:90])

rows.sort(key=lambda r: r["id"])
key = lambda q: re.sub(r"[^a-z]", "", q.lower())[:80]
first = {}
for r in rows:
    r["exclude"] = ""; r["copy_of"] = ""
    if r["quote"]:
        k = key(r["quote"])
        if k in first:
            f = first[k]
            if f["gen"] == r["gen"]: r["exclude"] = f"same passage as {f['id']}"
            else: r["copy_of"] = f"{f['id']} ({f['vol']} {f['year']})"
        else:
            first[k] = r
print("excluded repeats", sum(bool(r["exclude"]) for r in rows))
with open("yoga-gazetteers/results/fakir_coded_all.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, list(rows[0]), delimiter="\t"); w.writeheader(); w.writerows(rows)

rows = [r for r in rows if not r["exclude"]]
GENS = ["G1", "G2", "G3"]
c = collections.Counter((r["referent"], r["religion"], r["gen"]) for r in rows)
with open("yoga-gazetteers/results/fakir_referent_by_gen.tsv", "w", encoding="utf-8") as fh:
    fh.write("referent\treligion\t" + "\t".join(GENS) + "\n")
    for a, b in sorted({(a, b) for a, b, _ in c}):
        fh.write(f"{a}\t{b}\t" + "\t".join(str(c[(a, b, g)]) for g in GENS) + "\n")
t = collections.Counter()
for r in rows:
    if r["referent"] in IRRELEVANT: continue
    grp = "hindu" if r["religion"] in ("hindu", "sikh") else "muslim" if r["religion"] == "muslim" else "other"
    t[(grp, "attitude:" + r["attitude"], r["gen"])] += 1
    t[(grp, "practice:" + r["practice"], r["gen"])] += 1
    for tag in filter(None, (x.strip() for x in r["tags"].split(","))):
        t[(grp, tag, r["gen"])] += 1
with open("yoga-gazetteers/results/fakir_tags_by_gen.tsv", "w", encoding="utf-8") as fh:
    fh.write("religion_group\ttag\t" + "\t".join(GENS) + "\n")
    for a, b in sorted({(a, b) for a, b, _ in t}):
        fh.write(f"{a}\t{b}\t" + "\t".join(str(t[(a, b, g)]) for g in GENS) + "\n")
