# Översättningsprinciper

## 1a. Grundprinciper

**Spårbarhet framför elegans.** Varje term ska kunna motiveras med källa. Om en elegant översättning skulle dölja en etablerad svensk juridisk eller facklig term, väljs den etablerade termen.

**Ramverket, inte ramverkets ton.** DigComp 3.0 är skrivet i en formell EU-byråkratisk engelska med återkommande fraser ("Acknowledge the benefits of…", "Recognise that…"). Svenska översättningen ska vara läsbar svenska, inte ett kalkerat EU-svensk. Verbvalen kan variera där engelskan upprepar.

**Individen synliggörs.** Engelskans "individuals" översätts inte mekaniskt till "individer". I många fall är "personer" eller "man" naturligare. Subjektet ska framgå tydligt.

## 1b. Språkliga grundval

Tre strukturella val som gäller genomgående i hela översättningen:

### Tilltalsnivå

Engelskan använder "individuals" som återkommande subjekt. På svenska används **opersonlig konstruktion som default** ("Att bedöma...", "Att identifiera..."). När ett subjekt krävs för tydlighet används **"personen"** – aldrig "individen" (för formellt) eller "man" (könskodat och för vardagligt för ett ramverk).

### Verbform

Verb i learning outcomes och competence statements formuleras i **presens indikativ** ("Identifierar...", "Bedömer...", "Känner till..."), inte i infinitiv ("Att identifiera..."). Detta följer SeQF och gymnasieskolans ämnesplaner och läser som handlingskompetens snarare än beskrivning.

### Ordet "digital"

Ramverket handlar i sin helhet om digital kompetens. Ordet "digital" används därför **där det är semantiskt centralt**, men **kortas bort där det är redundant**. "In digital environments" upprepas inte mekaniskt i varje mening – den digitala kontexten är underförstådd.

## 2. ID-system

ID-strängar (`LO1.1.01`, `CS1.1.01`, kompetens-id `1.1`) översätts **aldrig**. De är ramverkets ryggrad och ska fungera identiskt i alla språkversioner.

AI-etiketterna `AI-Explicit`, `AI-Implicit` och `AI not Implicit or Explicit` behålls oöversatta som tekniska etiketter i datan. Förklaringen av dem översätts i dokumentationen.

## 3. Kärntermer – fasta val

Följande termer ska användas konsekvent och är fastställda i `GLOSSARY.md`:

| EN | SV | Motivering |
|---|---|---|
| digital competence | digital kompetens | Etablerat i svensk utbildningskontext |
| digital inclusion | digital inkludering | Cedefop, PTS, DIGG |
| digital exclusion | digital exkludering | Betonar det aktiva strukturella skeendet. Se decision_log.md. |
| personal data | personuppgifter | GDPR svensk version, art. 4 |
| data protection | dataskydd | GDPR svensk version |
| privacy | integritet / personlig integritet | Kontextberoende |
| misinformation | missinformation | Institutet för språk och folkminnen (Isof) |
| disinformation | desinformation | Institutet för språk och folkminnen (Isof) |
| wellbeing | välbefinnande | Folkhälsomyndigheten |
| accessibility | tillgänglighet | DOS-lagen, WCAG |
| AI system | AI-system | AI-förordningen sv version |
| high-risk AI system | AI-system med hög risk | AI-förordningen art. 6 |
| digital identity | digital identitet | eIDAS, DIGG |

## 4a. Kompetensområden

| EN | SV |
|---|---|
| Information search, evaluation and management | Söka, bedöma och hantera information |
| Communication and collaboration | Kommunicera och samarbeta |
| Content creation | Skapa innehåll |
| Safety, wellbeing, and responsible use | Säkerhet, välbefinnande och ansvarsfullt användande |
| Problem identification and solving | Identifiera och lösa problem |

Områdesnamnen följer verbform där detta läses idiomatiskt och substantivform där ett tillstånd eller förhållande ska uttryckas. Engelska källan använder genomgående substantivkonstruktion (nominaliserad gerundium), men i svenska läses handlingsorienterad verbform mer naturligt för områden som beskriver vad personen gör. Område 4 avviker eftersom "säkerhet" och "välbefinnande" är tillstånd, inte handlingar – samma skäl som ligger bakom att engelskan själv bryter sin gerundiumform i 2.5 Digital behaviour, 3.3 Copyright and licences, 3.4 Computational thinking and programming och 4.4 Environmental impacts.

*Fastställt 2026-04-20. Se decision_log.md för motivering.*

## 4b. Kompetensnivåer

| EN | SV |
|---|---|
| Basic | Grund |
| Intermediate | Medel |
| Advanced | Avancerad |
| Highly advanced | Mycket avancerad |

*Fastställt 2026-04-19. Se decision_log.md för motivering och övervägda alternativ.*

## 5. Dimensioner

| EN | SV |
|---|---|
| Knowledge | Kunskap |
| Skill | Färdighet |
| Attitude | Förhållningssätt |

"Attitude" översätts **inte** till "attityd" – det antyder subjektiv läggning. DigComp använder begreppet för att beskriva orienterande förhållningssätt till digital teknik, vilket i svensk utbildningsterminologi motsvarar "förhållningssätt".

## 6. Återkommande formler

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

## 7. "Digital environments"

Undvik kalkering. "in digital environments" kan oftast översättas med "digitalt" eller "i digitala miljöer" beroende på sats. Välj det som ger mest läsbar svenska.

## 8. Arbetsflöde per post

För varje post (LO eller CS):

1. Läs engelsk text i sin kontext (hela kompetensen, inte bara raden).
2. Slå upp alla ord som finns i termlistan – använd dessa utan variation.
3. Översätt. Sätt `translation_status: "draft"`, fyll i `translator` och `last_updated`.
4. Om ett val krävde avvägning – skriv en rad i `decision_log.md` och referera till post-ID:t.
5. Vid granskning sätts `reviewed_by` och status ändras till `"reviewed"`.
6. Status `"final"` sätts först i samband med release-tagg.

## 9. När osäker

Hellre markera `translation_status: "needs_review"` och skriva i `notes`-fältet än att gömma osäkerheten i en glatt översättning. Osäkerheter är data – de visar var ramverket möter motstånd i svensk kontext.
