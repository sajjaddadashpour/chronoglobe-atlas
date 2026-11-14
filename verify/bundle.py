"""Build per-layer, per-century JSON bundles under dist/.

The bundles are a generated release artifact. Do not commit them.
A record is copied into every century its date span overlaps, so the site
can lazy-load one small file for the year on screen. Example records are
written to ``*.examples.json`` and stay out of the data files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from verify.validate import LoadedDocument, Report, border_slot, repo_root, validate_root

FORMAT = "chronoglobe-bundle"
FORMAT_VERSION = "0.1.0"
FACT_URL = "https://chronoglobe.si/f/{id}@{version}"
CENTURY_RULE = (
    "A record is copied into every century its earliest/latest span overlaps. "
    "century_start is the mathematical floor of the year divided by 100, times 100 "
    "(not truncation toward zero). The bundle for year Y has "
    "century_start = floor(Y / 100) * 100. Example records are written to "
    "*.examples.json so the site can skip them. borders/gpl and borders/ccby "
    "are separate files and stay under their own licenses."
)
_VERSION_RE = re.compile(r'^version:\s*"?([^"\n]+?)"?\s*$', re.MULTILINE)


class ValidationFailed(Exception):
    def __init__(self, report: Report) -> None:
        super().__init__(f"{len(report.issues)} problem(s)")
        self.report = report


@dataclass
class Bundle:
    manifest: dict
    files: dict[str, str]


def century_start(year: int) -> int:
    return (year // 100) * 100


def century_starts(earliest: int, latest: int) -> list[int]:
    if not _is_int(earliest) or not _is_int(latest) or earliest > latest:
        return []
    first = century_start(earliest)
    last = century_start(latest)
    return list(range(first, last + 1, 100))


def dataset_version(root: Path) -> str:
    path = root / "CITATION.cff"
    if not path.is_file():
        return "0.0.0"
    match = _VERSION_RE.search(path.read_text(encoding="utf-8"))
    if match is None:
        return "0.0.0"
    return match.group(1).strip()


def build_bundle(root: Path, *, generated_at: str | None = None) -> Bundle:
    """Return the manifest and file texts for ``root``.

    Raise ``ValidationFailed`` when the tree is not valid. Nothing is written.
    """
    root = root.resolve()
    report = validate_root(root)
    if report.issues:
        raise ValidationFailed(report)
    version = dataset_version(root)
    when = generated_at or _now()
    grouped: dict[str, dict] = {}
    fact_bundles: dict[str, list[str]] = {}
    for doc in sorted(report.documents, key=lambda item: (item.path, str(item.document.get("id")))):
        for relative, record in _placements(doc, version):
            meta = {
                "century_start": record.pop("_century_start"),
                "example": record.pop("_example_file"),
                "kind": record.pop("_kind"),
                "layer": record.pop("_layer"),
                "license": record.pop("_license"),
            }
            bucket = grouped.get(relative)
            if bucket is None:
                bucket = {**meta, "records": []}
                grouped[relative] = bucket
            bucket["records"].append(record)
            fact_id = record.get("id")
            if isinstance(fact_id, str):
                paths = fact_bundles.setdefault(fact_id, [])
                if relative not in paths:
                    paths.append(relative)

    files: dict[str, str] = {}
    bundles: list[dict] = []
    for relative in sorted(grouped):
        bucket = grouped[relative]
        bucket["records"].sort(key=lambda item: (str(item.get("id")), item.get("path", "")))
        payload = {
            "century_start": bucket["century_start"],
            "count": len(bucket["records"]),
            "example": bucket["example"],
            "format": FORMAT,
            "format_version": FORMAT_VERSION,
            "kind": bucket["kind"],
            "layer": bucket["layer"],
            "license": bucket["license"],
            "records": bucket["records"],
            "version": version,
        }
        text = _dump(payload)
        files[relative] = text
        bundles.append(
            {
                "century_start": bucket["century_start"],
                "count": len(bucket["records"]),
                "example": bucket["example"],
                "kind": bucket["kind"],
                "layer": bucket["layer"],
                "license": bucket["license"],
                "path": relative,
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            }
        )

    by_kind: dict[str, int] = {}
    examples = 0
    facts: list[dict] = []
    for doc in sorted(report.documents, key=lambda item: str(item.document.get("id"))):
        by_kind[doc.kind] = by_kind.get(doc.kind, 0) + 1
        example = _is_example(doc)
        if example:
            examples += 1
        doc_id = doc.document.get("id")
        if not isinstance(doc_id, str):
            continue
        entry = {
            "bundles": fact_bundles.get(doc_id, []),
            "example": example,
            "id": doc_id,
            "kind": doc.kind,
            "license": _license_for(doc),
            "path": doc.path,
        }
        if doc.kind != "source":
            entry["fact_url"] = FACT_URL.format(id=doc_id, version=version)
        facts.append(entry)

    manifest = {
        "bundles": bundles,
        "century_rule": CENTURY_RULE,
        "counts": {
            "by_kind": dict(sorted(by_kind.items())),
            "examples": examples,
            "records": len(report.documents),
        },
        "fact_url_template": FACT_URL,
        "facts": facts,
        "format": FORMAT,
        "format_version": FORMAT_VERSION,
        "generated_at": when,
        "note": (
            "Generated from validated files. The repository files are the source of record. "
            "Records with example true are illustrations, not historical claims. Do not commit dist/."
        ),
        "version": version,
    }
    files["manifest.json"] = _dump(manifest)
    return Bundle(manifest=manifest, files=files)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="verify.bundle",
        description="Write per-layer, per-century bundles and a manifest.",
    )
    parser.add_argument("--root", type=Path, default=None, help="Atlas root (default: the repository).")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output directory (default: <root>/dist). Replaced on success.",
    )
    parser.add_argument(
        "--generated-at",
        default=None,
        help="Timestamp written into the manifest (default: now, UTC).",
    )
    args = parser.parse_args(argv)
    root = (args.root or repo_root()).resolve()
    output = (args.output or (root / "dist")).resolve()
    if output == root or output in root.parents:
        print("refusing to replace the repository root", file=sys.stderr)
        return 1
    try:
        bundle = build_bundle(root, generated_at=args.generated_at)
    except ValidationFailed as exc:
        for issue in exc.report.issues:
            print(issue, file=sys.stderr)
        print(f"{len(exc.report.issues)} problem(s); bundle not written", file=sys.stderr)
        return 1
    try:
        _publish(output, bundle.files)
    except OSError as exc:
        print(f"could not write {output}: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(bundle.files)} files in {output}")
    return 0


def _placements(doc: LoadedDocument, version: str) -> list[tuple[str, dict]]:
    example = _is_example(doc)
    suffix = ".examples.json" if example else ".json"
    license_name = _license_for(doc)
    if doc.kind == "source":
        relative = f"sources{suffix}"
        return [(relative, _record(doc, version, example, license_name, None, "source", "sources", example))]

    starts = century_starts(doc.document.get("earliest"), doc.document.get("latest"))
    placements: list[tuple[str, dict]] = []
    for start in starts:
        filename = f"c{start}{suffix}"
        if doc.kind == "border":
            slot = border_slot(doc.path) or "unknown"
            relative = f"borders/{slot}/{filename}"
            layer = f"borders-{slot}"
            kind = "border"
        elif doc.kind == "layer":
            layer = doc.document.get("layer")
            layer = layer if isinstance(layer, str) else "unknown"
            relative = f"layers/{layer}/{filename}"
            kind = "layer"
        else:
            folder = {"polity": "polities", "ruler": "rulers", "capital": "capitals"}[doc.kind]
            relative = f"{folder}/{filename}"
            layer = folder
            kind = doc.kind
        placements.append(
            (relative, _record(doc, version, example, license_name, start, kind, layer, example))
        )
    return placements


def _record(
    doc: LoadedDocument,
    version: str,
    example: bool,
    license_name: str,
    century: int | None,
    kind: str,
    layer: str,
    example_file: bool,
) -> dict:
    document = json.loads(json.dumps(doc.document))
    if doc.kind == "border" and doc.resolved_geometry is not None:
        document["geometry"] = doc.resolved_geometry
    record = {
        "document": document,
        "example": example,
        "id": doc.document.get("id"),
        "kind": doc.kind,
        "license": license_name,
        "path": doc.path,
        "_century_start": century,
        "_example_file": example_file,
        "_kind": kind,
        "_layer": layer,
        "_license": license_name,
    }
    doc_id = doc.document.get("id")
    if doc.kind != "source" and isinstance(doc_id, str):
        record["fact_url"] = FACT_URL.format(id=doc_id, version=version)
    return record


def _is_example(doc: LoadedDocument) -> bool:
    return doc.path.startswith("examples/") or doc.document.get("example") is True


def _license_for(doc: LoadedDocument) -> str:
    if doc.kind == "border" and border_slot(doc.path) == "gpl":
        return "GPL-3.0"
    return "CC-BY-4.0"


def _publish(output: Path, files: dict[str, str]) -> None:
    staging = output.with_name(output.name + ".staging")
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    try:
        for relative, text in files.items():
            path = staging / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        if output.exists():
            shutil.rmtree(output)
        staging.rename(output)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        raise


def _dump(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


if __name__ == "__main__":
    sys.exit(main())
