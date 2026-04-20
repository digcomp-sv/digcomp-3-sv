# Terminologibeslut

Detta dokument registrerar avvägningar som gjorts mellan möjliga svenska termer där valet inte var självklart. Varje post har datum, beslutsfattare, alternativ, valt alternativ och motivering. Tidigare beslut kan revideras – i så fall läggs en ny post till, den gamla stryks inte.

---

## 2026-04-19 — "Misinformation" / "Disinformation" → "Missinformation" / "Desinformation"

**Alternativ övervägda:** misinformation, missinformation (för "misinformation"); desinformation (för "disinformation").

**Valt:** Missinformation (med två s) respektive desinformation.

**Motivering:** De två termerna betecknar olika företeelser och ska hållas åtskilda i översättningen. Enligt MSB avser **desinformation** medvetet förvanskad eller felaktig information spridd med avsikt att påverka mottagaren. **Missinformation** används för oavsiktligt felaktig information – ofta oavsiktlig spridning av desinformation, men också annan felaktig information som sprids utan påverkansavsikt. DigComp använder båda termerna parallellt och distinktionen måste bevaras i den svenska översättningen.

Stavningen "missinformation" (med två s) är rekommenderad av Institutet för språk och folkminnen (Isof). Engelskans "misinformation" stavas med ett s, men det svenska förledet "miss-" (i betydelsen "felaktigt", "misslyckat") har etablerad stavning med två s i svenska ordlistor. Kalkeringen "misinformation" förekommer i svenskt skrivbruk men avviker från svensk ordbildningsnorm.

**Påverkar:** GLOSSARY.md, translation_principles.md, samtliga CS- och LO-texter som innehåller någon av termerna.

**Källa:** Institutet för språk och folkminnen, Frågelådan: <https://frageladan.isof.se/faqs/31473>. MSB:s definition av desinformation återges i samma svar.

---

## 2026-04-19 — Proficiency level names (4-nivåskalan)

**Alternativ övervägda:** Grundläggande/Mellannivå/Avancerad/Mycket avancerad; Grund/Medel/Avancerad/Mycket avancerad; Grundläggande/Mellan/Avancerad/Högt avancerad.

**Valt:** Grund / Medel / Avancerad / Mycket avancerad.

**Motivering:** De engelska termerna i DigComp 3.0 är Basic / Intermediate / Advanced / Highly advanced. Progressionen mellan nivåerna är monoton längs tre samverkande dimensioner (kognitiv belastning, uppgiftskomplexitet, autonomi/ledarskap) – det finns ingen kvalitativ brytpunkt som översättningen behöver markera med en särskild begreppsetikett. "Mycket avancerad" är den idiomatiska svenska motsvarigheten till "highly advanced". "Grund" och "Medel" valdes framför "Grundläggande" och "Mellannivå" för jämnare längdprofil över skalan och läsbarhet i tabeller och gränssnitt.

SeQF har inga helt motsvarande nivåer och gav därför ingen bindande vägledning. Den 8-nivåbaserade EQF-kopplingen i DigComp 3.0 hanteras som separat beslut.

**Påverkar:** `data/sv/proficiency_levels.json` (4-nivåskalan); samtliga CS- och LO-texter som innehåller nivåhänvisningar; `GLOSSARY.md` och `translation_principles.md` punkt 4.

---

## 2026-04-19 — REVIDERING: "Digital exclusion" → "Digital exkludering"

**Tidigare beslut (2026-04-18):** Digitalt utanförskap.

**Reviderat till:** Digital exkludering.

**Motivering:** Vid närmare övervägande väger den strukturella precisionen tyngre än matchningen mot myndighetspraxis. "Exkludering" betonar det aktiva skeendet – att någon eller något exkluderar – medan "utanförskap" tonar ner den systemiska dimensionen och placerar fokus på den uteslutnas tillstånd. 

DigComp:s egen definition ("marginalisation of an individual... deprived of full access") beskriver ett aktivt skeende. Inte ett passivt tillstånd. Och den svenska översättningen bör spegla detta.

Myndighetstermen "digitalt utanförskap" är väletablerad men bär en semantisk förenkling som inte passar i ett ramverk.

**Påverkar:** GLOSSARY.md, samt alla framtida översättningar som innehåller termen.

---

## 2026-04-18 — "Attitude" → "Förhållningssätt"

**Alternativ övervägda:** attityd, hållning, inställning, förhållningssätt.

**Valt:** Förhållningssätt.

**Motivering:** "Attityd" på svenska har en stark konnotation av subjektiv läggning eller åsikt. DigComp använder "attitude" i Bloom-traditionen där termen syftar på ett orienterande, handlingsberedskapsskapande förhållande till ett kunskapsområde. Svensk utbildningsterminologi (SeQF, gymnasieskolans ämnesplaner, högskoleförordningens bilaga 2) använder konsekvent "förhållningssätt" för denna dimension. Valet stärker också att DigComp läses som ett yrkesmässigt kompetensramverk, inte som ett personlighetsmått.

**Påverkar:** Alla 107 attityd-märkta LO:n, fältet `dimension` i `learning_outcomes.json`.

---

## 2026-04-18 — "Digital exclusion" → "Digitalt utanförskap" [ERSATT]

> ⚠️ **Detta beslut är ersatt av revideringen 2026-04-19.** Posten behålls för spårbarhet enligt dokumentets revideringsprincip.

**Alternativ övervägda:** digital exkludering, digitalt utanförskap, digital marginalisering.

**Valt:** Digitalt utanförskap.

**Motivering:** "Digital exkludering" är en kalkering som förekommer i EU-översättningar men sällan i svensk myndighetskommunikation. "Digitalt utanförskap" används av MSB, SKR, PTS och Post- och telestyrelsen i uppdragsbeskrivningar och rapporter. Termen kopplar också till det bredare "utanförskap"-begreppet i svensk socialpolitisk diskurs, vilket är korrekt givet DigComp-definitionens fokus på deltagande i ekonomiskt, socialt och politiskt liv.

**Noterat motargument:** "Exkludering" betonar den aktiva handlingen (någon exkluderas *av* systemet), medan "utanförskap" kan läsas som passivt tillstånd. Detta är en reell semantisk skillnad och kan komma att omprövas. För DigidelGov-sammanhang, där strukturella barriärer är centrala, kan "digital exkludering" vara mer precist i vissa texter. Beslutet gäller ramverkstermen; analysen i förklarande texter kan vara finkornigare.

---

## Mall för nya poster

```markdown
## ÅÅÅÅ-MM-DD — "EN-term" → "SV-term"

**Alternativ övervägda:** ...

**Valt:** ...

**Motivering:** ...

**Påverkar:** [LO-ID:n eller CS-ID:n som berörs, eller generell påverkan]

**Källa:** [Om valet stöds av etablerad svensk källa – länk eller referens]
```
