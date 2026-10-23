import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
BANNERS = ROOT / "assets" / "linkedin-banners"
TOOL = "https://linkedin-profile-image.magello.se"

PAGE = dict(
    title="LinkedIn-banners", kicker="Bildbank",
    lead="Färdiga bakgrundsbilder till din LinkedIn-profil i Magellos formspråk. Välj en, ladda ned och lägg upp den. Vill du ha en egen miljöbild gör du bannern i bildverktyget.",
    actions=[("Gör en egen banner", TOOL, "primary"),
             ("Till fotona", "bildbank.html", "secondary")],
)

URL = "../assets/linkedin-banners/"


def natural(name):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", name.lower())]


def size(path):
    mb = path.stat().st_size / 1e6
    return f"{mb:.1f} MB".replace(".", ",") if mb >= 1 else f"{mb * 1000:.0f} kB"


def tile(i, path):
    href = URL + path.name
    return (f'<figure class="sg-banner">'
            f'<a href="{href}" target="_blank" rel="noopener"><img src="{href}" loading="lazy" '
            f'alt="LinkedIn-banner {i}" width="1584" height="396"></a>'
            f'<figcaption><span class="sg-photo__name">Banner {i}</span>'
            f'<a class="sg-photo__dl" href="{href}" download>Ladda ned · PNG · {size(path)}</a></figcaption></figure>')


def body(sg):
    files = sorted((p for p in BANNERS.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")),
                   key=lambda p: natural(p.name))
    grid = "".join(tile(i, p) for i, p in enumerate(files, 1))
    gallery = sg.block("banners", "LinkedIn-banners", f"{len(files)} banners att välja bland",
        "Alla är 1584 × 396 px, det mått LinkedIn vill ha. Klicka på en banner för att se den i full storlek.",
        f'<div class="sg-banners">{grid}</div>' +
        sg.use(do=["Använd en banner tillsammans med en profilbild från bildverktyget",
                   "Kontrollera på mobilen att Magello-logotypen inte hamnar bakom profilbilden"],
               dont=["Lägga till egen text, filter eller färg på bannern",
                     "Beskära eller sträcka ut bannern"]))

    howto = sg.block("lagg-upp", "Så gör du", "Byt banner på LinkedIn",
        "Det tar en minut, på datorn eller i appen.",
        sg.demo(sg.steps("Ladda ned en banner", "Öppna din profil", "Byt bakgrundsbild")) +
        '<ol class="sg-text"><li>Ladda ned den banner du vill ha.</li>'
        '<li>Öppna din profil på LinkedIn.</li>'
        '<li>Klicka på pennan uppe till höger på bakgrundsbilden, välj <em>Ändra bild</em> och ladda upp filen. Spara.</li></ol>' +
        sg.sub("Gör en egen banner") +
        sg.text(f'Vill du ha en egen miljöbild, öppna <a href="{TOOL}">bildverktyget</a> och välj <em>LinkedIn – personlig topbanner</em>. '
                'Ladda upp ett foto, så får du en banner i samma formspråk som de här.'),
        rose=True)
    return gallery + howto
