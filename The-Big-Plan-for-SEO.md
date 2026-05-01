# The Big Plan for SEO
**DiscoverCloudcroft.com — Launch & First 90 Days**
Version 1.1 · May 1, 2026 · Single source of truth for SEO decisions on this site.

> **What changed from v1.0 (April 24).** A full technical SEO audit of the live repo (`md/seo-audit-2026-05-01.md`, May 1, 2026) found defects v1.0 didn't have visibility into: 40 broken canonicals, 167 broken internal links, 46 pages referencing a missing OG image, 6 indexable stub HTML files, the homepage canonical pointing to a nonexistent URL, 469 of 486 `<img>` tags missing dimensions. Site health score: **58/100.** v1.1 folds those findings into §7.6 (technical-audit punch list, new) and reshuffles §14 (Monday-morning actions) so the audit's quick-wins go first.

---

## 0. Source Material Reconciled in This Memo

This plan consolidates every SEO document currently in `md/DC-SEO-Plan/` plus the May 1 audit at `md/seo-audit-2026-05-01.md`:

| File | Role in this plan |
|---|---|
| **`md/seo-audit-2026-05-01.md` (May 1, 2026) — NEW in v1.1** | **Ground-truth technical audit of the live repo. Drives §7.6 and reorders §14. P0/P1 findings supersede the more abstract gap table from v1.0 §7.2.** |
| `SEO-Master-Plan.md` (v1.0, April 2026) | Canonical strategy. Most decisions inherit from here. |
| `DiscoverCloudcroft-SEO-Memo.docx` / `.docx.pdf` | Executive framing, AI-search argument, advertising model. |
| `SEO-STRATEGY-MEMO.md` (January 2026) | Earlier tactical memo. Treated as superseded where it conflicts with the April material. |
| `MM-DC-Digital-Strategy.txt` | Two-domain (MountainMonthly + DiscoverCloudcroft) discipline. |
| `DC-SEO-Pages-Ideas.pdf` | 25-keyword list with target pages. |
| `DC-SEO-Launch-Strategy.pages` / `Discover-SEO-Memo.pages` | Apple Pages native format; not machine-readable in this pass. Material in those files appears to be captured in the `.md` and `.docx` equivalents above. If not, flag and I will re-synthesize. |
| `topic-pages-consistency-audit.md` (2026-04-19, repo root) | Used in v1.0 to ground recommendations in the site's actual divergence. Mostly superseded by the May 1 audit, retained for the consistency-scorecard breakdown of the seven topic pages. |

Where two sources disagree, this memo picks one answer and footnotes the alternative. Where sources prescribe something the current static HTML + `sync-nav.py` + `common.css` workflow can't easily support, this memo names the constraint rather than pretending it away. **Where the May 1 audit's specific file-by-file findings conflict with anything in the older strategy memos, the audit wins.**

---

## 1. Executive Summary

DiscoverCloudcroft.com exists to answer one question: *Should I go to Cloudcroft, and what do I do when I get there?* The audience is a traveler in trip-planning mode, not an arrived visitor and not a local news reader (per `SEO-Master-Plan.md` §1 and `DiscoverCloudcroft-SEO-Memo.docx`).

The strategic bet is velocity in the first 90 days. Cloudcroft has almost no authoritative digital travel content compared to Sedona, Taos, or Ruidoso. A locally operated site that fills that gap now can lock page-one rankings in months rather than years, and — more importantly for the next two years — become the source that ChatGPT, Perplexity, and Google's AI Overview cite when asked about Cloudcroft. That window closes as AI-generated travel content scales into smaller markets. We move now.

The goal is not ranking for 25 keywords. The goal is becoming the authoritative answer to every Cloudcroft visitor query, human or AI. Both source memos converge on an 18–24 month horizon for that position to lock in; the 90-day plan in §12 gets us on that trajectory.

---

## 2. Goals & KPIs

KPIs are pulled from `SEO-Master-Plan.md` §9 and `SEO-STRATEGY-MEMO.md` (both files list six-month rolling targets). Where the two disagree, the April Master Plan wins.

| Metric | Baseline | 6-month target | Source |
|---|---|---|---|
| Organic sessions / month | TBD at launch | +50% over baseline month 2 | STRATEGY-MEMO |
| Keywords ranking top-10 in GSC | 0 | 20 | STRATEGY-MEMO |
| Pages indexed | ~30 at launch | 40+ | STRATEGY-MEMO |
| Average GSC position | TBD | < 15 | STRATEGY-MEMO |
| CTR (sitewide) | TBD | > 3% | STRATEGY-MEMO |
| Cited by at least one AI answer engine for a non-brand Cloudcroft query | No | Yes | derived from `DiscoverCloudcroft-SEO-Memo` |

Two non-numeric goals the memos insist on and that I am keeping in:

- **Own the regional feeder market.** El Paso, Alamogordo, Las Cruces, Albuquerque, Roswell. National traffic is not the prize (`DiscoverCloudcroft-SEO-Memo.docx`, "Geographic Advantage").
- **Be the site AI cites.** Structured, named, dated, updated. Details in §6 (AI-search optimization is embedded in the on-page standards, per `SEO-Master-Plan.md` §6).

**Open question:** We do not yet have a traffic baseline because the site has not been submitted to Google Search Console under the production domain. Week 1, Day 1 task.

---

## 3. Target Audience & Search Intent

One audience: trip-planning travelers, pre-booking. Four intents we build for, all visitor-side:

1. **Exploratory** — "is Cloudcroft worth it?" → Complete Guide, hero pages.
2. **Seasonal** — "cloudcroft fall colors," "cloudcroft christmas" → evergreen seasonal guides refreshed annually.
3. **Commercial** — "cabins in cloudcroft nm," "romantic cabins cloudcroft nm" → lodging directory and entity pages.
4. **Logistics** — "how far is cloudcroft from el paso," "cloudcroft elevation," "cloudcroft weather" → FAQ + day-trip landing pages.

News / civic / real-estate searches are explicitly **not** this site's lane. They belong to MountainMonthly.com and The Cloudcroft Reader (`MM-DC-Digital-Strategy.txt`, §1). See §6 for the non-cannibalization rule.

---

## 4. Keyword Strategy

The 25-keyword list in `DC-SEO-Pages-Ideas.pdf` and the expanded map in `SEO-Master-Plan.md` §3 are consistent. I'm using the Master Plan's six-category structure because it adds the day-trip feeder category the 25-keyword list doesn't.

Volume estimates below are carried through from `SEO-STRATEGY-MEMO.md` §"Target Keyword Strategy" and are explicitly labeled "Est." in that source. Treat them as directional until we pull real numbers from Ahrefs/Semrush in Week 1.

### 4.1 Primary keyword → page owner map

| Category | Primary keywords | Target page (owner) | Notes |
|---|---|---|---|
| Core travel | things to do in cloudcroft nm; cloudcroft new mexico travel guide; what to do in cloudcroft new mexico; weekend trip to cloudcroft nm | `complete-guide-to-cloudcroft-new-mexico-2026.html` | **Already exists in repo.** One page, 10+ keywords — per `DiscoverCloudcroft-SEO-Memo`, the single highest-leverage asset. |
| Brand / location | cloudcroft nm (est. 8,000–12,000/mo); cloudcroft new mexico (est. 4,000–6,000/mo) | `index.html` | Homepage. |
| Seasonal | cloudcroft fall colors / fall foliage; cloudcroft christmas events; cloudcroft summer events; cloudcroft winter activities; cloudcroft spring hiking | `season/fall-colors.html`, `season/christmas.html`, `season/summer.html`, `season/winter.html`, `season/spring.html` | Build **60–90 days ahead** of each peak (`SEO-Master-Plan.md` §3.2, §10.3; corroborated by `MM-DC-Digital-Strategy.txt` §6). Refresh annually on the same URL. |
| Outdoor | cloudcroft hiking trails; best hikes near cloudcroft nm; cloudcroft mountain biking trails; cloudcroft camping guide; sacramento mountains hiking; stargazing cloudcroft / cloudcroft dark sky | `do/guide-to-hiking-…` (exists), `do/guide-to-camping-…` (exists), `do/complete-guide-to-activities-…` (exists), `do/mountain-biking.html`, `do/stargazing.html` | Individual trail pages (Osha, Rim, Trestle) added over 12–18 months. |
| Lodging (highest commercial intent) | cabins in cloudcroft nm; cloudcroft nm lodging guide; places to stay in cloudcroft; best cabins in cloudcroft nm; romantic cabins cloudcroft nm; pet friendly cabins cloudcroft nm; cloudcroft cabin rentals with hot tub; lodging near cloudcroft new mexico | `stay/complete-guide-to-lodging-…` (exists) + individual entity pages | Highest ad revenue potential — this is where "directory" monetization lives. |
| Food & town | best restaurants in cloudcroft nm; cloudcroft coffee shops; cloudcroft breweries; cloudcroft shopping guide; burro avenue cloudcroft shops; bbq cloudcroft new mexico; cloudcroft breakfast spots; dog friendly restaurants cloudcroft | `eat/complete-guide-where-to-eat-…` (exists), `shop/complete-guide-where-to-shop-…` (exists), `shop/burro-avenue-walking-guide.html` | List pages rank well for this category per both April memos. |
| Day-trip feeders | el paso to cloudcroft; day trip from el paso to cloudcroft; albuquerque to cloudcroft; roswell to cloudcroft; alamogordo to cloudcroft; las cruces to cloudcroft; how far is cloudcroft from el paso; white sands cloudcroft | `visit/from-el-paso.html`, `visit/from-albuquerque.html`, `visit/from-alamogordo.html`, `visit/from-las-cruces.html`, `visit/from-roswell.html`, `visit/white-sands-cloudcroft.html` | El Paso and Albuquerque first (largest metros). |
| Logistics / FAQ | cloudcroft weather; cloudcroft elevation; how far is cloudcroft from el paso | `resources/faq.html` and inline FAQ schema on Complete Guide | FAQ schema is a Rich Results win. |

### 4.2 Rule: every page has exactly one primary keyword owner

From `SEO-Master-Plan.md` §3 and §15: *"Every page gets a keyword owner before it ships."* A page without a logged primary keyword does not pass audit. We keep a keyword map (spreadsheet or a tracked `md/keyword-map.md` file) and check it before drafting any new page.

### 4.3 Conflict note — keyword volumes

`SEO-STRATEGY-MEMO.md` offers volume estimates; `SEO-Master-Plan.md` and the April executive memo do not. The January numbers are labeled estimates and we treat them as such. **Action:** pull real volumes from Ahrefs or Semrush in Week 1 (budget for this is in `SEO-Master-Plan.md` §14: $100–$200/month).

---

## 5. On-Page SEO Standards

This is the contract every page ships against. Every bullet here is a "No" in the §13 audit checklist of `SEO-Master-Plan.md` if missing.

### 5.1 HEAD ordering (hard requirement — already in CLAUDE.md)

1. `<meta charset>`
2. `<title>` — 50–60 chars, primary keyword near the front, brand at end.
3. `<meta name="description">` — 150–160 chars, unique to the page, click-compelling.
4. `<link rel="canonical">` — pointing at the production `https://discovercloudcroft.com/<slug>` URL.
5. Open Graph block (title, description, image, url, type).
6. Twitter Card block.
7. Fonts (self-hosted `css/fonts.css` + Google Fonts preconnect, matching existing pattern).
8. `css/common.css`.
9. JSON-LD Schema.org block.
10. Inline page-specific `<style>`.

The homepage and every entity page I spot-checked already follow this (`index.html`, `eat/black-bear-coffee-shop.html`). The gap is **consistency across the seven complete-guide pages**, which `topic-pages-consistency-audit.md` (April 19, 2026) documents in detail — broken font stack on MAIN, `og:type=website` on pages that should be `article`, broken subpage nav paths on STAY, divergent schema types. That audit is the on-page punch list for Week 1.

### 5.2 Title / meta templates (copy-pasteable)

**Entity pages (restaurants, cabins, shops, attractions):**
```
<title>{Name}, Cloudcroft NM — {One-line differentiator} | DiscoverCloudcroft.com</title>
<meta name="description" content="{Name} in Cloudcroft, NM. {Two-sentence summary of what it is, why it matters, and a named local detail (street, trail, neighbor). 150–160 chars total}.">
```

**Topic / guide pages:**
```
<title>{Primary keyword, Title Case} ({Year}) | Cloudcroft, NM | DiscoverCloudcroft.com</title>
<meta name="description" content="{What the guide covers} — {the distinct local angle} — {who it is for}. Updated {Month Year}.">
```

**Seasonal pages:**
```
<title>Cloudcroft {Season} Guide ({Year}) — {Anchor detail, e.g. Aspen Peak, Christmas Events, Snow Report} | DiscoverCloudcroft.com</title>
<meta name="description" content="{When the season peaks} in Cloudcroft, NM. {What to do / see}, {where to stay}, {what to know}. Updated {Month Year}.">
```

**Day-trip pages:**
```
<title>{Origin City} to Cloudcroft — Day Trip & Weekend Guide | DiscoverCloudcroft.com</title>
<meta name="description" content="How to get to Cloudcroft from {Origin City} ({miles} miles, ~{time}). Best stops, what to do when you arrive, where to stay overnight.">
```

The "{Year}" in titles matters — `DiscoverCloudcroft-SEO-Memo.docx` explicitly argues dated titles outperform undated on CTR. Update annually on the same URL.

### 5.3 JSON-LD schema stubs (already established patterns in the repo)

Schema type by page category (matched to what I observed in the repo and to `SEO-Master-Plan.md` §4.3):

| Page type | Primary schema | Additional |
|---|---|---|
| Homepage | `TouristDestination` | `WebSite` with `potentialAction` SearchAction |
| Complete Guide (main) | `TouristDestination` + `FAQPage` + `BreadcrumbList` | Already present per the audit — keep this pattern |
| Complete Guide (section: eat, stay, do, shop) | `Article` + `BreadcrumbList` | Audit shows this is consistent across SHOP/DO/STAY/EAT |
| Lodging entity | `LodgingBusiness` (or `Hotel`, `VacationRental` as subtype fits) | `BreadcrumbList`, `geo` with lat/lon |
| Restaurant / coffee entity | `Restaurant` or `CafeOrCoffeeShop` (as used on Black Bear) | `BreadcrumbList`, `geo`, `priceRange`, `servesCuisine` |
| Shop / retail entity | `LocalBusiness` or `Store` | `BreadcrumbList`, `geo` |
| Trail / attraction entity | `TouristAttraction` | `BreadcrumbList`, `geo` |
| Event | `Event` | `location`, `startDate`, `endDate` |
| Season / seasonal guide | `Article` | `BreadcrumbList`, `about` pointing at TouristDestination |
| FAQ | `FAQPage` | — |

`SEO-Master-Plan.md` §4.3 requires **BreadcrumbList schema on every page**. That is not yet universal in the repo. Add it to `common.css` adjacent — i.e., treat the breadcrumb script as a shared component, templated from the page's directory depth, injected by a small build script (see §13 open questions).

### 5.4 Content structure requirements

Directly from `SEO-Master-Plan.md` §5:

- One `<h1>` per page, contains the primary keyword.
- 2–4 `<h2>` using secondary keywords.
- Word-count floors: 300 (utility), 800–1,500 (category/landing), 2,000+ (flagship). The Complete Guide should be north of 2,000.
- TL;DR or "Quick Facts" block near the top on guides over 1,000 words — **this is the AI-search lever**. AI extracts answers from formatted blocks; wall-of-prose pages get ignored or misquoted.
- Named entities in every page: specific trails (Osha, Rim, Trestle), streets (Burro Avenue, US-82), businesses (The Lodge at Cloudcroft, Mad Jack's), events (Aspenfest), geography (Sacramento Mountains, Lincoln National Forest, Sunspot). Generic travel copy is a fail.
- "Updated {Month Year}" visible on evergreen pages.
- E-E-A-T: first-person voice where appropriate, author bylines with local bio, original dated photos (stock imagery is banned on editorial pages per §5.3).

### 5.5 Images

Every image: descriptive filename (`osha-trail-fall-aspens.webp`, not `IMG_4021.jpg`), descriptive alt text, WebP/AVIF, explicit width/height to prevent CLS, lazy-loaded below fold. OG image 1200 × 630, per-page where the page warrants it, otherwise the `media/og-default.webp` fallback already in `index.html`.

### 5.6 Conflict note — elevation in hero copy

`SEO-STRATEGY-MEMO.md` Section "Technical SEO Recommendations → Example for homepage" uses **8,663 feet**. The current `index.html` uses **9,000 feet** in six places (meta description, OG description, Twitter description, JSON-LD description, hero image alt text, and the H1). The April Master Plan does not specify a number. This is a factual discrepancy in our own source material. **Action:** resolve to one canonical number (verify against Village of Cloudcroft official data or USGS), then find-and-replace sitewide. Until resolved, don't publish new pages that repeat either number.

---

## 6. Site Architecture & Internal Linking

### 6.1 The hub-and-spoke we actually have

Source memos describe hubs as `/activities/`, `/lodging/`, `/dining/`. The **actual repo** uses `/do/`, `/stay/`, `/eat/`, `/shop/`, plus `/visit/`, `/season/`, `/events/`, `/resources/`, `/about/`. Keep the existing URLs. Changing established URLs after publish is a hard rule violation in `SEO-Master-Plan.md` §4.1.

```
HOMEPAGE (/)
├── /complete-guide-to-cloudcroft-new-mexico-2026.html   (MAIN GUIDE — flagship)
├── /do/        (Activities hub)
│     ├── /do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html
│     ├── /do/guide-to-hiking-in-cloudcroft-new-mexico-2026.html
│     ├── /do/guide-to-camping-cloudcroft-new-mexico-2026.html
│     └── individual trail / attraction pages
├── /stay/      (Lodging hub — highest commercial intent)
│     ├── /stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html
│     └── individual cabins / hotels
├── /eat/       (Dining hub)
│     ├── /eat/complete-guide-where-to-eat-in-cloudcroft-2026.html
│     └── individual restaurants / cafes
├── /shop/      (Retail hub + Burro Avenue walking guide)
├── /visit/     (Day-trip feeders: El Paso, Albuquerque, etc.)
├── /season/    (Fall, Winter, Spring, Summer, Christmas)
├── /events/    (Events calendar — also the repeat-traffic lever)
├── /resources/ (FAQ, weather, elevation, how-far-is-X)
└── /about/     (E-E-A-T: editorial policy, author bios)
```

### 6.2 Linking rules (from `SEO-Master-Plan.md` §5.4)

- Every leaf links up to its hub. Every hub links down to its children.
- Every page carries ≥ 3 internal links to related content, not counting nav/footer.
- Anchor text is natural and descriptive. No "click here." No repeated exact-match anchors sitewide.
- Cross-category links are encouraged where real: hiking → pet-friendly dining, dark-skies → lodging, shopping → dining on Burro.
- Every page carries ≥ 1 authoritative outbound link where relevant (Lincoln National Forest, NM Tourism, NOAA, AllTrails).
- No affiliate / paid outbound in editorial without disclosure.

### 6.3 Two-domain discipline (`MM-DC-Digital-Strategy.txt`)

DiscoverCloudcroft.com and MountainMonthly.com are adjacent properties, both owned here. The rules are load-bearing:

1. **No duplicate content across domains.** Google will split authority or suppress one.
2. **Every high-value keyword has one domain owner.** Logged in the keyword map before publishing.
3. **MountainMonthly earns links through journalism; DiscoverCloudcroft consumes that authority via deliberate internal links** — e.g., a MountainMonthly feature on Burro Avenue's history links to the DiscoverCloudcroft Burro Avenue Walking Guide; the Walking Guide links back to the feature for context.
4. **Natural anchor text both ways.** No keyword stuffing across the bridge.

`MM-DC-Digital-Strategy.txt` §11 recommends **Option B: authority stack** — Mountain Monthly as the journalistic authority feeding Discover Cloudcroft as the commercial tourism arm. That's the operating posture.

### 6.4 Nav sync

CLAUDE.md is explicit: the top nav is duplicated into every HTML file and must **not** be hand-edited per page. Edit `content/sync-nav.py` and run it. Any SEO recommendation that changes the nav is a one-line change in `build_nav`, then the sync. This is a constraint for any new hub-and-spoke change proposed here.

---

## 7. Technical SEO

### 7.1 Already in place (verified in the repo)

- `robots.txt` at root allows full crawl; sitemap is referenced.
- `sitemap.xml` at root with the hubs, main guide, and homepage (367 lines at last check).
- Canonical, OG, Twitter, JSON-LD on homepage and the entity pages I spot-checked.
- Self-hosted fonts via `css/fonts.css`.

### 7.2 Gaps to close before/at launch (high-level)

This table was the v1.0 view. **Superseded by §7.6 below**, which is the file-counted, P0/P1-classified punch list from the May 1 audit. Keep this table only for the GSC/Bing/GA4 plumbing items, which the audit doesn't repeat:

| Gap | Where | Owner | Deadline |
|---|---|---|---|
| GSC property not verified against production domain | DNS | Chris | Week 1 Day 1 |
| Bing Webmaster Tools not set up | Bing | Chris | Week 1 |
| GA4 property not confirmed connected to GSC | GA4 + GSC | Chris | Week 1 |
| Elevation discrepancy (9,000 vs 8,663) | sitewide | editorial | Week 1 |

Everything else from the v1.0 gap table (BreadcrumbList universalization, broken font on MAIN, STAY nav paths, `og:type=website` on guides, per-page OG images) is captured with more precise scope in §7.6.

### 7.3 Core Web Vitals targets (non-negotiable)

- LCP < 2.5s
- CLS < 0.1
- INP < 200ms

**Conflict note:** `SEO-STRATEGY-MEMO.md` lists **First Input Delay (FID) < 100ms**. Google replaced FID with INP (Interaction to Next Paint) as a Core Web Vital on March 12, 2024. The Master Plan's INP < 200ms is current and correct. Use INP.

Verified with Lighthouse and PageSpeed Insights before any page indexes. CWV failures block publish.

### 7.4 Performance rules

- WebP/AVIF images, compressed, lazy-loaded below fold, explicit width/height.
- CSS minified. JS deferred for anything non-critical. (`js/common.js` is fine to load normally; anything added should be deferred.)
- Cloudflare (or equivalent) CDN fronts the site from day one — explicitly called out in `SEO-Master-Plan.md` §4.6 because edge caching matters for the El Paso / Albuquerque / Las Cruces feeder markets.
- Browser cache headers on static assets.

### 7.5 Indexing & submission

- Submit `sitemap.xml` to GSC and Bing the moment the site goes live.
- Manually request indexing of the top 10 pages via GSC URL Inspection on Day 1.
- `<meta name="robots" content="index,follow">` explicit on every page (Master Plan §4.2).

### 7.6 Technical-audit punch list (May 1, 2026 audit)

Source: `md/seo-audit-2026-05-01.md`. Files reviewed: 108 HTML files plus `css/`, `js/`, `robots.txt`, `sitemap.xml`. Worktree copies excluded. **Site health: 58/100.** Architecture is right; the metadata layer is leaking value.

#### P0 — actively block indexing or send Google the wrong signal

| ID | Issue | Count | Fix | Owner | Deadline |
|---|---|---|---|---|---|
| **B1** | Canonical points to a URL that doesn't exist on disk | **40 pages** (38% of indexable surface) — `do/golf.html` → `/do/where-to-play-golf-in-cloudcroft-2026.html`, `do/camp.html` → `/do/best-camping.html`, all 6 `season/*`, all `events/event-*`, etc. | Script across the 40 affected files: rewrite each `<link rel="canonical">` to its actual filename. Or ship a server rewrite (`.htaccess` / Netlify `_redirects`) for the pretty URL targets. | dev | Week 1 |
| **B2** | Six legacy duplicate / stub HTML files indexable; three share the homepage's title and description | `complete-guide-to-cloudcroft-new-mexico-2026 copy.html`, `…copy 2.html`, `index copy.html`, `do/complete-guide-to-activities-to-do-in-cloudcroft-2026 copy.html`, `stay/xxx-complete-guide-to-lodging-in-cloudcroft-new-mexico-2026 copy.html`, `topic-page-target-mockup.html` | **Delete all six** (cleanest). Otherwise add `<meta name="robots" content="noindex,nofollow">` and `Disallow:` in `robots.txt`. | dev | Week 1 Day 1 |
| **B3** | OG image referenced doesn't exist on disk | **46 pages** point to `media/og-default.webp` which is missing. 11 more reference `media/Index-24.webp` and `media/placeholder-hero-main.webp`, also missing. | Create `media/og-default.webp` at 1200×630, plus the two other missing assets. Verify by visiting the URLs after deploy. | design + dev | Week 1 |
| **B4** | Sitemap and on-disk file list are out of sync | `sitemap.xml` lists `/complete-guide-to-cloudcroft-new-mexico-2026.html` (file doesn't exist — homepage is `index.html` and canonicals to that fictional URL). Three real public pages NOT in sitemap: `shop/elk-shed.html`, `shop/turquoise.html`, `stay/stay-osha-trail.html`. | Drop the fictional entry, add the three missing pages. Best handled by a build script that emits `sitemap.xml` from the file tree. | dev | Week 1 |
| **B5** | Internal links to files that don't exist | **167 broken links.** Top offenders: `stay/lodging.html` (28 refs), `do/complete-guide-to-activities.html` (11 refs), `where to-hike-in-Cloudcroft-New-Mexico-2026.html` (8 refs — note literal space + capitals). Source files: `season/seasonal.html` (16 broken), `shelf/index-hold.html` (19), `footer-stuff.html` (11). | Site-wide find/replace for the top 5 broken targets resolves ~40 of 167. Then add `content/check-internal-links.py` to gate publishes. | dev | Weeks 1–2 |
| **B6** | `index.html` canonical points to a different URL than the page itself | Canonical = `https://discovercloudcroft.com/complete-guide-to-cloudcroft-new-mexico-2026.html`. Site homepage is `/`. No rewrite configured. Google may deindex `/`. | Set `index.html` canonical to `https://discovercloudcroft.com/`. Drop the fictional sitemap entry (B4). Or ship a 301 from `/complete-guide-…` to `/`. | dev | Week 1 Day 1 |

#### P1 — high priority, ship in Weeks 1–3

| ID | Issue | Count | Fix |
|---|---|---|---|
| **C1** | `<title>` over Google's ~60-char SERP cutoff | 87 of 106 pages (median 85, max 150) | Drop ` \| DiscoverCloudcroft.com` from titles (Google often appends site name automatically). Trim taglines. Aim 50–60 chars including geo. |
| **C2** | `<meta name="description">` over 160 chars | 83 pages; 44 over 200; max 313 | Tighten to 140–155. One CTA verb + one differentiator + geo. Scriptable. |
| **C3** | Homepage missing `Organization`, `WebSite`, and `SearchAction` schema | `index.html` | Add a 4th JSON-LD block: `Organization` (logo + `sameAs` socials + `contactPoint`) and `WebSite` (with `potentialAction: SearchAction`). Loses sitelinks search-box without it. |
| **C4** | `<img>` tags missing `width` and `height` | 469 of 486 (CLS risk) | Python helper using PIL to read each referenced image and inject intrinsic dimensions. Or set CSS `aspect-ratio` on wrappers. |
| **C5** | Hero image not preloaded | 100 of 108 pages | `<link rel="preload" as="image" href="…hero…" fetchpriority="high">` per template. |
| **C6** | `js/common.js` not deferred | 84 of 108 pages | One-line `sed`: add `defer` to the `<script src="…common.js">` tag site-wide. |
| **C7** | Duplicate IDs (`mobile-nav`, sometimes `menu`) | 12 pages including `do/complete-guide-to-activities-…`, `eat/big-daddys.html`, `eat/complete-guide-where-to-eat-…`, `shop/burro-ave-trading-post.html`, `shop/aspen-and-ivy.html`, `visit/where-to-visit.html`, etc. | Fix in `content/sync-nav.py` so it can never re-introduce a duplicate `mobile-nav` block. |
| **C8** | Entity JSON-LD `"url"` points to third-party site instead of the on-site canonical | 12 entity pages, all under `stay/` plus `do/guide-lincoln-national-forest-…`, `do/guide-to-hiking-…`, `eat/noisy-water-winery.html`. (`eat/black-bear-coffee-shop.html` has the correct pattern — copy it.) | Set `"url"` to the on-site canonical; move third-party domains into `sameAs`. |
| **C9** | Entity JSON-LD missing `geo` (lat/lng) | 55 entity pages | Add `geo` per entity from the actual address. Skip `aggregateRating` until first-party reviews exist (Google now penalizes self-serving). |
| **C10** | Guide pages missing `BreadcrumbList` schema | 12 guide pages including the four section complete-guides + the auto-services guide | 3-item BreadcrumbList per guide (Home → Section → Guide). Best implemented via a small injection script keyed on directory depth. |
| **C11** | `<img>` references to HEIC files (Chrome/Firefox can't render) | 5 references — 4 of them on `index.html` | Convert to `.jpg`/`.webp` via the existing `optimize-images.sh` pattern; update HTML refs. |
| **C12** | Broken `<img src>` references | 39, after URL-decoding and case-folding | Most are typos (`do/camp.html`'s `camp-00756.jpg.webp`) or stale paths. Build-time link checker. |
| **C13** | Case-only image filename mismatches | 9, all in eighteen99 / Black Bear lodge-plates series | Rename source files to canonical lowercase or update HTML refs. Will 404 on case-sensitive prod servers (Linux/CDNs). |
| **C14** | `<meta name="keywords">` present | 100 pages | Remove site-wide. Google ignored it since 2009; Bing treats excessive use as a quality-signal proxy (down-rank). |
| **C15** | Pages missing OG essentials (`og:image`, `og:url`, etc.) | 7 pages including `about/terms.html`, `about/privacy.html`, `stay/stay-spruce-cabins.html`, `resources/zenith-park-in-cloudcroft.html` | Privacy/terms still need OG basics. The `topic-page-target-mockup.html` and `shelf/*` files should be removed or noindexed (B2 / D1). |

#### P2 — medium priority, ship Weeks 3–6

`shelf/cloudcroft-review.html` exposed without noindex (D1). Inline `<style>` blocks of 20–30 KB on 10 guide pages — run `content/strip-duplicate-css.py` and `content/strip-guide-css.py` (D2). 11 pages don't mention "Cloudcroft, NM" at all (D3). 9 pages don't load `css/common.css` (D4). 4 inconsistent `viewport` meta forms (D5). 2 heading-level skips (D6). One URL with capital letter (`stay/stay-the-summit-inn-Cloudcroft-2026.html`) — rename + 301 redirect (D7). 5 thin pages under 300 words — `season/seasonal.html` is the worst, sitting at sitemap priority 0.9 with 204 words (D8). 360 image files >1 MB on disk; 309 >2 MB; one `.MOV` and one `.tif` in `media/` — run `optimize-images.sh` against every section photo dir (D9). 25 images missing `loading=` (D10). 10 imgs missing `alt` (all in the duplicate file slated for deletion, D11). Search Console verification file exposed without `noindex` (D12). Only 13 pages carry `dateModified` / `datePublished` — add to every entity JSON-LD (D13).

#### Quick-win punch list (10 highest impact-to-effort, ranked by the audit)

This is the audit's recommended ordering. **Adopted as the v1.1 launch-week sequence.**

1. **Delete the six duplicate/stub HTML files** (B2 + D14, E7).
2. **Create `media/og-default.webp` (1200×630)** plus the two other missing assets (B3).
3. **Fix `index.html`'s canonical** to `https://discovercloudcroft.com/`. Drop the fictional sitemap entry (B6 + half of B4).
4. **Script the 40 mismatched canonicals** to point to actual filenames (B1).
5. **Run `content/strip-duplicate-css.py` and `content/strip-guide-css.py`** (D2).
6. **Add `Organization`, `WebSite` (with `SearchAction`) JSON-LD to `index.html`** (C3).
7. **Tighten 87 titles + 83 descriptions** with one find/replace pattern (drop ` \| DiscoverCloudcroft.com`; trim descriptions ≤155 chars) (C1, C2).
8. **Add `width` + `height` to every `<img>`** via PIL helper (C4).
9. **Site-wide find/replace** of the top broken link targets (`stay/lodging.html`, `do/complete-guide-to-activities.html`, the typo'd hike URL) — resolves ~40 of 167 (B5).
10. **Fix the 12 entity pages** whose schema `"url"` points externally — copy the `eat/black-bear-coffee-shop.html` pattern (C8).

#### Things already good (preserve)

`robots.txt` is permissive and sitemap-aware. 99 of 108 pages have valid JSON-LD — none parse-fail. `<html lang="en">` set on every real page. `fonts.css` uses self-hosted woff2 with `font-display: swap`. Word count median is well above the thin-content floor; only 5 pages under 300 words and 3 of those are non-public. The duplicate / case-mismatch issues are concentrated — 60% of broken-link refs come from 5 files; 75% of HEIC refs come from `index.html` alone. Means most fixes are one-shot find/replace, not 100 individual edits.

---

## 8. AI-Search Optimization

This is the single most strategically important section of the plan. Pulled directly from `DiscoverCloudcroft-SEO-Memo.docx` "Impact on AI-Generated Search" and `SEO-Master-Plan.md` §6.

Build every page as if an AI will read it and decide whether to cite it. Four rules:

1. **Comprehensive answers.** One page that covers multiple related questions beats three thin pages. The Complete Guide is shaped this way on purpose.
2. **Named entities over generic keywords.** Consistent references to specific trails, streets, businesses, events build topical authority an AI can anchor on.
3. **Recency and update frequency.** Fall color guide refreshed every August. Events calendar updated quarterly minimum. Static brochure sites do not get cited.
4. **Structured content.** Headings, tables, FAQ blocks, TL;DRs. AI extracts from formatting; it ignores undifferentiated prose.

**First-mover window:** Cloudcroft has almost no authoritative digital travel content compared to larger destinations. AI models reflect that gap. A site that fills it now gets cited because there is nothing better to cite. The window closes as AI-generated content scales into smaller markets. That is the operating deadline.

Practical implication for every page: the writing standard that ranks well in Google ranks well in AI. They are not two strategies. This is the same strategy.

---

## 9. Content Production Roadmap (What to Write, In What Order)

From `SEO-Master-Plan.md` §10.1 and corroborated by `DiscoverCloudcroft-SEO-Memo.docx` "Launch Sequence":

1. **Complete Guide to Visiting Cloudcroft, New Mexico (2026)** — *already exists.* Audit pass + broken font fix + per-page OG image + `og:type=article` correction = Week 1.
2. **Lodging Directory** — highest commercial intent, attracts advertising. `stay/complete-guide-to-lodging-…` exists; audit pass + subpage nav path fix + directory-ready layout = Weeks 1–2.
3. **Hub pages: Things To Do, Where To Stay, Where To Eat** — `do/`, `stay/`, `eat/` complete guides exist; audit them against the on-page standard in §5 and close gaps.
4. **Seasonal pages, built 60–90 days ahead of peak.** At current date (April 24, 2026), the urgent one is **Summer** (school-out searches start May, peak July) and **Fall Colors** (peaks late September — start drafting in July). Winter/Christmas follows.
5. **Day-trip landing pages.** El Paso first (largest feeder), then Albuquerque. Add Alamogordo, Las Cruces, Roswell by end of Q3.
6. **Individual entity pages** — cabins, restaurants, shops, trails — filled in over 12–18 months at 2–3 substantial pieces per week for the first 90 days, then 1–2 per week.
7. **Link-bait content** (build to earn links, not to rank):
   - A Sacramento Mountains Fall Foliage map — visual, shareable.
   - An annual "Best of Cloudcroft" list — local businesses share and link.
   - The definitive Travel Guide (already = the Complete Guide).

---

## 10. Local SEO

Unambiguous across sources.

### 10.1 Google Business Profile

Claim/create a GBP for DiscoverCloudcroft.com under "Travel & Tourism" / "Destination." Fill every field — hours, description (keywords used naturally), photos, Q&A. Post weekly: events, seasonal content, new articles. GBP posts index fast and appear in SERPs (`SEO-Master-Plan.md` §7.1).

### 10.2 Citations & NAP

Same Name / Address / Phone format across:

- TripAdvisor (critical for travel)
- Yelp
- Foursquare / Apple Maps
- New Mexico True (state tourism)
- New Mexico Tourism Department directory
- Otero County tourism resources
- Visit Alamogordo (regional)
- AllTrails
- Roadtrippers
- TravelNM.com
- AAA travel guides

### 10.3 Backlink targets

Ranked for quality, not volume (`SEO-Master-Plan.md` §7.3):

1. New Mexico Tourism Department — a `.gov` link is gold.
2. Cloudcroft Chamber of Commerce.
3. Otero County visitor resources.
4. Lincoln National Forest official site.
5. Sunspot Solar Observatory.
6. Albuquerque Journal / El Paso Times / Las Cruces Sun-News travel sections — pitch seasonal travel stories.
7. AllTrails — submit or get editorially featured.
8. New Mexico True campaign — submit for inclusion.
9. **MountainMonthly.com** and **The Cloudcroft Reader** — owned; link intentionally from relevant stories.
10. Regional travel bloggers — press kit, comp stays with partner businesses, guest post exchange.

---

## 11. Measurement & Tooling

### 11.1 Stack

- **GA4** with enhanced measurement.
- **Google Search Console** — connected to GA4 for integrated data.
- **Bing Webmaster Tools.**
- **Lighthouse + PageSpeed Insights** run on every new page before index.
- **Ahrefs or Semrush** — one of the two, $100–$200/mo (`SEO-Master-Plan.md` §14). Decision: **start with Ahrefs** for backlink analysis given our link-building focus; can swap if the Semrush keyword tooling ends up more useful at Month 2.

### 11.2 Queries to track monthly in GSC (from `SEO-Master-Plan.md` §9.3)

- `cloudcroft` (brand)
- `cloudcroft nm` (location)
- `things to do cloudcroft` (activities)
- `cloudcroft cabins` (lodging)
- `cloudcroft restaurants` (dining)
- `cloudcroft fall colors` (seasonal)
- `day trip from el paso to cloudcroft` (feeder)

### 11.3 Monthly reporting cadence

One page in `md/` — `seo-monthly-{YYYY-MM}.md` — with: positions and impressions for the seven tracked queries, top 10 gainers/losers, indexed page count, CWV scorecard, new backlinks, link-building actions, decisions carried into next month.

---

## 12. 90-Day Launch Plan

Directly adapted from `SEO-Master-Plan.md` §10.2. Week 1 starts on launch day, not today — so if we launch May 1, Week 1 is May 1–7.

### Weeks 1–2: Foundation
- Verify GSC + Bing Webmaster Tools against production domain; submit sitemap.
- Fix all items in §7.2 gap table (the seven-page complete-guide audit punch list).
- Resolve elevation discrepancy sitewide.
- Add BreadcrumbList schema site-wide via shared injection.
- Publish: homepage, 3 hub pages (Things To Do, Where To Stay, Where To Eat), the Complete Guide, the Lodging Directory.
- Implement per-page OG images for the 7 flagship pages.
- Set up GBP listing and fill every field.
- Submit to NM Tourism Department directory.
- Full-site Lighthouse pass — fix any CWV failures before indexing picks up.
- Email the pre-launch subscriber list on launch day (traffic signal to Google).

### Weeks 3–4: Content velocity
- 2 day-trip landing pages (El Paso, Albuquerque).
- 3 activity guides (top hiking, summer, stargazing / dark sky).
- Internal linking audit — every page links to ≥ 3 others with natural anchor text.
- Reach out to Chamber of Commerce and Otero County for directory links.
- Begin outreach to New Mexico True for inclusion.
- Keyword map (`md/keyword-map.md`) committed to repo; every published page logged.

### Weeks 5–8: Authority building
- 2–3 substantial pieces per week.
- Prioritize seasonal content relevant in the next 60 days (Summer Events, early Fall Colors draft).
- Pitch 5 NM travel bloggers.
- Publish or refresh the definitive Cloudcroft Travel Guide as the linkable asset.
- Weekly GBP posts.
- Link intentionally from MountainMonthly.com and The Cloudcroft Reader where a relevant story exists.

### Weeks 9–12: Gap analysis & acceleration
- Pull GSC data: which queries have impressions but low clicks? Rewrite titles/metas.
- `site:visitcloudcroft.com` search to find gaps we haven't covered.
- Publish event-specific pages for Cloudcroft events in the next 6 months.
- Remaining day-trip pages (Roswell, Alamogordo, Las Cruces).
- Pitch El Paso and Albuquerque media seasonal travel stories (fall colors angle works for September placement).

### Ongoing after Day 90
- 1–2 substantial pieces per week.
- Every seasonal page refreshed annually on the same URL.
- Events calendar updated quarterly at minimum.
- Monthly GSC review (§11.3).
- Annual Complete Guide update — new year in title, refreshed content, same URL.

---

## 13. Open Questions & Risks

These are the decisions not fully resolved in the source material:

1. **URL structure discrepancy.** `SEO-Master-Plan.md` §4.1 shows clean trailing-slash URLs (`/things-to-do/hiking-cloudcroft-nm/`). The repo uses `.html` files in kebab-case directories. Both are fine for SEO; the rule that matters is "URL never changes after publish," which we follow by keeping the existing `.html` pattern. **No action — but do not mix styles going forward.**
2. **Elevation.** 9,000 vs 8,663. Decide once and replace sitewide. §5.6.
3. **Ahrefs vs Semrush.** Called out in §11.1. Defaulting to Ahrefs; revisit Month 2.
4. **BreadcrumbList injection.** How do we apply universally without hand-editing every page? Two options:
   - (a) Add a small Python script in `content/` (similar to `sync-nav.py`) that injects a BreadcrumbList JSON-LD block per file based on directory depth.
   - (b) Inject via a tiny deferred JS in `common.js`.
   Option (a) is better for SEO (server-rendered JSON-LD is indexed more reliably than JS-injected). **Recommend (a).**
5. **The two `.pages` files in `md/DC-SEO-Plan/`.** I couldn't parse them in this pass. If their content diverges from the `.md` and `.docx` equivalents, we'd miss guidance. **Action:** export both to PDF or Markdown and confirm.
6. **Baseline numbers.** GSC property is not yet verified, so every "TBD" in the KPI table is literal. Week 1 Day 1 priority.
7. **Editorial standards document.** `SEO-Master-Plan.md` §5.3 demands author bylines, About page credibility, dated updates. We do not yet have a standing `/about/editorial-policy.html` or byline pattern. Draft in Weeks 3–4.
8. **Stock imagery ban enforcement.** Policy exists; enforcement does not. Need a pre-publish visual check — either a one-line rule in the review prompts in `content/` or a photography log per entity.
9. **Advertising model collision with E-E-A-T.** Source memos are enthusiastic about turning category pages into paid directories. We need to separate editorial from commercial placement clearly (disclosure, visual demarcation) to avoid an E-E-A-T hit. Worth a standalone follow-up memo once the foundation is live.

### Risks

- **Velocity collapse.** The 90-day plan requires 2–3 substantial pieces per week. If we fall off that cadence, the first-mover window narrows. Mitigation: front-load seasonal and feeder pages that have the longest shelf-life per hour of work.
- **Cannibalization with MountainMonthly.com.** If both sites drift into the same topic space, Google suppresses one. Mitigation: keyword map is the gate, checked before every publish.
- **Over-reliance on the Complete Guide.** One page ranking for 10+ keywords is also one page to lose. Mitigation: build the second-tier guides (hiking, lodging, dining) to sufficient depth that the Complete Guide is the hub, not the sole ranking asset.
- **AI-generated competitor content.** Already proliferating per `DiscoverCloudcroft-SEO-Memo.docx`. Our defense is ground-level specificity — named trails, streets, cabins, coffee shops. Generic travel copy is a fail.

---

## 14. What I'd Do First on Monday Morning (v1.1 — reordered after the May 1 audit)

The May 1 audit reshuffles priorities. Three v1.0 actions are still right but they no longer go first. The new top of the list is the audit's quick-win punch list — six actions a single dev can knock out in a focused day or two, each of which clears a P0 indexing blocker.

### #1 — Run the audit's top-6 quick wins (the "P0 unblock" sprint)
**Effort:** 1–2 days for one developer. **Impact:** highest. Each of these is a P0 indexing blocker.

1. **Delete the six duplicate / stub HTML files** (B2). `index copy.html`, both root `complete-guide-…copy.html`, `do/complete-guide-…copy.html`, `stay/xxx-…copy.html`, `topic-page-target-mockup.html`. These are not in the sitemap and add no value. Three of them duplicate the homepage's exact title and meta description, which is actively harming ranking.
2. **Create `media/og-default.webp` at 1200×630** plus the two other missing assets (`Index-24.webp`, `placeholder-hero-main.webp`) (B3). 46 pages currently reference an OG image file that doesn't exist on disk. Social previews are silently broken.
3. **Fix `index.html`'s canonical** to `https://discovercloudcroft.com/` and drop the fictional sitemap entry pointing to `/complete-guide-to-cloudcroft-new-mexico-2026.html` (B6 + half of B4). Right now Google may be deindexing the homepage because the canonical points at a 404.
4. **Script the 40 mismatched canonicals** (B1). 38% of the indexable surface currently has a canonical pointing at a URL that doesn't exist. Either rewrite each canonical to the actual filename, or ship a single rewrite rule for the pretty-URL targets.
5. **Site-wide find/replace on the top broken-link targets** (B5). `stay/lodging.html` → `stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html`; `do/complete-guide-to-activities.html` → `do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html`; fix the typo'd `where to-hike-in-Cloudcroft-New-Mexico-2026.html`. Resolves ~40 of the 167 broken internal links.
6. **Fix the 12 entity pages whose JSON-LD `"url"` points to a third-party domain** (C8). Copy the pattern from `eat/black-bear-coffee-shop.html` — on-site canonical as `"url"`, third-party domain in `sameAs`. Currently every Stay entity is telling Google "the canonical entity profile lives at the property's own website."

After this single sprint, site health moves from 58/100 toward the 75–80 range. None of these are research questions; all are bounded find/replace or one-shot file deletions.

### #2 — Stand up GSC + Bing + GA4 against the production domain, and resolve the elevation discrepancy
**Effort:** half a day. **Impact:** high.
Same content as v1.0's #2. Without a verified GSC property under the production domain, every KPI in §2 stays TBD and the 90-day plan runs blind. While in there: pick 9,000 or 8,663 (verify against the Village of Cloudcroft's own published data) and find/replace sitewide — `index.html` alone references 9,000 in six places. Audit's quick-wins #1–#5 don't depend on this, but every measurement decision afterward does.

### #3 — Tighten 87 titles + 83 descriptions in one pass
**Effort:** half a day, mostly mechanical. **Impact:** high on CTR.
The audit's C1 + C2. Median title is 85 chars (Google cuts at ~60); max is 150. Median description is 182; max 313 (Google rewrites long descriptions, often badly). One scripted pass: drop ` | DiscoverCloudcroft.com` from titles (Google appends site name when configured via Schema), trim taglines to fit 50–60 chars including geo, trim descriptions to 140–155 with a CTA verb + a differentiator + geo. This is the single highest-leverage CTR move and it costs almost nothing.

### #4 — Add `Organization` + `WebSite` (with `SearchAction`) JSON-LD to `index.html`
**Effort:** 1 hour. **Impact:** brand SERP appearance.
The audit's C3. Currently the homepage has `TouristDestination` + `BreadcrumbList` + `FAQPage` + 8 `Event`s — but no `Organization` (publisher with logo + `sameAs` to social profiles + `contactPoint`) and no `WebSite` (with `potentialAction: SearchAction`). Without `WebSite/SearchAction`, the site loses sitelinks search-box eligibility. Without `Organization`, the publisher / E-E-A-T attachment is missing.

### #5 — Commit `md/keyword-map.md` to the repo
**Effort:** 2–3 hours. **Impact:** high on the discipline side.
Same as v1.0's #3. One Markdown table: primary keyword, search intent, owner URL (on DiscoverCloudcroft or MountainMonthly), status (live / drafted / planned / not claimed), last-updated date. Every "every page…" rule in `SEO-Master-Plan.md` hinges on this file existing as the gate before publish. Without it, the two-domain discipline in `MM-DC-Digital-Strategy.txt` is aspirational.

### What's no longer #1
The v1.0 #1 — *"Fix the complete-guide consistency failures from the April 19 audit"* — is now folded into the May 1 audit's broader scope. The font-family bug, the `og:type=website` corrections, the STAY subpage nav paths, the per-page OG images: all still need to happen, but they sit inside §7.6's P1 batch (titles, descriptions, JSON-LD `"url"` fix, BreadcrumbList universalization). The April 19 topic-pages audit was correct; it just wasn't the most-broken thing on the site. The May 1 site-wide audit found bigger fires.

After actions #1–#5 above, everything in Weeks 1–2 of §12 is executable and the plan is running. The remaining P1 items in §7.6 (C4 image dimensions across 469 imgs, C5 LCP preload across 100 pages, C6 `defer` on 84 pages, C7 duplicate IDs, C9 `geo` on 55 entity pages, C10 BreadcrumbList on 12 guides, C11 HEIC conversions, C12/C13/C14 image and meta cleanup) become the Weeks 3–6 backlog.

---

*Originally written April 24, 2026 (v1.0). Updated May 1, 2026 (v1.1) to fold in `md/seo-audit-2026-05-01.md`. Reviewed against `SEO-Master-Plan.md`, `SEO-STRATEGY-MEMO.md`, `DiscoverCloudcroft-SEO-Memo.docx(.pdf)`, `MM-DC-Digital-Strategy.txt`, `DC-SEO-Pages-Ideas.pdf`, `topic-pages-consistency-audit.md`, `md/seo-audit-2026-05-01.md`, and the current state of `index.html`, `robots.txt`, `sitemap.xml`, `eat/black-bear-coffee-shop.html`, and the repo's `CLAUDE.md`. Where sources conflicted, the May 1 technical audit is the default tiebreaker for file-counted defects; the April 2026 Master Plan is the default tiebreaker for strategic decisions. Unresolved source conflicts are explicitly flagged in §13.*
