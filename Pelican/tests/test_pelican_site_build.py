from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tests.site_test_utils import build_site


def test_site_build_smoke(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")

    assert (output_dir / "index.html").is_file()
    assert (output_dir / "sitemap.xml").is_file()
    assert (output_dir / "robots.txt").is_file()
    assert (output_dir / "static").is_dir()
    assert (output_dir / "blog").is_dir()
