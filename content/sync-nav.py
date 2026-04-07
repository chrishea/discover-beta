#!/usr/bin/env python3
"""Sync top nav across all HTML files using complete-guide-to-cloudcroft-new-mexico-2026.html as source."""
import os, re

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build_nav(prefix):
    p = prefix
    return f'''<header class="site-header" role="banner">
        <div class="header-inner">

            <nav class="header-nav" role="navigation" aria-label="Main navigation">
                <a href="{p}index.html" class="logo header-logo" aria-label="Discover Cloudcroft — home">
                    <span class="logo-discover">Discover</span>
                    <span class="logo-cloudcroft">Cloudcroft</span>
                    <span class="logo-beta">Beta</span>
                </a>
                <a href="{p}stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html">Stay</a>
                <a href="{p}eat/complete-guide-where-to-eat-in-cloudcroft-2026.html">Eat</a>
                <a href="{p}do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html">Activities</a>
                <a href="{p}do/complete-guide-to-activities.html">Explore</a>
                <a href="{p}do/where-to-hike-in-Cloudcroft-New-Mexico-2026.html">Trails</a>
                <a href="{p}do/what-events-are-happening-in-cloudcroft-2026.html">Events</a>
                <a href="{p}season/seasonal.html">Seasons</a>
                <a href="{p}plan.html">Plan</a>
                <a href="{p}contact.html">Contact</a>
            </nav>
            <button class="hamburger" aria-label="Open navigation menu" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <div class="mobile-nav-overlay" role="dialog" aria-label="Mobile navigation">
        <a href="{p}stay/complete-guide-to-lodging-in-cloudcroft-new-mexico-2026.html">Stay</a>
        <a href="{p}eat/complete-guide-where-to-eat-in-cloudcroft-2026.html">Eat</a>
        <a href="{p}do/complete-guide-to-activities-to-do-in-cloudcroft-2026.html">Activities</a>
        <a href="{p}do/complete-guide-to-activities.html">Explore</a>
        <a href="{p}do/where-to-hike-in-Cloudcroft-New-Mexico-2026.html">Trails</a>
        <a href="{p}do/what-events-are-happening-in-cloudcroft-2026.html">Events</a>
        <a href="{p}season/seasonal.html">Seasons</a>
        <a href="{p}plan.html">Plan</a>
        <a href="{p}contact.html">Contact</a>
    </div>'''

# Match header...</header> followed by optional whitespace and mobile-nav-overlay div
PATTERN = re.compile(
    r'<header class="site-header".*?</header>\s*(?:<div class="mobile-nav-overlay".*?</div>)?',
    re.DOTALL
)

count = 0
for root, dirs, files in os.walk(PROJECT):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
    for f in files:
        if not f.endswith('.html') or f == 'google8739391a40d00bda.html':
            continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, PROJECT)
        depth = rel.count(os.sep)
        prefix = '../' * depth
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
        new_nav = build_nav(prefix)
        new_content, n = PATTERN.subn(new_nav, content, count=1)
        if n and new_content != content:
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            count += 1
            print(f"  ✓ {rel}")
print(f"\nUpdated: {count} files")
