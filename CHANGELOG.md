# Ändringslogg

Denna fil dokumenterar större strukturella och organisatoriska förändringar i projektet. Enskilda terminologival dokumenteras i `decision_log.md`. Löpande commit-historik finns i Git.

---

## 2026-04-22 — Förenklat statusflöde, metadata-konvention och öppning för bidrag

Tre sammanhängande förändringar som rör hur projektet arbetar efter v0.1-releasen.

### Förenklat translation_status-flöde

Statusflödet för översättningsposter förenklas från fem nivåer till tre.

**Tidigare flöde:** `not_started → draft → needs_review → reviewed → final`

**Nytt flöde:** `not_started → draft → reviewed`

- `needs_review` tas bort. Osäkerhet om en översättning markeras istället i `notes`-fältet med beskrivning av vad som är osäkert. Poster med `notes != null` är per definition värda att återvända till.
- `final` tas bort. Statusen `reviewed` betyder "godkänt för push till main". Slutversion av en release framgår av Git-taggar (v0.1, v0.2, osv.) snarare än ett separat statusfält i datan.

**Bakgrund.** Det tidigare fem-nivåsflödet var lånat från översättningsprojekt med tydlig rollfördelning mellan översättare, granskare och releaseansvariga. I ett projekt drivet av en ensam projektägare blev skillnaderna mellan `draft`, `reviewed` och `final` artificiella — alla tre sattes ofta av samma person samma dag. Förenklingen speglar det faktiska arbetsflödet bättre och minskar risken för inkonsekvens mellan statusfältet och andra informationskällor (Git-historia, release-taggar).

### Konsekvent metadatastruktur och `@digcomp-sv`-konvention

JSON-filer med översättningar får enhetliga metadatafält: `translation_status`, `translator`, `reviewed_by`, `last_updated`, `notes`. Tidigare saknade vissa filer några av dessa fält.

- `competence_areas.json`: fem nya fält tillagda, alla 5 områden markerade som `reviewed`
- `proficiency_levels.json`: fem nya fält tillagda, alla 12 nivåer markerade som `reviewed`
- `competences.json`: `translator`, `reviewed_by`, `notes` tillagda (alla null — kompetenserna är inte översatta än)
- `learning_outcomes.json`, `competence_statements.json`, `glossary.json`: hade redan fälten, inga strukturella ändringar

**`@digcomp-sv`-konvention.** Värdet `@digcomp-sv` införs som standardattribut för `translator` och `reviewed_by` när översättningen är del av projektets officiella datamängd. Individuell spårbarhet finns alltid via Git-historik (commit-författare). Individuella bidragsgivare som skickar PR med drafts använder sitt eget användarnamn; när PR mergas och status sätts till `reviewed` kan värdet ersättas med `@digcomp-sv` eller behållas efter projektägarens bedömning.

Som konsekvens: 73 `translator`-fält i `glossary.json` bytts från `@tereseraymond` till `@digcomp-sv` eftersom termerna härrör från TERMINOLOGI.md som är projektets auktoritativa källa.

### Punkt om "digital environments" borttagen från translation_principles

Punkt 7 i `docs/translation_principles.md` löd tidigare: *"Undvik kalkering. 'In digital environments' kan oftast översättas med 'digitalt' eller 'i digitala miljöer' beroende på sats. Välj det som ger mest läsbar svenska."* Punkten tas bort som självständig princip. Skälet: vägledningen var vag och upprepar i praktiken bara den generella principen om att översätta idiomatiskt snarare än mekaniskt. Engelska DigComp 3.0 överanvänder inte heller frasen, så det finns ingen särskild risk att dokumentera bort.

### CONTRIBUTING och README öppnar för bidragsgivare

CONTRIBUTING.md är omskriven för att tydliggöra två vägar in: förslag via issues (ingen teknisk vana krävs) och pull requests för översättningsarbete (för Git-vana). Issues presenteras som projektets diskussionsforum där ämneskompetens från olika håll bidrar till en mer genomtänkt översättning.

README.md får en ny "Bidra till översättningen"-sektion som sammanfattar möjligheterna och pekar till CONTRIBUTING för detaljer. Tonen öppnar för ett bredare community på sikt, även om projektet för närvarande drivs av en ensam projektägare.

### Dokumentationsändringar

- `docs/translation_principles.md`: statusflödet och "När osäker" omskrivna; ny underrubrik om `@digcomp-sv`-konventionen; punkt 7 om "digital environments" borttagen
- `docs/errata_tracking.md`: referensen till `needs_review` ersatt
- `CONTRIBUTING.md`: omskriven
- `README.md`: ny Bidra-sektion + fotnot om LO1.2.16 + omskriven öppning med personligare ton + komprimerat licensstycke
- `CHANGELOG.md`: denna post

### Första learning outcome översatt

LO1.2.16 har översatts som levande exempel för CONTRIBUTING (draft-status, `@tereseraymond`). Posten räknas inte som start på LO-översättningen — en fotnot i README:s statustabell markerar detta.

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
