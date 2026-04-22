# Så bidrar du

Tack för att du är intresserad av att bidra till svensk översättning av DigComp 3.0. Projektet drivs för närvarande av Terese Raymond.

## Två sätt att bidra

Det finns två vägar in i projektet beroende på hur du vill arbeta.

### A. Förslag och frågor via issues

Issues är projektets diskussionsforum. Här kan vi resonera om terminologival, diskutera tolkningar och fånga upp fel. Ämneskompetens från olika håll bidrar till en mer genomtänkt översättning. Alla issues är öppna — vem som helst kan läsa tidigare diskussioner, kommentera, eller ta intryck av resonemang när de själva arbetar med liknande frågor.

Via Issues kan du också ställa frågor om översättningsprojektet eller DigComp i allmänhet.

Du är särskilt välkommen att öppna ett issue om du:

- har hittat ett fel eller en inkonsekvens
- vill föreslå en översättning utan att redigera filer själv
- undrar hur en viss term bör tolkas
- har ämneskompetens som kan förbättra ett terminologival
- vill diskutera en pågående översättning eller principfråga

Ingen teknisk vana krävs. Ingen fråga är för liten. Korta kommentarer är lika värdefulla som längre resonemang.

**Så gör du:**

1. Gå till [Issues-fliken](https://github.com/digcomp-sv/digcomp-3-sv/issues)
2. Klicka **"New issue"**
3. Skriv en tydlig rubrik som förklarar vad det handlar om
4. Beskriv förslaget, frågan eller felet i brödtexten
5. Om det gäller en specifik post i datan — ange gärna ID (t.ex. `LO1.2.16` eller `glossary: "Accessibility"`)

Projektägaren läser alla issues och svarar inom cirka en vecka. Godkända förslag förs in i datafilerna, tolkningsfrågor blir öppna diskussioner och principiella beslut dokumenteras som DL-poster i `decision_log.md`.

### B. Pull requests för översättning

Passar dig om du:
- är van vid Git och GitHub
- vill översätta en sammanhängande del av ramverket
- accepterar att följa etablerad terminologi och översättningsprinciper
- är beredd på att få feedback och göra justeringar

Så gör du:

1. **Öppna ett issue** först om du vill översätta en större del (till exempel en hel kompetens). Detta undviker dubbelarbete.
2. **Forka** repot till ditt eget GitHub-konto. (Fork = kopia av repot under ditt eget konto som du kan ändra fritt.)
3. **Skapa en branch** med ett beskrivande namn, till exempel `oversatt-kompetens-1-2` eller `glossary-forklaringar-del-1`. (Branch = separat arbetsspår där du gör dina ändringar utan att påverka huvudkoden.)
4. **Läs igenom** `docs/translation_principles.md` och `TERMINOLOGI.md` innan du börjar översätta.
5. **Översätt en kompetens i taget**, eller en annan sammanhängande enhet. Inte spridda poster.
6. **Öppna en pull request** med tydlig titel. (Pull request = förfrågan om att dina ändringar i din fork ska föras in i huvudrepot.) Exempel: `[CS 1.2] Översättning av kompetenspåståenden för "Evaluating information"`.
7. I PR-beskrivningen: lista terminologival som krävt avvägning och referera till relevant **DL-ID** i `docs/decision_log.md` om relevant. (DL-ID = identifierare för terminologibeslut, till exempel `DL-003`.)

## Vad händer efter du bidragit?

Projektägaren strävar efter att svara inom en vecka.

**Issues:** får kommentar, klassificeras, och antingen förs förslagen in i datan, besvaras eller diskuteras vidare.

**Pull requests:** granskas mot `TERMINOLOGI.md` och `translation_principles.md`. Om allt ser bra ut mergas PR:en. Om det behövs ändringar kommenteras PR:en med önskemål. Om en PR inte kan mergas som den är öppnas ett separat issue för att diskutera förbättringar tillsammans — PR:en lämnas öppen under diskussionen.

## Översättningsprocess per post

Här visas ett exempel ur JSON-filen på en post som ännu inte har blivit granskad (därför translation_status "draft")

```json
{
  "id": "LO1.2.16",
  "competence_id": "1.2",
  "proficiency_level": "Intermediate",
  "dimension": "Knowledge",
  "ai_label": "AI-Explicit",
  "text": {
    "en": "Recognise that AI systems may produce output which is inaccurate, even if it may seem plausible.",
    "sv": "Är medveten om att AI-system kan generera utdata som är felaktig, även när den framstår som rimlig."
  },
  "translation_status": "draft",
  "translator": "@tereseraymond",
  "reviewed_by": null,
  "last_updated": "2026-04-22",
  "notes": null
}
```

**translation_status** följer ett fast flöde:

* `not_started` → `draft` → `reviewed`

Vid granskning sätts reviewed_by och status ändras till "reviewed". Detta innebär att posten är godkänd för att pushas till main.

## Terminologidisciplin

Innan du översätter en mening:

1. Läs `docs/translation_principles.md`.
2. Slå upp varje fackterm i `TERMINOLOGI.md`.
3. Om termen finns i listan – använd den ordagrant. Variera inte för språklig elegans.
4. Om termen inte finns i listan och är ny – öppna ett issue med förslag innan du använder den i datan.

## När något inte passar

DigComp är skrivet för en EU-gemensam läsekrets. Vissa konstruktioner har ingen självklar svensk motsvarighet, som till exempel "engaging in citizenship through digital technologies". I sådana fall:

* Ta inte bort innehåll, kompromissa inte med betydelsen.
* Förklara tolkningsvalet i `notes`-fältet i JSON-posten.
* Lägg till en ny DL-post i `decision_log.md` om valet är principiellt.

## Att inte göra

* **Översätt inte ID:n.** `LO1.1.01` förblir `LO1.1.01`.
* **Översätt inte AI-etiketterna** (`AI-Implicit`, `AI-Explicit`, `AI not Implicit or Explicit`) i datan. De är tekniska etiketter.
* **Ändra inte strukturen** i JSON-filerna. Lägg inte till eller ta bort fält utan att först diskutera det i issue.
* **Redigera inte filerna i `sources/`.** De är orörda original.

## Om projektets arbetssätt just nu

Under projektets tidiga fas (version 0.x) arbetar projektägaren direkt på `main` för underhåll och strukturella ändringar. Bidragsgivare utifrån arbetar via branch och PR som beskrivet ovan. När projektet mognar och fler bidragsgivare involveras kommer även ägaren att gå över till branch- och PR-flöde. Se README-sektionen Versioner för hur versionsnummer tilldelas.
