# Errata-hantering

Errata för DigComp 3.0 hanteras via **GitHub Issues** i detta repo, inte som en separat markdown-fil. Varje rättelse som JRC publicerar blir ett eget issue, vilket ger bättre spårbarhet, sökbarhet och möjlighet att länka specifika rättelser till commits som inarbetar dem i den svenska översättningen.

Det här arbetsflödet är inspirerat av [PiAir/digcomp3-l10n](https://github.com/PiAir/digcomp3-l10n) (nederländska översättningen), som tillämpar samma modell.

## JRC:s officiella erratalista

<https://joint-research-centre.ec.europa.eu/projects-and-activities/education-and-training/digital-transformation-education/digital-competence-framework-digcomp/digcomp-30-resources/digcomp-30-errata_en>

Denna lista uppdateras löpande av JRC. Enligt Zenodo-posten för den redigerbara versionen skriver listan över den PDF som följer med zip-arkivet.

## Issue-modell

Varje errata öppnas som ett nytt issue med:

- **Label**: `errata`
- **Titel**: `Errata: [berörd post-ID] – kort beskrivning`
- **Body**:
  - Citat från JRC:s erratalista (datum, version)
  - Vilken post som påverkas (LO-ID, CS-ID, glossary-term, etc.)
  - Före/efter-jämförelse av engelskt källtext
  - Påverkan på eventuell befintlig svensk översättning (behöver ombedömning?)
- **Status**: öppet tills rättelsen är inarbetad i `data/sv/`
- **Commit-referens**: när rättelsen är införd, stäng issuet med referens till commiten

### Exempel på issue-titel

```
Errata: LO1.2.16 – förtydligande om AI-systemets output (JRC 2026-02-14)
```

## Arbetsflöde vid ny errata från JRC

1. **Kontrollera JRC:s erratasida** (förslagsvis månadsvis eller när projektet taggar ny version).
2. **Ladda ner senaste erratalistan** som PDF om förändringar finns. Spara som referens i `sources/errata/errata-YYYY-MM-DD.pdf` (valfritt, men bra för offline-arkivering).
3. **Öppna ett issue per errata-punkt.** En punkt per issue, även om flera punkter rör samma kompetens.
4. **Uppdatera datan i `data/sv/`:**
   - Korrigera `text.en` på påverkad post.
   - Om posten var översatt (`translation_status` draft eller högre): sätt `needs_review` och skriv i `notes` att errata kräver omprövning.
   - Lägg commit-referens i notes: `[errata] JRC 2026-02-14, se issue #42`.
5. **Stäng issuet** med commit-referens: `Fixes #42`.

## Varför GitHub Issues och inte en markdown-fil

- **Sökbart**: alla stängda issues finns kvar och kan filtreras på `label:errata`.
- **Kopplat till kod**: commits som inarbetar en rättelse kan referera till issuet med `Fixes #N`, vilket syns både i issuet och i commithistoriken.
- **Arbetsbart**: flera personer kan jobba parallellt på olika errata utan merge-konflikter i en gemensam spårningsfil.
- **Transparent**: en utomstående kan se exakt vilka errata som hanterats, när, och vad som är utestående.
- **Backup**: alla issues finns kvar även om GitHub skulle försvinna – de exporteras via GitHub API om det behövs.

## Initial genomgång

Vid repots första commit bör en genomgång av JRC:s nuvarande erratalista göras. Varje punkt öppnas som ett issue och tilldelas label `errata` + `initial-sync`. Detta skapar en startlinje mot vilken framtida errata kan spåras.
