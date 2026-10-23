#!/usr/bin/env python3
"""Sätter ihop webbplatsen för GitHub Pages i _site/.

Webbplatsen speglar repots katalogstruktur, så att styleguidens relativa länkar
(../assets/, ../tokens/, ../docs/) fungerar även under en undermapp som
https://magello-group.github.io/design-guidelines/. Hela fotobiblioteket kopieras,
för bildbanken, och för varje foto skapas en förhandsbild i assets/images/thumbs/
(kräver Pillow). Körs av GitHub Pages-workflowen.
"""
import pathlib, re, shutil
from urllib.parse import unquote

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "_site"
# Kopieras alltid, i sin helhet
dirs = ["styleguide", "tokens", "docs", "assets/graphics", "assets/logos", "assets/shapes",
        "assets/images/black-and-white", "assets/assignments-logos"]
# Office-mallarna och howto-dokumenten, som nedladdningar
files = ["assets/templates/Powerpoint-mall.potx", "assets/templates/Word-mall.dotx",
         "assets/templates/Powerpoint-mall-howto.pptx", "assets/templates/Word-mall-howto.docx",
         # Specialtypsnittet Kattux (Magellos eget), för nedladdning och sidans prov
         *(f"assets/fonts/KattuxAbc-Regular.{ext}" for ext in ("otf", "ttf", "woff2", "woff"))]

if out.exists():
    shutil.rmtree(out)
for d in dirs:
    shutil.copytree(root / d, out / d, ignore=shutil.ignore_patterns(".DS_Store"))
for f in files:
    (out / f).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / f, out / f)

# Förhandsbilder till bildbanken: 800 px breda JPEG, så att sidan inte laddar fullstora foton
from PIL import Image, ImageOps
thumbs = out / "assets" / "images" / "thumbs"
thumbs.mkdir(parents=True, exist_ok=True)
for photo in sorted((root / "assets/images/black-and-white").iterdir()):
    if photo.suffix.lower() not in (".jpg", ".jpeg", ".png"):
        continue
    with Image.open(photo) as im:
        im = ImageOps.exif_transpose(im).convert("L")
        im.thumbnail((800, 800))
        im.save(thumbs / f"{photo.stem}-{photo.suffix[1:].lower()}.jpg", quality=78, optimize=True, progressive=True)

# Filer utanför styleguide/ som sidorna, CSS:en eller JS:en pekar på
missing = []
sources = [*(root / "styleguide").glob("*.html"), *(root / "styleguide").glob("*/*.css"),
           *(root / "styleguide").glob("*/*.js")]
for src in sources:
    text = re.sub(r"<pre[ >].*?</pre>", "", src.read_text(), flags=re.S)  # kodexempel
    for ref in re.findall(r'(?:src|href)="([^"#?]+)|url\([\'"]?([^\'")#?]+)', text):
        ref = unquote(ref[0] or ref[1])
        if re.match(r"[a-z]+:|/|#", ref):
            continue
        target = (src.parent / ref).resolve()
        if not target.is_relative_to(root):
            continue
        rel = target.relative_to(root)
        dest = out / rel
        if dest.exists():   # redan kopierad eller skapad här (t.ex. förhandsbilder)
            continue
        if target.is_file():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, dest)
        elif not target.exists():
            missing.append(f"{src.relative_to(root)}: {ref}")

(out / "index.html").write_text("""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<title>Magellos formspråk</title>
<meta http-equiv="refresh" content="0; url=styleguide/">
<link rel="canonical" href="styleguide/">
</head>
<body><p><a href="styleguide/">Till styleguiden</a></p></body>
</html>
""")
(out / ".nojekyll").write_text("")

size = sum(p.stat().st_size for p in out.rglob("*") if p.is_file())
print(f"skrev {out.relative_to(root)}/ ({size / 1e6:.1f} MB)")
if missing:
    print("varning, länkar som inte går att lösa:", *missing, sep="\n  ")
