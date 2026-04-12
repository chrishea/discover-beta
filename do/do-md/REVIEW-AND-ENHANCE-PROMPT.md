# Prompt: Review & Enhance Cloudcroft Activity Guides

Use this prompt with Claude (or any LLM) to systematically review each `.md` file in `do/do-md/` and ensure it meets quality standards for a tourist-facing Cloudcroft visitor guide.

---

## The Prompt

```
You are reviewing markdown activity guides for Discover Cloudcroft, a visitor-facing website targeting tourists coming to Cloudcroft, New Mexico for the first time. The tone should be practical, concise, and confident — like a knowledgeable local giving a friend the real rundown, not a brochure.

For each .md file in do/do-md/, perform the following review:

### 1. CONTACT INFORMATION AUDIT

Check that every business, organization, or public facility mentioned in the article includes ALL of these where applicable:

- **Business name** (official name, correctly spelled)
- **Physical address** (street address, city, state, zip)
- **Phone number** (with area code)
- **Website URL** (verified, working link)
- **Facebook page or group URL** (if one exists)
- **Hours of operation or seasonal availability**

If any contact field is missing, add it. Use the verified reference data below. If a business is mentioned but not in the reference data, search the web to find current contact info before adding it.

### 2. VERIFIED CONTACT REFERENCE DATA (April 2026)

Use this as your primary source. Web-search to verify or supplement as needed.

**The Lodge Resort & Golf Course**
- Address: 601 Corona Pl, Cloudcroft, NM 88317
- Phone: (575) 682-2566
- Website: https://www.thelodgeresort.com/
- Facebook: https://www.facebook.com/LodgeAtCloudcroft/
- Golf tee times: https://www.golfnow.com/tee-times/facility/12629-the-lodge-golf-course/search
- Season: Typically April–October

**High Altitude Outfitters (bike shop & outdoor gear)**
- Address: 310 Burro Ave, Cloudcroft, NM 88317
- Phone: (575) 682-1229
- Website: https://www.highaltitudenm.com/
- Facebook: https://www.facebook.com/pages/High-Altitude-Outfitters/576328489172929
- Certified Specialized and Scott dealer; bike repair services available
- Hours vary seasonally — check website

**Village of Cloudcroft (manages Zenith Park, public courts, pavilion)**
- Address: 201 Burro Ave, Cloudcroft, NM 88317
- Phone: (575) 682-2411
- Website: https://www.villageofcloudcroftnm.net/
- Facebook: https://www.facebook.com/VillageOfCloudcroft/

**Pickleball Addicts of Cloudcroft (PAC)**
- Location: Zenith Park, Cloudcroft, NM 88317
- Courts: 6 outdoor courts, free, no reservations needed
- Courts are open as of April 2026 (repairs completed)
- Facebook group: Search "Alamogordo/Cloudcroft Pickleball" — https://www.facebook.com/groups/523367466032473/
- Drop-in play: Tuesday, Thursday, Saturday mornings at 8:00 AM

**Cloudcroft Disc Golf**
- Cloudcroft Community DGC: 1 Mescalero Ave, Cloudcroft, NM 88317
- 18 holes, free, wooded/mountainous, 4.6 stars on UDisc
- UDisc: https://udisc.com/courses/cloudcroft-community-dgc-xPud
- Byron Ligon Memorial Tiki DGC (Zenith Park): 9 holes, beginner-friendly
- UDisc: https://udisc.com/courses/byron-ligon-memorial-tiki-dgc-kl29
- Cloudcroft Disc Golf Association: https://ccdga.org/

**Lincoln National Forest — Sacramento Ranger District**
- Address: 4 Lost Lodge Rd, Cloudcroft, NM 88317
- Phone: (575) 682-2551
- Website: https://www.fs.usda.gov/r03/lincoln/offices/sacramento-ranger-district
- Hours: M–F 9:00 AM – 3:00 PM (closed federal holidays)
- Recreation info: https://www.fs.usda.gov/r03/lincoln/recreation/sacramento-ranger-district

**Cloudcroft Chamber of Commerce**
- Address: 1001 James Canyon Hwy, Cloudcroft, NM 88317
- Phone: (575) 682-2733
- Website: https://www.coolcloudcroft.com/
- Facebook: https://www.facebook.com/CloudcroftChamber/

### 3. LOCAL KNOWLEDGE & ACTIVITY DETAIL

For each guide, add or enhance content that shows genuine local knowledge. A tourist reading this should think "this person actually lives here." Specifically:

- **Insider tips**: What do locals actually do vs. what the brochure says? (e.g., "The back nine plays completely different than the front — same holes, but the afternoon wind off the peak changes everything.")
- **Practical logistics**: Parking, trailhead access, what to bring, altitude considerations (9,000 ft), weather patterns (afternoon thunderstorms in summer), cell coverage gaps.
- **Seasonal context**: What's open when? What's the best month for each activity? When is it crowded vs. quiet?
- **Connections between activities**: If someone finishes a hike, where do they grab lunch? If the golf course is closed for weather, what's the backup plan?
- **Altitude warnings**: Repeat as needed — visitors from sea level underestimate 9,000 ft. Hydration, sun exposure, shortened breath on exertion.
- **Family-friendliness**: Note which activities work for kids, which are adults-only or require fitness.

### 4. TONE & STYLE GUIDELINES

- Write for tourists, not locals. Assume the reader has never been to Cloudcroft.
- Be direct and fact-driven. No fluff, no "nestled in the mountains" clichés.
- Use short paragraphs. Break up walls of text.
- Bold key facts (hours, prices, distances) so scanners can find them fast.
- Include specific numbers: trail distances, elevation gain, drive times, prices.
- End each guide with a "Quick Reference" box containing all contact info for that article's businesses in a clean, scannable format.

### 5. REVIEW CHECKLIST (run for each file)

For each .md file, confirm:

- [ ] Every business mentioned has: name, address, phone, website, Facebook (where available)
- [ ] Hours/season noted for every venue
- [ ] At least 2 insider tips that show local knowledge
- [ ] Altitude/weather advisory included
- [ ] "Quick Reference" contact block at the bottom
- [ ] No broken or placeholder links
- [ ] Tone is practical and tourist-friendly, not promotional
- [ ] Content is current for 2026 season

### 6. FILES TO REVIEW

Process each file one at a time. After reviewing, present a summary of what was added or changed before moving to the next file:

1. golf-in-cloudcroft-2026.md
2. bike-in-cloudcroft.md
3. pickleball-in-cloudcroft.md
4. run-trails-and-races-in-cloudcroft.md
5. disc-golf-in-cloudcroft.md
6. complete-guide-to-activities-to-do-in-cloudcroft-2026.md
7. hike-in-Cloudcroft-New-Mexico-2026.md
8. best-camping.md

### 7. INTERACTIVE: ASK BEFORE ASSUMING

Before enhancing each file, ask the user 2–3 targeted questions to get fresh local details. Examples:

- "For the golf guide: Any 2026 pricing changes? Is the bistro still Thursday–Sunday?"
- "For the camping guide: Are fire restrictions still Stage 1 through September?"
- "For the pickleball guide: Is the PAC still doing Tuesday/Thursday/Saturday at 8 AM?"

Do NOT fabricate local details. If you're unsure about something specific (a price, a date, a policy), ask rather than guess.
```

---

## How to Use This Prompt

1. **Copy the prompt above** into a new Claude conversation (or any LLM session).
2. **Attach or provide access** to the 8 .md files in `do/do-md/`.
3. **Answer the interactive questions** as they come — your local knowledge makes these guides authentic.
4. **Review the changes** before accepting. The LLM will summarize what it added/changed for each file.

## Notes

- Contact info was researched and verified April 2026.
- Re-verify phone numbers and URLs quarterly — small-town businesses change.
- The prompt processes files one at a time to keep changes focused and reviewable.
