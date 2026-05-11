---
name: DiscoverCloudcroft
description: The tourism guide website (discovercloudcroft.com) that this repo (discover-beta) builds. Static hand-written HTML.
type: project
---

# DiscoverCloudcroft

## What
- Static, hand-written HTML tourism guide for Cloudcroft, NM.
- Domain: **discovercloudcroft.com**.
- Source: this repo, `discover-beta` (main branch).
- No build system, no framework, no package manager, no test suite, no linter. Every page is a self-contained `.html` file.

## Structure
- Root pages: `index.html`, `cloudcroft-review.html`, etc.
- Section directories: `stay/`, `eat/`, `do/`, `shop/`, `visit/`, `events/`, `season/`, `resources/`, `about/`, `shelf/`, `profile/`.
- Each section contains entity pages (one business per file) backed by Markdown sources in `*-md/` subfolders and photos in `*-photo/photo-<entity>/`.
- Shared assets: `css/common.css`, `css/fonts.css`, `js/common.js`, `media/`.

## Recent focus (as of 2026-05-11)
- **SEO work** — ranking tracker, review memo (2026-05-11), hub H1s, thin title fixes, ItemList JSON-LD. Recent merged PRs: #49, #50.
- **eighteen99 gallery** moved to first section + repopulated with real photos.
- **llms.txt / cloudcroftreader-llms-txt** — separate but parallel work on Reader.

## How to apply
- When Chris says "the site" without qualifier, it's almost certainly DiscoverCloudcroft.
- "I worked on X. Live now." → X is an entity page under one of the section directories.
- Coding conventions are documented at the top of `CLAUDE.md`. Don't introduce a framework or build step.
