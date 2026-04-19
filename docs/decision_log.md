# Terminologibeslut

Detta dokument registrerar avvägningar som gjorts mellan möjliga svenska termer där valet inte var självklart. Varje post har datum, beslutsfattare, alternativ, valt alternativ och motivering. Tidigare beslut kan revideras – i så fall läggs en ny post till, den gamla stryks inte.

---

## 2026-04-19 — Proficiency level names (4-nivåskalan)

**Alternativ övervägda:** Grundläggande/Mellannivå/Avancerad/Mycket avancerad; Grundläggande/Medelgod/Avancerad/Expertnivå; Grund/Fördjupad/Avancerad/Mycket avancerad; Grund/Medel/Hög/Avancerad; Grund/Medel/Avancerad/Expert; Grund/Medel/Avancerad/Specialist; Grund/Medel/Avancerad/Specialiserad; Grund/Medel/Avancerad/Särskilt specialiserad; Grund/Medel/Avancerad/Högt specialiserad.

**Valt:** Grund / Medel / Avancerad / I hög grad specialiserad.

**Motivering:** De engelska termerna i DigComp 3.0 är Foundation/Intermediate/Advanced/Highly specialised (tidigare formulering i detta dokument – "Basic/.../Highly advanced" – korrigeras härmed). Översättningen behöver bevara det kvalitativa språnget mellan nivå 3 och 4. "Advanced" beskriver självständig kompetensutövning i bredd, medan "highly specialised" beskriver smal djupkompetens i ett avgränsat område, ofta i en roll där personen utvecklar lösningar för andra. En platt progression där nivå 4 bara blir "mer avancerat" än nivå 3 missar ramverkets poäng.

Substantivformer som "Expert" och "Specialist" förkastades eftersom de drar mot att beskriva personen som helhet snarare än kompetensutövningen i en specifik kompetens. Detta ligger fel i DigComp, där en och samma person kan befinna sig på olika nivåer i olika kompetenser. JRC har också medvetet valt bort "expert" i den engelska versionen av samma skäl, och den svenska översättningen bör respektera den avvägningen. "Specialist" har dessutom en stark medicinsk konnotation på svenska som stör läsningen i andra sektorskontexter.

"Specialiserad" ensamt bevarar adjektivform men tappar intensifieraren "highly" och riskerar att läsas som "bara specialiserad". "Särskilt specialiserad" försöker bevara intensifieraren men "särskilt" är på svenska tvetydigt mellan "i synnerhet" och "i hög grad" – tvetydigheten försvagar nivåmarkeringen. "Högt specialiserad" är entydigt och kortare, men "I hög grad specialiserad" valdes för att den fulla formen är mer omisskännlig i löpande text och tydligare signalerar att "highly" avser grad av specialisering, inte att specialiseringen ligger "högt upp" i något annat avseende.

Varken "Grund/Medel/Hög/Avancerad" eller "Grund/Fördjupad/Avancerad/Mycket avancerad" bevarar kopplingen till originalets "advanced" på nivå 3. "Hög" är dessutom en svag kompetensmarkör som inte säger något specifikt om vad nivån innebär. "Mellannivå", "Medelgod" och "Fördjupad" förkastades till förmån för det kortare "Medel", som ger en jämnare längdprofil över de tre första nivåerna.

SeQF har inga helt motsvarande nivåer och gav därför ingen bindande vägledning. Den 8-nivåbaserade EQF-kopplingen i DigComp 3.0 hanteras som separat beslut.

**Påverkar:** `data/sv/proficiency_levels.json` (4-nivåskalan); samtliga CS- och LO-texter som innehåller nivåhänvisningar; GLOSSARY.md (termparet "highly specialised ↔ i hög grad specialiserad" läggs in).

**Not om gränssnitt:** Den fulla etiketten "I hög grad specialiserad" är lång och kan behöva kortas i tabellrubriker eller självskattningsverktyg. Kortformer hanteras som separat gränssnittsbeslut och får inte ändra den normativa benämningen i datafilerna.

---

## 2026-04-19 — REVIDERING: "Digital exclusion" → "Digital exkludering"

**Tidigare beslut (2026-04-18):** Digitalt utanförskap.

**Reviderat till:** Digital exkludering.

**Motivering:** Vid närmare övervägande väger den strukturella precisionen tyngre än matchningen mot myndighetspraxis. "Exkludering" betonar det aktiva skeendet – att någon eller något exkluderar – medan "utanförskap" tonar ner den systemiska dimensionen och placerar fokus på den uteslutnas tillstånd. 

DigComp:s egen definition ("marginalisation of an individual... deprived of full access") beskriver ett aktivt skeende. Inte ett passivt tillstånd. Och den svenska översättningen bör spegla detta.

Myndighetstermen "digitalt utanförskap" är väletablerad men bär en semantisk förenkling som inte passar i ett ramverk med rättighetsperspektiv.

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
