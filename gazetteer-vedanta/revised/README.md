# The third date: the revised state gazetteers, 1954–1989

Part of `../`. The colonial gazetteers give two dates, c. 1870–85 and c. 1900–18. The revised district
gazetteers published after Independence give a third. Censuses after 1951 no longer count castes, so this
layer is mostly qualitative: for each district, did the institutions and allegiances the colonial volumes
recorded survive, change or vanish?

## Sources and method

- **Volumes:** 37 usable revised gazetteers (`data/selection.tsv`, OCR in `data/ia_ocr/`):
  - Bombay/Maharashtra: Ahmadnagar, Kolhapur, Poona, Ratnagiri, Nasik.
  - Mysore/Karnataka: Bijapur, Dharwar, South Kanara.
  - Madras: Madurai.
  - Uttar Pradesh: 12 districts.
  - Bihar: 7 districts. West Bengal: Hooghly, Howrah. Orissa: Puri.
  - Haryana: Hissar, Karnal.
  - Maharashtra (Berar): Akola, Amravati. Madhya Pradesh: Jabalpur, Raipur.
- **Not available or unusable:** Meerut and Nagpur, plus no revised volume on IA for North Kanara, Belgaum,
  Thanjavur, Tirunelveli, Chingleput, Hoshangabad or Kangra.
- **Catalogue errors found and corrected:**
  - "Kolhapur 1960" (`dli.ministry.08450`) is the Wardha gazetteer; Kolhapur was coded from `dli.ernet.11572`,
    which IA dates to 1886 although the text is the revised edition.
  - Both "Akola" items (`dli.csl.3327`, `dli.ministry.08454`) are the Nasik gazetteer; the real Akola volume is
    `dli.csl.3197`.
- **Checklist:** for each district, `data/EARLIER_ITEMS.md` lists what the earlier layers found.
- **Coding:** by district, following `data/CODING_INSTRUCTIONS_REVISED.md`. Each row in
  `results/coded/RV*.notes.tsv` marks continuity as `same`, `changed`, `new` or `absent`, with a verbatim quote.
  Rows for land reform (`REFORM`) and endowment or temple law (`LAW`) are added.
- **Quote check:** 35 of 37 quotes sampled (30 random plus the key quotations below) were found in the OCR;
  the other two are an absent-row note and a quote split by a line break.

## Findings

### 1. Daśanāmī estates and mahants largely vanish from the texts

The landholding Gosāin mahants that filled the colonial volumes are mostly not mentioned at all.

- **Uttar Pradesh:**
  - Salempur (Moradabad), Anand Gir's 39 villages and the Gosāins' 44,784 acres (Mirzapur), and Ram Ratangir's
    36 villages (Gorakhpur) are absent.
  - So are Bhola Gir of Kankhal, the Pinnath colony (Almora), and the Itara and Srinagar mahants (Gonda).
- **Central Provinces:** Bheraghat's Puri mahants (Jabalpur) and Raipur's Dharampuri estate and Nāgā Gosāins
  are absent.
- **Punjab:** Hissar's Puri and Giri gurus are absent.
- **Bihar:** the Atīths of Saran, Champaran and Shahabad, 18,612 in Saran in 1872 and 26,753 in 1901, are not
  mentioned at all.

Where a cause is named, it is land reform:
- Sitapur: Goshains "before the abolition of zamindari some of them were zamindars".
- Gaya: the zamindari interests of the Bodh Gayā and Budhauli mahants "have now lapsed".
- Madhya Pradesh: the 1950 abolition of proprietary rights is described, though without naming the Raipur or
  Jabalpur estates.
- The Hindu religious-trust laws turn the remaining maṭhs into registered trusts: the Bihar Act 1950 (436
  trusts in Shahabad by 1963), the Bombay Act 1950, the MP Act 1951, the Madras HR&CE Act 1951 and the
  Orissa Act.

### 2. What survives is ceremonial, urban and institutional

- **Akhāṛās at the great melās.**
  - Allahabad: Nirbānī ("Naga Gosains") and Nirañjanī at Daraganj, leading the Magh/Kumbh procession.
  - Varanasi: Nirbānī, Nirañjanī and Jūnā akhāṛās.
  - Hardwar: the Kumbh, with 40 lakh attending in 1974.
  - Nasik: the Simhastha clashes of the Nirbānī and Nirañjanī, now policed.
- **The great maṭhs of Bengal.**
  - Hooghly: the Tārakeśvar maṭh is described more fully than ever, with the court finding that the Dasanāmīs
    are "Vedic Sannyasis" of the "school of Sankaracharya". After the 1924 satyāgraha it became a public
    endowment under a committee, with the mohanta as executive head and succession by disciple abolished.
  - Howrah: Bhot-Bagān is "the seat of the Dasanami sect in the district".
  - The pattern is a clear move from private mahant estate to public endowment.
- **Reprints.** The Gonda "followers of Shankaracharya" paragraph (without its mahants and figures), the Akola
  passage on Gosāin village priests and the Mahant of Māhūr, the Sultanganj convent (Bhagalpur), and the
  Gosāvī sections in Nasik and Ahmadnagar are all copied from the old gazetteers. They show the editors
  reproducing the colonial account rather than new observation.
- **Census of 1951:** it counts only "religious services" (Monghyr 1,780, "on the wane"; Shahabad 2,810;
  Saran 966). Saharanpur lists "Jogi, Goshain and Bairagi" faqirs as an Other Backward Class.

### 3. The Śaṅkara seats become more visible, while their jurisdiction over castes disappears

- **Kolhapur (1959):** "The building is occupied by Sankaracarya of Sankesvar. Although formerly it was a part
  of the Sankesvar Math, the link was broken about 50 years ago and now the Kolhapur math is known as Karvir
  Pitha" (p. 874).
  - The 1886 volume named only Saṅkeśvar. The Karvīr pīṭha is a seat formed in the interval (c. 1909).
  - Nasik's revised volume names a "Shankaracharya of Karaveer" (Dr. Kurtkoti) living at the Panchavati maṭh.
- **Purī (1977):**
  - The Govardhana (Gobardhana) maṭha is now named as one of Śaṅkara's four pīṭhas, "which still exists".
    In 1877 it is absent; in 1908 it is "the Sankaracharya" maṭh, never called Govardhana.
  - Its sannyāsīs sit on the Muktimaṇḍapa, whose verdicts on Jagannātha worship are "final".
  - Its library has grown from about 1,200 manuscripts to more than 2,000.
  - A Kāñcī Kāmakoṭi ashram was founded in Purī in 1973.
- **The jurisdiction over non-Brahmin castes, central to the 1880s picture, is gone:**
  - **South Kanara (1973):** the Kharvis, Servegāras, Marāṭhās and Ares appear only as occupational groups,
    with no Śṛṅgeri guru or fines. Tulu Brahmans are now "largely followers of Madhvacharya, only a small
    number remaining Smarthas".
  - **Dharwar (1959) and Bijapur (1966):** the Marāṭhā, Komṭi and Khatrī followers of the Śaṅkarācārya are
    gone. Smārta is a Brahman sect defined by Advaita, and the maṭh landscape is Mādhva and Vīraśaiva.
  - **Poona (1954) and Ahmadnagar (1976):** Smārtas "follow Śaṅkarācārya", and the Kuṇbīs still "cannot tell
    whether they are Smarts or Bhagvats". This is the 1880s wording, reprinted.
  - **Madurai (1960):** "mostly Smarthas and Vaishnavas", with the Smārta sub-castes taken from Thurston and
    still no seat named.

### 4. The comparison orders

- **Bairāgīs** now dominate Ayodhyā's description outright (Faizabad). The Gosāins appear there only in the
  story of their expulsion from Hanumāngaṛhī.
- **Nāth Jogīs** continue at Gorakhpur under Mahant Digvijay Nath. In Karnal the Shiva-temple priests are now
  "Jogis … of the Kanphara clan", where the 1880s had Gosain pujaris.

### 5. The rival seats at the third date

From the coded rivals layer (`../rivals/README.md`), which read the revised volumes beside the colonial ones:

| place | rival seat at the third date | change from the colonial picture |
|---|---|---|
| Ayodhyā (Faizabad 1960) | Hanumāngaṛhī's Nirbānī akhāṛā: at most 200 resident disciples, but land in five districts, money-lending and bought villages | fewer men (300–400 in 1877) but richer; the Gosāins' expulsion from it is told only here |
| Purī (1977) | about 130 maṭhs, about 30 of them Gauḍīya (2 in 1908); the Rāmānandī houses now listed as "Ramanuj" | the Śaṅkara-line houses are about 7; the maṭhs pass under state endowment control (1951–74) |
| Mathura (1968) | Vallabha, Haridāsī, Gauḍīya and Rāmānandī sub-sects | still no Daśanāmī house; the only Śaṅkara trace is a monthly paper (1961) |
| South Kanara (1973) | the Uḍupi maṭhs; the Mādhva hold extends to Dharmasthala, a Śaiva temple with Mādhva priests | Tulu Brahmans "largely followers of Madhvacharya, only a small number remaining Smarthas" |
| Dharwar (1959), Bijapur (1966) | the maṭh landscape is Mādhva and Vīraśaiva | the Kudalgi palanquin suit against the Hubli Liṅgāyat maṭh is dropped |
| Kolhapur (1959) | Kaneri (Liṅgāyat): Rs 1,300 a year | Saṅkeśvar's Kolhapur maṭh has become the Karvīr Pīṭha |
| Varanasi (1965) | Bairāgī akhāṛās (Bara and Chhota Gudarji), two Gorakhpanthī akhāṛās, Kabīr Chaura, Chaitanya and Vallabha maṭhs, the Kinaram shrine | the Gosāin estates (10,304 acres) disappear from view; the three Nāgā akhāṛās and the Bhinga Daṇḍī Ashram (1924) remain |
| Howrah, Hooghly (1972) | the Ramakrishna movement: 115 centres, about 1,259 hospital beds, about 63,000 pupils; the Brahmos reduced to relics (Howrah 63 in 1961) | Tārakeśvar recognised by a court as "governed by the Sankaracharya school of thought" |

The rival houses survive the third date better than the Daśanāmī estates. Where land reform and endowment law reach
both, as at Purī, the rivals keep the larger share of the maṭhs. The one new growth is the Ramakrishna movement,
which carries Advaita sannyāsa into modern Bengal. Only Purī (1977) files a Ramakrishna house under "Dashnami
Sannyasi".

## Summary

| district | third-date finding |
|---|---|
| Kolhapur | **seat added**: the Karvīr pīṭha, split from Saṅkeśvar c. 1909 |
| Puri | **seat named**: the Govardhana maṭha, on the Muktimaṇḍapa; Kāñcī ashram (1973) |
| Hooghly, Howrah | **continuity, institutionalised**: Tārakeśvar a public endowment (1924); Bhot-Bagān the Daśanāmī seat |
| Allahabad, Varanasi, Saharanpur, Nasik | **ceremonial continuity**: akhāṛās at the melās |
| Gonda, Akola, Bhagalpur, Ahmadnagar, Poona | **reprint**: old text copied, names and figures dropped |
| South Kanara, Dharwar, Bijapur | **jurisdiction gone**: no non-Brahmin castes under a Śaṅkarācārya; Smārta = Brahman sect |
| Sitapur, Gaya | **estates ended by zamindari abolition** (explicit) |
| Mirzapur, Moradabad, Gorakhpur, Almora, Raipur, Jabalpur, Hissar | **estates and mahants vanished** (only traces) |
| Saran, Champaran, Shahabad, Azamgarh, Bareilly | **Atīths / Gosāins vanished as a described caste** |
| Palamau | Athiths still described (Sanyasi and Grihast) |

The caveat applies throughout: absence from a gazetteer is not absence on the ground. The revised volumes were
written by state committees with different interests from the colonial compilers. They were less concerned with
castes and more with temples, trusts and pilgrimage. Part of the "vanishing" is a change of genre.

## Files

| file | content |
|---|---|
| `results/coded/RV*.notes.tsv` | coded rows (continuity, quote, page) |
| `data/EARLIER_ITEMS.md` | the per-district checklist from the earlier layers |
| `data/CODING_INSTRUCTIONS_REVISED.md` | coding rules |
| `data/selection.tsv` | volumes and IA identifiers, with the catalogue corrections |
