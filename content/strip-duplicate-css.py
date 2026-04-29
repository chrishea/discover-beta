#!/usr/bin/env python3
"""
Strip duplicate inline CSS from HTML files.

Approach:
1. Parse css/common.css into a set of top-level selectors (truth source).
2. For each .html file, find <style> blocks.
3. Parse each <style> block into rule chunks using a brace-aware walker
   (handles @keyframes, @media, and other nested-brace rules).
4. Remove rules whose normalized selector exists in common.css, EXCEPT for
   selectors in PRESERVE_INLINE (page-specific overrides like `.hero-bg`).
5. Remove orphaned section comments.
6. Collapse runs of blank lines.

CLI:
  --dry-run             Parse + report what would be removed; do not write.
  --file PATH           Target a single .html file (relative or absolute).
  --verbose             Print every removed selector.
  (no flags)            Process every .html file in the project.

The previous regex-based DUPLICATE_SELECTORS list was hard-coded against
the older detail-page system and missed the 2026 detail-page selectors
(.atglance, .menu-card-plus, .hours-table, .map-svg, .goodfor-grid,
.gallery-grid, .handoff-grid, .editor-wrap, .thesis, .picks-section,
.signals-inner, .stats-strip, .toc-nav, .note, .detail-block, …).
This rewrite reads common.css directly so it stays in sync automatically.
"""

import argparse
import os
import re
import sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMON_CSS = os.path.join(PROJECT, 'css', 'common.css')

# Selectors that MUST stay inline even if they exist in common.css.
# These carry per-page overrides (hero photo URL, page-specific overlays).
PRESERVE_INLINE = {
    '.hero-bg',
    '.hero-overlay',
    # Per-page hero word-span keyframe / animation tweaks
    '.hero-left h1 .word',
    '.hero-left h1 .word:nth-child(1)',
    '.hero-left h1 .word:nth-child(2)',
    '.hero-left h1 .word:nth-child(3)',
    '.hero-left h1 .word:nth-child(4)',
    '@keyframes heroWord',
}

# Section header / divider comments that get orphaned once their rules
# are removed. Drop them so we don't leave dangling decoration.
ORPHAN_COMMENT_PATTERNS = [
    r'/\*\s*--+\s*Hero(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*At-a-glance(?:\s+card)?\s*--+\s*\*/',
    r'/\*\s*--+\s*Signals?(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Stats?(?:\s+strip)?\s*--+\s*\*/',
    r'/\*\s*--+\s*TOC(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Thesis(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Menu(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Picks?(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Hours?(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Map(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Location(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Good[- ]?for(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Gallery(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Notes?(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Editor(?:\'s)?(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Handoff(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*CTA(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Footer(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Responsive(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Info[- ]?bar(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Highlights?(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*Tip[- ]?box(?:\s+\w+)*\s*--+\s*\*/',
    r'/\*\s*--+\s*About(?:\s+\w+)*\s*--+\s*\*/',
]


# ---------------------------------------------------------------------------
# CSS rule-block parser (brace-aware)
# ---------------------------------------------------------------------------

def parse_css_rules(css):
    """
    Walk a CSS string and yield (selector, full_block_text, start, end) for
    each top-level rule. Handles nested braces inside @keyframes / @media.

    Returns a list of dicts: {selector, full_text, start, end, body, is_at}.
    """
    rules = []
    i = 0
    n = len(css)
    while i < n:
        # Skip whitespace and comments at top level
        while i < n and css[i].isspace():
            i += 1
        if i >= n:
            break
        if css[i:i+2] == '/*':
            end = css.find('*/', i + 2)
            if end == -1:
                break
            i = end + 2
            continue

        # Begin selector. Read until '{', skipping comments inside.
        sel_start = i
        depth = 0
        while i < n:
            if css[i:i+2] == '/*':
                end = css.find('*/', i + 2)
                if end == -1:
                    return rules
                i = end + 2
                continue
            ch = css[i]
            if ch == '{':
                break
            i += 1
        if i >= n:
            break
        selector = css[sel_start:i].strip()
        body_open = i  # at '{'
        i += 1

        # Read the body, balancing braces.
        depth = 1
        while i < n and depth > 0:
            if css[i:i+2] == '/*':
                end = css.find('*/', i + 2)
                if end == -1:
                    return rules
                i = end + 2
                continue
            ch = css[i]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            i += 1
        body_close = i  # one past the closing '}'

        rule_text = css[sel_start:body_close]
        body_text = css[body_open + 1:body_close - 1]
        rules.append({
            'selector': selector,
            'full_text': rule_text,
            'start': sel_start,
            'end': body_close,
            'body': body_text,
            'is_at': selector.startswith('@'),
        })
    return rules


def normalize_selector(sel):
    """Lowercase and collapse whitespace for selector matching."""
    return re.sub(r'\s+', ' ', sel).strip()


def split_selector_list(sel):
    """A rule like `a, b, c { ... }` has 3 selectors. Split and trim."""
    parts = []
    depth = 0
    buf = []
    for ch in sel:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(''.join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append(''.join(buf).strip())
    return parts


# ---------------------------------------------------------------------------
# common.css selector set
# ---------------------------------------------------------------------------

def load_common_selectors():
    """Return a set of normalized top-level selectors defined in common.css."""
    if not os.path.exists(COMMON_CSS):
        sys.exit(f"FATAL: cannot find {COMMON_CSS}")
    with open(COMMON_CSS, 'r', encoding='utf-8') as f:
        css = f.read()

    selectors = set()
    for rule in parse_css_rules(css):
        sel = rule['selector']
        # @media / @supports: descend one level and collect inner selectors too
        if rule['is_at'] and (sel.startswith('@media') or sel.startswith('@supports')):
            inner = parse_css_rules(rule['body'])
            for inner_rule in inner:
                for s in split_selector_list(inner_rule['selector']):
                    selectors.add(normalize_selector(s))
            # Also record the @media block itself as a "container" — useful for
            # detecting that a media block is fully covered.
            selectors.add(normalize_selector(sel))
        elif rule['is_at']:
            # @keyframes, @font-face, @import, etc. — record by name.
            selectors.add(normalize_selector(sel))
        else:
            for s in split_selector_list(sel):
                selectors.add(normalize_selector(s))
    return selectors


# ---------------------------------------------------------------------------
# Stripping logic
# ---------------------------------------------------------------------------

def selector_should_be_stripped(selector, common_selectors):
    """
    Decide if a rule's selector(s) are fully covered by common.css.

    Returns True only if EVERY comma-separated selector matches common.css
    AND no part is in PRESERVE_INLINE.
    """
    parts = split_selector_list(selector)
    for part in parts:
        norm = normalize_selector(part)
        if norm in PRESERVE_INLINE:
            return False
        # Also skip preserve-inline matches that include a parent (e.g.
        # `.hero-left h1 .word:nth-child(1)`).
        for preserve in PRESERVE_INLINE:
            if preserve in norm:
                return False
        if norm not in common_selectors:
            return False
    return True


def strip_inline_block(style_content, common_selectors, verbose=False):
    """
    Remove duplicate rules from a single <style> block.
    Returns (cleaned_content, removed_selectors_list).
    """
    rules = parse_css_rules(style_content)
    if not rules:
        return style_content, []

    keep_spans = []  # list of (start, end) to keep from original style_content
    removed = []
    last_end = 0

    for rule in rules:
        sel = rule['selector']
        if rule['is_at']:
            # For @keyframes, only strip if the keyframe name is in common.css.
            # For @media, recursively handle inner rules.
            if sel.startswith('@media') or sel.startswith('@supports'):
                inner_rules = parse_css_rules(rule['body'])
                inner_kept = []
                inner_removed = []
                for ir in inner_rules:
                    if not ir['is_at'] and selector_should_be_stripped(ir['selector'], common_selectors):
                        inner_removed.append(ir['selector'])
                    else:
                        inner_kept.append(ir['full_text'])

                if inner_kept:
                    # Rebuild this @media block with only the kept inner rules
                    # — but only if we actually removed something. Otherwise
                    # keep the original verbatim (preserves formatting).
                    if inner_removed:
                        rebuilt = f"{sel} {{\n{chr(10).join(inner_kept)}\n}}"
                        # Append from last_end up to rule.start, then rebuilt
                        keep_spans.append(('text', style_content[last_end:rule['start']]))
                        keep_spans.append(('text', rebuilt))
                        last_end = rule['end']
                        removed.extend(f"@media:: {r}" for r in inner_removed)
                    # else: leave as-is — the for-loop's last_end will sweep it up
                else:
                    # All inner rules removable — drop the @media block entirely
                    keep_spans.append(('text', style_content[last_end:rule['start']]))
                    last_end = rule['end']
                    removed.append(f"{sel} (entire block)")
                    removed.extend(f"@media:: {r}" for r in inner_removed)
                continue

            # @keyframes / @font-face: strip if in common.css
            if normalize_selector(sel) in common_selectors and sel not in PRESERVE_INLINE:
                keep_spans.append(('text', style_content[last_end:rule['start']]))
                last_end = rule['end']
                removed.append(sel)
            continue

        # Regular rule
        if selector_should_be_stripped(sel, common_selectors):
            keep_spans.append(('text', style_content[last_end:rule['start']]))
            last_end = rule['end']
            removed.append(sel)

    # Append the trailing tail
    keep_spans.append(('text', style_content[last_end:]))

    cleaned = ''.join(s for _, s in keep_spans)

    # Strip explicitly-named orphaned section-header comments
    for pattern in ORPHAN_COMMENT_PATTERNS:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)

    # Strip ANY divider comment that's now dangling — `/* ---- ... ---- */`
    # or `/* ---- ... */` patterns that follow removed rules. Detect by
    # checking that the comment is immediately followed by whitespace then
    # another comment, the closing </style> region, or another divider —
    # i.e. it has no rule directly attached anymore.
    def comment_is_orphaned(text, m_start, m_end):
        # Look ahead from m_end. If the next non-whitespace is another
        # comment or the end of the string, this comment is orphaned.
        j = m_end
        while j < len(text) and text[j].isspace():
            j += 1
        if j >= len(text):
            return True
        if text[j:j+2] == '/*':
            return True
        return False

    divider_pattern = re.compile(r'/\*\s*-{2,}[^*]*-{2,}\s*\*/', re.DOTALL)
    while True:
        m = divider_pattern.search(cleaned)
        removed_any = False
        cursor = 0
        out = []
        for m in divider_pattern.finditer(cleaned):
            if comment_is_orphaned(cleaned, m.start(), m.end()):
                out.append(cleaned[cursor:m.start()])
                cursor = m.end()
                removed_any = True
        out.append(cleaned[cursor:])
        cleaned = ''.join(out)
        if not removed_any:
            break

    # Strip lines that are pure whitespace, then collapse blank-line runs.
    lines = cleaned.split('\n')
    lines = [('' if not line.strip() else line) for line in lines]
    cleaned = '\n'.join(lines)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

    # If the resulting block is just whitespace, leave a single newline
    if cleaned.strip() == '':
        cleaned = '\n'

    if verbose and removed:
        for r in removed:
            print(f"      − {r}")

    return cleaned, removed


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(filepath, common_selectors, dry_run=False, verbose=False):
    """
    Strip duplicate CSS from one HTML file.
    Returns (changed_bool, original_chars, new_chars, total_removed_count).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    style_pattern = re.compile(r'(<style>)(.*?)(</style>)', re.DOTALL)
    matches = list(style_pattern.finditer(content))
    if not matches:
        return False, 0, 0, 0

    new_content_parts = []
    cursor = 0
    total_orig = 0
    total_new = 0
    total_removed = 0

    for match in matches:
        new_content_parts.append(content[cursor:match.start(2)])
        original_style = match.group(2)
        cleaned_style, removed = strip_inline_block(
            original_style, common_selectors, verbose=verbose
        )
        new_content_parts.append(cleaned_style)
        cursor = match.end(2)
        total_orig += len(original_style)
        total_new += len(cleaned_style)
        total_removed += len(removed)

    new_content_parts.append(content[cursor:])
    new_content = ''.join(new_content_parts)

    if new_content == content:
        return False, total_orig, total_new, 0

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True, total_orig, total_new, total_removed


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def find_html_files():
    out = []
    for root, dirs, files in os.walk(PROJECT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for f in files:
            if f.endswith('.html') and f != 'google8739391a40d00bda.html':
                out.append(os.path.join(root, f))
    out.sort()
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true',
                        help='Report what would be removed; do not write.')
    parser.add_argument('--file', type=str, default=None,
                        help='Target a single .html file (path relative to repo or absolute).')
    parser.add_argument('--verbose', action='store_true',
                        help='Print every removed selector.')
    args = parser.parse_args()

    common_selectors = load_common_selectors()
    print(f"Loaded {len(common_selectors)} top-level selectors from css/common.css")

    if args.file:
        path = args.file
        if not os.path.isabs(path):
            path = os.path.join(PROJECT, path)
        if not os.path.exists(path):
            sys.exit(f"FATAL: {path} does not exist")
        files = [path]
    else:
        files = find_html_files()

    print(f"Mode: {'DRY-RUN (no writes)' if args.dry_run else 'WRITE'}")
    print(f"Files: {len(files)}")
    print("=" * 60)

    total_modified = 0
    total_orig = 0
    total_new = 0
    total_removed = 0

    for filepath in files:
        rel = os.path.relpath(filepath, PROJECT)
        changed, orig, new, removed = process_file(
            filepath, common_selectors,
            dry_run=args.dry_run, verbose=args.verbose,
        )
        if changed:
            total_modified += 1
            total_orig += orig
            total_new += new
            total_removed += removed
            saved = orig - new
            pct = (saved * 100 // orig) if orig > 0 else 0
            mark = '~' if args.dry_run else '✓'
            print(f"  {mark} {rel}  −{saved:,} chars ({pct}% smaller)  −{removed} rule(s)")
        elif args.verbose:
            print(f"  · {rel}  (no changes)")

    print("=" * 60)
    word = 'WOULD modify' if args.dry_run else 'Modified'
    print(f"{word}: {total_modified} file(s)")
    if total_orig:
        saved = total_orig - total_new
        pct = saved * 100 // total_orig if total_orig else 0
        print(f"Total CSS removed: {saved:,} chars ({pct}% reduction across affected files)")
        print(f"Total rules removed: {total_removed}")
    if args.dry_run:
        print("\n(dry-run: no files were written; rerun without --dry-run to apply)")


if __name__ == '__main__':
    main()
