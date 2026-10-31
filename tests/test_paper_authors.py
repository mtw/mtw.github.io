"""Author lists of the publication posts against the Crossref record of their DOI.

Opt-in like the external-link check: ``CHECK_CROSSREF=1 make test``. Compares the
surnames in order and the first initial of every author; middle initials and
diacritics are ignored, so "Ivo Hofacker" matches "Ivo L. Hofacker" but a misspelled
or missing author fails.
"""
import json
import os
import re
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

BLOG_DIR = Path(__file__).resolve().parents[1] / "content" / "blog"
CROSSREF = "https://api.crossref.org/works/"
USER_AGENT = "michaelwolfinger.com site tests (mailto:michael.wolfinger@univie.ac.at)"

pytestmark = pytest.mark.skipif(not os.environ.get("CHECK_CROSSREF"), reason="set CHECK_CROSSREF=1")


def _fold(text):
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z ]+", " ", text.replace("’", "").replace("'", "").lower()).split()


def _key(name):
    tokens = _fold(name)
    return (tokens[0][0], tokens[-1]) if tokens else ("", "")


def _split(authors):
    return [a.strip() for a in authors.replace(" and ", ", ").split(",") if a.strip()]


def _citation_doi(text, authors):
    """DOI from the line block that cites the paper itself: the block whose author
    line names every author of :paper_authors:."""
    surnames = {_key(a)[1] for a in authors}
    blocks = re.findall(r"(?:^[ \t]*\|.*\n)+", text, re.M)
    for block in blocks:
        if all(s in _fold(block) for s in surnames):
            match = re.search(r"doi:\s?(10\.\d{4,9}/[^\s<>`|\"']+)", block)
            if match:
                return match.group(1).rstrip(".,;)")
    return None


def _crossref_authors(doi):
    request = urllib.request.Request(CROSSREF + doi, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        record = json.load(response)["message"]
    return [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in record.get("author", [])]


def _posts():
    for path in sorted(BLOG_DIR.glob("*.rst")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^:paper_authors:\s*(.+)$", text, re.M)
        if not match:
            continue
        authors = _split(match.group(1))
        doi = _citation_doi(text, authors)
        if doi and not doi.startswith("10.5281/"):   # Zenodo records are not on Crossref
            yield path.name, doi, authors


def test_paper_authors_match_crossref():
    posts = list(_posts())
    assert len(posts) > 40, "the citation blocks were not recognised"

    def check(item):
        name, doi, authors = item
        try:
            record = _crossref_authors(doi)
        except urllib.error.HTTPError as e:
            return (name, doi, f"Crossref answered {e.code}")
        except (urllib.error.URLError, OSError) as e:
            pytest.skip(f"Crossref not reachable: {e}")
        if [_key(a) for a in authors] != [_key(a) for a in record]:
            return (name, doi, f"site: {authors}", f"Crossref: {record}")
        return None

    with ThreadPoolExecutor(6) as pool:
        problems = [p for p in pool.map(check, posts) if p]
    assert not problems, "\n".join(str(p) for p in problems)
