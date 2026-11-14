# Contributing

Outside submissions are not open yet.

This is the v0 data layer: schemas, a few illustrations under `examples/`, and a validator. Please do not open pull requests that add polities, rulers, capitals, borders, layers, or sources until submissions are announced. Issues that describe a schema bug or a validator bug are welcome.

## What will be required when submissions open

- One fact, one permanent id, one confidence label, and at least one source. Do not invent a fact, a date, a border, or a citation. If a source is not already a record in `sources/` with a real author, title, year, and a publisher, DOI, or URL, it cannot be cited.
- Ids are permanent lowercase slugs. The filename stem matches the id. Ids are never reused, including ids under `examples/`.
- Every fact has `earliest` and `latest`. Negative years are BCE. `-1` is 1 BCE. This layer does not rewrite year 0.
- Confidence is exactly one of `attested`, `scholarly-consensus`, `estimate`, `reconstructed`, `contested`, `legendary`.
- An estimate has a low, a high, and a method, with low less than or equal to high. A layer estimate uses `value_low`, `value_high`, and `method`.
- A contested fact may list `alternatives`. Each alternative has its own value and its own source ids. Disagreements stay in the file.
- Human-edited files may be YAML or JSON, one document per file. Quote `yes`, `no`, `on`, `off`, `y`, and `n`. Unquoted, YAML 1.1 would turn them into booleans. `true` and `false` may stay unquoted.
- Borders live in `borders/gpl/` or `borders/ccby/`. `provenance: historical-basemaps-gpl` is allowed only under `borders/gpl/`, and that folder cites a source with `dataset: historical-basemaps`. Files under `borders/ccby/` set `provenance: fresh-drawn`, `derived_from_gpl: false`, and `fresh_source` to a source with `dataset: fresh-drawn` and a non-GPL license. A CC-BY border must not cite a GPL source, must not reference a file under `borders/gpl/`, and must not be derived from a GPL shape. One shape per polity, year, and source.
- Illustrations stay under `examples/`, with `example: true` and a note that says `not a historical claim`. They are not results.

## Check a tree

```
python3 -m pip install -r requirements.txt -r requirements-dev.txt
make validate
make test
```

`make bundle` writes per-layer, per-century JSON files and `dist/manifest.json`. Those files are generated. Do not commit `dist/`.

## Licenses

Code is MIT (`LICENSE`). Data is CC-BY-4.0 (`LICENSE-DATA`). Inherited shapes in `borders/gpl/` are GPL-3.0 (`borders/gpl/LICENSE`). Cite the atlas with `CITATION.cff` and `docs/CITING.md`.
