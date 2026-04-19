# Officiell redigerbar version

Denna mapp är avsedd för den officiella redigerbara versionen av DigComp 3.0
som publicerats av JRC via Zenodo:

**DOI:** 10.5281/zenodo.17780383
**URL:** https://doi.org/10.5281/zenodo.17780383
**Filstorlek:** ca 64 MB
**Innehåll:** Adobe InDesign 2025-filer, Word-dokument, erratalista

## Varför filen inte ligger i repot

Zip-filen är för stor (64 MB) för att lägga direkt i Git-versionskontroll
utan Git LFS. Ladda ner den manuellt från Zenodo vid behov.

## När används den?

- Som referenslayout när PDF-release av den svenska översättningen
  genereras (se `scripts/`).
- Som källa för erratalistan (se `docs/errata_tracking.md`).

## Viktigt

Filerna ska förbli orörda. Eventuell redigering sker enbart i
`data/sv/*.json` och layouten genereras därifrån.
