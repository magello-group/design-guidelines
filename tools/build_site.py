#!/usr/bin/env python3
"""Sätter ihop webbplatsen för GitHub Pages i _site/.

Webbplatsen speglar repots katalogstruktur, så att styleguidens relativa länkar
(../assets/, ../tokens/, ../docs/) fungerar även under en undermapp som
https://magello-group.github.io/design-guidelines/. Tunga filer tas inte med:
av fotobiblioteket kopieras bara de foton som styleguiden använder. Kör:

    python3 tools/build_site.py
    python3 -m http.server 8000 -d _site     # öppna http://localhost:8000/
"""
import pathlib, re, shutil
from urllib.parse import unquote

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "_site"
# Kopieras alltid, i sin helhet
dirs = ["styleguide", "tokens", "docs", "assets/graphics", "assets/logos", "assets/shapes"]
# Office-mallarna och howto-dokumenten, som nedladdningar
files = ["assets/templates/Powerpoint-mall.potx", "assets/templates/Word-mall.dotx",
         "assets/templates/Powerpoint-mall-howto.pptx", "assets/templates/Word-mall-howto.docx"]

if out.exists():
    shutil.rmtree(out)
for d in dirs:
    shutil.copytree(root / d, out / d, ignore=shutil.ignore_patterns(".DS_Store"))
for f in files:
    (out / f).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / f, out / f)

# Publiceras inte. Specialtypsnittet saknar licenstext, så det tas med först när
# användningsrätten är klarlagd. Sidan faller då tillbaka på Roboto Condensed.
exclude = ["assets/fonts/"]

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
        if any(rel.as_posix().startswith(e) for e in exclude):
            continue
        dest = out / rel
        if target.is_file() and not dest.exists():
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
