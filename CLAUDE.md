# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static, hand-written HTML website for **DiscoverCloudcroft.com** — a tourism guide to Cloudcroft, NM. There is **no build system, no framework, no package manager, no test suite, and no linter**. Every page is a self-contained `.html` file. The "app" is the set of `.html` files at project root and under content section directories (`stay/`, `eat/`, `do/`, `shop/`, `visit/`, `events/`, `season/`, `resources/`, `about/`, `shelf/`, `profile/`).

## Running locally

```bash
npx serve -l 8000 --no-clipboard
```

This is the configuration in `.claude/launch.json`. Any static file server works; there is no dev server, no hot reload, no compile step.

## Architectural conventions

### Shared vs page-specific code
- **Reusable CSS** lives in `css/common.css` (the single shared stylesheet). `css/fonts.css` handles self-hosted font faces in `fonts/`.
- **Shared JS** is `js/common.js`: header scroll class, mobile hamburger, IntersectionObserver-driven `.visible` fade-ins, stat counter animation, back-to-top, and an auto-dismissing `#beta-modal`.
- **Page-specific CSS** goes in an inline `<style>` block in `<head>` — generally only hero background image/overlay tweaks and one-off layout adjustments. Avoid duplicating rules already in `common.css`; `content/strip-duplicate-css.py` and `content/strip-guide-css.py` enumerate which selectors are considered "already in common.css" and strip them from inline styles.
- Most pages pull Google Fonts (DM Sans, IBM Plex) in addition to `fonts.css`.

### Page templates
Two canonical templates drive most pages:

- **Entity pages** (one business — restaurant, shop, lodging, attraction): spec in `style/ui-entity-page.md`, canonical example `eat/black-bear-coffee-shop.html`. Schema.org type varies by category (`Restaurant`, `LodgingBusiness`, `TouristAttraction`, `LocalBusiness`, `Winery`, etc.).
- **Topic / guide pages** (landing pages, complete guides): spec in `style/ui-entity.md` and `style/ui-topic.md`. Schema.org type is usually `TouristDestination` or `Article`.

Every page must include: HEAD ordering (charset → title → meta description → canonical → OG → Twitter → fonts → stylesheet → Schema.org JSON-LD → inline `<style>`), skip-link, canonical `.site-header`, `.mobile-nav-overlay`, hero with word-span animation, info bar (4 items), main sections, CTA section, standard footer, `js/common.js` script, and a per-page IntersectionObserver that adds `.visible` to animated elements. Full checklist in `style/ui-entity.md`.

### Relative paths by depth
Subpages live one directory deep (`stay/*.html`, `eat/*.html`, etc.). They reference shared assets with `../css/common.css`, `../js/common.js`, `../media/...`. Root-level pages (`index.html`, `cloudcroft-review.html`) use bare paths (`css/common.css`). When creating or moving pages, adjust every asset reference and nav link to match the new depth.

### Nav sync
The top nav and mobile overlay are duplicated into every HTML file. **Do not hand-edit nav in individual pages.** Edit the nav in `content/sync-nav.py` (function `build_nav`), then run:

```bash
python3 content/sync-nav.py
```

The script walks every `.html` file (skipping hidden dirs and `google8739391a40d00bda.html`), computes the correct `../` prefix from directory depth, and rewrites the header + mobile overlay in place via a regex. `index.html` and the other root-level files get an empty prefix.

### Inline-CSS deduplication
When pages accumulate inline CSS that duplicates `common.css`:

```bash
python3 content/strip-duplicate-css.py   # pass 1 — shared components
python3 content/strip-guide-css.py       # pass 2 — guide-page components (TOC, market, lodge, compare, pick, tip)
```

Both scripts walk all `.html` files and rewrite inline `<style>` blocks. Review `DUPLICATE_SELECTORS` / `GUIDE_SELECTORS` in each script before trusting results — they are regex-based and targeted to specific known-duplicate rules.

### Color system (important — ignore the color memo)
The **current** palette in `css/common.css` is intentionally black, white, and grays. CSS variables like `--pine`, `--gold`, `--cta-red`, `--forest-green`, etc., all resolve to `#000000`, `#2B2B2B`, `#333333`, or `#444444`. Legacy variable names (`--midnight`, `--alpine`, `--golden-hour`, `--summit`, `--snow-cap`, `--cloud-drift`, `--granite`, `--twilight`) still exist as aliases and are referenced throughout page CSS and template docs — **keep using the variable names**, but don't assume they carry the warm gold/green meanings described in `md/COLOR-PALETTE-MEMO.md`. That memo documents an earlier palette and is out of date. `#2B2B2B` is the one "dark but not pure black" color used for dark cards and feature blocks.

## Content production workflow

Content for entity and guide pages is drafted as Markdown before HTML:

- **Prompt templates** that drive content+HTML generation: `content-prompt-template.md` (parameterized) and `rearch-build-md-prompt.md` (concrete example). They define a 12-section structure for entity guides (Executive summary → Verified facts → Appearance → type-specific sections → Grounds → History → Experience patterns → What to verify → Who it's for → Source notes → Fact-check notes).
- **Section Markdown sources** live in per-section folders: `stay/stay-md/`, `eat/eat-md/`, `do/do-md/`, `shop/shop-md/`, `events/events-md/`, `visit/visit-md/`, `resources/resources-md/`. These back the published HTML pages.
- **Section photos** live in `stay/stay-photo/photo-<entity>/`, `eat/eat-photo/photo-<entity>/`, etc. Always verify actual filenames on disk (`.jpg` vs `.JPG` vs `.webp`) before writing image references — mixed-case extensions are common and the Markdown templates explicitly warn about this.
- **Content guardrails** (from the templates): never fabricate addresses, phones, hours, rates, or policies; explicitly flag uncertainty; do not use emojis in generated content.
- **Review prompts** (`do/do-md/REVIEW-AND-ENHANCE-PROMPT.md`, `eat/eat-md/PROMPT-*.md`) define how business contact info is audited and reconciled against verified reference data.

## Media

- Source/hero images in `media/` (root-level) and section-specific `*-photo/` directories.
- `optimize-images.sh` resizes JPEGs >2000px wide, compresses to quality 80, and backs up originals to `media-originals/`. Requires ImageMagick.
- Prefer `.webp` variants where both exist.

## Git workflow

- Default branch is `main`. CI / deploy are not configured in this repo.
- Recent history has both merged PR commits and direct commits to main, with a mix of terse/typo messages; copy the style of meaningful recent commits rather than the noisy ones.
- `.gitignore` covers editor junk only; be careful not to commit large binaries (PDFs, raw photos) that don't belong on the site.
