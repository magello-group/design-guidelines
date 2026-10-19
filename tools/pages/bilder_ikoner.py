import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TOK = json.loads((ROOT / "tokens" / "tokens.json").read_text())

PAGE = dict(
    title="Bilder &amp; ikoner", h1="Bilder<br>&amp; ikoner", kicker="Grunder",
    lead="Foton är alltid svartvita och beskurna i polygoner. Ikonerna bär färgen. Tillsammans ger de lugn med en tydlig accent.",
)

IMG = "../assets/images/black-and-white/"


def body(sg):
    poly = sg.demo(
        '<div class="mg-poly-grid">'
        f'<img class="mg-poly-img mg-poly-img--a" src="{IMG}kontor-1.jpg" alt="Kontorsmiljö">'
        f'<img class="mg-poly-img mg-poly-img--b" src="{IMG}kontor-10.jpg" alt="Samarbete">'
        f'<img class="mg-poly-img mg-poly-img--c" src="{IMG}event-1.jpg" alt="Event"></div>', "plain")
    photos = sg.block("foton", "Foton", "Svartvita foton i polygonform",
        "Ingen färgkorrigering utöver gråskala och lätt kontrast. Beskär alltid i en polygon, aldrig en perfekt rektangel.",
        poly + sg.code('''img { filter: grayscale(1) contrast(1.05); }
.mg-poly-img--a { clip-path: polygon(7% 0%, 94% 2%, 100% 10%, 98% 90%, 93% 100%, 5% 97%, 0% 88%, 2% 8%); }''') +
        sg.use(do=["Använd verkliga människor och miljöer: kontor, möten, skärmar, whiteboards, händelser", "Välj lugna kompositioner med plats för text", "Växla polygon A/B/C mellan bilder på samma sida", "Skriv en alt-text som beskriver vad bilden visar"],
               dont=["Färgfoton, färgfilter eller dubbeltoner", "Stockkänsla: leende modeller vid skrivbord", "Perfekt rektangulära beskärningar", "Text direkt på ett livligt foto"],
               note=["Ladda gärna upp färgfoton i ett CMS. Svartvitt och polygonbeskärning läggs på av CSS", "Bildbiblioteket ligger i <code>assets/images/black-and-white/</code>"]))

    plate = sg.block("platta", "Text på foto", "Vit platta över bilden",
        "Text läggs aldrig direkt på fotot. Den ligger på en vit polygonplatta med åtta hörn, som en pappersflik ovanpå bilden.",
        sg.demo(f'''<div class="mg-img-block" style="padding-bottom:0"><div class="mg-img-block__frame">
<img class="mg-img-block__bg" src="{IMG}dator-1.jpg" alt="Magello kontor">
<div class="mg-img-block__plate"><p class="mg-kicker">Expertisområde</p><h2>Vi hjälper kunder bygga fungerande mjukvara</h2><p>Professionella, avskalade, tydliga och lite lekfulla</p><a href="#platta" class="mg-btn mg-btn--primary">Läs mer</a></div></div></div>''', "plain") +
        sg.code('''<div class="mg-img-block"><div class="mg-img-block__frame">
  <img class="mg-img-block__bg" src="…jpg" alt="…">
  <div class="mg-img-block__plate">
    <p class="mg-kicker">Expertisområde</p>
    <h2>Rubrik</h2><p>Text</p>
    <a class="mg-btn mg-btn--primary" href="#">Knapp</a>
  </div></div></div>''') +
        sg.use(do=["Plattan har kicker, rubrik, kort text och högst en knapp", "Låt bilden synas på minst halva ytan"],
               dont=["Fylla plattan med mer än fyra rader text", "Lägga två plattor på samma bild"]), rose=True)

    people = sg.block("personer", "Personbilder", "Runda och svartvita",
        "Profilbilder och porträtt är det enda stället där cirkelformen används.",
        sg.demo(f'<div class="sg-row"><img class="sg-avatar" src="{IMG}kontor-1.jpg" alt=""><img class="sg-avatar" src="{IMG}kontor-3.jpg" alt=""><img class="sg-avatar" src="{IMG}kontor-12.jpg" alt=""></div>') +
        sg.use(do=["Svartvit, rund, ansiktet centrerat", "Minst 80 px på webben"], dont=["Kvadratiska eller rundade rektangulära porträtt", "Färgade porträtt", "Cirklar för något annat än personer"]))

    icons = []
    for name, spec in TOK["icons"].items():
        icons.append(f'<div class="sg-icon"><img src="../assets/{spec["file"]}" alt=""><div class="sg-icon__name">{name}</div><div class="sg-icon__meaning">{spec["color"]} · {spec["meaning"]}</div></div>')
    icon_block = sg.block("ikoner", "Ikoner", "Platta vektorer i full färg",
        "Ikonerna är handritade, organiska och platta. Färgen väljs efter ikonens betydelse, inte efter var den hamnar.",
        sg.demo('<div class="sg-icons">' + "".join(icons) + "</div>", "white") +
        sg.spec(["Kontext", "Storlek"],
                [["Fristående blickfång (ikonrad)", "72 × 72 px"], ["Kort och erbjudanden", "40 × 40 px"], ["Inline i text, sidospalt", "24–32 px"], ["Citattecken (<code>citation.svg</code>)", "40 × 35 px, endast som dekor i citat"]]) +
        sg.use(do=["Visa ikoner i full färg och full styrka", "Max 2–3 färger per ikon", "Ladda ikoner som <code>&lt;img&gt;</code> med <code>alt=\"\"</code> när de är dekorativa", "Välj färg efter betydelse: blå teknik, grön dialog och godkänt, röd tid, gul idé"],
               dont=["Opacity, gråskala eller mörkare filter på ikoner", "Gradienter, skuggor eller kantlinje på ikoner", "Att byta färg på en ikon för att den ska passa en sida", "Magentafärgade ikoner utanför värdeorden"],
               note=["Värdeordens ikoner (<code>personliga</code>, <code>trygga</code>, <code>kommunikativa</code>, <code>lärande</code>) används bara när Magello som bolag beskrivs", "Nya ikoner: SVG, solida fills, inga effekter, ritade för vit, rose-50 och rose-100 bakgrund"]), rose=True)
    return photos + plate + people + icon_block
