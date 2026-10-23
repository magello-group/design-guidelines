import json, pathlib, unicodedata
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
LOGOS = ROOT / "assets" / "assignments-logos"
TOOL = "https://linkedin-profile-image.magello.se"

PAGE = dict(
    title="Kundlogotyper", kicker="Bildbank",
    lead="Logotyper för de företag och organisationer där Magellos konsulter har haft uppdrag. De visas bredvid uppdragen i konsulternas CV.",
    actions=[("Skapa en ny logotyp", TOOL, "primary"),
             ("Till fotona", "bildbank.html", "secondary")],
)

URL = "../assets/assignments-logos/"


def plain(text):
    """Jämförelsenyckel: gemener, å/ä/ö som a/a/o (samma som render.py i CV-flödet)."""
    text = unicodedata.normalize("NFC", text).lower()
    return text.translate(str.maketrans("åäöé", "aaoe"))


def sort_key(name):
    # Svensk ordning: å, ä, ö sist
    return [("zz" + {"å": "1", "ä": "2", "ö": "3"}[c]) if c in "åäö" else c for c in name.lower()]


def logos():
    manifest = json.loads((LOGOS / "manifest.json").read_text())
    names = {}
    for org, file in manifest.items():
        if not org.startswith("_"):
            names.setdefault(plain(file), []).append(org)
    out = []
    for path in LOGOS.iterdir():
        if path.suffix.lower() not in (".svg", ".png", ".jpg", ".jpeg"):
            continue
        orgs = names.get(plain(path.name))
        name = " / ".join(sorted(orgs, key=sort_key)) if orgs else path.stem.replace("-", " ").title()
        out.append((name, path))
    return sorted(out, key=lambda x: sort_key(x[0]))


def tile(name, path):
    href = URL + quote(unicodedata.normalize("NFC", path.name))
    return (f'<figure class="sg-logo" data-mg-filter-item>'
            f'<div class="sg-logo__img"><img src="{href}" alt="{name}" loading="lazy"></div>'
            f'<figcaption><span class="sg-logo__name">{name}</span>'
            f'<a class="sg-photo__dl" href="{href}" download>Ladda ned · {path.suffix[1:].upper()}</a></figcaption></figure>')


def body(sg):
    items = logos()
    grid = "".join(tile(n, p) for n, p in items)
    gallery = sg.block("logotyper", "Kundlogotyper", f"{len(items)} logotyper",
        "Sök på namnet. Alla logotyper är 200 × 200 px med genomskinlig bakgrund, så att de ser likadana ut bredvid varandra i CV:t.",
        '<p class="sg-logo-search"><label class="mg-field__label" for="logo-search">Sök</label>'
        '<input id="logo-search" class="mg-input" type="search" placeholder="Till exempel Volvo" '
        'data-mg-filter="#logo-grid" autocomplete="off"></p>'
        f'<div class="sg-logos" id="logo-grid">{grid}</div>'
        '<p class="sg-text" data-mg-filter-empty="#logo-grid" hidden>Ingen logotyp matchar sökningen.</p>' +
        sg.use(do=["Använd logotypen bara för att visa var en konsult har haft uppdrag",
                   "Använd den som den är, i den storlek CV:t ger den"],
               dont=["Ändra färger eller form på en kunds logotyp",
                     "Använda logotyperna i marknadsföring eller som referens utan kundens godkännande"]))

    add = sg.block("ny", "Ny logotyp", "Lägg till en kund",
        "Saknas en kund gör du logotypen i bildverktyget och lägger den i repot.",
        sg.demo(sg.steps("Hämta kundens logotyp som SVG", "Gör ikonen i bildverktyget", "Lägg filen i repot")) +
        '<ol class="sg-text">'
        f'<li>Hämta kundens logotyp, helst som SVG från kundens egen webbplats eller pressida.</li>'
        f'<li>Öppna <a href="{TOOL}">bildverktyget</a> och välj <em>Skapa ikoner för uppdrag i CV</em>. Flytta och skala logotypen och ladda ned ikonen på 200 × 200 px.</li>'
        '<li>Döp filen efter kunden med små bokstäver och bindestreck, till exempel <code>nya-kunden.svg</code>, och lägg den i '
        '<a href="https://github.com/magello-group/design-guidelines/tree/main/assets/assignments-logos"><code>assets/assignments-logos/</code></a>. '
        'Heter kunden något annat i CV:t än filnamnet, lägg till en rad i <code>manifest.json</code>.</li></ol>',
        rose=True)
    return gallery + add
