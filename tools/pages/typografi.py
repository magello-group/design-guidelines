PAGE = dict(
    title="Typografi", kicker="Grunder",
    lead="En enkel regel: Roboto Condensed för allt som signalerar, Roboto för allt som berättar. Typografin är Magellos röst, så den får ta plats.",
)


def sample(label, meta, html):
    return f'<div class="sg-type"><div class="sg-type__meta">{label}<span>{meta}</span></div><div>{html}</div></div>'


def body(sg):
    fonts = sg.block("typsnitt", "Typsnitt", "Två typsnitt, två roller",
        "Blanda aldrig tvärtom. Roboto på en knapp eller Condensed i löptext bryter tonen direkt. Inga andra typsnitt, utom <a href=\"typsnitt.html\">specialtypsnittet Kattux</a> vid speciella tillfällen.",
        '<div class="sg-two">'
        '<div><div class="sg-specimen">Aa</div><p class="sg-sub">Roboto Condensed</p>'
        '<p class="sg-text">Vikt 400, 500, 700. Rubriker, underrubriker, etiketter, knappar, navigation och siffror som blickfång. Smal, tydlig och lite formell.</p></div>'
        '<div><div class="sg-specimen sg-specimen--body">Aa</div><p class="sg-sub">Roboto</p>'
        '<p class="sg-text">Vikt 400, 500, 700 och kursiv 400. Brödtext, tabeller, listor, bildtexter och sidfot. Allt som berättar något.</p></div></div>'
        + sg.code('<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&family=Roboto+Condensed:wght@400;500;700&display=swap" rel="stylesheet">')
        + sg.spec(["Token", "Värde"], [["<code>--mg-font-head</code>", "&quot;Roboto Condensed&quot;, &quot;Arial Narrow&quot;, Arial, sans-serif"],
                                     ["<code>--mg-font-body</code>", "&quot;Roboto&quot;, system-ui, Arial, sans-serif"],
                                     ["<code>--mg-font-code</code>", "Consolas, ui-monospace, Menlo, monospace (bara tekniska texter)"]]))

    scale = (
        sample("Display / sidtitel", "Condensed 700<br>clamp(3.2–6.5rem)", '<div class="mg-doc-title" style="margin:0">Hållbara tjänster</div>') +
        sample("H1", "Condensed 500<br>2.25–3.5rem", '<div style="font:500 var(--mg-fs-h1)/1.1 var(--mg-font-head)">Vi hjälper kunder bygga mjukvara</div>') +
        sample("Underrubrik", "Condensed 400, text-2<br>1.1–1.35rem", '<div style="font:400 var(--mg-fs-subtitle)/1.55 var(--mg-font-head);color:var(--mg-text-2)">Professionella, avskalade, tydliga och lite lekfulla</div>') +
        sample("H2 sektion", "Condensed 500, magenta<br>1.5–1.8rem", '<div style="font:500 var(--mg-fs-h2)/1.15 var(--mg-font-head);color:var(--mg-magenta)">Vad vi erbjuder inom Digitala tjänster</div>') +
        sample("H2 artikel", "Condensed 700, svart<br>inne i löptext", '<div style="font:700 var(--mg-fs-h2)/1.2 var(--mg-font-head)">Hur vi arbetar</div>') +
        sample("H3", "Condensed 700<br>1.15–1.35rem", '<div style="font:700 var(--mg-fs-h3)/1.2 var(--mg-font-head)">Förstudier &amp; PoC</div>') +
        sample("Brödtext", "Roboto 400<br>1.125rem (18 px) / 1.6", '<p style="margin:0">Vi bygger moderna, robusta och säkra applikationer skapta för att växa. Med erfarenhet av komplexa backend-system till moderna webbapplikationer arbetar vi agilt och iterativt, nära er verksamhet.</p>') +
        sample("Kicker / etikett", "Condensed 700, versaler<br>.6875rem, spärrning .14em", '<span class="mg-kicker" style="margin:0">Expertisområde</span>') +
        sample("Länk i text", "Magenta, understruken", '<p style="margin:0">Läs mer om <a href="#skala">våra expertområden</a> eller kontakta oss.</p>') +
        sample("Liten text", "Roboto .8125rem", '<p style="margin:0;font-size:.8125rem;color:var(--mg-text-2)">Org no: 556531-7129 · VAT: SE556531712901</p>'))
    sc = sg.block("skala", "Skala", "Storlekar och vikter",
        "Rubrikerna är fluida (<code>clamp()</code>) och skalar mellan mobil och desktop. Alla storlekar finns som tokens i <code>:root</code>.",
        sg.demo(scale, "white"), rose=True)

    profiles = sg.block("profiler", "Profiler", "Tre typografiprofiler",
        "Skalan har tre profiler. Profilen väljs med en klass på <code>&lt;body&gt;</code> och avgörs av sidtypen, inte av enskilda element.",
        sg.spec(["Profil", "Klass på body", "Används på", "H2", "H3", "Radhöjd"],
                [["Standard", "ingen", "Landnings- och ingångssidor", "1.5–1.8rem", "1.15–1.35rem", "1.6"],
                 ["Editorial", "<code>mg-type-editorial</code>", "Artiklar, case, om oss, textsidor", "1.4–1.9rem", "1.15–1.35rem", "1.7"],
                 ["Showcase", "<code>mg-type-showcase</code>", "Startsida, komponentsidor", "1.5–1.8rem", "1.3–1.6rem", "1.5"]]) +
        sg.use(do=["Välj en profil per sida", "Behöver du en ny skala: lägg till en ny profil i <code>magello.css</code>"],
               dont=["Ändra tokenvärden på en enskild sida", "Blanda profiler på samma sida"]))

    rules = sg.block("regler", "Regler", "Så sätter du text",
        "Typografin är ett system: roller först, storlek sedan.",
        sg.use(do=["H2 på sektionsnivå är <strong>magenta</strong>: ”en ny idé börjar här”", "H2 inne i artikeltext är svart så den inte konkurrerar", "Etiketter står alltid <em>ovanför</em> rubriken de hör till", "Tätt radavstånd i rubriker (1.1–1.2), luftigt i brödtext (1.5–1.7)", "Mer luft ovanför en rubrik än under den", "Radlängd 70–75 tecken"],
               dont=["Roboto i knappar eller Condensed i löptext", "Versaler utom i etiketter", "Understrykningar utom länkar", "Löpande text i grå 300", "Utropstecken och fluffiga adjektiv", "Fler än två typsnitt"],
               note=["Texten är på svenska", "Rubriker beskriver vad något är eller gör: ”Vi hjälper kunder bygga fungerande mjukvara”", "Magenta text på vitt klarar bara stor eller fet text (4,2 : 1). Länkar i löptext är därför också understrukna"]))

    media = sg.block("tryck", "Andra medier", "Storlekar i dokument och presentationer",
        "Samma proportioner som på webben, uttryckta i punkter. Skalan utgår från brödtexten (faktor 1,0) och är hämtad ur Wordmallen. I Word och PowerPoint används mallarna i <code>assets/templates/</code> och deras formatmallar, se <code>docs/office-mallar.md</code>.",
        sg.spec(["Nivå", "Word (pt)", "Formatmall i Word", "Faktor", "Typsnitt", "PowerPoint (pt)"],
                [["Dokumenttitel (H1)", "36", "Inget avstånd (DocTitle)", "3,6", "Condensed 500", "40–54"],
                 ["Underrubrik", "22", "Underrubrik", "2,2", "Condensed 400, spärrning +0,75", "—"],
                 ["H2 (magenta)", "18", "Rubrik 1", "1,8", "Condensed 500", "28–32"],
                 ["H3", "16", "Rubrik 2", "1,6", "Condensed 700", "—"],
                 ["H4", "14", "Rubrik 3", "1,4", "Condensed 700", "—"],
                 ["H5 / H6", "12 / 10", "Rubrik 4 / 5", "1,2 / 1,0", "Condensed 700", "—"],
                 ["Brödtext", "10 (radavstånd 1,15)", "Normal, Brödtext", "1,0", "Roboto 400", "minst 18"],
                 ["Sidfot", "6,5", "Sidfot (i mallen)", "0,65", "Roboto 400, grå 300", "—"]]) +
        sg.text("I en presentation: aldrig under 14 pt, helst 18 pt eller mer för brödtext."), rose=True)
    return fonts + sc + profiles + rules + media
