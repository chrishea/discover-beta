# Discover Cloudcroft Color Palette Memo

**Date:** January 28, 2026
**Subject:** Website Color Theme Analysis

---

## Executive Summary

The Discover Cloudcroft website uses a carefully crafted color system designed to evoke the natural beauty of New Mexico's mountain retreat. The palette draws inspiration from the landscape: golden sunsets, pine forests, red earth, and mountain shadows.

---

## Primary Color Palettes

### 1. Gold/Earth Palette (Main Theme)

This is the dominant palette used across most pages:

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Pine Deep | `#d4a900` | Headings, primary accent |
| Pine Medium | `#e6bc00` | Secondary gold elements |
| Pine Light | `#fcd116` | Logo tagline, highlights, badges |
| Sunset Gold | `#8B0000` | CTA buttons, important actions |
| Sunset Warm | `#a31621` | Button hover states |
| Bark Brown | `#8B4513` | Tertiary accents |
| Text Dark | `#3d3200` | Primary body text |
| Text Light | `#6b5c3d` | Secondary/muted text |

**Rationale:** Gold tones reflect the warmth of mountain sunsets and New Mexico's famous golden light. The dark red provides strong contrast for calls-to-action while maintaining the southwestern aesthetic.

### 2. Forest Green Palette (Info Pages)

Used on About, Contact, and similar informational pages:

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| Pine Deep | `#1e5a3a` | Headings, primary accent |
| Pine Medium | `#2d7a4a` | Buttons, interactive elements |
| Pine Light | `#4a9a6a` | Highlights |
| Mountain Shadow | `#1a4a2e` | Dark backgrounds, footer |
| Sunset Gold | `#d4a84b` | Accent highlights |

**Rationale:** The green palette represents the pine forests surrounding Cloudcroft (elevation 8,676 ft). It's used for pages focused on community and information rather than tourism promotion.

---

## Structural Color Assignments

### Header/Navigation
- **Background:** `#2d4a3e` (dark teal-green)
- **Logo text:** `#ffffff` (white)
- **Tagline:** `#fcd116` (bright gold)
- **CTA Button:** `#8B0000` (dark red)

**Rationale:** The dark teal provides a stable, professional anchor while allowing the gold and white elements to stand out prominently.

### Hero Sections
- **Primary overlay:** Gradient from `rgba(0,0,0,0.3)` to `rgba(139,0,0,0.6)`
- **Text:** `#ffffff` with gold subtitle accents

**Rationale:** Semi-transparent overlays ensure text readability over photography while adding warmth.

### Body Content
- **Odd sections:** `#fffef5` (warm cream)
- **Even sections:** `#fffdf8` (off-white)
- **Cards:** `#ffffff` (pure white)

**Rationale:** Alternating subtle background tones create visual separation without harsh contrast.

### Footer
- **Main pages:** `#6b0000` (dark maroon)
- **Green theme pages:** `#1a332b` (very dark green)
- **Restaurant pages:** `#3D2314` (dark brown)
- **Column headers:** `#fcd116` (gold)

---

## Activity-Specific Accent Colors

Certain activity pages use sport-appropriate colors while maintaining brand consistency:

| Activity | Primary Color | Hex Code |
|----------|--------------|----------|
| Golf | Sports Green | `#1B5E20` / `#2E7D32` |
| Disc Golf | Orange | `#E65100` / `#FF9800` |
| Pickleball | Sports Blue | `#1565C0` / `#42A5F5` |

---

## Button System

### Primary Buttons
- **Default:** `#8B0000` background, white text
- **Hover:** `#a31621` with shadow `rgba(139,0,0,0.4)`

### Secondary Buttons
- **Default:** `rgba(255,255,255,0.15)` with white border
- **Hover:** `rgba(255,255,255,0.25)`

---

## Key Gradient Combinations

1. **Gold Gradient:** `linear-gradient(135deg, #fcd116, #e6bc00)` — CTAs, newsletters
2. **Forest Gradient:** `linear-gradient(135deg, #1a4a2e, #1e5a3a, #2d7a4a)` — Green theme heroes
3. **Sunset Overlay:** `linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(139,0,0,0.6))` — Hero images

---

## Design Philosophy

The color system embodies three core principles:

1. **Authenticity:** Colors drawn from the actual Cloudcroft landscape — golden sunlight, red earth, green pines, mountain shadows

2. **Warmth:** The predominant gold/brown palette creates an inviting, welcoming atmosphere appropriate for a tourism destination

3. **Contrast for Action:** Dark reds (`#8B0000`) are reserved exclusively for calls-to-action, creating clear visual hierarchy and guiding user behavior

---

## Accessibility Notes

- Text colors maintain WCAG AA contrast ratios against their backgrounds
- The dark brown text (`#3d3200`) on cream backgrounds provides good readability
- Gold accent text (`#fcd116`) is used sparingly and primarily on dark backgrounds where contrast is sufficient

---

## Recommendations for Future Development

1. **Consistency:** When creating new pages, use the Gold/Earth palette for tourism/promotional content and the Forest Green palette for informational/community content

2. **CTA Placement:** Reserve `#8B0000` exclusively for primary actions to maintain its visual impact

3. **Photography:** Hero images should have warm tones that complement the overlay gradients

---

*This memo documents the current color implementation as of January 2026.*
