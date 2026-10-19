PAGE = dict(
    title="Specialtypsnittet Kattux", kicker="Grunder",
    lead="Kattux är Magellos handritade typsnitt. Det används vid speciella tillfällen, främst i PowerPoint, som ett enstaka blickfång. Allt annat sätts i Roboto Condensed och Roboto.",
    actions=[("Ladda ned typsnittet", "../assets/fonts/KattuxAbc-Regular.otf", "primary")],
)

F = "../assets/fonts/"


def body(sg):
    specimen = sg.block("prov", "Prov", "Så ser Kattux ut",
        "Typsnittet heter <strong>Kattux Abc 20</strong> i Word och PowerPoint. Det finns i en vikt (Regular), har ingen kursiv eller fet och har bara versaler: gemener ritas som versaler.",
        sg.demo(
            '<p class="sg-kattux" style="font-size:clamp(2.5rem,1.5rem + 4vw,4.5rem);margin:0">Tänka fritt är stort, men tänka rätt är större</p>', "white") +
        sg.sub("Alfabet, siffror och tecken") +
        sg.demo(
            '<p class="sg-kattux sg-kattux--alphabet" style="margin:0">ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ<br>abcdefghijklmnopqrstuvwxyzåäö<br>0123456789<br>! ? . , : ; – ( ) &amp; @ % # ” ’ „ / £ §</p>') +
        sg.sub("I rubrikstorlek") +
        sg.spec(["Storlek", "Prov"],
                [["66 pt (PowerPoint, Innehåll - Platta)", '<span class="sg-kattux" style="font-size:3rem">Kombinera med grafik</span>'],
                 ["44 pt (PowerPoint, rubrik)", '<span class="sg-kattux" style="font-size:2.25rem">Tumme upp för framtiden</span>'],
                 ["28 pt (minsta storlek)", '<span class="sg-kattux" style="font-size:1.5rem">Välkommen till Magello</span>']]) +
        sg.text("Tecken som finns: A–Z, a–z, Å Ä Ö å ä ö, Á É á é, siffror, vanliga skiljetecken, ” ’ „ ‚ “ ‘, – (kort tankstreck), £, § och ©. "
                "Tecken som <strong>saknas</strong>: Ü ü, ß, €, — (långt tankstreck), ø, æ och de flesta andra accenter. Saknade tecken visas i ett annat typsnitt, så skriv om texten eller välj Roboto Condensed."))

    use = sg.block("anvandning", "Användning", "När Kattux får användas",
        "Kattux är ett undantag från regeln om två typsnitt (beslut D-45). Det är en accent, inte en del av typsnittsparet.",
        sg.spec(["Får användas", "Används inte"],
                [["Ett kort budskap eller citat i PowerPoint, i layouterna <em>Fokus - Rubrik på platta</em> och <em>Innehåll - Platta</em>", "Brödtext, listor, tabeller eller bildtexter"],
                 ["Rubrik eller blickfång på affisch, inbjudan, LinkedIn-bild eller annat material för ett särskilt tillfälle", "Webbplatsens rubriker, navigation, knappar eller formulär"],
                 ["Ett enstaka ord eller en kort fras per bild eller sida", "Som ersättning för Roboto Condensed i rubriker överlag"]]) +
        sg.use(do=["Använd Kattux för ett kort budskap, högst en mening",
                   "Sätt det stort: minst 28 pt, gärna 44–66 pt",
                   "Ge det luft och låt det stå ensamt på en platta eller ett foto",
                   "Låt resten av bilden eller sidan vara Roboto Condensed och Roboto"],
               dont=["Brödtext eller långa rubriker i Kattux",
                     "Kattux tillsammans med andra typsnitt än Roboto Condensed och Roboto",
                     "Mer än ett Kattux-element per bild",
                     "Fetstil eller kursiv. Typsnittet har bara en vikt, och Office fejkar fet och kursiv",
                     "Text med tecken som saknas (ü, ß, €, —)"],
               note=["Typsnittet har bara versaler. Skriv texten som vanligt, med stor bokstav där den ska vara",
                     "Utgår du från Magellos mall följer typsnittet med i filen",
                     "Den som saknar typsnittet kan visa presentationen men inte skriva ny text i Kattux. Skicka en PDF om du är osäker",
                     "Använd typsnittet bara i Magellos eget material"]), rose=True)

    install = sg.block("installera", "Installera", "Installera typsnittet",
        "Behövs bara om du ska skriva ny text i Kattux. Mallarna har redan typsnittet med sig.",
        '<div class="mg-btn-row"><a class="mg-btn mg-btn--secondary" href="' + F + 'KattuxAbc-Regular.otf" download>Ladda ned typsnittet</a></div>' +
        '<div class="sg-two"><div>' +
        sg.sub("Mac") +
        '<ol class="sg-text"><li>Ladda ned typsnittet.</li>'
        '<li>Dubbelklicka på filen.</li>'
        '<li>Klicka <em>Installera</em>.</li>'
        '<li>Starta om PowerPoint.</li></ol>' +
        '</div><div>' +
        sg.sub("PC") +
        '<ol class="sg-text"><li>Ladda ned typsnittet.</li>'
        '<li>Dubbelklicka på filen.</li>'
        '<li>Klicka <em>Installera</em>.</li>'
        '<li>Starta om PowerPoint.</li></ol>' +
        '</div></div>' +
        sg.text("Ska någon som inte har typsnittet ändra i din presentation? Spara den som PDF, eller be dem installera typsnittet."))

    return specimen + install + use
