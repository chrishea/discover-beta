# eat/eat-md inventory

Quick map of markdown sources to published HTML pages, since file naming is inconsistent.

## Pairings (MD → HTML)

| Markdown source | Published HTML |
|---|---|
| `big-daddy.md` | `eat/big-daddys.html` |
| `black-bear-coffee-shop-content.md` | `eat/black-bear-coffee-shop.html` |
| `brewery.md` | `eat/brewery.html` |
| `brother-n-law-bbq.md` | `eat/brother-n-law-bbq.html` |
| `cloudcroft-dining-guide.md` | `eat/complete-guide-where-to-eat-in-cloudcroft.html` |
| `cloudcroft-sandwich-shop-content.md` | `eat/cloudcroft-sandwich-shop.html` |
| `daves-cafe-content.md` | `eat/daves-cafe.html` |
| `dusty-boots-cafe-content.md` | `eat/dusty-boots-cafe.html` |
| `eight-the-cake-content.md` | `eat/eight-the-cake.html` |
| `eighteen99-content.md` | `eat/eighteen99.html` |
| `fernandos-burritos.md` | `eat/fernandos.html` |
| `high-rollin.md` | `eat/high-rollin.html` |
| `kennabelle-bakery-content.md` | `eat/kennabelle-bakery.html` |
| `levain-bakery-content.md` | `eat/levain.html` |
| `mad-jacks-bbq.md` | `eat/mad-jacks-bbq.html` |
| `noisy-water-winery.md` | `eat/noisy-water-winery.html` |
| `old-barrel-tea-company-content.md` | `eat/old-barrel-tea-company.html` |
| `ski-cloudcroft-food-service-content.md` | `eat/ski-cloudcroft-food-service.html` |
| `st-andrews-bar.md` | `eat/st-andrews-bar.html` |
| `western-bar.md` | `eat/western-bar.html` |

## HTML pages with no MD source

- `eat/complete-guide-to-groceries.html` — written directly in HTML, no markdown draft on file.

## MD files with no HTML page

- `eat-intro.md` — short prose snippet, intended as a section excerpt rather than a standalone page.
- `profile-Cloudcroft-2026-story-cloudcroft-brewery.md` — RTF-encoded file (saved from a word processor); needs cleanup before it can be reused. Companion longform piece for `brewery.md`.

## Naming inconsistency

Roughly half the MDs use a `-content.md` suffix (e.g. `daves-cafe-content.md`) and half use a bare slug (e.g. `brewery.md`). HTML filenames don't carry the suffix. New MDs should drop the `-content` suffix to match the HTML slug 1:1.
