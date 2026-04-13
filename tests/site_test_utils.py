from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
PELICAN_DIR = REPO_ROOT / "Pelican"


def build_site(tmp_path: Path, settings_file: str) -> Path:
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
            settings_file,
        ],
        cwd=PELICAN_DIR,
        check=True,
    )
    return output_dir
