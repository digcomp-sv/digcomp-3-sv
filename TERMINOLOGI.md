# Terminologi

Kontrollerad termlista för den svenska översättningen av DigComp 3.0. Samlar alla svenska val som fastställts i projektet – både termer ur JRC:s egen glossary och de strukturella beteckningar som ramverket använder (kompetensområden, kompetenser, nivåer, dimensioner).

## Filens roll

Detta är det redaktionella arbetsdokumentet där alla fastställda svenska val finns tillgängliga att slå upp. Maskinläsbar motsvarighet för JRC:s 126 glossary-termer finns i `data/sv/glossary.json`. Beslutshistoriken med motiveringar finns i `docs/decision_log.md` – termer som krävt avvägning hänvisar till DL-ID där resonemanget finns. Översättningsprinciperna som styr valen finns i `docs/translation_principles.md`.

## Koppling till datan

Fastställda val i denna fil ska synkas med motsvarande fält i JSON-filerna i `data/sv/`:

| Sektion i TERMINOLOGI | JSON-fil | Fält |
|---|---|---|
| Kompetensområden | `competence_areas.json` | `name.sv` |
| Kompetenser | `competences.json` | `name.sv` |
| Kompetensnivåer (4-nivå) | `proficiency_levels.json` | `four_level[].name.sv` |
| EQF-nivåer (8-nivå) | `proficiency_levels.json` | `eight_level[].parent_level_name.sv` |
| Dimensioner | `learning_outcomes.json` | `dimension` (oöversatt strukturfält) |
| AI-etiketter | `learning_outcomes.json`, `competence_statements.json` | `ai_label` (behålls oöversatta) |
| Alfabetisk termlista (JRC) | `glossary.json` | `term.sv` |

Tilläggstermer i den alfabetiska listan som inte finns i JRC:s glossary (markerade *Ej i JRC:s glossary*) har ingen JSON-motsvarighet.

Synkningen är idag manuell. Ett script för automatisk synk kan läggas till i `scripts/` senare.

## Status per post

Varje post har en status:

- ✅ **Fastställt.** Svenskt val är bekräftat och används konsekvent.
- 🟡 **Pågående.** Förslag finns men är inte slutgiltigt. Kan komma att ändras.
- ⬜ **TBD.** Ingen svensk term fastställd än.

## Innehåll

1. [Ramverksstruktur](#ramverksstruktur)
   - [Kompetensområden](#kompetensområden)
   - [Kompetenser](#kompetenser)
   - [Kompetensnivåer (4-nivåskalan)](#kompetensnivåer-4-nivåskalan)
   - [EQF-nivåer (8-nivåskalan)](#eqf-nivåer-8-nivåskalan)
   - [Dimensioner](#dimensioner)
   - [AI-etiketter](#ai-etiketter)
2. [Alfabetisk termlista](#alfabetisk-termlista)

---

# Ramverksstruktur

## Kompetensområden

De fem huvudområden som DigComp 3.0 delar in digital kompetens i. Namnen följer substantivform genomgående, med variation i struktur anpassad efter områdets inre logik. Se **DL-006** för motivering.

| ID | EN | SV | Status |
|---|---|---|---|
| 1 | Information search, evaluation and management | Sökning, bedömning och hantering av information | ✅ |
| 2 | Communication and collaboration | Kommunikation och samarbete | ✅ |
| 3 | Content creation | Skapande av innehåll | ✅ |
| 4 | Safety, wellbeing, and responsible use | Säkerhet, välbefinnande och ansvarsfullt användande | ✅ |
| 5 | Problem identification and solving | Problemidentifiering och problemlösning | ✅ |

## Kompetenser

De 21 kompetenser som fördelas över de fem områdena.

| ID | EN | SV | Status |
|---|---|---|---|
| 1.1 | Browsing, searching and filtering information | — | ⬜ |
| 1.2 | Evaluating information | — | ⬜ |
| 1.3 | Managing information | — | ⬜ |
| 2.1 | Interacting through and with digital technologies | — | ⬜ |
| 2.2 | Sharing through digital technologies | — | ⬜ |
| 2.3 | Engaging in citizenship through digital technologies | — | ⬜ |
| 2.4 | Collaborating through digital technologies | — | ⬜ |
| 2.5 | Digital behaviour | — | ⬜ |
| 2.6 | Managing digital identity | — | ⬜ |
| 3.1 | Developing digital content | — | ⬜ |
| 3.2 | Integrating and re-elaborating digital content | — | ⬜ |
| 3.3 | Copyright and licences | — | ⬜ |
| 3.4 | Computational thinking and programming | — | ⬜ |
| 4.1 | Protecting devices | — | ⬜ |
| 4.2 | Protecting personal data and privacy | — | ⬜ |
| 4.3 | Supporting wellbeing | — | ⬜ |
| 4.4 | Environmental impacts of digital technologies | — | ⬜ |
| 5.1 | Identifying and solving technical problems | — | ⬜ |
| 5.2 | Identifying needs and digital technological responses | — | ⬜ |
| 5.3 | Identifying creative solutions using digital technologies | — | ⬜ |
| 5.4 | Identifying and addressing digital competence needs | — | ⬜ |

## Kompetensnivåer (4-nivåskalan)

De fyra övergripande nivåerna för bedömning av kompetens. Se **DL-003** för motivering.

| EN | SV | Status |
|---|---|---|
| Basic | Grund | ✅ |
| Intermediate | Medel | ✅ |
| Advanced | Avancerad | ✅ |
| Highly advanced | Mycket avancerad | ✅ |

## EQF-nivåer (8-nivåskalan)

DigComp 3.0:s koppling till European Qualifications Framework (EQF) på åtta nivåer. Namnen ärvs från 4-nivåskalan genom `parent_level_name`. Ingen egen översättning av nivåetiketterna utöver det.

| EQF-nivå | CEFR-stil | Förälder (EN) | Förälder (SV) |
|---|---|---|---|
| 1 | A1 | Basic | Grund |
| 2 | A2 | Basic | Grund |
| 3 | B1 | Intermediate | Medel |
| 4 | B2 | Intermediate | Medel |
| 5 | C1 | Advanced | Avancerad |
| 6 | C1 | Advanced | Avancerad |
| 7 | C2 | Highly advanced | Mycket avancerad |
| 8 | C2 | Highly advanced | Mycket avancerad |

## Dimensioner

De tre dimensioner som learning outcomes klassificeras i. Se **DL-008** för motivering av "Attityder" (ersätter tidigare "Förhållningssätt" enligt DL-002).

| EN | SV | Status |
|---|---|---|
| Knowledge | Kunskap | ✅ |
| Skill | Färdighet | ✅ |
| Attitude | Attityder | ✅ |

## AI-etiketter

DigComp 3.0 markerar varje learning outcome och competence statement med en AI-etikett. Etiketterna behålls oöversatta i datan som tekniska etiketter. Beskrivningen av dem kan översättas i dokumentation.

| Etikett | Betydelse | Status |
|---|---|---|
| AI-Explicit | Posten hänvisar explicit till AI-system. | ✅ (oöversatt) |
| AI-Implicit | Posten berör AI utan att nämna det explicit. | ✅ (oöversatt) |
| AI not Implicit or Explicit | Posten berör inte AI. | ✅ (oöversatt) |

---

# Alfabetisk termlista

Alla fastställda svenska val samlade i alfabetisk ordning efter den engelska termen. JRC:s 126 glossary-termer finns med; även ramverkselement (kompetensområden, nivåer, dimensioner) dubbelförs hit för snabb uppslagning. Poster markerade ⬜ är sådana där svenskt val inte är fastställt.

## A

**Accessibility** → **Tillgänglighet** ✅
Den utsträckning i vilken produkter, system, tjänster, miljöer och faciliteter kan användas av människor med bredast möjliga spann av användarbehov och förmågor.
Källa: DOS-lagen (2018:1937), WCAG 2.1.

**Advanced** → **Avancerad** ✅
Se Kompetensnivåer i Ramverksstruktur. **DL-003**.

**AI-Explicit** → **AI-Explicit** ✅ *(oöversatt)*
Teknisk etikett i DigComp 3.0 som behålls på engelska i datan.

**AI-Implicit** → **AI-Implicit** ✅ *(oöversatt)*
Teknisk etikett i DigComp 3.0 som behålls på engelska i datan.

**AI not Implicit or Explicit** → **AI not Implicit or Explicit** ✅ *(oöversatt)*
Teknisk etikett i DigComp 3.0 som behålls på engelska i datan.

**AI system** → **AI-system** ✅
Ett maskinbaserat system som är utformat för att fungera med varierande grader av autonomi och som, för explicita eller implicita mål, härleder hur utdata ska genereras utifrån indata.
Källa: AI-förordningen (EU) 2024/1689, art. 3.

**Algorithm** → **Algoritm** ✅
Källa: SAOL.

**Anonymisation** → **Anonymisering** ✅
Behandling av data i syfte att oåterkalleligen förhindra identifiering av en enskild person.
Källa: Dataskyddsförordningen (GDPR), skäl 26.

**Antivirus software** → **Antivirusprogram** ✅
Källa: Etablerad.

**Application/App** → ⬜

**Assistive technologies** → **Hjälpmedel / tekniska hjälpmedel** ✅
I DigComp-kontext avses digitala hjälpmedel. Exempel: skärmläsare, anpassade tangentbord, läsassistenter.
Källa: Socialstyrelsens begreppssamling, MFD.

**Attitude** → **Attityder** ✅
Dimension i learning outcomes. **DL-008** (ersätter DL-002 som valde "Förhållningssätt"). Följer EU:s officiella svenska översättning i rådets rekommendation om nyckelkompetenser och i DigComp 2.2 på svenska.

## B

**Baiting** → **Baiting** ✅ *(oöversatt)*
Hänvisar till Social engineering i JRC:s glossary. Termen behålls oöversatt i svensk cybersäkerhetslitteratur.

**Basic** → **Grund** ✅
Se Kompetensnivåer i Ramverksstruktur. **DL-003**.

**Bias** → **Snedvridning / bias** 🟡
Systematisk avvikelse från ett sant värde. Förekommer som subjektiv, data-, algoritm-, utvecklar- och institutionaliserad bias.
Källa: AI-förordningen använder "bias". Slutligt val inte fastställt.

**Big data** → **Stordata** ✅
Källa: Språkrådet, terminologicentrum TNC.

## C

**Chatbot** → **Chattbot** ✅
Källa: Språkrådets rekommendation.

**Circular economy model** → ⬜

**Clickbait** → ⬜

**Cloud services** → **Molntjänster** ✅
Källa: Språkrådet.

**Competence statement** → ⬜

**Complex (task)** → **komplex (uppgift)** ✅
I DigComp definieras en komplex uppgift som en som inte är väldefinierad och består av många olika sammanlänkade delar. Antonym till "simple" och strukturellt motpol till "well-defined".

**Computable and non-computable problems** → ⬜

**Computational thinking** → ⬜

**Computer program** → ⬜

**Constructive alignment** → ⬜

**Copyright** → **Upphovsrätt** ✅
Källa: Upphovsrättslagen (1960:729).

**Creative Commons (licences)** → **Creative Commons-licenser** ✅
Egennamn på licensfamiljen; behålls oöversatt i grundformen.

**Cyber threat** → **Cyberhot** ✅
Källa: MSB.

**Cyberattack** → **Cyberattack** ✅
Källa: MSB.

**Cyberbullying** → **Nätmobbning** ✅
Källa: MSB, BRIS.

**Cybercrime** → **It-brottslighet** ✅
Källa: Polisen, MSB.

**Cybersecurity** → **Cybersäkerhet** ✅
Källa: MSB.

## D

**Data** → **Data** ✅
Källa: Etablerad.

**Data analysis** → **Dataanalys** ✅
Källa: Etablerad.

**Data backup** → **Säkerhetskopiering** ✅
Källa: MSB, Språkrådet.

**Data centre** → **Datacenter** ✅
Källa: Etablerad.

**Data collection tool** → ⬜

**Data processing** → **Databehandling** ✅
Källa: GDPR svensk version, art. 4.

**Data protection** → **Dataskydd** ✅
Källa: Dataskyddsförordningen (EU) 2016/679, svensk version.

**Data removal rights** → ⬜

**Data restoration** → **Dataåterställning** ✅
Källa: MSB.

**De-bunking** → ⬜

**Deceptive patterns** → ⬜

**Deep-fake** → **Djupförfalskning / deepfake** 🟡
Källa: MSB använder "deepfake" oöversatt; Språkrådet föreslår "djupförfalskning". Slutligt val inte fastställt.

**Design thinking** → ⬜

**Digital assistance tool** → ⬜

**Digital citizenship** → ⬜

**Digital collaboration tool** → ⬜

**Digital communication** → ⬜

**Digital communication tool** → ⬜

**Digital competence** → **Digital kompetens** ✅
*Ej i JRC:s glossary men används som ramverkets övergripande begrepp.*
Källa: Etablerad term i svensk utbildningskontext, Lgr 22.

**Digital content** → ⬜

**Digital content creation tool** → ⬜

**Digital device** → **Digital enhet** ✅
Källa: Etablerad.

**Digital environment** → ⬜

**Digital exclusion** → **Digital exkludering** ✅
**DL-005** (ersatte DL-001).

**Digital footprint** → **Digitalt fotavtryck / digitala spår** 🟡
Slutligt val inte fastställt.

**Digital identity** → **Digital identitet** ✅
Källa: eIDAS-förordningen, DIGG.

**Digital inclusion** → **Digital inkludering** ✅
Källa: PTS regeringsuppdrag 2023-02-23 (Digital inkludering).

**Digital interaction** → ⬜

**Digital legislation** → ⬜

**Digital literacy** → ⬜
*Ej i JRC:s glossary. Förekommer i DigComp-texter och behöver fastställas.* "Litteracitet" är inte ett etablerat svenskt uttryck; svenskt val bör vägas mot MIK-terminologin.

**Digital participation** → ⬜

**Digital platforms and services** → **Digitala plattformar och tjänster** ✅
Källa: DSA (förordning (EU) 2022/2065), svensk version.

**Digital reputation** → ⬜

**Digital search tool** → ⬜

**Digital services** → **Digitala tjänster** ✅
JRC:s glossary hänvisar denna term till Digital platforms and services.
Hänvisar till Digital platforms and services i JRC:s glossary.

**Digital stress** → ⬜

**Digital technologies** → ⬜

**Digital tool** → ⬜

**Disinformation** → **Desinformation** ✅
Falsk eller vilseledande information som avsiktligt skapas och sprids för att bedra. **DL-004**.
Källa: MSB, Psykologiskt försvar.

## E

**E-commerce** → **E-handel** ✅
Källa: Etablerad.

**Emoji** → **Emoji** ✅
Källa: Etablerad.

**Ethical (usage of digital technologies)** → **Etisk användning** 🟡
Svensk formulering inte slutligt fastställd.

**European Qualifications Framework (EQF)** → **Europeiska referensramen för kvalifikationer** ✅
Källa: Europeiska unionens råd (2018), se ordlista <https://eur-lex.europa.eu/legal-content/SV/TXT/HTML/?uri=CELEX:32018H1210(01)>.

**External storage** → **Extern lagring** ✅
Källa: Etablerad.

## F

**Filter bubble** → **Filterbubbla** ✅
Källa: Språkrådet.

## G

**Gamification** → **Spelifiering** ✅
Källa: Språkrådet.

**Generative AI** → **Generativ AI** ✅
Källa: AI-förordningen svensk version.

## H

**High-risk AI system** → **AI-system med hög risk** ✅
Källa: AI-förordningen art. 6.

**Highly advanced** → **Mycket avancerad** ✅
Se Kompetensnivåer i Ramverksstruktur. **DL-003**.

**Human-AI collaboration** → ⬜

**Human-centric** → ⬜

## I

**Identity theft** → **Identitetsstöld** ✅
Källa: Polisen, Brottsförebyggande rådet.

**Intellectual property** → **Immateriella rättigheter** ✅
Källa: PRV, immaterialrättslagstiftning.

**Intermediate** → **Medel** ✅
Se Kompetensnivåer i Ramverksstruktur. **DL-003**.

## J

**JSON** → **JSON** ✅ *(oöversatt)*
Akronym för JavaScript Object Notation. Används oöversatt på svenska.

## K

**Knowledge** → **Kunskap** ✅
Dimension i learning outcomes.

## L

**Learning outcomes** → ⬜

**Licence** → **Licens** ✅
Källa: Etablerad.

**Linked open data** → **Länkade öppna data** ✅
Källa: DIGG, Riksarkivet.

## M

**Machine learning** → **Maskininlärning** ✅
Källa: Etablerad.

**Malware** → **Skadlig kod** ✅
Källa: MSB.

**Misinformation** → **Missinformation** ✅
**DL-004**.
Källa: Institutet för språk och folkminnen.

**Multi-factor authentication** → **Multifaktorautentisering / flerfaktorsautentisering** ✅
Källa: MSB, DIGG.

## N

**National Qualifications Framework (NQF)** → **Nationell referensram för kvalifikationer** ✅
Källa: Europeiska unionens råd (2018), se ordlista <https://eur-lex.europa.eu/legal-content/SV/TXT/HTML/?uri=CELEX:32018H1210(01)>.

**Nudging** → ⬜
Används ofta oöversatt i svensk forskning.

## O

**Online platform** → **Onlineplattform** ✅
JRC:s glossary hänvisar denna term till Digital platforms and services.
Hänvisar till Digital platforms and services i JRC:s glossary.

**Online service** → **Onlinetjänst** ✅
JRC:s glossary hänvisar denna term till Digital platforms and services.
Hänvisar till Digital platforms and services i JRC:s glossary.

**Open data** → **Öppna data** ✅
Källa: DIGG, PSI-lagen.

**Open educational resources (OER)** → ⬜

**Operating system** → **Operativsystem** ✅
Källa: Etablerad.

## P

**Peripheral device** → **Kringutrustning** ✅
Källa: Etablerad.

**Personal data** → **Personuppgifter** ✅
Källa: GDPR art. 4.

**Personalisation** → ⬜

**Phishing** → **Nätfiske** ✅
Källa: MSB, Polisen.
Hänvisar till Social engineering i JRC:s glossary.

**Piracy** → **Piratkopiering** ✅
Källa: Etablerad.

**Plagiarism** → **Plagiat** ✅
Källa: Etablerad.

**Platform economy** → ⬜

**Pre-bunking** → ⬜

**Privacy** → ⬜

**Privacy tool** → ⬜

**Problem solving** → **Problemlösning** ✅
Källa: Etablerad.

**Proficiency level** → **Kompetensnivå** ✅
Källa: SeQF.

**Pseudonymisation** → **Pseudonymisering** ✅
Källa: GDPR skäl 26.

## R

**Reality-virtuality (RV) continuum** → ⬜

**Responsible use (of digital technologies)** → **Ansvarsfullt användande** ✅
Följer samma språkval som i område 4 (se **DL-006**).

**Right to disconnect** → **Rätten att koppla ned** ✅
Källa: Europaparlamentets resolution 2020/2121(INL) svensk version.

**Robot** → **Robot** ✅
Källa: Etablerad.

**Robotics** → **Robotik** ✅
Källa: Etablerad.

## S

**Simple (task)** → **enkel (uppgift)** ✅
I DigComp definieras en enkel uppgift som en som är väldefinierad och består av få delar. Antonym till "complex".

**Skill** → **Färdighet** ✅
Dimension i learning outcomes.

**Social engineering** → **Social manipulation** ✅
Källa: MSB.

**Social innovation** → ⬜

**Social media** → **Sociala medier** ✅
Källa: Etablerad.

**Social media influencer** → ⬜

**Software** → **Programvara / mjukvara** ✅
Källa: Etablerad.

**Specialised (purpose, task)** → ⬜

## T

**Task** → **Uppgift** ✅
Källa: Etablerad.

**Trustworthy AI** → **Tillförlitlig AI** ✅
Källa: AI-förordningen, Högnivågruppen för AI:s etiska riktlinjer.

## U

**United Nations (UN) Global Digital Compact (GDC)** → ⬜

**Universal Meaningful Connectivity (UMC)** → ⬜

**'Unplugged' activities** → ⬜

**User experience (UX) and Customer experience (CX)** → ⬜

## V

**Virtual assistant** → **Virtuell assistent** ✅
Källa: Etablerad.

**Virtual reality, realities (VR)** → **Virtuell verklighet (VR)** ✅
Källa: Etablerad.

## W

**Wellbeing** → **Välbefinnande** ✅
*Ej i JRC:s glossary som fristående term; JRC har "Wellbeing (in digital environments)".*
Källa: Folkhälsomyndigheten, målområde 7.

**Wellbeing (in digital environments)** → **Välbefinnande** ✅
Se Wellbeing.
Källa: Folkhälsomyndigheten, målområde 7.

**Well-defined (task, problem)** → **väldefinierad (uppgift, problem)** ✅
*Ej i JRC:s glossary som fristående term men förekommer återkommande i CS/LO-texterna och i definitionerna av "simple" och "complex".*
DigComp använder "well-defined" i teknisk betydelse från problemlösningsforskning: ett problem där starttillstånd, måltillstånd och tillåtna operationer är strukturellt specificerade. Inte att förväxla med "avgränsad" (som refererar till skala/omfattning, inte struktur).
Källa: Etablerad svensk fackterm i kognitionspsykologi och problemlösningsforskning (Newell & Simon-traditionen).
