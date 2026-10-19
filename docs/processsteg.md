# Processsteg

Visuell kedja av pil-formade steg som visar ett flöde eller en process. Varje steg är en klickbar eller passiv chevron-form byggd med `clip-path: polygon()`.

---

## Användning

```html
<div class="mg-steps">
  <div class="mg-step mg-step--blue">
    <span class="mg-step__num">Steg 1</span>Behovsanalys
  </div>
  <div class="mg-step mg-step--orange">
    <span class="mg-step__num">Steg 2</span>Arkitektur
  </div>
  <div class="mg-step mg-step--green">
    <span class="mg-step__num">Steg 3</span>Leverans
  </div>
  <div class="mg-step mg-step--magenta">
    <span class="mg-step__num">Steg 4</span>Klar!
  </div>
</div>
```

---

## Färgvarianter

Varje steg får en färgmodifier. Sista steget ska alltid använda `mg-step--magenta`.

| Klass             | Färg          | Textkorg |
|-------------------|---------------|----------|
| `mg-step--blue`   | `#31ABE2`     | Vit      |
| `mg-step--orange` | `#F9B804`     | Svart    |
| `mg-step--red`    | `#E3012F`     | Vit      |
| `mg-step--yellow` | `#FFDC00`     | Svart    |
| `mg-step--green`  | `#1BA660`     | Vit      |
| `mg-step--magenta`| `#EC008C`     | Vit      |

> **Regel:** Slutsteget i en process ska alltid märkas med `mg-step--magenta`.

---

## Regler och beteende

- **Första steget** har ingen indragning till vänster (enkelt polygon utan bakre spets).
- **Mellansteg och sista steget** har chevron-form (spets höger + indragning vänster).
- Stegen växer jämnt med `flex: 1` och bryter till ny rad vid smalare viewports.
- `mg-step__num` är en liten etikett (t.ex. "Steg 1") ovanför stegtexten.

---

## Tillgänglighet

- Använd `role="list"` på `.mg-steps` och `role="listitem"` på varje `.mg-step` när det är en semantisk lista.
- Om steg är interaktiva, använd `<button>` eller `<a>` i stället för `<div>`.
- Säkerställ tillräcklig kontrast: mörk text på gula/orange bakgrunder, vit text på blå/röda/gröna/magenta bakgrunder.

---

## Varianter

### Fyra steg (standard)

```html
<div class="mg-steps">
  <div class="mg-step mg-step--blue"><span class="mg-step__num">Steg 1</span>Behovsanalys</div>
  <div class="mg-step mg-step--orange"><span class="mg-step__num">Steg 2</span>Arkitektur</div>
  <div class="mg-step mg-step--green"><span class="mg-step__num">Steg 3</span>Leverans</div>
  <div class="mg-step mg-step--magenta"><span class="mg-step__num">Steg 4</span>Klar!</div>
</div>
```

### Tre steg

```html
<div class="mg-steps">
  <div class="mg-step mg-step--blue"><span class="mg-step__num">Steg 1</span>Analys</div>
  <div class="mg-step mg-step--orange"><span class="mg-step__num">Steg 2</span>Bygge</div>
  <div class="mg-step mg-step--magenta"><span class="mg-step__num">Steg 3</span>Driftsättning</div>
</div>
```

### Fem steg (alla färger)

```html
<div class="mg-steps">
  <div class="mg-step mg-step--blue"><span class="mg-step__num">Steg 1</span>Analys</div>
  <div class="mg-step mg-step--orange"><span class="mg-step__num">Steg 2</span>Design</div>
  <div class="mg-step mg-step--yellow"><span class="mg-step__num">Steg 3</span>Bygge</div>
  <div class="mg-step mg-step--green"><span class="mg-step__num">Steg 4</span>Test</div>
  <div class="mg-step mg-step--magenta"><span class="mg-step__num">Steg 5</span>Leverans</div>
</div>
```

---

## CSS-referens

```css
.mg-steps {
  display: flex;
  gap: 3px;
  flex-wrap: wrap;
}

.mg-step {
  flex: 1;
  min-width: 120px;
  padding: 14px 20px 14px 28px;
  clip-path: polygon(
    1% 4%,
    calc(100% - 16px) 1%,
    100% 50%,
    calc(100% - 16px) 96%,
    2% 100%,
    14px 50%
  );
  font: 700 .875rem/1.3 var(--mg-font-head);
  text-align: center;
}

/* Första steget saknar vänster spets */
.mg-step:first-child {
  clip-path: polygon(
    1% 4%,
    calc(100% - 16px) 1%,
    100% 50%,
    calc(100% - 16px) 96%,
    2% 100%
  );
}

.mg-step__num {
  display: block;
  font-size: .7rem;
  font-weight: 400;
  opacity: .7;
  margin-bottom: 4px;
}
```
