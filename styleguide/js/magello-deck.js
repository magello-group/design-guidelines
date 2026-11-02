/* ==========================================================================
   Magello webbpresentationer — bildmotor (magello-deck.js)
   Ren statisk HTML: öppna index.html direkt från disk, ingen server behövs.
     index.html            presentation (tangenter, helskärm, översikt)
     index.html?presenter  talarvy, öppnas med P och synkas via postMessage
   Första bilden har webbens signaturheader. När man går vidare roterar den
   bort som på webbens undersidor och bara ikonlogotypen ligger kvar.
   Se README.md för tangenter och markup.
   ========================================================================== */
(function () {
  'use strict';

  var $  = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  var W = 1920, H = 1080;
  var base = document.currentScript.src.replace(/[^/]*$/, '') + '../../assets/';   // där logos/ ligger
  var root = document.documentElement;
  var mode = /[?&]presenter\b/.test(location.search) ? 'presenter' : 'deck';
  root.classList.add('mode-' + mode);

  var deckEl = $('.deck');
  var slides = $$('.slide', deckEl);
  var steps  = slides.map(function (slide) { return $$('.step', slide); });
  var state  = { i: 0, step: 0 };
  var peer   = null;   // talarvyns fönster, eller presentationen sedd från talarvyn

  /* ── Signaturheader och ikonlogotyp ──────────────────────────────────
     Samma markup används på två sätt: som ett lager ovanpå bilderna som
     animeras (presentationsläget) och som statisk kopia i varje bild
     (översikt, utskrift och talarvy). */
  var tagline = deckEl.getAttribute('data-header') || '';
  var chromeHTML =
    '<div class="chrome__header">' +
      '<div class="chrome__shape"></div>' +
      '<div class="chrome__nav">' +
        '<img class="chrome__logo" src="' + base + 'logos/magello-magenta.svg" alt="Magello">' +
        (tagline ? '<span class="chrome__tagline">' + tagline + '</span>' : '') +
      '</div>' +
    '</div>' +
    '<img class="chrome__icon" src="' + base + 'logos/icon-logotype.svg" alt="Magello">';

  var frames = slides.map(function (slide, n) {
    var frame = document.createElement('div');
    frame.className = 'frame';
    slide.parentNode.insertBefore(frame, slide);
    frame.appendChild(slide);
    if (!slide.hasAttribute('data-no-chrome')) {
      var copy = document.createElement('div');
      copy.className = 'slide__chrome chrome' + (n === 0 ? ' is-cover' : '');
      copy.setAttribute('aria-hidden', 'true');
      copy.innerHTML = chromeHTML;
      slide.appendChild(copy);
    }
    frame.addEventListener('animationend', function (e) {
      if (e.target === frame) frame.classList.remove('is-leaving', 'is-entering');
    });
    frame.addEventListener('click', function () {
      if (!root.classList.contains('is-overview')) return;
      toggleOverview(false);
      go(n, 0);
    });
    return frame;
  });

  var layer = document.createElement('div');
  layer.className = 'deck__chrome';
  layer.innerHTML = '<div class="chrome">' + chromeHTML + '</div>';
  deckEl.appendChild(layer);
  var chrome = $('.chrome', layer);

  /* Skala så att 1920×1080 får plats, och låt sedan ytan växa i den andra
     riktningen så att bilden fyller hela fönstret utan svarta kanter. */
  function fit() {
    var w = deckEl.clientWidth || window.innerWidth;
    var h = deckEl.clientHeight || window.innerHeight;
    var f = Math.min(w / W, h / H);
    root.style.setProperty('--fit', f);
    deckEl.style.setProperty('--deck-w', (w / f) + 'px');
    deckEl.style.setProperty('--deck-h', (h / f) + 'px');
  }

  /* ── Navigation ──────────────────────────────────────────────────────
     step = antal visade .step-element på bilden. -1 betyder alla
     (används när man backar in på en bild). */
  function go(i, step, opts) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    var max = steps[i].length;
    step = step < 0 ? max : Math.min(step, max);
    var from = state.i;
    state = { i: i, step: step };

    if (mode === 'deck' && i !== from && !root.classList.contains('is-loading')) slideTo(from, i);
    frames.forEach(function (frame, n) { frame.classList.toggle('is-current', n === i); });
    steps[i].forEach(function (el, n) { el.classList.toggle('is-shown', n < step); });
    chrome.classList.toggle('is-cover', i === 0);
    chrome.classList.toggle('is-hidden', slides[i].hasAttribute('data-no-chrome'));

    if (mode === 'deck') history.replaceState(null, '', '#' + (i + 1));
    if (i !== 0) hideHelp();
    if (mode === 'presenter') renderPresenter();
    if (!(opts && opts.silent)) send({ deck: state });
  }

  // Gamla bilden glider ut och nya in. Klasserna tas bort när animationen är klar.
  function clearTransition() {
    frames.forEach(function (frame) { frame.classList.remove('is-leaving', 'is-entering'); });
  }

  function slideTo(from, to) {
    clearTransition();
    root.classList.toggle('is-back', to < from);
    frames[from].classList.add('is-leaving');
    frames[to].classList.add('is-entering');
  }

  function send(msg) {
    if (peer && !peer.closed) peer.postMessage(msg, '*');
  }

  function atEnd()   { return state.i === slides.length - 1 && state.step === steps[state.i].length; }
  function atStart() { return state.i === 0 && state.step === 0; }

  function next() {
    if (atEnd()) return;
    if (state.step < steps[state.i].length) go(state.i, state.step + 1);
    else go(state.i + 1, 0);
  }

  function prev() {
    if (atStart()) return;
    if (state.step > 0) go(state.i, state.step - 1);
    else go(state.i - 1, -1);
  }

  function fromHash() {
    var n = parseInt(location.hash.slice(1), 10);
    return isNaN(n) ? 0 : n - 1;
  }

  function toggleOverview(on) {
    on = typeof on === 'boolean' ? on : !root.classList.contains('is-overview');
    root.classList.toggle('is-overview', on);
    clearTransition();
    fit();
    if (on) frames[state.i].scrollIntoView({ block: 'center' });
  }

  function toggleFullscreen() {
    if (document.fullscreenElement) document.exitFullscreen();
    else root.requestFullscreen();
  }

  function openPresenter() {
    var url = location.href.split('#')[0].split('?')[0] + '?presenter#' + (state.i + 1);
    peer = window.open(url, 'deck-presenter', 'width=1400,height=820');
  }

  /* ── Talarvy ─────────────────────────────────────────────────────────
     Som PowerPoints föredragshållarvy: aktuell bild, nästa bild,
     anteckningar, tidtagning och klocka. Bara presentatören ser den.
     Bilderna ritas som kopior i samma dokument, så att talarvyn fungerar
     från disk utan iframes. */
  var ui = null;
  var elapsed = 0;               // ms före senaste start
  var runningSince = null;       // null när tidtagningen är pausad eller inte startad
  var timerStarted = false;      // tidtagningen startar när man går till bild 2
  var notesSize = 24;
  // Nedräkning: valfri. Slås på i talarvyn och startar när man går till bild 2.
  // Standardlängd i minuter: data-duration på <main class="deck">, annars 30.
  var cd = { on: false, minutes: parseInt(deckEl.getAttribute('data-duration'), 10) || 30, start: null };

  function pad(n) { return (n < 10 ? '0' : '') + n; }

  // Ikoner i knapparna: ifyllda former i magenta (Material Symbols, Apache 2.0). Stopp-ikonen är en polygon utan raka kanter.
  var ICON = (function () {
    function svg(d) { return '<svg class="presenter__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="' + d + '"/></svg>'; }
    return {
      play:   svg('M8 5v14l11-7z'),
      stop:   svg('M6 6.4L18 6l-.3 12-11.5-.3z'),
      replay: svg('M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z'),
      reset:  svg('M12 5V2L8 6l4 4V7c3.31 0 6 2.69 6 6 0 2.97-2.17 5.43-5 5.91v2.02c3.95-.49 7-3.85 7-7.93 0-4.42-3.58-8-8-8zm-6 8c0-1.65.67-3.15 1.76-4.24L6.34 7.34C4.9 8.79 4 10.79 4 13c0 4.08 3.05 7.44 7 7.93v-2.02c-2.83-.48-5-2.94-5-5.91z')
    };
  })();

  function buildPresenter() {
    document.title = 'Talarvy – ' + document.title;
    try { notesSize = parseInt(localStorage.getItem('deck-notes-size'), 10) || notesSize; } catch (e) {}
    ui = document.createElement('div');
    ui.className = 'presenter';
    ui.innerHTML =
      '<div class="presenter__main">' +
        '<div class="presenter__view presenter__view--current"></div>' +
        '<div class="presenter__controls">' +
          '<button type="button" data-act="prev">← Föregående</button>' +
          '<span class="presenter__pos"></span>' +
          '<button type="button" data-act="next">Nästa →</button>' +
        '</div>' +
        '<div class="presenter__notes-box">' +
          '<div class="presenter__notes-head">' +
            '<span class="presenter__label">Anteckningar</span>' +
            '<button type="button" data-act="smaller" title="Mindre text">A−</button>' +
            '<button type="button" data-act="bigger" title="Större text">A+</button>' +
          '</div>' +
          '<div class="presenter__notes"></div>' +
        '</div>' +
      '</div>' +
      '<div class="presenter__side">' +
        '<div class="presenter__next">' +
          '<span class="presenter__label presenter__next-label">Nästa bild</span>' +
          '<div class="presenter__view presenter__view--next" title="Gå till nästa"></div>' +
          '<p class="presenter__end">Sista bilden</p>' +
        '</div>' +
        '<div class="presenter__countdown">' +
          '<span class="presenter__label">Nedräkning</span>' +
          '<div class="presenter__cd-row">' +
            '<span class="presenter__cd-time" aria-live="off"></span>' +
            '<label class="presenter__cd-set"><input type="number" class="presenter__cd-min" min="1" max="240" step="1" aria-label="Längd i minuter"> min</label>' +
            '<button type="button" data-act="countdown">' + ICON.play + '<span>Aktivera</span></button>' +
            '<button type="button" data-act="cdrestart" hidden>' + ICON.replay + '<span>Starta om</span></button>' +
          '</div>' +
          '<div class="presenter__cd-bar" aria-hidden="true"><span></span></div>' +
        '</div>' +
        '<div class="presenter__bar">' +
          '<span class="presenter__label">Tid sedan start</span>' +
          '<div class="presenter__bar-row">' +
            '<span class="presenter__timer" title="Räknas från bild 2">00:00</span>' +
            '<button type="button" data-act="reset">' + ICON.reset + '<span>Nollställ</span></button>' +
          '</div>' +
        '</div>' +
      '</div>';
    document.body.appendChild(ui);

    var actions = {
      prev: prev,
      next: next,
      reset: function () { elapsed = 0; if (runningSince) runningSince = Date.now(); tick(); },
      countdown: function () {
        cd.on = !cd.on;
        cd.start = cd.on && state.i >= 1 ? Date.now() : null;
        tick();
      },
      cdrestart: function () { cd.start = state.i >= 1 ? Date.now() : null; tick(); },
      smaller: function () { setNotesSize(notesSize - 4); },
      bigger: function () { setNotesSize(notesSize + 4); }
    };
    ui.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-act]');
      if (btn) { actions[btn.getAttribute('data-act')](); btn.blur(); return; }
      if (e.target.closest('.presenter__view--next')) next();
    });
    var cdInput = $('.presenter__cd-min', ui);
    cdInput.value = cd.minutes;
    cdInput.addEventListener('change', function () {
      cd.minutes = Math.max(1, Math.min(240, parseInt(cdInput.value, 10) || cd.minutes));
      cdInput.value = cd.minutes;
      tick();
    });
    cdInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') cdInput.blur(); });
    window.addEventListener('resize', renderPresenter);
    setNotesSize(notesSize);
    tick();
    setInterval(tick, 1000);

    peer = window.opener;
    send({ hello: true });
  }

  function setNotesSize(px) {
    notesSize = Math.max(16, Math.min(48, px));
    $('.presenter__notes', ui).style.fontSize = notesSize + 'px';
    try { localStorage.setItem('deck-notes-size', notesSize); } catch (e) {}
  }

  function tick() {
    var s = Math.floor((elapsed + (runningSince ? Date.now() - runningSince : 0)) / 1000);
    $('.presenter__timer', ui).textContent = pad(Math.floor(s / 60)) + ':' + pad(s % 60);
    tickCountdown();
  }

  function tickCountdown() {
    var box = $('.presenter__countdown', ui);
    var out = $('.presenter__cd-time', ui);
    var fill = $('.presenter__cd-bar span', ui);
    $('[data-act="countdown"]', ui).innerHTML = cd.on ? ICON.stop + '<span>Stäng av</span>' : ICON.play + '<span>Aktivera</span>';
    $('[data-act="cdrestart"]', ui).hidden = !cd.on;
    box.classList.toggle('is-off', !cd.on);
    ui.classList.toggle('has-countdown', cd.on);
    out.className = 'presenter__cd-time';
    fill.className = '';
    if (!cd.on) { out.textContent = pad(cd.minutes % 1000) + ':00'; fill.style.width = '0'; return; }
    if (!cd.start) { out.textContent = 'Startar på bild 2'; out.classList.add('is-waiting'); fill.style.width = '0'; return; }
    var total = cd.minutes * 60;
    var left = total - Math.floor((Date.now() - cd.start) / 1000);
    var a = Math.abs(left);
    var done = Math.min(1, (total - left) / total);
    out.textContent = (left < 0 ? '−' : '') + pad(Math.floor(a / 60)) + ':' + pad(a % 60);
    // Siffrorna och stapeln har samma färg i steg (inga övertoningar):
    // grön upp till 75 %, orange upp till 90 %, sedan röd. Stapeln blinkar bara vid övertid.
    var phase = done < .75 ? 'is-green' : done < .9 ? 'is-orange' : 'is-red';
    out.classList.add(phase);
    if (left < 0) out.classList.add('is-over');
    fill.style.width = (done * 100) + '%';
    fill.className = phase;
    if (left < 0) fill.classList.add('is-pulse');
  }

  function renderSlide(view, i, step) {
    var copy = slides[i].cloneNode(true);
    $$('.step', copy).forEach(function (el, n) { el.classList.toggle('is-shown', n < step); });
    view.innerHTML = '';
    view.appendChild(copy);
    view.style.setProperty('--s', view.clientWidth / W);
  }

  function renderPresenter() {
    if (!ui) return;
    if (!timerStarted && state.i >= 1) { timerStarted = true; runningSince = Date.now(); tick(); }
    if (cd.on && !cd.start && state.i >= 1) { cd.start = Date.now(); tickCountdown(); }
    var hasMore = state.step < steps[state.i].length;
    var upcoming = hasMore ? [state.i, state.step + 1] : [state.i + 1, 0];
    var isLast = upcoming[0] >= slides.length;

    renderSlide($('.presenter__view--current', ui), state.i, state.step);
    if (!isLast) renderSlide($('.presenter__view--next', ui), upcoming[0], upcoming[1]);
    ui.classList.toggle('is-last', isLast);
    $('.presenter__next-label', ui).textContent = hasMore ? 'Nästa steg' : 'Nästa bild';
    $('[data-act="prev"]', ui).disabled = atStart();
    $('[data-act="next"]', ui).disabled = atEnd();

    var notes = $('.notes', slides[state.i]);
    $('.presenter__notes', ui).innerHTML = notes ? notes.innerHTML : '<p class="presenter__empty">Inga anteckningar.</p>';
    $('.presenter__pos', ui).textContent = (state.i + 1) + ' av ' + slides.length;
  }

  /* ── Tangenthjälp ─────────────────────────────────────────────────────
     Visas på startbilden de första 5 sekunderna, och försvinner direkt
     när man trycker på en tangent eller går vidare. Bara i presentationsläget, aldrig i talarvyn. */
  var help = null;

  function showHelp() {
    help = document.createElement('div');
    help.className = 'deck-help';
    help.setAttribute('role', 'note');
    help.innerHTML =
      '<span class="deck-help__title">Tangenter</span>' +
      '<dl>' +
        '<dt><kbd>→</kbd> <kbd>Mellanslag</kbd></dt><dd>Nästa</dd>' +
        '<dt><kbd>←</kbd></dt><dd>Föregående</dd>' +
        '<dt><kbd>P</kbd></dt><dd>Talarvy med anteckningar och tid</dd>' +
        '<dt><kbd>H</kbd></dt><dd>Helskärm</dd>' +
        '<dt><kbd>Ö</kbd></dt><dd>Översikt över alla bilder</dd>' +
      '</dl>';
    document.body.appendChild(help);
    setTimeout(hideHelp, 5000);
    document.addEventListener('keydown', hideHelp, { once: true });
  }

  function hideHelp() {
    if (!help) return;
    var el = help;
    help = null;
    el.classList.add('is-hidden');
    setTimeout(function () { el.remove(); }, 600);
  }

  /* ── Tangenter, meddelanden, svep och muspekare ───────────────────── */
  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName) || e.target.isContentEditable) return;
    var overview = root.classList.contains('is-overview');
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case 'Enter':
        next(); break;
      case ' ':
        if (e.shiftKey) prev(); else next(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace':
        prev(); break;
      case 'Home': go(0, 0); break;
      case 'End':  go(slides.length - 1, -1); break;
      case 'h': case 'H': toggleFullscreen(); break;
      case 'ö': case 'Ö': if (mode === 'deck') toggleOverview(); break;
      case 'Escape': if (!overview) return; toggleOverview(false); break;
      case 'p': case 'P': if (mode === 'deck') openPresenter(); break;
      default: return;
    }
    e.preventDefault();
  });

  // Presentationen svarar på talarvyns hälsning, så att synken överlever omladdning
  window.addEventListener('message', function (e) {
    var d = e.data || {};
    if (d.hello) { peer = e.source; send({ deck: state }); }
    if (d.deck && (d.deck.i !== state.i || d.deck.step !== state.step)) {
      peer = e.source;
      go(d.deck.i, d.deck.step, { silent: true });
    }
  });

  if (mode === 'deck') {
    var touchX = null;
    deckEl.addEventListener('touchstart', function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    deckEl.addEventListener('touchend', function (e) {
      if (touchX === null) return;
      var dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) { if (dx < 0) next(); else prev(); }
      touchX = null;
    });

    var idleTimer;
    document.addEventListener('mousemove', function () {
      root.classList.remove('is-idle');
      clearTimeout(idleTimer);
      idleTimer = setTimeout(function () { root.classList.add('is-idle'); }, 2500);
    });

    window.addEventListener('hashchange', function () {
      if (fromHash() !== state.i) go(fromHash(), 0);
    });
  }

  // Ingen animation vid första visningen, bara vid byte av bild
  root.classList.add('is-loading');
  window.addEventListener('resize', fit);
  fit();
  if (mode === 'presenter') buildPresenter();
  if (mode === 'deck' && fromHash() === 0) showHelp();
  go(fromHash(), 0, { silent: true });
  requestAnimationFrame(function () {
    requestAnimationFrame(function () { root.classList.remove('is-loading'); });
  });

  window.deck = { go: go, next: next, prev: prev, count: slides.length,
                  get state() { return { i: state.i, step: state.step }; } };
})();
