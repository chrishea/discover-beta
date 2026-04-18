# Prompt: Rewrite the Cloudcroft Activities Guide to Match ui-topic Template

## Objective

Rewrite `complete-guide-to-activities-in-Cloudcroft-NM-2026.html` so that it uses the same design system, CSS classes, HTML structure, JavaScript patterns, and visual conventions as `style/ui-topic.md` (the canonical topic-page template for DiscoverCloudcroft.com). The result should look like a sibling page to the main Complete Guide — same header, same footer, same card grid patterns, same animations, same typography — but with the activities content.

## Reference Files

- **Template:** `style/ui-topic.md` — the full HTML source for the topic-page pattern
- **Theme variant:** `style/ui-topic-theme.md` — a second reference with identical structure
- **Shared stylesheet:** `css/common.css` — must be linked (not inlined); contains header, footer, hero, section, card, button, animation, and responsive styles
- **Shared font stack:** `css/fonts.css` + Google Fonts (DM Sans 500/700, Inter 400/500/600)
- **Shared JS:** `js/common.js` — must be linked; handles header scroll behavior, hamburger toggle, back-to-top button
- **Content source:** The current `complete-guide-to-activities-in-Cloudcroft-NM-2026.html` — all written content, data, and source links from this file must be preserved

## Design System Rules (from common.css + ui-topic.md)

### Color palette (all black-and-white)
- `--pine: #000000` / `--pine-light: #333333`
- `--cream: #ffffff` / `--cream-dark: #f2f2f2`
- `--charcoal: #000000` / `--charcoal-light: #444444` / `--charcoal-muted: #777777`
- `--cta-red: #2B2B2B` (buttons, badges, CTA backgrounds)
- `--footer-main: #2B2B2B`
- Body font: Inter 400, 16px implied base, line-height 1.6
- Heading font: DM Sans 700
- Small labels/eyebrows: DM Sans 500-700, uppercase, letter-spacing 0.1–0.2em

### Page structure pattern
1. `<a class="skip-to-content">` — accessibility skip link
2. `<header class="site-header">` with `.header-inner`, `.header-nav`, `.header-logo`, `.hamburger`
3. `<div class="mobile-nav-overlay">` — mobile menu
4. `<main id="main-content">` containing:
   - **Hero** (`.hero` > `.hero-bg` + `.hero-overlay` + `.hero-content`) — full-viewport image hero with title, subtitle, meta items, fadeUp animations
   - **TOC bar** (`.toc-section` > `.toc-inner` > `.toc-label` + `.toc-links` with pill-style anchor links)
   - **Guide body** (`.guide-body` max-width 900px) containing numbered `.guide-section` blocks
   - **Full-width sections** (`.section` with `.section-container` max-width 1400px) for card grids, seasonal grid, practical info
   - **CTA banner** (`.guide-cta` dark background)
5. `<footer class="site-footer">` with footer grid, social icons, copyright
6. Back-to-top button
7. Inline `<script>` — IntersectionObserver for `.fade-in` and all card types

### Component patterns to use

| Content type | Template pattern | CSS class |
|---|---|---|
| Top 7 activities (main ranked list) | 2-column image card grid | `.things-grid` > `.thing-card` with `.thing-card-icon img`, h3, p, `.thing-card-link` |
| Outdoor activity categories (hiking, drives, camping, winter) | 3-column icon card grid | `.outdoor-grid` > `.outdoor-card` with `.outdoor-icon`, h3, p, `.outdoor-detail` |
| In-town stops (coffee, dining, browsing) | 2-column card grid with images or icons | `.restaurant-grid` > `.restaurant-card` (adapt for non-restaurant stops) or `.things-grid` |
| Seasonal activities (spring/summer/fall/winter) | 4-column season cards | `.seasonal-grid` > `.seasonal-card` with `.seasonal-icon`, h3, `.season-months`, p |
| Traveler-type recommendations | 3-column info cards | `.card-grid` > `.card` with `.card-icon`, h3, p |
| Planning notes / practical info | 3-column practical cards | `.practical-grid` > `.practical-card` with `.practical-icon`, h3, p |
| Callouts / tips | Tip box | `.tip-box` with `.tip-icon` + `<p>` |
| One-day itinerary (best bets) | Itinerary with time slots | `.itinerary-day` > `.day-header` + `.itin-stops` > `.itin-stop` (grid: time | content) |

### Key animation pattern
- All cards start with `opacity: 0; transform: translateY(20px)` and get `.visible` class added via IntersectionObserver
- Staggered delays via `:nth-child(n).visible { transition-delay: 0.07s * n }`
- Hero elements use CSS `@keyframes fadeUp` with staggered `animation-delay`

### Section numbering
- Each `.guide-section` gets a `<span class="section-number">01</span>` etc.
- h2 has `font-family: DM Sans`, `border-bottom: 3px solid #000`, `display: inline-block`

## Content Mapping

Map the existing content sections to template patterns:

| Existing section | Target template pattern | Section # |
|---|---|---|
| Hero + summary cards | Full hero with `.hero-content`, `.hero-meta` items | — |
| TOC | `.toc-section` with pill links | — |
| Intro | Opening text in first `.guide-section` | 01 |
| Overview (what it's good at / not) | `.guide-section` with prose + `.tip-box` | 02 |
| Best bets (one day) | `.itinerary-day` pattern | part of 02 |
| Best 7 activities | `.things-grid` > `.thing-card` (2-col image cards, use placeholder images) | 03 |
| Outdoor activities (hiking, drives, camping, winter) | `.outdoor-grid` > `.outdoor-card` (3-col icon cards) | 04 |
| In-town activities | `.restaurant-grid` or `.things-grid` (2-col cards) | 05 |
| Seasonal activities | `.seasonal-grid` > `.seasonal-card` (4-col) inside full-width `.seasonal-section` | 06 (full-width) |
| By traveler type | `.card-grid` > `.card` (3-col icon cards) inside full-width `.section` | 07 (full-width) |
| Planning notes | `.practical-grid` > `.practical-card` (3-col) inside full-width `.section` | 08 (full-width) |
| Source notes | `.guide-section` with styled link list | 09 |
| Research gaps | `.guide-section` or omit from public page | 10 or omit |
| CTA banner | `.guide-cta` (dark bg, two buttons) | — |

## Specific Instructions

1. **Link external CSS/JS — do not inline common styles.** Use `<link rel="stylesheet" href="css/common.css">` and `<script src="js/common.js"></script>`. Only page-specific overrides go in an inline `<style>` block (hero image, any section-specific tweaks).

2. **Use placeholder images.** For hero: `media/placeholder-hero-main.webp`. For activity cards: `media/placeholder-activity-biking.jpg` (or similar). Add descriptive `alt` text.

3. **Preserve all written content.** Every paragraph, bullet, callout, and source link from the current file must appear in the rewrite. Restructure into cards and grids, but do not cut text.

4. **Convert the 2026 callout** to a `.tip-box` with a ⚠️ icon and `<strong>2026 note:</strong>` lead.

5. **Nav links should match the template nav** (Stay, Eat, Explore, Trails, Events, Seasons, Plan, Contact) — not the old nav from the current file.

6. **Add structured data** (`application/ld+json` TouristDestination schema) matching the template pattern.

7. **Add SEO meta tags** (description, keywords, og:*, twitter:*) tuned for "activities in Cloudcroft NM 2026."

8. **Include the IntersectionObserver script** at the bottom matching the template pattern — observe all card types, `.fade-in` elements.

9. **Include the footer** matching the template exactly (brand block, Explore/Connect/Plan columns, social SVGs, copyright).

10. **Responsive:** Grids collapse per the template breakpoints (768px, 480px). Verify the patterns match.

## Output

A single HTML file: `complete-guide-to-activities-in-Cloudcroft-NM-2026.html` — ready to drop into the site root alongside the existing pages, linking to `css/common.css`, `css/fonts.css`, and `js/common.js`.
