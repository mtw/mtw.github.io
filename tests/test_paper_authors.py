"""Author lists and titles of the publication posts against the Crossref record of their DOI.

Opt-in like the external-link check: ``CHECK_CROSSREF=1 make test``. Authors are compared
by surname in order plus the first initial; middle initials and diacritics are ignored, so
"Ivo Hofacker" matches "Ivo L. Hofacker" but a misspelled or missing author fails. The
:paper_title: is compared letter by letter, ignoring case, punctuation and markup, so only
a different wording fails.
"""
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path

import pytest

from tests.site_test_utils import publication_entries

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


@lru_cache(maxsize=None)
def _crossref(doi):
    """The Crossref record of a DOI; a rate-limited answer is retried, not reported."""
    request = urllib.request.Request(CROSSREF + doi, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)["message"]
        except urllib.error.HTTPError as error:
            if error.code in (429, 503) and attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            raise


def _crossref_authors(doi):
    record = _crossref(doi)
    return [f"{a.get('given', '')} {a.get('family', '')}".strip() for a in record.get("author", [])]


def _letters(title):
    """Letters and digits of a title, nothing else.

    Publishers set the same title differently (RNA-Seq or RNASeq, 3'UTR or 3\u2032UTR,
    No Known Vector or No-Known-Vector, markup for species names), so word boundaries
    and punctuation are dropped and only the letters are compared.
    """
    title = re.sub(r"<[^>]+>", " ", title)
    title = unicodedata.normalize("NFKD", title)
    title = "".join(c for c in title if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def _list_only_entries():
    """Papers listed on the publications page that have no post of their own."""
    for entry in publication_entries():
        if entry["post"] is None and entry["doi"]:
            yield (f"publications.rst #{entry['number']}", entry["doi"],
                   _split(entry["authors"]), entry["title"])


def _has_crossref_title(doi):
    # Zenodo is not on Crossref, and a preprint record carries the title of its latest
    # version, which need not be the one the site cites
    return not doi.startswith(("10.5281/", "10.64898/", "10.1101/"))


def _titles():
    """(file name, DOI, :paper_title:) for the posts whose DOI Crossref knows."""
    for path in sorted(BLOG_DIR.glob("*.rst")):
        text = path.read_text(encoding="utf-8")
        doi = re.search(r"^:doi:\s*(\S+)$", text, re.M)
        title = re.search(r"^:paper_title:\s*(.+)$", text, re.M)
        if doi and title and _has_crossref_title(doi.group(1)):
            yield path.name, doi.group(1), title.group(1).strip()


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
    posts = list(_posts()) + [(name, doi, authors) for name, doi, authors, _ in _list_only_entries()]
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

    with ThreadPoolExecutor(4) as pool:
        problems = [p for p in pool.map(check, posts) if p]
    assert not problems, "\n".join(str(p) for p in problems)


def test_paper_titles_match_crossref():
    posts = list(_titles()) + [(name, doi, title) for name, doi, _, title in _list_only_entries()
                               if _has_crossref_title(doi)]
    assert len(posts) > 40, "the :paper_title: fields were not recognised"

    def check(item):
        name, doi, title = item
        try:
            record = _crossref(doi)
        except urllib.error.HTTPError as e:
            return (name, doi, f"Crossref answered {e.code}")
        except (urllib.error.URLError, OSError) as e:
            pytest.skip(f"Crossref not reachable: {e}")
        cited = record.get("title") or []
        if not cited:
            return (name, doi, "Crossref record has no title")
        if _letters(title) != _letters(cited[0]):
            return (name, doi, f"site: {title!r}", f"Crossref: {cited[0]!r}")
        return None

    with ThreadPoolExecutor(4) as pool:
        problems = [p for p in pool.map(check, posts) if p]
    assert not problems, "\n".join(str(p) for p in problems)


CC_RE = re.compile(r"creativecommons\.org/licenses/(by[a-z-]*)/(\d\.\d)")


def _cc_labels(record):
    """The Creative Commons licences Crossref lists for a work, as "CC BY 4.0" labels."""
    labels = set()
    for entry in record.get("license", []) or []:
        match = CC_RE.search(entry.get("URL", ""))
        if match:
            labels.add(f"CC {match.group(1).upper()} {match.group(2)}")
    return labels


def _licensed_posts():
    for path in sorted(BLOG_DIR.glob("*.rst")):
        text = path.read_text(encoding="utf-8")
        doi = re.search(r"^:doi:\s*(\S+)$", text, re.M)
        label = re.search(r"^:paper_license:\s*(.+?)\s*$", text, re.M)
        if doi and label and not doi.group(1).startswith(("10.5281/", "10.64898/")):
            yield path.name, doi.group(1), label.group(1)


def test_paper_licenses_match_crossref():
    """The quoted abstract names the licence of the paper, so the claim has to be the one
    the publisher registered. A paper without a licence in Crossref carries no claim."""
    posts = list(_licensed_posts())
    assert len(posts) > 30, "the :paper_license: fields were not recognised"

    def check(item):
        name, doi, label = item
        try:
            record = _crossref(doi)
        except urllib.error.HTTPError as e:
            return (name, doi, f"Crossref answered {e.code}")
        except (urllib.error.URLError, OSError) as e:
            pytest.skip(f"Crossref not reachable: {e}")
        registered = _cc_labels(record)
        if label not in registered:
            return (name, doi, f"site: {label}", f"Crossref: {sorted(registered) or 'none'}")
        return None

    with ThreadPoolExecutor(4) as pool:
        problems = [p for p in pool.map(check, posts) if p]
    assert not problems, "\n".join(str(p) for p in problems)
