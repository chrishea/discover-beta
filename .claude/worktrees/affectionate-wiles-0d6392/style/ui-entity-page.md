# Entity Page Template Specification

**Canonical reference:** `eat/black-bear-coffee-shop.html` (cleaned April 2026)

This document fully specifies how to build an entity page for DiscoverCloudcroft.com. An entity page is a standalone page for one business (restaurant, shop, attraction, lodging property, etc.). A new entity page can be built from this spec alone.

---

## Architecture

- Single-file HTML
- All **reusable** CSS lives in `css/common.css`
- Only **page-specific** CSS goes in a `<style>` block in `<head>` (hero background image, hero overlay opacity tweaks)
- No inline `style=""` attributes except truly one-off layout adjustments
- Shared JS in `js/common.js` (hamburger menu, back-to-top, scroll)
- Per-page IntersectionObserver script before `</body>`

---

## HEAD Structure

Order matters. Follow this exact sequence:

```html
<head>
    <!-- 1. Character set -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- 2. Title — Format: "Name | Category in Cloudcroft, NM" -->
    <title>Black Bear Coffee Shop | Coffee &amp; Gallery on Burro Ave, Cloudcroft, NM</title>

    <!-- 3. SEO meta -->
    <meta name="description" content="150-160 character description with primary keyword.">
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    <link rel="canonical" href="https://discovercloudcroft.com/eat/[filename].html">

    <!-- 4. Open Graph -->
    <meta property="og:title" content="Name | Category in Cloudcroft, NM">
    <meta property="og:description" content="Short description for social sharing.">
    <meta property="og:url" content="https://discovercloudcroft.com/eat/[filename].html">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://discovercloudcroft.com/media/og-default.webp">

    <!-- 5. Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Name | Cloudcroft, NM">
    <meta name="twitter:description" content="Short description.">
    <meta name="twitter:image" content="https://discovercloudcroft.com/media/og-default.webp">

    <!-- 6. Fonts -->
    <link href="../css/fonts.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&display=swap" rel="stylesheet">

    <!-- 7. Stylesheet -->
    <link rel="stylesheet" href="../css/common.css">

    <!-- 8. Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "[SchemaType]",
      "name": "[Business Name]",
      "description": "[Description]",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[Street]",
        "addressLocality": "Cloudcroft",
        "addressRegion": "NM",
        "postalCode": "88317",
        "addressCountry": "US"
      },
      "telephone": "[phone]",
      "url": "[website]",
      "servesCuisine": ["[type1]", "[type2]"]
    }
    </script>

    <!-- 9. Page-specific CSS (ONLY hero image + overlay) -->
    <style>
        .hero-bg {
            background: url('[path-to-hero-image]') center 40% / cover no-repeat;
        }

        .hero-overlay {
            background: linear-gradient(135deg, rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.2));
        }
    </style>
</head>
```

### Schema.org Types by Category
| Category | @type |
|----------|-------|
| Restaurant | `Restaurant` |
| Coffee shop | `CafeOrCoffeeShop` |
| Bakery | `Bakery` |
| Lodging | `LodgingBusiness`, `Hotel`, `BedAndBreakfast`, `Motel` |
| Attraction | `TouristAttraction` |
| Shop | `LocalBusiness` |
| Winery | `Winery` |
| Bar | `BarOrPub` |

---

## Color & Typography Tokens

All defined in `css/common.css :root`. Use these variables, never hardcode colors.

| Token | Value | Usage |
|-------|-------|-------|
| `--midnight` | `#000000` | Primary dark text |
| `--charcoal` | `#000000` | Body text, headings |
| `--charcoal-light` | `#444444` | Secondary body text, paragraphs |
| `--charcoal-muted` | `#777777` | Tertiary / muted text |
| `--pine-light` | `#333333` | Section labels |
| `--cream` | `#ffffff` | Page background |
| `--cream-dark` | `#f2f2f2` | Alternate section background |
| `--cloud-drift` | `#f2f2f2` | Alias for cream-dark |
| `--golden-hour` | `#000000` | Accent, card borders, buttons |
| `--gold` | `#000000` | Alias for golden-hour |
| `--alpine` | `#333333` | Link accent |
| `--ember` | `#333333` | Secondary accent |
| `--granite` | `#444444` | Alias for charcoal-light |
| `--twilight` | `#000000` | Dark accent |
| `--cta-red` | `#2B2B2B` | Dark CTA background (not red) |
| `--footer-main` | `#2B2B2B` | Footer background |

### Typography
- **Headings:** `font-family: 'DM Sans', sans-serif; font-weight: 700`
- **Body:** `font-family: 'Inter', sans-serif; font-weight: 400`
- **Section labels:** `font-family: 'DM Sans'; font-weight: 500; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 3px`

---

## BODY Structure — Section by Section

Every entity page follows this exact section order. Sections marked *optional* can be omitted.

### 1. Skip Link
```html
<a href="#main-content" class="skip-to-content">Skip to main content</a>
```

### 2. Site Header
```html
<header class="site-header" role="banner">
    <div class="header-inner">
        <nav class="header-nav" role="navigation" aria-label="Main navigation">
            <a href="../index.html" class="logo header-logo" aria-label="Discover Cloudcroft — home">
                <span class="logo-discover">Discover</span>
                <span class="logo-cloudcroft">Cloudcroft</span>
                <span class="logo-beta">Beta</span>
            </a>
            <a href="../stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html">Stay</a>
            <a href="../eat/complete-guide-where-to-eat-in-cloudcroft-2026.html">Eat</a>
            <a href="../do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html">Activities</a>
            <a href="../visit/where-to-visit.html">Visit</a>
            <a href="../events/top-events.html">Events</a>
            <a href="../season/seasonal.html">Seasons</a>
            <a href="../complete-guide-to-cloudcroft-new-mexico-2026.html#reels">Reels</a>
            <a href="../resources/resources.html">Resources</a>
            <a href="../resources/contact.html">Contact</a>
        </nav>
        <button class="hamburger" type="button" aria-label="Open navigation menu" aria-expanded="false"
            aria-controls="mobile-nav">
            <span></span><span></span><span></span>
        </button>
    </div>
</header>
```
- Use `../` prefix for all files in subdirectories

### 3. Mobile Nav Overlay
```html
<nav class="mobile-nav-overlay" id="mobile-nav" aria-label="Mobile navigation" hidden>
    <!-- Same links as header nav, same ../  prefix -->
</nav>
```

### 4. Hero Section
```html
<section class="hero" aria-label="Page hero">
    <div class="hero-bg" role="img" aria-label="[Descriptive alt text]"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="hero-badge">
            <span>[Category Label]</span>
        </div>
        <h1 class="hero-title">
            <span class="word">[Word1] </span>
            <span class="word">[Word2] </span>
            <span class="word">[Word3] </span>
        </h1>
        <p class="hero-subtitle">[1-2 sentence hook]</p>
        <div class="hero-ctas">
            <a href="#[section-id]" class="btn-primary">[Primary CTA]</a>
            <a href="#[section-id]" class="btn-secondary">[Secondary CTA]</a>
        </div>
    </div>
</section>
```
- Each word in h1 gets its own `<span class="word">` for staggered animation
- Hero BG is set in the page `<style>` block (the only page-specific CSS)
- Default hero-overlay in common.css is `rgba(0,0,0,0.6)` to `rgba(0,0,0,0.3)` — override in page `<style>` if the image needs a lighter or darker overlay

### 5. Info Bar
```html
<div class="info-bar">
    <div class="info-bar-inner">
        <div class="info-bar-item">
            <div class="info-bar-icon">&#x1F4CD;</div>
            <span>[Address]</span>
        </div>
        <div class="info-bar-item">
            <div class="info-bar-icon">&#x2615;</div>
            <span>[Category]</span>
        </div>
        <div class="info-bar-item">
            <div class="info-bar-icon">&#x1F4DE;</div>
            <span><a href="tel:[number]">[formatted phone]</a></span>
        </div>
        <div class="info-bar-item">
            <div class="info-bar-icon">&#x1F331;</div>
            <span>[Key Feature]</span>
        </div>
    </div>
</div>
```
- Always 4 items
- Use HTML entities for emoji (&#x1F4CD;, &#x2615;, etc.)

### 6. Main Content — `<main id="main-content" role="main">`

All content sections live inside `<main>`. Each section follows this wrapper pattern:

```html
<section class="section" id="[id]" aria-label="[Accessible label]">
    <div class="section-container">
        <!-- Content here -->
    </div>
</section>
```

For centered section headers (most sections except About):
```html
<div class="section-header-center">
    <span class="section-label">[Small Label]</span>
    <h2 class="section-title section-title-centered">[Section Title]</h2>
    <p class="section-description">[Optional subtitle]</p>
</div>
```

For alternating background sections, add the `section-alt` class:
```html
<section class="section section-alt" id="[id]" aria-label="[label]">
```

---

## Section Types — Component Catalog

### A. About Section
The first content section. Left-aligned text, no centered header.

```html
<section class="section" id="about" aria-label="About [Name]">
    <div class="section-container">
        <div class="about-grid">
            <div class="about-text fade-in">
                <span class="section-label">About</span>
                <h2 class="section-title">[Headline]</h2>
                <p>[Paragraph 1]</p>
                <p>[Paragraph 2]</p>
                <p>[Paragraph 3]</p>
                <div class="about-features">
                    <span class="about-feature">&#x2615; [Feature 1]</span>
                    <span class="about-feature">&#x1F3A8; [Feature 2]</span>
                    <span class="about-feature">&#x1F331; [Feature 3]</span>
                    <span class="about-feature">&#x1F6CD;&#xFE0F; [Feature 4]</span>
                    <span class="about-feature">&#x1F4CD; [Feature 5]</span>
                </div>
            </div>
        </div>
    </div>
</section>
```
- **CSS:** `.about-grid`, `.about-text`, `.about-features`, `.about-feature` — all in common.css
- Feature pills: 3-5 short tags summarizing the business identity
- The `.fade-in` class triggers IntersectionObserver animation

### B. Menu / Content Grid Section
Grid of cards showcasing menu categories, offerings, or key topics.

```html
<section class="section menu-section" id="menu" aria-label="Menu">
    <div class="section-container">
        <div class="section-header-center">
            <span class="section-label">[Label]</span>
            <h2 class="section-title section-title-centered">[Title]</h2>
            <p class="section-description">[Subtitle]</p>
        </div>
        <div class="entity-photo-feature">
            <img src="[photo-path]" alt="[descriptive alt]" loading="lazy">
        </div>
        <div class="menu-grid">
            <div class="menu-card">
                <h3>[Card Title]</h3>
                <p>[Card description]</p>
                <ul class="menu-items">
                    <li>[Item 1]</li>
                    <li>[Item 2]</li>
                </ul>
            </div>
            <!-- Repeat cards -->
        </div>
        <div class="tip-box">
            <span>&#x1F4F1;</span>
            <p><strong>[Bold lead.]</strong> [Supporting text with optional <a> link.]</p>
        </div>
    </div>
</section>
```
- **CSS:** `.menu-grid` (3-col responsive), `.menu-card`, `.menu-items` — all in common.css
- **`.entity-photo-feature`** — centered photo block, `max-width: 700px`, `border-radius: 12px` — in common.css
- **`.tip-box`** — flex row with emoji + text. Links inside `.tip-box` are automatically styled `steelblue` via `.tip-box a` in common.css
- `.menu-card` gets IntersectionObserver animation

### C. Gallery Section *(optional)*
Photo grid for the business.

```html
<section class="section" id="gallery" aria-label="[Gallery Label]">
    <div class="section-container">
        <div class="section-header-center">
            <span class="section-label">[Label]</span>
            <h2 class="section-title section-title-centered">[Title]</h2>
        </div>
        <div class="gallery-grid">
            <div class="gallery-item">
                <img src="[photo]" alt="[descriptive alt]" loading="lazy">
                <div class="gallery-caption">[Caption]</div>
            </div>
            <!-- Repeat items -->
        </div>
    </div>
</section>
```
- **CSS:** `.gallery-grid` (responsive multi-col), `.gallery-item`, `.gallery-caption` — all in common.css
- `.gallery-item` gets IntersectionObserver animation with staggered delays
- Can be combined with a highlights grid below the gallery

### D. Highlights Section
3-column feature cards, usually below a gallery or as a standalone section.

```html
<div class="highlights-grid" style="margin-top: 2rem;">
    <div class="highlight-card">
        <div class="highlight-icon">&#x1F3A8;</div>
        <h3>[Highlight Title]</h3>
        <p>[Description]</p>
    </div>
    <!-- 3 cards total -->
</div>
```
- **CSS:** `.highlights-grid` (3-col), `.highlight-card`, `.highlight-icon` — all in common.css
- Center-aligned text inside each card
- `.highlight-card` gets IntersectionObserver animation
- The `style="margin-top: 2rem;"` is allowed when the highlights-grid sits directly below a gallery-grid (it's a spacing context, not a style override)

### E. Visit / Plan Your Visit Section
Always uses `section-alt` for the background. Contains a 3-column grid of practical info cards.

```html
<section class="section section-alt" id="visit" aria-label="Plan your visit">
    <div class="section-container">
        <div class="section-header-center">
            <span class="section-label">Plan Your Visit</span>
            <h2 class="section-title section-title-centered">Visit [Name]</h2>
            <p class="section-description">[Subtitle]</p>
        </div>
        <div class="visiting-grid">
            <div class="visiting-card">
                <h3>Location</h3>
                <p><a href="[Google Maps directions URL]">[Street Address]</a>, City, NM ZIP.</p>
            </div>
            <div class="visiting-card">
                <h3>Hours</h3>
                <p>[Hours info or link to check current hours.]</p>
            </div>
            <div class="visiting-card">
                <h3>Contact</h3>
                <p><a href="tel:[number]">[formatted phone]</a><br>
                   <a href="[website]" target="_blank" rel="noopener noreferrer">[domain]</a></p>
            </div>
            <div class="visiting-card">
                <h3>Good to Know</h3>
                <p>[Practical tips, seating info, parking, etc.]</p>
            </div>
        </div>
    </div>
</section>
```
- **CSS:** `.visiting-grid` (3-col), `.visiting-card` — all in common.css
- **Links:** `.visiting-card a` is styled `steelblue` with no underline via common.css. No inline color styles needed.
- `.visiting-card` uses `<h3>` in the HTML. Common.css targets `.visiting-card h4` for styling — heading level in the CSS should be updated to match, or use `<h4>` in HTML to match. Currently the `<h3>` inherits general heading styles which works fine visually.
- `.visiting-card` gets IntersectionObserver animation
- Google Maps directions URL format: `https://www.google.com/maps/dir/?api=1&destination=[encoded address]`

### F. Profile Section *(optional)*
Links to an external article or feature story about the business.

```html
<section class="section" id="profile" aria-label="Profile">
    <div class="section-container">
        <div class="section-header-center">
            <span class="section-label">Profile</span>
            <h2 class="section-title section-title-centered">[Headline]</h2>
        </div>
        <div class="tip-box">
            <span>&#x1F4F0;</span>
            <p><strong>[Publication name]</strong> — <a href="[article-url]" target="_blank" rel="noopener noreferrer">[Article title]</a>. [Brief description of what the article covers.]</p>
        </div>
    </div>
</section>
```

### G. CTA Section
Full-width call-to-action block. Always the last section before `</main>`.

```html
<section class="cta-section" aria-label="Call to action">
    <div class="cta-container">
        <h2>[Compelling Headline]</h2>
        <p>[1-2 sentence summary]</p>
        <div class="cta-buttons">
            <a href="[website]" target="_blank" rel="noopener noreferrer" class="btn-primary">[Primary CTA]</a>
            <a href="[social-url]" target="_blank" rel="noopener noreferrer" class="btn-secondary">[Secondary CTA]</a>
            <a href="complete-guide-where-to-eat-in-cloudcroft-2026.html" class="btn-secondary">Explore More Dining</a>
        </div>
    </div>
</section>
```
- **CSS:** `.cta-section`, `.cta-container`, `.cta-buttons`, `.btn-primary`, `.btn-secondary` — all in common.css
- Background: `var(--cream-dark)`
- Centered text, max-width 700px

---

## Footer

```html
<footer class="site-footer" role="contentinfo" aria-label="Site footer">
    <div class="footer-grid">
        <div class="footer-col footer-brand" style="padding-top:2vh;text-align:center">DISCOVER CLOUDCROFT
            <span style="font-size:90%;">New Mexico's Mountain Retreat</span>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2026 DiscoverCloudcroft.com. All rights reserved.</p>
    </div>
</footer>
```
- **CSS:** `.site-footer`, `.footer-grid`, `.footer-col`, `.footer-brand`, `.footer-bottom` — all in common.css

---

## Back to Top Button

```html
<button class="back-to-top" aria-label="Back to top">&uarr;</button>
```
- Handled by `js/common.js`

---

## Scripts

Always placed at the end of `<body>`, after the footer and back-to-top button.

```html
<script src="../js/common.js"></script>
<script>
    (function () {
        var observerOptions = { threshold: 0.15, rootMargin: '0px 0px -50px 0px' };
        var fadeObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.fade-in, .menu-card, .highlight-card, .visiting-card, .gallery-item').forEach(function (el) {
            fadeObserver.observe(el);
        });
    })();
</script>
```

### How the fade-in works
1. Elements start at `opacity: 0; transform: translateY(20-30px)` (set in common.css per component)
2. IntersectionObserver watches them with `threshold: 0.15`
3. When 15% visible, the `.visible` class is added
4. `.visible` transitions to `opacity: 1; transform: translateY(0)`
5. Staggered delays via `:nth-child` rules in common.css
6. Observer unobserves after firing (animation runs once)

### Which elements to observe
Add every animated component class to the `querySelectorAll` string:
- `.fade-in` — about text, general fade targets
- `.menu-card` — menu/content grid cards
- `.highlight-card` — highlight feature cards
- `.visiting-card` — visit/plan cards
- `.gallery-item` — gallery photos

---

## Reusable CSS Classes in common.css

### Layout
| Class | Purpose |
|-------|---------|
| `.section` | Standard section wrapper (padding: 3rem) |
| `.section-alt` | Alternate background (var(--cream-dark)) |
| `.section-container` | Max-width 1400px centered container |
| `.section-header-center` | Centers section header text |

### Typography
| Class | Purpose |
|-------|---------|
| `.section-label` | Uppercase small label above section title |
| `.section-title` | Main section heading (clamp 1.8-2.5rem) |
| `.section-title-centered` | Centers the section title |
| `.section-description` | Subtitle paragraph below section title |

### Components
| Class | Purpose |
|-------|---------|
| `.entity-photo-feature` | Centered featured photo wrapper (max-width 700px) |
| `.entity-photo-feature img` | Photo styling (border-radius, object-fit cover) |
| `.about-grid` | About section layout grid |
| `.about-text` | About section text column |
| `.about-features` | Feature pill container |
| `.about-feature` | Individual feature pill/tag |
| `.menu-grid` | 3-col content card grid |
| `.menu-card` | Content card with fade-in animation |
| `.menu-items` | Bulleted list inside menu card |
| `.highlights-grid` | 3-col highlight card grid |
| `.highlight-card` | Centered highlight card |
| `.highlight-icon` | Emoji/icon above highlight title |
| `.gallery-grid` | Multi-col responsive photo grid |
| `.gallery-item` | Photo wrapper with hover caption reveal |
| `.gallery-caption` | Overlay caption on gallery photos |
| `.visiting-grid` | 3-col visiting info card grid |
| `.visiting-card` | Info card with left border accent |
| `.tip-box` | Flex row callout box (emoji + text) |
| `.cta-section` | Full-width CTA block |
| `.cta-container` | CTA content wrapper |
| `.cta-buttons` | CTA button row |
| `.btn-primary` | Primary dark button |
| `.btn-secondary` | Secondary outlined button |
| `.back-to-top` | Floating scroll-to-top button |

### Automatic Link Styling
| Selector | Color | Notes |
|----------|-------|-------|
| `.visiting-card a` | `steelblue` | No inline style needed |
| `.tip-box a` | `steelblue` | No inline style needed |
| `.info-bar-item a` | inherited | Styled via common.css |

---

## Do / Don't Rules

### DO
- Use `loading="lazy"` on all images except the hero
- Use `role="img"` and `aria-label` on the hero background div
- Use `aria-label` on every `<section>`
- Use `target="_blank" rel="noopener noreferrer"` on all external links
- Use HTML entities for emoji in the source (&#x1F4CD; not the emoji character)
- Use `<h1>` only in the hero; `<h2>` for section titles; `<h3>` for card titles
- Keep the page `<style>` block to hero-bg and hero-overlay only
- Place Google Maps directions links in the Location visiting-card
- List the IntersectionObserver selectors to match every animated component on the page

### DON'T
- Don't add `<style>` blocks for styles that belong in common.css
- Don't use inline `style=""` for colors, fonts, or spacing that common.css handles
- Don't use `style="text-align: center;"` — use `class="section-header-center"` instead
- Don't use `style="background: var(--cloud-drift);"` — use `class="section-alt"` instead
- Don't use inline `style="color: steelblue"` on visiting-card links — handled by `.visiting-card a`
- Don't use inline `style="color: var(--alpine)"` on tip-box links — handled by `.tip-box a`
- Don't hardcode color values; use CSS custom properties
- Don't skip the IntersectionObserver script — cards will remain invisible without it
- Don't use `<h4>` or lower for section-level headings
- Don't add documentation files (README, etc.) unless explicitly requested

---

## Checklist for New Entity Pages

1. [ ] `<title>` with business name + location keyword
2. [ ] `<meta name="description">` — 150-160 chars
3. [ ] `<link rel="canonical">` — full absolute URL
4. [ ] OG tags (title, description, url, type, image)
5. [ ] Twitter Card tags
6. [ ] Schema.org JSON-LD with correct `@type`
7. [ ] Page `<style>` contains ONLY hero-bg and hero-overlay
8. [ ] Site header with correct `../` path prefix
9. [ ] Mobile nav overlay with matching links
10. [ ] Hero: badge, h1 with word spans, subtitle, 2 CTA buttons
11. [ ] Info bar: 4 items (address, category, phone, key feature)
12. [ ] About section with section-label, h2, paragraphs, feature pills
13. [ ] Menu/content section with grid cards and tip-box
14. [ ] Gallery section with captioned photos *(if photos available)*
15. [ ] Highlights section (3 cards) *(if relevant)*
16. [ ] Visit section with `section-alt` class: Location, Hours, Contact, Good to Know
17. [ ] CTA section with primary + secondary buttons
18. [ ] Standard footer
19. [ ] Back-to-top button
20. [ ] `common.js` script tag
21. [ ] IntersectionObserver script with all animated selectors listed
22. [ ] All images have descriptive `alt` text
23. [ ] All images use `loading="lazy"`
24. [ ] No inline styles that duplicate common.css rules
25. [ ] All external links have `target="_blank" rel="noopener noreferrer"`
