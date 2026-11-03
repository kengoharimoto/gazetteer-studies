# Coding instructions: Śaṅkara maṭha presence in the gazetteers

Goal: for each Śaṅkara maṭha (seat or branch), record **where the gazetteers locate it and what they say about it
there**. Places chapters come first, but other chapters count too when they place a maṭha somewhere: its
buildings, estates or inām villages, revenue, grants, branches, the head's residence or tours, and disputes.

Working directory: `/mnt2/kengo/research/gazetteer-vedanta/`. Run Python only with `python3 -I`. Do not modify
anything outside your own output file.

## Input
- `mathas/results/hits_dedup.tsv` has these columns: hit_id, seat, volume, file, line, page_guess, match,
  context.
  - `file` is `<region>/<identifier>`. The OCR text is at `<region>/data/ia_ocr/<identifier>.txt`, where
    region `bombay` means top-level `data/ia_ocr/`.
  - `line` is the line number in that file.
- Your assignment lists the seats and volumes to cover.
- For every relevant hit, **open the OCR around the line** (sed -n 'L-60,L+80p') and read the whole entry. The
  context column is only a pointer.
- Many hits are false positives: Joshimath the town, Sankeshvar the market town on a road, Shankheshvar the
  Jain shrine, "Pushpagiri" the hill, people's surnames. Skip these quickly, unless the entry also describes
  a maṭha.
- Also search the volumes in your assignment for things the hit list may miss. Use grep -n on the seat's
  name, "math", "mutt", "Swami" or "Svami", "Shankaracharya", and the place names.

## Output
Write one TSV to the path given in your assignment, with this header (tab-separated):

```
id	seat	volume	year	district	place	institution	link	chapter	what_is_said	quote	page	confidence	notes
```

- **id:** your prefix plus a number (e.g. W01).
- **seat:** sankeshvar, karvir, sringeri, kudali, dvarka, jyotirmath, govardhan, kanchi_kumbakonam,
  pushpagiri, virupaksha, sivaganga, other (name it in notes), or unnamed_shankaracharya.
- **volume:** the label from hits_dedup (or the selection file). **year:** the publication year.
- **district / place:** the district, and the town or village where the institution is located.
- **institution:** what is there (e.g. "maṭh of the Sankeshvar Svāmi", "inām village", "tomb and monastery").
- **link:** one of:
  - `seat`: the head's own seat;
  - `branch`: a subordinate maṭha;
  - `estate`: inām or jāgīr land or villages;
  - `residence`: the head lives or stayed there;
  - `visit`: a tour or visit;
  - `temple`: a temple founded, managed or rebuilt by the maṭha;
  - `tradition`: a local tradition of Śaṅkara or the seat with no institution described;
  - `jurisdiction`: a statement of the territory or castes under it, if tied to a place.
- **chapter:** Places, or the chapter name if not Places (e.g. Castes, History, Religion, Land administration).
- **what_is_said:** a short summary. Include the figures (income, villages, acreage, population, dates) and
  who the followers are.
- **quote:** VERBATIM from the OCR, with OCR errors kept as they are. Copy enough to identify the passage
  (≥ 12 words). Never paraphrase inside this column.
- **page:** the printed page if you can find it (headers like "BELGAUM. 601" or isolated numbers). Otherwise
  "s.v. <entry name>".
- **confidence:** high, medium or low.
- **notes:** anything else: conflicts between sources, a reprint of an earlier text (for revised gazetteers),
  OCR uncertainty.

## Rules
- One row per place per volume per institution. If one entry describes the maṭha, its villages and its
  revenue, make one row and put the details in what_is_said.
- Caste chapter lines like "their guru is the Shankaracharya of Sankeshvar", with no place or institution,
  are NOT rows. Count them instead in a final comment line at the end of the file:
  `# caste_allegiance_mentions <seat> <volume>: <n>`.
- Vaiṣṇava, Mādhva, Liṅgāyat, Jain and Nāth maṭhas are not rows. The exception is when the text explicitly
  connects them to a Śaṅkara seat.
- For a revised (post-1950) gazetteer, say in notes whether the passage reprints the colonial text.
- Be complete for your assigned volumes and seats. When done, reply with a 10-line summary: the number of rows
  by seat, the most important passages, and anything surprising.
