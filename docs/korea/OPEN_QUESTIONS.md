# Open questions (Korea pass 1)

Rule: nothing that could not be checked against a source opened this pass was filled in.

## A. Sources not consulted

- Samguk sagi, Samguk yusa, Goryeosa: no edition was opened. Facts that go back to them are cited through EKC articles. Pass 2 should cite a specific edition (e.g. the National Institute of Korean History online texts on db.history.go.kr, which this pass did not open) and add page or juan references.
- Lee Ki-baik, *A New History of Korea* (1984); Michael J. Seth, *A History of Korea* (2010): in `sources/` as not consulted, and cited by no fact.
- *Cambridge History of Korea* vol. 1: not opened; no source record made.
- Wikipedia pages fetched but not used for any fact (Parhae, Old Chosŏn, Kaya confederacy, Jin (Korean state)): not added to `sources/`.

## B. Rulers left out (no usable year)

- Gojoseon (Old Joseon): Gija (row reign: 1122(?) – ? BC) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Buyeo: Hae Buru (row reign: none) - no reign year in the sources read
- Buyeo: Galsa (row reign: 21–?) - Galsa is the founder of a separate Buyeo offshoot (EKC treats 갈사 as a state); not a ruler of buyeo. No polity record made.
- Buyeo: Hae Dodu (row reign: ?–68) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Buyeo: Butae (row reign: none) - no reign year in the sources read
- Buyeo: Wigutae (row reign: none) - no reign year in the sources read
- Buyeo: Ganwigeo (row reign: none) - no reign year in the sources read
- Buyeo: Maryeo (row reign: none) - no reign year in the sources read
- Buyeo: Uiryeo (row reign: ?–285) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Buyeo: Uira (row reign: 286–?) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Buyeo: Hyeon (row reign: ?–346) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Buyeo: Yeoul (row reign: ?–384) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Daegaya: Ijinasi (row reign: 42 AD–?) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found
- Daegaya: Geumnim (row reign: none) - no reign year in the sources read
- Daegaya: Haji (row reign: none) - no reign year in the sources read
- Daegaya: Gasil (row reign: none) - no reign year in the sources read
- Daegaya: Inoe (row reign: none) - no reign year in the sources read
- Daegaya: Wolgwang (row reign: ?–562) - one bound unknown and the polity bound would give an implausible span; no EKC article with dates found

Also not modelled: DPRK premiers and presidents other than the supreme leaders; ROK prime ministers; Japanese Residents-General 1906-1910 (Itō, Sone, Terauchi); US military governor Helmick (1948-49, after the ROK began); kings of Okjeo, Dongye, the Samhan statelets and Gaya states other than Geumgwan Gaya.

## C. Facts flagged by the automatic cross-check

The script checked whether the stored years occur in the cited EKC text. Every flagged fact has a known reason:

- 300 / 101 / 200 / 50 / 440-460 type years are encodings of a century or "around the turn of the era" (Jin, Buyeo, Okjeo, Dongye, Samhan, Geumgwan Gaya).
- 195 BCE comes from the Wikipedia end date of Jun (EKC gives 194 for Wiman); it is used as the outer start of wiman-joseon and its capital and governance.
- 42 for Daegaya is derived (562 minus the 520 years in the Samguk sagi count reported by EKC).
- 919 = "the next year" after 918 (EKC 철원군: Goryeo moved to Songak the year after its founding).
- 412 (Jangsu), 259 (Geodeung), 895 (Dae Hyeonseok), 1864 (Cheoljong) are the Wikipedia side of a contested pair.
- 220 (Jun) and 1944 (Abe) come from Wikipedia; the EKC article is cited only for existence or the 1945 surrender.

- `wiman-joseon` (polity): years not found in the cited EKC text(s): [195]
- `jin` (polity): years not found in the cited EKC text(s): [101, 300]
- `buyeo` (polity): years not found in the cited EKC text(s): [200]
- `okjeo` (polity): years not found in the cited EKC text(s): [195, 300]
- `dongye` (polity): years not found in the cited EKC text(s): [195, 300]
- `mahan` (polity): years not found in the cited EKC text(s): [300]
- `jinhan` (polity): years not found in the cited EKC text(s): [300]
- `byeonhan` (polity): years not found in the cited EKC text(s): [300]
- `geumgwan-gaya` (polity): years not found in the cited EKC text(s): [50]
- `gojoseon-jun` (ruler): years not found in the cited EKC text(s): [220]
- `wiman-joseon-ugeo` (ruler): years not found in the cited EKC text(s): [195]
- `goguryeo-jangsu` (ruler): years not found in the cited EKC text(s): [412]
- `geumgwan-gaya-geodeung` (ruler): years not found in the cited EKC text(s): [259]
- `balhae-dae-hyeonseok` (ruler): years not found in the cited EKC text(s): [895]
- `joseon-cheoljong` (ruler): years not found in the cited EKC text(s): [1864]
- `japanese-korea-abe-nobuyuki` (ruler): years not found in the cited EKC text(s): [1944]
- `gojoseon-capital-centre-of-gojoseon` (capital): years not found in the cited EKC text(s): [195]
- `wiman-joseon-capital-wanggeom-seong` (capital): years not found in the cited EKC text(s): [195]
- `buyeo-capital-buyeo-seong` (capital): years not found in the cited EKC text(s): [200]
- `geumgwan-gaya-capital-gimhae` (capital): years not found in the cited EKC text(s): [50]
- `daegaya-capital-goryeong` (capital): years not found in the cited EKC text(s): [42]
- `goryeo-capital-cheorwon` (capital): years not found in the cited EKC text(s): [919]
- `goryeo-capital-gaegyeong` (capital): years not found in the cited EKC text(s): [919]
- `wiman-joseon-governance-01` (governance): years not found in the cited EKC text(s): [195]
- `buyeo-governance-01` (governance): years not found in the cited EKC text(s): [200]
- `mahan-governance-01` (governance): years not found in the cited EKC text(s): [300]
- `jinhan-governance-01` (governance): years not found in the cited EKC text(s): [300]
- `byeonhan-governance-01` (governance): years not found in the cited EKC text(s): [300]
- `geumgwan-gaya-governance-01` (governance): years not found in the cited EKC text(s): [50]
- `daegaya-governance-01` (governance): years not found in the cited EKC text(s): [42]

## D. Dates or facts to check in pass 2

- Unified Silla start: 668 (fall of Goguryeo) vs 676 (end of the Silla-Tang war). Only 668 is encoded.
- Okjeo and Dongye: end dates (absorption by Goguryeo) are not given in the sources read; 300 is a placeholder outer bound.
- Mahan: the end of the last Mahan statelets (4th to 6th century, debated) is not encoded.
- Joseon: the court's return to Gaegyeong in 1399-1405 is not encoded.
- Unified Silla: the abandoned 689 plan to move the capital to Dalgubeol is mentioned in a note but not checked.
- DPRK capital: the 1948 constitution named Seoul as capital until 1972. Not checked in a source opened this pass; only Pyongyang (provisional capital from 1946, per EKC) is encoded.
- ROK: the wartime capitals (Daejeon, Daegu, Busan, 1950-53) are not encoded.
- ROK governance: the constitutional form of each republic (presidential, parliamentary in 1960-61, Yushin 1972-81) needs a scholarly source; only the period headings are encoded.
- Soviet Civil Administration: exact start date (only the year 1945 is encoded) and its relation to the People's Committees, from a scholarly source.
- Gojong of Joseon (1863 vs 1864) and other one-year EKC/Wikipedia differences: check against Samguk sagi / Goryeosa / Joseon Wangjo Sillok with lunar dates.
- Balhae: Gang's accession (EKC header 795, body 794) and Dae Won-ui's end (793 vs 794).
- Hwando-seong's second capital phase from 342: end not given.

## E. Schema notes (no change made; see docs/iran/SCHEMA_PROPOSALS.md)

- The Iran proposals apply here too: a place/geometry reference for capitals, separate start and end labels, `contested-location` for capitals whose site is disputed (Gojoseon, Wanggeom-seong, Buyeo), and an `office` field to separate kings, presidents, acting presidents and committee chairs.
- Membership relations (geumgwan-gaya and daegaya in gaya; Samhan statelets) and overlordship (Goryeo under Yuan, Korea under the Japanese protectorate) are only in notes and governance layers.

## F. Rulers with one bound filled from the polity bound

- `wiman-joseon-wi-man`: no end year (row: 194–? BC); stored span 194 BCE / 108 BCE
- `wiman-joseon-ugeo`: no start year (row: ?–108 BC); stored span 195 BCE / 108 BCE
