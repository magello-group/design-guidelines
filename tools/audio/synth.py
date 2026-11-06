"""Magello sonic identity: lofi jazz/tech intro, sting and speech bed.
Pure numpy/scipy synthesis. 100 BPM, swung 16ths, key C major / D dorian.
Signature motif: A - G - E (the musical letters in mAGEllo), landing E on the downbeat.
"""
import numpy as np, soundfile as sf, pyloudnorm as pyln, sys, os
from scipy import signal
from scipy.ndimage import minimum_filter1d, uniform_filter1d

SR = 48000
BPM = 100
BEAT = 60 / BPM
S16 = BEAT / 4
BAR = BEAT * 4
SWING = S16 * 0.17

def mtof(m): return 440.0 * 2 ** ((m - 69) / 12)
def T(n): return np.arange(int(n * SR)) / SR

# ---------- filters ----------
def _sos(kind, fc, order=2):
    return signal.butter(order, fc, kind, fs=SR, output='sos')
def lp(x, fc, o=2): return signal.sosfilt(_sos('low', fc, o), x, axis=0)
def hp(x, fc, o=2): return signal.sosfilt(_sos('high', fc, o), x, axis=0)
def bp(x, lo, hi, o=2): return signal.sosfilt(_sos('band', [lo, hi], o), x, axis=0)
def peq(x, f0, g_db, Q=0.8):
    A = 10 ** (g_db / 40); w = 2 * np.pi * f0 / SR; al = np.sin(w) / (2 * Q)
    b = [1 + al * A, -2 * np.cos(w), 1 - al * A]; a = [1 + al / A, -2 * np.cos(w), 1 - al / A]
    return signal.lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)
def shelf_hi(x, f0, g_db):
    A = 10 ** (g_db / 40); w = 2 * np.pi * f0 / SR; al = np.sin(w) / 2 * np.sqrt(2)
    c = np.cos(w); sA = 2 * np.sqrt(A) * al
    b = [A * ((A + 1) + (A - 1) * c + sA), -2 * A * ((A - 1) + (A + 1) * c), A * ((A + 1) + (A - 1) * c - sA)]
    a = [(A + 1) - (A - 1) * c + sA, 2 * ((A - 1) - (A + 1) * c), (A + 1) - (A - 1) * c - sA]
    return signal.lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)

# ---------- buses ----------
class Bus:
    def __init__(self, n): self.x = np.zeros((n, 2))
    def add(self, sig, t, gain=1.0, pan=0.0):
        i = int(round(t * SR))
        if sig.ndim == 1:
            th = (pan + 1) * np.pi / 4
            sig = np.stack([sig * np.cos(th), sig * np.sin(th)], 1) * np.sqrt(2)
        if i < 0: sig = sig[-i:]; i = 0
        j = min(len(self.x), i + len(sig))
        if j > i: self.x[i:j] += sig[:j - i] * gain

# ---------- instruments ----------
rng = np.random.default_rng(1977)

def kick(vel=1.0, soft=False, boom=False):
    dur = 1.6 if boom else 0.55
    t = T(dur)
    f = 46 + (95 if not soft else 60) * np.exp(-t / 0.032)
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = np.sin(ph) * np.exp(-t / (0.9 if boom else (0.22 if soft else 0.3)))
    if not soft:
        click = lp(rng.standard_normal(len(t)) * np.exp(-t / 0.002), 3500)
        y += 0.35 * click
    y = np.tanh(1.8 * y) / np.tanh(1.8)
    return y * vel

def snare(vel=1.0):
    t = T(0.4)
    body = 0.7 * np.sin(2 * np.pi * (175 + 40 * np.exp(-t / 0.01)) * t) * np.exp(-t / 0.07)
    body += 0.3 * np.sin(2 * np.pi * 330 * t) * np.exp(-t / 0.04)
    n = bp(rng.standard_normal(len(t)), 1400, 7500) * np.exp(-t / 0.12)
    y = lp(body + 0.9 * n, 7000)
    return np.tanh(1.5 * y) * vel

def rim(vel=1.0):
    t = T(0.12)
    y = 0.6 * np.sin(2 * np.pi * 1650 * t) * np.exp(-t / 0.012)
    y += bp(rng.standard_normal(len(t)), 2000, 6000) * np.exp(-t / 0.008)
    return lp(y, 6500) * vel

_METAL = np.array([205.3, 304.4, 369.6, 522.7, 540.0, 800.0]) * 1.9
def hat(vel=1.0, open_=False):
    d = 0.42 if open_ else 0.06
    t = T(d + 0.05)
    m = sum(signal.square(2 * np.pi * f * t + rng.random() * 6) for f in _METAL)
    y = 0.4 * m + rng.standard_normal(len(t))
    y = bp(y, 6500, 13000, 2) * np.exp(-t / (0.16 if open_ else 0.022))
    return lp(y, 10000) * vel

def shaker(vel=1.0):
    t = T(0.1)
    env = (1 - np.exp(-t / 0.008)) * np.exp(-t / 0.03)
    return bp(rng.standard_normal(len(t)), 5000, 11000) * env * vel

def crash(vel=1.0, dur=2.2):
    t = T(dur)
    m = sum(signal.square(2 * np.pi * f * 1.37 * t + rng.random() * 6) for f in _METAL)
    y = hp(0.3 * m + rng.standard_normal(len(t)), 4500) * np.exp(-t / 0.7)
    y = lp(y, 11000)
    return np.stack([y, np.roll(y, 37)], 1) * vel

def rhodes_note(m, dur, vel):
    f = mtof(m); rel = 0.3
    t = T(dur + rel)
    I = (0.5 + 1.5 * vel) * np.exp(-t / 0.16) + 0.3
    y = np.sin(2 * np.pi * f * t + I * np.sin(2 * np.pi * f * t))
    y += vel * 0.22 * np.sin(2 * np.pi * f * 7.02 * t) * np.exp(-t / 0.025)
    dec = 2.2 * (262 / f) ** 0.6
    env = (1 - np.exp(-t / 0.0015)) * np.exp(-t / dec)
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.07)
    dr = 1 + 1.3 * vel
    return np.tanh(y * dr) / np.tanh(dr) * env * vel

def vibe_note(m, dur, vel):
    f = mtof(m)
    t = T(dur + 2.8)
    y = np.zeros(len(t))
    for r, a, d in [(1, 1.0, 1.7), (3.93, 0.28, 0.32), (9.6, 0.09, 0.07)]:
        y += a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / d)
    y += 0.12 * bp(rng.standard_normal(len(t)), 2000, 7000) * np.exp(-t / 0.002)
    off = t > dur + 0.4; y[off] *= np.exp(-(t[off] - dur - 0.4) / 0.35)
    return y * (1 - np.exp(-t / 0.001)) * vel

def bass_note(m, dur, vel):
    f = mtof(m)
    t = T(dur + 0.08)
    ph = 2 * np.pi * f * t
    y = np.sin(ph) + 0.28 * np.sin(2 * ph) + 0.09 * np.sin(3 * ph)
    y += 0.18 * np.sin(4 * ph) * np.exp(-t / 0.012)
    env = (1 - np.exp(-t / 0.004)) * (0.55 + 0.45 * np.exp(-t / 0.14))
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.03)
    return np.tanh(1.6 * y) * env * vel

def pad_note(m, dur, vel):
    f = mtof(m); rel = 1.0
    t = T(dur + rel)
    y = np.zeros(len(t))
    for det in (-0.004, 0.004):
        ff = f * (1 + det); ph0 = rng.random() * 6
        for k in range(1, int(2500 / ff) + 1):
            y += np.sin(2 * np.pi * k * ff * t + ph0 * k) / k
    env = np.minimum(1, t / 0.7)
    off = t > dur; env[off] *= np.exp(-(t[off] - dur) / 0.4)
    return y * env * vel

# ---------- effects ----------
def ir(rt=2.0, pre=0.018, lpf=5500, width=1.0):
    t = T(rt * 1.3)
    n = rng.standard_normal((len(t), 2)) * np.exp(-6.9 * t / rt)[:, None]
    n = lp(n, lpf); n = hp(n, 250)
    n[:, 1] = width * n[:, 1] + (1 - width) * n[:, 0]
    n = np.vstack([np.zeros((int(pre * SR), 2)), n])
    return n / np.sqrt((n ** 2).sum() / 2)

def reverb(x, h):
    out = np.stack([signal.oaconvolve(x[:, c], h[:, c])[:len(x)] for c in range(2)], 1)
    return out

def pingpong(x, time, fb=0.38, n=6, lpf=3500):
    out = np.zeros_like(x); cur = x.copy()
    for k in range(1, n + 1):
        cur = lp(cur, lpf) * fb
        d = int(time * k * SR)
        sh = np.zeros_like(x); sh[d:] = cur[:len(x) - d]
        if k % 2: sh = sh[:, ::-1]
        out += sh
    return out

def wow(x, depth=0.0011, rate=0.5, fl=0.00007, flr=6.1, loop_len=None):
    n = len(x); t = np.arange(n) / SR
    if loop_len:
        rate = max(1, round(rate * loop_len)) / loop_len
        flr = round(flr * loop_len) / loop_len
    d = (depth * (1 + np.sin(2 * np.pi * rate * t)) + fl * (1 + np.sin(2 * np.pi * flr * t))) * SR
    pos = np.arange(n) - d
    return np.stack([np.interp(pos, np.arange(n), x[:, c]) for c in range(2)], 1)

def tremolo(x, rate, depth, stereo=True, phase=0.0):
    t = np.arange(len(x)) / SR
    l = 1 + depth * np.sin(2 * np.pi * rate * t + phase)
    r = 1 + depth * np.sin(2 * np.pi * rate * t + phase + (np.pi if stereo else 0))
    return x * np.stack([l, r], 1) / (1 + depth)

def sidechain(n, kick_times, depth=0.35, rel=0.13):
    g = np.ones(n); t = np.arange(n) / SR
    for kt in kick_times:
        i = int(kt * SR); j = min(n, i + int(rel * 6 * SR))
        if i >= n: continue
        tt = t[i:j] - kt
        g[i:j] = np.minimum(g[i:j], 1 - depth * np.exp(-tt / rel) * np.minimum(1, tt / 0.004 + 0.3))
    return g[:, None]

def crackle(n, density=3.0, level=0.03, hiss=0.0025):
    out = np.zeros((n, 2))
    k = int(n / SR * density)
    pos = rng.integers(0, n - 200, k)
    amp = np.minimum(rng.pareto(2.5, k) * 0.3, 1.0) * level
    for p, a, c in zip(pos, amp, rng.integers(0, 2, k)):
        L = rng.integers(8, 60)
        out[p:p + L, c] += a * rng.standard_normal(L) * np.hanning(L)
        out[p:p + L, 1 - c] += 0.4 * a * rng.standard_normal(L) * np.hanning(L)
    out = bp(out, 900, 9000)
    h = bp(rng.standard_normal((n, 2)), 1500, 9000) * hiss
    return out + h

def tape_spinup(x, dur):
    """x is a sound starting at 0; return `dur` seconds that accelerate from standstill."""
    t = np.arange(int(dur * SR)) / SR
    p = dur / 2.4 * (t / dur) ** 2.4
    src = np.arange(len(x)) / SR
    y = np.stack([np.interp(p, src, x[:, c]) for c in range(2)], 1)
    return y * np.minimum(1, t / 0.35)[:, None]

def limiter(x, ceil_db=-1.3, win=0.012):
    c = 10 ** (ceil_db / 20)
    pk = np.max(np.abs(x), 1)
    g = np.minimum(1, c / np.maximum(pk, 1e-9))
    L = int(win * SR)
    g = minimum_filter1d(g, 2 * L)
    g = uniform_filter1d(g, L)
    return x * g[:, None]

def master(x, target_lufs, drive=1.0, name='', prefiltered=False):
    x = x if prefiltered else hp(x, 28, 2)
    meter = pyln.Meter(SR)
    x = x * 10 ** ((-20 - meter.integrated_loudness(x)) / 20)
    x = np.tanh(x * drive) / drive if drive > 1 else x
    for _ in range(3):
        l = meter.integrated_loudness(x)
        x = x * 10 ** ((target_lufs - l) / 20)
        x = limiter(x)
    l = meter.integrated_loudness(x)
    tp = 20 * np.log10(np.max(np.abs(signal.resample_poly(x, 4, 1, axis=0))))
    print(f"[{name}] LUFS {l:.1f}  truePeak {tp:.1f} dBTP  len {len(x)/SR:.1f}s")
    return x

def rms_db(x): return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)

# ---------- harmony ----------
CHORDS = {  # rootless Rhodes voicings, bass root (MIDI)
    'Dm9':   ([53, 57, 60, 64], 38),
    'G13':   ([53, 59, 64, 69], 31),
    'Cmaj9': ([52, 55, 59, 62], 36),
    'A7b13': ([55, 61, 65, 71], 33),
    'C69':   ([52, 55, 57, 62, 64], 36),
}
CHORDS_HI = {  # alternate voicings for bed variation
    'Dm9':   ([57, 60, 64, 65], 38),
    'G13':   ([59, 64, 65, 69], 31),
    'Cmaj9': ([55, 59, 62, 64], 36),
    'A7b13': ([61, 65, 67, 71], 33),
}
PROG = ['Dm9', 'G13', 'Cmaj9', 'A7b13']
FIFTH = {'Dm9': 45, 'G13': 38, 'Cmaj9': 43, 'A7b13': 40}
APPROACH = {'Dm9': 30, 'G13': 35, 'Cmaj9': 34, 'A7b13': 37}  # leads to next root

def hum(s=0.005): return rng.normal(0, s)
def vr(v, s=0.08): return float(np.clip(v + rng.normal(0, s), 0.05, 1.0))
