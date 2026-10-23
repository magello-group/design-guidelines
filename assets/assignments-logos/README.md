# Employer logos

Logos shown beside each assignment in the generated PDF. Resolution is deterministic
(no LLM), done in `render.py` → `resolve_logo()`:

1. **`manifest.json`** — maps an organization name (or alias) to a filename here.
   Keys are matched case-insensitively against each assignment's `organization`.
2. **Filename fallback** — if an organization is not in the manifest, `render.py` looks
   for `<org-slug>.{svg,png,jpg,jpeg}` (e.g. `Suicide Zero` → `suicide-zero.png`).
3. If nothing matches, the assignment simply renders without a logo (no error).

## Adding a logo

Drop the image file in this folder and, unless its name already slugifies from the
organization, add an entry to `manifest.json`:

```json
"Organisationens namn": "filnamn.png"
```

- SVG is preferred (crisp at print) and embedded as-is; raster (PNG/JPG) is capped at
  400px wide and re-encoded as PNG.
- Keep logos reasonably square/landscape; they are rendered at up to 26mm × 16mm.
- Only commit logos you have the right to use.
