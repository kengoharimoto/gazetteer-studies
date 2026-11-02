#!/usr/bin/env python3
"""Identify which Bombay Gazetteer volume each downloaded OCR file is, and score OCR quality.

Usage: python3 -I scripts/identify_volumes.py data/ia_candidates.tsv data/ia_ocr > data/volumes.tsv

Identification uses the IA title first, then the running heads / title page in the text
("[Bombay Gazetteer," + district name). Quality = share of alphabetic tokens (len>=4)
found in /usr/share/dict/words (crude, but ranks scans of the same volume well).
"""
import csv, os, re, sys, collections

# vol -> (district/subject, list of name variants used for matching)
VOLS = {
    "II": ("Surat and Broach", ["surat", "broach"]),
    "III": ("Kaira and Panch Mahals", ["kaira", "panch mahal"]),
    "IV": ("Ahmedabad", ["ahmedabad", "ahmadabad"]),
    "V": ("Cutch, Palanpur, Mahi Kantha", ["cutch", "palanpur", "mahi kantha"]),
    "VI": ("Rewa Kantha, Narukot, Cambay, Surat States", ["rewa kantha", "narukot", "cambay"]),
    "VII": ("Baroda", ["baroda"]),
    "VIII": ("Kathiawar", ["kathiawar"]),
    "IX-1": ("Gujarat Population: Hindus", ["gujarat population"]),
    "X": ("Ratnagiri and Savantvadi", ["ratnagiri", "savantvadi"]),
    "XI": ("Kolaba and Janjira", ["kolaba", "janjira"]),
    "XII": ("Khandesh", ["khandesh"]),
    "XIII-1": ("Thana pt 1", ["thana"]),
    "XIII-2": ("Thana pt 2", ["thana"]),
    "XIV": ("Thana places", ["thana"]),
    "XV-1": ("Kanara pt 1", ["kanara"]),
    "XV-2": ("Kanara pt 2", ["kanara"]),
    "XVI": ("Nasik", ["nasik"]),
    "XVII": ("Ahmadnagar", ["ahmadnagar", "ahmednagar"]),
    "XVIII-1": ("Poona pt 1", ["poona"]),
    "XVIII-2": ("Poona pt 2", ["poona"]),
    "XVIII-3": ("Poona pt 3", ["poona"]),
    "XIX": ("Satara", ["satara"]),
    "XX": ("Sholapur", ["sholapur"]),
    "XXI": ("Belgaum", ["belgaum"]),
    "XXII": ("Dharwar", ["dharwar"]),
    "XXIII": ("Bijapur", ["bijapur"]),
    "XXIV": ("Kolhapur", ["kolhapur"]),
}
ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50}


def roman(s):
    s = s.lower(); v = 0
    for a, b in zip(s, s[1:] + " "):
        x = ROMAN.get(a, 0); y = ROMAN.get(b, 0)
        v += -x if x < y else x
    return v


def to_roman(n):
    out = ""
    for val, sym in [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= val:
            out += sym; n -= val
    return out


words = set(w.strip().lower() for w in open("/usr/share/dict/words", encoding="utf-8", errors="ignore"))


def quality(text):
    toks = re.findall(r"[A-Za-z]{4,}", text[: 2_000_000])
    if not toks:
        return 0.0
    return sum(t.lower() in words for t in toks) / len(toks)


def district_votes(text):
    body = text.lower()
    c = collections.Counter()
    for vol, (_, names) in VOLS.items():
        c[vol] = sum(body.count(n) for n in names)
    return c


cand = {r["identifier"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t")}
d = sys.argv[2]
print("identifier\tyear\tia_title\tvol_guess\tdistrict\tchars\tquality\tpop_chapter\tbrahman_hits")
for fn in sorted(os.listdir(d)):
    if not fn.endswith(".txt") or fn.startswith("_"):
        continue
    ident = fn[:-4]
    t = open(os.path.join(d, fn), encoding="utf-8", errors="replace").read()
    r = cand.get(ident, {})
    title = (r.get("title", "") + " " + r.get("volume", "")).replace("\t", " ")
    # volume number from title, e.g. "Vol. 18 Part 1", "Vol.xviii Pt.ii", "Volume XV Part II"
    guess = ""
    m = re.search(r"vol(?:ume)?[\s.\-;]*([0-9]+|[ivxl]+)\b(?:.*?(?:part|pt)[\s.]*([0-9]+|[ivx]+)\b)?", title, re.I)
    if m:
        n = int(m.group(1)) if m.group(1).isdigit() else roman(m.group(1))
        p = m.group(2)
        guess = to_roman(n) if n else ""
        if p:
            guess += "-" + str(int(p) if p.isdigit() else roman(p))
    votes = district_votes(t)
    top = votes.most_common(1)[0][0] if votes else ""
    if not guess or guess not in VOLS and guess.split("-")[0] not in [k.split("-")[0] for k in VOLS]:
        guess = guess or ("?" + top)
    pop = len(re.findall(r"Chapter I[IT1l]{2}\.?\s*\n*\s*Population", t))
    br = len(re.findall(r"(?i)br[aáâéà4]hman", t))
    print("\t".join([ident, r.get("year", ""), title[:90], guess, VOLS.get(guess, ("", []))[0] or top,
                     str(len(t)), f"{quality(t):.3f}", str(pop), str(br)]))
