PAGE = dict(
    title="Språk och ton", kicker="Grunder",
    lead="Så låter Magello i text: personligt men professionellt. Sidan är en grund att bygga vidare på. "
         "Den börjar med orden vi använder och orden vi aldrig använder.",
    actions=[("Ord vi använder", "#ord", "primary"),
             ("Ord vi aldrig använder", "#aldrig", "secondary")],
)


def body(sg):
    tone = sg.block("ton", "Tonalitet", "Personligt men professionellt",
        "Vi skriver som en kunnig kollega pratar: rakt, varmt och utan omsvep. "
        "Läsaren ska känna att det finns människor bakom texten, och att de vet vad de gör.",
        sg.spec(["Personligt betyder", "Professionellt betyder"], [
            ["Vi skriver <em>vi</em> om Magello och tilltalar läsaren direkt", "Vi håller oss till fakta och säger det vi kan stå för"],
            ["Vardagliga ord före facktermer, när det går", "Rätt term när den behövs, förklarad första gången"],
            ["Namn på personer, kunder och team", "Konkreta resultat: vad vi gjorde och vad det gav"],
            ["En lättsam formulering får finnas", "Aldrig skämt på kundens eller någon annans bekostnad"],
        ]) +
        sg.sub("Våra värdeord i text",
               "Magellos värdeord är personliga, trygga, kommunikativa och lärande. Så märks de när vi skriver.") +
        sg.spec(["Värdeord", "Så låter det"], [
            ["Personliga", "Vi skriver till en människa, inte till en målgrupp. Gärna med namn och egna erfarenheter"],
            ["Trygga", "Vi lovar det vi kan hålla och visar hur. Siffror och exempel i stället för stora ord"],
            ["Kommunikativa", "Korta meningar, det viktigaste först och ett budskap per stycke"],
            ["Lärande", "Vi delar med oss av vad vi kan, och säger öppet vad vi har lärt oss"],
        ]))

    words = sg.block("ord", "Ord", "Ord vi använder",
        "Orden säger vem vi är. Använd dem konsekvent, så känns texterna igen oavsett vem som skrivit dem. Listan växer.",
        sg.spec(["Ord", "Använd så här", "Exempel"], [
            ["<strong>Tech-partner</strong>",
             "Så beskriver vi vår roll hos kunden: en partner som tar ansvar för tekniken tillsammans med kunden, inte bara levererar timmar",
             "<em>Magello är tech-partner till några av Sveriges mest kända varumärken.</em>"],
            ["<strong>Lång</strong>",
             "I stället för <em>gedigen</em>. Enkelt och sant, och går att belägga",
             "<em>Vi har lång erfarenhet av integration.</em> <em>En lång relation med kunden.</em>"],
        ]) +
        sg.use(do=["Skriv <em>tech-partner</em> med bindestreck. Stor bokstav bara först i en mening eller rubrik",
                   "Visa vad partnerskapet betyder: vad vi tar ansvar för och hur länge"],
               dont=["Byta mot <em>leverantör</em>, <em>resurs</em> eller <em>techpartner</em> utan bindestreck"]))

    never = sg.block("aldrig", "Ord vi aldrig använder", "Ord och uttryck vi undviker",
        "Vissa ord säger mindre än de låter. De gör texten tyngre och mindre trovärdig.",
        sg.spec(["Använd inte", "Varför", "Skriv i stället"], [
            ["<strong>gedigen</strong>", "Tomt och slitet. Säger inget om vad vi faktiskt kan",
             "Skriv <em>lång</em>: <em>lång erfarenhet</em>, <em>lång relation med kunden</em>. Lägg gärna till fakta, som <em>över 30 år</em>"],
            ["<strong>Överdrivet säljande text</strong>", "Läsaren slutar lyssna. Det låter som reklam, inte som en partner",
             "Säg vad vi gör och vad det ger, och låt resultatet tala"],
        ]) +
        sg.sub("Så känner du igen säljande text", "Superlativ, löften utan bevis och uppmaningar. Några exempel och hur de kan skrivas om.") +
        sg.spec(["Säljande", "Rakt"], [
            ["Vi förverkligar era digitala drömmar", "Vi bygger och förvaltar webb, appar och integrationer"],
            ["Lösningar i världsklass som överträffar alla förväntningar", "Säg vad som blev bättre och med hur mycket: snabbare, enklare, billigare"],
            ["Marknadens ledande experter", "Säg vad konsulterna har gjort och hur länge"],
            ["Tveka inte att kontakta oss", "Hör av dig till oss på info@magello.se"],
            ["Unik, innovativ, banbrytande", "Beskriv vad som är nytt och för vem"],
        ]) +
        sg.use(dont=["Superlativ och förstärkningsord: <em>bästa</em>, <em>ledande</em>, <em>unik</em>, <em>otrolig</em>",
                     "Utropstecken",
                     "Löften utan exempel eller siffror"],
               note=["Tveka? Läs meningen högt. Skulle du säga den till en kund över en kopp kaffe, då håller den"]),
        rose=True)

    write = sg.block("skriva", "Så skriver vi", "Regler för alla texter",
        "Gäller webb, presentationer, dokument, CV, LinkedIn och e-post.",
        sg.spec(["Regel", "Så gör du"], [
            ["Svenska", "Engelska facktermer bara när det inte finns ett vedertaget svenskt ord"],
            ["Det viktigaste först", "Första meningen ska gå att läsa ensam"],
            ["Korta meningar", "En tanke per mening. Dela långa meningar"],
            ["Aktiv form", "<em>Vi byggde appen</em>, inte <em>appen byggdes</em>"],
            ["Konkret", "Siffror, namn och exempel i stället för adjektiv"],
            ["Rubriker som säger något", "Rubriken beskriver vad något är eller gör, inte hur bra det är"],
            ["Inga utropstecken", "Tonen bärs av innehållet, inte av skiljetecken"],
        ]) +
        sg.sub("Före och efter") +
        sg.spec(["Före", "Efter"], [
            ["Magello är en gedigen och ledande leverantör som erbjuder innovativa helhetslösningar i världsklass!",
             "Magello är tech-partner till organisationer som vill bygga och förvalta digitala tjänster. Vi har lång erfarenhet av det, över 30 år."],
        ]))

    ai = sg.ai_start("ai", "Låt en AI-agent skriva eller granska texten. Agenten följer orden och tonen på den här sidan.",
        "Skriv eller granska en text enligt Magellos språk och ton. Texten handlar om: ",
        label="Med AI", title="Skriv med en AI-agent",
        example="en LinkedIn-post om att vi har fått en ny kund inom energi")

    return tone + words + never + write + ai
