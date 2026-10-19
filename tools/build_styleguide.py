#!/usr/bin/env python3
"""Bygger styleguiden (styleguide/*.html) från sidmodulerna i tools/pages/.

Kör:  python3 tools/build_styleguide.py

Varje sida är en Python-modul i tools/pages/ med PAGE = {slug, title, kicker, lead, body(),
actions (valfri)}. Layouten (header, sidospår, mobilmeny, footer) genereras här från NAV,
så att menyn är samma på alla sidor. Resultatet är ren statisk HTML utan byggsteg i webbläsaren.
"""
import importlib, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "styleguide"
sys.path.insert(0, str(ROOT / "tools"))
import sg  # noqa: E402

LOGO = (ROOT / "tools/partials/logo.svg.html").read_text()
BURGER = (ROOT / "tools/partials/burger.html").read_text()
CLOSE = (ROOT / "tools/partials/close.html").read_text()
CHEVRON = ('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 6L8 10L12 6" '
           'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ── Navigation: två nivåer. (etikett, url, [barn]) ──────────────────────────
NAV = [
    ("Grunder", "farg.html", [
        ("Färg", "farg.html"),
        ("Form", "form.html"),
        ("Typografi", "typografi.html"),
        ("Specialtypsnitt", "typsnitt.html"),
        ("Bilder &amp; ikoner", "bilder-ikoner.html"),
        ("Avstånd &amp; rörelse", "avstand-rorelse.html"),
    ]),
    ("Byggstenar", "komponenter.html", [
        ("Komponenter", "komponenter.html"),
        ("Sektioner", "sektioner.html"),
        ("Formulär &amp; feedback", "formular-feedback.html"),
        ("Markdown", "markdown.html"),
    ]),
    ("Navigation", "navigation.html", []),
    ("Mallar", "office.html", [
        ("Word &amp; PowerPoint", "office.html"),
        ("E-postsignatur", "e-postsignatur.html"),
    ]),
]
FEATURED = ("Tokens (JSON)", "../tokens/tokens.json")

PAGES = ["index", "farg", "form", "typografi", "typsnitt", "bilder-ikoner", "avstand-rorelse",
         "komponenter", "sektioner", "formular-feedback", "navigation", "markdown", "office",
         "e-postsignatur"]


def is_active(slug, url):
    return url == f"{slug}.html"


def nav_links(slug):
    out = []
    for label, url, kids in NAV:
        active = any(is_active(slug, k[1]) for k in kids) or (not kids and is_active(slug, url))
        cls = ' class="is-active"' if active else ""
        if kids:
            sub = "".join(
                f'<li><a href="{u}"{" class=\"is-active\"" if is_active(slug, u) else ""}>{l}</a></li>' for l, u in kids)
            out.append(
                f'<li class="mg-nav__has-sub">\n          <a href="{url}"{cls}>{label}</a>\n'
                f'          <button class="mg-nav__chevron-btn" aria-expanded="false" aria-label="Expandera {label}">{CHEVRON}</button>\n'
                f'          <ul class="mg-nav__sub">{sub}</ul>\n        </li>')
        else:
            out.append(f'<li><a href="{url}"{cls}>{label}</a></li>')
    return "\n        ".join(out)


def side_links(slug):
    out = []
    for label, url, kids in NAV:
        active = any(is_active(slug, k[1]) for k in kids) or (not kids and is_active(slug, url))
        cls = ' class="is-active"' if active else ""
        if kids:
            sub = "".join(
                f'<li><a href="{u}"{" class=\"is-active\"" if is_active(slug, u) else ""}>{l}</a></li>' for l, u in kids)
            out.append(
                f'<li class="mg-side-has-sub">\n      <div class="mg-side-parent">\n        <a href="{url}"{cls}>{label}</a>\n'
                f'        <button class="mg-side-toggle" aria-expanded="false" aria-label="Visa undermeny">{CHEVRON}</button>\n'
                f'      </div>\n      <ul class="mg-side-sub">{sub}</ul>\n    </li>')
        else:
            out.append(f'<li><a href="{url}"{cls}>{label}</a></li>')
    return "\n    ".join(out)


def mob_links(slug):
    out = []
    for label, url, kids in NAV:
        active = any(is_active(slug, k[1]) for k in kids) or (not kids and is_active(slug, url))
        cls = ' class="is-active"' if active else ""
        if kids:
            sub = "".join(
                f'<li><a href="{u}"{" class=\"is-active\"" if is_active(slug, u) else ""}>{l}</a></li>' for l, u in kids)
            out.append(
                f'<li class="mg-mob-has-sub">\n      <div class="mg-mob-parent">\n        <a href="{url}"{cls}>{label}</a>\n'
                f'        <button class="mg-mob-toggle" aria-expanded="false" aria-label="Visa undermeny">{CHEVRON}</button>\n'
                f'      </div>\n      <ul class="mg-mob-sub">{sub}</ul>\n    </li>')
        else:
            out.append(f'<li><a href="{url}"{cls}>{label}</a></li>')
    return "\n    ".join(out)


def layout(page):
    slug = page["slug"]
    title = page["title"].replace("&amp;", "&")
    crumb = ("" if slug == "index" else
             f'''<nav class="mg-breadcrumb" aria-label="Brödsmula">
      <a href="index.html">Hem</a>
      <span class="mg-breadcrumb__sep">/</span>
      <span aria-current="page">{page["title"]}</span>
    </nav>''')
    actions = ""
    if page.get("actions"):
        actions = '<div class="mg-ingang-actions">' + "".join(
            f'<a href="{u}" class="mg-btn mg-btn--{k}">{l}</a>' for l, u, k in page["actions"]) + "</div>"
    extra_head = page.get("head", "")
    body_cls = f' class="{page["body_class"]}"' if page.get("body_class") else ""
    return f'''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Magello styleguide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;0,700;1,400&family=Roboto+Condensed:wght@400;500;700&display=swap" rel="stylesheet">
{extra_head}<link rel="stylesheet" href="css/magello.css">
<link rel="stylesheet" href="css/styleguide.css">
</head>
<body{body_cls}>

<!-- ═══ SIDOSPÅR ═══════════════════════════════════════════════ -->
<div class="mg-side-nav" aria-label="Sidonavigering">
  <a class="mg-side-nav__logo" href="index.html" aria-label="Magello">
    <img src="../assets/logos/icon-logotype.svg" alt="Magello">
  </a>
  <ul class="mg-side-nav__links">
    {side_links(slug)}
  </ul>
  <a class="mg-side-nav__featured" href="{FEATURED[1]}">{FEATURED[0]}</a>
</div>

<!-- ═══ HEADER ═════════════════════════════════════════════════ -->
<div class="mg-page-header mg-page-header--rotate">
  <div class="mg-header-shape"></div>
  <nav class="mg-nav">
    <div class="mg-nav__inner">
      <a class="mg-nav__logo" href="index.html" aria-label="Magello">
        {LOGO}
      </a>
      <ul class="mg-nav__links">
        {nav_links(slug)}
      </ul>
      <a class="mg-nav__featured" href="{FEATURED[1]}">{FEATURED[0]}</a>
      {BURGER}
    </div>
  </nav>
</div>

<!-- ═══ MOBILMENY ══════════════════════════════════════════════ -->
<div class="mg-mobile-menu" id="mobile-menu" aria-hidden="true" aria-label="Mobilnavigering">
  <div class="mg-mobile-menu__head">
    <a href="index.html" class="mg-nav__logo" aria-label="Magello">
      {LOGO.replace("<svg ", '<svg style="height:32px;width:auto" ', 1)}
    </a>
    {CLOSE}
  </div>
  <ul class="mg-mobile-menu__links">
    {mob_links(slug)}
  </ul>
  <a class="mg-mobile-menu__featured" href="{FEATURED[1]}">{FEATURED[0]}</a>
</div>

<!-- ═══ SIDHUVUD ═══════════════════════════════════════════════ -->
<div class="mg-ingang-hero">
  <div class="mg-ingang-col">
    {crumb}
    <p class="mg-kicker">{page["kicker"]}</p>
    <h1 class="mg-ingang-title">{page["h1"] if page.get("h1") else page["title"]}</h1>
    <p class="mg-ingang-sub">{page["lead"]}</p>
    {actions}
  </div>
</div>

<main id="main-content">
{page["body"]}
</main>

{page.get("after", "")}
<!-- ═══ FOOTER ═════════════════════════════════════════════════ -->
<footer class="mg-footer">
  <div class="mg-wrap">
    <div class="mg-footer__inner">
      <div class="mg-footer__col"><span class="mg-footer__brand">Magello styleguide</span>Version 0.1<br>Formspråk för webb, dokument<br>och sociala medier</div>
      <div class="mg-footer__col">
        <a href="../tokens/tokens.json">tokens.json</a><br>
        <a href="../docs/design-language.md">design-language.md</a><br>
        <a href="../docs/design-guidelines-web.md">design-guidelines-web.md</a>
      </div>
      <div class="mg-footer__col" style="text-align:right">Västgötagatan 2<br>118 27 Stockholm<br>info@magello.se</div>
    </div>
  </div>
</footer>

<script src="js/magello.js"></script>
</body>
</html>
'''


def main():
    OUT.mkdir(exist_ok=True)
    for slug in PAGES:
        mod = importlib.import_module(f"pages.{slug.replace('-', '_')}")
        page = dict(mod.PAGE)
        page["slug"] = slug
        page["body"] = mod.body(sg)
        (OUT / f"{slug}.html").write_text(layout(page))
        print("skrev", f"styleguide/{slug}.html")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    main()
