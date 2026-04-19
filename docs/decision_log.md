# Terminologibeslut

Detta dokument registrerar avvägningar som gjorts mellan möjliga svenska termer där valet inte var självklart. Varje post har datum, beslutsfattare, alternativ, valt alternativ och motivering. Tidigare beslut kan revideras – i så fall läggs en ny post till, den gamla stryks inte.

---

## 2026-04-18 — "Attitude" → "Förhållningssätt"

**Alternativ övervägda:** attityd, hållning, inställning, förhållningssätt.

**Valt:** Förhållningssätt.

**Motivering:** "Attityd" på svenska har en stark konnotation av subjektiv läggning eller åsikt. DigComp använder "attitude" i Bloom-traditionen där termen syftar på ett orienterande, handlingsberedskapsskapande förhållande till ett kunskapsområde. Svensk utbildningsterminologi (SeQF, gymnasieskolans ämnesplaner, högskoleförordningens bilaga 2) använder konsekvent "förhållningssätt" för denna dimension. Valet stärker också att DigComp läses som ett yrkesmässigt kompetensramverk, inte som ett personlighetsmått.

**Påverkar:** Alla 107 attityd-märkta LO:n, fältet `dimension` i `learning_outcomes.json`.

---

## 2026-04-18 — "Digital exclusion" → "Digitalt utanförskap"

**Alternativ övervägda:** digital exkludering, digitalt utanförskap, digital marginalisering.

**Valt:** Digitalt utanförskap.

**Motivering:** "Digital exkludering" är en kalkering som förekommer i EU-översättningar men sällan i svensk myndighetskommunikation. "Digitalt utanförskap" används av MSB, SKR, PTS och Post- och telestyrelsen i uppdragsbeskrivningar och rapporter. Termen kopplar också till det bredare "utanförskap"-begreppet i svensk socialpolitisk diskurs, vilket är korrekt givet DigComp-definitionens fokus på deltagande i ekonomiskt, socialt och politiskt liv.

**Noterat motargument:** "Exkludering" betonar den aktiva handlingen (någon exkluderas *av* systemet), medan "utanförskap" kan läsas som passivt tillstånd. Detta är en reell semantisk skillnad och kan komma att omprövas. För DigidelGov-sammanhang, där strukturella barriärer är centrala, kan "digital exkludering" vara mer precist i vissa texter. Beslutet gäller ramverkstermen; analysen i förklarande texter kan vara finkornigare.

---

## [TBD] — Proficiency level names

Översättningen av Basic/Intermediate/Advanced/Highly advanced är inte slutligt fastställd. SeQF använder inte helt motsvarande nivåer. Alternativ:

* Grundläggande / Mellannivå / Avancerad / Mycket avancerad *(förslag, se translation_principles.md)*
* Grundläggande / Medelgod / Avancerad / Expertnivå
* Grund / Fördjupad / Avancerad / Mycket avancerad

Avvakta remiss innan slutligt val.

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
