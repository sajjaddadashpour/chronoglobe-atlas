# Chronoglobe Atlas

The open, sourced data behind [chronoglobe.si](https://chronoglobe.si): polities, rulers, capitals, borders and layers (population, GDP, climate, governance) through time. It's built so people and agents can keep making it more accurate.

**Status: v0 skeleton.** The schemas and validator come next.

## The rules
- Every fact cites at least one entry in `sources/`.
- Every date has an earliest and a latest bound.
- Every fact carries one label: `attested`, `scholarly-consensus`, `estimate`, `reconstructed`, `contested`, or `legendary`.
- Estimates come with a low value, a high value and a method. Disagreements are kept and shown, not hidden.
- Every fact has a permanent ID and a versioned link, and every release gets a DOI.

## Layout
```
sources/     one shared bibliography
polities/    states, empires, peoples, with dated ranges
rulers/      rulers and successions
capitals/    capitals by date
borders/     gpl/ = inherited historical-basemaps shapes (GPL-3.0); ccby/ = freshly drawn (CC-BY-4.0)
layers/      population, GDP, climate, governance values with ranges and methods
schema/      JSON Schemas
verify/      validator and bundle builder
docs/        design docs
```

## License
Code is under MIT (`LICENSE`). Data is under CC-BY-4.0 (`LICENSE-DATA`), except `borders/gpl/`, which stays GPL-3.0 (`borders/gpl/LICENSE`).
