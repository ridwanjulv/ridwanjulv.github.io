#!/usr/bin/env python3
"""
Convert markdown files from posts/new/ into blog post HTML pages
and prepend the new post entry to posts/posts.json.

Usage:
    python md_to_post.py

Requirements:
    pip install markdown
"""

import json
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Error: 'markdown' package required.")
    print("Run: pip install markdown")
    sys.exit(1)


ROOT       = Path(__file__).parent
POSTS_NEW  = ROOT / "posts" / "new"
POSTS_OUT  = ROOT / "posts"
POSTS_JSON = ROOT / "posts" / "posts.json"


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

POST_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Your Name</title>
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="stylesheet" href="../assets/css/post.css">
</head>
<body>

<nav>
  <a href="../index.html" class="nav-mark">Your Name</a>
  <ul class="nav-links">
    <li><a href="../about.html">About</a></li>
    <li><a href="../portofolio.html">Work</a></li>
    <li><a href="../about.html#experience">Experience</a></li>
    <li><a href="../blog.html">Blog</a></li>
    <li><a href="../contact.html">Contact</a></li>
  </ul>
</nav>

<div class="page-wrap">
  <article class="post">
    <header class="post-header">
      <div class="post-meta">
        <span class="post-tag">{tag}</span>
        <span class="post-date">{date}</span>
      </div>
      <h1 class="post-title">{title}</h1>
    </header>

    <div class="post-body">
{body}
    </div>

    <footer class="post-footer">
      <a href="../blog.html" class="post-back">&#8592; Back to Blog</a>
    </footer>
  </article>
</div>

<footer>
  <span>&#169; 2025 Your Name</span>
  <span>Built by hand &#8212; no frameworks</span>
</footer>

<script src="../assets/js/main.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Extract YAML-style frontmatter; return (fields dict, body string)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    fm = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm, text[match.end():]


def slugify(title):
    """Convert a title string to a URL-safe slug."""
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def indent_html(html, spaces=6):
    """Indent every non-empty line of an HTML block."""
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else "" for line in html.splitlines())


def prepend_to_json(entry):
    """Prepend a new post entry to posts/posts.json (newest first)."""
    if POSTS_JSON.exists():
        data = json.loads(POSTS_JSON.read_text(encoding="utf-8"))
    else:
        data = {"posts": []}

    # Avoid duplicates — remove existing entry with same slug before prepending
    data["posts"] = [p for p in data["posts"] if p.get("slug") != entry["slug"]]
    data["posts"].insert(0, entry)

    POSTS_JSON.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Core processor
# ---------------------------------------------------------------------------

def process(md_path):
    raw = md_path.read_text(encoding="utf-8")
    fm, body_md = parse_frontmatter(raw)

    title = fm.get("title", md_path.stem)
    tag   = fm.get("tag", "General")
    date  = fm.get("date", "")
    slug  = fm.get("slug", "") or slugify(title)

    # Convert markdown body to HTML
    md_processor = markdown.Markdown(extensions=["extra"])
    body_html = indent_html(md_processor.convert(body_md))

    # Write post HTML file
    post_html = POST_TEMPLATE.format(title=title, tag=tag, date=date, body=body_html)
    out_path = POSTS_OUT / f"{slug}.html"
    out_path.write_text(post_html, encoding="utf-8")
    print(f"  [OK] Created  posts/{slug}.html")

    # Prepend entry to posts.json
    prepend_to_json({"slug": slug, "title": title, "tag": tag, "date": date})
    print(f"  [OK] Updated  posts/posts.json  -- prepended \"{title}\"")

    # Archive processed markdown to done/
    done_dir = POSTS_NEW / "done"
    done_dir.mkdir(exist_ok=True)
    md_path.rename(done_dir / md_path.name)
    print(f"  [OK] Archived posts/new/{md_path.name} -> posts/new/done/")

    return slug


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    POSTS_NEW.mkdir(parents=True, exist_ok=True)

    md_files = sorted(POSTS_NEW.glob("*.md"))
    if not md_files:
        print("No .md files found in posts/new/ -- nothing to do.")
        print("Drop a markdown file there and re-run.")
        return

    print(f"Found {len(md_files)} file(s) in posts/new/\n")
    for md_path in md_files:
        print(f"Processing: {md_path.name}")
        process(md_path)
        print()

    print("All done.")


if __name__ == "__main__":
    main()
