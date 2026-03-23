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
      document.body.style.overflow = '';
      if (mobileBackdrop) mobileBackdrop.classList.remove('open');
    } else {
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
  var fadeSelectors = '.fade-in-section, .slide-in-bottom, .fade-in, .info-card, .stat-item';
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
})();
