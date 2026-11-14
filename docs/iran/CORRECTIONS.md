# Corrections to the old chronoglobe Iran data

Old data: `/workspace/chronoglobe/data/{polities.json, rulers/*.json, capitals/*.json}` and the map layers `public/data/world_*.geojson` (historical-basemaps, GPL). Labels were sampled at Isfahan, Susa, Tabriz and Mashhad.
New data: this branch (`polities/`, `rulers/`, `capitals/`, `layers/governance/`). Source ids refer to files in `sources/`. `eir-*` = Encyclopaedia Iranica (scholarly, full text read); `wp-*` = Wikipedia (secondary cross-check only).
"Old" values are given as stored (BCE negative).

## 1. Missing polities and gaps in the lineage (highest impact)

| # | Old | Fix | Source |
|---|---|---|---|
| 1.1 | No **Elam** polity. The map shows "Elam" at Susa only at -5000, then "Ur" (-4000 to -2000) and "Babylonia" (-1500 to -700) | Added `elam`, c. 3200 BCE (Proto-Elamite; no 5000 BCE start) to 646/539 BCE, with dynastic phases and Neo-Elamite kings | eir-elam-i (Vallat) |
| 1.2 | Neither Elam nor the Medes ever appear on the map between -1500 and -700 (Isfahan is "state societies and Aramaean kingdoms") | Needs new border snapshots (see borders/SNAPSHOT_PLAN.md) | eir-elam-i, eir-media-ii |
| 1.3 | Gap **1357-1370** between Ilkhanate (ends 1357) and Timurids (start 1370) | Added the post-Ilkhanid states: `chobanid` 1335-1357, `jalayirid` 1336-1431/32, `injuid` c.1325/1335-1353, `muzaffarid` 1314-1393, `kartid` 1245-1381/89, `sarbadar` 1337-1381 | eir-chobanids, eir-jalayerids, eir-inju-dynasty, eir-mozaffarids, eir-al-e-kart, eir-sarbedars |
| 1.4 | No **Tahirids, Ziyarids, Qara Qoyunlu, Persis/frataraka, Elymais** | Added | eir-taherids, eir-ziyarids, wp-en-qara-qoyunlu (secondary), eir-persis-kings-of, eir-frataraka, eir-elymais |
| 1.5 | Saffarids and Ghaznavids exist only outside the Iran lineage (`ca-saffarid`, `in-ghaznavid`) | Linked into the Iran lineage as predecessors/successors. The old ids are kept in `old_chronoglobe_id` | eir-saffarids, eir-ghaznavids |
| 1.6 | Abbasid polity **ends 875**, and its rulers stop at al-Mutawakkil (861) | Polity ends 1258 (fall of Baghdad), with governance periods: direct rule in Iran to 821, autonomous dynasties 821-945, Buyid/Seljuk tutelage 945-1258. Caliphs after 861 are an open question | eir-abbasid-caliphate, eir-il-khanids-i |
| 1.7 | Rashidun 651-661 | 632-661 as a polity; Iran control 637-651 recorded separately | eir-arab-ii-conquest, wp-en-list-of-monarchs-of-iran |
| 1.8 | Khwarazmian 1194-1221, with only 3 rulers from 1172 | 1097-1231, 7 rulers. Seljuk vassals to 1172; Jalāl-al-Din to 1231 | eir-khwarazmshahs-iii |
| 1.9 | Aq Qoyunlu 1469-1501 | Contested: start 1348 / c.1394-1403 / 1452, end 1503-1508. 1469 is only the move to Tabriz | eir-aq-qoyunlu, wp-en-aq-qoyunlu |
| 1.10 | Hotaki 1722-1729 | 1709 (Mir Ways at Kandahar) to 1738 (Kandahar surrenders to Nader). 1722-29 is kept as the Isfahan phase | eir-kandahar-iv, eir-afghanistan-x |
| 1.11 | Safavid ends 1736 | Contested: 1722 (Iranica, "ruled Persia from 1501 to 1722") vs 1736 (nominal shahs under Nader). Governance periods added | eir-safavid-dynasty |
| 1.12 | Qajar starts 1789 | Contested 1779 / 1786 / 1789 / 1796. Accession at Tehran 21 Mar 1786 | eir-fath-ali-shah, eir-zand-dynasty |
| 1.13 | No governance periods anywhere | Added 77, e.g. Qajar constitutional monarchy from 1906 (Majles opened 7 Oct 1906), Jalayirid amir-e olus to 1356 then sultanate, Zand wakil, Islamic Republic constitutions of 1979 and 1989 and the 2026 interim Leadership Council | eir-constitutional-revolution-ii, eir-jalayerids, eir-zand-dynasty, eir-constitution-islamic-republic |

## 2. Map-label errors (old basemap layers, sampled)

These labels come from the GPL historical-basemaps files. They are listed so the new border snapshots can fix them; the GPL files themselves were not edited.

| Year(s) | Point | Old label | Should be | Source |
|---|---|---|---|---|
| -4000 to -2000 | Susa | Ur | Elam (Proto-Elamite, Awan, Šimaški, sukkalmah). Mesopotamian control of Susa in some phases needs dated snapshots | eir-elam-i |
| -1500 to -700 | Susa | Babylonia | Elam (Middle and Neo-Elamite) | eir-elam-i |
| -700 to -600 | Isfahan | "state societies" | Median sphere (contested extent) | eir-media-ii |
| -200, -100 | Isfahan | Seleucid Kingdom | Parthian at -100 (Media taken 148 BCE) | eir-seleucid-empire |
| 300 | all | Parthian Empire | Sasanian Empire (from 224) | eir-sasanian-dynasty |
| 400 | all | "Persia" | Sasanian Empire (label too generic) | eir-sasanian-dynasty |
| 700 | all | Sasanian Empire | Umayyad Caliphate (Sasanians fell 650/651) | eir-sasanian-dynasty, eir-arab-ii-conquest |
| 1100, 1200 | Mashhad | Ghaznavid Emirate | Seljuk (1100); Khwarazmshah sphere (1200; needs checking). Khorasan was lost at Dandānqān in 1040 | eir-ghaznavids, eir-khwarazmshahs-iii |
| 1200 | Isfahan, Susa | Buwayhid Emirates | post-Seljuk western Iran: Khwarazmshah claims after Tekeš killed Ṭoḡrïl III in 1194 (needs border check). The Buyids ended in 1062 | eir-buyids |
| 1000, 1100 | Tabriz | Armenia | Needs checking (Rawwadids/Seljuks?). Open question | – |
| 1530-1700 | Susa, Tabriz | Ottoman Empire | Mostly Safavid. Tabriz changed hands several times; needs dated snapshots | eir-safavid-dynasty (snapshot work pending) |
| 1740 | all | Safavid Empire | Afsharid (Nader crowned 1736) | eir-afsharids |
| 1765-1810 | all | "Persia" | Zand (1765-94), Qajar (from 1786/89) | eir-zand-dynasty, eir-fath-ali-shah |
| 1765-1810 | Mashhad | Durrani / Afghanistan | Afsharid Khorasan until 1796, then Qajar | eir-afsharids |

## 3. Ruler-list errors

| Polity | Old | Fix | Source |
|---|---|---|---|
| Parthian | **Two Mithridates I records** (-171..-142 and -142..-132) | One reign, c. 171-138/132 BCE (contested end). Wikipedia splits it at the conquest of Babylonia | eir-ctesiphon; wp-en-list-of-monarchs-of-iran (Venning 2023) |
| Parthian | Mithridates II starts -124, overlapping Artabanus I (to -123) | c. 123-91 BCE | wp list (Venning 2023 p. 163) |
| Parthian | Gotarzes I -91..-80, Orodes I -80..-75, Sinatruces -75..-69, Phraates III -69..-57, Vonones I 8-12, Vardanes 40-46, Pacorus II 78-110 as one reign | Current list: 91-87, 87-79, c.78-70, 70-57, 6/7-11/12, 39-45/46, and Pacorus in two reigns (78-79, 81-115). The old data used an older list revision. All secondary | wp list rev. 1385173685 |
| Parthian | Vologases VI 207-213 | Contested: Iranica calls him Vologeses VI and gives 207-227/28 (rival of Artabanus IV); Wikipedia numbers him V, 207-213 | eir-sasanian-dynasty |
| Parthian | Artabanus IV 213-224 | 212/213-224 | eir-sasanian-dynasty, eir-arsacids-ii |
| **Rashidun** | Only Uthman and Ali. **Umar missing** | Abu Bakr 632-634, Umar 634-644 (in Iran from 637/638), Uthman, Ali, Ḥasan | eir-arab-ii-conquest; wp list (Venning 2023; Madelung 1997) |
| Medes | Wikipedia figures (Diakonoff) given as plain fact; no Scythian interregnum | Four chronologies kept as alternatives; Deioces `legendary`; Scythian interregnum row added | eir-media-ii, eir-deioces |
| Achaemenid | Cyrus "the Great" -559..-530 with no context; Bardiya as one plain record | Cyrus II king of Persia 559, empire from 550. Bardiya/Gaumāta contested (11 Mar vs 1 Jul 522). Bessus 330-329 and Cyrus I / Cambyses I (pre-imperial, estimate) added | eir-cyrus-iii, eir-bardiya |
| Achaemenid | Darius II -423..-404 | Contested 404/403 | eir-darius-iv-darius-ii |
| Sasanian | Yazdegerd III 633-651 | 632/633-651 (contested) | eir-arab-ii-conquest |
| Khwarazmian | Jalāl-al-Din 1220-1221 | 1220/21-1231 | eir-khwarazmshahs-iii |
| Qajar | **27 prime-minister terms mixed into the monarch list** (Amir Kabir, Amin al-Sultan, Mostowfi ol-Mamalek, ...) and "Reza Shah 1923-1925" listed as a ruler | Monarchs only; heads of government belong in a separate offices list (open question) | data-model fix |
| Pahlavi | 32 prime-minister terms mixed in, plus Reza Shah listed again as 1923-1925 (his premiership) | Reza Shah 15 Dec 1925 - 16 Sep 1941; Mohammad Reza 1941 - 11 Feb 1979 | wp list (secondary) |
| Islamic Republic | Presidents mixed in with Supreme Leaders; Ali Khamenei appears as 1981-1989 (as president) and 1989-2026 with no role | Supreme Leaders only: Khomeini 1979-3 Jun 1989, Ali Khamenei 4 Jun 1989-28 Feb 2026, interim Leadership Council (Art. 111), Mojtaba Khamenei from 8 Mar 2026 | eir-khomeini-i; wp-en-supreme-leader-of-iran; primary-assembly-of-experts-2026-03-08; news-reuters / news-bbc 2026-03-08 |
| Qajar | Mozaffar-al-Din to 1907, Moḥammad-ʿAli from 1907 | 1906/3 Jan 1907 boundary kept as a range (Iranica gives "1896-1906" and "1906-1909") | eir-constitutional-revolution-i, eir-ahmad-shah-qajar |
| Safavid | Suleiman I from 1666 | Ṣafi II from 3 Oct 1667, re-crowned as Solaymān I in 1668 (one reign) | wp list (Spuler 1977) |
| Aq Qoyunlu | Alvand and Murad cut at 1501 | Alvand 1497-1502, Murad 1500-1508 (in Fārs/Kerman) | wp list (Bosworth 2012), eir-aq-qoyunlu |
| Almost all Iran lists | `confidence: parsed-list` from "List of monarchs of Persia" (no revision id) | Every row now cites a fixed Wikipedia revision (1385173685), keeps the book it cites in `via`, and is marked `evidence: secondary-only` unless an Iranica text also supports it | – |

## 4. Capital errors

| Polity | Old | Fix | Source |
|---|---|---|---|
| **mongol-iran** | **Avarga 1206-1235, Karakorum 1235-1271** | No capital in Iran. These are Mongolian imperial seats. Iran was run by governors (Čin Temür, Körgüz, Arḡun Āqā), now listed with role `governor` | eir-cin-timur, eir-argun-aqa |
| Ilkhanate | Tabriz 1265-1307 overlaps Solṭāniya 1306-1335; nothing after 1335 | Tabriz 1265-1306, Solṭāniya 1306-1335, then Tabriz as the seat of the Chobanid-backed khans 1335-1357 (estimate). Years secondary | eir-il-khanids-i, eir-chobanids, wp-en-ilkhanate |
| Achaemenid | Pasargadae -550..-518, then "Persepolis (ceremonial), Susa, Ecbatana, Babylon" as one string | Five separate records with roles: Ecbatana (Cyrus's seat, Schmitt), Susa (administrative from Darius I), Babylon, Pasargadae (contested: "capital" per Gopnik vs ceremonial), Persepolis (from c. 518) | eir-achaemenid-dynasty-i, eir-pasargadae, eir-persepolis |
| Parthian | Only Ctesiphon, from -129 | Nisa, Hecatompylos, Ecbatana (summer), and Ctesiphon from Mithradates I (c. 171-138) | eir-ctesiphon, eir-arsacids-ii |
| Abbasid | Stops at Samarra 836-892 | Baghdad again 892-1258 | wp-en-abbasid-caliphate |
| Safavid | Isfahan 1598-1736 | Isfahan 1597/98-1722 (Hotaki-held 1722-29) | eir-isfahan-vii |
| Qajar | Tehran from 1789 | Tehran from 1786 | eir-fath-ali-shah |
| Seleucid | Seleucia 305-240, Antioch 240-63 only | Babylon 312-305, Seleucia on the Tigris (eastern capital, lost 141), Antioch (western) | eir-seleucid-empire, wp-en-seleucid-empire |
| Sasanian | Istakhr 224-226, Ctesiphon 226-637 | Ctesiphon from 224/226 (Iranica: from Ardashir). Istakhr kept as secondary-only | eir-ctesiphon |
| Medes, Elam, Tahirid, Ziyarid, Chobanid, etc. | none | Added (Ecbatana; Susa, Anshan, Madaktu, Hidalu; Merv then Nishapur; Ray and Gorgān; Tabriz...) | see `capitals/<polity>/` |

## 5. Data-model corrections

- Old dates were single integers. New dates carry `earliest`/`latest`, `display`, `confidence`, `sources`, and `alternatives` where sources disagree.
- Old `confidence` values (`parsed-list`, `curated-verified`) mixed provenance with certainty. New: `confidence` (one of the six labels) plus `evidence` (scholarly-or-primary / news / secondary-only).
- Ruler roles (head of state vs head of government vs rival claimant vs puppet) are now explicit (`title`, `role`).
