#!/usr/bin/env python3
"""
Inject the Google Analytics 4 (gtag.js) snippet into every published
HTML page's <head>, right after the opening <head> tag.

Idempotent: if the GA_ID string is already present on a page, the page
is skipped. Re-running this script never duplicates the tag.

Skips: shelf/, drafts/, .claude/, media-originals/, content-archive/,
the Google site-verification file.

CLI:
  --dry-run     Report planned changes without writing.
  --verbose     Print every file checked.
  --ga-id ID    Override the default Measurement ID.
"""

import argparse
import os
import re
import sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_GA_ID = 'G-2CQ53PCP3M'

SKIP_DIRS = {'.claude', '.git', 'node_modules', 'media-originals',
             'drafts', 'shelf', 'content-archive'}
SKIP_FILES = {'google8739391a40d00bda.html'}


def gtag_snippet(ga_id: str) -> str:
    """The exact gtag.js block used on the 3 pages that already had it."""
    return (
        '\n'
        '    <!-- Google tag (gtag.js) -->\n'
        f'    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>\n'
        '    <script>\n'
        '      window.dataLayer = window.dataLayer || [];\n'
        '      function gtag(){dataLayer.push(arguments);}\n'
        '      gtag(\'js\', new Date());\n'
        '\n'
        f'      gtag(\'config\', \'{ga_id}\');\n'
        '    </script>\n'
    )


def find_html_files(root: str):
    out = []
    for r, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs
                   if not d.startswith('.') and d not in SKIP_DIRS]
        for f in files:
            if not f.endswith('.html'):
                continue
            if f in SKIP_FILES:
                continue
            out.append(os.path.join(r, f))
    out.sort()
    return out


def inject(html: str, ga_id: str) -> tuple[str, bool]:
    """Return (new_html, changed). Idempotent — skip if already present."""
    if ga_id in html:
        return html, False
    # Insert right after the opening <head> tag.
    # Match the literal "<head>" with optional attributes (rare but safe).
    pattern = re.compile(r'(<head\b[^>]*>)', re.IGNORECASE)
    m = pattern.search(html)
    if not m:
        return html, False
    insert_at = m.end()
    new_html = html[:insert_at] + gtag_snippet(ga_id) + html[insert_at:]
    return new_html, True


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true',
                        help='Report planned changes without writing.')
    parser.add_argument('--verbose', action='store_true',
                        help='Print every file checked.')
    parser.add_argument('--ga-id', default=DEFAULT_GA_ID,
                        help=f'GA4 Measurement ID (default {DEFAULT_GA_ID}).')
    args = parser.parse_args()

    files = find_html_files(PROJECT)
    mode = 'DRY-RUN' if args.dry_run else 'WRITE'
    print(f'Mode: {mode}')
    print(f'GA ID: {args.ga_id}')
    print(f'Files: {len(files)}')
    print('=' * 60)

    injected = 0
    already_present = 0
    no_head = 0

    for fp in files:
        rel = os.path.relpath(fp, PROJECT)
        with open(fp, 'r', encoding='utf-8') as fh:
            html = fh.read()
        if args.ga_id in html:
            already_present += 1
            if args.verbose:
                print(f'  · {rel}  (GA already present)')
            continue
        new_html, changed = inject(html, args.ga_id)
        if not changed:
            no_head += 1
            print(f'  ! {rel}  (no <head> found — skipped)')
            continue
        mark = '~' if args.dry_run else '✓'
        if not args.dry_run:
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(new_html)
        injected += 1
        if args.verbose or not args.dry_run:
            print(f'  {mark} {rel}')

    print('=' * 60)
    word = 'WOULD inject' if args.dry_run else 'Injected'
    print(f'{word}: {injected} file(s)')
    print(f'Already present: {already_present} file(s)')
    if no_head:
        print(f'No <head> found: {no_head} file(s)')


if __name__ == '__main__':
    main()
