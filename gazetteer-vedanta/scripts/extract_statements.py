#!/usr/bin/env python3
"""Pull religious-affiliation statements out of a Bombay Gazetteer population chapter.

Usage: python3 -I scripts/extract_statements.py VOL OCRFILE OUT_PREFIX

Anchors
  * The marginal running note printed on every page of the population chapter,
        "Chapter III. Population. <Class>. <Caste>, <Caste>."
    gives a closed list of caste names treated on that page (survives OCR well).
  * Each religion sentence (sect term + cue word) is assigned to the marginal caste
    name of the current or previous page that occurs last in the text before it.
  * Populations: "<Caste>[, or ...,] [are returned as] numbering [about] N" and
    "N (males .., females ..) [were] <Caste>" in class introductions.

Writes OUT_PREFIX.statements.tsv and OUT_PREFIX.castes.tsv.
"""
import bisect, collections, re, sys, unicodedata

vol, path, out = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(path, encoding="utf-8", errors="replace").read()
text = re.sub(r"-\s*\n\s*(?=[a-z])", "", text)
text = re.sub(r"\s+", " ", text)

FOLD = {"é": "a", "á": "a", "à": "a", "â": "a", "ä": "a", "ã": "a", "’": "'", "‘": "'"}


def skeleton(t):
    o = []
    for i, c in enumerate(t):
        if c in FOLD:
            o.append(FOLD[c]); continue
        if c in "4106|!" and 0 < i < len(t) - 1 and t[i - 1].isalpha() and t[i + 1].isalpha():
            o.append({"4": "a", "1": "i", "0": "o", "6": "o", "|": "i", "!": "i"}[c]); continue
        b = unicodedata.normalize("NFKD", c)[0]
        o.append(b.lower() if len(b) == 1 else "?")
    return "".join(o)


skel = skeleton(text)


def key(name):
    """fuzzy key for a caste name: skeleton letters only, vowels collapsed, plural s dropped."""
    s = re.sub(r"[^a-z ]", "", skeleton(name))
    s = re.sub(r"[aeiouy]+", "a", s)
    s = re.sub(r"s\b", "", s)
    return s.strip()


# ------------------------------------------------------------- population chapter + marginal notes
MARG = re.compile(r"Chapter\s*[IiHhTtlf1m]{1,3}[.,\-—•\s]{0,5}(?:Popul\w*|Peop\w*)[.,\-]?\s*((?:[A-ZÀ-ɏ][\w'’À-ɏ]*"
                  r"(?:[ -][A-Za-zÀ-ɏ][\w'’À-ɏ]*){0,3}\s?[.,;:]\s*){1,7})")
CLASSWORDS = {"brahmans", "writers", "traders", "husbandmen", "craftsmen", "manufacturers", "bards", "actors",
              "personal servants", "servants", "shepherds", "fishers", "labourers", "unsettled tribes",
              "depressed castes", "depressed classes", "beggars", "religious beggars", "musalmans", "parsis",
              "christians", "jews", "early tribes", "wild tribes", "hindus", "religion", "population",
              "movements", "census details", "census", "divisions", "language", "villages", "houses",
              "communities", "chapter", "people", "census details", "minor", "others", "ascetics", "jains",
              "traders and merchants", "musicians", "players", "castes", "tribes", "ceremonies", "customs",
              "community", "condition", "religious houses", "religious", "names", "food", "dress", "births",
              "marriages", "deaths", "migration", "towns", "schools", "teachers", "priests", "aged"}
marks = []
for m in MARG.finditer(text):
    names = [re.sub(r"[.,;:]$", "", x).strip() for x in re.split(r"(?<=[.,;:])\s+", m.group(1))]
    cl, castes = [], []
    for n in names:
        if not n or len(n) < 3:
            continue
        (cl if n.lower() in CLASSWORDS else castes).append(n)
    marks.append((m.start(), m.end(), cl, castes))

if marks:
    pos = [m[0] for m in marks]
    runs, cur = [], [pos[0]]
    for x in pos[1:]:
        if x - cur[-1] < 60000:
            cur.append(x)
        else:
            runs.append(cur); cur = [x]
    runs.append(cur)
    best = max(runs, key=len)
    POP_A, POP_B = max(0, best[0] - 25000), best[-1] + 8000
else:
    POP_A, POP_B = 0, len(text)
marks = [m for m in marks if POP_A <= m[0] <= POP_B]
mark_pos = [m[0] for m in marks]

# ------------------------------------------------------------- lexicon
LEX = [
    ("SMARTA", r"\bsm[a-z]{1,2}r?ts?\b|\bsmart[h]?a?s?\b"),
    ("SHANKARACHARYA", r"\bs[h]?[a-z]?nk[a-z]?r[a-z]{0,3}ch[a-z]{0,2}r[iy]?a?s?\b|\bs[h]?ankar[a-z]{0,3}ch"),
    ("SRINGERI", r"\bs[h]?r[i]?[a-z]?ng[ae]?r[iy]\b|\bs[h]?ring[a-z]?ri\b"),
    ("SANKESHVAR", r"\bs[h]?[a-z]nk[e]?sh?[vw][a-z]r\b"),
    ("KUDALI", r"\bk[uo]d[a-z]?l[iy]\b"),
    ("KARVIR", r"\bk[a-z]rv[i]r\b"),
    ("ADVAITA", r"\badv[a-z]{1,2}t|\badwait|\bved[a-z]nt"),
    ("GOSAVI", r"\bd[a-z]?sh?n[a-z]m|\bgos[a-z]v[i]s?\b|\bgos[a-z]{0,2}ins?\b|\bs[a-z]nn?y[a-z]s[i]"),
    ("BHAGVAT", r"\bbh[a-z]g[a-z]?v[a-z]?ts?\b"),
    ("MADHVA", r"\bm[a-z]dhv(?:[a-z]{0,2}ch|a\b|as\b|s\b)|\buttr[a-z]d[iy]|\br[a-z]gh[a-z]vendr|\bvy[a-z]sr[a-z]y"),
    ("RAMANUJA", r"\br[a-z]m[a-z]n[uo]j|\bs[h]?r[i]\s?v[a-z]{1,2}shn[a-z]v"),
    ("VALLABHA", r"\bv[a-z]ll[a-z]bh|\bpusht[i]m|\bgos[a-z]{0,2}ij[i]\b|\bm[a-z]h[a-z]r[a-z]j\b"),
    ("SVAMINARAYAN", r"\bs[vw][a-z]m[i]n[a-z]r[a-z]y[a-z]n"),
    ("RAMANANDI", r"\br[a-z]m[a-z]n[a-z]nd|\br[a-z]m[a-z]v[a-z]t|\bb[a-z]{1,2}r[a-z]g[i]s?\b"),
    ("KABIR", r"\bk[a-z]b[i]r"),
    ("VAISHNAV", r"\bv[a-z]{1,2}shn[a-z]vs?\b|\bvaishn"),
    ("SHAIVA", r"\bsh[a-z]{1,2}v[a-z]?s\b|\bshaiv|\bsaiv"),
    ("LINGAYAT", r"\bl[i]ng[a-z]{1,2}y[a-z]ts?\b|\bjang[a-z]ms?\b"),
    ("NATH", r"\bk[a-z]nph[a-z]t|\bn[a-z]thp[a-z]nth|\bgor[a-z]?kh?n[a-z]th"),
    ("MAHANUBHAV", r"\bm[a-z]h[a-z]nubh[a-z]v|\bm[a-z]nbh[a-z]v"),
    ("WARKARI", r"\bv[a-z]rk[a-z]r[i]|\bvithob|\bp[a-z]ndh[a-z]rp[uo]r"),
    ("JAIN", r"\bj[a-z]{1,2}ns?\b"),
]
LEXC = [(lab, re.compile(p)) for lab, p in LEX]
SECT = {l for l, _ in LEX} - {"WARKARI", "JAIN", "GOSAVI", "ADVAITA"}
CUE = re.compile(r"spiritual|teacher|guru|pontiff|\bsect\b|\bsects\b|follower|disciple|religio|"
                 r"\bthey are\b|\bare (?:all )?(?:either )?(?:sm|v[a-z]ishn|bh[a-z]g|l[i]ng|m[a-z]dhv|followers)|"
                 r"\bsv[a-z]m[i]\b|\bswami\b|\bmath\b|monaster|initiat|belong|\bhead\b|worship")
GURU_CUE = re.compile(r"spiritual|teacher|guru|pontiff|guide|disciple|follower|initiat|\bhead\b|\bsv[a-z]m[i]\b|\bswami\b")

# ------------------------------------------------------------- pages
PAGE = re.compile(r"Bombay\s+Gazetteer,?\]?\s+(\d{1,4})\b|\b[A-Z]{4,}[.:,]?\s+(\d{1,4})(?=\s+[A-Z(‘'\[])")
pages = [(m.start(), m.group(1) or m.group(2)) for m in PAGE.finditer(text)]
page_pos = [p for p, _ in pages]


def page_at(a):
    i = bisect.bisect_right(page_pos, a) - 1
    return pages[i][1] if i >= 0 else ""


# ------------------------------------------------------------- caste assignment
def candidates_near(a):
    """marginal caste names of this and the previous two marginal notes."""
    i = bisect.bisect_right(mark_pos, a) - 1
    names, cls = [], []
    for j in range(max(0, i - 2), min(len(marks), i + 2)):
        names += marks[j][3]
        cls += marks[j][2]
    return list(dict.fromkeys(names)), (marks[i][2] if i >= 0 else [])


skel_keyspace = None


def last_mention(name, a, window=8000):
    """position of the last mention of `name` before offset a (fuzzy on skeleton)."""
    k = re.sub(r"[^a-z]", "", skeleton(name))
    if len(k) < 3:
        return -1
    stem = k[:max(4, min(len(k) - 1, 7))]
    # allow OCR vowel noise inside the stem
    pat = re.compile(r"\b" + "".join(c if c not in "aeiou" else "[a-z]" for c in stem))
    best = -1
    for m in pat.finditer(skel, max(0, a - window), a):
        best = m.start()
    return best


bounds = [0] + [m.end() for m in re.finditer(r"(?<=[a-z\)\]'’”])[.;]\s+(?=[A-Z‘'\"“])", text)] + [len(text)]
rows = []
for i in range(len(bounds) - 1):
    s0, s1 = bounds[i], bounds[i + 1]
    if s1 < POP_A or s0 > POP_B:
        continue
    sk = skel[s0:s1]
    labs = [lab for lab, rx in LEXC if rx.search(sk)]
    if not (set(labs) & SECT) or not CUE.search(sk):
        continue
    names, cls = candidates_near(s0)
    # mentions inside the sentence itself before the sect term also count
    scored = sorted(((last_mention(n, s0 + 60), n) for n in names), reverse=True)
    caste = scored[0][1] if scored and scored[0][0] >= 0 else ""
    dist = s0 - scored[0][0] if caste else ""
    sent = text[s0:s1].strip()
    rows.append([vol, str(s0), page_at(s0), "/".join(cls), caste, str(dist), "|".join(names),
                 ",".join(labs), "guru" if GURU_CUE.search(sk) else "",
                 sent[:800] + ("…" if len(sent) > 800 else "")])

# ------------------------------------------------------------- populations
NUMWORD = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve "
                                         "thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
NUMWORD.update({"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
                "ninety": 90})


def num(s):
    d = re.sub(r"[^\d]", "", s)
    if d:
        return int(d)
    tot = 0
    for w in re.split(r"[\s-]+", s.lower()):
        tot += NUMWORD.get(w, 0)
    return tot or None


pops = []
P1 = re.compile(r"([A-Z][\w'’À-ɏ]+(?: [A-Z][\w'’À-ɏ]+){0,2})[^.;|\d]{0,170}?,?\s+"
                r"(?:(?:are|aro|arc|ave|ate|is)\s+)?(?:return[\w-]*\s*(?:as\s+)?)?num[\w-]*\s*b?\w*\s+"
                r"(?:about|abont|only|perhaps about|in all)?\s*([\d,]{2,9}|[a-z]+(?:-[a-z]+)?)(?!\s*(?:houses|famil))")
P2 = re.compile(r"\b([\d,]{2,9})\s*\((?:males?|m\.)\s*[\d,]+\s*,\s*(?:females?|f\.)\s*[\d,]+\)\s*(?:were\s+)?"
                r"([A-Z][\w'’À-ɏ]+(?: [A-Z][\w'’À-ɏ]+){0,2})")
for rx, order in ((P1, (1, 2)), (P2, (2, 1))):
    for m in rx.finditer(text, POP_A, POP_B):
        name, n = m.group(order[0]), num(m.group(order[1]))
        if n and name.split()[0] not in {"The", "They", "These", "Of", "In", "Total", "Hindus", "Musalmans", "And"}:
            pops.append((key(name), name, n, page_at(m.start())))
popd = collections.defaultdict(list)
for k, name, n, pg in pops:
    popd[k].append((n, name, pg))

# ------------------------------------------------------------- per-caste summary
by = collections.defaultdict(lambda: collections.Counter())
guru = collections.defaultdict(lambda: collections.Counter())
cls_of = {}
for r in rows:
    c = r[4] or "?"
    for l in r[7].split(","):
        by[c][l] += 1
        if r[8]:
            guru[c][l] += 1
    cls_of.setdefault(c, r[3])

with open(out + ".statements.tsv", "w", encoding="utf-8") as f:
    f.write("vol\toffset\tpage\tclass\tcaste\tdist\tcandidates\tlabels\tguru_cue\tsentence\n")
    for r in rows:
        f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
allcastes = list(dict.fromkeys([c for m in marks for c in m[3]]))
with open(out + ".castes.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tclass\tcaste\tpopulation\tpop_source_name\tlabels_all\tlabels_guru\n")
    seen = set()
    for c in allcastes + [c for c in by if c not in allcastes]:
        k = key(c)
        if k in seen:
            continue
        seen.add(k)
        p = popd.get(k) or popd.get(re.sub(r"a$", "", k)) or []
        p = max(p, key=lambda x: x[0]) if p else ("", "", "")
        cl = next((m[2] for m in marks if c in m[3]), [])
        f.write("\t".join([vol, "/".join(cl[-1:]), c, str(p[0]), p[1],
                           ",".join(f"{l}:{n}" for l, n in by[c].most_common()),
                           ",".join(f"{l}:{n}" for l, n in guru[c].most_common())]) + "\n")
print(f"{vol}: pop chapter {POP_A}-{POP_B}, {len(marks)} marginal notes, {len(allcastes)} marginal castes, "
      f"{len(rows)} statements, {len(pops)} population figures", file=sys.stderr)
