SEO Master Plan
DiscoverCloudcroft.com (+ MountainMonthly.com pairing)
Version: 1.0 Date: April 2026 Purpose: Single source of truth for training contributors, briefing designers/developers, and auditing every page on the site. Every page ships against this plan, and every page is reviewed against this plan.

1. North Star
DiscoverCloudcroft.com exists to answer one question: Should I go to Cloudcroft, and what do I do when I get there?
The audience is a traveler in trip-planning mode — searching before they book, not after they arrive. Every page, every headline, every image, and every piece of schema serves that intent.
The long goal: become the authoritative answer any time anyone — human or AI — searches anything about visiting Cloudcroft. Target 18 to 24 months of consistent publishing to lock that position in. Once earned, it is durable and defensible.
Three operating principles:
Ground-level specificity wins. Name the trail, the street, the cabin, the shop. Generic travel copy loses to local fact. AI can fabricate generalities — it cannot invent which parking lot fills up first.
Build for AI crawlers and humans simultaneously. Accurate facts, named entities, clear headings, current dates, regular updates. This is not two strategies. It is one.
Velocity in the first 90 days. Early indexing, early backlinks, and early content depth create a lead that competitors on Wix or AI-template platforms cannot close.

2. Two-Domain Relationship (Do Not Violate)

Rules:
Never duplicate content across domains. Google will split authority or suppress one.
Every high-value keyword gets one clear owner. Log it in the Keyword Map before publishing.
Mountain Monthly earns backlinks through journalism and passes authority to Discover Cloudcroft via deliberate internal links. Discover Cloudcroft links back to Mountain Monthly for context and credibility ("read our in-depth coverage of…").
Anchor text is natural. No keyword stuffing across the bridge.
Before publishing any page, ask: does this topic already exist on the other domain? Which has stronger authority? Will this compete internally? If yes — consolidate.

3. Keyword Map (Owners, Targets, Intent)
Every published page must be logged against a keyword in this map. If a page does not have a primary keyword owner entry, it does not ship.
3.1 Core Travel — Highest Value
Target page: Complete Guide to Visiting Cloudcroft, New Mexico (2026)

3.2 Seasonal — Build 60 to 90 Days Ahead of Demand
Target pages: Fall Color Guide, Christmas in Cloudcroft, Summer Festival Guide, Winter Activities Guide, Spring Hiking Guide

3.3 Outdoor — Longest Tail, Each Trail Earns Its Own Page
Target pages: Best Hiking Trails Near Cloudcroft, Cloudcroft Outdoor Recreation Guide, individual trail pages (Osha, Rim, etc.)
cloudcroft hiking trails
best hikes near cloudcroft nm
cloudcroft mountain biking trails
cloudcroft camping guide
sacramento mountains hiking
stargazing cloudcroft new mexico / cloudcroft dark sky
things to do cloudcroft with kids
cloudcroft mountain biking
3.4 Lodging — Highest Commercial Intent
Target pages: Cabin Guide, Lodging Directory, Weekend Getaway Guide
cabins in cloudcroft nm
cloudcroft nm lodging guide
places to stay in cloudcroft
best cabins in cloudcroft nm
romantic cabins cloudcroft nm
pet friendly cabins cloudcroft nm
cloudcroft cabin rentals with hot tub
lodging near cloudcroft new mexico
3.5 Food & Town — List Pages Rank Well
Target pages: Dining Guide, Burro Avenue Walking Guide, individual restaurant pages
best restaurants in cloudcroft nm
cloudcroft coffee shops
cloudcroft breweries
cloudcroft shopping guide
burro avenue cloudcroft shops
bbq cloudcroft new mexico
cloudcroft breakfast spots
dog friendly restaurants cloudcroft
3.6 Day-Trip & Planning — Feeder Markets
Target pages: One landing page per origin city, plus planning/FAQ content
day trip from el paso to cloudcroft
el paso to cloudcroft
albuquerque to cloudcroft
roswell to cloudcroft
alamogordo to cloudcroft
las cruces to cloudcroft
cloudcroft weather
cloudcroft elevation
how far is cloudcroft from el paso
white sands cloudcroft

4. Technical Standards (Every Page)
Pages that miss any item in this section fail audit.
4.1 URLs
Static, keyword-rich, hyphenated, lowercase. Example: /things-to-do/hiking-cloudcroft-nm/
No dynamic parameters for primary content (?id=42 is a fail).
Flat architecture — no primary page deeper than 3 clicks from the homepage.
URL never changes after publish. Update content, not the slug.
4.2 Meta & Head
Every page must have:
<title><!-- 50–60 chars, primary keyword near the front, brand at end --></title>
<meta name="description" content="<!-- 150–160 chars, unique, compels the click -->">
<link rel="canonical" href="https://discovercloudcroft.com/<slug>/">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="index,follow">
Open Graph (required on every page):
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://discovercloudcroft.com/images/og/<page>.jpg">
<meta property="og:url" content="https://discovercloudcroft.com/<slug>/">
<meta property="og:type" content="website"> <!-- or article for guides -->
<meta name="twitter:card" content="summary_large_image">
4.3 Schema.org / Structured Data (JSON-LD)
Every page carries at least one schema block, matched to page type:

Geo-coordinates and full NAP markup live on Contact/About. areaServed on LocalBusiness points to Otero County, NM.
4.4 Sitemap & Indexing
sitemap.xml at root, auto-generated, every public URL included, excludes admin/utility.
robots.txt allows full crawl of public content.
Verify in Google Search Console and Bing Webmaster Tools before launch via DNS.
Submit sitemap to both the moment the site goes live.
Manually request indexing of the top 10 pages via GSC URL Inspection on day one.
4.5 Core Web Vitals (Non-Negotiable Targets)

Verified with Lighthouse and PageSpeed Insights before a page indexes.
4.6 Performance Rules
Self-host fonts. No external font CDN round-trips.
Images served as WebP or AVIF, compressed, lazy-loaded below the fold, explicit width/height to prevent CLS.
CSS minified. JS deferred for anything non-critical.
Cloudflare (or equivalent) CDN fronts the site from day one. Edge caching matters for the El Paso / Albuquerque / Las Cruces feeder markets.
Browser cache headers set for static assets.

5. Content Standards (Every Page)
5.1 Structure
One <h1> per page, contains the primary keyword.
Two to four <h2> subheadings using secondary keywords.
<h3> and below used for true nesting only.
Minimum 300 words for utility pages; 800 to 1,500 words for category/landing pages; 2,000+ for flagship guides.
Short paragraphs (2 to 4 sentences). Scannable bullets where they earn their place. Tables when comparing.
TL;DR or "Quick Facts" block near the top on guides over 1,000 words — AI loves this.
5.2 Named Entities (The AI Search Lever)
Every page references specific, verifiable local entities:
Trail names (Osha Trail, Rim Trail, Trestle Recreation Area)
Streets (Burro Avenue, US-82)
Businesses (The Lodge at Cloudcroft, Mad Jack's Mountaintop Barbecue)
Events (Aspenfest, Christmas Mountain)
Geography (Sacramento Mountains, Lincoln National Forest, Sunspot)
Generic travel copy is a fail. A page without named local entities does not pass audit.
5.3 E-E-A-T Signals (Experience, Expertise, Authoritativeness, Trustworthiness)
First-person voice where appropriate: "The aspen grove on the Osha Trail peaks in late September — here is exactly when to go."
Specific detail competitors can't fake: which parking lot fills first, where the best green chile lives, February road conditions.
Every article carries an author byline with local bio context.
Real, dated, original photos. Stock imagery is an E-E-A-T red flag and is banned on editorial pages.
An About page that establishes local credibility. Link to it from author bios.
Dates visible on updates ("Updated April 2026").
5.4 Internal Linking (Hub and Spoke)
ACTIVITIES HUB (/activities/)
    ├── /activities/hiking-trails/
    ├── /activities/mountain-biking/
    ├── /activities/camping/
    ├── /activities/dark-skies/
    └── /activities/pickleball/

LODGING HUB (/lodging/)
    ├── /lodging/vacation-rentals/
    ├── /lodging/cabins/
    ├── /lodging/grand-cloudcroft-hotel/
    └── /lodging/summit-inn/

DINING HUB (/dining/)
    ├── /dining/mad-jacks-bbq/
    ├── /dining/big-daddys/
    ├── /dining/brother-n-law-bbq/
    └── /dining/western-bar/
Rules:
Every leaf page links back up to its hub. Every hub links down to its children.
Every page carries at least 3 internal links to related content (not counting nav/footer).
Anchor text is natural and descriptive. No "click here." No repeated exact-match anchors across the site.
Cross-category links are encouraged where real: hiking → pet-friendly, dark-skies → lodging, shopping → dining.
5.5 External Links
Link to authoritative sources: Lincoln National Forest, New Mexico Tourism Department, NOAA, AllTrails.
Link to MountainMonthly.com reporting when relevant ("read our coverage of the wildfire response").
No affiliate or commercial outbound links from editorial content without disclosure.
5.6 Images
Every image carries descriptive alt text (keyword-relevant, not stuffed).
OG image is 1200 × 630, branded, per-page where the page matters.
File names are descriptive: osha-trail-fall-aspens.webp, not IMG_4021.jpg.

6. AI-Search Optimization (Cite-Ability)
Build every page as if an AI will read it and decide whether to cite it. Four rules:
Comprehensive answers. A complete guide answering multiple related questions in one place gets cited. Thin single-topic pages do not.
Named entities over generic keywords. Consistent references to specific trails, streets, businesses, events build topical authority.
Recency and update frequency. Refresh the fall color guide every August. Update the events calendar quarterly. Add new trail pages over time. Static brochure sites do not get cited.
Structured content. Clear headings, organized sections, labeled tables, explicit FAQ blocks. AI extracts answers from formatted pages and ignores undifferentiated prose.
First mover window: Cloudcroft has almost no authoritative digital content compared to larger destinations. AI models reflect that gap. A site that fills the gap now gets cited simply because there is nothing better to cite. That window closes as AI-generated travel content scales into smaller markets. Move now.

7. Local SEO
7.1 Google Business Profile
Claim/create GBP for DiscoverCloudcroft.com under "Travel & Tourism" / "Destination."
Fill every field: hours, description (keywords used naturally), photos, Q&A.
Post weekly — events, seasonal content, new articles. GBP posts index fast and appear in SERPs.
Accumulate reviews. Ask featured businesses to reference the site. Ask readers to review.
7.2 Citations & NAP Consistency
Same Name, Address, Phone format across:
TripAdvisor (critical for travel)
Yelp
Foursquare / Apple Maps
New Mexico True (state tourism)
New Mexico Tourism Department directory
Otero County tourism resources
Visit Alamogordo (regional)
AllTrails
Roadtrippers
TravelNM.com
AAA travel guides
7.3 Backlink Targets (Quality over Volume)
New Mexico Tourism Department — directory listing (.gov link is gold)
Cloudcroft Chamber of Commerce — listing, possible reciprocal
Otero County visitor resources
Lincoln National Forest official site
Sunspot Solar Observatory
Albuquerque Journal / El Paso Times / Las Cruces Sun-News travel sections — pitch seasonal travel stories
AllTrails — submit trail content or get featured editorially
New Mexico True campaign — submit for inclusion
MountainMonthly.com — own it, link intentionally from relevant stories
The Cloudcroft Reader — own it, link from relevant stories
Regional travel bloggers — press kit, comp stays with partner businesses, guest post exchange
7.4 Link-Bait Content (Build These to Earn Links)
A Cloudcroft Travel Guide comprehensive enough that other sites reference it.
A Sacramento Mountains Wildflower / Fall Foliage map — visual, shareable, linkable.
An annual Best of Cloudcroft list — local businesses share and link.

8. Differentiation vs. Competitors

Our unique angles:
Dark skies / stargazing (Sunspot proximity)
Pet-friendly niche (underserved)
"Escape the heat" for El Paso and desert visitors
Apple orchards (unique to the area)
Historic logging heritage (authentic local story)

9. Measurement
9.1 Stack
Google Analytics 4 with enhanced measurement
Google Search Console (connected to GA4 for integrated data)
Bing Webmaster Tools
Lighthouse / PageSpeed Insights (run on every new page)
9.2 KPIs and Goals (Rolling 6-Month Targets)

9.3 Queries to Track in GSC Monthly
cloudcroft (brand)
cloudcroft nm (location)
things to do cloudcroft (activities)
cloudcroft cabins (lodging)
cloudcroft restaurants (dining)
cloudcroft fall colors (seasonal)
day trip from el paso to cloudcroft (feeder)

10. Launch & Publishing Cadence
10.1 Launch Sequence (Built in This Order)
Complete Guide to Visiting Cloudcroft, New Mexico (2026) — captures 10+ keywords immediately, single highest-impact page.
Lodging Directory — highest commercial intent, attracts advertising.
Seasonal pages built 60–90 days before each peak.
Individual trail, restaurant, and cabin pages — fill in over time, expand over 12–18 months.
10.2 90-Day Roadmap
Weeks 1–2: Foundation
Verify GSC + Bing Webmaster Tools; submit sitemap
Publish homepage, 3 hub pages (Things To Do, Where To Stay, Where To Eat), 5 core content pages
Implement all schema across live pages
Set up GBP listing
Submit to NM Tourism Department directory
Lighthouse audit — fix any CWV issues before indexing picks up
Weeks 3–4: Content Velocity
2 day-trip landing pages (El Paso, Albuquerque)
3 activity guides (top hiking, skiing/snow, summer)
Internal linking audit — every page links to at least 3 others
Pitch Chamber of Commerce and Otero County for links
Weeks 5–8: Authority Building
Publish 2–3 substantial pieces per week
Prioritize seasonal content relevant in 60 days
Reach out to 5 NM travel bloggers
Publish the Cloudcroft Travel Guide (the definitive linkable asset)
Post weekly to GBP
Link from relevant MountainMonthly.com and Cloudcroft Reader stories
Weeks 9–12: Gap Analysis & Acceleration
Pull GSC data: which queries are appearing? Which pages have impressions but low clicks? Optimize titles/meta.
site:visitcloudcroft.com in Google — find gaps we have not covered.
Publish event-specific pages for Cloudcroft events in the next 6 months.
Build remaining day-trip landing pages (Roswell, Alamogordo, Las Cruces).
Pitch El Paso and Albuquerque media seasonal travel stories.
10.3 Ongoing
Publish 2–3 substantial pieces per week for the first 90 days, then 1–2 per week.
Every seasonal page refreshed annually — same URL, updated content and dated.
Events calendar updated quarterly at minimum.

11. Email Capture (Search Traffic Is Rented)
Every high-ranking page offers:
Newsletter signup
A free guide download (PDF of the Complete Guide, seasonal checklists)
First-party data capture
The pre-launch subscriber list becomes a traffic source the moment the site goes live. Early traffic signals Google the site has an audience, which accelerates ranking.

12. Advertising & Monetization Model
Every category page is a directory waiting to happen. Content serves travelers; structure serves advertisers.
Lodging Guide → paid listings page
Dining Guide → featured placement
Burro Avenue Walking Guide → spotlight ads for local merchants
Events Calendar → sponsorship for the Village, Chamber, local businesses
Events calendar also generates repeat traffic — lowers bounce rate, improves dwell time, signals quality to Google

13. Page Audit Checklist
Run this checklist against every page — new and existing. A "No" in any row requires a fix before publish or re-review.
13.1 Strategy
[ ] Page is logged in the Keyword Map with a single primary keyword owner
[ ] Page does not compete with an existing page on this domain
[ ] Page does not duplicate content on MountainMonthly.com
13.2 URL & Head
[ ] URL is static, lowercase, hyphenated, keyword-rich, no parameters
[ ] Page is ≤ 3 clicks from the homepage
[ ] <title> 50–60 chars, primary keyword near the front
[ ] <meta description> unique, 150–160 chars, click-compelling
[ ] <link rel="canonical"> set correctly
[ ] Open Graph title, description, image, url, type — all present
[ ] Twitter Card tag present
13.3 Schema
[ ] Appropriate page-type schema implemented (TouristDestination / LodgingBusiness / Restaurant / Event / FAQPage / LocalBusiness)
[ ] BreadcrumbList schema on every page
[ ] Author / Article schema on editorial content
[ ] Geo-coordinates on business pages
[ ] Schema validates in Rich Results Test
13.4 Content
[ ] Single <h1> containing the primary keyword
[ ] 2–4 <h2> subheadings using secondary keywords
[ ] Minimum word count met for page type
[ ] TL;DR or Quick Facts block on long guides
[ ] Named local entities present (trails, streets, businesses, events)
[ ] E-E-A-T: first-person or author byline, specific local detail, About page linked
[ ] Original, dated photos — no stock imagery on editorial pages
[ ] "Updated [Month Year]" visible on evergreen pages
13.5 Linking
[ ] At least 3 relevant internal links (natural anchor text)
[ ] Page links up to its hub (if leaf) or down to children (if hub)
[ ] Cross-category link present where relevant
[ ] Authoritative external link present where relevant
[ ] Cross-domain link to MountainMonthly.com where relevant
13.6 Performance
[ ] LCP < 2.5s
[ ] CLS < 0.1
[ ] INP < 200ms
[ ] All images WebP/AVIF, compressed, lazy-loaded, explicit dimensions
[ ] Descriptive file names + alt text on every image
[ ] Fonts self-hosted
[ ] JS deferred where non-critical
13.7 Conversion
[ ] Newsletter signup present
[ ] Relevant CTA (download a guide, view the directory, book a stay)
[ ] Clear path to the next page the visitor would want
13.8 Indexing
[ ] Page in sitemap.xml
[ ] Submitted via GSC URL Inspection (if high priority)
[ ] No noindex / disallow blocking crawl

14. Budget Guardrails
Free / low-cost (do first):
Meta tags, schema, canonical — dev time only
Google Business Profile — free
GSC, Bing Webmaster Tools, GA4 — free
Internal linking improvements — content time
Paid investments (justify with ROI):
Original photography — $500–$1,000 for a strong OG image library
Page speed optimization — $500–$2,000
Outsourced writing — $100–$300/article (use only for volume; E-E-A-T pages stay in-house)
SEO tools (Ahrefs, Semrush) — $100–$200/month

15. Operating Rules (Short Version)
Every page gets a keyword owner before it ships.
Every page passes the Section 13 checklist before it ships.
Every page names real local entities.
Every page links in three directions — up, down, across.
Every seasonal page refreshes annually on the same URL.
Every AI answer about Cloudcroft is an opportunity — build the page that gets cited.
Photograph everything. Stock is banned on editorial.
Two sites, two lanes. No cannibalization. Cross-link intentionally.
90-day launch velocity is the moat. Do not slow down.
The goal is not 25 keywords. The goal is the authoritative answer.

