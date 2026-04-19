# Topic Pages — Consistency Audit
DiscoverCloudcroft.com · seven "Complete Guide" / "Guide to" pages
Audit date: 2026-04-19

## Files audited

| Code | File | Dir |
|---|---|---|
| MAIN | complete-guide-to-cloudcroft-new-mexico-2026.html | / |
| SHOP | complete-guide-where-to-shop-in-cloudcroft-2026.html | /shop |
| DO | complete-guide-to-activities-to-do-in-cloudcroft-2026.html | /do |
| STAY | complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html | /stay |
| EAT | complete-guide-where-to-eat-in-cloudcroft-2026.html | /eat |
| CAMP | guide-to-camping-cloudcroft-new-mexico-2026.html | /do |
| HIKE | guide-to-hiking-in-cloudcroft-new-mexico-2026.html | /do |

Baselines: `css/common.css` and `js/common.js` load on every file. `common.css` defines the shared hero, header, footer, section, CTA, and color tokens (`--pine`, `--gold`, `--alpine`, `--midnight`, `--snow-cap`, etc. — all currently resolving to black, white, or gray per `:root`). These findings are about what each page layers on top in inline `<style>`.

---

## Consistency Scorecard

Cells flagged with ⚠ diverge from the majority. Cells with ✅ match the majority pattern.

| Dimension | MAIN | SHOP | DO | STAY | EAT | CAMP | HIKE |
|---|---|---|---|---|---|---|---|
| **Structure** | ⚠ Uses `.guide-section` numbered (01, 02…) + `.hero-meta` inside hero (not info-bar). TouristDestination + FAQPage + BreadcrumbList JSON-LD. 2,597 lines. | ✅ `.section`/`.section-alt`, `.toc-nav` (5 pills), `.info-bar` (4 items), Article JSON-LD. Canonical guide shape. | ✅ Same as SHOP + `.toc-nav` (6 pills). Article JSON-LD. Info-bar **6 items** ⚠. | ✅ Same shape, `.toc-nav` (6 pills). Article JSON-LD. Info-bar **3 items** ⚠. | ✅ Same shape, `.toc-nav` (5 pills). Article JSON-LD. Info-bar **2 items** ⚠. | ⚠ **No TOC.** Custom `.campground-card`, `.resource-card`, `.tip-card`, `.camp-badge` system. TouristAttraction JSON-LD. | ⚠ **No TOC.** Custom `.menu-card`/`.menu-grid` + `.gallery-grid` (only file with gallery). TouristAttraction JSON-LD. |
| **Typography** | ⚠ H2 inline rule has a **broken font-family**: `'IBM Plex serif, sans-serif;` (unclosed quote, nonsense stack — falls back to sans). H1 `clamp(1.85–3.75rem)` — smaller than common.css default. | ✅ Relies on `common.css` baseline: Plex Serif H1 `clamp(2.5–4rem)`, Plex Sans body, no H2 override. | ✅ Same as SHOP. | ✅ Same as SHOP. | ✅ Same as SHOP. Body color override `#555`. | ✅ Plex Sans baseline + `.camp-type-header h3` at 1.6rem. Legacy variable usage is extensive but resolves identically. | ✅ Plex Sans baseline + custom `.menu-card h3` sizing. |
| **Color** | ⚠ Adds `#c8943e` golden focus-outline; references `var(--alpine, #3a6b1e)` fallback green (dead code — variable is #333). | ⚠ **Purple hero gradient** `#2d1b4e → #1a1035 → #3d2066` — only file with chromatic hero. | ⚠ Hero badge inline `rgba(255,255,255,0.7)` (transparent white — unique). | ⚠ **Green checkmark `#2e7d32`** + **amber warning `#e6a200`** in `.pros-cons` — only file using these live. | ⚠ **Light-green badge** `rgba(185,228,190,0.6)` + darker overlay `rgba(0,0,0,0.55/0.35)`. Body `#555`, links `steelblue`. | ⚠ Same `#2e7d32` green / `#e6a200` amber as STAY. Heavy legacy variable usage. | ✅ Pure B/W/gray, no custom hex beyond common.css tokens. |
| **Visual elements** | Photo hero (`media/artemis-earth copy.jpg`), numbered section badges, no card images, stat/counter blocks. | ⚠ **Gradient-only hero** (no photo). Text-only `.lodge-card`s. | Photo hero (pickleball), **emoji icons** in info-bar, `.lodge-card-image` w/ 16:9. | Photo hero (The Lodge), `<img>` inside `.lodge-card`, emoji icons, `.pros-cons` 2-col grid w/ SVG-style checkmarks. | Photo hero (chicken-fried steak), `<img>` cards w/ `.lodge-card-link` wrapper, emoji icons. | ⚠ **No photos** — gradient placeholders only. Custom badge system (3 variants). Emoji icons. | ⚠ Photo hero + **photo gallery grid** (`.gallery-grid`) — only file with one. 12 trail cards with trail photos. Emoji icons. |
| **Tone / formatting** | Title Case H2. Steelblue links via common.css. No "Last updated." `og:type=article`, custom `og:image`. | Title Case. Mixed bullet/ordered lists. No citations. `og:type=website`, og-default.webp. | Title Case. Both list types. `og:type=website`, og-default.webp. | Title Case. ⚠ **Broken nav paths** — subpage nav refers to root files as `index.html` / `eat/…` instead of `../index.html` / `../eat/…`. `og:type=website`. | Title Case. Custom link color `steelblue` w/ hover underline. `og:type=website`. | Title Case. ⚠ Links rendered `var(--alpine)` = #333 (no blue). Forest Service contacts surfaced inline. `og:type=website`. | Title Case. `og:type=website`. No citations section; credits embedded in cards. |

---

## What's Consistent Across All Seven

Stated plainly, what every page does the same:

- Loads `css/fonts.css`, `css/common.css`, and both IBM Plex families from Google Fonts (`IBM Plex Sans` 400/500/700 + `IBM Plex Serif` 400/700).
- Runs `js/common.js` (header scroll class, mobile hamburger, `.visible` IntersectionObserver, stat counter, back-to-top, `#beta-modal`).
- Includes a skip-to-content link, `.site-header` with logo + primary nav, `.mobile-nav-overlay`, and `.site-footer`.
- Uses a full-bleed `.hero` with `.hero-bg`, `.hero-overlay`, centered `.hero-content`, an H1 with `.word` span animation, and a subtitle.
- Uses Title Case for H1 and H2 headings.
- Ends with a CTA block (custom section styled to lead into "plan your trip").
- Includes a JSON-LD schema block in `<head>` (type varies).
- Includes OG and Twitter card meta tags, a canonical link, and a meta description that leads with action ("Plan …", "Where to eat …", "Find the best …").
- Treats the TOC-like navigation (when present) as pill buttons, not an HTML `<nav>` with bullets.
- Animates section entry via the `.visible` observer class rather than CSS-only keyframes.

The palette inherited from `css/common.css` is intentionally monochrome — black (`--pine: #000`, `--midnight: #000`), charcoals (`--granite: #444`), a 5% gray (`--cloud-drift: #f2f2f2`), and white (`--snow-cap: #fff`). The CSS variable names imply a warm alpine palette; the `md/COLOR-PALETTE-MEMO.md` describes that earlier design. The current baseline is B/W/gray.

---

## What Diverges, and Where

### Dimension 1 — Structure

- **Info-bar item count.** SHOP/CAMP/HIKE use 4 items. MAIN swaps `.info-bar` for `.hero-meta` inside the hero (3 items). STAY = 3. EAT = 2. DO = 6. Majority = 4.
- **TOC presence.** MAIN/SHOP/DO/STAY/EAT ship a `.toc-nav` pill row (5 files). CAMP and HIKE omit it entirely.
- **Section class naming.** SHOP/DO/STAY/EAT/CAMP/HIKE use `.section` and `.section-alt` (alternating backgrounds). MAIN uses `.guide-section` with numbered badges ("01 / Overview"). Majority = `.section` / `.section-alt`.
- **JSON-LD @type.** Article for SHOP/DO/STAY/EAT. TouristDestination + BreadcrumbList + FAQPage for MAIN. TouristAttraction for CAMP/HIKE. There is no single majority; the four topic-guides agree on Article.

### Dimension 2 — Typography

- **H2 treatment.** MAIN declares its own H2 rule with a typo: `font-family: 'IBM Plex serif, sans-serif;` (line 364). The unclosed single quote renders as an invalid declaration; the browser drops it and falls back to `sans-serif`. The other six inherit from `common.css`, where the hero title is Plex Serif 700 but H2 in sections is the default body stack (Plex Sans) unless a page overrides.
- **Hero H1 sizing.** `common.css` sets `clamp(2.5rem, 5vw, 4rem)`. MAIN narrows to `clamp(1.85rem, 1.2rem + 4.2vw, 3.75rem)`. The other six use the default.
- **Body color.** EAT sets body `#555`; the rest inherit `#333` (common.css).

### Dimension 3 — Color

- **Hero background.** SHOP is a purple CSS gradient (`#2d1b4e → #1a1035 → #3d2066`). MAIN/DO/STAY/EAT/HIKE use a photograph with the shared overlay. CAMP uses a gradient only (no photo).
- **Hero badge.** DO = `rgba(255,255,255,0.7)` (transparent white). EAT = `rgba(185,228,190,0.6)` (light green). MAIN/SHOP/STAY/CAMP/HIKE use the default opaque badge defined in `common.css`.
- **Accent colors in body content.** STAY and CAMP introduce `#2e7d32` (green) and `#e6a200` (amber) for checkmarks / warnings. No other file uses them.
- **Hero overlay opacity.** Common default is `rgba(0,0,0,0.6)` → `rgba(0,0,0,0.3)`. SHOP lightens to `0.3 → 0.15`. EAT darkens to `0.55 → 0.35`. Others use the default or a near-default.
- **Dead-code color reference.** MAIN references `var(--alpine, #3a6b1e)` as a fallback; `--alpine` actually resolves to `#333333`, so the green hex is never rendered but remains in source.

### Dimension 4 — Visual elements

- **Photographic hero vs. gradient.** Photo: MAIN/DO/STAY/EAT/HIKE. Gradient-only: SHOP, CAMP.
- **Card images.** Image-bearing cards: DO (`.lodge-card-image` 16:9), STAY (`<img>` inside `.lodge-card`), EAT (`<img>` + `.lodge-card-link` wrapper), HIKE (`.trail-photo` 16:9). Text-only cards: MAIN, SHOP, CAMP.
- **Emoji icons in info-bar.** Present in DO/STAY/EAT/CAMP/HIKE. Absent in MAIN/SHOP.
- **Unique components.** `.pros-cons` grid (STAY only). `.campground-card` / `.resource-card` / `.camp-badge` (CAMP only). `.menu-card` / `.gallery-grid` / `.gallery-item` (HIKE only). `.section-number` / `.section-label` pills (MAIN only).

### Dimension 5 — Tone & formatting

- **Link color.** Common.css ships `steelblue`. EAT reaffirms it explicitly on `.lodge-card-contact a`. CAMP overrides on `.campground-link` to `var(--alpine)` (= #333). Others inherit default.
- **Bullet vs. numbered.** MAIN and DO mix numbered and bulleted lists purposefully (numbered for priority). CAMP uses a tag/badge system in place of lists.
- **Citations / footnotes / last-updated.** None of the seven files carry a "Last updated" stamp or a formal sources/citations section. HIKE embeds Forest Service contact info inside trail cards; CAMP embeds reservation URLs in resource cards. The rest have no source attribution visible on-page.
- **OG type.** MAIN = `article`; all others = `website`. OG image: MAIN points at `placeholder-hero-main.webp`; the others all fall back to `og-default.webp`.
- **Subpage nav paths.** STAY's copy of `.site-header` references root-level pages as `index.html`, `eat/…`, etc. — missing the `../` prefix the other subpage files use. This is a functional bug, not a style choice. `content/sync-nav.py` exists specifically to prevent this; it appears STAY was edited after the last sync run or was hand-edited.

---

## Outliers

- **MAIN** — distinct on *three* dimensions: unique section naming (`.guide-section` numbered badges instead of `.section`/`.section-alt`), unique hero-meta variant instead of `.info-bar`, and a literally broken H2 font-family declaration. Feels like a different template generation — likely the oldest or newest of the set.
- **CAMP** — distinct on *five* dimensions: no TOC, no photos, unique card-system vocabulary, extensive legacy variable usage, and live green/amber accents. Reads as a reference/resource page rather than a narrative guide.
- **HIKE** — distinct on *three* dimensions: no TOC, unique `.menu-card` vocabulary, and the only page with a photo gallery grid. Reads as a trail index, not a guide.
- **SHOP** — the only file with a chromatic hero (purple gradient). Otherwise conforms to the guide template.
- **EAT** — minor on its own, but accumulates three small divergences (2-item info-bar, green badge, darker overlay, body `#555`).

---

## Recommended Standardization Priorities

Ranked by impact, with rationale grounded in the files above.

1. **Fix the broken H2 rule in MAIN (line 364).** One-line syntax error nukes the intended H2 styling across the flagship page. Unclosed quote in `font-family: 'IBM Plex serif, sans-serif;`. High impact, zero risk.
2. **Choose one section-naming convention.** MAIN is the only page using `.guide-section` with numbered badges; the other six use `.section` / `.section-alt`. Pick one (majority = `.section`/`.section-alt`) and convert MAIN, or keep MAIN's system and migrate the others. Today the convention is 6-to-1, so converting MAIN is the cheaper move.
3. **Standardize the info-bar.** Decide 4 items vs. 3 vs. 6 vs. 2. Four is the most common value when you count SHOP/CAMP/HIKE together (three files at 4). Decide whether emoji icons are in or out — right now DO/STAY/EAT/CAMP/HIKE use them and MAIN/SHOP don't. Emoji is the 5-to-2 majority.
4. **Decide whether TOC is required.** Five files ship it, two (CAMP/HIKE) don't. These two are the longest-form non-guide pages, so a legitimate case exists to exempt them — but that exemption should be documented in `style/ui-topic.md`, not implicit.
5. **Pick one JSON-LD type per page class.** The four topic-guides agree on `Article`; MAIN uses `TouristDestination`; CAMP/HIKE use `TouristAttraction`. Either codify "guides = Article, single-topic reference pages = TouristAttraction, the flagship = TouristDestination," or unify. Current state is decipherable but inconsistent.
6. **Retire or normalize the inline color overrides.** SHOP's purple hero is the single most visible divergence. If color is returning to the palette, do it through `common.css` and the `:root` tokens; if not, remove the purple gradient. Same logic for EAT's green badge and the `#2e7d32` / `#e6a200` pair in STAY/CAMP.
7. **Run `sync-nav.py`.** STAY's nav paths are wrong from the subpage depth. This is a mechanical fix the repo already has tooling for.
8. **Add a "Last updated" stamp and a sources/citations convention.** No file carries either today. For 2026-dated guides, this is the lowest-effort credibility lift available.

Items 1 and 7 are mechanical bug fixes. Items 2–4 are template decisions. Items 5–6 are content/design governance. Item 8 is new surface area.
