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
| **Kudali / Kudalgi** (Shimoga, Mysore) | two traditions: a branch appointed by Śṛṅgeri (Rice 1876, p. 380; 1897, pp. 459–60), or founded by the Saṅkeśvar secessionist (Belgaum 1884, pp. 601–02). Its Svāmī rebuilt the Hallur temple and holds the village (Dharwar, p. 722), and won the crosswise-palkhi privilege at Hubli up to the Privy Council (p. 757) | — |
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

## Findings

1. **The gazetteers describe one Śaṅkara maṭh network in detail, and it is Saṅkeśvar's.**
   - Śṛṅgeri had the widest following in the caste chapters, but no buildings outside Mysore.
   - Saṅkeśvar had a seat, urban branches, thirty inām villages across seven jurisdictions, temple patronage
     and a touring svāmī.
   - It is also the seat whose story the gazetteer tells as a secession from Śṛṅgeri. Kudali is claimed by
     both lines.
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
   - Kudali: a village and temple patronage.
4. **After Independence the seats become more visible** (Karvīr, Govardhana, Kāñcī at Purī). Their estates and
   their jurisdiction over castes disappear from the texts. This matches `../revised/README.md`.

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
| `CODING_INSTRUCTIONS.md` | coding rules |
