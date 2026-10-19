#!/usr/bin/env python3
"""Genererar ett Tailwind-tema (tokens/tailwind.css) från tokens/tokens.json.

Temat är för Tailwind v4 (CSS-first). Importera det efter Tailwind:

    @import "tailwindcss";
    @import "./tailwind.css";

Då finns Magellos färger, typsnitt, avstånd, containerbredd och brytpunkter som
utilities, till exempel bg-mg-rose-100, text-mg-magenta, font-head, p-mg-5,
max-w-mg och nav:flex. Komponenterna (knappar, kort, navigation) kommer fortfarande
från styleguide/css/magello.css, som länkas före projektets egen CSS.

Kör:  python3 tools/make_tailwind.py
"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
t = json.loads((root / "tokens" / "tokens.json").read_text())
L = t["layout"]

lines = ["/* Genererad av tools/make_tailwind.py från tokens/tokens.json. Ändra inte för hand. */",
         "@theme {"]
lines.append("  /* Färger: bg-mg-rose-100, text-mg-magenta … */")
for group in ("neutral", "accent"):
    for name, c in t["color"][group].items():
        lines.append(f"  --color-mg-{name}: {c['value']};")
lines.append("  /* Typsnitt: font-head, font-body, font-code */")
for key in ("head", "body", "code"):
    f = t["font"][key]
    fams = [f["family"]] + [x.strip() for x in f["fallback"].split(",")]
    fams = [f'"{x}"' if " " in x else x for x in fams]
    lines.append(f"  --font-{key}: {', '.join(fams)};")
lines.append("  /* Avstånd: p-mg-5, gap-mg-6, mt-mg-8 … */")
for k, v in t["space"].items():
    if k != "unit":
        lines.append(f"  --spacing-mg-{k}: {v}px;")
lines.append("  /* Containerbredd: max-w-mg (inklusive gutter), max-w-mg-text (löptext) */")
lines.append(f"  --container-mg: {L['contentWidth']}px;")
lines.append("  --container-mg-text: 680px;")
lines.append("  /* Brytpunkter: tablet: (600), nav: (769, ovanför hamburgerläget), desktop: (1024) */")
bp = L["breakpoints"]
lines.append(f"  --breakpoint-tablet: {bp['tablet']}px;")
lines.append(f"  --breakpoint-nav: {bp['mobileMenu'] + 1}px;")
lines.append(f"  --breakpoint-desktop: {bp['desktop']}px;")
lines.append("}")
out = root / "tokens" / "tailwind.css"
out.write_text("\n".join(lines) + "\n")
print("skrev", out.relative_to(root))
