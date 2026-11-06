import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
AUDIO = ROOT / "assets" / "audio"
URL = "../assets/audio/"

PAGE = dict(
    title="Ljud", kicker="Grunder",
    lead="Magellos ljud till video: ett intro, en ljudlogotyp och bakgrundsmusik till intervjuer. "
         "Allt har samma tempo, ackord och motiv, så delarna går att klippa ihop.",
    actions=[("Ladda ned introt", URL + "magello-intro.m4a", "primary"),
             ("Bakgrundsmusik", "#bakgrund", "secondary")],
)

PLAY = '<svg class="mg-audio__icon-play" viewBox="0 0 20 20" aria-hidden="true"><polygon points="5,2 18,10 5,18"/></svg>'
PAUSE = ('<svg class="mg-audio__icon-pause" viewBox="0 0 20 20" aria-hidden="true">'
         '<polygon points="4,2 8,2 8,18 4,18"/><polygon points="12,2 16,2 16,18 12,18"/></svg>')


def size(path):
    mb = path.stat().st_size / 1e6
    return f"{mb:.1f} MB".replace(".", ",") if mb >= 1 else f"{mb * 1000:.0f} kB"


def player(file, title, length, loop=False, preload="metadata"):
    path = AUDIO / file
    return (f'<div class="sg-track">'
            f'<div class="mg-audio" data-mg-audio>'
            f'<button type="button" class="mg-audio__play" aria-pressed="false" aria-label="Spela {title.lower()}">{PLAY}{PAUSE}</button>'
            f'<div class="mg-audio__body"><div class="mg-audio__head"><span class="mg-audio__title">{title}</span>'
            f'<span class="mg-audio__time">{length}</span></div>'
            f'<div class="mg-audio__seek" role="slider" tabindex="0" aria-label="Spola i {title.lower()}" '
            f'aria-valuemin="0" aria-valuemax="0" aria-valuenow="0">'
            f'<div class="mg-progress"><div class="mg-progress__fill"></div></div></div></div>'
            f'<audio src="{URL}{file}" preload="{preload}"{" loop" if loop else ""}></audio></div>'
            f'<a class="sg-photo__dl" href="{URL}{file}" download>Ladda ned · {file} · {size(path)}</a></div>')


def body(sg):
    intro = sg.block("intro", "Intro", "Intro och ljudlogotyp",
        "Introt börjar med ett svep och en trumvirvel, går över i ett groove på 110 BPM och slutar med motivet A–G–E på ett utklingande ackord. "
        "Ljudlogotypen är bara svepet och slutet.",
        '<div class="sg-tracks">' +
        player("magello-intro.m4a", "Intro", "0:25") +
        player("magello-intro-15s.m4a", "Intro, kort", "0:15") +
        player("magello-ljudlogotyp.m4a", "Ljudlogotyp", "0:07") +
        '</div>' +
        sg.use(do=["Lägg introt eller ljudlogotypen först i videon, under logotyp eller titel",
                   "Använd ljudlogotypen i korta klipp, Shorts och logotypanimationer",
                   "Klipp på hela takter (2,18 s) om du kortar själv"],
               dont=["Lägga tal ovanpå introt. Det är gjort för att höras ensamt",
                     "Ändra tempo, tonhöjd eller lägga till effekter",
                     "Använda musiken i material som inte är Magellos"]))

    bed = sg.block("bakgrund", "Bakgrund", "Bakgrundsmusik under tal",
        "Samma ackord och ljud som introt, men glesare och utan melodi. Frekvenserna där rösten ligger är sänkta, så att tal hörs tydligt.",
        '<div class="sg-tracks">' +
        player("magello-bakgrund.m4a", "Bakgrund, loop", "2:19", loop=True) +
        player("magello-bakgrund-45min.m4a", "Bakgrund, 45 minuter", "45:00", preload="none") +
        '</div>' +
        sg.use(do=["Sänk bakgrunden 8–12 dB under tal",
                   "Tona över från introts sista ackord till bakgrunden. De hör ihop musikaliskt",
                   "Använd loopen och upprepa den om du behöver annan längd. Skarven hörs inte"],
               dont=["Lägga bakgrunden på full nivå under tal",
                     "Blanda med annan musik i samma video"],
               note=["Loopen är 2:20 och börjar om på ett taktslag, 45-minutersversionen tonar ut de sista 8 sekunderna",
                     "45-minutersversionen är 44 MB. Ladda ned den bara när du behöver den"]),
        rose=True)

    use = sg.block("anvanda", "I en video", "Så sätter du ljudet i en video",
        "Ordningen nedan passar intervjuer och presentationer på YouTube och LinkedIn.",
        sg.demo(sg.steps("Introt under titeln", "Tona över till bakgrunden", "Sänk under tal", "Avsluta med ljudlogotypen")) +
        sg.spec(["Del", "Fil", "Nivå"],
                [["Inledning", "<code>magello-intro.m4a</code> eller <code>magello-intro-15s.m4a</code>", "Full nivå (−14 LUFS)"],
                 ["Övergång", "Tona över under introts sista ackord, cirka 3 sekunder", "—"],
                 ["Tal", "<code>magello-bakgrund.m4a</code> eller 45-minutersversionen", "8–12 dB under talet"],
                 ["Slut", "<code>magello-ljudlogotyp.m4a</code>", "Full nivå"]]))

    motif = sg.block("motiv", "Ljudidentitet", "Ljudlogotypen A–G–E",
        "Motivet är de tre bokstäverna i Magello som också är toner: A, G och E. Det spelas på glockenspiel och landar alltid på slutackordet.",
        sg.spec(["Egenskap", "Värde"],
                [["Tempo", "110 BPM, en takt är 2,18 s, raka sextondelar"],
                 ["Ackord", "Dm9 – G13 – Cmaj9 – A7b13, slutackord C6/9"],
                 ["Motiv", "A – G – E, sista tonen på slutackordets första slag"],
                 ["Instrument", "Knäppande syntar, elpiano, glockenspiel, djup bas, handklapp och hi-hat"],
                 ["Ljudnivå", "Intro och ljudlogotyp −14 LUFS, bakgrund −18 LUFS, högst −1 dBTP"],
                 ["Format", "AAC (M4A), 48 kHz stereo, 256 kbit/s (45 minuter: 128 kbit/s)"]]) +
        sg.sub("Från formspråk till ljud") +
        sg.spec(["Formspråket", "Ljudet"],
                [["Roboto Condensed: täta, exakta former", "Raka sextondelar, korta knäppande toner och tydliga trumslag"],
                 ["Spärrade etiketter och luftig brödtext", "Tystnad mellan tonerna och klar diskant, med ekon och rumsklang som fyller ut"],
                 ["Magenta används sparsamt och med avsikt", "Motivet A–G–E är ljudets magenta och bär slutet"],
                 ["Rosagrått är kärnan", "En mjuk bas och ackordmatta under allt"]]) +
        sg.text("Musiken är syntetiserad från grunden för Magello, utan samplingar eller sång. "
                "Källkoden finns i <code>tools/audio/</code>, så att nya versioner kan göras med samma ljud."),
        rose=True)

    return intro + bed + use + motif
