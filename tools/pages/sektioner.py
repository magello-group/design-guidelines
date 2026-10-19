PAGE = dict(
    title="Sektioner", kicker="Byggstenar",
    lead="Hur en sida sätts ihop av sektioner: öppning, innehåll, rosa avdelare, uppmaning och sidfot. Plus de sidtyper Magello har.",
)

IMG = "../assets/images/black-and-white/"


def body(sg):
    types = sg.block("sidtyper", "Sidtyper", "Fem sidtyper",
        "Alla sidor byggs av samma sektioner i en bestämd ordning. Välj sidtyp först, bygg sedan.",
        sg.spec(["Sidtyp", "Öppning", "Typografiprofil", "Header", "Sektioner"],
                [["Startsida", "Hero med foto och vit platta", "Showcase", "Sticky, kollapsar vid scroll", "Expertis-split, erbjudandekort, case, kontakt"],
                 ["Ingångssida", "Kicker, rubrik, underrubrik, knappar, ingress", "Standard", "Fast, roterar bort (<code>--rotate</code>)", "Bildplatta, kort, processteg, case, kontaktkort, CTA"],
                 ["Artikel / case", "Sidtitel med brödsmula", "Editorial", "Fast, roterar bort", "Löptext, infoblock efter varandra, citat, fler case"],
                 ["Textsida (om oss)", "Sidtitel (DocTitle) med underrubrik", "Editorial", "Fast, roterar bort", "Löptext, infoblock, tidslinje, värdekort"],
                 ["Verktyg / app", "Mörk rosagrå topbar, tvåkolumns arbetsyta", "—", "Applikationsmeny", "Kontrollpanel + canvas. Se formulär och feedback"]]))

    hero = sg.block("hero", "Öppning", "Sidhuvud för ingångssidor",
        "Brödsmula, kicker, rubrik, underrubrik, ett knappar-par och en ingress. Den här sidan öppnar på samma sätt.",
        sg.demo('<div class="mg-ingang-hero" style="padding-top:0"><div class="mg-ingang-col" style="padding:0">'
                '<nav class="mg-breadcrumb" aria-label="Brödsmula"><a href="#hero">Hem</a><span class="mg-breadcrumb__sep">/</span><span aria-current="page">Vår expertis</span></nav>'
                '<p class="mg-kicker">Expertisområde</p><h2 class="mg-ingang-title" style="font-size:clamp(2.4rem,5vw,4rem)">Hållbara<br>digitala tjänster</h2>'
                '<p class="mg-ingang-sub">Vi bygger digitala lösningar som löser era faktiska problem.</p>'
                '<div class="mg-ingang-actions"><a class="mg-btn mg-btn--primary" href="#hero">Prata med oss</a><a class="mg-btn mg-btn--secondary" href="#hero">Vad vi erbjuder</a></div></div></div>', "plain") +
        sg.code('''<div class="mg-ingang-hero"><div class="mg-ingang-col">
  <nav class="mg-breadcrumb">…</nav>
  <p class="mg-kicker">Expertisområde</p>
  <h1 class="mg-ingang-title">Rubrik</h1>
  <p class="mg-ingang-sub">Underrubrik</p>
  <div class="mg-ingang-actions">… två knappar …</div>
  <p class="mg-ingang-intro">Ingress …</p>
</div></div>''') +
        sg.use(do=["Brödsmulan på exakt samma höjd på alla undersidor (156 px från sidtopp)", "En primär och en sekundär knapp, i den ordningen", "Rubriken är H1, en per sida"],
               dont=["Rubriken under headern så att brödsmulan skyms", "Mer än två knappar", "Linje under hero"],
               note=["Innehållet börjar under headern: <code>padding-top: var(--mg-header-h)</code> (fast header tar ingen plats i flödet)"]))

    title = sg.block("sidtitel", "Öppning", "Sidtitel (DocTitle)",
        "För artiklar, case och textsidor. Stor rubrik, underrubrik och en valfri liten etikett. Aldrig en linje under.",
        sg.demo('<div class="mg-page-title" style="padding-top:0"><div class="mg-page-title__inner">'
                '<nav class="mg-breadcrumb"><a href="#sidtitel">Hem</a><span class="mg-breadcrumb__sep">/</span><span aria-current="page">Om oss</span></nav>'
                '<h2 class="mg-doc-title" style="font-size:clamp(2.4rem,5vw,4rem)">Vi har levererat värde i 30 år</h2>'
                '<p class="mg-doc-sub" style="font-size:1.4rem;line-height:1.6">Vi hjälper er bygga hållbara lösningar för långa relationer</p>'
                '<span class="mg-page-title__since">Sedan 1996</span></div></div>', "plain") +
        sg.use(do=["Underrubrik i text-2, 22 pt med luftigt radavstånd", "Brödsmula ovanför rubriken"], dont=["Linje eller ram under titeln", "Titel i magenta"]), rose=True)

    head = sg.block("sektionshuvud", "Innehåll", "Sektionshuvud",
        "Varje sektion börjar med etikett (kicker), magenta H2 och en kort ingress. Det är det som signalerar att en ny idé börjar.",
        sg.demo('<div class="mg-section-head" style="margin:0"><p class="mg-label">Specialistområden</p><h2>Vad vi erbjuder inom Digitala tjänster</h2><p>Oavsett om ni behöver enskilda konsulter eller kompletta agila team anpassar vi oss efter era behov.</p></div>', "plain") +
        sg.code('''<div class="mg-section-head">
  <p class="mg-label">Specialistområden</p>
  <h2>Vad vi erbjuder</h2>
  <p>Ingress …</p>
</div>''') +
        sg.use(do=["Etiketten beskriver kategorin, inte innehållet", "Sektionens H2 är magenta, en rubrik per sektion"], dont=["Etikett under rubriken", "Fler än en H2 i sektionshuvudet"]))

    rose = sg.block("rosa", "Avdelare", "Rosagrå sektion",
        "Rosa sektioner ger rytm och ersätter linjer. De har polygonkanter och ligger mellan vita sektioner.",
        sg.demo('<section class="mg-section--rose" style="margin:0"><div class="mg-wrap"><div class="mg-section-head" style="margin:0"><p class="mg-label">Uppdrag</p><h2>Projekt som gör skillnad</h2><p>Ett urval av uppdrag vi gjort.</p></div></div></section>', "plain") +
        sg.code('''<section class="mg-section--rose">
  <div class="mg-wrap"> … </div>
</section>''') +
        sg.use(do=["Växla vit och rosa sektion nedåt på sidan", "Lägg vita kort på rosa sektion så att formerna syns"],
               dont=["Två rosa sektioner efter varandra", "Svart eller starkt färgad sektionsbakgrund", "Egen clip-path på sektioner: använd <code>.mg-section--rose</code>"]))

    split = sg.block("split", "Innehåll", "Bild och text",
        "Två kolumner: text med kicker, rubrik, ingress och knapp, intill en polygonformad svartvit bild som rätas ut vid hover.",
        sg.demo(f'<div class="mg-expertis-split"><div class="mg-expertis-split__content"><span class="mg-kicker">Expertis</span><h3 class="mg-expertis-split__title">Bygg din affär med AI och digital innovation</h3><p class="mg-expertis-split__ingress">Magello omsätter AI och automation till verklig affärsnytta.</p><a class="mg-btn mg-btn--primary" href="#split">Läs mer</a></div><div class="mg-expertis-split__img"><img src="{IMG}dator-1.jpg" alt=""></div></div>', "plain") +
        sg.use(do=["Byt sida på bilden mellan sektioner", "Knappen är sektionens enda primära handling"], dont=["Två bilder i samma split", "Text över bilden"]))

    cases = sg.block("case", "Innehåll", "Case-kort",
        "Bild, kicker, rubrik och en rad. Rosa textyta med polygonform under en svartvit bild. Hela kortet är en länk.",
        sg.demo(f'<div class="mg-case-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:var(--mg-space-5)">'
                f'<a href="#case" class="mg-case-card"><img src="{IMG}dator-2.jpg" alt="Moverot" class="mg-case-card__img"><div class="mg-case-card__body"><p class="mg-case-card__kicker">App-utveckling</p><h3>Moverot</h3><p>Appen som gör friskvård enkelt och roligt.</p></div></a>'
                f'<a href="#case" class="mg-case-card"><img src="{IMG}kontor-10.jpg" alt="SOS Barnbyar" class="mg-case-card__img"><div class="mg-case-card__body"><p class="mg-case-card__kicker">Portal &amp; plattform</p><h3>SOS Barnbyar</h3><p>En medlemsportal som engagerar givare.</p></div></a></div>', "plain") +
        sg.use(do=["Foto svartvitt, rubrik = kundens namn", "Visa 3–4 case och en ”Se alla uppdrag”-knapp"], dont=["Färgfoton", "Mer än två rader beskrivning"]), rose=True)

    article = sg.block("artikel", "Layout", "Artikel: allt i en kolumn",
        "Undersidor är en enda kolumn. Ingress och löptext går i full bredd. Informationsrutor läggs efter varandra i flödet och aldrig i en smal högerkolumn.",
        sg.demo('<div class="mg-prose"><h2>Magello i korthet</h2><p>Vi utgår från vårt kontor i Stockholm med räckvidd över hela landet. Texten fortsätter i full bredd även efter informationsrutorna.</p>'
                '<aside class="mg-article-sidebar"><div class="mg-sidebar__block"><span class="mg-sidebar__label">Magello i siffror</span><div class="mg-sidebar__facts-row"><div class="mg-sidebar__fact"><span class="mg-sidebar__num">30</span><span class="mg-sidebar__desc">år</span></div><div class="mg-sidebar__fact"><span class="mg-sidebar__num">120</span><span class="mg-sidebar__desc">konsulter</span></div></div></div></aside>'
                '<h2>Hur vi arbetar</h2><p>Nästa avsnitt börjar direkt efter rutan.</p></div>', "white") +
        sg.spec(["Ordning", "Innehåll"],
                [["1", "Brödsmula och sidtitel"], ["2", "Ingress i full bredd"], ["3", "Löptext (<code>.mg-prose</code>)"], ["4", "Citat (valfritt)"], ["5", "Informationsrutor efter varandra, i full bredd"], ["6", "Mer löptext"]]) +
        sg.use(do=["Texten återgår till 100 % bredd efter en ruta", "Fakta i en rad inne i rutan"],
               dont=["<code>float: right</code> eller en smal högerkolumn för informationsrutor", "Två kolumner på artikelsidor"],
               note=["Direktiv: använd inte högerställda informationsrutor. Lägg dem efter varandra som den rosagrå infoblock-rutan"]))

    foot = sg.block("sidfot", "Avslut", "Uppmaning och sidfot",
        "Sidan avslutas med en uppmaning (rubrik, text, en primär knapp) och sidfoten i tre kolumner utan linje ovanför.",
        sg.spec(["Kolumn", "Innehåll"],
                [["1", "<strong style=\"color:var(--mg-magenta)\">Magello</strong> (magenta), adress"], ["2", "Organisationsnummer, momsnummer"], ["3", "Telefon, e-post, webb (högerjusterad)"]]) +
        sg.use(do=["Sidfot i liten text, <code>--mg-text-2</code>", "Behåll tre kolumner på desktop, stapla på mobil"], dont=["Linje ovanför sidfoten", "Mörk sidfot"]), rose=True)
    return types + hero + title + head + rose + split + cases + article + foot
