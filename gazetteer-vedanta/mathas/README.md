# The Śaṅkara maṭhas in the gazetteers: Saṅkeśvar and the other seats

Part of `../`. This extends `../sringeri/README.md` from Śṛṅgeri to every Śaṅkara seat and branch the volumes
mention. The question is where the gazetteers locate each maṭha, and what they say about it there: buildings,
estates, revenue, branches, the head's residence and tours. Places chapters come first; other chapters count
when they place a maṭha somewhere.

## Sources and method

- **Search.** `scripts/collect.py` searches every downloaded OCR text in the study, across all six regions,
  the revised gazetteers and the volumes added for the Śṛṅgeri layer.
  - It uses one pattern per seat: Saṅkeśvar, Karvīr, Kudali, Dvārkā, Jyotirmaṭh/Joshimath, Govardhana,
    Kāñcī/Kumbakoṇam, Puṣpagiri, Virūpākṣa, Śivagaṅgā and Śṛṅgeri, plus "Shankaracharya" near
    math/monastery/seat.
  - It found 736 hits. After backup scans of the same volume were dropped (`scripts/dedupe.py`), 471 remained
    (`results/hits_dedup.tsv`).
- **Coding.** The hits were coded by region under `CODING_INSTRUCTIONS.md`. Each hit was read in its full
  OCR entry. Each volume was also searched directly for maṭha, Svāmi and place names the patterns could miss.
  - West and Deccan: `results/coded/W.tsv`.
  - North and east: `results/coded/N.tsv`.
  - South and Mysore: `results/coded/S.tsv`.
- **Merge.** `scripts/merge.py` combines them into `results/mathas.tsv`: 63 rows, each with a verbatim quote and
  page.
  - Five rows from a second scan of Atkinson vol. XI are dropped.
  - The Śṛṅgeri rows are in `../sringeri/results/places.tsv`.
- **Quote check.** All 68 coded quotes, before the merge dropped five, were found verbatim in the OCR
  (`scripts/check_quotes.py`).
- **Not rows.** Caste lines naming a guru with no place or institution were counted in comment lines at the
  end of each coded file. They are not rows.
- **Catalogue error found.** The backup scan for Nagpur 1908 (`dli.ministry.07863`) is the revised Thane
  gazetteer of 1982. The CP layer used the correct primary scan, so its results stand. The selection file is
  annotated.

## The seats one by one

| seat | colonial gazetteers (1870s–1910s) | revised (1950s–80s) |
|---|---|---|
| **Śṛṅgeri** (Mysore) | a landed estate in Mysore; one branch at Kudali; no maṭh in Bombay or Madras (`../sringeri/`). Its Svāmī visited Nagpur c. 1903–04 (Wardha 1906, p. 53) | devotional traces in South Kanara |
| **Saṅkeśvar** (Belgaum) | the fullest maṭh account in the Bombay series, with a network of maṭhs, inām villages and temple works (below) | the Kolhapur branch now independent |
| **Karvīr** (Kolhapur) | not yet a separate seat: the Kolhapur maṭh "belonging to the Sankeshvar Svami" | Karvīr Pīṭha, split from Saṅkeśvar c. 1909 (Kolhapur 1959, p. 874); its Śaṅkarācārya Dr Kurtakoti at a Panchavati maṭh in Nasik (Nasik 1977, pp. 199–201) |
| **Kudali / Kudalgi** (Shimoga, Mysore) | two traditions: a branch appointed by Śṛṅgeri (Rice 1876, p. 380; 1897, pp. 459–60), or founded by the Saṅkeśvar secessionist (Belgaum 1884, pp. 601–02). Its Svāmī rebuilt the Hallur temple and holds the village (Dharwar, p. 722), and won the crosswise-palkhi privilege at Hubli up to the Privy Council (p. 757). The Mysore files (1933–34) show most of its income came from estates outside Mysore: 30 taluks and states in Dharwar, Bijapur, Belgaum, North Kanara, Bellary, Anantapur and the southern Maratha states (`archives/README.md`) | — |
| **Dvārkā** (Gujarat) | only in the Gujarat population volume (1901, p. 542): "Shārada Pīth … endowed by the Gaekwar of Baroda, who sanctions the appointment of every new pontiff"; referee for Gujarat's Śaivas. The Kathiawar volume's Dwarka entry (1884) describes no maṭh | — |
| **Jyotirmaṭh** (Garhwal) | named in lists of the four maṭhs (Atkinson 1884, p. 768; 1886, p. 272). Garhwal 1910 (p. 56): Śaṅkara "established the Joshimath monastery". The Joshimath place entries describe no maṭh: Joshimath is the winter seat of the Badrinath Rawal, a Nambūri whose office tradition ties to Śaṅkara. No Jyotirmaṭh Śaṅkarācārya is named. Atkinson also says the Garhwal Daśanāmīs' "chief math … is at Sringeri" (p. 862) | — |
| **Govardhana** (Purī) | Hunter 1877: none. O'Malley 1908 (p. 288): "the Sankaracharya" maṭh "said to have been founded by Sankaracharya himself", about 1,200 MSS; never called Govardhana | named as the Gobardhana maṭha "still extant"; its certificate once needed by Jagannātha priests (Purī 1977) |
| **Kāñcī / Kumbakoṇam** | Kumbakoṇam: "the math of Sankaracharya", Rs 14,000 a year, appoints the managers of three temples incl. one at Conjeeveram (Tanjore 1906, pp. 72, 218). Kāñcī: only Śaṅkara's founding (Chingleput 1879, p. 26) | the Kāñcī Kāmakoṭi Pīṭha founds an ashram at Purī (1973; Purī 1977, p. 511) |
| **Śivagaṅgā** (Bangalore) | the maṭh in financial trouble; at the guru's wish its endowments are managed by the Muzrai department (Rice 1897, p. 91). The sect is not stated | — |
| **Virūpākṣa / Hampi** | no maṭh described; only a guru whose not being allowed to ride into Hampi is blamed for the festival's decline (Bellary 1872, p. 379), and the Vidyāraṇya tradition (Bellary 1904, pp. 284–85) | — |
| **Puṣpagiri** (Cuddapah) | no maṭh in the Cuddapah Manual (1875) or the Gazetteer (1915); every hit is the hill or a temple | — |

## Saṅkeśvar: the one network the gazetteers describe

- **The seat (Belgaum 1884, pp. 600–02).**
  - A maṭh of about two acres with a sacrifice hall for 1,000 people. The present svāmī is the twelfth.
  - Devotees are Brahmans, Rajputs, Marāṭhās, Shimpis, Panchals and Gabits. The claimed jurisdiction runs "from
    the Malprabha to the Himalayas (?)".
  - Income: about Rs 30,000 a year from thirty inām villages, plus tribute and re-admission fines. The villages
    are spread over seven jurisdictions: 15 in Kolhapur, 5 in Belgaum, 3 in the Nizam's territory, 2 each in the
    Patvardhan estate, Satara and Savantvadi, and 1 in Bijapur. The svāmī tours to levy contributions.
  - Origin as told: Shankarbhāratī left Śṛṅgeri c. 1570 and was refused re-entry. He founded Kudalgi, and then,
    with villages granted by a Bijapur officer, maṭhs at Kolhapur and Saṅkeśvar.
- **On the ground in Kolhapur (1886).**
  - The Saṅkeśvar Svāmī's maṭh is one of the city's two large maṭhs (p. 312).
  - Khidrapur is "an alienated village belonging to Sankeshvar Svami" (p. 302).
  - The spire and domes of the Ambābāī temple were added by a Śaṅkarācārya of Saṅkeśvar, at a reputed cost of
    Rs 1 lakh (pp. 309–10).
- **Afterwards.**
  - Under Shahu (1884–1922) an unnamed "religious pitha" was "practically disestablished and its endowments
    withdrawn" (Kolhapur 1959, p. 94). It probably means this maṭh (low confidence).
  - The Kolhapur maṭh became the Karvīr Pīṭha "about 50 years ago", that is about 1909 (p. 874).
- **Its neighbour and equal: Kudli's estates** (from the Mysore government files, `archives/README.md`).
  - Kudalgi is the first maṭh in Saṅkeśvar's own origin story. The Mysore files show the same maṭh, Kudli, holding
    estates on the same ground.
  - Its Agent's 1934 list names 30 taluks and states outside Mysore:
    - Dharwar: 11 taluks;
    - Bijapur: 6 taluks;
    - Belgaum (Parasgad) and North Kanara (Mundgod);
    - Bellary and Anantapur;
    - the southern Maratha states: Kolhapur (Torgal), Ramdurg, Sangli, Miraj Senior and Junior, Savanur,
      Sirasangi, Jamkhandi.
  - Saṅkeśvar's thirty villages lie mainly in Kolhapur, Belgaum and the Maratha states (1884). Kudli's lie mainly
    in Dharwar and Bijapur (1934). Together they cover the Bombay Karnatak.
  - Bombay levied nazarana on Kudli's Dharwar and Bijapur ināms (Rs 2,745 and Rs 1,167, 1936). In 1896 a Bombay
    officer, forwarded by the Commissioner of the Southern Division, recommended exempting the Svāmī of Kudalgi from
    the Arms Act. His reason was that "his brother Swami of Sankeshwar in the Belgaum District, who is in no way
    superior in position, has been exempted" (copied into a Mysore file of 1903).
  - The two seats also competed. In 1913 a Saṅkeśvar nominee challenged Śṛṅgeri's accredited agent in Khandesh.

## Other Śaṅkarācārya sites with no named seat

- **Nasik, Panchavati (1883, pp. 518–19; reprinted 1977).** The tomb of a Śaṅkarācārya who "is said to have come
  from Shringeri", with a monastery built by Peshwa ministers. It receives Rs 500 from Pimpalner and a
  Government grant of Rs 288.
- **Nirmal, Thana (1882, pp. 292–93, 325; 1982).** The reputed samādhi of a Śaṅkarācārya, with a fair of
  6,000–7,000 pilgrims and a temple with a Government grant of Rs 421. The 1982 volume names him "the eighth
  Shankaracharya Vidyashankar Bharati".
- **Poona (1885, p. 340).** About 1750 a Śaṅkarācārya, "it is said by bribing", allowed a Jain temple in the
  city.
- **Bodh Gayā (1906, p. 48).** A Giri maṭh, "one of the seven Saivite orders established by Sankara Acharya".
  The 1957 Gaya volume drops this.
- **Bengal, 1972.**
  - Tārakeśvar is "governed by the Sankaracharya school of thought" (a court finding, Hooghly).
  - A "Sankar Math" was founded at Ramrajatala, Howrah, in 1919.
- **Smārta houses outside the named seats** (coded as `other`):
  - Bhāskarācārya, the Komaṭis' "deputy of Shankaracharya", with four monasteries (Bodhan, Nander, near Hampi,
    near Penukonda) and a residence at Narayan-Devarkeri (Sholapur 1884, pp. 74–75; Dharwar 1884, p. 131).
  - The Shenvi Smārta svāmī's maṭhs at Khanapur, Karwar, Bombay, Nasik and Benares (Belgaum p. 91,
    Ratnagiri p. 117, Nasik p. 41).
  - The Havigs' Svarṇavallī maṭh at Sonda (Kanara 1883, pp. 345–46).
  - A Smārta guru residing at Avani, Kolar (Rice 1876, p. 106; 1897, p. 117).
  - A madam at Trikkayikkād ascribed to Śaṅkara (Malabar 1908, p. 458).

## Rival maṭhs and orders

The Śaṅkara maṭhs in these sources keep meeting other institutions. These records are where they appear. The
regional picture is in the synthesis, "Evidence 3: how many". None of this is coded systematically.

- **Mādhva maṭhs (the Karnatak, Mysore).**
  - The Mysore files record complaints by the Uttarādi maṭh (Hole Narsipur, 1906) and the Ahobila maṭh (Mysore,
    1907) against the Śṛṅgeri Svāmī's processions.
  - The Śrī Vaiṣṇava protest when he entered the Raṅganātha temple at Srirangapatna, with the Parakāla Svāmī,
    1895.
  - The Vyāsarāja maṭh of Sosale claimed equal treatment with Śṛṅgeri in the State's first-day bhikṣā (1931).
  - Uḍupi is the guru seat of the Vaiṣṇava Brahmans of Kanara. By 1973 the Tulu Brahmans are "largely followers
    of Madhvacharya".
- **Liṅgāyat maṭhs.**
  - Kanara's Konkan Kuṇbīs left "the Lingayat guide of Chitaldurg" for Śṛṅgeri in 1881.
  - The Kudalgi Svāmī's crosswise palanquin at Hubli was contested by the Liṅgāyat Mursavirad Svāmī (Dharwar
    1884, p. 757).
  - Liṅgāyat objections were feared when Kudli got the ambari (1931). Mysore regulated the Murgi maṭh's
    "Jagadguru" title and processions.
  - At Śṛṅgeri itself, Liṅgāyats are "reconciled by being allowed to blow their conch-shells in the processions"
    (Rice).
- **Vaiṣṇava maṭhs in Purī.** Of the town's 70-odd maṭhs most are Vaiṣṇava foundations (Emār, Rāghavadāsa and
  others). "The Sankaracharya" maṭh is one among them (1908).
- **Bairāgī akhāṛās (the north).**
  - The Gosāin–Bairāgī battle at Hardwar (1760).
  - The Gosāins' expulsion from Hanumāngaṛhī in Ayodhyā.
  - Precedence among Daśanāmī, Bairāgī and Udāsī akhāṛās at the Kumbh.
  - In Benares the census returns 141 Bairāgīs against 4,106 Gosāins (1891); in Ayodhyā the gazetteer describes
    Bairāgī dominance.
- **Nāth Jogīs.** The Gorakhnāth maṭh at Gorakhpur. In Karnal the Gosāin temple priests give way to "Jogis … of the
  Kanphara clan".
- **Tamil non-Brahmin Śaiva maṭhs.** The Tanjore gazetteer's list of the district's chief maṭhs (1906, p. 72)
  names the "Sudra maths" of Dharmapuram, Tiruvāvaḍuturai, Tiruppanandāl and Tiruppugalūr first. It names the
  Kumbakoṇam Śaṅkara maṭh last.
- **The rival seats against the Śaṅkara maṭhs** (from the coded rivals layer, `../rivals/README.md`; also on the
  combined map and in the places finder):

  | rival seat | tradition | what the texts give it | nearest Śaṅkara comparison |
  |---|---|---|---|
  | Tiruvāvaḍuturai (Tanjore) | Tamil Śaiva ādhīnam | about 29,000 acres, Rs 2 lakhs a year | Kumbakoṇam Śaṅkara maṭh, Rs 14,000 and three temples |
  | Dharmapuram (Tanjore) | Tamil Śaiva ādhīnam | about 2,500 acres and 27 temples; nearby Tiruppanandāḷ (Rs 80,000 a year) was held independent of it in court | listed before Kumbakoṇam (Tanjore 1906) |
  | Chitradurga (Murugha maṭh) | Liṅgāyat | supreme Liṅgāyat guru; lost the Konkan Kuṇbīs to Śṛṅgeri (1881) | Śṛṅgeri, Kudli |
  | Nandgaon | Bairāgī | a Feudatory State of 560 villages (granted 1723) | Dharampuri, the largest Gosāin estate in the CP, 40 villages |
  | Lormi | Bairāgī | 103–104 villages (1826 grant) | as above |
  | Kawardha (Damakheda line) | Kabīrpanthī | a lay following claimed at 500,000 | no Śaṅkara seat in the CP |
  | Tilla | Nāth | Akbar's sanad for a jagir | no Śaṅkara seat in the Punjab |
  | Bohar | Nāth | land; Rohtak's asthals are half Bairāgī, Gosāins fourth | as above |
  | Dera Baba Nanak | Udāsī | jagir Rs 2,602 | as above |
  | Vadtal | Svāminārāyaṇa | one of two seats; 287,687 followers in 1901 | Dvārkā's Śāradā pīṭha, no stated following |

  In the Bombay Karnatak the comparison runs the other way: Saṅkeśvar (30 inām villages, Rs 30,000) and Kudli (Rs
  35,047 in 1933) are richer than the Liṅgāyat maṭhs around them, whose largest stated income is Kaneri's Rs 1,500.
- **Numbers behind the rivalry (census 1891, persons; `../census-images/README.md`):**

  | province | Daśanāmī / Gosāin | rival orders |
  |---|---|---|
  | NWP and Oudh | 103,320 | Jogī 78,387; Bairāgī 31,979 |
  | Punjab | Gosain 13,344; Sanniasi 9,799 | Jogī-Rawal 91,937; Bairāgī 47,561; Udāsī 15,194 |
  | Central Provinces | Gosain 24,796; Sanyasi 2,449 | Bairāgī 29,298; Jogī 6,094; Nāth 5,008 |

  - The akhāṛā and maṭh rivalries above are between orders of comparable size. "Jogī" is the largest census heading in the
    north, but it is not a body of Nāth ascetics: about half Muslim in the Punjab, and in the NWP described more often
    as a householder caste (`../yoga-gazetteers/`).
  - The Bairāgīs outnumber the Daśanāmīs in the Punjab and the CP.
  - These are census headings with loose categories, householders included. In Tamil Madras the comparable figure is the Brahman shares:
    Smārta 47.6%, Aiyaṅgār 22.7%, Mādhva 2,650 persons.
- **Calcutta.** No Śaṅkara maṭh is located in the city. The Daśanāmī foundations nearby (Bhot-Bagān, Tārakeśvar)
  stand in a landscape of Gauḍīya Vaiṣṇava "circles" and Kālī worship (24 Parganas 1914).

## Findings

**Overall verdict of the study** (synthesis, "The answer"): Śaṅkara's tradition was
**regional, not dominant**. The maṭha evidence is part of why.
- **Where the seats were strong.** Its seats were richly endowed only where it also outnumbered the other traditions:
  Saṅkeśvar and Kudli in the Bombay Karnatak, Śṛṅgeri in Mysore, and the Daśanāmī estates of the Ganges plain.
- **Where the seats were names.** Elsewhere the four-pīṭha scheme survives mostly as a list (Dvārkā, Jyotirmaṭh,
  Purī). Where the gazetteers compare, the rival houses are as rich or richer (see "Rival maṭhs and orders" above).


1. **The gazetteers describe one Śaṅkara maṭh network in detail, and it is Saṅkeśvar's.**
   - Śṛṅgeri had the widest following in the caste chapters, but no buildings outside Mysore.
   - Saṅkeśvar had a seat, urban branches, thirty inām villages across seven jurisdictions, temple patronage
     and a touring svāmī.
   - It is also the seat whose story the gazetteer tells as a secession from Śṛṅgeri. Kudali is claimed by
     both lines.
   - The Mysore files add Kudli's own estates on the same ground. Its Agent's 1934 list names 30 taluks and
     states outside Mysore, chiefly in Dharwar (11 taluks) and Bijapur (6) and the southern Maratha states. In 1933
     they brought Rs 16,798 of an income of Rs 35,047, against Rs 5,594 from inside Mysore. Bombay calls the maṭh
     "Kudalgi" and ranks its svāmī with Saṅkeśvar's (`archives/README.md`, "The Kudli estates, 1934").
2. **The four-pīṭha scheme appears as a list, not as institutions.** Dvārkā, Jyotirmaṭh and Purī are named as
   Śaṅkara's seats mainly in lists of the four maṭhs (Atkinson 1884, Gujarat 1901). Where the gazetteers
   describe the place itself:
   - Dvārkā's entry describes only the temple.
   - Joshimath's describes only the Badrinath Rawal's winter quarters.
   - Purī's is "the Sankaracharya" maṭh, with a library.
   - None of the three names a living pontiff before 1977, when Purī's Govardhana maṭha is called "still
     extant".
3. **The south has endowed Smārta maṭhs, described as estates and temple patrons and given no followers:**
   - Kumbakoṇam: Rs 14,000 a year and three temples.
   - Śivagaṅgā: under Muzrai management.
   - Kudali: a village and temple patronage in the gazetteers; in the Mysore files, estates across the Bombay
     Karnatak (see finding 1).
4. **After Independence the seats become more visible** (Karvīr, Govardhana, Kāñcī at Purī). Their estates and
   their jurisdiction over castes disappear from the texts. This matches `../revised/README.md`.

## Inām registers and archival files: Puṣpagiri and Virūpākṣa

Requested: the two maṭhs' presence in the inām registers. What could be found online (Nov 2026):

- **The registers themselves are not online.** These are the Madras Inam Commission's inām fair registers and
  title-deed registers (1860s), which would list the maṭhs' inām villages in Cuddapah, Bellary, Kurnool and
  Anantapur. They are not on the Internet Archive. Nor is any printed abstract of them, or of the Board of
  Revenue's inām proceedings.
- **The Madras Legislative Council question files on IA give nothing on either maṭha.** Searched: religious
  and service ināms 1921, 1932 and 1935; lands and revenue of temples and mutts 1946–47; commissioners to mutts
  1933.
- **The Madras manuals and gazetteers in the study** have no inām statement for either maṭha. Puṣpagiri appears
  only as a temple hill and village (Cuddapah 1875 and 1915). Hampi appears as the Virūpākṣa temple, and its
  svāmī only as the guru barred from riding into Hampi (Bellary 1872, p. 379).
- **What was found** is in the Mysore Muzrai (religious endowments) files of the Karnataka State Archives,
  digitised on IA (`results/archives.tsv`).
  - **Virūpākṣa (A01, 1935–36):**
    - The agent of "Sri Sankaracharya Virupaksha Samsthanam, Hampi" asks for royal honours on a Mysore
      tour.
    - The Svāmī cannot produce his papers, which "were left behind in the Nizam's Dominions". He states
      that "his Mutt is a branch of Sri Sringeri Mutt".
    - Mysore grants only the ordinary insignia, for want of information on "the status of the Mutt, the circle
      of its disciples and the standing of the present Head".
    - This is the only source in the study that describes the Hampi maṭh as an institution. It presents the
      maṭh as a Śṛṅgeri branch with its records in Hyderabad, whose standing Mysore could not verify.
  - **Puṣpagiri:** no file found.
  - **In passing:**
    - Mysore's gifts of elephants to the Śaṅkarācārya maṭh "at Kumbakonam", catalogued as "Kanchi Komakoti"
      (1925), and to the same maṭh "of Conjeevaram" (1936). They date the maṭh's return to Kāñcī between the
      two (A02–A03, catalogue descriptions only).
    - A State grant to a Śaṅkarācārya temple of the Avani maṭh (1930, A04).
- **Followed up** in `archives/README.md`: 338 Mysore files on the Śṛṅgeri and Kudli maṭhs (lands in and outside the State, debts, branches, successions, honours, Government management).
- **Next step if wanted:** the inām fair registers for Cuddapah and Bellary are held at the Tamil Nadu Archives
  (Chennai), with copies at the Andhra Pradesh State Archives (Hyderabad) and the Karnataka State Archives
  (Bengaluru, for Bellary). They would have to be consulted there or requested as copies.

## Limits

- The search is pattern-based. A maṭha described without any seat name or the word Śaṅkarācārya could be
  missed, although each coder also searched their volumes for "math", "mutt" and "Svāmi".
- Not available on IA: the South Canara *Manual* vol. II and a descriptive Chingleput gazetteer.
- Coverage of Mysore is limited to Rice's two editions. Mysore lies outside the study's six regions.
- `other` is a judgement category (Smārta houses not tied to a named pīṭha). Drop it for a pīṭha-only count.

## Files

| file | content |
|---|---|
| `results/mathas.tsv` | 63 merged rows: seat, place, institution, link, chapter, summary, verbatim quote, page |
| `results/coded/{W,N,S}.tsv` | the coded files, with comment lines for caste-allegiance counts and null results |
| `results/hits.tsv`, `results/hits_dedup.tsv` | the search output |
| `scripts/collect.py`, `dedupe.py`, `merge.py`, `check_quotes.py` | search, de-duplication, merge, quote check (run with `python3 -I` from `gazetteer-vedanta/`) |
| `results/archives.tsv` | archival files (Mysore Muzrai) on the Virūpākṣa, Kāñcī/Kumbakoṇam and Avani maṭhs |
| `CODING_INSTRUCTIONS.md` | coding rules |
