# Coding instructions: Karnataka State Archives files on the Śṛṅgeri and Kudli Śṛṅgeri maṭhas

The files are Mysore government records, digitised by the Karnataka State Archives and put on the Internet
Archive:
- Muzrai (religious endowments) files;
- Revenue (SR), Local Fund (LB), General and Financial (GF), Police (POL), Municipal (MUPL/ML) and
  Land-Records (dep-lr) files;
- Mysore Gazette notices and Mysore Code regulations.

Each file is a scan of a manuscript or typescript file. The typed parts (notes to the Dewan or Maharaja, orders,
printed proceedings) are usually OCR'd legibly. Handwritten notes and Kannada are garbled.

Goal: what the records show about the maṭhs as institutions:
- their lands (jāgīr, inām villages, properties inside and outside Mysore State) and revenues (land revenue,
  ganja/toddy/excise shares, cash allowances, loans);
- their branches (other maṭhs of the Śṛṅgeri line, and where they are);
- the head's tours and the honours the State granted or refused;
- succession;
- State management and intervention (agents, Government management 1935–40, audits);
- disputes with other maṭhs (Mādhva, Liṅgāyat) over processions and honours.

Working directory: `/mnt2/kengo/research/gazetteer-vedanta/`. Run Python only with `python3 -I`. Write only your
own output file.

## Input
- `mathas/archives/results/catalogue.tsv` has these columns: identifier, year, title, description, matha,
  topic, include. The OCR is in `mathas/data/archives/ocr/<identifier>.txt`. Some are empty: no OCR on IA.
- Your assignment lists the files to cover (by matha and/or year range).

## Output
Write one TSV per assignment, with this header:

```
id	identifier	year	matha	topic	places	what_is_said	quote	legibility	confidence	notes
```

- **matha:** sringeri (the seat at Sringeri), kudli_sringeri (the Kudli Śṛṅgeri maṭh, Shimoga taluk),
  avani_sringeri, hubli_sringeri, sringeri_branch (name the place in places), or other (name it in notes).
  - Distinguish carefully: "Sri Akshobhya Tirtha matt at Kudli" is a Mādhva maṭh. It is NOT the Kudli
    Śṛṅgeri maṭh. Skip it unless the file compares the two.
- **topic:** one of
  - `estate` (jāgīr, ināms, villages, leases, resumption, nazarana);
  - `revenue` (excise/ganja/toddy/land-revenue shares, cash allowances, tasdik);
  - `finance` (loans, debts, investments, suits for recovery);
  - `management` (agents, Government management, budgets, audits, internal affairs);
  - `succession`;
  - `tour_honours` (visits, tours, insignia, rahadari, guards, escorts, temple maryādas, procession disputes);
  - `branch` (another maṭh of the line, or property at a named place);
  - `local` (municipality, roads, schools, police);
  - `other`.
- **places:** every place the file ties to the maṭh's property, branch or tour, separated by `;`. Use the
  form "Village (Taluk, District/State)" where given.
- **what_is_said:** 1–4 sentences. Give the figures (rupees, acres, villages, dates), the parties, and the
  decision or order. Say who decided: Muzrai Commissioner, Dewan, Maharaja, Madras Government.
- **quote:** VERBATIM from the OCR (≥ 12 words), with OCR errors kept as they are. Pick the sentence that best
  carries the content. If the OCR is illegible or empty, write `(no legible text)` and base what_is_said on
  the catalogue description, saying so in notes.
- **legibility:** `good`, `partial` or `none`.
- **confidence:** `high`, `medium` or `low`.
- **notes:** anything else: conflicts, links to other files, the claimed origin of a branch, OCR doubts.

## Rules
- One row per file. If a file is irrelevant (e.g. a plague notice, a road in Sringeri town), still give it a
  row with topic `local` or `other` and a one-line what_is_said. Coverage must be complete for your
  assignment.
- Read the legible parts of each file properly. Search inside long files with grep for "Matt", "Mutt", "inam",
  "village", "Rs", "Swami", "Jagadguru", "branch", "Madras", "Nizam", "Bombay" and the place names.
- Never invent text: quotes must be copyable from the OCR file.
- When done, reply with a ≤15-line summary covering:
  - the number of rows and how many were legible;
  - the main facts about the maṭh's lands and revenues, with figures;
  - the branches and their places;
  - the State's interventions;
  - anything surprising.
