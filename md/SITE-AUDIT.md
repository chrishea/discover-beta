# Discover Cloudcroft — Full Site Audit Report

**Date:** 2026-02-26
**Pages audited:** 45 HTML files (4 duplicates/copies skipped)
**Domain:** discovercloudcroft.com

---

## Phase 1: Technical Audit

### 1.1 Link Integrity

| Metric | Count |
|--------|-------|
| Valid internal links | 954 |
| Placeholder `#` links | 518 |
| Broken internal links | 83 |

**Broken links by cause:**

| Issue | References | Affected Files |
|-------|-----------|----------------|
| `events.html` does not exist | 14 links from 7 files | about, contact, dark-skies, history, real-estate, shopping |
| `back-door.html` does not exist | 55+ links from 4 files | attractions, dining, local-media, lodging (nav + logo) |
| `lodging.html#rentals` — anchor ID missing | 6 links from 5 files | attractions, dining, index, local-media, pickleball |
| `privacy-policy.html` / `terms-of-use.html` — wrong filenames | 4 links from 2 files | index.html, pickleball.html (should be `privacy.html` / `terms.html`) |
| `attractions.html#events` / `#stewardship` — IDs missing | 2 links from index.html | index.html |

**Placeholder links:** 518 `href="#"` links across nearly every page, concentrated in footers (social icons, "Contact Us", "Press & Media", "Chamber of Commerce", "Partner With Us", "Privacy Policy", "Terms of Use").

### 1.2 Missing Images

**46 missing image files** referenced in HTML:

| Page | Missing Files | Count |
|------|--------------|-------|
| `index.html` | `placeholder-event-mayfair.jpg`, `placeholder-event-harvestfest.jpg`, `placeholder-event-christmas.jpg`, `placeholder-season-spring.jpg`, `placeholder-season-summer.jpg`, `placeholder-activity-hiking.jpg`, `placeholder-activity-ohv.jpg`, `placeholder-activity-walks.jpg`, `Index-3.jpg`, `Index-5.jpg` | 10 |
| `dining.html` | `placeholder-dine-big-daddys.jpg`, `-brother-n-law-bbq.jpg`, `-cloudcroft-brewery.jpg`, `-mad-jacks.jpg`, `-western-bar.jpg`, `-instant-karma.jpg`, `-high-rollin.jpg` | 7 |
| `big-daddys.html` | Entire `media/art-big-daddys/` directory missing (8 files) | 7 |
| `mad-jacks-bbq.html` | Entire `media/art-mad-jacks/` directory missing (8 files) | 7 |
| `high-rollin.html` | `DC-Pix-High-Rollin-01001.png` through `01006.png`, `logo-high-rollin.png` | 7 |
| `cloudcroft-brewery.html` | `IMG_8468.jpeg` | 2 |
| `summer.html` | `blue-donkey.png` | 1 |

### 1.3 Orphan Files

- **2 orphan HTML pages:** `entity-page-template.html` (expected), `offline.html` (expected — PWA fallback)
- **57 of 78 media files** are never referenced by any HTML page (~130 MB unused)
- **3 "back-door copy" files** and 1 duplicate template should be deleted

### 1.4 Image Performance

**57 of 78 images exceed 500 KB.** Worst offenders:

| File | Size |
|------|------|
| `Winter-02.JPG` | 20.7 MB |
| `placeholder-season-winter.jpg` | 18.4 MB |
| `Index-1.jpg` / `Index-56.jpg` / `placeholder-hero-main.jpg` | 15.8 MB each |
| `HA-Classic-00002.jpg` | 14.4 MB |
| `placeholder-activity-biking.jpg` | 13.4 MB |

Total media directory: **194.7 MB** — most images are uncompressed originals that need conversion to optimized WebP.

### 1.5 SEO

**Strengths:** 43 of 45 pages score 10/10 on core SEO tags (title, description, canonical, OG, Twitter Card). All titles and descriptions are unique. All canonical URLs correctly formatted.

**Issues found:**

| Issue | Count | Details |
|-------|-------|---------|
| Heading hierarchy skips (h2 → h4) | 18 pages | Systemic pattern in "Location" sections of business pages, plus about, contact, dark-skies, emergency-services, history, nearby-destinations, real-estate |
| Missing `<h1>` | 1 page | `emergency-services.html` starts at h2 |
| Missing JSON-LD structured data | 3 business pages | `high-rollin.html`, `instant-karma.html`, `western-bar.html` (peers all have it) |
| Canonical URL inconsistency | 1 page | `index.html` uses `https://discovercloudcroft.com` (no trailing slash) |

### 1.6 PWA

**manifest.json:** Fully valid. All 10 icon files exist. All required fields present. Shortcuts configured.

**sw.js issues:**
- Runtime cache never cleaned — stale entries accumulate indefinitely
- No cache size limit — unbounded storage growth on mobile
- No query string normalization — UTM parameters cause cache misses
- 29 pages not precached (only available offline if previously visited)

**Per-page PWA tags:** All 43 content pages have manifest link, theme-color, and service worker registration.

### 1.7 Security

**Overall: Good.** No external JS dependencies, no dangerous patterns (innerHTML/eval/document.write), no API keys or credentials exposed, all HTML structure valid.

| Issue | Severity | Details |
|-------|----------|---------|
| 38 pages lack `:focus` CSS styles | High | Keyboard navigation severely impaired |
| 39 pages lack skip-to-content links | High | Screen reader users can't bypass nav |
| 38 pages have no ARIA role attributes | Medium | Only 7 pages have banner/menubar/contentinfo roles |
| `--pine-light` on white fails WCAG AA | Medium | Contrast ratio 2.58–2.76:1 (needs 3:1 minimum) |
| 1 iframe without `sandbox` | Medium | `local-media.html` — cloudcroftreader.com embed |
| 5 inline `onclick` handlers | Low | `contact.html` (4) + `offline.html` (1) — would block CSP |
| 1 HTTP link | Low | `cannabis.html` → `http://backcountrycannabisnm.com` |
| 8 plaintext emails | Low | Across 5 files — spam scraping risk |
| Contact form non-functional | Low | preventDefault + alert only, no backend |

---

## Phase 2: Content Completeness

### 2.1 Coverage Scorecard

| Category | Covered | Missing | Grade |
|----------|---------|---------|-------|
| **Lodging** | 3 properties + camping (10 sites) + vacation rentals | The Lodge Resort (naming confusion), Crofting Cabins, RV parks, Sleepy Grass/Silver campgrounds | C+ |
| **Dining** | 7 restaurants with detail pages | Rebecca's/Lodge Restaurant, Dave's Cafe, Dusty Boots, Mountain Top Mercantile, Spruce Moose | C |
| **Activities** | Hiking (6 trails), biking (8 routes), camping, pickleball, dark skies, golf, disc golf | Ski Cloudcroft, fishing, horseback riding, ATV/OHV, bird watching, rock climbing, geocaching | C |
| **Attractions** | Sunspot Observatory, dark skies, history, rail trail | Trestle Recreation Area, Sacramento Mountains Museum, Zenith Park, The Flume | C+ |
| **Events** | 2 detail pages (Lumberjack Day, Bike Classic) | No events.html page, no Mayfair/Oktoberfest/July Jamboree/Christmas/Aspenfest/farmers market pages | D |
| **Seasonal Guides** | All 4 seasons covered with activities + events | Road conditions (only winter), packing lists, seasonal closures missing on 3 of 4 | B- |
| **Practical Info** | FAQ (directions, altitude, cell, weather, pets), emergency services | Gas stations, parking, detailed route descriptions, air travel/car rental info | B |
| **Nearby Destinations** | White Sands, High Rolls, La Luz, Timberon, Mayhill | Ruidoso, Alamogordo, Tularosa, Three Rivers, Sitting Bull Falls, Valley of Fires, Carrizozo, Mescalero | D+ |
| **Shopping & Services** | 16 shops on directory + art galleries, cannabis, real estate, groceries | No individual shop detail pages (directory adequate for small village) | B+ |

### 2.2 Content Quality

**Critical finding: Zero real photographs on any page except the homepage and bike classic hero.** All business, trail, campground, and attraction pages use emoji icons as image placeholders. Despite 78 files in `media/` (194 MB), almost none are referenced outside `index.html`.

| Quality Issue | Count |
|---------------|-------|
| Pages using emoji placeholders instead of photos | 40+ |
| Pages with broken image references | 5 (index, dining, big-daddys, mad-jacks, high-rollin) |
| Business pages missing embedded maps | All (use emoji map placeholders) |
| Missing phone numbers | 2 (high-rollin, instant-karma) |

---

## Phase 3: Missing Assets Inventory

| Page | Issue Type | Description | Priority |
|------|-----------|-------------|----------|
| `dining.html` | Missing images | 7 `placeholder-dine-*.jpg` files don't exist — **entire listing page has broken images** | **High** |
| `index.html` | Missing images | 10 image refs to nonexistent files (events, seasons, activities sections) | **High** |
| `big-daddys.html` | Missing images | Entire `media/art-big-daddys/` directory missing (7 files) | **High** |
| `mad-jacks-bbq.html` | Missing images | Entire `media/art-mad-jacks/` directory missing (7 files) | **High** |
| `high-rollin.html` | Missing images | 7 `DC-Pix-High-Rollin-*.png` files + logo missing | **High** |
| `cloudcroft-brewery.html` | Missing image | `IMG_8468.jpeg` doesn't exist | Medium |
| `summer.html` | Missing image | `blue-donkey.png` doesn't exist | Medium |
| All business pages | Missing photos | Use emoji icons instead of real photographs | **High** |
| All business pages | Missing maps | Use emoji placeholder instead of embedded Google Maps | Medium |
| `events.html` | Missing page | 14 nav/footer links point to this nonexistent page | **High** |
| `back-door.html` | Missing page | 55+ links from 4 pages point to this nonexistent file | **High** |
| All seasonal pages | Missing photos | Use emoji placeholders, no seasonal photography | Medium |
| `nearby-destinations.html` | Missing content | 5 of 10+ destinations, uses `destination-image-placeholder` class | Medium |

---

## Phase 4: Cross-Page Consistency

### 4.1 Navigation: 5 Different Structures

| Structure | Pages | Description |
|-----------|-------|-------------|
| **Standard** (links to `index.html#section`) | 33 pages | The majority pattern |
| **Direct links** (Home, Lodging, Dining, Activities, Events) | 6 pages | about, contact, dark-skies, history, real-estate, shopping |
| **Links to `back-door.html`** (BUG) | 4 pages | attractions, dining, local-media, lodging |
| **Self-referencing** (`#section`) | 1 page | index.html (correct) |
| **No nav** | 1 page | offline.html (expected) |

### 4.2 Footer: 3 Variants + 26 Unique Link Combinations

| Variant | Pages | Columns |
|---------|-------|---------|
| A — Standard | 34 pages | Explore \| Visit \| Plan \| Connect |
| B — Flat | 6 pages | No column headers (about, contact, dark-skies, history, real-estate, shopping) |
| C — Seasonal | 4 pages | Seasons \| Explore \| Visit \| Plan |

26 distinct footer link combinations exist. Copyright year only on homepage.

### 4.3 Color Schemes: 3 Theme Groups

| Theme | Pages | `--pine-deep` |
|-------|-------|---------------|
| Blue (Material Design) | 41 pages | `#1565C0` |
| Teal | 3 pages (attractions, dining, lodging) | `#2a9d8f` |
| Custom night sky | 1 page (dark-skies) | N/A |

Note: CLAUDE.md documents a pine-green palette (`#2D6B4A`) that no page actually uses — the documentation is out of date.

### 4.4 Accessibility Elements Distribution

| Element | Pages WITH | Pages WITHOUT |
|---------|-----------|---------------|
| Skip-to-content link | 6 | 39 |
| `role="banner"` on header | 6 | 38 |
| `role="contentinfo"` on footer | 7 | 37 |
| `aria-label` on nav | 7 | 37 |
| `:focus` CSS styles | 7 | 38 |
| Social follow bar (red top bar) | 2 | 43 |
| Mobile menu close button | 6 | 39 |

### 4.5 Font Loading

44 of 45 pages load identical Google Fonts. `offline.html` loads a reduced subset (intentional).

---

## Phase 5: Prioritized Action Plan

### CRITICAL (site is broken)

| # | Issue | Files | Fix |
|---|-------|-------|-----|
| 1 | **4 pages nav/logo link to nonexistent `back-door.html`** | attractions, dining, local-media, lodging | Change all `back-door.html` refs to `index.html` — one-line fix per file |
| 2 | **`events.html` doesn't exist but is linked from 7 pages** | about, contact, dark-skies, history, real-estate, shopping + nav | Create events.html OR update 14 links |
| 3 | **Dining page has 7 broken images** — all `placeholder-dine-*.jpg` missing | dining.html | Add the 7 image files or update references |
| 4 | **Homepage has 10 broken image references** | index.html | Add missing files or fix src paths |
| 5 | **3 business pages have entire image directories missing** (big-daddys, mad-jacks, high-rollin) | big-daddys.html, mad-jacks-bbq.html, high-rollin.html | Add ~21 missing image files |
| 6 | **`privacy-policy.html` / `terms-of-use.html` wrong filenames** | index.html, pickleball.html | Change to `privacy.html` / `terms.html` — one-line fix |
| 7 | **`lodging.html#rentals` anchor doesn't exist** | lodging.html (+ 5 pages linking to it) | Add `id="rentals"` to the appropriate section |

### HIGH PRIORITY (significantly hurts UX)

| # | Issue | Scope | Fix |
|---|-------|-------|-----|
| 8 | **No real photos on 40+ pages** — all use emoji placeholders | Site-wide | Add photographs to business, trail, attraction, and seasonal pages |
| 9 | **38 pages lack `:focus` styles** — keyboard nav broken | 38 HTML files | Add `:focus` CSS rules to each page |
| 10 | **39 pages lack skip-to-content links** | 39 HTML files | Add skip-link markup + CSS to each page |
| 11 | **5 navigation structures** — inconsistent user experience | 10 pages differ from standard | Standardize all pages to one nav pattern |
| 12 | **518 placeholder `#` links** in footers site-wide | All pages | Replace with real URLs (contact.html, privacy.html, terms.html, social profiles, etc.) |
| 13 | **Missing dining coverage** — Rebecca's, Dave's Cafe, Dusty Boots, Mountain Top Mercantile, Spruce Moose | dining.html + new pages | Add to dining.html, create detail pages for each |
| 14 | **No events calendar page** — only 2 of 10+ events have pages | New events.html + event pages | Create events.html directory + pages for Mayfair, Oktoberfest, July Jamboree, Christmas, Aspenfest |
| 15 | **Nearby destinations incomplete** — missing Ruidoso, Alamogordo, Tularosa, + 6 more | nearby-destinations.html | Add sections for each missing destination |
| 16 | **Missing activities** — Ski Cloudcroft, fishing, horseback, ATV/OHV | activities.html + new pages | Create dedicated pages or add content sections |
| 17 | **WCAG contrast failure** — `--pine-light` text fails AA at all sizes | CSS variables site-wide | Darken `--pine-light` to at least `#4A8EB0` for 3:1 contrast |

### MEDIUM PRIORITY (noticeable quality issues)

| # | Issue | Scope | Fix |
|---|-------|-------|-----|
| 18 | **Images need compression** — 57 files over 500KB, many 10-20MB | media/ directory | Compress all images, convert to WebP, target <200KB each |
| 19 | **57 orphan media files** (~130MB unused) | media/ directory | Audit and delete unused files |
| 20 | **Heading hierarchy skips** (h2→h4) on 18 pages | 18 HTML files | Change `<h4>` to `<h3>` in Location sections |
| 21 | **38 pages missing ARIA roles** (banner, contentinfo, menubar) | 38 HTML files | Add role attributes to header, footer, nav |
| 22 | **26 different footer link combinations** | All pages | Standardize footer markup across all pages |
| 23 | **3 pages use teal color scheme** instead of blue | attractions, dining, lodging | Update `:root` variables to match site standard |
| 24 | **No embedded Google Maps** on any business page | All business pages | Replace emoji map placeholders with iframe embeds |
| 25 | **Social follow bar only on 2 pages** | 43 pages missing it | Add to all pages or remove from the 2 |
| 26 | **3 business pages missing JSON-LD** | high-rollin, instant-karma, western-bar | Add structured data matching peer pages |
| 27 | **Service worker cache issues** — unbounded growth, no query normalization | sw.js | Add cache size limits, strip query params before matching |
| 28 | **1 iframe missing sandbox attribute** | local-media.html | Add `sandbox="allow-scripts allow-same-origin"` |
| 29 | **Seasonal guides lack road conditions** (except winter) + seasonal closures | spring, summer, fall | Add road condition and closure sections |
| 30 | **Contact form non-functional** | contact.html | Integrate with backend (Formspree, Netlify Forms, etc.) |
| 31 | **Delete duplicate files** | back-door copy (x3), entity-page-template 2 | Delete 4 files |
| 32 | **Gas station info missing** — critical for remote village | faq.html or new page | Add fuel availability information |
| 33 | **Copyright year only on homepage** | 43 pages | Add year to all footers |

### LOW PRIORITY (polish and enhancements)

| # | Issue | Scope | Fix |
|---|-------|-------|-----|
| 34 | Update CLAUDE.md — documents pine-green palette but site uses blue | CLAUDE.md | Update color documentation |
| 35 | Add `loading="lazy"` to 10 remaining images | 5 files | One-line fix per image |
| 36 | Upgrade HTTP link to HTTPS | cannabis.html | Change `http://backcountrycannabisnm.com` to `https://` |
| 37 | Obfuscate 8 plaintext email addresses | 5 files | Use JS rendering or contact forms |
| 38 | Move 5 inline onclick handlers to addEventListener | contact.html, offline.html | Enables future CSP |
| 39 | Add `offline.html` responsive breakpoints | offline.html | Add @media queries |
| 40 | Remove `.DS_Store` from repo + add `.gitignore` | media/.DS_Store | Delete + create .gitignore |
| 41 | Add individual shop detail pages | 16 new pages | Optional — shopping.html directory may be sufficient |
| 42 | Add scroll-to-top button | All pages | New UI element |
| 43 | Create pages for Sacramento Mountains Museum, Zenith Park, The Flume | 3 new pages | New content |
| 44 | Add `index.html` canonical trailing slash | index.html | Change to `https://discovercloudcroft.com/` |

---

## Summary Counts

| Metric | Count |
|--------|-------|
| Broken internal links | 83 |
| Placeholder `#` links | 518 |
| Missing image files | 46 |
| Orphan media files | 57 |
| Missing `alt` tags | 0 |
| SEO tag gaps | 4 (heading hierarchy on 18 pages, 1 missing h1, 3 missing JSON-LD, 1 canonical inconsistency) |
| Accessibility issues | 39 pages missing skip links, 38 missing focus styles, 38 missing ARIA roles, 1 contrast failure |
| Pages with content gaps | 12+ (events, nearby destinations, missing activities, thin lodging) |
| **Total: Critical** | **7** |
| **Total: High** | **10** |
| **Total: Medium** | **16** |
| **Total: Low** | **11** |
