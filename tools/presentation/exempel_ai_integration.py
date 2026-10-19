"""Exempel: erbjudandet AI + Integration i webbens formspråk (spår B).
Kör: python tools/presentation/exempel_ai_integration.py ut.pptx"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from magello_pptx import *  # noqa

# 1  Förstasida med signaturytan
cover("kontor-1", "Erbjudande", "AI + Integration", "Från AI-potential till verksamhetsnytta", "2026-08-19",
      nav=["Utgångsläget", "Lösningen", "Genomförande"], featured="Nästa steg")

# 2  Stor typografi ------------------------------------------------------
s = page()
text(s, L, 1350000, W, 300000, [("kicker", "Erbjudandet i korthet")])
text(s, L, 1700000, W, h_of("display", 2), [("display", "Vi gör AI-potential till verksamhetsnytta.")])
text(s, L, 4000000, 8000000, 1000000, [("sub", "Vi kombinerar AI-kompetens med integrations- och arkitekturkompetens.")])
text(s, L, 5200000, 7400000, 900000, [("lead", "Så hjälper vi svenska företag och organisationer att omsätta AI-potential till verklig verksamhetsnytta.")])

# 3  Vi hjälper kunden att ------------------------------------------------
s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Så skapar vi nytta")])
text(s, L, 1300000, W, h_of("h1", 1), [("h1", "Vi hjälper kunden att")])
rows = [("light", "Identifiera", "var AI kan skapa störst nytta"),
        ("nodes", "Förstå", "vilka data, system och processer som krävs"),
        ("cloud-arrow", "Integrera", "AI med verksamhetens befintliga IT-landskap"),
        ("timer", "Automatisera", "processer och omsätta resultat i handling"),
        ("rocket", "Skala", "AI med återanvändbara komponenter")]
c3 = (W - 2 * 450000) / 3
item_grid(s, rows, 2450000, 3, c3, 450000, 2150000)
poly_pic(s, P("kontor-21"), L + 2 * (c3 + 450000), 2450000 + 2150000, c3, 1850000, "image-c")
notes(s, "Skala AI-lösningar genom återanvändbara integrations- och AI-komponenter. Det är kombinationen som skapar verklig verksamhetsnytta.")

# 4  Citat på bakgrundsbild --------------------------------------------------
s = photo_page("kontor-24")
pw, ph_ = 8800000, 3500000
py = (SH - ph_) / 2 + 200000
plate(s, L, py, pw, ph_)
img(s, CITE, L, py + 550000, h=620000)
text(s, L + 1050000, py + 450000, pw - 1050000, 2000000,
     [("quote", "AI skapar potentialen. Integration gör det möjligt att realisera den.")])
text(s, L + 1050000, py + 2550000, pw - 1050000, 600000, [("sub", "Det är kombinationen som skapar verklig verksamhetsnytta.", dict(size=22))])

# 5  Avdelare --------------------------------------------------------------
divider("workshop_tavla_3", "Utgångsläget", "Varför AI behöver integration",
        "En bra AI-modell räcker sällan för att skapa verksamhetsnytta.")

# 6  Bild och text -------------------------------------------------------------
s = page()
text(s, L, 1350000, 5200000, 5100000, [
    ("kicker", "Utgångsläget"),
    ("h1", "En bra AI-modell räcker sällan", dict(before=14)),
    ("body", "Generativ AI, agenter och prediktiva modeller kan effektivisera processer. Men en pilot skapar ingen nytta på egen hand.", dict(before=22)),
    ("body", "AI behöver rätt information vid rätt tidpunkt, och resultatet måste kunna användas i befintliga processer.", dict(before=12, bold=True)),
])
poly_pic(s, P("kontor-8"), 6800000, 0, SW - 6800000, SH, [(8, 0), (100, 0), (100, 100), (0, 100)])
notes(s, "AI skapar snabbt nya möjligheter för svenska företag och organisationer. Generativ AI, intelligenta agenter, prediktiva modeller och automatiserade beslutsstöd kan effektivisera processer, förbättra kundupplevelser och skapa helt nya arbetssätt.\n"
         "Men för att AI ska skapa verklig verksamhetsnytta räcker det sällan med en bra AI-modell eller ett framgångsrikt pilotprojekt.\n"
         "AI behöver tillgång till rätt information, i rätt sammanhang, vid rätt tidpunkt, och resultaten från AI behöver kunna omsättas i verksamhetens befintliga processer och system.")

# 7  Två beroenden ---------------------------------------------------------------
s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Två beroenden")])
text(s, L, 1300000, W, h_of("h1", 1), [("h1", "AI och integration behöver varandra")])
c2 = (W - 900000) / 2
for i, (ic, h3, b) in enumerate([
        ("nodes", "AI behöver data", "Datan finns oftast redan, men den är spridd över affärssystem, CRM, ekonomisystem, dokument, databaser och API."),
        ("arrow-up-right", "Resultatet behöver en process", "En AI som hittar en kundmöjlighet skapar lite värde om resultatet stannar där. Nyttan uppstår när det förs tillbaka till CRM och påverkar nästa steg.")]):
    x = L + i * (c2 + 900000)
    icon(s, ic, x, 2700000, 700000)
    text(s, x, 3650000, c2, 2800000, [("h3", h3, dict(size=28)), ("body", b, dict(before=10, color="text2"))])

# 8  Påstående, stor typografi ------------------------------------------------------
s = page()
text(s, L, 1150000, W, 300000, [("kicker", "Därför")])
text(s, L, 1500000, W, h_of("display", 3), [("display", "AI-arkitektur och integrationsarkitektur behöver utvecklas tillsammans.", dict(size=66))])
c2 = (W - 600000) / 2
text(s, L, 4700000, c2, 1600000, [("body", "AI behöver integration för att få tillgång till verksamhetens information och kunna agera i dess processer.", dict(bold=True))])
text(s, L + c2 + 600000, 4700000, c2, 1600000, [("body", "Traditionella integrationer är byggda för förutsägbara flöden. AI kräver att data, modeller, agenter och beslut samverkar dynamiskt.", dict(color="text2"))])

# 9  Bild och text, bilden till vänster -----------------------------------------------
s = page()
poly_pic(s, P("kontor-19"), 0, 0, 5400000, SH, [(0, 0), (100, 0), (92, 100), (0, 100)])
text(s, 6150000, 1350000, R - 6150000, 5100000, [
    ("kicker", "Vårt erbjudande"),
    ("h1", "Integration är en avgörande förmåga", dict(before=14)),
    ("body", "Vi hjälper organisationer att gå från isolerade AI-initiativ till lösningar som är integrerade med data, system och processer.", dict(before=22)),
    ("body", "Vi bygger förmågan att använda AI där den gör störst skillnad.", dict(before=12, bold=True)),
])

# 10  Risker ------------------------------------------------------------------------------
s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Riskerna")])
text(s, L, 1300000, W, h_of("h1", 1), [("h1", "Vad händer om beroendet inte hanteras?")])
risk = [("nodes", "AI blir isolerat", "Fastnar i piloten och är svår att integrera."),
        ("cloud-arrow", "Data blir ett hinder", "AI saknar aktuell och fullständig information."),
        ("timer", "Manuella steg kvarstår", "Information kopieras fortfarande för hand."),
        ("arrow-up-right", "AI skapar inte handling", "Resultatet når aldrig verksamhetens processer."),
        ("markup", "Teknisk skuld byggs upp", "Punktlösningar och dubbla datakällor."),
        ("rocket", "Skalningen blir dyr", "Komplexiteten växer med varje nytt system.")]
item_grid(s, risk, 2450000, 3, c3, 450000, 2150000)
notes(s, "När AI-initiativ drivs separat från integrations- och arkitekturarbetet uppstår ofta samma typer av problem.")

# 11  Det som ska stå ut: rosagrå ---------------------------------------------------------
s = page()
poly(s, 0, 1200000, SW, 4700000, "section-rose", "rose100")
text(s, L, 1900000, W, 300000, [("kicker", "Resultatet")])
text(s, L, 2300000, W, h_of("display", 3), [("display", "Investerat i AI, men inte byggt förmågan att skala AI.", dict(size=66))])
notes(s, "Resultatet blir att organisationen har investerat i AI, men inte byggt förmågan att skala AI.")

# 12  Avdelare --------------------------------------------------------------------------------
divider("powerpoint-13", "Lösningen", "Vår lösning: AI + Integration",
        "Tre kompetensområden som tillsammans gör AI skalbart.")

# 13  Tre områden ----------------------------------------------------------------------------
areas = [("AI-förmågor", "AI-tillämpningar som skapar konkret verksamhetsnytta.", "kontor-6",
          "Vi hjälper organisationen att identifiera och utveckla AI-tillämpningar som skapar konkret verksamhetsnytta.",
          ["Generativ AI och AI-assistenter", "AI-agenter", "Intelligent automatisering", "Prediktiv analys",
           "Dokument- och informationshantering", "AI-baserat beslutsstöd", "RAG och kunskapslösningar",
           "AI-integration mot processer"], "dator-1"),
         ("Integrationsförmågor", "AI som kommunicerar med befintliga system och data.", "kontor-22",
          "Vi säkerställer att AI-lösningarna kan kommunicera med organisationens befintliga system och data.",
          ["API-management", "Systemintegration", "Event-driven architecture", "Integration as a Service",
           "Data- och informationsflöden", "Microservices", "Workflow och orchestration", "Molnintegration",
           "SaaS- och verksamhetssystem"], "powerpoint-9"),
         ("Arkitektur och governance", "Principer för kontrollerad skalning av AI och integration.", "whiteboard-3",
          "Vi skapar de gemensamma principer som krävs för att AI och integration ska kunna skalas på ett kontrollerat sätt.",
          ["AI- och integrationsarkitektur", "Data governance", "Informationssäkerhet", "Identitet och åtkomst",
           "API- och integrationsstandarder", "Observability och monitorering", "Governance för AI-agenter",
           "Återanvändbara komponenter"], "workshop_tavla_1")]
s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Kompetensområden")])
text(s, L, 1300000, W, h_of("h1", 1), [("h1", "Tre områden, en helhet")])
for i, (h3, short, photo, _, _, _) in enumerate(areas):
    x = L + i * (c3 + 450000)
    poly_pic(s, P(photo), x, 2450000, c3, 2200000, ["image-a", "image-c", "image-a"][i])
    text(s, x, 4900000, c3, 1600000, [("h3", h3, dict(size=26)), ("small", short, dict(before=6, color="text2"))])

# 14-16  Område: stor rubrik + helhöjdsbild ----------------------------------------------------
for h3, short, _, desc, ex, photo in areas:
    s = page()
    lw = 7500000
    text(s, L, 1000000, lw, 300000, [("kicker", "Kompetensområde")])
    text(s, L, 1350000, lw, h_of("title", 1), [("title", h3, dict(size=54))])
    text(s, L, 2450000, lw - 300000, 1000000, [("sub", desc, dict(size=22))])
    text(s, L, 3750000, lw, 300000, [("kicker", "Exempel")])
    plain_list(s, L, 4120000, lw, ex, cols=2, size=18, gap=350000)
    poly_pic(s, P(photo), 8800000, 0, SW - 8800000, SH, [(12, 0), (100, 0), (100, 100), (0, 100)])

# 17  Pilot -> verksamhet ------------------------------------------------------------------------
s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Från pilot till verksamhet")])
text(s, L, 1300000, W, h_of("display", 1), [("display", "Vi bygger inte AI för AI:s skull.", dict(size=64))])
text(s, L, 2500000, 8600000, 900000, [("sub", "Vi utgår från verksamhetens processer och identifierar var AI kan skapa mätbar nytta. Ett typiskt scenario:", dict(size=22))])
steps(s, L, 3750000, W, 1050000, ["Kunddata", "Integration", "AI-analys", "Beslut", "Verksamhets- system", "Automatiserad åtgärd"], size=17)
text(s, L, 5250000, 8600000, 900000, [("body", "Så blir AI en del av verksamhetens process i stället för ytterligare ett fristående verktyg.", dict(bold=True, size=22))])

# 18-19  Nytta ---------------------------------------------------------------------------------------
gain = [("timer", "Effektivare processer", "AI automatiserar analys, dokumenthantering, klassificering och sökning."),
        ("light", "Bättre beslutsstöd", "Information från flera system ger medarbetare bättre underlag."),
        ("thumbs-up", "Bättre kundupplevelse", "Mer relevanta svar, rekommendationer och automatiserade tjänster."),
        ("cloud-arrow", "Snabbare informationsflöden", "Data i realtid eller nära realtid via API och eventdrivna integrationer."),
        ("arrow-up-right", "Automatiserade arbetsflöden", "AI kan initiera eller genomföra nästa steg i processen."),
        ("rocket", "Skalbar AI-användning", "Nya AI-tillämpningar utan att varje lösning byggs från grunden."),
        ("nodes", "Lägre kostnad och komplexitet", "Återanvändbara integrationer och komponenter i stället för punktlösningar.")]
c2g = (W - 900000) / 2
for part in (gain[:4], gain[4:]):
    s = page()
    text(s, L, 1000000, W, 300000, [("kicker", "Effekter")])
    text(s, L, 1300000, W, h_of("h1", 1), [("h1", "Vilken nytta kan skapas?")])
    item_grid(s, part, 2300000, 2, c2g, 900000, 2250000, body_size=18)
    if len(part) == 3:
        poly_pic(s, P("kontor-16"), L + c2g + 900000, 2300000 + 2250000, c2g, 1950000, "image-c")

# 20  Avdelare -----------------------------------------------------------------------------------------
divider("powerpoint-10", "Genomförande", "Så genomför vi ett AI- och integrationsprojekt",
        "Sex steg från idé till skalbar lösning.")

# 21  Översikt -------------------------------------------------------------------------------------------
s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Genomförande")])
text(s, L, 1300000, W, h_of("h1", 1), [("h1", "Sex steg från idé till skalbar lösning")])
short = ["Assessment", "Mål- arkitektur", "Use case", "Bygg och integrera", "Test och validering", "Produktion och skalning"]
desc = ["Mål, processer och system", "AI och integration som en helhet", "Ett konkret fall med tydlig nytta",
        "AI och integration byggs parallellt", "Tekniskt och för verksamheten", "Skala till nya use cases"]
steps(s, L, 2750000, W, 1100000, short, nums=["Steg %d" % (i + 1) for i in range(6)], size=17)
cw6 = (W - 5 * 50000) / 6
for i, d in enumerate(desc):
    text(s, L + i * (cw6 + 50000) + 60000, 4100000, cw6 - 200000, 1600000, [("small", d, dict(size=18, color="text2"))])

# 22-27  Steg -------------------------------------------------------------------------------------------
STEPS = [
    (1, "AI & Integration Assessment", "Vi börjar med att förstå mål, processer, systemlandskap och AI-möjligheter.",
     "Vi kartlägger bland annat",
     ["Use cases med störst potential", "Data som AI behöver", "Var datan finns", "Berörda system",
      "Befintliga API och integrationer", "Informations- och säkerhetskrav", "Processer som ska påverkas", "Tekniska begränsningar"],
     "kontor-21", "light", "Resultat: en prioriterad roadmap över AI-initiativ och integrationsförmågor."),
    (2, "Design av målarkitektur", "Vi tar fram en målarkitektur där AI och integration är en sammanhängande helhet.",
     "Vi definierar bland annat",
     ["AI-komponenter", "Datakällor", "API", "Integrationsflöden", "Event och meddelanden", "Dataflöden",
      "Säkerhet och identitet", "Governance", "Monitorering", "Plattform och standarder"],
     "whiteboard-3", "nodes", "Mål: en arkitektur för första use caset och kommande AI-tillämpningar."),
    (4, "Bygg och integrera", "AI-lösningen utvecklas parallellt med integrationsförmågan.",
     "Vi etablerar exempelvis",
     ["API mot verksamhetssystem", "Dataflöden", "Eventflöden", "AI-tjänster", "RAG och kunskapslösningar",
      "AI-agenter", "Workflow och orchestration", "Säkerhet och åtkomst", "Logging och monitorering"],
     "dator-1", "cloud-arrow", "AI integreras i verksamhetsprocessen, inte bara i ett system."),
    (5, "Test och verksamhetsvalidering", "Lösningen testas både tekniskt och ur verksamhetsperspektiv.",
     "Vi verifierar bland annat",
     ["AI-resultatens kvalitet", "Datakvalitet", "Integrationernas robusthet", "Säkerhet", "Prestanda",
      "Felhantering", "Spårbarhet", "Användarupplevelse", "Verksamhetsnytta"],
     "kontor-19", None, None),
]


def step_page(n, name, intro, lead, items, photo, ic, outcome):
    s = page()
    lw = 7550000
    text(s, L, 1000000, lw, 300000, [("kicker", "Steg %d av 6" % n)])
    text(s, L, 1300000, lw, h_of("h1", 1), [("h1", name, dict(size=44))])
    text(s, L, 2200000, lw - 300000, 800000, [("sub", intro, dict(size=22))])
    text(s, L, 3300000, lw, 300000, [("kicker", lead)])
    plain_list(s, L, 3650000, lw, items, cols=2, size=18, gap=350000)
    if outcome:
        icon(s, ic, L, 6080000, 420000)
        text(s, L + 620000, 6030000, lw - 620000, 500000, [("body", outcome, dict(bold=True, size=20))], anchor=MSO_ANCHOR.MIDDLE)
    poly_pic(s, P(photo), 8800000, 0, SW - 8800000, SH, [(12, 0), (100, 0), (100, 100), (0, 100)])


for st in STEPS[:2]:
    step_page(*st)

s = page()
text(s, L, 1000000, W, 300000, [("kicker", "Steg 3 av 6")])
text(s, L, 1300000, W, h_of("h1", 1), [("h1", "Prioriterat AI-use case")])
text(s, L, 2250000, 8600000, 800000, [("sub", "Vi väljer ett konkret use case där nyttan är tydlig och definierar det tillsammans:", dict(size=22))])
steps(s, L, 3400000, W, 1000000, ["Problem", "AI-förmåga", "Data", "Integration", "Process", "Mätbar effekt"], size=18)
icon(s, "rocket", L, 4900000, 1100000)
text(s, L + 900000, 4950000, 8600000, 1000000, [("h3", "Så kan vi snabbt visa värdet och samtidigt bygga komponenterna för fortsatt utveckling.", dict(size=28))], anchor=MSO_ANCHOR.MIDDLE)

for st in STEPS[2:]:
    step_page(*st)

s = page()
text(s, L, 1350000, 5800000, 5000000, [
    ("kicker", "Steg 6 av 6"),
    ("title", "Produktionssättning och skalning", dict(before=12, size=48)),
    ("body", "När lösningen är validerad etableras den för produktion.", dict(before=24, size=22)),
    ("body", "Därefter kan organisationen återanvända integrations- och AI-komponenterna för nya use cases.", dict(before=10, size=22, bold=True)),
])
poly_pic(s, P("event-5"), 7000000, 0, SW - 7000000, SH, [(10, 0), (100, 0), (100, 100), (0, 100)])

# 28  Nästa steg: helbild + platta ----------------------------------------------------------------------
s = photo_page("kontor-20")
pw, ph_ = 7400000, 3900000
py = SH - ph_ - 650000
plate(s, L, py, pw, ph_)
text(s, L, py + 450000, pw, 300000, [("kicker", "Nästa steg")])
text(s, L, py + 800000, pw, h_of("title", 1), [("title", "Börja med en kartläggning", dict(size=54))])
text(s, L, py + 1650000, pw - 400000, 900000, [("lead", "Vi tar reda på var AI kan skapa störst nytta hos er och vilka integrationer som krävs.")])
xb = button(s, L, py + 2650000, "Prata med oss", True)
text(s, L, py + 3400000, pw, 300000, [("small", ["Magello   ", ("info@magello.se   ·   Västgötagatan 2, 118 27 Stockholm", dict(color="text2", font=BODY))], dict(size=13, color="magenta", font=HEAD, bold=True))])



save(sys.argv[1] if len(sys.argv) > 1 else "AI-och-Integration.pptx", title="AI + Integration")
