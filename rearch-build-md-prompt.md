# Prompt: Create Cabins at Cloudcroft Booking Guide + Web Page

You are producing a Cloudcroft lodging booking guide in Markdown, plus an accompanying single-file HTML web page. Follow the instructions below exactly.

## 1. Review the reference file for style, tone, and structure

Open and carefully read:

`/sessions/nice-beautiful-hopper/mnt/discover-beta/stay/stay-md/stay-dusty-boots-motel-booking-guide.md`

This is your stylistic template. Note its voice: concise, fact-driven, skeptical of unverified claims, and explicit about what is confirmed vs. what needs to be verified. It uses short paragraphs, bulleted fact lists, and flags uncertainty. Mirror that voice and discipline.

## 2. Produce a new Markdown file at exactly this path

`/sessions/nice-beautiful-hopper/mnt/discover-beta/stay/stay-md/cabins-at.md`

Subject: **The Cabins at Cloudcroft** (Cloudcroft, New Mexico). Use the same 12-section structure as the Dusty Boots guide:

1. Executive summary
2. Verified booking facts (bullet list: official name, address, phone, official website, operating status, booking path, room/cabin types, in-cabin amenities, kitchen/fireplace/hot tub details, pet policy, check-in/out times, Wi-Fi, parking, accessibility, cabin count)
3. What the property appears to be
4. Rooms and accommodations (confirmed / likely / unclear / strengths / drawbacks)
5. Dining and drinking (or "Food and provisions" if no on-site dining)
6. Grounds and setting
7. History and significance
8. Guest experience patterns (hard facts / positive patterns / caution patterns)
9. What travelers should verify before booking
10. Who should book The Cabins at Cloudcroft (Best for / Probably not best for)
11. Source notes (Official / Tourism-community / Local reporting / Review-pattern analysis)
12. Fact-check notes and uncertainty flags

### Research requirements

- Pull confirmed facts from the official Cabins at Cloudcroft website, Cloudcroft Chamber of Commerce directory, New Mexico Tourism, Tripadvisor, Booking.com, VRBO/Airbnb listings if applicable, BringFido, and any Cloudcroft Reader local coverage.
- Also review the existing page at `/sessions/nice-beautiful-hopper/mnt/discover-beta/stay/stay-cabins-at-cloudcroft.html` for facts already gathered — cross-check these rather than inheriting blindly.
- Every factual claim should be either clearly confirmed with a source or explicitly flagged as "appears current; should be checked directly" or "less than 95% certain."
- Never invent phone numbers, addresses, rates, or policies. If you cannot confirm, say so.

## 3. Produce a companion single-file HTML web page

Save as: `/sessions/nice-beautiful-hopper/mnt/discover-beta/stay/stay-cabins-at.html` (or overwrite the existing `stay-cabins-at-cloudcroft.html` if the user confirms; default to creating the new filename and leaving the old one intact).

- Match the visual style, layout, color palette, typography, and section rhythm of `stay-dusty-boots-motel-cloudcroft.html` (same directory). Use it as your HTML template.
- Populate the page with the content from `cabins-at.md`.
- Embed photos from this folder — use all 18 files, referenced with relative paths:

  `stay-photo/photo-cabins-at/cabins-at-00444.JPG.webp` through `cabins-at-00461.JPG` (mix of .webp and .JPG extensions — preserve exact filenames as they appear on disk).

- Use photos as: one hero image at the top, a gallery grid in the middle, and contextual inline images in the Rooms, Grounds, and Dining sections where appropriate.
- Include descriptive `alt` text for every image (accessibility).
- Ensure the page is responsive and mobile-friendly.
- Include the verified contact block (name, address, phone, website) in a prominent, clearly styled card near the top.

## 4. Deliverables

At the end, present two `computer://` links:

- the new Markdown file
- the new HTML page

Keep any post-amble brief. Flag any facts you could not verify in a short "Open questions" note for the user.

## Guardrails

- Do not fabricate amenities, rates, or policies.
- Preserve the Dusty Boots guide's habit of explicitly marking uncertainty.
- Do not use emojis.
- Keep prose clear and concise.
