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


def minify_html_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.html"):
        path.write_text(
            minify_html.minify(
                compact_ldjson(path.read_text(encoding="utf-8")),
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
