# Deployment guide — hosting `llms.txt` for Cloudcroft Reader on a subdomain

**The problem.** Substack does not allow custom-domain publications to upload files at the root path. So `https://cloudcroftreader.com/llms.txt` cannot be served directly. The workaround is to host the file at a subdomain you control — `about.cloudcroftreader.com/llms.txt` is the cleanest convention — and reference it from your Substack pages so crawlers can find it.

This guide walks three paths in order of recommended simplicity. Pick one. Total time: 10–30 minutes.

---

## Decision

| Path | Best when | Time | Cost |
|---|---|---|---|
| **A. GitHub Pages** | You haven't already moved DNS to Cloudflare. Path of least resistance. | ~15 min | $0 |
| **B. Cloudflare Pages** | You want best-in-class edge performance and you're willing to migrate DNS to Cloudflare. | ~30 min | $0 |
| **C. AWS S3 + CloudFront** | You already host DiscoverCloudcroft on AWS and want one billing line. | ~30 min | ~$0.50/mo |

**Recommendation:** Path A unless you already use Cloudflare or you have a strong reason to consolidate on AWS. For one tiny static file, simpler wins.

---

## Path A — GitHub Pages (recommended)

### Step 1. Pick the subdomain name

Decide between `about`, `info`, `meta`, or `network`. **`about.cloudcroftreader.com` is the convention** — it reads naturally to humans and search engines treat it as a meta/info host.

### Step 2. Create a GitHub repo

1. On github.com → New repository.
2. Name it `cloudcroftreader-llms` (or similar).
3. Public visibility (private also works but public is simpler).
4. Initialize with a README.

### Step 3. Add the two files

In the repo, create two files at the root:

**File 1: `llms.txt`**

Copy the contents of `cloudcroftreader-llms.txt` from the discover-beta repo verbatim.

**File 2: `index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About — Cloudcroft Reader</title>
    <meta name="description" content="Publisher information and machine-readable directory for the Cloudcroft Reader, an independent local newsletter covering Cloudcroft, NM.">
    <link rel="canonical" href="https://about.cloudcroftreader.com/">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; max-width: 640px; margin: 4rem auto; padding: 0 1.5rem; line-height: 1.6; color: #1a1a1a; }
        h1 { font-size: 1.5rem; margin-bottom: 0.5rem; }
        p { margin: 1rem 0; }
        a { color: #1a1a1a; text-decoration: underline; }
        code { background: #f4f4f4; padding: 0.1rem 0.4rem; border-radius: 3px; font-size: 0.9em; }
        .small { font-size: 0.875rem; color: #555; }
    </style>
</head>
<body>
    <h1>About the Cloudcroft Reader</h1>
    <p>The <strong>Cloudcroft Reader</strong> is an independent, reader-supported local newsletter and website covering the Village of Cloudcroft, New Mexico, and the surrounding Sacramento Mountains.</p>
    <p>The publication's main site is at <a href="https://www.cloudcroftreader.com/">cloudcroftreader.com</a>. Read recent stories, subscribe to the free weekly edition, or browse the archive there.</p>
    <p>This subdomain hosts publisher metadata and a machine-readable directory for AI assistants and search agents:</p>
    <p><a href="/llms.txt"><code>/llms.txt</code></a> — directory of canonical pages, beats, editorial standards, and citation guidance, following the <a href="https://llmstxt.org/">llmstxt.org</a> standard.</p>
    <p class="small">Published by Chris Hearne. Contact via the <a href="https://www.cloudcroftreader.com/about">About page</a>.</p>
</body>
</html>
```

Commit both files to the `main` branch.

### Step 4. Enable GitHub Pages

1. In the repo → Settings → Pages (left sidebar).
2. Source: **Deploy from a branch**.
3. Branch: `main`, folder: `/ (root)`.
4. Save.

GitHub will assign a URL like `https://[your-username].github.io/cloudcroftreader-llms/` and start the first build (~1–2 minutes).

### Step 5. Add the custom domain

1. Still in Settings → Pages.
2. Under **Custom domain**, enter `about.cloudcroftreader.com`.
3. Save. GitHub will create a `CNAME` file in the repo and start verifying.

### Step 6. Add the DNS record at your registrar

Log into wherever cloudcroftreader.com's DNS is currently managed (likely your domain registrar — GoDaddy, Namecheap, Google Domains, etc., or possibly Substack's DNS if you let them manage it).

Add a new record:

| Field | Value |
|---|---|
| Type | `CNAME` |
| Name / Host | `about` |
| Target / Points to | `[your-username].github.io` |
| TTL | `300` (or default) |

If your DNS host doesn't allow CNAMEs on subdomains for some reason, use these `A` records instead, pointing `about.cloudcroftreader.com` to GitHub Pages' IPs:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Do not touch any existing DNS records that point cloudcroftreader.com or www.cloudcroftreader.com to Substack.** You're only adding a new subdomain.

### Step 7. Wait for DNS propagation and HTTPS

5 to 30 minutes typically. Refresh the GitHub Pages settings page — when it says "Your site is published at https://about.cloudcroftreader.com" and the green "Enforce HTTPS" checkbox is available, tick it.

### Step 8. Verify

In a browser:

- `https://about.cloudcroftreader.com/` — should show the index page.
- `https://about.cloudcroftreader.com/llms.txt` — should serve the raw Markdown content of llms.txt.

Both must work over HTTPS with no certificate warning.

### Step 9. Reference from Substack

This is what makes the file discoverable. Two places to add the link:

**On your Substack About page** — open `https://www.cloudcroftreader.com/about` in the Substack editor and add a line near the bottom:

> For AI assistants and search agents: a machine-readable directory of this publication's content and editorial standards is available at [about.cloudcroftreader.com/llms.txt](https://about.cloudcroftreader.com/llms.txt).

**In your Substack publication settings** — Settings → Branding → Custom website footer (or similar; Substack moves these around), add the same link.

That's it for Path A.

---

## Path B — Cloudflare Pages

Use this only if you want to move cloudcroftreader.com's DNS to Cloudflare for the speed and security upgrades, not for this file alone.

### Step 1. Create the GitHub repo

Same as Path A, Steps 1–3.

### Step 2. Migrate DNS to Cloudflare

1. cloudflare.com → sign up (free).
2. Add a site → enter `cloudcroftreader.com` → Free plan.
3. Cloudflare scans your existing DNS records. **Review every one.** Confirm the records pointing to Substack are present and correct.
4. Cloudflare gives you two nameservers (e.g., `dana.ns.cloudflare.com`, `vlad.ns.cloudflare.com`).
5. Log into your domain registrar and change the nameservers for cloudcroftreader.com to the Cloudflare pair. Propagation: 1–24 hours.

⚠️ **Migration risk.** If you misconfigure any record during the import, your Substack site goes down until you fix it. Do the migration during a quiet window and have the Substack support DNS instructions open in another tab as backup.

### Step 3. Create the Pages project

1. Cloudflare dashboard → Workers & Pages → Create application → Pages → Connect to Git.
2. Authorize Cloudflare to read your GitHub.
3. Select the `cloudcroftreader-llms` repo.
4. Build settings: no build command, output directory `/`.
5. Deploy.

### Step 4. Bind the subdomain

1. In the Pages project → Custom domains → Set up a custom domain.
2. Enter `about.cloudcroftreader.com`.
3. Cloudflare auto-creates the DNS record because it's now managing the zone.

### Step 5. Verify and link from Substack

Same as Path A, Steps 8–9.

---

## Path C — AWS S3 + CloudFront

For consolidating with the existing DiscoverCloudcroft AWS hosting.

### Step 1. Create the S3 bucket

1. AWS Console → S3 → Create bucket.
2. Name: `about.cloudcroftreader.com` (must match the subdomain exactly).
3. Region: same as your existing buckets.
4. Untick "Block all public access" (and acknowledge — this bucket needs to be publicly readable).
5. Create.

### Step 2. Enable static website hosting

1. Bucket → Properties → Static website hosting → Edit → Enable.
2. Index document: `index.html`.
3. Error document: `index.html`.
4. Save.

### Step 3. Add bucket policy

Bucket → Permissions → Bucket policy → paste:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::about.cloudcroftreader.com/*"
  }]
}
```

### Step 4. Upload the files

Upload `index.html` and `llms.txt` from Path A, Step 3. Set Content-Type:
- `index.html` → `text/html`
- `llms.txt` → `text/plain; charset=utf-8` (or `text/markdown; charset=utf-8` if you prefer; both are acceptable per the llmstxt.org spec)

### Step 5. Request an ACM certificate

1. AWS Console → Certificate Manager → must be in **us-east-1** (required for CloudFront).
2. Request a public certificate for `about.cloudcroftreader.com`.
3. Validate via DNS — ACM gives you a CNAME record to add at your DNS host.
4. Wait for issuance (5–30 min).

### Step 6. Create the CloudFront distribution

1. CloudFront → Create distribution.
2. Origin: the S3 bucket's static-website endpoint (the long `…s3-website-us-east-1.amazonaws.com` URL, **not** the bucket REST endpoint).
3. Viewer protocol policy: Redirect HTTP to HTTPS.
4. Alternate domain name (CNAME): `about.cloudcroftreader.com`.
5. Custom SSL certificate: the ACM cert from Step 5.
6. Default root object: `index.html`.
7. Create.

Distribution takes 5–15 minutes to deploy. Cloudfront gives you a domain like `d1234abcd.cloudfront.net`.

### Step 7. DNS record

At your DNS host, add a CNAME:

| Field | Value |
|---|---|
| Type | `CNAME` |
| Name | `about` |
| Target | `d1234abcd.cloudfront.net` |

### Step 8. Verify and link from Substack

Same as Path A, Steps 8–9.

---

## Maintenance

- **Re-run the generation prompt every 90 days** to refresh the "Representative reporting" picks (per `cloudcroftreader-llms-txt-prompt.md`).
- When the file changes, commit to GitHub → Pages/Cloudflare auto-deploy; for AWS, re-upload to S3 and run a CloudFront invalidation: `aws cloudfront create-invalidation --distribution-id [ID] --paths "/*"`.
- Watch for Substack to announce native llms.txt support. If they ship it, mirror the file at the root (`cloudcroftreader.com/llms.txt`) and add a `Link:` HTTP header or `<link rel="ai-routing">` from the Substack pages to the canonical location. Keep the subdomain version live as a backup.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Browser shows certificate warning | HTTPS not yet provisioned | Wait 5–30 minutes; GitHub Pages/Cloudflare auto-provision after DNS resolves. |
| `about.cloudcroftreader.com` shows the Substack site | DNS conflict — a wildcard record is intercepting | Check for `*` CNAME at the registrar; remove or scope it. |
| `/llms.txt` downloads instead of displaying | Browser default behavior for `text/plain` — not a problem | Confirm it serves cleanly via `curl -I` and that the body is correct. |
| Substack edit doesn't save the about-page link | Substack rate-limits markdown updates on the about page | Wait a minute and retry. |

## What you'll have when this is done

- `https://about.cloudcroftreader.com/` — a minimal landing page that introduces the Reader to a human visitor and points them to the main Substack.
- `https://about.cloudcroftreader.com/llms.txt` — the machine-readable directory, deployment-ready and discoverable.
- A link from the Substack About page to the subdomain, completing the discovery loop for crawlers and LLM agents.
- A repeatable update path — edit the GitHub repo, every change auto-deploys.

Total ongoing cost: $0 (Path A) or $0–$1/month (Path C). Time to ship: 15–30 minutes the first time, 1 minute for every subsequent update.
