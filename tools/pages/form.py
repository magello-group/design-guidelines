import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TOK = json.loads((ROOT / "tokens" / "tokens.json").read_text())

PAGE = dict(
    title="Form", kicker="Grunder",
    lead="Magello ritar sina former som polygoner där inget är exakt rakt. Formen ger rörelse och skiljer Magello från alla som använder rundade eller perfekt rektangulära rutor.",
)


def poly_css(points):
    return "polygon(" + ", ".join(f"{x}% {y}%" for x, y in points) + ")"


def body(sg):
    compare = sg.demo(
        '<div class="sg-compare">'
        '<div><span class="sg-demo-label">Fel — perfekt rektangel</span><div class="sg-compare__fig sg-compare__fig--bad">Rak, industriell, anonym</div></div>'
        '<div><span class="sg-demo-label">Rätt — Magello-polygon</span><div class="sg-compare__fig sg-compare__fig--good">Levande, handgjord, igenkännbar</div></div>'
        '</div>', "plain")
    steps = ('<ol class="sg-steps-list">'
             '<li><strong>Börja med en rektangel.</strong> Den som innehållet skulle få utan formspråk.</li>'
             '<li><strong>Flytta varje hörn 2–7 %</strong> bort från sin exakta plats, i olika riktningar. Övre vänster kan sjunka 3 %, övre höger flytta 2 % in från kanten.</li>'
             '<li><strong>Lägg gärna till en femte eller sjätte punkt</strong> (ett avfasat hörn) för att ge formen riktning.</li>'
             '<li><strong>Kontrollera att ingen kant blev exakt vågrät eller lodrät.</strong> Då är den klar.</li></ol>')
    scale = sg.spec(["Storlek", "Exempel", "Avvikelse per hörn"],
                    [["Liten", "Etiketter, pills, ikonramar", "2–4 %"],
                     ["Medel", "Knappar, kort, infoblock", "2–6 %"],
                     ["Stor", "Sektioner, hero-plattor, bildytor", "3–8 %, gärna fler punkter"]])
    principle = sg.block("princip", "Princip", "Inga exakta kanter",
        "Hörnen avviker några procent från ett perfekt rätblock. Avvikelserna är medvetna och konsekventa, aldrig slumpmässiga.",
        compare + sg.sub("Så ritar du en ny form") + steps + sg.sub("Hur mycket ska formen avvika?") + scale +
        sg.code("""/* 5-hörnig knapp: inget hörn är 0% eller 100% på båda axlarna */
clip-path: polygon(2% 5%, 99% 0%, 100% 88%, 97% 100%, 0% 95%);

/* Fel: perfekt rektangel */
clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);"""))

    # katalog
    figs = []
    for name, spec in TOK["shape"]["polygons"].items():
        pts = poly_css(spec["points"])
        hov = f'--ph:{poly_css(spec["hover"])};' if spec.get("hover") else ""
        hover_note = " · hover öppnar formen" if spec.get("hover") else ""
        raw = " ".join(f"{x},{y}" for x, y in spec["points"])
        figs.append(f'<div class="sg-shape" tabindex="0"><div class="sg-shape__fig" style="--p:{pts};{hov}"></div>'
                    f'<div class="sg-shape__name">{name}</div><div class="sg-shape__use">{spec["use"]}{hover_note}</div>'
                    f'<div class="sg-shape__pts">{raw}</div></div>')
    catalog = sg.block("familj", "Formfamiljen", "Namngivna former",
        "Varje form har ett namn, ett användningsområde och koordinater i procent. Formerna finns som SVG i <code>assets/shapes/</code> och som värden i <code>tokens/tokens.json</code>. Håll muspekaren över en form som har hover-läge.",
        sg.demo('<div class="sg-shapes">' + "".join(figs) + '</div>', "white") +
        sg.text("Alla former visas här i rose-200. Faktisk fyllnadsfärg anges i <code>tokens.json</code> (<code>shape.polygons.*.fill</code>).") +
        sg.use(do=["Välj en befintlig form innan du skapar en ny", "Skapa en ny form som variant av en befintlig, med samma skalregel", "Låt stora element ha fler punkter än små"],
               dont=["Kopiera en form och ändra den så att den är nästan rak", "Använda samma form identiskt på alla element på en sida: växla mellan varianter", "Skära former så att text eller ansikten kapas"]),
        rose=True)

    hover = sg.block("hover", "Rörelse", "Formen öppnas vid hover",
        "När en klickbar polygon hovras blir den <em>mer rektangulär</em>. Den slappnar av. Den försvinner inte och byter inte färg dramatiskt.",
        sg.demo('<div class="sg-row"><a class="sg-hover-demo" href="#hover">Peka här</a>'
                '<a class="mg-btn mg-btn--primary" href="#hover">Primär knapp</a>'
                '<a class="mg-btn mg-btn--secondary" href="#hover">Sekundär knapp</a></div>') +
        sg.spec(["Läge", "Knapp (polygon)"],
                [["Vila", "<code>2% 5%, 99% 0%, 100% 88%, 97% 100%, 0% 95%</code>"],
                 ["Hover", "<code>0% 2%, 100% 0%, 99% 93%, 96% 100%, 1% 98%</code>"]]) +
        sg.use(do=["Animera <code>clip-path</code> 350–400 ms med <code>ease</code>", "Låt hover-formen ha samma antal punkter som vilo-formen", "Stäng av animationen med <code>prefers-reduced-motion</code>"],
               dont=["Rotera eller skala klickbara former vid hover", "Byta till rundade hörn vid hover", "Animera mer än en egenskap utöver bakgrundsfärg"]))

    media = sg.block("medier", "Andra medier", "Så använder du formerna utanför webben",
        "Formerna är geometri, inte CSS. I Word, PowerPoint, Figma och tryck byggs de som fria former (Freeform / Redigera punkter).",
        sg.spec(["Medium", "Gör så här"],
                [["PowerPoint, Keynote", "Utgå från <a href=\"powerpoint.html\">Powerpoint-mallen</a>, där layouterna redan har formerna. Behövs fler: importera SVG från <code>assets/shapes/</code> eller rita en Freeform med punkterna från <code>tokens.json</code>. Låt SVG:n sträckas (den har <code>preserveAspectRatio=\"none\"</code>)."],
                 ["Word, PDF", "Utgå från <a href=\"word.html\">Word-mallen</a>. Fler former finns sist i <code>Powerpoint-mall-howto.pptx</code> och i <code>Word-mall-howto.docx</code>, eller infoga SVG från <code>assets/shapes/</code> som bild."],
                 ["Figma, Illustrator", "Dra in SVG:erna. Koordinaterna är procent av en 100 × 100-ruta, skala till önskad storlek."],
                 ["Sociala medier, bilder", "Beskär foton med polygonerna <code>image-a/b/c</code>. Lägg text på en <code>plate</code>, inte direkt på fotot."],
                 ["Agent som genererar SVG", "Läs polygonerna ur <code>tokens/tokens.json</code> och skriv <code>&lt;polygon points=…&gt;</code> i en viewBox på 100 × 100."]]),
        rose=True)
    return principle + catalog + hover + media
