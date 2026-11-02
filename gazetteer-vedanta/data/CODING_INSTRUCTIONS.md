# Coding instructions: caste-level sect affiliation in the Bombay Gazetteer

You are coding religious-affiliation statements from the population chapter (Chapter III) of one or
more volumes of the *Gazetteer of the Bombay Presidency* (ed. J. M. Campbell, 1877–1904).
Input per volume (in `results/extract/`):

- `<VOL>.statements.tsv`: sentences containing a sect term plus a religious cue word, with an
  automatic caste guess (`caste`, from the marginal running notes; often the class heading like
  "Brahmans" or an OCR-garbled caps form such as "DESUASTHS"), the page, and the matched `labels`.
- `<VOL>.castes.tsv`: the castes named in the marginal notes, with any population figure found.
- The full OCR text is in `data/ia_ocr/<identifier>.txt` (see `data/selection.tsv` for which file is
  which volume). **Consult it** whenever the caste of a statement is unclear: search for the
  sentence and read backwards to the start of the caste account ("X, or Y, are returned as
  numbering about N…", or in the 1880–83 volumes "X, or Y, are found…").

## Output

One TSV per volume, `results/coded/<VOL>.coded.tsv`, with header:

```
vol	district	caste	caste_std	class	population	pop_year	affiliation	pitha	scope	evidence_page	quote	confidence	note
```

One row per caste (or per caste section, if the text splits a caste, e.g. Deshasths into Smarts
and Madhvas: then one row per section, with its own population if given).

- `caste`: as printed (repair OCR: "Karha'da's" → "Karhadas"); `caste_std`: standard romanised
  form without diacritics, e.g. `Deshastha`, `Chitpavan/Konkanastha`, `Maratha`, `Kunbi`, `Lingayat Vani`.
- `class`: the Gazetteer's class heading (Brahmans, Writers, Traders, Husbandmen, Craftsmen, ...).
- `population`: the figure the Gazetteer gives for this caste in this district (integer, no commas);
  blank if none. `pop_year`: 1872 or 1881 (whichever census the volume uses; usually stated).
- `affiliation`: one code (pick the one the text asserts for this caste as a whole; if the text
  splits the caste, split the row):
  - `SMARTA` — said to be Smarts, or their guru/spiritual teacher/head is a Shankaracharya or a
    Smart svami (any seat).
  - `SMARTA_BHAGVAT` — explicitly "Smart Bhagvats" / "Bhagvats" in a Smarta sense (Deccan usage).
  - `MADHVA`, `RAMANUJA`, `VALLABHA`, `SVAMINARAYAN`, `RAMANANDI`, `KABIR`, `MAHANUBHAV`,
    `NATH`, `LINGAYAT`, `JAIN`
  - `VAISHNAV_UNSPEC` — "Vaishnavs" with no further school; `SHAIVA_UNSPEC` — "Shaivs" with no school.
  - `MIXED` — the text says the caste is divided between named sects without proportions
    (put the sects in `note`, e.g. "Smart|Madhva").
  - `OTHER_GURU` — a named guru/math that is none of the above (name it in `pitha`).
  - `NONE_STATED` — use only if the caste appears in the statements but no affiliation is asserted
    (e.g. it is only compared with Smarts).
- `pitha`: the seat or teacher named, normalised: `Sringeri`, `Sankeshvar`, `Kudali`, `Karvir`,
  `Dvarka`, `Kanchi`, `Sonavda (Kavale)`, `Uttaradi`, `Raghavendra`, `Vyasaraya`, etc.; else as printed.
- `scope`: `caste` (statement about the caste as a whole), `part` (about some of them: "some are…",
  "a few…"), or `general` (statement about Hindus/Brahmans of the district in general — code these
  as separate rows with caste = `ALL HINDUS` or `ALL BRAHMANS`).
- `quote`: the decisive sentence, verbatim from the OCR (trim to ≤ 300 chars).
- `confidence`: `high` (explicit, caste unambiguous), `medium` (explicit but caste attribution
  inferred from context), `low` (OCR or attribution doubtful).
- `note`: anything a historian should know (e.g. "guru visits yearly and receives presents",
  "also worship Vithoba", "teacher is a Gosavi of the Bharati order").

## Rules

- Do not infer affiliation from caste stereotypes or outside knowledge; code only what this
  Gazetteer volume says. A caste with no statement simply gets no row.
- Ignore sentences that only *mention* a sect in passing (history of Madhva pontiffs, comparison
  "unlike Smarts…") unless they assert something about a caste's own affiliation.
- Renunciant groups (Gosavis, Sanyasis, Bairagis, Jangams) are coded like any caste, with a `note`.
- Keep OCR-garbled quotes as they are in the OCR, so they can be found again by search.
- Report at the end: number of rows per volume, and any volume where the statements file looked
  badly segmented or the OCR was too poor (and which backup scan in `data/selection.tsv` you used).
