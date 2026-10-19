# Beslutslogg — Magellos designspråk

Här står varje designbeslut med datum och motivering, så att formspråket kan utvecklas utan att tappa bort varför saker ser ut som de gör. **Lägg nya beslut längst ned.** Ändra aldrig ett gammalt beslut i efterhand: lägg till ett nytt som ersätter det och hänvisa till det gamla.

Format: `ID · Datum · Beslut — Varför`. Beslut 1–46 är övertagna från referenssajten (okt 2026) och märkta med dess datum.

## Form, färg och bild

| ID | Datum | Beslut | Varför |
|---|---|---|---|
| D-01 | 2026-10 | Inga linjer som avgränsare. Hårlinjer i `--mg-rose-200` tillåts bara i tabeller, formulärfält och mobilmenyns listor | En linje säger att något slutar, en form säger att något börjar |
| D-02 | 2026-10 | Accentfärger används aldrig som kant, understrykning eller linje. Bara fyllnad och textfärg | Accentfärger tillhör former och ikoner |
| D-03 | 2026-10 | Alla synliga former är polygoner. Ingen kant är exakt horisontell eller vertikal. Hörn avviker 2–7 % | Formerna ska kännas handgjorda och rörliga |
| D-04 | 2026-10 | Foton är alltid svartvita (`grayscale(1) contrast(1.05)`). Ikoner aldrig | Svartvitt låter magenta och ikonerna bära färgen |
| D-05 | 2026-10 | Knappar är femhörningar. Primär = magenta, sekundär = `--mg-rose-200` (hover `--mg-rose-300`). Outline-knappen är borttagen | Outline kräver kantlinje, vilket strider mot D-01 och D-02 |
| D-06 | 2026-10 | Inga gradienter, skuggor, rundade hörn på rektanglar eller mörkt läge | Platt, avskalat formspråk |
| D-07 | 2026-10 | Undantag: dropdown-lagret får ha diffus skugga | Det ligger över innehåll och syns annars inte |
| D-08 | 2026-10 | Undantag: verktyg och appar har mörk rosagrå topbar `#3D2535` | Skiljer verktygsyta från innehåll |
| D-09 | 2026-10 | Personbilder är runda | Enda cirkeln i systemet |
| D-10 | 2026-10 | Kort har ingen box-shadow-ring | Ringen klipptes av `clip-path` och syntes bara som svaga streck |
| D-11 | 2026-10 | Citat använder `citation.svg` överallt | Artikelsidan hade ett textcitattecken |
| D-12 | 2026-10 | Bakgrundsbilder görs som `<img>` med `object-fit: cover`, inte som CSS-bakgrund via variabel | Relativa URL:er i CSS-variabler bryts när CSS-filen ligger i en undermapp. `<img>` ger alt-text |
| D-13 | 2026-10 | Inline-feedback är en fylld ruta med polygonform, inte en ruta med kant till vänster | Accentfärg som kant är förbjuden (D-02) |

## Layout och typografi

| ID | Datum | Beslut | Varför |
|---|---|---|---|
| D-14 | 2026-10 | Max innehållsbredd och navigationens bredd är 1024 px (`--mg-wide`) | Tidigare 1080. Bättre radlängd och linjerar med navigationen |
| D-15 | 2026-10 | Brödtext är 18 px (`--mg-fs-body: 1.125rem`) | Tidigare 16 px. Texter ska vara 2 px större |
| D-16 | 2026-10 | Allt innehåll delar vänsterkant med logotypen. Alla containrar använder samma bredd och gutter som navigationen | Logotypens vänsterkant är sidans fasta linje |
| D-17 | 2026-10 | Brödsmulan sitter på `--mg-header-h + --mg-space-6` (156 px) på alla undersidor. Avståndet under sätts av containern | Tidigare hoppade den mellan sidtyper |
| D-18 | 2026-10 | Inga löpnummer (01, 02, 03) på kort och listor som dekoration | Siffrorna tillförde ingen information |
| D-19 | 2026-10 | Inga högerställda informationsrutor. Infoblock ligger efter varandra i full bredd | Flytande sidorutor bröt textflödet |
| D-20 | 2026-10 | H2 på sektionsnivå är magenta, H2 inne i artikeltext svart | Sektionen markerar, flödet ska inte konkurrera |
| D-21 | 2026-10 | Alla tokens som används måste vara definierade (`--mg-space-2` till `-9`) | En saknad token gör hela deklarationen ogiltig utan felmeddelande |
| D-22 | 2026-10 | Tre typografiprofiler via klass på `<body>`: standard, `mg-type-editorial`, `mg-type-showcase` | Sidorna hade tyst olika typskalor. Skillnaderna är nu namngivna |

## Navigation

| ID | Datum | Beslut | Varför |
|---|---|---|---|
| D-23 | 2026-10 | Hamburgermeny på ≤768 px på alla sidor | Samma standardbeteende överallt |
| D-24 | 2026-10 | Startsidans header är sticky (tröskel 8 px). Undersidors header är fixed och roterar 90° vid 80 px (`mg-page-header--rotate`) | Startsidan lugn, undersidor får rörelsen |
| D-25 | 2026-10 | När headern roterat bort tar sidospåret över | Navigationen ska alltid vara nåbar |
| D-26 | 2026-10 | Dropdown styrs bara av `.is-open`, 220 ms stängningsfördröjning, ingen lucka, lyssnare på menyn, `position: fixed` placerad av JS | CSS-hover stängde menyn i luckan. Transform på headern bryter `absolute` |
| D-27 | 2026-10 | I sidospåret fäller hover och klick på huvudlänk ut undermenyn (klicket navigerar inte) | Sidospåret är kompakt. Underlänkarna är de verkliga målen |

## Komponenter och bibliotek

| ID | Datum | Beslut | Varför |
|---|---|---|---|
| D-28 | 2026-10 | Max en primär knapp per vy | Tydlig huvudhandling |
| D-29 | 2026-10 | Sista steget i en process är alltid magenta | "Klart!" signalerar slut |
| D-30 | 2026-10 | Ett kort (`.mg-card`) med modifiers `--text`, `--image`, `--compact` och rutnät `.mg-card-grid` | Tre klasser hade identisk form och yta |
| D-31 | 2026-10 | En knappdefinition. `--icon` för knappar med ikon. Gamla `mg-btn-primary` borttagen | Två knappar med olika polygon fanns parallellt |
| D-32 | 2026-10 | Namnkrockar löstes: `.mg-case-tile`, `.mg-case-teaser`, `.mg-field__label` | Samma klassnamn betydde olika komponenter |
| D-33 | 2026-10 | All CSS i `magello.css`, all JS i `magello.js`. Sidor innehåller bara markup | Tidigare dubblerades ca 20 kB CSS och 4 kB JS i varje sida. Andra projekt kopierar filerna rakt av |
| D-34 | 2026-10 | `.mg-prose` täcker Markdown-element. Texter från Strapi skrivs i Markdown (`richtext`) | Enklast möjligt för redaktören |

## Den här katalogen

| ID | Datum | Beslut | Varför |
|---|---|---|---|
| D-35 | 2026-10-19 | `tokens/tokens.json` är maskinläsbar källa för färg, typ, avstånd, rörelse, former och regler | Agenter som skapar PowerPoint, Word, SVG och bilder behöver värden, inte bara text |
| D-36 | 2026-10-19 | Formerna finns som SVG i `assets/shapes/`, genererade ur `tokens.json` | Former ska kunna importeras i Office, Figma och Illustrator |
| D-37 | 2026-10-19 | Styleguiden är statisk HTML genererad av `tools/build_styleguide.py` ur sidmoduler | Header och footer skrivs en gång. Ingen byggkedja i webbläsaren |
| D-38 | 2026-10-19 | `AGENTS.md` är agenternas ingång. `CLAUDE.md` pekar dit | En källa för instruktioner till alla agenter |
| D-39 | 2026-10-19 | `design-language.md` (tidigare `design-guidelines-general.md`) är mediaoberoende. `design-guidelines-web.md` är webb | Samma principer ska gälla Word, PowerPoint och webb |
| D-40 | 2026-10-19 | Inline-feedback i biblioteket (`.mg-inline-*`) använder fylld polygonruta i stället för `border-left` | Följer D-02 och D-13 |
| D-41 | 2026-10-19 | Word och PowerPoint utgår alltid från Magellos officiella mallar `Word-mall.dotx` och `Powerpoint-mall.potx`. Kopior ligger i `assets/templates/`, originalen på intranätet. Kopiorna ändras aldrig här utan hämtas med `tools/sync_templates.py`, och nya dokument skapas med `tools/new_office_file.py` | Mallarna har redan Magellos layouter, formatmallar, sidhuvud och former. Dokument som byggs från tomt eller från äldre exempelfiler glider isär. En källa för hur Office-dokument ser ut |
| D-42 | 2026-10-19 | Profilbilder, LinkedIn-banners och -inlägg, svartvita miljöbilder och kundlogotyper görs i bildverktyget https://linkedin-profile-image.magello.se, inte för hand | Verktyget ger samma filter, rosa ton, former och mått varje gång. Handgjorda varianter glider isär |
| D-43 | 2026-10-19 | Styleguiden publiceras på GitHub Pages (https://magello-group.github.io/design-guidelines/) vid push till `main`. Bygget fallerar om genererade filer inte är committade, och bara de foton styleguiden använder publiceras | Alla ska kunna se formspråket utan att klona repot, och det publicerade ska alltid motsvara källan. Hela fotobiblioteket är för tungt för en webbplats |
| D-44 | 2026-10-19 | Styleguiden har en sida för Word och PowerPoint (`office.html`) med två vägar: med agent (`tools/new_office_file.py`, layouter, formatmallar) och manuellt (öppna mallen, utgå från howto-dokumenten). Howto-dokumenten ligger i `assets/templates/` och synkas med mallarna. De äldre exempelfilerna, referensbilderna och bakgrundsformerna i `assets/templates/` är borttagna | En ingång för alla som gör Office-dokument, oavsett arbetssätt. Howto-dokumenten är intranätets egna instruktioner och ersätter de lösa exempelfilerna |
| D-45 | 2026-10-19 | Specialtypsnittet Kattux (Kattux Abc 20, `assets/fonts/`) får användas vid speciella tillfällen, främst i PowerPoint, för ett kort budskap i minst 28 pt, högst ett element per bild. Kompletterar hård regel 6 (bara Roboto Condensed och Roboto), som i övrigt gäller. Kattux ingår inte i `magello.css` | Typsnittet finns redan i de officiella mallarna och används vid särskilda tillfällen. Regeln om två typsnitt behöver ett tydligt, avgränsat undantag i stället för en tyst avvikelse |
| D-46 | 2026-10-19 | Mallarna och howto-dokumenten i `assets/templates/` är originalen, inte kopior från intranätet. Synkscriptet och `tools/new_office_file.py` är borttagna. Människor skapar dokument genom att dubbelklicka på mallen, och agenter byter själva innehållstyp. Ersätter delarna av D-41 och D-44 som handlar om intranätet och scripten | En källa i stället för två. Användare ska inte behöva köra kommandon, och instruktionerna ska vara så enkla som möjligt |
| D-47 | 2026-10-19 | Max-bredd för container och navigation är 1280 px (`--mg-wide`) med 40 px gutter, alltså 1200 px innehåll. Gutter 64 px på desktop är borttagen. Ersätter D-14 | 1024 px kändes smalt på vanliga skärmar (1440 och 1920 px). 1200 går jämnt att dela i 12, 6, 4, 3 och 2 kolumner, och 1280 motsvarar Tailwinds `max-w-7xl` |
| D-48 | 2026-10-19 | På sidor med sidospår (över 768 px) får containrar högermarginalen `--mg-gutter-end`, som växer så att innehållet alltid ligger 24 px från sidospåret. Vänsterkanten ändras inte | Sidospåret (192 px) låg över text och komponenter i bredder upp till ca 1630 px. Marginalen är fast, så innehållet hoppar inte när spåret visas |
| D-49 | 2026-10-19 | I hamburgerläge (≤ 768 px) ligger headern kvar efter scroll och blir lägre (72 → 56 px, logotyp 38 → 32 px) i stället för att glida bort | Navigationen ska alltid vara nåbar, även på mobil, där sidospåret saknas (jämför D-25) |
| D-50 | 2026-10-19 | `tokens/tailwind.css` är ett Tailwind v4-tema (`@theme`) genererat ur `tokens.json` med `tools/make_tailwind.py`. Komponenterna finns fortfarande bara i `magello.css` | Projekt som bygger med Tailwind ska få samma färger, avstånd och bredder som utilities, utan att magello.css skrivs om eller får ett byggsteg (D-33, D-37) |
