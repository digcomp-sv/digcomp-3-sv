# DigComp 3.0 på svenska

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19652093.svg)](https://doi.org/10.5281/zenodo.19652093)

Öppen, spårbar översättning av Europeiska kommissionens ramverk **DigComp 3.0 – European Digital Competence Framework for Citizens (Fifth Edition, 2025)** till svenska.

## Status

Version: **0.0.1 (extrahering från JRC-källa klar, översättning ej påbörjad)**

| Komponent | Poster | Översatta | Status |
|---|---|---|---|
| Kompetensområden | 5 | 0 | ⏳ |
| Kompetenser | 21 | 0 | ⏳ |
| Nivåer (4 + 8) | 12 | 0 | ⏳ |
| Kompetenspåståenden (CS) | 362 | 0 | ⏳ |
| Learning outcomes (LO) | 523 | 0 | ⏳ |
| Ordlista | 126 | 0 | ⏳ |

## Källa

* Cosgrove, J. & Cachia, R. (2025). *DigComp 3.0: European Digital Competence Framework – Fifth Edition*. Publications Office of the European Union, Luxembourg. JRC144121.
* Data supplement v. 24 nov 2025.

Originaldata (oförändrad) ligger i `sources/`. Översättningsarbetet sker enbart i `data/sv/`.

## Om projektet

Syftet är att tillhandahålla en öppen och maskinläsbar svensk version av DigComp 3.0 som kan återanvändas av olika aktörer utan att översättningen behöver göras om för varje sammanhang.

Alla fastställda svenska val finns samlade i `TERMINOLOGI.md`. Motiveringar för val som krävt avvägning dokumenteras i `docs/decision_log.md` och kan diskuteras öppet via issues och pull requests. Översättningsprinciperna står i `docs/translation_principles.md`. Större strukturella förändringar i dokumentationen loggas i `CHANGELOG.md`. Se `CONTRIBUTING.md` för praktisk vägledning om att bidra till översättningarna.

Att placera översättningsarbetet i ett öppet och versionshanterat arkiv är ett initiativ av Terese Raymond. Arbetet är strukturerat för att i framtiden överföras till en organisation som kan ta ansvar för långsiktig förvaltning.

Licensen (CC BY-SA 4.0) säkerställer att arbetet förblir öppet. Översättningen får användas fritt – även kommersiellt – men ingen enskild aktör kan privatisera eller stänga in själva översättningstexten.

## Hur strukturen fungerar

All data finns som JSON. Varje post har ett stabilt ID (`LO1.1.01`, `CS1.1.01`) som **aldrig översätts**. Endast textfält översätts, och varje översättning registrerar översättare, granskare, tidsstämpel och status.

### Versionering

Detta repo hanterar svensk översättning av DigComp 3.x-familjen. Versioner av själva översättningen hanteras via Git-taggar (v0.1, v1.0, osv.). Vid en eventuell framtida DigComp 4.0 med strukturella förändringar skapas ett nytt repo.

```
digcomp-3-sv/
├── sources/                              # Orörd JRC data supplement (xlsx)
├── sources-official/                     # Orörd editerbar version (InDesign + Word, hämtas manuellt)
├── data/sv/                              # Översättningen (source of truth)
│   ├── competence_areas.json             # 5 områden
│   ├── competences.json                  # 21 kompetenser
│   ├── proficiency_levels.json           # 4-nivå + 8-nivå (EQF)
│   ├── competence_statements.json        # 362 CS
│   ├── learning_outcomes.json            # 523 LO
│   └── glossary.json                     # 126 termer
├── weblate/                              # Weblate-kompatibla CSV-filer (genereras)
│   ├── core-framework/sv.csv
│   ├── levels/sv.csv
│   ├── statements/sv.csv
│   ├── outcomes/sv.csv
│   └── glossary/sv.csv
├── docs/
│   ├── translation_principles.md         # Översättningsprinciper
│   ├── decision_log.md                   # Terminologibeslut (DL-ID)
│   └── errata_tracking.md                # Arbetsflöde för JRC:s errata (via GitHub Issues)
├── scripts/
│   ├── README.md                         # Dokumentation av scripten
│   ├── requirements.txt                  # Python-beroenden
│   ├── generate_docx.py                  # Remissdokumentgenerering
│   └── export_to_weblate_csv.py          # Export till Weblate-format
├── releases/                             # Genererade remissdokument (taggade)
├── CHANGELOG.md                          # Större strukturella förändringar i dokumentationen
├── CONTRIBUTING.md
├── TERMINOLOGI.md                        # Samtliga fastställda svenska val (termer + ramverksstruktur)
├── LICENSE                               # Översikt över licenser
├── LICENSE-CC-BY-SA                      # För översättningen och datan
└── LICENSE-scripts                       # Apache 2.0 för scripts/
```

## Licenser

Detta repo har **två licenser** för olika typer av material, inspirerat av modellen i [PiAir/digcomp3-l10n](https://github.com/PiAir/digcomp3-l10n):

* **Översättningen, datan och dokumentationen** (allt utanför `scripts/`) — [CC BY-SA 4.0](LICENSE-CC-BY-SA) (Erkännande-DelaLika). Licensvalet är ärvt från JRC:s editerbara version.
* **Scripts och tekniska verktyg** (`scripts/`) — [Apache License 2.0](LICENSE-scripts). Scripten är fristående kod och licensieras separat för att maximera återanvändbarhet.

## Citering

Om du använder denna översättning i ditt arbete, vänligen citera den:

> digcomp-sv contributors (2026). *DigComp 3.0 på svenska* (Version 0.0.1) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.19652094

Använd **concept-DOI** [10.5281/zenodo.19652093](https://doi.org/10.5281/zenodo.19652093) om du vill referera till projektet i allmänhet (pekar alltid på senaste version). Använd **version-DOI** om du vill referera till en specifik version.

För automatgenererad citation i olika format (APA, BibTeX, etc.), använd "Cite this repository"-knappen uppe till höger på GitHub, eller se CITATION.cff.

## Relaterade översättningsprojekt

* **Nederländska:** [PiAir/digcomp3-l10n](https://github.com/PiAir/digcomp3-l10n) — använder Weblate, förväntas klar mars 2026. Förebild för detta projekts struktur.
* **DigComp 2.2 på svenska** (2022) — översatt av arbetsgrupp från SVERD, Dataföreningen m.fl. ([PDF](https://dfs.se/digcomp_ramverket_for_digital_kompetens_for_medborgare/))

## Officiell källmaterial

* **Publikation (PDF):** <https://publications.jrc.ec.europa.eu/repository/handle/JRC144121>
* **Redigerbar version (InDesign + Word):** <https://doi.org/10.5281/zenodo.17780383>
* **Erratalista (alltid senaste versionen):** <https://joint-research-centre.ec.europa.eu/projects-and-activities/education-and-training/digital-transformation-education/digital-competence-framework-digcomp/digcomp-30-resources/digcomp-30-errata_en>
* **Riktlinjer för anpassning och översättning:** <https://joint-research-centre.ec.europa.eu/projects-and-activities/education-and-training/digital-transformation-education/digital-competence-framework-digcomp/digcomp-30-resources_en>

Erratalistan uppdateras löpande av JRC. Hur vi hanterar erratainarbetning beskrivs i `docs/errata_tracking.md` (arbetsflöde via GitHub Issues).
