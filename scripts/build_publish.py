#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build the Pelican publish site and optimize deploy assets."
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory relative to Pelican/ or an absolute path",
    )
    parser.add_argument(
        "--settings",
        default="publishconf.py",
        help="Pelican settings file relative to Pelican/",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    pelican_dir = repo_root / "Pelican"
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = pelican_dir / output_dir

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pelican",
            "content",
            "-o",
            str(output_dir),
            "-s",
            args.settings,
        ],
        cwd=pelican_dir,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts" / "optimize_publish.py"),
            str(output_dir),
            "--source-static-dir",
            str(pelican_dir / "pelican-theme" / "static"),
        ],
        cwd=repo_root,
        check=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
