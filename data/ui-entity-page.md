# UI Topic Page Template

Reference file: `eat/where-to-eat-cloudcroft-1899-at-the-lodge-2026.html`

This document defines the standard page template used for individual topic pages (restaurants, shops, attractions, lodging properties, etc.) on DiscoverCloudcroft.com.

---

## Architecture Overview

Single-file HTML with all CSS inline in `<head>`. No build system. Shared assets from `css/common.css`, `css/fonts.css`, `js/common.js`, and Google Fonts (DM Sans 500/700).

---

## HEAD Structure

```
1. <meta charset="UTF-8">
2. <meta name="viewport">
3. <title> — Format: "Name | Category in Cloudcroft, NM — Tagline"
4. <meta name="description"> — 150-160 chars, primary keyword
5. <meta name="keywords"> — comma-separated
6. <link rel="canonical"> — full absolute URL
7. OG tags: og:title, og:description, og:url, og:type (website), og:image
8. Twitter tags: twitter:card (summary_large_image), twitter:title, twitter:description, twitter:image
9. Font links: ../css/fonts.css, Google Fonts preconnect, DM Sans
10. <link rel="stylesheet" href="../css/common.css">
11. Schema.org JSON-LD <script> — type varies by page category
12. <style> — all page-specific CSS inline
```

### Schema.org Types by Category
- Restaurant pages → `Restaurant`
- Lodging pages → `LodgingBusiness`, `Hotel`, `BedAndBreakfast`, `Motel`
- Activity pages → `TouristAttraction`
- Shop pages → `LocalBusiness`
- Winery → `Winery`
- Guide/article pages → `Article`
- Event pages → `Event`

---

## CSS Design System

### Color Variables (from common.css)
```css
--midnight       /* dark text */
--golden-hour    /* accent / gold */
--granite        /* secondary text */
--cloud-drift    /* light section background */
--snow-cap       /* white card background */
--alpine         /* link color */
--charcoal       /* info-bar text */
--cream-dark     /* info-bar background */
--ember          /* accent */
--twilight       /* accent */
```

### Dark Background Color
`#2B2B2B` — used for dark cards, feature blocks, and the bottom-line section. NOT pure black.

### Shared Patterns

**Card base:**
```css
background: #ffffff;
border-radius: 12px;
padding: 2rem;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
border-top: 4px solid var(--golden-hour);
```

**Dark card:**
```css
background: #2B2B2B;
border-radius: 12px;
padding: 2rem;
color: #fff;
```
- Headings: `color: var(--golden-hour)`
- Body text: `color: rgba(255, 255, 255, 0.7)` or `0.8`

**Fade-in animation (all cards):**
```css
opacity: 0;
transform: translateY(20px);

.visible {
    opacity: 1;
    transform: translateY(0);
    transition: opacity 0.5s ease, transform 0.5s ease;
}
/* Stagger with nth-child: */
:nth-child(2).visible { transition-delay: 0.1s; }
:nth-child(3).visible { transition-delay: 0.2s; }
:nth-child(4).visible { transition-delay: 0.3s; }
```

**Tip box:**
```css
display: flex; align-items: flex-start; gap: 1rem;
background: #fffbe6; border: 1px solid #f0d060;
border-radius: 12px; padding: 1.25rem 1.5rem; margin-top: 2rem;
```

**Responsive breakpoints:**
- 1024px: 3-col → 2-col
- 768px: 2-col → 1-col

---

## BODY Structure — Section by Section

### 1. Skip Link
```html
<a href="#main-content" class="skip-to-content">Skip to main content</a>
```

### 2. Header (canonical)
```html
<header class="site-header" role="banner">
    <div class="header-inner">
        <nav class="header-nav" role="navigation" aria-label="Main navigation">
            <a href="[prefix]index.html" class="logo header-logo" aria-label="Discover Cloudcroft — home">
                <span class="logo-discover">Discover</span>
                <span class="logo-cloudcroft">Cloudcroft</span>
                <span class="logo-beta">Beta</span>
            </a>
            <a href="[prefix]stay/lodging.html">Stay</a>
            <a href="[prefix]eat/complete-guide-to-dining.html">Eat</a>
            <a href="[prefix]do/complete-guide-to-activities.html">Explore</a>
            <a href="[prefix]do/where to-hike-in-Cloudcroft-New-Mexico-2026.html">Trails</a>
            <a href="[prefix]do/what-events-are-happening-in-cloudcroft-2026.html">Events</a>
            <a href="[prefix]season/seasonal.html">Seasons</a>
            <a href="[prefix]plan.html">Plan</a>
            <a href="[prefix]contact.html">Contact</a>
        </nav>
        <button class="hamburger" aria-label="Open navigation menu" aria-expanded="false">
            <span></span><span></span><span></span>
        </button>
    </div>
</header>
```
- **Path prefix:** `../` for files in subdirectories, empty for root files.

### 3. Mobile Nav Overlay
```html
<div class="mobile-nav-overlay" role="dialog" aria-label="Mobile navigation">
    <!-- Same links as header nav, same prefix rules -->
</div>
```

### 4. Hero Section
```html
<section class="hero" aria-label="Page hero">
    <div class="hero-bg" role="img" aria-label="[descriptive alt]"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="hero-badge"><span>[Category Label]</span></div>
        <h1 class="hero-title">
            <span class="word">[Word] </span>
            <span class="word">[Word] </span>
            <!-- Each word gets its own span for staggered animation -->
        </h1>
        <p class="hero-subtitle">[1-2 sentence description]</p>
        <div class="hero-ctas">
            <a href="#[section]" class="btn-primary">[Primary CTA]</a>
            <a href="#[section]" class="btn-secondary">[Secondary CTA]</a>
        </div>
    </div>
</section>
```

**Hero background options:**
- Photo: `background: url('../media/[image].webp') center 40% / cover no-repeat;`
- Gradient (no photo): `background: linear-gradient(135deg, #color1 0%, #color2 50%, #color3 100%);`

### 5. Info Bar
```html
<div class="info-bar">
    <div class="info-bar-inner">
        <div class="info-bar-item">
            <div class="info-bar-icon">[emoji]</div>
            <span>[Fact]</span>
        </div>
        <!-- 4 items total -->
    </div>
</div>
```

### 6. Main Content — `<main id="main-content" role="main">`

Standard sections inside main, each following this pattern:

```html
<section class="section" id="[id]" aria-label="[label]">
    <div class="section-container">
        <div style="text-align: center;">
            <span class="section-label">[Small Label]</span>
            <h2 class="section-title section-title-centered">[Section Title]</h2>
            <p class="section-description">[Subtitle]</p>
        </div>
        <!-- Section content: grids, cards, lists -->
    </div>
</section>
```

Alternate background for every other section: `style="background: var(--cloud-drift);"`

### 7. Standard Section Types

**About section** — `.about-grid` (2-col: text + image)
- Left: `.about-text` with `.section-label`, `h2.section-title`, paragraphs, `.about-features` (tag cloud)
- Right: `.about-image` with `<img>` or placeholder

**Grid cards** — `.menu-grid`, `.also-grid`, `.brigade-grid`, `.wine-grid`, etc.
- 3-col responsive grid
- Cards: white (light) or #2B2B2B (dark)
- Each card: emoji icon, h3, paragraph, optional `<ul class="menu-items">` list

**Highlights section** — `.highlights-grid` (3-col)
- Cards: `.highlight-card` with `.highlight-icon`, h3, p
- Light style with subtle border

**Visiting/Plan section** — `.visiting-grid` (2x2)
- Cards: `.visiting-card` with `.visiting-icon`, h3, p
- Standard items: Location, Hours, Contact, Good to Know

**Feature block** — dark full-width block for signature content
```css
display: grid; grid-template-columns: 1fr 1fr;
background: #2B2B2B; border-radius: 16px; color: #fff; padding: 3rem;
```

### 8. CTA Section
```html
<section class="cta-section" aria-label="Call to action">
    <div class="cta-container">
        <h2>[Headline]</h2>
        <p>[Description]</p>
        <div class="cta-buttons">
            <a href="[url]" class="btn-primary">[Primary]</a>
            <a href="[url]" class="btn-secondary">[Secondary]</a>
        </div>
    </div>
</section>
```

### 9. Footer
Standard site footer with `.footer-grid` (4 columns: brand, explore links, connect links, plan links), `.footer-bottom` copyright. Uses `../` prefix for subdirectory pages.

### 10. Scripts
```html
<script src="[prefix]js/common.js"></script>
<script>
    (function() {
        var observerOptions = { threshold: 0.15, rootMargin: '0px 0px -50px 0px' };
        var fadeObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('[comma-separated list of animated selectors]').forEach(function(el) {
            fadeObserver.observe(el);
        });
    })();
</script>
```

---

## Naming Conventions

### File names
- Dining: `where-to-eat-cloudcroft-[name]-[year].html`
- Lodging: `stay-[name]-cloudcroft.html` or `the-lodge-at-cloudcroft-[year].html`
- Activities: `complete-guide-to-[activity].html` or `where-to-[verb]-in-cloudcroft-[year].html`
- Shopping: `guide-to-shopping-in-cloudcroft-[year].html`
- Guides: `complete-guide-to-[topic]-[year].html`

### CSS class naming
- Grid containers: `.[topic]-grid` (e.g., `.menu-grid`, `.wine-grid`, `.brigade-grid`)
- Cards: `.[topic]-card` (e.g., `.menu-card`, `.wine-card`, `.brigade-card`)
- Dark cards: `.also-card`, `.pick-card`
- Utilities: `.fade-in`, `.tip-box`, `.section-label`, `.section-title`

---

## Checklist for New Pages

1. [ ] Title with location keyword
2. [ ] Meta description (150-160 chars)
3. [ ] Canonical URL
4. [ ] OG + Twitter tags
5. [ ] Schema.org JSON-LD (correct type)
6. [ ] Canonical header with correct path prefix
7. [ ] Mobile nav overlay
8. [ ] Hero with badge, h1 (word spans), subtitle, 2 CTAs
9. [ ] Info bar (4 items)
10. [ ] About section (2-col: text + image)
11. [ ] Main content sections (cards, grids, lists)
12. [ ] Highlights section (3 cards)
13. [ ] Visit/Plan section (4 cards: location, hours, contact, tips)
14. [ ] CTA section
15. [ ] Standard footer
16. [ ] IntersectionObserver script for all animated elements
17. [ ] All images have descriptive alt text
18. [ ] Responsive breakpoints (1024px, 768px)
