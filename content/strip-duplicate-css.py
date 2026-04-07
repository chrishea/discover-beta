#!/usr/bin/env python3
"""
Strip duplicate inline CSS from HTML files.
Removes CSS rules that are already defined in css/common.css,
keeping only page-specific overrides (hero background, unique components).
"""

import re
import os
import glob

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSS selectors/blocks that are fully covered by common.css
# These will be REMOVED from inline <style> blocks
DUPLICATE_SELECTORS = [
    # Hero (already in common.css)
    r'\.hero\s*\{[^}]*height:\s*65vh[^}]*\}',
    r'\.hero-badge\s+span\s*\{[^}]*\}',
    r'\.hero-title\s+\.word:nth-child\(\d+\)\s*\{[^}]*animation-delay[^}]*\}',
    r'\.hero-subtitle\s*\{[^}]*animation:\s*fadeUp[^}]*\}',
    r'\.hero-ctas\s*\{[^}]*animation:\s*fadeUp[^}]*\}',

    # Info bar (common.css lines 998-1040)
    r'\.info-bar\s*\{[^}]*background:\s*var\(--cream-dark\)[^}]*\}',
    r'\.info-bar-item\s*\{[^}]*color:\s*var\(--charcoal\)[^}]*\}',
    r'\.info-bar-item\s+a\s*\{[^}]*\}',
    r'\.info-bar-item\s+a:hover\s*\{[^}]*\}',
    r'\.info-bar-icon\s*\{[^}]*width:\s*40px[^}]*\}',

    # Menu section (common.css lines 1113-1198)
    r'\.menu-section\s*\{[^}]*background:\s*var\(--cloud-drift\)[^}]*\}',
    r'\.menu-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.menu-card\s*\{[^}]*background:\s*#ffffff[^}]*\}',
    r'\.menu-card\.visible\s*\{[^}]*\}',
    r'\.menu-card:nth-child\(\d+\)\.visible\s*\{[^}]*transition-delay[^}]*\}',
    r'\.menu-card:hover\s*\{[^}]*\}',
    r'\.menu-card-icon\s*\{[^}]*font-size:\s*2r?e?m?[^}]*\}',
    r'\.menu-card\s+h3\s*\{[^}]*\}',
    r'\.menu-card\s+p\s*\{[^}]*\}',
    r'\.menu-card\s*>\s*p\s*\{[^}]*\}',
    r'\.menu-items\s*\{[^}]*\}',
    r'\.menu-items\s+li\s*\{[^}]*\}',
    r'\.menu-items\s+li:last-child\s*\{[^}]*\}',

    # Highlight cards (common.css lines 1225-1272)
    r'\.highlight-card\s*\{[^}]*background:\s*rgba\(0,\s*0,\s*0,\s*0\.05\)[^}]*\}',
    r'\.highlight-card:hover\s*\{[^}]*background:\s*rgba\(0,\s*0,\s*0,\s*0\.1\)[^}]*\}',
    r'\.highlight-card\s+h3\s*\{[^}]*color:\s*#2B2B2B[^}]*\}',
    r'\.highlight-card\s+p\s*\{[^}]*color:\s*#555555[^}]*\}',

    # Gallery (now in common.css)
    r'\.gallery-grid\s*\{[^}]*display:\s*grid[^}]*\}',
    r'\.gallery-item\s*\{[^}]*border-radius:\s*12px[^}]*\}',
    r'\.gallery-item\.visible\s*\{[^}]*\}',
    r'\.gallery-item:nth-child\(\d+\)\.visible\s*\{[^}]*transition-delay[^}]*\}',
    r'\.gallery-item\s+img\s*\{[^}]*\}',
    r'\.gallery-item:hover\s+img\s*\{[^}]*transform:\s*scale[^}]*\}',
    r'\.gallery-caption\s*\{[^}]*position:\s*absolute[^}]*\}',
    r'\.gallery-item:hover\s+\.gallery-caption\s*\{[^}]*opacity:\s*1[^}]*\}',

    # Tip box (now in common.css)
    r'\.tip-box\s*\{[^}]*display:\s*flex[^}]*background:\s*#fffbe6[^}]*\}',
    r'\.tip-box\s+p\s*\{[^}]*\}',

    # CTA section (common.css lines 1323-1354)
    r'\.cta-section\s*\{[^}]*background:\s*#f2f2f2[^}]*\}',
    r'\.cta-container\s+h2\s*\{[^}]*color:\s*#2B2B2B[^}]*\}',
    r'\.cta-container\s+p\s*\{[^}]*color:\s*#555555[^}]*\}',
    r'\.cta-buttons\s*\{[^}]*display:\s*flex[^}]*\}',

    # Footer gradient (now in common.css)
    r'\.site-footer::before\s*\{[^}]*gradientBorder[^}]*\}',
    r'@keyframes\s+gradientBorder\s*\{[^}]*0%\s*\{[^}]*\}[^}]*100%\s*\{[^}]*\}[^}]*\}',

    # About image (common.css)
    r'\.about-image\s+img\s*\{[^}]*width:\s*100%[^}]*object-fit:\s*cover[^}]*border-radius:\s*12px[^}]*\}',
]

# Patterns for responsive blocks that only contain common component rules
DUPLICATE_MEDIA_CONTENT = [
    r'\.menu-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.gallery-grid\s*\{[^}]*grid-template-columns[^}]*\}',
    r'\.info-bar-inner\s*\{[^}]*gap[^}]*\}',
    r'\.cta-buttons\s*\{[^}]*flex-direction[^}]*\}',
    r'\.highlights-grid\s*\{[^}]*grid-template-columns[^}]*\}',
]

# Comments to strip
COMMENT_PATTERNS = [
    r'/\*\s*--?\s*Menu cards?\s*--?\s*\*/',
    r'/\*\s*--?\s*Highlights?\s*--?\s*\*/',
    r'/\*\s*--?\s*Gallery\s*--?\s*\*/',
    r'/\*\s*--?\s*Tip Box\s*--?\s*\*/',
    r'/\*\s*--?\s*CTA\s*--?\s*\*/',
    r'/\*\s*--?\s*Footer gradient\s*--?\s*\*/',
    r'/\*\s*--?\s*Responsive\s*--?\s*\*/',
    r'/\*\s*──\s*Menu cards?\s*──\s*\*/',
    r'/\*\s*──\s*Highlights?\s*──\s*\*/',
    r'/\*\s*──\s*Gallery\s*──\s*\*/',
    r'/\*\s*──\s*Tip Box\s*──\s*\*/',
    r'/\*\s*──\s*CTA\s*──\s*\*/',
    r'/\*\s*──\s*Footer gradient\s*──\s*\*/',
    r'/\*\s*──\s*Responsive\s*──\s*\*/',
    r'/\*\s*──\s*Info Bar\s*──\s*\*/',
    r'/\*\s*--?\s*Info Bar\s*--?\s*\*/',
]


def strip_duplicate_css(style_content):
    """Remove duplicate CSS rules from a style block."""
    original = style_content

    # Strip duplicate selectors
    for pattern in DUPLICATE_SELECTORS:
        style_content = re.sub(pattern, '', style_content, flags=re.DOTALL)

    # Handle @keyframes gradientBorder (multiline with nested braces)
    style_content = re.sub(
        r'@keyframes\s+gradientBorder\s*\{[^}]*\{[^}]*\}[^}]*\{[^}]*\}\s*\}',
        '', style_content, flags=re.DOTALL
    )

    # Handle @media blocks — strip rules inside them that are duplicates
    def clean_media_block(match):
        media_query = match.group(1)
        media_content = match.group(2)

        for pattern in DUPLICATE_MEDIA_CONTENT:
            media_content = re.sub(pattern, '', media_content, flags=re.DOTALL)

        # If media block is now empty (only whitespace), remove entirely
        if re.match(r'^\s*$', media_content):
            return ''

        return f'@media {media_query} {{{media_content}}}'

    style_content = re.sub(
        r'@media\s*(\([^)]+\))\s*\{((?:[^{}]|\{[^}]*\})*)\}',
        clean_media_block, style_content, flags=re.DOTALL
    )

    # Strip orphaned comments
    for pattern in COMMENT_PATTERNS:
        style_content = re.sub(pattern, '', style_content, flags=re.IGNORECASE)

    # Clean up excessive blank lines (more than 2 consecutive)
    style_content = re.sub(r'\n{3,}', '\n\n', style_content)

    # Clean up lines that are only whitespace
    lines = style_content.split('\n')
    cleaned_lines = []
    blank_count = 0
    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 1:
                cleaned_lines.append(line)
        else:
            blank_count = 0
            cleaned_lines.append(line)

    style_content = '\n'.join(cleaned_lines)

    return style_content


def process_hero_bg(style_content):
    """
    Simplify .hero-bg to only keep the background property.
    Remove background-size (redundant with shorthand) and animation (in common.css).
    """
    # Match .hero-bg block and extract just the background URL/gradient
    def simplify_hero_bg(match):
        block = match.group(0)
        # Extract the background line
        bg_match = re.search(r'background:\s*url\([^)]+\)[^;]*;', block)
        if bg_match:
            bg_line = bg_match.group(0)
            return f'.hero-bg {{\n    {bg_line}\n}}'
        # Keep gradient backgrounds too
        bg_match = re.search(r'background:\s*linear-gradient\([^;]+;', block)
        if bg_match:
            bg_line = bg_match.group(0)
            return f'.hero-bg {{\n    {bg_line}\n}}'
        return block

    style_content = re.sub(
        r'\.hero-bg\s*\{[^}]*\}',
        simplify_hero_bg, style_content, flags=re.DOTALL
    )

    return style_content


def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find inline <style> blocks
    style_pattern = re.compile(r'(<style>)(.*?)(</style>)', re.DOTALL)
    matches = list(style_pattern.finditer(content))

    if not matches:
        return False, 0, 0

    modified = False
    for match in reversed(matches):  # Process from end to preserve positions
        original_style = match.group(2)
        cleaned_style = strip_duplicate_css(original_style)
        cleaned_style = process_hero_bg(cleaned_style)

        if cleaned_style != original_style:
            start = match.start(2)
            end = match.end(2)
            content = content[:start] + cleaned_style + content[end:]
            modified = True

    if modified:
        original_len = len(match.group(2))
        new_len = len(cleaned_style)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, original_len, new_len

    return False, 0, 0


def main():
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(PROJECT):
        # Skip hidden dirs and data dir
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for f in files:
            if f.endswith('.html') and f != 'google8739391a40d00bda.html':
                html_files.append(os.path.join(root, f))

    html_files.sort()

    total_modified = 0
    total_saved = 0

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, PROJECT)
        modified, orig_len, new_len = process_file(filepath)
        if modified:
            saved = orig_len - new_len
            total_saved += saved
            total_modified += 1
            print(f"  ✓ {rel_path} (−{saved} chars)")
        else:
            print(f"  · {rel_path} (no changes)")

    print(f"\n{'='*50}")
    print(f"Modified: {total_modified} files")
    print(f"Total CSS removed: ~{total_saved:,} characters")


if __name__ == '__main__':
    main()
