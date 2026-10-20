# Instruktioner för AI-agenter — Magellos designspråk

Du ska skapa eller ändra grafisk kommunikation för Magello: webb, dokument, presentationer, bilder eller sociala medier. Den här katalogen är din enda källa till hur Magello ser ut. Följ den, och uppfinn inget eget.

## 1. Läs i den här ordningen

| Uppdrag | Läs |
|---|---|
| **Alla uppdrag** | `docs/design-language.md` (designspråket i ord, sju principer) |
| **Webb, UI, Strapi** | `docs/design-guidelines-web.md`, öppna `styleguide/` och kopiera `styleguide/css/magello.css` + `styleguide/js/magello.js` **oförändrade**. Med Tailwind: importera även `tokens/tailwind.css` (v4-tema) |
| **Word** | `docs/design-language.md`, `docs/office-mallar.md`, `styleguide/word.html` och mallen `assets/templates/Word-mall.dotx` |
| **PowerPoint** | **Fråga först vilket spår som gäller** (se avsnitt 2). Spår A, mallen: `docs/office-mallar.md`, `styleguide/powerpoint.html`, `styleguide/typsnitt.html` (Kattux) och `assets/templates/Powerpoint-mall.potx`. Spår B, webbens formspråk: `docs/presentation-webb.md` och `tools/presentation/` |
| **PDF** | `docs/design-language.md`, `tokens/tokens.json` (typ i pt), formerna i `assets/shapes/`. Skapas PDF:en från Word eller PowerPoint gäller raden ovan |
| **Bilder, SVG, sociala medier** | `docs/design-language.md` (avsnittet Bilder och Bildverktyget), `tokens/tokens.json` (färg, former), `assets/shapes/`, `assets/logos/`, `assets/images/black-and-white/` (alla foton visas i `styleguide/bildbank.html`) |
| **E-postsignatur** | `styleguide/e-postsignatur.html` (signaturen, HTML och textversion). Ändra inte innehållet, byt bara namn, titel, LinkedIn och mobilnummer |
| **Profilbilder, LinkedIn-bilder, svartvita miljöbilder, kundlogotyper** | Bildverktyget https://linkedin-profile-image.magello.se och avsnittet Bildverktyget i `docs/design-language.md` |
| **Ny komponent eller ändring av formspråket** | `DECISIONS.md`, `styleguide/`, och avsnittet [Utveckla formspråket](#6-utveckla-formspråket) nedan |

Texten räcker inte för att få rätt utseende. **Facit är `styleguide/` (levande exempel), `styleguide/css/magello.css` och `tokens/tokens.json`.** Avviker ditt resultat från dem har du fel.

## 2. Arbetssätt

1. **Fråga först.** Ställ frågorna i slutet av `docs/design-language.md` (alla medier) och, för webb, avsnitt 2 i `docs/design-guidelines-web.md`. Föreslå standardvalet (★) om användaren inte har en åsikt. Fråga aldrig samma sak två gånger.
   **Presentationer:** fråga alltid vilket spår användaren vill ha, innan du gör något annat:
   - **Spår A, Magellos PowerPoint-mall.** Presentationen byggs i `Powerpoint-mall.potx` med mallens layouter och platshållare, så att användaren enkelt kan ändra och bygga vidare själv. Se `docs/office-mallar.md`.
   - **Spår B, webbens formspråk.** Agenten konstruerar hela presentationen från en tom 16:9-presentation så att den ser ut som webben: signaturytan på förstasidan, stor typografi, helbilder, luft. Se `docs/presentation-webb.md` och biblioteket i `tools/presentation/`.
   ★ Spår A om användaren själv ska fortsätta arbeta i presentationen, spår B om agenten ska leverera en färdig presentation. Blanda aldrig spåren.
2. **Bygg med tokens, inte med ögonmått.** Färger, typsnitt, avstånd och former hämtas ur `tokens/tokens.json` eller `magello.css`. Hitta aldrig på mellanvärden.
3. **Kopiera, skriv inte om.** På webben kopierar du `magello.css` och `magello.js`. Markup kopierar du från motsvarande styleguide-sida.
4. **Självgranska** mot checklistan nedan innan du levererar. Jämför visuellt med styleguiden.
5. **Rapportera avvikelser.** Måste du bryta mot en regel, säg vilken och varför. Gissa inte tyst.
6. **Skriv på svenska.** Utan utropstecken och utan fluffiga adjektiv. Rubriker beskriver vad något är eller gör.

## 3. Hårda regler (bryt aldrig utan att fråga)

1. **Inga linjer som avgränsare.** Struktur skapas av luft, bakgrundsskiften och former. Undantag: hårlinjer i tabellceller, ramen runt formulärfält och mobilmenyns listor, i rosagrått.
2. **Accentfärger är fyllnad, aldrig kant, streck eller understrykning.** Magenta, blå, orange, grön, röd, gul fyller former, ikoner, knappar och text.
3. **Alla synliga former är polygoner.** Ingen kant är exakt vågrät eller lodrät. Hörnen avviker 2–7 %. Inga rundade hörn (personbilder är enda cirkeln).
4. **Foton är alltid svartvita** (`grayscale(1) contrast(1.05)`) och beskurna i polygonform. Ikoner är alltid i full färg.
5. **Rosagrått är kärnan.** Sidan är i huvudsak svart, vit och rosagrå. Magenta används sparsamt: primär knapp, sektionsrubrik, länk, utvalt ord.
6. **Typsnitt:** Roboto Condensed för allt som signalerar (rubriker, knappar, etiketter), Roboto för allt som berättar (brödtext). Inga andra typsnitt. Undantag: specialtypsnittet **Kattux** (Kattux Abc 20) får användas vid speciella tillfällen, främst i PowerPoint, för ett kort budskap i stor storlek (minst 28 pt), högst ett element per bild eller sida, aldrig i brödtext, knappar eller navigation. Se `styleguide/typsnitt.html`.
7. **Inga gradienter, inga skuggor, inget mörkt läge.** (Funktionella undantag finns, se `docs/design-guidelines-web.md` avsnitt 5 och 41.)
8. **En primär knapp per vy.** Primär = magenta, sekundär = rose-200. Ingen outline-knapp.
9. **Det sista steget i en process är alltid magenta.**
10. **Informationsrutor läggs efter varandra i full bredd**, aldrig i en smal högerkolumn bredvid texten.
11. **Allt innehåll delar vänsterkant med logotypen.**
12. **Inga löpnummer (01, 02, 03)** som dekoration.
13. **Text på foto** läggs på en vit polygonplatta, aldrig direkt på bilden.
14. **Respektera `prefers-reduced-motion`** och håll kontrast på minst 4,5 : 1 för brödtext.
15. **Word utgår alltid från Magellos officiella mall** (`assets/templates/Word-mall.dotx`). **PowerPoint följer det spår användaren valt:** spår A utgår från `assets/templates/Powerpoint-mall.potx`, spår B byggs från en tom 16:9-presentation enligt `docs/presentation-webb.md`. Med mall: skapa själv en kopia och byt innehållstypen från mall till dokument (.potx → .pptx, .dotx → .docx), använd mallens layouter och formatmallar, och ändra inte tema, bakgrunder eller sidhuvud. Utgå aldrig från en annan mall. Be aldrig användaren köra kommandon. Se `docs/office-mallar.md`.
16. **Profilbilder, LinkedIn-banners och -inlägg, svartvita miljöbilder och kundlogotyper görs i bildverktyget** https://linkedin-profile-image.magello.se, aldrig för hand. Hänvisa användaren dit och säg vilken tjänst som passar.

## 4. Använda `tokens/tokens.json`

Filen är maskinläsbar och är källan till färger, typografi (web, tryck, presentation), avstånd, layout, rörelse, former och regler.

```python
import json
t = json.load(open("tokens/tokens.json"))
magenta = t["color"]["accent"]["magenta"]["value"]            # "#EC008C"
btn     = t["shape"]["polygons"]["button"]["points"]           # [[2,5],[99,0],[100,88],[97,100],[0,95]]
h2_pt   = t["type"]["print"]["h2"]["pt"]                       # 18  (Word)
```

**Rita en form som SVG** (till exempel för en bild eller en slide): skriv en `<polygon>` i en viewBox på `0 0 100 100` med `preserveAspectRatio="none"` och punkterna ur `shape.polygons`. Färdiga filer finns i `assets/shapes/` (genereras ur `tokens.json` när GitHub Pages bygger).

**Typografi i dokument:** i Word och PowerPoint kommer typografin från mallens formatmallar och layouter (se `docs/office-mallar.md`). `type.print` och `type.presentation` beskriver samma skala i pt, för kontroll och för andra medier. Brödtext i presentation aldrig under 18 pt, absolut minimum 14 pt.

**Office-mallar:** `assets.officeTemplates` i tokens anger filer, layouter och formatmallar. Mallarna i `assets/templates/` är originalen.

## 5. Checklista innan leverans

- [ ] Utgår Word från Magellos mall? Följer PowerPoint det spår användaren valt (A: mallens layouter, B: `docs/presentation-webb.md`)?
- [ ] Syns den rosagrå signaturytan där den ska (förstasida, omslag, header)?
- [ ] Är alla synliga former polygoner utan exakt raka kanter?
- [ ] Är alla foton svartvita och beskurna i polygonform?
- [ ] Är magenta bara fyllnad, rubrikfärg och länk, aldrig linje?
- [ ] Är rubriker Roboto Condensed och brödtext Roboto? På webben: är H2 magenta? I presentationer (spår B): är rubrikerna svarta, som DocTitle och h1?
- [ ] Är all text på svenska, utan utropstecken?
- [ ] Ligger allt innehåll på samma vänsterkant som logotypen?
- [ ] Ligger infoblock efter varandra i full bredd?
- [ ] Finns högst en primär knapp eller handling per vy?
- [ ] Är ikonerna i full färg och utan opacity?
- [ ] Har alla tokens som används ett värde? (På webb: kör token-kontrollen i `docs/design-guidelines-web.md` avsnitt 4.)
- [ ] Är kontrasten minst 4,5 : 1 för brödtext? (Magenta text på vitt klarar bara stor eller fet text.)
- [ ] Jämförde du resultatet visuellt med motsvarande sida i `styleguide/`?

## 6. Utveckla formspråket

Formspråket ska kunna växa, men som ett system: en ny sak ska stärka de sju principerna, inte kringgå dem.

1. **Härled först.** Finns det ett liknande mönster? Återanvänd dess form, färg och rörelse. Bryter din lösning mot en princip är den fel.
2. **Lägg nya komponenter som modifier** på en befintlig (`.mg-card--namn`), inte som en kopia med egen polygon.
3. **Uppdatera i den här ordningen:**
   1. `tokens/tokens.json` (nya färger, former eller värden).
   2. `styleguide/css/magello.css` (och `magello.js` vid beteende). Håll tokens i `:root`.
   3. En sida i `tools/pages/` med levande exempel, "Gör / Gör inte / Tänk på" och markup.
   4. `docs/design-language.md` (om principerna eller mediaoberoende regler ändras) och `docs/design-guidelines-web.md` (webbdetaljer).
   5. En rad i `DECISIONS.md` med datum och motivering.
4. **Testa** att komponenten ser rätt ut i 375, 768, 1280 och 1842 px, med bara rubriken ifylld och med allt ifyllt, och med tangentbord.
5. **Fråga användaren** innan du ändrar en hård regel (avsnitt 3) eller en befintlig komponents utseende.

## 7. Vad du inte gör

- Rundade hörn på rektanglar, perfekt raka kanter på synliga former.
- Linjer, accentfärgade kanter eller understrykningar som dekoration.
- Gradienter, skuggor, genomskinliga ikoner, färgfoton, mörkt läge.
- Fler än ett typsnittspar (Kattux vid speciella tillfällen undantaget, se regel 6). Fler än en accentfärg per komponent (processteg undantagna).
- Högerställda informationsrutor. Löpnummer som dekoration.
- Egna färgvärden, egna avstånd (20, 40 px) eller egna `max-width` på containrar.
- Skriva om `magello.css` från beskrivningen i stället för att kopiera den.
