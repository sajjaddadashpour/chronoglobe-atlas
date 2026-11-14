"""Good and bad fixtures for the Chronoglobe validator."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from verify.bundle import ValidationFailed, build_bundle, century_starts, main as bundle_main
from verify.validate import main, validate_root, yaml11_bool_issues

REPO = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).parent / "fixtures"
GOOD = FIXTURES / "good" / "mini"

EXAMPLE_IDS = {
    "src-example-gazetteer",
    "src-example-sketch",
    "src-example-reading-a",
    "src-example-reading-b",
    "examplemere",
    "example-ruler-north",
    "example-ruler-south",
    "examplehaven",
    "examplemere-border",
    "examplemere-population",
    "examplemere-gdp",
    "examplemere-climate",
    "examplemere-governance",
}

BAD = {
    "yaml-no-trap": ("unquoted YAML scalar 'no'", "YAML 1.1"),
    "duplicate-ids": ("duplicate id 'fixture-dup'",),
    "dangling-source": ("src-missing", "not in sources/"),
    "dangling-succession": ("missing-ruler", "does not resolve to a ruler"),
    "estimate-missing-range": ("confidence estimate requires low, high, method",),
    "border-provenance-folder": ("allowed only under borders/gpl/",),
    "border-ccby-derives-from-gpl": ("must not derive from GPL shapes",),
    "border-ccby-missing-fresh-source": ("must declare fresh_source",),
    "contested-dangling-alternative": ("alternative 0", "src-missing"),
    "border-ccby-cites-gpl": (
        "must not cite a GPL or historical-basemaps source",
        "dataset 'fresh-drawn'",
    ),
    "border-fresh-in-gpl": ("borders/gpl/ requires provenance 'historical-basemaps-gpl'",),
    "border-ccby-geometry-ref-gpl": ("must not reference a GPL shape",),
}

YAML11_WORDS = ["yes", "Yes", "YES", "no", "No", "NO", "on", "On", "off", "OFF", "y", "Y", "n", "N"]

LICENSE_SECTION = (
    "Code is under MIT (`LICENSE`). Data is under CC-BY-4.0 (`LICENSE-DATA`), "
    "except `borders/gpl/`, which stays GPL-3.0 (`borders/gpl/LICENSE`)."
)


def _text(report) -> str:
    return "\n".join(str(issue) for issue in report.issues)


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _source(root: Path, name: str = "src-fixture") -> None:
    _write(
        root,
        f"sources/{name}.json",
        json.dumps(
            {
                "id": name,
                "authors": ["Fixture Author"],
                "title": "Fixture source, not a real work",
                "year": 2026,
                "publisher": "Fixture Press",
            }
        ),
    )


def _polity(root: Path, earliest: int = 1, latest: int = 1) -> None:
    _source(root)
    _write(
        root,
        "polities/fixture-polity.yaml",
        (
            "id: fixture-polity\nname: Fixture Polity\n"
            f"earliest: {earliest}\nlatest: {latest}\n"
            "sources:\n  - src-fixture\nconfidence: legendary\n"
            'note: "Fixture. Not a historical claim."\n'
        ),
    )


def test_repository_is_valid():
    """v0 ships illustrations only. Update this when sourced records are added."""
    report = validate_root(REPO)
    assert report.issues == [], _text(report)
    ids = {doc.document["id"] for doc in report.documents}
    assert ids == EXAMPLE_IDS
    assert all(doc.path.startswith("examples/") for doc in report.documents)
    assert report.files_checked == len(EXAMPLE_IDS)


def test_examples_are_marked_and_not_historical_dates():
    report = validate_root(REPO)
    assert report.issues == [], _text(report)
    for doc in report.documents:
        assert doc.document["example"] is True
        assert "not a historical claim" in doc.document["note"].casefold()
        if doc.kind == "source":
            continue
        assert doc.document["earliest"] >= 9000
        assert doc.document["latest"] >= 9000


def test_readme_license_section_stays():
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    assert LICENSE_SECTION in readme
    assert "GPL-3.0" in readme


def test_schemas_are_draft_2020_12():
    for path in sorted((REPO / "schema").glob("*.json")):
        Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))


def test_good_fixtures_pass():
    report = validate_root(GOOD)
    assert report.issues == [], _text(report)
    kinds = {doc.path: doc.kind for doc in report.documents}
    assert kinds["sources/src-fixture-book.json"] == "source"
    assert kinds["borders/gpl/fixture-border-gpl.yaml"] == "border"
    assert kinds["borders/ccby/fixture-border-ccby.yaml"] == "border"
    climate = next(doc for doc in report.documents if doc.document["id"] == "fixture-climate")
    assert climate.document["note"] == "no"
    assert climate.document["confidence"] == "scholarly-consensus"
    polity = next(doc for doc in report.documents if doc.document["id"] == "fixture-polity")
    assert polity.document["earliest"] < 0
    ccby = next(doc for doc in report.documents if doc.document["id"] == "fixture-border-ccby")
    assert ccby.resolved_geometry["type"] == "Polygon"


@pytest.mark.parametrize("name", sorted(BAD))
def test_bad_fixtures_fail(name: str):
    report = validate_root(FIXTURES / "bad" / name)
    text = _text(report)
    assert report.issues, name
    for needle in BAD[name]:
        assert needle in text, (name, needle, text)


def test_yaml_no_trap_fails():
    report = validate_root(FIXTURES / "bad" / "yaml-no-trap")
    text = _text(report)
    assert "unquoted YAML scalar 'no'" in text
    assert "YAML 1.1" in text


@pytest.mark.parametrize("word", YAML11_WORDS)
def test_unquoted_yaml11_bool_word_is_rejected(word: str):
    issues = yaml11_bool_issues(f"flag: {word}\n", "trap.yaml")
    assert len(issues) == 1
    assert f"unquoted YAML scalar {word!r}" in issues[0].message


@pytest.mark.parametrize("word", ["yes", "no", "on", "off", "y", "n"])
def test_quoted_yaml11_bool_word_is_kept(word: str):
    assert yaml11_bool_issues(f'flag: "{word}"\n', "ok.yaml") == []
    assert yaml11_bool_issues(f"flag: '{word}'\n", "ok.yaml") == []


def test_true_false_comments_and_longer_words_are_not_traps():
    assert yaml11_bool_issues("flag: true\nother: false\n", "ok.yaml") == []
    assert yaml11_bool_issues("# no\nid: ok\n", "ok.yaml") == []
    assert yaml11_bool_issues("flag: no way\n", "ok.yaml") == []
    assert yaml11_bool_issues("flag: |\n  no\n", "ok.yaml") == []


def test_span_reversed_fails(tmp_path: Path):
    _polity(tmp_path, earliest=10, latest=1)
    report = validate_root(tmp_path)
    assert any("earliest must be <= latest" in issue.message for issue in report.issues)


def test_estimate_low_above_high_fails(tmp_path: Path):
    _polity(tmp_path)
    _write(
        tmp_path,
        "rulers/fixture-ruler-a.yaml",
        (
            "id: fixture-ruler-a\nname: Fixture Ruler A\npolity: fixture-polity\n"
            "earliest: 1\nlatest: 2\nsources:\n  - src-fixture\nconfidence: estimate\n"
            "low: 5\nhigh: 1\nmethod: fixture method\n"
        ),
    )
    report = validate_root(tmp_path)
    assert any("requires low <= high" in issue.message for issue in report.issues)


def test_alternatives_rejected_unless_contested(tmp_path: Path):
    _polity(tmp_path)
    _write(
        tmp_path,
        "polities/fixture-polity.yaml",
        (
            "id: fixture-polity\nname: Fixture Polity\nearliest: 1\nlatest: 1\n"
            "sources:\n  - src-fixture\nconfidence: attested\n"
            "alternatives:\n  - value: other\n    sources:\n      - src-fixture\n"
        ),
    )
    report = validate_root(tmp_path)
    assert any("only allowed when confidence is contested" in issue.message for issue in report.issues)


def test_unclosed_ring_fails(tmp_path: Path):
    _fresh_border(tmp_path, "[[0, 0], [1, 0], [1, 1], [0, 1]]")
    report = validate_root(tmp_path)
    assert any("is not closed" in issue.message for issue in report.issues)


def test_border_needs_one_geometry(tmp_path: Path):
    _fresh_border(tmp_path, "[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]", geometry=False)
    report = validate_root(tmp_path)
    assert any("geometry or a geometry_ref" in issue.message for issue in report.issues)


def test_layer_directory_must_match(tmp_path: Path):
    _polity(tmp_path)
    _write(
        tmp_path,
        "layers/population/fixture-population.yaml",
        (
            "id: fixture-population\nlayer: gdp\npolity: fixture-polity\n"
            "earliest: 1\nlatest: 1\nvalue_low: 1\nvalue_high: 2\nunit: persons\n"
            "method: fixture\nsources:\n  - src-fixture\nconfidence: legendary\n"
        ),
    )
    report = validate_root(tmp_path)
    assert any("must match the directory" in issue.message for issue in report.issues)


def test_id_must_match_filename(tmp_path: Path):
    _source(tmp_path)
    _write(
        tmp_path,
        "polities/wrong-name.yaml",
        (
            "id: fixture-polity\nname: Fixture Polity\nearliest: 1\nlatest: 1\n"
            "sources:\n  - src-fixture\nconfidence: legendary\n"
        ),
    )
    report = validate_root(tmp_path)
    assert any("must match the filename stem" in issue.message for issue in report.issues)


def test_example_true_outside_examples_fails(tmp_path: Path):
    _source(tmp_path)
    _write(
        tmp_path,
        "polities/fixture-polity.yaml",
        (
            "id: fixture-polity\nname: Fixture Polity\nearliest: 1\nlatest: 1\n"
            "sources:\n  - src-fixture\nconfidence: legendary\nexample: true\n"
            'note: "Illustration only. Not a historical claim."\n'
        ),
    )
    report = validate_root(tmp_path)
    assert any("only allowed under examples/" in issue.message for issue in report.issues)


def test_examples_must_be_marked(tmp_path: Path):
    _write(
        tmp_path,
        "examples/polities/fixture-polity.yaml",
        (
            "id: fixture-polity\nname: Fixture Polity\nearliest: 9000\nlatest: 9000\n"
            "sources:\n  - src-fixture\nconfidence: legendary\n"
        ),
    )
    _write(
        tmp_path,
        "examples/sources/src-fixture.json",
        json.dumps(
            {
                "id": "src-fixture",
                "authors": ["Fixture Author"],
                "title": "Fixture source, not a real work",
                "year": 2026,
                "publisher": "Fixture Press",
                "example": True,
                "note": "Illustration only. Not a historical claim.",
            }
        ),
    )
    report = validate_root(tmp_path)
    assert any("must set example: true" in issue.message for issue in report.issues)


def test_duplicate_border_key_fails(tmp_path: Path):
    _fresh_border(tmp_path, "[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]")
    _write(
        tmp_path,
        "borders/ccby/fixture-border-b.yaml",
        (tmp_path / "borders/ccby/fixture-border.yaml")
        .read_text(encoding="utf-8")
        .replace("id: fixture-border\n", "id: fixture-border-b\n"),
    )
    report = validate_root(tmp_path)
    assert any("duplicate border for polity" in issue.message for issue in report.issues)


def test_self_succession_fails(tmp_path: Path):
    _polity(tmp_path)
    _write(
        tmp_path,
        "rulers/fixture-ruler-a.yaml",
        (
            "id: fixture-ruler-a\nname: Fixture Ruler A\npolity: fixture-polity\n"
            "earliest: 1\nlatest: 1\nsuccession:\n  - role: successor\n    id: fixture-ruler-a\n"
            "sources:\n  - src-fixture\nconfidence: legendary\n"
        ),
    )
    report = validate_root(tmp_path)
    assert any("must not point at the ruler itself" in issue.message for issue in report.issues)


def test_year_outside_span_fails(tmp_path: Path):
    _fresh_border(tmp_path, "[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]")
    text = (tmp_path / "borders/ccby/fixture-border.yaml").read_text(encoding="utf-8")
    (tmp_path / "borders/ccby/fixture-border.yaml").write_text(
        text.replace("year: 1\n", "year: 5\n"),
        encoding="utf-8",
    )
    report = validate_root(tmp_path)
    assert any("year must lie inside earliest and latest" in issue.message for issue in report.issues)


def test_yaml_rejects_a_second_document(tmp_path: Path):
    _write(tmp_path, "polities/two.yaml", "id: one\n---\nid: two\n")
    report = validate_root(tmp_path)
    assert any("one YAML document" in issue.message for issue in report.issues)


def test_source_needs_a_locator(tmp_path: Path):
    _write(
        tmp_path,
        "sources/src-bare.json",
        json.dumps(
            {
                "id": "src-bare",
                "authors": ["Fixture Author"],
                "title": "Bare",
                "year": 2026,
            }
        ),
    )
    report = validate_root(tmp_path)
    assert any("publisher, a doi, or a url" in issue.message for issue in report.issues)


def test_cli_accepts_the_repository(capsys: pytest.CaptureFixture[str]):
    assert main(["--root", str(REPO)]) == 0
    assert "valid" in capsys.readouterr().out


def test_cli_rejects_the_no_trap(capsys: pytest.CaptureFixture[str]):
    assert main(["--root", str(FIXTURES / "bad" / "yaml-no-trap")]) == 1
    captured = capsys.readouterr()
    assert "unquoted YAML scalar 'no'" in captured.err
    assert captured.out == ""


def test_century_starts_use_mathematical_floor():
    assert century_starts(-150, -150) == [-200]
    assert century_starts(-100, -1) == [-100]
    assert century_starts(1, 100) == [0, 100]
    assert century_starts(-50, 50) == [-100, 0]
    assert century_starts(9000, 9001) == [9000]
    assert century_starts(-450, -400) == [-500, -400]


def test_bundle_of_the_repository_keeps_examples_apart(tmp_path: Path):
    output = tmp_path / "dist"
    assert bundle_main(["--root", str(REPO), "--output", str(output), "--generated-at", "2026-11-14T00:00:00Z"]) == 0
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["format"] == "chronoglobe-bundle"
    assert manifest["version"] == "0.1.0"
    assert manifest["generated_at"] == "2026-11-14T00:00:00Z"
    assert manifest["counts"]["records"] == len(EXAMPLE_IDS)
    assert manifest["counts"]["examples"] == len(EXAMPLE_IDS)
    assert manifest["fact_url_template"] == "https://chronoglobe.si/f/{id}@{version}"
    paths = [item["path"] for item in manifest["bundles"]]
    assert paths
    assert all(path.endswith(".examples.json") for path in paths)
    assert not any(path.startswith("borders/gpl/") for path in paths)
    population = json.loads((output / "layers/population/c9000.examples.json").read_text(encoding="utf-8"))
    ids = {record["id"] for record in population["records"]}
    assert ids == {"examplemere-population"}
    assert "examplemere-governance" not in ids
    assert population["records"][0]["fact_url"] == "https://chronoglobe.si/f/examplemere-population@0.1.0"
    assert all(not key.startswith("_") for record in population["records"] for key in record)
    fact = next(item for item in manifest["facts"] if item["id"] == "examplemere")
    assert fact["fact_url"] == "https://chronoglobe.si/f/examplemere@0.1.0"
    border = json.loads((output / "borders/ccby/c9000.examples.json").read_text(encoding="utf-8"))
    assert border["license"] == "CC-BY-4.0"
    assert border["records"][0]["document"]["geometry"]["type"] == "Polygon"


def test_good_fixture_bundle_splits_centuries_and_licenses(tmp_path: Path):
    bundle = build_bundle(GOOD, generated_at="2026-11-14T00:00:00Z")
    manifest = bundle.manifest
    assert manifest["generated_at"] == "2026-11-14T00:00:00Z"
    assert manifest["version"] == "0.0.0"
    assert manifest["counts"]["examples"] == 0
    assert manifest["counts"]["by_kind"]["layer"] == 4
    population = [item for item in manifest["bundles"] if item["layer"] == "population"]
    assert {item["century_start"] for item in population} == {-500, -400}
    assert all(item["license"] == "CC-BY-4.0" for item in population)
    gpl = next(item for item in manifest["bundles"] if item["layer"] == "borders-gpl")
    ccby = next(item for item in manifest["bundles"] if item["layer"] == "borders-ccby")
    assert gpl["license"] == "GPL-3.0"
    assert ccby["license"] == "CC-BY-4.0"
    assert gpl["path"].startswith("borders/gpl/")
    assert ccby["path"].startswith("borders/ccby/")
    ccby_body = json.loads(bundle.files[ccby["path"]])
    assert ccby_body["records"][0]["document"]["geometry"]["type"] == "Polygon"
    assert "examplemere" not in {item["id"] for item in manifest["facts"]}
    output = tmp_path / "dist"
    assert bundle_main(["--root", str(GOOD), "--output", str(output)]) == 0
    assert (output / "manifest.json").is_file()
    assert (output / gpl["path"]).is_file()


def test_bundle_refuses_an_invalid_tree(tmp_path: Path):
    output = tmp_path / "dist"
    bad = FIXTURES / "bad" / "yaml-no-trap"
    assert bundle_main(["--root", str(bad), "--output", str(output)]) == 1
    assert not output.exists()
    with pytest.raises(ValidationFailed):
        build_bundle(bad)


def test_dist_is_gitignored():
    ignore = (REPO / ".gitignore").read_text(encoding="utf-8")
    assert "dist/" in ignore.splitlines()


def _fresh_border(root: Path, ring: str, *, geometry: bool = True) -> None:
    _write(
        root,
        "sources/src-fixture-sketch.yaml",
        (
            "id: src-fixture-sketch\nauthors:\n  - Fixture Author\n"
            'title: "Fixture fresh sketch, not a real map"\nyear: 2026\n'
            'url: "https://example.invalid/fixture-sketch"\nlicense: CC-BY-4.0\n'
            "dataset: fresh-drawn\n"
        ),
    )
    _write(
        root,
        "polities/fixture-polity.yaml",
        (
            "id: fixture-polity\nname: Fixture Polity\nearliest: 1\nlatest: 1\n"
            "sources:\n  - src-fixture-sketch\nconfidence: legendary\n"
        ),
    )
    geometry_block = (
        "geometry:\n  type: Polygon\n  coordinates:\n    - " + ring + "\n" if geometry else ""
    )
    _write(
        root,
        "borders/ccby/fixture-border.yaml",
        (
            "id: fixture-border\npolity: fixture-polity\nyear: 1\nearliest: 1\nlatest: 1\n"
            "sources:\n  - src-fixture-sketch\nconfidence: legendary\n"
            "provenance: fresh-drawn\nderived_from_gpl: false\n"
            "fresh_source: src-fixture-sketch\n" + geometry_block
        ),
    )
