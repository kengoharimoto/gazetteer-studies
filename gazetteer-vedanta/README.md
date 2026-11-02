# Śaṅkara's following in the Bombay Presidency, c. 1872–1901 (Gazetteer study)

How widespread was allegiance to Śaṅkara's lineages (Smārta householders under a Śaṅkarācārya,
Daśanāmī renunciants), region by region, in the *Gazetteer of the Bombay Presidency*
(ed. J. M. Campbell, 27 vols, 1877–1904), and did the picture change?

## Sources

- `data/selection.tsv`: the volumes used (vols II–XXIV; population chapters), with the Internet
  Archive identifier of the primary and backup scan of each. OCR text in `data/ia_ocr/`
  (`<identifier>.txt`, IA `_djvu.txt`; untrusted downloaded data).
- `data/ia_candidates.tsv`: all IA items found for "Gazetteer … Bombay" (catalogue search, 2026-11-02).

## Two layers of evidence

1. **District sect tables, 1872 census.** Volumes based on the 1872 census print
   "<District> Hindu Sects, 1872" (Vaiṣṇava subdivided into Rāmānuja, Vallabhācārī, Kabīrpanthī,
   Mādhvācārī, Svāminārāyaṇa; Śaiva; Ascetics; "Unsectarian" / "Mixed"; Śrāvaka) with a prose
   summary. **The 1872 classification has no Smārta category**: Smārtas presumably fall under
   "unsectarian/mixed" (or Śaiva). Extracted with `scripts/extract_sect_census.py`
   (`--dump` prints the passages for hand transcription; the OCR mangles figures).
2. **Caste accounts.** Each caste account states religious practice, often naming the caste's
   guru ("Their spiritual teacher is Shankarāchārya the pontiff of the Smart Brāhmans",
   Marāṭhās of Dharwar, vol. XXII p. 138). `scripts/extract_statements.py` pulls every sentence
   with a sect term and a religious cue word and attaches it to a caste via the marginal running
   notes ("Chapter III. Population. <Class>. <Caste>."). The statements are then coded by caste
   following `data/CODING_INSTRUCTIONS.md` into `results/coded/<VOL>.coded.tsv`.

Gujarat district volumes (II–VIII) have short population chapters; Gujarati caste accounts are
in vol. IX pt 1 (1901, province-wide, not by district).

## Scripts

- `fetch_ia_ocr.py`: download IA OCR for a candidate list or `selection.tsv`.
- `identify_volumes.py`: guess volume and score OCR quality (dictionary-word share).
- `extract_statements.py`: religion statements + marginal-note caste index + population figures
  (`results/extract/<VOL>.statements.tsv`, `.castes.tsv`).
- `extract_sect_census.py`: 1872 census sect summaries.
- `extract_accounts.py`: earlier attempt segmenting by caste-account openings (works for the
  1884–86 template only; superseded by `extract_statements.py`, kept for comparison).
- `aggregate.py`: district tables from the coded rows (`results/smarta_range.tsv` etc.).
- `plot_map.py`: `results/smarta_map.png` (needs matplotlib; run without `-I`).

## Results

`results/README.md`: the report (Bombay pilot, coded 2026-11-02).

## Status and next steps

- Bombay Presidency: done (cross-section 1872–86). Change over time still open: compare with the revised
  state gazetteers (Poona 1954, Dharwar 1959 on IA) and check the 1881–1901 Bombay census reports.
- Madras Presidency: done with Thurston (1909) and the 1871/1891 census, because the Madras
  manuals and gazetteers lack caste-level sect statements. Report: `madras/README.md`.
- North (United Provinces, NWP & Oudh): Daśanāmīs, 1869–1911 (Atkinson, Oudh gazetteer, Nevill, census 1891).
  Report: `north/README.md`.
- Bengal Presidency (Bengal, Bihar, Orissa): Daśanāmīs, 1872–1918 (Hunter; Bengal/Bihar and Orissa District
  Gazetteers). Report: `bengal/README.md`.
- Punjab: Daśanāmīs, 1881–1919 (district gazetteers 1883–84 and revised; Rose's Glossary).
  Report: `punjab/README.md`.
- Central Provinces and Berar: in progress (`cp/`).
