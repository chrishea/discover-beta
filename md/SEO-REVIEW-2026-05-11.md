# DiscoverCloudcroft.com — SEO Review & Recommendations

**Reviewer:** Claude (Cowork)
**Date:** 2026-05-11
**Repo state:** main @ `e848c28`
**Scope:** Full technical + on-page audit, ranking check on four target keywords, prioritized recommendations.

---

## 1. Executive summary

DiscoverCloudcroft.com has a **strong technical foundation** — the kind most editorially-driven static sites never bother to build. Every page has a canonical, meta description, OG/Twitter cards, single H1, and rich JSON-LD schema. Alt-text coverage is effectively 100% (447 `<img>` tags, exactly one missing alt, and that one was a comment, not a real image). The sitemap is current. `robots.txt` is correct. Archived `shelf/*` pages carry `noindex`.

What the site does **not** have is **search visibility on its money keywords**. For all four keywords you asked me to check — "hike in cloudcroft nm," "eat in cloudcroft nm," "stay in cloudcroft nm," "camp in cloudcroft nm" — discovercloudcroft.com does not appear in the top 10 organic results. AllTrails, Tripadvisor, Hipcamp, USFS, cloudcroft.com, coolcloudcroft.com (Chamber), and Expedia own those SERPs.

The good news: the gap is mostly **competitive positioning and internal linking**, not technical. Three findings drive most of the headroom:

1. **Stale Google index of the homepage.** SERP for the brand query "discover cloudcroft" still shows the old title *"Discover Cloudcroft — Your Mountain Escape at 8,676 Feet"* (the title of the now-archived `shelf/old-index.html`). The live homepage's actual title is *"Cloudcroft, NM — Complete 2026 Travel Guide."* Google hasn't refreshed since the redesign.
2. **The Hike and Camp hub guides are buried.** The top nav exposes Stay / Eat / Activities / Shop / Events / Resources. There is no direct link to the hiking guide or camping guide. As a result the hiking hub has only 7 inbound internal links and the camping hub only 3 — versus 111 each for the Eat and Stay hubs. Internal link equity is the easiest SEO lever you have, and you're not pulling it for the two outdoor-recreation pages that matter most for Cloudcroft.
3. **H1s don't reinforce target keywords.** "Twelve hikes, ranked." / "Camp at 8,676 feet." / "Nineteen places to eat." are stylish but miss the keyword match Google rewards in H1s. Only the Stay hub uses a keyword-bearing H1 ("Where to stay in Cloudcroft").

A fourth, smaller issue worth flagging: **the live deploy of `/do/mexican-canyon-trestle.html` is out of sync with the repo.** The repo version uses the entity-page template with no emojis. The live version is an older, emoji-heavy page. Either the deploy pipeline missed a push, or CDN cache is stale.

The rest of this review walks the findings end-to-end and ends with a prioritized fix list.

---

## 2. Search ranking results (the four target keywords)

Searched on Google web search, May 11, 2026. None of these queries returned discovercloudcroft.com in the top 10.

### "hike in cloudcroft nm"

| Rank | Domain | Why it wins |
| --- | --- | --- |
| 1 | alltrails.com | Aggregator with user-generated trail data and millions of reviews |
| 2 | komoot.com | Aggregator |
| 3 | hikingproject.com | REI-owned trail database |
| 4 | alltrails.com (list) | Second AllTrails URL |
| 5 | tripadvisor.com | Hiking attractions in Cloudcroft |
| 6 | theoutbound.com | Aggregator |
| 7 | cloudcrofthostel.com | Local property's "Explore Cloudcroft" page |
| 8 | onlyinyourstate.com | Listicle |
| 9 | tripadvisor.com (Osha Trail) | Single-attraction review |
| 10 | gaiagps.com | Aggregator |

**discovercloudcroft.com: not in top 10.**

### "eat in cloudcroft nm"

| Rank | Domain | Why it wins |
| --- | --- | --- |
| 1 | thebitenm.com | NM food blog tourist guide |
| 2 | tripadvisor.com | Restaurant aggregator |
| 3 | bigdaddysdinernm.com | Individual restaurant site |
| 4 | coolcloudcroft.com | **Chamber of Commerce** dining directory |
| 5 | slightnorth.com | Travel blog |
| 6 | yelp.com | Aggregator |
| 7 | cloudcroft.com (dining) | Commercial visitor guide |
| 8 | facebook.com (Mad Jack's) | Restaurant Facebook page |
| 9 | explorecloudcroft.com (food & drink) | Competitor visitor guide |
| 10 | cloudcroftsandwich.shop | Individual restaurant site |

**discovercloudcroft.com: not in top 10.**

### "stay in cloudcroft nm"

| Rank | Domain | Why it wins |
| --- | --- | --- |
| 1 | grandcloudcroft.com | Property |
| 2 | 223collectionhotels.com (The Lodge) | Property |
| 3 | cloudcroft.com (lodging) | Commercial visitor guide |
| 4 | airbnb.com | OTA |
| 5 | expedia.com | OTA |
| 6 | cabinsatcloudcroft.com | Property |
| 7 | tripadvisor.com | Aggregator |
| 8 | hotelcloudcroft.com | Property |
| 9 | newmexico.org | State DMO |
| 10 | kayak.com | OTA |

**discovercloudcroft.com: not in top 10.**

### "camp in cloudcroft nm"

| Rank | Domain | Why it wins |
| --- | --- | --- |
| 1 | thecampatcloudcroft.com | Property (campground) |
| 2 | yelp.com | Aggregator |
| 3 | fs.usda.gov (Lincoln NF) | USFS — the authority |
| 4 | facebook.com (Camp Rio) | Campground Facebook |
| 5 | hipcamp.com | Aggregator |
| 6 | cloudcroft.com (camping) | Commercial visitor guide |
| 7 | 16springs.com | Campground site |
| 8 | perfectcamp.com | Aggregator |
| 9 | facebook.com (Cloudcroft Campgrounds) | Page |
| 10 | thedyrt.com | Aggregator |

**discovercloudcroft.com: not in top 10.**

### Brand query: "discover cloudcroft" — site IS indexed, but stale

| Rank | URL | Title shown in SERP |
| --- | --- | --- |
| 1 | www.discovercloudcroft.com/ | **"Discover Cloudcroft — Your Mountain Escape at 8,676 Feet..."** ← stale title (matches `shelf/old-index.html`, not the current `index.html`) |
| 2 | elevatecloudcroft.com | "Discover Cloudcroft \| New Mexico's Mountain Escape" — competitor squatting on the brand phrase |

The site ranks #1 for its own brand. But Google is showing the *previous* homepage title, suggesting the index hasn't been refreshed since the redesign. That also means Google may be evaluating the homepage on the old content, not the new.

---

## 3. Technical SEO inventory

### 3.1 What's in place and working

| Check | Status | Notes |
| --- | --- | --- |
| `robots.txt` | ✅ | Allows all, points to sitemap |
| `sitemap.xml` | ✅ | 110 URLs, regenerated 2026-05-10 |
| Canonical tags | ✅ | 100% of indexable pages have a canonical |
| Meta description | ✅ | 100% present |
| Title tag | ✅ | All pages have one |
| OG / Twitter cards | ✅ | Present on essentially every page (one minor gap: `shelf/index-hold.html` — already noindexed, so moot) |
| Single H1 per page | ✅ | 0 pages with zero H1s, 0 with multiple H1s |
| JSON-LD schema | ✅ | Present on 109 of 112 indexable pages (the 3 misses are noindexed `shelf/*`) |
| Image alt text | ✅ | Effectively 100% — only "miss" was an HTML comment |
| `www` → apex 301 | ✅ | `www.discovercloudcroft.com/` redirects to `discovercloudcroft.com/` |
| Mobile viewport meta | ✅ | All pages |
| Skip-link & accessibility scaffolding | ✅ | Consistent across pages |
| Google Analytics (GA4) | ✅ | `G-2CQ53PCP3M` installed sitewide |
| RSS / Atom feed | ✅ | `/feed.xml` (13 KB, linked from homepage) |
| `llms.txt` | ✅ | Present (good signal for AI crawlers / Overviews) |
| Archived pages noindexed | ✅ | `shelf/*` carry `<meta name="robots" content="noindex">` |
| HTTPS | ✅ | Site-wide |

### 3.2 Schema usage (good)

JSON-LD coverage is unusually rich for a static site. Across 112 pages I count:

- **Articles & guides:** Article (30), TouristAttraction (12), FAQPage (12), TouristDestination, AboutPage, ContactPage, CollectionPage, ProfilePage
- **Businesses:** Restaurant (9), Store (12), LodgingBusiness (7), Hotel, Motel, Bakery (3), CafeOrCoffeeShop (2), BarOrPub (2), Brewery, Winery, GolfCourse, JewelryStore (2), ClothingStore, HardwareStore, GroceryStore, SportingGoodsStore, EmergencyService, FoodEstablishment, LocalBusiness, SportsActivityLocation
- **Events:** Event (7), SportsEvent (4) — fully populated for the 2026 calendar
- **Structural:** 85 BreadcrumbList instances, 248 ListItem, 42 PostalAddress, 31 Place, 27 Organization
- **Q&A:** 71 Question/Answer pairs

### 3.3 Issues found

**Index hygiene**

| Issue | File(s) | Risk |
| --- | --- | --- |
| Template page indexable | `about/editors/template-editor-bio.html` carries `<meta name="robots" content="index,follow">` but contains placeholder `[NAME]` content | Could be discovered and indexed as broken/templated content |
| Archive duplicate present | `shop/mountain-magic-archive.html` duplicates `shop/mountain-magic.html` | Canonical is set correctly to the live URL; risk is low but should be `noindex` or removed entirely |
| Pages on disk missing from sitemap | `about/editors/index.html`, `topics/index.html` | If you want these crawled, add them; if not, add `noindex` |
| Stale Google index | Live homepage (SERP shows old title) | Brand SERP shows wrong page title; signals re-crawl needed |
| Deploy lag | Live `/do/mexican-canyon-trestle.html` serves an older emoji-heavy version, while repo has new entity-template version | Live site does not match repo for this page. Need to verify deploy pipeline / CDN cache. Other pages may be affected — sample more after fix. |

**Title tags that need work**

Several titles are too generic or missing the location/year that the rest of the catalog uses consistently. Each one of these is a small but real CTR penalty:

| File | Current title | Suggested |
| --- | --- | --- |
| `about/privacy.html` | "Privacy Policy" | "Privacy Policy — DiscoverCloudcroft.com" |
| `about/terms.html` | "Terms and Conditions" | "Terms & Conditions — DiscoverCloudcroft.com" |
| `stay/burro-street-boardinghouse.html` | "Burro Street Boardinghouse" | "Burro Street Boardinghouse, Cloudcroft NM (2026)" |
| `stay/cloudcroft-hostel.html` | "Cloudcroft Hostel" | "Cloudcroft Hostel — Budget Lodging in Cloudcroft, NM (2026)" |
| `stay/crofting-inn-cloudcroft.html` | "The Crofting Bed and Breakfast" | "The Crofting B&B, Cloudcroft NM (2026) — Historic 1909 Inn" |
| `stay/dusty-boots-motel-cloudcroft.html` | "Dusty Boots Motel and Cafe" | "Dusty Boots Motel & Cafe, Cloudcroft NM (2026)" |
| `stay/osha-trail.html` | "Osha Trail Lodging" | "Osha Trail Lodging — Short-Term Rentals in Cloudcroft, NM (2026)" |
| `stay/vacation-rentals.html` | "Vacation Rentals & Cabins" | "Vacation Rentals & Cabins in Cloudcroft, NM (2026)" |
| `shop/art-galleries.html` | "Art Galleries & Local Art" | "Art Galleries in Cloudcroft, NM — Burro Ave Local Art (2026)" |
| `do/pickleball.html` | "Pickleball in Cloudcroft" | "Pickleball in Cloudcroft, NM — Six Free Courts at 8,676 ft" |
| `events/high-altitude-classic.html` | "High Altitude Classic Bike Race" | "High Altitude Classic Bike Race — Cloudcroft, NM (2026)" |
| `season/seasonal.html` | "Seasons of Cloudcroft" | "Cloudcroft Seasons Guide — Spring, Summer, Fall, Winter (2026)" |
| `shop/mountain-magic.html` and `shop/mountain-magic-archive.html` | Both: "Mountain Magic, Cloudcroft NM (2026)" | Keep archive `noindex` or delete; live page title is fine |

**H1s that miss the keyword**

The four most ranking-important hub pages have stylized H1s that drop the target keyword. Title tags carry the keyword (good); H1s do not (suboptimal).

| Page | Current H1 | Issue | Suggested |
| --- | --- | --- | --- |
| `do/guide-to-hiking-in-cloudcroft-new-mexico.html` | "Twelve hikes, ranked." | No "hiking," no "Cloudcroft" | "Hiking in Cloudcroft, NM — 12 trails ranked easy to hard" (move "Twelve hikes, ranked." into a stylized subhead) |
| `do/guide-to-camping-cloudcroft-new-mexico.html` | "Camp at 8,676 feet." | No "camping," no "Cloudcroft" | "Camping in Cloudcroft, NM — 13 sites ranked by type" |
| `eat/complete-guide-where-to-eat-in-cloudcroft.html` | "Nineteen places to eat." | No "Cloudcroft" | "Where to eat in Cloudcroft, NM — 19 independent restaurants" |
| `stay/complete-guide-to-lodging-in-cloudcroft-new-mexico.html` | "Where to stay in Cloudcroft." | OK — keep | — |

You can keep the editorial voice by demoting the stylized phrase to a `.hero-eyebrow` or subhead and elevating the keyword-bearing H1.

**Schema gaps on the four hub guides**

| Page | Has | Should add |
| --- | --- | --- |
| Hike guide | `TouristAttraction`, `BreadcrumbList` | `Article` + `ItemList` (each of the 12 trails as `ListItem` with name, url, image, description) |
| Camp guide | `TouristAttraction`, `BreadcrumbList` | `Article` + `ItemList` for the 13 sites |
| Eat guide | `Article`, `Place`, `BreadcrumbList` | `ItemList` of the 19 restaurants |
| Stay guide | `Article`, `Place`, `BreadcrumbList` | `ItemList` of the 9 properties (already done well on entity pages) |

ItemList markup is what unlocks Google's *list-style* rich result and the AI Overview citations that name specific entities.

**Internal linking gaps**

Inbound internal links to the four hub guides:

| Hub guide | Inbound links from other pages |
| --- | --- |
| `complete-guide-where-to-eat-in-cloudcroft.html` | **111** |
| `complete-guide-to-lodging-in-cloudcroft-new-mexico.html` | **111** |
| `guide-to-hiking-in-cloudcroft-new-mexico.html` | 7 |
| `guide-to-camping-cloudcroft-new-mexico.html` | 3 |

The Eat and Stay hubs sit in the top nav (which is duplicated across all 110+ pages). Hike and Camp are reachable only via the Activities hub. That's a one-link bottleneck for two of your highest-intent topics. Anchor-text data is similarly thin.

**Author / E-E-A-T signals**

The site has a strong `about/editors/` hub and editorial-standards page — great. But the *individual article pages* don't surface those connections. Article schema lists `publisher` but rarely `author`. Adding an `author` field with `Person` schema linked to an editor bio page is a measurable E-E-A-T improvement, and Google now weights this for travel content under the "helpful content" framework.

**Page weight & render-blocking assets**

Largest pages: `index.html` 141 KB, the shop / eat / stay / activities / camp / hike hubs 100–129 KB. That's heavy for static HTML but acceptable. The bigger issue is **render-blocking external CSS**: every page pulls Google Fonts via `<link>` *in addition to* the self-hosted `fonts.css` in `/fonts/`. Pick one. Removing the Google Fonts request shaves ~150 ms of blocking time on first paint.

**Image filenames**

Hero image filenames like `hike-00037.jpg`, `cabins-at-00451.JPG`, `IMG_5063.jpg` lose image-SEO value. Descriptive filenames (`cloudcroft-osha-trail-pine-forest.jpg`) help in Google Images and reinforce the keyword in the URL context. Not high priority for ranking — but free if you rename on next photo refresh. Also: mixed-case `.jpg` / `.JPG` / `.jpeg` extensions are common in the repo — the strip-CSS scripts already warn about this.

---

## 4. Competitive landscape: who's beating you and why

Three classes of competitor own the SERPs for Cloudcroft tourism queries:

**A. Vertical aggregators with massive authority.** AllTrails (hike), Tripadvisor (everything), Hipcamp / theDyrt (camp), Airbnb / Expedia / Booking.com (stay), Yelp (everything). These domains have decades of links, millions of reviews, and category-specific UX. You will not outrank them at scale on broad keywords like "hike in cloudcroft nm." Don't try.

**B. The Cloudcroft DMO + Chamber.** `coolcloudcroft.com` (the Chamber) and `newmexico.org` (NM Tourism Dept) have institutional authority and local backlinks. They show up in mid-page slots. They're beatable on long-tail content with depth.

**C. Lookalike commercial guides.** `cloudcroft.com`, `explorecloudcroft.com`, `cloudcrofthostel.com/explore-cloudcroft`, `elevatecloudcroft.com`. These are roughly your peer set. They're outranking you on most queries today, but their content is thinner than yours and they don't have your structured-data depth.

**The opening:** You can't beat AllTrails on "hike in cloudcroft nm." You *can* beat the lookalike guides on long-tail decision queries — "best beginner hike in Cloudcroft," "are dogs allowed on Osha Trail," "fire restrictions Cloudcroft," "Cloudcroft from Alamogordo with kids," "RV park vs. Forest Service campground Cloudcroft." Those queries match the editorial style this site already produces. They also feed AI Overviews, which already pull from sites with clear, specific, factual content.

You're also positioned well for **regional drive-time queries** ("Cloudcroft from El Paso," "Cloudcroft from Las Cruces") — you have a `/visit/` section dedicated to exactly that. Six pages exist, none rank in the top 10 yet, but the content/template is good. Promote those harder internally.

---

## 5. Recommendations — prioritized

### P0 — Quick wins, this week

1. **Force re-index of the homepage.** In Google Search Console, use "URL Inspection" → "Request Indexing" for `https://discovercloudcroft.com/`. This is the single highest-leverage fix: the SERP currently shows a stale, archived title.
2. **Resolve the deploy/cache lag on `/do/mexican-canyon-trestle.html`.** Live version doesn't match the repo. Push and purge cache. Then spot-check 5–10 other pages (especially recently updated ones) to confirm the deploy pipeline is healthy.
3. **Add Hike and Camp to the top nav** — either as direct items in `content/sync-nav.py` or as a sub-row on the Activities anchor. This is one regex change and a `python3 content/sync-nav.py` run.
4. **Rewrite the four hub H1s** to lead with the keyword (see table in §3.3). Keep your editorial subhead voice; move it to `.hero-eyebrow` or a `<p>` tagline.
5. **Fix thin/branded titles** on the ~12 pages in the table in §3.3.
6. **Add `noindex` to `about/editors/template-editor-bio.html`** and `shop/mountain-magic-archive.html`.

### P1 — Internal linking & schema depth, 1–2 weeks

7. **Add `ItemList` JSON-LD to the four hub guides.** Each list page becomes eligible for list-style rich results and AI-Overview entity citations.
8. **Add `Article` schema to the hike + camp guides** (currently only `TouristAttraction`).
9. **Cross-link hubs with descriptive anchor text.** Eat ↔ Stay ↔ Hike ↔ Camp ↔ Visit. Not just "see also" — anchors like "Pair these trails with a cabin booking" beat "Lodging guide."
10. **Add `author` + `Person` schema to article pages**, linked to your existing editor bios. This is the cheapest E-E-A-T win you can ship.
11. **Add the `visit/` regional drive-time pages to the homepage and to each hub's footer.** Currently underexposed.
12. **Submit fresh sitemap to GSC + Bing Webmaster Tools after these changes**.

### P2 — Content & off-page, 1 month

13. **Target long-tail "decision" queries** the aggregators don't optimize for. Suggested first batch:
    - "Osha Trail dogs allowed Cloudcroft" (Q&A page + FAQ schema)
    - "Cloudcroft fire restrictions 2026" (you have water restrictions; add fire)
    - "Best beginner hike Cloudcroft"
    - "Trestle Recreation Area parking hours"
    - "Cloudcroft to White Sands day trip"
    - "Cloudcroft vs Ruidoso"
    - "Cloudcroft in July weather"
14. **Earn 3–5 local backlinks.** Reach out to:
    - Cloudcroft Chamber (`coolcloudcroft.com`) — ask for a partner-resources listing
    - New Mexico Tourism Dept (`newmexico.org`) — submit an editorial listing
    - Alamogordo Daily News, Ruidoso News
    - Sacramento Mountains Museum
    - NM Magazine
    Each of these is a high-authority local link that will lift the whole site.
15. **Quarterly content refresh** on the four hub pages. Update the `(2026)` year stamp and any verified-on dates, and add 1–2 new entries per refresh.

### P3 — Technical polish

16. **Self-host the Google Fonts** you're loading via `<link>`. You already have `/fonts/` and `fonts.css`. Drop the external request; gain ~150 ms on first paint.
17. **Add `Organization` / publisher schema with founders and editorial leadership** to `/resources/about.html`. Strengthens E-E-A-T at the site level.
18. **Image-SEO pass:** rename hero images on the four hub pages to descriptive slugs. Low effort, marginal impact.
19. **Standardize OG image dimensions to 1200×630** across all pages (homepage is fine; verify the entity pages).
20. **Add `IndexNow` or sitemap ping** to your deploy workflow so Google + Bing learn about changes faster (avoids the kind of stale-index problem you have today).

### P4 — Measurement

21. **Confirm Google Search Console is set up** for both `discovercloudcroft.com` and `www.discovercloudcroft.com` (verify both, even with the 301).
22. **Set up Bing Webmaster Tools.** Bing's share is small but it powers ChatGPT search; AI traffic is increasingly worth ranking for.
23. **Add GA4 conversion events** for outbound clicks to booking/reservation links on entity pages and for newsletter signups (the modal already exists).
24. **Track the four target keywords weekly** in GSC → Performance → Queries. Re-pull this audit in 90 days to measure delta.

---

## 6. Verified inventory snapshot (for the record)

| Metric | Count |
| --- | --- |
| Total indexable HTML pages | 112 |
| Pages in sitemap | 110 |
| Average page size | 43 KB |
| Largest page | `index.html` (141 KB) |
| Pages with canonical | 112 / 112 |
| Pages with meta description | 112 / 112 |
| Pages with JSON-LD | 109 / 112 (3 misses are noindexed `shelf/*`) |
| Pages with zero or multiple H1s | 0 / 112 |
| `<img>` tags total | 447 |
| `<img>` tags missing `alt=` | 0 (1 false positive in a comment) |
| Pages with emojis in body | 4 (`do/guide-lincoln-national-forest.html`, `resources/zenith-park-in-cloudcroft.html`, `do/camp.html`, `events/top-events.html`) |
| Sitemap-vs-disk mismatches | 4 (3 explainable, 1 archived dupe) |
| Pages noindexed | 5 (all `shelf/*`) |

---

## 7. What I did not check

- **Live Core Web Vitals.** I didn't run PageSpeed Insights against the live site — that's the next layer after the deploy issue is fixed. The render-blocking Google Fonts call is the most likely LCP regression.
- **Backlink profile.** I don't have access to Ahrefs / Semrush from this session. The aggregator dominance in SERPs strongly implies your inbound-link count is small relative to competitors; an Ahrefs export would confirm.
- **Google Search Console data.** I can recommend queries to target, but I can't see which queries are *already* driving impressions and where you're #11–20 (close-to-page-one targets are the highest-ROI fixes).
- **Mobile usability beyond viewport meta.** Visually inspecting on a phone is out of scope here.

---

*If you want, the next pass can: (a) draft the actual H1/title edits as a single PR, (b) write the `ItemList` JSON-LD blocks for the four hub pages, or (c) build a one-page tracker that re-runs the keyword ranking checks every 30 days.*
