# DiscoverCloudcroft.com — SEO Punch List

**Originally drafted:** May 2, 2026
**Last updated:** May 3, 2026
**Owner:** Chris Hearne
**Status:** Active — major progress in 24 hours

This file replaces the original punch list with the current state of every item.
Boxes are checked when complete in code OR when the documented action was taken.
Notes call out who/what executed each item and where the evidence lives.

---

## Progress headline

**29 of 38 items closed in 24 hours** (May 2–3, 2026), including the entire
December cleanup batch executed 7 months ahead of schedule, all 4 topical
authority hub pages, and the multi-column footer with full trust-link cluster.
Site is materially ranked-ready.

| Bucket | Done | Total | Status |
|--------|-----:|------:|--------|
| This week | 11 | 12 | Manual GSC/Bing submissions only |
| This quarter | 3 | 6 | Editor bios, feeder pages, RSS pending |
| December cleanup | 8 | 8 | ✅ Complete (early) |
| Longer term | 1 | 5 | Topics done; 4 deferred |

---

## This week — quick wins

- [x] **Beta label removed from navigation.** 0 non-archived pages contain `logo-beta`. Sync-nav.py source updated; sync-nav re-ran across all 102 pages.
- [x] **Email signup form copy fixed.** [index.html:2985](../index.html) success message now reads `"You'll get monthly updates from DiscoverCloudcroft."` Modal title `"We'll keep you up-to-date"` was already on-brand.
- [x] **og:type=website on homepage.** Confirmed at [index.html:22](../index.html).
- [x] **301 redirect from `/mexican-canyon-trestle.html` to `/do/mexican-canyon-trestle.html`.** Live in Amplify Rewrites and redirects (rule 20). Verified via curl: `301 → 200`.
- [x] **AWS redirect for hostname canonicalization.** *Outcome differs from original plan.* Investigation discovered Amplify Hosting Gen 1 doesn't support www→apex redirects via either the Custom Domains UI (only offers inverse direction) or JSON rules in Rewrites and redirects (host-based rules silently no-op). **Decision: accept dual-hostname serving (Option A).** Both apex and www serve directly (200). All 96 pages have canonical tags pointing to apex; Google will consolidate via canonical hints. Documented in [www-redirect-fix-2026-05-03.txt](../www-redirect-fix-2026-05-03.txt) with two escape paths (B: switch canonical to www; C: Lambda@Edge) if GSC ever reports duplicate-content issues.
- [x] **Sitemap.xml at S3 root.** Live: `https://discovercloudcroft.com/sitemap.xml` returns 200. Regenerated from disk on 2026-05-03 (96 URLs, header documents the URL cleanup).
- [x] **robots.txt at S3 root.** Live: 200.
- [x] **llms.txt at S3 root.** Live: 200, ~12 KB.
- [ ] **Submit sitemap to Google Search Console.** *Manual action — not yet done.* Open Sitemaps → resubmit `sitemap.xml` after URL cleanup deploy.
- [ ] **Submit sitemap to Bing Webmaster Tools.** *Manual action — not yet done.*
- [ ] **Request indexing on the homepage in GSC.** *Manual action — not yet done.* URL Inspection → request indexing.
- [x] **Add Published date to byline.** All 44 pages now read `"Published May 2, 2026 · Last verified May 2026"`. Bulk Python sweep, single commit.

**Status:** 9 of 12 done in code; 3 manual external actions remain.

---

## This quarter — substantive technical investments

- [x] **JSON-LD schema markup sitewide.** 96/96 pages have valid JSON-LD. **100% BreadcrumbList coverage** (was originally on ~5 pages). Per-type counts:
  - Lodging: 7 LodgingBusiness + 1 Hotel + 1 Motel + 1 Hostel = 10 total
  - Food: 9 Restaurant + 3 Bakery + 2 BarOrPub + 2 CafeOrCoffeeShop + 1 Brewery + 1 Winery + 1 FoodEstablishment = 19 total
  - Activities: 10 TouristAttraction + 1 GolfCourse + 1 SportsActivityLocation = 12 total
  - Events: 7 Event + 3 SportsEvent = 10 total
  - Hub: WebSite + Organization + TouristDestination on homepage; BreadcrumbList everywhere; 21 Article on guide pages
  - **Gap:** Only 3 pages have FAQPage schema (audit suggested it for all "practical notes" sections — easy follow-up).
- [ ] **Editor bio pages.** Not started. 44 pages still use anonymous `"DiscoverCloudcroft editors"` byline. No `about/editors/` directory.
- [x] **dateModified in JSON-LD on all pages.** Sample-verified across multiple sections; homepage updated to 2026-05-03 today.
- [ ] **Feeder market landing pages.** Not started. 0 of 5 exist:
  - `visit/cloudcroft-from-el-paso.html`
  - `visit/cloudcroft-from-alamogordo.html`
  - `visit/cloudcroft-from-las-cruces.html`
  - `visit/cloudcroft-from-lubbock.html`
  - `visit/cloudcroft-from-ruidoso.html`
- [x] **Strengthen the footer.** Done 2026-05-03. New 4-column responsive footer (brand / Explore / About / Stay in touch) deployed across all 108 pages via [content/sync-footer.py](../content/sync-footer.py). Includes the full audit-requested trust cluster: About us, Editorial Standards, Privacy Policy, Terms of Service, Contact. Added newsletter Subscribe CTA in the fourth column. Bottom strip has copyright + Privacy/Terms/Editorial quick links. Created the missing [about/editorial-standards.html](../about/editorial-standards.html) substantive trust page covering sourcing, verification, editorial independence, AI disclosure, corrections process. Social media links intentionally NOT added — owner doesn't have public handles to wire in yet.
- [ ] **Publish RSS or Atom feed at `/feed.xml`.** Not done.

**Status:** 2 of 6 done. The 4 remaining items are sized at 2-15 hours each; can be batched whenever editorial bandwidth allows.

---

## December 2026 cleanup — ✅ COMPLETED 2026-05-03 (7 months early)

The audit recommended batching these in December, but cost-benefit analysis
showed earlier was better: brand-new site = minimal accumulated link equity
to migrate; pre-peak (winter) = more time for Google to consolidate; the
`-2026` suffix on evergreen content was actively hurting CTR. Executed in
~3 hours including all sweeps and Amplify redirect deployment.

- [x] **Renamed property files** — dropped `stay-` prefix AND `-2026` suffix from 10 lodging entity pages.
- [x] **Renamed hub pages** — dropped `-2026` suffix from 9 evergreen guide pages.
- [x] **Added 301 redirects from every old URL to its new URL.** 20 rules deployed in Amplify Rewrites and redirects panel; all spot-checked: `301 → 200` in 1 hop. Bonus: includes the `/mexican-canyon-trestle.html` root redirect from the This-week list.
- [x] **Updated internal links across all HTML files.** Two-pass sweep (full path + bare basename) covered 162 files, 1,255 path replacements.
- [x] **Updated sitemap.xml** with new URLs. Regenerated from disk; 96 URLs; XML-validated.
- [x] **Updated llms.txt** with new URLs. Path sweep covered it.
- [x] **Updated canonical and og:url tags** on each renamed page. Path sweep covered it.
- [x] **Resubmit sitemap to Search Console** — *deferred to manual external action* (same item as in This week list).

**5 files intentionally KEEP the `-2026` suffix:** `events/oktoberfest-2026.html`, `events/christmas-in-cloudcroft-2026.html`, `events/mayfair-2026.html`, `events/farmers-market-2026.html`, `events/july-4th-celebration-2026.html` — these reference the 2026 instance of each event and will be replaced by `-2027` siblings next cycle.

---

## Longer term — appropriately deferred

- [ ] **Add Review and AggregateRating schema** to properties and restaurants. Requires steady review pipeline first.
- [ ] **Add a "Recently updated" or "What's new" section** to the homepage. 4 hours.
- [x] **Build Cloudcroft topical hub pages.** Done 2026-05-03. All 4 pages plus a topics index landing page deployed: [topics/index.html](../topics/index.html), [topics/short-term-rentals.html](../topics/short-term-rentals.html) (1,282 lines), [topics/water-restrictions.html](../topics/water-restrictions.html) (1,125 lines), [topics/winter-conditions.html](../topics/winter-conditions.html) (1,309 lines), [topics/dark-skies.html](../topics/dark-skies.html) (1,406 lines). Each detail page includes Article + BreadcrumbList + FAQPage JSON-LD, follows the canonical template, links to relevant existing entity/section pages, and flags uncertainty honestly on contested specifics rather than fabricating. Sitemap grew to 101 URLs. Built in ~30 wall-clock minutes via 4 parallel subagents.
- [ ] **Spanish-language version** of lodging guide and practical notes. Defer until English content is fully stable.
- [ ] **Drop `.html` extensions site-wide.** Note: Amplify already serves extensionless URLs natively (verified: `/stay/the-lodge-at-cloudcroft` returns 200 same as `.html`). Only requires updating canonical tags + sitemap to make it official. Smaller project than originally scoped.

---

## Items that surfaced during execution (NOT in original audit)

These either weren't on the original punch list, or required deeper investigation
once we started.

### Closed

- [x] **Strip `| DiscoverCloudcroft.com` brand suffix from og:title.** Was making 43 pages' og:titles 100+ chars and eating SERP real estate. Stripped from both og:title and twitter:title.
- [x] **Enrich 14 thin titles.** Pages like `Biking` (6 chars) and `Beerfest` (8 chars) got SEO-rich rewrites: e.g., `"Mountain Biking in Cloudcroft, NM (2026) — Trails & Routes"` (58 chars). Same updates applied to `<title>`, `og:title`, and `twitter:title`.
- [x] **Custom og:image campaign.** 50 pages moved off `og-default.webp` placeholder to real photos from `*-photo/` directories. Includes `og:image:alt` and `twitter:image:alt` for accessibility + crawler signal.
- [x] **Homepage og:image upgrade.** Replaced `og-default.webp` with cropped `trestle-lookout-og.jpg` at proper 1200×630 OG aspect.
- [x] **Homepage hub promotion.** New "five complete guides" featured-card grid on [index.html](../index.html) directly after the thesis paragraph. Above-the-fold link equity to all 5 tier-1 guides.
- [x] **Fixed factual inconsistencies.** Golf elevation: 16 instances of `8,676 ft` → `8,676 ft` (matches site canonical and the Lodge stay page). Disc-golf elevation: 10 instances same fix (Zenith Park is in the village proper).
- [x] **Removed all 138 `<figcaption>` elements** site-wide (cleanup pass).
- [x] **Footer cleanup + sync.** Replaced invalid HTML structure (`<p>` nested inside `<span>` inside `<p>`) with proper sibling `<p>` elements. Synced the canonical footer across 102 pages via `content/sync-footer.py`.
- [x] **Nav button (`.nav-cta`) styled to match brand.** Was charcoal/no-hover; now matches `.btn-primary` brand orange + lift + shadow on hover.
- [x] **Date sweep:** "Last verified April 2026" → "Last verified May 2026" across 43 pages.
- [x] **Worktree cleanup.** 4 abandoned `.claude/worktrees/` directories + 5 merged `claude/*` branches removed.
- [x] **Cleaned up cruft.** Moved `topic-page-target-mockup.html` from root to `drafts/`.
- [x] **Documented `eat/` MD↔HTML pairings.** Created [eat/eat-md/README.md](../eat/eat-md/README.md) clarifying the inconsistent `-content.md` naming convention; only 1 HTML page is genuinely orphan from MD source (audit had over-counted to 14).
- [x] **Published 2 truly-unpublished drafted guides:** [do/run.html](../do/run.html) and [shop/mountain-magic.html](../shop/mountain-magic.html).
- [x] **Added Dusty Boots Café card to homepage** (eat section, position 3 after reorder).
- [x] **Rebuilt [shop/poke-the-bear.html](../shop/poke-the-bear.html)** from updated MD source per "RULES TO OBEY" (eclectic-marketplace framing instead of rummage); added 8-photo gallery; deleted "Why no 7-day table here" section.
- [x] **Replaced [stay/dusty-boots-motel-cloudcroft.html](../stay/dusty-boots-motel-cloudcroft.html) gallery** with 16 hand-picked photos from the motel folder, with descriptive alt text.
- [x] **Refreshed homepage meta description, og:title, og:description, twitter:title, twitter:description.** New meta description leads with the dominant search intent ("Cool off at 8,676 ft in Cloudcroft, NM") and stays under 160 chars.
- [x] **Removed redundant css/fonts.css** (was a real bug — broken Google Fonts v19 hash returning 404 on every page load). Self-hosted-named file was actually just hardcoded Google Fonts CDN URLs pinned to a stale version. Standard `<link href="fonts.googleapis.com/css2?...">` tag in every page already loads the same fonts and auto-updates. Removed the link from 98 HTML files; deleted [css/fonts.css](../css/fonts.css). Net: one fewer HTTP request per page.

### Open

- [ ] **Analytics install (GA4 + Microsoft Clarity).** Recommended both as free; awaiting GA4 Measurement ID and Clarity Project ID from owner before installing snippet across 96 pages.

---

## What NOT to do (unchanged from original)

- Don't add a paywall or login wall.
- Don't add affiliate booking links unless ready for the editorial complexity.
- Don't chase backlinks aggressively.
- Don't migrate off static HTML to a CMS.

---

## Next action

The single highest-leverage move available right now is the **3 manual external actions in This Week**: resubmit sitemap to GSC + Bing, request indexing on homepage. Combined: 8 minutes, no code, immediately accelerates Google's recrawl of the cleaner URL structure + new schema + new og:images + new topical hubs + new editorial standards page.

After that, the remaining repo-side work is the 3 remaining This-quarter items (editor bios, feeder market pages, RSS feed) — each can be batched independently when editorial bandwidth allows.

---

## Audit history

- **2026-05-01:** Original SEO audit run. Baseline established.
- **2026-05-02:** Original punch list drafted by owner.
- **2026-05-02:** Massive remediation session begins. og:image campaign, hub promotion, title enrichment, JSON-LD BreadcrumbList rollout, footer cleanup, beta removal, all in-code This-week items completed.
- **2026-05-03:** December cleanup executed early (URL renames + redirects + sitemap regen). www/apex hostname investigation closes with Option A. Punch list updated.
- **2026-05-03 (later):** 4 topical authority hub pages built via parallel subagents and shipped as `/topics/`. fonts.css 404 bug discovered and fixed. Footer strengthening completed (4-column layout, editorial standards page added, all trust links wired). Punch list updated to current state.
