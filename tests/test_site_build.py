from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PELICAN_DIR = REPO_ROOT / "Pelican"


def test_site_build_smoke(tmp_path):
    output_dir = tmp_path / "output"

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pelican",
            "content",
            "-o",
            str(output_dir),
            "-s",
            "publishconf.py",
        ],
        cwd=PELICAN_DIR,
        check=True,
    )

    assert (output_dir / "index.html").is_file()
    assert (output_dir / "sitemap.xml").is_file()
    assert (output_dir / "robots.txt").is_file()
    assert (output_dir / "static").is_dir()
    assert (output_dir / "blog").is_dir()
