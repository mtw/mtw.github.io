#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import json
import re

import minify_html
import rcssmin
import rjsmin




def minify_css_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.css"):
        path.write_text(rcssmin.cssmin(path.read_text(encoding="utf-8")), encoding="utf-8")


def minify_js_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.js"):
        path.write_text(rjsmin.jsmin(path.read_text(encoding="utf-8")), encoding="utf-8")


LDJSON = re.compile(r'(<script type="?application/ld\+json"?>)(.*?)(</script>)', re.S)


def compact_ldjson(html: str) -> str:
    """Rewrite each JSON-LD block as compact JSON; the HTML minifier leaves them alone."""
    def repl(m):
        try:
            data = json.loads(m.group(2))
        except json.JSONDecodeError:
            return m.group(0)
        return m.group(1) + json.dumps(data, separators=(",", ":"), ensure_ascii=False) + m.group(3)
    return LDJSON.sub(repl, html)


IMG_TAG = re.compile(r"<img\b[^>]*>", re.I)
ATTR = re.compile(r"""([a-zA-Z-]+)=(?:"([^"]*)"|'([^']*)'|([^\s>]+))""")
SITE_PREFIX = "https://michaelwolfinger.com/"


def _local_image(output_dir: Path, src: str) -> Path | None:
    if src.startswith(SITE_PREFIX):
        src = src[len(SITE_PREFIX):]
    elif src.startswith("/"):
        src = src[1:]
    elif "://" in src or src.startswith("//"):
        return None
    path = output_dir / src.split("?", 1)[0]
    return path if path.is_file() else None


def annotate_images(html: str, output_dir: Path) -> str:
    """Add width/height (no layout shift) and lazy loading to local images.

    The first image of a page is the likeliest above-the-fold candidate and stays eager.
    """
    from PIL import Image

    seen = 0

    def repl(m):
        nonlocal seen
        tag = m.group(0)
        attrs = {k.lower(): (a or b or c) for k, a, b, c in ATTR.findall(tag)}
        seen += 1
        extra = []
        path = _local_image(output_dir, attrs.get("src", ""))
        if path and "width" not in attrs and "height" not in attrs:
            try:
                with Image.open(path) as im:
                    extra.append(f'width="{im.width}" height="{im.height}"')
            except OSError:
                pass
        if seen > 1 and "loading" not in attrs:
            extra.append('loading="lazy" decoding="async"')
        if not extra:
            return tag
        end = "/>" if tag.endswith("/>") else ">"
        return tag[: -len(end)].rstrip() + " " + " ".join(extra) + " " + end


    return IMG_TAG.sub(repl, html)


def minify_html_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.html"):
        path.write_text(
            minify_html.minify(
                annotate_images(compact_ldjson(path.read_text(encoding="utf-8")), output_dir),
                minify_doctype=False,
                minify_css=True,
                minify_js=True,
            ),
            encoding="utf-8",
        )


def optimize_publish(output_dir: Path) -> None:
    minify_css_files(output_dir)
    minify_js_files(output_dir)
    minify_html_files(output_dir)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Minify CSS/JS/HTML in a Pelican output directory."
    )
    parser.add_argument("output_dir", type=Path, help="Pelican output directory")
    args = parser.parse_args()

    optimize_publish(args.output_dir.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
