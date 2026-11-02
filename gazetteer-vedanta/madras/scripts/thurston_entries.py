#!/usr/bin/env python3
"""Split Thurston, Castes and Tribes of Southern India (1909; Gutenberg text) into entries and
extract the sentences about sect, guru and math from each.

Usage: python3 -I scripts/thurston_entries.py   (from madras/) ->
  results/thurston/entries.tsv      vol, entry, start_line, n_chars, n_cue_sentences
  results/thurston/packets/volN.txt for each entry with cues: heading + line no. + the cue sentences
                                    (with one sentence of context either side)
"""
import os, re

CUE = re.compile(r"(?i)sm[aâ]rt|s[ah]?ankar[aâ]?ch|sr[iî]nger|sivaganga|kumbak[oô]n|conjeeveram|kanchi|kamakoti|"
                 r"pushpagiri|virupaksh|hampi|ahobil|vanamamalai|parakal|te[nn]galai|tenkalai|vadagalai|vadakalai|"
                 r"madhva|ramanuj|lingay|saivite|vaishnav|\bsaiva\b|\bguru|\bmutts?\b|\bmath\b|spiritual|sect\b|"
                 r"tiruvadu|dharmapur|pandaram|dasari|satani|sri vaishnava|tatacharya|jiyar|swami")
os.makedirs("results/thurston/packets", exist_ok=True)
rows = []
for n in range(1, 8):
    raw = open(f"data/thurston/vol{n}.txt", encoding="latin-1").read().replace("\r", "")
    a = raw.find("*** START OF")
    b = raw.find("*** END OF")
    body = raw[a:b if b > 0 else len(raw)]
    lines = body.split("\n")
    heads = [(i, m.group(1)) for i, l in enumerate(lines)
             for m in [re.match(r"^([A-Z][\w'À-ÿ ()-]{1,50}?)\.--", l)] if m]
    out = []
    for k, (i, name) in enumerate(heads):
        j = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        text = re.sub(r"\s+", " ", " ".join(lines[i:j]))
        sents = re.split(r"(?<=[.;!?\"])\s+(?=[A-Z\"(\[])", text)
        hit = [s_i for s_i, s in enumerate(sents) if CUE.search(s)]
        keep = sorted({x for h in hit for x in (h - 1, h, h + 1) if 0 <= x < len(sents)})
        rows.append((n, name, i, len(text), len(hit)))
        if hit:
            out.append(f"### {name}  [vol {n}, line {i}, {len(text)} chars]\n" +
                       "\n".join(("* " if x in hit else "  ") + sents[x] for x in keep) + "\n")
    open(f"results/thurston/packets/vol{n}.txt", "w", encoding="utf-8").write("\n".join(out))
with open("results/thurston/entries.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tentry\tstart_line\tn_chars\tn_cue_sentences\n")
    for r in rows:
        f.write("\t".join(map(str, r)) + "\n")
print(len(rows), "entries;", sum(1 for r in rows if r[4]), "with cues")
