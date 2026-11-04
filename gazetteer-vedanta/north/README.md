# The North: Daśanāmīs in the United Provinces (NWP & Oudh), c. 1870–1910

Part of `../` (the Bombay and Madras studies). In the north, Śaṅkara's following appears in the colonial
sources mainly as the Daśanāmī renunciant orders, not as Smārta householders. These are the Gosāins (Goshain,
Gusain), Atīts (Atith), Sannyāsīs and Daṇḍīs. This sub-study maps them district by district in the United
Provinces, against Bairāgīs, Jogīs and Udāsīs, at two dates.

## Sources

| layer | source | date | volumes |
|---|---|---|---|
| AT | Atkinson, *Statistical, Descriptive and Historical Account of the NWP* | 1874–86 (census 1872/1881) | 14 (+2 district offprints) |
| OU | *Gazetteer of the Province of Oudh* | 1877–78 (census 1869) | 3 |
| UP | Nevill et al., *District Gazetteers of the United Provinces* | 1903–11 (census 1901) | 48 districts |
| census | Census of India 1891, NWP & Oudh, Report ch. VII | 1891 | see `data/census/NOTES.md` |

- Selections: `data/selection_up.tsv` and `data/selection_atkinson.tsv`; OCR in `data/ia_ocr/`.
- Cue-sentence packets: `scripts/make_packets.py` → `results/packets/`.
- Coding: by volume, following `data/CODING_INSTRUCTIONS_NORTH.md`, into `results/coded/<VOL>.counts.tsv`
  (headcounts, 389 rows) and `<VOL>.notes.tsv` (institutions and events, 381 rows about Daśanāmīs).
- Aggregation: `scripts/aggregate_north.py` → `results/gosain_counts.tsv`, `results/dasnami_notes.tsv`.
- Quote check: 36 of 40 sampled quotes are found verbatim in the coded volume's OCR. The other four are in
  the backup scan actually used, or differ only by small OCR corrections the coder made.
- Not available:
  - The Atkinson offprint for Etawah: the download failed.
  - The 1891 and 1901 census caste *tables*: the OCR is unreadable, with only the index legible.

## 1. How many: the headcounts

**Province total, 1891:** Goshain Dasnami **103,320**; Goshain unspecified 38,477 in NWP & Oudh, about 0.2% of the
population. The Oudh gazetteer (1869) has "upwards of 40,000" Goshains in Oudh alone.

**District table, 1891 (read from page images, `../census-images/results/up1891_goshain.tsv` and
`up1891_ascetics.tsv`).** Daśanāmī Goshains by district (persons):
- Gonda 11,478; Gorakhpur 7,010; Fyzabad 5,371; Meerut 5,083; Sitapur 4,414; Mirzapur 4,258; Bareilly 4,023;
  Ballia 3,804; Jaunpur 3,638.
- Fyzabad division 27,844 in all.
- Muttra's 17,131 Goshains are all "unspecified" (Vaiṣṇava).
- Azamgarh returns no Goshains but 5,764 Jogis. Its 1881 Atits were apparently returned as Jogis.

**By district** (`results/gosain_counts.tsv`; Gosāin includes Atīt/Atīth, which these sources call householder
Daśanāmīs, "a subdivision of the Gosains"):

| District (census) | Gosāin + Atīt | Bairāgī | Jogī |
|---|---|---|---|
| Kumaon (1872 / 1881) | 8,860 / 2,940 | 233 | 1,726 |
| Basti (1872) | 8,214 | 2,250 | |
| Bareilly (1872) | 6,169 | 1,472 | 667 |
| Azamgarh (1881) | 5,642 | 341 | |
| Meerut (1872) | 5,326 | 3,913 | 11,292 |
| Gorakhpur (1872 / Nevill) | 5,284 / 13,944 | 3,132 | |
| Bulandshahr (1872) | 4,408 | 2,215 | 6,777 |
| Mirzapur (1881) | 4,348 | 217 | |
| Jaunpur (1881) | 4,201 | 133 | |
| Kheri, Sitapur (1869) | 4,049; 4,040 | | |
| Etah (1872) | 3,961 | 93 | 11,048 |
| Moradabad (1881) | 3,849 | 1,222 | 2,402 |
| Shahjahanpur, Rampur (1881) | 2,620; 2,582 | 1,554; – | 895; 513 |
| Ballia (1881) | 2,532 | 562 | |
| Allahabad (1881) | 1,931 | | |
| Fyzabad (1901) | 1,847 | | |
| Saharanpur (1872 / 1901) | 1,611 / 1,733 | 1,171 / 1,513 | 8,751 / 9,377 |
| Cawnpore, Muzaffarnagar, Garhwal | 1,810; 1,193; 1,125 | ; 620; | ; 9,059; 1,063 |
| Fatehpur, Jhansi, Muttra, Lalitpur | 940; 526; 262 (Vaiṣṇava "Gosains" there); 192 | | |
| Benares (1881, district) | 17 (Benares city: 1,391 Gosains) | 650 | 159 |

Reading the numbers:

- **Where they were.** The Gosāins are thickest in the **Himalaya (Kumaon), the eastern districts
  (Gorakhpur, Basti, Azamgarh, Mirzapur, Jaunpur, Ballia) and Rohilkhand (Bareilly, Moradabad)**, with a
  second cluster in the upper Doab (Meerut, Bulandshahr, Etah). Even there they are only 0.3–0.9% of the
  population.
- **Jogīs often outnumber them.** In the Doab, Jogīs exceed Gosāins (Meerut, Muzaffarnagar, Etah).
- **Bairāgīs are counted inconsistently.** Bairāgī *ascetics* are fewer than Gosāins in most districts. The
  very large "Rāmānandī" figures in some volumes (Muttra 49,509; Agra over 71,000) are lay sect returns, not
  ascetics.
- **Change over time is hard to read.** Only a few districts have counts at two dates:
  - Kumaon falls from 8,860 to 2,940 between 1872 and 1881, probably a reclassification.
  - Saharanpur is stable (1,611 → 1,733).
  - Gorakhpur rises from 5,284 to 13,944.
  The 1891 report warns why: "the words Goshain, Bairagi, Jogi, Saniyasi were apparently used by a
  considerable proportion of the enumerators as interchangeable". Nevill (1900s) mostly drops separate counts
  and folds ascetics into "Faqirs".

### Rival orders in the 1891 census

From the 1891 NWP and Oudh caste table (`../census-images/results/up1891_ascetics.tsv`, `up1891_goshain.tsv`), in
persons:

| order | 1891 | where strongest |
|---|---|---|
| Goshain–Dasnami | 103,320 | Gonda 11,478; Gorakhpur 7,010; Fyzabad 5,371 |
| Goshain, unspecified | 38,477 | Muttra 17,131 (Vaiṣṇava gosvāmīs) |
| Goshain, named Vaiṣṇava sub-heads | 752 | Gauriya 432, Radhavallabhi 252 |
| Jogī | 78,387 | Saharanpur 13,713; Meerut 11,987; Muzaffarnagar 9,229 |
| Bairāgī | 31,979 | Aligarh 4,157; Meerut 4,138; Bulandshahr 2,708; Fyzabad 2,017 |

- The Jogīs are almost as numerous as the Daśanāmīs, concentrated in the upper Doab.
- The Bairāgīs are about a third of the Daśanāmīs. Their ascetic count understates the Rāmānandī presence that
  the gazetteers describe at Ayodhyā. The 1891 report warns that enumerators used Goshain, Bairagi, Jogi and
  Saniyasi interchangeably.

## 2. What they were: institutions, land, arms and trade

Daśanāmī notes per district are tabulated in `results/dasnami_notes.tsv`. The most are in Garhwal, Gonda,
Allahabad, Benares and Kheri.

1. **Landholding Gosāins.** This is the most frequent kind of note; land rows are the largest group.
   - Moradabad: the Salempur Gosāin math, about 36 villages, under a line of Ban mahants.
   - Gorakhpur: Mahant Ram Ratangir of Harpur, 36 villages.
   - Mirzapur: Mahant Anand Gir, 39 villages; Gosāins hold 44,784 acres in all.
   - Gonda: the Bhāratī mahant of Itara and the Ban mahant of Srinagar; 89 villages under "Mahant Goshain" in
     1869 and 34 in 1905.
   - Kankhal: Bhola Gir.
   - Benares: Gosāins hold 10,304 acres.
   - Elsewhere: Gosāin shares of 1–9% of the land in parganas of Bareilly, Moradabad, Allahabad and Ghazipur.
2. **Military Gosāins of the 18th century.**
   - Rajā Indargir and Anupgir (Himmat Bahadur), with "five thousand naked men" at the siege of Allahabad,
     and Sikandra (Cawnpore) as a jāgīr, 1804–40.
   - Bundelkhand: the Jhansi Gosāins are said to descend from Himmat's followers.
   - Himmat Gir's Nāgā cavalry under Shuja-ud-daula, and Goshainganj (Lucknow).
   - Langir, "Mahant of Garh Goshain", hanged in 1805.
   - Mahantgir, deputy governor of Allahabad, rebelled in 1720.
   - The Gosāin–Bairāgī battle at Hardwar, 1760.
3. **Trade and banking.**
   - Mirzapur's Gosaintola of Gosāin merchants, and "Sanyasi" merchants trading with the Deccan before 1781.
   - Gonda: the Gosāins of Balrampur "monopolised" the hill trade in jewels and drugs.
   - Allahabad and Benares: Gosāin bankers (Partabgir).
4. **Akhāṛās and melās.** The Nirbānī, Nirañjanī, Jūnā and Mahānirbānī akhāṛās of "Naga Goshains" at
   Daraganj (Allahabad) and Kankhal (Hardwar), and in Benares at Shivala and Hanuman ghats. They march at the
   Kumbh beside Bairāgī (Nirvāṇī, Nirmohī, Digambarī) and Udāsī akhāṛās.
5. **Śaṅkara and the doctrine.**
   - Garhwal and Kumaon: Śaṅkara founded Jyotirmaṭh (Joshimath), restored Badrinath and died at Kedar. The
     four maṭhas (Śṛṅgeri, Jyotir, Śāradā, Govardhana) are listed with the ten names, and Daśanāmī Gosāins
     serve Rudranath, Kalpeswar and other temples.
   - Gonda: Goshains are "followers of Shankaracharya", in ten classes.
   - Census 1891: 3½ orders are Daṇḍīs, 6½ are "Atits" who "carry on trade and often accumulate property … Some
     of them even marry (Sanjogi)", and "Goshains of the latter six and a half classes are most numerous in
     these provinces."
6. **The word "Gosain" is not only Daśanāmī.** In Muttra/Brindaban, Agra and Pilibhit "Gosains" are mostly
   Vallabha and Chaitanya lineage heads, and these are coded OTHER. Kedarnath and Ukhimath are under *Jangam*
   (Vīraśaiva) "gosains".

## 3. Findings in relation to Bombay and Madras

1. **The same institution, a different social form.**
   - In the south, Śaṅkara's following is a Smārta householder constituency attached to a pīṭha: Śṛṅgeri,
     Saṅkeśvar, Dvārkā.
   - In the north, the colonial sources see it as a body of Daśanāmī ascetics and householder Atīts.
   - These northerners are not tied to a southern seat. They organise as maṭhas and akhāṛās, landholders,
     fighting bands and merchants.
   - The Smārta householder appears in the northern gazetteers only incidentally.
2. **Jurisdiction vs property.** In Kanara, Śṛṅgeri's tie to non-Brahmin castes is jurisdiction and dues. In the
   UP it is Gosāin property: villages, revenue-free grants, jāgīrs, trading houses. Both are worldly bases. The
   Atīt is the northern counterpart of the Smārta householder: initiated, often married, propertied.
3. **The orders form a recognised hierarchy.** In both north and south the colonial compilers knew the ten
   names and the four maṭhas (Garhwal, census 1891). They saw Daṇḍīs as the strict core and Atīts as the
   worldly majority.

## 4. Caveats and next steps

- **Counts are soft.**
  - Enumerators conflated the orders (census 1891).
  - Many Atkinson tables are damaged in OCR (Aligarh, Mainpuri, Basti partly), and census years are sometimes
    inferred.
  - "Gosain" counts in Muttra and Agra are Vaiṣṇava.
- **Two dates per district.** The real two-date comparison is in the notes (land, maths), not the counts:
  Gonda went from 89 villages (1869) to 34 (1905).
- **Possible next steps.**
  - Read the 1891 and 1901 caste tables from page images rather than OCR, for clean district headcounts.
  - The Bengal Presidency (Risley 1891; Bengal District Gazetteers): Atīths and Gosāins in Bihar.
  - The Punjab (Rose's Glossary).

## Files

| file | content |
|---|---|
| `results/coded/<VOL>.counts.tsv`, `.notes.tsv` | coded rows (AT, OU, UP volumes) |
| `results/gosain_counts.tsv` | district × layer × census year headcounts |
| `results/dasnami_notes.tsv` | Daśanāmī notes by district and kind |
| `results/packets/` | cue-sentence packets |
| `data/census/NOTES.md` | 1891 census figures and remarks |
