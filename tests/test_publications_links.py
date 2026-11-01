import re
from pathlib import Path

import pytest

from tests.site_test_utils import author_key, fold_letters, publication_entries, split_authors


REPO_ROOT = Path(__file__).resolve().parents[1]
PELICAN_DIR = REPO_ROOT
PUBLICATIONS_RST = PELICAN_DIR / "content" / "publications.rst"
BLOG_DIR = PELICAN_DIR / "content" / "blog"


def test_publications_blog_links_reference_existing_posts():
    text = PUBLICATIONS_RST.read_text()

    blog_refs = re.findall(r"<\{filename\}(/?blog/[^>]+\.rst)>", text)
    assert blog_refs, "No blog post references found in publications.rst"

    malformed_refs = [ref for ref in blog_refs if not ref.startswith("/blog/")]
    assert not malformed_refs, f"Malformed blog refs in publications.rst: {malformed_refs}"

    missing_posts = []
    for ref in blog_refs:
        rel_path = ref.removeprefix("/blog/")
        post_path = BLOG_DIR / rel_path
        if not post_path.is_file():
            missing_posts.append((ref, str(post_path)))

    assert not missing_posts, f"Missing blog posts referenced from publications.rst: {missing_posts}"


FIELD_RE = re.compile(r"^:(?P<key>[a-z_]+):\s*(?P<value>.+?)\s*$", re.MULTILINE)


def _post_fields(path: Path) -> dict:
    fields = {}
    for match in FIELD_RE.finditer(path.read_text(encoding="utf-8")):
        fields.setdefault(match.group("key"), match.group("value"))
    return fields


def test_publication_numbers_run_without_gaps():
    numbers = [entry["number"] for entry in publication_entries()]
    assert numbers == sorted(numbers, reverse=True), "the list is not in descending order"
    assert set(numbers) == set(range(1, max(numbers) + 1)), "a number is missing or used twice"


@pytest.mark.parametrize("entry", [e for e in publication_entries() if e["post"]],
                         ids=lambda e: str(e["number"]))
def test_publication_entry_matches_the_post_it_links_to(entry):
    """The landing page repeats what the post's metadata says, and the metadata is what
    `CHECK_CROSSREF=1` compares with the Crossref record. Where the two disagree, the
    error is on this page: title, journal, year, DOI and the authors have to match."""
    assert entry["post"].is_file(), f"{entry['post']} does not exist"
    fields = _post_fields(entry["post"])
    number = entry["number"]
    assert fields.get("doi") == entry["doi"], f"#{number}: DOI differs from the post"
    assert fold_letters(fields.get("paper_title", "")) == fold_letters(entry["title"]), \
        f"#{number}: title {entry['title']!r} is not the :paper_title: of the post"
    assert fold_letters(fields.get("journal", "")) == fold_letters(entry["journal"]), \
        f"#{number}: journal {entry['journal']!r} is not the :journal: of the post"
    assert fields.get("year") == entry["year"], f"#{number}: year differs from the post"
    listed = [author_key(a) for a in split_authors(entry["authors"])]
    cited = [author_key(a) for a in split_authors(fields.get("paper_authors", ""))]
    assert listed == cited, f"#{number}: author list differs from the post"
