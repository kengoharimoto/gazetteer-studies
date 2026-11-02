# Punjab: Daśanāmīs, 1881–1919

Part of `../`. As in the North (`../north/`) and Bengal (`../bengal/`), Śaṅkara's following in the Punjab
appears in the colonial sources as the Daśanāmī orders: Gosains/Gusains, Sanyasis, Dandis. This sub-study
looks for them district by district against the orders that dominate the Punjab: Jogis/Naths, Udasis and
Bairagis.

## Sources

| layer | source | date (census) | volumes |
|---|---|---|---|
| PA | *Gazetteer of the … District 1883–84* | 1883–84 (1881) | 28 districts |
| PB | *Punjab District Gazetteers*, revised, Part A | 1897–1918 (1891/1901) | 21 districts |
| RO | H. A. Rose, *Glossary of the Tribes and Castes of the Punjab and NWFP* | 1911–19 | 3 vols (I religion, II–III castes) |

- Selections: `data/selection_p1883.tsv`, `data/selection_p1904.tsv`, `data/selection_rose.tsv`; OCR in
  `data/ia_ocr/`.
- Cue packets: `scripts/make_packets.py`. Coding rules: `data/CODING_INSTRUCTIONS_PUNJAB.md`, on top of
  `../north/data/CODING_INSTRUCTIONS_NORTH.md`. Output: `results/coded/`, 434 quoted rows.
- Tables: `scripts/aggregate_punjab.py` → `results/gosain_counts.tsv`, `results/dasnami_notes.tsv`. Vaiṣṇava
  "Gosains" are excluded from the Daśanāmī column.
- Quote check: 29 of 30 sampled quotes are verbatim in the OCR. The miss is a scrambled table row.
- Gaps:
  - Sirsa, Ludhiana, Simla and Kohat have no 1883–84 volume on IA.
  - Several revised-series files are Part B statistics volumes (Gurdaspur, Lahore) or cover only part of a
    district (Kangra = Kulu and Lahul-Spiti; Simla = Simla Hill States).
  - Many caste tables are scrambled in the OCR.

## 1. Headcounts: a thin presence, confined to the south-east

| district (census) | Gosain / Sanyasi | Jogi | Bairagi | Udasi |
|---|---|---|---|---|
| Hisar (1881) | Gusain 1,479 | 1,919 | 1,867 | – |
| Delhi (1881) | Gusain 690 | (lost) | (lost) | – |
| Rohtak (1881) | Gusain 565 | 3,765 | 6,909 | – |
| Hoshiarpur (1881) | Sannyasi 556 | – | 778 | 800 |
| Shahpur (1891) | Sanyasi 146 | 246 | 260 | – |
| Kulu (1891) | Gusain 95 | – | 657 | – |
| Karnal, Ambala, Gurdaspur, Sialkot (1881) | – | 9,267; 11,897; 2,216; 3,282 | 4,620; –; 1,055; 1,065 | |
| Ludhiana (1901) | Sanyasis "very few" | | 914 | 1,949 (2,366 in 1881) |
| western districts (Multan, Jhang, Montgomery, Muzaffargarh, Dera Ghazi Khan, Dera Ismail Khan, Bannu, Peshawar, Hazara) | **none** | 500–700 where printed | | |

What the numbers show:

- **Daśanāmīs appear only in the south-east and in Hoshiarpur**, the districts adjoining the United Provinces.
  Even there they are a few hundred to 1,500 persons.
- **Jogis outnumber them** almost everywhere. Some of these Jogi counts are the menial or musician Jogi caste,
  not Kanphaṭa monks.
- **Bairagis and Udasis** hold the field in the central and eastern districts.
- **In the west there are no Daśanāmīs at all.** The "Gosains/Gusains" there are **Vaiṣṇava gurus of the Kirār
  traders**: the Lalji and Shamji lines sent from Brindaban c. 1600 (Muzaffargarh, Dera Ismail Khan, Leiah).

## 2. Institutions and descriptions

Daśanāmī notes per district are in `results/dasnami_notes.tsv`. The most are in Kangra, Karnal and Hisar,
besides Rose.

1. **Kangra: the one strong case.**
   - 1883–84: Gosains are "Dasnami or Saniasi" in ten tribes. Giri is prevalent, and the founder is "Shankar
     Acharaj". They are "the principal inhabitants" of Jwalamukhi.
   - They are the hills' greatest capitalists and wholesale traders, in opium (bought in Kulu), charas,
     shawl-wool and cloth as far as Hyderabad, but "much deteriorated by internal dissensions".
   - They are organised in akhāṛās under mahants. Adopted chelas inherit, not sons. Celibacy is seldom
     observed. Their burials are marked by a "math" to Mahadeo.
   - 1897 (Kulu): Gusains from Jwalamukhi still come to Outer Saraj every summer to lend against opium and
     blankets. Some have settled as landholding peasants. "Bairagi or Gusain" has become a caste name.
   - Rose adds a history: Sannyasis who fled to the hills married Brahmans and grew rich controlling the trade
     between hills and plains, lending at 24, 60 and 72 per cent.
2. **Karnal and Hisar (south-east).**
   - Gosain pujaris serve Shiva temples, including a Gir Gosain math said to be 800 years old.
   - The Puri line of Ramthali has an elected mahant and a network of samādhis across Kaithal, Patiala, Nabha
     and Delhi (Rose, vol. I).
   - Gosains and Kanphaṭa Jogis act as priests of Sitala shrines. Gosains and Jogis are buried sitting in salt.
   - Hisar (1904) gives a full account:
     - Gosains are a subdivision of the Sanyasis, with founder "Shambhu Acharj" and ten chelas.
     - They are divided into gharbārī (married), matdhārī (celibate, keeping village maths and Shiva temples)
       and abdhut Gosains.
     - The Puri guru is at Kharak and the Giri guru at Bilak, both in the district.
3. **Jalandhar.** A Sanyasi "mat" at Paddi Matwali, founded by Gambhir Parbat. It held revenue-free grants
   and a levy on surrounding villages until British rule. Its mahant, Kailas Parbat, is guru to the
   **Maharaja of Nepal** (1904).
4. **Rose's *Glossary*.**
   - The ten names and four maṭhas are given, and Daṇḍīs are distinguished from the "Dashanami or Goswami"
     majority.
   - Gosains are "a semi-secularised offshoot of the Sannyasi order", with gharbārī, matdhārī, āsandhārī and
     abdhut divisions.
   - Militant Nāgās arose when Rajputs were admitted.
   - Yet Rose closes his Gosain entry by calling them "correctly classed as a Vaishnava sect". The category was
     unstable even for the compiler.
5. **Comparison orders.**
   - Jogis: Tilla Gorakhnath (Jhelum) is the head of all Jogi places in the Punjab, with Bohar (Rohtak) and
     Koh Kirana (Jhang/Shahpur), all with jagirs and fairs.
   - Udasis: Dera Baba Nanak, Bhuman Shah (Montgomery), the akharas at Amritsar.
   - Bairagis: the Ram Thamman fair near Lahore (about 60,000 people), and eight Bairagi mahants in
     Hoshiarpur.

## 3. Findings in relation to the other regions

1. **The Punjab is the edge of the Daśanāmī world.** The orders thin out westward from the UP:
   - thousands per district in the UP and Bihar;
   - hundreds in the Punjab's south-east;
   - nothing west of Lahore, where the word "Gosain" belongs to Vaiṣṇava Kirār gurus.
   The ascetic field belongs to the Nāth Jogīs, the Sikh Udāsīs and the Bairāgīs.
2. **The same social form as elsewhere: householder trader-lenders.** Where Daśanāmīs are strong, in the Kangra
   hills, they are married Gosains organised by chela succession, controlling credit and long-distance trade.
   These are the counterparts of the UP's Atīts, Bihar's Gharbārī Atīths and the Gosain bankers of Mirzapur.
3. **Links to princely courts.** The Paddi Matwali mahant as guru to the Maharaja of Nepal parallels Bengal's
   Bhot-Bagān and its Tibetan connection, and Lucknow's Himmat Gir under the Nawabs. In the colonial record the
   orders are visible chiefly where they touched courts, credit and land.

## Files

| file | content |
|---|---|
| `results/coded/PA*.tsv`, `PB*.tsv`, `ROSE*.tsv` | coded rows (counts and notes) |
| `results/gosain_counts.tsv` | district × layer × year headcounts |
| `results/dasnami_notes.tsv` | Daśanāmī notes by district and kind |
| `results/packets/` | cue-sentence packets |
