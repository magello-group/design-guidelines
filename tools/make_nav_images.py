#!/usr/bin/env python3
"""Tar skärmdumpar av navigationens lägen till styleguide/img/ (används på sidan Navigation).

Kräver Google Chrome (sätt CHROME=/sökväg/till/chrome om den inte ligger på standardplatsen) och Pillow.
Kör:  python3 tools/build_styleguide.py && python3 tools/make_nav_images.py
"""
import os, pathlib, shutil, subprocess, sys, time
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SG = ROOT / "styleguide"
OUT = SG / "img"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
PORT = 7981

INJECT = """<style>*,*::before,*::after{transition:none!important}</style><script>window.addEventListener('load',()=>setTimeout(()=>{const s=location.hash;
if(s.includes('drop')){document.querySelector('.mg-nav__has-sub').dispatchEvent(new MouseEvent('mouseenter'));}
if(s.includes('side')){document.querySelector('.mg-page-header').classList.add('is-scrolled');
 document.querySelector('.mg-side-nav').classList.add('is-visible');
 setTimeout(()=>{const a=document.querySelector('.mg-side-parent > a');a&&a.click();},300);}
if(s.includes('menu')){document.querySelector('.mg-nav__burger').click();
 setTimeout(()=>{const t=document.querySelector('.mg-mob-toggle');t&&t.click();},60);}
},200));</script>"""

# (filnamn, hash, fönsterstorlek, beskärning (x0, y0, x1, y1) eller None)
SHOTS = [
    ("nav-header.png", "#", (1280, 150), None),
    ("nav-dropdown.png", "#drop", (1280, 300), None),
    ("nav-sidespar.png", "#side", (1280, 640), (900, 0, 1280, 640)),
    ("nav-mobil.png", "#", (390, 150), None),
    ("nav-mobilmeny.png", "#menu", (390, 640), None),
]


def main():
    OUT.mkdir(exist_ok=True)
    tmp = SG / "_state.html"
    html = (SG / "navigation.html").read_text().replace("</body>", INJECT + "</body>")
    tmp.write_text(html)
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT)], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.3)
    try:
        for name, hash_, (w, h), crop in SHOTS:
            raw = OUT / ("raw_" + name)
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                            f"--window-size={w},{h}", "--virtual-time-budget=12000", f"--screenshot={raw}",
                            f"http://localhost:{PORT}/styleguide/_state.html{hash_}"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
            im = Image.open(raw)
            if crop: im = im.crop(crop)
            im.save(OUT / name, optimize=True)
            raw.unlink()
            print("skrev", OUT / name)
    finally:
        srv.terminate()
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
