# Śaṅkara's following in the British Indian gazetteers, c. 1866–1918

How widespread was allegiance to Śaṅkara's lineages, region by region, and did the picture change?

The study reads the colonial district gazetteers, the caste glossaries and the census across six regions of
British India. In the colonial record the tradition takes two forms:
- in the south and west, **Smārta householders** under a Śaṅkarācārya's seat (Śṛṅgeri, Saṅkeśvar, Dvārkā …);
- in the north, east and centre, the **Daśanāmī orders** and their householder offshoots (Gosāins, Atīts,
  Sannyāsīs).

**Start here:** `SYNTHESIS.md` (published as a page from `SYNTHESIS.html`).

## Regions

| region | object | main sources | folder / report |
|---|---|---|---|
| Bombay Presidency | Smārta allegiance by caste and district | *Gazetteer of the Bombay Presidency* (Campbell, 1877–1904), vols II–XXIV; 1872 census sect tables | top level: `data/`, `scripts/`, `results/README.md` |
| Madras Presidency | Smārta Brahmans; Śaiva/Vaiṣṇava balance | Thurston & Rangachari, *Castes and Tribes of Southern India* (1909); census 1871/1891 (the manuals and gazetteers lack caste-level sect statements) | `madras/README.md` |
| United Provinces (NWP & Oudh) | Daśanāmīs | Atkinson's NWP Gazetteer (1874–86); *Gazetteer of the Province of Oudh* (1877–78); Nevill's District Gazetteers (1903–11); census 1891 | `north/README.md` |
| Bengal, Bihar, Orissa | Daśanāmīs | Hunter, *Statistical Account of Bengal* (1875–77); Bengal / Bihar and Orissa District Gazetteers (1905–18) | `bengal/README.md` |
| Punjab | Daśanāmīs | Punjab District Gazetteers 1883–84 and revised (1897–1918); Rose's *Glossary* (1911–19) | `punjab/README.md` |
| Central Provinces and Berar | Daśanāmīs | Grant's *Gazetteer* (1870); CP District Gazetteers (1905–11); Russell & Hira Lal (1916) | `cp/README.md` |
| revised state gazetteers (third date) | continuity of the earlier institutions and allegiances, 1954–1989 | 37 revised district gazetteers (Maharashtra, Mysore/Karnataka, Madras, UP, Bihar, West Bengal, Orissa, Haryana, MP) | `revised/README.md` |
| combined map (all six regions) | Daśanāmī and Smārta persons by district on one map | the census tables and `results/smarta_range.tsv` | `map/combined_map.png` (`map/plot_combined.py`, points in `map/combined_points.tsv`) |
| Śṛṅgeri in the Places chapters | where the maṭha, its branches and estates are located | Places chapters of all volumes; Kanara XV-2, Thana XIV, Poona XVIII-3; Rice's *Mysore* (1876, 1897) | `sringeri/README.md` |
| census caste tables (all regions) | headcounts | UP 1891, Bengal 1901, Bombay 1881, Punjab 1891, CP 1891, Madras 1891, read from page images | `census-images/README.md` |

## Method

1. **Sources.** Scans and OCR come from the Internet Archive.
   - Each region keeps a selection table (`data/selection*.tsv`) with the primary and backup scan of every
     volume.
   - Downloads are done with `scripts/fetch_ia_ocr.py`.
   - Downloaded OCR and page images are kept out of git (see `../.gitignore`). Re-fetch them from the
     selection tables.
2. **Extraction.** Sentences mentioning sects, orders, gurus or maṭhs are pulled into compact packets
   (Bombay: `scripts/extract_statements.py`; other regions: `*/scripts/make_packets.py`).
3. **Coding.** Each volume is coded by hand-checked agents following written rules.
   - Rules: `data/CODING_INSTRUCTIONS.md` for Bombay; for the other regions, the `CODING_INSTRUCTIONS_*.md` in
     each folder's `data/`, built on `north/data/CODING_INSTRUCTIONS_NORTH.md`.
   - Every coded row carries a verbatim quote and page.
   - Random spot checks found 29–30 of 30 quotes verbatim in the scans in each region.
4. **Aggregation.** District tables are built in each region's `scripts/aggregate*.py`. Vaiṣṇava "Gosains"
   are excluded from the Daśanāmī columns.
5. **Census tables.** These were read from page images and reconciled with the printed totals. Print
   inconsistencies are flagged, not corrected.

## Bombay files (top level)

- `data/selection.tsv`, `data/ia_candidates.tsv`: volumes and IA identifiers.
- `data/sect_census_1872.tsv`: the 1872 "Hindu Sects" tables, transcribed by hand. They have no Smārta class.
- `data/district_hindu_totals.tsv`: denominators.
- `scripts/`:
  - `extract_statements.py`: the religion statements and a caste index from the marginal notes.
  - `extract_sect_census.py`
  - `aggregate.py`
  - `plot_map.py` (needs matplotlib; run without `-I`).
  - `identify_volumes.py`
  - `extract_accounts.py`: an earlier extractor, superseded.
- `results/`:
  - `coded/<VOL>.coded.tsv`
  - `smarta_range.tsv`
  - `smarta_castes.tsv`
  - `district_affiliation.tsv`
  - `pitha_mentions.tsv`
  - `smarta_map.png`
  - `README.md`: the Bombay report.

## Status

All six regions are coded and reported. The census caste tables are read for all six. The revised state gazetteers (1954–1989) are coded as a third date. Open lines:
- maṭha records and inām registers (Śṛṅgeri, Saṅkeśvar, Kumbakoṇam, Bodh Gayā) to test what the gazetteers
  only glimpse.
