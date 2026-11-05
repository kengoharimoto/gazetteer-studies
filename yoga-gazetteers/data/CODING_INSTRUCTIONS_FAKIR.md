# Coding instructions, round two: "fakir/faqir" and "sadhu" in the gazetteers

You code passages from British Indian district gazetteers, caste glossaries and census reports (1866–1935), and from
the revised Indian state gazetteers (1954–1989). The study asks what "yoga", "yogi" and "Jogi" meant to the writers of
these texts. Round one coded passages containing yoga, yogi and Jogi. This round codes passages containing **fakir
(faqir, fakeer) and sadhu**, for two purposes:
1. **Usage.** Whom do the writers call "fakir" and "sadhu"? Is "fakir" used for Hindu ascetics as well as Muslim ones?
   How are such people judged?
2. **Practice without the word.** Find passages that describe yogic or ascetic practice without using the word
   "yoga": posture, breath, trance, the raised arm, the bed of spikes, burial alive, sitting between fires, standing,
   silence, fasting, self-mortification and similar.

Each input row is one passage: `id`, volume metadata, the `terms` that matched, and `text` (about 1000 characters of
OCR). Code what the passage says about **the people the matched terms refer to**.

## Output

Write one TSV row per input passage (never skip a passage), with a header line and these columns:

`id	referent	religion	attitude	practice	tags	page	quote	note`

- **referent**: the main sense of the matched term(s). Use one code:

  | code | use when the term refers to … |
  |---|---|
  | MUSLIM_RELIGIOUS | Muslim mendicants, Sufi orders (Qadiri, Chishti, Madari, Jalali, Benawa …), pīrs and their followers, a dargāh's attendants |
  | HINDU_ASCETIC | Hindu or Sikh ascetics or renunciants (sannyāsī, bairāgī, gosāīn, jogī, udāsī, nāgā, aghorī, "Hindu fakirs"), or a sādhu as a holy man |
  | GENERIC_MENDICANT | religious beggars as a class, without religion specified, or mixed: "fakirs and beggars", "the mendicant classes" |
  | CENSUS_CATEGORY | "Faqir" as a census or caste heading or a population figure; a list of groups classed under it |
  | SAINT_SHRINE | a named holy man, a legend about one, or his tomb or shrine; also a land grant to one |
  | NAME | the term is only part of a personal or place name ("Fakir Chand", "Sadhu Bela") and the passage says nothing about ascetics |
  | OTHER | an unrelated sense ("sadhu" meaning merchant, "sadhu" meaning good) |
  | JUNK | OCR garbage, an index or a table line with no readable statement |

- **religion**: the religion of the referent as the passage states or makes plain: `muslim`, `hindu`, `sikh`,
  `mixed` (explicitly both), or `unclear`. Do not infer it from the word "fakir" alone.
- **attitude**: the writer's own stance toward these people, as the wording shows it: `neg`, `neu`, `pos` or `mixed`.
  Reported opinions ("the people revere him") are `neu` unless the writer adds his own judgement.
- **practice**: `yes` if the passage describes a bodily or contemplative practice of the kind listed in purpose 2,
  otherwise `no`. Describe the practice in `note` in a few words (e.g. "arm held up for years", "sits in five fires",
  "buried alive at will, samādhi").
- **tags**: comma-separated, possibly empty, from the round-one list:
  - fraud, crime, low_status, beggar, performer, magic, healing, austerity, meditation, burial, learning, sanctity,
    order, householder, political, numbers, reform, western, health;

  plus these two:
  - `land`: endowments, rent-free land, maintenance grants;
  - `fakir_for_hindu`: the word fakir is applied to a Hindu or Sikh ascetic. Use it whenever religion is `hindu` or
    `sikh` and a matched term is fakir or faqir.
- **page**: the printed page number if visible in the passage; otherwise empty. Never guess.
- **quote**: the shortest verbatim span (8–40 words) from `text` that supports your referent code, or the practice if
  `practice` is yes. Copy it exactly as it stands in the OCR, errors included, because a script will check it. Use …
  only between two verbatim pieces. Leave it empty for NAME, OTHER and JUNK.
- **note**: optional, at most 20 words.

## Rules

- When a passage has several fakirs or sādhus, code the dominant one. Put anything notable about the others in `note`.
- Be literal. Do not import what you know about Sufis, Nāths or sādhus into a passage that does not say it.
