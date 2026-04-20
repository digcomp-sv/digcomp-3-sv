# Så bidrar du

## Kort version

1. Öppna ett **issue** för terminologifrågor innan du översätter en hel kompetens – det sparar tid.
2. Jobba på en **branch**, inte på `main`.
3. Översätt **en kompetens i taget**, inte spridda poster.
4. Öppna en **pull request** med tydlig titel: `[CS 1.2] Översättning av kompetenspåståenden för Evaluating information`.
5. I PR-beskrivningen: lista eventuella terminologival som krävt avvägning och referera till relevant DL-ID i `docs/decision_log.md`.

## Om arbetsflödet

Reglerna ovan gäller bidragsgivare utifrån. Projektägaren arbetar under projektets tidiga fas (version 0.x) direkt på `main` för underhåll och strukturella ändringar. När projektet mognar och fler bidragsgivare involveras kommer ägaren också gå över till branch- och PR-flöde.

## Översättningsprocess per post

I JSON-filen:

```json
{
  "id": "LO1.2.16",
  "competence_id": "1.2",
  "proficiency_level": "Intermediate",
  "dimension": "Knowledge",
  "ai_label": "AI-Explicit",
  "text": {
    "en": "Recognise that AI systems may produce output which is inaccurate, even if it may seem plausible.",
    "sv": "Känner till att AI-system kan generera utdata som är felaktiga, även när de framstår som trovärdiga."
  },
  "translation_status": "draft",
  "translator": "@anvandarnamn",
  "reviewed_by": null,
  "last_updated": "2026-04-18",
  "notes": null
}
```

**translation_status** följer ett fast flöde:

* `not_started` → `draft` → `needs_review` → `reviewed` → `final`

Endast releasegranskare sätter `final`.

## Terminologidisciplin

Innan du översätter en mening:

1. Läs `docs/translation_principles.md`.
2. Slå upp varje fackterm i `TERMINOLOGI.md`.
3. Om termen finns i listan – använd den ordagrant. Variera inte för språklig elegans.
4. Om termen inte finns i listan och är ny – öppna ett issue med förslag innan du använder den i datan.

## När något inte passar

DigComp är skrivet med global EU-publik i åtanke. Vissa konstruktioner passar dåligt in i svensk förvaltningskultur. Exempel: "engaging in citizenship through digital technologies" har ingen självklar svensk motsvarighet. Då:

* Ta inte bort innehåll, kompromissa inte med betydelsen.
* Förklara tolkningsvalet i `notes`-fältet i JSON-posten.
* Lägg till en ny DL-post i `decision_log.md` om valet är principiellt.

## Att inte göra

* **Översätt inte ID:n.** `LO1.1.01` förblir `LO1.1.01`.
* **Översätt inte AI-etiketterna** (`AI-Implicit`, `AI-Explicit`, `AI not Implicit or Explicit`) i datan. De är tekniska etiketter.
* **Ändra inte strukturen** i JSON-filerna. Lägg inte till eller ta bort fält utan att först diskutera det i issue.
* **Redigera inte filerna i `sources/`.** De är orörda original.
