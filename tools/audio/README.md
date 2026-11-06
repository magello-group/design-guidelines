# Ljud — källkod

Magellos ljud (`assets/audio/`) är syntetiserat från grunden i Python, utan samplingar. Här finns koden, så att nya versioner kan göras med samma ljud, ackord och motiv.

| Fil | Vad |
|---|---|
| `synth.py` | Instrument, effekter, mastring och ackorden (Dm9 – G13 – Cmaj9 – A7b13) |
| `compose_crisp.py` | Stilarna och arrangemangen. Magellos ljud är stilen `kondenserad` (110 BPM) |

Kräver Python 3.12 med `numpy`, `scipy`, `soundfile` och `pyloudnorm`. Körs inte av GitHub Pages.

```bash
python tools/audio/compose_crisp.py tools/audio ut kondenserad          # intro, intro 15 s och bakgrundsloop (WAV)
python tools/audio/compose_crisp.py tools/audio ut sting kondenserad    # ljudlogotypen
```

Filerna i `assets/audio/` är AAC (M4A) 256 kbit/s, utom 45-minutersversionen som är 128 kbit/s. Den är bakgrundsloopen upprepad med 8 sekunders uttoning. Byt namn enligt `assets/audio/` när du lägger in nya versioner, och skriv en rad i `DECISIONS.md`.
