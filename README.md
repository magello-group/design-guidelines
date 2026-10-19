# design-guidelines

Magellos formspråk, samlat i en katalog som du kan ta med och bygga vidare på i ett nytt projekt. Underlaget är gjort för att användas av **både människor och AI-agenter** som skapar grafisk kommunikation: webb, dokument, presentationer, bilder och sociala medier.

Styleguiden är publicerad på **https://magello-group.github.io/design-guidelines/**. Lokalt öppnar du **`styleguide/index.html`** i en webbläsare för en levande styleguide med bruksanvisning per färg, form, komponent, sektion och meny.

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
| [`assets/`](assets/) | Logotyper, ikoner, svartvita foton (urval), SVG-former (`shapes/`) |
| [`assets/fonts/`](assets/fonts/) + [`styleguide/typsnitt.html`](styleguide/typsnitt.html) | Specialtypsnittet Kattux för speciella tillfällen, främst i PowerPoint: regler och installation på Mac och PC |
| [Bildverktyget](https://linkedin-profile-image.magello.se) | Profilbilder, LinkedIn-banners och -inlägg, svartvita miljöbilder och kundlogotyper för CV. Används i stället för att göra sådana bilder för hand |
| [`DECISIONS.md`](DECISIONS.md) | Beslutslogg med datum och motivering |
| [`tools/`](tools/) | Byggscript för styleguide, SVG-former, navigationsbilder och Pages-webbplatsen, |

## Kom igång

**Titta på styleguiden:**

```bash
python3 -m http.server 8000
# öppna http://localhost:8000/styleguide/
```

**Starta ett nytt projekt med Magellos formspråk:**

1. Kopiera hela katalogen till det nya projektet (eller bara de delar du behöver).
2. Webb: länka `styleguide/css/magello.css` och `styleguide/js/magello.js`, och kopiera markup från styleguide-sidorna.
3. Word och PowerPoint: utgå alltid från `assets/templates/Word-mall.dotx` och `assets/templates/Powerpoint-mall.potx`, aldrig ett tomt dokument. Se `docs/office-mallar.md`.
4. Profilbilder, LinkedIn-bilder och kundlogotyper: gör dem i [bildverktyget](https://linkedin-profile-image.magello.se).
5. Be en agent läsa `AGENTS.md` först. Den vet vilken fil som gäller för vilket uppdrag.

## Bygga om

Styleguide-sidorna genereras av Python (kräver Python 3.12 eller nyare, inga paket):

```bash
python3 tools/make_shapes.py        # SVG-former i assets/shapes/ ur tokens.json
python3 tools/build_styleguide.py   # styleguide/*.html ur tools/pages/*.py
python3 tools/make_nav_images.py    # skärmdumpar av navigationens lägen (kräver Chrome och Pillow)
```

### Publicering på GitHub Pages

Vid varje push till `main` bygger [`.github/workflows/pages.yml`](.github/workflows/pages.yml) styleguiden och publicerar den på https://magello-group.github.io/design-guidelines/. Jobbet kör `make_shapes.py` och `build_styleguide.py` och fallerar om någon genererad fil skiljer sig från den committade, så kör båda och committa resultatet innan du pushar. Sedan sätter `tools/build_site.py` ihop webbplatsen i `_site/`: styleguiden, tokens, docs, ikoner, logotyper, former, Office-mallarna som nedladdningar och de foton styleguiden använder (inte hela fotobiblioteket). Det kan också köras manuellt under Actions (*Run workflow*).

Testa lokalt:

```bash
python3 tools/build_site.py
python3 -m http.server 8000 -d _site   # öppna http://localhost:8000/
```

Första gången måste *Settings → Pages → Source* i repot vara satt till **GitHub Actions**.

### Office-mallar

Mallarna i `assets/templates/` är originalen. Ändra dem här och skriv en rad i `DECISIONS.md`. Hur de används står på [styleguide/office.html](styleguide/office.html).

Header, sidospår, mobilmeny och footer definieras en gång i `tools/build_styleguide.py`. Innehållet per sida ligger i `tools/pages/<sida>.py` och skrivs med hjälpfunktionerna i `tools/sg.py` (`block`, `demo`, `use`, `code`, `spec`).

## Utveckla formspråket

Följ avsnitt 6 i [`AGENTS.md`](AGENTS.md): härled från principerna, lägg nya komponenter som modifier, uppdatera tokens, CSS, styleguide, docs och beslutsloggen i den ordningen, och fråga innan du ändrar en hård regel.

## Ursprung

Katalogen bygger på `magello-design` (referenssajten, riktlinjerna och mallarna) och är gjord för att kunna lyftas ut och utvecklas vidare på egen hand. Fotobiblioteket här är ett urval (de nio foton som styleguiden använder). Hela biblioteket finns i `magello-design/web/images/black-and-white/`.
