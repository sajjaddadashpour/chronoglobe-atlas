# Schema v0.2: decision sheet for Sajjad

This is a plain-English reading of the 14 proposals in `docs/iran/SCHEMA_PROPOSALS.md` (atlas `main`). Nothing in the schema, the validator, or any data file is changed on this branch. The point is to decide what v0.2 should hold before the South Asia pass begins.

Every fact in the atlas still needs a source, a confidence label, and a date range. Where sources disagree, every reading is kept, one per source. The recommendations below are about whether the schema can hold that cleanly, or whether we would again have to hide the extra detail in `note` fields, as we did in the Iran passes.

Recommendations are **yes** (put it in v0.2), **no**, or **defer** (not needed for South Asia 1700–1947; come back later). They are grouped into what we should lock before the South Asia pass, and what can wait.

## Must have before South Asia

These are the places where v0 already failed us on Iran, and where eighteenth- and nineteenth-century South Asia will fail in the same way, only more often: overlapping claims, nominal Mughal sovereignty, peshwas and residents, and princely states under British paramountcy.

### 1. Separate start and end bounds on date facts

- **What it is:** Give a fact its own start bounds and end bounds (each with earliest, latest, and a display string such as "c. 1707" or "1501/02"), instead of one outer `earliest`/`latest` pair for the whole span.
- **Why it matters:** Many accessions are a short disputed range, while the death or deposition is a known year. South Asia will also have A.H. years that span two A.D. years, which we already keep as bounds. One outer pair cannot show both things exactly.
- **Recommendation: yes**

### 2. Labels per bound

- **What it is:** Allow a confidence label on the start and a different one on the end.
- **Why it matters:** A state's beginning can be contested (when does Hyderabad stop being a Mughal province and become a polity of its own?) while its end is attested. A single label has to choose the weaker one, which misleads the reader.
- **Recommendation: yes**

### 3. Meaning of `low` / `high` on estimated dates

- **What it is:** Say clearly what `low` and `high` mean on a date fact, or let the start and end bounds satisfy the estimate. Today those fields just repeat `earliest`/`latest`.
- **Why it matters:** If we do not lock this, every new estimate in the South Asia pass will keep copying the same numbers into two places, and a later reader may think they are a separate measurement.
- **Recommendation: yes** (a clarification, and if possible stop requiring a separate `low`/`high` when the bounds already carry the range). This does not add a new kind of fact.

### 5. Unknown bounds

- **What it is:** Allow a start or an end to be marked unknown, instead of forcing a year. Today 16 Iran records borrow the polity's outer bound, and two undated kings could not be entered at all.
- **Why it matters:** Many princely-state reigns, and some eighteenth-century accessions, are only partly dated. Borrowing the polity's span makes a guess look like a source.
- **Recommendation: yes**

### 6. Alternatives on legendary and other labels

- **What it is:** Let `alternatives` appear on facts that are not only `contested` (including `legendary` and `reconstructed`), and let each alternative carry its own confidence label and its own dates.
- **Why it matters:** This is how we keep every source's reading, which is the rule you have already set. Deioces could not use `alternatives` because the fact was `legendary`. South Asia will have contested borders and competing chronologies that are scholarly, not legendary; those need the same structure, one reading per source.
- **Recommendation: yes**

### 7. Polity names and identifiers

- **What it is:** Store sourced names in more than one language, alternative names, and stable identifiers (especially a Wikidata id).
- **Why it matters:** The cite button and the goal of Chronoglobe as a citable atlas need a stable id and a proper name, not only an English snapshot label. South Asia also needs Persian, Urdu, Hindi and other forms (Awadh / Oudh, Mysore / Mahisur, and so on).
- **Recommendation: yes**

### 8. Polity succession

- **What it is:** Add predecessor and successor polity ids, as rulers already have, and let the validator check that those ids exist.
- **Why it matters:** The Mughal breakup, the East India Company giving way to the Raj, the Sikh misls giving way to Ranjit Singh's empire, and the Raj giving way to India and Pakistan are succession facts. Leaving them only in notes makes the globe harder to walk and easier to get wrong.
- **Recommendation: yes**

### 9. Categorical governance

- **What it is:** Let the governance layer store a category from a controlled list (for example "subsidiary-alliance princely state" or "Company presidency"), instead of a dummy 1/1 measurement.
- **Why it matters:** The difference between British India, a princely state under paramountcy, and a still-independent successor state is a core fact of this period, not a number.
- **Recommendation: yes**

### 10. Ruler role, and capital role

- **What it is:** Add a role on rulers (claimant, regent, co-ruler, puppet, interregnum) and on capitals (capital, seat, residence, dynastic centre). Today this is buried in `note`.
- **Why it matters:** South Asia is full of double offices: a Chhatrapati and a peshwa, a nizam and a British resident, a nawab under Mughal suzerainty then under the Company, and claimants such as Bahadur Shah II in 1857. A note cannot be filtered or checked.
- **Recommendation: yes**

### 11. Partial control

- **What it is:** Record periods when a polity controlled only part of a region, or held nominal rather than effective rule, with dates, a region, sources and a confidence label.
- **Why it matters:** This is the central mapping problem of South Asia from 1707 to 1947. The later Mughals, Maratha chauth, Durrani claims in the Punjab, and British paramountcy over princely states cannot be drawn as tidy, non-overlapping countries without inventing a false picture.
- **Recommendation: yes**

### 12. Source fields

- **What it is:** Add `consulted` (and how), `tier` (scholarly, primary, news, secondary-crosscheck), `accessed`, `revision`, `editors` and `isbn` to sources, and refuse a fact whose only sources are `consulted: no`. Today this lives in the source `note`.
- **Why it matters:** Iran pass 2 still had 171 rulers that rest only on Wikipedia. The validator should enforce the rule we already write by hand: a fact needs a source we actually opened.
- **Recommendation: yes**

## Later

These matter, but they are not what will block a careful 1700–1947 South Asia pass.

### 4. Open-ended spans

- **What it is:** Mark a span as still going on, instead of setting `latest` to the year of the pass (Iran used 2026).
- **Why it matters:** India, Pakistan, Bangladesh, Nepal, Sri Lanka and others continue after 1947, and the Islamic Republic records already have this problem. Almost every polity in a 1700–1947 pass has a real end date, so the pass can proceed without it.
- **Recommendation: defer** until we edit present-day states, then yes.

### 13. Open questions as data

- **What it is:** Keep open questions next to the record they concern, as a list on the record or as an `issues/` collection, instead of only in a markdown file.
- **Why it matters:** It would make unanswered items harder to lose. The Iran method (`docs/iran/OPEN_QUESTIONS.md`) worked well enough to copy for South Asia for now.
- **Recommendation: defer**

### 14. Relative or synchronism dating

- **What it is:** Allow a date to be a king-list position or a synchronism with another reign ("dated Shu-Sin 6") without converting it into an absolute year.
- **Why it matters:** This is what Potts's Shimashki tables needed, and what we must not invent a chronology to fill. It is not how 1700–1947 South Asia is dated. Those years use A.D. and A.H. calendars.
- **Recommendation: defer** until an ancient Near Eastern or similarly documented pass, then yes.

## Summary

| No. | Proposal | Recommendation | When |
|----:|----------|----------------|------|
| 1 | Separate start and end bounds | yes | before South Asia |
| 2 | Labels per bound | yes | before South Asia |
| 3 | Clarify `low`/`high` on date estimates | yes | before South Asia |
| 4 | Open-ended spans | defer | later |
| 5 | Unknown bounds | yes | before South Asia |
| 6 | Alternatives on more labels | yes | before South Asia |
| 7 | Names and identifiers | yes | before South Asia |
| 8 | Polity succession | yes | before South Asia |
| 9 | Categorical governance | yes | before South Asia |
| 10 | Ruler and capital roles | yes | before South Asia |
| 11 | Partial control | yes | before South Asia |
| 12 | Source fields and a consulted-source gate | yes | before South Asia |
| 13 | Open questions as data | defer | later |
| 14 | Relative or synchronism dating | defer | later |

No proposal is recommended as a no. If v0.2 needs to be cut down, the ones I would not drop before South Asia are **1, 2, 6, 10, 11 and 12**. Those are the ones that stop us inventing tidy dates, hiding disagreement, or drawing the successor states as if they were modern countries.

Once you mark each row yes, no, or defer, Chief of Staff can implement the approved changes. The schema itself should not move until you say so.
