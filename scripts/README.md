# scripts/

Hjälpscript för repot. Datan i `data/sv/*.json` är alltid source of truth – dessa script läser datan, de skriver inte till den.

## Installation

```bash
pip install -r scripts/requirements.txt
```

## generate_docx.py

Genererar ett Word-dokument (.docx) från JSON-datan. Används för att släppa remissversioner.

### Användning

```bash
# Hela dokumentet, all data inklusive ej översatta poster
python scripts/generate_docx.py

# Bara översatta poster (status draft eller senare)
python scripts/generate_docx.py --status-filter draft

# Endast slutgiltiga poster (för v1.0-release)
python scripts/generate_docx.py --status-filter final

# Ange utdatafilens namn
python scripts/generate_docx.py --output releases/v0.1-draft/digcomp-3-sv.docx
```

### Vad genereras

1. **Titelsida** — rubrik, version, datum, översättningsgrad, källhänvisning, licens.
2. **Innehållsförteckning** — de 5 områdena med sina 21 kompetenser.
3. **Kompetensnivåer** — 4-nivåsystemet med beskrivningar.
4. **Kompetensavsnitt** — en sektion per kompetens med:
   - Beskrivning
   - Kompetenspåståenden (CS) grupperade per nivå
   - Learning outcomes (LO) som tabell, sorterad efter nivå och dimension
5. **Ordlista** — alfabetiskt ordnad termlista.

### Visning av översättningsstatus

- **Översatt** — svensk text visas som normal text.
- **Ej översatt** — engelsk text visas kursivt i röd färg omgiven av `[Ej översatt: …]`.
- **Draft/needs_review** — status visas som grå etikett efter texten.
- **AI-Explicit-etiketter** — små markeringar visar DigComp:s AI-klassificering.

Detta gör att generering mitt i arbetet ger meningsfull output: allt som är översatt läses normalt, allt som saknas är tydligt markerat och kan användas som arbetslista.

## extract_from_xlsx.py (framtida)

Återsynk från JRC:s officiella data supplement, t.ex. vid större uppdateringar. Används bara när JRC släpper ny version. Rörs inte annars.

## Utvecklingsprinciper för script

- Scripten ska **aldrig** skriva till `data/sv/*.json` — det är ett mänskligt översättningsarbete.
- Scripten ska **aldrig** röra `data/source/` eller `data/source-official/` — det är orörda original.
- Alla script ska fungera när de körs från repo-roten.
- Beroenden hålls på ett minimum och deklareras i `requirements.txt`.
