# Iran polities: names, identifiers and succession

The v0 polity schema has one `name` and no fields for other languages, Wikidata ids or polity succession. This table keeps them; each record's `note` repeats them.
Persian names are fa.wikipedia article titles and Wikidata ids come from English Wikipedia pageprops (source `wp-fa-langlinks`, secondary). Neither has been checked for scope.

| id | English name | Persian | Wikidata | old chronoglobe id | predecessors | successors |
|---|---|---|---|---|---|---|
| `elam` | Elam | ایلام (تمدن ایلام) | Q128904 |  |  | `achaemenid` (Susiana absorbed by the Persians (Cyrus?); Anshan was already ruled by the early Achaemenids/Teispids) |
| `medes` | Median kingdom (Medes) | ماد | Q8735 | medes |  | `achaemenid` |
| `achaemenid` | Achaemenid Empire | شاهنشاهی هخامنشی | Q389688 | achaemenid | `medes`; `elam` | `argead` |
| `argead` | Argead Macedonian rule (Alexander and successors) |  |  | alexander | `achaemenid` | `seleucid` |
| `seleucid` | Seleucid Empire | امپراتوری سلوکی | Q93180 | seleucid | `argead` | `parthian` (on the Iranian plateau, 148-129 BCE) |
| `persis` | Persis (frataraka dynasts and kings of Persis) | پارس (فرترکه / شاهان پارس) | Q3746183 |  | `seleucid` | `sasanian` |
| `elymais` | Elymais | الیمائی | Q1275158 |  | `seleucid` | `sasanian` |
| `parthian` | Parthian (Arsacid) Empire | شاهنشاهی اشکانی | Q1986139 | parthian | `seleucid` | `sasanian` |
| `sasanian` | Sasanian Empire | شاهنشاهی ساسانی | Q83891 | sasanian | `parthian`; `persis` | `rashidun` |
| `rashidun` | Rashidun Caliphate | خلافت راشدین | Q12490507 | rashidun | `sasanian` | `umayyad` |
| `umayyad` | Umayyad Caliphate | خلافت اموی | Q8575586 | umayyad | `rashidun` | `abbasid` |
| `abbasid` | ʿAbbasid Caliphate | خلافت عباسی | Q12536 | abbasid | `umayyad` | `tahirid` (in Khorasan); `saffarid`; `samanid`; `buyid` (over the caliph in Baghdad 945); `ilkhanate` (1258) |
| `tahirid` | Tahirids | طاهریان | Q373981 |  | `abbasid` | `saffarid` |
| `saffarid` | Saffarids | صفاریان | Q45310 | ca-saffarid | `tahirid` | `ghaznavid`; `samanid` (in Khorasan after 900) |
| `samanid` | Samanids | سامانیان | Q12150341 | samanid | `tahirid`; `saffarid` | `ghaznavid` |
| `ziyarid` | Ziyarids | زیاریان | Q207044 |  | `samanid` | `seljuk` |
| `buyid` | Buyids (Būyids) | آل بویه | Q273874 | buyid | `ziyarid`; `abbasid` | `seljuk` |
| `ghaznavid` | Ghaznavids | غزنویان | Q249578 | in-ghaznavid | `samanid`; `saffarid` | `seljuk` (in Khorasan after Dandānqān 1040) |
| `seljuk` | Great Seljuk Sultanate | امپراتوری سلجوقی | Q3708094 | seljuk | `ghaznavid`; `buyid` | `khwarazmian` |
| `khwarazmian` | Khwarazmshahs (Anuštegin line) | خوارزمشاهیان | Q63134381 | khwarazmian | `seljuk` | `mongol-iran` |
| `mongol-iran` | Mongol Empire: direct rule in Iran (pre-Ilkhanid governors) |  |  | mongol-iran | `khwarazmian` | `ilkhanate` |
| `ilkhanate` | Ilkhanate (Il-Khanids) | ایلخانان | Q178084 | ilkhanate | `mongol-iran`; `abbasid` | `chobanid`; `jalayirid`; `injuid`; `muzaffarid`; `kartid`; `sarbadar` |
| `chobanid` | Chobanids | چوپانیان | Q1089675 |  | `ilkhanate` | `jalayirid` (Azarbaijan taken by Šayḵ Ovays 1359) |
| `jalayirid` | Jalayirids | جلایریان | Q866716 |  | `ilkhanate`; `chobanid` | `qara-qoyunlu`; `timurid` (Timurid occupations of Jalayirid lands) |
| `injuid` | Injuids | آل اینجو | Q1067513 |  | `ilkhanate` | `muzaffarid` |
| `muzaffarid` | Muzaffarids | آل مظفر | Q877670 |  | `ilkhanate`; `injuid` | `timurid` |
| `kartid` | Kartids (Āl-e Kart) | کرتیان | Q1734616 |  | `mongol-iran` | `timurid` |
| `sarbadar` | Sarbadars (Sarbedārs) | سربداران | Q1931074 |  | `ilkhanate` | `timurid` |
| `timurid` | Timurid Empire | امپراتوری تیموری | Q484195 | timurid | `chobanid`; `jalayirid`; `muzaffarid`; `kartid`; `sarbadar`; `injuid` | `qara-qoyunlu` (western Iran from 1452); `aq-qoyunlu`; `safavid` |
| `qara-qoyunlu` | Qara Qoyunlu | قره‌قویونلو | Q324470 |  | `jalayirid`; `timurid` | `aq-qoyunlu` |
| `aq-qoyunlu` | Aq Qoyunlu | آق‌قویونلو | Q555994 | aq-qoyunlu | `qara-qoyunlu`; `timurid` | `safavid` |
| `safavid` | Safavid Iran | ایران صفوی | Q18234383 | safavid-iran | `aq-qoyunlu`; `timurid` | `hotaki`; `afsharid` |
| `hotaki` | Hotaki (Ḡilzay) dynasty | هوتکیان | Q627449 | hotaki | `safavid` | `afsharid` |
| `afsharid` | Afsharid Iran | ایران افشاری | Q63149558 | afsharid-iran | `safavid`; `hotaki` | `zand` (in western and southern Iran); `qajar` |
| `zand` | Zand dynasty |  | Q97629053 | zand-iran | `afsharid`; `safavid` | `qajar` |
| `qajar` | Qajar Iran | ایران قاجاری | Q63158027 | qajar-iran | `zand`; `afsharid` | `pahlavi` |
| `pahlavi` | Pahlavi Iran | ایران پهلوی | Q107258515 | pahlavi-iran | `qajar` | `islamic-republic` |
| `islamic-republic` | Islamic Republic of Iran | جمهوری اسلامی ایران | Q794 | islamic-republic-iran | `pahlavi` |  |

## Periods of control over Iran

Recorded in the draft for polities whose span is wider than their rule over Iran.

- `seleucid`: -312 to -148 (Media held until 148 BCE); scholarly-consensus; sources: eir-seleucid-empire
- `seleucid`: -148 to -141 (Babylonia held until 141 BCE); scholarly-consensus; sources: eir-seleucid-empire
- `rashidun`: 637 to 651 (Qādesiya probably June 637, Šuštar 642, Sistān campaign 650/51 or 651/52); scholarly-consensus; sources: eir-arab-ii-conquest
- `abbasid`: 750 to 821 (direct rule); scholarly-consensus; sources: eir-abbasid-caliphate
- `abbasid`: 821 to 892 (nominal suzerainty over autonomous dynasties; disintegration clear after c. 892); scholarly-consensus; sources: eir-abbasid-caliphate
- `ghaznavid`: 999 to 1040 (Khorasan held from the Samanid collapse until the defeat at Dandānqān, 1040 (start year estimated)); estimate; sources: eir-ghaznavids, eir-khorasan-vi
- `timurid`: 1381 to 1452 (western Iran lost to the Qara Qoyunlu 1452-53); estimate; sources: wp-en-qara-qoyunlu

## Kind

The schema's `kind` is one of state, empire, people, other. The draft's fuller wording is kept here and in each note.

- `elam`: kingdom / succession of dynasties (federal highland-lowland state)
- `medes`: kingdom / tribal confederation (extent and statehood debated)
- `achaemenid`: empire (King of Kings)
- `argead`: empire (Macedonian kingship over the former Achaemenid realm)
- `seleucid`: empire (Macedonian dynasty)
- `persis`: regional dynasty under Seleucid, then Arsacid, suzerainty
- `elymais`: semi-independent kingdom, often under Parthian suzerainty
- `parthian`: empire (King of Kings)
- `sasanian`: empire (King of Kings of Ērān and Anērān)
- `rashidun`: caliphate
- `umayyad`: caliphate
- `abbasid`: caliphate
- `tahirid`: hereditary governorship of Khorasan under the caliphate
- `saffarid`: amirate (Sistan-based)
- `samanid`: amirate
- `ziyarid`: amirate (Ṭabarestān and Gorgān)
- `buyid`: confederation of amirates (Fārs, Jebāl/Ray, Iraq, Kermān)
- `ghaznavid`: sultanate
- `seljuk`: sultanate
- `khwarazmian`: shahdom (Seljuk vassals, then independent empire)
- `mongol-iran`: province(s) of the Mongol Empire under governors
- `ilkhanate`: khanate (Mongol appanage, autonomous from 1260)
- `chobanid`: amirate ruling through puppet il-khans, then in own name
- `jalayirid`: amirate, sultanate from 1356
- `injuid`: governorship turned dynasty (Fārs)
- `muzaffarid`: amirate / sultanate (Yazd, Kerman, Fārs)
- `kartid`: maliks of Herat (Mongol vassals, then independent)
- `sarbadar`: republican-like amirate of notables and dervishes (western Khorasan)
- `timurid`: empire, later appanage states
- `qara-qoyunlu`: Turkmen tribal confederation / sultanate
- `aq-qoyunlu`: Turkmen tribal confederation / sultanate
- `safavid`: shahdom
- `hotaki`: tribal principality (Kandahar), rulers of Isfahan 1722-29
- `afsharid`: shahdom (Nader's empire, then Khorasan principality)
- `zand`: regency (wakil) / khanate
- `qajar`: shahdom; constitutional monarchy from 1906
- `pahlavi`: constitutional monarchy (in form); autocratic in practice
- `islamic-republic`: Islamic republic (velāyat-e faqih)
