"""Redirect pages for URLs that once existed.

REDIRECTS in pelicanconf.py maps an old site-relative path to a target URL. After the site
is written, a small no-index HTML page with a meta refresh and a canonical link is placed
at each old path, so bookmarks and search results keep working without any server-side
configuration (GitHub Pages cannot redirect). Old paths ending in '/' get an index.html.
"""
import html
import pathlib

from pelican import signals

MARKER = "<!-- mtw-redirects -->"
PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  """ + MARKER + """
  <meta charset="UTF-8" />
  <title>Michael T. Wolfinger</title>
  <meta name="robots" content="noindex, follow" />
  <meta http-equiv="refresh" content="0; url={target}" />
  <link rel="canonical" href="{target}" />
</head>
<body>
  <p>This page has moved. Continue to <a href="{target}">{target}</a>.</p>
</body>
</html>
"""


def write_redirects(pelican):
    siteurl = pelican.settings.get("SITEURL", "")
    for old, target in pelican.settings.get("REDIRECTS", {}).items():
        if target.startswith("/"):
            target = siteurl + target
        path = pathlib.Path(pelican.output_path) / old.lstrip("/")
        if old.endswith("/") or not path.suffix:
            path = path / "index.html"
        # Never overwrite a real page. A stub from a previous run (the dev server keeps the
        # output directory between rebuilds) is recognised by its marker, or, for stubs
        # written before the marker existed, by being a small meta-refresh page.
        if path.exists():
            existing = path.read_text(encoding="utf-8", errors="ignore")
            is_stub = MARKER in existing or ("http-equiv" in existing and "refresh" in existing and len(existing) < 2000)
            if not is_stub:
                raise RuntimeError(f"redirect {old} would overwrite an existing page")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(PAGE.format(target=html.escape(target, quote=True)), encoding="utf-8")


def register():
    signals.finalized.connect(write_redirects)
