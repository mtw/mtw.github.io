from pathlib import Path
import re
import subprocess
import sys
import unicodedata


REPO_ROOT = Path(__file__).resolve().parents[1]
PELICAN_DIR = REPO_ROOT


def build_site(tmp_path: Path, settings_file: str) -> Path:
    output_dir = tmp_path / "output"
    if settings_file == "publishconf.py":
        subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "build_publish.py"),
                "--output-dir",
                str(output_dir),
                "--settings",
                settings_file,
            ],
            cwd=REPO_ROOT,
            check=True,
        )
    else:
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


def fold_letters(text: str) -> str:
    """Letters and digits of a string, nothing else.

    Titles and journal names are set differently in different places (RNA-Seq or
    RNASeq, 3'UTR or 3\u2032UTR, diacritics or not), so comparisons that are about the
    wording and not about the typography run through this.
    """
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def split_authors(value: str) -> list:
    """An author list written as "A, B and C" into its names."""
    return [name.strip() for name in value.replace(" and ", ", ").split(",") if name.strip()]


def author_key(name: str) -> tuple:
    """(first initial, surname), folded: "Ivo L. Hofacker" matches "Ivo Hofacker"."""
    folded = unicodedata.normalize("NFKD", name)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    tokens = re.sub(r"[^a-z ]+", " ", folded.replace("\u2019", "").replace("'", "").lower()).split()
    return (tokens[0][0], tokens[-1]) if tokens else ("", "")


ENTRY_RE = re.compile(r"^\s*\|\s*(?P<number>\d+)\.\s*:link-flat-strong:`(?P<title>.+?)\s*<(?P<target>[^>]+)>`")


def publication_entries() -> list:
    """The numbered entries of content/publications.rst, one dict each.

    An entry is a line block: the numbered title link, the author line, the journal line
    and the line with the DOI. Unnumbered blocks (manuscripts under review) are skipped.
    """
    content = REPO_ROOT / "content"
    lines = (content / "publications.rst").read_text(encoding="utf-8").splitlines()
    entries = []
    for index, line in enumerate(lines):
        match = ENTRY_RE.match(line)
        if not match:
            continue
        rest = []
        for follower in lines[index + 1:]:
            stripped = follower.strip()
            if not stripped.startswith("|"):
                break
            rest.append(stripped[1:].strip())
        journal_line = next((l for l in rest if re.search(r"\*.+?\*", l) and re.search(r"\(\d{4}\)", l)), "")
        doi_line = next((l for l in rest if "doi:" in l), "")
        journal = re.search(r"\*(.+?)\*", journal_line)
        year = re.findall(r"\((\d{4})\)", journal_line)
        doi = re.search(r"doi:\s*(10\.[^\s<>`]+)", doi_line)
        target = match.group("target")
        entries.append({
            "number": int(match.group("number")),
            "line": index + 1,
            "title": " ".join(match.group("title").split()),
            "target": target,
            "post": content / target.replace("{filename}/", "") if target.startswith("{filename}") else None,
            "authors": re.sub(r":ul:`([^`]+)`", r"\1", rest[0]) if rest and not rest[0].startswith("*") else "",
            "journal": journal.group(1) if journal else "",
            "year": year[-1] if year else "",
            "doi": doi.group(1) if doi else "",
        })
    return entries
