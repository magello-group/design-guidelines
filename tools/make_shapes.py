#!/usr/bin/env python3
"""Genererar SVG-former (assets/shapes/*.svg) från tokens/tokens.json.

Formerna är polygoner i procent av bredd/höjd. SVG:erna har viewBox 0 0 100 100 och
preserveAspectRatio="none", så de kan skalas till valfri proportion i Word, PowerPoint,
Figma m.m. Kör:  python3 tools/make_shapes.py
"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((root / "tokens" / "tokens.json").read_text())
colors = {**tokens["color"]["neutral"], **tokens["color"]["accent"]}
out = root / "assets" / "shapes"
out.mkdir(parents=True, exist_ok=True)

def svg(points, fill, title):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="200" height="120" '
            f'preserveAspectRatio="none" role="img">\n  <title>{title}</title>\n'
            f'  <polygon points="{pts}" fill="{fill}"/>\n</svg>\n')

for name, spec in tokens["shape"]["polygons"].items():
    fill = colors[spec["fill"]]["value"]
    (out / f"{name}.svg").write_text(svg(spec["points"], fill, f'{name}: {spec["use"]}'))
    if spec.get("hover"):
        (out / f"{name}-hover.svg").write_text(svg(spec["hover"], fill, f'{name} (hover)'))
print(f"{len(list(out.glob('*.svg')))} former skrevna till {out}")
