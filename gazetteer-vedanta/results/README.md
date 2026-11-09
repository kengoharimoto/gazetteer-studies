# Śaṅkara's following in the Bombay Gazetteer: results

Pilot over the *Gazetteer of the Bombay Presidency* (ed. J. M. Campbell), district volumes
II–XXIV (1877–86) and vol. IX pt 1 *Gujarat Population: Hindus* (1901). Method and sources:
`../README.md`. Coding rules: `../data/CODING_INSTRUCTIONS.md`.

## 1. What the Gazetteer can and cannot tell us

**Two kinds of evidence, and neither isolates the Smārtas directly.**

- **The 1872 census sect tables** (`../data/sect_census_1872.tsv`) cover 11 districts, every volume built on
  1872 figures. Their classes are Vaiṣṇava (Rāmānuja, Vallabha, Kabīrpanthī, Mādhva, Svāminārāyaṇa, and
  locally Bījmārgī and Parṇāmī), Śaiva, Ascetic, "Unsectarian" ("mixed" in Gujarat) and Śrāvaka.
  - **There is no Smārta class.** Where the Smārtas went depends on the district.
    - Ratnagiri returned 99.7% of its Hindus as Śaiva and 0.05% as unsectarian.
    - Thana: 28.9% Śaiva, 69.7% unsectarian.
    - Nasik: 10.5% and 88.0%. Khandesh: 3.4% and 93.8%.
  - These are neighbouring Marathi districts with similar populations, so the split records each district's
    enumeration practice, not religion.
  - In Gujarat, vol. IX says the Dvārkā Śaṅkarācārya is the referee in religious questions "for followers of
    Shaivism in Gujarat", and its index heads the entry "Shaivs or Smarts" (p. 542). Gujarat's 1872 "Śaiva"
    figure (690,124) is therefore roughly the Smārta constituency there.
  - The 1881-based volumes (1884–86) print no sect tables at all.
- **Caste accounts** (575 coded rows in `coded/`, one file per volume). Each caste account states the caste's
  religion. Many name a guru and his seat:
  - "Their spiritual teacher is Shankarāchārya the pontiff of the Smart Brāhmans" (Marāṭhās, Dharwar, p. 138).
  - "Their high priest is Shankaracharya, the great Smart pontiff who lives at Sankeshvar" (Deshasthas,
    Kolhapur, p. 45).
  - These statements give a caste-by-caste picture. A district share can then be computed against the census
    totals (`../data/district_hindu_totals.tsv`).

## 2. How large was the following, district by district

Share of the district's Hindu population belonging to castes the Gazetteer says follow a Śaṅkarācārya or
Smārta teacher. Two figures are given: castes **asserted** Smārta, and asserted **plus** castes the text
splits between Smārtas and Bhāgavatas (Mādhva/Vaiṣṇava) without proportions. Full table:
`smarta_range.tsv`. Map: `smarta_map.png`.

| District (census) | asserted | + split castes | main castes / seat named |
|---|---|---|---|
| **Kanara (1881)** | **32.4%** | **38.6%** | Havigs 39,710; Konkan Kuṇbīs 14,812; Arers 17,461; Komārpaiks 8,743; ~70 castes; Śṛṅgeri, the Havig maṭhas of Rāmacandrapura and Sonda |
| Dharwar (1881) | 7.6% | 7.8% | Marāṭhās 44,085; Komṭis 8,238; Khatrīs 4,060; Śaṅkarācārya, Saṅkeśvar |
| Belgaum (1881) | 0.8% | 7.7% | Bāndekars, Nārvekars, Rajputs, some Kuṇbīs; Saṅkeśvar |
| Ahmadnagar (1881) | 1.3% | 5.3% | Deshasthas 27,249 split; Karhāḍās; Saṅkeśvar |
| Sholapur (1881) | 0.5% | 5.2% | Komṭis 2,295; Deshasthas and Konkaṇasthas split; Śṛṅgeri, Saṅkeśvar |
| Poona (1881) | 1.1% | 5.1% | Telīs 8,710; Deshasthas 32,749 split; Brahmans under Śṛṅgeri |
| Kolhapur (1881) | 3.7% | 3.7% | Deshasthas 18,116; Chitpāvans; Karhāḍās; Saṅkeśvar |
| Bijapur (1881) | 3.0% | 3.0% | Marāṭhās 15,877; Smārta Deshasthas; guide at Sonda |
| Thana (1872) | 1.4% | 2.8% | Chitpāvans 8,722; small Brahman castes |
| Kolaba (1881) | 2.3% | 2.3% | Chitpāvans 8,337 |
| Ratnagiri (1872) | 0 | 1.5% | Shenvis; Chitpāvans (no figure) |
| Satara (1881) | 0.1% | 0.1% | Pardeshis only; the volume names no Śaṅkarācārya at all |
| Nasik (1872) | 0 | 0 | Dravids only (no figure); Panchavati maṭha |
| Gujarat (1891, all) | ≈0 | ≈0 | Jeṭhvā Rajputs only; Dvārkā (but see §1: the "Śaiva" 7% of 1872) |

**Caveats on these figures.**

- **Gosāvīs.** The 1881 census counts **33,851 Gosávis ("Devotees, &c.")** in the Presidency: Deccan 19,247,
  Gujarat 6,036, Konkan 5,269, Bombay City 1,947, Karnatak 1,352 (read from the page image;
  `../census-images/results/bombay1881_gosavi.tsv`). They are the Daśanāmī caste and order. They are not
  counted in the Smārta shares above.

- **Not counted.** Castes said to be Smārta but given no population figure are left out of the totals. The
  biggest such gaps are the Chitpāvans of Poona and Ratnagiri. The split castes are counted whole in the second
  column, so that column overstates them.
- **Kuṇbīs.** The Kuṇbīs of Poona (about 400,000) and Ahmadnagar (about 304,000) are excluded. The Gazetteer
  says they "cannot tell whether they are Smarts or Bhāgvats". Counting them raises Poona to 52% and
  Ahmadnagar to 48%. That is the main finding for the Deccan, discussed in §3.
- **Āgrīs.** The Āgrīs of Kolaba (44,191) are likewise "nominally Smarts and Bhagvats", and are excluded.

### Rival sects in the 1872 census

The 1872 sect tables (`../data/sect_census_1872.tsv`, 11 districts) have no Smārta class, but they show the rivals,
as a share of Hindus:

| region (districts in the table) | Vaiṣṇava | Śaiva | note |
|---|---|---|---|
| Gujarat | 36.8% | 3.2% | Vallabha and Svāminārāyaṇa; the rest "mixed" |
| Deccan (Khandesh, Nasik) | 1.6% | 6.4% | mostly returned as "mixed" |
| Konkan (Thana, Ratnagiri) | 0.6% | 67.9% | Ratnagiri's 99.7% "Śaiva" |

Gujarat is the Vaiṣṇava presidency division. In the Konkan "Śaiva" absorbs the Smārtas. For the Gosāvī count
(33,851 in 1881) there is no rival table: the Bombay census returns them under "Devotees".

### Rival seats in the Bombay Presidency

From the coded rivals layer (`../rivals/README.md`; rows in `../rivals/results/coded/S.tsv`):

| region | rival seat (tradition) | what the texts give it | Śaṅkara comparison in the same region |
|---|---|---|---|
| Gujarat | Vadtal and Ahmedabad (Svāminārāyaṇa gādīs) | 287,687 followers (1901); lay followers owe a twentieth to a tenth of yearly income; Vadtal: a Rs 75,000 temple (1824), 500–1000 inmates, eleven branches, two festivals of about 20,000 pilgrims | the Dvārkā Śāradā pīṭha: endowed by the Gaekwar, "referee" for Gujarat's Śaivas, no stated following |
| Gujarat | the Vallabha Mahārājs' temples | about 647,256 followers, "the largest and most influential Vaishnav sect"; temples worth Rs 1,00,000 (Surat) and Rs 80,000 (Ahmedabad); "upwards of a score" of Mahārājs in Kathiawar | as above. In Ahmedabad city, Svāminārāyaṇa sādhus (315) outnumber Gosāīs and Vairāgīs (261); in Cutch and Baroda the Gosāīs are the largest ascetic body |
| Kanara | Sonda: the Terbidi/Vādirāja maṭh (Mādhva, a branch of Uḍupi) | land grants of 1593 and 1706; "the Vaishnavs hold him in as much reverence as the Smarts hold Shankaracharya" | the Svarṇavallī Smārta maṭh beside it; Śṛṅgeri over most Kanara castes |
| Kanara | Ulvi (Liṅgāyat) | 10,000–12,000 pilgrims | Śṛṅgeri won 14,812 Konkan Kuṇbīs from the Chitradurga guru (1881) |
| Dharwar | the Uttarādi house (Savanur) and the Rāghavendra house (Mādhva) | over two-thirds and about a third of the Vaiṣṇav Brahmans; the lines are "on unfriendly terms" | Kudli's Dharwar ināms (11 taluks, 1934) |
| Dharwar | Hubli Mūrusāvira (Liṅgāyat), largest of Hubli's 15 maṭhs | Liṅgāyats at least 300,000 (38.5% of Hindus) | the Kudalgi Svāmī lost his palanquin suit against it up to the Privy Council (c. 1830) |
| Kolhapur | Kaneri (Liṅgāyat) | Rs 1,500 a year (1886), 5,000–6,000 disciples; the largest stated Liṅgāyat income | Saṅkeśvar: 30 inām villages, Rs 30,000 |

- **Gujarat:** the Vaiṣṇava seats dominate in followers and in temple wealth.
- **The Karnatak:** the Liṅgāyat maṭhs are the denser network, but Saṅkeśvar and Kudli are the richer seats. It
  is the one region of the study where the Śaṅkara houses out-endow their rivals.

## 3. Findings

**Place in the study's verdict (`../SYNTHESIS.md`, "The answer"): Śaṅkara's tradition was regional, not dominant.**
- **Outnumbered the others:** the Bombay Presidency holds two of the regions where it outnumbered the other traditions.
  - The Kanara coast: 32–39% of Hindus in castes said to be Smārta, under Śṛṅgeri.
  - The Karnatak: Saṅkeśvar and Kudli, the richest Śaṅkara seats in the study.
- **A Brahman matter:** in the Marathi Deccan the following is mostly Brahman, and the Kuṇbīs "cannot tell whether
  they are Smarts or Bhāgvats".
- **Minority:** in Gujarat the Vallabhas and Svāminārāyaṇs hold the followings. Dvārkā has none stated.

1. **Kanara is the exception, and it reflects jurisdiction more than doctrine.**
   - In the Kanara volume (1883) nearly every caste is placed under the Śṛṅgeri Jagadguru, from Havig
     Brahmans to fishermen, potters and Kumbhārs.
   - The Smārta tie for non-Brahmin castes is described as jurisdiction: the "head of the Smart monastery at
     Shringeri … whose decision is accepted as final" in caste disputes (Komārpaiks, p. 293).
   - He also collects "tithes from them through his deputies" (Arers).
2. **The map was changing in the 1880s.** The Konkan Kuṇbīs were "till last year (1881) … followers of the
   Liṅgāyat guide of Chitaldurg… But the pārupatyagār or manager of the Smārt Jagadguru of Shringeri has
   persuaded them to acknowledge him as their Teacher and to pay a nominal contribution" (Kanara, p. 218). This
   is direct evidence of Śṛṅgeri actively recruiting non-Brahmin castes, and it is the strongest datum for the
   "did it change" question.
3. **In the Karnatak and southern Deccan the Śaṅkarācārya reaches beyond Brahmins, almost always as an
   arbiter.**
   - Castes outside the Brahmans are named as his followers: Marāṭhās (Dharwar 44,085; Bijapur 15,877),
     Komṭis, Khatrīs/Paṭvegārs, Rajputs and Telīs.
   - The usual formula is that he is "the pontiff of all Smart Hindus" and receives presents or decides caste
     disputes. He is not presented as a doctrinal teacher. Bijapur says the Marāṭhās "are not very zealous
     members of the sect".
4. **In the Marathi Deccan and Konkan the Smārtas are mostly a Brahman matter.** The cultivating majority sits
   outside the categories: Kuṇbīs and Mālīs "cannot tell" whether they are Smārtas or Bhāgavatas. Seen from
   the Gazetteer, the Śaṅkarācārya's following there is a Brahman institution, plus scattered trading and
   artisan castes.
5. **There is a geography of seats.** `pitha_mentions.tsv` lists the seats named for castes in each district.
   - **Saṅkeśvar** for Kolhapur, Belgaum, Dharwar, Ahmadnagar and Sholapur. Belgaum gives a local foundation
     account: Shankarbhāratī left Śṛṅgeri about 1570.
   - **Śṛṅgeri** for Kanara and for the Brahmans of Poona: "the head of the Shringeri monastery … is the
     pontiff of all members of the Smart sect" (Poona, p. 234).
   - **Sonda** for Bijapur Smārtas and Kanara.
   - **Kavale/Sonavda** for Sārasvats in Ratnagiri, Belgaum and Dharwar.
   - **Dvārkā** for Gujarat.
   - **Kūḍali** only once (Dharwar Jingars, low confidence).
   - **No Karvīr** Śaṅkarācārya is named even in the Kolhapur volume, which places the Kolhapur Deshasthas under
     Saṅkeśvar.
6. **Gujarat is a different religious world.** The Vāṇiyā castes are Vallabha, or Vallabha and Jain. The
   cultivating and artisan castes are spread across Svāminārāyaṇa, Rāmānandī, Kabīrpanthī, Bījmārgī and
   Śaiva. The Brahmans are simply "followers of Shiva", with the Dvārkā Śaṅkarācārya as referee.

## 4. Compiler effects: read the map with care

How often a volume mentions the Smārtas varies more by compiler and date than by district. The early volumes
(Kolaba 1883, Khandesh 1880, Nasik 1883) almost never use "Smārta" or "Śaṅkarācārya"; their caste accounts say
"Shaivs or Vaishnavs in religion". The Karnatak volumes of 1883–84 (Kanara, Dharwar) use them constantly.
Satara (1885) never names a Śaṅkarācārya. So part of the north–south gradient on the map reflects the sources.
Kanara's very high figure is partly a property of its compiler, who asked every caste about its spiritual
teacher. The Konkan Kuṇbī passage shows the answers were not formulaic.

## 5. Change over time

- **1872 vs 1881 within a district.** This is not possible from the Gazetteer: the 1881-based volumes print no sect
  tables, and the 1872 tables have no Smārta class.
- **Gazetteer (1880s) vs the revised state gazetteers (1950s–80s).** Done in `../revised/README.md`: Kolhapur,
  Poona, Ahmadnagar, Nasik, Ratnagiri, Dharwar, Bijapur and South Kanara. There is no revised North Kanara or
  Belgaum on IA.
  - The jurisdiction over non-Brahmin castes has gone by the 1950s–70s.
  - The Karvīr Pīṭha has split from Saṅkeśvar (c. 1909).
- **The Bombay census reports, checked Nov 2026** (OCR in `../census-images/data/ia_ocr/`, not in git):
  - **1891** (`wbsl.4318`): no sect table. It only remarks that Brahmans everywhere divide into Vaiṣṇavas and
    "the Smarta or followers of Siva".
  - **1901** (`in.ernet.dli.2015.55938`, p. 61): a sect table exists (Subsidiary Table V), with a class "Shaiv or
    Smart" including "Pashupat, Sankarachari, &c.":
    - Shaiv or Smart: "nearly 3,000,000";
    - Vaiṣṇava sects: "hardly exceed half a million";
    - Liṅgāyat: "over 800,000".

    Enumerators were told not to press "low-caste and ignorant people", so a "very large proportion" is
    unspecified.
  - **1911** (`india.history.resource.92542`): no sect table, but it describes the Saṅkeśvar Śaṅkarācārya's
    agents (dharmādhikārīs) "in every town" of the Deccan, with appeals to him "final". It adds that "the
    authority of the Shankaracharya is declining", and that at Wai, Mahuli, Pandharpur and Kolhapur "he is little
    more than a name".
  - **1881:** the IA scan (`wbsl.8730`) returned a server error.

## 6. Reliability

- **Quotes.** All 575 coded rows carry a verbatim OCR quote and a page. In a random spot-check, 30 of 30 quotes
  were found verbatim in the OCR. Three Kanara attributions were also read in context, and all three were
  correct.
- **Caste labels.** The extractor's caste labels were often wrong (marginal notes in the OCR). The coders
  re-attributed each statement from the text and recorded the correction in `note`.
- **Low confidence.** 23 rows are marked `low`. Pages for Kanara and Satara are interpolated, accurate to about
  ±2 pages.
- **Overlap.** Vol. V (Cutch) was assigned to two coders by mistake; the surviving file is complete.
- **Not coded.** The many one-line Liṅgāyat castes of Bijapur; the ascetic accounts in vol. IX; the sub-caste
  accounts of Gujarat Brahmans (no sect sentences found).
- **For you to review.** The rows marked `medium`/`low` in `smarta_castes.tsv`, especially Gosavis in Kanara
  (coded Smārta because "Shankaracharya founded the order"), Jingars in Dharwar (Kūḍali), and Paṭvegārs in
  Bijapur.

## Files

| file | content |
|---|---|
| `coded/<VOL>.coded.tsv` | caste-level coding, one file per volume |
| `smarta_range.tsv` | district shares, three tiers |
| `smarta_castes.tsv` | all Smārta and Smārta-split rows, with quotes |
| `district_affiliation.tsv` | all affiliations by district |
| `pitha_mentions.tsv` | seats named, by volume |
| `smarta_map.png` | schematic map |
| `extract/` | raw extractor output (statements, caste index); superseded by `coded/` |
