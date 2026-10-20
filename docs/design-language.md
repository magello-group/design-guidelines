# Magello — Designspråk

> Den här filen beskriver Magellos formspråk i ord, oberoende av medium. Den är skriven för att kunna ges till Claude (eller en människa) som ska skapa PowerPoint, Word-dokument, PDF:er, LinkedIn-bilder, utskrifter, affischer eller annat som ska kännas som Magello.
> Den innehåller inget som är webbspecifikt. Webbimplementation (CSS, komponenter, Strapi) finns i `design-guidelines-web.md`, som bygger på samma principer.
>
> **Filnamn:** tidigare `design-guidelines-general.md`. Heter nu `design-language.md` eftersom den beskriver själva designspråket, inte en teknisk riktlinje.

---

## Så använder du filen

1. Läs **Känsla och ton** och **De sju principerna** först. Resten är tillämpning.
2. Svara på **frågorna i slutet** (eller be användaren göra det) innan du börjar skapa. Saknas svar: använd de rekommenderade standardvalen.
3. Följ **Checklistan** innan du levererar.
4. När reglerna krockar med varandra gäller ordningen: principerna > färg och typografi > övriga mönster.
5. Hittar du inget uttryckligt svar, resonera utifrån principerna. Magello-formspråket är ett system, inte en samling regler att plocka från.

**Visuell referens:** `styleguide/` är en komplett statisk styleguide som visar formspråket i praktiken, med bruksanvisning per komponent (se tabellen nedan). Öppna `styleguide/index.html`. Maskinläsbara värden finns i `tokens/tokens.json` och formerna som SVG i `assets/shapes/`. Webbspecifik kod hör hemma i `docs/design-guidelines-web.md`.

**Word utgår alltid från Magellos officiella mall**, `assets/templates/Word-mall.dotx`, aldrig från ett tomt dokument. **PowerPoint görs på ett av två sätt**, som användaren väljer: med `assets/templates/Powerpoint-mall.potx` (spår A) eller konstruerad av en agent i webbens formspråk (spår B, `docs/presentation-webb.md`). Hur de används, vilka layouter och formatmallar som finns och var de avviker från tokens står i `docs/office-mallar.md`.

Referensmaterial: `assets/templates/Powerpoint-mall-howto.pptx` och `assets/templates/Word-mall-howto.docx` visar mallarna i bruk, och `styleguide/powerpoint.html` och `styleguide/word.html` beskriver hur de används med AI-agent eller för hand.

### Visuell referens — styleguiden

Öppna `styleguide/index.html` i en webbläsare. Varje sida visar något levande och förklarar när det ska användas och när inte:

| Sida | Visar |
|---|---|
| `styleguide/farg.html` | Palett med roller, proportioner, accent som fyllnad, kontrast |
| `styleguide/form.html` | Polygonspråket: princip, formkatalog med koordinater, hover, andra medier |
| `styleguide/typografi.html` | Typsnitt, skala, profiler, språkregler, storlekar i Word och PowerPoint |
| `styleguide/typsnitt.html` | Specialtypsnittet Kattux: när det används, teckenuppsättning, installation på Mac och PC |
| `styleguide/bilder-ikoner.html` | Svartvita foton, platta över bild, personbilder, ikonbibliotek |
| `styleguide/avstand-rorelse.html` | Avståndsskala, layout, brytpunkter, rörelse |
| `styleguide/komponenter.html` | Knappar, kort, processteg, citat, infoblock, tabell, tidslinje, kontaktkort |
| `styleguide/sektioner.html` | Sidtyper, sidhuvud, rosa sektion, bild och text, case, artikellayout |
| `styleguide/formular-feedback.html` | Fält, val, uppladdning, pills, toast, laddning |
| `styleguide/navigation.html` | Header, dropdown, sidospår, mobilmeny, brödsmula |
| `styleguide/powerpoint.html` | PowerPoint: i första hand med AI-agent, annars mallen och layouterna |
| `styleguide/word.html` | Word: mallen, formatmallarna och med AI-agent |
| `styleguide/markdown.html` | Hur Markdown (till exempel från Strapi) renderas |

Tillgångar (logotyper, ikoner, svartvita foton) ligger i `assets/logos/`, `assets/graphics/` och `assets/images/black-and-white/`.

---

## Känsla och ton

**Syfte:** Visa hur Magello kan hjälpa kunder lösa sina egentliga problem. Vi ska vara trovärdiga, men också personliga med en lättsam och lekfull sida.

**Målgrupp:** Chefer, rekryterare och beställande IT-personer.

**Känsla:** Professionell, avskalad, tydlig och typografisk. Lite lekfull.

**Referenser vi gillar som bas:** volvocars.com/se och tesla.com. Mycket luft, få element, stor tydlig typografi, bilder som får ta plats.

**Så märks lekfullheten:** I formerna. Inget är perfekt rektangulärt, allt har liv i hörnen. Allvaret ligger i typografin, luften och den dämpade färgskalan.

**Språk:** Svenska. Skriv konkret och varmt, utan utropstecken och utan fluffiga adjektiv. Rubriker beskriver vad något är eller gör ("Vi hjälper kunder bygga fungerande mjukvara"), inte hur fantastiskt det är.

---

## De sju principerna

### 1. Inga linjer som avgränsare
Vi delar inte upp innehåll med streck. Struktur skapas av luft, bakgrundsskiftningar och former. En linje säger "här slutar något", en form säger "här börjar något".
- Undantag som får finnas: ljusa linjer inne i tabeller där läsbarheten kräver det, och ramen runt ett inmatningsfält. Aldrig som dekoration.

### 2. Accentfärger är fyllnad, aldrig kant
Magenta, blå, orange, grön, röd och gul fyller former, ikoner, knappar och text. De ritas aldrig som streck, understrykningar eller kantlinjer.

### 3. Former har rörelse — ingen kant är exakt rak
Alla synliga former (rutor, knappar, bildbeskärningar, sektionsbakgrunder) är polygoner där hörnen avviker några procent från ett perfekt rätblock. Ingen kant är exakt horisontell eller vertikal. Det ser handgjort och levande ut, inte som ett misstag.

### 4. Allt är svartvitt utom varumärket
Foton är alltid svartvita. Då får magenta och ikonernas färger hela scenen. Färgfoton konkurrerar med varumärket.

### 5. Rosagrått är kärnan
Svart text på vitt är grunden. Den rosagrå paletten ger varma ytor och struktur. Magenta används sparsamt och med avsikt. Sidor, bilder och dokument ska i huvudsak vara svarta, vita och rosagrå.

### 6. Signaturen: den diagonala rosagrå ytan
Alla Magellos grafiska produkter har en rosagrå yta med en lutande, skärande kant. Den är det mest igenkännbara elementet. Se förstasidan i `assets/templates/Word-mall.dotx` och `assets/templates/Powerpoint-mall.potx`. Använd den i toppen av förstasidor, omslag och landningsytor, inte på varje sida.

### 7. Luft och en gemensam linje
Generöst med luft, särskilt ovanför rubriker. Avståndet under en rubrik är alltid mindre än ovanför, så att rubriken hör ihop med sin text. Allt innehåll följer **samma vänsterkant**: logotypens vänsterkant avgör var texten börjar, på varje sida och i varje bild.

---

## Färger

### Neutraler

| Namn | Hex | Används till |
|---|---|---|
| Svart | `#000000` | Brödtext, rubriker i löpande innehåll |
| Vit | `#FFFFFF` | Bakgrund, ytor ovanpå foton |
| Textgrå | `#4C4A4A` | Underrubriker, sekundär text och ingresser |
| Rosagrå 50 | `#F7F3F3` | Ljusaste bakgrund, faktarutor, tabellband |
| Rosagrå 100 | `#F4EBEB` | Signaturytan, sektionsbakgrund, textrutor |
| Rosagrå 200 | `#E3D6D6` | Sekundär knapp, tabellrubrik, ljusa fyllnader |
| Rosagrå 300 | `#DED4D4` | Hover på sekundär knapp, tabellsummering |
| Grå 300 | `#BFBFBF` | Diskreta etiketter, årtal, sidfot |

### Accenter

| Namn | Hex | Roll |
|---|---|---|
| **Magenta** | `#EC008C` | Primär accent: logotyp, primär knapp, andra-nivåns rubriker, utvalda ord |
| Blå | `#31ABE2` | Ikoner, processteg |
| Orange | `#F9B804` | Ikoner, processteg |
| Röd | `#E3012F` | Ikoner, fel |
| Gul | `#FFDC00` | Ikoner, varning |
| Grön | `#1BA660` | Ikoner, klart/lyckat |

### Regler
- Magenta används för rubriker på sektionsnivå, logotypen, primära handlingar och enstaka ord. Aldrig som stor yta med brödtext ovanpå.
- De övriga accenterna hör hemma i ikoner, illustrationer och processteg. De används inte som textfärg.
- Max en accentfärg dominerar en komponent. Blanda inte flera i samma ikon eller ruta, förutom i processteg där färgerna avlöser varandra.
- Inga gradienter, inga skuggor, inget mörkt läge.
- Mörka ytor används inte i marknadsmaterial. (Verktyg och appar har en mörk rosagrå toppbalk, se webbfilen.)
- Kontrast: brödtext minst 4,5:1 mot bakgrunden. Magenta text på vitt uppfyller kravet för stor text; använd svart för små brödtexter.

---

## Typografi

**En enkel regel: Roboto Condensed för allt som signalerar, Roboto för allt som berättar.**

| Typsnitt | Används till |
|---|---|
| **Roboto Condensed** (vikt 400/500/700) | Rubriker, underrubriker, etiketter, knappar, siffror som blickfång |
| **Roboto** (vikt 400/500/700, kursiv 400) | Brödtext, tabeller, listor, bildtexter, sidfot |
| Consolas | Kod, bara i tekniska dokument |

Blanda aldrig tvärtom: Roboto i en knapp eller Condensed i löptext förstör tonen direkt. Inga andra typsnitt, med ett undantag:

**Specialtypsnittet Kattux** (Kattux Abc 20) är Magellos handritade typsnitt för speciella tillfällen, främst i PowerPoint. Det får bära ett kort budskap eller citat i stor storlek (minst 28 pt, gärna 44–66 pt), högst ett element per bild eller sida, alltid tillsammans med Roboto Condensed och Roboto. Aldrig brödtext, listor, tabeller, knappar eller navigation. Typsnittet har bara versaler (gemener ritas som versaler) och en vikt. Det har å, ä och ö men saknar bland annat ü, ß, € och långt tankstreck. Filerna finns i `assets/fonts/`, och installation och regler står i `styleguide/typsnitt.html`.

### Storlekar i tryck och presentation

Skalan utgår från brödtexten (faktor 1,0) och är hämtad ur Wordmallen.

| Nivå | Typsnitt och vikt | Storlek (Word) | Faktor | Färg |
|---|---|---|---|---|
| Dokumenttitel (H1) | Condensed 500 (700 för stor display) | 36 pt | 3,6 | Svart |
| Underrubrik | Condensed 400, spärrning +0,75 pt | 22 pt | 2,2 | Textgrå |
| H2 | Condensed 500 | 18 pt | 1,8 | **Magenta** |
| H3 | Condensed 700 | 16 pt | 1,6 | Svart |
| H4 | Condensed 700 | 14 pt | 1,4 | Svart |
| H5 | Condensed 700 | 12 pt | 1,2 | Svart |
| H6 / etikett | Condensed 700 | 10 pt | 1,0 | Svart |
| Brödtext | Roboto 400 | 10 pt, radavstånd 1,15 | 1,0 | Svart |
| Sidhuvud | Roboto | 7 pt | 0,7 | Svart (titel fet) |
| Sidfot | Roboto | 6,5 pt | 0,65 | Grå 300 |

**I Word** Dokumenttitel eller DocTitle ska vara dokumentets huvudtitel, för Magellos mallar så sätter det fält i sidhuvudet på sida två och framåt. I Word-mallen heter H2 **Rubrik 1**, H3 **Rubrik 2** och så vidare (se `docs/office-mallar.md`).
**I PowerPoint** gäller samma proportioner men större: titel 40–54 pt, H2 28–32 pt, brödtext minst 18 pt. Aldrig under 14 pt i en presentation.

### Typografiska regler
- **H1 är magenta**: den signalerar "en ny idé börjar här". Rubriker inne i löpande artiklar kan vara svarta så att de inte konkurrerar.
- **Etiketter (kickers)**: Condensed fet, versaler, bred bokstavsspärrning (cirka 0,12–0,14 em), magenta. De placeras alltid *ovanför* rubriken de tillhör och anger kategori, inte innehåll.
- **Siffror som blickfång** (till exempel "30 år"): Condensed fet, stor storlek, grå 300 eller magenta.
- **Länkar och accentord**: magenta.
- **Radavstånd**: tätt i rubriker (1,1–1,2), luftigt i brödtext (1,5–1,6 på skärm, 1,15 i Word).
- **Radlängd**: 70–75 tecken per rad är lagom. Längre rader tröttar.
- **Avstånd**: mellanrummet före en rubrik är ungefär dubbelt så stort som efter den.
- Listor: punkt (nivå 1), cirkel (nivå 2), fyrkant (nivå 3). Cirka 4 px/3 pt mellan punkterna.
- Ingen text i versaler utom etiketter. Inga understrykningar utom länkar.

---

## Formspråket i praktiken

### Så ritar du en Magello-form

1. Börja med en rektangel.
2. Flytta varje hörn 2–7 % bort från sin exakta position, i olika riktningar. Övre vänster hörn kan sjunka 3 %, övre höger kan flytta 2 % in från kanten, och så vidare.
3. Lägg gärna till en femte eller sjätte punkt (ett avfasat hörn) för att ge formen en riktning.
4. Kontrollera att ingen kant råkar bli exakt vågrät eller lodrät.

**Skalregel:** Små former (etiketter, ikoner) avviker 2–4 %. Medelstora (knappar, rutor, kort) 2–6 %. Stora (hela sektioner, bildytor) 3–8 %, gärna med fler punkter.

I PowerPoint och Word finns formerna redan i mallarnas layouter och sidhuvuden. Behövs fler byggs de som *fria former* (Freeform / Redigera punkter) eller som färdiga SVG-former från `assets/shapes/`. Bakgrundsformer att kopiera finns sist i `assets/templates/Powerpoint-mall-howto.pptx`.

### Formfamiljen

| Form | Hur den ser ut | Används till |
|---|---|---|
| **Signaturytan** | Bred rosagrå yta med lutande underkant | Överdel på omslag och förstasidor |
| **Femhörning** | Rektangel med fem hörn, inget rakt | Knappar och handlingsytor |
| **Låda** | Rektangel med 4–6 lätt avvikande hörn | Faktarutor, kort, citatrutor |
| **Pappersflik** | Låda med ett avfasat hörn uppe till höger | Textrutor (callout) |
| **Bildplatta** | Vit låda med åtta hörn ovanpå ett foto | Rubrik och text ovanpå foto |
| **Chevron** | Pilform: spets åt ena hållet, skåra åt andra | Processteg |
| **Diamant och hexagon** | Små symmetriska former | Markörer i tidslinje, märken |
| **Pill** | Avlång med spetsiga ändar | Statusetiketter |

### Rörelse och interaktion
Där formerna är klickbara (digitalt material) blir de lite mer rektangulära när man pekar på dem. De "slappnar av". Detaljerna finns i webbfilen.

---

## Bilder

- **Alla foton är svartvita.** Ingen färgkorrigering utöver gråskala och lätt kontrast.
- **Fotona klipps i polygonformer** (se formfamiljen). Aldrig en perfekt rektangel.
- **Bildplatta**: när text läggs på foto görs det på en vit polygonplatta, inte direkt på bilden.
- **Personbilder är runda** och svartvita. Det är det enda stället där cirkelformen används.
- **Bildmotiv**: kontor, möten, skärmar, whiteboards, händelser. Verkliga människor och miljöer, helst inte stockkänsla. Lugna kompositioner med plats för text.
- **Bildtext och alt-text**: beskriv vad bilden visar, inte att det är en bild.
- Bildbiblioteket ligger i `assets/images/black-and-white/`. Alla foton visas och kan laddas ned i styleguidens [Bildbank](https://magello-group.github.io/design-guidelines/styleguide/bildbank.html).

### Bildverktyget

Profilbilder, LinkedIn-bilder, svartvita miljöbilder och kundlogotyper görs i Magellos bildverktyg, **https://linkedin-profile-image.magello.se**, inte för hand. Verktyget ger rätt filter, rosa ton, former och mått. Allt körs lokalt i webbläsaren, och inga bilder laddas upp till någon server.

| Tjänst | Ger | Använd till |
|---|---|---|
| Ny profilbild | Svartvit profilbild med rosa ton | Profilbild på LinkedIn, i CV och presentationer |
| Linkedin – Personlig top banner | Banner med Magellos formgivning, utifrån en miljöbild | Bakgrundsbild på LinkedIn-profilen |
| Linkedin – Text på profilbild | Profilbild med text (till exempel "Konsult") | Profilbild med budskap |
| Linkedininlägg för nyanställd | Inläggsbild med valfri text, färg, rotation och överlägg | Välkomstinlägg på LinkedIn |
| Powerpoint – Skapa svartvita miljöbilder | Svartvit miljöbild, 1080 × 1080 px | Bilder i PowerPoint och LinkedIn-inlägg ur färgfoton |
| Skapa ikoner för uppdrag i CV | Kundlogotyp (SVG in) beskuren till 200 × 200 px | Kundlogotyper i CV och uppdragslistor |

En agent kan hänvisa till verktyget och beskriva vilken tjänst som passar, men ska inte själv bygga sådana bilder med egna filter eller former.

---

## Ikoner och grafik

- Ikoner är **platta vektorer**: solida fyllnader, inga gradienter, inga skuggor, ingen kantlinje.
- Formspråket är handritat och organiskt, "pappersklippt", inte geometriskt perfekt.
- **Färgen väljs efter betydelsen**, inte efter var ikonen hamnar: blå = teknik och koppling, grön = dialog och godkänt, röd = tid och brådska, gul = idé, magenta = Magello-värden, orange + mörkblå = innovation.
- Max 2–3 färger per ikon.
- Ikoner visas alltid i full färg och full styrka: aldrig gråskala, aldrig genomskinliga.
- Ikonen ska fungera på vit, rosagrå 50 och rosagrå 100.
- Ikonstorlek: 40 px/12 mm i rutor och kort, 72 px/20 mm som fristående blickfång.
- Ikonbiblioteket ligger i `assets/graphics/`. Magellos fyra värdeord (Personliga, Trygga, Kommunikativa, Lärande) har ett eget set i `assets/graphics/värdeord/` som bara används när Magello som bolag beskrivs.
- Citattecknet (`citation.svg`) är dekor för citat, inte en fristående ikon.

---

## Innehållsmönster

Det här är återkommande byggstenar. Oavsett medium ska de se ut och bete sig likadant.

### Knappar och handlingsytor
- Femhörning, aldrig rundade hörn, ingen kantlinje.
- **Primär**: magenta fyllnad, vit text. Max en per vy eller bild.
- **Sekundär**: rosagrå 200 fyllnad, svart text. Aldrig en "outline"-knapp med kant.
- Text i Roboto Condensed 500, lätt bokstavsspärrning. Verb som beskriver handlingen: "Prata med oss", "Läs om våra expertområden".

### Infoblock och faktarutor
- Rosagrå 50 eller 100, polygonform, liten magenta etikett överst.
- **Infoblock placeras efter varandra i textflödet, i full bredd.** De flyter aldrig upp i en smal högerkolumn bredvid texten. Ingress och brödtext går alltid i full bredd.
- Siffror ("Magello i siffror") visas i en rad inne i rutan.

### Citat
- Stort citattecken (`citation.svg`) till vänster, citatet i Condensed 500, svart, större än brödtext.
- Ingen kantlinje till vänster och ingen genomskinlighet.

### Textruta (callout)
- Rosagrå 100, pappersflik-hörn uppe till höger, ingen kantlinje.
- Kort text, ofta med en stor siffra eller symbol som blickfång.

### Kort
- Vit eller rosagrå yta i polygonform, svartvit bild överst, etikett, rubrik och en kort text.
- Inga löpnummer (01, 02, 03) som dekor. Numrering används bara när ordningen betyder något, som i processteg.

### Processteg
- Kedja av chevrons i accentfärger som avlöser varandra: blå, orange, röd, gul, grön.
- **Sista steget är alltid magenta** ("Klar!").
- Första steget har ingen skåra åt vänster. Ett litet "Steg 1" visas ovanför stegets namn.

### Tidslinje
- Årtal i grå 300 till vänster, diamantmarkörer i rosagrå 200, aktuellt år markerat med magenta fyllnad och större diamant.
- Bakgrund rosagrå 50, aldrig svart.

### Tabeller
- Rubrikrad rosagrå 200 med fet text. Varannan rad rosagrå 50. Första kolumnen fet.
- Mycket ljusa celllinjer (rosagrå 50 eller vit). Summeringsrad fet med dubbel linje ovanför. Inga mörka linjer, inga accentlinjer.
- Siffror högerjusteras, text vänsterjusteras.

### Sidhuvud och sidfot (dokument)
- Sidhuvud: dokumentets titel i fet 7 pt uppe till vänster, datum i normal vikt. Den rosagrå signaturytan med logotypen i magenta överst på förstasidan.
- Sidfot: tre kolumner i liten grå text, utan linje ovanför. "Magello" i magenta, adress, organisationsnummer, momsnummer, telefon, e-post.

### Layout och marginaler
- A4: marginal topp och vänster 2,54 cm, höger 2,95 cm, botten 3,0 cm. Textbredd cirka 15,5 cm.
- Presentationer: samma vänsterkant på alla bilder. Logotypens vänsterkant avgör.
- Tomt utrymme är en del av designen. Fyll inte varje yta.

---

## Logotyp

- **Fullständig ordlogotyp** (magenta, i en vit pill/bricka): `assets/logos/magello-magenta.svg`. Standard överst på sidor och dokument.
- **Vit logotyp** (transparent bakgrund): `assets/logos/magello-white-transparent-letters.svg`, bara på mörka eller fotobaserade ytor.
- **Ikonlogotyp** (oregelbunden oktogon med vit inre form): `assets/logos/icon-logotype.svg`, när utrymmet är litet: favicon, profilbild, smala spalter.
- Frizon runt logotypen: minst logotypens egen höjd. Ingen skugga, ingen rotation (utom där rörelsen är del av ett digitalt gränssnitt), inga andra färger än magenta och vit.

---

## Vad vi inte gör

- Rundade hörn på rektanglar (profilbilder är enda cirkeln).
- Linjer som avgränsare, accentfärgade kantlinjer eller understrykningar.
- Gradienter, skuggor, genomskinliga ikoner, färgfoton, mörkt läge.
- Perfekt vågräta eller lodräta kanter på synliga former.
- Högerställda informationsrutor som textflödet viker undan för.
- Löpnummer som dekoration.
- Fler än ett typsnittspar (Kattux vid speciella tillfällen undantaget). Fler än en accentfärg per komponent.
- Utropstecken och överdrivna adjektiv.
- Sidor som tvingas fyllas till kanten.

---

## Checklista innan leverans

- [ ] Utgår ett Word-dokument eller en presentation från Magellos mall (`Word-mall.dotx`, `Powerpoint-mall.potx`)?
- [ ] Syns den rosagrå signaturytan där den ska (förstasida, omslag)?
- [ ] Är alla synliga former polygoner, utan exakt raka kanter?
- [ ] Är alla foton svartvita och beskurna i polygonform?
- [ ] Är profilbilder, LinkedIn-bilder och kundlogotyper gjorda i bildverktyget (https://linkedin-profile-image.magello.se)?
- [ ] Används magenta bara som fyllnad, rubrikfärg och länk, aldrig som linje?
- [ ] Är rubriker i Roboto Condensed och brödtext i Roboto?
- [ ] Är H2 magenta och etiketter versaler, spärrade och magenta?
- [ ] Är all text på svenska, utan utropstecken?
- [ ] Ligger allt innehåll på samma vänsterkant som logotypen?
- [ ] Ligger infoblock efter varandra i full bredd, inte i en smal sidokolumn?
- [ ] Finns det en enda primär knapp eller handling per vy?
- [ ] Är ikonerna i full färg?
- [ ] Är kontrasten minst 4,5:1 för brödtext?
- [ ] Har du lämnat tillräckligt med luft?

---

## Frågor att ställa innan du börjar

Ställ frågorna i ordning. Föreslå standardvalet (markerat med ★) om användaren inte har en åsikt, och gå vidare utan att fråga om samma sak två gånger.

### Om uppdraget
1. **Vad ska skapas?** Presentation, Word-dokument, PDF/rapport, affisch, LinkedIn-bild, e-postmall, annat?
2. **Vad är syftet med materialet?** (Sälja, informera, rekrytera, dokumentera, bjuda in.)
3. **Vem läser eller tittar?** Chefer, rekryterare, beställande IT-personer, kunder, kollegor? ★ Chefer och beställare.
4. **Var används det?** Skärm, utskrift, projektor, sociala medier? Avgör storlekar och minsta textstorlek.
5. **Word eller PowerPoint?** Word utgår alltid från `assets/templates/Word-mall.dotx` (A4), se `docs/office-mallar.md`. För andra format: fråga om format och sidstorlek.
   **PowerPoint: mallen eller webbens formspråk?** Spår A utgår från `assets/templates/Powerpoint-mall.potx` (16:9) och mallens layouter, så att användaren enkelt kan ändra själv (`docs/office-mallar.md`). Spår B låter en agent konstruera presentationen så att den ser ut som webben (`docs/presentation-webb.md`). ★ Spår A om användaren ska bygga vidare själv, spår B om agenten levererar en färdig presentation.

### Om innehållet
6. **Vilket är det enda budskap mottagaren ska minnas?** Det styr rubrik och struktur.
7. **Finns texten redan, eller ska den skrivas?** Om den ska skrivas: ton enligt avsnittet Känsla och ton. Svenska.
8. **Vilka bilder finns?** ★ Använd `assets/images/black-and-white/` (visas i Bildbanken). Egna foton görs om i bildverktyget. Nya foton görs svartvita och klipps i polygonform.
9. **Finns siffror, citat, tidslinjer, processer eller jämförelser?** Då används de matchande mönstren i avsnittet Innehållsmönster.
10. **Ska något få en tydlig handling?** (Kontakta oss, läs mer, sök tjänsten.) Max en primär handling.

### Om formen
11. **Hur dramatisk ska formen vara?** ★ Signaturytan på omslaget, lugna polygoner därefter. Mer dramatik på omslag och avdelare, mindre i brödtextsidor.
12. **Ska en accentfärg lyftas?** ★ Magenta. Övriga accenter bara i ikoner och processteg.
13. **Vilken ton: mer formell eller mer lekfull?** ★ Avskalat och tydligt, lekfullheten i formerna.
14. **Finns referensmaterial som ska efterliknas eller undvikas?** Be om ett exempel och jämför med principerna.

### Om leveransen
15. **Vilket format ska levereras?** (.pptx, .docx, .pdf, .png, .svg.) Bädda in typsnitten eller exportera till PDF om mottagaren saknar Roboto.
16. **Ska materialet kunna uppdateras av någon annan?** Då används mallens formatmallar (Rubrik 1–6, tabellformat) i stället för manuell formatering.
17. **Ska det vara tillgängligt (läsbart av skärmläsare)?** Då behövs alt-texter, tydlig rubrikstruktur och kontrast enligt avsnittet Färger.
