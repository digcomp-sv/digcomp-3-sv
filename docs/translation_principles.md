# Översättningsprinciper

Detta dokument samlar de principiella regler som styr översättningen av DigComp 3.0 till svenska. Enskilda termval, ramverkselement (områden, kompetenser, nivåer, dimensioner) och deras svenska motsvarigheter står i `TERMINOLOGI.md`. Motiveringar för val som krävt avvägning står i `docs/decision_log.md`.

## 1. Grundprinciper

**Spårbarhet framför elegans.** Varje term ska kunna motiveras med källa. Om en elegant översättning skulle dölja en etablerad svensk juridisk eller facklig term, väljs den etablerade termen.

**Ramverket, inte ramverkets ton.** DigComp 3.0 är skrivet i en formell EU-byråkratisk engelska med återkommande fraser ("Acknowledge the benefits of…", "Recognise that…"). Svenska översättningen ska vara läsbar svenska, inte ett kalkerat EU-svenska. Verbvalen kan variera där engelskan upprepar.

**Individen synliggörs.** Engelskans "individuals" översätts inte mekaniskt till "individer". I många fall är "personer" eller "man" naturligare. Subjektet ska framgå tydligt.

## 2. Språkliga grundval

Tre strukturella val som gäller genomgående i hela översättningen:

### Tilltalsnivå

Engelskan använder "individuals" som återkommande subjekt. På svenska används **opersonlig konstruktion som default** ("Att bedöma...", "Att identifiera..."). När ett subjekt krävs för tydlighet används **"personen"** – aldrig "individen" (för formellt) eller "man" (könskodat och för vardagligt för ett ramverk).

### Verbform

Verb i learning outcomes och competence statements formuleras i **presens indikativ** ("Identifierar...", "Bedömer...", "Känner till..."), inte i infinitiv ("Att identifiera..."). Detta följer SeQF och gymnasieskolans ämnesplaner och läser som handlingskompetens snarare än beskrivning.

### Ordet "digital"

Ramverket handlar i sin helhet om digital kompetens. Ordet "digital" används därför **där det är semantiskt centralt**, men **kortas bort där det är redundant**. "In digital environments" upprepas inte mekaniskt i varje mening – den digitala kontexten är underförstådd.

## 3. ID-system

ID-strängar (`LO1.1.01`, `CS1.1.01`, kompetens-id `1.1`) översätts **aldrig**. De är ramverkets ryggrad och ska fungera identiskt i alla språkversioner.

AI-etiketterna `AI-Explicit`, `AI-Implicit` och `AI not Implicit or Explicit` behålls oöversatta som tekniska etiketter i datan. Förklaringen av dem översätts i dokumentationen.

## 4. Kompetensområden, kompetenser och nivåer

Se `TERMINOLOGI.md`, sektionen Ramverksstruktur, för de fastställda svenska namnen. Beslutshistorik finns i `decision_log.md` (DL-003 för kompetensnivåer, DL-006 för kompetensområden).

Områdesnamnen följer substantivform genomgående, lojalt med engelska källans konstruktion. Variation mellan områdena sker inte i form utan i struktur, anpassad efter varje områdes inre logik. Se DL-006 för motivering.

## 5. Dimensioner

Se `TERMINOLOGI.md`, sektionen Ramverksstruktur. Beslutshistorik för "Attitude" → "Förhållningssätt" finns i DL-002.

"Attitude" översätts **inte** till "attityd" – det antyder subjektiv läggning. DigComp använder begreppet för att beskriva orienterande förhållningssätt till digital teknik, vilket i svensk utbildningsterminologi motsvarar "förhållningssätt".

## 6. Återkommande formler

Engelskan i DigComp 3.0 använder återkommande fraser som inleder learning outcomes och competence statements. Dessa översätts konsekvent enligt följande mönster:

| EN inledning | SV inledning |
|---|---|
| Acknowledge the benefits of… | Är medveten om fördelarna med… |
| Acknowledge the importance of… | Är medveten om vikten av… |
| Recognise that… | Känner till att… |
| Identify… | Identifierar… / Urskiljer… |
| Describe… | Beskriver… |
| Distinguish between… | Skiljer mellan… |
| Assess… | Bedömer… |
| Support others to… | Stödjer andra att… |
| Lead or contribute to… | Leder eller bidrar till… |

Dessa är stilregler för återkommande fraskonstruktioner, inte enskilda termer – de hör därför hemma i principerna snarare än i TERMINOLOGI.

## 7. Arbetsflöde per post

För varje post (LO eller CS):

1. Läs engelsk text i sin kontext (hela kompetensen, inte bara raden).
2. Slå upp alla ord som finns i `TERMINOLOGI.md` – använd dessa utan variation.
3. Översätt. Sätt `translation_status: "draft"`, fyll i `translator` och `last_updated`.
4. Om ett val krävde avvägning – skriv en ny DL-post i `decision_log.md` och referera till post-ID:t.
5. Vid granskning sätts `reviewed_by` och status ändras till `"reviewed"`. Detta innebär att posten är godkänd för att pushas till main.

Release hanteras via Git-taggar (v0.1, v0.2, osv.) – ingen separat status för slutversion behövs i datan.

### Konvention för `translator` och `reviewed_by`

- **`@digcomp-sv`** används som standardvärde för översättningar och granskningar som är projektets officiella datamängd. Individuell spårbarhet finns alltid via Git-historik (commit-författare).
- **Individuella namn** (t.ex. `@anvandarnamn`) används av bidragsgivare som skickar PR med `draft`-översättningar. När PR mergas och status sätts till `reviewed` kan namnet ersättas med `@digcomp-sv` eller behållas efter projektägarens bedömning — särskilt om bidraget är distinkt och förtjänar explicit kreditering.

## 8. När osäker

Hellre lämna posten som `draft` och beskriva osäkerheten i `notes`-fältet än att gömma osäkerheten i en glatt översättning. Osäkerheter är data – de visar var ramverket möter motstånd i svensk kontext.

Poster där `notes` innehåller text är per definition värda att återvända till. För att hitta alla osäkra poster, filtrera på `notes != null`.
