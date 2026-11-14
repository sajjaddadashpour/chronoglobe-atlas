# Citing Chronoglobe Atlas

Cite a fact, or cite a release. Code in this repository is MIT (`LICENSE`). The dataset is CC-BY-4.0 (`LICENSE-DATA`). Shapes under `borders/gpl/` stay GPL-3.0 (`borders/gpl/LICENSE`). Attribute each of those licenses when you share the material it covers. Illustrations under `examples/` are not facts. Do not cite them as history.

## A single fact

A fact's permanent URL is:

```
https://chronoglobe.si/f/<id>@<version>
```

`<id>` is the fact's permanent lowercase slug, the same id as in the file and in the bundle. It does not change when a later release corrects the record. `<version>` is the dataset release, the `version` field in `CITATION.cff`. The URL without `@<version>` means the latest release. Prefer the versioned form, so a reader can open the record you used.

v0.1.0 ships only illustrations. This URL is the shape, not a historical claim:

```
https://chronoglobe.si/f/examplemere@0.1.0
```

The id is unique across polities, rulers, capitals, borders, and layer values. Sources are bibliography entries. Cite a source by its own id and its publisher, DOI, or URL. A source does not get a fact URL.

## A release, and Zenodo

Each numbered GitHub release is archived on [Zenodo](https://zenodo.org/). Zenodo mints a DOI for that version and a concept DOI that covers every version. Record both in `CITATION.cff` under `identifiers` when they exist, and add them to the cite-this forms below.

- The version DOI identifies one release. Use it when the fact URL pins `@<version>`.
- The concept DOI identifies the dataset across releases. Use it when you mean the atlas in general and are not pinning a version.

v0.1.0 has not been archived yet. There is no DOI. Do not invent one. Until `CITATION.cff` lists a DOI, cite the versioned fact URL and the repository.

## Cite this dataset

Replace the version and the year when you cite a later release. Add the Zenodo DOI as soon as this file and `CITATION.cff` publish one.

### APA

Dadashpour, S. (2026). *Chronoglobe Atlas* (Version 0.1.0) [Data set]. https://github.com/sajjaddadashpour/chronoglobe-atlas

### Chicago

Dadashpour, Sajjad. 2026. *Chronoglobe Atlas*. Version 0.1.0. Dataset. https://github.com/sajjaddadashpour/chronoglobe-atlas.

### BibTeX

```bibtex
@dataset{dadashpour2026chronoglobe,
  author = {Dadashpour, Sajjad},
  title = {Chronoglobe Atlas},
  year = {2026},
  version = {0.1.0},
  url = {https://github.com/sajjaddadashpour/chronoglobe-atlas},
  note = {Code MIT. Data CC-BY-4.0. borders/gpl/ is GPL-3.0. DOI pending Zenodo archive.}
}
```

## Cite one fact

Use the fact's `name` (or `place`, for a capital) as the title. Keep the version in the URL. This example uses an illustration id:

### APA

Dadashpour, S. (2026). Examplemere. In *Chronoglobe Atlas* (Version 0.1.0). https://chronoglobe.si/f/examplemere@0.1.0

### Chicago

Dadashpour, Sajjad. 2026. "Examplemere." In *Chronoglobe Atlas*, version 0.1.0. https://chronoglobe.si/f/examplemere@0.1.0.

### BibTeX

```bibtex
@misc{dadashpour2026examplemere,
  author = {Dadashpour, Sajjad},
  title = {Examplemere},
  year = {2026},
  howpublished = {Chronoglobe Atlas, version 0.1.0},
  url = {https://chronoglobe.si/f/examplemere@0.1.0},
  note = {Illustration id, not a historical claim.}
}
```

When you cite a real fact, drop the illustration note, keep the confidence label and the fact's sources next to your claim, and name the license of any border you redrew or redistributed. A CC-BY fact and a GPL border are not the same license.
