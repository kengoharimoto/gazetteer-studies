#!/usr/bin/env python3
"""Every place that matters in the gazetteer-vedanta study, with the spellings the sources use and the modern name.

Run: python3 -I map/places_data.py   (writes map/places.tsv)
Fields per entry:
  name      the form used in the study's reports
  variants  spellings found in the sources (colonial, OCR-normalised, revised gazetteers), ';'-separated
  modern    modern name of the place
  district  modern district (for a colonial district: the modern district(s) covering it)
  state     modern state / country
  lat, lon  approximate (district headquarters or town)
  kinds     district | seat | branch | site  (seat = Śaṅkara seat; branch = branch, estate or temple of a seat;
            site = other maṭh, Śaṅkarācārya site or place discussed in the reports)
  region    the study's region: Bombay, Madras, UP, Bengal, Punjab, CP, Mysore, Hyderabad, Other
  note      what the study says about it (short)
  refs      study folders
Coordinates are approximate and meant for orientation, not for measurement.
"""
P = []
def add(name, variants, modern, district, state, lat, lon, kinds, region, note="", refs=""):
    P.append(dict(name=name, variants=variants, modern=modern, district=district, state=state, lat=lat, lon=lon,
                  kinds=kinds, region=region, note=note, refs=refs))

# ---------------- Bombay Presidency ----------------
B = "Bombay"
add("Ratnagiri", "Ratnágiri", "Ratnagiri", "Ratnagiri", "Maharashtra", 16.99, 73.30, "district", B,
    "1872 census returned 99.7% of Hindus as 'Śaiva'; Smārta Shenvis under the Kavaḷe svāmī.", "results/; revised/")
add("Kolaba", "Kolába", "Raigad (district), Alibag (HQ)", "Raigad", "Maharashtra", 18.64, 72.87, "district", B, "", "results/")
add("Thana", "Tána; Thane", "Thane", "Thane; Palghar", "Maharashtra", 19.20, 72.97, "district", B,
    "Places volume XIV (1882) read for the maṭha layer.", "results/; mathas/")
add("Kanara", "North Kanara; Kánara; Canara", "Uttara Kannada (Karwar HQ)", "Uttara Kannada", "Karnataka", 14.81, 74.13, "district", B,
    "Śṛṅgeri's stronghold: 32–39% of Hindus in castes asserted Smārta; about 45 caste entries name 'the Smart monastery at Shringeri'. No Śṛṅgeri maṭh located in the district. Rivals: the Konkan Kuṇbīs left a Liṅgāyat guide of Chitaldurg for Śṛṅgeri in 1881.", "results/; sringeri/")
add("Nasik", "Násik; Nashik", "Nashik", "Nashik", "Maharashtra", 20.00, 73.79, "district;site", B,
    "Panchavati: tomb and monastery of a Śaṅkarācārya 'said to have come from Shringeri' (1883, pp. 518–19); Dr Kurtakoti, Śaṅkarācārya of Karvīr, lived here (1977). A Śṛṅgeri maṭh building at Nasik appears in a 1940 Mysore file.", "results/; mathas/; revised/")
add("Ahmadnagar", "Ahmednagar; Ahmadnagar", "Ahilyanagar (renamed 2024)", "Ahilyanagar", "Maharashtra", 19.09, 74.74, "district", B,
    "'the decrees of Shankaracharya at Shankeshvar' are final; Kuṇbīs 'cannot tell whether they are Smarts or Bhagvats'.", "results/; revised/")
add("Poona", "Puna; Pune", "Pune", "Pune", "Maharashtra", 18.52, 73.86, "district;site", B,
    "Brahmans' pontiff the head of Śṛṅgeri; c. 1750 a Śaṅkarācārya allowed a Jain temple in the city (Places, 1885).", "results/; mathas/")
add("Satara", "Sátára", "Satara", "Satara", "Maharashtra", 17.68, 74.00, "district", B, "", "results/")
add("Sholapur", "Solapur", "Solapur", "Solapur", "Maharashtra", 17.66, 75.91, "district", B,
    "Arya Kshatris hold sanads from 'the Shankaracharya of Shringeri'; Komaṭis under Bhāskarācārya, 'deputy of Shankaracharya'.", "results/; mathas/")
add("Belgaum", "Belgaon", "Belagavi", "Belagavi", "Karnataka", 15.85, 74.50, "district", B,
    "Places volume describes the Saṅkeśvar maṭh in full (1884, pp. 600–02).", "results/; mathas/")
add("Dharwar", "Dhárwár; Dharwad", "Dharwad", "Dharwad; Haveri; Gadag", "Karnataka", 15.46, 75.01, "district", B,
    "Marāṭhās, Komṭis and Khatrīs under the Śaṅkarācārya; about 7.6% of Hindus in castes asserted Smārta. A village named Shringeri near Hangal is unrelated (an old weir). Eleven of its taluks held Kudli maṭh property (1934); Bombay levied Rs 2,745 nazarana on the maṭh's Dharwar ināms (1936).", "results/; mathas/; mathas/archives/")
add("Bijapur", "Bijápur", "Vijayapura", "Vijayapura; Bagalkot", "Karnataka", 16.83, 75.71, "district", B,
    "Marāṭhās 'Smārts … their guide being Shankarāchārya'. Six taluks held Kudli maṭh property (1934); Rs 1,167 nazarana on its Bijapur ināms (1936).", "results/; revised/; mathas/archives/")
add("Kolhapur", "Kolhápur; Karvir; Karvīr; Karveer; Karaveer", "Kolhapur", "Kolhapur", "Maharashtra", 16.70, 74.24, "district;branch", B,
    "Saṅkeśvar Svāmī's maṭh in the city (1886); became the Karvīr Pīṭha c. 1909 (1959, p. 874); Ambābāī temple spire added by a Śaṅkarācārya of Saṅkeśvar.", "results/; mathas/; revised/")
add("Surat", "", "Surat", "Surat", "Gujarat", 21.17, 72.83, "district", B, "Gujarat: Vaiṣṇava (Vallabha, Svāminārāyaṇa).", "results/")
add("Broach", "", "Bharuch", "Bharuch", "Gujarat", 21.70, 72.98, "district", B, "", "results/")
add("Kaira", "", "Kheda", "Kheda", "Gujarat", 22.75, 72.68, "district", B, "", "results/")
add("Panch Mahals", "Panch Maháls", "Panchmahal (Godhra HQ)", "Panchmahal", "Gujarat", 22.78, 73.61, "district", B, "", "results/")
add("Ahmedabad", "Ahmadabad", "Ahmedabad", "Ahmedabad", "Gujarat", 23.02, 72.57, "district", B, "", "results/")
add("Cutch", "Kachh", "Kutch", "Kutch", "Gujarat", 23.25, 69.67, "district", B, "", "results/")
add("Kathiawar", "Káthiáwár", "Saurashtra", "Rajkot and neighbouring districts", "Gujarat", 22.30, 70.80, "district", B,
    "Its Dwarka entry (1884) describes the temple only, no maṭha.", "results/; mathas/")
add("Khandesh", "Khándesh", "Jalgaon, Dhule, Nandurbar", "Jalgaon; Dhule; Nandurbar", "Maharashtra", 21.00, 75.56, "district", B, "", "results/")
add("Bombay", "Bombay City", "Mumbai", "Mumbai", "Maharashtra", 18.95, 72.83, "district", B, "1,947 Gosāvīs in 1881.", "census-images/")

# ---------------- Madras Presidency ----------------
M = "Madras"
for name, var, modern, dist, state, la, lo, note in [
    ("Anantapur", "", "Anantapur", "Anantapur; Sri Sathya Sai", "Andhra Pradesh", 14.68, 77.60, ""),
    ("Bellary", "Ballari", "Ballari", "Ballari; Vijayanagara", "Karnataka", 15.14, 76.92, "Hampi lies in this district. Thurston: the Śṛṅgeri Svāmī's 1888 visit led to a procession dispute with Liṅgāyats."),
    ("Chingleput", "Chengalpat; Chengalpattu", "Chengalpattu", "Chengalpattu; Kanchipuram; Tiruvallur", "Tamil Nadu", 12.69, 79.98, "The exception in the Tamil division: 60% Aiyaṅgār, 12% Smārta (1891). Crole's Manual (1879) is the descriptive source."),
    ("Cuddapah", "Kadapa", "Kadapa", "YSR Kadapa", "Andhra Pradesh", 14.47, 78.82, "Puṣpagiri lies in this district."),
    ("Ganjam", "", "Ganjam", "Ganjam", "Odisha", 19.31, 84.79, ""),
    ("Godavari", "", "East and West Godavari", "East Godavari; West Godavari", "Andhra Pradesh", 16.99, 82.25, ""),
    ("Kistna", "Krishna", "Krishna", "Krishna; NTR", "Andhra Pradesh", 16.19, 81.13, "Census shows movement in the Śaiva/Vaiṣṇava balance 1871–1891."),
    ("Kurnool", "Karnul", "Kurnool", "Kurnool; Nandyal", "Andhra Pradesh", 15.83, 78.04, ""),
    ("Madras", "Madras City", "Chennai", "Chennai", "Tamil Nadu", 13.08, 80.27, ""),
    ("Madura", "Madurai", "Madurai", "Madurai", "Tamil Nadu", 9.93, 78.12, "42% Smārta, 26% Aiyaṅgār among Brahmans (1891); revised volume (1960) still names no seat. A Śṛṅgeri branch maṭh at Madura (Mysore files)."),
    ("Malabar", "", "Kozhikode and neighbouring districts", "Kozhikode; Malappuram; Palakkad; Kannur; Wayanad", "Kerala", 11.25, 75.78, "'Smarta' mostly the Nambūtiri caste judge; a madam near Tanur ascribed to Śaṅkara (1908)."),
    ("Nellore", "", "Nellore", "Sri Potti Sriramulu Nellore", "Andhra Pradesh", 14.44, 79.99, ""),
    ("North Arcot", "", "Vellore", "Vellore; Tiruvannamalai; Ranipet; Tirupattur", "Tamil Nadu", 12.92, 79.13, ""),
    ("Salem", "", "Salem", "Salem; Namakkal; Dharmapuri; Krishnagiri", "Tamil Nadu", 11.66, 78.15, "Śṛṅgeri Matam's 'papal bulls' for the Marka Brahmans of Tali (1918)."),
    ("South Canara", "South Kanara; Dakshina Kannada", "Dakshina Kannada and Udupi", "Dakshina Kannada; Udupi", "Karnataka", 12.87, 74.84, "Śṛṅgeri the guru seat of non-Brahmin castes (Kharvis, Marāṭhās, Servegāras, Ares, Chaptegāras) in Thurston; gone by 1973. Rivals: the Mādhvas of Uḍupi; by 1973 Tulu Brahmans are 'largely followers of Madhvacharya'."),
    ("Tanjore", "Thanjavur", "Thanjavur", "Thanjavur; Tiruvarur; Nagapattinam", "Tamil Nadu", 10.79, 79.14, "64% of Brahmans in Smārta sub-castes (1891)."),
    ("Travancore", "", "Thiruvananthapuram (former state)", "southern Kerala", "Kerala", 8.52, 76.94, "Princely state."),
    ("Vizagapatam", "Visakhapatnam", "Visakhapatnam", "Visakhapatnam; Vizianagaram", "Andhra Pradesh", 17.69, 83.22, "Carmichael's Manual (1869) on the Smārta line 'at Sringagiri'."),
    ("Coimbatore", "", "Coimbatore", "Coimbatore; Tiruppur; Erode", "Tamil Nadu", 11.02, 76.96, ""),
    ("Nilgiris", "Nilgiri Hills", "The Nilgiris", "The Nilgiris", "Tamil Nadu", 11.41, 76.70, ""),
    ("South Arcot", "", "Cuddalore and Villupuram", "Cuddalore; Villupuram; Kallakurichi", "Tamil Nadu", 11.75, 79.75, ""),
    ("Trichinopoly", "Tiruchirappalli", "Tiruchirappalli", "Tiruchirappalli; Perambalur; Karur", "Tamil Nadu", 10.80, 78.69, "About 55% Smārta among Brahmans (1891)."),
    ("Tinnevelly", "Tirunelveli", "Tirunelveli", "Tirunelveli; Thoothukudi; Tenkasi", "Tamil Nadu", 8.73, 77.70, "About 55% Smārta among Brahmans (1891)."),
    ("Pudukota", "Pudukkottai", "Pudukkottai", "Pudukkottai", "Tamil Nadu", 10.38, 78.82, "Princely state."),
]:
    add(name, var, modern, dist, state, la, lo, "district", M, note, "madras/; census-images/")

# ---------------- United Provinces ----------------
U = "UP"
for name, var, modern, dist, state, la, lo, note in [
    ("Dehra Dun", "Dehradun", "Dehradun", "Dehradun", "Uttarakhand", 30.32, 78.03, ""),
    ("Saharanpur", "", "Saharanpur", "Saharanpur; Haridwar", "Uttar Pradesh / Uttarakhand", 29.97, 77.55, "Includes Hardwar and Kankhal (Bhola Gir's Gosāins, the Nirañjanī and Nirbānī akhāṛās)."),
    ("Muzaffarnagar", "", "Muzaffarnagar", "Muzaffarnagar; Shamli", "Uttar Pradesh", 29.47, 77.70, ""),
    ("Meerut", "", "Meerut", "Meerut; Baghpat", "Uttar Pradesh", 28.98, 77.71, "5,326 Gosāins (1872), 5,083 Daśanāmīs (1891)."),
    ("Bulandshahr", "", "Bulandshahr", "Bulandshahr", "Uttar Pradesh", 28.40, 77.85, ""),
    ("Aligarh", "", "Aligarh", "Aligarh; Hathras", "Uttar Pradesh", 27.88, 78.08, ""),
    ("Muttra", "Mathura", "Mathura", "Mathura", "Uttar Pradesh", 27.49, 77.67, " Rivals: Vallabha and Gauḍīya Vaiṣṇava centre. Its 17,131 'Gosains' in 1891 are all unspecified, with no Bairāgīs or Jogīs returned: probably Braj's whole ascetic population (1881: 9,812 Bairāgīs, 3,627 Jogīs; 1901: 18,272 Faqīrs, only 803 Gosāins), not Daśanāmīs."),
    ("Agra", "", "Agra", "Agra", "Uttar Pradesh", 27.18, 78.01, ""),
    ("Farukhabad", "Farrukhabad; Fatehgarh", "Farrukhabad", "Farrukhabad; Kannauj", "Uttar Pradesh", 27.39, 79.58, ""),
    ("Mainpuri", "", "Mainpuri", "Mainpuri", "Uttar Pradesh", 27.23, 79.02, ""),
    ("Etawah", "", "Etawah", "Etawah; Auraiya", "Uttar Pradesh", 26.78, 79.02, ""),
    ("Etah", "", "Etah", "Etah; Kasganj", "Uttar Pradesh", 27.56, 78.66, ""),
    ("Bareilly", "Bareli", "Bareilly", "Bareilly", "Uttar Pradesh", 28.37, 79.43, "6,169 Gosāins (1872), 4,023 Daśanāmīs (1891)."),
    ("Bijnor", "", "Bijnor", "Bijnor", "Uttar Pradesh", 29.37, 78.14, ""),
    ("Budaun", "Badaun", "Badaun", "Budaun", "Uttar Pradesh", 28.04, 79.12, ""),
    ("Moradabad", "Muradabad", "Moradabad", "Moradabad; Sambhal; Amroha", "Uttar Pradesh", 28.84, 78.77, "Salempur Gosāin maṭh (Ban mahants, 36 villages)."),
    ("Shahjahanpur", "", "Shahjahanpur", "Shahjahanpur", "Uttar Pradesh", 27.88, 79.91, ""),
    ("Pilibhit", "", "Pilibhit", "Pilibhit", "Uttar Pradesh", 28.63, 79.80, ""),
    ("Cawnpore", "Kanpur", "Kanpur", "Kanpur Nagar; Kanpur Dehat", "Uttar Pradesh", 26.45, 80.33, ""),
    ("Fatehpur", "", "Fatehpur", "Fatehpur", "Uttar Pradesh", 25.93, 80.81, ""),
    ("Banda", "", "Banda", "Banda; Chitrakoot", "Uttar Pradesh", 25.48, 80.33, ""),
    ("Hamirpur", "", "Hamirpur", "Hamirpur; Mahoba", "Uttar Pradesh", 25.95, 80.15, ""),
    ("Allahabad", "Prayag", "Prayagraj", "Prayagraj; Kaushambi", "Uttar Pradesh", 25.44, 81.85, "Akhāṛās at Daraganj lead the Magh/Kumbh procession."),
    ("Jhansi", "", "Jhansi", "Jhansi", "Uttar Pradesh", 25.45, 78.57, ""),
    ("Jalaun", "Orai", "Jalaun", "Jalaun", "Uttar Pradesh", 26.15, 79.33, ""),
    ("Lalitpur", "", "Lalitpur", "Lalitpur", "Uttar Pradesh", 24.69, 78.42, ""),
    ("Benares", "Banaras; Kashi; Varanasi", "Varanasi", "Varanasi; Chandauli; Bhadohi", "Uttar Pradesh", 25.32, 83.01, "Nirañjanī, Jūnā and Nirbānī akhāṛās; a Śṛṅgeri branch maṭh appears in a 1935 Mysore file. Rivals: Nevill (1909, pp. 92–93): 'Vedantism … almost exclusively prevails'; Rāmānanda's and Vallabha's influence is strong, 'but … the shrines dedicated to the cult of Shiva greatly predominate'. 1891 census: 4,106 Gosāins (1,899 Daśanāmī), 419 Jogīs, 141 Bairāgīs; 89.4% Hindu, 10.3% Muslim (1901)."),
    ("Mirzapur", "", "Mirzapur", "Mirzapur; Sonbhadra", "Uttar Pradesh", 25.15, 82.57, "Mahant Anand Gir's 39 villages; Gosāins owned 44,784 acres."),
    ("Jaunpur", "", "Jaunpur", "Jaunpur", "Uttar Pradesh", 25.75, 82.69, ""),
    ("Ghazipur", "", "Ghazipur", "Ghazipur", "Uttar Pradesh", 25.58, 83.58, ""),
    ("Ballia", "", "Ballia", "Ballia", "Uttar Pradesh", 25.76, 84.15, ""),
    ("Gorakhpur", "", "Gorakhpur", "Gorakhpur; Deoria; Kushinagar; Maharajganj", "Uttar Pradesh", 26.76, 83.37, "Ram Ratangir's 36 villages; 13,944 Atīths; the Nāth temple. Rivals: the Gorakhnāth temple is the centre of the Nāth Jogīs, the rival Śaiva ascetic network."),
    ("Basti", "", "Basti", "Basti; Siddharthnagar; Sant Kabir Nagar", "Uttar Pradesh", 26.80, 82.73, ""),
    ("Azamgarh", "", "Azamgarh", "Azamgarh; Mau", "Uttar Pradesh", 26.07, 83.18, ""),
    ("Kumaun", "Kumaon", "Kumaon (Almora, Nainital)", "Almora; Nainital; Bageshwar; Pithoragarh", "Uttarakhand", 29.60, 79.66, "8,860 Gosāins (1872); Pinnath Gosāin colony."),
    ("Garhwal", "British Garhwal", "Garhwal (Pauri, Chamoli)", "Pauri Garhwal; Chamoli; Rudraprayag", "Uttarakhand", 30.15, 78.78, "Jyotirmaṭh and Badrinath lie here."),
    ("Tarai", "Terai", "Udham Singh Nagar", "Udham Singh Nagar", "Uttarakhand", 28.98, 79.40, ""),
    ("Lucknow", "", "Lucknow", "Lucknow", "Uttar Pradesh", 26.85, 80.95, ""),
    ("Unao", "Unnao", "Unnao", "Unnao", "Uttar Pradesh", 26.55, 80.49, ""),
    ("Rae Bareli", "Rai Bareli", "Raebareli", "Raebareli", "Uttar Pradesh", 26.23, 81.24, ""),
    ("Sitapur", "", "Sitapur", "Sitapur", "Uttar Pradesh", 27.57, 80.68, "Goshains 'before the abolition of zamindari some of them were zamindars' (revised)."),
    ("Hardoi", "", "Hardoi", "Hardoi", "Uttar Pradesh", 27.40, 80.13, ""),
    ("Kheri", "Lakhimpur", "Lakhimpur Kheri", "Lakhimpur Kheri", "Uttar Pradesh", 27.95, 80.78, ""),
    ("Fyzabad", "Faizabad", "Ayodhya (district renamed 2018)", "Ayodhya; Ambedkar Nagar", "Uttar Pradesh", 26.78, 82.13, "Ayodhyā dominated by the Bairāgī akhāṛās. Rivals: the gazetteer describes Bairāgī dominance, yet the 1891 census returns 5,371 Daśanāmīs against 2,017 Bairāgīs; enumerators used these words loosely."),
    ("Gonda", "", "Gonda", "Gonda; Balrampur", "Uttar Pradesh", 27.13, 81.97, "Goshains 'followers of Shankaracharya'; 11,478 Daśanāmīs (1891)."),
    ("Bahraich", "", "Bahraich", "Bahraich; Shravasti", "Uttar Pradesh", 27.57, 81.60, ""),
    ("Sultanpur", "", "Sultanpur", "Sultanpur; Amethi", "Uttar Pradesh", 26.26, 82.07, ""),
    ("Partabgarh", "Pratapgarh", "Pratapgarh", "Pratapgarh", "Uttar Pradesh", 25.90, 81.95, ""),
    ("Bara Banki", "Barabanki", "Barabanki", "Barabanki", "Uttar Pradesh", 26.93, 81.19, ""),
]:
    add(name, var, modern, dist, state, la, lo, "district", U, note, "north/; census-images/")

# ---------------- Bengal, Bihar, Orissa ----------------
G = "Bengal"
for name, var, modern, dist, state, la, lo, note in [
    ("Calcutta", "Kolkata", "Kolkata", "Kolkata", "West Bengal", 22.57, 88.36, " Rivals: almost no Daśanāmīs (3 Atīths, 13 Gosāins in 1901). The ground belonged to Chaitanya Vaiṣṇavism and Kālī (Kālīghāṭ), and among the educated to the Brahmos (24 Parganas 1914)."),
    ("Murshidabad", "", "Murshidabad", "Murshidabad", "West Bengal", 24.18, 88.27, ""),
    ("Rajshahi", "", "Rajshahi", "Rajshahi", "Bangladesh", 24.37, 88.60, ""),
    ("Jalpaiguri", "", "Jalpaiguri", "Jalpaiguri", "West Bengal", 26.52, 88.72, ""),
    ("Darjeeling", "Darjiling", "Darjeeling", "Darjeeling", "West Bengal", 27.04, 88.26, ""),
    ("Rangpur", "", "Rangpur", "Rangpur", "Bangladesh", 25.75, 89.25, ""),
    ("Pabna", "", "Pabna", "Pabna", "Bangladesh", 24.00, 89.24, ""),
    ("Patna", "", "Patna", "Patna", "Bihar", 25.59, 85.14, ""),
    ("Gaya", "", "Gaya", "Gaya; Aurangabad; Nawada; Jehanabad", "Bihar", 24.79, 85.00, "Bodh Gayā lies here; zamindari of the mahants 'have now lapsed' (1957). A Śṛṅgeri maṭh building at Gaya (Mysore files, 1940s)."),
    ("Shahabad", "Arrah", "Bhojpur, Buxar, Rohtas, Kaimur", "Bhojpur; Buxar; Rohtas; Kaimur", "Bihar", 25.56, 84.66, "3,454 Atīths (1872), 7,246 (1901); 436 trusts by 1963."),
    ("Saran", "Chapra", "Saran (Chhapra)", "Saran; Siwan; Gopalganj", "Bihar", 25.78, 84.73, "Largest Daśanāmī circle on the map: 18,612 Atīths (1872), 26,753 (1901); absent from the revised volume."),
    ("Champaran", "", "East and West Champaran", "East Champaran; West Champaran", "Bihar", 26.65, 84.92, "6,063 Atīths (1872), 9,768 (1901)."),
    ("Muzaffarpur", "", "Muzaffarpur", "Muzaffarpur; Vaishali; Sitamarhi", "Bihar", 26.12, 85.39, ""),
    ("Darbhanga", "", "Darbhanga", "Darbhanga; Madhubani; Samastipur", "Bihar", 26.15, 85.90, ""),
    ("Monghyr", "Munger", "Munger", "Munger; Begusarai; Khagaria; Lakhisarai; Jamui", "Bihar", 25.38, 86.47, "Mahants of Dularpur and Suja; 1,780 in 'religious services' (1951)."),
    ("Bhagalpur", "", "Bhagalpur", "Bhagalpur; Banka", "Bihar", 25.25, 87.01, "Sultanganj convent of Sannyāsīs."),
    ("Malda", "Maldah", "Malda", "Malda", "West Bengal", 25.00, 88.14, ""),
    ("Hazaribagh", "", "Hazaribagh", "Hazaribagh and neighbours", "Jharkhand", 23.99, 85.36, ""),
    ("Ranchi", "", "Ranchi", "Ranchi and neighbours", "Jharkhand", 23.34, 85.31, ""),
    ("Palamau", "Palamu; Daltonganj", "Palamu (Medininagar HQ)", "Palamu; Garhwa; Latehar", "Jharkhand", 24.04, 84.07, "Athiths still described in the revised volume."),
    ("Singhbhum", "Chaibasa", "Singhbhum", "West and East Singhbhum; Seraikela-Kharsawan", "Jharkhand", 22.55, 85.81, ""),
    ("Hill Tippera", "Tippera", "Tripura", "Tripura", "Tripura", 23.84, 91.28, "Princely state."),
    ("Hooghly", "Hugli", "Hooghly", "Hooghly", "West Bengal", 22.90, 88.39, "Tārakeśvar lies here."),
    ("Howrah", "Haora", "Howrah", "Howrah", "West Bengal", 22.59, 88.31, "Bhot-Bagān, 'the seat of the Dasanami sect in the district'; a 'Sankar Math' at Ramrajatala (1919)."),
    ("Puri", "Purushottama Puri; Jagannath Puri; Pooree", "Puri", "Puri", "Odisha", 19.81, 85.83, "Govardhana maṭha: absent in Hunter (1877), 'the Sankaracharya' maṭh in 1908, named Gobardhana in 1977. Rivals: the 70-odd maṭhs of Purī are mostly Vaiṣṇava foundations (Emār, Rāghavadāsa and others)."),
    ("Cuttack", "Katak", "Cuttack", "Cuttack", "Odisha", 20.46, 85.88, ""),
    ("Balasore", "Baleshwar", "Balasore", "Balasore", "Odisha", 21.49, 86.93, ""),
]:
    add(name, var, modern, dist, state, la, lo, "district", G, note, "bengal/; census-images/")

# ---------------- Punjab ----------------
J = "Punjab"
for name, var, modern, dist, state, la, lo, note in [
    ("Hissar", "Hisar", "Hisar", "Hisar; Fatehabad; Sirsa; Bhiwani", "Haryana", 29.15, 75.72, "Puri guru at Kharak, Giri guru at Bilak; 1,479 Gusains (1881), 2,318 Gosains (1891)."),
    ("Rohtak", "", "Rohtak", "Rohtak; Jhajjar", "Haryana", 28.90, 76.61, ""),
    ("Gurgaon", "", "Gurugram", "Gurugram; Nuh; Rewari", "Haryana", 28.46, 77.03, ""),
    ("Delhi", "Dehli", "Delhi", "Delhi", "Delhi", 28.65, 77.23, ""),
    ("Karnal", "", "Karnal", "Karnal; Kurukshetra; Kaithal; Panipat", "Haryana", 29.69, 76.99, "Gosain pujaris of Shiva temples; later 'Jogis … of the Kanphara clan'. Rivals: Nāth Jogīs replace the Gosāin temple priests."),
    ("Ambala", "Umballa", "Ambala", "Ambala; Yamunanagar; Rupnagar", "Haryana / Punjab", 30.38, 76.78, ""),
    ("Simla", "", "Shimla", "Shimla", "Himachal Pradesh", 31.10, 77.17, ""),
    ("Kangra", "", "Kangra", "Kangra; Kullu; Lahaul and Spiti; Hamirpur", "Himachal Pradesh", 32.10, 76.27, "Kangra Gosāin traders and lenders."),
    ("Hoshiarpur", "", "Hoshiarpur", "Hoshiarpur; Una", "Punjab / Himachal Pradesh", 31.53, 75.91, ""),
    ("Jalandhar", "Jullundur", "Jalandhar", "Jalandhar; Kapurthala; Nawanshahr", "Punjab", 31.33, 75.58, ""),
    ("Ludhiana", "", "Ludhiana", "Ludhiana", "Punjab", 30.90, 75.85, ""),
    ("Firozpur", "Ferozepore", "Firozpur", "Firozpur; Moga; Fazilka", "Punjab", 30.93, 74.61, ""),
    ("Multan", "", "Multan", "Multan", "Pakistan (Punjab)", 30.20, 71.47, ""),
    ("Jhang", "", "Jhang", "Jhang", "Pakistan (Punjab)", 31.27, 72.32, ""),
    ("Montgomery", "", "Sahiwal", "Sahiwal", "Pakistan (Punjab)", 30.66, 73.11, ""),
    ("Lahore", "", "Lahore", "Lahore", "Pakistan (Punjab)", 31.55, 74.34, ""),
    ("Amritsar", "", "Amritsar", "Amritsar; Tarn Taran", "Punjab", 31.63, 74.87, ""),
    ("Gurdaspur", "", "Gurdaspur", "Gurdaspur; Pathankot", "Punjab", 32.04, 75.40, ""),
    ("Sialkot", "", "Sialkot", "Sialkot", "Pakistan (Punjab)", 32.49, 74.53, ""),
    ("Gujrat", "", "Gujrat", "Gujrat", "Pakistan (Punjab)", 32.57, 74.08, ""),
    ("Gujranwala", "", "Gujranwala", "Gujranwala", "Pakistan (Punjab)", 32.16, 74.19, ""),
    ("Shahpur", "", "Sargodha", "Sargodha; Khushab", "Pakistan (Punjab)", 32.27, 72.47, ""),
    ("Jhelum", "", "Jhelum", "Jhelum; Chakwal", "Pakistan (Punjab)", 32.93, 73.73, ""),
    ("Rawalpindi", "", "Rawalpindi", "Rawalpindi; Attock", "Pakistan (Punjab)", 33.60, 73.05, ""),
    ("Hazara", "Abbottabad", "Hazara (Abbottabad)", "Abbottabad; Mansehra; Haripur", "Pakistan (Khyber Pakhtunkhwa)", 34.15, 73.21, ""),
    ("Peshawar", "", "Peshawar", "Peshawar", "Pakistan (Khyber Pakhtunkhwa)", 34.01, 71.58, ""),
    ("Kohat", "", "Kohat", "Kohat", "Pakistan (Khyber Pakhtunkhwa)", 33.59, 71.44, ""),
    ("Bannu", "", "Bannu", "Bannu", "Pakistan (Khyber Pakhtunkhwa)", 32.99, 70.60, ""),
    ("Dera Ismail Khan", "", "Dera Ismail Khan", "Dera Ismail Khan", "Pakistan (Khyber Pakhtunkhwa)", 31.83, 70.90, ""),
    ("Dera Ghazi Khan", "", "Dera Ghazi Khan", "Dera Ghazi Khan", "Pakistan (Punjab)", 30.05, 70.63, ""),
    ("Muzaffargarh", "", "Muzaffargarh", "Muzaffargarh", "Pakistan (Punjab)", 30.07, 71.19, ""),
]:
    add(name, var, modern, dist, state, la, lo, "district", J, note, "punjab/; census-images/")

# ---------------- Central Provinces and Berar ----------------
C = "CP"
for name, var, modern, dist, state, la, lo, note in [
    ("Saugor", "Sagar", "Sagar", "Sagar", "Madhya Pradesh", 23.84, 78.74, ""),
    ("Damoh", "", "Damoh", "Damoh", "Madhya Pradesh", 23.83, 79.44, ""),
    ("Jubbulpore", "Jabalpur", "Jabalpur", "Jabalpur; Katni", "Madhya Pradesh", 23.18, 79.95, "Bheraghat, held by Puri Gosāin mahants under a Bhonsla grant; 2,080 Gosāins (1891)."),
    ("Mandla", "", "Mandla", "Mandla; Dindori", "Madhya Pradesh", 22.60, 80.37, ""),
    ("Seoni", "", "Seoni", "Seoni", "Madhya Pradesh", 22.09, 79.55, ""),
    ("Narsinghpur", "", "Narsinghpur", "Narsinghpur", "Madhya Pradesh", 22.95, 79.19, "Sankal: a village said to take its name from Śaṅkara's stay."),
    ("Hoshangabad", "", "Narmadapuram (renamed 2022)", "Narmadapuram; Harda", "Madhya Pradesh", 22.75, 77.72, ""),
    ("Nimar", "", "Khandwa (East Nimar)", "Khandwa; Burhanpur", "Madhya Pradesh", 21.82, 76.35, ""),
    ("Betul", "", "Betul", "Betul", "Madhya Pradesh", 21.90, 77.90, ""),
    ("Chhindwara", "", "Chhindwara", "Chhindwara", "Madhya Pradesh", 22.06, 78.94, ""),
    ("Wardha", "", "Wardha", "Wardha", "Maharashtra", 20.74, 78.60, "The Śṛṅgeri Śaṅkarācārya visited Nagpur c. 1903–04 (Wardha 1906)."),
    ("Nagpur", "", "Nagpur", "Nagpur", "Maharashtra", 21.15, 79.09, "Gosāins held 50–70 villages; 2,914 Gosāins (1891)."),
    ("Chanda", "", "Chandrapur", "Chandrapur; Gadchiroli", "Maharashtra", 19.96, 79.30, ""),
    ("Bhandara", "", "Bhandara", "Bhandara; Gondia", "Maharashtra", 21.17, 79.65, ""),
    ("Balaghat", "", "Balaghat", "Balaghat", "Madhya Pradesh", 21.80, 80.18, ""),
    ("Raipur", "", "Raipur", "Raipur and neighbours", "Chhattisgarh", 21.25, 81.63, "Dharampuri estate (40 villages by 1909); Deopur Nāgā Gosāins; 3,194 Gosāins (1891)."),
    ("Bilaspur", "", "Bilaspur", "Bilaspur and neighbours", "Chhattisgarh", 22.08, 82.15, ""),
    ("Sambalpur", "", "Sambalpur", "Sambalpur and neighbours", "Odisha", 21.47, 83.97, ""),
    ("Bastar", "Jagdalpur", "Bastar", "Bastar and neighbours", "Chhattisgarh", 19.08, 82.02, "Feudatory state."),
    ("Kanker", "", "Kanker", "Kanker", "Chhattisgarh", 20.27, 81.49, "Feudatory state."),
    ("Nandgaon", "", "Rajnandgaon", "Rajnandgaon", "Chhattisgarh", 21.10, 81.03, "Feudatory state."),
    ("Khairagarh", "", "Khairagarh", "Khairagarh-Chhuikhadan-Gandai", "Chhattisgarh", 21.42, 80.98, "Feudatory state."),
    ("Chhuikhadan", "", "Chhuikhadan", "Khairagarh-Chhuikhadan-Gandai", "Chhattisgarh", 21.52, 80.99, "Feudatory state."),
    ("Kawardha", "", "Kabirdham (Kawardha)", "Kabirdham", "Chhattisgarh", 22.01, 81.23, "Feudatory state."),
    ("Sakti", "", "Sakti", "Sakti", "Chhattisgarh", 22.03, 82.96, "Feudatory state."),
    ("Raigarh", "", "Raigarh", "Raigarh", "Chhattisgarh", 21.90, 83.40, "Feudatory state."),
    ("Sarangarh", "", "Sarangarh", "Sarangarh-Bilaigarh", "Chhattisgarh", 21.59, 83.08, "Feudatory state."),
    ("Bamra", "Deogarh", "Deogarh", "Deogarh", "Odisha", 21.62, 84.20, "Feudatory state."),
    ("Rairakhol", "", "Rairakhol", "Sambalpur", "Odisha", 21.07, 84.38, "Feudatory state."),
    ("Sonpur", "", "Subarnapur (Sonepur)", "Subarnapur", "Odisha", 20.84, 83.92, "Feudatory state."),
    ("Kalahandi", "", "Kalahandi", "Kalahandi", "Odisha", 19.91, 83.17, "Feudatory state."),
    ("Makrai", "", "Makrai (Harda)", "Harda", "Madhya Pradesh", 22.07, 77.10, "Feudatory state."),
    ("Akola", "", "Akola", "Akola; Washim", "Maharashtra", 20.70, 77.00, "Berar: village priests 'more frequently Gosains than Brahmans'; a Brahman 'shankaracharya' office at Basim."),
    ("Amraoti", "Amravati", "Amravati", "Amravati", "Maharashtra", 20.93, 77.75, "Berar."),
]:
    add(name, var, modern, dist, state, la, lo, "district", C, note, "cp/; census-images/")

# ---------------- Maṭha places (seats, branches, other sites) ----------------
add("Śṛṅgeri", "Sringeri; Shringeri; Sringéri; Srngeri; Sringagiri; Sringa-giri; Rishya-Sringa-giri; Sringiri; Shringori", "Sringeri", "Chikkamagaluru", "Karnataka", 13.42, 75.25, "seat", "Mysore",
    "Seat of the Jagadguru, 'proprietor of the surrounding tract'; jāgīr of about 9,144 people granted 1346; revenue c. Rs 50,000 plus Rs 1,000 a month from Mysore (Rice 1876, 1897). Located in no Bombay or Madras Places chapter. Rivals: Liṅgāyats (Kanara's Konkan Kuṇbīs left 'the Lingayat guide of Chitaldurg' for Śṛṅgeri in 1881; Bellary procession dispute 1888; Liṅgāyat conches allowed in Śṛṅgeri's processions); Mādhvas (Uḍupi; Uttarādi and Ahobila complaints 1906–07; Srirangapatna 1895; Vyāsarāja's claim to equal honours 1931); the Havig gurus (Svarṇavallī, Rāmacandrapura); and the seats that separated from it, Saṅkeśvar and Kudli, which held the Bombay Karnatak estates.", "sringeri/; mathas/")
add("Saṅkeśvar", "Sankeshvar; Sankeshwar; Sankesvar; Shankeshvar; Sankeswar", "Sankeshwar", "Belagavi", "Karnataka", 16.27, 74.48, "seat", "Bombay",
    "Seat of the Saṅkeśvar Svāmī: 30 inām villages in seven jurisdictions, Rs 30,000 a year; told as a secession from Śṛṅgeri c. 1570 (Belgaum 1884, pp. 600–02). Its villages lie mainly in Kolhapur, Belgaum and the Maratha states; those of its neighbour Kudli (Kudalgi), the first maṭh of its origin story, lie mainly in Dharwar and Bijapur (30 taluks and states in the 1934 list; 'Kudli estates' filter). A Bombay officer (1896) recommended exempting the Kudalgi Svāmī from the Arms Act like his 'brother Swami of Sankeshwar … in no way superior in position'.", "mathas/; mathas/archives/")
add("Kudli", "Kudali; Kūḍali; Kudalgi; Kudli Sringeri Matt; Uddughatti Mutt", "Kudli (Koodli)", "Shivamogga", "Karnataka", 14.00, 75.68, "seat", "Mysore",
    "Confluence of the Tunga and Bhadra. A Smārta maṭh whose guru was appointed by Śṛṅgeri (Rice) or founded by the Saṅkeśvar secessionist (Belgaum). Mysore files: 'a separate branch … at the Partition of A. D. 1656-57'; income Rs 35,047 (1933), of which villages and lands outside Mysore brought Rs 16,798 and those inside Rs 5,594. Estates (Agent's list, March 1934): Dharwar (Ranibennur, Karajgi, Hangal, Kod, Shiggaon, Navalgund, Kalghatgi, Dharwar, Hubli, Ron, Gadag); Bijapur (Badami, Bagalkot, Bagevadi, Bijapur, Sindgi, Hungund); Belgaum (Parasgad); North Kanara (Mundgod); Bellary (Kudligi, Harapanahalli); Anantapur (Madakasira); Kolhapur (Torgal), Ramdurg, Sangli (Shirahatti), Miraj Senior (Lakshmeshwar), Miraj Junior (Gudageri), Savanur, Sirasangi, Jamkhandi (Kundgol). Bombay levied nazarana on the Dharwar and Bijapur ināms (Rs 2,745 and Rs 1,167, 1936) and calls the maṭh 'Kudalgi' or the 'Uddughatti Mutt'. Use the 'Kudli estates' filter to see them. Also a Mādhva maṭh (Akṣobhya Tīrtha).", "mathas/; sringeri/; mathas/archives/")
add("Dvārkā", "Dwarka; Dwarika; Dwárka; Sharada Pith; Shārada Pīth", "Dwarka", "Devbhumi Dwarka", "Gujarat", 22.24, 68.97, "seat", "Bombay",
    "'Shārada Pīth … endowed by the Gaekwar of Baroda, who sanctions the appointment of every new pontiff' (Gujarat 1901, p. 542).", "mathas/")
add("Jyotirmaṭh", "Joshimath; Jyotir-math; Jotirmath; Jyotirdham", "Jyotirmath (Joshimath)", "Chamoli", "Uttarakhand", 30.56, 79.56, "seat", "UP",
    "Named in lists of the four maṭhs; 'established the Joshimath monastery' (Garhwal 1910). Place entries describe only the Badrinath Rawal's winter seat.", "mathas/")
add("Badrinath", "Badrinath; Badri", "Badrinath", "Chamoli", "Uttarakhand", 30.74, 79.49, "site", "UP",
    "Temple 'said to have been erected … by Sankara Acharya'; Nambūri Rawal from Malabar; estates of 164 villages and parts of 111 (1910).", "mathas/")
add("Kumbakoṇam", "Kumbakonam; Kumbakōnam; Combaconum; Kumbhakonam", "Kumbakonam", "Thanjavur", "Tamil Nadu", 10.96, 79.38, "seat", "Madras",
    "'the math of Sankaracharya', income nearly Rs 14,000, appoints the managers of three temples incl. one at Conjeeveram (Tanjore 1906). Catalogued as 'Kanchi Komakoti matt at Kumbakonam' in 1925.", "madras/; mathas/")
add("Kāñcī", "Conjeeveram; Conjeveram; Conjeevaram; Kanchi; Kanchipuram", "Kanchipuram", "Kanchipuram", "Tamil Nadu", 12.83, 79.70, "branch", "Madras",
    "Where Śaṅkara 'founded a matam' (Crole 1879, p. 26); a temple managed from Kumbakoṇam (1906); the maṭh is 'of Conjeevaram' by 1936.", "madras/; mathas/")
add("Purī (Govardhana maṭha)", "Gobardhana; Govardhana; Bhog Gobardhan; Vardhana-math", "Govardhan Math, Puri", "Puri", "Odisha", 19.80, 85.85, "seat", "Bengal",
    "Absent in 1877; 'the Sankaracharya' maṭh with c. 1,200 MSS (1908); 'Gobardhana Matha … still extant' (1977). A Kāñcī Kāmakoṭi ashram founded at Purī in 1973.", "mathas/; revised/")
add("Śivagaṅgā", "Sivaganga; Shivaganga; Dakshina Kasi", "Shivagange", "Bengaluru Rural (Nelamangala)", "Karnataka", 13.17, 77.22, "seat", "Mysore",
    "Maṭh in financial difficulty, endowments under Muzrai management at the guru's wish (Rice 1897); funds lent for the Śṛṅgeri Jagadguru's visit (1927).", "mathas/")
add("Avani", "Avani Sringeri Mutt", "Avani", "Kolar (Mulbagal taluk)", "Karnataka", 13.10, 78.33, "branch", "Mysore",
    "'A guru of the Smarta sect resides here' (Rice 1876, 1897); a Śaṅkarācārya temple with a State grant (1930); 'Avani Sringeri Mutt' (1933).", "mathas/")
add("Hampi", "Virupaksha; Virūpākṣa; Pampa; Pampapati; Hampi Samsthanam", "Hampi", "Vijayanagara", "Karnataka", 15.335, 76.46, "branch", "Madras",
    "Sri Sankaracharya Virupaksha Samsthanam: its Svāmī calls it 'a branch of Sri Sringeri Mutt', papers 'left behind in the Nizam's Dominions' (Mysore file, 1935–36). No maṭh in the Bellary volumes.", "mathas/")
add("Puṣpagiri", "Pushpagiri; Puspagiri", "Pushpagiri", "YSR Kadapa", "Andhra Pradesh", 14.54, 78.77, "site", "Madras",
    "Temple hill and hamlet of Kotlur in the Cuddapah volumes; no maṭh described, and no archival file found.", "mathas/")
add("Khidrapur", "Khidrápur", "Khidrapur", "Kolhapur", "Maharashtra", 16.63, 74.70, "branch", "Bombay",
    "'an alienated village belonging to Sankeshvar Svami' (Kolhapur 1886, p. 302).", "mathas/")
add("Hallur", "", "Hallur", "Haveri", "Karnataka", 14.87, 75.68, "branch", "Bombay",
    "Rangnath temple rebuilt by the Kudalgi Svāmī, who was granted the village (Dharwar 1884, p. 722).", "mathas/")
add("Hubli", "Hubballi; Hubli Sringeri Matt", "Hubballi", "Dharwad", "Karnataka", 15.36, 75.12, "branch", "Bombay",
    "Kudalgi Svāmī's crosswise-palkhi privilege upheld up to the Privy Council (Dharwar 1884, p. 757); Hubli taluk is in the Kudli maṭh's 1934 property list. (The 1923 'Hubli Sringeri Matt' file is really about Kudli.)", "mathas/; mathas/archives/")
add("Nirmal", "Nirmal (Bassein)", "Nirmal", "Palghar (Vasai)", "Maharashtra", 19.40, 72.80, "site", "Bombay",
    "Reputed samādhi of a Śaṅkarācārya; temple of Shankaracharya Svāmī built after 1739, Government grant Rs 421 (Thana 1882).", "mathas/")
add("Sonda", "Sonda; Sunda; Swadi; Svarnavalli; Honalli Math", "Sonda (Swarnavalli)", "Uttara Kannada (Sirsi)", "Karnataka", 14.72, 74.82, "site", "Bombay",
    "Honalli (Svarṇavallī) Smārta maṭh, seat of the Havig Brahmans' guru: a separate line, not a Śṛṅgeri branch (Kanara 1883).", "sringeri/; mathas/")
add("Bodh Gayā", "Bodh Gaya; Buddh Gaya; Budh Gaya", "Bodh Gaya", "Gaya", "Bihar", 24.70, 84.99, "site", "Bengal",
    "Giri maṭh, 'one of the seven Saivite orders established by Sankara Acharya' (Gaya 1906); Mahabodhi dispute.", "bengal/; mathas/")
add("Tārakeśvar", "Tarakeswar; Tarakeshwar", "Tarakeswar", "Hooghly", "West Bengal", 22.89, 88.02, "site", "Bengal",
    "Mahant 'a celibate of the Dasnami order'; a public endowment after 1924; 'governed by the Sankaracharya school of thought' (1972).", "bengal/; revised/; mathas/")
add("Bhot-Bagān", "Bhot Bagan; Ghusuri", "Bhot Bagan (Ghusuri)", "Howrah", "West Bengal", 22.61, 88.35, "site", "Bengal",
    "Tashi Lama's grant to Puran Gir Gosāin (1785); mahant elected 'by the other Dasnami Mahants of Bengal' (1905).", "bengal/; revised/")
add("Hardwar", "Haridwar; Kankhal", "Haridwar", "Haridwar", "Uttarakhand", 29.95, 78.16, "site", "UP",
    "Kumbh melā; Kankhal Gosāins (Bhola Gir, 4,024 acres); a Śṛṅgeri maṭh building at Haridwar (Mysore file, 1944). Rivals: the Gosāin–Bairāgī battle at Hardwar, 1760; precedence among Daśanāmī, Bairāgī and Udāsī akhāṛās at the Kumbh.", "north/; revised/; mathas/")
add("Bodhan", "", "Bodhan", "Nizamabad", "Telangana", 18.66, 77.88, "site", "Hyderabad",
    "One of four monasteries of Bhāskarācārya, the Komaṭis' 'deputy of Shankaracharya' (Sholapur 1884).", "mathas/")
add("Nander", "Nanded", "Nanded", "Nanded", "Maharashtra", 19.15, 77.31, "site", "Hyderabad",
    "Another of Bhāskarācārya's monasteries (Sholapur 1884).", "mathas/")
add("Khanapur", "", "Khanapur", "Belagavi", "Karnataka", 15.64, 74.51, "site", "Bombay",
    "'The Smart svami has a monastery at Khanapur', with two villages: the Shenvi Smārta svāmī (Belgaum 1884, p. 91).", "mathas/")
add("Kollur", "", "Kollur", "Udupi", "Karnataka", 13.86, 74.81, "site", "Madras",
    "Mūkāmbikā temple; image said to have been consecrated by Śaṅkara (South Kanara 1973).", "sringeri/")
add("Karkal", "Karkala", "Karkala", "Udupi", "Karnataka", 13.21, 74.99, "site", "Madras",
    "An image 'installed at Karkal by Shree Jagadguru Narasimha Bharati Swamiji of Sringeri Matha' (1973).", "sringeri/")
add("Kaladi", "Kalady; Kallady", "Kalady", "Ernakulam", "Kerala", 10.17, 76.44, "site", "Other",
    "Śaṅkara's birthplace (Atkinson spells it 'Kallady'); the Śṛṅgeri Jagadguru's escort from Mysore to Kaladi (1923).", "mathas/")
add("Rāmeśvaram", "Rameswaram; Rameshvar", "Rameswaram", "Ramanathapuram", "Tamil Nadu", 9.29, 79.31, "branch", "Madras",
    "A Śṛṅgeri branch maṭh, named in a 1935 Mysore file on legacies.", "mathas/")
add("Tirupati", "", "Tirupati", "Tirupati", "Andhra Pradesh", 13.63, 79.42, "branch", "Madras",
    "Śṛṅgeri maṭh branch at Tirupati, managed by committees (1940).", "mathas/")
add("Bangalore (Sultanpet)", "Bangalore; Bengaluru; Sultanpet", "Bengaluru", "Bengaluru Urban", "Karnataka", 12.97, 77.58, "branch", "Mysore",
    "'Sringeri Matt, Sultanpet, Bangalore city' (1923); the Jagadguru's processions in the city (1907).", "mathas/")
add("Mysore", "Mysuru", "Mysuru", "Mysuru", "Karnataka", 12.30, 76.64, "site", "Mysore",
    "Capital of the princely state whose Muzrai files record the Śṛṅgeri and Kudli maṭhs.", "mathas/")
add("Sangli", "", "Sangli", "Sangli", "Maharashtra", 16.85, 74.58, "branch", "Bombay",
    "Kudli Śṛṅgeri maṭh properties in Sangli State (1935).", "mathas/")
add("Hole Narsipur", "Holenarasipura", "Holenarasipura", "Hassan", "Karnataka", 12.79, 76.24, "site", "Mysore",
    "The Śṛṅgeri Svāmī's visits (1892) and an adda-palakki dispute in front of the Uttarādi maṭh (1906).", "mathas/")
add("Srirangapatna", "Seringapatam; Srirangapatam", "Srirangapatna", "Mandya", "Karnataka", 12.42, 76.68, "site", "Mysore",
    "Visits of the Śṛṅgeri Svāmī to the Ranganātha temple (1894–95, 1907).", "mathas/")
add("Nanjangud", "", "Nanjangud", "Mysuru", "Karnataka", 12.12, 76.68, "site", "Mysore",
    "The Śṛṅgeri Jagadguru's endowments to the Śrīkaṇṭheśvara temple (1892, 1907).", "mathas/")
add("Kigga", "", "Kigga", "Chikkamagaluru", "Karnataka", 13.46, 75.21, "site", "Mysore",
    "Ṛṣyaśṛṅga temple, in the Śṛṅgeri jāgīr.", "mathas/")
add("Belavadi", "Belvadi", "Belavadi", "Chikkamagaluru", "Karnataka", 13.27, 75.84, "branch", "Mysore",
    "An inām village of the Śṛṅgeri maṭh (tank, quarry, land disposals 1902–40).", "mathas/")
add("Ayodhyā", "Ajodhya; Oudh", "Ayodhya", "Ayodhya", "Uttar Pradesh", 26.80, 82.20, "site", "UP",
    "Dominated by the Bairāgī akhāṛās; the Gosāins appear only in the story of their expulsion from Hanumāngaṛhī. The Rāmānandī Bairāgīs were the Daśanāmīs' direct rival in the north.", "north/; revised/")
add("Gokarn", "Gokarna", "Gokarna", "Uttara Kannada", "Karnataka", 14.55, 74.32, "site", "Bombay",
    "Pilgrimage centre of Kanara castes; earlier seat of the Havig gurus' line before Sonda.", "results/; mathas/")

add("Udagatti", "Uddughatti; Uddughatti Mutt", "Udagatti", "Haveri (Ranibennur taluk)", "Karnataka", 14.55, 75.70, "branch", "Bombay",
    "Where the Kudli svāmīs lived in the Bombay country; Bombay records call the maṭh 'Kudalgi' or the 'Uddughatti Mutt' (Mysore files, 1936).", "mathas/archives/")
add("Tīrthamuttūr", "Tirthamuthur; Tirtha muthur Mutt", "Tirthamuttur", "Shivamogga (Tirthahalli taluk)", "Karnataka", 13.70, 75.24, "branch", "Mysore",
    "'a vassal Mutt to the Sringeri Mutt, paying an annual subsidy of Rs 31-4-0'; its svāmīs consecrated at Śṛṅgeri (1923).", "mathas/archives/")

# Kudli Śṛṅgeri maṭh: properties outside Mysore, from its Agent's list of March 1934 (mathas/archives, K32).
# Taluks already present as districts or branches (Dharwar, Hubli, Bijapur, Kolhapur) carry the fact in their notes.
add('Ranibennur', 'Ranebennur', 'Ranebennuru', 'Haveri', 'Karnataka', 14.62, 75.62, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Karajgi', 'Karajagi', 'Karajagi', 'Haveri', 'Karnataka', 14.86, 75.45, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Hangal', 'Hanagallu; Hanagal', 'Hanagal', 'Haveri', 'Karnataka', 14.76, 75.12, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Kod', 'Hirekerur', 'Hirekerur (Kod taluk)', 'Haveri', 'Karnataka', 14.46, 75.39, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Shiggaon', 'Siggavi', 'Shiggaon', 'Haveri', 'Karnataka', 14.99, 75.22, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Navalgund', 'Navalgunda', 'Navalgund', 'Dharwad', 'Karnataka', 15.56, 75.37, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Kalghatgi', 'Kalaghatagi', 'Kalghatgi', 'Dharwad', 'Karnataka', 15.18, 74.97, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Ron', 'Rona', 'Ron', 'Gadag', 'Karnataka', 15.7, 75.73, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Gadag', '', 'Gadag-Betageri', 'Gadag', 'Karnataka', 15.43, 75.63, "estate", "Bombay" if 'Dharwar District'.find("Bellary")<0 and 'Dharwar District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Dharwar District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Mundgod', '', 'Mundgod', 'Uttara Kannada', 'Karnataka', 14.97, 75.04, "estate", "Bombay" if 'North Kanara'.find("Bellary")<0 and 'North Kanara'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (North Kanara), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Parasgad', 'Saundatti', 'Saundatti (Parasgad taluk)', 'Belagavi', 'Karnataka', 15.77, 75.12, "estate", "Bombay" if 'Belgaum District'.find("Bellary")<0 and 'Belgaum District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Belgaum District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Badami', '', 'Badami', 'Bagalkot', 'Karnataka', 15.92, 75.68, "estate", "Bombay" if 'Bijapur District'.find("Bellary")<0 and 'Bijapur District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bijapur District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Bagalkot', '', 'Bagalkote', 'Bagalkot', 'Karnataka', 16.18, 75.7, "estate", "Bombay" if 'Bijapur District'.find("Bellary")<0 and 'Bijapur District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bijapur District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Bagevadi', 'Basavana Bagevadi', 'Basavana Bagewadi', 'Vijayapura', 'Karnataka', 16.57, 75.97, "estate", "Bombay" if 'Bijapur District'.find("Bellary")<0 and 'Bijapur District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bijapur District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Sindgi', '', 'Sindagi', 'Vijayapura', 'Karnataka', 16.92, 76.23, "estate", "Bombay" if 'Bijapur District'.find("Bellary")<0 and 'Bijapur District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bijapur District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Hungund', '', 'Hungund', 'Bagalkot', 'Karnataka', 16.06, 76.06, "estate", "Bombay" if 'Bijapur District'.find("Bellary")<0 and 'Bijapur District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bijapur District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Kudligi', '', 'Kudligi', 'Vijayanagara', 'Karnataka', 14.9, 76.38, "estate", "Bombay" if 'Bellary District'.find("Bellary")<0 and 'Bellary District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bellary District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Harapanahalli', '', 'Harapanahalli', 'Vijayanagara', 'Karnataka', 14.79, 75.99, "estate", "Bombay" if 'Bellary District'.find("Bellary")<0 and 'Bellary District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Bellary District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Madakasira', '', 'Madakasira', 'Sri Sathya Sai', 'Andhra Pradesh', 13.94, 77.27, "estate", "Bombay" if 'Anantapur District'.find("Bellary")<0 and 'Anantapur District'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Anantapur District), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Torgal', 'Thoragallu; Kankanvadi', 'Torgal', 'Belagavi', 'Karnataka', 15.97, 75.16, "estate", "Bombay" if 'Kolhapur State'.find("Bellary")<0 and 'Kolhapur State'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Kolhapur State), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Ramdurg', '', 'Ramdurg', 'Belagavi', 'Karnataka', 15.95, 75.3, "estate", "Bombay" if 'Ramdurg State'.find("Bellary")<0 and 'Ramdurg State'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Ramdurg State), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Shirahatti', 'Giddehosapura', 'Shirahatti', 'Gadag', 'Karnataka', 15.23, 75.58, "estate", "Bombay" if 'Sangli State; a village under attachment (1935)'.find("Bellary")<0 and 'Sangli State; a village under attachment (1935)'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Sangli State; a village under attachment (1935)), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Lakshmeshwar', '', 'Lakshmeshwar', 'Gadag', 'Karnataka', 15.13, 75.47, "estate", "Bombay" if 'Miraj Senior State'.find("Bellary")<0 and 'Miraj Senior State'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Miraj Senior State), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Gudageri', '', 'Gudageri', 'Dharwad', 'Karnataka', 15.12, 75.37, "estate", "Bombay" if 'Miraj Junior State'.find("Bellary")<0 and 'Miraj Junior State'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Miraj Junior State), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Savanur', '', 'Savanur', 'Haveri', 'Karnataka', 14.97, 75.33, "estate", "Bombay" if 'Savanur State'.find("Bellary")<0 and 'Savanur State'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Savanur State), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Sirasangi', '', 'Sirasangi', 'Belagavi', 'Karnataka', 15.68, 75.27, "estate", "Bombay" if 'Sirasangi jagir'.find("Bellary")<0 and 'Sirasangi jagir'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Sirasangi jagir), in the maṭh Agent's list of March 1934.", "mathas/archives/")
add('Kundgol', '', 'Kundgol', 'Dharwad', 'Karnataka', 15.26, 75.25, "estate", "Bombay" if 'Jamkhandi State'.find("Bellary")<0 and 'Jamkhandi State'.find("Anantapur")<0 else "Madras",
    "Taluk holding Kudli maṭh property (Jamkhandi State), in the maṭh Agent's list of March 1934.", "mathas/archives/")

add("Kālīghāṭ", "Kalighat", "Kalighat", "Kolkata", "West Bengal", 22.52, 88.34, "site", "Bengal",
    "Rival centre: the great Kālī pilgrimage of the Calcutta region (24 Parganas 1914).", "SYNTHESIS.md (Rivals)")
add("Khardah", "Khardaha", "Khardaha", "North 24 Parganas", "West Bengal", 22.72, 88.38, "site", "Bengal",
    "Rival centre: 'a favourite place of pilgrimage for Vaishnavas, as it was the home of Nityananda' (24 Parganas 1914).", "SYNTHESIS.md (Rivals)")
add("Dakshineswar", "Dakhineswar", "Dakshineswar", "North 24 Parganas", "West Bengal", 22.65, 88.36, "site", "Bengal",
    "Rani Rasmani's temples to Kālī and Kṛṣṇa with twelve Śiva shrines; the 1914 gazetteer does not mention Ramakrishna, whose order (Belur Math, 1898) took Daśanāmī sannyāsa.", "SYNTHESIS.md (Rivals)")
add("Uḍupi", "Udipi; Udupi", "Udupi", "Udupi", "Karnataka", 13.34, 74.75, "site", "Madras",
    "Rival centre: seat of the Mādhva maṭhs; Kanara and South Canara Vaiṣṇava Brahmans' guru is 'a Tulu Brahman, who lives in celibacy at the Vaishnav monastery at Udipi'.", "results/; madras/")

# ---------------- Rivals: notes appended to place entries (synthesis, "Rivals: who else held the ground") ----------------
_PUNJAB = "Rivals: in the Punjab the Jogīs, the Sikh-linked Udāsīs and the Bairāgīs dominate; Daśanāmīs are thin, none in the west (punjab/README.md)."
_GUJ = "Rivals: Gujarat is Vaiṣṇava (Vallabha, Svāminārāyaṇa); the Dvārkā Śaṅkarācārya is referee only for its 'Śaivas'."
_BENGAL = "Rivals: Bengal proper is a Vaiṣṇava landscape; Sannyāsīs number in the tens per district against tens of thousands of caste-rejecting Vaiṣṇavas (Hunter, 1872)."
RIVALS = {
    "Saṅkeśvar": "Rivals: a Saṅkeśvar nominee challenged Śṛṅgeri's accredited agent in Khandesh (1913, Mysore files).",
    "Kudli": "Rivals: Liṅgāyat objections were feared when its Svāmī was allowed the ambari (1931); a rival line of claimants was rejected 1875–1929; the Mādhva Akṣobhya Tīrtha maṭh stands in the same village.",
    "Hubli": "Rivals: the Liṅgāyat Mursavirad Svāmī imitated the Kudalgi Svāmī's crosswise palkhi; the dispute went up to the Privy Council (Dharwar 1884, p. 757).",
    "Dharwar": "Rivals: Liṅgāyat country; by 1959 the revised volume's maṭh landscape is Mādhva and Vīraśaiva.",
    "Bijapur": "Rivals: by 1966 the revised volume's maṭh landscape is Mādhva and Vīraśaiva.",
    "Mysore": "Rivals: the Ahobila maṭh complained of the Śṛṅgeri Svāmī passing in procession before it (1907).",
    "Hampi": "Rivals: put forward as a rival seat to Śṛṅgeri at the 1912 succession (Mysore files).",
    "Khandesh": "Rivals: Śṛṅgeri's accredited agent here was challenged by a nominee of Saṅkeśvar (1913, Mysore files).",
    "Kumbakoṇam": "Rivals: Tanjore's list of chief maṭhs (1906) names the non-Brahmin Śaiva maṭhs of Dharmapuram, Tiruvāvaḍuturai, Tiruppanandāl and Tiruppugalūr first; the Vaḍagalai Ahobila maṭh had moved to Narasimhapuram nearby (Thurston).",
    "Tanjore": "Rivals: the non-Brahmin Śaiva maṭhs (Dharmapuram, Tiruvāvaḍuturai) and the Śrīvaiṣṇavas.",
    "Chingleput": "Rivals: a Śrīvaiṣṇava stronghold (60% Aiyaṅgār among Brahmans, 1891).",
    "Madura": "Rivals: Aiyaṅgār Śrīvaiṣṇavas are 26% of Brahmans (1891).",
    "Purī (Govardhana maṭha)": "Rivals: the town's 70-odd maṭhs are mostly Vaiṣṇava foundations (Emār, Rāghavadāsa and others).",
    "Bodh Gayā": "Rivals: the Mahabodhi Society (Buddhist) contested the Mahant's possession of the temple; the High Court found for the Mahant (1906).",
    "Tārakeśvar": _BENGAL, "Bhot-Bagān": _BENGAL, "Hooghly": _BENGAL, "Howrah": _BENGAL,
    "Murshidabad": _BENGAL, "Rajshahi": _BENGAL, "Malda": _BENGAL, "Rangpur": _BENGAL, "Pabna": _BENGAL,
    "Dvārkā": "Rivals: in Vaiṣṇava Gujarat (Vallabha, Svāminārāyaṇa) its pontiff is referee only for the 'Śaivas'.",
    "Surat": _GUJ, "Broach": _GUJ, "Kaira": _GUJ, "Panch Mahals": _GUJ, "Ahmedabad": _GUJ, "Cutch": _GUJ, "Kathiawar": _GUJ,
    "Allahabad": "Rivals: Bairāgī and Udāsī akhāṛās beside the Daśanāmī ones at the Magh and Kumbh melās.",
    "Badrinath": "Rivals: its Rawal is a Nambūri from Malabar; Kedarnath and Ukhimath are described as a Jangama (Liṅgāyat) maṭh (Atkinson; Garhwal 1910).",
    "Garhwal": "Rivals: Kedarnath and Ukhimath are described as a Jangama (Liṅgāyat) maṭh under a Malabar Rawal (Atkinson; Garhwal 1910).",
    "Sonda": "Rivals: the Vaiṣṇava Terbidi (Vādirāja) maṭh stands beside the Svarṇavallī maṭh at Sonda (Kanara 1883).",
    "Uḍupi": "Rivals: South Canara's largest Tulu Brahman group, the Shivallis (28,660 in 1891), are Mādhva: 'the great bulk of the Tulu Brahmins' (Sturrock 1894).",
    "Kolhapur": "Rivals: the city's other large maṭh belongs to a Jain Svāmī, and the Jains claim the Ambābāī temple was once theirs (1886).",
    "Tirupati": "Rivals: the Tirumala Tirupati Devasthanams claim oversight of the Śṛṅgeri branch because they pay its allowances (1940).",
}
for _n in ["Hissar", "Rohtak", "Gurgaon", "Delhi", "Ambala", "Simla", "Kangra", "Hoshiarpur", "Jalandhar", "Ludhiana", "Firozpur",
           "Multan", "Jhang", "Montgomery", "Lahore", "Amritsar", "Gurdaspur", "Sialkot", "Gujrat", "Gujranwala", "Shahpur",
           "Jhelum", "Rawalpindi", "Hazara", "Peshawar", "Kohat", "Bannu", "Dera Ismail Khan", "Dera Ghazi Khan", "Muzaffargarh"]:
    RIVALS[_n] = _PUNJAB
_names = {p["name"] for p in P}
assert not set(RIVALS) - _names, set(RIVALS) - _names
for p in P:
    if p["name"] in RIVALS and "Rivals:" not in p["note"]:
        p["note"] = (p["note"] + " " + RIVALS[p["name"]]).strip()
        if "SYNTHESIS.md" not in p["refs"]:
            p["refs"] = (p["refs"] + "; SYNTHESIS.md (Rivals)").strip("; ")

# ---------------- Census counts of the Daśanāmīs and rival orders, by district (census-images/results/) ----------------
def _census_lines():
    import csv, os
    R = "census-images/results/"
    if not os.path.exists(R + "up1891_ascetics.tsv"):
        return {}
    n = lambda x: int(str(x).replace(",", "").strip() or 0) if str(x).replace(",", "").strip().isdigit() else 0
    f = lambda x: f"{x:,}"
    out = {}
    for r in csv.DictReader(open(R + "up1891_ascetics.tsv", encoding="utf-8"), delimiter="\t"):
        t = f"Census 1891: Daśanāmī {f(n(r['goshain_dasnami']))}"
        if n(r["goshain_unspecified"]): t += f" (+ {f(n(r['goshain_unspecified']))} unspecified Goshains)"
        out[r["district"]] = t + f"; Bairāgī {f(n(r['bairagi']))}; Jogī {f(n(r['jogi']))}."
    for r in csv.DictReader(open(R + "punjab1891_castes.tsv", encoding="utf-8"), delimiter="\t"):
        if r["district"].startswith("TOTAL"): continue
        out[r["district"]] = (f"Census 1891: Gosain {f(n(r['gosain_t']))}; Sanniasi {f(n(r['sanniasi_t']))}; Jogī-Rawal {f(n(r['jogi_rawal_t']))}; "
                              f"Bairāgī {f(n(r['bairagi_t']))}; Udāsī {f(n(r['udasi_t']))}.")
    for r in csv.DictReader(open(R + "cp1891_castes.tsv", encoding="utf-8"), delimiter="\t"):
        if r["sex"] != "persons" or r["district_or_state"].startswith("TOTAL"): continue
        out[r["district_or_state"]] = (f"Census 1891: Gosain {f(n(r['gosain']))}; Bairāgī {f(n(r['bairagi']))}; Jogī {f(n(r['jogi']))}; "
                                       f"Nāth {f(n(r['nath']))}.")
    for r in csv.DictReader(open(R + "madras1891_tamil_smarta_vs_aiyangar.tsv", encoding="utf-8"), delimiter="\t"):
        if r["district"].startswith(("#", "Division")): continue
        out[r["district"]] = (f"Census 1891, Brahmans: Smārta sub-castes {r['smarta_pct']}%; Aiyaṅgār (Śrīvaiṣṇava) {r['aiyangar_pct']}%; "
                              f"Mādhva {f(n(r['madhva']))}.")
    for r in csv.DictReader(open(R + "bengal1901_atith_gosain.tsv", encoding="utf-8"), delimiter="\t"):
        if r["district"] == "TOTAL": continue
        out[r["district"]] = f"Census 1901: Atīth {f(n(r['atith_total']))}; 'Gosain' {f(n(r['gosain_total']))} (a mixed column, largely Vaiṣṇava)."
    return out
_C = _census_lines()
_C["South Canara"] = ("Census 1891, Brahmans (95,739): Sarasvata 30,273 (split Smārta/Vaiṣṇava); Sivalli 28,660 (Mādhva); Havig 11,234 and Kota 11,017 "
                      "(Smārta, own gurus); Karāḍi 2,731, Konkanastha 3,200, Chitpāvan 1,491, Padia 154 (Smārta, under Śṛṅgeri: about 8% of Brahmans); "
                      "Kandavara 1,576; Saklapuri 463 (sringeri/README.md).")
for p in P:
    if "district" in p["kinds"] and p["name"] in _C and p["name"] != "Benares" and "Census 18" not in p["note"] and "Census 19" not in p["note"]:  # Benares: counts already in its rivals note
        p["note"] = (p["note"] + " " + _C[p["name"]]).strip()
        if "census-images/" not in p["refs"]:
            p["refs"] = (p["refs"] + "; census-images/").strip("; ")
        if p["name"] == "South Canara" and "sringeri/" not in p["refs"]:
            p["refs"] += "; sringeri/"

# ---------------- Rival seats and facts from the coded rivals layer (rivals/README.md) ----------------
add("Lormi", "", "Lormi", "Mungeli", "Chhattisgarh", 22.28, 81.70, "site", "CP",
    "Rival seat: a Bairāgī estate of 103–104 villages, a Bhonsla grant of 1826 that passed from the chela to his four sons (rivals N-coding).", "rivals/")
add("Tilla", "Tilla Jogian; Gorakh Tilla", "Tilla Jogian", "Jhelum", "Pakistan (Punjab)", 32.88, 73.36, "site", "Punjab",
    "Rival seat: the chief Nāth (Kānphaṭā) monastery of the Punjab, with Akbar's sanad for a jagir, resumed over a murder for the gaddī and later restored (rivals N-coding).", "rivals/")
add("Bohar", "", "Bohar", "Rohtak", "Haryana", 28.86, 76.65, "site", "Punjab",
    "Rival seat: a Kānphaṭā (Nāth) maṭh holding land; Rohtak's 299 asthals on 2,725 acres are half Bairāgī, with the Gosāins fourth (rivals N-coding).", "rivals/")
add("Dera Baba Nanak", "", "Dera Baba Nanak", "Gurdaspur", "Punjab", 32.03, 75.03, "site", "Punjab",
    "Rival seat: Udāsī institution with a jagir of Rs 2,602 (rivals N-coding).", "rivals/")
add("Tiruvāvaḍuturai", "Tiruvaduturai; Tiruvavaduturai", "Thiruvavaduthurai", "Mayiladuthurai", "Tamil Nadu", 11.03, 79.53, "site", "Madras",
    "Rival seat: non-Brahmin Śaiva ādhīnam, about 29,000 acres and Rs 2 lakhs a year, against about Rs 14,000 for the Kumbakoṇam Śaṅkara maṭh (Tanjore 1906; rivals S-coding).", "rivals/; mathas/")
add("Dharmapuram", "", "Dharmapuram", "Mayiladuthurai", "Tamil Nadu", 11.08, 79.65, "site", "Madras",
    "Rival seat: non-Brahmin Śaiva ādhīnam; head of the 'Sudra maths' listed first among Tanjore's chief maṭhs (1906), superior of Tiruppanandāḷ (Rs 80,000 a year).", "rivals/; mathas/")
add("Chitradurga", "Chitaldrug; Chitaldroog; Chitaldurg", "Chitradurga", "Chitradurga", "Karnataka", 14.23, 76.40, "site", "Mysore",
    "Rival seat: the Murugha maṭh, supreme guru of the Liṅgāyats; Kanara's 14,812 Konkan Kuṇbīs left 'the Lingayat guide of Chitaldurg' for Śṛṅgeri in 1881; the hill maṭh stood deserted owing to 'the opposition of other sects' (rivals S-coding).", "rivals/; sringeri/")
add("Vadtal", "Vartal; Wadtal", "Vadtal", "Kheda", "Gujarat", 22.60, 72.87, "site", "Bombay",
    "Rival seat: one of the two Svāminārāyaṇa seats; feeds 500–1,000 inmates and draws 20,000 pilgrims a festival; Svāminārāyaṇs 287,687 in 1901 (rivals S-coding).", "rivals/")
RIVALS2 = {
    "Nandgaon": "Rivals (coded): a Bairāgī Feudatory State of 560 villages, granted 1723; succession by adoption (Grant 1870) or primogeniture (Russell 1916).",
    "Kawardha": "Rivals (coded): seat of a Kabīrpanthī gaddī line claiming 500,000 followers; rival mahants litigated up to the Bombay High Court.",
    "Gonda": "Rivals (coded): the Nānakshāhī (Udāsī) taluqdar of Maswasi held 17,215 acres in the district.",
    "Ahmedabad": "Rivals (coded): in the city Svāminārāyaṇa sādhus (315) outnumber Gosāīs and Vairāgīs (261).",
    "Bilaspur": "Rivals (coded): Bairāgīs own 156 of the district's 2,242 villages; Kabīrpanthīs 99,260.",
    "Ayodhyā": "Rivals (coded): Hanumāngaṛhī's Nirbānī akhāṛā had 300–400 resident disciples (1877), 250 (1905), at most 200 (1960), but grew richer; the Gosāins' expulsion from it is told only in 1960.",
    "Purī (Govardhana maṭha)": "Rivals (coded): 29 Purī maṭhs drew Rs 1,45,400 a year from land in 1848; Śaṅkara-line houses are about 7 of some 130 in 1977.",
    "Calcutta": "Rivals (coded): the 1901 report counts 1,799 Brahmos (Jorasanko, Jorabagan, Moochipara) and 14,079 Baishnabs, with no Sannyāsī heading.",
    "Saharanpur": "Rivals (coded): at Kankhal Gokul Dās Udāsī held 3,199 acres against Bhola Gir Goshain's 4,024; the Bairāgīs lost the 1760 Hardwar battle with 1,800 dead.",
    "Dehra Dun": "Rivals (coded): the largest landholder is the Udāsī Guru Ram Rai temple (Dehra itself and five revenue-free villages).",
}
for p in P:
    if p["name"] in RIVALS2 and "Rivals (coded):" not in p["note"]:
        p["note"] = (p["note"] + " " + RIVALS2[p["name"]]).strip()
        if "rivals/" not in p["refs"]:
            p["refs"] = (p["refs"] + "; rivals/").strip("; ")

if __name__ == "__main__":
    import csv
    cols = ["name", "variants", "modern", "district", "state", "lat", "lon", "kinds", "region", "note", "refs"]
    with open("map/places.tsv", "w", encoding="utf-8") as f:
        w = csv.DictWriter(f, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(P)
    print(len(P), "places")
