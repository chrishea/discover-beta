# Prompt Template: Discover Cloudcroft Content Generation

This is a reusable prompt template. Values inside `{{DOUBLE_BRACES}}` are placeholders to be populated from a CSV row before sending the prompt.

---

## CSV schema

Each CSV row should supply the following columns (placeholder name = column header):

| Placeholder | Description | Example |
|---|---|---|
| `{{SUBJECT-MATTER}}` | Official business name | `The Cabins at Cloudcroft` |
| `{{SUBJECT-TYPE}}` | Category of business | `Lodging`, `Retail`, `Dining`, `Activity`, `Service` |
| `{{SUBJECT-SHORT-NAME}}` | Short/filename-safe name | `cabins-at`, `new-village-hardware` |
| `{{SUBJECT-URL}}` | Official website URL (if known) | `https://www.cabinsatcloudcroft.com` |
| `{{SUBJECT-ADDRESS}}` | Street address | `1006 Coyote Ave, Cloudcroft, NM 88317` |
| `{{SUBJECT-PHONE}}` | Main phone number | `(575) 682-2396` |
| `{{OUTPUT-CATEGORY}}` | Top-level section directory | `stay`, `shop`, `eat`, `do`, `visit` |
| `{{OUTPUT-MD-FILENAME}}` | Markdown filename (no extension) | `cabins-at`, `new-village-hardware-content` |
| `{{OUTPUT-HTML-FILENAME}}` | HTML filename (no extension) | `stay-cabins-at-cloudcroft`, `shop-new-village-hardware` |
| `{{PHOTO-FOLDER}}` | Photo subfolder name | `photo-cabins-at`, `photo-new-village-hardware` |
| `{{REFERENCE-MD-PATH}}` | Reference markdown style template | `stay/stay-md/stay-dusty-boots-motel-booking-guide.md` |
| `{{REFERENCE-HTML-PATH}}` | Reference HTML visual template | `stay/stay-dusty-boots-motel-cloudcroft.html` |
| `{{EXISTING-PAGE-PATH}}` | Existing page to cross-check (optional; blank if none) | `stay/stay-cabins-at-cloudcroft.html` |
| `{{SECTION-4-HEADING}}` | Section 4 heading (type-specific) | `Rooms and accommodations`, `Products and departments`, `Menu and offerings` |
| `{{SECTION-5-HEADING}}` | Section 5 heading (type-specific) | `Dining and drinking`, `Services offered`, `Food and provisions` |
| `{{SECTION-9-HEADING}}` | Section 9 heading (type-specific) | `What travelers should verify before booking`, `What shoppers should know before visiting` |
| `{{SECTION-10-HEADING}}` | Section 10 heading (type-specific) | `Who should book {{SUBJECT-MATTER}}`, `Who should shop at {{SUBJECT-MATTER}}` |
| `{{AUDIENCE-NOUN}}` | Audience word | `travelers`, `shoppers`, `diners`, `visitors` |
| `{{CTA-VERB}}` | Primary call-to-action verb | `Book`, `Shop`, `Reserve a table`, `Plan a visit` |

---

## PROMPT

You are producing a Discover Cloudcroft content guide in Markdown, plus an accompanying single-file HTML web page. Follow the instructions below exactly.

### 1. Review the reference file for style, tone, and structure

Open and carefully read:

`/Users/chrishea/Library/Mobile Documents/com~apple~CloudDocs/GitHub/discover-beta/{{REFERENCE-MD-PATH}}`

This is your stylistic template. Note its voice: concise, fact-driven, skeptical of unverified claims, and explicit about what is confirmed vs. what needs to be verified. It uses short paragraphs, bulleted fact lists, and flags uncertainty. Mirror that voice and discipline.

### 2. Produce a new Markdown file at exactly this path

`/Users/chrishea/Library/Mobile Documents/com~apple~CloudDocs/GitHub/discover-beta/{{OUTPUT-CATEGORY}}/{{OUTPUT-CATEGORY}}-md/{{OUTPUT-MD-FILENAME}}.md`

Subject: **{{SUBJECT-MATTER}}** (Cloudcroft, New Mexico). Category: **{{SUBJECT-TYPE}}**. Use the same 12-section structure as the reference guide, with headings adapted to the subject type:

1. Executive summary
2. Verified facts (bullet list tailored to {{SUBJECT-TYPE}}: official name, address, phone, official website, operating status, hours of operation, {{SUBJECT-TYPE}}-specific details, accessibility, pricing if applicable, contact methods)
3. What the {{SUBJECT-TYPE}} appears to be
4. {{SECTION-4-HEADING}} (confirmed / likely / unclear / strengths / drawbacks)
5. {{SECTION-5-HEADING}}
6. Grounds and setting
7. History and significance
8. Experience patterns (hard facts / positive patterns / caution patterns)
9. {{SECTION-9-HEADING}}
10. {{SECTION-10-HEADING}} (Best for / Probably not best for)
11. Source notes (Official / Tourism-community / Local reporting / Review-pattern analysis)
12. Fact-check notes and uncertainty flags

#### Research requirements

- Pull confirmed facts from the official {{SUBJECT-MATTER}} website ({{SUBJECT-URL}}), the Cloudcroft Chamber of Commerce directory, New Mexico Tourism, relevant third-party platforms appropriate to {{SUBJECT-TYPE}} (e.g., Tripadvisor, Booking.com, Yelp, Google Business, Facebook), and any Cloudcroft Reader local coverage.
- If `{{EXISTING-PAGE-PATH}}` is provided, also review the existing page at `/Users/chrishea/Library/Mobile Documents/com~apple~CloudDocs/GitHub/discover-beta/{{EXISTING-PAGE-PATH}}` for facts already gathered — cross-check these rather than inheriting blindly.
- Every factual claim should be either clearly confirmed with a source or explicitly flagged as "appears current; should be checked directly" or "less than 95% certain."
- Never invent phone numbers, addresses, rates, hours, or policies. If you cannot confirm, say so.

### 3. Produce a companion single-file HTML web page

Save as: `/Users/chrishea/Library/Mobile Documents/com~apple~CloudDocs/GitHub/discover-beta/{{OUTPUT-CATEGORY}}/{{OUTPUT-HTML-FILENAME}}.html`.

- Match the visual style, layout, color palette, typography, and section rhythm of `/Users/chrishea/Library/Mobile Documents/com~apple~CloudDocs/GitHub/discover-beta/{{REFERENCE-HTML-PATH}}`. Use it as your HTML template.
- Populate the page with the content from `{{OUTPUT-MD-FILENAME}}.md`.
- Embed all photos from this folder, referenced with relative paths from the HTML file's location:

  `{{OUTPUT-CATEGORY}}-photo/{{PHOTO-FOLDER}}/`

  **Preserve the exact filename and extension of every photo as it appears on disk.** Verify filenames with a directory listing before writing the HTML — do not assume extensions.

- Use photos as: one hero image at the top, a gallery grid in the middle, and contextual inline images in the {{SECTION-4-HEADING}}, Grounds, and {{SECTION-5-HEADING}} sections where appropriate.
- Include descriptive `alt` text for every image (accessibility).
- Ensure the page is responsive and mobile-friendly.
- Include a verified contact block (name, address, phone, website) in a prominent, clearly styled card near the top.
- Use {{CTA-VERB}} as the primary call-to-action verb on buttons.
- Use {{AUDIENCE-NOUN}} as the audience reference where prose requires it.

### 4. Deliverables

At the end, present two `computer://` links:

- the new Markdown file
- the new HTML page

Keep any post-amble brief. Flag any facts you could not verify in a short "Open questions" note for the user.

### Guardrails

- Do not fabricate amenities, hours, rates, or policies.
- Preserve the reference guide's habit of explicitly marking uncertainty.
- Do not use emojis.
- Keep prose clear and concise.
- Before writing image references, verify actual filenames on disk with `ls`.

---

## Example CSV rows

```csv
SUBJECT-MATTER,SUBJECT-TYPE,SUBJECT-SHORT-NAME,SUBJECT-URL,SUBJECT-ADDRESS,SUBJECT-PHONE,OUTPUT-CATEGORY,OUTPUT-MD-FILENAME,OUTPUT-HTML-FILENAME,PHOTO-FOLDER,REFERENCE-MD-PATH,REFERENCE-HTML-PATH,EXISTING-PAGE-PATH,SECTION-4-HEADING,SECTION-5-HEADING,SECTION-9-HEADING,SECTION-10-HEADING,AUDIENCE-NOUN,CTA-VERB
The Cabins at Cloudcroft,Lodging,cabins-at,https://www.cabinsatcloudcroft.com,"1006 Coyote Ave, Cloudcroft, NM 88317",(575) 682-2396,stay,cabins-at,stay-cabins-at-cloudcroft,photo-cabins-at,stay/stay-md/stay-dusty-boots-motel-booking-guide.md,stay/stay-dusty-boots-motel-cloudcroft.html,stay/stay-cabins-at-cloudcroft.html,Cabins and accommodations,Food and provisions,What travelers should verify before booking,Who should book The Cabins at Cloudcroft,travelers,Book
New Village Hardware,Retail,new-village-hardware-content,,"Cloudcroft, NM 88317",,shop,new-village-hardware-content,shop-new-village-hardware,photo-new-village-hardware,stay/stay-md/stay-dusty-boots-motel-booking-guide.md,stay/stay-dusty-boots-motel-cloudcroft.html,,Products and departments,Services offered,What shoppers should know before visiting,Who should shop at New Village Hardware,shoppers,Shop
```
