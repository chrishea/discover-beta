#!/usr/bin/env python3
"""
Generate an Atom 1.0 feed at /feed.xml from the most recently-modified
HTML pages on the site.

How it works:
  1. Walks every published .html file (skipping shelf/, drafts/,
     content-archive/, the Google verification file).
  2. Extracts canonical URL, <title>, meta description, and the
     dateModified value from the page's JSON-LD blocks.
  3. Sorts by dateModified descending.
  4. Takes the top N (default 25).
  5. Writes /feed.xml at repo root.

Usage:
  python3 content/sync-feed.py
  python3 content/sync-feed.py --max 40
  python3 content/sync-feed.py --dry-run

Re-run whenever pages get new dateModified stamps.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_URL = 'https://discovercloudcroft.com'
FEED_URL = f'{SITE_URL}/feed.xml'
SITE_NAME = 'DiscoverCloudcroft.com'
SITE_TAGLINE = "An independent visitor's guide to Cloudcroft, NM."
AUTHOR_NAME = 'DiscoverCloudcroft editors'
AUTHOR_EMAIL = 'hello@discovercloudcroft.com'

SKIP_DIRS = {'.claude', '.git', 'node_modules', 'media-originals',
             'drafts', 'shelf', 'content-archive'}
SKIP_FILES = {'google8739391a40d00bda.html', 'feed.xml'}


def extract_metadata(filepath: str):
    """Return (canonical_url, title, description, date_modified) or None."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception:
        return None

    # Title
    m = re.search(r'<title>([^<]+)</title>', html)
    title = m.group(1).strip() if m else None
    if not title:
        return None

    # Canonical URL — REQUIRED. Skip pages without it (drafts, mockups).
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
    if not m:
        return None
    canonical = m.group(1).strip()

    # Description
    m = re.search(
        r'<meta\s+name="description"\s+content="([^"]+)"', html)
    description = m.group(1).strip() if m else ''

    # dateModified — pull from any JSON-LD block. Take the most-recent
    # if multiple blocks have it.
    dates = []
    blocks = re.findall(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        html, re.DOTALL)
    for b in blocks:
        try:
            obj = json.loads(b)
            items = obj if isinstance(obj, list) else [obj]
            for item in items:
                if isinstance(item, dict):
                    d = item.get('dateModified')
                    if isinstance(d, str):
                        dates.append(d)
        except Exception:
            continue
    if not dates:
        # Fall back to file mtime
        date_modified = datetime.fromtimestamp(
            os.path.getmtime(filepath),
            tz=timezone.utc).date().isoformat()
    else:
        date_modified = max(dates)
    return canonical, title, description, date_modified


def find_pages():
    """Walk the project and yield candidate HTML files."""
    out = []
    for r, dirs, files in os.walk(PROJECT):
        dirs[:] = [d for d in dirs
                   if not d.startswith('.') and d not in SKIP_DIRS]
        for f in files:
            if not f.endswith('.html'):
                continue
            if f in SKIP_FILES:
                continue
            if 'copy' in f.lower() or f.startswith('xxx-'):
                continue
            out.append(os.path.join(r, f))
    return out


def xml_escape(s: str) -> str:
    return (s.replace('&', '&amp;')
             .replace('<', '&lt;')
             .replace('>', '&gt;')
             .replace('"', '&quot;'))


def to_iso8601(date_str: str) -> str:
    """Convert YYYY-MM-DD to YYYY-MM-DDT00:00:00Z."""
    return f'{date_str}T00:00:00Z'


def build_atom(entries: list, generated_at: str) -> str:
    """Build an Atom 1.0 feed string."""
    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<feed xmlns="http://www.w3.org/2005/Atom">')
    lines.append('')
    lines.append(f'  <title>{xml_escape(SITE_NAME)}</title>')
    lines.append(f'  <subtitle>{xml_escape(SITE_TAGLINE)}</subtitle>')
    lines.append(f'  <link href="{SITE_URL}/" />')
    lines.append(f'  <link rel="self" type="application/atom+xml" '
                 f'href="{FEED_URL}" />')
    lines.append(f'  <id>{SITE_URL}/</id>')
    lines.append(f'  <updated>{generated_at}</updated>')
    lines.append('  <author>')
    lines.append(f'    <name>{xml_escape(AUTHOR_NAME)}</name>')
    lines.append(f'    <email>{AUTHOR_EMAIL}</email>')
    lines.append('  </author>')
    lines.append('  <rights>'
                 'Copyright 2026 Mountain Monthly LLC. '
                 'Editorial content; see editorial standards at '
                 f'{SITE_URL}/about/editorial-standards.html'
                 '</rights>')
    lines.append('')
    for url, title, desc, date in entries:
        lines.append('  <entry>')
        lines.append(f'    <title>{xml_escape(title)}</title>')
        lines.append(f'    <link href="{xml_escape(url)}" />')
        lines.append(f'    <id>{xml_escape(url)}</id>')
        lines.append(f'    <updated>{to_iso8601(date)}</updated>')
        if desc:
            lines.append(f'    <summary>{xml_escape(desc)}</summary>')
        lines.append('    <author>')
        lines.append(f'      <name>{xml_escape(AUTHOR_NAME)}</name>')
        lines.append('    </author>')
        lines.append('  </entry>')
        lines.append('')
    lines.append('</feed>')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--max', type=int, default=25,
                        help='Max number of entries (default 25).')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print planned entries; do not write file.')
    args = parser.parse_args()

    files = find_pages()
    rows = []
    for fp in files:
        meta = extract_metadata(fp)
        if not meta:
            continue
        rows.append(meta)

    # Sort by dateModified descending, then by URL for stability
    rows.sort(key=lambda r: (r[3], r[0]), reverse=True)
    entries = rows[:args.max]

    generated_at = datetime.now(tz=timezone.utc).strftime(
        '%Y-%m-%dT%H:%M:%SZ')

    feed = build_atom(entries, generated_at)

    target = os.path.join(PROJECT, 'feed.xml')
    print(f'Total candidate pages: {len(rows)}')
    print(f'Entries in feed:       {len(entries)}')
    print(f'Generated at:          {generated_at}')
    print()
    print('Top 10 entries:')
    for url, title, desc, date in entries[:10]:
        print(f'  {date}  {url}')
    print()
    if args.dry_run:
        print('DRY RUN — not writing.')
        return
    with open(target, 'w', encoding='utf-8') as f:
        f.write(feed)
    print(f'Wrote: {target}')


if __name__ == '__main__':
    main()
