# Chronoglobe Atlas

The open, sourced data behind [chronoglobe.si](https://chronoglobe.si): polities, rulers, capitals, borders and layers (population, GDP, climate, governance) through time. It's built so people and agents can keep making it more accurate.

**Status: v0 data layer.** Schemas, a validator, and a few illustrations under `examples/`. Those illustrations are not historical claims. Outside submissions are not open yet (`CONTRIBUTING.md`).

## The rules
- Every fact cites at least one entry in `sources/`.
- Every date has an earliest and a latest bound. Negative years are BCE.
- Every fact carries one label: `attested`, `scholarly-consensus`, `estimate`, `reconstructed`, `contested`, or `legendary`.
- Estimates come with a low value, a high value and a method. Disagreements are kept and shown, not hidden.
- Every fact has a permanent ID and a versioned link (`docs/CITING.md`), and every release gets a DOI.
- `historical-basemaps-gpl` borders live only under `borders/gpl/`. Borders under `borders/ccby/` are freshly drawn and do not derive from GPL shapes.
- Hand-edited YAML must quote `yes`, `no`, `on`, `off`, `y`, and `n`. Unquoted, YAML 1.1 would turn them into booleans.

## Layout
```
sources/     one shared bibliography
polities/    states, empires, peoples, with dated ranges
rulers/      rulers and successions
capitals/    capitals by date
borders/     gpl/ = inherited historical-basemaps shapes (GPL-3.0); ccby/ = freshly drawn (CC-BY-4.0)
layers/      population, GDP, climate, governance values with ranges and methods
examples/    illustrations of the schemas, marked example: true, not historical claims
schema/      JSON Schemas (draft 2020-12)
verify/      validator, tests, and the bundle builder
docs/        citing
```

## Check locally
```
python3 -m pip install -r requirements.txt -r requirements-dev.txt
make validate
make test
```
`make validate` runs `python3 -m verify`. `make bundle` writes small per-layer, per-century JSON files and `dist/manifest.json` after a clean check. Those files are generated; do not commit `dist/`. Agents should read `llms.txt`.

## License
Code is under MIT (`LICENSE`). Data is under CC-BY-4.0 (`LICENSE-DATA`), except `borders/gpl/`, which stays GPL-3.0 (`borders/gpl/LICENSE`).
