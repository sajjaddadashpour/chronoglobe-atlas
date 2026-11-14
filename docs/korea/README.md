# Korea pass 1

First import of Korean polities into the atlas, following the conventions of the Iran pass (`docs/iran/README.md`, `docs/iran/SCHEMA_PROPOSALS.md`). Nothing in `schema/` or `verify/` was changed. Generated on 2026-11-14 (America/Regina) by the pass scripts (kept outside the repo); every value below comes from a source fetched this pass.

## What is in this pass

| kind | records |
|---|---|
| polities | 27 |
| rulers (incl. heads of state / governors) | 265 |
| capitals | 37 |
| governance periods (`layers/governance/`) | 35 |
| sources | 262 (250 Encyclopedia of Korean Culture articles) |

Polities: gojoseon, wiman-joseon, jin, buyeo, okjeo, dongye, mahan, jinhan, byeonhan, gaya, geumgwan-gaya, daegaya, goguryeo, baekje, silla (to 668), unified-silla, balhae, later-baekje, taebong (Later Goguryeo / Majin / Taebong), goryeo, joseon (to 1897), korean-empire, japanese-korea (1910-45), usamgik, soviet-civil-administration, north-korea, south-korea.

### Confidence labels

| kind | attested | scholarly-consensus | estimate | reconstructed | legendary | contested |
|---|---|---|---|---|---|---|
| polity | 9 | 3 | 7 | 0 | 0 | 8 |
| ruler | 0 | 197 | 2 | 0 | 6 | 60 |
| capital | 12 | 13 | 0 | 0 | 0 | 12 |
| governance | 8 | 13 | 5 | 0 | 0 | 9 |
| **all 364** | 29 | 226 | 14 | 0 | 6 | 89 |

### Evidence

Each note ends with an evidence class:

- `scholarly-or-primary`: both bounds read in an Encyclopedia of Korean Culture (EKC) article: 294 facts.
- `scholarly-partial`: one bound from EKC, the other from Wikipedia: 12.
- `secondary-only`: the years rest on Wikipedia only (an EKC article may still be cited for the name or existence): 58.

Facts whose cited sources are only Wikipedia: **53 of 364 (14.6%)**. Almost all are modern officeholders (governors-general, ROK presidents and acting presidents, DPRK leaders, US and Soviet occupation heads) and the ROK republic periods. Premodern Wikipedia-only rows: Bu of Gojoseon and Seong of Balhae. The years of Isipum, Jwaji, Chwihui and Jilji of Geumgwan Gaya and of Jun of Gojoseon also come only from Wikipedia, but those records cite EKC as well (for the critical reading or for existence), so their notes say `secondary-only` without counting as Wikipedia-only. As in the Iran pass, Wikipedia-only rulers carry `scholarly-consensus` and the note says `Evidence: secondary-only`.

## Sources

- **Encyclopedia of Korean Culture (한국민족문화대백과사전, encykorea.aks.ac.kr), Academy of Korean Studies.** The main scholarly source. Every article cited was fetched in full and searched (Korean text); writer and year are in the source note where the page gives them. EKC articles are signed expert entries, but they are copyrighted: facts are restated, nothing is copied. The site search does not work for scripts, so articles were found through Wikidata property P9475 (EKC ID), Korean Wikipedia external links, and links between EKC pages.
- **English Wikipedia, pinned revisions** (secondary cross-check only, CC BY-SA 4.0, facts restated): List of monarchs of Korea (rev 1380042635), Governor-General of Chōsen (1373668098), List of presidents of South Korea (1382209069), Supreme Leader (North Korean title) (1384705164), United States Army Military Government in Korea (1378984422), Soviet Civil Administration (1385678512). Wikidata items and EKC IDs came from the Wikipedia/Wikidata APIs (`sources/wp-en-wikidata-korea.yaml`, CC0).
- **Not consulted this pass:** Samguk sagi (1145), Samguk yusa, Goryeosa (1451), Lee Ki-baik *A New History of Korea* (1984) and Seth *A History of Korea* (2010) are in `sources/` with `Consulted: no` and are cited by no fact. Facts that go back to Samguk sagi or Samguk yusa are cited through the EKC article that reports them, and the note says so. *The Cambridge History of Korea* vol. 1 and the National Institute of Korean History database (db.history.go.kr) were not opened, and there are no source records for them. Citing a specific edition of the chronicles is left for pass 2 (OPEN_QUESTIONS A).

## Conventions (same as the Iran pass, plus Korea-specific choices)

- `earliest` / `latest` are the outer bounds; inner readings are in `note` ("Reign as given: ...") and, for contested facts, in `alternatives`, each with its own sources and label.
- One label per fact = the weaker of start and end (attested < scholarly-consensus < estimate < reconstructed < legendary < contested).
- Where a source gives only a century ("1st century BCE", "around the turn of the era"), the years are this pass's encoding of it. The note or alternative says so, and the label is `estimate` or `contested`.
- **Early Samguk sagi chronology.** Rulers whose dates rest only on early Samguk sagi / Garakguk-gi are `contested`, with two readings: "Samguk sagi reign as given" (labelled reconstructed), and a "critical reading" (no years) citing the EKC polity article. This covers Goguryeo #2-#9 (before Sansang), Baekje #2-#12 (before Geunchogo), Silla #2-#16 (before Naemul), Geumgwan Gaya #2-#9 and Daeso of Buyeo. The founders (Dangun, Jumong/Dongmyeong, Onjo, Hyeokgeose, Suro) and Geumwa are `legendary`.
- **EKC vs Wikipedia disagreements.** Where they differ by even one year (often a lunar/solar or accession-year difference), the fact is `contested` with both readings. EKC and Wikipedia differ for 20 rulers. 19 are contested with both readings; Geumwa is labelled legendary and his two readings are in the note. See CONTESTED.md.
- **Split reigns.** A king who ruled twice gets two records (`-2` suffix): Chungnyeol, Chungseon, Chungsuk, Chunghye; ROK acting presidents Ho Chong and Han Duck-soo; Park Chung Hee as acting president and as president; Saitō and Ugaki as governors-general.
- **Polity splits.** Silla is split at 668 into silla / unified-silla, as old chronoglobe did; EKC treats it as one state, 57 BCE-935 CE. Joseon is split at 1897 from the Korean Empire; EKC's Joseon runs to 1910. Gojoseon and Wiman Joseon are separate; EKC allows both scopes. Old "Samhan" is split into mahan, jinhan and byeonhan. Old "Gaya" is split into the gaya confederacy plus geumgwan-gaya and daegaya.
- **Governance** is the Iran 0/1 indicator layer. Goryeo has four periods: monarchy 918-1170, military regime 1170-1270, Yuan overlordship 1259/1270-1356 (contested start), monarchy 1356-1392. The Korean Empire has the Japanese protectorate 1905/1906-1910 (contested start). South Korea uses the republic period headings of the Wikipedia list only; the constitutional form of each republic is not encoded (OPEN_QUESTIONS).
- **Modern heads.** The DPRK record holds the three supreme leaders. Premiers are left out (old chronoglobe mixed them in). The ROK record holds presidents and every acting president in the Wikipedia timeline. Kim Il-sung's 1946-48 chairmanship is filed under soviet-civil-administration.
- Kings with no year were dropped. So were kings with only one bound where filling it from the polity bound would make an implausible span of centuries (Buyeo after Daeso, Daegaya, Gija). This is stricter than the Iran pass, where the polity-bound fill was applied to 16 records. All are listed in OPEN_QUESTIONS B and F.
- Ongoing polities and officeholders end at 2026, with the note "not an end date".
- Ids follow the Iran pattern (`<polity>-<name>`, `<polity>-capital-<place>`, `<polity>-governance-<nn>`); EKC sources are `ekc-<article id>-<slug>`.
- **Automatic check.** For every fact citing EKC, the script checked that its stored years occur in the cited article text. 30 facts were flagged; each is explained in OPEN_QUESTIONS C. All are century encodings, the Wikipedia side of a contested pair, or derived years (e.g. 919 = "the next year" after 918).

## Files

- `CORRECTIONS.md`: what changes against old chronoglobe Korea data.
- `CONTESTED.md`: scholarly disputes and every contested record.
- `OPEN_QUESTIONS.md`: gaps, dropped rows, flagged checks.
- `SNAPSHOT_PLAN.md`: proposed map snapshot years and candidate map sources (no geometry in this pass).

Validation: `python3 -m verify` and `pytest` pass.
