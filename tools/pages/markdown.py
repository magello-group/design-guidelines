PAGE = dict(
    title="Markdown", kicker="Byggstenar",
    lead="Redaktörer skriver texter i Markdown, till exempel i ett Strapi-fält. Designen formger resultatet. Inga klasser, ingen HTML.",
)

ROWS = [
    ("Rubriker", "## Rubrik 2\n\n### Rubrik 3", '<h2>Rubrik 2 — avsnitt</h2><h3>Rubrik 3 — underavsnitt</h3>', "<code>#</code> (rubrik 1) är sidans titel och skrivs inte i texten."),
    ("Text", "Ett stycke med **fet**, *kursiv* och en [länk](https://magello.se).", '<p>Ett stycke med <strong>fet</strong>, <em>kursiv</em> och en <a href="#">länk</a>.</p>', "Brödtext 18 px. Länkar är magenta och understrukna."),
    ("Listor", "- Punkt ett\n- Punkt två\n\n1. Första\n2. Andra", '<ul><li>Punkt ett</li><li>Punkt två</li></ul><ol><li>Första</li><li>Andra</li></ol>', "Numrerad lista när ordningen betyder något."),
    ("Citat", "> Vi är generalister med spetskompetens.", '<blockquote><p>Vi är generalister med spetskompetens.</p></blockquote>', "Blir automatiskt ett Magello-citat med citattecknet."),
    ("Tabell", "| Område | Fokus |\n|---|---|\n| Cloud | Skalbarhet |\n| Integration | Flöden |", '<table><thead><tr><th>Område</th><th>Fokus</th></tr></thead><tbody><tr><td>Cloud</td><td>Skalbarhet</td></tr><tr><td>Integration</td><td>Flöden</td></tr></tbody></table>', "Rosa rubrikrad och bandning. Första kolumnen fet."),
    ("Luft", "Första stycket.\n\n---\n\nNästa avsnitt.", '<p>Första stycket.</p><hr><p>Nästa avsnitt.</p>', "<code>---</code> ger extra luft, aldrig en linje."),
]


def body(sg):
    rows = ""
    for title, md, rendered, note in ROWS:
        rows += (f'<h3 class="sg-sub">{title}</h3><div class="sg-two sg-md"><div><span class="sg-demo-label">Du skriver</span>{sg.code(md)}</div>'
                 f'<div><span class="sg-demo-label">Det blir</span><div class="mg-prose">{rendered}</div></div></div><p class="sg-text">{note}</p>')
    guide = sg.block("syntax", "Syntax", "Skriv så här, få det här",
        "Alla Markdown-fält renderas till HTML i en <code>&lt;div class=\"mg-prose\"&gt;</code>. Bibliotekets <code>.mg-prose</code> formger allt.", rows)
    rules = sg.block("regler", "Regler", "Vad som inte ska stå i Markdown",
        "Håll texten enkel. Det som ska se ut på ett särskilt sätt görs med komponenter, inte med syntax.",
        sg.use(do=["Rubrik 2 och 3, stycken, listor, citat och tabeller", "Korta stycken, en tanke per stycke", "Länka med beskrivande text, inte ”klicka här”"],
               dont=["<code># Rubrik 1</code>. Sidans titel är H1", "Bilder i texten. Använd bildkomponenter så att de blir svartvita och polygonformade", "Rå HTML eller färgade ord", "Kodblock, om inte sajten är teknisk"],
               note=["Rendera med en standardparser (<code>marked</code>, <code>markdown-it</code>) med tabeller påslagna, <code>html: false</code>, och sanitera ändå", "Sidor som visar Markdown använder typografiprofilen <code>mg-type-editorial</code> när de är artiklar"]) +
        sg.sub("Strapi") +
        sg.text("I Strapi 5 är fälttypen <code>richtext</code> Markdown-editorn. Använd den för alla längre texter. Se avsnitt 36 i <code>docs/design-guidelines-web.md</code> för innehållsmodellen och <a href=\"#syntax\">syntaxen ovan</a> som facit för utseendet."), rose=True)
    return guide + rules
