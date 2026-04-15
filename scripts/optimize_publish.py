#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import minify_html
import rcssmin
import rjsmin


def compile_theme_css(source_static_dir: Path, output_dir: Path) -> None:
    source_css = source_static_dir / "m-light.css"
    compiled_css = output_dir / "static" / "m-light.compiled.css"
    compiled_css.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            sys.executable,
            str(source_static_dir / "postprocess.py"),
            source_css.name,
            "-o",
            str(compiled_css),
        ],
        cwd=source_static_dir,
        check=True,
    )


def minify_css_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.css"):
        path.write_text(rcssmin.cssmin(path.read_text(encoding="utf-8")), encoding="utf-8")


def minify_js_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.js"):
        path.write_text(rjsmin.jsmin(path.read_text(encoding="utf-8")), encoding="utf-8")


def minify_html_files(output_dir: Path) -> None:
    for path in output_dir.rglob("*.html"):
        path.write_text(
            minify_html.minify(
                path.read_text(encoding="utf-8"),
                minify_doctype=False,
                minify_css=True,
                minify_js=True,
            ),
            encoding="utf-8",
        )


def optimize_publish(output_dir: Path, source_static_dir: Path) -> None:
    compile_theme_css(source_static_dir, output_dir)
    minify_css_files(output_dir)
    minify_js_files(output_dir)
    minify_html_files(output_dir)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile and minify publish-only CSS/JS/HTML assets in a Pelican output directory."
    )
    parser.add_argument("output_dir", type=Path, help="Pelican output directory")
    parser.add_argument(
        "--source-static-dir",
        type=Path,
        default=Path("Pelican/pelican-theme/static"),
        help="Theme static source directory containing m-light.css and postprocess.py",
    )
    args = parser.parse_args()

    optimize_publish(args.output_dir.resolve(), args.source_static_dir.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
