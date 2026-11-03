# Śṛṅgeri in the Places chapters

Part of `../`. The caste chapters show who claimed the Śṛṅgeri Svāmi as guru (Bombay's Kanara, Madras's South
Canara: see `../results/README.md`, `../madras/README.md`). This layer asks the other question: where do the
gazetteers locate the maṭha itself, its branches, estates and visits, in their "Places" chapters?

## Sources and method

- **Searched:** every downloaded OCR text in the study:
  - Bombay Gazetteer, vols II–XXIV;
  - the Madras manuals and gazetteers;
  - the revised state gazetteers.
- **Added for this layer** (`data/selection.tsv`, OCR in `data/ia_ocr/`, kept out of git):
  - the Places volumes Bombay had lacked: Kanara pt 2 (XV-2), Thana (XIV) and Poona pt 3 (XVIII-3);
  - the South Canara *Manual* vol I (1894);
  - Rice's Mysore gazetteer vol II in its 1876 and 1897 editions. Śṛṅgeri lies in Kadur district, Mysore,
    outside the six regions.
- **Search pattern:** `scripts/collect_hits.py` lists every mention of Śṛṅgeri, Śaṅkarācārya or a Smārta maṭha,
  allowing for the OCR spellings (Shringeri, Sringéri, Sringagiri, Srngeri …), with context
  (`results/hits.tsv`, 354 hits).
- **Reading:** each hit was read. The place-located ones were checked against the full entry in the OCR and
  entered in `results/places.tsv` (18 rows) with quote and page.
- **What does not count as presence:**
  - caste statements of allegiance (already coded in the regional layers);
  - the Vidyāraṇya/Vijayanagar history told in nearly every volume;
  - Dharwar's homonymous village of Shringeri near Hangal (an old weir);
  - "Sringirikhi" and similar words.

## Findings

### 1. Outside Mysore, no gazetteer locates a Śṛṅgeri maṭha

- The colonial Places chapters of Bombay and Madras describe no maṭha, branch, estate or agent of Śṛṅgeri
  anywhere in the two presidencies.
- This includes Kanara and South Canara. There the caste chapters put almost every Hindu caste under "the head
  of the Smart monastery at Shringeri in west Maisur" (some 45 caste entries in Kanara pt 1 alone).
- Kanara's Places volume describes one Smārta maṭha, the **Honalli (Svarṇavallī) maṭha at Sonda**. It
  presents it as the seat of a separate Havig line, not a Śṛṅgeri branch: "the head-quarters of the spiritual
  Teacher or guru of the Havig or Haig Brahmans" (XV-2, 345–46).
- The jurisdiction the caste chapters report was exercised from across the border, by touring and through
  caste headmen who forwarded fines. It had no local buildings for the gazetteers to describe.

### 2. In Mysore the seat is a landed principality, and it has a branch at Kudali

- **Rice 1876 and 1897, s.v. Sringeri:**
  - The Jagadguru is "proprietor of the surrounding tract of country".
  - The maṭha has a jāgīr in Koppa taluq of about 9,144 people in 1897, "administered in imitation of the Mysore
    revenue system".
  - Its grant is dated by inscription to 1346 (Harihara I and his brothers), and it was re-established by the
    Keladi king Venkatappa Nayak in 1621.
  - Its revenue is about Rs. 50,000 a year, plus Rs. 1,000 a month from the Mysore State. That grant appears
    in 1876 and again in 1897.
  - Navarātri feeding of "all classes" is described.
  - Liṅgāyats are "reconciled by being allowed to blow their conch-shells in the processions".
  - The 1897 text largely repeats 1876, adding the jāgīr entry and the Rs. 50,000 revenue figure.
- **Kudali (Shimoga):**
  - "the seat of a matha connected with the one at Sringeri, the original Guru having been appointed by the
    Sringeri Swami about 500 years ago to minister to the Smartas of Mahratta descent".
  - The Maratha army that burnt it in 1791 was "threatened with excommunication, which was averted by timely
    gifts".
  - This is the only Śṛṅgeri branch the sources name. It serves Marathi-speaking Smārtas, the same people
    whom the Bombay Deccan volumes place under Śṛṅgeri or Saṅkeśvar.

### 3. In the Deccan the Śṛṅgeri name survives as an origin story

- **Saṅkeśvar (Belgaum 1884, 601–02).** The fullest account of a Śaṅkara maṭha in the Bombay series. It is
  told as a secession from Śṛṅgeri:
  - Shankarbhāratī left Śṛṅgeri about 1570 and was refused re-entry. He founded a maṭha at Kudalgi, that is
    Kudali, and then maṭhs at Kolhapur and Saṅkeśvar with grants from a Bijapur officer.
  - The maṭha has thirty inām villages across seven jurisdictions and an income of Rs. 30,000.
  - Its devotees are Brahmans, Rajputs, Marāṭhās, Shimpis, Panchals and Gabits.
  - Its claimed jurisdiction runs "from the Malprabha to the Himalayas (?)".
  - Kolhapur (1886) confirms the network on the ground: the Saṅkeśvar Svāmī's maṭh is one of the city's two
    large maṭhs, and Khidrapur is "an alienated village belonging to Sankeshvar Svami".
  - **The two Kudali stories conflict.** Mysore says Śṛṅgeri appointed the Kudali guru; Belgaum says Kudali was
    founded by the seceding Shankarbhāratī. Each tradition claims the same branch.
- **Nasik (1883, 518–19).** The Panchavati Śaṅkarācārya maṭh is tied to a pontiff who "is said to have come from
  Shringeri in Maisur" under the second Peshwa. It was built by Peshwa ministers and supported by a
  Government grant. The 1977 revised volume reprints this text.
- **Other Śaṅkarācārya sites, not tied to Śṛṅgeri:**
  - Nirmal in Thana: a "great temple of Shankaracharya Svami" raised after 1739, with a Government grant.
  - Poona: a Śaṅkarācārya, said to have been bribed in c. 1750, allowed a Jain temple in the city.

### 4. After Independence: devotional traces only

- **South Kanara (1973):**
  - Śṛṅgeri appears as the place where the Jagadguru Narasimha Bhāratī installed an image at Karkal.
  - A Śāradāmbā temple at Harekala is "just like that of Sharadamba at Sringeri".
  - Several places are said to have been visited by Śaṅkara (Kollur, Kadaba, Subrahmanya).
  - As in the colonial volumes, no Śṛṅgeri maṭha is located in the district.
- **Kolhapur (1959):** the Saṅkeśvar maṭh in the city has become the independent Karvīr Pīṭha (see
  `../revised/README.md`).

## What this adds

- Śṛṅgeri's reach in the 1880s, the deepest of any Śaṅkara seat in the colonial record, was a reach without
  buildings. The seat was a landed estate in Mysore that the state subsidised. Its following in Bombay and
  Madras was held together by tours, dues and fines.
- The visible network of maṭhs in the western Deccan, with inām villages, urban maṭhs and Government grants,
  belongs to Saṅkeśvar and its Kolhapur offshoot. The gazetteers describe Saṅkeśvar as a break from Śṛṅgeri.
- For mapping "presence", the caste chapters and the Places chapters give opposite pictures:
  - Kanara: dense allegiance, no maṭh.
  - Kolhapur and Belgaum: dense maṭhs and estates, with a guru the castes name as "Shankaracharya of Sankeshvar".

## Limits

- Places chapters were read through the OCR hits only. A maṭha described without the words Śṛṅgeri, Śaṅkarācārya
  or Smārta (for instance "the Svāmi's maṭh") would be missed.
- The South Canara *Manual* vol II (1895), and with it any Places section, is not on IA.
- The Madras district gazetteers (1904–15) were searched, but several volumes are incomplete on IA (North Arcot;
  Chingleput has only its statistical appendix).
- Pages marked "s.v." could not be read from the OCR and are cited by entry.

## Files

| file | content |
|---|---|
| `results/places.tsv` | 18 place-located entries, with institution, link to Śṛṅgeri, quote and page |
| `results/hits.tsv` | all 354 hits with context (input to the reading) |
| `scripts/collect_hits.py` | the search (run with `python3 -I` from `gazetteer-vedanta/`) |
| `scripts/fetch.py` | sequential OCR download for the added volumes |
| `data/selection.tsv` | the added volumes and IA identifiers |
