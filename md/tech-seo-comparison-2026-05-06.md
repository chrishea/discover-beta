# Technology Platform & SEO Practices Comparison

**Date:** May 6, 2026
**Sites:** discovercloudcroft.com vs. newmexico.org, visitalbuquerque.org, santafe.org, taos.org, discoverruidoso.com, visitlascruces.com.
**Scope:** Platform, tooling, schema, and on-page SEO practices only. No content/positioning analysis — see `competitive-analysis-2026-05-06.md` for that.

---

## 1. TL;DR

The peer set splits cleanly into two camps:

- **Five sites likely run on Simpleview** — newmexico.org, visitalbuquerque.org, santafe.org, taos.org, visitlascruces.com. Simpleview is the DMO-industry-standard CMS, supporting 1,000+ destinations, and these sites all show the structural fingerprints (partner listings, integrated event calendar modules, listings IDs in URLs, identical IA patterns).
- **One peer is on Squarespace** — discoverruidoso.com (confirmed: every page is canonical-aliased to `discoverruidoso.squarespace.com`).
- **discovercloudcroft.com is the outlier** — hand-rolled static HTML, hosted on AWS, no CMS, no framework, no build system. Every page is a self-contained `.html` file.

That outlier status is both the biggest asset and the biggest liability:

- **Asset.** Full control of the DOM, schema, performance budget, and URL structure. The site can ship aggressive structured data that no Simpleview tenant can match without engineering work outside the CMS — and it does (the homepage already serves Organization + WebSite/SearchAction + TouristDestination + BreadcrumbList + FAQPage + 8 Events `@graph`).
- **Liability.** Every change is hand-edited across 108 files. The May 1 audit found 40 canonical mismatches, 167 broken internal links, 46 missing OG images, six indexable stub pages, and 469 of 486 images missing width/height — defects a CMS would catch by default but that hand-rolled HTML reproduces every time someone copy-pastes a template.

The competitive question is **not** "is the platform good enough?" — it is. The question is **whether the editorial discipline keeps up with the platform's flexibility.**

---

## 2. Methodology and data quality

What's directly observed:
- **discovercloudcroft.com:** read source files in the repo (108 HTML files reviewed in the May 1 audit; homepage and five strategy docs read directly for this report).
- **discoverruidoso.com:** Squarespace confirmed via search results showing `discoverruidoso.squarespace.com` URLs across the site.

What's inferred from public signals:
- **The five Simpleview sites:** Inferred from (a) industry data — Simpleview supports 1,000+ DMOs, is described in industry research as "the only fully-integrated industry-specific destination management platform"; (b) IA patterns shared across these sites (event calendar module structure, partner listings format, URL conventions like `/listing/[business-name]/[id]/`); (c) Santa Fe's parent municipality (`santafenm.gov`) has a published sole-source procurement record naming SimpleView LLC as a vendor. None of this is conclusive without BuiltWith / Wappalyzer login access (egress allowlist blocked direct fetch of these domains during this research).

Where you see a "likely Simpleview" label in this report, treat it as 80% confidence based on industry pattern-matching. A 30-second BuiltWith lookup would convert it to certainty.

---

## 3. Platform and hosting

| Site | Likely platform | Hosting / CDN signal | Build / deploy model |
|---|---|---|---|
| **newmexico.org** | Simpleview CMS (likely) | Simpleview-managed, Akamai/Cloudflare typical | SaaS, CMS-driven |
| **visitalbuquerque.org** | Simpleview CMS (likely) | Simpleview-managed | SaaS, CMS-driven |
| **santafe.org** | Simpleview CMS (likely; parent city has SimpleView procurement record) | Simpleview-managed | SaaS, CMS-driven |
| **taos.org** | Simpleview CMS (likely) | Simpleview-managed | SaaS, CMS-driven |
| **discoverruidoso.com** | **Squarespace** (confirmed) | Squarespace-managed (Cloudflare in front) | SaaS, drag-and-drop CMS |
| **visitlascruces.com** | Simpleview CMS (likely) | Simpleview-managed | SaaS, CMS-driven |
| **discovercloudcroft.com** | **No CMS** — hand-rolled HTML | AWS (S3 + CloudFront most likely, given the SEO docs reference) | Static files, manual deploy, no build step |

**Implication.**

The Simpleview tenants get a defined feature set (event modules, partner directories, mobile apps via Visit Widget, accessibility tooling, map publishing, A/B testing) for a recurring license fee, but they're stuck inside Simpleview's templating system. Their schema, page speed, and DOM structure are largely whatever Simpleview decides to ship.

Squarespace gives Ruidoso baseline quality with zero configuration but the lowest ceiling — schema customization is fiddly, server-side redirects require workarounds, and `discoverruidoso.squarespace.com` showing up in canonical-aliasing search results suggests their domain mapping isn't perfectly clean.

Discover Cloudcroft has the highest ceiling and the lowest floor. The audit findings are the floor showing through.

---

## 4. Tooling layer — analytics, tag managers, forms, maps

What each site appears to run on top of its platform.

| Tool category | Typical Simpleview tenant | Ruidoso (Squarespace) | discovercloudcroft.com |
|---|---|---|---|
| **Analytics** | GA4 + Simpleview's built-in reporting (referrals, impressions, partner clicks) | GA4 + Squarespace Analytics | GA4 only (`G-2CQ53PCP3M`, gtag.js installed top-of-`<head>`) |
| **Tag manager** | GTM common but optional | Limited GTM support | Not installed (gtag direct) |
| **Search Console** | Standard | Standard | **Linked, but not yet linked to GA4** per the Apr 24 conversation — open task |
| **CRM / partner management** | Simpleview CRM (the whole point of the platform — integrated with CVENT for lead routing) | None (manual) | None |
| **Event module** | Simpleview Events module + Visit Widget mobile app | Squarespace Events (basic) | None — events live as JSON-LD `@graph` on the homepage only, no dedicated calendar page |
| **Lodging directory** | Simpleview Listings (CRM-fed, schema-marked, filterable) | Hand-built collection of pages | Hand-built guide pages |
| **Newsletter / forms** | Simpleview Forms + integrations (Mailchimp, Constant Contact) | Squarespace Forms | Custom HTML form → Google Apps Script → Google Sheet (per Apr 27 fix) |
| **Maps** | Simpleview Map Publisher (custom POI maps) | Squarespace native (Google Maps) | None visible on homepage |
| **Search on site** | Simpleview Search module | Squarespace native search | None — no on-site search box |
| **Cookie banner / consent** | Simpleview accessibility partner integration | Squarespace native | Not implemented |
| **Image CDN** | Cloudinary or Akamai typical | Squarespace's own image proxy | Plain S3/CloudFront serving local assets |

**Implication.**

The Simpleview tenants get an integrated CRM-CMS pipeline that turns "businesses listed on the website" into "leads routed to those businesses" — that's the platform's whole revenue justification for DMOs. Discover Cloudcroft has none of that integrated layer. It doesn't need to (no CRM, no member-fee model, no lead routing) but it also can't easily add it. Building a partner-facing dashboard from scratch is a multi-week engineering project.

The GA4-but-no-GTM choice on DC is fine for now but adds friction every time you want to add a pixel, fire an event, or A/B-test a CTA. GTM is the tooling layer the rest of this category eventually adopts.

---

## 5. Schema and structured data

This is where DC actually leads.

**discovercloudcroft.com homepage** (`index.html`) carries six JSON-LD blocks:

1. `Organization` (with publisher attribution to Mountain Monthly LLC, dateModified)
2. `WebSite` with `potentialAction: SearchAction` (sitelinks-search-box eligibility)
3. `TouristDestination` (with `touristType` array and `includesAttraction` array — Lincoln National Forest, Mexican Canyon Trestle, Sacramento Mountains)
4. `BreadcrumbList`
5. `FAQPage` with 5 questions (altitude, weather, cell service, gas/supplies, pet-friendly)
6. `@graph` of 8 `Event` objects with full `Place` + `PostalAddress` + dates + status

That's six entity types on one page. The rewritten `complete-guide-to-cloudcroft-new-mexico-2026.html` adds `Article`, `LodgingBusiness ItemList`, and `Restaurant ItemList` for a total of nine entity types across the two flagship pages.

**Typical Simpleview tenant** ships a smaller, more conservative schema set — usually `LocalBusiness` (or `Hotel`/`Restaurant`) on listings pages, `Event` on event pages, `BreadcrumbList` on most pages, and `Organization` on the homepage. They generally do not stack 6+ entity types on one page; the CMS template doesn't encourage it and there's no rich-result rationale that requires it.

**Squarespace (Ruidoso)** ships baseline schema by default — `Organization`, `WebSite`, `BlogPosting` on blog pages. Limited customization without code injection.

**Where DC's schema breaks down:** the audit's C8 finding — 12 entity pages have JSON-LD where the `"url"` field points to the third-party business website (Airbnb, Summit Inn's own domain, Lincoln National Forest's USFS page) instead of the on-site canonical. That tells Google the canonical entity profile lives elsewhere, which weakens the on-site signal. `eat/black-bear-coffee-shop.html` does it correctly (own URL as `"url"`, third-party in `sameAs`); the 12 stay/* and do/* pages do it backwards. Fix is mechanical: swap `url` and `sameAs`.

**The other open schema items per the audit:**
- 12 guide pages lack `BreadcrumbList` (C10).
- 55 entity pages lack `geo` lat/lng (C9) — blocks map-pack distance computations.
- No `aggregateRating` anywhere (C9 — correct call to skip until first-party reviews exist; Google now penalizes self-serving ratings).

**Net.** DC is ahead on schema *aggressiveness* on the two best pages, behind on schema *consistency* across the rest of the site. The rest of the peer set is the inverse — uniform mediocrity rather than peaks and valleys.

---

## 6. Meta tags, OG, and Twitter cards

| Practice | Simpleview tenants | Ruidoso (Squarespace) | discovercloudcroft.com |
|---|---|---|---|
| **`<meta charset>` and viewport** | Standard | Standard | Standard |
| **`<title>` length discipline** | Generally 50–65 chars (CMS-templated) | Generally short, sometimes too short | **Median 85 chars, max 150 chars** — 87 of 106 pages over the SERP cutoff (audit C1) |
| **`<meta name="description">`** | 140–160 chars typical | Short | **Median 182 chars, max 313 chars** — 83 pages over 160, 44 over 200 (audit C2) |
| **Canonical** | CMS-managed, generally correct | Squarespace-managed | **Self-canonical, but 40 of 105 mismatch the page's own filename** (audit B1) |
| **OG tags (title/description/image/url/type/site_name)** | Full set, CMS-templated | Full set, Squarespace-templated | **Full set on homepage, but `og:image` references missing files on 46 pages** (audit B3) |
| **OG image dimensions (width/height)** | Often present | Sometimes missing | **Specified on homepage (1200×630)** — well-formed where present |
| **Twitter card** | Full set | Full set | Full set on homepage |
| **`hreflang` (language alternates)** | Often present (Spanish on Albuquerque/NM) | Rare | None — single-language site |
| **`<link rel="alternate" application/rss+xml">` (RSS)** | Rare | Sometimes | **Present on homepage** (`/feed.xml`) |
| **`robots` meta** | Mostly correct | Squarespace-managed | Present where needed; **6 stub pages should have noindex but don't** (audit B2) |

**Implication.**

The Simpleview tenants are *unremarkably correct* on meta hygiene. The CMS templates handle 90% of it without a content editor having to think.

DC's meta layer is the single biggest gap between the platform's potential and what's currently shipped. The infrastructure (preconnect to Google Fonts, preload of hero LCP, well-formed OG tags) is sophisticated; the per-page metadata (title length, description length, canonicals pointing to non-existent files) is sloppy. A weekend's work with a Python script that walks every HTML file, trims titles to 60 chars, trims descriptions to 155, and rewrites canonicals to match each file's actual path would close most of this gap.

---

## 7. Performance — image, font, JS, and render practices

| Signal | Simpleview tenants | Ruidoso (Squarespace) | discovercloudcroft.com |
|---|---|---|---|
| **Image format** | WebP increasingly; many sites still serve JPEG/PNG via the CMS image proxy | WebP via Squarespace image proxy | Mixed — `.jpg`, `.jpeg`, `.JPG`, `.webp` co-exist (CLAUDE.md flags this; `optimize-images.sh` handles bulk resize) |
| **Responsive images (`srcset` / `<picture>`)** | Common (CMS-generated) | Common | **Rare** — most `<img>` tags are single-source |
| **`width`/`height` on `<img>`** | Mostly present (CMS injects intrinsic dims) | Mostly present | **17 of 486 have it; 469 do not** — large CLS risk (audit C4) |
| **`loading="lazy"`** | Common below-fold | Common | Most have `lazy`; 25 don't have any `loading=` attribute |
| **Hero LCP preload** | Sometimes (CMS-templated) | Rare | **Homepage and complete-guide page do; 100 of 108 pages don't** (audit C5) |
| **Font strategy** | CMS-bundled | Squarespace-bundled | **Hybrid** — IBM Plex from Google Fonts on most pages + self-hosted via `css/fonts.css` (per CLAUDE.md and SEO Master Plan §4.6, the ambition is "fonts self-hosted, no external font CDNs") |
| **`font-display: swap`** | Inconsistent | Default | Implemented |
| **JavaScript** | Heavier — CMS framework + analytics + map widgets + module scripts | Squarespace bundle (heavyish) | **Single shared `js/common.js` + gtag.js** — exceptionally lean |
| **`defer` / `async` on scripts** | CMS-managed | Squarespace-managed | **84 of 108 pages do not defer `js/common.js`** (audit C6) |
| **Cumulative Layout Shift (CLS) risk** | Low (CMS-managed dimensions) | Low | **High** — direct consequence of missing image dimensions |
| **HTTPS** | Universal | Universal | Universal |

**Implication.**

DC's per-page JavaScript footprint is dramatically lighter than every peer — one shared `js/common.js` (~400 lines for the hamburger, scroll observer, modal, back-to-top) plus gtag.js. Simpleview tenants typically ship 1–3 MB of CMS framework JS plus map and partner-listing widgets. That's a real LCP and TTI advantage for DC in principle.

The principle is being squandered by the image dimension gap. A page with a fast script bundle but unsized hero and gallery images will still score poorly on Core Web Vitals because CLS dominates the visible-instability score. Fix the image dimensions and the lean-JS advantage becomes a real Core Web Vitals win.

---

## 8. URL structure and routing

| Practice | Simpleview tenants | Ruidoso (Squarespace) | discovercloudcroft.com |
|---|---|---|---|
| **URL casing** | Lowercase, hyphenated | Lowercase, hyphenated | Mostly lowercase, but **mixed-case offenders exist** (`stay/stay-the-summit-inn-Cloudcroft-2026.html`) |
| **Spaces in filenames** | Never | Never | **Stub `*copy*.html` files have spaces** (audit B2); `optimize-images.sh` and SEO Master Plan §5.6 explicitly forbid this rule going forward |
| **Trailing slash handling** | Server-handled | Server-handled | Inconsistent (some links link to `/section/`, some to `/section/page.html`) |
| **Pretty URLs (no `.html`)** | Standard | Standard | **Not implemented** — some canonicals reference pretty URLs (`/do/best-camping`) but the file is `do/camp.html` and no rewrite exists, breaking 40 canonicals (audit B1) |
| **Sectioning** | `/things-to-do/`, `/places-to-stay/`, `/events/`, etc. | Same convention | `/do/`, `/eat/`, `/stay/`, `/shop/`, `/season/` — terser, similar pattern |
| **Listings IDs in URLs** | `/listing/[business-name]/[ID]/` (newmexico.org pattern visible in search results) | None | None — entity slugs only |
| **Broken internal links** | Generally caught by CMS | Generally caught by CMS | **167 broken `<a href>`** — `stay/lodging.html` referenced 28 times but doesn't exist; `do/complete-guide-to-activities.html` referenced 11 times (audit B5) |

**Implication.**

The CMS-based peer sites get URL hygiene almost for free. DC, hand-rolled, has accumulated the URL-rewrite tech debt that comes from *intending* to ship pretty URLs without ever actually shipping the server-side rewrite that would make them work. Easy fix: pick one (literal `.html` or pretty), enforce site-wide, ship a `_redirects` (or `.htaccess`) to handle the migration. The Big Plan's Monday-morning action list now leads with this.

---

## 9. Sitemap and robots.txt

| | Simpleview tenants | Ruidoso (Squarespace) | discovercloudcroft.com |
|---|---|---|---|
| **`robots.txt`** | Auto-generated, conservative | Auto-generated | **Permissive and correct** — `User-agent: * / Allow: / / Sitemap: https://discovercloudcroft.com/sitemap.xml` |
| **Sitemap** | Auto-generated, dynamic | Auto-generated, dynamic | **Hand-maintained `sitemap.xml`** — annotated with comments; well-organized; **lists 1 fictional URL, omits 3 real public pages** (audit B4) |
| **Sitemap index for large sites** | Yes | Yes | Not needed at current scale |
| **News sitemap / image sitemap** | Sometimes | Rarely | None |
| **`lastmod` accuracy** | Auto-set to actual modification date | Auto-set | Manually set (e.g., `2026-05-04` across most entries) — accurate but coarse |

**Implication.**

DC's robots.txt is correct. The sitemap is well-intentioned and well-commented but, because it's hand-edited, has drifted from the on-disk file list. A Python script that reads the directory tree and emits the sitemap (excluding `*copy*`, `xxx-*`, `shelf/*`, `drafts/*`, the Google verification file, etc.) closes this gap permanently. The exclusion rules are already documented in the existing sitemap's header comment — codifying them in a generator is a 30-line script.

---

## 10. SEO practice maturity scorecard

A 1–5 score per practice area. 5 = best-in-class for the comparison set; 1 = significant gap.

| Practice area | NM peer set median | DC current | DC ceiling (after audit fixes) |
|---|---|---|---|
| Platform reliability | 4 | 3 | 4 |
| Schema breadth | 3 | **4** | **5** |
| Schema consistency across pages | 4 | 2 | 4 |
| Meta tag hygiene (titles, descriptions, canonicals) | 4 | 2 | 4 |
| OG / Twitter card hygiene | 4 | 3 | 4 |
| Page speed (script weight) | 3 | **5** | 5 |
| Page speed (CLS — image dimensions) | 4 | 1 | 4 |
| URL structure consistency | 4 | 2 | 4 |
| Internal linking integrity | 4 | 2 | 4 |
| Sitemap accuracy | 4 | 3 | 5 |
| Robots.txt correctness | 4 | 5 | 5 |
| Multilingual support | 3 (Spanish on ABQ/NM) | 1 (none) | 1 (out of scope) |
| Accessibility / WCAG | 3 | not measured | — |
| **Total / 60** | ~46 | ~33 | ~50 |

**Read the scorecard like this.** The peer set runs at a competent ~46/60 across the board — no peaks, no valleys, the typical CMS-based DMO experience. DC currently runs at ~33/60 because the meta-tag and image-dimension defects pull it down hard, but those are *defect-class* issues with mechanical fixes — not architectural problems. The ceiling for DC, if the May 1 audit findings are closed, is ~50/60, which would put it ahead of every peer in the comparison set on technical SEO.

The path from 33 to 50 is the audit punch list. Nothing on it requires a platform migration, a CMS, or new capabilities. It's all execution discipline on the platform that already exists.

---

## 11. Recommendations specific to platform and SEO practice

These are technical-execution recommendations, not content/positioning. They map to the existing audit and Big Plan.

**Tier 1 — fixes that close the gap to the peer set (do first, ~2 weeks of work)**

1. **Canonical sweep.** Rewrite all 40 mismatched canonicals to match each file's actual path. Decide once whether to ship pretty URLs (with `_redirects` / `.htaccess`) or accept literal `.html`. Map B1 + B6.
2. **Delete or `noindex` the six stub `*copy*.html` files.** B2 — three are byte-identical to the homepage's title and description.
3. **Generate `media/og-default.webp` (or `.jpg`) at 1200×630, plus `Index-24.webp` and `placeholder-hero-main.webp`.** B3 affects 46 pages of social previews.
4. **Sitemap regenerator script.** Walk disk, emit XML, exclude per the existing comment block. Replace hand-edited `sitemap.xml`. B4.
5. **Internal-link checker script.** Walk disk, validate every `<a href>` target. Fix the 167 broken links. The most-referenced broken targets (`stay/lodging.html` ×28, `do/complete-guide-to-activities.html` ×11) are renamed-file casualties — pick canonical filenames and `sed` site-wide. B5.
6. **Title and description trim script.** Walk disk, trim titles to ≤60 chars (drop ` | DiscoverCloudcroft.com` site-wide; Google appends site name automatically when configured via Schema), trim descriptions to ≤155. C1 + C2.

**Tier 2 — fixes that build on the platform's strength (next 2–4 weeks)**

7. **Image dimensions.** Python helper using PIL — read each referenced image, write `width=` and `height=` into every `<img>`. Closes the CLS gap. C4.
8. **Hero LCP preload on all 100 templates.** Per-page preload tag. C5.
9. **Add `defer` to `js/common.js` site-wide.** One `sed` line. C6.
10. **Fix the 12 entity-page schema URL/sameAs swaps.** Mechanical. C8.
11. **Add `geo` to entity-page schema.** Lat/lng per business address. C9.
12. **Add `BreadcrumbList` to the 12 guide pages that lack it.** C10.
13. **Self-host fonts per Master Plan §4.6.** Drop Google Fonts links from `<head>`, finish the `css/fonts.css` migration. Removes a render-blocking external dependency.

**Tier 3 — capabilities to add (next 30–90 days)**

14. **GTM container.** Replace the direct gtag.js install with GTM. Future-proofs adding pixels, custom events, A/B test scripts, and consent-mode without touching every page.
15. **Search Console → GA4 link.** Open task from the Apr 24 GA setup conversation. Without this, ranking data isn't visible inside GA4.
16. **CWV monitoring.** PageSpeed Insights API or Lighthouse CI run weekly against the top 10 pages, results saved to a `md/cwv-trend.md`. Catches regressions before they show up in Search Console's CWV report two months later.
17. **Schema generator helper.** A small Python lib that emits schema blocks from a YAML or JSON spec per page. Codifies the schema patterns from the rewritten complete-guide page so they propagate consistently. Closes the schema-consistency gap.

**What not to do**

- **Don't migrate to a CMS.** The peer set's CMS lock-in is a competitive disadvantage — DC's hand-rolled site is more performant and more schema-flexible. The audit defects are execution gaps, not platform gaps. Migrating to WordPress or Simpleview to "fix" them would lose the platform advantages and add vendor cost.
- **Don't add features the peer set has just because they have them.** Simpleview's CRM-CMS pipeline solves a problem (member-fee partner management) that DC doesn't have. A "partner dashboard" or "lead routing" build is months of work for no current revenue.
- **Don't optimize for mobile-app parity.** Visit Widget gives Simpleview tenants a mobile app for ~$30k/year. DC has no mobile app. That's fine; mobile-web on AWS-hosted static HTML can be excellent without an app shell.

---

## 12. Summary tables for skim-reading

**Where DC leads the comparison:**
- Schema breadth (6 entity types on the homepage)
- JavaScript weight (single `~400-line common.js` + gtag.js)
- Hosting flexibility (AWS / static / hand-rolled)
- robots.txt correctness

**Where DC matches the comparison:**
- HTTPS (universal)
- Mobile-friendliness (responsive design baseline)
- Site-search discoverability via SearchAction schema (most peers also have this)

**Where DC trails the comparison:**
- Meta-tag hygiene at the page level (titles, descriptions, canonical accuracy)
- Image-dimension consistency (469 of 486 missing — high CLS risk)
- Internal-link integrity (167 broken)
- Sitemap accuracy (1 fictional URL, 3 missing real pages)
- OG image asset availability (46 references to missing files)
- CMS-managed conveniences (event modules, partner directories, multilingual support)

**The competitive question for the next 90 days** is whether the audit punch list ships fast enough to convert the platform's potential into measurable Core Web Vitals and Search Console gains before the peer set's CMS-default polish keeps eating Cloudcroft's lunch on shoulder traffic.

---

*Last updated: May 6, 2026 · v1.0 · Companion to `competitive-analysis-2026-05-06.md`. Tech inferences for Simpleview-likely sites are pattern-matched from industry data; direct BuiltWith / Wappalyzer confirmation pending. DC findings are first-hand from `seo-audit-2026-05-01.md` and direct file inspection.*
