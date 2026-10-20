PAGE = dict(
    title="Word", kicker="Mallar",
    lead="Word-dokument från Magello utgår alltid från Magellos mall. Ladda ned mallen, dubbelklicka och börja skriva.",
    actions=[("Ladda ned Word-mallen", "../assets/templates/Word-mall.dotx", "primary"),
             ("Ladda ned instruktionen", "../assets/templates/Word-mall-howto.docx", "secondary")],
)

T = "../assets/templates/"

STYLES = [
    ["DocTitle (Inget avstånd)", "Dokumentets titel. Den hamnar också i sidhuvudet"],
    ["Underrubrik", "Undertitel direkt under titeln"],
    ["Rubrik 1", "Avsnittsrubrik, magenta"],
    ["Rubrik 2–4", "Underavsnitt"],
    ["Normal", "All löptext"],
    ["Liststycke", "Punkt- och nummerlistor"],
    ["Code (Rubrik)", "Kod i tekniska dokument"],
    ["Tabell: Magello – Default", "Standardtabell, varannan rad färgad"],
    ["Tabell: Magello – Summary", "Vänsterkolumn och översta raden markerade"],
]


def downloads(items):
    return '<div class="mg-btn-row">' + "".join(
        f'<a class="mg-btn mg-btn--secondary" href="{T}{f}" download>{label}</a>' for label, f in items) + '</div>'


def body(sg):
    manual = sg.block("sa-gor-du", "Så gör du", "Skapa ett dokument ur mallen",
        "Det fungerar likadant på Mac och PC.",
        sg.demo(sg.steps("Ladda ned mallen", "Dubbelklicka på filen", "Spara som vanligt")) +
        '<ol class="sg-text"><li>Ladda ned mallen.</li>'
        '<li>Dubbelklicka på filen. Word öppnar ett nytt dokument som bygger på mallen.</li>'
        '<li>Skriv, och spara som vanligt. Mallen ändras inte.</li></ol>' +
        downloads([("Word-mallen", "Word-mall.dotx"), ("Word-instruktion", "Word-mall-howto.docx")]))

    rules = sg.block("regler", "Instruktion", "Se hur mallen används",
        "Instruktionen visar steg för steg hur mallen används, med exempel du kan kopiera.",
        sg.use(do=["Skriv titeln med formatmallen DocTitle, så hamnar den i sidhuvudet",
                   "Använd mallens formatmallar",
                   "Var sparsam med färg. Behövs en accent, välj magenta",
                   "Använd svartvita foton från <a href=\"bildbank.html\">Bildbanken</a>"],
               dont=["Börja från ett tomt dokument",
                     "Byta typsnitt eller färger på rubriker och brödtext",
                     "Färgfoton eller egna former med raka hörn",
                     "Klistra in med formatering från andra dokument. Klistra in som text"],
               note=["Grafiken i sidhuvudet ändras från sida två. Datumet uppdateras av sig självt"]),
        rose=True)

    styles = sg.block("formatmallar", "Formatmallar", "Välj rätt formatmall",
        "Formatmallarna finns under <em>Start</em>. Tabellformaten finns under <em>Tabelldesign</em>.",
        sg.spec(["Formatmall", "Använd till"], STYLES))

    agent = sg.ai_start("ai",
        "En AI-agent kan också skriva dokumentet åt dig. Den utgår från Word-mallen och använder formatmallarna.",
        "Skriv ett Word-dokument om: ",
        label="Med AI", title="Låt en AI-agent skriva dokumentet",
        example="en offert på ett integrationsprojekt, två sidor")

    return manual + rules + styles + agent
