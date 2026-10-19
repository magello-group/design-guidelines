# Magello Web Design Guidelines

> **Syfte:** instruktioner och frågor för att bygga nya webbprojekt från grunden, eller styla om existerande projekt, så att de får Magellos look and feel. Alla CSS-värden, polygonkoordinater och animationskurvor är exakta och kan kopieras rakt av.
>
> **Läs först:** `design-language.md` (formspråket i ord, oberoende av medium). Den här filen är webbimplementationen av samma principer och innehåller dessutom ett kapitel om hur komponenterna blir redaktörsvänliga byggstenar i **Strapi**.
>
> **Språk:** svenska. **Status:** speglar styleguiden i `styleguide/` (oktober 2026).

---

## Innehåll

1. [Så använder du dokumentet](#1-så-använder-du-dokumentet)
2. [Frågor inför start](#2-frågor-inför-start)
3. [Läge A — nytt projekt från grunden](#3-läge-a--nytt-projekt-från-grunden)
4. [Läge B — omstyling av ett existerande projekt](#4-läge-b--omstyling-av-ett-existerande-projekt)
5. [Beslutslogg — alla designbeslut i ett ögonkast](#5-beslutslogg--alla-designbeslut-i-ett-ögonkast)
6. [Designfilosofi](#6-designfilosofi)
7. [Polygonspråket — hur du skapar nya former](#7-polygonspråket--hur-du-skapar-nya-former)
8. [Komponenttänket — varje element är fristående](#8-komponenttänket--varje-element-är-fristående)
9. [Typografi — principer och skala](#9-typografi--principer-och-skala)
10. [Färgpalett & tokens](#10-färgpalett--tokens)
11. [Layout, bredd och linjering](#11-layout-bredd-och-linjering)
12. [Header — startsida](#12-header--startsida)
13. [Header — undersidor (rotation + sidospår)](#13-header--undersidor-rotation--sidospår)
14. [Dropdown-meny och undermenyer](#14-dropdown-meny-och-undermenyer)
15. [Mobilmeny (hamburgermeny)](#15-mobilmeny-hamburgermeny)
16. [Animationer — komplett lista](#16-animationer--komplett-lista)
17. [Knappar](#17-knappar)
18. [Sektioner & bakgrunder](#18-sektioner--bakgrunder)
19. [Bilder — behandling](#19-bilder--behandling)
20. [Ikoner & grafik](#20-ikoner--grafik)
21. [Kort (cards)](#21-kort-cards)
22. [Processsteg (chevrons)](#22-processsteg-chevrons)
23. [Tabell](#23-tabell)
24. [Artikel — undersidans layout](#24-artikel--undersidans-layout)
25. [Sidtitel och ingångssida](#25-sidtitel-och-ingångssida)
26. [Pullquote](#26-pullquote)
27. [Infoblock](#27-infoblock)
28. [Tidslinje](#28-tidslinje)
29. [Footer](#29-footer)
30. [Kontaktkort och uppmaningssektion (CTA)](#30-kontaktkort-och-uppmaningssektion-cta)
31. [Formulärkomponenter](#31-formulärkomponenter)
32. [Komponentstates](#32-komponentstates)
33. [Feedback & notifieringar](#33-feedback--notifieringar)
34. [Tool/app-layout](#34-toolapp-layout)
35. [Loading-indikatorer](#35-loading-indikatorer)
36. [Strapi — redaktörsvänliga komponenter](#36-strapi--redaktörsvänliga-komponenter)
37. [Logotyper & artefakter](#37-logotyper--artefakter)
38. [Fil- och katalogstruktur](#38-fil--och-katalogstruktur)
39. [Checklista för ny sida](#39-checklista-för-ny-sida)
40. [Snabbreferens — Skapa nya element](#40-snabbreferens--skapa-nya-element)
41. [Kända avvikelser i biblioteket](#41-kända-avvikelser-i-biblioteket)

---

## 1. Så använder du dokumentet

Det här dokumentet har två syften:

- **Läge A — nytt projekt:** bygg en webbplats eller ett verktyg från grunden med Magellos formspråk.
- **Läge B — omstyling:** ta ett existerande projekt (egen eller extern kodbas) och styla om det så att det följer formspråket, utan att ändra funktion eller innehåll.

Samma regler gäller i båda lägena. Skillnaden är startpunkten: i läge A börjar du med tomt papper, i läge B med en inventering.

### Snabbaste vägen: kopiera biblioteket, bygg markup

All CSS och JavaScript som behövs ligger färdig i repot:

- [`styleguide/css/magello.css`](../styleguide/css/magello.css) — tokens, bas, navigation, knappar, kort, formulär, feedback m.m. (ca 2 500 rader, uppdelad i sektioner).
- [`styleguide/js/magello.js`](../styleguide/js/magello.js) — header-scroll, sidospår, mobilmeny, dropdown och undermenyer (ca 140 rader, inga beroenden).

**Kopiera dem oförändrade till projektet och länka dem. Skriv inte om CSS:en från texten i det här dokumentet.** Sidorna är sedan bara markup (och högst ett tiotal rader sidspecifik CSS). Bygg dina sidor genom att kopiera markup från motsvarande referenssida. Textens CSS-block i det här dokumentet är till för att förklara *varför*; `magello.css` är facit.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&family=Roboto+Condensed:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/magello.css">
…
<script src="js/magello.js"></script>
```

### Arbetsordning (för Claude och för utvecklare)

1. **Fråga först.** Gå igenom [Frågor inför start](#2-frågor-inför-start). Föreslå standardvalet (★) och gå vidare när användaren inte har en åsikt. Fråga aldrig samma sak två gånger.
2. **Välj läge.** Finns det redan kod som ska stylas om → läge B ([avsnitt 4](#4-läge-b--omstyling-av-ett-existerande-projekt)). Annars läge A ([avsnitt 3](#3-läge-a--nytt-projekt-från-grunden)).
3. **Läs filosofin och beslutsloggen** ([avsnitt 5](#5-beslutslogg--alla-designbeslut-i-ett-ögonkast) och [6](#6-designfilosofi)). De förklarar *varför*, så att du kan lösa fall som dokumentet inte nämner.
4. **Kopiera `css/magello.css` och `js/magello.js` oförändrade** och bygg sidorna med markup från styleguide-sidorna. Komponentkapitlen förklarar hur varje komponent är tänkt att användas.
5. **Om innehållet ska redigeras i Strapi:** följ [Strapi-kapitlet](#36-strapi--redaktörsvänliga-komponenter) när du väljer vilka fält komponenterna ska ha.
6. **Verifiera** med checklistorna i slutet och mät, gissa inte (se [Linjering](#11-layout-bredd-och-linjering)).
7. **Rapportera avvikelser.** Måste du bryta mot en regel, säg vilken och varför. Lägg den i listan över kända avvikelser.

### Relation till övriga filer (katalogen `design-guidelines/`)

| Fil eller katalog | Innehåll | När du läser den |
|---|---|---|
| `AGENTS.md` | Instruktioner för AI-agenter: läsordning, arbetssätt, checklistor | Agenter läser den först |
| `docs/design-language.md` | Designspråket i ord, utan webbspecifika detaljer | Alltid först. Gäller även PowerPoint, Word och PDF |
| `docs/design-guidelines-web.md` (den här) | Webbimplementation: tokens, CSS, komponenter, navigation, Strapi | Alla webbprojekt |
| `tokens/tokens.json` | Färg, typografi, avstånd, rörelse, former (polygoner) och regler som maskinläsbara värden | Agenter och verktyg som genererar grafik |
| `styleguide/css/magello.css`, `styleguide/js/magello.js` | **Det delade biblioteket**: all CSS och JS | **Kopiera rakt av.** Facit för utseende och beteende |
| `styleguide/*.html` | Styleguiden: levande exempel och bruksanvisning per komponent | **Facit för markup.** Formulär och feedback: `formular-feedback.html`. Markdown: `markdown.html` |
| `assets/` | Logotyper, ikoner, svartvita foton, SVG-former (`shapes/`), mallar (`templates/`) | Kopiera eller länka till dem |
| `DECISIONS.md` | Logg över designbeslut med datum | När du vill förstå eller ändra något |

### Använd katalogen som referens i andra projekt

Lägg ett par rader i det andra projektets `CLAUDE.md` eller `AGENTS.md` (byt sökväg till där katalogen ligger, eller använd repo-URL:en https://github.com/magello-group/design-guidelines):

```markdown
## Design
Följ Magellos designspråk. Läs hela design-guidelines/AGENTS.md och
design-guidelines/docs/design-guidelines-web.md innan du ändrar UI.
Kopiera design-guidelines/styleguide/css/magello.css och js/magello.js oförändrade.
Facit för markup och bruksanvisning är design-guidelines/styleguide/.
Värden (färg, typ, former) finns i design-guidelines/tokens/tokens.json.
Svara på frågorna i avsnitt 2 innan du börjar.
```

**Facit är `styleguide/css/magello.css`, sidorna i `styleguide/` och `tokens/tokens.json`, inte din tolkning av texten.** För typografi (avsnitt 9), formulär (31–35), knappar (17) och layout (11): använd `magello.css` och kopiera markup från motsvarande styleguide-sida. Avviker resultatet visuellt, åtgärda tills det matchar.

### Regler om regler

- **Principerna är viktigare än enskilda värden.** Hitta aldrig på en lösning som bryter mot en princip bara för att dokumentet inte nämner situationen. Härled från principerna.
- **Exakta värden är exakta.** CSS-värden, polygonkoordinater och tidskurvor kan kopieras rakt av.
- **Mät, gissa inte.** Linjering, avstånd och höjder ska verifieras i webbläsaren.
- **Odefinierade tokens är fel.** En `var(--mg-...)` som saknas gör hela CSS-deklarationen ogiltig utan felmeddelande (se beslutsloggen).
- **Bygg inte om innehållet.** I läge B ändrar du utseende, inte texter, URL:er eller funktion, om inte användaren ber om det.
- **Webbplatsen är bara på svenska** (`lang="sv"`), om inte användaren uttryckligen säger annat.
---

## 2. Frågor inför start

Ställ frågorna i ordning. De första sju är generella och gäller alla Magello-projekt (de motsvarar frågorna i `design-language.md`). Resten är webbspecifika. ★ = standardval om användaren inte har en åsikt.

### Del 1 — Generella frågor

1. **Vad ska skapas, och i vilket syfte?** Informera, sälja, rekrytera, ett verktyg som någon använder? ★ Publik informationswebb som presenterar Magello och dess tjänster.
2. **Vem är målgruppen?** ★ Chefer, rekryterare och beställande IT-personer.
3. **Vilken ton ska det ha?** ★ Professionell, avskalad, tydlig och typografisk, med lekfullheten i formerna.
4. **Finns referenser som ska efterliknas eller undvikas?** ★ volvocars.com/se och tesla.com som bas: luft, stor typografi, få element.
5. **Vilket är budskapet som ska fastna hos besökaren?** Det styr hero och struktur.
6. **Vilka bilder, ikoner och texter finns redan?** ★ `images/black-and-white/` och `graphics/`. Saknas text: skriv den på svenska enligt tonen i general-filen.
7. **Hur dramatisk ska formen vara?** ★ Polygonspråk enligt avsnitt 7, mest dramatik i hero och sektionsavdelare, lugnare i innehåll.

### Del 2 — Typ av produkt

8. **Vad är det för typ av produkt?**
   - ★ **Publik informationswebb** — besökare surfar och läser (magello.se, tjänstesidor, case, artiklar).
   - **Verktyg/app** — användaren gör något aktivt: laddar upp, konfigurerar, genererar, sparar. Se [Tool/app-layout](#34-toolapp-layout).
   - **Blandat** — publik del plus inloggad del. Fråga vilken del som ska formges nu.
9. **Ska det finnas en meny, och vilken typ?**
   - ★ **Som magello.se** — header som roterar bort och blir ett sidospår vid scroll, med hamburgermeny på mobil.
   - **Applikationsmeny** — fast mörk rosagrå topbar (`#3D2535`) med logotyp och primär handling.
   - **Ingen meny** — single-page eller stegvis flöde.
10. **Hur många menynivåer?** ★ Två: huvudlänkar med högst en undernivå. Avgör om dropdown och accordion behövs.
11. **Ska innehållet ta upp hela bredden?** ★ Blandat: hero och bildytor går ut mot kanten, text och komponenter i en container på `1280px` (1200 px innehåll). Verktyg: full bredd.
12. **Finns formulär eller inmatningsfält?** Om ja: realtidsvalidering vid blur eller bara vid submit? ★ Vid blur. Se [Formulär](#31-formulärkomponenter).
13. **Finns feedback till användaren (bekräftelser, fel, laddning)?** ★ Toast för kort feedback, spinner under 3 s, progressbar eller overlay över 3 s.

### Del 3 — Teknik och leverans

14. **Vilket ramverk eller vilken stack används?** (Ren HTML/CSS, React/Vite, Next.js, Astro, annat.) ★ Ramverksneutral CSS med `mg-`-klasser som fungerar i allt.
15. **Ska projektet ha ett CMS?** ★ Strapi. Då gäller [Strapi-kapitlet](#36-strapi--redaktörsvänliga-komponenter): vem redigerar, behövs förhandsvisning (draft/preview), vilken mediahantering (lokalt, S3, Azure Blob)?
16. **Hur ska stilen levereras?** ★ `styleguide/css/magello.css` och `styleguide/js/magello.js` kopieras oförändrade och länkas. Sidspecifika avvikelser läggs i en liten `<style>` på sidan, eller i projektets egen CSS efter `magello.css`.
17. **Vilken tillgänglighetsnivå gäller?** ★ WCAG 2.2 AA: kontrast 4,5:1, synlig fokusmarkering (2 px magenta, 2 px offset), alt-texter från mediabiblioteket, `prefers-reduced-motion` respekteras.
18. **Vilka webbläsare ska stödjas?** ★ Aktuella versioner av Chrome, Safari, Firefox, Edge. `clip-path: polygon()` och `cqw`-enheter är inga problem där.
19. **Finns det ett befintligt designsystem eller en befintlig kodbas som ska styla om?** Ja → läge B. Be om repo-åtkomst eller en körande instans.
20. **Hur snabbt kan innehållsägarna svara på frågor under arbetet?** Avgör hur mycket du får gissa. Lista antaganden i slutet av arbetet.

> Sammanfatta svaren i högst tio rader innan du börjar och låt användaren rätta. Det sparar timmar.
---

## 3. Läge A — nytt projekt från grunden

1. **Skapa katalogstruktur** enligt [Fil- och katalogstruktur](#38-fil--och-katalogstruktur). Kopiera `logos/`, `graphics/` och `images/black-and-white/`.
2. **Kopiera `styleguide/css/magello.css` och `styleguide/js/magello.js`** oförändrade och länka dem (typsnitt, tokens, reset och alla komponenter ingår). Välj typografiprofil på `<body>` ([avsnitt 9](#9-typografi--principer-och-skala)).
3. **Bygg skalet:** kopiera `<header>`, mobilmeny, sidospår och `<footer>` från en referenssida. Välj headertyp enligt fråga 9: startsida (sticky) eller undersida (`mg-page-header--rotate`). Skalet är samma på alla sidor.
4. **Skapa sidmallar** utifrån produkttypen:
   - Startsida: hero med foto och vit platta, expertis-split, erbjudandekort, case, kontakt.
   - Ingångssida: hero med kicker, rubrik, underrubrik, knappar och ingress, därefter sektioner.
   - Artikel/case/undersida: sidtitel, löpande innehåll i full bredd med infoblock efter varandra (se [Artikel](#24-artikel--undersidans-layout)).
5. **Bygg sektioner av färdiga komponenter.** Kopiera markup från referenssidorna. Behöver du något nytt, följ [Hur du skapar en ny komponent](#8-komponenttänket--varje-element-är-fristående) och lägg det som modifier på en befintlig komponent när det går.
6. **Koppla CMS** (om valt) genom att göra varje komponent datadriven enligt Strapi-kapitlet. Bygg komponenterna statiska först, flytta sedan innehållet till fält.
7. **Verifiera** enligt [Checklista för ny sida](#39-checklista-för-ny-sida) och [Snabbreferens](#40-snabbreferens--skapa-nya-element).
---

## 4. Läge B — omstyling av ett existerande projekt

Mål: samma funktion och innehåll, nytt utseende. Arbeta lager för lager så att du alltid kan jämföra före och efter.

### Steg 0 — Inventera (ändra ingenting)

1. Lista sidmallar, återkommande komponenter och globala stilar (`grep -o 'class="[^"]*"'` eller motsvarande i ramverket).
2. Ta skärmbilder av varje mall i 375, 768 och 1280 px som baslinje.
3. Notera funktioner som är känsliga: formulär, modaler, komponentbibliotek (MUI, Bootstrap, Tailwind), tredjepartswidgets som inte går att styla.
4. Fråga användaren om något som ska **behållas** oförändrat (logotyp, varumärkesfärger som avviker, juridiska texter).

### Steg 1 — Översättningstabell: gammalt → Magello

| Gammalt | Magello | Anmärkning |
|---|---|---|
| Primärfärg, länkfärg, knappfärg | `--mg-magenta` `#EC008C` | En primär accent. Byt inte ut andra varumärken utan att fråga |
| Bakgrundsgrå (`#f5f5f5` m.fl.) | `--mg-rose-50` / `--mg-rose-100` | Välj närmast i ljushet |
| Kantgrå (`#ddd`, `#e5e5e5`) | `--mg-rose-200` | Bara om en linje är funktionell (tabell, fält) |
| Rubriktypsnitt | Roboto Condensed | 500 för H1/H2, 700 för H3 och lägre |
| Brödtypsnitt | Roboto 400, 18 px / 1.6 | |
| Rundade hörn (`border-radius`) | `clip-path: polygon()` | Profilbilder runda är undantaget |
| `box-shadow` som kant eller lyft | Bakgrundsskifte eller form | Se undantag i beslutsloggen |
| `border` som avdelare | Luft, bakgrundsskifte eller form | |
| Färgfoton | `filter: grayscale(1) contrast(1.05)` | Ikoner är undantaget |
| Gradient | Platt färg | |
| Mörkt läge | Ta bort | Verktygens mörka topbar är undantaget |
| Container 960/1024/1080/1140 | `--mg-wide: 1280px` (1200 px innehåll) | Se D-47 |
| Hover med färgbyte | Hover som öppnar formen (`clip-path`) | Se [Polygonspråket](#7-polygonspråket--hur-du-skapar-nya-former) |

### Steg 2 — Fundament först

Kopiera `styleguide/css/magello.css` och `styleguide/js/magello.js` till projektet och länka dem **före** projektets egen CSS. Då finns tokens, reset, typografi och alla komponenter på plats. Välj typografiprofil på `<body>` (standard, `mg-type-editorial` eller `mg-type-showcase`). Utan detta blir allt senare arbete osäkert. Kör token-kontrollen.

**Med Tailwind (v4):** länka `magello.css` och `magello.js` som ovan och importera temat efter Tailwind:

```css
@import "tailwindcss";
@import "../design-guidelines/tokens/tailwind.css";
```

Då finns tokens som utilities: `bg-mg-rose-100`, `text-mg-magenta`, `font-head`, `p-mg-5`, `max-w-mg`, `max-w-mg-text` och brytpunkterna `tablet:`, `nav:` (över hamburgerläget) och `desktop:`. Använd ändå `.mg-wrap` som container, eftersom den har högermarginalen för sidospåret. Bygg inte om komponenterna (knappar, kort, navigation) med utilities, utan använd klasserna i `magello.css`. Temat genereras ur `tokens.json` av `tools/make_tailwind.py` när GitHub Pages bygger och ändras aldrig för hand.

### Steg 3 — Container och linjering

Gör att **allt innehåll delar vänsterkant med logotypen**: alla containers använder samma `max-width: var(--mg-wide)` och `padding-inline: var(--mg-gutter)` som navigationen. Mät med skriptet i [Linjering](#11-layout-bredd-och-linjering).

### Steg 4 — Navigation

Välj mönster från fråga 9. Header, dropdown, sidospår och mobilmeny implementeras enligt navigationskapitlena. Hamburgermeny på ≤768 px på **alla** sidor.

### Steg 5 — Komponent för komponent

Ta dem i den här ordningen. Varje steg ska vara klart och verifierat innan nästa startar:

1. Knappar → 2. Typografi i innehåll → 3. Sektioner och bakgrunder → 4. Kort → 5. Bilder → 6. Tabeller → 7. Formulär → 8. Feedback och states → 9. Footer.

För varje komponent: hitta motsvarande mönster i komponentkapitlen. Saknas det: [skapa en ny](#8-komponenttänket--varje-element-är-fristående) utifrån principerna.

### Steg 6 — Rensa kvarvarande avvikelser

Kör revisionskommandona. Varje träff ska antingen åtgärdas eller dokumenteras som undantag.

```bash
# Rundade hörn (förväntat: bara profilbilder)
grep -rn "border-radius" src/ --include="*.css" --include="*.html" --include="*.tsx" --include="*.vue"
# Skuggor (förväntat: bara dropdown-lagret)
grep -rn "box-shadow" src/ --include="*.css" --include="*.html"
# Gradienter
grep -rn "gradient" src/ --include="*.css" --include="*.html"
# Kantlinjer (förväntat: tabell, formulärfält, mobilmeny)
grep -rnE "border(-top|-bottom|-left|-right)?:\s*[0-9.]+px" src/
# Accentfärger som kant
grep -rnE "border[^;]*(EC008C|--mg-magenta|--mg-blue|--mg-red|--mg-green)" src/
# Färgfoton som saknar grayscale
grep -rn "<img" src/ | grep -v "grayscale"
# Odefinierade tokens: listar alla använda tokens, jämför med :root
grep -rhoE "var\(--mg-[a-z0-9-]+" src/ | sort -u | sed 's/var(//' > /tmp/used.txt
grep -rhoE "^\s*--mg-[a-z0-9-]+" src/ | tr -d ' ' | sort -u > /tmp/defined.txt
comm -23 /tmp/used.txt /tmp/defined.txt
```

### Steg 7 — Verifiera

- Visuellt i 375, 768, 1280 och en bred skärm (1842 px). Jämför med baslinjen.
- Tangentbord: tabb genom hela sidan, fokus synligt, dropdown nåbar.
- `prefers-reduced-motion: reduce` avstängt rörelser.
- Kontrast 4,5:1 för brödtext.
- Funktionen är intakt: formulär skickas, länkar leder rätt, inga konsolfel.

### Stoppregler

Stanna och fråga användaren om:

- ett tredjepartsbibliotek inte går att styla utan att bryta funktion,
- en befintlig komponent har ingen motsvarighet i dokumentet och ingen princip räcker för att härleda den,
- innehåll måste ändras för att formspråket ska fungera (till exempel numrerade listor som dekoration).
---

## 5. Beslutslogg — alla designbeslut i ett ögonkast

Beslut som tagits under bygget av referenssajten (styleguiden i `styleguide/`). Nya projekt ska följa dem. Kolumnen *Varför* ger underlag för att härleda liknande situationer.

### Form och färg

| # | Beslut | Varför |
|---|---|---|
| 1 | Inga linjer som avgränsare. Funktionella hårlinjer i `--mg-rose-200` tillåts i tabeller, formulärfält och mobilmenyns listor | En linje säger "här slutar något", en form säger "här börjar något" |
| 2 | Accentfärger används aldrig som kant, understrykning eller linje. Bara som fyllnad och textfärg | Accentfärger tillhör former och ikoner |
| 3 | Alla synliga former är polygoner. Ingen kant är exakt horisontell eller vertikal | Formerna ska kännas handgjorda och rörliga |
| 4 | Foton är alltid svartvita (`grayscale(1) contrast(1.05)`). Ikoner aldrig | Svartvitt låter magenta och ikonerna bära färgen |
| 5 | Knappar är femhörningar. Primär = magenta, sekundär = `--mg-rose-200` (hover `--mg-rose-300`). Outline-knappen är borttagen | Outline krävde kantlinje, som strider mot princip 1 och 2 |
| 6 | Sekundärknappens bakgrund är exakt `--mg-rose-200`, inte `#F2C4CE` | Konsekvens med palettens token |
| 7 | Inga gradienter, inga skuggor, inga rundade hörn på rektanglar, inget mörkt läge | Platt, avskalat formspråk |
| 8 | Undantag: dropdown-lagret får ha en diffus skugga, eftersom det ligger över innehåll | Annars syns det inte mot sidan |
| 9 | Undantag: verktyg och appar har en mörk rosagrå topbar `#3D2535` | Skiljer verktygsyta från innehåll, håller tonskalan |
| 10 | Personbilder är runda | Enda cirkeln i systemet |

### Layout och typografi

| # | Beslut | Varför |
|---|---|---|
| 11 | Maxbredd för innehåll och navigation är **1280 px** (`--mg-wide`), 1200 px innehåll | Ersätter 1024 px, se D-47 i `DECISIONS.md` |
| 12 | Brödtext är **18 px** (`--mg-fs-body: 1.125rem`, rad 1.6) | Tidigare 16 px. Texterna ska vara 2 px större för läsbarhet |
| 13 | **Allt innehåll delar vänsterkant med logotypen.** Alla containers använder samma bredd och gutter som navigationen | Logotypens vänsterkant är sidans fasta linje. Mätt: logotyp och brödsmula båda på 473 px vid 1842 px skärm |
| 14 | **Brödsmulan sitter på samma höjd på alla undersidor:** `--mg-header-h + --mg-space-6` från sidtopp (156 px) | Tidigare hoppade den mellan sidtyper |
| 15 | **Inga löpnummer (01, 02, 03)** på kort och listor som dekoration. Numrering bara där ordningen betyder något (processteg) | Siffrorna tillförde ingen information |
| 16 | **Inga högerställda informationsrutor.** Infoblock placeras efter varandra i full bredd, formade som rosagrå `mg-infoblock`. Ingress och text går alltid i 100 % bredd | Flytande sidorutor bröt textflödet och skapade en tvåkolumnskänsla |
| 17 | H2 på sektionsnivå är magenta, H2 inne i artikeltext svart | Sektionen markerar, flödet ska inte konkurrera |
| 18 | Tidslinjens bakgrund är `--mg-rose-50`, aldrig svart | Inga mörka ytor |
| 19 | Alla design-tokens som används måste vara definierade (`--mg-space-2` till `--mg-space-9`). `--mg-space-10` finns inte | En saknad token gör hela deklarationen ogiltig. Det orsakade 0 px padding utan felmeddelande |

### Navigation

| # | Beslut | Varför |
|---|---|---|
| 20 | Hamburgermeny på ≤768 px på **alla** sidor, helskärmsdrawer som glider in från höger. Fulla navlänkar visas bara över 768 px | Standardbeteende, samma överallt |
| 21 | Startsidans header är `position: sticky` (tröskel 8 px). Undersidors header är `position: fixed` och roterar 90° vid scroll > 80 px | Startsidan ska vara lugn. Undersidor får rörelsen |
| 22 | När headern roterat bort tar **sidospåret** över (högerställd vit pilpanel med ikonlogotyp) | Navigationen ska alltid vara nåbar |
| 23 | Dropdown (desktop) styrs bara av JS-klassen `.is-open`, inte CSS `:hover`. Ingen lucka mellan länk och meny. 220 ms stängningsfördröjning. `mouseenter`/`mouseleave` på både listpunkt och undermeny. Stängs vid scroll och klick utanför | CSS-hover stängde menyn när musen passerade luckan |
| 24 | Dropdownen är `position: fixed` och placeras av JS (`getBoundingClientRect`) | Header med `transform` bryter `position: absolute`. Annars hamnade den i 0,0 |
| 25 | **I sidospåret:** undermenyn visas vid **hover**, och ett **klick på huvudlänken expanderar** undermenyn i stället för att navigera. Chevron fungerar också | Sidospåret är kompakt. Underlänkarna är de verkliga målen |
| 26 | Headern har `pointer-events: none` när den är roterad | Den är klickbar annars och blockerar innehåll |
| 27 | Menyer och rörelse respekterar `prefers-reduced-motion` | Tillgänglighet |

### Komponenter

| # | Beslut | Varför |
|---|---|---|
| 28 | Inputfält har hel gråkant (funktionell) och accentfärgad kant vid state. Inget rundat | Tydligt att det är ett fält |
| 29 | Inline-feedback görs som fylld ruta, inte som kant till vänster | Accentfärg som kant är förbjuden |
| 30 | Pull-quote använder `citation.svg` utan opacity | Ikoner visas i full styrka |
| 31 | Sista steget i en process är alltid magenta | "Klart!" signalerar slut |
| 32 | Max en primärknapp per vy | Tydlig huvudhandling |

### Biblioteket och komponenterna (refaktorering)

| # | Beslut | Varför |
|---|---|---|
| 33 | All CSS ligger i **`styleguide/css/magello.css`** och all JS i **`styleguide/js/magello.js`**. Sidorna innehåller bara markup och högst ett tiotal rader sidspecifik CSS | Tidigare dubblerades ca 20 kB CSS och 4 kB JS i varje sida. En annan session kan nu kopiera filerna rakt av och få exakt samma utseende |
| 34 | Tre **typografiprofiler** via klass på `<body>`: standard (landningssidor), `mg-type-editorial` (artiklar, case, text), `mg-type-showcase` (startsida, komponentsidor) | Sidorna hade tyst olika typskalor (`--mg-fs-h2`, `-h3`, radhöjd). Nu är skillnaderna namngivna och dokumenterade |
| 35 | Headern har en bas (sticky, startsida) och modifiern **`mg-page-header--rotate`** (fixed + rotation, undersidor) | Skillnaden fanns som olika regler för samma klass på olika sidor |
| 36 | **Ett kort, `.mg-card`**, med modifiers `--text`, `--image`, `--compact`, och rutnät `.mg-card-grid` (`--loose`, `--three`). Ersätter `mg-expertis-card`, `mg-offering-block` och `mg-cards` | Tre klasser hade identisk form och yta |
| 37 | Kort har **ingen `box-shadow`-ring** | Ringen klipptes av `clip-path` och syntes bara som svaga streck vid hörnen |
| 38 | **En knappdefinition** (`.mg-btn`, `--primary`, `--secondary`) och modifiern `--icon` för knappar med ikon. Den gamla klassen `mg-btn-primary` är borttagen | Två knappar med olika polygon, versaler och padding fanns parallellt |
| 39 | **Brödsmulans avstånd sätts av containern** (`.mg-ingang-col .mg-breadcrumb`, `.mg-page-title .mg-breadcrumb`), inte av brödsmulan själv | Samma komponent hade fyra olika marginaler beroende på sida |
| 40 | Citat använder **`citation.svg`** överallt, också på artikelsidan | Artikelsidan hade ett textcitattecken i magenta |
| 41 | Bakgrundsbilder görs som **`<img>` med `object-fit: cover`**, inte som `background-image` från en CSS-variabel | CSS-variabler med relativa URL:er bryts när CSS-filen ligger i `css/`. `<img>` ger även alt-text |
| 42 | Namnkrockar löstes med egna namn: startsidans case-kort heter **`.mg-case-tile`**, casesidans **`.mg-case-teaser`**, formulärets fältetikett **`.mg-field__label`** | Samma klassnamn betydde olika komponenter på olika sidor |
| 43 | Odefinierade tokens fick standardvärden i `:root` | Ingångssidans underrubrik och mobilmenyns avstånd föll tyst tillbaka eftersom `--mg-fs-subtitle` och `--mg-space-9` saknades på vissa sidor |
| 44 | `.mg-prose` täcker Markdown-element (listor, citat, tabeller, kod, `---`) | Texter från Strapi skrivs i Markdown. Se avsnitt 36 och `styleguide/markdown.html` |
| 45 | Headerpolygonens hack följer `--mg-wide` (inte hårdkodat 1080 px) | Hacket ska hamna vid logotypens vänsterkant |
| 46 | Oanvänd CSS togs bort (`mg-expertis-card__num`, `mg-stats`, `mg-intro*`, `mg-step--active`) | Död kod i ett bibliotek vilseleder |
---

## 6. Designfilosofi

Magello-designen har ett tydligt visuellt språk: **organiska polygoner, en mjuk rosagrå palett och typografisk tydlighet**. Det är inte en estetik där man väljer delar. Det är ett system där alla delar förstärker varandra. Förstå *varför* reglerna finns, så kan du applicera dem på element som inte finns i dokumentet ännu.

Samma principer, formulerade för alla medier, finns i `design-language.md`. Läs dem först. Det här avsnittet är deras webbversion.

### Känsla och syfte

- **Syfte:** presentera hur Magello kan hjälpa kunder lösa sina egentliga problem, trovärdigt men personligt och lekfullt.
- **Målgrupp:** chefer, rekryterare, beställande IT-personer.
- **Känsla:** professionell, avskalad, tydlig, typografisk.
- **Referenser:** volvocars.com/se, tesla.com: luft, stor typografi, få element.

### De sju grundprinciperna

**1. Inga linjer som avgränsare.**
Struktur skapas av luft, bakgrundsskiften och polygonformer. Funktionella hårlinjer i `--mg-rose-200` får finnas i tabeller, formulärfält och mobilmenyns listor, aldrig som dekoration.

> ✗ `border-bottom: 1px solid #E3D6D6` under en rubrik
> ✓ Nästa sektions bakgrundsfärg skapar uppdelningen

**2. Accentfärger är fyllnad, aldrig kant.**
Magenta, blå, orange, grön, röd och gul tillhör former, text och ikoner. Aldrig `border`, `outline` som dekor eller streck.

> ✗ `border-left: 3px solid var(--mg-magenta)`
> ✓ `background: var(--mg-magenta)` som badge, knapp eller etikett

**3. Polygoner ger rörelse.**
Ingen synlig kant är exakt horisontell eller vertikal. Hörnen avviker 2–7 % från ett perfekt rätblock. Se [Polygonspråket](#7-polygonspråket--hur-du-skapar-nya-former).

**4. Allt är svartvitt utom varumärket.**
Foton renderas alltid i svartvitt. Ikoner är undantaget: de visas i full färg.

**5. Rosagrått är kärnan, magenta används sparsamt.**
Sidan ska i huvudsak vara svart, vit och rosagrå. Magenta för H2, logotyp, primär handling och enstaka ord.

**6. Signaturen: den rosagrå ytan med lutande kant.**
Headern är en rosagrå polygon som drar sig nedåt åt ena hållet. Den är det mest igenkännbara elementet och används på landningsytor.

**7. Luft och gemensam linje.**
Generöst ovanför rubriker, tätare under. Allt innehåll delar vänsterkant med logotypen.

### Komponenter, inte stilar

Varje visuellt element (kort, citat, steg, tidslinje, faktaruta) är en självständig komponent med eget CSS-scope. Du ska kunna flytta vilken komponent som helst till en annan sida utan att bryta designen. Undvik att styla direkt på HTML-taggar (`p`, `h2`, `div`) utanför ett definierat scope som `.mg-prose`.

### Att härleda en ny lösning

Saknar du ett mönster, fråga dig i den här ordningen:

1. Bryter lösningen mot någon av de sju principerna? Då är den fel.
2. Finns en liknande komponent? Återanvänd dess form, färg och rörelse.
3. Vilken bakgrund (`white`, `rose-50`, `rose-100`, `rose-200`)?
4. Vilken polygon, och hur ser den ut på hover?
5. Vilken typografi (Condensed signalerar, Roboto berättar)?
6. Räcker luft och bakgrundsskifte, eller behövs verkligen en kant? (Oftast räcker det.)
7. Fungerar det i 375 px och 1842 px?

---

## 7. Polygonspråket — hur du skapar nya former

Magello har ett konsekvent sätt att rita polygoner. När du skapar ett nytt element ska du följa dessa regler.

### Grundregel: inga exakta 0/100-hörn

Raka hörn (0% 0%) syns som skarpa, industriella kanter. Magello-polygoner avviker alltid lite:

```
Undvika: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)  ← perfekt rektangel
Använd:  polygon(0% 2%, 98% 0%, 100% 97%, 2% 100%)    ← levande form
```

### Avvikelsemått per hörn-typ

| Hörn | Avvikelse på X | Avvikelse på Y | Exempel |
|---|---|---|---|
| Övre vänster | 0–3% | 2–5% | `0% 3%` eller `2% 0%` |
| Övre höger | 96–100% | 0–3% | `98% 0%` eller `100% 2%` |
| Nedre höger | 96–100% | 95–100% | `97% 100%` eller `100% 96%` |
| Nedre vänster | 0–4% | 95–100% | `0% 97%` eller `3% 100%` |

### Formdramatik: extra punkter ger "vikt"

Lägg till en extra punkt för att ge formen rörelse eller riktning. Headerns polygon har en extra punkt som gör att höger sida drar sig upp:

```css
/* 5-punkts header-polygon — extra nedre punkt skapar riktning */
clip-path: polygon(
  0% 0%,
  100% 0%,
  100% 55%,              /* höger sida slutar på 55% */
  20px 100%,             /* extra punkt nere till vänster */
  0% 82%                 /* vänster sida slutar på 82% */
);
```

### Pil/chevron-former

Sidospåret och processstegen är pilformer. Principen: en sida har en spets (50% Y på X-kanten).

```css
/* Sidospår — pil pekar åt vänster */
clip-path: polygon(16% 0%, 100% 0%, 100% 100%, 16% 100%, 0% 50%);

/* Processsteg — pil pekar åt höger, inre spets åt vänster */
clip-path: polygon(
  1% 4%,
  calc(100% - 16px) 1%,
  100% 50%,              /* höger spets */
  calc(100% - 16px) 96%,
  2% 100%,
  14px 50%               /* vänster inre spets */
);
```

### Skalning: mer dramatik på stora element

- **Liten komponent** (badge, swatch): avvikelse 2–4%
- **Medelstor komponent** (kort, knapp, infoblock): avvikelse 2–6%
- **Stor form** (sektion, hero-platta): avvikelse 3–8%, fler punkter

### Hover-animation: formen öppnas upp

När en polygon-form hovras ska den **bli mer rektangulär** — inte försvinna eller byta färg dramatiskt. Det ger känslan av att formen "slappnar av":

```css
/* Vila-state: lite oregelbunden */
clip-path: polygon(2% 5%, 99% 0%, 100% 88%, 97% 100%, 0% 95%);

/* Hover-state: mer öppen, mer rak */
clip-path: polygon(0% 2%, 100% 0%, 99% 93%, 96% 100%, 1% 98%);
```

---

## 8. Komponenttänket — varje element är fristående

### Namnkonvention: BEM-inspirerad med `mg-`-prefix

Alla klasser börjar med `mg-` (Magello) och följer ett block–element-mönster:

```
.mg-[block]                  ← hela komponenten
.mg-[block]__[element]       ← del av komponenten
.mg-[block]--[modifier]      ← variant av komponenten
```

Exempel: `.mg-card`, `.mg-card__body`, `.mg-card--featured`

### Varje komponent äger sin egna CSS

Styla aldrig på nakna HTML-taggar utanför ett definierat scope. Enda undantaget är `.mg-prose` som är ett dedikerat scope för redaktionell löptext.

```css
/* ✗ Undvik: globalt stilat h2 */
h2 { color: var(--mg-magenta); }

/* ✓ Rätt: scoped till blocket */
.mg-section-head h2 { color: var(--mg-magenta); }
.mg-prose h2 { color: var(--mg-black); }
```

### Komponenters relativa storlek

Komponenter ska fungera oavsett omgivning. Använd `%`, `em` och `rem` — inte `px` för storlekar som ska skala med sammanhanget.

### Hur du skapar en ny komponent

Fråga dig:
1. **Vad är blocket?** — ge det ett `mg-`-namn
2. **Vilken bakgrundsfärg?** — välj bland `white`, `rose-50`, `rose-100`, `rose-200`
3. **Ska det ha polygon-kanter?** — ja om det är en synlig "låda"
4. **Hur mår det på hover?** — polygon öppnas + ev. bakgrundsskifte
5. **Vad är typografin?** — se typografi-matrisen i sektion 4

### Exempel: ny "Citat-person"-komponent

```css
/* Nytt block */
.mg-person-quote {
  display: flex;
  gap: var(--mg-space-5);
  padding: var(--mg-space-6);
  background: var(--mg-rose-50);
  clip-path: polygon(0% 0%, 100% 2%, 98% 98%, 0% 100%); /* ← polygon, ej rektangel */
}

/* Element: avatar */
.mg-person-quote__avatar {
  width: 64px; height: 64px;
  flex-shrink: 0;
  filter: grayscale(1);           /* ← svartvitt */
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); /* hexagon */
}

/* Element: text */
.mg-person-quote__text {
  font: 400 1rem/1.6 var(--mg-font-body);
  color: var(--mg-text-2);
}

/* Element: namn */
.mg-person-quote__name {
  font: 700 .75rem/1 var(--mg-font-head);
  letter-spacing: .1em; text-transform: uppercase;
  color: var(--mg-magenta);
  margin-top: var(--mg-space-3);
}
```

Det ser omedelbart ut som Magello — utan att man kopierat en befintlig komponent — för att det följer polygonspråket, färgvalen och typografi-matrisen.

---

## 9. Typografi — principer och skala

### Hur typografin tänker

Magello-typografin bygger på **en enkel regel: Condensed för allt synligt, Roboto för allt läsbart**.

- **Roboto Condensed** (smal, tydlig, lite formell) — rubriker, knappar, etiketter, nav. Allt som *signalerar* något. Används med varierande vikt: 400 för subtitles, 500 för sektionsrubriker, 700 för kickers och starka rubriker.
- **Roboto** (normal bredd, bekväm) — brödtext, faktarutor, footer, tabeller. Allt som *berättar* något.

**Blanda aldrig tvärtom.** Roboto på en knapp eller Condensed på löptext bryter tonen direkt.

### Storlekshierarki

| Nivå | Sammanhang | Storlek | Vikt |
|---|---|---|---|
| **Display / DocTitle** | Öppning av en undersida | `clamp(3.2rem, 2rem + 5vw, 6.5rem)` | 700 |
| **H1 hero** | Startsidans hero | `clamp(2.25rem, 1.5rem + 3.2vw, 3.5rem)` | 500 |
| **H2 sektion** | Rubriker inuti sektioner | `clamp(1.5rem, 1.35rem + .6vw, 1.8rem)` | 500 |
| **H2 artikel** | Rubriker i löptext | `clamp(1.4rem, 1.25rem + .7vw, 1.9rem)` | 700 |
| **H3** | Underrubriker | `clamp(1.15rem, 1.1rem + .3vw, 1.35rem)` | 700 |

Alla rubrikstorlekar är Roboto Condensed.

**Brödtext är 18 px** (`--mg-fs-body: 1.125rem`, radhöjd 1.6). Den var tidigare 16 px och höjdes 2 px för läsbarhet. Texter i kort och komponenter är något mindre (15 px / .9375rem) men aldrig under 12 px.

**Sektionsrubriker (H2) är alltid magenta** — signalerar "ny idé börjar här".
**Artikelrubriker (H2 i `.mg-prose`) är svarta** — de är i flödet och ska inte konkurrera med sektionen.

### Subtitle-regelns fyra parametrar

En Subtitle används direkt under DocTitle eller H1 som ett lugnande komplement. Den är alltid:
- `22pt` storlek (inte rem — det är ett medvetet val för att matcha tryckfilen)
- `line-height: 2.2` (ovanligt hög — ger luft och läsbarhet)
- `color: var(--mg-text-2)` (#4C4A4A) — varken svart eller grå
- `letter-spacing: 0.02em`

### Etiketter och kickers

Etiketter (`.mg-kicker`, `.mg-label`) är alltid:
- Condensed 700
- ~0.69rem
- `letter-spacing: .12–.14em`
- `text-transform: uppercase`
- Magenta

De identifierar kategorin/sammanhanget, inte innehållet. Placera alltid en etikett *ovanför* rubriken den tillhör.

### Nya typografiska element — hur du tänker

När du behöver ett nytt typografiskt element:

| Fråga | Svar → stil |
|---|---|
| Är det en etikett/kategori? | Kicker-stil: Condensed 700, small-caps, magenta |
| Är det en rubrik? | Condensed, vikt 500 (mjuk) eller 700 (stark) |
| Är det löptext? | Roboto 400, `color: var(--mg-text-2)`, line-height 1.5–1.7 |
| Är det ett faktablock/siffra? | Condensed 700, stor storlek, `color: var(--mg-grey-300)` |
| Är det en länk i text? | `color: var(--mg-magenta)`, underline |
| Är det nav/knapptext? | Condensed 400–500, ingen underline, hover → magenta |

### Google Fonts-import

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&family=Roboto+Condensed:wght@400;500;700&display=swap" rel="stylesheet">
```

### Font-tokens

```css
--mg-font-body: "Roboto", system-ui, Arial, sans-serif;
--mg-font-head: "Roboto Condensed", "Arial Narrow", Arial, sans-serif;
```

- **`var(--mg-font-head)`** — Roboto Condensed. Används för alla rubriker, knappar, kickers, nav-länkar, featured-länk.
- **`var(--mg-font-body)`** — Roboto. Används för brödtext, faktarutor, footer.

### Typografisk skala

| Roll | CSS | Font | Vikt | Storlek |
|---|---|---|---|---|
| DocTitle / H1 stor | `.mg-doc-title` | Condensed | 700 | `clamp(3.2rem, 2rem + 5vw, 6.5rem)` |
| H1 (startsida/hero) | `.mg-hero__title` | Condensed | 500 | `clamp(2.25rem, 1.5rem + 3.2vw, 3.5rem)` |
| Subtitle (undersida) | `.mg-doc-sub` | Condensed | 400 | 22pt |
| H2 (sektioner) | `h2` i `.mg-section-head` | Condensed | 500 | `clamp(1.5rem, 1.35rem + .6vw, 1.8rem)` |
| H3 | | Condensed | 700 | `clamp(1.15rem, 1.1rem + .25vw, 1.35rem)` (standard), se profiler |
| H4 | | Condensed | 700 | `clamp(1.19rem, 1.1rem + .35vw, 1.4rem)` |
| Kicker (etikett) | `.mg-kicker` | Condensed | 700 | 0.6875rem, uppercase, letter-spacing .14em |
| Brödtext | `body` | Roboto | 400 | 1.125rem (18 px) / 1.6 |
| Nav-länk | `.mg-nav__links a` | Roboto | 400 | .875rem |
| Featured nav | `.mg-nav__featured` | Condensed | 500 | .875rem |

### Typografiprofiler

Typskalan (`--mg-fs-h1`, `-h2`, `-h3`, `-subtitle` och `--mg-lh-body`) finns i **tre profiler** i `magello.css`. Profilen väljs med en klass på `<body>`. Alla andra storlekar är gemensamma.

| Profil | Klass på `<body>` | Används på | H1 | H2 | H3 | Underrubrik | Radhöjd brödtext |
|---|---|---|---|---|---|---|---|
| **Standard** (landning) | ingen | Ingångssidor (`digitala-tjanster.html`) | `2.25–3.5rem` | `1.5–1.8rem` | `1.15–1.35rem` | `1.1–1.35rem` | 1.6 |
| **Editorial** | `mg-type-editorial` | Artiklar, case, om oss, textsidor | `2–3.2rem` | `1.4–1.9rem` | `1.15–1.35rem` | standard | 1.7 |
| **Showcase** | `mg-type-showcase` | Startsida, komponentsida | standard | standard | `1.3–1.6rem` | `1.3–1.75rem` | 1.5 |

Regler:

- Välj profil efter sidtyp, aldrig per element. Blanda inte profiler på en sida.
- **Ändra aldrig tokenvärden på en enskild sida.** Behövs en ny skala, lägg till en profil i `magello.css`.
- Alla tokens som komponenter använder ska finnas i `:root`. En saknad token (till exempel `--mg-fs-subtitle`) gör att hela `font`-deklarationen tyst ogiltigförklaras.

### Subtitle-specifikation (undersidor)

```css
.mg-doc-sub {
  font: 400 22pt/2.2 var(--mg-font-head);
  color: var(--mg-text-2);           /* #4C4A4A */
  letter-spacing: 0.02em;
  margin-top: 34px;
  margin-bottom: 24px;
}
```

### H2 i sektioner är alltid magenta

```css
.mg-section-head h2 {
  font: 500 var(--mg-fs-h2)/1.15 var(--mg-font-head);
  color: var(--mg-magenta);
}
```
---

## 10. Färgpalett & tokens

```css
:root {
  /* Neutraler */
  --mg-black:    #000000;
  --mg-white:    #FFFFFF;
  --mg-text-2:   #4C4A4A;   /* sekundär text — rubriker i löptext, subtitles */
  --mg-rose-50:  #F7F3F3;   /* ljusaste bakgrund, alternativa rader i tabell */
  --mg-rose-100: #F4EBEB;   /* header-bakgrund, mobilmeny, sektionsbakgrund */
  --mg-rose-200: #E3D6D6;   /* dividers, kort-outline, sekundärknapp */
  --mg-rose-300: #DED4D4;   /* table-footer border */
  --mg-grey-300: #BFBFBF;   /* labels, år i tidslinje, breadcrumb */

  /* Primär accent */
  --mg-magenta:  #EC008C;   /* ★ Primär — logga, knappar, aktiva states, H2 */

  /* Sekundära accenter — ikoner och illustrationer, ALDRIG som linjer */
  --mg-blue:     #31ABE2;
  --mg-orange:   #F9B804;
  --mg-red:      #E3012F;
  --mg-yellow:   #FFDC00;
  --mg-green:    #1BA660;
}
```

**Regel:** Accentfärger (magenta, blå, orange, röd, gul, grön) används **aldrig** som raka streck, kanter eller dividers. De finns bara på:
- Text (magenta: rubriker, kicker, links, aktiva nav-val)
- Fyllnader på ikoner och illustrationer
- Bakgrunder på knappar och processteg
- Diamant/hexagon-badge i sidospalt

Den fullständiga token-listan (inklusive typskala, avstånd och layout) finns i [Layout, bredd och linjering](#11-layout-bredd-och-linjering). **Använd bara tokens som finns där.**

---

## 11. Layout, bredd och linjering

### Samlade tokens

Tokens definieras en gång, i `:root` i `styleguide/css/magello.css`. Blocket nedan är en utskrift av filen. **Alla tokens som används i komponenter måste finnas här.** En `var()` som pekar på en odefinierad token ogiltigförklarar hela deklarationen utan felmeddelande (så uppstod 0 px padding på ingångssidorna när `--mg-space-10` användes, och så föll ingångssidans underrubrik tillbaka till brödtypsnitt eftersom `--mg-fs-subtitle` saknades).

```css
:root {
  /* Neutraler */
  --mg-black: #000000;
  --mg-white: #FFFFFF;
  --mg-text-2: #4C4A4A;
  --mg-rose-50: #F7F3F3;
  --mg-rose-100: #F4EBEB;
  --mg-rose-200: #E3D6D6;
  --mg-rose-300: #DED4D4;
  --mg-grey-300: #BFBFBF;
  /* Accenter */
  --mg-magenta: #EC008C;
  --mg-blue: #31ABE2;
  --mg-orange: #F9B804;
  --mg-red: #E3012F;
  --mg-yellow: #FFDC00;
  --mg-green: #1BA660;
  /* Typsnitt */
  --mg-font-body: "Roboto", system-ui, Arial, sans-serif;
  --mg-font-head: "Roboto Condensed", "Arial Narrow", Arial, sans-serif;
  --mg-font-code: Consolas, ui-monospace, "Cascadia Mono", Menlo, monospace;
  /* Typskala */
  --mg-fs-h1: clamp(2.25rem, 1.5rem + 3.2vw, 3.5rem);
  --mg-fs-subtitle: clamp(1.1rem, 1rem + 0.5vw, 1.35rem);
  --mg-fs-h2: clamp(1.5rem, 1.35rem + .6vw, 1.8rem);
  --mg-fs-h3: clamp(1.15rem, 1.1rem + .25vw, 1.35rem);
  --mg-fs-body: 1.125rem;
  --mg-lh-body: 1.6;
  --mg-fs-display: clamp(2.8rem, 2rem + 4vw, 5rem);
  --mg-fs-small: .875rem;
  --mg-lh-tight: 1.1;
  --mg-fs-h4: clamp(1.19rem, 1.1rem + .35vw, 1.4rem);
  /* Avstånd */
  --mg-space-2: 8px;
  --mg-space-3: 12px;
  --mg-space-4: 16px;
  --mg-space-5: 24px;
  --mg-space-6: 36px;
  --mg-space-7: 48px;
  --mg-space-8: 64px;
  --mg-space-9: 96px;
  /* Layout */
  --mg-gutter: 20px;
  --mg-gutter-end: var(--mg-gutter);
  --mg-wide: 1280px;
  --mg-side-w: 192px;
  --mg-nav-h: 72px;
  --mg-nav-h-compact: 56px;
  --mg-hext: 48px;
  --mg-header-h: calc(var(--mg-nav-h) + var(--mg-hext));
  --mg-text-w: 680px;
}

@media (min-width: 600px) {
  :root { --mg-gutter: 40px; }
}
@media (min-width: 769px) {
  body:has(.mg-side-nav) {
    --mg-gutter-end: max(var(--mg-gutter),
      calc(var(--mg-side-w) + var(--mg-space-5) - max(0px, (100vw - var(--mg-wide)) / 2)));
  }
}

/* Typografiprofiler (klass på <body>) */
.mg-type-editorial {
  --mg-fs-h1: clamp(2rem, 1.5rem + 2.5vw, 3.2rem);
  --mg-fs-h2: clamp(1.4rem, 1.25rem + .7vw, 1.9rem);
  --mg-fs-h3: clamp(1.15rem, 1.1rem + .3vw, 1.35rem);
  --mg-lh-body: 1.7;
}
.mg-type-showcase {
  --mg-fs-subtitle: clamp(1.3rem, 1.1rem + 1vw, 1.75rem);
  --mg-fs-h3: clamp(1.3rem, 1.2rem + .5vw, 1.6rem);
  --mg-lh-body: 1.5;
}
```

### Reset och bas

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--mg-white);
  color: var(--mg-black);
  font: 400 var(--mg-fs-body)/var(--mg-lh-body) var(--mg-font-body);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
a { color: inherit; text-decoration: underline; text-underline-offset: 2px; }
a:hover { color: var(--mg-magenta); }
a:focus-visible { outline: 2px solid var(--mg-magenta); outline-offset: 2px; }
img { max-width: 100%; display: block; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```

### Wrapper — den enda containern

```css
.mg-wrap {
  max-width: var(--mg-wide);        /* 1280 px = 1200 px innehåll */
  margin-inline: auto;
  padding-inline: var(--mg-gutter) var(--mg-gutter-end); /* 20 / 40 px */
}
```

Navigationens `.mg-nav__inner` använder samma bredd och samma vänstermarginal. Det är därför logotypen och innehållet hamnar på samma vänsterkant.

**Plats för sidospåret.** På sidor med sidospår (över 768 px) växer högermarginalen `--mg-gutter-end` så att innehållet alltid håller `--mg-space-5` (24 px) avstånd till spåret. Vänsterkanten flyttas inte, innehållet blir bara smalare på höger sida i de bredder där spåret annars skulle ligga över texten (ungefär 769 till 1630 px). Containrar ska därför alltid skriva `padding-inline: var(--mg-gutter) var(--mg-gutter-end)`, aldrig bara `var(--mg-gutter)`.

### Linjering — regeln

> **Allt innehåll delar vänsterkant med logotypen.** Det gäller brödsmula, kicker, rubrik, brödtext, bildplatta, kort och sektionsrubriker.

Så gör du:

- Alla innehållscontainrar är `.mg-wrap` eller har samma `max-width: var(--mg-wide)` och `padding-inline: var(--mg-gutter) var(--mg-gutter-end)`.
- Container med egen bakgrund (till exempel `.mg-ingang-col`, vit platta ovanpå ett hero-foto) skriver `width: min(var(--mg-wide), 100%)`, `margin-inline: auto`, `padding-inline: var(--mg-gutter) var(--mg-gutter-end)`.
- Använd **aldrig** egna `max-width` som 960 eller 1080 för en container som ska linjera med logotypen. Det var orsaken till en förskjutning på 32 px.
- Använd inte `clamp()` med egna värden för sidopadding. Använd `--mg-gutter`.

**Mät, gissa inte.** Klistra in i webbläsarens konsol på en skärm bredare än 1100 px:

```js
const left = s => Math.round(document.querySelector(s).getBoundingClientRect().left);
console.table({
  logo:       left('.mg-nav__logo'),
  breadcrumb: left('.mg-breadcrumb'),
  rubrik:     left('h1'),
});
// Alla tre ska ha samma värde (473 px vid 1842 px bredd).
```

Fungerar bara när headern inte är roterad (scrollY < 80). En roterad header ger koordinater i det transformerade rummet.

### Höjd på brödsmulan

Alla undersidor har brödsmulan på exakt samma avstånd från sidtopp: **`--mg-header-h + --mg-space-6`** (120 + 36 = 156 px).

| Sidtyp | Så uppnås 156 px |
|---|---|
| Sidtitel (`.mg-page-title`) | `padding-top: calc(var(--mg-header-h) + var(--mg-space-6))` |
| Ingångssida (`.mg-ingang-hero` → `.mg-ingang-col`) | Hero `padding-top: var(--mg-header-h)`, kolumn `padding-top: var(--mg-space-6)` |

Fixed header tar ingen plats i flödet, därför måste innehållet själv kompensera. Sidan får aldrig starta under headern (brödsmulan hamnar då delvis skymd).

```js
// Kontrollera: ska skriva ut 156 på alla undersidor
Math.round(document.querySelector('.mg-breadcrumb').getBoundingClientRect().top + scrollY)
```

### Brytpunkter

| Brytpunkt | Beteende |
|---|---|
| `max-width: 599px` | En kolumn, gutter 20 px, footer staplad |
| `≥ 600 px` | Gutter 40 px, container max 1280 px (1200 px innehåll) |
| `> 768 px` med sidospår | Högermarginalen `--mg-gutter-end` växer så att innehållet inte hamnar under sidospåret |
| `max-width: 768px` | Hamburgermeny ersätter navlänkar. Headern ligger kvar efter scroll och blir lägre (56 px) i stället för att rotera. Sidospåret döljs |
| `max-width: 900px` | Tvåkolumnslayouter (till exempel kort) faller till en kolumn |

### Avstånd i innehåll

| Element | Före | Efter |
|---|---|---|
| Sidtitel (H1) | `--mg-space-3` | `--mg-space-3` |
| H2 sektion | `--mg-space-3` (efter label) | `--mg-space-7` (till innehållet) |
| H2 artikel | `--mg-space-8` | `--mg-space-4` |
| Stycke | 0 | `--mg-space-5` |
| Sektion | `--mg-space-8`–`9` (padding-block) | |

**Tumregel:** avståndet ovanför en rubrik är alltid tydligt större än under den.
---

## 12. Header — startsida

På startsidan (index.html) är headern `position: sticky`. Den har en rosagrå signaturpolygon som kollapsar när användaren scrollar.

### CSS

```css
.mg-page-header {
  position: sticky;
  top: 0;
  z-index: 100;
  padding-bottom: var(--mg-hext);    /* 48px extra höjd för polygonen */
  background: transparent;
  transition: padding-bottom 0.4s ease;
}
.mg-page-header.is-scrolled {
  padding-bottom: 0;
}

/* Rosagrå polygonform — 5 punkter */
.mg-header-shape {
  position: absolute;
  inset: 0;
  background: var(--mg-rose-100);
  clip-path: polygon(
    0% 0%,
    100% 0%,
    100% 55%,
    calc(max(0px, (100% - var(--mg-wide)) / 2) + var(--mg-gutter)) 100%,
    0% 82%
  );
  transition: clip-path 0.4s ease;
}

/* Kollapsar till rektangel vid scroll */
.mg-page-header.is-scrolled .mg-header-shape {
  clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 100%);
}
```

### Nav-innehåll

```css
.mg-nav {
  position: relative;
  z-index: 2;
  height: 72px;
  display: flex;
  align-items: center;
}
.mg-nav__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--mg-space-5);
  width: 100%;
  max-width: var(--mg-wide);
  margin-inline: auto;
  padding-inline: var(--mg-gutter);
}

/* Logotyp */
.mg-nav__logo svg { height: 38px; width: auto; }

/* Navlänkar */
.mg-nav__links { display: flex; gap: var(--mg-space-6); list-style: none; }
.mg-nav__links a {
  font: 400 .875rem/1 var(--mg-font-body);
  text-decoration: none;
  color: var(--mg-black);
  letter-spacing: .01em;
}
.mg-nav__links a:hover { color: var(--mg-magenta); }
.mg-nav__links a.is-active { color: var(--mg-magenta); font-weight: 500; }

/* Featured-länk (t.ex. "Lediga jobb") — magenta med skev understrykningslinje */
.mg-nav__featured {
  font: 500 .875rem/1 var(--mg-font-head);
  color: var(--mg-magenta);
  text-decoration: none;
  letter-spacing: .03em;
  white-space: nowrap;
  position: relative;
  padding-bottom: 3px;
  transition: opacity .2s;
}
.mg-nav__featured::after {
  content: '';
  position: absolute;
  bottom: -1px; left: 0; right: 0;
  height: 2px;
  background: var(--mg-magenta);
  clip-path: polygon(0% 0%, 100% 30%, 97% 100%, 0% 70%); /* skev underline */
}
.mg-nav__featured:hover { opacity: .65; color: var(--mg-magenta); }
```

### JavaScript

Header-beteendet ligger i `styleguide/js/magello.js` (kopiera filen, skriv inte om den). Startsidans header (`.mg-page-header`, sticky) toggler klassen `is-scrolled` efter 8 px scroll. Undersidors header (`.mg-page-header--rotate`) gör det efter 80 px.

### Hero-sektion (startsida)

Hero-sektionen dras upp under headern med negativ `margin-top`:

```css
.mg-hero {
  position: relative;
  min-height: calc(560px + var(--mg-header-h));
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: calc(-1 * var(--mg-header-h)); /* överlapp med sticky header */
}
.mg-hero__bg {
  position: absolute; inset: 0;
  background-image: url('/images/black-and-white/kontor-1.jpg');
  background-size: cover;
  background-position: center 30%;
  filter: grayscale(1) contrast(1.05);
}
.mg-hero__wrap {
  position: relative; z-index: 2;
  width: 100%;
  padding-top: calc(var(--mg-header-h) + var(--mg-space-8));
  padding-bottom: var(--mg-space-8);
}

/* Vit polygonplatta på hero-texten — 8 hörn */
.mg-hero__plate {
  background: var(--mg-white);
  padding: var(--mg-space-7);
  max-width: 540px;
  clip-path: polygon(
    0% 3%, 4% 0%, 97% 2%, 100% 6%,
    98% 94%, 94% 100%, 2% 97%, 0% 93%
  );
}
```
---

## 13. Header — undersidor (rotation + sidospår)

På **undersidor** (om-oss.html, digitala-tjanster.html m.fl.) är headern `position: fixed`. När användaren scrollar ner 80px:

1. **Headern roteras 90° medsols** med `transform-origin: right top` — vänstra hörnet faller nedåt och headern glider ut ur bild längs högerkanten.
2. **Sidospåret (`.mg-side-nav`)** glider in från höger med vit polygonbakgrund och innehåller ikon-logotypen + navlänkar.

### CSS — header (fixed + rotation)

Headern har en bas (sticky, startsidan) och en modifier för undersidor. Markup: `<div class="mg-page-header mg-page-header--rotate">`.

```css
.mg-page-header {
  position: sticky; top: 0; z-index: 100;
  padding-bottom: var(--mg-hext);
  background: transparent;
  transition: padding-bottom 0.4s ease;
}
.mg-page-header.is-scrolled { padding-bottom: 0; }

/* Undersidor: fast header som roterar bort och lämnar plats åt sidospåret */
.mg-page-header--rotate {
  position: fixed; left: 0; right: 0;
  transform-origin: right top;   /* NYCKEL: roterar från höger övre hörn */
  transition: padding-bottom 0.4s ease,
              transform 0.6s cubic-bezier(0.4, 0, 0.6, 1);
}
.mg-page-header--rotate.is-scrolled {
  transform: rotate(90deg);      /* höger sida blir botten, headern glider bort */
  pointer-events: none;          /* klickbar när dold */
}
```

**Viktigt:** `transform-origin: right top` gör att det vänstra hörnet roterar nedåt. Utan detta roterar headern från mitten.

### CSS — sidospår (.mg-side-nav)

```css
.mg-side-nav {
  position: fixed;
  right: 0; top: 0; bottom: 0;
  width: 192px;
  z-index: 200;
  background: var(--mg-white);
  /* Pil-form som pekar åt vänster — polygonens vänstersida pekar inåt */
  clip-path: polygon(16% 0%, 100% 0%, 100% 100%, 16% 100%, 0% 50%);
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  padding: var(--mg-space-5) var(--mg-space-6) var(--mg-space-5) var(--mg-space-9);
  /* Dold state */
  transform: translateX(100%);
  opacity: 0;
  /* Fördröjning: vänta på att headern börjat röra sig */
  transition: transform 0.42s cubic-bezier(0, 0, 0.2, 1) 0.18s,
              opacity 0.28s ease 0.18s;
  pointer-events: none;
}
.mg-side-nav.is-visible {
  transform: translateX(0);
  opacity: 1;
  pointer-events: auto;
}
```

**Animationstiming:** Headern roterar i 0.6s. Sidospåret väntar 180ms (delay) och glider sedan in på 420ms — skapar känslan av ett sammanhängande rörelse.

### CSS — sidospårets innehåll

```css
/* Ikon-logotyp (icon-logotype.svg) — ca 70px bred, längst upp */
.mg-side-nav__logo {
  display: flex; align-items: center; justify-content: flex-end;
  text-decoration: none;
  margin-bottom: var(--mg-space-6);
  flex-shrink: 0;
}
.mg-side-nav__logo img { width: 70px; height: auto; display: block; }

/* Navlänkar — alltid horisontella (ej roterade) */
.mg-side-nav__links {
  list-style: none;
  display: flex; flex-direction: column;
  align-items: flex-end;
  flex: 1; justify-content: center;
  gap: 0;
}
.mg-side-nav__links a {
  font: 400 .8rem/1 var(--mg-font-body);
  text-decoration: none; color: var(--mg-black);
  letter-spacing: .01em; padding: 10px 0;
  transition: color .2s; display: block;
  text-align: right; white-space: nowrap;
}
.mg-side-nav__links a:hover { color: var(--mg-magenta); }
.mg-side-nav__links a.is-active { color: var(--mg-magenta); font-weight: 500; }

/* Featured-länk längst ned */
.mg-side-nav__featured {
  font: 500 .75rem/1 var(--mg-font-head);
  color: var(--mg-magenta); letter-spacing: .03em;
  text-decoration: none; padding: 10px 0 0;
  margin-top: var(--mg-space-5); flex-shrink: 0;
  text-align: right;
}
```

### HTML — sidospår

```html
<div class="mg-side-nav" aria-label="Sidonavigering">
  <a class="mg-side-nav__logo" href="/" aria-label="Magello">
    <img src="/logos/icon-logotype.svg" alt="Magello">
  </a>
  <ul class="mg-side-nav__links">
    <li><a href="/digitala-tjanster.html">Vår expertis</a></li>
    <li><a href="#">Underkonsult</a></li>
    <li><a href="/om-oss.html" class="is-active">Om oss</a></li>
    <li><a href="#">Kontakta oss</a></li>
  </ul>
  <a class="mg-side-nav__featured" href="#">Lediga jobb</a>
</div>
```

### Innehållsförskjutning (undersidor med fixed header)

Med `position: fixed` tar headern ingen plats i flödet. Kompensera med padding-top på page-title:

```css
.mg-page-title {
  padding-top: calc(var(--mg-header-h) + var(--mg-space-6)); /* 120px + 36px */
  padding-bottom: 0;
}
```

### JavaScript

Se `styleguide/js/magello.js`. Den sköter scroll-tröskeln (80 px för `--rotate`), sidospårets `is-visible` (bara över 768 px), hamburgermenyn (öppna, stäng, `Escape`) och resize. Ingen sidspecifik JS behövs.

### Mobil-override (undersidor)

På mobil (hamburgerläge) ska headern **aldrig** rotera eller försvinna. Den ligger kvar efter scroll och blir lägre: navigationen går från 72 till 56 px och logotypen från 38 till 32 px. Polygonens förlängning försvinner som på desktop. Sidospåret döljs helt. Se D-48.

```css
@media (max-width: 768px) {
  .mg-side-nav { display: none !important; }
}
/* Måste ligga efter .mg-page-header--rotate.is-scrolled */
@media (max-width: 768px) {
  .mg-page-header.is-scrolled {
    transform: none;
    pointer-events: auto;
  }
  .mg-page-header.is-scrolled .mg-nav { height: var(--mg-nav-h-compact); }
  .mg-page-header.is-scrolled .mg-nav__logo svg { height: 32px; }
}
```

`.mg-nav` och logotypen har `transition: height 0.3s ease`, som stängs av vid `prefers-reduced-motion`.

> **Undermenyer** i sidospåret öppnas vid hover och klick på huvudlänk. Se [Dropdown-meny och undermenyer](#14-dropdown-meny-och-undermenyer).
---

## 14. Dropdown-meny och undermenyer

Navigationen har högst **två nivåer**. Samma menystruktur renderas på tre ställen och ska hållas synkad:

| Plats | När | Klassprefix | Öppnas med |
|---|---|---|---|
| Dropdown i headern | Desktop (>768 px), innan scroll | `mg-nav__` | Hover, chevron-klick |
| Sidospår | Desktop efter scroll > 80 px | `mg-side-` | Hover, klick på huvudlänk, chevron-klick |
| Mobilmeny | ≤768 px | `mg-mob-` | Chevron-klick (accordion) |

### Dropdown i headern

#### HTML

```html
<ul class="mg-nav__links">
  <li class="mg-nav__has-sub">
    <a href="/digitala-tjanster.html" class="is-active">Vår expertis</a>
    <button class="mg-nav__chevron-btn" aria-expanded="false" aria-label="Expandera Vår expertis">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
        <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
    <ul class="mg-nav__sub">
      <li><a href="/casesida.html">Case</a></li>
    </ul>
  </li>
  <li><a href="/om-oss.html">Om oss</a></li>
</ul>
```

#### CSS

```css
.mg-nav__links li { position: relative; }
.mg-nav__has-sub { display: inline-flex; align-items: center; }

.mg-nav__chevron-btn {
  background: none; border: none; cursor: pointer; padding: 2px 4px;
  color: inherit; display: flex; align-items: center; line-height: 1;
}
.mg-nav__chevron-btn svg { transition: transform .2s ease; }
.mg-nav__has-sub.is-open .mg-nav__chevron-btn svg { transform: rotate(180deg); }

/* position: fixed + JS-placering. Se "Varför fixed?" nedan. */
.mg-nav__sub {
  position: fixed; top: 0; left: 0;
  background: var(--mg-white); list-style: none;
  min-width: 170px; padding: 6px 0;
  box-shadow: 0 6px 24px rgba(0,0,0,.09);   /* enda tillåtna skuggan */
  opacity: 0; pointer-events: none;
  transform: translateY(-6px);
  transition: opacity .18s ease, transform .18s ease;
  z-index: 300;
}
.mg-nav__sub a {
  display: block; padding: 10px 20px;
  font: 400 .875rem/1 var(--mg-font-head);
  color: var(--mg-black); text-decoration: none; white-space: nowrap;
}
.mg-nav__sub a:hover,
.mg-nav__sub a.is-active { color: var(--mg-magenta); }

/* Synlighet styrs ENBART av .is-open — aldrig av :hover */
.mg-nav__has-sub.is-open .mg-nav__sub {
  opacity: 1; pointer-events: auto; transform: translateY(0);
}
```

#### JavaScript

Se `styleguide/js/magello.js`, avsnittet *Dropdown i headern*. Funktioner: `positionSub` (placerar `position: fixed`-menyn vid länkens underkant), `openDrop`, `scheduleClose` (220 ms, en timer per listpunkt i en `WeakMap`) och `closeAllDrops` (scroll, klick utanför, `Escape`). Kopiera filen rakt av.

#### Regler som gör att menyn inte försvinner

Fem saker ska alla vara på plats. Saknas en av dem stänger menyn när användaren rör musen från huvudlänken mot undermenyn.

1. **Ingen CSS `:hover` styr synligheten.** `:hover` på listpunkten släcker menyn i samma ögonblick som pekaren lämnar den. Bara `.is-open` får visa menyn.
2. **Ingen lucka.** Menyns överkant ligger exakt vid länkens underkant (`rect.bottom`, inte `rect.bottom + 8`).
3. **Fördröjd stängning (220 ms)** med en timer per listpunkt (`WeakMap`), så att musen hinner nå menyn.
4. **Lyssnare på själva undermenyn.** `mouseenter` avbryter timern, `mouseleave` startar den på nytt.
5. **Fördröjt byte till grannen (150 ms).** När en meny redan är öppen öppnas grannens meny först efter 150 ms hover, så att musen kan gå snett ned över grannlänken utan att menyn byts.

Dessutom: vid scroll flyttas öppna menyer med headern och stängs bara när headern roterat bort eller lämnat skärmen. Stäng vid klick utanför och `Escape`. Chevron-knappens `aria-expanded` ska spegla läget.

#### Varför `position: fixed`?

Headern har `transform` (rotationen vid scroll). Ett barn med `position: absolute` hamnar då relativt den transformerade föräldern och placeras fel, till exempel i vänstra hörnet (0, 0). Med `position: fixed` och koordinater från `getBoundingClientRect()` placeras menyn alltid mot fönstret.

#### Känd begränsning

När headern är roterad (`.is-scrolled`) returnerar `getBoundingClientRect()` koordinater i det roterade rummet (till exempel `top: -941, left: 1790`). Det är inget problem: roterad header har `pointer-events: none` och sidospåret tar över navigationen.

### Undermenyer i sidospåret

Sidospåret (se [Header — undersidor](#13-header--undersidor-rotation--sidospår)) visar samma struktur som dropdownen men som en lodrät lista. Undermenyn **fälls ut vid hover** och **vid klick på huvudlänken**.

#### HTML

```html
<ul class="mg-side-nav__links">
  <li class="mg-side-has-sub">
    <div class="mg-side-parent">
      <a href="/digitala-tjanster.html" class="is-active">Vår expertis</a>
      <button class="mg-side-toggle" aria-expanded="false" aria-label="Visa undermeny">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
    <ul class="mg-side-sub">
      <li><a href="/casesida.html">Case</a></li>
    </ul>
  </li>
  <li><a href="/om-oss.html">Om oss</a></li>
</ul>
```

#### CSS

```css
.mg-side-parent { display: flex; align-items: center; justify-content: space-between; gap: 4px; }
.mg-side-toggle {
  background: none; border: none; cursor: pointer;
  color: var(--mg-text-2); padding: 0;
  display: flex; align-items: center; flex-shrink: 0;
}
.mg-side-toggle svg { transition: transform .2s ease; }
.mg-side-has-sub:hover .mg-side-toggle svg,
.mg-side-toggle[aria-expanded="true"] svg { transform: rotate(180deg); }

.mg-side-sub { list-style: none; max-height: 0; overflow: hidden; transition: max-height .3s ease; }
.mg-side-has-sub:hover .mg-side-sub,
.mg-side-sub.is-open { max-height: 200px; }
.mg-side-sub a {
  display: block; padding: 5px 0 5px 10px; text-align: right;
  font: 400 .78rem/1 var(--mg-font-head);
  color: var(--mg-text-2); text-decoration: none;
}
.mg-side-sub a:hover, .mg-side-sub a.is-active { color: var(--mg-magenta); }
```

Textfärgerna ska vara mörka (`--mg-text-2`, `--mg-magenta`), för sidospåret har vit bakgrund. Vita `rgba(255,255,255,…)`-färger från en tidigare version gjorde undermenyn osynlig.

#### JavaScript — klick på huvudlänk expanderar

Också i `styleguide/js/magello.js`: chevron-knapparna (`.mg-mob-toggle`, `.mg-side-toggle`) fäller ut och in. I sidospåret fäller även ett klick på huvudlänken (`.mg-side-parent > a`) ut undermenyn i stället för att navigera, via `preventDefault`.

> **Designval:** huvudlänken i sidospåret leder inte vidare när den har undernivå. Underlänkarna är de verkliga målen. Har en huvudlänk en egen sida ska den sidan också finnas som första punkt i undermenyn ("Översikt").

### Tillgänglighet för menyerna

- Chevron-knappen har `aria-expanded` och `aria-label`.
- Allt går att nå med tangentbord: Tab till chevron, Enter/Space öppnar, `Escape` stänger.
- Fokus ska vara synligt (global `:focus-visible`-regel).
- Dolda menyer har `pointer-events: none` och `opacity: 0`. Lägg även `visibility: hidden` om innehållet inte ska nås av tangentbord eller skärmläsare när menyn är stängd.
---

## 15. Mobilmeny (hamburgermeny)

Alla sidor har en hamburgerknapp och ett helskärms-drawer som glider in från höger. Bakgrunden är `var(--mg-rose-100)`.

### Hamburgerknapp i nav

```html
<button class="mg-nav__burger" aria-label="Öppna meny"
        aria-expanded="false" aria-controls="mobile-menu">
  <svg width="24" height="18" viewBox="0 0 24 18" fill="none" aria-hidden="true">
    <rect width="24" height="2" rx="1" fill="currentColor"/>
    <rect y="8" width="24" height="2" rx="1" fill="currentColor"/>
    <rect y="16" width="24" height="2" rx="1" fill="currentColor"/>
  </svg>
</button>
```

```css
.mg-nav__burger {
  display: none;
  background: none; border: none; cursor: pointer;
  color: var(--mg-black); padding: 4px;
  flex-shrink: 0; align-items: center;
}
@media (max-width: 768px) {
  .mg-nav__links    { display: none; }
  .mg-nav__featured { display: none; }
  .mg-nav__burger   { display: flex; }
}
```

### Drawer HTML

```html
<div class="mg-mobile-menu" id="mobile-menu" aria-hidden="true" aria-label="Mobilnavigering">
  <div class="mg-mobile-menu__head">
    <a href="/" class="mg-nav__logo" aria-label="Magello">
      <!-- Full Magello SVG-logotyp, height: 32px -->
      <svg ...>...</svg>
    </a>
    <button class="mg-mobile-menu__close" aria-label="Stäng meny">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M5 5L19 19M19 5L5 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </button>
  </div>
  <ul class="mg-mobile-menu__links">
    <li><a href="/digitala-tjanster.html">Vår expertis</a></li>
    <li><a href="#">Underkonsult</a></li>
    <li><a href="/om-oss.html">Om oss</a></li>
    <li><a href="#">Kontakta oss</a></li>
  </ul>
  <a class="mg-mobile-menu__featured" href="#">Lediga jobb</a>
</div>
```

### Drawer CSS

```css
.mg-mobile-menu {
  position: fixed;
  inset: 0;
  z-index: 300;
  background: var(--mg-rose-100);
  display: flex; flex-direction: column;
  padding: var(--mg-space-5) var(--mg-gutter) var(--mg-space-7);
  transform: translateX(100%);       /* dold till höger */
  transition: transform 0.38s cubic-bezier(0, 0, 0.2, 1);
  visibility: hidden;
}
.mg-mobile-menu.is-open {
  transform: translateX(0);
  visibility: visible;
}
.mg-mobile-menu__head {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: var(--mg-space-9); /* 96px till länkarna */
}
.mg-mobile-menu__close {
  background: none; border: none; cursor: pointer;
  color: var(--mg-black); padding: 8px; line-height: 1;
}
.mg-mobile-menu__links {
  list-style: none;
  display: flex; flex-direction: column;
  gap: 0; flex: 1; justify-content: center;
}
/* Stora navlänkar med dividers */
.mg-mobile-menu__links a {
  font: 700 var(--mg-fs-h2)/1.15 var(--mg-font-head);
  text-decoration: none; color: var(--mg-black);
  display: block; padding: var(--mg-space-4) 0;
  border-bottom: 1px solid var(--mg-rose-200);
}
.mg-mobile-menu__links li:first-child a { border-top: 1px solid var(--mg-rose-200); }
.mg-mobile-menu__links a.is-active,
.mg-mobile-menu__links a:hover { color: var(--mg-magenta); }
.mg-mobile-menu__featured {
  font: 500 1rem/1 var(--mg-font-head);
  color: var(--mg-magenta); text-decoration: none;
  letter-spacing: .03em; margin-top: var(--mg-space-6);
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .mg-mobile-menu { transition: none; }
}
```
### Accordion i mobilmenyn

Undermenyer i mobilmenyn fälls ut med chevron-knappen. Hela rubrikraden är klickbar mot sin sida; chevron öppnar undernivån.

```html
<ul class="mg-mobile-menu__links">
  <li class="mg-mob-has-sub">
    <div class="mg-mob-parent">
      <a href="/digitala-tjanster.html" class="is-active">Vår expertis</a>
      <button class="mg-mob-toggle" aria-expanded="false" aria-label="Visa undermeny">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
    <ul class="mg-mob-sub">
      <li><a href="/casesida.html">Case</a></li>
    </ul>
  </li>
  <li><a href="/om-oss.html">Om oss</a></li>
</ul>
```

```css
.mg-mob-parent { display: flex; align-items: stretch; border-bottom: 1px solid var(--mg-rose-200); }
.mg-mob-parent > a {
  flex: 1; display: block;
  padding: var(--mg-space-4) var(--mg-space-6);
  font: 500 1.1rem/1 var(--mg-font-head);
  color: var(--mg-black); text-decoration: none;
}
.mg-mob-parent > a.is-active { color: var(--mg-magenta); }
.mg-mob-toggle {
  background: none; border: none; cursor: pointer;
  padding: 0 var(--mg-space-5); color: var(--mg-black);
  display: flex; align-items: center;
}
.mg-mob-toggle svg { transition: transform .2s ease; }
.mg-mob-toggle[aria-expanded="true"] svg { transform: rotate(180deg); }
.mg-mob-sub { list-style: none; max-height: 0; overflow: hidden; transition: max-height .3s ease; }
.mg-mob-sub.is-open { max-height: 300px; }
.mg-mob-sub a {
  display: block; padding: 12px calc(var(--mg-space-6) + 14px);
  font: 400 .9rem/1 var(--mg-font-head);
  color: var(--mg-text-2); text-decoration: none;
  border-bottom: 1px solid var(--mg-rose-100);
}
.mg-mob-sub a:hover, .mg-mob-sub a.is-active { color: var(--mg-magenta); }
```

Mobilmenyns rosa hårlinjer (`--mg-rose-200` och `--mg-rose-100`) är funktionella listavgränsare i en helskärmslista. Det är ett av de få tillåtna linjeundantagen.

---

## 16. Animationer — komplett lista

| Element | Trigger | Animation | Timing |
|---|---|---|---|
| Header shape (startsida) | scroll > 8px | `clip-path` kollapsar | `0.4s ease` |
| Header rotation (undersida) | scroll > 80px | `rotate(90deg)` från `right top` | `0.6s cubic-bezier(0.4, 0, 0.6, 1)` |
| Header blir lägre (mobil) | scroll > 80px (undersida), 8px (startsida) | `height` 72 → 56 px | `0.3s ease` |
| Sidospår slide-in | scroll > 80px (desktop) | `translateX(0)` + `opacity: 1` | `0.42s cubic-bezier(0, 0, 0.2, 1)` med `0.18s delay` |
| Mobilmeny drawer | hamburgare-klick | `translateX(0)` | `0.38s cubic-bezier(0, 0, 0.2, 1)` |
| Knapp hover | hover | `clip-path` öppnas | `0.35s ease` |
| Offer-kort hover | hover | `clip-path` + `background` | `0.35s ease` |
| Bild hover (split layout) | hover på förälder | `clip-path` rätas ut | `0.4s ease` |
| Case-kortbild hover | hover | `clip-path` rotation | `0.4s ease` |
| Overlay på case-kort | hover | `opacity` 0 → .88 | `0.4s ease` |
| Filter-tab hover | hover | `clip-path` + `background` | `0.25s / 0.35s ease` |
| Dropdown (header) | `.is-open` | `opacity` + `translateY(-6px → 0)` | `0.18s ease` |
| Undermeny sidospår/mobil | hover / klick | `max-height` 0 → 200/300 px | `0.3s ease` |
| Chevron | öppen undermeny | `rotate(180deg)` | `0.2s ease` |

---

## 17. Knappar

5-hörns polygon, ingen kant exakt horisontell eller vertikal.

```css
.mg-btn {
  display: inline-block;
  font: 500 .9375rem/1 var(--mg-font-head);
  letter-spacing: .04em;
  padding: 16px 32px;
  text-decoration: none;
  cursor: pointer;
  border: none;
  clip-path: polygon(2% 5%, 99% 0%, 100% 88%, 97% 100%, 0% 95%);
  transition: clip-path .35s ease;
}
.mg-btn:hover {
  clip-path: polygon(0% 2%, 100% 0%, 99% 93%, 96% 100%, 1% 98%);
}
.mg-btn:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 4px;
}

/* Primär — magenta */
.mg-btn--primary  { background: var(--mg-magenta); color: white; }
.mg-btn--primary:hover { color: white; }

/* Sekundär — rose-200 */
.mg-btn--secondary { background: var(--mg-rose-200); color: var(--mg-black); }
.mg-btn--secondary:hover { background: var(--mg-rose-300); color: var(--mg-black); opacity: 1; }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .mg-btn { transition: none; }
  .mg-btn:hover { clip-path: polygon(2% 5%, 99% 0%, 100% 88%, 97% 100%, 0% 95%); opacity: .82; }
}
```

### Regler för knappar

- **Primär = magenta** (`--mg-magenta`, vit text). **Sekundär = rose-200** (`--mg-rose-200`, svart text, hover `--mg-rose-300`).
- Ett par visas som **primär först, sekundär efter**. Max en primär per vy.
- **Ingen outline-variant.** En knapp med kant utan fyllnad kräver `border`/`box-shadow` som kant, vilket strider mot principen om accentfärger och linjer (och `clip-path` skär ändå bort kanten).
- Ingen kant på någon knapp. `clip-path` klipper bort `border`.
- Ikon, om den finns, sitter till vänster med 8 px mellanrum.
- Disabled: `opacity: .35; cursor: not-allowed;`.
- Fokus: `outline: 3px solid currentColor; outline-offset: 4px;`.
- Texten är ett verb som beskriver handlingen.
- **Knapp med ikon:** lägg modifiern `.mg-btn--icon` (`display: inline-flex; align-items: center; gap: 8px;`). Utan den är knappen `inline-block`, vilket ger exakt samma radhöjd som löpande text.
- Det finns **en** knappdefinition. En äldre variant (`.mg-btn-primary`, versaler, större padding) är borttagen.
---

## 18. Sektioner & bakgrunder

### Vit sektion (standard)

```css
.mg-section { padding-block: var(--mg-space-8); }
```

### Rosagrå sektion med polygon-kanter

```css
.mg-section--rose {
  background: var(--mg-rose-100);
  padding-block: calc(var(--mg-space-8) + 24px);
  clip-path: polygon(0% 3%, 62% 0%, 100% 2%, 100% 97%, 38% 100%, 0% 98%);
  margin-block: var(--mg-space-4);
}
```

### Sektionshuvud

```css
.mg-section-head { margin-bottom: var(--mg-space-7); }
.mg-label {
  font: 700 .6875rem/1 var(--mg-font-head);
  letter-spacing: .12em; text-transform: uppercase;
  color: var(--mg-magenta); margin-bottom: var(--mg-space-3);
}
```

---

## 19. Bilder — behandling

**Alla foton renderas i svartvitt** och klipps i oregelbundna polygoner.

```css
/* Grundfilter för alla bilder */
filter: grayscale(1) contrast(1.05);

/* Tre poly-varianter för bildgalleri */
.mg-poly-img--a { aspect-ratio: 4/3; clip-path: polygon(7% 0%, 94% 2%, 100% 10%, 98% 90%, 93% 100%, 5% 97%, 0% 88%, 2% 8%); }
.mg-poly-img--b { aspect-ratio: 3/4; clip-path: polygon(6% 0%, 97% 3%, 100% 15%, 96% 96%, 88% 100%, 2% 98%, 0% 84%, 4% 4%); }
.mg-poly-img--c { aspect-ratio: 4/3; clip-path: polygon(0% 5%, 4% 0%, 98% 2%, 100% 12%, 96% 100%, 2% 96%); }
```

### Bildgaller-grid (tre kolumner)

```css
.mg-poly-grid {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: var(--mg-space-5); align-items: start;
}
@media (max-width: 599px) { .mg-poly-grid { grid-template-columns: 1fr; } }
```

### Split-bild med hover-animation

```css
.mg-expertis-split__img img {
  display: block; width: 100%; height: 400px;
  object-fit: cover;
  filter: grayscale(1) contrast(1.05);
  clip-path: polygon(3% 0%, 100% 2%, 97% 98%, 0% 100%);
  transition: clip-path .4s ease;
}
.mg-expertis-split:hover .mg-expertis-split__img img {
  clip-path: polygon(0% 0%, 100% 1%, 100% 100%, 3% 98%);
}
```

---

## 20. Ikoner & grafik

### Ikonspråket — principer

Alla ikoner i Magello-designen är **platta SVG-vektorer**. De följer exakt samma designlogik som resten av systemet:

- **Inga gradienter** — fyllnadsfärger är solida
- **Inga drop shadows** — djup skapas av form, inte effekter
- **Aldrig opacity-sänkning** — ikoner visas alltid i fullstyrka
- **Oregelbundna, organiska former** — liksom polygonerna i layouten, är ikonerna handritade och rörliga, inte geometriskt perfekta
- **Accentfärger som fyllnad** — ikoner är ett av de få ställen accentfärger (blå, röd, gul, grön, magenta) används som fyllnad, inte bara text

### Ikonernas färglogik

Ikonerna är *inte* monokromatiska. Varje ikon har en dominerande accentfärg som väljs utifrån ikonens semantiska betydelse — inte efter vilken sida den visas på. Det är ikonens *känsla* som styr färgen.

| Ikon | Fil | Dominerande färg | Hex | Semantik |
|---|---|---|---|---|
| Noder/nätverk | `nodes.svg` | Blå | `#009EE3` | Teknologi, kopplingar |
| Markup/kod | `markup.svg` | Blå | `#009FE3` | Kod, digitalt |
| Pratbubbla | `speak-bouble.svg` | Grön | `#00964F` | Dialog, kommunikation |
| Timer | `timer.svg` | Röd | `#E20430` | Tid, brådska, agile |
| Tumme upp | `thumbs-up.svg` | Grön | `#00964F` | Kvalitet, godkänt |
| Raket | `rocket.svg` | Mörkblå + orange | `#0D3956` + `#FC611F` | Innovation, lansering |
| Glödlampa | `light.svg` | Gul | `#FFDD00` | Idé, AI, insikt |
| Pil upp-höger | `arrow-up-right.svg` | Blå | `#009FE3` | Tillväxt, länk vidare |
| Moln+pil | `cloud-arrow.svg` | Röd | `#E20430` | Moln, driftsättning |
| Citationstecken | `citation.svg` | Blå | `#28ABE3` | Citat-dekor (ej standalone) |

### Värdeords-ikoner `/graphics/värdeord/`

Värdeordsikonerna är ett eget set kopplade till Magello-identiteten. De följer magenta/grönt/blått/gult-uppdelningen och används *enbart* på sidor som kommunicerar Magello som bolag.

| Fil | Värdeord | Dominerande färg | Hex |
|---|---|---|---|
| `personliga.svg` | Personliga | Gul/amber | `#FBBA00` |
| `trygga.svg` | Trygga | Blå | `#009EE3` |
| `kommunikativa.svg` | Kommunikativa | Magenta | `#EC008C` |
| `lärande.svg` | Lärande | Grön | `#00964F` |

### Storlekar per kontext

Ikonstorlek är *inte* fri — den beror på sammanhang:

| Kontext | Storlek | CSS |
|---|---|---|
| Ikonsektion (standalone showcase) | 72 × 72 px | `width: 72px; height: 72px` |
| Erbjudandekort (offer-card) | 40 × 40 px | `width: 40px; height: 40px` |
| Värdeords-kort | 40 × 40 px | `width: 40px; height: 40px` |
| Sidospalt / inline | 24–32 px | `width: 28px; height: 28px` |
| Citation-dekor (`::before`) | 40 × 35 px | `width: 40px; height: 35px` |

### HTML — inline eller img?

Ikoner laddas alltid via `<img>` — inte inline SVG — om de inte behöver ärva CSS-färg (t.ex. via `currentColor`). Befintliga ikoner är färgsatta i SVG-koden och behöver inte `currentColor`.

```html
<!-- Standard — img med alt="" för dekorativa ikoner -->
<img src="/graphics/light.svg" alt="" width="40" height="40">

<!-- Med semantisk betydelse — alt beskriver vad ikonen representerar -->
<img src="/graphics/nodes.svg" alt="Systemarkitektur" width="72" height="72">
```

### CSS — inbäddning i komponent

```css
/* I ett offer-card eller liknande komponent */
.mg-offer-card__icon {
  width: 40px; height: 40px;
  flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
}
.mg-offer-card__icon img {
  width: 100%; height: 100%;
  object-fit: contain;
  /* ALDRIG: filter, opacity, grayscale — ikoner visas alltid i originalfärg */
}
```

### Vad du INTE gör med ikoner

```css
/* ✗ Aldrig: */
img.icon { opacity: 0.55; }          /* dämpar ikonen */
img.icon { filter: grayscale(1); }   /* gör den svartvit — strider mot systemet */
img.icon { filter: brightness(0.8); } /* mörknar den */
```

Svartvitt gäller **foton** — aldrig ikoner. Ikoner är en av de enda synliga bärarna av accentfärg i gränssnittet och ska synas med full styrka.

### Citation.svg — speciell användning

`citation.svg` är inte en fristående ikon — den är en dekor för `.mg-pullquote`. Den laddas via CSS `background-image` i ett `::before`-pseudoelement och ska aldrig visas standalone eller med opacity:

```css
.mg-pullquote::before {
  content: '';
  position: absolute;
  left: 0; top: -4px;
  width: 40px; height: 35px;
  background: url('/graphics/citation.svg') no-repeat left top / contain;
  /* Ingen opacity — citattecknet ska synas tydligt */
}
```

### Skapa en ny ikon — riktlinjer

Om du behöver en ny ikon som passar i systemet:

1. **Stil:** Handritad, organisk — inte geometriskt perfekt. Liknar Magello-ikonernas rörelsekänsla.
2. **Format:** SVG, `fill="none"` på root-elementet, solida fills på paths.
3. **Färg:** Välj en av accentfärgerna baserat på ikonens semantik (se tabellen ovan). Blanda max 2–3 färger per ikon.
4. **Storlek:** Rita i ett rimligt viewBox (t.ex. `0 0 100 100`) — storleken sätts av CSS.
5. **Bakgrund:** Ikonen ska fungera på vit, rose-50 och rose-100 bakgrund.
6. **Inga effekter:** Ingen stroke, ingen gradient, ingen drop shadow.
7. **Placering:** Spara i `/graphics/[namn].svg`. Namnge med bindestreck, engelska.

---

## 21. Kort (cards)

Alla kort är polygonytor utan kant och utan skugga. De använder tokens för yta och avstånd, och formen skiljer dem från bakgrunden. CSS:en finns i avsnittet *KORT* i `styleguide/css/magello.css`.

### Kortfamiljen

| Kort | Används till | Klasser | Yta |
|---|---|---|---|
| Textkort | Expertisområden, tjänster | `.mg-card .mg-card--text` | Vit polygon |
| Bildkort | Expertis med foto | `.mg-card .mg-card--image` + `__img`, `__body`, `__kicker` | Vit polygon |
| Kompakt kort | Tre korta fakta i rad | `.mg-card .mg-card--compact` + `__label` | Vit polygon |
| Erbjudandekort | Ikon + text, hover öppnar formen | `.mg-offer-card` | Rosagrå 50 |
| Värdekort | Värdeord med ikon överst | `.mg-value-card` | Rosagrå 100 |
| Ingångskort | Länk till undersida | `.mg-sub-card` | Vit polygon |
| Case-kort (panel) | Case på landningssidor | `.mg-case-card` | Rosagrå 50 text |
| Case-tile | Case med bildöverlägg vid hover (startsida) | `.mg-case-tile` | Ingen |
| Case-teaser | Kompakt case med text och länk | `.mg-case-teaser` | Vit |
| Utvalt case | Stort case, bild + text | `.mg-case-featured` | Rosagrå 50 |
| Kontaktkort | Person med foto | `.mg-contact-card` (avsnitt 30) | Rosagrå 100 |

Rutnät: `.mg-card-grid` (auto-fill, min 300 px), `.mg-card-grid--loose` (min 280 px, större mellanrum) och `.mg-card-grid--three` (exakt tre kolumner, en på mobil).

### Grunden: ett kort med tre varianter

```css
.mg-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--mg-space-5);
}
.mg-card-grid--loose { grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: var(--mg-space-6); }
.mg-card-grid--three { grid-template-columns: repeat(3, 1fr); gap: var(--mg-space-3); margin: var(--mg-space-6) 0; }
@media (max-width: 700px) { .mg-card-grid--three { grid-template-columns: 1fr; } }

.mg-card {
  background: var(--mg-white);
  clip-path: polygon(0% 0%, 100% 2%, 98% 96%, 95% 100%, 3% 98%, 0% 4%);
}
/* Textkort */
.mg-card--text { padding: var(--mg-space-6) var(--mg-space-5); }
.mg-card--text h3 { font: 700 var(--mg-fs-h3)/1.2 var(--mg-font-head); margin-bottom: var(--mg-space-3); color: var(--mg-black); }
.mg-card--text p  { font-size: .9375rem; color: var(--mg-text-2); line-height: 1.65; }
/* Kompakt kort */
.mg-card--compact { padding: var(--mg-space-5) var(--mg-space-4); }
.mg-card__label {
  font: 700 .6875rem/1 var(--mg-font-head);
  letter-spacing: .1em; text-transform: uppercase;
  color: var(--mg-magenta); margin-bottom: var(--mg-space-3); display: block;
}
.mg-card--compact h3 { font: 700 1rem/1.2 var(--mg-font-head); margin-bottom: var(--mg-space-3); }
.mg-card--compact p  { font-size: .8125rem; color: var(--mg-text-2); line-height: 1.6; margin: 0; }
/* Bildkort */
.mg-card--image h3 { font: 700 var(--mg-fs-h4)/1.2 var(--mg-font-head); margin-bottom: var(--mg-space-3); }
.mg-card--image p  { font-size: .9375rem; color: var(--mg-text-2); }
```

```html
<div class="mg-card-grid">
  <article class="mg-card mg-card--text">
    <h3>Förstudier &amp; PoC</h3>
    <p>Grunden för en lyckad digital lösning läggs tidigt.</p>
  </article>
  <article class="mg-card mg-card--text">…</article>
</div>
```

### Regler

- **Ingen `box-shadow` och ingen kantlinje.** En skugga som ring runt ett polygonklippt kort syns bara som ett svagt streck vid hörnen. Formen och bakgrunden räcker.
- Ett vitt kort på vit sida syns bara genom sin text. Lägg kort på en rosagrå sektion, eller använd rosa kort (`.mg-offer-card`) när formen ska synas.
- **Inga löpnummer** (01, 02, 03) på kort.
- Kortets rubrik är H3, kortets text är Roboto i `--mg-text-2`.
- Kortvarianten väljs efter innehållet (se Strapi-kartläggningen i avsnitt 36): bild → bildkort, ikon → erbjudandekort, annars textkort.
- En ny kortvariant skapas som modifier (`.mg-card--namn`) på `.mg-card`, inte som en ny komponent med kopierad polygon.

### Callout-ruta

```css
.mg-callout {
  background: var(--mg-rose-200);
  padding: 20px 24px 24px;
  clip-path: polygon(0% 6%, 5% 0%, 92% 2%, 100% 9%, 97% 100%, 3% 96%);
}
```
---

## 22. Processsteg (chevrons)

Kedjad pilform byggd med `clip-path: polygon()`.

```css
.mg-steps { display: flex; gap: 3px; flex-wrap: wrap; }

.mg-step {
  flex: 1; min-width: 120px;
  padding: 14px 20px 14px 28px;
  clip-path: polygon(
    1% 4%, calc(100% - 16px) 1%, 100% 50%,
    calc(100% - 16px) 96%, 2% 100%, 14px 50%
  );
  font: 700 .875rem/1.3 var(--mg-font-head); text-align: center;
}

/* Första steget — ingen vänsterspets */
.mg-step:first-child {
  clip-path: polygon(
    1% 4%, calc(100% - 16px) 1%, 100% 50%,
    calc(100% - 16px) 96%, 2% 100%
  );
}

/* Färgvarianter */
.mg-step--blue    { background: var(--mg-blue);    color: white; }
.mg-step--orange  { background: var(--mg-orange);  color: var(--mg-black); }
.mg-step--red     { background: var(--mg-red);     color: white; }
.mg-step--yellow  { background: var(--mg-yellow);  color: var(--mg-black); }
.mg-step--green   { background: var(--mg-green);   color: white; }
.mg-step--magenta { background: var(--mg-magenta); color: white; }

/* Stegnummer-label */
.mg-step__num {
  display: block;
  font-size: .7rem; font-weight: 400;
  opacity: .7; margin-bottom: 4px;
}
```

**Regel:** Sista steget i en process ska alltid vara `mg-step--magenta`.

---

## 23. Tabell

```css
.mg-table { width: 100%; border-collapse: collapse; font-size: .9375rem; }
.mg-table th, .mg-table td {
  padding: 10px 14px; border: 1px solid var(--mg-rose-200);
  text-align: left; vertical-align: top;
}
.mg-table thead th { background: var(--mg-rose-200); font: 700 .875rem/1 var(--mg-font-head); }
.mg-table tbody tr:nth-child(even) { background: var(--mg-rose-50); }
.mg-table tbody td:first-child { font-weight: 700; }
.mg-table tfoot td { font-weight: 700; border-top: 2px solid var(--mg-rose-300); }
```

Celllinjerna är **funktionella hårlinjer** i `--mg-rose-200`, ett av de få tillåtna linjeundantagen. Aldrig accentfärgade och aldrig som dekoration utanför tabellen.


Markdown-tabeller i `.mg-prose` får samma utseende via `.mg-prose table` (rosa rubrikrad, bandning, första kolumnen fet).
---

## 24. Artikel — undersidans layout

> **Designdirektiv:** använd inte högerställda informationsrutor. Informationsrutor läggs efter varandra i textflödet, formade som den rosagrå `mg-infoblock`. Ingress och brödtext går alltid i 100 % bredd.

Undersidan är en **enda kolumn**. Ordningen är:

1. Brödsmula och sidtitel
2. Ingress i full bredd
3. Löptext (`.mg-prose`)
4. Pull-quote (valfri)
5. En eller flera informationsrutor efter varandra, i full bredd
6. Mer löptext

Texten återgår alltid till 100 % bredd efter en informationsruta. Inget flyter bredvid texten (`float`) och inget lägger sig i en smal kolumn bredvid den (`grid-template-columns: 1fr 300px`).

### CSS

```css
.mg-article-layout { padding-block: var(--mg-space-8); }

/* Informationsrutor som ligger efter varandra */
.mg-article-sidebar { display: block; margin: var(--mg-space-6) 0; }
.mg-sidebar__block {
  background: var(--mg-rose-50);
  padding: var(--mg-space-5) var(--mg-space-6);
  margin-bottom: var(--mg-space-5);
  clip-path: polygon(0% 0%, 100% 1%, 99% 99%, 0% 100%);
}
.mg-sidebar__block:last-child { margin-bottom: 0; }

/* Siffror/fakta visas i en rad inne i rutan (full bredd används väl) */
.mg-sidebar__facts-row {
  display: flex; flex-wrap: wrap;
  gap: var(--mg-space-4) var(--mg-space-8);
  margin-top: var(--mg-space-4);
}
.mg-sidebar__facts-row .mg-sidebar__fact {
  border-bottom: none; margin-bottom: 0; padding-bottom: 0; flex: 0 0 auto;
}
.mg-sidebar__num { font: 700 2rem/1 var(--mg-font-head); color: var(--mg-grey-300); }
```

### HTML

```html
<div class="mg-article-layout">
  <div class="mg-prose">
    <p class="mg-lead">Ingress i full bredd …</p>
    <p>Brödtext …</p>
    <blockquote class="mg-pullquote"><p>Citat …</p></blockquote>

    <!-- Informationsrutor efter varandra -->
    <aside class="mg-article-sidebar">
      <div class="mg-sidebar__block">
        <p class="mg-infoblock__label">Magello i siffror</p>
        <div class="mg-sidebar__facts-row">
          <div class="mg-sidebar__fact"><span class="mg-sidebar__num">30</span> år</div>
          <div class="mg-sidebar__fact"><span class="mg-sidebar__num">120</span> konsulter</div>
        </div>
      </div>
      <div class="mg-sidebar__block">
        <p class="mg-infoblock__label">Certifieringar</p>
        <p>…</p>
      </div>
    </aside>

    <h2>Hur vi arbetar</h2>   <!-- texten fortsätter i 100 % bredd -->
    <p>…</p>
  </div>
</div>
```

Ingen `style="clear:both"` och ingen clearfix behövs, eftersom inget flyter.

### Faktarutor — metadata i artiklar och case

Metadata (kund, roll, teknik, period, taggar, författare, datum) visas som en **informationsruta efter ingressen**, med raden av fakta inne i rutan. Inte som en högerspalt. På mobil blir faktaraden en lodrät lista.

---

## 25. Sidtitel och ingångssida

Två startmönster för undersidor. De delar brödsmula, kicker och rubrik och ska ligga på **exakt samma höjd och vänsterkant** (se [Linjering](#11-layout-bredd-och-linjering)).

| Mönster | Används till | Klasser |
|---|---|---|
| Sidtitel (DocTitle) | Om oss, artiklar, case, textsidor | `.mg-page-title` |
| Ingångssida | Expertisområden, landningssidor | `.mg-ingang-hero` + `.mg-ingang-col` |

### Sidtitel (DocTitle)

Brödsmula, stor rubrik, underrubrik och "sedan"-etikett.

```css
.mg-page-title { padding-top: calc(var(--mg-header-h) + var(--mg-space-6)); padding-bottom: 0; }
.mg-doc-title {
  font: 700 clamp(3.2rem, 2rem + 5vw, 6.5rem)/1 var(--mg-font-head);
  color: var(--mg-black);
  letter-spacing: -.01em;
  margin-bottom: var(--mg-space-3);
}
.mg-doc-sub {
  font: 400 22pt/2.2 var(--mg-font-head);
  color: var(--mg-text-2);
  letter-spacing: 0.02em;
  margin-top: 34px;
  margin-bottom: 24px;
}
.mg-page-title__since {
  font: 700 .75rem/1 var(--mg-font-head);
  letter-spacing: .12em; text-transform: uppercase;
  color: var(--mg-grey-300);
  margin-bottom: var(--mg-space-7);
  display: block;
}
```

```html
<div class="mg-page-title">
  <div class="mg-page-title__inner mg-wrap">
    <nav class="mg-breadcrumb" aria-label="Brödsmula">
      <a href="/">Hem</a>
      <span class="mg-breadcrumb__sep">/</span>
      <span aria-current="page">Om oss</span>
    </nav>
    <h1 class="mg-doc-title">Vi har levererat värde i 30 år</h1>
    <p class="mg-doc-sub">Vi hjälper er bygga hållbara lösningar för långa relationer</p>
    <span class="mg-page-title__since">Sedan 1996</span>
  </div>
</div>
```

**Ingen** linje under sidtiteln.

### Ingångssida (hero med kicker och handlingar)

Ingångssidor börjar med en kolumn med brödsmula, kicker, rubrik, underrubrik, knappar och ingress. Bakom kolumnen kan ett hero-foto ligga (svartvitt).

```css
.mg-ingang-hero {
  background-size: cover;
  background-position: center;
  padding-top: var(--mg-header-h);              /* fixed header tar ingen plats */
}
.mg-ingang-col {
  width: min(var(--mg-wide), 100%);              /* samma bredd som navigationen */
  margin-inline: auto;
  background: var(--mg-white);
  padding: var(--mg-space-6) var(--mg-gutter);   /* 36 px topp ger brödsmula på 156 px */
  padding-bottom: var(--mg-space-9);
}
.mg-kicker {
  display: inline-block;
  font: 700 .6875rem/1 var(--mg-font-head);
  letter-spacing: .14em; text-transform: uppercase;
  color: var(--mg-magenta); margin-bottom: var(--mg-space-4);
}
.mg-ingang-title {
  font: 700 clamp(3.2rem, 2rem + 5vw, 6.5rem)/1 var(--mg-font-head);
  letter-spacing: -.01em;
  margin-bottom: var(--mg-space-5);
}
.mg-ingang-sub {
  font: 400 var(--mg-fs-subtitle)/1.55 var(--mg-font-head);
  color: var(--mg-text-2);
  max-width: 60ch;
  margin-bottom: var(--mg-space-7);
}
.mg-ingang-actions { display: flex; gap: var(--mg-space-4); flex-wrap: wrap; }
.mg-ingang-intro {
  font: 400 1.05rem/1.75 var(--mg-font-body);
  color: var(--mg-text-2);
  max-width: 68ch;
  margin-top: var(--mg-space-7);
  padding-top: var(--mg-space-7);
}
.mg-breadcrumb {
  display: flex; gap: var(--mg-space-2); align-items: center;
  font: 400 .75rem/1 var(--mg-font-body);
  color: var(--mg-grey-300);
}
/* Avståndet under brödsmulan sätts av containern, inte av brödsmulan */
.mg-ingang-col .mg-breadcrumb { margin-bottom: var(--mg-space-6); }
.mg-page-title .mg-breadcrumb { margin-bottom: var(--mg-space-4); }
.mg-breadcrumb a { color: var(--mg-grey-300); text-decoration: none; }
.mg-breadcrumb a:hover { color: var(--mg-magenta); }
.mg-breadcrumb__sep { opacity: .4; }
```

```html
<div class="mg-ingang-hero">
  <div class="mg-ingang-col">
    <nav class="mg-breadcrumb" aria-label="Brödsmula">…</nav>
    <p class="mg-kicker">Expertisområde</p>
    <h1 class="mg-ingang-title">Hållbara<br>digitala tjänster</h1>
    <p class="mg-ingang-sub">Vi bygger digitala lösningar som löser era faktiska problem.</p>
    <div class="mg-ingang-actions">
      <a href="#kontakt" class="mg-btn mg-btn--primary">Prata med oss</a>
      <a href="#specialistomraden" class="mg-btn mg-btn--secondary">Vad vi erbjuder</a>
    </div>
    <p class="mg-ingang-intro">Magello är engagerade i att …</p>
  </div>
</div>
```

Knapparna är ett par: **primär magenta först, sekundär rose-200 efter**. Se [Knappar](#17-knappar). En outline-knapp (kant utan fyllnad) används inte.

> Bilden är ett `<img class="mg-img-block__bg" src="…" alt="…">`, inte en CSS-bakgrund. Då fungerar den oavsett var CSS-filen ligger, och den får alt-text.

Ingångssidan får gärna följas av en bildsektion (`.mg-img-block`) och därefter innehållssektioner. Den har inget löpnummer på sina kort.

#### Bildsektion på ingångssida

```css
.mg-img-block {
  max-width: var(--mg-wide);
  margin-inline: auto;
  padding-inline: var(--mg-gutter);
  padding-block: 0 var(--mg-space-9);
}
.mg-img-block__frame { position: relative; min-height: 420px; }
.mg-img-block__bg {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover; object-position: center;
  filter: grayscale(1) contrast(1.05);
}
.mg-img-block__plate {
  position: relative; z-index: 2;
  background: var(--mg-white);
  padding: var(--mg-space-7);
  max-width: 380px;
  margin: var(--mg-space-8);
  clip-path: polygon(0% 3%, 4% 0%, 97% 2%, 100% 6%, 98% 94%, 94% 100%, 2% 97%, 0% 93%);
}
@media (max-width: 768px) {
  .mg-img-block__frame { min-height: 300px; }
  .mg-img-block__plate { max-width: none; margin: var(--mg-space-5); }
}
```

Padding använder `--mg-gutter`, inte egna `clamp()`-värden, så att bilden linjerar med resten.
---

## 26. Pullquote

Citat med `citation.svg` som dekor (utan opacity).

```css
.mg-pullquote {
  margin: var(--mg-space-7) 0;
  position: relative;
  padding-left: 56px;
}
.mg-pullquote::before {
  content: '';
  position: absolute;
  left: 0; top: -4px;
  width: 40px; height: 35px;
  background: url('/graphics/citation.svg') no-repeat left top / contain;
  /* ALDRIG opacity här */
}
.mg-pullquote p {
  font: 500 clamp(1.2rem, 1rem + 1vw, 1.6rem)/1.35 var(--mg-font-head) !important;
  color: var(--mg-black) !important;
  margin: 0 !important;
}
```


Citat som skrivs som Markdown (`> citat`) får samma utseende via `.mg-prose blockquote`. Samma `citation.svg` används på alla sidor, även artikelsidan.
---

## 27. Infoblock

Ruta i löptext med magenta etikett.

```css
.mg-infoblock {
  background: var(--mg-rose-50);
  padding: var(--mg-space-5) var(--mg-space-6);
  margin: var(--mg-space-6) 0;
  clip-path: polygon(0% 0%, 100% 1%, 99% 99%, 0% 100%);
}
.mg-infoblock__label {
  font: 700 .65rem/1 var(--mg-font-head);
  letter-spacing: .12em; text-transform: uppercase;
  color: var(--mg-magenta); margin-bottom: var(--mg-space-3);
}
```

### Regler

- Infoblock **läggs efter varandra i textflödet, i full bredd**. De flyter aldrig upp i en smal högerspalt.
- Texten före och efter infoblocket går i 100 % bredd.
- Faktaraden (till exempel "Magello i siffror") visas horisontellt inne i rutan (`.mg-sidebar__facts-row`).
- Flera block efter varandra delar samma stil och har `--mg-space-5` mellan sig.

---

## 28. Tidslinje

Vertikal tidslinje med platt rosa linje, diamantformade punkter och årstal till vänster. Linjen är **inte** en accentfärg och har ingen gradient.

```css
.mg-timeline-section {
  background: var(--mg-rose-50);   /* ALDRIG svart bakgrund */
  padding-block: var(--mg-space-9);
  margin-block: var(--mg-space-8);
}

/* Vertikal linje: platt rose-200. Ingen gradient, ingen accentfärg */
.mg-timeline {
  position: relative;
  padding-left: 120px;
}
.mg-timeline::before {
  content: '';
  position: absolute;
  left: 88px; top: 0; bottom: 0;
  width: 1px;
  background: var(--mg-rose-200);
}

/* Diamantpunkt på linjen */
.mg-timeline-item::before {
  content: '';
  position: absolute;
  left: -6px; top: 6px;
  width: 11px; height: 11px;
  background: var(--mg-rose-200);
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
}

/* Highlight-punkt (nuvarande år) */
.mg-timeline-item--highlight::before {
  background: var(--mg-magenta);
  width: 15px; height: 15px;
  left: -8px; top: 4px;
}

/* Årstal */
.mg-timeline-item__year {
  position: absolute;
  left: -120px; top: 0;
  width: 100px; text-align: right;
  font: 700 1rem/1 var(--mg-font-head);
  color: var(--mg-grey-300);
}
.mg-timeline-item--highlight .mg-timeline-item__year {
  color: var(--mg-magenta); font-size: 1.1rem;
}

/* Text */
.mg-timeline-item__text { font: 400 .9375rem/1.55 var(--mg-font-body); color: var(--mg-text-2); }
.mg-timeline-item--highlight .mg-timeline-item__text { color: var(--mg-black); font-weight: 500; }
```

---

## 29. Footer

Tre kolumner, ljus text, magenta brand-namn.

```css
.mg-footer { padding: var(--mg-space-7) 0; }
.mg-footer__inner {
  display: grid; grid-template-columns: 1fr 1fr 1fr;
  gap: var(--mg-space-6);
}
.mg-footer__col { font-size: .8125rem; line-height: 1.7; color: var(--mg-text-2); }
.mg-footer__brand {
  color: var(--mg-magenta);
  font: 700 .875rem/1 var(--mg-font-head);
  display: block; margin-bottom: var(--mg-space-2);
}
@media (max-width: 599px) {
  .mg-footer__inner { grid-template-columns: 1fr; gap: var(--mg-space-5); }
}
```

---

## 30. Kontaktkort och uppmaningssektion (CTA)

### Kontaktkort

Person med foto, namn, titel och kontaktuppgifter. Fotot är svartvitt och **runt** (personbilder är den enda cirkeln i systemet). Kortet är en polygon i rosagrå 100.

```css
.mg-contact-card {
  display: flex; gap: var(--mg-space-6); align-items: flex-start;
  background: var(--mg-rose-100);
  padding: var(--mg-space-7);
  clip-path: polygon(0% 3%, 4% 0%, 97% 2%, 100% 6%, 98% 94%, 94% 100%, 2% 97%, 0% 93%);
}
.mg-contact-card__photo {
  width: 120px; height: 120px; flex-shrink: 0;
  object-fit: cover;
  filter: grayscale(1) contrast(1.05);
  border-radius: 50%;                       /* personbild: runt */
}
.mg-contact-card__name  { font: 700 var(--mg-fs-h3)/1.2 var(--mg-font-head); }
.mg-contact-card__title { color: var(--mg-text-2); margin-bottom: var(--mg-space-3); }
.mg-contact-card__links { display: flex; flex-direction: column; gap: var(--mg-space-2); }
.mg-contact-card__links a { color: var(--mg-magenta); }
@media (max-width: 768px) {
  .mg-contact-card { flex-direction: column; }
  .mg-contact-card__photo { width: 80px; height: 80px; }
}
```

### CTA-sektion

Avslutar en sida med en tydlig handling. Rubrik, valfri text och **en** primärknapp.

```css
.mg-cta { padding-block: var(--mg-space-9); }
.mg-cta__inner {
  max-width: var(--mg-wide);
  margin-inline: auto;
  padding-inline: var(--mg-gutter);
  display: flex; flex-direction: column; align-items: flex-start;
  gap: var(--mg-space-6);
}
```

### Ingångskort (undersidor)

Kort som leder till sidans underliggande sidor. Rubrik, kort text och en länk med pil. Vit polygon, ingen kant, **inga löpnummer**.

```css
.mg-sub-card {
  background: var(--mg-white);
  clip-path: polygon(2% 2%, 99% 0%, 100% 95%, 97% 100%, 0% 98%);
  padding: var(--mg-space-7) var(--mg-space-6) var(--mg-space-6);
  display: flex; flex-direction: column; gap: var(--mg-space-3);
}
```

Raden av ingångskort ligger på en `--mg-rose-100`-sektion (`.mg-subpages`) så att de vita polygonerna syns.

---

## 31. Formulärkomponenter

Formulär följer samma designspråk som övriga komponenter. Inputfältets ram är en funktionell hårlinje, men inga andra raka ramar runt element, accentfärger som fill och en tydlig semantisk logik för knappar.

### Inputfält

Inputfält har en **tydlig grå border runt hela fältet** (inte bara en underkant) för att göra det tydligt att det är ett inmatningsfält. Border byter färg beroende på state.

```css
.mg-input {
  width: 100%;
  padding: 10px 13px;
  border: 1.5px solid #CCCCCC;
  background: #FAFAFA;
  font-family: var(--mg-font-body);
  font-size: 0.9rem;
  outline: none;
  color: var(--mg-black);
  transition: border-color 0.2s, background 0.2s;
  border-radius: 0; /* Aldrig rundade hörn */
}

.mg-input:focus      { border-color: var(--mg-blue); background: #fff; }
.mg-input.is-error   { border-color: var(--mg-red);  background: #fff5f5; }
.mg-input.is-success { border-color: var(--mg-green); }
.mg-input:disabled   { opacity: 0.4; cursor: not-allowed; }
```

Textarea använder exakt samma klass och stil som `input`. `resize: vertical` tillåts, `resize: horizontal` inte.

### Fältetikett

```css
.mg-field__label {
  font-family: var(--mg-font-head);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--mg-black);
  display: block;
  margin-bottom: 6px;
}
```

### Felmeddelande och bekräftelse under fält

```html
<div class="field-error">Ange en giltig e-postadress</div>
<div class="field-success">Giltig LinkedIn-profil</div>
```

```css
.field-error   { font-size: 0.75rem; color: var(--mg-red);   margin-top: 5px; font-weight: 500; }
.field-success { font-size: 0.75rem; color: var(--mg-green); margin-top: 5px; font-weight: 500; }
```

### Upload-zon (drag & drop)

Upload-zonen är ett polygon-klippt område med streckad kant. Ingen solid border — streckad kant signalerar "lägg något här".

```html
<div class="mg-upload-zone">
  <i class="mg-icon-upload"></i>
  <div class="mg-upload-zone__text">Dra och släpp din bild här</div>
  <div class="mg-upload-zone__sub">JPG, PNG eller WEBP — max 5 MB</div>
</div>
```

```css
.mg-upload-zone {
  border: 2px dashed #CCCCCC;
  padding: 2rem;
  text-align: center;
  clip-path: polygon(1% 3%, 97% 0, 100% 3%, 99% 97%, 96% 100%, 2% 99%, 0 96%);
  background: #F8F8F8;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
}
.mg-upload-zone:hover      { border-color: var(--mg-blue); background: #f0f9ff; }
.mg-upload-zone.is-drag-over { border-color: var(--mg-magenta); background: #fff0f8; }

.mg-upload-zone__text { font-family: var(--mg-font-head); font-size: 0.9rem; font-weight: 700; color: var(--mg-black); }
.mg-upload-zone__sub  { font-size: 0.75rem; color: var(--mg-grey-300); margin-top: 4px; }
```

### Semantisk knappfärg

Knappens färg ska spegla vad den gör — inte enbart var den sitter i layouten.

| Handling | Variant | Bakgrund | Text |
|----------|---------|----------|------|
| Skapa, Generera, Spara, Ladda ner | `mg-btn--primary` | `#EC008C` (magenta) | Vit |
| Återställ, Avbryt, Stäng, Rensa | `mg-btn--secondary` | `#E3D6D6` (`--mg-rose-200`) | Svart |

**Regler:**
- Aldrig fler än en `mg-btn--primary` per vy.
- Sekundärknappen placeras alltid till höger om primärknappen (eller under i staplad layout).
- Ikoner ska sitta till vänster om texten med 8px gap.

Grundstilen för `.mg-btn` finns i [Knappar](#17-knappar). I formulär och verktyg läggs bara detta till:

```css
.mg-btn { display: inline-flex; align-items: center; gap: 8px; }
.mg-btn:disabled { opacity: 0.35; cursor: not-allowed; }
```

Ikoner på knappar hämtas från Tabler Icons och ska vara 18px:

```html
<!-- Primär: skapar något -->
<button class="mg-btn mg-btn--primary">
  <i class="ti ti-sparkles"></i>Skapa bild
</button>

<!-- Sekundär: återställer -->
<button class="mg-btn mg-btn--secondary">
  <i class="ti ti-refresh"></i>Återställ
</button>
```

---

## 32. Komponentstates

Fyra grundstates gäller för alla interaktiva komponenter. Accentfärgen används alltid som fill — aldrig som border (undantag: inputfältets `border-color` byter per state).

| State | Färg | Hex | Pill-text |
|-------|------|-----|-----------|
| Fel / Error | Röd | `#E20430` | "Fel" |
| Success / Klar | Grön | `#00964F` | "Klar" |
| Laddar / Bearbetar | Blå | `#009EE3` | "Bearbetar" |
| Inaktiv / Disabled | Grå | `#AAAAAA` | "Ej tillgänglig" |
| Varning | Gul | `#FFDD00` | "Varning" (svart text) |

### Pill-etikett

Pill-etiketten används för att snabbt kommunicera state i t.ex. listor, kort eller ovanför formulärdelar.

```css
.mg-pill {
  display: inline-block;
  padding: 4px 12px;
  font-family: var(--mg-font-head);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  clip-path: polygon(6% 0, 94% 0, 100% 50%, 94% 100%, 6% 100%, 0 50%);
}
.mg-pill--error    { background: #E20430; color: #fff; }
.mg-pill--success  { background: #00964F; color: #fff; }
.mg-pill--loading  { background: #009EE3; color: #fff; }
.mg-pill--disabled { background: #AAAAAA; color: #fff; }
.mg-pill--warning  { background: #FFDD00; color: var(--mg-black); }
```

### Loading-knapp

En knapp i loading-state behåller sin primärfärg men tonas ner och spinner ersätter ikonen:

```html
<button class="mg-btn mg-btn--primary" style="opacity:0.75;cursor:wait;" disabled>
  <span class="mg-spinner mg-spinner--sm"></span>Skapar...
</button>
```

---

## 33. Feedback & notifieringar

### Toast-notifieringar

Toast visas temporärt (3–5 sek) i nedre högra hörnet, `position: fixed`, `z-index: 900`. Polygon-klipps för att följa designspråket.

```css
.mg-toast {
  padding: 14px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 280px;
  max-width: 420px;
  clip-path: polygon(0 0, 97% 0, 100% 4%, 99% 96%, 96% 100%, 2% 100%, 0 96%);
}
.mg-toast--success { background: #00964F; color: #fff; }
.mg-toast--error   { background: #E20430; color: #fff; }
.mg-toast--info    { background: #009EE3; color: #fff; }
.mg-toast--warning { background: #FFDD00; color: var(--mg-black); }

.mg-toast__title { font-family: var(--mg-font-head); font-size: 0.9rem; font-weight: 700; }
.mg-toast__msg   { font-size: 0.8rem; opacity: 0.9; margin-top: 2px; }
```

**Copyregler för toast:**
- Beskriv vad som hände, inte vad som gick fel. "Bilden kunde inte skapas" — inte "Error 500".
- Lägg till vad användaren ska göra om något gick fel: "Formatet stöds inte. Använd JPG, PNG eller WEBP."
- Inga utropstecken. Ingen "successfully"-suffix.

### Inline-feedback

Inline-feedback sitter direkt under eller bredvid det element det gäller. Aldrig som ram eller kantlinje (inte heller `border-left`). Alltid som en fylld ruta med polygonform:

```css
.mg-inline-error,
.mg-inline-info  { padding: 10px 14px; font-size: 0.85rem; font-weight: 500;
                   clip-path: polygon(0 0, 99% 2%, 100% 98%, 1% 100%); }
.mg-inline-error { background: #fff0f2; color: #E20430; }
.mg-inline-info  { background: #f0f8ff; color: #005a8a; }
```

---

## 34. Tool/app-layout

Verktyg och applikationer (t.ex. bildgeneratorer, konfiguratorer) har en annan layoutstruktur än marknadssidor. Huvudregeln är **tvåkolumns-arbetsyta**: kontrollpanel till vänster, canvas/preview till höger.

### Topbar

Topbar är mörkfärgad för att tydligt skilja den från sidans innehåll. Använd **mörk rose-grå** (`#3D2535`) — inte svart — för att hålla ihop med varumärkets rosa tonskala.

```css
.mg-app-topbar {
  background: #3D2535;
  padding: 11px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}
```

Logotypen i topbar är alltid i magenta (`#EC008C`). Sidtiteln i muted vit (`rgba(255,255,255,0.65)`).

### Kontrollpanel (sidebar)

```css
.mg-app-sidebar {
  width: 240px;
  background: var(--mg-white);
  padding: 1rem;
  overflow-y: auto;
  flex-shrink: 0;
}
```

Fält i sidebar är något kompaktare (padding 7–10px) men annars identiska med övriga formulärfält.

### Canvas-yta

Canvas-ytan visar det som genereras eller redigeras. Schackbräde-bakgrund markerar transparens/tom yta:

```css
.mg-app-canvas {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #e8e8e8;
  position: relative;
  overflow: hidden;
}
/* Schackbräde-bakgrund */
.mg-app-canvas__bg {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--mg-rose-200) 1px, transparent 1px),
    linear-gradient(90deg, var(--mg-rose-200) 1px, transparent 1px);
  background-size: 20px 20px;
}
```

### Mobil-anpassning för app-layout

På skärmar under 768px bryts tvåkolumns-layouten vertikalt: canvas ovanför, kontrollpanel under.

```css
@media (max-width: 768px) {
  .mg-app-body { flex-direction: column; }
  .mg-app-sidebar { width: 100%; }
}
```

---

## 35. Loading-indikatorer

### Spinner

Spinner används för kort obestämd väntan (< 10 sek). Magenta är default, blå för systemoperationer.

```css
.mg-spinner {
  display: inline-block;
  border-radius: 50%;
  border: 3px solid var(--mg-rose-200);
  border-top-color: var(--mg-magenta);
  animation: mg-spin 0.9s linear infinite;
}
.mg-spinner--md { width: 36px; height: 36px; }
.mg-spinner--sm { width: 14px; height: 14px; border-width: 2px; }
.mg-spinner--lg { width: 48px; height: 48px; border-width: 4px; }
.mg-spinner--blue { border-top-color: var(--mg-blue); }

@keyframes mg-spin { to { transform: rotate(360deg); } }
```

### Progress bar

Progress bar används när stegens antal är känt. Klipps med polygon för att följa designspråket.

```css
.mg-progress {
  background: var(--mg-rose-200);
  height: 6px;
  clip-path: polygon(0 0, 96% 0, 100% 50%, 96% 100%, 0 100%);
  overflow: hidden;
}
.mg-progress__fill {
  height: 100%;
  background: var(--mg-magenta);
  clip-path: polygon(0 0, 96% 0, 100% 50%, 96% 100%, 0 100%);
  transition: width 0.4s ease;
}
.mg-progress__fill--done { background: var(--mg-green); }
```

### Skeleton screen

Skeleton screens används vid sidladdning eller när innehåll hämtas asynkront. Ersätter tomma ytor med animerade grå platshållare.

```css
.mg-skeleton {
  background: var(--mg-rose-200);
  position: relative;
  overflow: hidden;
  border-radius: 2px;
}
.mg-skeleton::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255,255,255,0.6) 50%,
    transparent 100%
  );
  animation: mg-shimmer 1.5s infinite;
}
@keyframes mg-shimmer {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}
```

### Loading overlay

Overlay blockerar canvas/arbetsyta under längre operationer. Bakgrunden matchar topbar-färgen:

```css
.mg-loading-overlay {
  position: absolute;
  inset: 0;
  background: rgba(61, 37, 53, 0.92);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 1rem;
  z-index: 50;
  clip-path: polygon(0 0, 97% 0, 100% 3%, 100% 97%, 97% 100%, 3% 100%, 0 97%, 0 3%);
}
.mg-loading-overlay__text {
  font-family: var(--mg-font-head);
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.04em;
}
```

---

## 36. Strapi — redaktörsvänliga komponenter

Det här kapitlet beskriver hur designsystemets komponenter blir **byggstenar i Strapi** (v5), så att en redaktör kan skapa och ändra sidor med så lite arbete som möjligt och ändå aldrig kan bryta formspråket. Kapitlet är ramverksneutralt: det beskriver data och renderingsregler, inte React, Astro eller Next.

**Texter skrivs i Markdown.** Alla längre texter är Strapis fälttyp `richtext` (Markdown-editorn). Det är det enklaste för redaktören: ett fält, ingen verktygsrad att fela i, och designen tar hand om utseendet. Se [36.4](#364-markdown--så-skrivs-texterna).

### 36.1 Fem principer för redaktörsvänlighet

1. **Bara rubriken är obligatorisk.** En sida eller ett block ska gå att publicera med enbart en rubrik. Allt annat är valfritt och lägger till innehåll.
2. **Text är Markdown, resten är fält.** Löpande text skrivs som Markdown i ett enda fält. Visuella element (kort, steg, case, bild på platta) är block med några få enkla fält.
3. **Designen bestämmer, redaktören fyller i.** Redaktören väljer aldrig polygonform, färg, avstånd, rubriknivå eller bildbehandling.
4. **Tomt fält = elementet försvinner.** Frontenden renderar bara det som är ifyllt, och avstånden kollapsar. Inga tomma etiketter, inga hål.
5. **Det som kan härledas ska inte matas in.** Brödsmula, undermenyer, sidospår, "se alla"-länkar, datum, stegfärger och nummer härleds ur strukturen.

### 36.2 Det redaktören väljer — och inte väljer

| Redaktören **väljer** | Designen **bestämmer** |
|---|---|
| Rubrik, Markdown-text, bild, länk | Polygonform (A/B/C växlar automatiskt efter position) |
| Sektionsbakgrund: vit eller rosa (bara där det är relevant) | Färger, typsnitt, storlekar, rubriknivå (H1/H2/H3) |
| Bildsida: vänster eller höger (bara i `split`) | Svartvitt foto, bildbeskärning, bildproportion |
| Ikon från en fast lista (bara i kort) | Ikonstorlek och placering |
| Ordning på block och poster (dra och släpp) | Avstånd mellan block, ingen tom luft |
| Vilka sidor som finns i menyn | Dropdown, sidospår, mobilmeny, brödsmula |

Rosa sektionsbakgrund får aldrig ligga bredvid en annan rosa. Frontenden tvingar vit om föregående block redan är rosa.

### 36.3 Innehållstyper

| Typ | Strapi-typ | Obligatoriskt | Valfritt |
|---|---|---|---|
| **Page** (Sida, även startsidan med slug `start`) | Collection | `title` | `hero`, `body`, `blocks`, `seo` |
| **Case** | Collection | `title` | `client`, `summary`, `image`, `tags`, `facts`, `body`, `seo` |
| **Article** (Artikel) | Collection | `title` | `ingress`, `image`, `author`, `tags`, `body`, `seo` |
| **Person** | Collection | `name` | `role`, `photo`, `email`, `phone` |
| **Tag** | Collection | `name` | |
| **Navigation** | Single | `items` (kan vara tom) | |
| **Site settings** | Single | `orgName` | `address`, `orgNo`, `vat`, `phone`, `email`, `featuredLink`, `defaultSeoImage` |

Alla använder Draft & Publish. Språk: bara svenska, så i18n-pluginet är avstängt. Startsidan är en vanlig Page (slug `start`); ingen egen typ behövs.

#### Den minsta möjliga sidan

```json
{ "title": "Om oss" }
```

Det är en giltig, publicerbar sida. Frontenden renderar brödsmula (härledd ur Navigation), rubriken som H1 och sidfoten.

#### En enkel textsida (bara Markdown)

```json
{
  "title": "Om oss",
  "body": "Vi har levererat värde i 30 år.\n\n## Magello i korthet\n\nVi utgår från vårt kontor i Stockholm …"
}
```

De flesta sidor behöver inte mer än så. Blocken nedan lägger man till när sidan ska ha något visuellt.

#### En rik sida

```json
{
  "title": "Hållbara digitala tjänster",
  "hero": {
    "kicker": "Expertisområde",
    "subtitle": "Vi bygger digitala lösningar som löser era faktiska problem.",
    "image": { "id": 12 },
    "primaryCta":   { "label": "Prata med oss",   "page": { "slug": "kontakt" } },
    "secondaryCta": { "label": "Vad vi erbjuder", "url": "#specialistomraden" }
  },
  "body": "Magello är engagerade i att …",
  "blocks": [
    { "__component": "blocks.card-grid", "head": { "label": "Specialistområden", "heading": "Vad vi erbjuder" }, "items": [ … ] },
    { "__component": "blocks.steps", "items": [ { "title": "Uppstart" }, { "title": "Utveckling" }, { "title": "Förvaltning" } ] },
    { "__component": "blocks.case-list" },
    { "__component": "blocks.contact", "person": { "id": 3 } }
  ]
}
```

### 36.4 Markdown — så skrivs texterna

Alla Markdown-fält renderas till HTML och läggs i en `<div class="mg-prose">`. Redaktören skriver ren Markdown. **Inga klasser, ingen HTML.** Bibliotekets `.mg-prose` formger allt. Facit för hur varje element ser ut: [`styleguide/markdown.html`](../styleguide/markdown.html).

| Redaktören skriver | Renderas som |
|---|---|
| `## Rubrik` | H2 (svart i löpande text) |
| `### Underrubrik` | H3 |
| Vanlig text | Stycke, 18 px, `--mg-text-2` |
| `**fet**`, `*kursiv*` | Fet (svart, 700), kursiv |
| `[text](url)` | Magenta länk |
| `- punkt` / `1. punkt` | Punktlista / numrerad lista |
| `> citat` | Magello-citat (`citation.svg`, Condensed 500) |
| `\| tabell \|` (GFM) | Tabell med rosa rubrikrad och bandning |
| `---` | Extra luft (ingen linje) |
| `` `kod` `` | Liten kodmarkering (för tekniska texter) |

**Inte tillåtet i Markdown:**

- `# Rubrik 1`. Sidtiteln är sidans H1. Frontenden ska nedgradera eller ignorera `#` i texten.
- Bilder (`![]()`). Bilder läggs med blocken *Bildplatta*, *Bild och text* eller *Galleri*, så att de alltid blir svartvita och polygonformade.
- Rå HTML. Rendera med `html: false` och sanitera ändå.
- Kodblock (` ``` `), om inte sajten är teknisk.

Rendera Markdown med en standardparser (`marked` eller `markdown-it`) med tabeller påslagna. Externa länkar får `rel="noopener"`.

### 36.5 Delade komponenter (`shared`)

| Komponent | Fält | Obligatoriskt |
|---|---|---|
| `shared.link` | `label`, `page` (relation till Page), `url` (sträng) | `label`, samt `page` **eller** `url` |
| `shared.section-head` | `label` (kicker), `heading`, `intro` (text) | inget. Hela huvudet utelämnas om alla är tomma |
| `shared.hero` | `kicker`, `title` (åsidosätter sidtiteln), `subtitle`, `image`, `primaryCta`, `secondaryCta` | inget. Sidtiteln används som H1 |
| `shared.seo` | `metaTitle`, `metaDescription`, `ogImage` | inget. Standard: sidtiteln, ingress, hero-bild |

Regel för `shared.link`: välj hellre `page` (relation) än `url` för interna länkar, så att länken inte går sönder om sidans slug ändras. `url` används för externa länkar och ankare (`#kontakt`).

### 36.6 Block (dynamic zone `blocks`)

En Page har fältet `body` (Markdown) och därefter `blocks`, en **dynamic zone** där redaktören lägger till block och drar dem i ordning. Alla block har ett valfritt `head` (`shared.section-head`) där det är relevant.

| Block (`blocks.*`) | Används till | Obligatoriskt | Valfritt | Designen bestämmer | Renderas som |
|---|---|---|---|---|---|
| `text` | Löpande text mellan andra block | `body` (Markdown) | | Allt i avsnitt 36.4 | `.mg-prose` |
| `image-plate` | Stor bild med text på vit platta | `image` | `title`, `text`, `cta` | Svartvitt, platta med åtta hörn | `.mg-img-block` |
| `split` | Bild bredvid text | `title` | `text`, `image`, `cta`, `imageSide` | Polygonbild, hover öppnar formen | `.mg-expertis-split` |
| `card-grid` | Rutnät av kort (även värdeord, erbjudanden) | `items` (minst 1) | `head`, `tone` | Kortvariant efter innehåll (se nedan) | `.mg-card-grid` + `.mg-card` / `.mg-offer-card` |
| `steps` | Process eller faser | `items` (minst 2) | `head`, `labelPrefix`, `closing` | Färger, chevron-form, magenta sista steg, "Steg n" | `.mg-steps` |
| `case-list` | Utvalda uppdrag | | `head`, `cases`, `tag`, `limit` | Rutnät, svartvita bilder, "Se alla" | `.mg-case-card` |
| `contact` | Kontaktperson | `person` | `head` | Rund svartvit bild, rosa polygon | `.mg-contact-card` |
| `cta` | Avslutande uppmaning | `title` | `text`, `link` | En primärknapp | `.mg-cta` |
| `infoblock` | Rosa faktaruta i textflödet | `body` (Markdown) | `label` | Efter varandra i full bredd | `.mg-infoblock` |
| `facts` | Siffror och nyckeltal | `items` | `label` | Rad inne i infoblock | `.mg-sidebar__facts-row` |
| `timeline` | Historik | `items` | `head` | Sista posten markeras automatiskt | `.mg-timeline-section` |
| `gallery` | 1–3 bilder | `images` | `head` | Polygon A/B/C växlar | `.mg-poly-grid` |
| `subpages` | Kort till underliggande sidor | | `head` | **Hämtas automatiskt ur Navigation** | `.mg-subpages` |

Det som **inte** är block, eftersom Markdown räcker: citat (`>`), tabeller, punktlistor, rubriker och vanliga stycken.

#### Kortvarianter i `card-grid` (formen följer innehållet)

| Posten har … | Kortet blir … |
|---|---|
| `image` | Bildkort med svartvit bild överst (`.mg-card .mg-card--image`) |
| `icon` (ingen bild) | Erbjudandekort med ikon, rosa polygon (`.mg-offer-card`) |
| varken bild eller ikon | Textkort med vit polygon (`.mg-card .mg-card--text`) |

Poster i `card-grid`: `title` (obligatoriskt), `text` (kort ren text), `image`, `icon` (enum), `link`. Inget löpnummer renderas.

#### Stegfärger i `steps` — automatiskt

Alla steg utom det sista tar färg i ordningen **blå → orange → röd → gul → grön** (börjar om vid behov). **Sista steget är alltid magenta.** Redaktören anger inget.

| Antal steg | Färger |
|---|---|
| 2 | blå, magenta |
| 3 | blå, orange, magenta |
| 4 | blå, orange, röd, magenta |
| 6 | blå, orange, röd, gul, grön, magenta |

`labelPrefix` (till exempel "Fas" eller "Steg") ger "Fas 1", "Fas 2" automatiskt. Utelämnas den visas ingen etikett.

#### Ikonlistan (`icon`)

Ikoner väljs ur en **fast uppsättning** (enum), inte som fritt uppladdade filer, så att ikonerna alltid har rätt formspråk och färg: `nodes`, `markup`, `speak-bouble`, `timer`, `thumbs-up`, `rocket`, `light`, `arrow-up-right`, `cloud-arrow`, samt Magellos värdeord `personliga`, `trygga`, `kommunikativa`, `lärande`. Lägger du till en ikon uppdaterar en utvecklare enumet.

### 36.7 Navigation, brödsmula och sidospår — noll arbete för redaktören

`Navigation` är en single type med högst två nivåer:

```json
{
  "items": [
    { "label": "Vår expertis", "page": { "slug": "digitala-tjanster" },
      "children": [ { "label": "Case", "page": { "slug": "case" } } ] },
    { "label": "Om oss", "page": { "slug": "om-oss" } }
  ]
}
```

Från den här enda strukturen genererar frontenden huvudmenyn med dropdown, sidospåret med undermenyer, hamburgermenyn med accordion, brödsmulan på varje sida (Hem / föräldern / sidan), blocket `subpages` och aktiv-markeringen (`is-active`). Redaktören lägger bara till en sida i Navigation och drar den på plats. "Lediga jobb" och andra utvalda länkar ligger i `Site settings.featuredLink`.

### 36.8 Bilder (Media Library)

- Redaktören laddar upp ett vanligt färgfoto. Svartvitt (`grayscale(1) contrast(1.05)`) och polygonbeskärning läggs på av CSS.
- **Alt-text:** fyll `alternativeText` i mediabiblioteket. Saknas den renderas `alt=""` (dekorativ). Beskriv vad bilden visar.
- Använd Strapis genererade storlekar (`thumbnail`, `small`, `medium`, `large`) i `srcset`.
- Rekommenderat: minst 1600 px bred för hero och bildplatta. Bilder renderas som `<img>` med `object-fit: cover`, så ingen manuell beskärning behövs.
- Ikoner och logotyper laddas inte upp via redaktörsflödet. De ligger i frontendens `graphics/` och `logos/`.

### 36.9 Knappar och länkar

Knappen är alltid en knapp: första länken i en hero är primär (magenta), andra är sekundär (rose-200). Redaktören väljer inte knapptyp. Max en primär knapp per vy.

### 36.10 Exempel: scheman

`src/components/blocks/text.json`:

```json
{
  "collectionName": "components_blocks_texts",
  "info": { "displayName": "Text", "icon": "align-left", "description": "Löpande text. Skriv i Markdown." },
  "attributes": {
    "body": { "type": "richtext", "required": true }
  }
}
```

`src/components/blocks/card-grid.json`:

```json
{
  "collectionName": "components_blocks_card_grids",
  "info": { "displayName": "Kortrutnät", "icon": "apps", "description": "Rutnät av kort. Fyll i en rubrik per kort, resten är valfritt." },
  "attributes": {
    "head":  { "type": "component", "repeatable": false, "component": "shared.section-head" },
    "tone":  { "type": "enumeration", "enum": ["white", "rose"], "default": "white" },
    "items": { "type": "component", "repeatable": true, "component": "blocks.card", "required": true, "min": 1 }
  }
}
```

`src/components/blocks/card.json`:

```json
{
  "collectionName": "components_blocks_cards",
  "info": { "displayName": "Kort", "icon": "layout" },
  "attributes": {
    "title": { "type": "string", "required": true, "maxLength": 60 },
    "text":  { "type": "text", "maxLength": 240 },
    "image": { "type": "media", "multiple": false, "allowedTypes": ["images"] },
    "icon":  { "type": "enumeration",
               "enum": ["nodes","markup","speak-bouble","timer","thumbs-up","rocket","light","arrow-up-right","cloud-arrow","personliga","trygga","kommunikativa","lärande"] },
    "link":  { "type": "component", "repeatable": false, "component": "shared.link" }
  }
}
```

`src/api/page/content-types/page/schema.json` (utdrag):

```json
{
  "kind": "collectionType",
  "collectionName": "pages",
  "info": { "singularName": "page", "pluralName": "pages", "displayName": "Sida" },
  "options": { "draftAndPublish": true },
  "pluginOptions": { "i18n": { "localized": false } },
  "attributes": {
    "title":  { "type": "string", "required": true, "maxLength": 80 },
    "slug":   { "type": "uid", "targetField": "title", "required": true },
    "hero":   { "type": "component", "repeatable": false, "component": "shared.hero" },
    "body":   { "type": "richtext" },
    "blocks": {
      "type": "dynamiczone",
      "components": [
        "blocks.text", "blocks.image-plate", "blocks.split", "blocks.card-grid",
        "blocks.steps", "blocks.case-list", "blocks.contact", "blocks.cta",
        "blocks.infoblock", "blocks.facts", "blocks.timeline", "blocks.gallery", "blocks.subpages"
      ]
    },
    "seo": { "type": "component", "repeatable": false, "component": "shared.seo" }
  }
}
```

Bara `title` och `slug` (som genereras av titeln) är `required`. Det är kärnan i "minst möjligt".

### 36.11 Renderingsregler för frontenden

1. **Tomt = utelämnat.** Rendera inget element för ett tomt fält, och låt inget avstånd stå kvar.
2. **Rubriknivå härleds.** Sidtitel → H1. Blockets `heading` → H2. Kortrubriker → H3. Markdown `##` → H2, `###` → H3. Redaktören väljer aldrig nivå.
3. **Polygonvariant växlar deterministiskt** efter position (`index % 3` → A/B/C), inte slumpat, så att serverrenderat och klientrenderat blir lika.
4. **Svartvitt och polygon läggs på av CSS.** Rendera `<img>` med komponentens klass, inga inline-stilar.
5. **Aldrig två rosa sektioner bredvid varandra.** Tvinga vit om föregående sektion är rosa.
6. **Max en primärknapp per vy.** Om flera `cta` finns på en sida: första blir primär, övriga sekundär.
7. **Brödsmula, aktiv länk och meny kommer från Navigation**, inte från block.
8. **Layout följer innehåll.** Bild finns → bildlayout. Annars textlayout.
9. **Spacing mellan block** är alltid sektionens `padding-block`. Redaktören kan inte lägga till egen luft.
10. **Markdown renderas till `.mg-prose`** (avsnitt 36.4). Sanitera alltid.
11. **Förhandsvisning:** konfigurera Strapis Preview så att utkast öppnas i frontenden med samma komponenter.
12. **Typografiprofil:** startsida och ingångssidor använder standardprofilen. Artiklar, case och textsidor sätter `class="mg-type-editorial"` på `<body>` ([avsnitt 9](#9-typografi--principer-och-skala)).

### 36.12 Redigeringsupplevelsen i Strapi-admin

- **Fältbeskrivningar på svenska** för varje fält ("Visas som liten rosa etikett ovanför rubriken").
- **Teckengränser** (`maxLength`) som hindrar rubriker från att bryta layouten: titel 80, undertitel 160, korttitel 60, korttext 240, case-sammanfattning 160.
- **Namnge block på svenska** och i den ordning de oftast används: Text, Bildplatta, Kortrutnät, Process, Case, Kontakt, Uppmaning …
- **Begränsa blocklistan per innehållstyp.** Case och Article behöver bara `body` (Markdown) och eventuellt `facts`.
- **Standardvärden:** `tone: white`, `limit: 4`.
- **Roller:** redaktörsrollen har bara Content Manager och Media Library. Content-Type Builder och inställningar är endast för utvecklare.
- **Utkast och publicering** (Draft & Publish) på alla innehållstyper, med preview-länk i admin.
- **Konfigurera listvyn** så att `title`, `slug` och `updatedAt` syns.
- **Ge redaktörerna ett Markdown-fusklapp:** `styleguide/markdown.html` visar exakt vad varje tecken blir. Länka den i adminpanelen.
- **Dokumentera "första sidan" i 3 steg:** skapa sida, skriv rubrik, publicera. Allt annat är tillägg.

### 36.13 Vad som inte blir en redaktörskomponent

| Element | Varför inte | Var det bor |
|---|---|---|
| Header, sidospår, mobilmeny, dropdown | Struktur, inte innehåll | Kod, matas av `Navigation` |
| Footer | Samma på alla sidor | Kod, matas av `Site settings` |
| Brödsmula | Härleds | Kod |
| Logotyper, ikonbibliotek | Varumärkestillgångar | Kod (`logos/`, `graphics/`) |
| Formulär och verktyg | Funktion, inte innehåll | Kod |
| Toast, spinner, progressbar, states | Gränssnitt | Kod |
| Färgprover, typografiprover | Dokumentation | Styleguiden (`styleguide/`) |
| Filterflikar för case | Härleds ur `Tag` | Kod |
| Citat, tabeller, listor | Räcker som Markdown | `body` |

### 36.14 Så bygger du ett nytt block i Strapi

1. Finns det en befintlig komponent som nästan passar? Utöka den med ett **valfritt** fält i stället för att skapa en ny.
2. Räcker Markdown? Då behövs inget block.
3. Skriv fältlistan. Markera **det enda** obligatoriska fältet (oftast en rubrik eller bild). Allt annat valfritt.
4. Kan något härledas? Då tas fältet bort (färg, nummer, länkar, ordning).
5. Finns det ett designval redaktören måste göra? Håll det till `tone` (vit/rosa) eller `imageSide`.
6. Sätt `maxLength` så att innehållet inte kan spränga komponenten. Skriv ett svenskt `description`.
7. Implementera renderingen enligt [renderingsreglerna](#3611-renderingsregler-för-frontenden) med komponentens CSS från `styleguide/css/magello.css`.
8. Lägg till blocket i `blocks`-listan där det ska finnas.
9. Testa med **bara rubriken ifylld**, och med alla fält ifyllda. Båda ska se ut som Magello.

### 36.15 Kartläggning: referenssajtens komponenter → Strapi

| Referenssajtens komponent | Strapi |
|---|---|
| Hero med bild och vit platta (startsida) | `Page.hero` med `image` (slug `start`) |
| Ingångssidans hero (`mg-ingang-*`) | `Page.hero` |
| Sidtitel / DocTitle (`mg-page-title`) | `Page.hero` med `subtitle` (rekommendation: använd samma hero) |
| Bildsektion (`mg-img-block`) | `blocks.image-plate` |
| Expertis-split (`mg-expertis-split`) | `blocks.split` |
| Text-, bild- och ikonkort, värdeord | `blocks.card-grid` |
| Case-rutnät och filterflikar | `blocks.case-list` (+ `Tag`) |
| Processteg (`mg-steps`) | `blocks.steps` |
| Pull-quote | `> citat` i Markdown |
| Infoblock | `blocks.infoblock` |
| "Magello i siffror" | `blocks.facts` |
| Tidslinje | `blocks.timeline` |
| Tabell | Markdown-tabell |
| Bildgalleri (`mg-poly-grid`) | `blocks.gallery` |
| Kontaktkort | `blocks.contact` → `Person` |
| Ingångskort till undersidor | `blocks.subpages` (automatiskt) |
| CTA-sektion | `blocks.cta` |
| Löpande text | `Page.body`, `blocks.text` (Markdown) |
| Artikelsida (`mg-article-*`) | `Article` |
| Casesida (`mg-case-*`) | `Case` |
| Footer | `Site settings` |
---

## 37. Logotyper & artefakter

### Fullständig logotyp (horisontell ordlogotyp)

Fil: `/logos/magello-magenta.svg`
Inline SVG: `viewBox="0 0 1298 333"`, magenta fill `#EC008C`.
Används i header/nav, höjd 38px. I mobilmeny, höjd 32px.

I nav-HTML:
```html
<a class="mg-nav__logo" href="/" aria-label="Magello">
  <svg viewBox="0 0 1298 333" fill="none" xmlns="http://www.w3.org/2000/svg">
    <title>Magello</title>
    <rect x="114" y="41" width="1096" height="251" fill="white"/>
    <!-- ... övriga paths i magenta #EC008C ... -->
  </svg>
</a>
```

### Ikon-logotyp (polygonsymbol)

Fil: `/logos/icon-logotype.svg`
Format: magenta oregelbunden oktogon med vit inre form.
`viewBox="0 0 351 375"`.

```xml
<svg width="351" height="375" viewBox="0 0 351 375" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M167.718 0L30.4129 36.8187L0 176.204L44.9485 333.998L241.514 374.762
           L335.437 300.467L350.867 112.209L251.354 10.7388L167.718 0Z" fill="#EC008C"/>
  <path d="M143.791 85.4722L43.6068 189.134L135.069 207.763L161.01 303.097
           L267.679 202.065L275.058 107.826L143.791 85.4722Z" fill="white"/>
</svg>
```

Används i sidospåret på undersidor: `width: 70px`.

### Vit logotyp (transparent bakgrund)

Fil: `/logos/magello-white-transparent-letters.svg`
Används på mörka eller foto-bakgrunder.

### Citation-dekoration

Fil: `/graphics/citation.svg`
Används som `::before`-dekor i `.mg-pullquote`. **Aldrig med opacity.**

---

## 38. Fil- och katalogstruktur

```
design-guidelines/
├── README.md
├── AGENTS.md                     ← Instruktioner för AI-agenter (CLAUDE.md pekar hit)
├── DECISIONS.md                  ← Beslutslogg
├── docs/
│   ├── design-language.md        ← Designspråket i ord (alla medier)
│   ├── design-guidelines-web.md  ← Den här filen (webb)
│   └── processteg.md
├── tokens/
│   └── tokens.json               ← Maskinläsbara tokens, former och regler
├── assets/
│   ├── logos/                    ← magello-magenta.svg, icon-logotype.svg, vit logotyp
│   ├── graphics/                 ← Ikoner, citation.svg, värdeord/
│   ├── images/black-and-white/   ← Svartvita foton (urval)
│   ├── shapes/                   ← SVG-former genererade ur tokens.json
│   └── templates/                ← Word- och PowerPoint-mallar och howto-dokument
├── styleguide/                   ← Statisk styleguide (öppna index.html)
│   ├── css/magello.css           ← ALL CSS (tokens, bas, komponenter). Kopiera rakt av
│   ├── css/styleguide.css        ← Bara dokumentationselement för styleguiden
│   ├── js/magello.js             ← ALL JS (header, sidospår, mobilmeny, dropdown). Kopiera rakt av
│   ├── img/                      ← Skärmdumpar av navigationens lägen
│   └── index.html, farg.html, form.html, typografi.html, bilder-ikoner.html,
│       avstand-rorelse.html, komponenter.html, sektioner.html,
│       formular-feedback.html, navigation.html, markdown.html
└── tools/                        ← Byggscript: sidor, SVG-former, navigationsbilder
```

Styleguiden genereras av `tools/build_styleguide.py` ur sidmodulerna i `tools/pages/`. Header, sidospår, mobilmeny och footer skrivs en gång (i `build_styleguide.py`) och blir identisk markup på alla sidor. `magello.css` hänvisar till `../graphics/citation.svg`; styleguiden åsidosätter sökvägen i `styleguide.css` eftersom grafiken ligger i `assets/graphics/`.

### Ett projekt som använder designen

Kopiera `styleguide/css/magello.css`, `styleguide/js/magello.js`, `assets/logos/`, `assets/graphics/` och de foton du behöver in i projektet. Behåll `graphics/` bredvid `css/`, eller ändra sökvägen i den enda `url('../graphics/citation.svg')` i `magello.css`. Header, mobilmeny, sidospår och footer är identisk markup på alla sidor: i ett riktigt projekt hör den hemma i en layoutkomponent.

---

## 39. Checklista för ny sida

### Grund
- [ ] `lang="sv"` på `<html>`, `<meta name="viewport">`
- [ ] Google Fonts: Roboto + Roboto Condensed
- [ ] `css/magello.css` och `js/magello.js` kopierade oförändrade och länkade (CSS före projektets egen CSS)
- [ ] Typografiprofil vald på `<body>` (standard, `mg-type-editorial` eller `mg-type-showcase`)
- [ ] **Alla** `var(--mg-…)` som projektets egen CSS använder är definierade (kör token-kontrollen i avsnitt 4)

### Layout
- [ ] Innehållet använder `.mg-wrap` (1280 px, gutter 20/40 px, högermarginal `--mg-gutter-end`)
- [ ] Inget innehåll hamnar under sidospåret i 769–1630 px
- [ ] Logotyp och innehåll delar vänsterkant (mät med skriptet i avsnitt 11)
- [ ] Brödsmulan ligger på 156 px från sidtopp på alla undersidor
- [ ] Inga högerställda informationsrutor. Infoblock ligger efter varandra i full bredd
- [ ] Inga löpnummer på kort och listor

### Navigation
- [ ] Header-typ: **startsida** → `.mg-page-header` (sticky, tröskel 8 px) | **undersida** → `.mg-page-header.mg-page-header--rotate` (fixed, rotation + sidospår, tröskel 80 px)
- [ ] Hamburgerknapp och mobilmeny-drawer på alla sidor, `@media (max-width: 768px)`
- [ ] Mobil-override för rotation (`transform-origin: 50% 0 !important`) och sidospår dolt
- [ ] `pointer-events: none` på `.mg-page-header.is-scrolled`
- [ ] Dropdown och sidospår fungerar (kommer med `magello.js`: `.is-open`, 220 ms timer, ingen lucka, hover och klick på huvudlänk i sidospåret)

### Visuellt
- [ ] Alla foton: `filter: grayscale(1) contrast(1.05)` + `clip-path: polygon()`
- [ ] Inga accentfärger som kantlinjer, understrykningar eller streck
- [ ] Inga gradienter, skuggor (utom dropdown), rundade hörn (utom personbilder) eller mörkt läge
- [ ] Ikoner utan opacity och utan filter
- [ ] Tidslinje: `background: var(--mg-rose-50)`, platt `--mg-rose-200`-linje
- [ ] Pullquote `::before`: ingen opacity på `citation.svg`
- [ ] Knappar: primär magenta, sekundär `--mg-rose-200`, ingen outline, max en primär per vy
- [ ] `prefers-reduced-motion: reduce` inaktiverar transitions och animationer

### Innehåll och tillgänglighet
- [ ] H1 finns en gång per sida. H2 på sektionsnivå är magenta
- [ ] Alt-text på alla meningsbärande bilder (`alt=""` på dekorativa)
- [ ] Kontrast ≥ 4,5:1 för brödtext, synlig fokusmarkering
- [ ] Tangentbord når hela sidan (tabb, Enter, Escape)
- [ ] Testat i 375, 768, 1280 och 1842 px
---

## 40. Snabbreferens — Skapa nya element

### Ny sektion

Fråga: Vad är bakgrunden?
- Vit → `padding-block: var(--mg-space-8)` — ingen clip-path nödvändig
- Rosagrå → lägg till `clip-path: polygon(0% 3%, 62% 0%, 100% 2%, 100% 97%, 38% 100%, 0% 98%)` och `background: var(--mg-rose-100)`
- Aldrig: svart, mörkgrå eller en stark accentfärg som sektionsbakgrund

### Ny "låda" / kort / ruta

```css
.mg-[nytt-namn] {
  background: var(--mg-rose-50);           /* eller white / rose-100 */
  padding: var(--mg-space-5) var(--mg-space-6);
  clip-path: polygon(0% 0%, 100% 2%, 98% 98%, 0% 100%); /* ← alltid polygon */
}
```

Hover (om interaktiv):
```css
.mg-[nytt-namn]:hover {
  background: var(--mg-rose-100);          /* ett steg mörkare */
  clip-path: polygon(0% 1%, 99% 0%, 100% 99%, 1% 100%); /* lite mer rektangulär */
  transition: clip-path .35s ease, background .35s ease;
}
```

### Ny rubrik i en komponent

```css
.mg-[block]__title {
  font: 700 var(--mg-fs-h4)/1.2 var(--mg-font-head); /* Condensed alltid */
  color: var(--mg-black);                             /* svart om i innehållsflöde */
  margin-bottom: var(--mg-space-3);
}
```

Om det är ett sektionshuvud (utanför flödet):
```css
.mg-[block]__heading { color: var(--mg-magenta); }   /* magenta på sektionsnivå */
```

### Ny bild

```css
.mg-[block]__img {
  filter: grayscale(1) contrast(1.05);     /* alltid svartvitt */
  clip-path: polygon(0% 0%, 97% 2%, 100% 98%, 2% 100%); /* alltid polygon */
  object-fit: cover;
}
```

### Ny etikett/badge

```css
.mg-[block]__label {
  font: 700 .6875rem/1 var(--mg-font-head);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mg-magenta);
  display: block;
  margin-bottom: var(--mg-space-3);
}
```

### Ny ikon i en komponent

```css
.mg-[block]__icon {
  width: 40px; height: 40px;
  flex-shrink: 0;
}
.mg-[block]__icon img {
  width: 100%; height: 100%;
  object-fit: contain;
  /* ALDRIG: opacity, filter, grayscale på ikoner */
}
```

### Ny länk/knapp-liknande element (inte en knapp)

```css
.mg-[block]__link {
  font: 500 .8125rem/1 var(--mg-font-head);
  color: var(--mg-magenta);
  text-decoration: none;
  letter-spacing: .04em;
}
.mg-[block]__link:hover { text-decoration: underline; }
```

### Kontrollista för varje nytt element

Innan du är klar, svara ja på alla:

- [ ] Har alla synliga kanter `clip-path: polygon()` (ingen rak rektangel)?
- [ ] Används accentfärger (magenta etc.) bara som fyllnad/text — inte som kantlinjer?
- [ ] Använder rubriker `var(--mg-font-head)` (Condensed)?
- [ ] Använder löptext `var(--mg-font-body)` (Roboto)?
- [ ] Är löptextens färg `var(--mg-text-2)` (#4C4A4A) — inte ren svart?
- [ ] Är foton i svartvitt med `filter: grayscale(1)`?
- [ ] Är ikoner i fullstyrka (ingen opacity)?
- [ ] Har hover-effekter `transition` med mjuk kurva (`ease` eller cubic-bezier)?
- [ ] Är komponenten självständig — fungerar den utan beroende av omgivningen?
- [ ] Ligger innehållet på samma vänsterkant som logotypen?
- [ ] Ligger eventuella informationsrutor efter varandra i full bredd?
- [ ] Fungerar komponenten med bara rubriken ifylld, om den ska redigeras i Strapi?

---

## 41. Kända avvikelser i biblioteket

Det här dokumentet beskriver **målbilden**. Biblioteket (`styleguide/css/magello.css`) följer den i allt väsentligt, men följande kvarstående avvikelser är kända. Åtgärda dem i `magello.css` när respektive komponent ändå ska användas, eller ta ett medvetet beslut att ändra dokumentet (och notera det i `DECISIONS.md`).

| # | Avvikelse | Var i `magello.css` | Åtgärd |
|---|---|---|---|
| 1 | Tidslinjens lodräta linje är magenta med gradient | `.mg-timeline::before` | Gör linjen `--mg-rose-200`, platt. Magenta bara på markerad punkt |
| 2 | Kontaktkortets foto är kvadratiskt (`border-radius: 0`) | `.mg-contact-card__photo` | Personbilder ska vara runda. Bekräfta om kvadrat är avsiktligt |
| 3 | Dropdown-menyn har en diffus skugga | `.mg-nav__sub` | Dokumenterat undantag (lagret ligger över innehåll) |
| 4 | Case-teasers har mörka platshållare med gradient (`linear-gradient(135deg, #222, #444)`) och case-hero har reservfärg `#2a2a2a` | `.mg-case-teaser`-delen, `.mg-case-hero` | Ersätt med svartvita foton |
| 5 | Tre typografiprofiler (standard, editorial, showcase). Samma sidtyp kan hamna i två profiler | `:root`, `.mg-type-*` | Låt samma sidtyp ha samma profil. Överväg att slå ihop till en skala |
| 6 | Tre case-kortvarianter med olika utseende | `.mg-case-card`, `.mg-case-tile`, `.mg-case-teaser` | Välj en och gör övriga till modifiers |
| 7 | Erbjudande- och värdekort har polygoner som skiljer sig några procent från kortets polygon | `.mg-offer-card`, `.mg-value-card` | Låt dem använda `.mg-card`-polygonen som modifier |
| 8 | Tvåkolumnslayout med sidopanel på artikel- och caselayouterna | `.mg-article-layout`, `.mg-case-layout`, `.mg-case-sidebar` | Lägg faktarutorna som infoblock efter varandra i full bredd enligt [Artikel](#24-artikel--undersidans-layout) |
| 9 | Dokumentationselement i biblioteket (färgprover, `.mg-page-hero`, `.mg-demo-box`, `.mg-state-card` med accentkant) hör till den gamla referenssajten, inte till designsystemet | Avsnittet *DOKUMENTATION* | Flytta till `styleguide.css` eller ta bort |
| 10 | Några funktionella undantag från "inga gradienter/runda hörn": skeleton-shimmer, spinner, radioknappar, fokusring på formulärfält | `.mg-skeleton`, `.mg-spinner` m.fl. | Dokumenterade undantag. Endast funktionella element |
| 11 | Länkar i löptext är magenta (4,2 : 1 mot vitt) och klarar därmed inte AA för normal text. Understrykning är det som gör dem urskiljbara | `.mg-prose a` | Överväg en mörkare magenta för små texter eller behåll understrykningen |

Rapportera nya avvikelser här när du hittar dem.
