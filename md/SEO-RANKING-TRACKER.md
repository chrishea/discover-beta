# SEO Ranking Tracker — DiscoverCloudcroft.com

Monthly check of where **discovercloudcroft.com** ranks for the four target keywords. Re-run on or near the 11th of each month.

---

## How to re-run (5 minutes)

1. Open a private/incognito Google window (avoid personalization). Set location to **Cloudcroft, NM** or **United States** if possible.
2. Run each of the four queries below verbatim.
3. Scan the first 30 results. Record the position of any `discovercloudcroft.com` URL.
4. If not in top 30, record `>30`. If not in top 10 but on page 2, record `11–20` or `21–30`.
5. Add a new row to each section using today's date.
6. Note any new top-3 competitors that didn't appear last time.
7. Commit: `git add md/SEO-RANKING-TRACKER.md && git commit -m "ranking check $(date +%Y-%m-%d)"`

**Tip:** Use [valentin.app SERP checker](https://www.valentin.app/) or [whatsmyserp.com](https://www.whatsmyserp.com/) for unpersonalized checks. Google Search Console's *Performance → Queries* report is the most accurate ground truth — pull avg. position for each query if available.

---

## Target keywords

| # | Query | Hub page being tracked |
| --- | --- | --- |
| 1 | `hike in cloudcroft nm` | [/do/guide-to-hiking-in-cloudcroft-new-mexico.html](https://discovercloudcroft.com/do/guide-to-hiking-in-cloudcroft-new-mexico.html) |
| 2 | `eat in cloudcroft nm`  | [/eat/complete-guide-where-to-eat-in-cloudcroft.html](https://discovercloudcroft.com/eat/complete-guide-where-to-eat-in-cloudcroft.html) |
| 3 | `stay in cloudcroft nm` | [/stay/complete-guide-to-lodging-in-cloudcroft-new-mexico.html](https://discovercloudcroft.com/stay/complete-guide-to-lodging-in-cloudcroft-new-mexico.html) |
| 4 | `camp in cloudcroft nm` | [/do/guide-to-camping-cloudcroft-new-mexico.html](https://discovercloudcroft.com/do/guide-to-camping-cloudcroft-new-mexico.html) |

Also tracking the brand query as a sanity check:

| # | Query | Notes |
| --- | --- | --- |
| 5 | `discover cloudcroft` | Should rank #1; watch for stale title in SERP |

---

## 1. "hike in cloudcroft nm"

| Date | DCcroft rank | URL ranking | Top 3 competitors | Notes |
| --- | --- | --- | --- | --- |
| 2026-05-11 | >30 | — | alltrails.com, komoot.com, hikingproject.com | Baseline. Aggregators dominate. ItemList JSON-LD and H1 rewrite shipped today; expect crawl effect by early June. |

---

## 2. "eat in cloudcroft nm"

| Date | DCcroft rank | URL ranking | Top 3 competitors | Notes |
| --- | --- | --- | --- | --- |
| 2026-05-11 | >30 | — | thebitenm.com, tripadvisor.com, bigdaddysdinernm.com | Baseline. Chamber (`coolcloudcroft.com`) at #4. |

---

## 3. "stay in cloudcroft nm"

| Date | DCcroft rank | URL ranking | Top 3 competitors | Notes |
| --- | --- | --- | --- | --- |
| 2026-05-11 | >30 | — | grandcloudcroft.com, 223collectionhotels.com (The Lodge), cloudcroft.com | Baseline. OTAs and property sites own the SERP. |

---

## 4. "camp in cloudcroft nm"

| Date | DCcroft rank | URL ranking | Top 3 competitors | Notes |
| --- | --- | --- | --- | --- |
| 2026-05-11 | >30 | — | thecampatcloudcroft.com, yelp.com, fs.usda.gov (Lincoln NF) | Baseline. USFS is the authority source. |

---

## 5. Brand query: "discover cloudcroft"

| Date | DCcroft rank | URL ranking | Title shown in SERP | Notes |
| --- | --- | --- | --- | --- |
| 2026-05-11 | 1 | https://www.discovercloudcroft.com/ | "Discover Cloudcroft — Your Mountain Escape at 8,676 Feet..." | **STALE.** SERP showing the old `shelf/old-index.html` title. Re-indexing requested. |

---

## Secondary queries to spot-check (every other month)

These are decision-stage long-tail queries where this site's editorial style should beat aggregators. Worth tracking once positioned.

| # | Query | Best landing page | Initial check |
| --- | --- | --- | --- |
| S1 | `osha trail cloudcroft` | /do/osha-trail.html | TBD |
| S2 | `mexican canyon trestle hike` | /do/mexican-canyon-trestle.html | TBD |
| S3 | `cloudcroft from el paso` | /visit/cloudcroft-from-el-paso.html | TBD |
| S4 | `cloudcroft from alamogordo` | /visit/cloudcroft-from-alamogordo.html | TBD |
| S5 | `cloudcroft from las cruces` | /visit/cloudcroft-from-las-cruces.html | TBD |
| S6 | `cloudcroft fire restrictions 2026` | /topics/water-restrictions.html (closest) | TBD — content gap to fill |
| S7 | `cloudcroft water restrictions` | /topics/water-restrictions.html | TBD |
| S8 | `cloudcroft winter conditions` | /topics/winter-conditions.html | TBD |
| S9 | `best beginner hike cloudcroft` | /do/guide-to-hiking-in-cloudcroft-new-mexico.html | TBD |
| S10 | `cloudcroft vs ruidoso` | /visit/cloudcroft-from-ruidoso.html | TBD |

---

## Decision rules

- **Green / on track:** rank improves by 5+ positions month over month, or enters top 10.
- **Yellow / hold:** rank within ±3 positions for 60+ days. Time to revisit on-page content.
- **Red / regress:** rank drops 5+ positions or competitors with new content displace DCcroft. Investigate immediately — usually a content freshness issue or a competitor relaunch.

## What to do based on results

| If… | Then… |
| --- | --- |
| Rank in top 10 | Defend it: refresh content quarterly, watch competitors |
| Rank 11–20 | Highest-ROI tier. Add 1–2 new sections, improve internal anchor text, build 1 external link |
| Rank 21–30 | Likely a content depth or schema problem. Audit and rewrite |
| Not in top 30 | Either thin content or indexing problem. Check GSC coverage, request re-indexing |

## Useful links

- [Google Search Console](https://search.google.com/search-console) — ground-truth ranking data
- [Bing Webmaster Tools](https://www.bing.com/webmasters) — covers ChatGPT/Copilot search
- [PageSpeed Insights](https://pagespeed.web.dev/) — page-level perf
- [Schema.org validator](https://validator.schema.org/) — paste a URL, check JSON-LD parses
- [Rich Results Test](https://search.google.com/test/rich-results) — see what Google sees for the page

---

*Tracker created 2026-05-11 alongside [SEO-REVIEW-2026-05-11.md](./SEO-REVIEW-2026-05-11.md). Update monthly.*
