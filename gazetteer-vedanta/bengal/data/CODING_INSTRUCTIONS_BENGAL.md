# Coding instructions: Daśanāmīs in Bengal, Bihar and Orissa

Follow `../../north/data/CODING_INSTRUCTIONS_NORTH.md` in full: same output files
(`results/coded/<VOL>.counts.tsv`, `<VOL>.notes.tsv`), same columns, `group_std`, `kind` and `order` codes,
same rules. Changes and additions for Bengal:

## Sources

- `HU01`–`HU19`: W. W. Hunter, *A Statistical Account of Bengal* (1875–77), several districts per volume.
  Census 1872. Hunter prints, for each district, a long caste list with numbers ("Atith … 1,234"), and a
  religion section with sects. Fill `district` from the district account the statement sits in.
- `BG01`–`BG46`: *Bengal* / *Bihar and Orissa District Gazetteers* (O'Malley and others, 1905–18). Census 1901
  (sometimes 1911). One district per volume.
- Selections: `data/selection_hunter.tsv`, `data/selection_bdg.tsv`. Packets: `results/packets/<VOL>.txt`.

## Terms in this region

- Daśanāmī: Atīth / Atit (very common in Bihar and Bengal for householder and monastic Daśanāmīs), Gosāin /
  Gossain, Sannyāsī / Sanyasi, Daṇḍī, Paramhaṃsa, Giri, Purī, Bhāratī. Atīth and Atit count as `GOSAIN`.
- **Vaiṣṇava "Gosains" in Bengal are very common.** They are the hereditary gurus of the Chaitanya
  (Gauḍīya) movement, Nityānanda and Advaita lineages at Śāntipur, Navadvīp and Khardah. They are NOT
  Daśanāmī: code them `OTHER` with a note. Bengali "Gosain" or "Goswami" without further marks is usually
  Vaiṣṇava. Classify by context, and when unsure use `OTHER`.
- Also distinguish Vaiṣṇava Bairāgīs / Vaishnavas (Bengal's "Boishtom"), Kanphaṭa Jogīs and the Bengal
  "Jugi" weaver caste. The Jugi caste is not ascetic: code it `OTHER`.

## Key institutions to watch for (code what the text says)

- Bodh Gayā maṭha (Gaya): Śaiva Giri mahants holding the Mahābodhi temple and large estates.
- Tārakeśvar (Hooghly): the mahant (Giri) of the Śiva temple.
- Purī: the Govardhana maṭha (Śaṅkarācārya), and Daśanāmī maṭhas beside the many Vaiṣṇava ones.
- Daśanāmī landholders and mahants in Bihar (e.g. Monghyr, Bhagalpur, Saran, Purnea). The Sannyāsī and Fakīr
  "rebellion" of the 1760s–1800 in north Bengal (Rangpur, Dinajpur, Bogra, Mymensingh, Rajshahi): code as
  `MILITARY`.
