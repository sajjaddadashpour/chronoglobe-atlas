# Open questions and things deliberately left out

Rule for this pass: anything that could not be checked against a source opened this pass was left out or marked unknown. This file lists those gaps.

## A. Sources that could not be consulted (books)

- **Bosworth, *The New Islamic Dynasties* (1996).** Not opened. Reign dates for the medieval dynasties currently rest on Iranica text plus the Wikipedia list, which cites Ross 1977, Daryaee 2012 and Venning 2023. Iranica cites NID for the Ziyarids (no. 81, pp. 166-67), Samanids (pp. 170-71), Saffarids (no. 84, pp. 172-73) and Khwarazmshahs (no. 89, pp. 178-80). Next step: check every medieval ruler row against NID.
- **Cambridge History of Iran vols 2-7, Briant (2002), Daryaee (2009 and the 2012 *Oxford Handbook* tables), Potts (*Archaeology of Elam*).** Kept in `sources/` with "Consulted: no" in the note, and no longer cited by any fact (see README.md). No ISBNs are given because none were checked.
- **Iranica articles not online.** SAMANIDS, TIMURIDS, QARA QOYUNLU, QAJAR DYNASTY, PAHLAVI DYNASTY, SALJUQS (Great Seljuks), XERXES, KHORASAN viii-ix and TABRIZ return only index or landing pages. The Seljuk, Timurid, Qara Qoyunlu and Pahlavi data are therefore **secondary-only** (Wikipedia).

## B. Rulers left out or with unknown bounds

- Elam: most kings before the Neo-Elamite period (the Awan and Šimaški king lists, the sukkalmahs from Kutir-Nahhunte I to Kuk-Našur III, the Igihalkids and the Šutrukids). Iranica names them but gives no reign years. Only floruits are recorded.
- Elam: Tammaritu, Indabigaš and the Neo-Elamite III kings Hallutaš-Inšušinak and Atta-hamiti-Inšušinak have no years.
- Persis: the later kings of Persis (1st century BCE to 3rd century CE) up to Pābag. The Iranica TABLE 1 was not extracted.
- Elymais: the full Kamnaskirid/Arsacid-branch list down to Orodes V (221/222 CE, Wikipedia infobox only).
- Abbasid caliphs after al-Mutawakkil (861), down to 1258. Not imported because the Wikipedia Iran list stops at 861. Source needed: Bosworth NID.
- Ghaznavid sultans after Masʿud I (1040-1186).
- Chobanids: the end of Ḥasan-e Kūček and the start of Malek Ašraf were not extracted from Iranica (the text is long; the dates are in Table 41, which was not parsed).
- Jalayirids: start years for Ovays II, Moḥammad and Ḥosayn II, and the end for Maḥmud. Also the AH year for Ḥosayn II's death (Iranica gives 9 Nov 1431).
- Muzaffarids: Shah Maḥmud (Isfahan), the end of Zayn-al-ʿĀbedin, Shah Manṣur and the other princes of 1387-93.
- Sarbadars: Masʿud's end (Wikipedia 1343 only) and the leaders 1351-1361 (Yaḥyā Karābi, Ḥaydar, Loṭf-Allāh). Only Wikipedia has them, and its two lists disagree.
- Timurids: Badiʿ-al-Zamān (1506-07, old data only) and Abu Saʿid Mirzā's end (1458 in the Iran list vs 1469).
- Hotaki: Ḥosayn Hotak at Kandahar (to 1738) is not in the sources read.
- Qajar: the coronation year of Āqā Moḥammad Khan (1796?) and the Majles vote deposing Aḥmad Shah (commonly 31 Oct 1925) were not in the sources read.
- Islamic Republic: presidents and prime ministers. The old dataset mixed them into the monarch list. They are not in this pass and belong in a separate `offices` list. Masoud Pezeshkian has been president since 28 Jul 2024 (Wikipedia President of Iran, secondary).
- Islamic Republic: exact date the Leadership Council took over (28 Feb or 1 Mar 2026). Sources say "after" Ali Khamenei's death; CBS reported it on 1 Mar 2026 but was not cited.

## C. Facts flagged by the automatic cross-check

Each ruler citing an Iranica article was checked: do its bound years occur in the cached text of that article? Rows where some years were not found are below. In most of them the missing year comes from the Wikipedia reading kept as the other bound, but every row needs a human check.

- `elam` Humban-haltaš III: partly-found, years not in the cited Iranica text: [645]
- `elam` Šutur-Nahhunte, son of Humban-umena III: partly-found, years not in the cited Iranica text: [600]
- `persis` Baydād (Bagadates): partly-found, years not in the cited Iranica text: [170, 180, 200]
- `persis` Ardaxšīr I: partly-found, years not in the cited Iranica text: [165, 180, 200]
- `persis` Vahbarz (Oborzos): partly-found, years not in the cited Iranica text: [150, 200]
- `persis` Wādfradād I: partly-found, years not in the cited Iranica text: [150, 200]
- `persis` Unknown King I: none-found, years not in the cited Iranica text: [101, 150]
- `persis` Dārāyān I: partly-found, years not in the cited Iranica text: [100]
- `persis` Wādfradād III: partly-found, years not in the cited Iranica text: [100]
- `saffarid` Ya'qub: partly-found, years not in the cited Iranica text: [879]
- `saffarid` Khalaf: partly-found, years not in the cited Iranica text: [1002]
- `ziyarid` Mardavij: partly-found, years not in the cited Iranica text: [927]
- `ziyarid` Bisutun: partly-found, years not in the cited Iranica text: [966]
- `khwarazmian` Arslāntigin Muhammad I: partly-found, years not in the cited Iranica text: [1128]
- `jalayirid` Šāh Valad: partly-found, years not in the cited Iranica text: [1411]
- `jalayirid` Solṭān Maḥmud: partly-found, years not in the cited Iranica text: [1411]
- `injuid` Šaraf-al-Din Maḥmud Šāh Inju: partly-found, years not in the cited Iranica text: [1336]
- `injuid` Ḡiāṯ-al-Din Kayḵosrow: partly-found, years not in the cited Iranica text: [1336]
- `kartid` Šams-al-Din I: partly-found, years not in the cited Iranica text: [1277]
- `kartid` Šams-al-Din II (Rokn-al-Din): partly-found, years not in the cited Iranica text: [1277]
- `kartid` Šams-al-Din III: partly-found, years not in the cited Iranica text: [1330]
- `kartid` Ḥāfeẓ: partly-found, years not in the cited Iranica text: [1330]
- `sarbadar` Wajih-al-Din Masʿud: partly-found, years not in the cited Iranica text: [1344]
- `sarbadar` Pahlavān Ḥasan Dāmḡāni: partly-found, years not in the cited Iranica text: [1361]
- `qara-qoyunlu` Jahānšāh: partly-found, years not in the cited Iranica text: [1436]
- `aq-qoyunlu` Uzun Hasan: partly-found, years not in the cited Iranica text: [1453]
- `qajar` Mohammad Ali: partly-found, years not in the cited Iranica text: [1907]

## D. Secondary-only polities (no scholarly source opened)

- `rashidun`: start or end rests only on Wikipedia
- `umayyad`: start or end rests only on Wikipedia
- `seljuk`: start or end rests only on Wikipedia
- `timurid`: start or end rests only on Wikipedia
- `qara-qoyunlu`: start or end rests only on Wikipedia
- `pahlavi`: start or end rests only on Wikipedia

In total, 248 ruler rows are secondary-only (Wikipedia list or articles). Each keeps its underlying citation in its `note` ("The Wikipedia row cites: ...") (e.g. "Venning 2023 p. 163") so the next pass can check the cited book directly.

## E. Other gaps

- Persian (fa) names of polities are fa.wikipedia article titles, a secondary source. Some are descriptive ("تمدن ایلام" = "Elamite civilisation", "قوم ماد" = "Median people"); proper polity names should be confirmed. Zand is left blank because its langlink points to a list page.
- Persian names of rulers were not collected in this pass.
- Wikidata QIDs were not checked for scope. Example: the Zand QID Q97629053 may be a list item.
- Iranica Ilkhanid capital years: the article mentions Marāḡa, Tabriz and Solṭāniya without years. The years come from Wikipedia.
- Achaemenid Pasargadae "capital vs ceremonial site" needs Briant/CHI 2 to settle.
## F. From the conversion to the v0 schema

Dropped because they have no year at all and v0 requires `earliest` and `latest` (still open questions):

- ruler Siruk-tuh (draft `ruler/elam/003`): no reign year in any source read; v0 requires earliest and latest.
- ruler Tammaritu (draft `ruler/elam/016`): no reign year in any source read; v0 requires earliest and latest.

One bound unknown. The record uses the polity's outer bound in its place, and its note says so. These need the real year:

- `elam-humban-nikas-ii` (Humban-nikaš II (Ummanigaš)): `latest` set to the polity bound -539.
- `elam-sutur-nahhunte-son-of-humban-umena-iii` (Šutur-Nahhunte, son of Humban-umena III): `latest` set to the polity bound -539.
- `elymais-kamnaskires-i` (Kamnaskires I (Soter)): `latest` set to the polity bound 224.
- `ziyarid-keikavus` (Keikavus): `latest` set to the polity bound 1091.
- `ziyarid-gilanshah` (Gilanshah): `earliest` set to the polity bound 927.
- `mongol-iran-nosal` (Nosal (*Baysal)): `latest` set to the polity bound 1256.
- `mongol-iran-korguz` (Körgüz): `earliest` set to the polity bound 1219.
- `chobanid-hasan-e-kucek` (Ḥasan-e Kūček (Shaikh Ḥasan "the Lesser")): `latest` set to the polity bound 1357.
- `chobanid-malek-asraf` (Malek Ašraf): `earliest` set to the polity bound 1335.
- `jalayirid-soltan-mahmud` (Solṭān Maḥmud): `latest` set to the polity bound 1432.
- `jalayirid-soltan-ovays-ii` (Solṭān Ovays II): `earliest` set to the polity bound 1336.
- `jalayirid-soltan-mohammad` (Solṭān Moḥammad): `earliest` set to the polity bound 1336.
- `jalayirid-hosayn-ii-b-ala-al-dawla` (Ḥosayn II b. ʿAlāʾ-al-Dawla): `earliest` set to the polity bound 1336.
- `muzaffarid-zayn-al-abedin` (Zayn-al-ʿĀbedin): `latest` set to the polity bound 1393.
- `elymais-capital-susa` (Susa): `latest` set to the polity bound 224.
- `elymais-capital-seleucia-on-the-hedyphon` (Seleucia on the Hedyphon (Jānešīn?)): `latest` set to the polity bound 224.

Ongoing facts (Islamic Republic, its governance period since 1989, Mojtaba Khamenei, Tehran as capital) use `latest: 2026`, the year of this pass, because v0 has no open-ended span.
