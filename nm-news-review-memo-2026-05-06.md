# MEMO — Review of nm.news / Ctrl+P Publishing

**To:** Chris Hea
**From:** Editorial review
**Date:** May 6, 2026
**Re:** nm.news (and the Ctrl+P Publishing network), with focus on `#thepaper`

---

## Disclosure up front

I could not load `https://nm.news/` directly — it isn't on this session's network allowlist, so I'm working from the public record (search results, KUNM, KRQE, Albuquerque Journal, Santa Fe Reporter, *Editor and Publisher*, the company's own LinkedIn and About pages indexed in search). Where this memo cites observable structure (anchor-fragment routing, shared-domain hierarchy, the editor-of-record for three papers), it's quoted from search snippets that surface the underlying facts. Where I'm characterizing editorial intent or political risk, I'm reasoning from the public record. I've flagged the difference.

You asked me to be tough. I'm being tough.

---

## What it actually is

`nm.news` is the network skin for **Ctrl+P Publishing Co.**, owned and run by **Pat Davis** — former Albuquerque City Councilor (2015–2023, Council President 2020 and 2023), co-founder of the cannabis consulting firm *Weeds*, and a continuously active political figure in the state. Ctrl+P launched the nm.news platform in 2025 as a "local news infrastructure network" to share content, subscribers, and back-office services across its properties.

The portfolio under that umbrella, as of mid-2025:

- **The Paper** — Albuquerque alt-weekly, launched October 2020 at `abq.news`. The lead brand and the apparent reason you anchored on `#thepaper`.
- **Santa Fe Reporter** — 50-year-old institution, purchased August 2024 from Bob Meeker and Andy Zusman.
- **Sandoval Signpost** — community paper purchased earlier; transitioning to free monthly mail-drop in Placitas and Bernalillo as of April 2025.
- **Corrales Comment** — community paper purchased from a retiring owner.
- **The Independent News** — Edgewood community paper.
- **City Desk ABQ** — apparently rolled into the network (`citydesk.org`).
- **NM Political Report** — older nonprofit, repositioned by Davis.

That's seven editorial brands under one ownership. nm.news won LION Publishers' 2025 "Product of the Year" award.

---

## What's genuinely good

I don't want to be unfair, so let me put the real strengths on the table first.

1. **The network model is legitimately the right answer for community journalism in 2026.** Independent local papers can't carry their own ad sales, design, technology, distribution, subscription, and accounting overhead anymore. Centralizing the back office while preserving editorial output is the only viable economic structure left. Pat Davis is doing what Lenfest, Tiny News Collective, and others are doing nationally — and he's doing it in a state where almost nobody else is even trying.
2. **The portfolio is real.** Buying the Santa Fe Reporter and bringing it back to New Mexico ownership for the first time in nearly 30 years is a meaningful civic act. So is rescuing the Corrales Comment from retirement-driven shutdown. These are properties that would otherwise have closed or been sold to a McClatchy-equivalent.
3. **The LION award is not nothing.** It's peer-recognized in the local-news industry. It rewards demonstrated revenue-and-subscription scaling, not vibes.
4. **Domain naming.** `nm.news` is one of the better short-domain plays in U.S. local journalism. Two letters, the right TLD, instantly memorable. Good marketing instinct.

That's the case for. The case against is longer.

---

## The structural problems

### 1. "Editorial independence" is partially fictional

Public materials describe the network as a federation of independent papers. The KUNM and *Editor and Publisher* coverage uses the same phrase. **It's not accurate.** Per the Sandoval Signpost's own published staff note, **Kevin Hendricks edits a "combined newsroom" serving the Sandoval Signpost, the Corrales Comment, and The Independent News.** That is one editor for three papers, all owned by the same company.

That's not editorial independence. That's centralized editing with three different mastheads. It's a content-mill structure dressed in legacy-brand uniforms. There may be a defensible operational argument for it (small papers can't each afford their own EIC), but it should be disclosed plainly to readers — and it isn't.

The Santa Fe Reporter and The Paper appear to retain their own editorial leadership, which is the only reason this critique stops at three papers and not all seven. But the precedent has been set, and the trajectory of network consolidation in local news is uniformly toward more sharing of edit work, not less.

### 2. The conflict-of-interest exposure is severe and not publicly addressed

Davis is the owner of a network that includes:

- A statehouse-focused paper (**Santa Fe Reporter**)
- A state-political news outlet (**NM Political Report**)
- An Albuquerque-focused alt-weekly (**The Paper**) — covering a city government he was a Council President of as recently as 2023
- A community paper covering Sandoval County (**Sandoval Signpost**) — an adjacent jurisdiction to ABQ politics

He simultaneously co-owns *Weeds*, a cannabis consulting firm, and chaired the City Council's Cannabis Legalization Working Group during legalization, an issue he continues to consult on commercially.

A serious newspaper publisher with active political and commercial interests in the topics his papers cover needs a published recusal policy, an independent ombudsman, or — at minimum — a transparent conflict-disclosure on every relevant story. **The public-facing materials I can find disclose none of those mechanisms.** Saying "each publication retains editorial independence" is a slogan, not a policy. It does not survive contact with the first cannabis-regulation story or the first ABQ City Council scandal that touches a Davis-era vote.

This is the single most important issue for the credibility of the whole network. It is also the easiest one to fix — publish the policy. The fact that they haven't tells you something about how seriously they're taking the conflict question.

### 3. The information architecture is unfinished and the SEO is fragmented

You pointed at `nm.news/#thepaper`. That's a **fragment-anchor route** — meaning The Paper's content is being rendered into the nm.news front page and accessed by an in-page anchor link, not via a URL with its own canonical address. Meanwhile, The Paper's own brand domain `abq.news` exists separately. So:

- If The Paper's content is canonical at `abq.news`, the version under `nm.news/#thepaper` is duplicate-content surfaced behind a fragment anchor that Google won't crawl distinctly.
- If The Paper's content is canonical at `nm.news/#thepaper`, then `abq.news` is a deprecated brand and the network has quietly killed The Paper's domain identity without saying so.
- Either reading is bad. The third option — the content is mirrored at both addresses with proper canonicals pointing one way or the other — would be defensible, but the existence of `nm.news/#thepaper` as a routing pattern at all suggests the team is still using fragment anchors as primary navigation, which is a 2010s design pattern.

Across the portfolio, the network operates **at least seven separate domains**: `nm.news`, `abq.news`, `sfreporter.com`, `sandovalsignpost.com`, `corralescomment.com`, `citydesk.org`, plus The Independent News. Each builds its own domain authority in isolation; none consolidates link equity for the network as a whole. From a Google-ranking standpoint, this is the worst of all worlds — the operating company has no single brand domain that accumulates authority, and each individual domain is too small to compete with the *Albuquerque Journal* or *Santa Fe New Mexican*.

The right architectural call for a network of this size in 2026 is **one strong domain with subdirectories or subdomains for each masthead**, plus 301 redirects from the legacy domains. That preserves brand equity and consolidates link signals. Choosing six independent domains plus a portal is choosing fragmentation.

### 4. The LION "Product of the Year" award is doing more work in marketing copy than it should

LION's award is real. It rewards a defined thing — sustainable local-news *business* models. It is not a journalism award. It is not a Pulitzer, an IRE, an Edward R. Murrow, or even a New Mexico Press Association first-place. The network's marketing leans heavily on "award-winning," and on close inspection, the most prominent award is for the back-office innovation, not for the work that appears on the page. That's a subtle tell about where the operator's pride actually lives.

If the front-of-book journalism were carrying the network on its own, the award stack would look different.

### 5. Marketing claims that don't survive scrutiny

The Paper's About page describes its team as producing "the region's most-read weekly paper and largest daily digital newsletter readership in the state." Those are testable claims. **Neither claim is sourced or numbered in the publicly available materials.** "Most-read" against what circulation comparison? The *Albuquerque Journal* dwarfs every alt-weekly in the state on weekly readership; if the comparison is "most-read alt-weekly," that's true but a much smaller claim. "Largest daily digital newsletter readership in the state" — is that bigger than the *Albuquerque Journal*'s daily newsletter? KRQE's? KOAT's? Source New Mexico's? Without a number, this is sales copy, not journalism.

A network that wants to be taken seriously as a journalism enterprise should not be making circulation claims it isn't willing to put numbers next to.

### 6. The economic model is still community-paper economics

Switching the Sandoval Signpost from paid subscription to "free monthly mail-drop to every household in Placitas and Bernalillo" is a meaningful tell. That's the print model of mid-2000s shoppers and pennysavers. It pencils only on advertising — and ad markets in suburban New Mexico are not what they were a decade ago. The network's Sandoval/Corrales/Independent products appear to be, structurally, free community advertisers with editorial content stapled in. That has been a viable model in plenty of places and eras. But it's not journalism economics; it's distribution economics. The pitch and the product should match.

---

## Summary verdict

**Net:** Pat Davis is doing the right thing strategically — consolidating endangered local-news brands, building shared infrastructure, and keeping community papers alive that would otherwise have died. The portfolio is real. The award is real. The civic value of saving the Santa Fe Reporter is real.

**But** the public posture of the network — independent papers, editorial firewalls, award-winning journalism — does not yet match the operational reality of one combined newsroom across three of the seven titles, an unaddressed conflict-of-interest exposure on the part of the publisher, an unfinished information architecture that fragments brand and SEO, and marketing claims that won't survive being asked to show their work.

**If I were on the board, I'd push three things, in this order:**

1. **Publish a network-wide editorial conflict-of-interest policy** — including a recusal protocol for any story touching cannabis, ABQ City Council 2015–2023 history, or Davis's continuing political activities. Name an independent ombudsman. Without this, the network's credibility on its most consequential beats is open to permanent challenge.
2. **Pick an architectural model and finish it.** Either consolidate to one master domain with masthead subdirectories (and 301 the rest), or commit to seven independent brands and kill the portal. The current half-state is the worst option.
3. **Drop the unsourced superlatives.** "Most-read weekly in the region" and "largest daily digital newsletter in the state" should either be substantiated with audited numbers or removed. Operating with claims you can't defend in a press-council complaint is unforced reputational risk.

**If those three don't happen in the next twelve months, the network will look in 2027 a lot like the small-town consolidated chains that critics already accuse it of resembling — only with better technology and a sharper domain name.**

That's the tough version. There's a softer version where I emphasize the civic mission and the LION recognition. You asked for tough. There it is.

---

*Sources consulted: KUNM "Former Albuquerque City Councilor Pat Davis buys the Santa Fe Reporter" (Aug 14, 2024); Santa Fe New Mexican "Albuquerque publishing group buys 'Santa Fe Reporter'"; Editor and Publisher "Santa Fe Reporter, 50-years young, returns to New Mexico ownership with deal to join Ctrl+P Publishing Group"; Albuquerque Journal "ABQ city councilor buys newspaper in Placitas"; New Mexico In Focus "Pat Davis on Challenges Facing Ctrl+P Publishing and its Outlets"; Sandoval Signpost staff masthead; The Paper About page (abq.news); nm.news About page (via search); LinkedIn profile for Pat Davis (Ctrl+P) and the nm.news company page; Wikipedia "Santa Fe Reporter" and "Media in Albuquerque, New Mexico." Direct fetch of nm.news was unavailable in this session.*
