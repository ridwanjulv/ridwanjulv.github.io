# ridwanjulv.dev

Personal blog of Ridwan Julvianto — writing about JavaScript, DevOps, career growth, and short TIL notes.

Built with [Eleventy (11ty) v3](https://www.11ty.dev/), a zero-JavaScript static site generator. No framework, no CMS, no client-side JS. Just HTML, CSS, and Markdown.

> **AI disclosure:** This site's design, layout, and scaffolding were built with the assistance of Claude (Anthropic). The written content reflects my own experience and opinions. If AI involvement bothers you, that's fair — I wanted to be upfront about it.

---

## Local development

**Prerequisites:** Node.js 18+

```bash
npm install
npm start        # dev server at http://localhost:8080 with live reload
npm run build    # production build → _site/
```

---

## How to update the site

### Write a new post

Create a Markdown file in `content/blog/`:

```bash
content/blog/my-post-title.md
```

Minimum front matter:

```yaml
---
title: Your Post Title
description: One-sentence summary shown in cards and feeds.
date: 2025-01-15
tags:
  - javascript   # javascript | devops | career | til
---

Your content here...
```

Optional front matter:

```yaml
draft: true          # excluded from production builds, visible in --serve
updated: 2025-03-01  # shows "Updated" date in post header
```

### Edit the about page

Edit `content/about.md`. The page uses raw HTML internally for the skills grid and experience list — update those sections directly.

### Change site metadata

Edit `_data/metadata.js` — site title, URL, description, and author info.

### Add or rename a tag

Tags are free-form. Add any tag to a post's front matter and a tag page is generated automatically. The four main content pillars are `javascript`, `devops`, `career`, and `til`, but you can add others freely.

### Update the sidebar or footer

Edit `_includes/layouts/base.njk`. The sidebar nav groups (Writing / Info / Theme) and the footer content are both in this file.

### Edit styles

All styles live in `css/index.css`. The file uses CSS custom properties (`--color-*`, `--font-*`) at the top of `:root` — tweak those first before changing individual rules.

Dark/light/auto theme toggle is CSS-only via `body:has(#theme-dark:checked)` — no JavaScript involved.

---

## Project structure

```
content/
  blog/          ← blog posts (Markdown)
  about.md       ← about page
  index.njk      ← home page
  blog.njk       ← blog archive (paginated)
  tag-pages.njk  ← auto-generated tag pages
_includes/
  layouts/
    base.njk     ← HTML shell, sidebar, footer
    post.njk     ← blog post layout (TOC, prev/next nav)
    home.njk     ← thin wrapper for non-post pages
  postslist.njk  ← reusable post list partial
_data/
  metadata.js    ← site-wide metadata
_config/
  filters.js     ← custom Eleventy filters (readableDate, readingTime, toc, …)
css/
  index.css      ← all styles (inlined at build time, no external CSS requests)
.github/
  workflows/
    gh-pages.yml ← GitHub Actions deploy to GitHub Pages
```

---

## Deployment

The site deploys automatically to GitHub Pages on every push to `main` via `.github/workflows/gh-pages.yml`.

To deploy manually:

```bash
npm run build
# then push _site/ contents to your gh-pages branch, or let the Action handle it
```

---

## Tech stack

| Thing | What |
|---|---|
| Generator | [Eleventy v3](https://www.11ty.dev/) |
| Templating | Nunjucks (`.njk`) + Markdown |
| Syntax highlighting | [Prism.js](https://prismjs.com/) via `@11ty/eleventy-plugin-syntaxhighlight` (zero JS) |
| Styles | Plain CSS, custom properties, no framework |
| Fonts | Georgia / Lora (serif body), system monospace for code |
| Client JS | None |
| Deployment | GitHub Actions → GitHub Pages |
