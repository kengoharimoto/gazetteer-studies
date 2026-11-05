# Śṛṅgeri and Kudli in the Mysore government files, 1876–1959

Part of `../` (the Śaṅkara maṭhas layer). The gazetteers saw Śṛṅgeri only as a subsidised estate in Mysore, and
Kudli only as a disputed branch. These files show both maṭhs as institutions:
- their lands inside and outside Mysore State;
- their revenues and debts;
- their branches;
- their successions;
- their tours and honours;
- the State's management of them.

## Sources and method

- **The files.** Karnataka State Archives files digitised on the Internet Archive:
  - Muzrai (religious endowments);
  - Revenue, Local Fund, General and Financial, Police, Municipal and Land-Records;
  - Mysore Gazette notices and Mysore Code regulations.
- **Selection.** Found by searching the catalogue descriptions for Śṛṅgeri and Kudli spellings: 391 files.
  `scripts/classify.py` sorts them (`results/catalogue.tsv`). Excluded:
  - the Mādhva Akṣobhya Tīrtha maṭh at Kudli (12 files, checked by title);
  - Kudli's temples;
  - newspaper digests;
  - plague notices.
  That leaves 338 files.
- **OCR.** Downloaded with `scripts/fetch_ocr.py` (kept out of git). 335 arrived; three are refused by the
  server. The typed pages (notes to the Dewan, orders, printed proceedings) read well. Handwriting and Kannada
  do not.
- **Coding.** Three coders under `CODING_INSTRUCTIONS.md`:
  - Śṛṅgeri to 1925: `results/coded/SA.tsv`;
  - Śṛṅgeri from 1926: `SB.tsv`;
  - Kudli, Avani and Hubli: `K.tsv`.
  There is one row per file (338 rows, merged in `results/archive_rows.tsv`):
  - legibility: 168 good, 88 partial, 82 none (those rest on the catalogue description, and say so);
  - topics: tours and honours 73, management 47, estate 33, revenue 22, succession 19, branches 16,
    finance 13; local and routine items 82, other 33.
- **Quote check.** All 250 quotes were found verbatim in the OCR of their own file
  (`scripts/check_quotes.py`). The headline facts below were also re-read in the OCR.
- **Catalogue corrections.**
  - The file catalogued as "Hubli Sringeri Matt" (1923) is the Kudli recognition of Valukeśvara Bhāratī (1925).
  - Several files dated 1892 or 1923 contain papers of 1905–07 or 1924–25.
  - Four "Sringeri" files concern a private person or a town temple.

## 1. Śṛṅgeri: a principality in debt

- **The jāgīr.**
  - The Sringeri Jahgir Inam Settlement Regulation (IV of 1897) declares that the jāgīr "vests in the Guru for
    the time being". It settles the minor ināms at the Guru's request and bars the courts from questioning the
    settlement.
  - An inām investigation was held at Śṛṅgeri in February–March 1898. A Gazette notice of April 1908 lists over
    220 villages.
  - The maṭh's Agent held Amildar's revenue powers (1892) and the Deputy Commissioner's excise powers in the
    jāgīr (1905).
- **Revenues beyond the jāgīr.**
  - Toddy revenue of 13 villages in the Chikmagalur and Koppa taluks (allowed 1903, Belavadi among them).
  - Ganja revenue claims, filed yearly from 1893.
  - Sayar (customs) "from time immemorial", cut to areca nut in 1887 and replaced by a share of municipal octroi.
  - A tasdik of Rs 500 a month through the Koppa treasury.
  - Mineral rights (1908–20).
  - Inām villages outside the jāgīr: Belavadi, Harakere/Sarvamangala, Jodi Dyavasandra (Hoskote; half gifted in
    1914, half bought in 1940, 236 acres).
- **Debt.**
  - A loan of Rs 1,25,000 from the Maharaja's personal estate (1891, 4%) was spent partly on jewels. It stood at
    Rs 1,31,812 in 1904. The Dewan remarked that the maṭh "does not appear to have known solvency within
    living memory".
  - In 1936 the maṭh owed over Rs 75,000 and could not recover about Rs 2 lakhs it had lent out. Government
    lent it Rs 75,000 at 5%.
- **Property outside Mysore** (from the management files of 1935–44):
  - the Ramnad and Sivaganga grants of the Sethupatis (1864, 1894), whose income fell from over Rs 10,000 a
    year to almost nothing;
  - a mortgage on Sendanadi village and houses at Tirupattur;
  - shares of Pudurvalasai;
  - Coimbatore lands taken over through bad loans (Avanasi 179 acres, Kangayam, Kaniyur);
  - a Tinnevelly debt and an Aravankulam mortgage;
  - sites at Erode;
  - a Gokarna property;
  - Pimpalgaon (Rahuri), a Sindia grant of 1793 whose income goes to the Nasik maṭh;
  - places in the Bombay Karnatak (Gangapur, Gajendragad, Paravi Basapur);
  - Kaladi: a Travancore grant of Rs 495 a year and 26 acres.
- **Branches named:**
  - Sultanpet in Bangalore (drought japam, Rs 1,000 each in 1919 and 1923);
  - Tirupati (a committee of eight in 1940; the TTD claims oversight);
  - Nasik/Panchavati (a suit against the municipality, 1942);
  - Haridwar (repairs before the 1945 Kumbh);
  - Gaya, Benares, Rameswaram and Madura;
  - a "vassal Mutt", Tīrthamuttūr in Tirthahalli taluk, which pays Rs 31-4-0 a year and whose Svāmīs are
    consecrated at Śṛṅgeri (1923).
  - Khandesh had an accredited agent, challenged there by a nominee of Saṅkeśvar (1913).

## 2. The State and the Jagadguru

- **1912.**
  - The Svāmī died after 46 years without naming a successor; the papers call this unprecedented.
  - The Maharaja had a 19-year-old, Narasimha Śāstrī, consecrated as Candraśekhara Bhāratī.
  - The State ran the maṭh through its Agent, inventoried its properties "within and outside Mysore State", and
    handed it back in August 1912.
- **1930s.**
  - The Svāmī's recurring illness led to the takeover of the maṭh and all its properties under Government
    management by the order of 30 January 1936 (from 17 February). It was extended "until further orders" in
    1937 at the Svāmī's own request.
  - From 1938 he had a free hand in internal affairs within the budget.
  - In 1944 his South Indian disciples asked for the maṭh to be handed back, and were refused. The return of the
    properties is ordered in 1959.
  - The successor, Abhinava Vidyātīrtha, was nominated and given sannyāsa in 1931 under Government sanction. He
    was educated in Bangalore in 1936–37 at Government's insistence.
- **Police and guards.** A police guard was kept on the treasury and the Śāradāmbā jewels, the maṭh paying Rs 100
  of Rs 166 a month. Sepoys were lent.

## 3. Tours and honours

- **Tours into British India** were arranged with the Madras Government:
  - 1891–95 to Rameswaram, with 3 elephants, 25 swords, 25 muskets and 400 followers;
  - 1907 to Kaladi through Coimbatore, Salem, North Arcot, Tanjore, Madura, Tinnevelly, Malabar and
    Travancore (Madras Order 83 Political);
  - 1924, by G.O. 97.
- **In Mysore**, receptions followed the 1895 memoranda: a 21-gun salute, Palace honours and Rs 300 bhikṣā.
- **Disputes:**
  - Śrī Vaiṣṇavas and the Parakāla Svāmī demanded purification after his entry into the Raṅganātha temple at
    Srirangapatna (1895). The Regent refused.
  - The Uttarādi (1906) and Ahobila (1907) maṭhs complained of his processions.
  - He was advised not to enter the Belur temple in 1924.
- **Old grants reproduced in these files** (copies, not originals): a Nizam's order of 1779–80 giving the
  Svāmī authority over Mallikārjuna and other Deccan temples and one anna in the rupee from temple funds, and a
  rahadari letter of Tipu Sultan.

## 4. Kudli: a maṭh of its own, with Bombay estates

- **Origin.** The files give the maṭh's own account, contested by Śṛṅgeri:
  - In 1846 the Śṛṅgeri side called Kudli "but a branch Matt", a *tondu* (subordinate) maṭh. The Huzur Adalat
    (1847–49) held that it "is not a Tondu Matt", that it is a maṭh "guided by its own laws".
  - The Dewan to the Resident, 1895: "The Kudli Matt as a separate branch of the original Matt at Sringeri came
    into existence at the Partition of A. D. 1656-57".
  - A Bombay officer's recommendation of 1896 (forwarded by the Commissioner, Southern Division, and copied into a
    Mysore file of 1903) asks for the Svāmī of Kudalgi to be exempted from the Arms Act. It notes that "his brother
    Swami of Sankeshwar … who is in no way superior in position, has been exempted". This puts Kudli on a level
    with Saṅkeśvar.
  - No file says that Śṛṅgeri appoints the Kudli guru, as Rice (1876, 1897) does. The archive agrees with the
    Belgaum gazetteer that Kudli and Saṅkeśvar came out of one secession. It dates the split to 1656–57, where
    the gazetteer gives c. 1570.
- **Lands** (Muzrai Commissioner, 1933):
  - income Rs 35,046-13-6: villages in the State Rs 4,499, villages outside Rs 10,504, sircar lands in the
    State Rs 1,095, outside Rs 6,294, varṣāsana from disciples Rs 1,024;
  - so most of the income came from outside Mysore.
  - The outside properties are listed in 1934 (see "The Kudli estates, 1934" below).
  - Bombay levied succession nazarana on the Dharwar and Bijapur ināms (Rs 2,745 and Rs 1,167, 1936). The
    ināms were granted to "Shankarbha[rati] and his successors". Bombay records call the maṭh "Kudalgi" or the
    "Uddughatti Mutt", after Udagatti in Ranibennur taluk, where the svāmīs lived.
  - In Mysore it held five jodi villages granted before 1822, and Hangarahalli (Kumsi).

### The Kudli estates, 1934

- **The source.** In March 1934 the Government Agent of the maṭh, H. S. Sampangiramiah, drew up a list of the
  taluks outside Mysore where the maṭh held property (file coded as K32 in `results/coded/K.tsv`).
  - It went through the Resident to Bombay, Madras, Hyderabad and the Deccan States, so that their officers would
    help the Agent collect revenue.
  - Bombay instructed the Collectors of Dharwar, Kanara, Belgaum and Bijapur (G.R. 17 April and 4 October 1934),
    and Madras the Collectors of Bellary and Anantapur.

| where | taluks or estates in the list | follow-up |
|---|---|---|
| Dharwar District (Bombay) | Ranibennur, Karajgi, Hangal (Hanagallu), Kod, Shiggaon (Siggavi), Navalgund, Kalghatgi, Dharwar, Hubli, Ron, Gadag | nazarana Rs 2,745 on the Dharwar ināms (1936) |
| Bijapur District (Bombay) | Badami, Bagalkot, Bagevadi, Bijapur, Sindgi, Hungund | nazarana Rs 1,167 (1936) |
| Belgaum District (Bombay) | Parasgad | |
| North Kanara (Bombay) | Mundgod | |
| Bellary District (Madras) | Kudligi, Harapanahalli | |
| Anantapur District (Madras) | Madakasira | |
| Kolhapur State | Thoragallu (Torgal), Kankanvadi | |
| Ramdurg State | Ramdurg | |
| Sangli State | Shirahatti, with a village (Giddehosapura?) in Shirahatti taluk | a village under attachment; Sangli asked for certified copies of the Agent's powers (1935) |
| Miraj Senior / Miraj Junior | Lakshmeshwar / Gudageri | |
| Savanur State; Sirasangi jagir | Savanur; Sirasangi | |
| Jamkhandi State | Kundgol | |
| Hyderabad State | Yelburga, Surapura (Shorapur) | no property found in Shorapur, Shahpur or Andola |

- **More properties in other files:**
  - A 1935 file has the Government Agent recovering sums from one Hutchu Rao "in respect of the properties in
    Sangli State and Venkatapura Village".
  - The Bombay inām grants were made to "Shankarbha[rati] and his successors", on condition of nazarana.
- **Where they lie.** Twenty-seven of the places are mapped as crosses in the Gazetteer Places Finder
  (`../../map/places_map.html`, the "Kudli estates" filter). Dharwar, Hubli and Bijapur carry the fact in their
  existing entries. The combined map (`../../map/combined_map.png`) marks all 30 taluks and states. Hyderabad
  is left out of both maps, since it reported no property.
- **What it shows.** Nearly all the estates lie between Saṅkeśvar and Kudli, in the Dharwar–Bijapur country and the
  southern Maratha states. That is where the Bombay gazetteers place the Kudalgi Svāmī's village and temple at
  Hallur and his procession privilege at Hubli.
- **Honours.**
  - The *adda-palakki* (crosswise palanquin) was refused in 1884, 1895 and about 1905–07 "as a matter of
    principle and policy". Kudli had held this privilege at Hubli up to the Privy Council (Dharwar gazetteer
    1884).
  - The *ambari* on an elephant was allowed in 1927, and confirmed in 1931 over feared Liṅgāyat objections.
- **Succession and management.**
  - A rival line, superseded in 1875, was rejected repeatedly (1904–1929).
  - The recognised line had three successions between 1924 and 1936.
  - Government managed the properties from 1933, at the Svāmī's request, until March 1941.
  - In 1929 Śṛṅgeri's Agent suspected Kudli of dropping "Kudli" from its name.

## 5. Avani and Hampi

- **Avani:**
  - Its svāmī died at Mahabubabad (Hyderabad State) in 1925.
  - Memorials of 1924 claim the maṭh's "absolute independence" of other maṭhs and its foundation by
    Vidyāraṇya.
  - Its head processed in Bangalore in 1934 on the strength of an 1894 rahadari.
- **Hampi:** a 1912 petition and press letter put Hampi forward as the rival seat to Śṛṅgeri at the 1912
  succession. Compare the 1935–36 file in `../results/archives.tsv`, where the Hampi Svāmī calls his maṭh "a
  branch of Sri Sringeri Mutt".

## What this adds to the study

**Place in the study's verdict** (`../../SYNTHESIS.md`, "The answer"): Śaṅkara's
tradition was regional, not dominant. These files show what that meant for the two Mysore seats.
- **Śṛṅgeri:** its reach outside its own jāgīr was made of branches at pilgrimage centres, debts and tours, not
  landed followings. Even in its own district the Liṅgāyats and Śrīvaiṣṇavas were the larger bodies.
- **Kudli:** its weight lay in its Bombay ināms (1934), the same country as Saṅkeśvar's. That is the one region where
  the Śaṅkara houses out-endowed their rivals.
- **The state:** its management of both seats (1912, 1933–59) shows how far they depended on the princely state
  rather than on a following that could sustain them.


1. **The two pictures fit together.** The gazetteers' "seat without buildings" outside Mysore is confirmed, and
   explained. Śṛṅgeri's reach outside the jāgīr took two forms:
   - grants, mortgages and branch maṭhs at pilgrimage centres (Rameswaram, Kaladi, Tirupati, Nasik, Haridwar,
     Benares);
   - debts owed to it in the Tamil districts.
   It held no estates among the Kanara castes who called it their guru.
2. **Kudli was a Bombay-Karnatak landholder.** Most of its income came from ināms in Dharwar, Bijapur and the
   Maratha states. That is the Saṅkeśvar country, and it fits the Bombay files' pairing of the two svāmīs as
   equals. The gazetteers' "Kudalgi" and the Mysore "Kudli" are one maṭh, seen from its estates and from its
   seat.
3. **The princely state, not British India, made and unmade these seats:**
   - consecration (1912);
   - management (1936–59 at Śṛṅgeri, 1933–41 at Kudli);
   - honours, regulated by precedent down to the palanquin's angle.
   British India appears as the Madras Government arranging tours and Bombay collecting nazarana.

## Limits

- Selection was by catalogue description. A file about the maṭhs whose description names neither would be
  missed.
- 82 files have no legible OCR. Their rows rest on the catalogue description.
- The archive is Mysore's. Śṛṅgeri's and Kudli's own records, and the Bombay and Madras files on their ināms,
  were not searched.

## Files

| file | content |
|---|---|
| `results/catalogue.tsv` | 391 catalogue entries, classified (matha, topic, include) |
| `results/archive_rows.tsv` | 338 coded rows (one per file): matha, topic, places, summary, verbatim quote, legibility |
| `results/coded/{SA,SB,K}.tsv` | the three coded files |
| `scripts/classify.py`, `fetch_ocr.py`, `merge.py`, `check_quotes.py` | classification, download, merge, quote check (`python3 -I`, from `gazetteer-vedanta/`) |
| `CODING_INSTRUCTIONS.md` | coding rules |
