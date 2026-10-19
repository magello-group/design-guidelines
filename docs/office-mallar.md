# Magello — Office-mallar (Word och PowerPoint)

> Den här filen beskriver Magellos officiella mallar för Word och PowerPoint och hur en människa eller en agent använder dem. Principerna står i `design-language.md`. Här står vad som finns i mallarna och vilken layout eller formatmall som ska användas till vad.

**Regel:** Ett Word-dokument från Magello utgår alltid från Word-mallen, aldrig från ett tomt dokument eller en annan mall. En PowerPoint-presentation utgår från PowerPoint-mallen när användaren valt spår A (nedan).

## Två spår för PowerPoint

Fråga alltid användaren vilket spår som gäller innan presentationen byggs.

| | Spår A: PowerPoint-mallen (den här filen) | Spår B: webbens formspråk |
|---|---|---|
| Passar när | Användaren själv ska ändra och bygga vidare | En agent ska leverera en färdig presentation |
| Utgår från | `Powerpoint-mall.potx`, layouter och platshållare | En tom 16:9-presentation, tokens och `tools/presentation/` |
| Utseende | Mallens layouter, plattor och Kattux | Som webben: signaturyta, stor typografi, helbilder, luft |
| Läs | Den här filen | `docs/presentation-webb.md` |

Mallen är gjord för att människor enkelt ska kunna göra presentationer själva. Spår B är för när en agent konstruerar hela presentationen och ska få samma utseende som webben. Blanda inte spåren.

| Mall | Fil här | Blir |
|---|---|---|
| PowerPoint | `assets/templates/Powerpoint-mall.potx` | `.pptx`, 16:9 (33,867 × 19,05 cm) |
| Word | `assets/templates/Word-mall.dotx` | `.docx`, A4 stående |
| Instruktion för PowerPoint-mallen | `assets/templates/Powerpoint-mall-howto.pptx` | Läses och används som exempel, inte som mall |
| Instruktion för Word-mallen | `assets/templates/Word-mall-howto.docx` | Läses och används som exempel, inte som mall |

Styleguidesidan `styleguide/office.html` (Word och PowerPoint) har nedladdningsknappar och korta instruktioner för den som gör dokumentet själv.

## Källa

Filerna i `assets/templates/` är originalen. Ändringar i mallarna görs här, i repot, och beslutas som andra ändringar i formspråket (se `DECISIONS.md`).

## Skapa ett nytt dokument

**Människa:** ladda ned mallen och dubbelklicka på den. Word eller PowerPoint öppnar ett nytt, namnlöst dokument som bygger på mallen, på både Mac och PC. Spara det som vanligt. Själva mallen ändras inte.

**Agent:** en `.potx` eller `.dotx` är ett Office-paket (zip) med innehållstypen *template*. Agenten skapar själv en kopia, byter huvuddelens innehållstyp i `[Content_Types].xml` från `presentationml.template.main+xml` till `presentationml.presentation.main+xml` (PowerPoint) eller från `wordprocessingml.template.main+xml` till `wordprocessingml.document.main+xml` (Word), och sparar filen som `.pptx` eller `.docx`. Sedan fyller den mallens layouter och formatmallar, till exempel med python-pptx eller python-docx. PowerPoint-mallen innehåller 28 exempelbilder som visar layouterna. Agenten tar bort dem den inte använder.

Byt aldrig ut mallens tema, bakgrunder eller former. Skriv text i platshållarna och använd mallens formatmallar. Lägg inte till egna textrutor med egen formatering när en platshållare finns. Be aldrig en människa köra kommandon för att skapa ett dokument.

## PowerPoint-mallen

Mallen har en bakgrundsbild (master) och 13 layouter. Rubriker är Roboto Condensed (Medium), brödtext Roboto Medium. Mallens grafik och färger är förvalda.

| # | Layout | Platshållare | Använd till |
|---|---|---|---|
| 1 | **Förstasida** | bild, rubrik | Första bilden. Rubrik och datum, svartvitt foto, logotyp |
| 2 | **Innehåll - Grå bård** | rubrik, innehåll, två bildytor | Innehållsbild med rosagrå bård. Standard för innehåll med bild eller grafik |
| 3 | **Innehåll - Enkel** | rubrik, innehåll | Standard för text, tabeller, diagram och processer |
| 4 | **Sektion - Röd platta** | bild, rubrik | Avdelare mellan delar av presentationen |
| 5 | **Sektion - Gul platta** | bild, rubrik | Som 4, med gul platta |
| 6 | **Sektion - Grön platta** | bild, rubrik | Som 4, med grön platta |
| 7 | **Fokus - Rubrik vänster på bild** | bild, rubrik | Ett budskap över en helbild. Avslutning, "Nästa steg" |
| 8 | **Fokus - Med innehåll** | rubrik, innehåll | Ett budskap med en kort förklarande text |
| 9 | **Fokus - Rubrik på platta** | bild, rubrik | Citat eller kort påstående på färgad platta |
| 10 | **Innehåll - Platta** | innehåll | Kort text på färgad platta, gärna kombinerad med grafik |
| 11 | **Bild - Stor bild** | bild | Ett foto som fyller bilden |
| 12 | **Bilder - Flera** | fyra bildytor | Bildkollage, team, miljöer |
| 13 | **Tom utan rubrik** | inga | Fri yta för diagram eller grafik som inte passar en annan layout |

**Ordning i en vanlig presentation:** Förstasida → (Sektion) → Innehåll - Enkel / Grå bård → Fokus → … → Fokus - Rubrik vänster på bild ("Nästa steg").

**Storlekar (pt):** mallens rubriker är 36–54 pt, brödtext 28 / 24 / 20 / 18 pt per nivå. Det stämmer med `type.presentation` i `tokens/tokens.json`. Gå aldrig under 18 pt för brödtext (absolut minimum 14 pt).

**Exempelbilderna** (28 st, behålls utan `--empty`) visar hur layouterna fylls: tabeller, diagram, processteg och statusrapport. Titta på dem innan du bygger, och ta bort dem du inte använder.

**Foton:** byt bild i platshållaren. Använd svartvita foton (`assets/images/black-and-white/`). Layouternas beskärning ger polygonformen.

## Word-mallen

A4 stående. Första sidans sidhuvud har den rosagrå signaturytan med diagonal kant och logotyp, följande sidor logotypsymbolen. Sidhuvudet visar dokumenttitel och datum som fält. Sidfot med Magellos adress, organisationsnummer och telefon. Typsnitten Roboto, Roboto Condensed och Roboto Condensed Medium är inbäddade.

Använd formatmallarna nedan. Namnen står som de heter i svensk Word, med det engelska namnet (python-docx) inom parentes.

| Formatmall | Storlek | Utseende | Använd till | Token (`type.print`) |
|---|---|---|---|---|
| **Inget avstånd** (`No Spacing`, alias `DocTitle`) | 36 pt | Roboto Condensed Medium, svart | Dokumentets titel, en gång på första sidan | `h1` |
| **Underrubrik** (`Subtitle`) | 22 pt | Roboto Condensed, textgrå, spärrad | Undertitel direkt under titeln | `subtitle` |
| **Rubrik 1** (`Heading 1`) | 18 pt | Roboto Condensed Medium, magenta | Avsnittsrubrik | `h2` |
| **Rubrik 2** (`Heading 2`) | 16 pt | Roboto Condensed, fet, svart | Underavsnitt | `h3` |
| **Rubrik 3** (`Heading 3`) | 14 pt | Roboto Condensed, fet | | `h4` |
| **Rubrik 4–6** (`Heading 4`–`6`) | 12 / 10 pt | Roboto Condensed, fet | Sällan | `h5`, `h6` |
| **Normal** (`Normal`) och **Brödtext** (`Body Text`) | 10 pt | Roboto, radavstånd 1,15 | All löptext | `body` |
| **Liststycke** (`List Paragraph`) | 10 pt | Roboto, indrag | Punkt- och nummerlistor | `body` |
| **Tabellformat** / **Tabellformat vänterjusterat** | 10 pt | Roboto, vänster- respektive högerjusterad | Text i tabellceller (högerjusterad för siffror) | `body` |
| Tabellformat **Magello – Default** (`List Table 4 Accent 5`) | 10 pt | Roboto, varannan rad färgad | Standardtabell | |
| Tabellformat **Magello – Summary** (`Grid Table 5 Dark Accent 5`) | 10 pt | Vänsterkolumn markerad, översta raden rubriker | Sammanställningar | |
| Tabellformat **Tabell 1** (`tabell 1`) | | Ingen formatering | Ren tabell | |
| **Rubrik** (`Title`, alias `Code`) | | Consolas | Kod i tekniska dokument | |

Observera att Words rubriknivåer ligger ett steg under styleguidens: Words **Rubrik 1** motsvarar H2 (magenta) och dokumenttiteln är formatmallen **Inget avstånd**. Formatmallen **Rubrik** (`Title`) har aliaset `Code` och är till för kod, inte för rubriker. **Titel** (42 pt fet) är bara bas för underrubriken och används inte direkt.

Ersätt platshållartexten "Dokument titel" på första sidan. Sidhuvudet hämtar titeln med fältet `STYLEREF DOCTITLE` och dagens datum med fältet `DATE`, så de uppdateras när fälten uppdateras (Cmd/Ctrl+A, F9). Skriv därför titeln med formatmallen **Inget avstånd** (`DocTitle`), annars blir sidhuvudet tomt.

## Kända avvikelser mot tokens

Mallarna är facit för hur Word och PowerPoint ser ut. Följande skiljer sig från `tokens/tokens.json`. Rätta dem i mallarna här, inte genom att formatera om enskilda dokument i efterhand. Använd mallens förvalda färger när du färgar former och text i ett Office-dokument, så att dokumentet blir enhetligt.

| Var | Mallen | Tokens |
|---|---|---|
| PowerPoint, temafärger | magenta `#EB008C`, blå `#009EE1`, röd `#E91739`, gul `#FDDB00`, grön `#08A45D`, lila `#CE00DE`, ingen orange | magenta `#EC008C`, blå `#31ABE2`, röd `#E3012F`, gul `#FFDC00`, grön `#1BA660`, orange `#F9B804`, ingen lila |
| PowerPoint, textfärg (dk1) | `#333333` | svart `#000000` |
| PowerPoint, ljus bakgrund (lt2) | `#F4EAEA` | rose-100 `#F4EBEB` |
| PowerPoint, brödtext | Roboto Medium (500) | Roboto 400 |
| PowerPoint, temats typsnitt | Aptos / Aptos Display (layouterna sätter Roboto, men text som klistras in kan få Aptos) | Roboto Condensed / Roboto |
| Word, magenta (accent5 och Rubrik 1) | `#E02B86` | `#EC008C` |
| Word, temats typsnitt | Arial | Roboto Condensed / Roboto |

Båda mallarna har specialtypsnittet **Kattux Abc 20** inbäddat, och PowerPoint-layouterna *Fokus - Rubrik på platta* och *Innehåll - Platta* använder det. Det är ett tillåtet undantag från typsnittsparet (D-45). Använd det bara för ett kort budskap i stor storlek, se `styleguide/typsnitt.html`.
