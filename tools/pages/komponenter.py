PAGE = dict(
    title="Komponenter", kicker="Byggstenar",
    lead="Knappar, kort, processteg, citat, tabeller och mer. Varje komponent visas levande, med när den ska användas, när den inte ska det och markupen att kopiera.",
)

IMG = "../assets/images/black-and-white/"
GR = "../assets/graphics/"


def body(sg):
    # ---------------------------------------------------------- knappar
    buttons = sg.block("knappar", "Komponent", "Knappar",
        "Fem hörn, ingen kant exakt rak. Knappens färg speglar vad den gör: primär (magenta) för huvudhandlingen, sekundär (rosa) för det som backar eller kompletterar.",
        sg.demo('<div class="sg-row"><a class="mg-btn mg-btn--primary" href="#knappar">Prata med oss</a>'
                '<a class="mg-btn mg-btn--secondary" href="#knappar">Vad vi erbjuder</a>'
                '<button class="mg-btn mg-btn--primary" disabled>Inaktiv</button></div>') +
        sg.code('''<a class="mg-btn mg-btn--primary" href="#">Prata med oss</a>
<a class="mg-btn mg-btn--secondary" href="#">Vad vi erbjuder</a>''') +
        sg.spec(["Klass", "Utseende", "Används till"],
                [["<code>.mg-btn--primary</code>", "Magenta, vit text", "Skapa, spara, skicka, kontakta. Huvudhandlingen i vyn"],
                 ["<code>.mg-btn--secondary</code>", "Rose-200, svart text (hover rose-300)", "Avbryt, återställ, ”vad vi erbjuder”. Kompletterar den primära"],
                 ["<code>.mg-btn--icon</code>", "Lägger ikon + text i rad (<code>inline-flex</code>, 8 px mellanrum)", "Knappar med ikon till vänster om texten"]]) +
        sg.use(do=["Högst <strong>en</strong> primär knapp per vy", "Primär först, sekundär efter (eller under i staplat läge)", "Skriv ett verb som beskriver handlingen: ”Prata med oss”", "Fokus syns som 3 px kontur med 4 px avstånd"],
               dont=["Knapp med kant och utan fyllnad (outline)", "Flera magenta knappar bredvid varandra", "Versaler eller utropstecken i knapptexten", "Rundade hörn"]))

    # ---------------------------------------------------------- kort
    cards = sg.block("kort", "Komponent", "Kort",
        "Kortvarianten väljs efter innehållet: bild ger bildkort, ikon ger erbjudandekort, annars textkort. Alla är polygoner utan kant och skugga.",
        sg.sub("Textkort") +
        sg.demo('<div class="mg-card-grid">'
                '<article class="mg-card mg-card--text"><h3>Förstudier &amp; PoC</h3><p>Grunden för en lyckad digital lösning läggs tidigt. Vi bygger och testar en Proof of Concept som validerar teknik och affärsnytta.</p></article>'
                '<article class="mg-card mg-card--text"><h3>UX &amp; Tillgänglighet</h3><p>Vi kombinerar design med data för att skapa intuitiva gränssnitt som människor faktiskt kan och vill använda.</p></article>'
                '</div>', "white") +
        sg.code('''<div class="mg-card-grid">
  <article class="mg-card mg-card--text"><h3>Rubrik</h3><p>Text …</p></article>
</div>''') +
        sg.sub("Bildkort") +
        sg.demo(f'<div class="mg-card-grid mg-card-grid--loose"><div class="mg-card mg-card--image"><img class="mg-card__img" src="{IMG}dator-1.jpg" alt="Systemarkitektur">'
                '<div class="mg-card__body"><div class="mg-card__kicker"><span class="mg-kicker">Backend &amp; moln</span></div><h3>Systemarkitektur</h3><p>Vi designar skalbara system som håller.</p></div></div>'
                f'<div class="mg-card mg-card--image"><img class="mg-card__img" src="{IMG}whiteboard-2-.jpg" alt="Agila leveranser"><div class="mg-card__body"><div class="mg-card__kicker"><span class="mg-kicker">Agile</span></div><h3>Agila leveranser</h3><p>Korta cykler och tydlig dialog.</p></div></div></div>', "white") +
        sg.sub("Erbjudandekort", "Rosa yta med ikon. Hover öppnar formen och går ett steg mörkare.") +
        sg.demo(f'<div class="mg-offer-grid"><div class="mg-offer-card"><div class="mg-offer-card__icon"><img src="{GR}light.svg" alt=""></div><div class="mg-offer-card__body"><h3 class="mg-offer-card__title">AI &amp; Automation</h3><p class="mg-offer-card__desc">Omsätt AI och automation till verklig affärsnytta.</p><a class="mg-offer-card__link" href="#kort">Läs mer →</a></div></div>'
                f'<div class="mg-offer-card"><div class="mg-offer-card__icon"><img src="{GR}nodes.svg" alt=""></div><div class="mg-offer-card__body"><h3 class="mg-offer-card__title">Cloud</h3><p class="mg-offer-card__desc">Azure, AWS, GCP och private clouds.</p><a class="mg-offer-card__link" href="#kort">Läs mer →</a></div></div></div>') +
        sg.sub("Kompakt kort och värdekort") +
        sg.demo(f'<div class="mg-card-grid mg-card-grid--three" style="margin:0"><div class="mg-card mg-card--compact"><span class="mg-card__label">Consulting</span><h3>Expertis i uppdrag</h3><p>Seniora konsulter som tar ägarskap.</p></div>'
                '<div class="mg-card mg-card--compact"><span class="mg-card__label">Solutions</span><h3>Färdiga lösningar</h3><p>Bygger på beprövade metoder.</p></div>'
                '<div class="mg-card mg-card--compact"><span class="mg-card__label">Team</span><h3>Agila team</h3><p>Anpassar sig efter ert behov.</p></div></div>', "white") +
        sg.demo(f'<div class="mg-values" style="margin:0"><div class="mg-value-card"><span class="mg-value-card__icon"><img src="{GR}värdeord/personliga.svg" alt=""></span><span class="mg-value-card__word">Personliga</span><p>Vi lyssnar och anpassar oss efter varje kunds situation.</p></div>'
                f'<div class="mg-value-card"><span class="mg-value-card__icon"><img src="{GR}värdeord/trygga.svg" alt=""></span><span class="mg-value-card__word">Trygga</span><p>Stabil leverans med seniora konsulter.</p></div></div>', "white") +
        sg.spec(["Kort", "Klasser", "Yta", "Används till"],
                [["Textkort", "<code>.mg-card.mg-card--text</code>", "Vit", "Expertisområden, tjänster"],
                 ["Bildkort", "<code>.mg-card.mg-card--image</code>", "Vit", "Expertis med foto"],
                 ["Kompakt kort", "<code>.mg-card.mg-card--compact</code>", "Vit", "Tre korta fakta i rad"],
                 ["Erbjudandekort", "<code>.mg-offer-card</code>", "Rosa 50", "Erbjudanden med ikon, hover"],
                 ["Värdekort", "<code>.mg-value-card</code>", "Rosa 100", "Värdeord med ikon"],
                 ["Rutnät", "<code>.mg-card-grid</code> (<code>--loose</code>, <code>--three</code>)", "—", "Placerar kort"]]) +
        sg.use(do=["Rubrik (H3) och en kort text per kort", "Lägg vita kort på rosa sektion, eller använd rosa kort när formen ska synas", "Ny variant = modifier på <code>.mg-card</code>, inte en ny komponent"],
               dont=["Löpnummer (01, 02, 03) som dekor", "Skugga eller kant runt kortet", "Fler än ett budskap per kort", "Kort i kort"]), rose=True)

    # ---------------------------------------------------------- steg
    steps = sg.block("steg", "Komponent", "Processteg",
        "Kedjade chevrons som visar ett förlopp. Stegen avlöser varandra i accentfärger. Det sista steget är alltid magenta.",
        sg.demo('<div class="mg-steps" role="list">'
                '<div class="mg-step mg-step--blue" role="listitem"><span class="mg-step__num">Fas 1</span>Uppstartsfasen</div>'
                '<div class="mg-step mg-step--orange" role="listitem"><span class="mg-step__num">Fas 2</span>Utvecklingsfasen</div>'
                '<div class="mg-step mg-step--green" role="listitem"><span class="mg-step__num">Fas 3</span>Leveransfasen</div>'
                '<div class="mg-step mg-step--magenta" role="listitem"><span class="mg-step__num">Fas 4</span>Förvaltning</div></div>') +
        sg.code('''<div class="mg-steps" role="list">
  <div class="mg-step mg-step--blue" role="listitem"><span class="mg-step__num">Fas 1</span>Uppstart</div>
  <div class="mg-step mg-step--magenta" role="listitem"><span class="mg-step__num">Fas 2</span>Klar</div>
</div>''') +
        sg.spec(["Antal steg", "Färgordning"],
                [["2", "blå, magenta"], ["3", "blå, orange, magenta"], ["4", "blå, orange, grön, magenta"], ["6", "blå, orange, röd, gul, grön, magenta"]]) +
        sg.use(do=["Sista steget i magenta", "2–6 steg", "Ett litet ”Steg n” eller ”Fas n” ovanför namnet"],
               dont=["Magenta i mitten av kedjan", "Fler än sex steg", "Långa meningar i stegen"]))

    # ---------------------------------------------------------- citat / rutor
    quote = sg.block("citat", "Komponent", "Citat, infoblock och textruta",
        "Tre sätt att lyfta något ur löptexten. Alla placeras i textflödet, i full bredd, och aldrig i en smal kolumn bredvid texten.",
        sg.sub("Citat") +
        sg.demo('<div class="mg-pullquote"><p>Vi är generalister med spetskompetens och är inte begränsade till specifika produkter eller metodiker.</p></div>', "plain") +
        sg.sub("Infoblock", "Rosa faktaruta med magenta etikett. Flera block läggs efter varandra.") +
        sg.demo('<div class="mg-infoblock" style="margin:0"><span class="mg-infoblock__label">Våra expertisområden</span><ul><li><strong>Digitala tjänster</strong> — från idé till robust digital produkt</li><li><strong>Integration</strong> — knyta ihop affärsprocesser</li><li><strong>Cloud</strong> — skalbara och kostnadseffektiva molnlösningar</li></ul></div>', "white") +
        sg.sub("Textruta (callout)", "Pappersflik uppe till höger. Kort text, gärna med en stor siffra eller symbol som blickfång.") +
        sg.demo('<div class="mg-callout"><p class="mg-callout__title">Vi söker nya medarbetare</p><p>Är du en erfaren systemutvecklare som vill jobba med oss? Hör av dig!</p></div>', "white") +
        sg.use(do=["Ett citat per vy. Det är ett utdrag, inte en puffruta", "Infoblock efter varandra i full bredd, formade som den rosa rutan", "Siffror (”Magello i siffror”) i en rad inne i rutan"],
               dont=["Högerställda informationsrutor som texten viker undan för", "Kantlinje till vänster om ett citat", "Citattecknet som fristående ikon eller med opacity", "Fler än tre rutor i rad"],
               note=["Ingress och brödtext går alltid i 100 % bredd. Texten återgår till full bredd efter varje ruta"]), rose=True)

    # ---------------------------------------------------------- tabell
    table = sg.block("tabell", "Komponent", "Tabell",
        "Rubrikraden är rosa, varannan rad är tonad och första kolumnen är fet. Linjerna i cellerna är funktionella hårlinjer i rosagrått.",
        sg.demo('<div class="mg-table-wrap"><table class="mg-table"><thead><tr><th>Kompetens</th><th>Nivå</th><th>Certifieringar</th><th>Tillgänglig</th></tr></thead><tbody>'
                '<tr><td>Systemarkitektur</td><td>Senior</td><td>TOGAF, AWS SA</td><td>Omgående</td></tr>'
                '<tr><td>Backend / Java</td><td>Senior</td><td>Oracle Java SE</td><td>2026-Q1</td></tr>'
                '<tr><td>Testautomatisering</td><td>Mid</td><td>ISTQB</td><td>Omgående</td></tr></tbody>'
                '<tfoot><tr><td colspan="4">3 konsulter · Uppdaterad 2026-10-19</td></tr></tfoot></table></div>', "plain") +
        sg.use(do=["Lägg tabellen i <code>.mg-table-wrap</code> så den scrollar sidledes på mobil", "Vänsterjustera text, högerjustera siffror", "Använd <code>&lt;tfoot&gt;</code> för summering"],
               dont=["Mörka linjer eller accentfärgade linjer", "Tabeller för layout", "Fler än sex kolumner på mobil utan scroll"]))

    # ---------------------------------------------------------- tidslinje
    timeline = sg.block("tidslinje", "Komponent", "Tidslinje",
        "Årtal i grått, diamantmarkörer i rosa och den nuvarande punkten markerad med magenta fyllnad.",
        sg.demo('<div class="mg-timeline" role="list">'
                '<div class="mg-timeline-item" role="listitem"><span class="mg-timeline-item__year">1996</span><p class="mg-timeline-item__text">Bolaget grundades i Linköping.</p></div>'
                '<div class="mg-timeline-item" role="listitem"><span class="mg-timeline-item__year">2015</span><p class="mg-timeline-item__text">Red Hat utser oss till European Business Partner of the Year.</p></div>'
                '<div class="mg-timeline-item mg-timeline-item--highlight" role="listitem"><span class="mg-timeline-item__year">2026</span><p class="mg-timeline-item__text">Magello fyller 30 år.</p></div></div>', "plain") +
        sg.use(do=["Bakgrund rosagrå 50 för hela sektionen", "Markera nuvarande år med <code>--highlight</code>", "En mening per punkt"],
               dont=["Svart bakgrund", "Fler än tolv punkter i rad"],
               note=["Den lodräta linjen bör vara platt rose-200. I referenssajten är den ännu magenta med gradient (känd avvikelse)"]), rose=True)

    # ---------------------------------------------------------- kontakt
    contact = sg.block("kontakt", "Komponent", "Kontaktkort och uppmaning",
        "Person med foto och kontaktuppgifter, och en avslutande uppmaning med en primär knapp.",
        sg.demo(f'<div class="mg-contact-card"><img class="mg-contact-card__photo" src="{IMG}kontor-1.jpg" alt=""><div><p class="mg-contact-card__name">Anna Karlsson</p><p class="mg-contact-card__title">Konsultchef</p><div class="mg-contact-card__links"><a href="mailto:anna@magello.se">anna@magello.se</a><a href="tel:+46800000000">+46 8 000 00 00</a></div></div></div>', "white") +
        sg.demo('<section class="mg-cta" style="padding-block:0"><div class="mg-cta__inner" style="padding-inline:0"><h2 class="mg-cta__heading">Redo att ta nästa steg?</h2><p class="mg-cta__text">Oavsett om ni vill utforska ett specifikt område eller diskutera en bredare utmaning — vi lyssnar gärna.</p><a class="mg-btn mg-btn--primary" href="#kontakt">Kontakta oss</a></div></section>', "plain") +
        sg.use(do=["Kontaktkort: namn, titel, e-post, telefon. Foto svartvitt", "Uppmaning: rubrik, en kort text och en primär knapp", "Placera uppmaningen sist på sidan, före sidfoten"],
               dont=["Mer än en primär handling i uppmaningen", "Färgfoto i kontaktkortet"]))
    return buttons + cards + steps + quote + table + timeline + contact
