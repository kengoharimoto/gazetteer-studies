# Bengal Presidency: Daśanāmīs in Bengal, Bihar and Orissa, 1872–1918

Part of `../` (with Bombay, Madras and the North). As in the United Provinces (`../north/`), Śaṅkara's
following in the east appears in the colonial sources as Daśanāmī renunciants and householders: Atīths, Gosāins,
Sannyāsīs and Daṇḍīs. This sub-study maps them by district at two dates.

## Sources

| layer | source | date (census) | volumes |
|---|---|---|---|
| HU | W. W. Hunter, *A Statistical Account of Bengal* | 1875–77 (1872) | 19 |
| BG | *Bengal* / *Bihar and Orissa District Gazetteers* (O'Malley and others) | 1905–18 (1901/1911) | 46 districts |

- Selections and download: `data/selection_hunter.tsv`, `data/selection_bdg.tsv`; OCR in `data/ia_ocr/`.
- Cue packets: `scripts/make_packets.py`, adapted from the North script with Bengali spellings (Gossain,
  Goswami, Atith); output in `results/packets/`.
- Coding rules: `data/CODING_INSTRUCTIONS_BENGAL.md`, on top of `../north/data/CODING_INSTRUCTIONS_NORTH.md`.
  Output: `results/coded/<VOL>.counts.tsv` / `.notes.tsv`.
- Tables: `scripts/aggregate_bengal.py` → `results/gosain_counts.tsv`, `results/dasnami_notes.tsv`.
  Vaiṣṇava "Gosains" (Chaitanya gurus) are excluded from the Daśanāmī column.
- Quote check: 29 of 30 sampled quotes are verbatim in the OCR. The 30th is two passages joined by "…".
- Gaps:
  - Dacca: on IA only as a statistics volume.
  - Pabna (1900s): the file is the statistics companion.
  - Singhbhum (1872): the caste figures are illegible.
  - Monghyr (1872): the Atīth figure is unrecoverable.

## 1. Headcounts: Bihar is the Daśanāmī heartland, Bengal proper is Vaiṣṇava

1872 (Hunter), persons; the Atīth/Gosāin column is Daśanāmī only:

| region | district | Atīth/Gosāin | Sannyāsī | Vaiṣṇava (caste-rejecting) |
|---|---|---|---|---|
| **Bihar** | Saran | **18,612** | 179 | 3,777 |
| | Champaran | 6,063 | 803 | 4,190 |
| | Shahabad | 3,454 | 758 | 1,070 |
| | Gaya | 1,141 | 1,842 | 1,395 |
| | Tirhut | 1,080 | **5,002** | 6,726 |
| | Monghyr | n/a | 1,356 | n/a |
| | Purniah | 393 | 1,004 | 2,554 |
| | Patna | 106 | 937 | 2,082 |
| | Bhagalpur | 57 | 564 | 3,066 |
| **Chota Nagpur** | Hazaribagh | 1,706 | 5 | 799 |
| | Lohardaga | 594 | 3,929 (?) | 4,459 |
| | Manbhum | 290 | – | 12,262 |
| **Orissa** | Balasor | – | 1,652 | 18,651 |
| | Puri | – | 576 | 6,770 |
| **Bengal proper** | Midnapur | – | 436 | **96,178** |
| | 24 Parganas | – | – | 36,563 |
| | Bardwan | – | 84 | 37,362 |
| | Rangpur | – | 268 | 24,451 |
| | Murshidabad | – | 190 | 21,464 |
| | Hugli, Rajshahi, Pabna, Noakhali | – | 26; 37; 5; 3 | 20,373; 14,268; 8,726; 2,131 |

Reading the numbers:

- **Change over time.** Saran's Atīths grow from **18,612 (1872) to 26,753 (1901)**. The 1901 census quoted in
  the Saran gazetteer gives **50,042 Atīths** for Bengal and Eastern Bengal together.
- **Bihar against Bengal proper.** Bihar's Daśanāmīs run into the thousands per district. In Bengal proper
  Sannyāsīs are in the tens or low hundreds, while caste-rejecting Vaiṣṇavas (Bairāgī, Boishtom) number in the
  tens of thousands. Bengal proper is a Vaiṣṇava landscape.
- **What the later layer gives.** The 1900s gazetteers mostly print only occupational "religious mendicants"
  totals, so the Hunter layer carries the numbers.

## 2. Institutions and events

Daśanāmī notes per district are in `results/dasnami_notes.tsv`. The most are in Gaya, Bogra, Puri, Saran,
Rangpur, Hooghly and Howrah.

1. **Bodh Gayā (Gaya).**
   - Hunter (1877) has only "a large convent of Sanyāsīs" with an elected celibate mahant.
   - The 1906 gazetteer gives a maṭh "of the Hindu sect of Girs, one of the … Saivite orders established by
     Sankara Acharya", founded in the late 16th century, with the village of Taradih by farman c. 1727.
   - It narrates the Mahābodhi Society dispute (1891–1906): the High Court found the Mahant in possession and
     sole superintendent of the temple. The gazetteer calls the order one "founded by one of the bitterest
     enemies of Buddhism".
2. **A network of Bengal mahants (Howrah, Bhot-Bagān).**
   - The Tashi Lama assigned the Tibetan monastery at Ghusuri to Puran Gir Gosāin (mahant 1785, killed by
     dacoits in 1795). His line ends in Trilokh Chandra Gir, elected in 1905 by "the other Dasnami Mahants of
     Bengal".
   - The Tārakeśvar mahant ("a celibate of the Dasnami order of sannyasis", estates of Rs 16,000 a year) is
     called the most influential of them.
   - This is the only explicit evidence for a corporate body of Daśanāmī mahants in the eastern sources.
3. **Landholding Gosāins.**
   - Bogra: the Giri Gosāins of Sherpur are celibate Brahman zamindars who keep their line by adoption.
   - Monghyr: "The mendicant or Sannyasi classes have acquired wealth and importance", naming the Mahants of
     Dularpur and Suja.
   - Saran: the Gharbārī (householder) Atīths are zamindars, moneylenders and cultivators.
   - Midnapur and Bogra have *sannyāsottar* rent-free tenures, against hundreds of *vaishnavottar* ones.
4. **The Sannyāsī–Fakīr raids, 1760s–1800 (north Bengal).**
   - The 1773 Council on "Sanyasis or Faquirs".
   - Bands of 700–1,500 in Rangpur in the 1780s, with fortified hermitages that combined money-lending with
     raiding.
   - In 1777, 200 Nāgās destroyed Majnu Fakīr's band.
   - Mymensingh: Madhupur jungle forts, Jamalpur "then called Sanyasiganj", and zamindars forced to grant
     rent-free land that the Sannyāsīs' descendants still held.
5. **Purī.**
   - Hunter (1877) says nothing at all about Śaṅkara's maṭha.
   - O'Malley (1908) has "the Sankaracharya" maṭh near Svargadvāra, "said to have been founded by Sankaracharya
     himself", with a library of about 1,200 manuscripts. He gives no endowment and never uses the name
     *Govardhana*.
   - It stands among more than 70 maṭhas dominated by rich Vaiṣṇava foundations (Emār, Rāghavadāsa,
     Uttara-pārśva), which hold zamindārīs and Maratha grants.
6. **Atīths defined.**
   - Hunter: "Dasnāmī Daṇḍīs who have not resigned the world".
   - Census 1901 (quoted in the Saran gazetteer): "followers of Sankaracharya", divided into Sannyāsī and
     Gharbārī Atīths, keeping the names Giri, Purī and so on and burying their dead seated.

## 3. Findings in relation to the other presidencies

1. **The eastern pattern repeats the United Provinces.**
   - Daśanāmīs are concentrated in **Bihar** and adjoining Chota Nagpur, contiguous with the UP's eastern
     districts (Gorakhpur, Basti, Azamgarh, Ballia).
   - Their strength there is in the propertied **householder Atīth**, not in ascetic numbers.
   - In Bengal proper the field belongs to Chaitanya Vaiṣṇavism. "Gosain" there means a Vaiṣṇava guru, and
     Daśanāmīs appear only as a few powerful mahants (Tārakeśvar, Bhot-Bagān) and as 18th-century raiders.
2. **A Śaṅkara seat without a following.** At Purī, one of Śaṅkara's four seats, the colonial gazetteers barely
   register the maṭha: absent in 1877, a library and a legend in 1908. Compare Śṛṅgeri's very visible
   jurisdiction in Kanara and South Canara (Bombay and Madras studies).
3. **The two-date evidence points to growth, not decline:**
   - Saran Atīths rose from 18,612 to 26,753 between 1872 and 1901.
   - At Bodh Gayā the gazetteers move from an anonymous "convent of Sanyāsīs" (1877) to a named Giri maṭh with
     a Mughal grant (1906).
   Some of this growth is better description in the later source rather than more Daśanāmīs.

## Files

| file | content |
|---|---|
| `results/coded/HU*.tsv`, `BG*.tsv` | coded rows (counts and notes) |
| `results/gosain_counts.tsv` | district × layer × year headcounts (Daśanāmī Gosāin/Atīth, Sannyāsī, Vaiṣṇava, Jogī) |
| `results/dasnami_notes.tsv` | Daśanāmī notes by district and kind |
| `results/packets/` | cue-sentence packets |
