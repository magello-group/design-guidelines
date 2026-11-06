"""Crisp, airy alternatives inspired by the typography (Roboto Condensed):
clean precise transients, open highs, generous space between notes (letter-spacing),
no tape wobble. Same harmony and A-G-E signature motif as the lofi set.
usage: python compose_crisp.py <dir-with-synth.py> <outdir> [style ...]
"""
import sys
sys.path.insert(0, sys.argv[1])
from synth import *

OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

MEL = [
    (0, 6, 81, 2, .80), (0, 8, 79, 4, 1.0), (0, 12, 76, 4, .85),
    (1, 2, 74, 2, .70), (1, 4, 76, 2, .75), (1, 8, 79, 6, .90),
    (2, 6, 81, 2, .80), (2, 8, 79, 4, 1.0), (2, 12, 76, 4, .85),
    (3, 4, 77, 2, .75), (3, 8, 76, 4, .85), (3, 12, 73, 4, .80),
    (4, 6, 81, 2, .80), (4, 8, 79, 4, 1.0), (4, 12, 76, 2, .85), (4, 14, 74, 2, .70),
    (5, 0, 76, 4, .85), (5, 6, 79, 2, .75), (5, 8, 83, 6, .95),
    (6, 6, 81, 2, .80), (6, 8, 79, 4, 1.0), (6, 12, 76, 4, .85),
    (7, 2, 77, 2, .70), (7, 4, 76, 2, .70), (7, 6, 74, 2, .70), (7, 8, 76, 3, .80),
]

# ---------- crisp instruments ----------
def ep_crisp(m, dur, vel):
    f = mtof(m); t = T(dur + 0.3)
    I = (0.8 + 2.0 * vel) * np.exp(-t / 0.09) + 0.15
    y = np.sin(2 * np.pi * f * t + I * np.sin(2 * np.pi * f * t))
    if f * 14 < 18000:
        y += vel * 0.35 * np.sin(2 * np.pi * f * 14.0 * t) * np.exp(-t / 0.012)
    dec = 1.4 * (262 / f) ** 0.5
    env = (1 - np.exp(-t / 0.0008)) * np.exp(-t / dec)
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.06)
    return y * env * vel

def pluck(m, dur, vel):
    f = mtof(m); t = T(dur + 0.25); y = np.zeros(len(t))
    for k in range(1, int(14000 / f) + 1):
        y += np.sin(2 * np.pi * k * f * t + k * 0.3) / k * np.exp(-t * (2.0 + k * k * 0.8))
    env = 1 - np.exp(-t / 0.0007)
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.05)
    return y * env * vel * 0.6

def glock(m, dur, vel):
    f = mtof(m); t = T(dur + 2.4); y = np.zeros(len(t))
    for r, a, d in [(1, 1, 1.5), (2.76, 0.4, 0.5), (5.40, 0.2, 0.18), (8.93, 0.08, 0.07)]:
        if f * r < 19000: y += a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / d)
    y += 0.12 * hp(rng.standard_normal(len(t)), 5000) * np.exp(-t / 0.0015)
    off = t > dur + 0.5; y[off] *= np.exp(-(t[off] - dur - 0.5) / 0.45)
    return y * vel

def flute(m, dur, vel):
    f = mtof(m); t = T(dur + 0.4)
    ph = 2 * np.pi * np.cumsum(f * (1 + 0.004 * np.sin(2 * np.pi * 5.2 * t) * np.minimum(1, t / 0.4))) / SR
    y = np.sin(ph) + 0.12 * np.sin(2 * ph) + 0.04 * np.sin(3 * ph)
    br = bp(rng.standard_normal(len(t)), min(f * 1.5, 8000), min(f * 6, 16000)) * 0.35
    env = np.minimum(1, t / 0.05) * (0.85 + 0.15 * np.exp(-t / 0.1))
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.12)
    return (y + br * (0.6 + 0.4 * np.exp(-t / 0.08))) * env * vel * 0.8

def sub_bass(m, dur, vel):
    f = mtof(m); t = T(dur + 0.06); ph = 2 * np.pi * f * t
    y = np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.12 * np.sin(8 * ph) * np.exp(-t / 0.006)
    env = (1 - np.exp(-t / 0.002)) * (0.7 + 0.3 * np.exp(-t / 0.15))
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.02)
    return y * env * vel

def kick_crisp(vel=1.0, soft=False, boom=False):
    k = kick(vel, soft=soft, boom=boom)
    t = np.arange(len(k)) / SR
    k += (0.12 if soft else 0.3) * vel * hp(rng.standard_normal(len(k)), 3000) * np.exp(-t / 0.0015)
    return k

def clap(vel=1.0):
    t = T(0.4); env = np.zeros(len(t))
    for o, a in [(0, .8), (0.009, .8), (0.018, 1.0)]:
        tt = t - o; env += (tt >= 0) * np.exp(-np.maximum(tt, 0) / 0.004) * a
    tt = t - 0.018; env += (tt >= 0) * np.exp(-np.maximum(tt, 0) / 0.12) * 0.55
    return bp(rng.standard_normal(len(t)), 900, 8000) * env * vel

def hat_crisp(vel=1.0, open_=False):
    t = T((0.45 if open_ else 0.07) + 0.03)
    m = sum(signal.square(2 * np.pi * f * 2.1 * t + rng.random() * 6) for f in [205.3, 304.4, 369.6, 522.7, 540.0, 800.0])
    y = hp(0.35 * m + rng.standard_normal(len(t)), 8000, 4) * np.exp(-t / (0.18 if open_ else 0.018))
    return y * vel

def tick(vel=1.0):
    t = T(0.03)
    y = 0.5 * np.sin(2 * np.pi * 3600 * t) * np.exp(-t / 0.003) + hp(rng.standard_normal(len(t)), 6000) * np.exp(-t / 0.0012)
    return y * vel

def shaker_crisp(vel=1.0):
    t = T(0.09)
    return hp(rng.standard_normal(len(t)), 7000, 4) * (1 - np.exp(-t / 0.006)) * np.exp(-t / 0.025) * vel

def crash_crisp(vel=1.0, dur=2.6):
    x = crash(vel, dur)
    return hp(x, 6000) * 1.4

def air(n, level):
    """slowly breathing high noise: the 'white space' of the page"""
    t = np.arange(n) / SR
    a = bp(rng.standard_normal((n, 2)), 7000, 15000)
    g = 0.6 + 0.4 * np.sin(2 * np.pi * 0.11 * t[:, None] + np.array([[0.0, 1.3]]))
    return a * g * level

# ---------- styles ----------
STYLES = {
    # 1: letter-spaced: short precise stabs with air between, glass motif
    'sparrad': dict(
        bpm=98, swing=0.06, keys=ep_crisp, mel=[(glock, 0, 1.0)], bassi=sub_bass,
        chord_hits=[(0, 2, .75), (6, 1, .5), (10, 2, .65)],
        bass=[(0, 'r', 4, .95), (10, 'r', 2, .75), (14, 'a', 2, .6)],
        kick=[(0, 1.0), (7, .4), (10, .85)], back=[(4, clap, .8), (12, clap, .9)],
        hats=[.7, 0, .45, .25, .6, 0, .45, 0, .7, 0, .45, .25, .6, 0, .45, 0],
        ticks=[(3, .5), (11, .4)], shake=False, pad=.6, pad_up=12, air=.004,
        rt=2.6, delay=3, delay_fb=.35, keys_delay=.25, roll='tick',
        bed=dict(chord_hits=[(0, 3, .5), (10, 2, .3)], bass=[(0, 'r', 8, .7), (10, 'r', 3, .5)],
                 kick=[(0, .7), (10, .45)], back=[(12, rim, .4)],
                 hats=[.35, 0, .2, 0] * 4, ticks=[(11, .25)], shake=False)),
    # 2: airy: long chords, breathy flute motif doubled with glock, lots of room
    'luftig': dict(
        bpm=92, swing=0.13, keys=ep_crisp, mel=[(flute, 0, .9), (glock, 12, .25)], bassi=bass_note,
        chord_hits=[(0, 12, .55), (10, 5, .4)],
        bass=[(0, 'r', 8, .85), (10, 'f', 4, .6), (14, 'a', 2, .5)],
        kick=[(0, .9), (10, .7)], back=[(4, rim, .55), (12, clap, .55)],
        hats=[.5, .15, .3, .15] * 4, ticks=[], shake=True, pad=1.0, pad_up=12, air=.007,
        rt=3.6, delay=6, delay_fb=.3, keys_delay=.15, roll='shaker',
        bed=dict(chord_hits=[(0, 14, .42)], bass=[(0, 'r', 8, .7), (10, 'f', 4, .45)],
                 kick=[(0, .6), (10, .4)], back=[(12, rim, .3)],
                 hats=[.25, 0, .15, 0] * 4, ticks=[], shake=True)),
    # 3: condensed: tight straight 16ths, pluck arp, more drive
    'kondenserad': dict(
        bpm=110, swing=0.0, keys=pluck, mel=[(glock, 0, 1.0), (pluck, -12, .35)], bassi=sub_bass,
        chord_hits=[(0, 2, .7), (3, 1, .45), (6, 2, .6), (10, 1, .5), (12, 2, .55)], arp=.32,
        bass=[(0, 'r', 3, 1.0), (3, 'r', 1, .6), (6, 'f', 2, .7), (8, 'r', 2, .8), (11, 'r', 1, .6), (14, 'a', 2, .7)],
        kick=[(0, 1.0), (6, .7), (10, .9)], back=[(4, clap, .85), (12, clap, .9)],
        hats=[.7, .3, .5, .3] * 4, open_hat=True, ticks=[(7, .45), (15, .45)], shake=False,
        pad=.5, pad_up=0, air=.003, rt=1.8, delay=2, delay_fb=.3, keys_delay=.12, roll='clap',
        bed=dict(chord_hits=[(0, 2, .45), (6, 2, .3)], arp=.16, bass=[(0, 'r', 6, .7), (8, 'r', 2, .5), (14, 'a', 2, .45)],
                 kick=[(0, .65), (10, .45)], back=[(12, rim, .35)],
                 hats=[.35, .12, .2, .12] * 4, open_hat=False, ticks=[(15, .25)], shake=False)),
}


def chord(bus, inst, name, t, dur, vel, strum=0.006):
    notes = CHORDS[name][0]
    for k, m in enumerate(notes):
        bus.add(inst(m, dur, vr(vel, 0.04)), t + k * strum, 1.0, (k / (len(notes) - 1) - 0.5) * 0.7)


def render(sty, kind, groove_bars=8, tail=6.5):
    st = dict(STYLES[sty]); bed = kind == 'bed'
    if bed: st.update(st['bed'])
    bt = 60 / st['bpm']; s16 = bt / 4; bar = 4 * bt; sw = s16 * st['swing']
    PICK = 0.0 if bed else 2 * bt
    tf = PICK + groove_bars * bar
    L = groove_bars * bar
    N = int(((L + 5.0) if bed else (tf + tail)) * SR)
    drums, keys, bass, mel, pad, fx = (Bus(N) for _ in range(6))
    kicks = []

    def tp(b, p): return max(0.0, PICK + b * bar + p * s16 + (sw if p % 2 else 0) + hum(0.002))

    if not bed:
        # kick-start: reverse-reverb swell of the pickup chord + roll
        src = Bus(int(2.5 * SR))
        chord(src, st['keys'], 'A7b13', 0.02, 0.5, 0.8)
        w = reverb(src.x, ir(2.2, 0.0, 12000))[:int(PICK * SR)][::-1]
        w *= np.linspace(0, 1, len(w))[:, None] ** 1.5
        keys.add(w * 1.6, 0)
        for i in range(8):
            v = 0.15 + 0.8 * (i / 7) ** 1.5
            t0 = i * s16
            if st['roll'] == 'tick': drums.add(tick(v), t0, 0.5, 0.3)
            elif st['roll'] == 'shaker': drums.add(shaker_crisp(v), t0, 0.5, -0.3)
            else: drums.add(clap(v * 0.8), t0, 0.5, 0.0)
        rc = crash_crisp(0.5, 1.4)[::-1]
        fx.add(rc * np.linspace(0, 1, len(rc))[:, None] ** 2, PICK - len(rc) / SR)

    for b in range(groove_bars):
        ch = PROG[b % 4]
        full = bed or b >= max(1, groove_bars // 2)
        last = (not bed) and b == groove_bars - 1
        sec = (b // 16) % 4
        for p, v in st['kick']:
            t = tp(b, p); drums.add(kick_crisp(vr(v, .03), soft=bed), t, 0.5 if bed else 0.72); kicks.append(t)
        if not bed or sec >= 1:
            for p, inst, v in st['back']:
                drums.add(inst(vr(v, .04)), tp(b, p), 0.5, 0.1)
        for p, v in enumerate(st['hats']):
            if v and (full or p % 2 == 0):
                drums.add(hat_crisp(vr(v, .05)), tp(b, p), 0.3, 0.4)
        if st.get('open_hat') and full and not last:
            for p in (2, 10):
                drums.add(hat_crisp(.4, True), tp(b, p), 0.22, 0.4)
        for p, v in st['ticks']:
            drums.add(tick(v), tp(b, p), 0.3, -0.5)
        if st['shake'] and full:
            for p in range(16):
                drums.add(shaker_crisp(vr(.4 if p % 2 else .25)), tp(b, p), 0.25, -0.45)
        if last:
            for p, v in [(13, .3), (14, .5), (15, .7)]:
                drums.add(clap(v), tp(b, p), 0.4, -0.1)
        hits = st['chord_hits'] if not last else st['chord_hits'][:2]
        for p, d, v in hits:
            chord(keys, st['keys'], ch, tp(b, p), d * s16, v)
        if st.get('arp') and (full or bed):
            notes = CHORDS[ch][0]; seq = notes + notes[::-1][1:-1]
            for p in range(16 if not last else 8):
                keys.add(pluck(seq[p % len(seq)] + 12, s16 * 0.9, vr(st['arp'], .04)), tp(b, p), 0.6, 0.6 * np.sin(p))
        for m in CHORDS[ch][0]:
            pad.add(pad_note(m + st['pad_up'], bar, 0.5), PICK + b * bar)
        root, fifth = CHORDS[ch][1], FIFTH[ch]
        for p, which, d, v in st['bass']:
            m = root if which == 'r' else fifth if which == 'f' else (35 if last else APPROACH[ch])
            if bed and which == 'a' and b % 4 != 3: continue
            bass.add(st['bassi'](m, d * s16, vr(v, .03)), tp(b, p))

    if bed:
        for b in range(0, groove_bars, 8):
            mel.add(glock(76, 1.0, 0.3), tp(b, 0) + 0.01, 1.0, 0.3)
    else:
        mlist = [] if groove_bars == 0 else MEL if groove_bars >= 8 else [n for n in MEL if n[0] < groove_bars - 1] + \
            [(groove_bars - 1,) + n[1:] for n in MEL if n[0] == 7]
        sig = [(-4, 81, 2 * s16, .85), (-2, 79, 2 * s16, .9), (0, 76, 2.4, 1.0)]
        for inst, shift, g in st['mel']:
            for bb, p, m, d, v in mlist:
                if bb < groove_bars:
                    mel.add(inst(m + shift, d * s16, vr(v, .04)) * g, tp(bb, p), 1.0, 0.15)
            for o, m, d, v in sig:
                mel.add(inst(m + shift, d, v) * g, tf + o * s16, 1.0, 0.15)
        # final hit
        drums.add(kick_crisp(1.0, boom=True), tf, 1.0); kicks.append(tf)
        fx.add(crash_crisp(0.8, 3.0), tf)
        fb = st['bassi'](36, 4.5, 1.0); fb *= np.exp(-np.arange(len(fb)) / SR / 1.1)
        bass.add(fb, tf)
        keyfin = ep_crisp if st['keys'] is pluck else st['keys']
        for k, m in enumerate(CHORDS['C69'][0]):
            keys.add(keyfin(m, 5.0, 0.75), tf + k * 0.02, 1.0, (k / 4 - 0.5) * 0.7)
        for m in CHORDS['C69'][0]:
            pad.add(pad_note(m + st['pad_up'], 2.0, 0.55), tf)

    # ---------- mix ----------
    hall = ir(st['rt'], 0.025, 11000); room = ir(0.5, 0.004, 12000)
    sc = sidechain(N, kicks, depth=0.12 if bed else 0.28)
    d = drums.x; d = d + 0.12 * reverb(d, room)
    k = hp(keys.x, 140) * sc
    k = k + st['keys_delay'] * pingpong(k, st['delay'] * s16, st['delay_fb'], 5, 9000)
    p = hp(lp(pad.x, 2400), 200) * sc
    bs = lp(bass.x, 2500) * sidechain(N, kicks, 0.3 if not bed else 0.15)
    v = hp(mel.x, 180)
    v = v + 0.3 * pingpong(v, st['delay'] * s16, st['delay_fb'], 6, 10000)
    stems = {'drums': d, 'keys': k * (0.42 if bed else 0.46), 'pad': p * (0.07 if bed else 0.03) * st['pad'], 'bass': bs * (0.4 if bed else 0.48),
             'mel': v * (0.2 if bed else 0.34), 'fx': fx.x * 0.3}
    send = stems['keys'] * 0.3 + stems['pad'] * 0.5 + stems['mel'] * 0.5 + stems['fx'] * 0.3 + stems['drums'] * 0.04
    mix = sum(stems.values()) + 0.5 * reverb(send, hall) + air(N, st['air'] * (0.6 if bed else 1))
    mix = shelf_hi(mix, 10000, 2.5)
    if bed:
        mix = peq(mix, 2600, -5.0, 0.7); mix = peq(mix, 1100, -2.0, 0.9)
        mix = hp(mix, 28, 2)
        Lx = int(L * SR); tl = mix[Lx:]; mix = mix[:Lx].copy(); mix[:len(tl)] += tl
    else:
        mix = peq(mix, 4500, 3.0, 0.7)
        fade = int(min(2.5, tail - 1.6) * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None] ** 2
    name = f'{sty}-{kind}'
    print(name, {kk: round(rms_db(vv), 1) for kk, vv in stems.items()})
    return master(mix, -18 if bed else -14, drive=1.3, name=name, prefiltered=bed)


if __name__ == '__main__':
    if sys.argv[3:4] == ['sting']:
        for st in sys.argv[4:]:
            n = list(STYLES).index(st) + 1
            sf.write(f'{OUT}/forslag{n}-{st}-sting.wav', render(st, 'intro', 0, tail=6.5), SR, subtype='PCM_24')
        sys.exit()
    styles = sys.argv[3:] or list(STYLES)
    for i, s in enumerate(styles, 1):
        n = list(STYLES).index(s) + 1
        sf.write(f'{OUT}/forslag{n}-{s}-intro.wav', render(s, 'intro', 8), SR, subtype='PCM_24')
        sf.write(f'{OUT}/forslag{n}-{s}-intro-15s.wav', render(s, 'intro', 4, tail=15 - 1080 / STYLES[s]['bpm']), SR, subtype='PCM_24')
        sf.write(f'{OUT}/forslag{n}-{s}-bakgrund-loop.wav', render(s, 'bed', 64), SR, subtype='PCM_24')
