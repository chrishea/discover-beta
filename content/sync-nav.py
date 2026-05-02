#!/usr/bin/env python3
"""
Sync top nav across HTML files.

Replaces the entire `<header class="site-header">...</header>` block plus
any number of trailing `<nav class="mobile-nav-overlay">...</nav>` blocks
with a single canonical pair, prefixed correctly based on file depth.

Earlier versions of this script had two bugs:
  1) build_nav() accepted a `prefix` arg but never applied it, so deep
     pages got root-level paths that 404 from inside subdirs.
  2) The regex matched `<div class="mobile-nav-overlay">` while the actual
     HTML uses `<nav>`, so each run *appended* a new mobile-nav block
     instead of replacing the existing one — leading to 4–8 duplicate
     mobile-nav blocks in many shop/ and eat/ pages.

Both fixes land in this rewrite. The replacement regex now greedily
consumes any number of consecutive mobile-nav blocks, so a single run
collapses duplicates back to one.

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


def build_nav(prefix: str) -> str:
    p = prefix
    return f'''<header class="site-header" role="banner">
        <div class="header-inner">

            <nav class="header-nav" role="navigation" aria-label="Main navigation">
                <a href="{p}index.html" class="logo header-logo" aria-label="Discover Cloudcroft — home">
                    <span class="logo-discover">Discover</span>
                    <span class="logo-cloudcroft">Cloudcroft</span>
                </a>
                <a href="{p}stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html">Stay</a>
                <a href="{p}eat/complete-guide-where-to-eat-in-cloudcroft-2026.html">Eat</a>
                <a href="{p}do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html">Activities</a>
                <a href="{p}shop/complete-guide-where-to-shop-in-cloudcroft-2026.html">Shop</a>
                <a href="{p}events/top-events.html">Events</a>

                <a href="{p}resources/resources.html">Resources</a>
                <a href="{p}resources/contact.html">Contact</a>
                <button type="button" class="nav-cta" data-signup-open data-signup-source="nav-mobile">Connect</button>
            </nav>
            <button class="hamburger" type="button" aria-label="Open navigation menu" aria-expanded="false"
                aria-controls="mobile-nav">
                <span></span><span></span><span></span>
            </button>
        </div>


        <nav class="mobile-nav-overlay" id="mobile-nav" aria-label="Mobile navigation" hidden>
            <a href="{p}stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html">Stay</a>
            <a href="{p}eat/complete-guide-where-to-eat-in-cloudcroft-2026.html">Eat</a>
            <a href="{p}do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html">Activities</a>
            <a href="{p}shop/complete-guide-where-to-shop-in-cloudcroft-2026.html">Shop</a>
            <a href="{p}events/top-events.html">Events</a>

            <a href="{p}resources/resources.html">Resources</a>
            <a href="{p}resources/contact.html">Contact</a>


        </nav>
    </header>'''


# Match the full header+mobile-nav region:
#   <header class="site-header"...</header>
#   followed by ANY NUMBER of trailing <nav class="mobile-nav-overlay">...</nav>
#   blocks (with whitespace between them).
# Also match legacy <div class="mobile-nav-overlay">...</div> for safety.
PATTERN = re.compile(
    r'<header class="site-header".*?</header>'
    r'(?:\s*(?:<nav class="mobile-nav-overlay".*?</nav>'
    r'|<div class="mobile-nav-overlay".*?</div>))*',
    re.DOTALL,
)


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
                        help='Process only HTML files under this directory '
                             '(relative to repo root or absolute).')
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
        depth = rel.count(os.sep)
        prefix = '../' * depth
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
        new_nav = build_nav(prefix)
        new_content, n = PATTERN.subn(new_nav, content, count=1)
        if n == 0:
            no_match += 1
            if args.verbose:
                print(f"  ?  {rel}  (no header block found)")
            continue
        if new_content == content:
            no_change += 1
            if args.verbose:
                print(f"  ·  {rel}  (already in sync)")
            continue
        # Count how many mobile-nav blocks the regex absorbed (for reporting)
        absorbed = content.count('<nav class="mobile-nav-overlay"')
        mark = '~' if args.dry_run else '✓'
        suffix = f"  [collapsed {absorbed} mobile-nav blocks]" if absorbed > 1 else ""
        if not args.dry_run:
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
        count += 1
        print(f"  {mark} {rel}{suffix}")

    print("=" * 60)
    word = 'WOULD update' if args.dry_run else 'Updated'
    print(f"{word}: {count} file(s)")
    if no_match:
        print(f"No header-block match: {no_match} file(s)")
    if no_change:
        print(f"Already in sync: {no_change} file(s)")


if __name__ == '__main__':
    main()
