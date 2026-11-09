# Śaṅkara's following in the British Indian gazetteers, c. 1866–1918

How widespread was allegiance to Śaṅkara's lineages, region by region, and did the picture change?

The study reads the colonial district gazetteers, the caste glossaries and the census across six regions of
British India. In the colonial record the tradition takes two forms:
- in the south and west, **Smārta householders** under a Śaṅkarācārya's seat (Śṛṅgeri, Saṅkeśvar, Dvārkā …);
- in the north, east and centre, the **Daśanāmī orders** and their householder offshoots (Gosāins, Atīts,
  Sannyāsīs).

**Start here:** `SYNTHESIS.md` (published as a page from `SYNTHESIS.html`).
To look up a place: the **Gazetteer Places Finder** (`map/places_map.html`, also published as a page). It is a
searchable map of every district, maṭha, estate and site in the study, with the spellings the sources use and the
modern names. It includes the 27 taluks outside Mysore that the Kudli Śṛṅgeri maṭh's Agent listed in 1934 as holding
its properties (Dharwar, Bijapur, Belgaum, North Kanara, Bellary, Anantapur and the southern Maratha states), shown
with a cross and filtered by the "Kudli estates" chip (`mathas/archives/README.md`).
Each colonial district entry also carries its census counts of the Daśanāmīs and the comparable orders, from the
transcribed tables in `census-images/results/`:
- UP and the CP, 1891: Daśanāmī or Gosain (CP with Sanyāsī and Daṇḍī) against Bairāgī;
- Punjab, 1891: Gosain and Sanniasi against Bairāgī and Udāsī;
- in all three, the Jogī (Punjab Jogī-Rawal; CP also Nāth) count is given but marked "mostly a caste, not compared";
- Bengal, 1901: Atīth and the mixed "Gosain" column;
- Tamil Madras, 1891: the Smārta, Aiyaṅgār and Mādhva shares of Brahmans.
Places with evidence of a rival tradition have a "Rivals:" note (78 entries), and ten carry facts from the coded
rivals layer ("Rivals (coded):"). Eight rival seats have their own entries: Tilla and Bohar (Nāth), Dera Baba
Nanak (Udāsī), Lormi (Bairāgī), Tiruvāvaḍuturai and Dharmapuram (Tamil Śaiva), Chitradurga (Liṅgāyat) and Vadtal
(Svāminārāyaṇa) (`rivals/README.md`).
The finder opens with the study's verdict: Śaṅkara's tradition was regional, not dominant. Its rival seats (purple
crosses) show where other traditions held the larger followings.

**Public repository:** https://github.com/kengoharimoto/gazetteer-studies, with `../yoga-gazetteers/`. It leaves out
the raw text layers that carry long extracts from the post-independence gazetteers, which may still be in copyright:
`revised/results/packets/`, `mathas/results/hits.tsv`, `mathas/results/hits_dedup.tsv` and
`sringeri/results/hits.tsv`. The coded results, with their short quotations, are included. The scripts rebuild the
left-out files from the Internet Archive OCR (`scripts/fetch_ia_ocr.py`, then `revised/scripts/make_packets.py`,
`mathas/scripts/collect.py` and `sringeri/scripts/collect_hits.py`). Licence: CC BY 4.0
for the reports, notes and coded data, MIT for the scripts (`../LICENSE.md` in the public repository).

## The answer

As in the synthesis (`SYNTHESIS.md`, "The answer"; published page `SYNTHESIS.html`). **Regional, not dominant.** The
tradition was present in some form in every region and carried the highest learned prestige, but it outnumbered the
other traditions in only four areas.

1. **Two social forms in two halves of India.** In the south and west: Smārta householders under a seat (a maṭha
   headed by a Śaṅkarācārya). In the north, east and centre: the Daśanāmī orders, which owned land and were turning
   into a caste.
2. **It led on the Kanara coast, among Tamil Brahmans (48% Smārta), in the eastern Ganges plain and in the Bombay
   Karnatak.** Everywhere else a Vaiṣṇava, Liṅgāyat, Nāth or Sikh-linked tradition had the larger following and,
   usually, the larger estates.
3. **The seats were weaker than the name suggests.** Śṛṅgeri was a small, indebted principality in Mysore that
   depended on the Mysore state, with branches at pilgrimage centres but no land among the castes who called it their
   guru. The landed weight in the west lay with two seats that broke away from Śṛṅgeri: Saṅkeśvar (c. 1570; thirty
   inām villages) and Kudli (1656–57; estates in 30 taluks and states, mainly Dharwar and Bijapur). The other three
   of the four seats barely appear.
4. **After independence the estates disappeared and the seats became more visible.**

## The evidence, and where it is

The synthesis presents five kinds of evidence:

| Evidence | What it shows | Detail |
|---|---|---|
| 1. Who followed | the two forms; allegiance as jurisdiction and property; orders turning into a caste | regional reports; `results/README.md` (Bombay) |
| 2. Where | region by region, strongest to weakest, with who held more | regional reports; `map/` |
| 3. How many | census counts of the Daśanāmīs and the rival orders in the same tables; rival houses' wealth | `census-images/README.md`; `rivals/README.md` (615 coded rows) |
| 4. The seats | what each seat held; Śṛṅgeri and its two offshoots | `sringeri/README.md`; `mathas/README.md`; `mathas/archives/README.md` |
| 5. Change | three dates: 1866–1890, 1900–1918, 1954–1989 | regional reports; `revised/README.md` |

Two cautions carried through the study:
- **Census headings are not followings.** The census "Jogī" is left out of every comparison of orders. It is the
  largest heading in the north, but mostly a householder caste, not the Nāth order: in the Punjab "Jogī & Rawal" was
  about half Muslim (36,718 of 75,469 in British Territory, 1891), and in the UP the gazetteers describe Jogīs more
  often as a caste (`../yoga-gazetteers/`). The Daśanāmīs are compared only with the Bairāgīs and Udāsīs. The headings
  include householders on both sides, and enumerators used "Goshain, Bairagi, Jogi, Saniyasi" interchangeably (NWP
  1891).
- **Rival houses were as rich or richer** where both are described (Tiruvāvaḍuturai Rs 2 lakhs a year against
  Kumbakoṇam's Rs 14,000; the Bairāgī state of Nandgaon, 560 villages, against Dharampuri's 40), except in the Bombay
  Karnatak, where Saṅkeśvar and Kudli out-endow the Liṅgāyat maṭhs.

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
| combined map (all six regions) | Daśanāmī and Smārta persons by district, with the Śaṅkara maṭhs, Śṛṅgeri's branches from the Mysore files and the Kudli maṭh's 1934 estates (30 taluks and states), on one map | the census tables and `results/smarta_range.tsv` | `map/combined_map.png` (`map/plot_combined.py`, points in `map/combined_points.tsv`) |
| places finder | 268 places (colonial districts and states, Śaṅkara seats, branches, Kudli estates, other sites incl. rival centres): source spellings, modern name, district and state, what the study says, where in the repo | all layers | `map/places_map.html`, built from `map/places.tsv` (edit `map/places_data.py`, then run `map/build_geo.py` and `map/build_page.py`) |
| Śṛṅgeri in the Places chapters | where the maṭha, its branches and estates are located | Places chapters of all volumes; Kanara XV-2, Thana XIV, Poona XVIII-3; Rice's *Mysore* (1876, 1897) | `sringeri/README.md` |
| all Śaṅkara maṭhas (Saṅkeśvar, Karvīr, Kudali, Dvārkā, Jyotirmaṭh, Govardhana, Kumbakoṇam, Śivagaṅgā …) | where each seat and branch is located and what is said there | all volumes, coded by region | `mathas/README.md` |
| Mysore archive files (1876–1959) | Śṛṅgeri and Kudli as institutions: lands, debts, branches, successions, honours, State management. Includes the Kudli maṭh's estates outside Mysore (the Agent's list of 1934: Dharwar, Bijapur, Belgaum, North Kanara, Bellary, Anantapur, the southern Maratha states) | 338 Karnataka State Archives files | `mathas/archives/README.md` |
| rivals | the traditions that competed with Śaṅkara's: Bairāgīs, Nāth Jogīs, Udāsīs, Kabīrpanthīs, Mādhva, Śrīvaiṣṇava, Liṅgāyat, Tamil Śaiva, Vallabha, Svāminārāyaṇa and Gauḍīya houses, the reform movements; Benares, Ayodhyā, Mathura and Calcutta | all volumes already read, plus revised Mathura (1968) and Calcutta texts; 615 coded rows | `rivals/README.md` |
| census caste tables (all regions) | headcounts | UP 1891, Bengal 1901, Bombay 1881, Punjab 1891, CP 1891, Madras 1891, read from page images | `census-images/README.md` |

## Method

1. **Sources.** Scans and OCR come from the Internet Archive.
   - About 270 colonial volumes in all: 264 volume IDs in the selection tables (3 of the Śṛṅgeri ones duplicate or
     unused scans), plus Thurston's 7 volumes and the census reports; and 37 usable revised gazetteers (39 selected,
     Meerut and Nagpur unusable). The 20 Madras manuals were surveyed but not coded.
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

All six regions are coded and reported. The census caste tables are read for all six. The revised state gazetteers
(1954–1989) are coded as a third date. The Śaṅkara maṭhs are located across all volumes (`sringeri/`, `mathas/`), and
338 Mysore government files on Śṛṅgeri and Kudli are coded (`mathas/archives/`).

## Open lines

- the Bombay and Madras inām records (the Inam Commission's registers) for the Saṅkeśvar and Kudli estates, the
  Puṣpagiri and Virūpākṣa maṭhs, and Kumbakoṇam. They are not online; see `mathas/README.md`;
- the maṭhs' own records (Śṛṅgeri, Saṅkeśvar, Kudli, Kumbakoṇam, Bodh Gayā).
- the rival seats in districts not yet downloaded (Srirangam, Ahobila, Śrīperumbudūr; the Chhattisgarh Feudatory
  States) and legible Calcutta census tables (1901, 1911); see `rivals/README.md`.
