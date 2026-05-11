#!/usr/bin/env python3
"""
Sync the site footer across HTML files.

Replaces the entire `<footer class="site-footer">...</footer>` block with
a single canonical footer.

CLI:
  --dir PATH       Process only HTML files under this directory
                   (relative to repo root). Default: whole repo.
  --dry-run        Report planned changes without writing.
  --verbose        Print every file checked (not just changed).
"""

import argparse
import os
import re
import sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


FOOTER = '''<footer class="site-footer" role="contentinfo" aria-label="Site footer">
        <div class="footer-inner">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="/" class="footer-brand-mark">DISCOVER <span>CLOUDCROFT</span></a>
                    <p>An independent visitor's guide to Cloudcroft, New Mexico's mountain retreat. Lodging, dining,
                        activities, shopping, events, and seasonal travel
                        planning. </p>
                </div>
                <div class="footer-col">
                    <h4>Explore</h4>
                    <ul>
                        <li><a href="/stay/complete-guide-to-lodging-in-cloudcroft-new-mexico.html">Stay</a></li>
                        <li><a href="/eat/complete-guide-where-to-eat-in-cloudcroft.html">Eat</a></li>
                        <li><a href="/do/complete-guide-to-activities-to-do-in-cloudcroft.html">Activities</a></li>
                        <li><a href="/shop/complete-guide-where-to-shop-in-cloudcroft.html">Shop</a></li>
                        <li><a href="/visit/where-to-visit.html">Visit</a></li>
                        <li><a href="/events/top-events.html">Events</a></li>
                        <li><a href="/topics/">Topics</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>About</h4>
                    <ul>
                        <li><a href="/resources/about.html">About us</a></li>
                        <li><a href="/about/editorial-standards.html">Editorial standards</a></li>
                        <li><a href="/about/privacy.html">Privacy policy</a></li>
                        <li><a href="/about/terms.html">Terms of service</a></li>
                        <li><a href="/resources/contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Stay in touch</h4>
                    <p>Monthly updates from DiscoverCloudcroft. No spam. Unsubscribe anytime.</p>
                    <button type="button" class="footer-cta" data-signup-open
                        data-signup-source="footer">Subscribe</button>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 <a href="https://discovercloudcroft.com/" style="color:coral;"
                        rel="noopener noreferrer">DiscoverCloudcroft.com</a>, powered by Mountain Monthly LLC, the
                    mountain's newspaper since 1988. All rights reserved.</p>

            </div>
        </div>
    </footer>'''


PATTERN = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)


def find_html_files(root):
    out = []
    for r, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for f in files:
            if not f.endswith('.html') or f == 'google8739391a40d00bda.html':
                continue
            out.append(os.path.join(r, f))
    out.sort()
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dir', type=str, default=None,
                        help='Process only HTML files under this directory.')
    parser.add_argument('--dry-run', action='store_true',
                        help='Report planned changes without writing.')
    parser.add_argument('--verbose', action='store_true',
                        help='Print every file checked.')
    args = parser.parse_args()

    if args.dir:
        target_root = args.dir
        if not os.path.isabs(target_root):
            target_root = os.path.join(PROJECT, target_root)
        if not os.path.isdir(target_root):
            sys.exit(f"FATAL: {target_root} is not a directory")
    else:
        target_root = PROJECT

    files = find_html_files(target_root)
    rel_root = os.path.relpath(target_root, PROJECT)
    mode = 'DRY-RUN' if args.dry_run else 'WRITE'
    print(f"Mode: {mode}")
    print(f"Scope: {rel_root}/  ({len(files)} HTML files)")
    print("=" * 60)

    count = 0
    no_match = 0
    no_change = 0

    for fp in files:
        rel = os.path.relpath(fp, PROJECT)
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
        new_content, n = PATTERN.subn(FOOTER, content, count=1)
        if n == 0:
            no_match += 1
            if args.verbose:
                print(f"  ?  {rel}  (no <footer class=\"site-footer\"> found)")
            continue
        if new_content == content:
            no_change += 1
            if args.verbose:
                print(f"  ·  {rel}  (already in sync)")
            continue
        mark = '~' if args.dry_run else '✓'
        if not args.dry_run:
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
        count += 1
        print(f"  {mark} {rel}")

    print("=" * 60)
    word = 'WOULD update' if args.dry_run else 'Updated'
    print(f"{word}: {count} file(s)")
    if no_match:
        print(f"No footer-block match: {no_match} file(s)")
    if no_change:
        print(f"Already in sync: {no_change} file(s)")


if __name__ == '__main__':
    main()
