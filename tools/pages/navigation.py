PAGE = dict(
    title="Navigation", kicker="Byggstenar",
    lead="Header, dropdown, sidospår, mobilmeny och brödsmula. Samma menystruktur renderas på tre ställen och ska hållas synkad. Den här styleguiden är byggd med mönstret, så prova det direkt.",
)


def fig(src, caption, narrow=False):
    cls = "sg-figure sg-figure--narrow" if narrow else "sg-figure"
    return f'<figure class="{cls}"><img src="img/{src}" alt="{caption}"><figcaption>{caption}</figcaption></figure>'


def body(sg):
    overview = sg.block("oversikt", "Översikt", "Tre uttryck för samma meny",
        "Navigationen har högst två nivåer: huvudlänkar med högst en undernivå. Menyn finns i header (desktop), sidospår (desktop efter scroll) och hamburgermeny (mobil).",
        sg.spec(["Plats", "När", "Klassprefix", "Öppnas med"],
                [["Header med dropdown", "Desktop (över 768 px), överst på sidan", "<code>mg-nav__</code>", "Hover, chevron-klick"],
                 ["Sidospår", "Desktop efter 80 px scroll", "<code>mg-side-</code>", "Hover, klick på huvudlänk, chevron"],
                 ["Mobilmeny", "768 px och smalare", "<code>mg-mob-</code>", "Chevron (accordion)"]]) +
        sg.use(do=["Prova själv: håll musen över ”Grunder”, scrolla ner och se sidospåret, smalna av fönstret och öppna hamburgaren", "Hamburgermeny på <strong>alla</strong> sidor under 768 px"],
               dont=["Fler än två nivåer", "Olika menyinnehåll i header, sidospår och mobilmeny"]))

    header = sg.block("header", "Header", "Signaturytan som header",
        "Headern är den rosagrå signaturpolygonen med logotyp, länkar och en utvald länk (”Lediga jobb”) med skev understrykning. Det finns två varianter.",
        fig("nav-header.png", "Header överst på sidan: logotyp, huvudlänkar med chevron och utvald länk.") +
        sg.spec(["Variant", "Klass", "Beteende", "Tröskel"],
                [["Startsida", "<code>.mg-page-header</code>", "<code>position: sticky</code>. Polygonen kollapsar till en rektangel vid scroll", "8 px"],
                 ["Undersida", "<code>.mg-page-header.mg-page-header--rotate</code>", "<code>position: fixed</code>. Roterar 90° ut ur bild och lämnar plats åt sidospåret", "80 px"]]) +
        sg.code('''<div class="mg-page-header mg-page-header--rotate">
  <div class="mg-header-shape"></div>
  <nav class="mg-nav"><div class="mg-nav__inner">
    <a class="mg-nav__logo" href="/"><!-- logotyp --></a>
    <ul class="mg-nav__links">…</ul>
    <a class="mg-nav__featured" href="#">Lediga jobb</a>
    <button class="mg-nav__burger" aria-label="Öppna meny">…</button>
  </div></nav>
</div>''') +
        sg.use(do=["Innehållet på undersidor börjar under headern: <code>padding-top: var(--mg-header-h)</code>", "Logotypens vänsterkant är sidans linje: innehållet linjerar mot den", "Headern har <code>pointer-events: none</code> när den roterat bort"],
               dont=["Rotera eller dölja headern på mobil (där ligger den kvar och blir lägre)", "Ändra headerns polygon utan att behålla den lutande kanten"]))

    drop = sg.block("dropdown", "Dropdown", "Undermeny under huvudlänken",
        "Menyn öppnas vid hover eller klick på chevron och ligger direkt under länken. Den är <code>position: fixed</code> och placeras av JavaScript.",
        fig("nav-dropdown.png", "Dropdown öppen under ”Grunder”. Chevron vänd uppåt.") +
        sg.use(do=["Synlighet styrs bara av klassen <code>.is-open</code>", "Ingen lucka mellan länk och meny", "220 ms stängningsfördröjning och lyssnare på själva menyn", "Stäng vid scroll, klick utanför och <code>Escape</code>"],
               dont=["CSS <code>:hover</code> som styr synlighet. Menyn stängs när pekaren passerar luckan", "<code>position: absolute</code>. Headern har <code>transform</code> och menyn hamnar i vänstra hörnet", "Meny som öppnar åt fel håll"],
               note=["All logik finns i <code>js/magello.js</code>. Kopiera filen, skriv inte om den"]), rose=True)

    side = sg.block("sidospar", "Sidospår", "Navigationen följer med",
        "När headern rotat bort glider ett vitt sidospår in från höger med ikonlogotyp och samma länkar. Ett klick på en huvudlänk fäller ut undermenyn i stället för att navigera.",
        fig("nav-sidespar.png", "Sidospåret efter scroll: ikonlogotyp, länkar, utfälld undermeny och utvald länk.", narrow=True) +
        sg.use(do=["Visa undermenyn vid hover och vid klick på huvudlänken", "Ge huvudlänken en egen första punkt (”Översikt”) i undermenyn om den har en egen sida", "Mörk text (<code>--mg-text-2</code>, magenta vid aktiv/hover): sidospåret har vit bakgrund"],
               dont=["Visa sidospåret på mobil", "Vit text på vit bakgrund"],
               note=["Sidospåret visas först när headern rotat (<code>.is-visible</code>), efter 80 px scroll"]))

    mobile = sg.block("mobil", "Mobilmeny", "Hamburgermeny och drawer",
        "Under 768 px ersätts navlänkarna av en hamburgare som öppnar en helskärmsdrawer från höger. Bakgrunden är rosagrå 100 och undermenyer fälls ut som accordion.",
        '<div class="sg-two">' + fig("nav-mobil.png", "Mobil: logotyp och hamburgare.", narrow=True) + fig("nav-mobilmeny.png", "Mobilmenyn öppen med utfälld undermeny.", narrow=True) + '</div>' +
        sg.use(do=["Stäng med kryss och <code>Escape</code>", "Lås sidans scroll medan menyn är öppen", "Stora tryckytor: länkarna är 1.1 rem och har 16 px luft ovan och under"],
               dont=["Dölja den utvalda länken (”Lediga jobb”). Den ligger längst ned i drawern", "Fler än ett nivåsteg"],
               note=["Mobilmenyns listor har rosa hårlinjer. Det är ett av få tillåtna linjeundantag (funktionella listavgränsare)"]), rose=True)

    crumb = sg.block("brodsmula", "Brödsmula", "Var är jag?",
        "Brödsmulan sitter över sidans kicker eller rubrik, i liten grå text. Den sitter på samma höjd på alla undersidor: <strong>156 px</strong> från sidtopp (120 px header + 36 px luft).",
        sg.demo('<nav class="mg-breadcrumb" aria-label="Brödsmula"><a href="#brodsmula">Hem</a><span class="mg-breadcrumb__sep">/</span><a href="#brodsmula">Byggstenar</a><span class="mg-breadcrumb__sep">/</span><span aria-current="page">Navigation</span></nav>') +
        sg.use(do=["Sista nivån är aktuell sida (<code>aria-current=\"page\"</code>), inte länkad", "Avståndet under brödsmulan sätts av containern (<code>.mg-ingang-col</code>, <code>.mg-page-title</code>)"],
               dont=["Brödsmula skymd av headern", "Olika höjd på olika sidor", "Brödsmula på startsidan"]))

    a11y = sg.block("tillganglighet", "Tillgänglighet", "Tangentbord och skärmläsare",
        "Menyerna ska fungera utan mus.",
        sg.spec(["Behov", "Så här"],
                [["Chevron-knappar", "<code>aria-expanded</code> och <code>aria-label</code>. Enter/Space öppnar"], ["Stänga", "<code>Escape</code> stänger meny och dropdown"], ["Fokus", "Synlig 2 px magenta kontur (<code>:focus-visible</code>)"], ["Dolda menyer", "<code>pointer-events: none</code>, och <code>visibility: hidden</code> om innehållet inte ska nås"], ["Rörelse", "<code>prefers-reduced-motion</code> stänger av rotation och glidning"]]), rose=True)
    return overview + header + drop + side + mobile + crumb + a11y
