# DigComp 3.0 på svenska

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19652093.svg)](https://doi.org/10.5281/zenodo.19652093)

En öppen och spårbar översättning till svenska av Europeiska kommissionens ramverk **DigComp 3.0 – European Digital Competence Framework for Citizens (Fifth Edition, 2025)**.

Det mesta av arbetet här är mänskligt dubbel- och trippelkollande av 36 000+ ord men projektstrukturen har skapats med stöd av Claude (Anthropic). Samma språkmodell används även för att hålla ihop översättningarna och fånga inkonsekvenser. Återanvänd gärna vad som finns här, men kom ihåg att detta fortfarande är ett pågående arbete, så saker kan ändras. Ingen deadline är satt ännu. Det beror på hur många vi blir som hjälps åt!

DigComp 3.0 är utgivet av Europeiska kommissionens Joint Research Centre (JRC) under Creative Commons Attribution 4.0 International (CC BY 4.0), vilket tillåter översättning. Detta är alltså *inte* EU:s officiella svenska version av DigComp 3.0.

Innehållet i ramverket har inte ändrats, utökats eller förkortats. Översättningsarbetet gäller uteslutande formuleringen på svenska. Alla fastställda svenska val finns samlade i `TERMINOLOGI.md`. Motiveringar dokumenteras i `docs/decision_log.md`. Principer står i `docs/translation_principles.md`. Strukturella förändringar loggas i `CHANGELOG.md`. Se `CONTRIBUTING.md` för hur du bidrar.

Initiativet drivs av Terese Raymond som till vardags arbetar som projektledare för Digidel inom föreningen Sambruk. Arbetet här är strukturerat för att i framtiden kunna överföras till en organisation som kan ta ansvar för långsiktig förvaltning.

## Status

Version: **0.1 (2026-04-21)**

Första release efter projektomstrukturering och första substantiella översättningsarbete. Se `CHANGELOG.md` för full beskrivning.

| Komponent | Poster | Översatta | Status |
|---|---|---|---|
| Kompetensområden | 5 | 5 | ✅ |
| Kompetenser | 21 | 0 | ⏳ |
| Nivåer (4 + 8) | 12 | 12 | ✅ |
| Kompetenspåståenden (CS) | 362 | 0 | ⏳ |
| Learning outcomes (LO) | 523 | 0 | ⏳ |
| Ordlista | 126 | 73 termer / 0 förklaringar | 🟡 |

*NOT: LO1.2.16 är översatt som dokumentationsexempel och räknas inte som start på LO-översättningen.*

## Källa

* Cosgrove, J. & Cachia, R. (2025). *DigComp 3.0: European Digital Competence Framework – Fifth Edition*. Publications Office of the European Union, Luxembourg. JRC144121.
* Data supplement v. 24 nov 2025.

Originaldata (oförändrad) ligger i `sources/`. Översättningsarbetet sker enbart i `data/sv/`.

## Hur strukturen fungerar

All data finns som JSON. Varje post har ett stabilt ID (`LO1.1.01`, `CS1.1.01`) som **aldrig översätts**. Endast textfält översätts, och varje översättning registrerar översättare, granskare, tidsstämpel och status.

Datan är maskinläsbar och kan användas direkt i egna system — till exempel självskattningsverktyg, kompetensvalideringssystem eller läroplaner. Den kan också exporteras till andra format via scripten i `scripts/`:

- **Word-dokument (`.docx`)** — för remissversioner eller traditionell läsning. Översatta poster visas som normal text, ej översatta som röd kursiv för tydlig arbetslistmarkering. Kan filtreras per status (draft, reviewed). Se `scripts/README.md` för alternativ.
- **Weblate-kompatibla CSV-filer** — för den som vill använda Weblate eller liknande översättningsgränssnitt.

Scripten läser alltid från `data/sv/*.json` och skriver aldrig tillbaka — datan är source of truth och förblir mänskligt hanterad.

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

## Bidra gärna i översättningsarbetet

Översättningsprojektet drivs för närvarande av Terese Raymond men förhoppningen på sikt är ett community där alla med intresse hjälps åt med översättningar och resonerar öppet.

Det finns två sätt att bidra:

- **Via issues** — Ingen teknisk vana krävs. Här går det bra att posta förslag på översättningar, diskutera redan gjorda översättningar eller ställa andra typer av frågor om DigComp och projektet.
- **Via pull requests** — För dig som är van vid Git.

Ambitionen är att svara på frågor och bidrag inom en vecka. Se [`CONTRIBUTING.md`](CONTRIBUTING.md) för utförlig vägledning.

## Licenser

Detta repo har **två licenser** för olika typer av material, inspirerat av modellen i [PiAir/digcomp3-l10n](https://github.com/PiAir/digcomp3-l10n):

* **Översättningen, datan och dokumentationen** (allt utanför `scripts/`) — [CC BY-SA 4.0](LICENSE-CC-BY-SA) (Erkännande-DelaLika). Översättningen får användas fritt, även kommersiellt, men ingen enskild aktör kan privatisera själva översättningstexten. Licensen är strängare än JRC-källans CC BY 4.0 — den säkerställer att arbetet förblir öppet också när det återanvänds och bearbetas.
* **Scripts och tekniska verktyg** (`scripts/`) — [Apache License 2.0](LICENSE-scripts). Scripten är fristående kod och licensieras separat för att maximera återanvändbarhet.

## Citering

Om du använder denna översättning i ditt arbete, vänligen citera den:

> digcomp-sv contributors (2026). *DigComp 3.0 på svenska* (Version 0.1) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.19652093

Använd **concept-DOI** [10.5281/zenodo.19652093](https://doi.org/10.5281/zenodo.19652093) om du vill referera till projektet i allmänhet (pekar alltid på senaste version).

För automatgenererad citation i olika format (APA, BibTeX, etc.), använd "Cite this repository"-knappen uppe till höger på GitHub eller se CITATION.cff.

## Relaterade översättningsprojekt

* **Nederländska:** [PiAir/digcomp3-l10n](https://github.com/PiAir/digcomp3-l10n) — använder Weblate, förväntas klar mars 2026. Förebild för detta projekts struktur.
* **DigComp 2.2 på svenska** (2022) — översatt av arbetsgrupp från SVERD, Dataföreningen m.fl. ([PDF](https://dfs.se/digcomp_ramverket_for_digital_kompetens_for_medborgare/))

## Officiellt källmaterial

* **Publikation (PDF):** <https://publications.jrc.ec.europa.eu/repository/handle/JRC144121>
* **Redigerbar version (InDesign + Word):** <https://doi.org/10.5281/zenodo.17780383>
* **Erratalista (alltid senaste versionen):** <https://joint-research-centre.ec.europa.eu/projects-and-activities/education-and-training/digital-transformation-education/digital-competence-framework-digcomp/digcomp-30-resources/digcomp-30-errata_en>
* **Riktlinjer för anpassning och översättning:** <https://joint-research-centre.ec.europa.eu/projects-and-activities/education-and-training/digital-transformation-education/digital-competence-framework-digcomp/digcomp-30-resources_en>

Erratalistan uppdateras löpande av JRC. Hur vi hanterar erratainarbetning beskrivs i `docs/errata_tracking.md` (arbetsflöde via GitHub Issues).
