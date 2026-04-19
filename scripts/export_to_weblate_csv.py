#!/usr/bin/env python3
"""
export_to_weblate_csv.py
------------------------
Exporterar JSON-datan i data/sv/ till CSV-filer i Weblate-kompatibelt format
(location, source, target) för att möjliggöra översättning via
hosted.weblate.org eller annan Weblate-instans.

Datastrukturen i JSON är source of truth. CSV-filerna regenereras vid behov.

Skapas en mapp per komponent enligt PiAir/digcomp3-l10n:s konvention:
    core-framework/   (kompetensområden + kompetenser)
    levels/           (kompetensnivåer)
    statements/       (kompetenspåståenden)
    outcomes/         (learning outcomes)
    glossary/         (ordlista)

Användning:
    python scripts/export_to_weblate_csv.py [--output-dir DIR]

Exempel:
    # Standard: exporterar till weblate/ i repo-roten
    python scripts/export_to_weblate_csv.py

    # Ange annan utmapp
    python scripts/export_to_weblate_csv.py --output-dir /tmp/weblate-export

Beroenden: bara standardbiblioteket (json, csv, pathlib).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "sv"
DEFAULT_OUTPUT = REPO_ROOT / "weblate"


def load_json(name: str):
    path = DATA_DIR / name
    if not path.exists():
        sys.exit(f"Hittar inte {path}. Kör scriptet från repo-roten.")
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def write_csv(rows: list[dict], path: Path) -> None:
    """Skriv CSV med Weblate-standardkolumner: location, source, target."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["location", "source", "target"])
        for row in rows:
            writer.writerow([row["location"], row["source"], row["target"] or ""])


def export_core_framework(output_dir: Path) -> None:
    """Kompetensområden + kompetenser: namn och beskrivningar."""
    areas = load_json("competence_areas.json")
    comps = load_json("competences.json")
    rows = []

    for area in areas:
        rows.append({
            "location": f"area.{area['id']}.name",
            "source": area["name"]["en"],
            "target": area["name"].get("sv"),
        })
        rows.append({
            "location": f"area.{area['id']}.descriptor",
            "source": area["descriptor"]["en"],
            "target": area["descriptor"].get("sv"),
        })

    for comp in comps:
        rows.append({
            "location": f"competence.{comp['id']}.name",
            "source": comp["name"]["en"],
            "target": comp["name"].get("sv"),
        })
        rows.append({
            "location": f"competence.{comp['id']}.descriptor",
            "source": comp["descriptor"]["en"],
            "target": comp["descriptor"].get("sv"),
        })

    write_csv(rows, output_dir / "core-framework" / "sv.csv")
    print(f"  core-framework: {len(rows)} rader")


def export_levels(output_dir: Path) -> None:
    """Kompetensnivåer: namn, beskrivningar, syften."""
    data = load_json("proficiency_levels.json")
    rows = []

    for i, level in enumerate(data["four_level"]):
        rows.append({
            "location": f"level.4.{i}.name",
            "source": level["name"]["en"],
            "target": level["name"].get("sv"),
        })
        rows.append({
            "location": f"level.4.{i}.description",
            "source": level["description"]["en"],
            "target": level["description"].get("sv"),
        })
        rows.append({
            "location": f"level.4.{i}.purpose",
            "source": level["purpose"]["en"],
            "target": level["purpose"].get("sv"),
        })

    for i, level in enumerate(data["eight_level"]):
        rows.append({
            "location": f"level.8.eqf{level['eqf_level']}.description",
            "source": level["description"]["en"],
            "target": level["description"].get("sv"),
        })

    write_csv(rows, output_dir / "levels" / "sv.csv")
    print(f"  levels: {len(rows)} rader")


def export_statements(output_dir: Path) -> None:
    """Kompetenspåståenden (CS)."""
    statements = load_json("competence_statements.json")
    rows = []

    for s in statements:
        rows.append({
            "location": s["id"],
            "source": s["text"]["en"],
            "target": s["text"].get("sv"),
        })

    write_csv(rows, output_dir / "statements" / "sv.csv")
    print(f"  statements: {len(rows)} rader")


def export_outcomes(output_dir: Path) -> None:
    """Learning outcomes (LO)."""
    outcomes = load_json("learning_outcomes.json")
    rows = []

    for o in outcomes:
        rows.append({
            "location": o["id"],
            "source": o["text"]["en"],
            "target": o["text"].get("sv"),
        })

    write_csv(rows, output_dir / "outcomes" / "sv.csv")
    print(f"  outcomes: {len(rows)} rader")


def export_glossary(output_dir: Path) -> None:
    """Ordlista: termer och förklaringar."""
    glossary = load_json("glossary.json")
    rows = []

    for i, entry in enumerate(glossary):
        # Använd engelska termen som location för att göra den läsbar i Weblate
        location_term = entry["term"]["en"].lower().replace(" ", "_").replace("/", "_")
        rows.append({
            "location": f"term.{location_term}",
            "source": entry["term"]["en"],
            "target": entry["term"].get("sv"),
        })
        rows.append({
            "location": f"explanation.{location_term}",
            "source": entry["explanation"]["en"],
            "target": entry["explanation"].get("sv"),
        })

    write_csv(rows, output_dir / "glossary" / "sv.csv")
    print(f"  glossary: {len(rows)} rader")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Exportera JSON-data till Weblate-kompatibla CSV-filer."
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Utmapp för CSV-filerna. Standard: {DEFAULT_OUTPUT}",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Exporterar till {args.output_dir}/")
    export_core_framework(args.output_dir)
    export_levels(args.output_dir)
    export_statements(args.output_dir)
    export_outcomes(args.output_dir)
    export_glossary(args.output_dir)
    print("✓ Klar.")


if __name__ == "__main__":
    main()
