PAGE = dict(
    title="PowerPoint", kicker="Mallar",
    lead="Låt en AI-agent göra presentationen. Den följer Magellos formspråk och använder rätt mall. Vill du göra den själv utgår du från PowerPoint-mallen.",
    actions=[("Kom igång med AI", "#ai", "primary"),
             ("Ladda ned PowerPoint-mallen", "../assets/templates/Powerpoint-mall.potx", "secondary")],
)

T = "../assets/templates/"
DOCS = "https://github.com/magello-group/design-guidelines/blob/main/docs/"

LAYOUTS = [
    ["Förstasida", "Första bilden: rubrik, datum och svartvitt foto"],
    ["Innehåll - Grå bård", "Innehåll med bild eller grafik"],
    ["Innehåll - Enkel", "Text, tabeller, diagram och processer"],
    ["Sektion - Röd / Gul / Grön platta", "Avdelare mellan delar av presentationen"],
    ["Fokus - Rubrik vänster på bild", "Ett budskap över en helbild. Avslutning, ”Nästa steg”"],
    ["Fokus - Med innehåll", "Ett budskap med en kort förklarande text"],
    ["Fokus - Rubrik på platta", "Citat eller kort påstående på färgad platta"],
    ["Innehåll - Platta", "Kort text på färgad platta, gärna med grafik"],
    ["Bild - Stor bild", "Ett foto som fyller bilden"],
    ["Bilder - Flera", "Bildkollage, team, miljöer"],
    ["Tom utan rubrik", "Fri yta för diagram eller grafik"],
]


def downloads(items):
    return '<div class="mg-btn-row">' + "".join(
        f'<a class="mg-btn mg-btn--secondary" href="{T}{f}" download>{label}</a>' for label, f in items) + '</div>'


def body(sg):
    ai = sg.ai_start("ai",
        "Det enklaste och bästa sättet att göra en presentation. Agenten läser reglerna, frågar vad som saknas och lämnar en färdig .pptx. Du behöver inte installera eller köra något.",
        "Gör en PowerPoint-presentation om: ",
        title="Låt en AI-agent göra presentationen",
        example="vårt erbjudande inom Cloud, 10 bilder, till en kund i energibranschen")

    tracks = sg.block("tva-spar", "Med AI", "Agenten frågar vilket utseende du vill ha",
        "Det finns två sätt att göra en presentation. Agenten frågar alltid först. Vet du redan, skriv det direkt i texten till agenten.",
        sg.spec(["", "Mallen", "Webbens formspråk"], [
            ["Passar när", "Du själv ska ändra, byta bilder och lägga till bilder efteråt", "Agenten ska leverera en färdig presentation"],
            ["Utseende", "Mallens layouter, plattor och Kattux", "Signaturyta, stor typografi, helbilder och luft, som webben"],
            ["Ändra efteråt", "Enkelt, via layouterna", "Möjligt, men textrutor och former ligger fritt"],
            ["Skriv till agenten", "<em>Använd PowerPoint-mallen</em>", "<em>Använd webbens formspråk</em>"],
        ]) +
        sg.use(do=["Ge agenten innehållet: anteckningar, ett dokument eller en gammal presentation",
                   "Säg vem som ska se presentationen och hur lång den ska vara",
                   "Be om PDF också om mottagaren kan sakna typsnitten"],
               dont=["Be agenten ”göra det snyggt” utan underlag",
                     "Ändra färger eller typsnitt i efterhand"],
               note=["Agentens instruktioner står i <a href='" + DOCS + "office-mallar.md'><code>office-mallar.md</code></a> och <a href='" + DOCS + "presentation-webb.md'><code>presentation-webb.md</code></a>"]))

    manual = sg.block("sjalv", "Utan AI", "Gör presentationen själv",
        "Det fungerar likadant på Mac och PC.",
        sg.demo(sg.steps("Ladda ned mallen", "Dubbelklicka på filen", "Spara som vanligt")) +
        '<ol class="sg-text"><li>Ladda ned mallen.</li>'
        '<li>Dubbelklicka på filen. PowerPoint öppnar en ny presentation som bygger på mallen.</li>'
        '<li>Skriv, och spara som vanligt. Mallen ändras inte.</li></ol>' +
        downloads([("PowerPoint-mallen", "Powerpoint-mall.potx"), ("PowerPoint-instruktion", "Powerpoint-mall-howto.pptx")]) +
        sg.use(do=["Använd mallens layouter under <em>Ny bild</em>",
                   "Var sparsam med färg. Behövs en accent, välj magenta",
                   "Byt exempelbilderna mot svartvita foton från <a href=\"bildbank.html\">Bildbanken</a>"],
               dont=["Börja från en tom presentation",
                     "Byta typsnitt eller färger på rubriker och brödtext",
                     "Färgfoton eller egna former med raka hörn"],
               note=["Instruktionen visar mallen i bruk. Grafik och bakgrundsformer att kopiera finns sist i den",
                     "Rubriken på färgad platta använder <a href=\"typsnitt.html\">specialtypsnittet Kattux</a>. Använd det bara för ett kort budskap"]),
        rose=True)

    layouts = sg.block("layouter", "Utan AI", "Välj rätt layout",
        "Välj layout under <em>Ny bild</em>. En presentation börjar med Förstasida och slutar gärna med Fokus - Rubrik vänster på bild.",
        sg.spec(["Layout", "Använd till"], LAYOUTS))

    return ai + tracks + manual + layouts
