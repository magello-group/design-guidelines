PAGE = dict(
    title="E-postsignatur", kicker="Mallar",
    lead="Alla på Magello har samma e-postsignatur. Kopiera signaturen nedan, klistra in den i Outlook och byt till dina egna uppgifter.",
)

# Logotypen måste ligga på en publik adress för att synas hos mottagaren.
# PNG, eftersom Outlook inte visar SVG. Filen är 4× för skarpa skärmar.
LOGO = "https://magello-group.github.io/design-guidelines/assets/logos/magello-email.png"

# Signaturen är en tabell med inline-stilar. E-postprogram ignorerar CSS-filer,
# klasser och webbtypsnitt, så allt står direkt på elementen.
SIG = f"""<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;font-family:Roboto,Arial,sans-serif;font-size:14px;line-height:1.5;color:#000000;">
  <tr>
    <td style="padding:0 0 16px 0;">
      <strong>Förnamn Efternamn</strong>, Senior Consultant<br>
      <a href="https://www.linkedin.com/in/your-username/" style="color:#000000;text-decoration:none;">https://www.linkedin.com/in/your-username/</a><br>
      <a href="tel:+46768123465" style="color:#000000;text-decoration:none;">+46 768 123 465</a>
    </td>
  </tr>
  <tr>
    <td style="padding:0 0 16px 0;">
      <a href="https://magello.se"><img src="{LOGO}" width="85" height="22" alt="Magello" style="display:block;border:0;width:85px;height:22px;"></a>
    </td>
  </tr>
  <tr>
    <td style="font-size:13px;line-height:1.5;color:#4C4A4A;">
      <span style="color:#EC008C;">Magello</span><br>
      Västgötagatan 2<br>
      118 27 Stockholm<br>
      Sweden<br>
      <br>
      <a href="tel:+4686331300" style="color:#4C4A4A;text-decoration:none;">+46 8 633 13 00</a><br>
      <a href="mailto:info@magello.se" style="color:#4C4A4A;text-decoration:none;">info@magello.se</a><br>
      <a href="https://magello.se" style="color:#4C4A4A;text-decoration:none;">magello.se</a><br>
      <br>
      Org no: 556531-7129<br>
      VAT: SE556531712901
    </td>
  </tr>
</table>"""

TEXT = """Förnamn Efternamn, Senior Consultant
https://www.linkedin.com/in/your-username/
+46 768 123 465

Magello
Västgötagatan 2
118 27 Stockholm
Sweden

+46 8 633 13 00
info@magello.se
magello.se

Org no: 556531-7129
VAT: SE556531712901"""

WHERE = [
    ["Nya Outlook och Outlook på webben", "Inställningar → Konto → Signaturer"],
    ["Klassiska Outlook (Windows)", "Arkiv → Alternativ → E-post → Signaturer"],
    ["Outlook för Mac", "Outlook → Inställningar → Signaturer"],
    ["Outlook i mobilen", "Inställningar → ditt konto → Signatur. Använd versionen utan HTML"],
]

FIELDS = [
    ["Namn och titel", "Ditt namn i fetstil, titeln efter ett kommatecken. Titeln på engelska, som på LinkedIn"],
    ["LinkedIn", "Byt <code>your-username</code> mot ditt användarnamn, både i texten och i länken"],
    ["Mobilnummer", "Byt både den synliga texten och länken (<code>tel:+46…</code>, utan mellanslag)"],
    ["Logotyp och adress", "Ändra inte. Uppgifterna är desamma för alla"],
]


def body(sg):
    sig = sg.block("signatur", "Outlook", "Signaturen",
        "Markera hela signaturen i rutan, från namnet till momsnumret, och kopiera (Cmd/Ctrl + C). Formatering, logotyp och länkar följer med.",
        sg.demo(SIG, "white") +
        sg.sub("Så lägger du in den") +
        '<ol class="sg-text"><li>Kopiera signaturen ovan.</li>'
        '<li>Öppna signaturinställningarna i Outlook (se tabellen) och skapa en ny signatur.</li>'
        '<li>Klistra in och byt namn, titel, LinkedIn och mobilnummer till dina egna.</li>'
        '<li>Välj signaturen som standard för nya meddelanden och svar, för varje inkorg du har.</li></ol>' +
        sg.spec(["Program", "Hitta signaturerna"], WHERE), rose=True)

    fields = sg.block("falt", "Fyll i", "Det här byter du",
        "Allt annat i signaturen är gemensamt och ska se likadant ut för alla.",
        sg.spec(["Fält", "Gör så här"], FIELDS) +
        sg.use(do=["Byt telefonlänken, inte bara den synliga texten",
                   "Testa genom att skicka ett mejl till dig själv och klicka på länkarna",
                   "Använd versionen utan HTML i mobilen och i program som inte visar bilder"],
               dont=["Lägga till citat, bilder, banners eller egna färger",
                     "Byta typsnitt eller storlek",
                     "Klistra in logotypen som en bifogad bild. Den ska hämtas från länken"],
               note=["Signaturen är en kolumn, så den fungerar också på smala skärmar",
                     "Logotypen hämtas från styleguidens webbplats. Mottagare som blockerar bilder ser texten ”Magello”"]))

    text = sg.block("utan-html", "Utan HTML", "Signatur i ren text",
        "För mobilen, för program som bara skickar ren text och för den som vill ha en enkel signatur.",
        sg.code(TEXT), rose=True)

    it = sg.block("html", "För IT", "Signaturens HTML",
        "Används när signaturen läggs ut centralt, till exempel med en signaturtjänst i Microsoft 365. Tabell med inline-stilar, eftersom e-postprogram inte läser CSS-filer. Färgerna är magenta <code>#EC008C</code> och textgrå <code>#4C4A4A</code> från tokens.",
        sg.code(SIG))

    return sig + fields + text + it
