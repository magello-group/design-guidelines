/* ==========================================================================
   Magello designsystem — delad JavaScript (magello.js)
   Header-scroll, sidospår, mobilmeny, dropdown och undermenyer.
   Ingen build, inga beroenden. Se design-guidelines-web.md (avsnitt 12–15).
   ========================================================================== */
(function () {
  'use strict';

  var $  = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var isMobile = function () { return window.innerWidth <= 768; };
  var setExpanded = function (el, open) { if (el) el.setAttribute('aria-expanded', open ? 'true' : 'false'); };

  /* ── Header och sidospår ─────────────────────────────────────────────
     Startsidan (sticky) kollapsar polygonen efter 8 px. Undersidor
     (.mg-page-header--rotate) roterar headern efter 80 px och visar sidospåret. */
  var header  = $('.mg-page-header');
  var sideNav = $('.mg-side-nav');
  if (header) {
    var threshold = header.classList.contains('mg-page-header--rotate') ? 80 : 8;
    var onScroll = function () {
      var scrolled = window.scrollY > threshold;
      header.classList.toggle('is-scrolled', scrolled);
      if (sideNav && !isMobile()) sideNav.classList.toggle('is-visible', scrolled);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () {
      if (sideNav && isMobile()) sideNav.classList.remove('is-visible');
      else onScroll();
    });
    onScroll();
  }

  /* ── Mobilmeny (hamburgare) ────────────────────────────────────────── */
  var burger     = $('.mg-nav__burger');
  var mobileMenu = $('.mg-mobile-menu');
  var closeBtn   = $('.mg-mobile-menu__close');
  function setMenu(open) {
    if (!mobileMenu) return;
    mobileMenu.classList.toggle('is-open', open);
    mobileMenu.setAttribute('aria-hidden', open ? 'false' : 'true');
    setExpanded(burger, open);
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (burger)   burger.addEventListener('click', function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener('click', function () { setMenu(false); });

  /* ── Dropdown i headern (desktop) ──────────────────────────────────────
     Synligheten styrs bara av .is-open, aldrig av CSS :hover.
     220 ms stängningsfördröjning per listpunkt, så att musen hinner från
     länk till meny. Undermenyn ligger i listpunkten i DOM:en, så listpunktens
     mouseenter/mouseleave täcker även menyn. Egna lyssnare på undermenyn får
     inte finnas: deras mouseleave startade stängningen när musen gick från
     menyn tillbaka till länken, och menyn försvann under pekaren.
     När en meny redan är öppen byter hover till grannen först efter 150 ms,
     så att musen kan gå snett ned över grannlänken utan att menyn byts.
     Ett musklick på chevron när menyn öppnats av hover håller den öppen
     (tangentbord och touch växlar). Scroll flyttar menyn i stället för att
     stänga den, och stänger bara när headern inte syns. */
  var closeTimers = new WeakMap();
  var openTimers  = new WeakMap();
  function positionSub(item) {
    var sub = $('.mg-nav__sub', item);
    if (!sub) return;
    var rect = item.getBoundingClientRect();
    sub.style.top  = rect.bottom + 'px';   /* position: fixed, ingen lucka */
    sub.style.left = rect.left + 'px';
  }
  function setDrop(item, open) {
    item.classList.toggle('is-open', open);
    setExpanded($('.mg-nav__chevron-btn', item), open);
  }
  function openDrop(item) {
    clearTimeout(closeTimers.get(item));
    clearTimeout(openTimers.get(item));
    positionSub(item);
    $$('.mg-nav__has-sub.is-open').forEach(function (o) {
      if (o !== item) { clearTimeout(closeTimers.get(o)); setDrop(o, false); }
    });
    setDrop(item, true);
  }
  function scheduleClose(item) {
    closeTimers.set(item, setTimeout(function () { setDrop(item, false); }, 220));
  }
  function closeAllDrops() {
    $$('.mg-nav__has-sub.is-open').forEach(function (o) { setDrop(o, false); });
  }
  $$('.mg-nav__has-sub').forEach(function (item) {
    item.addEventListener('mouseenter', function () {
      var other = $$('.mg-nav__has-sub.is-open').some(function (o) { return o !== item; });
      if (other) openTimers.set(item, setTimeout(function () { openDrop(item); }, 150));
      else openDrop(item);
    });
    item.addEventListener('mouseleave', function () {
      clearTimeout(openTimers.get(item));
      scheduleClose(item);
    });
  });
  $$('.mg-nav__chevron-btn').forEach(function (btn) {
    var pointer = '';
    btn.addEventListener('pointerdown', function (e) { pointer = e.pointerType; });
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var item = btn.closest('.mg-nav__has-sub');
      var hovered = e.detail > 0 && pointer === 'mouse' && item.matches(':hover');   /* mus, inte touch eller Enter/Space */
      pointer = '';
      if (item.classList.contains('is-open') && !hovered) setDrop(item, false); else openDrop(item);
    });
  });
  document.addEventListener('click', closeAllDrops);
  window.addEventListener('scroll', function () {
    var rotated = header && header.matches('.mg-page-header--rotate.is-scrolled');
    $$('.mg-nav__has-sub.is-open').forEach(function (o) {
      var r = o.getBoundingClientRect();
      if (rotated || r.bottom <= 0) setDrop(o, false); else positionSub(o);
    });
  }, { passive: true });

  /* ── Undermenyer i mobilmeny och sidospår (accordion) ──────────────────
     Chevron-knappen fäller ut/in. I sidospåret fäller även ett klick på
     huvudlänken ut undermenyn (i stället för att navigera). */
  function toggleSub(li) {
    var sub = $('.mg-mob-sub, .mg-side-sub', li);
    if (!sub) return;
    var open = sub.classList.toggle('is-open');
    setExpanded($('.mg-mob-toggle, .mg-side-toggle', li), open);
  }
  $$('.mg-mob-toggle, .mg-side-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () { toggleSub(btn.closest('li')); });
  });
  $$('.mg-side-has-sub .mg-side-parent > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      toggleSub(link.closest('.mg-side-has-sub'));
    });
  });

  /* ── Kopiera-knapp ──────────────────────────────────────────────────
     <button class="mg-btn mg-btn--secondary" data-mg-copy="#id">Kopiera</button>
     kopierar textinnehållet i #id. Knapptexten blir "Kopierat" i 2 s
     (ändra med data-mg-copied). */
  $$('[data-mg-copy]').forEach(function (btn) {
    var label = btn.textContent;
    btn.addEventListener('click', function () {
      var target = $(btn.getAttribute('data-mg-copy'));
      if (!target) return;
      var text = target.textContent;
      var done = function () {
        btn.textContent = btn.getAttribute('data-mg-copied') || 'Kopierat';
        setTimeout(function () { btn.textContent = label; }, 2000);
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(done);
      } else {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); done(); } catch (e) { /* markera för hand */ }
        ta.remove();
      }
    });
  });

  /* ── Filtrera en lista ──────────────────────────────────────────────
     <input type="search" data-mg-filter="#lista"> döljer barn med
     data-mg-filter-item i #lista vars text inte innehåller söktexten.
     Ett element med data-mg-filter-empty="#lista" visas när inget matchar. */
  var fold = function (s) { return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); };
  $$('[data-mg-filter]').forEach(function (input) {
    var sel = input.getAttribute('data-mg-filter');
    var list = $(sel);
    if (!list) return;
    var items = $$('[data-mg-filter-item]', list);
    var empty = $('[data-mg-filter-empty="' + sel + '"]');
    input.addEventListener('input', function () {
      var q = fold(input.value.trim());
      var shown = 0;
      items.forEach(function (it) {
        var hit = !q || fold(it.textContent).indexOf(q) !== -1;
        it.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.hidden = shown > 0;
    });
  });

  /* ── Escape stänger meny och dropdown ──────────────────────────────── */
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    setMenu(false);
    closeAllDrops();
  });
})();
