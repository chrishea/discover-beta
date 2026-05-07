# Editor Bios — Publishing Playbook

This directory holds the **editorial team pages** for DiscoverCloudcroft.com.
The structure is scaffolded; the people aren't filled in yet. This README
is the step-by-step for going from scaffold to published bios + named
bylines across the site.

## Why this matters (briefly)

The audit recommended replacing the anonymous "DiscoverCloudcroft editors"
byline with named editor pages because:

- **E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)** —
  Google's quality evaluators look for a real human accountable for the content
- Schema.org `Person` and `ProfilePage` types fed by these pages tell search
  engines who's behind the site
- A page bylined by "Chris Hearne — Editor, Lodging" is meaningfully more
  trustworthy than one bylined "DiscoverCloudcroft editors"

## What's in this directory

| File | Purpose |
|------|---------|
| `index.html` | The `/about/editors/` landing page that lists all editors. Currently shows two placeholder cards. |
| `template-editor-bio.html` | The starting template for each individual editor's detail page. **Don't publish this file as-is** — copy it. |
| `README.md` | This file. |

## Step-by-step: publish a new editor

Replace `[name]` with a URL-safe lowercase slug, e.g. `chris-hea` or `j-smith`.

### 1. Create the bio detail page

```bash
cp about/editors/template-editor-bio.html about/editors/[slug].html
```

Open the new file and replace every `[PLACEHOLDER]` token. Search for `[`
to find them — they're listed in the comment at the top of the file. The
critical ones:

- `[NAME]` — full name as it should appear in bylines
- `[ROLE]` — e.g. "Editor — Lodging & Dining", "Founding Editor", "Trails Editor"
- `[SLUG]` — must match the filename (without `.html`)
- `[SHORT_BIO]` — 120 chars, used in meta description and og:description
- `[LONG_BIO]` — 2-3 paragraphs in the body
- `[BEAT_BULLETS]` — what they cover (3-6 list items)
- `[CREDENTIALS]` — background; be honest, don't pad
- `[CONFLICTS]` — disclosures; if none, say so plainly
- `[PHOTO_URL]` — see step 2
- `[PHOTO_ALT]` — descriptive alt text
- `[EMAIL]` — direct contact

### 2. Add the photo

Save the editor's photo as `media/editors/[slug].jpg` (square, at least
400×400, ideally 800×800). Reference it as
`https://discovercloudcroft.com/media/editors/[slug].jpg`
in the `[PHOTO_URL]` token.

If you don't have `media/editors/` yet:
```bash
mkdir -p media/editors
```

### 3. Add a card to the editors index

Open `about/editors/index.html` and:

1. Replace one of the two placeholder `<article class="editor-card placeholder-card">` blocks with a real card pointing at `[slug].html`. Pattern:

```html
<a class="editor-card" href="[slug].html">
    <img class="editor-photo" src="../../media/editors/[slug].jpg" alt="[NAME]">
    <div class="editor-card-body">
        <h2 class="editor-name">[NAME]</h2>
        <p class="editor-role">[ROLE]</p>
        <p>One-line teaser (under ~100 chars). What they cover and why they're qualified.</p>
        <span class="editor-card-arrow">Read full bio &rarr;</span>
    </div>
</a>
```

2. (Once 2+ editors are real) add an `ItemList` JSON-LD block in the `<head>`
   per the comment in `about/editors/index.html`.

### 4. Update bylines on guide pages

Currently 44+ pages carry the byline:

```html
<p class="hero-byline"><strong>DiscoverCloudcroft editors</strong> &middot; Published May 2, 2026 &middot; Last verified May 2026</p>
```

For pages this editor wrote or owns, replace with:

```html
<p class="hero-byline"><strong><a href="/about/editors/[slug].html">[NAME]</a></strong> &middot; Published May 2, 2026 &middot; Last verified May 2026</p>
```

You can do this manually one page at a time, or write a one-off Python
sweep that takes a slug + a list of file paths and rewrites the byline.
A skeleton for the sweep:

```python
import os, re

EDITOR_SLUG = 'chris-hea'
EDITOR_NAME = 'Chris Hearne'
PAGES = [
    'stay/the-lodge-at-cloudcroft.html',
    'stay/complete-guide-to-lodging-in-cloudcroft-new-mexico.html',
    # ... pages this editor owns
]
OLD = r'<strong>DiscoverCloudcroft editors</strong>'
NEW = f'<strong><a href="/about/editors/{EDITOR_SLUG}.html">{EDITOR_NAME}</a></strong>'

for fp in PAGES:
    with open(fp) as f: html = f.read()
    new = re.sub(OLD, NEW, html, count=1)
    if new != html:
        with open(fp, 'w') as f: f.write(new)
        print(f'Updated {fp}')
```

Pages that aren't owned by a single editor should keep the
"DiscoverCloudcroft editors" byline (and link it to the team page):

```html
<p class="hero-byline"><strong><a href="/about/editors/">DiscoverCloudcroft editors</a></strong> &middot; ...</p>
```

### 5. Update the sitemap

Add the new editor URLs:

```xml
<url>
  <loc>https://discovercloudcroft.com/about/editors/[slug].html</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <priority>0.7</priority>
</url>
```

Or regenerate from disk:
```bash
python3 content/sync-feed.py
```

### 6. Verify before commit

- [ ] Photo loads at the URL referenced
- [ ] All `[PLACEHOLDER]` tokens replaced — search the file for `[` to confirm
- [ ] Email in `mailto:` and JSON-LD matches
- [ ] BreadcrumbList JSON-LD has the editor's name
- [ ] Card on `index.html` links correctly
- [ ] Byline updates on guide pages render correctly

### 7. Commit and push

```bash
git add about/editors/[slug].html about/editors/index.html media/editors/[slug].jpg sitemap.xml [pages-with-byline-updates]
git commit -m "Add editor bio: [NAME]"
git push origin main
```

Amplify auto-deploys.

## A note on honesty

Editor bios are an SEO signal, but more importantly they're a **trust
signal**. Don't pad credentials. Don't invent prior work. Don't add a fake
co-editor "for symmetry." If only one person is responsible for the site,
publish one bio and own it. Two unpadded bios beat four padded ones every
time.
