# Magello — Presentation i webbens formspråk (spår B)

> Den här filen beskriver hur en AI-agent bygger en PowerPoint-presentation som ser ut som Magellos webb, utan Magellos PowerPoint-mall. Principerna står i `design-language.md`. Förlagan är styleguiden (`styleguide/`), `styleguide/css/magello.css` och `tokens/tokens.json`. Ett färdigt bibliotek och ett exempel finns i `tools/presentation/`.

## Två spår för PowerPoint

Det finns två sätt att göra en presentation. **Fråga alltid användaren vilket spår som gäller innan du börjar** (se `AGENTS.md`, avsnitt 2).

| | Spår A: Magellos PowerPoint-mall | Spår B: webbens formspråk |
|---|---|---|
| **Passar när** | Användaren själv ska bygga vidare, byta text, lägga till bilder och återanvända layouter | En agent bygger hela presentationen och användaren vill ha ett färdigt, genomarbetat resultat |
| **Utgår från** | `assets/templates/Powerpoint-mall.potx` | En tom 16:9-presentation och tokens |
| **Utseende** | Mallens layouter, platshållare, plattor och Kattux | Som webben: signaturyta, stor typografi, helbilder, luft |
| **Redigera efteråt** | Enkelt, via layouter och platshållare | Möjligt men manuellt: textrutor och former ligger fritt på bilden |
| **Läs** | `docs/office-mallar.md` | Den här filen |

Blanda inte spåren i samma presentation.

## Arbetsgång (spår B)

1. Ställ frågorna i `design-language.md`, inklusive valet av spår.
2. Läs innehållet och dela upp det: **ett budskap per bild**. Långa originaltexter flyttas till talarnoterna, inte till mindre teckenstorlek.
3. Bygg med `tools/presentation/magello_pptx.py` (python-pptx, Pillow, cairosvg). Se `tools/presentation/exempel_ai_integration.py`.
4. Rendera och granska varje bild visuellt (till exempel via PDF). Rätta allt som överlappar, bryts mitt i ord eller går utanför sin yta.
5. Leverera `.pptx`. Skicka även PDF om mottagaren kan sakna Roboto.

## Format och raster

| Mått | Värde |
|---|---|
| Format | 16:9, 33,867 × 19,05 cm (12 192 000 × 6 858 000 EMU) |
| Vänster- och högermarginal | 2,75 cm (990 000 EMU). Logotypens vänsterkant är innehållets vänsterkant |
| Innehållsbredd | 28,37 cm |
| Etikett (kicker) | cirka 2,8 cm från överkant på innehållsbilder |
| Rubrik | direkt under etiketten, cirka 3,6 cm från överkant |
| Brödtextens radlängd | högst 70–75 tecken. Smal spalt (cirka 20 cm) hellre än full bredd |

## Typografi

Rubriker är alltid samma sak som **DocTitle i Word och h1 på webben**: Roboto Condensed Medium (500), svart. **Rubriker är aldrig magenta**, inte heller enstaka ord i en rubrik.

| Roll | Typsnitt | Storlek (pt) | Färg | Används till |
|---|---|---|---|---|
| Hero | Roboto Condensed Medium | 88–96 | Svart | Förstasidans titel |
| Display | Roboto Condensed Medium | 60–72 | Svart | Stora påståenden, avdelare, områdesrubriker |
| Rubrik (h1) | Roboto Condensed Medium | 44–54 | Svart | Vanlig bildrubrik |
| Underrubrik | Roboto Condensed 400 | 22–26 | Textgrå `#4C4A4A` | Ingress direkt under rubriken |
| Mellanrubrik (h3) | Roboto Condensed 700 | 22–28 | Svart | Rubrik i rutnät och kolumner |
| Brödtext | Roboto 400 | 18–22, radavstånd cirka 1,35 | Svart eller textgrå | Löptext |
| Etikett (kicker) | Roboto Condensed 700, versaler, spärrning 0,14 em | 13–14 | Magenta | Kategori ovanför rubriken |
| Brödsmula, datum | Roboto 400 / Condensed 700 versaler | 13 | Grå 300 `#BFBFBF` | Diskret information |

Regler:
- Låt den stora typografin bära bilden. Hellre ett påstående i 66 pt än fem punkter i 18 pt.
- Brödtext aldrig under 18 pt. Etiketter och brödsmulor får vara 13–14 pt.
- Sätt temats typsnitt till Roboto Condensed och Roboto, så att text som läggs till i PowerPoint blir rätt.
- Typsnitten bäddas inte in. Mottagaren behöver Roboto och Roboto Condensed installerade, annars skicka PDF.

## Färg

- Bilden är i huvudsak **vit, svart och svartvita foton**.
- **Rosagrått används sparsamt**, bara för att få något att stå ut: signaturytan på förstasidan och högst en eller två framhävda bilder i hela presentationen (en rosagrå sektion med polygonkanter, `section-rose`). Inga rosagrå rutor eller kort runt vanlig text.
- **Magenta** bara i: logotyper, etiketter, utvald menylänk på förstasidan, primär knapp (högst en) och sista processteget.
- Ikoner i full färg. Processteg i ordningen blå, orange, röd, gul, grön, magenta (färre steg: se `docs/processsteg.md`).

## Logotyper

| Bild | Logotyp | Placering |
|---|---|---|
| Förstasidan | `assets/logos/magello-magenta.svg` | Uppe till vänster i signaturytan, vänsterkant = innehållets vänsterkant, höjd cirka 1,2 cm |
| Bild 2 och framåt | `assets/logos/icon-logotype.svg` | I övre högra hörnet, lika långt från överkant och högerkant (cirka 0,95 cm), höjd cirka 2,1 cm |

Har platsen för ikonlogotypen en bakgrund (foto, platta eller färgad yta) utelämnas ikonlogotypen på den bilden. Biblioteket gör det automatiskt i `save()`.

## Förstasidan: signaturytan

Förstasidan är webbens header uppförstorad (se `styleguide/navigation.html`, Signaturytan som header):

- Ett svartvitt foto fyller hela bilden.
- Över fotot ligger den rosagrå signaturytan (rosagrå 100) från överkanten ner till cirka 68 % av höjden, med webbens headerpolygon: hela bredden upptill, högerkanten slutar på 55 % av ytans höjd, den lägsta punkten ligger rakt under logotypens vänsterkant och vänsterkanten slutar på 82 %. Den lutande kanten får aldrig rätas ut.
- Uppe till vänster logotypen. Till höger en menyrad i Roboto Condensed Medium 15 pt med presentationens avsnitt, och ett avslutande avsnitt som utvald länk i magenta med webbens skeva understrykning.
- Etikett, hero-titel, underrubrik i textgrått och datum som liten grå etikett, alla på logotypens vänsterkant och inom signaturytan.

## Bildtyper

| Bildtyp | Så ser den ut | Använd till |
|---|---|---|
| **Påstående** | Vit bild. Etikett, rubrik i 60–72 pt över två till tre rader, eventuellt två spalter brödtext under | Kärnbudskap, "Därför" |
| **Rubrik och rutnät** | Etikett, rubrik, sedan ikon + mellanrubrik + en mening i två eller tre kolumner, utan rutor. En ruta kan ersättas av ett polygonbeskuret foto | Förmågor, risker, nyttor (högst sex per bild) |
| **Bild och text** | Svartvitt foto i full höjd längs ena kanten med en snedskuren innerkant. Text i den andra halvan. Byt sida på fotot mellan bilder | Förklarande innehåll |
| **Helbild med platta** | Svartvitt helbildsfoto med en vit polygonplatta (`plate`) som bär etikett, rubrik och underrubrik. Text ligger aldrig direkt på foto | Avdelare mellan avsnitt, citat, avslutning |
| **Citat** | Helbild med platta, blått citattecken (`assets/graphics/citation.svg`) och citatet i Roboto Condensed 700 | Ett kort budskap |
| **Framhävd** | Rosagrå sektion (`section-rose`) med ett påstående i display-storlek | Högst en eller två gånger per presentation |
| **Område eller steg** | Text till vänster (etikett, rubrik, underrubrik, etikett, punktlista i två spalter, ett resultat med ikon i fet stil), foto i full höjd till höger | Delar av ett erbjudande, steg i en metod |
| **Process** | Etikett, rubrik, chevrons (`docs/processsteg.md`) med "Steg n" ovanför namnet och korta beskrivningar under | Flöden och metoder |
| **Uppmaning** | Helbild med platta: rubrik, en mening, en primär knapp och kontaktuppgifter | Sista bilden |

Ordning i en vanlig presentation: Förstasida → Påstående → Avdelare → innehåll → Framhävd → Avdelare → … → Uppmaning.

## Former och foton

- Alla former är polygoner ur `tokens.json` (`shape.polygons`): `plate`, `section-rose`, `image-a/b/c`, `case-image`, `button`, `chevron`. Ingen kant är exakt vågrät eller lodrät, utom där en yta går ut i bildens kant.
- Foton ur `assets/images/black-and-white/`, gjorda svartvita med `grayscale(1) contrast(1.05)`. Beskär i polygonform eller låt fotot gå ut i bildkanten med en snedskuren innerkant.
- Inga skuggor, gradienter eller kantlinjer. Ta bort temats formstil (`p:style`) från former som ritas, annars får de skugga.

## Kontroll före leverans

- [ ] Frågade du vilket spår som gäller?
- [ ] Har förstasidan signaturytan med webbens polygon och logotyp?
- [ ] Har bild 2 och framåt ikonlogotypen i övre högra hörnet, utom där hörnet har bakgrund?
- [ ] Är alla rubriker svart Roboto Condensed Medium, utan magenta?
- [ ] Används rosagrått bara på förstasidan och på högst en eller två framhävda bilder?
- [ ] Ligger text på foto alltid på en vit platta?
- [ ] Är brödtexten minst 18 pt, och ryms all text inom sin yta utan avstavning mitt i ord?
- [ ] Delar allt innehåll vänsterkant med logotypen?
- [ ] Har bilder med kortad text originaltexten i talarnoterna?
- [ ] Granskade du alla bilder visuellt?
