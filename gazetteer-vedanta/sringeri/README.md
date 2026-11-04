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
  - **The Mysore government files qualify "branch".** (See `../mathas/archives/README.md`.)
    - The Huzur Adalat (1847–49) held that Kudli was not a *tondu* (subordinate) maṭh of Śṛṅgeri.
    - The Dewan (1895) dates its separation to "the Partition of A. D. 1656-57".
    - Most of its income came from estates outside Mysore. Its Agent's 1934 list names 30 taluks and states:
      Dharwar (11 taluks), Bijapur (6), Belgaum, North Kanara, Bellary, Anantapur and the southern Maratha states.
      In 1933 these brought Rs 16,798 of Rs 35,047, against Rs 5,594 from inside Mysore.
    - Bombay calls the maṭh "Kudalgi" and ranks its svāmī with Saṅkeśvar's.

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

## Rivals around Śṛṅgeri

Śṛṅgeri's following was won and held against neighbouring gurus. These notes come from the volumes and files already
read (see also the synthesis, "Rivals: who else held the ground", and `../mathas/README.md`, "Rival maṭhs and
orders").

- **Liṅgāyats.**
  - Kanara's Konkan Kuṇbīs had been "followers of the Lingayat guide of Chitaldurg" until 1881, when Śṛṅgeri's
    agent "persuaded them to acknowledge him" (Kanara 1883, p. 218).
  - The Śṛṅgeri Svāmī's 1888 visit to Bellary led to a dispute with the Liṅgāyats over guru processions
    (Thurston).
  - At Śṛṅgeri itself, Liṅgāyats are "reconciled by being allowed to blow their conch-shells in the processions"
    (Rice).
- **Mādhvas.**
  - Uḍupi is the guru seat of Kanara's Vaiṣṇava Brahmans. By 1973 South Kanara's Tulu Brahmans are "largely
    followers of Madhvacharya, only a small number remaining Smarthas".
  - The Mysore files record the Uttarādi (1906) and Ahobila (1907) maṭhs complaining about the Svāmī's
    processions.
  - The Parakāla Svāmī and the Śrī Vaiṣṇavas demanded purification after his entry into the Srirangapatna temple
    (1895).
  - The Vyāsarāja maṭh of Sosale claimed equality with Śṛṅgeri in State honours (1931).
- **Other Smārta lines in the same country.**
  - The Havig Brahmans follow their own gurus: Svarṇavallī at Sonda and Rāmacandrapura.
  - The Shenvis follow the Kavaḷe svāmī.
- **The seats that separated from Śṛṅgeri.**
  - Saṅkeśvar and Kudli took the Bombay Karnatak estates.
  - A Saṅkeśvar nominee challenged Śṛṅgeri's accredited agent in Khandesh (1913).
  - Hampi was put forward as a rival seat at the 1912 succession, though its Svāmī later called his maṭh "a branch
    of Sri Sringeri Mutt" (1935–36).

### The rival seats around Śṛṅgeri

From the coded rivals layer (`../rivals/README.md`; rows in `../rivals/results/coded/S.tsv`). These seats are also
on the combined map and in the places finder ("Rival seats" filter).

| rival seat (tradition) | where | what the texts give it | bearing on Śṛṅgeri |
|---|---|---|---|
| Uḍupi: the eight maṭhs (Mādhva) | South Canara | the Kṛṣṇa temple rotates among them every two years; each svāmī spends fourteen years "levying contributions" in Canara and Mysore; the Shivallis (28,660 in 1891) "warmly adopted" Madhva after being Smārtas | Śṛṅgeri keeps only the Tulu Brahmans "as have remained Smarthas", the Marathi-speaking Smārtas and the non-Brahmin castes |
| Sonda: the Vādirāja (Terbidi) maṭh (Mādhva, a branch of Uḍupi) | Kanara | land grants of 1593 and 1706; "the Vaishnavs hold him in as much reverence as the Smarts hold Shankaracharya" | stands beside the Svarṇavallī Smārta maṭh at Sonda |
| Chitradurga: the Murugha maṭh (Liṅgāyat) | Mysore | the supreme Liṅgāyat guru; its hill maṭh deserted owing to "the opposition of other sects" | lost the 14,812 Konkan Kuṇbīs of Kanara to Śṛṅgeri's agent in 1881 |
| Melukote (Śrīvaiṣṇava) | Mysore | the 1614 royal estate; 400 Brahmans on daily allowance; the Parakāla svāmī | in 1891 the Śrīvaiṣṇavas are the largest Brahman sub-division even in Kadur, Śṛṅgeri's own district (5,357 against 2,384 "Smārta") |
| Liṅgāyat maṭhs of Kadur | Mysore | Liṅgāyats outnumber all Brahmans in Kadur more than two to one (37,657 against 17,026, 1891) | conches allowed in Śṛṅgeri's processions; the 1888 Bellary procession dispute |
| Rāmacandrapura; Svarṇavallī (Smārta, separate lines) | Shimoga; Sonda | the Havigs' gurus | Smārtas outside Śṛṅgeri's authority |

So Śṛṅgeri's seat stood in a district where Liṅgāyats were the larger community and Śrīvaiṣṇavas the larger Brahman
sect. Its reach lay among the castes of the coast and the Marathi Smārtas, not among its neighbours.

### Rival totals: South Canara Brahmans in the 1891 census

The census gives no ascetic counts for Śṛṅgeri's country. It does give South Canara's Brahmans by sub-division
(`../census-images/results/madras1891_brahman_subdivisions.tsv`; 95,739 Brahmans in all). The affiliations are
those the study's sources give: Sturrock's *South Canara Manual* (1894), Thurston, and the revised gazetteer
(1973).

| sub-division (as printed) | persons | affiliation in the sources |
|---|---|---|
| Sarasvata | 30,273 | split: Smārta Shenvis under the Kavaḷe svāmī, Vaiṣṇavas under a svāmī in Goa (Ratnagiri 1880) |
| Sivalli (Shivalli) | 28,660 | Mādhva: "the great bulk of the Tulu Brahmins of South Canara adopted the teaching of … Madhvacharya" (Sturrock); Uḍupi |
| Havig | 11,234 | Smārta, own guru (Rāmacandrapura) |
| Kota | 11,017 | Smārta (1973) |
| Konkanasta, Chittapavana | 3,200; 1,491 | Smārta, "adherents of the Sringeri math" (Sturrock) |
| Karati (Karāḍi) | 2,731 | Smārta, "owe allegiance to the Sringeri math" (Sturrock) |
| Kandavara | 1,576 | Smārta (1973) |
| Sakalapura (Saklapuri) | 463 | Smārta, own maṭh |
| Padia | 154 | Smārta, acknowledge "the head of Sringeri math" (Sturrock) |

- **Under Śṛṅgeri directly:** only the Marathi-speaking immigrant Brahmans (Karāḍi, Chitpāvan/Konkaṇastha,
  Padia), about 7,600 or 8% of the district's Brahmans.
- **The Tulu Brahmans:** the largest Tulu group, the Shivallis, are Mādhva.
- **The other Smārtas** (Havig, Kota, Kandavara, Saklapuri, about 24,000) follow their own gurus.
- **Śṛṅgeri's real weight** in South Canara was therefore among the non-Brahmin castes (Kharvis, Marāṭhās,
  Servegāras, Ares, Chaptegāras), as Thurston and Sturrock say. Among Brahmans it was a minority beside the Mādhvas.
- **Caveat:** Konkanasta and Chittapavana may be one group returned under two names. The Sarasvata total mixes
  the two sects.

For the rival ascetic orders in the north (Jogīs, Bairāgīs, Udāsīs), see `../census-images/README.md`, "Rival
orders in the same tables".

## What this adds

- Śṛṅgeri's reach in the 1880s, the deepest of any Śaṅkara seat in the colonial record, was a reach without
  buildings. The seat was a landed estate in Mysore that the state subsidised. Its following in Bombay and
  Madras was held together by tours, dues and fines.
- The visible network of maṭhs in the western Deccan, with inām villages, urban maṭhs and Government grants,
  belongs to Saṅkeśvar and its Kolhapur offshoot. The gazetteers describe Saṅkeśvar as a break from Śṛṅgeri.
- For mapping "presence", the caste chapters and the Places chapters give opposite pictures:
  - Kanara: dense allegiance, no maṭh.
  - Kolhapur and Belgaum: dense maṭhs and estates, with a guru the castes name as "Shankaracharya of Sankeshvar".
- Śṛṅgeri's one named branch, Kudli, turns out to be a landholder in the same Bombay Karnatak country as
  Saṅkeśvar (its 1934 estates, from the Mysore files). The western Deccan's Śaṅkara estates therefore belonged to
  the two seats that separated from Śṛṅgeri, not to Śṛṅgeri itself.

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
