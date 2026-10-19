PAGE = dict(
    title="Word och PowerPoint", kicker="Mallar",
    lead="Word-dokument och presentationer från Magello utgår alltid från Magellos mallar. Ladda ned mallen, dubbelklicka och börja skriva.",
    actions=[("Ladda ned PowerPoint-mallen", "../assets/templates/Powerpoint-mall.potx", "primary"),
             ("Ladda ned Word-mallen", "../assets/templates/Word-mall.dotx", "secondary")],
)

T = "../assets/templates/"

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


def steps(*items):
    colors = ["blue", "orange", "green"][:len(items) - 1] + ["magenta"]
    return ('<div class="mg-steps" role="list">' + "".join(
        f'<div class="mg-step mg-step--{c}" role="listitem"><span class="mg-step__num">Steg {i}</span>{t}</div>'
        for i, (c, t) in enumerate(zip(colors, items), 1)) + '</div>')


def downloads(items):
    return '<div class="mg-btn-row">' + "".join(
        f'<a class="mg-btn mg-btn--secondary" href="{T}{f}" download>{label}</a>' for label, f in items) + '</div>'


def body(sg):
    manual = sg.block("sa-gor-du", "Så gör du", "Skapa ett dokument ur mallen",
        "Det fungerar likadant på Mac och PC.",
        sg.demo(steps("Ladda ned mallen", "Dubbelklicka på filen", "Spara som vanligt")) +
        '<ol class="sg-text"><li>Ladda ned mallen.</li>'
        '<li>Dubbelklicka på filen. Word eller PowerPoint öppnar ett nytt dokument som bygger på mallen.</li>'
        '<li>Skriv, och spara som vanligt. Mallen ändras inte.</li></ol>' +
        downloads([("PowerPoint-mallen", "Powerpoint-mall.potx"), ("Word-mallen", "Word-mall.dotx")]))

    howto = sg.block("howto", "Instruktioner", "Se hur mallen används",
        "Ladda ned och öppna. Dokumenten visar steg för steg hur mallen används, med exempel du kan kopiera.",
        downloads([("PowerPoint-instruktion", "Powerpoint-mall-howto.pptx"), ("Word-instruktion", "Word-mall-howto.docx")]) +
        sg.use(do=["Skriv titeln med formatmallen DocTitle, så hamnar den i sidhuvudet",
                   "Använd mallens formatmallar och layouter",
                   "Var sparsam med färg. Behövs en accent, välj magenta",
                   "Byt exempelbilderna mot egna svartvita foton"],
               dont=["Börja från ett tomt dokument",
                     "Byta typsnitt eller färger på rubriker och brödtext",
                     "Färgfoton eller egna former med raka hörn",
                     "Klistra in med formatering från andra dokument. Klistra in som text"],
               note=["Grafiken i Words sidhuvud ändras från sida två. Datumet uppdateras av sig självt",
                     "Grafik och bakgrundsformer att kopiera finns sist i PowerPoint-instruktionen",
                     "Rubriken på färgad platta använder <a href=\"typsnitt.html\">specialtypsnittet Kattux</a>. Använd det bara för ett kort budskap"]), rose=True)

    layouts = sg.block("layouter", "PowerPoint", "Välj rätt layout",
        "Välj layout under <em>Ny bild</em>. En presentation börjar med Förstasida och slutar gärna med Fokus - Rubrik vänster på bild.",
        sg.spec(["Layout", "Använd till"], LAYOUTS))

    styles = sg.block("formatmallar", "Word", "Välj rätt formatmall",
        "Formatmallarna finns under <em>Start</em>. Tabellformaten finns under <em>Tabelldesign</em>.",
        sg.spec(["Formatmall", "Använd till"], STYLES), rose=True)

    tracks = sg.block("tva-spar", "PowerPoint", "Två sätt att göra en presentation",
        "Agenten frågar alltid först vilket spår du vill ha. Välj mallen om du själv ska ändra och bygga vidare. "
        "Välj webbens formspråk om agenten ska leverera en färdig presentation som ser ut som webben.",
        sg.spec(["", "Spår A: PowerPoint-mallen", "Spår B: webbens formspråk"], [
            ["Passar när", "Du själv ska ändra, byta bilder och lägga till bilder", "En agent ska bygga hela presentationen"],
            ["Utgår från", "<code>Powerpoint-mall.potx</code>, layouter och platshållare", "En tom 16:9-presentation och tokens"],
            ["Utseende", "Mallens layouter, plattor och Kattux", "Signaturyta, stor typografi, helbilder och luft, som webben"],
            ["Ändra efteråt", "Enkelt, via layouterna", "Möjligt, men textrutor och former ligger fritt"],
            ["Instruktion", "<a href='https://github.com/magello-group/design-guidelines/blob/main/docs/office-mallar.md'><code>docs/office-mallar.md</code></a>",
             "<a href='https://github.com/magello-group/design-guidelines/blob/main/docs/presentation-webb.md'><code>docs/presentation-webb.md</code></a>"],
        ]) +
        sg.code("""Läs https://github.com/magello-group/design-guidelines/blob/main/AGENTS.md.
Gör en presentation om vårt erbjudande inom moln i webbens formspråk (spår B).""") +
        sg.use(do=["Säg vilket spår du vill ha, annars frågar agenten",
                   "Spår B: rubriker i svart, rosagrått bara där något ska sticka ut",
                   "Spår B: be om PDF om mottagaren saknar Roboto"],
               dont=["Blanda spåren i samma presentation",
                     "Magenta rubriker i spår B"]))

    agent = sg.block("agent", "Med agent", "Låt en agent göra dokumentet",
        "Be agenten läsa <a href='https://github.com/magello-group/design-guidelines/blob/main/AGENTS.md'><code>AGENTS.md</code></a>. Agenten skapar själv ett dokument ur mallen, använder layouterna och formatmallarna och lämnar en vanlig .pptx eller .docx. Du behöver inte köra något.",
        sg.code("""Läs https://github.com/magello-group/design-guidelines/blob/main/AGENTS.md.
Gör en presentation om vårt erbjudande inom moln utifrån Magellos PowerPoint-mall (spår A). Börja med Förstasida och avsluta
med Fokus - Rubrik vänster på bild. Använd svartvita foton.""") +
        sg.text("Detaljerna för agenter, och var mallarna avviker från tokens, står i <a href='https://github.com/magello-group/design-guidelines/blob/main/docs/office-mallar.md'><code>docs/office-mallar.md</code></a>."))

    return manual + howto + tracks + layouts + styles + agent
