import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TOK = json.loads((ROOT / "tokens" / "tokens.json").read_text())

PAGE = dict(
    title="Avstånd &amp; rörelse", h1="Avstånd<br>&amp; rörelse", kicker="Grunder",
    lead="Generöst med luft ovanför rubriker, tätare under. Rörelse används för att öppna former, inte för att dekorera.",
)


def body(sg):
    sp = TOK["space"]
    names = ["2", "3", "4", "5", "6", "7", "8", "9"]
    use_for = {"2": "Tätt mellan ikon och text", "3": "Mellan rubrik och etikett", "4": "Mellan relaterade element", "5": "Standardavstånd mellan stycken och kort", "6": "Kortpadding, mellan block", "7": "Mellan rubrik och innehåll i en sektion", "8": "Sektionspadding", "9": "Stora sektioner, hero"}
    rows = "".join(
        f'<div class="sg-space"><span class="sg-space__name">--mg-space-{n}</span><span class="sg-space__bar" style="width:{sp[n]}px"></span><span class="sg-space__px">{sp[n]} px</span></div>'
        for n in names)
    space = sg.block("avstand", "Avstånd", "Åttapunktsskala",
        "Skalan går från <code>--mg-space-2</code> (8 px) till <code>--mg-space-9</code> (96 px). Det finns ingen <code>--mg-space-1</code> och ingen <code>--mg-space-10</code>. En saknad token gör att hela CSS-deklarationen tyst ogiltigförklaras.",
        sg.demo(rows) + sg.spec(["Token", "px", "Används till"], [[f"<code>--mg-space-{n}</code>", sp[n], use_for[n]] for n in names]) +
        sg.use(do=["Mer luft ovanför en rubrik än under", "Samma avstånd mellan samma sorts block", "Använd tokens, inte egna px-värden"],
               dont=["Fylla varje yta till kanten", "Mer luft under en rubrik än ovanför", "Egna mellanvärden som 20 eller 40 px"]))

    L = TOK["layout"]
    layout = sg.block("layout", "Layout", "En container, en vänsterkant",
        "Allt innehåll delar vänsterkant med logotypen. Navigationen och innehållet använder samma container, samma bredd och samma sidomarginal.",
        sg.spec(["Token", "Värde", "Anmärkning"],
                [["<code>--mg-wide</code>", f'{L["contentWidth"]} px', "Max innehållsbredd, samma för navigation och innehåll"],
                 ["<code>--mg-gutter</code>", "20 / 40 px", "Sidomarginal: mobil, 600 px+"],
                 ["<code>--mg-gutter-end</code>", "minst <code>--mg-gutter</code>", "Högermarginal. Växer på sidor med sidospår så att innehållet aldrig hamnar under spåret"],
                 ["<code>--mg-side-w</code>", f'{L["sideNavWidth"]} px', "Sidospårets bredd"],
                 ["<code>--mg-nav-h-compact</code>", f'{L["navHeightCompact"]} px', "Headerns höjd i hamburgerläge efter scroll"],
                 ["<code>--mg-nav-h</code>", f'{L["navHeight"]} px', "Navigationens höjd"],
                 ["<code>--mg-hext</code>", f'{L["headerExtension"]} px', "Polygonens förlängning under navigationen"],
                 ["<code>--mg-header-h</code>", f'{L["headerHeight"]} px', "Navigation + förlängning. Innehållet på undersidor börjar här"]]) +
        sg.code('''.mg-wrap {
  max-width: var(--mg-wide);      /* 1280 px = 1200 px innehåll + 2 × 40 px */
  margin-inline: auto;
  padding-inline: var(--mg-gutter) var(--mg-gutter-end);
}''') +
        sg.sub("Brytpunkter") +
        sg.spec(["Bredd", "Händer"],
                [["≤ 599 px", "En kolumn, gutter 20 px, footer staplad"], ["≥ 600 px", "Gutter 40 px, container max 1280 px (1200 px innehåll)"], ["> 768 px med sidospår", "Högermarginalen växer så att innehållet håller 24 px avstånd till sidospåret"],
                 ["≤ 768 px", "Hamburgermeny ersätter navlänkar. Sidospåret döljs. Headern ligger kvar efter scroll och blir lägre (56 px)"], ["≤ 900 px", "Tvåkolumnslayouter faller till en kolumn"]]) +
        sg.use(do=["Använd <code>.mg-wrap</code> för allt innehåll", "Mät att logotyp, brödsmula och rubrik har samma vänsterkant"],
               dont=["Egna <code>max-width</code> (960, 1080, 1140) på containrar som ska linjera", "Egna <code>clamp()</code>-värden för sidopadding"]), rose=True)

    m = TOK["motion"]
    rows = [[k, v.get("property", "—"), v.get("duration", "—"), v.get("easing", "—")] for k, v in m.items() if isinstance(v, dict)]
    motion = sg.block("rorelse", "Rörelse", "Rörelse som öppnar former",
        "Rörelsen är sparsam och har en uppgift: att ge en klickbar form liv, eller att flytta navigationen ur vägen.",
        sg.demo('<div class="sg-row"><a class="sg-hover-demo" href="#rorelse">Hover: formen öppnas</a><a class="mg-btn mg-btn--primary" href="#rorelse">Knapp</a>'
                '<div class="mg-offer-card" style="max-width:320px"><div class="mg-offer-card__icon"><img src="../assets/graphics/light.svg" alt=""></div><div class="mg-offer-card__body"><h3 class="mg-offer-card__title">Erbjudandekort</h3><p class="mg-offer-card__desc">Hovra: formen öppnas och bakgrunden går ett steg mörkare.</p></div></div></div>') +
        sg.spec(["Namn", "Egenskap", "Tid", "Kurva"], rows) +
        sg.use(do=["Animera <code>clip-path</code> och bakgrundsfärg", "Respektera <code>prefers-reduced-motion</code>: inga transitions, formen öppnas inte", "Håll tider mellan 180 och 600 ms"],
               dont=["Studsande, roterande eller blinkande effekter", "Rörelse som inte hjälper användaren", "Parallax och scroll-jacking"]))
    return space + layout + motion
