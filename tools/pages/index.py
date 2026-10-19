PAGE = dict(
    title="Magellos formspråk", kicker="Styleguide", h1="Magellos<br>formspråk",
    lead="Så ser Magello ut, och hur du använder färg, form och komponenter. För människor och AI-agenter som skapar webb, dokument, presentationer och sociala medier.",
    actions=[("Börja med principerna", "#principer", "primary"), ("Ladda ner tokens", "../tokens/tokens.json", "secondary")],
)

PRINCIPLES = [
    ("1. Inga linjer som avgränsare", "Struktur skapas av luft, bakgrundsskiften och former. En linje säger att något slutar, en form säger att något börjar."),
    ("2. Accentfärger är fyllnad", "Magenta, blå, orange, grön, röd och gul fyller former, ikoner, knappar och text. De ritas aldrig som streck eller kant."),
    ("3. Former har rörelse", "Ingen synlig kant är exakt vågrät eller lodrät. Hörnen avviker 2–7 % från ett rätblock, så det ser handgjort ut."),
    ("4. Svartvitt utom varumärket", "Foton är alltid svartvita. Då får magenta och ikonernas färger hela scenen."),
    ("5. Rosagrått är kärnan", "Svart text på vitt är grunden. Den rosagrå paletten ger värme och struktur. Magenta används sparsamt och med avsikt."),
    ("6. Signaturytan", "En rosagrå yta med lutande kant. Det mest igenkännbara elementet. Används överst på landningsytor, inte överallt."),
    ("7. Luft och en gemensam linje", "Generöst ovanför rubriker, tätare under. Allt innehåll delar vänsterkant med logotypen."),
]


def body(sg):
    cards = "".join(f'<article class="mg-card mg-card--text"><h3>{t}</h3><p>{d}</p></article>' for t, d in PRINCIPLES)
    intro = sg.block("om", "Om styleguiden", "Ett formspråk, flera medier",
        "Magello är professionellt och avskalat, men inte stelt. Allvaret ligger i typografin, luften och den dämpade färgskalan. Lekfullheten ligger i formerna.",
        sg.text("Styleguiden är uppdelad i <strong>Grunder</strong> (färg, form, typografi, bilder, avstånd), <strong>Byggstenar</strong> (komponenter, sektioner, formulär, Markdown) och <strong>Navigation</strong>. Varje sida visar hur något ser ut, <em>när</em> det ska användas och när det inte ska det.")
        + sg.text("Allt du ser på sidorna är byggt med samma CSS som ska användas i andra projekt: <code>css/magello.css</code> och <code>js/magello.js</code>. Du kan alltså kopiera markup direkt från exemplen."))
    principles = sg.block("principer", "Utgångspunkt", "Sju principer",
        "Alla regler i styleguiden följer av de här sju. Saknar du ett mönster: härled från principerna i stället för att hitta på något som bryter mot dem.",
        f'<div class="mg-card-grid">{cards}</div>', rose=True)
    nav = sg.block("hitta", "Hitta rätt", "Vad vill du göra?", "",
        sg.link_cards([
            ("rgb.svg", "Välja färger", "Palett, roller, proportioner och kontrast.", "farg.html", "Till färg"),
            ("nodes.svg", "Rita en form", "Polygonspråket: så skapar du nya former och när formen öppnas.", "form.html", "Till form"),
            ("speak-bouble.svg", "Sätta text", "Typsnitt, skala, profiler och språkregler.", "typografi.html", "Till typografi"),
            ("rocket.svg", "Bygga en sida", "Knappar, kort, steg, citat, tabeller och sektioner med bruksanvisning.", "komponenter.html", "Till komponenter"),
            ("check-mark-checked.svg", "Skapa ett formulär", "Fält, states, feedback och laddning.", "formular-feedback.html", "Till formulär"),
            ("arrow-up-right.svg", "Bygga menyer", "Header, dropdown, sidospår, mobilmeny och brödsmula.", "navigation.html", "Till navigation"),
        ]))
    agents = sg.block("agenter", "AI-agenter", "Använd styleguiden som underlag",
        "Styleguiden är gjord för att läsas av både människor och agenter. Börja med <a href='https://github.com/magello-group/design-guidelines/blob/main/AGENTS.md'><code>AGENTS.md</code></a> i <a href='https://github.com/magello-group/design-guidelines'>repot på GitHub</a>, hämta värden ur <code>tokens/tokens.json</code> och rita former med SVG-filerna i <code>assets/shapes/</code>.",
        sg.code("""# Exempel på uppdrag till en agent
Läs https://github.com/magello-group/design-guidelines/blob/main/AGENTS.md
och docs/design-language.md i samma repo. Skapa en presentation (16:9) om vårt
erbjudande inom Cloud. Använd tokens/tokens.json för färger och typsnitt, formerna
i assets/shapes/ och mallen assets/templates/Powerpoint-mall.potx. Följ checklistan
i AGENTS.md innan du levererar.""")
        + sg.use(do=["Be agenten läsa <a href='https://github.com/magello-group/design-guidelines/blob/main/AGENTS.md'><code>AGENTS.md</code></a> först", "Hänvisa till tokens och former i stället för att beskriva dem", "Be om en självgranskning mot checklistan"],
                 dont=["Be agenten ”göra det snyggt” utan underlag", "Låta agenten uppfinna egna färger eller former"]))
    return intro + principles + nav + agents
