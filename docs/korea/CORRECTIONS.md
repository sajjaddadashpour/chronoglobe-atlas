# Corrections to old chronoglobe Korea data

Old data: `sajjaddadashpour/chronoglobe` (`data/polities.json`, `data/rulers/*.json`, `data/capitals/*.json`, main at 8bcc27d). Mapping old id to new ids, then the main changes. A generated old-vs-new comparison is at the end.

## Polities

- `kr-gojoseon` (400-108 BCE) becomes `gojoseon` and `wiman-joseon`. Gojoseon's start is contested: 2333 BCE is the legendary date and the firm attestation is the mid-4th century BCE. Both are kept as alternatives, so `earliest` is now -2333 (outer bound). The 400 BCE start had no source. Wiman Joseon (c. 194/195-108 BCE) is now its own polity.
- `kr-samhan` (100 BCE-300 CE) is split into `mahan`, `jinhan` and `byeonhan`. Same century encoding, now each cited to its EKC article.
- `kr-gaya` (42-562) becomes `gaya` (1st c. BCE-562) plus member states `geumgwan-gaya` (contested start 42 CE vs turn of the era, to 532) and `daegaya` (contested start, to 562). Old data used Suro's legendary 42 CE as an uncontested start.
- `kr-goguryeo` start (-37) is now contested between 37 BCE (Samguk sagi) and the 1st century BCE or earlier. `kr-baekje` (-18) is contested between 18 BCE and 3rd-century statehood. `kr-silla` (-57) is contested on the early chronology.
- New polities that were missing: `jin`, `buyeo`, `okjeo`, `dongye`, `later-baekje` (892/900-936), `taebong` (901-918).
- `kr-japanese-rule` is now `japanese-korea`, `kr-usamgik` is `usamgik`, `kr-soviet-admin` is `soviet-civil-administration`, `c-north-korea` is `north-korea`, `c-south-korea` is `south-korea`. The spans are unchanged; the sources are now EKC.

## Rulers

- Old lists were partial (e.g. Goguryeo 7, Baekje 6, Silla 7, Goryeo 13 kings). They are now complete wherever a year exists: Goguryeo 28, Baekje 32 (incl. Buyeo Pung), Silla 29 + Unified Silla 27, Goryeo 38 records (34 kings; 4 with two reigns), Joseon 26, Balhae 15, Geumgwan Gaya 10.
- Gwanggaeto: old 391-413 is now contested. The stele gives 391-412, Samguk sagi 392-413, Wikipedia 391-412.
- Jangsu: old 413-491; now contested between EKC 413-490 and Wikipedia 412-491.
- Munmu: old `kr-silla` 661-668 plus `kr-unified-silla` 661-681 (a duplicate). Now one record, `unified-silla-munmu` 661-681, with a note that he acceded in 661.
- Chungnyeol: old single 1274-1308. Now two reigns, 1274-1298 and 1298-1308, with Chungseon's 1298 reign between them. Chungsuk and Chunghye are also split.
- Joseon Gojong: old 1864-1897; now contested (EKC 1863, Wikipedia 1864).
- Gojoseon Jun: old -220 to -194; now -220 to -195 (Wikipedia), with EKC confirming him as the last king before Wiman; years secondary-only.
- Japanese governors-general: added the missing Ugaki Kazushige (acting, 1927) and Saitō Makoto's second term (1929-31). There are now 10 records.
- North Korea: the old list mixed 11 premiers with the leaders, and Kim Il-sung appeared twice (premier 1948-72, leader 1948-94). Now only the three supreme leaders (1948-94, 1994-2011, 2011-). Premiers are left for a separate office list.
- South Korea: added all acting presidents in the Wikipedia timeline (Ho Chong twice, Kwak Sang-hoon, Baek Nak-jun, Park Choong-hoon, Goh Kun, Hwang Kyo-ahn, Han Duck-soo twice, Choi Sang-mok, Lee Ju-ho). Park Chung Hee is now acting president 1962-63 plus president 1963-79 (not split at 1972). Chun Doo-hwan is now one record, 1980-88 (old data split it at 1981; the 1981 Fifth Republic change is a governance period).
- USAMGIK and the Soviet administration had no rulers. Now: Hodge, Arnold, Lerch, Dean and Ahn Chai-hong; Shtykov, Romanenko, Lebedev, and Kim Il-sung as committee chairman 1946-48.

## Capitals

- Goguryeo: Gungnae 3-427 is kept but the 3 CE move is contested. Added Hwando-seong (209-246). Pyongyang is split at 586 into the Anhak/Daeseong-san phase (427-586) and Jangan-seong (586-668).
- Balhae: old data had Dongmo 698-742 and Sanggyeong 755-926, with a gap 742-755 and Donggyeong missing. Now Dongmo-san 698-742, Junggyeong 742-755/756, Sanggyeong 755/756-785/late 780s, Donggyeong 785-794, Sanggyeong again 793/794-926.
- Gaya: old data had Goryeong as the Gaya capital only after Gimhae's surrender in 532. EKC puts Daegaya at Goryeong throughout, leading the later league from the mid-5th century. Now Goryeong is the capital of daegaya over its own span and Gimhae that of geumgwan-gaya.
- Goryeo: added Cheorwon 918-919 before the move to Gaegyeong.
- Gojoseon: old "Wanggeom-seong (near Pyongyang)" stated the Pyongyang theory as fact. The location is now contested (Liaoning / migration / Pyongyang; for Wiman Joseon, Pyongyang vs Liaodong Xiandu).
- Added capitals for buyeo (contested location), later-baekje (Mujinju, Wansanju), taebong (Cheorwon, Songak, Cheorwon) and soviet-civil-administration (Pyongyang).

## Generated comparison (old vs new, by script)

Lists ruler records whose old span differs from the new outer span, old records with no counterpart, and the capitals on each side. Name matching is automatic and may miss renamed rulers (e.g. "Bojang" vs "Go Bojang"); treat it as a checklist.

### `kr-gojoseon` (Gojoseon) 400 BCE to 108 BCE -> `gojoseon` 2333 BCE to 108 BCE, `wiman-joseon` 195 BCE to 108 BCE

Rulers: old 1, new 5.
- Old `Jun of Gojoseon` -220 to -194 -> `gojoseon-jun` -220 to -195 (scholarly-consensus).

Capitals: old 1 (Wanggeom-seong (near Pyongyang) -400--108), new 2 (centre of Gojoseon (location contested) -361--195; Wanggeom-seong (location contested) -195--108).

### `kr-samhan` (Samhan (Mahan, Jinhan, Byeonhan)) 100 BCE to 300 CE -> `mahan` 100 BCE to 300 CE, `jinhan` 100 BCE to 300 CE, `byeonhan` 100 BCE to 300 CE

Rulers: old 0, new 0.

Capitals: old 0 (), new 0 ().

### `kr-goguryeo` (Goguryeo) 37 BCE to 668 CE -> `goguryeo` 100 BCE to 668 CE

Rulers: old 7, new 28.
- Old `Jangsu` 413 to 491 -> `goguryeo-jangsu` 412 to 491 (contested).

Capitals: old 3 (Jolbon -37-3; Gungnae (Ji'an) 3-427; Pyongyang 427-668), new 5 (Jolbon (Huanren area) -37-3; Gungnae-seong (Ji'an) 3-427; Hwando-seong (Ji'an) 209-246; Pyongyang (Anhak Palace / Daeseong-san) 427-586; Jangan-seong (Pyongyang) 586-668).

### `kr-baekje` (Baekje) 18 BCE to 660 CE -> `baekje` 18 BCE to 660 CE

Rulers: old 6, new 32.

Capitals: old 3 (Wiryeseong (Seoul area) -18-475; Ungjin (Gongju) 475-538; Sabi (Buyeo) 538-660), new 3 (Hanseong / Wirye-seong (Seoul) -18-475; Ungjin (Gongju) 475-538; Sabi (Buyeo) 538-660).

### `kr-silla` (Silla) 57 BCE to 668 CE -> `silla` 57 BCE to 668 CE

Rulers: old 7, new 29.
- Old `Munmu` 661 to 668 -> `unified-silla-munmu` 661 to 681 (scholarly-consensus).

Capitals: old 1 (Seorabeol (Gyeongju) -57-668), new 1 (Geumseong / Seorabeol (Gyeongju) -57-668).

### `kr-gaya` (Gaya confederacy) 42 CE to 562 CE -> `gaya` 100 BCE to 562 CE, `geumgwan-gaya` 50 BCE to 532 CE, `daegaya` 42 CE to 562 CE

Rulers: old 0, new 10.

Capitals: old 2 (Gimhae (Geumgwan Gaya) 42-532; Goryeong (Daegaya) 532-562), new 2 (Gimhae -50-532; Goryeong 42-562).

### `kr-unified-silla` (Unified Silla) 668 CE to 935 CE -> `unified-silla` 668 CE to 935 CE

Rulers: old 6, new 27.

Capitals: old 1 (Gyeongju 668-935), new 1 (Gyeongju (Geumseong) 668-935).

### `kr-balhae` (Balhae) 698 CE to 926 CE -> `balhae` 698 CE to 926 CE

Rulers: old 5, new 15.

Capitals: old 2 (Dongmo Mountain 698-742; Sanggyeong 755-926), new 5 (Dongmo-san (Chengshanzi, Dunhua) 698-742; Junggyeong Hyeondeok-bu (Xigucheng, Helong) 742-756; Sanggyeong Yongcheon-bu (Dongjingcheng, Ning'an) 755-794; Donggyeong Yongwon-bu (Hunchun) 785-794; Sanggyeong Yongcheon-bu (Dongjingcheng, Ning'an) 793-926).

### `kr-goryeo` (Goryeo) 918 CE to 1392 CE -> `goryeo` 918 CE to 1392 CE

Rulers: old 13, new 38.
- Old `Chungnyeol` 1274 to 1308 -> `goryeo-chungnyeol` 1274 to 1298 (scholarly-consensus).

Capitals: old 3 (Gaegyeong (Kaesong) 918-1232; Ganghwa 1232-1270; Gaegyeong (Kaesong) 1270-1392), new 4 (Cheorwon 918-919; Gaegyeong (Kaesong) 919-1232; Ganghwa 1232-1270; Gaegyeong (Kaesong) 1270-1392).

### `kr-joseon` (Joseon) 1392 CE to 1897 CE -> `joseon` 1392 CE to 1897 CE

Rulers: old 17, new 26.
- Old `Gojong` 1864 to 1897 -> `joseon-gojong` 1863 to 1897 (contested).

Capitals: old 2 (Gaegyeong (Kaesong) 1392-1394; Hanseong (Seoul) 1394-1897), new 2 (Gaegyeong (Kaesong) 1392-1394; Hanseong (Hanyang, Seoul) 1394-1897).

### `kr-korean-empire` (Korean Empire) 1897 CE to 1910 CE -> `korean-empire` 1897 CE to 1910 CE

Rulers: old 2, new 2.

Capitals: old 1 (Hanseong (Seoul) 1897-1910), new 1 (Hanseong (Seoul) 1897-1910).

### `kr-japanese-rule` (Korea under Japanese rule (Chōsen)) 1910 CE to 1945 CE -> `japanese-korea` 1910 CE to 1945 CE

Rulers: old 8, new 10.

Capitals: old 1 (Keijō (Seoul) 1910-1945), new 1 (Keijō (Seoul) 1910-1945).

### `kr-usamgik` (United States Army Military Government in Korea) 1945 CE to 1948 CE -> `usamgik` 1945 CE to 1948 CE

Rulers: old 0, new 5.

Capitals: old 1 (Seoul 1945-1948), new 1 (Seoul 1945-1948).

### `kr-soviet-admin` (Soviet Civil Administration in North Korea) 1945 CE to 1948 CE -> `soviet-civil-administration` 1945 CE to 1948 CE

Rulers: old 0, new 4.

Capitals: old 0 (), new 1 (Pyongyang 1945-1948).

### `c-north-korea` (North Korea) 1948 CE to present -> `north-korea` 1948 CE to 2026 CE

Rulers: old 14, new 3.
- Old `Kim Il-sung` 1948 to 1972 -> `north-korea-kim-il-sung` 1948 to 1994 (scholarly-consensus).
- Old `Kim Il` 1972 to 1976 -> `soviet-civil-administration-kim-il-sung` 1946 to 1948 (scholarly-consensus).
- Old `Pak Song-chol` 1976-1977 (Premier of North Korea): no matching record in this pass.
- Old `Yon Hyong-muk` 1988-1992 (Premier of North Korea): no matching record in this pass.
- Old `Hong Song-nam` 1998-2003 (Premier of North Korea): no matching record in this pass.
- Old `Pak Pong-ju` 2003-2007 (Premier of North Korea): no matching record in this pass.
- Old `Kim Yong-il` 2007-2010 (Premier of North Korea): no matching record in this pass.
- Old `Choe Yong-rim` 2010-2013 (Premier of North Korea): no matching record in this pass.
- Old `Pak Pong-ju` 2013-2019 (Premier of North Korea): no matching record in this pass.
- Old `Kim Jae-ryong` 2019-2020 (Premier of North Korea): no matching record in this pass.
- Old `Kim Tok-hun` 2020-None (Premier of North Korea): no matching record in this pass.
- Old `Kim Il-sung` 1948-1994 (Supreme Leader of North Korea): no matching record in this pass.

Capitals: old 1 (Pyongyang 1948-None), new 1 (Pyongyang 1948-2026).

### `c-south-korea` (South Korea) 1948 CE to present -> `south-korea` 1948 CE to 2026 CE

Rulers: old 18, new 26.
- Old `Park Chung-hee` 1963 to 1972 -> `south-korea-park-chung-hee-2` 1963 to 1979 (scholarly-consensus).
- Old `Park Chung-hee` 1972-1979 (President of South Korea): no matching record in this pass.
- Old `Chun Doo-hwan` 1980 to 1981 -> `south-korea-chun-doo-hwan` 1980 to 1988 (scholarly-consensus).
- Old `Chun Doo-hwan` 1981-1988 (President of South Korea): no matching record in this pass.

Capitals: old 1 (Seoul 1948-None), new 1 (Seoul 1948-2026).
