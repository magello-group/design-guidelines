# design-guidelines

Magellos formspråk, samlat i en katalog som du kan ta med och bygga vidare på i ett nytt projekt. Underlaget är gjort för att användas av **både människor och AI-agenter** som skapar grafisk kommunikation: webb, dokument, presentationer, bilder och sociala medier.

Styleguiden finns på **https://magello-group.github.io/design-guidelines/**: en levande styleguide med bruksanvisning per färg, form, komponent, sektion och meny, och mallar och typsnitt att ladda ned.

## Innehåll

| Sökväg | Vad |
|---|---|
| [`AGENTS.md`](AGENTS.md) | **Börja här om du är en AI-agent.** Läsordning, hårda regler, checklista, hur formspråket utvecklas (`CLAUDE.md` pekar hit) |
| [`styleguide/`](styleguide/) | Statisk styleguide (13 sidor). Levande exempel, "Gör / Gör inte / Tänk på", markup att kopiera |
| [`styleguide/css/magello.css`](styleguide/css/magello.css) + [`styleguide/js/magello.js`](styleguide/js/magello.js) | **Det delade biblioteket**: all CSS och JS. Kopiera oförändrade till andra webbprojekt |
| [`docs/design-language.md`](docs/design-language.md) | Designspråket i ord, utan webbdetaljer. Underlag för PowerPoint, Word, PDF, bilder |
| [`docs/design-guidelines-web.md`](docs/design-guidelines-web.md) | Webbriktlinjer: frågor, nytt projekt eller omstyling, tokens, komponenter, navigation, Strapi med Markdown |
| [`tokens/tokens.json`](tokens/tokens.json) | Färg, typografi (web, tryck, presentation), avstånd, layout, rörelse, former (polygoner) och regler som maskinläsbara värden |
| [`docs/office-mallar.md`](docs/office-mallar.md) + [`styleguide/office.html`](styleguide/office.html) | Magellos officiella Word- och PowerPoint-mallar, med agent eller för hand: hur ett nytt dokument skapas, layouter, formatmallar och kända avvikelser |
| [`assets/templates/`](assets/templates/) | **Officiella mallar**: [`Powerpoint-mall.potx`](assets/templates/Powerpoint-mall.potx) och [`Word-mall.dotx`](assets/templates/Word-mall.dotx) och howto-dokumenten [`Powerpoint-mall-howto.pptx`](assets/templates/Powerpoint-mall-howto.pptx) och [`Word-mall-howto.docx`](assets/templates/Word-mall-howto.docx) |
| [`assets/`](assets/) | Logotyper, ikoner, svartvita foton, SVG-former (`shapes/`) |
| [Bildbanken](https://magello-group.github.io/design-guidelines/styleguide/bildbank.html) | Alla svartvita foton att titta på och ladda ned, och en översikt över bildverktygets tjänster |
| [`assets/fonts/`](assets/fonts/) + [`styleguide/typsnitt.html`](styleguide/typsnitt.html) | Specialtypsnittet Kattux för speciella tillfällen, främst i PowerPoint: regler och installation på Mac och PC |
| [Bildverktyget](https://linkedin-profile-image.magello.se) | Profilbilder, LinkedIn-banners och -inlägg, svartvita miljöbilder och kundlogotyper för CV. Används i stället för att göra sådana bilder för hand |
| [`DECISIONS.md`](DECISIONS.md) | Beslutslogg med datum och motivering |
| [`docs/presentation-webb.md`](docs/presentation-webb.md) + [`tools/presentation/`](tools/presentation/) | Presentationer som en agent konstruerar i webbens formspråk (spår B): raster, typografi, bildtyper, logotyper och ett bibliotek med exempel |
| [`tools/`](tools/) | Byggscript för styleguide, SVG-former, navigationsbilder och Pages-webbplatsen, |

## Kom igång

**Titta på styleguiden:** öppna https://magello-group.github.io/design-guidelines/.

**Starta ett nytt projekt med Magellos formspråk:**

1. Kopiera hela katalogen till det nya projektet (eller bara de delar du behöver).
2. Webb: länka `styleguide/css/magello.css` och `styleguide/js/magello.js`, och kopiera markup från styleguide-sidorna.
3. Word: utgå alltid från `assets/templates/Word-mall.dotx`. PowerPoint: välj spår. Använd `assets/templates/Powerpoint-mall.potx` när du själv ska kunna ändra (`docs/office-mallar.md`), eller låt en agent konstruera presentationen i webbens formspråk (`docs/presentation-webb.md`).
4. Profilbilder, LinkedIn-bilder och kundlogotyper: gör dem i [bildverktyget](https://linkedin-profile-image.magello.se).
5. Be en agent läsa `AGENTS.md` först. Den vet vilken fil som gäller för vilket uppdrag.

## Ändra och publicera

Ändra i källfilerna och pusha till `main`. GitHub Pages bygger och publicerar resten, och ingen behöver bygga något eller starta en server på sin egen dator.

| Vad du ändrar | Var |
|---|---|
| Styleguidens sidor | `tools/pages/<sida>.py` (header, sidospår, mobilmeny och footer i `tools/build_styleguide.py`) |
| Färger, typografi, avstånd, former | `tokens/tokens.json` |
| CSS och JS | `styleguide/css/magello.css`, `styleguide/js/magello.js` |
| Office-mallar | `assets/templates/` (originalen). Skriv en rad i `DECISIONS.md` |

Vid varje push till `main` kör [`.github/workflows/pages.yml`](.github/workflows/pages.yml) scripten i `tools/`, som genererar former, Tailwind-tema och styleguide-sidor, och publicerar webbplatsen på https://magello-group.github.io/design-guidelines/. Den kan också köras under Actions (*Run workflow*). Första gången måste *Settings → Pages → Source* i repot vara satt till **GitHub Actions**.

## Utveckla formspråket

Följ avsnitt 6 i [`AGENTS.md`](AGENTS.md): härled från principerna, lägg nya komponenter som modifier, uppdatera tokens, CSS, styleguide, docs och beslutsloggen i den ordningen, och fråga innan du ändrar en hård regel.

## Ursprung

Katalogen bygger på `magello-design` (referenssajten, riktlinjerna och mallarna) och är gjord för att kunna lyftas ut och utvecklas vidare på egen hand. Hela fotobiblioteket finns i `assets/images/black-and-white/` och visas i Bildbanken.
