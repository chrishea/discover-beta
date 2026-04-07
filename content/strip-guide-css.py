#!/usr/bin/env python3
"""
Strip duplicate guide-page CSS from HTML files (pass 2).
Removes TOC, market, lodge, compare, pick, tip card patterns
now consolidated into common.css.
"""

import re
import os

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Guide component selectors to strip
GUIDE_SELECTORS = [
    # TOC nav
    r'\.toc-nav\s*\{[^}]*position:\s*sticky[^}]*\}',
    r'\.toc-nav-inner\s*\{[^}]*\}',
    r'\.toc-nav-inner::-webkit-scrollbar\s*\{[^}]*\}',
    r'\.toc-pill\s*\{[^}]*\}',
    r'\.toc-pill:hover\s*\{[^}]*\}',

    # Market cards
    r'\.market-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.market-card\s*\{[^}]*background:\s*#ffffff[^}]*\}',
    r'\.market-card\.visible\s*\{[^}]*\}',
    r'\.market-card:nth-child\(\d+\)\.visible\s*\{[^}]*\}',
    r'\.market-card-icon\s*\{[^}]*\}',
    r'\.market-card\s+h3\s*\{[^}]*\}',
    r'\.market-card\s+p\s*\{[^}]*\}',

    # Lodge cards
    r'\.lodge-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.lodge-card\s*\{[^}]*background:\s*#ffffff[^}]*\}',
    r'\.lodge-card\.visible\s*\{[^}]*\}',
    r'\.lodge-card:nth-child\(\d+\)\.visible\s*\{[^}]*\}',
    r'\.lodge-card\s+img\s*\{[^}]*\}',
    r'\.lodge-card-icon\s*\{[^}]*\}',
    r'\.lodge-card\s+h3\s*\{[^}]*\}',
    r'\.lodge-card\s+p\s*\{[^}]*\}',
    r'\.lodge-card-contact\s*\{[^}]*\}',
    r'\.lodge-card-contact\s+a\s*\{[^}]*\}',
    r'\.lodge-card-contact\s+a:hover\s*\{[^}]*\}',
    r'\.lodge-card-guide\s*\{[^}]*\}',
    r'\.lodge-card-guide:hover\s*\{[^}]*\}',
    r'\.property-type\s*\{[^}]*\}',

    # Compare cards
    r'\.compare-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.compare-card\s*\{[^}]*background:\s*#ffffff[^}]*\}',
    r'\.compare-card\.visible\s*\{[^}]*\}',
    r'\.compare-card:nth-child\(\d+\)\.visible\s*\{[^}]*\}',
    r'\.compare-card\s+h3\s*\{[^}]*\}',
    r'\.compare-card\s+p\s*\{[^}]*\}',
    r'\.compare-card\s+\.pick-name\s*\{[^}]*\}',

    # Pick cards
    r'\.picks-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.pick-card\s*\{[^}]*background:\s*#c9e0a5[^}]*\}',
    r'\.pick-card\.visible\s*\{[^}]*\}',
    r'\.pick-card:nth-child\(\d+\)\.visible\s*\{[^}]*\}',
    r'\.pick-card-icon\s*\{[^}]*\}',
    r'\.pick-card\s+h3\s*\{[^}]*\}',
    r'\.pick-card\s+p\s*\{[^}]*\}',

    # Tip cards
    r'\.tip-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.tip-card\s*\{[^}]*background:\s*#ffffff[^}]*\}',
    r'\.tip-card\.visible\s*\{[^}]*\}',
    r'\.tip-card:nth-child\(\d+\)\.visible\s*\{[^}]*\}',
    r'\.tip-card-icon\s*\{[^}]*\}',
    r'\.tip-card\s+h3\s*\{[^}]*\}',
    r'\.tip-card\s+p\s*\{[^}]*\}',

    # Bottom line section
    r'\.bottom-line-section\s*\{[^}]*background:\s*#000000[^}]*\}',
    r'\.bottom-line-inner\s*\{[^}]*\}',
    r'\.bottom-line-inner\s+h2\s*\{[^}]*\}',
    r'\.bottom-line-inner\s+p\s*\{[^}]*\}',

    # Section alt
    r'\.section-alt\s*\{[^}]*background:\s*var\(--cloud-drift\)[^}]*\}',
]

# Media query content to strip
GUIDE_MEDIA_CONTENT = [
    r'\.lodge-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.market-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.compare-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.picks-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.tip-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.toc-nav-inner\s*\{[^}]*padding[^}]*\}',
]

# Comments to strip
GUIDE_COMMENTS = [
    r'/\*\s*──\s*Sticky TOC Nav\s*──\s*\*/',
    r'/\*\s*──\s*Market Grid[^*]*\*/',
    r'/\*\s*──\s*Property Grid[^*]*\*/',
    r'/\*\s*──\s*Compare Grid\s*──\s*\*/',
    r'/\*\s*──\s*Pick Cards[^*]*\*/',
    r'/\*\s*──\s*Tip Cards\s*──\s*\*/',
    r'/\*\s*──\s*Bottom Line[^*]*\*/',
    r'/\*\s*──\s*Cloud-drift[^*]*\*/',
]


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Strip guide selectors
    for pattern in GUIDE_SELECTORS:
        content = re.sub(pattern, '', content, flags=re.DOTALL)

    # Strip guide comments
    for pattern in GUIDE_COMMENTS:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)

    # Clean media blocks
    def clean_media(match):
        mq = match.group(1)
        mc = match.group(2)
        for p in GUIDE_MEDIA_CONTENT:
            mc = re.sub(p, '', mc, flags=re.DOTALL)
        if re.match(r'^\s*$', mc):
            return ''
        return f'@media {mq} {{{mc}}}'

    content = re.sub(
        r'@media\s*(\([^)]+\))\s*\{((?:[^{}]|\{[^}]*\})*)\}',
        clean_media, content, flags=re.DOTALL
    )

    # Clean up blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Clean orphaned section comments
    content = re.sub(r'/\*\s*──[^*]*──\s*\*/\s*\n\s*\n', '\n', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        saved = len(original) - len(content)
        return True, saved
    return False, 0


def main():
    total_modified = 0
    total_saved = 0

    for root, dirs, files in os.walk(PROJECT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for f in sorted(files):
            if not f.endswith('.html') or f == 'google8739391a40d00bda.html':
                continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, PROJECT)
            modified, saved = process_file(fp)
            if modified:
                total_modified += 1
                total_saved += saved
                print(f"  ✓ {rel} (−{saved} chars)")

    print(f"\n{'='*50}")
    print(f"Modified: {total_modified} files")
    print(f"Total CSS removed: ~{total_saved:,} characters")


if __name__ == '__main__':
    main()
