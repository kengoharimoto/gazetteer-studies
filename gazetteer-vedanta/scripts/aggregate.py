#!/usr/bin/env python3
"""Combine coded caste rows into district summaries.

Usage: python3 -I scripts/aggregate.py   (run from the study directory)

Reads results/coded/*.coded.tsv and data/district_hindu_totals.tsv; writes
  results/district_affiliation.tsv  one row per district x affiliation group:
      coded population, share of the district's Hindu population, number of castes, castes
  results/smarta_castes.tsv         every SMARTA / SMARTA_BHAGVAT row, with seat, class, quote
  results/pitha_mentions.tsv        seats named, by district
Only rows with scope = caste or part and a population figure count towards the shares; `part`
rows are counted at full population but flagged (the Gazetteer gives no proportion).
"""
import csv, glob, collections, os

GROUP = {
    "SMARTA": "Smarta (Shankaracharya)", "SMARTA_BHAGVAT": "Smarta (Shankaracharya)",
    "MADHVA": "Madhva", "RAMANUJA": "Ramanuja/Shrivaishnava", "VALLABHA": "Vallabha",
    "SVAMINARAYAN": "Svaminarayan", "RAMANANDI": "Ramanandi/Bairagi", "KABIR": "Kabirpanthi",
    "VAISHNAV_UNSPEC": "Vaishnava (unspecified)", "SHAIVA_UNSPEC": "Shaiva (unspecified)",
    "LINGAYAT": "Lingayat", "NATH": "Nath", "MAHANUBHAV": "Mahanubhav", "JAIN": "Jain",
    "MIXED": "Mixed (several sects named)", "OTHER_GURU": "Other named guru", "NONE_STATED": "None stated",
}

totals = {}
for r in csv.DictReader(open("data/district_hindu_totals.tsv", encoding="utf-8"), delimiter="\t"):
    totals[r["vol"]] = r

rows = []
for f in sorted(glob.glob("results/coded/*.coded.tsv")):
    with open(f, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if not r.get("caste") or r["caste"].upper().startswith("ALL "):
                continue
            rows.append(r)


def num(x):
    try:
        return int(str(x).replace(",", "").strip())
    except ValueError:
        return None


agg = collections.defaultdict(lambda: {"pop": 0, "n": 0, "n_nopop": 0, "part": 0, "castes": []})
for r in rows:
    if r.get("scope") not in ("caste", "part"):
        continue
    g = GROUP.get(r["affiliation"].strip(), r["affiliation"].strip() or "?")
    a = agg[(r["vol"], g)]
    p = num(r.get("population"))
    a["n"] += 1
    if p:
        a["pop"] += p
    else:
        a["n_nopop"] += 1
    if r["scope"] == "part":
        a["part"] += 1
    a["castes"].append(f'{r["caste_std"] or r["caste"]}{"" if p else " (no fig.)"}{" [part]" if r["scope"] == "part" else ""}'
                       f'{" =" + str(p) if p else ""}')

vols = sorted({k[0] for k in agg}, key=lambda v: list(totals).index(v) if v in totals else 99)
with open("results/district_affiliation.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tdistrict\tregion\tcensus\thindu_total\tgroup\tcoded_pop\tshare_pct\tn_castes\tn_without_pop\tn_part\tcastes\n")
    for v in vols:
        t = totals.get(v, {})
        tot = num(t.get("hindu_total"))
        for (vv, g), a in sorted(agg.items(), key=lambda kv: -kv[1]["pop"]):
            if vv != v:
                continue
            share = f'{100 * a["pop"] / tot:.1f}' if tot and a["pop"] else ""
            f.write("\t".join([v, t.get("district", ""), t.get("region", ""), t.get("census", ""),
                               str(tot or ""), g, str(a["pop"]), share, str(a["n"]), str(a["n_nopop"]),
                               str(a["part"]), "; ".join(a["castes"])]) + "\n")

with open("results/smarta_castes.tsv", "w", encoding="utf-8") as f:
    cols = ["vol", "district", "caste", "caste_std", "class", "population", "pop_year", "affiliation", "pitha",
            "scope", "evidence_page", "confidence", "quote", "note"]
    f.write("\t".join(cols) + "\n")
    for r in rows:
        if r["affiliation"].strip() in ("SMARTA", "SMARTA_BHAGVAT") or "smart" in (r.get("note") or "").lower() \
                and r["affiliation"].strip() == "MIXED":
            f.write("\t".join((r.get(c) or "").replace("\t", " ") for c in cols) + "\n")

pm = collections.defaultdict(collections.Counter)
for r in rows:
    if r.get("pitha"):
        pm[r["vol"]][r["pitha"].strip()] += 1
with open("results/pitha_mentions.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tpitha\tn_castes\n")
    for v in pm:
        for p, n in pm[v].most_common():
            f.write(f"{v}\t{p}\t{n}\n")
print(f"{len(rows)} coded rows from {len(set(r['vol'] for r in rows))} volumes")

# ------------------------------------------------------------- Smarta range per district
# tier 1 (lo):  castes coded SMARTA / SMARTA_BHAGVAT, scope caste
# tier 2 (mid): + Smarta `part` rows + MIXED rows whose sect list ("A|B" in `note`) includes Smart
# tier 3 (hi):  + MIXED Smart rows that the text calls nominal ("cannot tell", "nominally")
import re
NOMINAL = re.compile(r"cannot\s*tel|can not tel|nominally|nominal", re.I)
rng = collections.defaultdict(lambda: {"lo": 0, "mid": 0, "hi": 0, "n_lo": 0, "n_mid": 0, "n_hi": 0, "nofig": [],
                                       "mixed": [], "nominal": []})
for r in rows:
    aff, scope = r["affiliation"].strip(), r.get("scope")
    if scope not in ("caste", "part"):
        continue
    p = num(r.get("population"))
    note = r.get("note") or ""
    is_sm = aff in ("SMARTA", "SMARTA_BHAGVAT")
    # the sect list is written "A|B|C" in `note`; Smart must be one of its members
    is_mixed_sm = aff == "MIXED" and re.search(r"(?:^|[\s|(])Smart\w*\s*\||\|\s*Smart", note)
    if not (is_sm or is_mixed_sm):
        continue
    d = rng[r["vol"]]
    name = r.get("caste_std") or r["caste"]
    if not p:
        d["nofig"].append(name)
        continue
    nominal = is_mixed_sm and NOMINAL.search((r.get("quote") or "") + " " + (r.get("note") or ""))
    if is_sm and scope == "caste":
        d["lo"] += p; d["n_lo"] += 1
    if not nominal:
        d["mid"] += p; d["n_mid"] += 1
        if is_mixed_sm or scope == "part":
            d["mixed"].append(f"{name} {p}")
    else:
        d["nominal"].append(f"{name} {p}")
    d["hi"] += p; d["n_hi"] += 1
with open("results/smarta_range.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tdistrict\tregion\tcensus\thindu_total\tasserted\tasserted_pct\twith_mixed\twith_mixed_pct\t"
            "with_nominal\twith_nominal_pct\tn_asserted\tmixed_or_part_castes\tnominal_castes\tsmarta_castes_without_figure\n")
    for v in totals:
        t = totals[v]; d = rng.get(v)
        if not d:
            continue
        tot = num(t["hindu_total"])
        pct = lambda x: f"{100 * x / tot:.1f}" if tot else ""
        f.write("\t".join([v, t["district"], t["region"], t["census"], str(tot or ""), str(d["lo"]), pct(d["lo"]),
                           str(d["mid"]), pct(d["mid"]), str(d["hi"]), pct(d["hi"]), str(d["n_lo"]),
                           "; ".join(d["mixed"]), "; ".join(d["nominal"]), "; ".join(d["nofig"])]) + "\n")
