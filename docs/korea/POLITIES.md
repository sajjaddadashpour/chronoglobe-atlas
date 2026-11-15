# Korea polities: names, identifiers and succession

The v0 polity schema has one `name` and no fields for other languages, Wikidata ids or polity succession. This table keeps them; each record's `note` repeats the Korean name and the dating.
Korean names are the kowiki titles (or, where the English Wikipedia page has no kowiki sitelink, the hangul from the polity note), and Wikidata ids come from the English Wikipedia pageprops lookup consulted for this pass (source `wp-en-wikidata-korea`, secondary, cache `_work/wd.json`). Neither has been checked for scope.

The "old chronoglobe id" column is the site polity id in `sajjaddadashpour/chronoglobe` (`data/polities.json`). An old id may point at only one atlas id (the site build stops on a conflict), so a split old record is mapped once, to the best-matching new id. The choices are listed after the table.

| id | English name | Korean | Wikidata | old chronoglobe id | predecessors | successors |
|---|---|---|---|---|---|---|
| `gojoseon` | Gojoseon (Old Joseon) | 고조선 | Q28405 | kr-gojoseon |  | `wiman-joseon` |
| `jin` | Jin (Jinguk) | 진국 | Q1155101 |  |  | `mahan`; `jinhan`; `byeonhan` (on the reading that Jin existed) |
| `wiman-joseon` | Wiman Joseon | 위만조선 | Q703340 |  | `gojoseon` | Han commanderies (not modelled) |
| `buyeo` | Buyeo | 부여 | Q28511 |  |  | `goguryeo` |
| `okjeo` | Okjeo | 옥저 | Q713393 |  |  | `goguryeo` |
| `dongye` | Dongye (Ye) | 동예 | Q105946539 |  |  | `goguryeo`; `silla` (not resolved) |
| `mahan` | Mahan | 마한 | Q704278 | kr-samhan | `jin` | `baekje` |
| `jinhan` | Jinhan | 진한 | Q701273 |  | `jin` | `silla` |
| `byeonhan` | Byeonhan (Byeonjin) | 변한 | Q1378584 |  | `jin` | `gaya` |
| `gaya` | Gaya confederacy | 가야 | Q28084 | kr-gaya | `byeonhan` | `silla` (fall of Daegaya, 562) |
| `geumgwan-gaya` | Geumgwan Gaya (Garak-guk) | 금관가야 | Q715210 |  |  | `silla` (surrender, 532); member of `gaya` |
| `daegaya` | Daegaya | 대가야 | Q1157054 |  |  | `silla` (fall, 562); member of `gaya` |
| `goguryeo` | Goguryeo | 고구려 | Q28370 | kr-goguryeo | `buyeo` | `unified-silla`; `balhae` (claims of continuity contested) |
| `baekje` | Baekje | 백제 | Q28428 | kr-baekje | `mahan` | `unified-silla` |
| `silla` | Silla (to 668) | 신라 | Q28456 | kr-silla | `jinhan` | `unified-silla` |
| `unified-silla` | Unified Silla (Later Silla) | 통일신라 | Q715257 | kr-unified-silla | `silla`; `baekje`; `goguryeo` | `goryeo` |
| `balhae` | Balhae (Bohai) | 발해 | Q28322 | kr-balhae | `goguryeo` (claims of continuity contested) | Liao (Khitan, not modelled); refugees to `goryeo` |
| `later-baekje` | Later Baekje (Hubaekje) | 후백제 | Q698239 |  |  | `goryeo` |
| `taebong` | Later Goguryeo / Majin / Taebong | 태봉 | Q699871 |  |  | `goryeo` |
| `goryeo` | Goryeo | 고려 | Q28208 | kr-goryeo | `taebong`; `later-baekje`; `unified-silla` | `joseon` |
| `joseon` | Joseon | 조선 | Q28179 | kr-joseon | `goryeo` | `korean-empire` |
| `korean-empire` | Korean Empire (Daehan Jeguk) | 대한제국 | Q28233 | kr-korean-empire | `joseon` | `japanese-korea` |
| `japanese-korea` | Korea under Japanese rule (Chōsen) | 일제강점기 | Q503585 | kr-japanese-rule | `korean-empire` | `usamgik`; `soviet-civil-administration` |
| `usamgik` | United States Army Military Government in Korea | 재조선 미국 육군사령부 군정청 | Q484104 | kr-usamgik | `japanese-korea` | `south-korea` |
| `soviet-civil-administration` | Soviet Civil Administration in Korea | 소비에트 민정청 | Q15242873 | kr-soviet-admin | `japanese-korea` | `north-korea` |
| `south-korea` | Republic of Korea (South Korea) | 대한민국 | Q884 | c-south-korea | `usamgik` |  |
| `north-korea` | Democratic People's Republic of Korea (North Korea) | 조선민주주의인민공화국 | Q423 | c-north-korea | `soviet-civil-administration` |  |

## Mapping decisions (old site ids and snapshot names)

An old chronoglobe id cannot be pointed at two atlas ids. Three old records were split in this pass; each is mapped to one atlas id.

- `kr-gojoseon` / snapshot `Gojoseon` → `gojoseon`, not `wiman-joseon`. The old id covered 400–108 BCE, which includes Wiman Joseon (c. 194–108 BCE), but the surviving `Gojoseon` polygons are in the −400, −323, −300 and −200 snapshots, all before Wiman's coup. `wiman-joseon` has no separate old id or polygon.
- `kr-samhan` / snapshot `Samhan` → `mahan`, not `jinhan` or `byeonhan`. The old record was one "Samhan (Mahan, Jinhan, Byeonhan)" polity. Mahan was the largest of the three confederations (54 statelets in the Sanguozhi, against 12 each for Jinhan and Byeonhan). There is no `Samhan` polygon in the current `public/data/world_*.geojson` snapshots; the name exists only in `data/polities.json`.
- `kr-gaya` / snapshot `Gaya` → `gaya`, not `geumgwan-gaya` or `daegaya`. The atlas still has a confederacy record, and the `Gaya` polygons (years 100, 200, 300, 400) show the league rather than a single member state. `geumgwan-gaya` and `daegaya` have no separate old ids or polygons. The site snapshots list had no `Gaya` entry (the polygons pointed nowhere); the site wiring adds `"Gaya": ["kr-gaya"]` so the existing old-id path can open the card. Borders are unchanged.

One-to-one old ids, unchanged except for the atlas slug: `kr-goguryeo` → `goguryeo` (snapshot names `Goguryeo` and `Koguryo`), `kr-baekje` → `baekje` (`Baekje`, `Paekche`), `kr-silla` → `silla` (`Silla` before 668), `kr-unified-silla` → `unified-silla` (`Unified Silla`, `Silia`, and `Silla` from 668), `kr-balhae` → `balhae` (`Balhae`, `Parhae`), `kr-goryeo` → `goryeo` (`Goryeo`, and `Korea` in the Goryeo span), `kr-joseon` → `joseon` (`Joseon`, and `Korea` in the Joseon span), `kr-korean-empire` → `korean-empire` (`Korean Empire`, and `Korea` in 1897–1910), `kr-japanese-rule` → `japanese-korea` (`Korea under Japanese rule`), `kr-usamgik` → `usamgik` (`Korea (USA)`), `kr-soviet-admin` → `soviet-civil-administration` (`Korea (USSR)`), `c-south-korea` → `south-korea` (`South Korea`, `Korea, Republic of`), `c-north-korea` → `north-korea` (`North Korea`, `Korea, Democratic People's Republic of`).

New polities with no old site id and no snapshot polygon: `jin`, `wiman-joseon`, `buyeo`, `okjeo`, `dongye`, `jinhan`, `byeonhan`, `geumgwan-gaya`, `daegaya`, `later-baekje`, `taebong`.

## Snapshot names not mapped

These `NAME` values appear on the Korean peninsula in `public/data/world_*.geojson` but are not mapped to an atlas polity.

- `Koreans` (year −2000) and `Paleo-Koreans` (years −1500, −1000, −700): people or culture labels in the inherited basemap, not a state in this pass. Mapping them to `gojoseon` would treat the legendary 2333 BCE start as a fact.
- `Jin` in the year 300 snapshot: a Chinese Jin-dynasty polygon that happens to touch the peninsula bounding box. Korean Jin (`jin`, 진국) is a 3rd-to-2nd-century BCE polity and has no snapshot polygon. The year 400 `Jin` polygon does not meet the peninsula.

## Kind

The schema's `kind` is one of state, empire, people, other. The draft's fuller wording is kept in each note.

- `gojoseon`: kingdom (start and centre contested)
- `jin`: state (existence debated)
- `wiman-joseon`: kingdom
- `buyeo`: kingdom
- `okjeo`: people / polity group
- `dongye`: people
- `mahan`: confederation of statelets
- `jinhan`: confederation of statelets
- `byeonhan`: confederation of statelets
- `gaya`: confederacy (never unified)
- `geumgwan-gaya`: kingdom; member of the Gaya confederacy
- `daegaya`: kingdom; member of the Gaya confederacy
- `goguryeo`: kingdom
- `baekje`: kingdom
- `silla`: kingdom (to 668; atlas split)
- `unified-silla`: kingdom (from 668; atlas split)
- `balhae`: kingdom
- `later-baekje`: kingdom
- `taebong`: kingdom
- `goryeo`: kingdom
- `joseon`: kingdom
- `korean-empire`: empire (protectorate from 1905/1906 is a governance period)
- `japanese-korea`: colony administered by the Government-General of Chōsen
- `usamgik`: military occupation administration (south of the 38th parallel)
- `soviet-civil-administration`: military occupation administration (north of the 38th parallel)
- `south-korea`: republic
- `north-korea`: republic
