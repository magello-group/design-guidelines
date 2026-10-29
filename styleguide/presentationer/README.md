# Webbpresentationer (spår C)

Ett alternativ till PowerPoint: Magello-presentationer som ren statisk HTML som ser ut som magello.se. Se spår C i `AGENTS.md` och beslut D-62 i `DECISIONS.md`. Ingen server, ingen build och inga beroenden: dubbelklicka på en presentations `index.html` så öppnas den i webbläsaren. Allt fungerar direkt från disk, även talarvyn. Typsnitten hämtas från Google Fonts som på webben, så utan nätverk faller texten tillbaka på Arial.

## Signaturheader

Första bilden visar webbens header: rosagrå polygon med logotypen och, om `data-header` finns på `<main class="deck">`, en text till höger. När man går vidare roterar headern bort som på webbens undersidor och ikonlogotypen glider in uppe till höger. Den ligger kvar på alla övriga bilder. `data-no-chrome` på en bild döljer den.

## Ny presentation

1. Kopiera `styleguide/presentationer/mall/` till en ny mapp bredvid, till exempel `styleguide/presentationer/kundevent/`.
2. Skriv en `<section class="slide">` per bild.
3. Dubbelklicka på `index.html`.

Se `exempel/` för alla layouter.

### Utanför det här repot

Presentationen behöver de här filerna, med samma inbördes placering som i repot:

```
styleguide/css/magello.css         tokens, typsnitt och bas (det delade biblioteket)
styleguide/css/magello-deck.css    bildlayouter, signaturheader, talarvy, utskrift
styleguide/js/magello-deck.js      motor: navigation, steg, övergångar, översikt, talarvy
assets/logos/magello-magenta.svg, assets/logos/icon-logotype.svg   läses av magello-deck.js
assets/graphics/citation.svg       citattecknet, läses av magello-deck.css
assets/graphics/, assets/images/black-and-white/   ikoner och foton som bilderna använder
```

`magello-deck.js` hittar logotyperna i `../../assets/logos/` räknat från skriptets mapp, och `magello-deck.css` hittar citattecknet i `../../assets/graphics/`. Kopiera filerna oförändrade, precis som `magello.css`.

## Storlek

Bilderna fyller alltid hela fönstret, utan svarta kanter. Innehållet är gjort för 1920×1080 och skalas så att det får plats. Är fönstret bredare eller högre än 16:9 växer bilden i den riktningen, och text och foton följer med. Utskrift och översikt är alltid 16:9.

## Tangenter

| Tangent | Funktion |
|---|---|
| → ↓ Mellanslag Enter PageDown | Nästa steg eller bild |
| ← ↑ Shift+Mellanslag PageUp | Föregående |
| Home / End | Första / sista bilden |
| F | Helskärm |
| O | Översikt (klicka på en bild för att gå dit, Esc stänger) |
| S | Talarvy i nytt fönster (se nedan) |

Svep åt sidan på mobil. Adressen visar bildnummer (`#4`) så att man kan länka till en bild. Presentationsklickers fungerar eftersom de skickar PageUp/PageDown.

## Talarvy

Som föredragshållarvyn i PowerPoint: bara du ser den, publiken ser presentationen.

1. Öppna presentationen och tryck **S**. Talarvyn öppnas i ett eget fönster.
2. Flytta presentationsfönstret till projektorn och tryck **F** för helskärm. Behåll talarvyn på din skärm.
3. Bläddra i vilket fönster som helst, de följer varandra.

Talarvyn visar aktuell bild, nästa bild (eller nästa steg), anteckningarna från `<aside class="notes">`, tid sedan start med paus och nollställning, och klockan. A− och A+ ändrar textstorleken i anteckningarna. Klicka på nästa bild för att gå dit.

## Markup

```html
<main class="deck" data-header="Kundevent · Oktober 2026">
<section class="slide">                 <!-- en bild, minst 1920×1080 -->
  <span class="kicker">Etikett</span>
  <h2>Rubriken är slutsatsen</h2>
  <ul>
    <li class="step">Kommer fram vid nästa klick</li>
  </ul>
  <aside class="notes">Talarmanus, visas bara i talarvyn.</aside>
</section>
</main>
```

| Layout | Används till |
|---|---|
| `slide--title` | Första bilden, som webbens hero: foto i `.slide__media` och `.plate` med etikett, `h1`, `.lead`, `.meta` |
| (ingen) | Vanlig innehållsbild |
| `slide--section` | Avsnittsbild med `h2` och `.lead` på rosagrå yta. Inga löpnummer |
| `slide--statement` | En mening i stor text |
| `slide--quote` | `blockquote` med `cite` |
| `slide--image` | Text vänster, svartvitt foto höger i `.slide__media` |
| `slide--photo` | Helbild med text på vit `.plate` |
| `slide--end` | Avslutning |

Byggstenar: `.cols` (`.cols--3`, `.cols--4`), `.card`, `.icon`, `.stat` (`.stat--grey`), `.lead`, `.small`, `pre`. `<em>` färgar ett accentord magenta.

## PDF

Skriv ut (Cmd+P) i Chrome, välj *Spara som PDF*, marginaler *Inga* och kryssa i *Bakgrundsgrafik*. Varje bild blir en sida i 16:9 med alla steg synliga.

## Struktur

```
styleguide/css/magello-deck.css           bildlayouter
styleguide/js/magello-deck.js             motor
styleguide/presentationer/mall/           mall att kopiera
styleguide/presentationer/exempel/        alla layouter och talarvyn
```

Exemplet publiceras med styleguiden: https://magello-group.github.io/design-guidelines/styleguide/presentationer/exempel/

Rubrikerna är vanlig Roboto och bildrubrikerna svarta. Avsnitts- och tackrubriker är magenta. Det är medvetna avsteg för spår C, se D-62 i `DECISIONS.md`.
