# Terminologibeslut

Detta dokument registrerar avvägningar som gjorts mellan möjliga svenska termer där valet inte var självklart. Varje post har ett ID (`DL-XXX`), datum, alternativ, valt alternativ och motivering. Tidigare beslut kan revideras – i så fall läggs en ny post till med nytt DL-ID, den gamla stryks inte utan markeras som ersatt med korsreferens.

Posterna listas i omvänd kronologisk ordning (nyaste först). DL-ID:na tilldelas löpande och behåller sin nummer även när den underliggande posten ersätts.

---

## DL-008 — 2026-04-22 — REVIDERING: "Attitude" → "Attityder"

**Ersätter:** DL-002 (2026-04-18)

**Tidigare beslut:** Attitude → Förhållningssätt (se DL-002).

**Nytt beslut:** Attitude → Attityder.

**Motivering för revidering:** "Attityder" är den etablerade svenska översättningen av "attitudes" i EU:s kompetensterminologi och bör därmed användas också i DigComp 3.0 på svenska:

- Rådets rekommendation om nyckelkompetenser för livslångt lärande (officiell svensk version via EUR-Lex) definierar kompetens som "en kombination av kunskaper, färdigheter och attityder".
- EPALE (Europeiska kommissionens plattform för vuxenutbildning) och övriga EU-plattformar använder samma översättning genomgående.
- DigComp 2.2 på svenska (2022) använder "kunskaper, färdigheter och attityder" som översättning av EU:s "knowledge, skills and attitudes".

DL-002 motiverades språkligt med att "attityd" på svenska kan ha negativ eller vardagligt färgad klang och att svensk utbildningsterminologi (SeQF, gymnasieskolans ämnesplaner) använder "förhållningssätt" för motsvarande dimension. Det är en rimlig observation isolerat sett, men den krockar med kravet på terminologisk konsistens med övriga EU-ramverk. DigComp 3.0 ingår i en terminologistack (EQF, Europass, ESCO, rådets rekommendation om nyckelkompetenser) där "attityder" är den etablerade svenska termen. Att avvika bryter kontinuiteten både bakåt (DigComp 2.2 på svenska) och i sidled (övriga EU-ramverk).

**Påverkar:** Dimensionen i learning outcomes, `TERMINOLOGI.md`, dokumentationstexter. Ingen faktisk ändring i datafilerna eftersom dimensionsfältet (`"dimension": "Attitude"`) bevarar källans form och inte översätts i JSON.

**Källa:** EUR-Lex (rådets rekommendation om nyckelkompetenser för livslångt lärande, svensk version), DigComp 2.2 på svenska (2022), EPALE svenska plattformen.

---

## DL-007 — (ej tilldelad)

Numret reserverades för en DL-post om "In digital environments" som aldrig skrevs. Se CHANGELOG 2026-04-22 för varför posten utelämnades.

---

## DL-006 — 2026-04-20 — Kompetensområden (5 områden)

**Alternativ övervägda:** Verbform genomgående; substantivform genomgående; blandad form per område utifrån idiomatisk läsning.

**Valt:** Substantivform genomgående.

1. Sökning, bedömning och hantering av information
2. Kommunikation och samarbete
3. Skapande av innehåll
4. Säkerhet, välbefinnande och ansvarsfullt användande
5. Problemidentifiering och problemlösning

**Motivering:** Engelska källan använder genomgående substantivkonstruktion (huvudsakligen gerundium). Den svenska översättningen följer samma form av lojalitet mot ramverket. Substantivform är också den etablerade genren för rubriker på denna abstraktionsnivå i svenskt fackspråk (myndighetsdokument, utbildningsplaner, läroplaner) och separerar tydligt områdesnamnen från learning outcomes och competence statements, där verb i presens indikativ används.

Variation mellan områdena sker inte i form utan i struktur, där varje områdesnamn följer sin egen inre logik:

- **Område 1 och 3** har verbalsubstantiv med objekt angivet via prepositionen "av". Denna konstruktion gör det explicit vad handlingarna syftar på.
- **Område 2** har två parallella handlingar utan gemensamt objekt.
- **Område 4** är tillståndsorienterat (säkerhet, välbefinnande) med en ansvarsdimension – inte handlingsorienterat.
- **Område 5** har handlingar med objekt inbakat i sammansatta ord (problem-identifiering, problem-lösning).

**Termval inom område 4:**
- "Wellbeing" översätts "välbefinnande" enligt fastställd term i TERMINOLOGI.md (källa: Folkhälsomyndigheten).
- "Use" översätts "användande" (inte "användning"). Båda är synonyma i svensk fackterminologi; valet här är språkligt snarare än principiellt.

**Påverkar:** `data/sv/competence_areas.json` (fältet `name.sv` för samtliga fem områden); `translation_principles.md`; `TERMINOLOGI.md`.

---

## DL-005 — 2026-04-20 — REVIDERING: "Digital exclusion" → "Digital exkludering"

**Ersätter:** DL-001 (2026-04-18 — Digital exclusion → Digitalt utanförskap).

**Reviderat till:** Digital exkludering.

**Motivering:** Myndighetstermen "digitalt utanförskap" är väletablerad men bär en semantisk förenkling som inte passar i ett ramverk.

**Påverkar:** `TERMINOLOGI.md`, samt alla framtida översättningar som innehåller termen.

---

## DL-004 — 2026-04-19 — "Misinformation" / "Disinformation" → "Missinformation" / "Desinformation"

**Alternativ övervägda:** misinformation, missinformation (för "misinformation"); desinformation (för "disinformation").

**Valt:** Missinformation (med två s) respektive desinformation.

**Motivering:** De två termerna betecknar olika företeelser och ska hållas åtskilda i översättningen. Enligt MSB avser **desinformation** medvetet förvanskad eller felaktig information spridd med avsikt att påverka mottagaren. **Missinformation** används för oavsiktligt felaktig information – ofta oavsiktlig spridning av desinformation, men också annan felaktig information som sprids utan påverkansavsikt. DigComp använder båda termerna parallellt och distinktionen måste bevaras i den svenska översättningen.

Stavningen "missinformation" (med två s) är rekommenderad av Institutet för språk och folkminnen (Isof). Engelskans "misinformation" stavas med ett s, men det svenska förledet "miss-" (i betydelsen "felaktigt", "misslyckat") har etablerad stavning med två s i svenska ordlistor. Kalkeringen "misinformation" förekommer i svenskt skrivbruk men avviker från svensk ordbildningsnorm.

**Påverkar:** `TERMINOLOGI.md`, `translation_principles.md`, samtliga CS- och LO-texter som innehåller någon av termerna.

**Källa:** Institutet för språk och folkminnen, Frågelådan: <https://frageladan.isof.se/faqs/31473>. MSB:s definition av desinformation återges i samma svar.

---

## DL-003 — 2026-04-19 — Proficiency level names (4-nivåskalan)

**Alternativ övervägda:** Grundläggande/Mellannivå/Avancerad/Mycket avancerad; Grund/Medel/Avancerad/Mycket avancerad; Grundläggande/Mellan/Avancerad/Högt avancerad.

**Valt:** Grund / Medel / Avancerad / Mycket avancerad.

**Motivering:** De engelska termerna i DigComp 3.0 är Basic / Intermediate / Advanced / Highly advanced. Progressionen mellan nivåerna är monoton längs tre samverkande dimensioner (kognitiv belastning, uppgiftskomplexitet, autonomi/ledarskap) – det finns ingen kvalitativ brytpunkt som översättningen behöver markera med en särskild begreppsetikett. "Mycket avancerad" är den idiomatiska svenska motsvarigheten till "highly advanced". "Grund" och "Medel" valdes framför "Grundläggande" och "Mellannivå" för jämnare längdprofil över skalan och läsbarhet i tabeller och gränssnitt.

SeQF har inga helt motsvarande nivåer och gav därför ingen bindande vägledning. Den 8-nivåbaserade EQF-kopplingen i DigComp 3.0 hanteras som separat beslut.

**Påverkar:** `data/sv/proficiency_levels.json` (4-nivåskalan); samtliga CS- och LO-texter som innehåller nivåhänvisningar; `TERMINOLOGI.md` och `translation_principles.md`.

---

## DL-002 — 2026-04-18 — "Attitude" → "Förhållningssätt" [ERSATT av DL-008]

**Alternativ övervägda:** attityd, hållning, inställning, förhållningssätt.

**Valt:** Förhållningssätt.

**Motivering:** "Attityd" på svenska har en stark konnotation av subjektiv läggning eller åsikt. DigComp använder "attitude" i Bloom-traditionen där termen syftar på ett orienterande, handlingsberedskapsskapande förhållande till ett kunskapsområde. Svensk utbildningsterminologi (SeQF, gymnasieskolans ämnesplaner, högskoleförordningens bilaga 2) använder konsekvent "förhållningssätt" för denna dimension. Valet stärker också att DigComp läses som ett yrkesmässigt kompetensramverk, inte som ett personlighetsmått.

**Påverkar:** Alla 107 attityd-märkta LO:n, fältet `dimension` i `learning_outcomes.json`; `TERMINOLOGI.md`.

---

## DL-001 — 2026-04-18 — "Digital exclusion" → "Digitalt utanförskap" [ERSATT av DL-005]

> ⚠️ **Detta beslut är ersatt av DL-005 (2026-04-20).** Posten behålls för spårbarhet enligt dokumentets revideringsprincip.

**Alternativ övervägda:** digital exkludering, digitalt utanförskap, digital marginalisering.

**Valt:** Digitalt utanförskap.

**Motivering:** "Digital exkludering" är en kalkering som förekommer i EU-översättningar men sällan i svensk myndighetskommunikation. "Digitalt utanförskap" används av MSB, SKR, PTS och Post- och telestyrelsen i uppdragsbeskrivningar och rapporter. Termen kopplar också till det bredare "utanförskap"-begreppet i svensk socialpolitisk diskurs, vilket är korrekt givet DigComp-definitionens fokus på deltagande i ekonomiskt, socialt och politiskt liv.

**Noterat motargument:** "Exkludering" betonar den aktiva handlingen (någon exkluderas *av* systemet), medan "utanförskap" kan läsas som passivt tillstånd. Detta är en reell semantisk skillnad och kan komma att omprövas.

---

## Mall för nya poster

```markdown
## DL-XXX — ÅÅÅÅ-MM-DD — "EN-term" → "SV-term"

**Alternativ övervägda:** ...

**Valt:** ...

**Motivering:** ...

**Påverkar:** [LO-ID:n eller CS-ID:n som berörs, eller generell påverkan]

**Källa:** [Om valet stöds av etablerad svensk källa – länk eller referens]
```

Vid revidering av ett tidigare beslut: använd formatet `DL-XXX — ÅÅÅÅ-MM-DD — REVIDERING: "...", ange **Ersätter:** i ingressen, och markera den ersatta posten med `[ERSATT av DL-XXX]` i rubriken.
