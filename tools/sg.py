"""Hjälpfunktioner för att skriva styleguide-sidor (används av build_styleguide.py).

Allt som returneras är HTML-strängar som använder klasser från css/magello.css
(mg-*) och css/styleguide.css (sg-*). Skriv nytt innehåll med de här funktionerna
så blir alla sidor uppbyggda på samma sätt.
"""
import html


def esc(text):
    return html.escape(text, quote=False)


def demo(inner, variant=""):
    """Levande exempel i en rosa polygonruta. variant: '' | 'white' | 'plain'."""
    cls = "sg-demo" + (f" sg-demo--{variant}" if variant else "")
    return f'<div class="{cls}">\n{inner}\n</div>'


def code(text):
    """Kodruta (HTML/CSS-exempel). Texten escapas."""
    return f'<pre class="sg-code"><code>{esc(text.strip(chr(10)))}</code></pre>'


def _card(kind, label, items):
    pill = {"do": ("success", label or "Gör"), "dont": ("error", label or "Gör inte"), "note": ("loading", label or "Tänk på")}[kind]
    lis = "".join(f"<li>{i}</li>" for i in items)
    return (f'<div class="sg-use__card"><span class="mg-pill mg-pill--{pill[0]}">{pill[1]}</span>'
            f'<ul>{lis}</ul></div>')


def use(do=None, dont=None, note=None, do_label=None, dont_label=None, note_label=None):
    """Tre kort: Gör / Gör inte / Tänk på. Utelämna det du inte behöver."""
    cards = []
    if do: cards.append(_card("do", do_label, do))
    if dont: cards.append(_card("dont", dont_label, dont))
    if note: cards.append(_card("note", note_label, note))
    return '<div class="sg-use">' + "".join(cards) + "</div>"


def spec(headers, rows, cls=""):
    """Tabell med komponentens egenskaper. rows = lista av listor (HTML tillåts)."""
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="mg-table-wrap"><table class="mg-table {cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def block(id_, label, title, lead, body="", level=2, rose=False):
    """Ett dokumenterat avsnitt: etikett, rubrik, ingress och innehåll. rose=True ger rosagrå sektion."""
    lead_html = f"<p>{lead}</p>" if lead else ""
    cls = "mg-section--rose sg-block sg-block--rose" if rose else "sg-block"
    return (f'<section class="{cls}" id="{id_}" aria-labelledby="h-{id_}">\n<div class="mg-wrap">\n'
            f'  <div class="mg-section-head">\n    <p class="mg-label">{label}</p>\n'
            f'    <h{level} id="h-{id_}">{title}</h{level}>\n    {lead_html}\n  </div>\n{body}\n</div>\n</section>\n')


def sub(title, text="", level=3):
    """Underrubrik med valfri text inne i ett block."""
    t = f"<p class=\"sg-text\">{text}</p>" if text else ""
    return f'<h{level} class="sg-sub">{title}</h{level}>{t}'


def text(s):
    return f'<p class="sg-text">{s}</p>'


def props(rows):
    """Liten lista med egenskaper (Klass, Fil, Strapi …) som pill-liknande rader."""
    items = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    return f'<dl class="sg-props">{items}</dl>'


def link_cards(items):
    """Erbjudandekort (ikon + text + länk) till andra sidor.
    items = [(ikon, rubrik, text, url, länktext)], ikon = filnamn i assets/graphics/."""
    cards = "".join(
        f'<div class="mg-offer-card"><div class="mg-offer-card__icon"><img src="../assets/graphics/{i}" alt=""></div>'
        f'<div class="mg-offer-card__body"><h3 class="mg-offer-card__title">{t}</h3>'
        f'<p class="mg-offer-card__desc">{d}</p><a class="mg-offer-card__link" href="{u}">{lt} →</a></div></div>'
        for i, t, d, u, lt in items)
    return f'<div class="mg-offer-grid">{cards}</div>'
