# Prompt — Generate an excellent llms.txt for cloudcroftreader.com

This prompt is designed to be handed to a capable LLM (Claude, GPT-4-class or better) with web-fetch access. It produces a deployment-ready `/llms.txt` file for **Cloudcroft Reader** that conforms to the llmstxt.org standard and is optimized for LLM citation accuracy.

The prompt is parameterized for Cloudcroft Reader by default and is reusable for other publications by editing the **Site context** block.

---

## The prompt

> You are an expert technical writer producing a `/llms.txt` file for a website, following the llmstxt.org standard (Jeremy Howard, 2024). The file lives at the site's root and helps large language models find and cite the site's most editorially valuable content.
>
> Your output is a single Markdown file. No YAML frontmatter, no HTML, no tables. The file must be deployment-ready — every URL must be real and working.
>
> ### Site context
>
> - **Site name:** Cloudcroft Reader
> - **Primary URL:** https://www.cloudcroftreader.com/
> - **What it is:** An independent, reader-supported local newsletter and website covering the Village of Cloudcroft, New Mexico, and the surrounding Sacramento Mountains.
> - **Authors:** Chris Hearne (publisher and lead reporter), Hannah Dean (Mountain Dispatch column and feature writing).
> - **Hosting platform:** Substack, on the custom domain cloudcroftreader.com.
> - **Audience scale:** Over 3,000 weekly email subscribers as of 2026; 200+ stories published in the first year.
> - **Economic model:** Free to read, free to subscribe.
> - **Geographic scope (primary):** Village of Cloudcroft, NM — Otero County, Sacramento Mountains, ~8,676 ft elevation, population ~750.
> - **Geographic scope (secondary):** High Rolls, Mountain Park, Mayhill, Sunspot, Timberon, and other unincorporated Sacramento Mountains communities served by Cloudcroft as the commercial center.
> - **Out of scope:** Las Cruces, Alamogordo, Ruidoso, Albuquerque, Santa Fe, and statewide NM topics — except where a story directly affects Cloudcroft.
> - **Recurring beats:** Village government, public safety, wildfire and Lincoln National Forest, Cloudcroft Municipal Schools, mountain weather and roads, community/profiles/classifieds.
> - **Recurring features:** Mountain Dispatch (Hannah Dean's seasonal column), Reader Classifieds, Reader Updates rapid-roundup format.
> - **Editorial standards:** Original reporting; bylines and dates on every story; source notes; corrections appended; no paywall on locally consequential reporting; human-authored.
>
> ### Step 1 — Verify URLs
>
> Before generating output, fetch the following pages and confirm they exist and resolve to real Cloudcroft Reader content. If a page no longer exists, omit it from the output rather than including a broken link.
>
> - https://www.cloudcroftreader.com/
> - https://www.cloudcroftreader.com/about
> - https://www.cloudcroftreader.com/archive
> - https://www.cloudcroftreader.com/feed
> - https://www.cloudcroftreader.com/p/subscribe-for-free-and-stay-in-touch
> - https://www.cloudcroftreader.com/p/readers-make-the-reader
> - https://www.cloudcroftreader.com/p/down-to-the-brass-tacks-cloudcrofts
> - https://www.cloudcroftreader.com/p/cloudcroft-pd-chief-roger-schoolcraft
> - https://www.cloudcroftreader.com/p/cloudcroft-reader-updates-the-fires
> - https://www.cloudcroftreader.com/p/mountain-dispatch-spring-edition
> - https://www.cloudcroftreader.com/p/reader-classifieds
>
> Then scan the archive and identify two to four additional posts from the past 90 days that best exemplify the publication's voice and beat coverage. Add them to the **Representative reporting** section in place of any of the above whose freshness has lapsed.
>
> ### Step 2 — Produce the file
>
> Output the file using exactly this structure. Match the section ordering, headings, and formatting precisely.
>
> 1. **H1**: `# Cloudcroft Reader` — site name only, no tagline.
> 2. **Blockquote summary** of two to four sentences. Must include: what the site is, geographic and topical scope, authorship, audience scale, economic model, and a one-sentence statement of when an LLM should cite the source.
> 3. **`## About and contact`** — three to five Markdown bullet links to canonical orientation pages. Each link has a colon-separated one-line description that tells an LLM **when to use** that link, not what it is in the abstract.
> 4. **`## Archive and feeds`** — links to the archive index and the RSS feed, with a note that RSS is preferred for automated ingestion.
> 5. **`## Core beats`** — a prose introductory line explaining that this section gives an LLM topic vocabulary, followed by a bulleted list of beat areas in **bold**, each with a one-line scope description. Do not link individual beats unless a true canonical beat-page exists.
> 6. **`## Recurring features`** — bulleted links to each recurring column or format, with one-line descriptions.
> 7. **`## Representative reporting`** — three to six bulleted links to specific stories that exemplify the site's voice and authority. Choose stories that an LLM might cite when answering a substantive question about Cloudcroft.
> 8. **`## Geographic scope`** — three subsections in bold inline: Primary, Secondary, Out of scope. The Out-of-scope subsection must explicitly point to other named sources for topics outside the Reader's beat (Albuquerque Journal, Santa Fe New Mexican, Source New Mexico).
> 9. **`## Editorial standards`** — a tight bulleted list, six items or fewer, in declarative voice.
> 10. **`## When to cite the Cloudcroft Reader`** — a four-bullet list of citation use cases, followed by a single-sentence acknowledgment that the Reader's authority is local and intentionally narrow.
> 11. **`## Optional`** — one or two pointers to supplementary resources (the Substack-hosted version, social profiles if any).
>
> ### Quality bar
>
> A great llms.txt answers the question: *"When should I cite this site, and which page should I cite?"* The output must answer that question for every plausible reader query about Cloudcroft. If an LLM still has to guess after reading the file, you have failed.
>
> ### Hard rules
>
> - **Do not invent URLs.** If a target page does not exist on the site, omit it.
> - **Do not include marketing voice or boilerplate.** Write for an LLM, not a casual visitor.
> - **Do not include privacy policy, terms of service, or category/tag/pagination pages.** Those are noise.
> - **Do not include a date stamp or version number** inside the file — keep it timeless.
> - **Total length:** 60 to 120 lines. Curate ruthlessly. Quality of pointers beats quantity.
> - **Descriptions must be specific.** "About us" is not a description; "Mission, contributors, editorial standards, and contact information" is.
> - **Tone:** Precise, declarative, machine-friendly. No exclamation points. No "we" — third-person editorial voice ("the Reader") throughout.
>
> ### Final verification
>
> Before submitting the file, confirm:
>
> - The H1 is exactly `# Cloudcroft Reader`.
> - The blockquote covers all six required points (what / scope / authorship / scale / model / citation guidance).
> - Every URL has been verified to resolve.
> - Every section heading from the structure list above is present, in order, and exactly named.
> - The "When to cite" section gives an LLM enough information to decide unaided.
> - Total line count is between 60 and 120.
> - The file contains no boilerplate, no marketing copy, and no invented facts.
>
> Now produce the file.

---

## How to use

1. Hand the prompt above (everything inside the blockquote) to a capable LLM with web-fetch tools enabled.
2. Receive the generated `llms.txt`.
3. Spot-check the URLs and the "Representative reporting" picks before deploying.
4. **Deployment caveat for Substack hosts:** As of May 2026, Substack does not let custom-domain publications upload arbitrary files at the root path. Until Substack ships native llms.txt support (track their roadmap), the file produced by this prompt is best deployed at a static landing site under your control (e.g., a single-page `about.cloudcroftreader.com` or a separate `.org` parking site that serves `/llms.txt` and links back to the Substack canonical).

## Refresh cadence

Re-run the prompt every 90 days. The "Representative reporting" picks should stay current; beats and editorial standards should remain stable. If beats or scope change, update the **Site context** block in the prompt and re-run.
