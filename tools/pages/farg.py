import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TOK = json.loads((ROOT / "tokens" / "tokens.json").read_text())

PAGE = dict(
    title="Färg", kicker="Grunder",
    lead="Sidan ska i huvudsak vara svart, vit och rosagrå. Magenta är den enda accent som får synas stort. Övriga accenter lever i ikoner, steg och status.",
)


def lum(hex_):
    h = hex_.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def swatch(key, spec):
    hex_ = spec["value"]
    dark = lum(hex_) < 0.35
    fg = "#fff" if dark else "#000"
    cls = "sg-swatch__chip" + (" sg-swatch__chip--white" if hex_.upper() == "#FFFFFF" else "")
    return (f'<div class="sg-swatch"><div class="{cls}" style="background:{hex_};color:{fg}">{hex_}</div>'
            f'<div class="sg-swatch__body"><div class="sg-swatch__name">{key}</div>'
            f'<div class="sg-swatch__meta"><code>{spec["css"]}</code></div>'
            f'<div class="sg-swatch__role">{spec["role"]}</div></div></div>')


def body(sg):
    c = TOK["color"]
    neutrals = "".join(swatch(k, v) for k, v in c["neutral"].items())
    accents = "".join(swatch(k, v) for k, v in c["accent"].items())
    N = {k: v["value"] for k, v in c["neutral"].items()}
    A = {k: v["value"] for k, v in c["accent"].items()}

    palette = sg.block("palett", "Paletten", "Neutraler och accenter",
        "Färgerna finns som tokens (<code>--mg-*</code>) i <code>css/magello.css</code> och som värden i <code>tokens/tokens.json</code>. Använd alltid token eller hex från tabellen. Hitta inte på mellanvärden.",
        sg.sub("Neutraler", "Det här är sidans grund: text, ytor och struktur.") +
        f'<div class="sg-swatches">{neutrals}</div>' +
        sg.sub("Accenter", "Magenta är primär. De övriga används i ikoner, processteg och status, aldrig som textfärg eller stor yta.") +
        f'<div class="sg-swatches">{accents}</div>' +
        sg.text("Den vita rutan har en ram i rosagrått enbart för att den ska synas här. Vit yta på vit sida har ingen kant i designen."))

    # proportioner
    parts = [("Vitt", 55, N["white"]), ("Rosagrått", 24, N["rose-100"]), ("Text (svart, grått)", 13, N["black"]), ("Magenta", 5, A["magenta"]), ("Övriga accenter", 3, A["blue"])]
    bar = '<div class="sg-ratio">' + "".join(f'<span style="flex:{w};background:{col}"></span>' for _, w, col in parts) + "</div>"
    legend = '<div class="sg-ratio-legend">' + "".join(f"<span>{n} · ca {w} %</span>" for n, w, _ in parts) + "</div>"
    ratio_block = sg.block("proportioner", "Proportioner", "Så mycket av varje",
        "Rosagrått ger värme, svart ger tydlighet och magenta pekar ut det viktigaste. Ju mindre magenta, desto starkare blir den.",
        sg.demo(bar + legend) +
        sg.use(do=["Låt vitt och rosagrått bära ytorna", "Använd magenta för en sak i taget: primär knapp, sektionsrubrik, länk eller utvalt ord", "Låt ikoner och processteg bära de övriga accenterna"],
               dont=["Fylla stora ytor med magenta och lägga brödtext ovanpå", "Använda två accenter som textfärg bredvid varandra", "Göra sektioner svarta, mörkgrå eller starkt färgade"],
               note=["Mörka ytor används inte i marknadsmaterial. Verktyg och appar har en mörk rosagrå topbar (<code>#3D2535</code>) som enda undantag"]))

    # accent som fyllnad
    fill = sg.block("fyllnad", "Regel", "Accentfärger är fyllnad, aldrig kant",
        "Magenta och de andra accenterna fyller former, ikoner, knappar och text. De ritas aldrig som streck, understrykning eller kantlinje.",
        sg.demo(
            '<div class="sg-two"><div><span class="sg-demo-label">Rätt</span><div class="sg-row sg-row--top">'
            '<a class="mg-btn mg-btn--primary" href="#fyllnad">Magenta fyllnad</a>'
            '<span class="mg-pill mg-pill--success">Klar</span><span class="mg-pill mg-pill--loading">Bearbetar</span></div></div>'
            '<div><span class="sg-demo-label">Fel</span><div style="padding:14px 18px;border-left:3px solid var(--mg-magenta);background:#fff;color:var(--mg-text-2);font-size:.9375rem">Accentfärg som kantlinje bryter principen.</div></div></div>'
        ) +
        sg.use(do=["Fyll knappar, etiketter, ikoner och former", "Använd magenta som textfärg för H2, länkar och enstaka ord", "Behöver du en understrykning: gör den som en skev polygon (som i ”Lediga jobb”)"],
               dont=["<code>border-left: 3px solid magenta</code> som accentlinje", "Färgade streck som avgränsare mellan sektioner", "Understrukna rubriker i accentfärg"]) +
        sg.text("Undantag: ett fokus- och statusmarkerat formulärfält byter kantfärg (blå, röd, grön). Det är funktionellt och beskrivs under <a href=\"formular-feedback.html\">Formulär &amp; feedback</a>."))

    # kontrast
    pairs = [
        ("Brödtext", N["black"], N["white"]),
        ("Sekundär text", N["text-2"], N["white"]),
        ("Brödtext på rosa", N["black"], N["rose-100"]),
        ("Sekundär text på rosa", N["text-2"], N["rose-100"]),
        ("Magenta text på vitt", A["magenta"], N["white"]),
        ("Vit text på magenta (knapp)", N["white"], A["magenta"]),
        ("Svart text på rose-200 (sekundär knapp)", N["black"], N["rose-200"]),
        ("Grå 300 text på vitt", N["grey-300"], N["white"]),
        ("Vit text på blå", N["white"], A["blue"]),
        ("Svart text på gul", N["black"], A["yellow"]),
        ("Vit text på grön", N["white"], A["green"]),
        ("Vit text på röd", N["white"], A["red"]),
    ]
    rows = []
    for name, fg, bg in pairs:
        r = ratio(fg, bg)
        ok = "Ja" if r >= 4.5 else ("Endast stor text" if r >= 3 else "Nej")
        cls = "sg-pass" if r >= 4.5 else ("" if r >= 3 else "sg-fail")
        rows.append([name, f'<span class="sg-ratio-chip" style="background:{bg};color:{fg}">Aa Magello</span>', f"{r:.1f} : 1", f'<span class="{cls}">{ok}</span>'])
    contrast = sg.block("kontrast", "Tillgänglighet", "Kontrast",
        "Brödtext ska ha minst 4,5 : 1 mot bakgrunden (WCAG AA). Stor text (från 24 px, eller 19 px fet) klarar 3 : 1. Värdena nedan är beräknade från tokens.",
        sg.spec(["Kombination", "Prov", "Kvot", "Klarar AA för brödtext"], rows) +
        sg.use(do=["Använd svart eller <code>--mg-text-2</code> för brödtext", "Använd magenta på vitt för rubriker och länkar (stor eller fet text)", "Kontrollera nya kombinationer innan du använder dem"],
               dont=["Grå 300 som brödtext. Den är bara till diskreta etiketter, årtal och brödsmula", "Vit liten text på gul eller blå yta"]),
        )

    # semantik
    sem = [("Fel", A["red"], "#fff", "mg-pill--error", "Något gick fel eller är ogiltigt"),
           ("Klart", A["green"], "#fff", "mg-pill--success", "Lyckades, giltigt, godkänt"),
           ("Info / bearbetar", A["blue"], "#fff", "mg-pill--loading", "Pågår eller neutral information"),
           ("Varning", A["yellow"], "#000", "mg-pill--warning", "Kan bli ett problem (svart text)")]
    sem_rows = [[f'<span class="mg-pill {cls}">{n}</span>', f"<code>{col}</code>", d] for n, col, _, cls, d in sem]
    semantic = sg.block("status", "Status", "Färger med betydelse",
        "Accentfärgerna får också en semantisk roll i gränssnitt. Roll och färg hänger ihop. Använd aldrig röd för något positivt.",
        sg.spec(["Roll", "Färg", "Betyder"], sem_rows), rose=True)

    return palette + ratio_block + fill + contrast + semantic
