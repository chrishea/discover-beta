(function () {
  'use strict';

  // ===== HEADER SCROLL EFFECT =====
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 60) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // ===== MOBILE MENU TOGGLE =====
  var hamburger = document.querySelector('.hamburger');
  // Support all mobile menu naming patterns
  var mobileNav = document.querySelector('.mobile-nav-overlay')
    || document.querySelector('.mobile-menu')
    || document.querySelector('.mobile-overlay');
  var mobileBackdrop = document.querySelector('.mobile-nav-backdrop');

  function toggleMobileMenu() {
    if (!hamburger || !mobileNav) return;
    var isOpen = mobileNav.classList.contains('open');

    hamburger.classList.toggle('active');
    hamburger.setAttribute('aria-expanded', String(!isOpen));

    if (isOpen) {
      mobileNav.classList.remove('open');
      mobileNav.setAttribute('hidden', '');
      document.body.style.overflow = '';
      if (mobileBackdrop) mobileBackdrop.classList.remove('open');
    } else {
      mobileNav.removeAttribute('hidden');
      mobileNav.classList.add('open');
      document.body.style.overflow = 'hidden';
      if (mobileBackdrop) mobileBackdrop.classList.add('open');
    }
  }

  if (hamburger) {
    hamburger.addEventListener('click', toggleMobileMenu);
  }

  if (mobileBackdrop) {
    mobileBackdrop.addEventListener('click', toggleMobileMenu);
  }

  // Close mobile menu on link click
  if (mobileNav) {
    var mobileLinks = mobileNav.querySelectorAll('a');
    mobileLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        if (mobileNav.classList.contains('open')) {
          toggleMobileMenu();
        }
      });
    });
  }

  // ===== INTERSECTION OBSERVER: Fade-in elements =====
  var fadeSelectors = '.fade-in-section, .slide-in-bottom, .fade-in, .info-card, .stat-item, .trail-card, .tip-card, .highlight-card';
  var fadeElements = document.querySelectorAll(fadeSelectors);

  if (fadeElements.length > 0) {
    if ('IntersectionObserver' in window) {
      var fadeObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            entry.target.classList.add('visible');
            fadeObserver.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      fadeElements.forEach(function (el) {
        fadeObserver.observe(el);
      });
    } else {
      // Fallback: show everything immediately
      fadeElements.forEach(function (el) {
        el.classList.add('is-visible');
        el.classList.add('visible');
      });
    }
  }

  // ===== COUNTER ANIMATION =====
  var statNumbers = document.querySelectorAll('.stat-number[data-target]');
  var countersStarted = false;

  function animateCounters() {
    if (countersStarted) return;
    countersStarted = true;

    statNumbers.forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-target'));
      var suffix = el.getAttribute('data-suffix') || '';
      var type = el.getAttribute('data-type') || 'integer';
      var duration = 2000;
      var startTime = null;

      function step(timestamp) {
        if (!startTime) startTime = timestamp;
        var elapsed = timestamp - startTime;
        var progress = Math.min(elapsed / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);

        if (type === 'year') {
          el.textContent = Math.floor(eased * target);
        } else if (type === 'decimal') {
          el.textContent = (eased * target).toFixed(1) + suffix;
        } else {
          el.textContent = Math.floor(eased * target).toLocaleString() + suffix;
        }

        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          if (type === 'decimal') {
            el.textContent = target.toFixed(1) + suffix;
          } else {
            el.textContent = target.toLocaleString() + suffix;
          }
        }
      }

      requestAnimationFrame(step);
    });
  }

  if (statNumbers.length > 0 && 'IntersectionObserver' in window) {
    var statsSection = document.querySelector('.stats-section')
      || document.querySelector('.stats-bar')
      || document.querySelector('.stats-grid');

    if (statsSection) {
      var counterObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCounters();
            counterObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.3 });

      counterObserver.observe(statsSection);
    }
  } else if (statNumbers.length > 0) {
    animateCounters();
  }

  // ===== BACK TO TOP =====
  var backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });

    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ===== BETA MODAL =====
  var betaModal = document.getElementById('beta-modal');
  var betaProgress = document.getElementById('beta-modal-progress');
  if (betaModal && betaProgress) {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        betaProgress.style.width = '0%';
      });
    });
    setTimeout(function () {
      betaModal.style.opacity = '0';
      setTimeout(function () {
        betaModal.remove();
      }, 400);
    }, 12000);
  }

  // ===== SIGNUP MODAL (site-wide) =====
  // Auto-injects #signupModal markup if missing, then wires up every
  // [data-signup-open] trigger on the page (footer Subscribe, nav CTAs, etc.).
  var GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxBHtNoCm_a44NFoYyUerR8qUqj5379Wb1GgbIMjZeHVBoF2f2jH79HclzLzK9j_frT/exec';
  var EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  var signupOpeners = document.querySelectorAll('[data-signup-open]');
  if (signupOpeners.length > 0) {
    var signupModal = document.getElementById('signupModal');
    if (!signupModal) {
      var wrapper = document.createElement('div');
      wrapper.innerHTML = [
        '<div class="signup-modal" id="signupModal" role="dialog" aria-modal="true" aria-labelledby="signupModalTitle" hidden>',
        '  <div class="signup-modal__backdrop" data-modal-close></div>',
        '  <div class="signup-modal__panel" role="document">',
        '    <button type="button" class="signup-modal__close" aria-label="Close" data-modal-close>&times;</button>',
        '    <h2 id="signupModalTitle">We\'ll keep you up-to-date</h2>',
        '    <div class="form-container" id="modalFormContainer">',
        '      <form class="form-row" id="modalSignupForm" novalidate>',
        '        <input type="email" id="modalEmailInput" placeholder="Your email address" required autocomplete="email" aria-label="Email address">',
        '        <button type="submit" id="modalSubmitBtn">Notify Me</button>',
        '      </form>',
        '      <div class="error-message" id="modalErrorMessage" role="alert">Something went wrong. Please try again.</div>',
        '      <div class="success-message">',
        '        <div class="check"><svg viewBox="0 0 24 24"><polyline points="6 12 10 16 18 8"></polyline></svg></div>',
        '        <h3>You\'re on the list!</h3>',
        '        <p>You\'ll get monthly updates from <b>DiscoverCloudcroft</b>.</p>',
        '      </div>',
        '    </div>',
        '    <div class="signup-modal__reassurance">We won\'t share your address.</div>',
        '  </div>',
        '</div>'
      ].join('');
      signupModal = wrapper.firstElementChild;
      document.body.appendChild(signupModal);
    }

    var signupPanel = signupModal.querySelector('.signup-modal__panel');
    var signupForm = document.getElementById('modalSignupForm');
    var signupInput = document.getElementById('modalEmailInput');
    var signupBtn = document.getElementById('modalSubmitBtn');
    var signupContainer = document.getElementById('modalFormContainer');
    var signupErrorEl = document.getElementById('modalErrorMessage');

    var signupLastTrigger = null;
    var signupCurrentSource = 'modal';
    var signupAutoCloseTimer = null;

    function signupFocusables() {
      return Array.prototype.slice.call(
        signupPanel.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
      ).filter(function (el) {
        return !el.disabled && el.offsetParent !== null;
      });
    }

    function signupKeydown(e) {
      if (e.key === 'Escape') {
        e.preventDefault();
        closeSignupModal();
        return;
      }
      if (e.key === 'Tab') {
        var focusables = signupFocusables();
        if (!focusables.length) return;
        var first = focusables[0];
        var last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    }

    function resetSignupForm() {
      if (signupAutoCloseTimer) { clearTimeout(signupAutoCloseTimer); signupAutoCloseTimer = null; }
      signupContainer.classList.remove('success', 'error');
      signupBtn.disabled = false;
      signupBtn.textContent = 'Notify Me';
      signupInput.value = '';
    }

    function openSignupModal(trigger) {
      signupLastTrigger = trigger || null;
      signupCurrentSource = (trigger && trigger.getAttribute('data-signup-source')) || 'modal';
      resetSignupForm();
      signupModal.hidden = false;
      document.body.classList.add('signup-modal-open');
      document.addEventListener('keydown', signupKeydown);
      window.requestAnimationFrame(function () { signupInput.focus(); });
    }

    function closeSignupModal() {
      signupModal.hidden = true;
      document.body.classList.remove('signup-modal-open');
      document.removeEventListener('keydown', signupKeydown);
      if (signupLastTrigger && typeof signupLastTrigger.focus === 'function') {
        signupLastTrigger.focus();
      }
    }

    signupOpeners.forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        if (mobileNav && mobileNav.contains(el) && mobileNav.classList.contains('open')) {
          toggleMobileMenu();
        }
        openSignupModal(el);
      });
    });

    signupModal.addEventListener('click', function (e) {
      if (e.target.hasAttribute('data-modal-close')) {
        closeSignupModal();
      }
    });

    signupForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = signupInput.value.trim();

      if (!EMAIL_PATTERN.test(email)) {
        signupContainer.classList.add('error');
        signupErrorEl.textContent = 'Please enter a valid email address.';
        signupInput.focus();
        return;
      }

      signupContainer.classList.remove('error');
      signupBtn.disabled = true;
      signupBtn.textContent = 'Sending...';

      var formData = new FormData();
      formData.append('email', email);
      formData.append('source', signupCurrentSource);
      formData.append('timestamp', new Date().toISOString());

      fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        mode: 'no-cors',
        body: formData
      }).then(function () {
        signupContainer.classList.add('success');
        signupAutoCloseTimer = setTimeout(closeSignupModal, 2000);
      }).catch(function () {
        signupContainer.classList.add('error');
        signupErrorEl.textContent = "We couldn't reach the server. Please check your connection and try again.";
        signupBtn.disabled = false;
        signupBtn.textContent = 'Notify Me';
      });
    });
  }
})();
