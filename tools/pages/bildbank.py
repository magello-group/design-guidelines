import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PHOTOS = ROOT / "assets" / "images" / "black-and-white"
TOOL = "https://linkedin-profile-image.magello.se"

PAGE = dict(
    title="Bildbank", kicker="Bilder",
    lead="Magellos svartvita foton från kontor, möten och event. Ladda ned dem i full storlek. Behöver du en profilbild, en LinkedIn-bild eller en egen miljöbild gör du den i bildverktyget.",
    actions=[("Till bildverktyget", TOOL, "primary"),
             ("Så används bilderna", "bilder-ikoner.html", "secondary")],
)

IMG = "../assets/images/black-and-white/"
THUMB = "../assets/images/thumbs/"   # skapas av tools/build_site.py vid publicering

# Grupper i den ordning de visas: (prefix i filnamnet, rubrik)
GROUPS = [
    ("kontor", "Kontor"),
    ("dator", "Vid datorn"),
    ("whiteboard", "Whiteboard"),
    ("workshop", "Workshop"),
    ("event", "Event"),
    ("powerpoint", "Till presentationer"),
]

TOOLS = [
    ("Ny profilbild", "Svartvit profilbild med Magellos rosa ton."),
    ("LinkedIn – personlig topbanner", "Ladda upp en miljöbild och få en banner i Magellos formspråk till din LinkedIn-profil."),
    ("LinkedIn – text på profilbild", "Lägg en text på din profilbild och ladda ned resultatet."),
    ("LinkedIn-inlägg för nyanställd", "Bild till ett välkomstinlägg med valfri text, färg, rotation och överlägg."),
    ("Svartvita miljöbilder", "Gör om ett färgfoto till en svartvit Magellobild, 1080 × 1080 px, för PowerPoint eller LinkedIn."),
    ("Ikoner för uppdrag i CV", "Ladda upp kundens logotyp som SVG och få en ikon på 200 × 200 px till CV:t."),
]


def natural(name):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", name.lower())]


def size(path):
    mb = path.stat().st_size / 1e6
    return f"{mb:.1f} MB".replace(".", ",") if mb >= 1 else f"{mb * 1000:.0f} kB"


def figure(path, i):
    name = path.name
    stem = path.stem
    variant = "a" if i % 2 == 0 else "c"
    full = IMG + name
    return (f'<figure class="sg-photo">'
            f'<a href="{full}" target="_blank" rel="noopener">'
            f'<img class="mg-poly-img mg-poly-img--{variant}" src="{THUMB}{stem}-{path.suffix[1:].lower()}.jpg" loading="lazy" '
            f'onerror="this.onerror=null;this.src=\'{full}\'" alt="{stem}"></a>'
            f'<figcaption><span class="sg-photo__name">{stem}</span>'
            f'<a class="sg-photo__dl" href="{full}" download>Ladda ned · {path.suffix[1:].upper()} · {size(path)}</a>'
            f'</figcaption></figure>')


def body(sg):
    files = sorted((p for p in PHOTOS.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png")),
                   key=lambda p: natural(p.name))
    grouped, seen = [], set()
    for prefix, title in GROUPS:
        items = [p for p in files if p.name.lower().startswith(prefix)]
        seen.update(items)
        if items:
            grouped.append((title, items))
    rest = [p for p in files if p not in seen]
    if rest:
        grouped.append(("Övrigt", rest))

    gallery = ""
    for title, items in grouped:
        figs = "".join(figure(p, i) for i, p in enumerate(items))
        gallery += sg.sub(f"{title} <span class=\"sg-photo__count\">{len(items)}</span>") + f'<div class="sg-photos">{figs}</div>'

    photos = sg.block("foton", "Bildbank", f"{len(files)} svartvita foton",
        "Klicka på en bild för att se den i full storlek, eller ladda ned den direkt. Filerna är i full upplösning och kan vara stora.",
        gallery +
        sg.use(do=["Beskär fotot i en polygon när du använder det (se <a href=\"bilder-ikoner.html\">Bilder &amp; ikoner</a>)",
                   "Välj en bild med lugn komposition och plats för text",
                   "Skriv en alt-text som beskriver vad bilden visar"],
               dont=["Färglägga, tona eller lägga filter på fotona",
                     "Lägga text direkt på fotot. Använd en vit platta",
                     "Använda bilderna utanför Magellos egen kommunikation"],
               note=["Behöver du en egen miljöbild? Gör om ditt färgfoto i bildverktyget, så blir det svartvitt och rätt beskuret",
                     "Bilderna under <em>Till presentationer</em> är 1920 × 1080 px och passar en hel bild i PowerPoint"]))

    tools = "".join(
        f'<div class="sg-use__card"><h3 class="sg-tool__title">{t}</h3><p class="sg-text">{d}</p></div>'
        for t, d in TOOLS)
    tool_block = sg.block("bildverktyget", "Skapa egna bilder", "Bildverktyget",
        "Profilbilder, LinkedIn-bilder, egna svartvita miljöbilder och kundlogotyper till CV görs i Magellos bildverktyg. Det ger rätt filter, rosa ton, form och mått, och allt körs i din webbläsare. Inga bilder laddas upp till någon server.",
        f'<div class="sg-use">{tools}</div>'
        f'<p><a class="mg-btn mg-btn--secondary" href="{TOOL}" target="_blank" rel="noopener">Öppna bildverktyget</a></p>' +
        sg.use(do=["Använd bildverktyget för alla profil- och LinkedIn-bilder", "Ladda upp kundlogotypen som SVG för skarpast ikon"],
               dont=["Göra profilbilder eller banners för hand i andra program", "Använda färgfoton på LinkedIn eller i CV"]),
        rose=True)
    return photos + tool_block
