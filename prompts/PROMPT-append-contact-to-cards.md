# PROMPT: Append Contact Info to Restaurant Cards

## Objective

For each restaurant card in `eat/complete-guide-where-to-eat-in-cloudcroft-2026.html`, append a contact-info block at the bottom of the card containing three fields: **street address**, **website**, and **phone number**. Pull the data from the corresponding `.md` content file in `eat-md/`.

---

## HTML pattern to insert

Each card ends with `</p>` followed by the closing `</div>` and `</a>`. Insert a `<div class="lodge-card-contact">` block between the `</p>` and the closing `</div>`, using this format:

```html
<div class="lodge-card-contact">
    <span>&#x1F4CD; [Street Address]</span>
    <span>&#x1F4DE; [Phone Number]</span>
    <span>&#x1F310; <a href="[Website URL]" target="_blank" rel="noopener">[Display Domain]</a></span>
</div>
```

**Rules:**
- If a field is missing or marked "not confirmed" / "none confirmed" in the .md file, **omit that span entirely** — do not insert a placeholder.
- If the website is a Facebook page, use the Facebook URL and display "Facebook" as the link text.
- Strip `https://www.` from display domains for brevity (e.g., `cloudcroftbrewing.com` not `https://www.cloudcroftbrewing.com/`).
- If a card already has a `lodge-card-contact` div, **replace it** with the new standardized version rather than adding a second one.

---

## Card-to-file mapping

Work through each card in source order. The HTML comment above each card names the restaurant.

| # | Card (HTML comment) | .md source file | Notes |
|---|---|---|---|
| 1 | Eighteen99 | `eighteen99-content.md` | |
| 2 | Cloudcroft Brewery | `eat-brewery.md` | |
| 3 | Mad Jack's Mountaintop BBQ | **no .md file** | See fallback data below |
| 4 | Dusty Boots Café | `dusty-boots-cafe-content.md` | |
| 5 | Black Bear Coffee Shop | `black-bear-coffee-shop-content.md` | Already has malformed contact div — replace |
| 6 | Cloudcroft Sandwich Shop | `cloudcroft-sandwich-shop-content.md` | |
| 7 | Western Bar & Cafe | **no .md file** | See fallback data below; already has partial contact div — replace |
| 8 | Brother-N-Law BBQ | **no .md file** | See fallback data below |
| 9 | Big Daddy's Diner | **no .md file** | Already has partial contact div — replace |
| 10 | High Rollin' Coffee | **no .md file** | See fallback data below |
| 11 | Noisy Water Winery | **no .md file** | See fallback data below |
| 12 | Dave's Café | `daves-cafe-content.md` | Website field = Facebook |
| 13 | Old Barrel Tea Company | `old-barrel-tea-company-content.md` | |
| 14 | Eight the Cake | `eight-the-cake-content.md` | Already has partial contact div — replace |
| 15 | Ski Cloudcroft Food Service | `ski-cloudcroft-food-service-content.md` | |
| 16 | Levain It Up | `levain-bakery-content.md` | |
| 17 | Fernando's | **no .md file** | Already has partial contact div — replace |
| 18 | KennaBelles Kreations | `kennabelle-bakery-content.md` | Already has partial contact div — replace |

---

## Fallback data for restaurants without .md files

Use these values for cards that have no corresponding content file. These come from the individual HTML restaurant pages and public listings.

**Mad Jack's Mountaintop BBQ**
- Address: 105 James Canyon Hwy, Cloudcroft, NM 88317
- Phone: (575) 682-7577
- Website: https://www.madjacksbbq.com/

**Western Bar & Cafe**
- Address: 304 Burro Ave, Cloudcroft, NM 88317
- Phone: (575) 682-2445
- Website: westernbarandcafe.net (found in HTML page)

**Brother-N-Law BBQ**
- Address: 209 James Canyon Hwy, Cloudcroft, NM 88317
- Phone: (215) 858-0400
- Website: https://brothernlawbbq.com/

**Big Daddy's Diner**
- Address: 1705 James Canyon Hwy, Cloudcroft, NM 88317
- Phone: (575) 682-1224
- Website: none — omit

**High Rollin' Coffee**
- Address: 109 James Canyon Hwy, Cloudcroft, NM 88317
- Phone: not confirmed — omit
- Website: none confirmed; Facebook page (facebook.com/p/High-Rollin-Coffee-61550359681157) is primary online presence

**Noisy Water Winery**
- Address: 505 Burro Ave, Ste 105, Cloudcroft, NM 88317
- Phone: (575) 682-6610
- Website: https://noisywaterwinery.com/

**Fernando's**
- Address: not confirmed — omit
- Phone: not confirmed — omit
- Website: not confirmed — omit

---

## Data to pull from each .md file

Open the `.md` file and look in **Section 2: Verified business facts** for these fields:
- **Address** → use the value after `**Address:**` or `**Location:**`
- **Phone** → use the value after `**Phone:**`
- **Website** → use the value after `**Website:**` or `**Official website:**`
  - If the field says "not confirmed" or "none confirmed," check for a Facebook URL in the same section and use that instead.
  - If no Facebook URL either, omit the website span.

---

## CSS to add

Add this CSS block inside the existing `<style>` tag in the `<head>`:

```css
.lodge-card-contact {
    margin-top: auto;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(0, 0, 0, 0.08);
    font-size: 0.8rem;
    line-height: 1.8;
    color: #555;
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
}
.lodge-card-contact a {
    color: #2a7d4f;
    text-decoration: none;
}
.lodge-card-contact a:hover {
    text-decoration: underline;
}
```

---

## Execution checklist

1. Add the CSS block to `<style>` in `<head>`.
2. For each of the 18 cards, in source order:
   a. Read the corresponding .md file (or use fallback data).
   b. Extract address, phone, website.
   c. Build the `lodge-card-contact` div with only the spans that have data.
   d. If a `lodge-card-contact` div already exists, replace it.
   e. If none exists, insert it after the `</p>` and before the closing `</div>`.
3. After all 18 cards are done, verify the total count of `lodge-card-contact` divs equals 18 (or 17 if Fernando's has no data at all).
4. Spot-check three cards against their .md source to confirm accuracy.
