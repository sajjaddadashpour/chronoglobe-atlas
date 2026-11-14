"""Validate Chronoglobe JSON and YAML against schema/ plus the citation rules.

Rules enforced here, on top of JSON Schema:

- Every fact has a permanent id: a lowercase slug, unique in the tree, and
  equal to the filename stem.
- Every fact cites at least one source id that exists in sources/.
- Every fact has an earliest year and a latest year. Negative years are BCE.
  earliest must be less than or equal to latest.
- Exactly one confidence label: attested, scholarly-consensus, estimate,
  reconstructed, contested, legendary.
- An estimate requires a low, a high, and a method, with low <= high.
  Layer estimates use value_low, value_high, and method.
- Contested facts may carry alternatives. Each alternative has sources.
  Alternatives on any other label are rejected.
- An unquoted YAML scalar yes/no/on/off/y/n (any case) is rejected. YAML 1.1
  would silently turn those words into booleans. Quote them.
- Border provenance historical-basemaps-gpl is allowed only under borders/gpl/.
  borders/ccby/ must be fresh-drawn, must name a fresh-drawn source, and must
  not derive from GPL shapes.
- One border shape per polity, year, and source.
- Files under examples/ are illustrations: example true, and a note that says
  they are not a historical claim.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError
from referencing import Registry, Resource
from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError as RuamelYAMLError
from yaml.scanner import ScannerError
from yaml.tokens import ScalarToken

# Words YAML 1.1 treats as booleans and YAML 1.2 leaves as strings.
# true/false are real booleans in both and are allowed.
YAML11_BOOL_WORDS = frozenset({"yes", "no", "on", "off", "y", "n"})

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXAMPLE_MARK = "not a historical claim"
GPL_PROVENANCE = "historical-basemaps-gpl"
FRESH_PROVENANCE = "fresh-drawn"
LAYER_NAMES = frozenset({"population", "gdp", "climate", "governance"})
DATA_SUFFIXES = frozenset({".json", ".yaml", ".yml"})
TREES = ("sources", "polities", "rulers", "capitals", "borders", "layers", "examples")
FACT_KINDS = frozenset({"polity", "ruler", "capital", "border", "layer"})
KIND_BY_DIR = {
    "sources": "source",
    "polities": "polity",
    "rulers": "ruler",
    "capitals": "capital",
    "borders": "border",
    "layers": "layer",
}

SCHEMA_FILES = {
    "source": "source.schema.json",
    "polity": "polity.schema.json",
    "ruler": "ruler.schema.json",
    "capital": "capital.schema.json",
    "border": "border.schema.json",
    "layer": "layer.schema.json",
}


@dataclass(frozen=True)
class Issue:
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


@dataclass
class LoadedDocument:
    path: str
    kind: str
    document: dict
    resolved_geometry: dict | None = None


@dataclass
class Report:
    issues: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)
    documents: list[LoadedDocument] = field(default_factory=list)
    files_checked: int = 0

    @property
    def ok(self) -> bool:
        return not self.issues


def repo_root() -> Path:
    """Directory that contains verify/ and schema/."""
    return Path(__file__).resolve().parents[1]


def validate_root(root: Path) -> Report:
    """Validate one atlas root. Fixture trees reuse this repo's schema/."""
    root = root.resolve()
    report = Report()
    try:
        validators = load_validators(schema_dir_for(root))
    except (OSError, json.JSONDecodeError, SchemaError, KeyError) as exc:
        report.issues.append(Issue("schema", f"could not load schemas: {exc}"))
        return report

    for path in _discover(root):
        _validate_file(root, path, validators, report)
    report.issues.extend(cross_check(report.documents))
    return report


def schema_dir_for(root: Path) -> Path:
    local = root / "schema"
    if (local / "source.schema.json").is_file():
        return local
    packaged = repo_root() / "schema"
    if (packaged / "source.schema.json").is_file():
        return packaged
    raise FileNotFoundError(f"no schema directory under {root} or {repo_root()}")


def load_validators(schema_dir: Path) -> dict[str, Draft202012Validator]:
    resources: list[tuple[str, Resource]] = []
    schemas: dict[str, dict] = {}
    for path in sorted(schema_dir.glob("*.json")):
        contents = json.loads(path.read_text(encoding="utf-8"))
        schemas[path.name] = contents
        schema_id = contents.get("$id")
        if isinstance(schema_id, str):
            resources.append((schema_id, Resource.from_contents(contents)))
    registry = Registry().with_resources(resources)
    validators = {
        kind: Draft202012Validator(schemas[filename], registry=registry)
        for kind, filename in SCHEMA_FILES.items()
    }
    validators["geometry"] = Draft202012Validator(
        {"$ref": "https://chronoglobe.si/schema/v0/common.schema.json#/$defs/geometry"},
        registry=registry,
    )
    return validators


def cross_check(documents: list[LoadedDocument]) -> list[Issue]:
    issues: list[Issue] = []
    issues.extend(_duplicate_ids(documents))
    source_ids = _ids_of(documents, "source")
    polity_ids = _ids_of(documents, "polity")
    ruler_ids = _ids_of(documents, "ruler")
    sources_by_id = {
        doc.document["id"]: doc.document
        for doc in documents
        if doc.kind == "source" and isinstance(doc.document.get("id"), str)
    }
    for doc in documents:
        issues.extend(_document_rules(doc, source_ids, polity_ids, ruler_ids, sources_by_id))
    issues.extend(_border_keys(documents))
    return issues


def yaml11_bool_issues(text: str, path: str) -> list[Issue]:
    """Plain scalars YAML 1.1 would coerce to bool. Quoted scalars are kept.

    ``true`` and ``false`` are real booleans in YAML 1.2 and are not flagged.
    """
    issues: list[Issue] = []
    try:
        tokens = list(yaml.scan(text))
    except (ScannerError, yaml.YAMLError) as exc:
        return [Issue(path, f"YAML parse error: {exc}")]
    for token in tokens:
        if not isinstance(token, ScalarToken) or not token.plain:
            continue
        if token.value.lower() not in YAML11_BOOL_WORDS:
            continue
        line = token.start_mark.line + 1
        column = token.start_mark.column + 1
        issues.append(
            Issue(
                path,
                (
                    f"line {line}, column {column}: unquoted YAML scalar {token.value!r} "
                    "would be a boolean under YAML 1.1 (yes/no/on/off/y/n, any case); quote it"
                ),
            )
        )
    return issues


def border_slot(path: str) -> str:
    """Return ``gpl`` or ``ccby`` when the file lives in that license folder."""
    parts = path.split("/")
    try:
        index = parts.index("borders")
    except ValueError:
        return ""
    if index + 1 >= len(parts) - 1:
        return ""
    slot = parts[index + 1]
    if slot in {"gpl", "ccby"}:
        return slot
    return ""


def layer_folder(path: str) -> str:
    parts = path.split("/")
    try:
        index = parts.index("layers")
    except ValueError:
        return ""
    if index + 1 >= len(parts) - 1:
        return ""
    return parts[index + 1]


def kind_for(path: str) -> str | None:
    parts = path.split("/")
    if parts[0] == "examples":
        parts = parts[1:]
    if not parts:
        return None
    return KIND_BY_DIR.get(parts[0])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="verify",
        description="Validate the Chronoglobe Atlas data layer.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Atlas root to validate (default: the repository that contains verify/).",
    )
    args = parser.parse_args(argv)
    root = (args.root or repo_root()).resolve()
    report = validate_root(root)
    for warning in report.warnings:
        print(f"warning: {warning}")
    if report.issues:
        for issue in report.issues:
            print(issue, file=sys.stderr)
        print(f"{len(report.issues)} problem(s) in {root}", file=sys.stderr)
        return 1
    if report.warnings:
        print(f"valid ({report.files_checked} files, {len(report.warnings)} warnings)")
    else:
        print(f"valid ({report.files_checked} files)")
    return 0


def _discover(root: Path) -> list[Path]:
    found: list[Path] = []
    for tree in TREES:
        directory = root / tree
        if not directory.is_dir():
            continue
        for path in sorted(item for item in directory.rglob("*") if item.is_file()):
            relative = path.relative_to(root)
            if any(part.startswith(".") for part in relative.parts):
                continue
            if path.suffix.lower() not in DATA_SUFFIXES:
                continue
            found.append(path)
    return found


def _validate_file(
    root: Path,
    path: Path,
    validators: dict[str, Draft202012Validator],
    report: Report,
) -> None:
    rel = path.relative_to(root).as_posix()
    report.files_checked += 1
    kind = kind_for(rel)
    if kind is None:
        report.issues.append(
            Issue(
                rel,
                "data files must live under sources/, polities/, rulers/, capitals/, borders/, layers/, or examples/ of those",
            )
        )
        return
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        report.issues.append(Issue(rel, f"not valid UTF-8: {exc}"))
        return

    suffix = path.suffix.lower()
    if suffix in {".yaml", ".yml"}:
        traps = yaml11_bool_issues(text, rel)
        if traps:
            report.issues.extend(traps)
            return
        try:
            data = _load_yaml(text)
        except (RuamelYAMLError, ValueError) as exc:
            report.issues.append(Issue(rel, f"YAML parse error: {exc}"))
            return
    else:
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            report.issues.append(Issue(rel, f"JSON parse error: line {exc.lineno}: {exc.msg}"))
            return

    if not isinstance(data, dict):
        report.issues.append(Issue(rel, "document must be one JSON object"))
        return

    _schema_issues(validators[kind], data, rel, report)
    document = LoadedDocument(path=rel, kind=kind, document=data)
    if kind == "border":
        document.resolved_geometry = _border_geometry(root, rel, data, validators["geometry"], report)
    report.documents.append(document)


def _load_yaml(text: str) -> object:
    loader = YAML(typ="safe")
    documents = list(loader.load_all(text))
    while documents and documents[-1] is None:
        documents.pop()
    if len(documents) != 1:
        raise ValueError(f"expected one YAML document, found {len(documents)}")
    return documents[0]


def _schema_issues(validator: Draft202012Validator, document: object, path: str, report: Report) -> None:
    for error in sorted(validator.iter_errors(document), key=lambda err: list(err.absolute_path)):
        location = "/" + "/".join(str(part) for part in error.absolute_path)
        if not location.strip("/"):
            location = "(root)"
        report.issues.append(Issue(path, f"{location}: {error.message}"))


def _border_geometry(
    root: Path,
    rel: str,
    data: dict,
    geometry_validator: Draft202012Validator,
    report: Report,
) -> dict | None:
    has_geometry = "geometry" in data
    has_ref = "geometry_ref" in data
    if has_geometry == has_ref:
        report.issues.append(
            Issue(rel, "border needs a GeoJSON geometry or a geometry_ref, and not both")
        )
        if not has_geometry:
            return None
    if has_geometry:
        geometry = data.get("geometry")
        if isinstance(geometry, dict):
            report.issues.extend(_closure_issues(geometry, rel))
            return geometry
        return None

    ref = data.get("geometry_ref")
    if not isinstance(ref, str):
        return None
    target, problem = _geometry_ref_target(root, rel, ref)
    if problem or target is None:
        report.issues.append(Issue(rel, problem or "geometry_ref does not resolve"))
        return None
    try:
        payload = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        report.issues.append(Issue(rel, f"geometry_ref {ref!r} is not JSON: {exc}"))
        return None
    geometry, problems = _geometry_from_geojson(payload, rel)
    report.issues.extend(problems)
    if geometry is None:
        return None
    _schema_issues(geometry_validator, geometry, rel, report)
    report.issues.extend(_closure_issues(geometry, rel))
    return geometry


def _geometry_ref_target(root: Path, rel: str, ref: str) -> tuple[Path | None, str | None]:
    if ref.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", ref) or ref.startswith("~"):
        return None, "geometry_ref must be a repository-relative path"
    if "\\" in ref or any(part == ".." for part in Path(ref).parts):
        return None, "geometry_ref must not contain '..'"
    if not ref.endswith(".geojson"):
        return None, "geometry_ref must point at a .geojson file"
    slot = border_slot(rel)
    parts = rel.split("/")
    try:
        index = parts.index("borders")
    except ValueError:
        return None, "geometry_ref is only allowed on a border"
    if not slot:
        return None, "border files must live in borders/gpl/ or borders/ccby/ before they can reference a shape"
    license_prefix = "/".join(parts[: index + 2])
    ref_posix = Path(ref).as_posix()
    if not ref_posix.startswith(license_prefix + "/"):
        if slot == "ccby" and "/gpl/" in f"/{ref_posix}/":
            return None, "borders/ccby/ must not reference a GPL shape"
        if slot == "gpl" and "/ccby/" in f"/{ref_posix}/":
            return None, "borders/gpl/ must not reference a ccby shape"
        return None, f"geometry_ref must stay inside {license_prefix}/"
    if slot == "ccby" and "/gpl/" in f"/{ref_posix}/":
        return None, "borders/ccby/ must not reference a GPL shape"
    candidate = (root / ref).resolve()
    allowed = (root / license_prefix).resolve()
    if not candidate.is_relative_to(allowed):
        return None, "geometry_ref escapes its license folder"
    if not candidate.is_file():
        return None, f"geometry_ref {ref!r} does not resolve to a file"
    return candidate, None


def _geometry_from_geojson(data: object, path: str) -> tuple[dict | None, list[Issue]]:
    if not isinstance(data, dict):
        return None, [Issue(path, "geometry_ref must contain a GeoJSON object")]
    kind = data.get("type")
    if kind in {"Polygon", "MultiPolygon"}:
        return data, []
    if kind == "Feature":
        geometry = data.get("geometry")
        if isinstance(geometry, dict) and geometry.get("type") in {"Polygon", "MultiPolygon"}:
            return geometry, []
        return None, [Issue(path, "geometry_ref Feature geometry must be a Polygon or MultiPolygon")]
    if kind == "FeatureCollection":
        features = data.get("features")
        if not isinstance(features, list) or len(features) != 1:
            return None, [
                Issue(path, "geometry_ref FeatureCollection must contain exactly one feature (one shape)")
            ]
        return _geometry_from_geojson(features[0], path)
    return None, [
        Issue(
            path,
            "geometry_ref must be a Polygon, MultiPolygon, Feature, or single-feature FeatureCollection",
        )
    ]


def _closure_issues(geometry: dict, path: str) -> list[Issue]:
    kind = geometry.get("type")
    coordinates = geometry.get("coordinates")
    issues: list[Issue] = []
    if kind == "Polygon" and isinstance(coordinates, list):
        for index, ring in enumerate(coordinates):
            issues.extend(_ring_closed(ring, path, f"geometry ring {index}"))
    elif kind == "MultiPolygon" and isinstance(coordinates, list):
        for poly_index, polygon in enumerate(coordinates):
            if not isinstance(polygon, list):
                continue
            for ring_index, ring in enumerate(polygon):
                issues.extend(_ring_closed(ring, path, f"geometry polygon {poly_index} ring {ring_index}"))
    return issues


def _ring_closed(ring: object, path: str, where: str) -> list[Issue]:
    if not isinstance(ring, list) or len(ring) < 4:
        return []
    if ring[0] != ring[-1]:
        return [Issue(path, f"{where} is not closed (first and last position differ)")]
    return []


def _duplicate_ids(documents: list[LoadedDocument]) -> list[Issue]:
    by_id: dict[str, list[str]] = {}
    for doc in documents:
        doc_id = doc.document.get("id")
        if isinstance(doc_id, str):
            by_id.setdefault(doc_id, []).append(doc.path)
    issues: list[Issue] = []
    for doc_id, paths in sorted(by_id.items()):
        if len(paths) > 1:
            listed = ", ".join(paths)
            issues.append(Issue(paths[0], f"duplicate id {doc_id!r} at {listed}"))
    return issues


def _ids_of(documents: list[LoadedDocument], kind: str) -> set[str]:
    return {
        doc.document["id"]
        for doc in documents
        if doc.kind == kind and isinstance(doc.document.get("id"), str)
    }


def _document_rules(
    doc: LoadedDocument,
    source_ids: set[str],
    polity_ids: set[str],
    ruler_ids: set[str],
    sources_by_id: dict[str, dict],
) -> list[Issue]:
    issues: list[Issue] = []
    data = doc.document
    doc_id = data.get("id")
    if isinstance(doc_id, str) and not SLUG_RE.fullmatch(doc_id):
        issues.append(
            Issue(
                doc.path,
                f"id {doc_id!r} must be a permanent lowercase slug (letters, digits, single hyphens)",
            )
        )
    if isinstance(doc_id, str) and doc_id != Path(doc.path).stem:
        issues.append(
            Issue(doc.path, f"id {doc_id!r} must match the filename stem {Path(doc.path).stem!r}")
        )
    issues.extend(_example_rules(doc))
    for name in ("name", "title", "place", "unit", "method", "subject"):
        value = data.get(name)
        if isinstance(value, str) and not value.strip():
            issues.append(Issue(doc.path, f"{name} must not be blank"))

    if doc.kind == "source":
        if not any(_nonblank(data.get(key)) for key in ("publisher", "doi", "url")):
            issues.append(Issue(doc.path, "source must include a publisher, a doi, or a url"))
        issues.extend(_source_dataset_rules(doc))
        return issues

    issues.extend(_span_rules(doc))
    issues.extend(_citation_rules(doc, source_ids))
    issues.extend(_estimate_rules(doc))
    issues.extend(_alternative_rules(doc, source_ids))
    if doc.kind in {"ruler", "capital", "border"} or (doc.kind == "layer" and "polity" in data):
        issues.extend(_polity_ref(doc, polity_ids))
    if doc.kind == "ruler":
        issues.extend(_succession_rules(doc, ruler_ids))
    if doc.kind == "border":
        issues.extend(_border_rules(doc, source_ids, sources_by_id))
    if doc.kind == "layer":
        issues.extend(_layer_rules(doc))
    return issues


def _example_rules(doc: LoadedDocument) -> list[Issue]:
    under_examples = doc.path.startswith("examples/")
    marked = doc.document.get("example") is True
    issues: list[Issue] = []
    if under_examples and not marked:
        issues.append(Issue(doc.path, "files under examples/ must set example: true"))
    if marked and not under_examples:
        issues.append(Issue(doc.path, "example: true is only allowed under examples/"))
    if under_examples or marked:
        note = doc.document.get("note")
        if not isinstance(note, str) or EXAMPLE_MARK not in note.casefold():
            issues.append(
                Issue(doc.path, f"example files must include {EXAMPLE_MARK!r} in note")
            )
    return issues


def _source_dataset_rules(doc: LoadedDocument) -> list[Issue]:
    dataset = doc.document.get("dataset")
    license_name = doc.document.get("license")
    if dataset == "historical-basemaps" and not _is_gpl_license(license_name):
        return [Issue(doc.path, "dataset historical-basemaps requires a GPL license")]
    if dataset == "fresh-drawn" and (not _nonblank(license_name) or _is_gpl_license(license_name)):
        return [Issue(doc.path, "dataset fresh-drawn requires a non-GPL license")]
    return []


def _span_rules(doc: LoadedDocument) -> list[Issue]:
    earliest = doc.document.get("earliest")
    latest = doc.document.get("latest")
    if _is_int(earliest) and _is_int(latest) and earliest > latest:
        return [
            Issue(
                doc.path,
                "earliest must be <= latest (negative years are BCE; -1 is 1 BCE)",
            )
        ]
    return []


def _citation_rules(doc: LoadedDocument, source_ids: set[str]) -> list[Issue]:
    who = doc.document.get("id")
    name = who if isinstance(who, str) else doc.path
    return _unknown_sources(
        doc.path,
        doc.document.get("sources"),
        source_ids,
        f"{doc.kind} {name!r} must cite at least one source id that resolves in sources/",
        f"{doc.kind} {name!r} cites source ids that are not in sources/",
    )


def _unknown_sources(
    path: str,
    sources: object,
    source_ids: set[str],
    empty_message: str,
    unknown_message: str,
) -> list[Issue]:
    if not isinstance(sources, list) or len(sources) == 0:
        return [Issue(path, empty_message)]
    unknown = [item for item in sources if not isinstance(item, str) or item not in source_ids]
    if not unknown:
        return []
    listed = ", ".join(repr(item) for item in unknown)
    return [Issue(path, f"{unknown_message}: {listed}")]


def _estimate_rules(doc: LoadedDocument) -> list[Issue]:
    if doc.document.get("confidence") != "estimate":
        return []
    if doc.kind == "layer":
        low = doc.document.get("value_low")
        high = doc.document.get("value_high")
        low_name, high_name = "value_low", "value_high"
    else:
        low = doc.document.get("low")
        high = doc.document.get("high")
        low_name, high_name = "low", "high"
    method = doc.document.get("method")
    missing: list[str] = []
    if not _is_number(low):
        missing.append(low_name)
    if not _is_number(high):
        missing.append(high_name)
    if not _nonblank(method):
        missing.append("method")
    if missing:
        listed = ", ".join(missing)
        return [Issue(doc.path, f"confidence estimate requires {listed}")]
    if low > high:
        return [Issue(doc.path, f"confidence estimate requires {low_name} <= {high_name}")]
    return []


def _alternative_rules(doc: LoadedDocument, source_ids: set[str]) -> list[Issue]:
    alternatives = doc.document.get("alternatives")
    if alternatives is None:
        return []
    if doc.document.get("confidence") != "contested":
        return [Issue(doc.path, "alternatives are only allowed when confidence is contested")]
    if not isinstance(alternatives, list):
        return []
    issues: list[Issue] = []
    for index, alternative in enumerate(alternatives):
        if not isinstance(alternative, dict):
            continue
        issues.extend(
            _unknown_sources(
                doc.path,
                alternative.get("sources"),
                source_ids,
                f"alternative {index} must cite at least one source id that resolves in sources/",
                f"alternative {index} cites source ids that are not in sources/",
            )
        )
        for low_name, high_name in (("value_low", "value_high"), ("low", "high")):
            low = alternative.get(low_name)
            high = alternative.get(high_name)
            if _is_number(low) and _is_number(high) and low > high:
                issues.append(Issue(doc.path, f"alternative {index} requires {low_name} <= {high_name}"))
    return issues


def _polity_ref(doc: LoadedDocument, polity_ids: set[str]) -> list[Issue]:
    polity = doc.document.get("polity")
    if isinstance(polity, str) and polity not in polity_ids:
        return [Issue(doc.path, f"polity {polity!r} does not resolve to a polity")]
    return []


def _succession_rules(doc: LoadedDocument, ruler_ids: set[str]) -> list[Issue]:
    succession = doc.document.get("succession")
    if succession is None:
        return []
    if not isinstance(succession, list):
        return []
    issues: list[Issue] = []
    own_id = doc.document.get("id")
    for index, link in enumerate(succession):
        if not isinstance(link, dict):
            continue
        ruler_id = link.get("id")
        if not isinstance(ruler_id, str):
            continue
        if ruler_id == own_id:
            issues.append(Issue(doc.path, f"succession link {index} must not point at the ruler itself"))
        elif ruler_id not in ruler_ids:
            issues.append(
                Issue(doc.path, f"succession id {ruler_id!r} does not resolve to a ruler")
            )
    return issues


def _border_rules(
    doc: LoadedDocument,
    source_ids: set[str],
    sources_by_id: dict[str, dict],
) -> list[Issue]:
    issues: list[Issue] = []
    data = doc.document
    slot = border_slot(doc.path)
    provenance = data.get("provenance")
    derived = data.get("derived_from_gpl")
    if not slot:
        issues.append(Issue(doc.path, "border files must live in borders/gpl/ or borders/ccby/"))
    if provenance == GPL_PROVENANCE and slot != "gpl":
        issues.append(
            Issue(
                doc.path,
                "provenance 'historical-basemaps-gpl' is allowed only under borders/gpl/",
            )
        )
    if slot == "gpl":
        issues.extend(_gpl_border_rules(doc, sources_by_id))
    elif slot == "ccby":
        issues.extend(_ccby_border_rules(doc, source_ids, sources_by_id))
    year = data.get("year")
    earliest = data.get("earliest")
    latest = data.get("latest")
    if _is_int(year) and _is_int(earliest) and _is_int(latest) and (year < earliest or year > latest):
        issues.append(Issue(doc.path, "year must lie inside earliest and latest"))
    if derived is True and provenance != GPL_PROVENANCE:
        issues.append(
            Issue(
                doc.path,
                "derived_from_gpl true is only allowed with provenance 'historical-basemaps-gpl' under borders/gpl/",
            )
        )
    return issues


def _gpl_border_rules(doc: LoadedDocument, sources_by_id: dict[str, dict]) -> list[Issue]:
    issues: list[Issue] = []
    data = doc.document
    if data.get("provenance") != GPL_PROVENANCE:
        issues.append(
            Issue(doc.path, "borders/gpl/ requires provenance 'historical-basemaps-gpl'")
        )
    if data.get("derived_from_gpl") is not True:
        issues.append(
            Issue(
                doc.path,
                "borders/gpl/ shapes are inherited from historical-basemaps, so derived_from_gpl must be true",
            )
        )
    if "fresh_source" in data:
        issues.append(Issue(doc.path, "borders/gpl/ must not declare a fresh_source"))
    cited = _cited_sources(data, sources_by_id)
    if not any(source.get("dataset") == "historical-basemaps" for source in cited):
        issues.append(
            Issue(
                doc.path,
                "a historical-basemaps-gpl border must cite a source whose dataset is historical-basemaps",
            )
        )
    return issues


def _ccby_border_rules(
    doc: LoadedDocument,
    source_ids: set[str],
    sources_by_id: dict[str, dict],
) -> list[Issue]:
    issues: list[Issue] = []
    data = doc.document
    if data.get("provenance") != FRESH_PROVENANCE:
        issues.append(Issue(doc.path, "borders/ccby/ must declare provenance 'fresh-drawn'"))
    if data.get("derived_from_gpl") is not False:
        issues.append(
            Issue(
                doc.path,
                "borders/ccby/ must not derive from GPL shapes (derived_from_gpl must be false)",
            )
        )
    fresh = data.get("fresh_source")
    sources = data.get("sources")
    if not isinstance(fresh, str):
        issues.append(
            Issue(
                doc.path,
                "borders/ccby/ must declare fresh_source, a source id that resolves in sources/",
            )
        )
    else:
        if fresh not in source_ids:
            issues.append(
                Issue(doc.path, f"fresh_source {fresh!r} does not resolve in sources/")
            )
        elif not isinstance(sources, list) or fresh not in sources:
            issues.append(Issue(doc.path, "fresh_source must be listed in sources"))
        else:
            record = sources_by_id.get(fresh, {})
            if record.get("dataset") != "fresh-drawn":
                issues.append(
                    Issue(doc.path, "fresh_source must have dataset 'fresh-drawn'")
                )
            if not _nonblank(record.get("license")) or _is_gpl_license(record.get("license")):
                issues.append(Issue(doc.path, "fresh_source must carry a non-GPL license"))
    for source in _cited_sources(data, sources_by_id):
        if source.get("dataset") == "historical-basemaps" or _is_gpl_license(source.get("license")):
            source_id = source.get("id")
            issues.append(
                Issue(
                    doc.path,
                    f"borders/ccby/ must not cite a GPL or historical-basemaps source ({source_id!r})",
                )
            )
    return issues


def _cited_sources(data: dict, sources_by_id: dict[str, dict]) -> list[dict]:
    sources = data.get("sources")
    if not isinstance(sources, list):
        return []
    return [sources_by_id[item] for item in sources if isinstance(item, str) and item in sources_by_id]


def _layer_rules(doc: LoadedDocument) -> list[Issue]:
    issues: list[Issue] = []
    data = doc.document
    folder = layer_folder(doc.path)
    layer = data.get("layer")
    if folder not in LAYER_NAMES:
        issues.append(
            Issue(
                doc.path,
                "layer files must live in layers/population/, layers/gdp/, layers/climate/, or layers/governance/",
            )
        )
    elif isinstance(layer, str) and layer != folder:
        issues.append(Issue(doc.path, f"layer {layer!r} must match the directory {folder!r}"))
    polity = data.get("polity")
    subject = data.get("subject")
    has_polity = isinstance(polity, str) and bool(polity)
    has_subject = isinstance(subject, str) and bool(subject.strip())
    if not has_polity and not has_subject:
        issues.append(Issue(doc.path, "layer value must name a polity id or a subject"))
    low = data.get("value_low")
    high = data.get("value_high")
    if _is_number(low) and _is_number(high) and low > high:
        issues.append(Issue(doc.path, "value_low must be <= value_high"))
    return issues


def _border_keys(documents: list[LoadedDocument]) -> list[Issue]:
    seen: dict[tuple[str, int, str], str] = {}
    issues: list[Issue] = []
    for doc in documents:
        if doc.kind != "border":
            continue
        polity = doc.document.get("polity")
        year = doc.document.get("year")
        sources = doc.document.get("sources")
        if not isinstance(polity, str) or not _is_int(year) or not isinstance(sources, list):
            continue
        for source in sources:
            if not isinstance(source, str):
                continue
            key = (polity, year, source)
            previous = seen.get(key)
            if previous is not None:
                issues.append(
                    Issue(
                        doc.path,
                        (
                            f"duplicate border for polity {polity!r}, year {year}, source {source!r} "
                            f"(also {previous})"
                        ),
                    )
                )
            else:
                seen[key] = doc.path
    return issues


def _is_gpl_license(value: object) -> bool:
    return isinstance(value, str) and "gpl" in value.lower()


def _nonblank(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


if __name__ == "__main__":
    sys.exit(main())
