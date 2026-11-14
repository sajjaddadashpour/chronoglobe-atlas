# Iran data passes

The real records in the atlas for the polities of the Iranian plateau from Elam to the Islamic Republic, with rulers, capitals and governance periods. Nothing here is border geometry.

## Iran pass 2 (`iran-pass-2-sources`)

Lane-Poole, *The Mohammadan Dynasties* (1894), and Zambaur, *Manuel de généalogie et de chronologie* (1927), were consulted via Chief of Staff transcriptions of archive.org page images (`research/lanepoole_1894.md`, `research/zambaur_1927.md`). Both are older manuals, superseded by Bosworth, *The New Islamic Dynasties* (1996), which still could not be borrowed (`research/bosworth_batch1.md`). Potts, *The Archaeology of Elam* (1999, 1st ed.) was consulted for the pages transcribed in `research/potts_batch1.md`.

A.H. years were converted with the standard tabular (civil) Islamic calendar to Julian A.D. years. When an A.H. year spans two A.D. years, both bounds are kept. Lane-Poole's own printed A.D. years are used as his reading; no printed A.D. year differed from the conversion by more than one year.

| Folder | Records | What |
|---|---|---|
| `sources/` | pass-1 131, plus 2 | Added `lanepoole-1894` and `zambaur-1927`. `potts-elam` is now marked consulted for the transcribed pages. (The repo also holds later Korea sources.) |
| `polities/` | 38 | Unchanged in number. Elam gained a Potts start reading (c. 2600–2500 BC) as a contested alternative |
| `rulers/<polity>/` | 463 | 383 from pass 1, plus 79 rulers added from the books (both years printed) and Mar-biti-apla-usur from Potts p. 262 |
| `capitals/<polity>/` | 86 | Unchanged this pass |
| `layers/governance/<polity>/` | 77 | Unchanged this pass |
| `research/` | 4 | CoS transcriptions (Lane-Poole, Zambaur, Potts batch 1) and the Bosworth borrow note |
| `docs/iran/` | 8 | This file, CORRECTIONS, CONTESTED, OPEN_QUESTIONS, POLITIES, ID_MAP, SNAPSHOT_PLAN, SCHEMA_PROPOSALS |

Confidence labels across the 664 Iran facts: scholarly-consensus 449, estimate 79, attested 43, contested 72, reconstructed 20, legendary 1.

Evidence behind rulers: 283 rest on a scholarly source that was read (Iranica and/or Lane-Poole, Zambaur, Potts), **179 rest only on Wikipedia** (was 248 in pass 1), 1 on news reports. 69 of the 248 Wikipedia-only rows now cite a consulted book. Schema and validator were not changed.

## Iran pass 1 (`iran-pass-1`)

The first real records in the atlas: the polities of the Iranian plateau from Elam (c. 3200 BCE) to the Islamic Republic, with rulers, capitals and governance periods. Nothing here is border geometry.

## What was on the pass-1 branch


| Folder | Records | What |
|---|---|---|
| `sources/` | 131 | Bibliography: 74 Encyclopaedia Iranica articles (full text read), 11 scholarly books (listed, **not consulted**), 42 English Wikipedia revisions and 1 Wikipedia/Wikidata metadata query (secondary cross-check only), 2 news reports, 1 official statement |
| `polities/` | 38 | One file per polity |
| `rulers/<polity>/` | 383 | One file per ruler reign |
| `capitals/<polity>/` | 86 | One file per capital period |
| `layers/governance/<polity>/` | 77 | One file per governance period |
| `docs/iran/` | 8 | This file, CORRECTIONS, CONTESTED, OPEN_QUESTIONS, POLITIES, ID_MAP, SNAPSHOT_PLAN, SCHEMA_PROPOSALS |

Confidence labels across the 584 facts: scholarly-consensus 396, estimate 78, attested 46, contested 43, reconstructed 20, legendary 1.

Evidence behind rulers (pass 1): 134 rest on a scholarly source that was read (Iranica), 248 rest only on Wikipedia, 1 on news reports. Every record says which in its `note` (`Evidence: ...`). Of the capitals, 55 have scholarly support and 31 are Wikipedia only. Of the governance periods, 69 have scholarly support and 8 are Wikipedia only.

## How the draft was mapped to v0

The v0 schemas are flat: one `earliest`, one `latest`, one label, one `note` per fact. The draft recorded more than that. Nothing was invented to fill the gaps. Anything the schema has no field for is kept in the record's `note` and in these docs.

- **Span.** `earliest` is the earliest possible start and `latest` is the latest possible end. The inner bounds (for example a start of 250 to 247 BCE) and the display text are in `note` as "Reign as given: ...", "Start ... ; end ...".
- **One label per record.** Polities had separate labels for start and end. The record carries the weaker one, in this order: attested, scholarly-consensus, estimate, reconstructed, legendary, contested. Both original labels are kept in `note`.
- **Estimates.** v0 needs `low`, `high` and `method` on an estimate. For date facts, `low` and `high` are the same outer year bounds as `earliest` and `latest`, and `method` says so. They are not a separate measurement.
- **Contested.** Each reading is an entry in `alternatives` with its own `sources`. Polity readings also carry `low` and `high` years. Readings of a bound that was not itself contested, and the four chronologies of Deioces (a `legendary` fact), are kept in `note`, because v0 allows `alternatives` only on contested facts.
- **Unknown bounds.** 16 records have one bound the sources do not give. They use the polity's outer bound instead, and their note says so. Two Elamite kings with no year at all (Siruk-tuh, Tammaritu) were left out. All are listed in OPEN_QUESTIONS.md, section F.
- **Ongoing.** The Islamic Republic, its 1989 governance period, Mojtaba Khamenei and Tehran as capital have `latest: 2026`, the year of this pass, and a note saying it is not an end date.
- **Governance.** The governance layer holds numbers only. Each period is encoded as an indicator: `value_low: 1`, `value_high: 1`, the form of governance in `subject`, and a `method` saying this is a category and not a measurement.
- **Books not consulted.** The draft listed Cambridge History of Iran vols 2-7, Bosworth's *New Islamic Dynasties*, Briant, Daryaee (2009 and 2012) and Potts in some polities' `sources`. None of them was opened in this pass, so they are no longer cited by any fact. They stay in `sources/` (notes say "Consulted: no"). Each record that listed one says "Further reading, not consulted this pass: ...".
- **Persian names, Wikidata ids, the old chronoglobe id, the draft's wording of each polity's kind, predecessors/successors and periods of control over Iran** are in each polity's `note` and in POLITIES.md.
- **Wikipedia prose.** The draft kept Wikipedia's "notes" column for each ruler row. That text is CC-BY-SA prose, so it was not carried into this CC-BY data. The book each Wikipedia row cites is kept ("The Wikipedia row cites: ...").
- **Ids.** Rulers are `<polity>-<name slug>`, capitals `<polity>-capital-<place slug>`, and governance periods `<polity>-governance-<nn>`. A `-2`, `-3` suffix marks a repeated name (for example `parthian-phraates-iv-2`). ID_MAP.md maps every draft id to its atlas id.

## Rules this pass kept

Every fact cites at least one source that is a file in `sources/`. Wikipedia is a secondary cross-check only, and its source notes say so. Where an Iranica date and a Wikipedia date disagree, both readings are kept and the fact is `contested`. No date or ruler was added that was not in the draft, and the draft added none that a source opened in that pass did not support.

## Checks

`python3 -m verify` and `make test` pass on this branch. Three repository tests used to assert that the tree held only the 13 illustrations ("Update this when sourced records are added"). They now check that the illustrations are unchanged and kept apart from the real data. No schema and no validator rule was changed.
