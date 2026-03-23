#!/usr/bin/env python3
"""Remove duplicate inline CSS from HTML files that link common.css."""
import re
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

# Selectors that are in common.css and should be removed from inline styles
# These are regex patterns that match the selector part of a CSS rule
COMMON_SELECTORS = [
    # Reset & custom properties
    r'\*\s*,\s*\*::before\s*,\s*\*::after',
    r'\*::before\s*,\s*\*::after',  # continuation lines
    r':root',
    r'html',
    r'::selection',
    r'body',
    r'a\s*\{',  # bare a tag
    r'a:focus-visible\s*,\s*button:focus-visible',
    r'\*:focus-visible',
    r'ul\s*\{',
    r'img\s*\{',
    # Skip to content
    r'\.skip-to-content',
    r'\.skip-to-content:focus',
    # Header
    r'\.site-header(?!\.)',
    r'\.site-header\.scrolled',
    r'\.header-inner',
    r'\.logo\s*\{',  # but not .logo-beta etc
    r'\.header-logo(?!\s+\.)',  # .header-logo but not .header-logo .logo-discover
    r'\.header-logo\s+span',
    r'\.header-logo\s+\.logo-discover',
    r'\.header-logo\s+\.logo-cloudcroft',
    r'\.logo-discover',
    r'\.logo-cloudcroft',
    r'\.logo\s+span',
    r'\.logo-beta',
    # Nav
    r'\.main-nav(?!\s+a)',
    r'\.main-nav\s+a(?!\.)',
    r'\.main-nav\s+a:hover',
    r'\.main-nav\s+a:focus',
    r'\.main-nav\s+a\.active',
    r'\.header-nav(?!\s+a)',
    r'\.header-nav\s+a(?!\.)',
    r'\.header-nav\s+a::after',
    r'\.header-nav\s+a:hover',
    r'\.header-nav\s+a:hover::after',
    r'\.header-nav\s+a\.active',
    # Phone
    r'\.phone-link',
    r'\.nav-phone',
    r'\.header-phone',
    # Hamburger
    r'\.hamburger(?!\.)',
    r'\.hamburger\s+span',
    r'\.hamburger\.(active|open)\s+span',
    # Mobile
    r'\.mobile-menu(?!\.)',
    r'\.mobile-menu\.open',
    r'\.mobile-menu\s+a(?!\.)',
    r'\.mobile-menu\s+a:hover',
    r'\.mobile-menu\s+a:focus',
    r'\.mobile-menu\s+a\.active',
    r'\.mobile-overlay(?!\.)',
    r'\.mobile-overlay\.open',
    r'\.mobile-overlay\s+a(?!\.)',
    r'\.mobile-overlay\s+a:hover',
    r'\.mobile-nav-overlay',
    r'\.mobile-nav-backdrop',
    # Hero base
    r'\.hero\s*\{',
    r'\.hero-bg\s*\{',
    r'\.hero-overlay\s*\{',
    r'\.hero-gradient-overlay',
    r'\.hero-content\s*\{',
    r'\.hero-content\s+h1(?!\s+\.)',
    r'\.hero-content\s+h1\s+span',
    r'\.hero-content\s+p',
    r'\.hero-title\s*\{',
    r'\.hero-headline',
    r'\.hero-subtitle\s*\{',
    # Buttons
    r'\.btn-primary\s*\{',
    r'\.btn-primary:hover',
    r'\.btn-outline',
    # Section utilities
    r'\.section\s*\{',
    r'\.section-container\s*\{',
    r'\.section-header\s*\{',
    r'\.section-header\s+h2',
    r'\.section-header\s+p',
    r'\.section-label',
    r'\.section-title\s*\{',
    r'\.section-title-centered',
    # Stat items
    r'\.stat-number',
    r'\.stat-label',
    # Footer
    r'\.site-footer\s*\{',
    r'\.footer-gradient-border',
    r'\.footer-inner',
    r'\.footer-grid\s*\{',
    r'\.footer-brand',
    r'\.footer-col',
    r'\.footer-social',
    r'\.footer-bottom',
    r'\.social-icons',
    # Back to top
    r'\.back-to-top(?!\.)',
    r'\.back-to-top\.visible',
    r'\.back-to-top:hover',
]

# Keyframe animations in common.css
COMMON_KEYFRAMES = [
    'pageLoad', 'pageIn', 'fadeInUp', 'fadeUp', 'kenBurns',
    'footerBorderMorph', 'footerGradient', 'gradientBorder',
    'gradientFlow', 'wordReveal',
]

def parse_css_rules(css_text):
    """Parse CSS text into individual rules with their selectors."""
    rules = []
    i = 0
    while i < len(css_text):
        # Skip whitespace
        while i < len(css_text) and css_text[i] in ' \t\n\r':
            i += 1
        if i >= len(css_text):
            break

        # Check for comments
        if css_text[i:i+2] == '/*':
            end = css_text.find('*/', i)
            if end == -1:
                break
            rules.append(('comment', css_text[i:end+2]))
            i = end + 2
            continue

        # Check for @keyframes
        if css_text[i] == '@' and 'keyframes' in css_text[i:i+20]:
            # Find the animation name
            match = re.match(r'@keyframes\s+(\S+)\s*\{', css_text[i:])
            if match:
                name = match.group(1)
                # Find matching closing brace (nested braces)
                brace_count = 0
                j = i + match.end() - 1  # position of opening brace
                brace_count = 1
                j += 1
                while j < len(css_text) and brace_count > 0:
                    if css_text[j] == '{':
                        brace_count += 1
                    elif css_text[j] == '}':
                        brace_count -= 1
                    j += 1
                rules.append(('keyframes', name, css_text[i:j]))
                i = j
                continue

        # Check for @media
        if css_text[i] == '@' and 'media' in css_text[i:i+10]:
            # Find the media query
            brace_start = css_text.find('{', i)
            if brace_start == -1:
                break
            media_query = css_text[i:brace_start].strip()
            # Find matching closing brace
            brace_count = 1
            j = brace_start + 1
            while j < len(css_text) and brace_count > 0:
                if css_text[j] == '{':
                    brace_count += 1
                elif css_text[j] == '}':
                    brace_count -= 1
                j += 1
            rules.append(('media', media_query, css_text[i:j]))
            i = j
            continue

        # Regular rule: selector { ... }
        brace_start = css_text.find('{', i)
        if brace_start == -1:
            break
        selector = css_text[i:brace_start].strip()
        # Find matching closing brace
        brace_count = 1
        j = brace_start + 1
        while j < len(css_text) and brace_count > 0:
            if css_text[j] == '{':
                brace_count += 1
            elif css_text[j] == '}':
                brace_count -= 1
            j += 1
        rules.append(('rule', selector, css_text[i:j]))
        i = j

    return rules

def is_common_selector(selector):
    """Check if a selector matches one in common.css."""
    selector = selector.strip()

    # Check each common selector pattern
    for pattern in COMMON_SELECTORS:
        if re.match(r'^' + pattern + r'$', selector):
            return True
        # Also check without the \{ at end if present in pattern
        clean_pattern = pattern.rstrip(r'\{').rstrip()
        if re.match(r'^' + clean_pattern + r'$', selector):
            return True

    # Multi-selector rules (comma-separated)
    parts = [p.strip() for p in selector.split(',')]
    if len(parts) > 1:
        all_common = all(is_common_selector(p) for p in parts)
        if all_common:
            return True

    return False

def is_common_keyframe(name):
    """Check if a keyframe animation is in common.css."""
    return name in COMMON_KEYFRAMES

def filter_media_query(media_text):
    """Filter a media query to remove common rules but keep page-specific ones."""
    # Extract the media condition and body
    match = re.match(r'(@media[^{]+)\{(.*)\}\s*$', media_text, re.DOTALL)
    if not match:
        return media_text

    condition = match.group(1).strip()
    body = match.group(2)

    # Parse rules inside the media query
    inner_rules = parse_css_rules(body)

    kept_rules = []
    for rule in inner_rules:
        if rule[0] == 'rule':
            selector = rule[1]
            if not is_common_selector(selector):
                kept_rules.append(rule[2])
        elif rule[0] == 'keyframes':
            if not is_common_keyframe(rule[1]):
                kept_rules.append(rule[2])
        elif rule[0] == 'comment':
            kept_rules.append(rule[1])
        else:
            kept_rules.append(rule[-1])

    if not kept_rules:
        return None

    return condition + ' {\n' + '\n'.join(kept_rules) + '\n}'

def process_file(filepath):
    """Process a single HTML file to remove duplicate CSS."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if it links common.css
    if 'common.css' not in content:
        return 0

    # Find the style block
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        return 0

    original_css = style_match.group(1)
    original_size = len(original_css.encode('utf-8'))

    # Parse the CSS
    rules = parse_css_rules(original_css)

    # Filter rules
    kept_parts = []
    for rule in rules:
        if rule[0] == 'comment':
            # Keep comments that precede page-specific rules
            kept_parts.append(rule[1])
        elif rule[0] == 'keyframes':
            name = rule[1]
            if not is_common_keyframe(name):
                kept_parts.append(rule[2])
        elif rule[0] == 'media':
            condition = rule[1]
            # prefers-reduced-motion is fully in common.css
            if 'prefers-reduced-motion' in condition:
                # Filter inner rules, keep only page-specific ones
                filtered = filter_media_query(rule[2])
                if filtered:
                    kept_parts.append(filtered)
            else:
                # For other media queries, filter out common selectors
                filtered = filter_media_query(rule[2])
                if filtered:
                    kept_parts.append(filtered)
        elif rule[0] == 'rule':
            selector = rule[1]
            if not is_common_selector(selector):
                kept_parts.append(rule[2])

    new_css = '\n' + '\n'.join(kept_parts) + '\n'
    new_size = len(new_css.encode('utf-8'))

    # Replace in content
    new_content = content[:style_match.start(1)] + new_css + content[style_match.end(1):]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    saved = original_size - new_size
    return saved

def main():
    html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]
    html_files.sort()

    total_saved = 0
    for filename in html_files:
        filepath = os.path.join(BASE, filename)
        saved = process_file(filepath)
        if saved > 0:
            print(f"{filename}: removed {saved:,} bytes ({saved/1024:.1f} KB)")
            total_saved += saved
        elif saved < 0:
            print(f"{filename}: WARNING - size increased by {-saved} bytes")
        else:
            print(f"{filename}: no changes")

    print(f"\nTotal saved: {total_saved:,} bytes ({total_saved/1024:.1f} KB)")

if __name__ == '__main__':
    main()
