# Ändringslogg

Denna fil dokumenterar större strukturella och organisatoriska förändringar i projektet. Enskilda terminologival dokumenteras i `decision_log.md`. Löpande commit-historik finns i Git.

---

## v0.1 — 2026-04-21 (Zenodo-release)

Första grundläggande release efter projektomstrukturering och inledande översättningsarbete. Ersätter v0.0.1 (som var en ren extraheringsmilstolpe) som aktuell referensversion.

**Översatt innehåll:**
- `proficiency_levels.json` — 4-nivå + 8-nivå komplett (namn, beskrivningar, syften)
- `competence_areas.json` — 5 områden komplett (namn + descriptorer)
- `glossary.json` — 73 av 126 termer synkade (draft-status, förklaringar återstår)

**Strukturella förändringar** (se posten 2026-04-20 nedan för detaljer):
- GLOSSARY.md → TERMINOLOGI.md
- DL-ID-system i decision_log
- CHANGELOG.md tillagd
- Rensad glossary.json
- CITATION.cff: versions- och datumfält tillagda

**Terminologibeslut i denna release** (DL-001 till DL-006):
- Digital exclusion, Attitude, Proficiency levels, Misinformation/Disinformation, Kompetensområden, samt fastställande av complex/simple/well-defined.

---

## 2026-04-20 — Omstrukturering av dokumentation

Ombyggnad av projektets redaktionella dokumentation för att minska överlappningar och synkningsarbete mellan filerna.

**Bakgrund.** En maskinöversättning hade fyllt i svenska fält i `data/sv/glossary.json` och markerat poster som `completed` utan att faktiskt vara klara. När detta upptäcktes och backades blev det tydligt att den befintliga dokumentationsstrukturen bar på sårbarheter: termval och motiveringar låg spridda mellan `GLOSSARY.md`, `translation_principles.md` och `decision_log.md`, med överlappande innehåll som krävde synkning i flera filer vid varje förändring.

**Ändringar.**

- `GLOSSARY.md` omdöpt till `TERMINOLOGI.md` och utvidgad till att omfatta alla fastställda svenska val i projektet, inklusive ramverksstruktur (områden, kompetenser, nivåer, dimensioner, AI-etiketter) och alla 126 JRC-glossary-termer plus tilläggstermer. Tidigare innehöll filen 45 selektivt utvalda termer utan uttalat urvalskriterium.
- `TERMINOLOGI.md` kompletterad med statusmarkeringar (✅ fastställt, 🟡 pågående, ⬜ TBD) och en tabell som visar synkningskopplingar till JSON-filerna i `data/sv/`.
- `TERMINOLOGI.md` har dessutom 48 nya fastställda svenska val för termer ur JRC:s glossary där svensk fackterminologi var entydig (antivirusprogram, molntjänster, säkerhetskopiering, etc.).
- `translation_principles.md` rensad på termtabeller. Punkt 3 (Kärntermer), punkt 4 (Kompetensnivåer) och punkt 5 (Dimensioner) har flyttats till TERMINOLOGI.md. Principerna hänvisar nu dit via DL-ID. Numreringen räknad om.
- `decision_log.md` försedd med DL-ID (DL-001 till DL-006) retroaktivt. Posterna listas i omvänd kronologisk ordning (nyaste först) med bevarad numrering.
- Revideringsposten från 2026-04-19 om "digital exclusion" rensad. Motiveringen innehöll analytisk argumentation ur rättighetsperspektiv som inte hörde hemma i en värdeneutral översättningsdokumentation. Den ersatta posten heter nu DL-005 (2026-04-20) med renodlat språklig motivering. Det tidigare beslutet DL-001 står kvar som ersatt men behållet enligt dokumentets revideringsprincip.
- Ny DL-006: de fem kompetensområdena fastställda med svenska namn i substantivform.
- `data/sv/glossary.json` återställd till ren JRC-extraktion (126 poster, alla sv-fält `null`, status `not_started` genomgående).
- README.md och CONTRIBUTING.md uppdaterade med nya filreferenser.

**Motivering.**

Tidigare fanns terminformation på tre ställen (principles, decision_log, glossary) vilket skapade synkningsarbete och risk för inkonsekvens. Ny arkitektur:

- `translation_principles.md` = regler och genomgående språkliga val
- `TERMINOLOGI.md` = samtliga fastställda svenska val, samlade för uppslagning
- `decision_log.md` = historiken bakom valen, med DL-ID för referens från övriga dokument

Varje informationselement hör hemma på exakt ett ställe. Principles hänvisar till TERMINOLOGI för enskilda termval. TERMINOLOGI hänvisar till decision_log för motivering av val som krävt avvägning.

**Påverkar.** All redaktionell dokumentation i projektet. Datastrukturen i `data/sv/` är oförändrad utöver återställningen av `glossary.json`.
