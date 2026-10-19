PAGE = dict(
    title="Formulär &amp; feedback", h1="Formulär<br>&amp; feedback", kicker="Byggstenar",
    lead="Fält, val, uppladdning och feedback följer samma formspråk som resten. Kanten runt ett fält är det enda stället där en hel ram är tillåten.",
)


def body(sg):
    fields = sg.block("falt", "Formulär", "Textfält och val",
        "Fältet har en tydlig grå kant runt hela fältet så att det syns att man kan skriva där. Kanten byter färg efter tillstånd. Inga rundade hörn.",
        sg.demo('<div class="sg-two"><div>'
                '<div class="mg-field"><label class="mg-field__label" for="f1">Standard</label><input class="mg-input" id="f1" type="text" placeholder="Skriv här…"><span class="mg-field-msg mg-field-msg--hint">Hjälptext om fältet behöver förklaras</span></div>'
                '<div class="mg-field"><label class="mg-field__label" for="f2">Fel <span class="mg-field__hint">— röd kant</span></label><input class="mg-input is-error" id="f2" type="email" value="anna@ogiltigt"><span class="mg-field-msg mg-field-msg--error">Ange en giltig e-postadress</span></div>'
                '<div class="mg-field"><label class="mg-field__label" for="f3">Giltigt <span class="mg-field__hint">— grön kant</span></label><input class="mg-input is-success" id="f3" type="text" value="linkedin.com/in/anna-k"><span class="mg-field-msg mg-field-msg--success">Giltig LinkedIn-profil</span></div>'
                '<div class="mg-field"><label class="mg-field__label" for="f4">Inaktivt</label><input class="mg-input" id="f4" type="text" value="Inte redigerbart" disabled></div></div>'
                '<div><div class="mg-field"><label class="mg-field__label" for="f5">Textarea</label><textarea class="mg-textarea" id="f5" placeholder="Beskriv ditt projekt…"></textarea><span class="mg-field-msg mg-field-msg--hint">Max 500 tecken</span></div>'
                '<div class="mg-field"><label class="mg-field__label" for="f6">Lista</label><div class="mg-select-wrap"><select class="mg-select" id="f6"><option>Välj alternativ…</option><option>Magello svart</option><option>Magello vit</option></select></div></div></div></div>', "white") +
        sg.code('''<div class="mg-field">
  <label class="mg-field__label" for="email">E-post</label>
  <input class="mg-input is-error" id="email" type="email">
  <span class="mg-field-msg mg-field-msg--error">Ange en giltig e-postadress</span>
</div>''') +
        sg.spec(["State", "Kant", "Klass"],
                [["Vila", "Grå, hel ram", "<code>.mg-input</code>"], ["Fokus", "Blå (accent som funktion)", "automatiskt"], ["Fel", "Röd + röd meddelandetext", "<code>.is-error</code>"], ["Giltigt", "Grön + grön meddelandetext", "<code>.is-success</code>"], ["Inaktivt", "Dämpad, ej klickbar", "<code>disabled</code>"]]) +
        sg.use(do=["En etikett per fält, ovanför fältet, Condensed fet versaler", "Felmeddelandet säger vad användaren ska göra: ”Ange en giltig e-postadress”", "Validera vid blur (när användaren lämnar fältet)", "Textarea får bara växa i höjdled"],
               dont=["Platshållartext i stället för etikett", "Rundade hörn eller skuggor på fält", "Felmeddelande bara i färg utan text", "Alla fält röda samtidigt"],
               note=["Fältets kantfärg som state är ett av få tillåtna undantag från ”accent är aldrig kant”, eftersom den är funktionell"]))

    checks = sg.block("val", "Formulär", "Checkbox, radio och uppladdning",
        "Checkbox för flerval, radio för enval. De fylls med magenta vid val. Uppladdningszonen är en polygon med streckad kant som signalerar ”lägg något här”.",
        sg.demo('<div class="sg-two"><div><span class="sg-demo-label">Checkbox — flerval</span><div class="mg-check-group">'
                '<label class="mg-check-label"><input type="checkbox" checked> Svart bakgrund</label>'
                '<label class="mg-check-label"><input type="checkbox"> Lägg till logotyp</label>'
                '<label class="mg-check-label"><input type="checkbox" disabled> Ej tillgängligt</label></div></div>'
                '<div><span class="sg-demo-label">Radio — enval</span><div class="mg-check-group">'
                '<label class="mg-check-label"><input type="radio" name="fmt" checked> Kvadrat 1:1</label>'
                '<label class="mg-check-label"><input type="radio" name="fmt"> Cirkel</label>'
                '<label class="mg-check-label"><input type="radio" name="fmt"> Rektangel 4:3</label></div></div></div>', "white") +
        sg.demo('<div class="sg-two"><label class="mg-upload-zone" for="up"><div class="mg-upload-zone__text">Dra och släpp din bild här</div><div class="mg-upload-zone__sub">JPG, PNG eller WEBP — max 5 MB</div><input type="file" id="up" accept="image/*" style="display:none"></label>'
                '<div class="mg-upload-zone is-drag-over" aria-hidden="true"><div class="mg-upload-zone__text">Släpp bilden här</div><div class="mg-upload-zone__sub">Drag-over: magenta kant</div></div></div>', "white") +
        sg.use(do=["Checkbox när flera val är möjliga, radio när exakt ett ska väljas", "Berätta tillåtna filtyper och max storlek i uppladdningszonen"],
               dont=["Radio för flerval", "Uppladdning utan besked om format och storlek"]), rose=True)

    states = sg.block("status", "Feedback", "Status, notiser och inline-feedback",
        "Fyra tillstånd, alltid i accentfärg som <em>fyllnad</em>. Pills för status i listor, toast för tillfälliga besked, inline-feedback intill det den gäller.",
        sg.sub("Pills") +
        sg.demo('<div class="sg-row"><span class="mg-pill mg-pill--error">Fel</span><span class="mg-pill mg-pill--success">Klar</span><span class="mg-pill mg-pill--loading">Bearbetar</span><span class="mg-pill mg-pill--disabled">Ej tillgänglig</span><span class="mg-pill mg-pill--warning">Varning</span><span class="mg-pill mg-pill--magenta">Nytt</span></div>') +
        sg.sub("Toast", "Visas 3–5 sekunder i nedre högra hörnet. Beskriv vad som hände och vad användaren ska göra.") +
        sg.demo('<div class="sg-two"><div>'
                '<div class="mg-toast mg-toast--success"><div class="mg-toast__body"><div class="mg-toast__title">Bild skapad</div><div class="mg-toast__msg">Din profilbild är klar att ladda ner.</div></div><button class="mg-toast__close" aria-label="Stäng">×</button></div>'
                '<div class="mg-toast mg-toast--error"><div class="mg-toast__body"><div class="mg-toast__title">Bilden kunde inte skapas</div><div class="mg-toast__msg">Formatet stöds inte. Använd JPG, PNG eller WEBP.</div></div><button class="mg-toast__close" aria-label="Stäng">×</button></div></div>'
                '<div><div class="mg-toast mg-toast--info"><div class="mg-toast__body"><div class="mg-toast__title">Ansikte hittat</div><div class="mg-toast__msg">Vi centrerade bilden kring ansiktet.</div></div><button class="mg-toast__close" aria-label="Stäng">×</button></div>'
                '<div class="mg-toast mg-toast--warning"><div class="mg-toast__body"><div class="mg-toast__title">Låg bildkvalitet</div><div class="mg-toast__msg">Bilden är under 400 × 400 px.</div></div><button class="mg-toast__close" aria-label="Stäng">×</button></div></div></div>', "white") +
        sg.sub("Inline-feedback", "Fylld ruta med polygonform, direkt intill det den gäller. Aldrig en ram eller en kantlinje.") +
        sg.demo('<div class="mg-inline-error"><strong>Filen är för stor.</strong> Max 5 MB, din fil är 8,2 MB.</div><div class="mg-inline-info">Bilden beskärs automatiskt till 1:1.</div><div class="mg-inline-success">Bilden är sparad och klar att använda.</div>', "white") +
        sg.spec(["Tillstånd", "Färg", "Pill-text"],
                [["Fel", "Röd <code>#E3012F</code>", "Fel"], ["Klart", "Grön <code>#1BA660</code>", "Klar"], ["Bearbetar / info", "Blå <code>#31ABE2</code>", "Bearbetar"], ["Varning", "Gul <code>#FFDC00</code> (svart text)", "Varning"], ["Inaktivt", "Grå", "Ej tillgänglig"]]) +
        sg.use(do=["Beskriv vad som hände: ”Bilden kunde inte skapas”", "Lägg till vad användaren ska göra: ”Använd JPG, PNG eller WEBP”", "Inga utropstecken, ingen ”successfully”"],
               dont=["”Error 500”", "Accentfärgad kant till vänster om ett meddelande", "Toast som ligger kvar för alltid"]))

    loading = sg.block("laddar", "Feedback", "Laddning",
        "Spinner för kort, obestämd väntan (under 3 sekunder), progressbar när antalet steg är känt, skeleton vid sidladdning.",
        sg.demo('<div class="mg-spinner-row"><div class="mg-spinner-item"><div class="mg-spinner mg-spinner--lg"></div><span class="mg-spinner-item__label">Stor</span></div>'
                '<div class="mg-spinner-item"><div class="mg-spinner mg-spinner--md"></div><span class="mg-spinner-item__label">Medium</span></div>'
                '<div class="mg-spinner-item"><div class="mg-spinner mg-spinner--sm"></div><span class="mg-spinner-item__label">Liten</span></div>'
                '<div class="mg-spinner-item"><div class="mg-spinner mg-spinner--md mg-spinner--blue"></div><span class="mg-spinner-item__label">Blå (system)</span></div></div>', "white") +
        sg.demo('<div class="sg-two"><div><div class="mg-progress" style="margin-bottom:6px"><div class="mg-progress__fill" style="width:65%"></div></div><div class="mg-progress__label">Steg 2 av 3 — genererar bild…</div></div>'
                '<div><div class="mg-skeleton-card"><div class="mg-skeleton mg-skeleton-img"></div><div class="mg-skeleton mg-skeleton-line" style="width:72%;margin-bottom:var(--mg-space-2)"></div><div class="mg-skeleton mg-skeleton-line" style="width:48%"></div></div></div></div>', "white") +
        sg.use(do=["Spinner under 3 sekunder, progressbar eller overlay med text över 3 sekunder", "Visa ett skeleton som liknar innehållet som kommer"],
               dont=["Spinner utan text vid långa operationer", "Blockera hela sidan för en kort laddning"],
               note=["Spinner, radioknappar och skeleton-shimmer är runda eller har gradient av funktionella skäl. Det är de enda undantagen"]), rose=True)

    buttons = sg.block("knappfarg", "Knappar i formulär", "Knappens färg följer handlingen",
        "I formulär och verktyg väljs knappens färg efter vad den gör, inte efter var den sitter.",
        sg.spec(["Handling", "Variant", "Färg"],
                [["Skapa, generera, spara, ladda ner, skicka", "<code>.mg-btn--primary</code>", "Magenta, vit text"], ["Återställ, avbryt, stäng, rensa", "<code>.mg-btn--secondary</code>", "Rose-200, svart text"]]) +
        sg.use(do=["Sekundärknappen till höger om primärknappen", "Ikon till vänster om texten med 8 px mellanrum (<code>.mg-btn--icon</code>)"],
               dont=["Mer än en primärknapp per vy", "Röd knapp för ”Avbryt”"]))
    return fields + checks + states + loading + buttons
