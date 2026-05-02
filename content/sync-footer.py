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
        <p style="text-align:center;padding:1vh;font-weight:700;">
            <span class="footer-brand">DISCOVER <span>CLOUDCROFT</span></span>
            | <span style="color:coral;">New Mexico's Mountain Retreat</span>
        </p>
        <p style="text-align:center;font-size:85%;">
            &copy; 2026
            <a href="https://www.DiscoverCloudcroft.com" target="_blank" rel="noopener noreferrer"
                style="color:rgb(194,224,249);text-decoration:underline;">DiscoverCloudcroft.com</a>.
            All rights reserved.
        </p>
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
