"""Guard the metadata invariants the theme and URL scheme rely on.

ARTICLE_URL is blog/{year}/{slug}/ and SLUGIFY_SOURCE is 'basename', so a post without an
explicit :slug: would get its file name (including the date prefix and the blog/ folder)
in its URL. Every post therefore has to carry the metadata the templates and the structured
data expect, and slugs must not collide on a case-insensitive filesystem.
"""
import re
from datetime import date
from pathlib import Path

import pytest

BLOG_DIR = Path(__file__).resolve().parents[1] / "content" / "blog"
REQUIRED = ("date", "slug", "category", "tags", "summary", "description")
SECTIONS = {"guides", "essays", "talks"}
FIELD_RE = re.compile(r"^:(?P<key>[a-z_]+):\s*(?P<value>.*?)\s*$", re.MULTILINE)


def _fields(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fields = {}
    for match in FIELD_RE.finditer(text):
        fields.setdefault(match.group("key"), match.group("value"))
    return fields


def _posts():
    return sorted(BLOG_DIR.glob("*.rst"))


def _date(value: str) -> date:
    return date.fromisoformat(value.strip()[:10])


def test_blog_directory_has_posts():
    assert len(_posts()) >= 64


@pytest.mark.parametrize("post", _posts(), ids=lambda p: p.name)
def test_post_has_required_metadata(post):
    fields = _fields(post)
    missing = [key for key in REQUIRED if not fields.get(key)]
    assert not missing, f"{post.name}: missing {missing}"
    if fields.get("section"):
        assert fields["section"] in SECTIONS, f"{post.name}: unknown :section: {fields['section']}"
    if fields.get("modified"):
        assert _date(fields["modified"]) >= _date(fields["date"]), f"{post.name}: modified before date"
    assert not re.search(r"^\d{4}-\d{2}-\d{2}-", fields["slug"]), f"{post.name}: slug carries a date prefix"


def test_slugs_are_unique_case_insensitively():
    seen = {}
    for post in _posts():
        fields = _fields(post)
        key = (_date(fields["date"]).year, fields["slug"].lower())
        assert key not in seen, f"{post.name} collides with {seen[key]} on {key}"
        seen[key] = post.name


def test_canonical_urls_on_paper_stubs_point_at_existing_posts():
    stubs = BLOG_DIR.parent / "publications" / "papers"
    slugs = {(_date(f["date"]).year, f["slug"]) for f in (_fields(p) for p in _posts())}
    for stub in sorted(stubs.glob("*.rst")):
        canonical = _fields(stub).get("canonical_url")
        if not canonical:
            continue
        match = re.search(r"/blog/(\d{4})/([^/]+)/?$", canonical)
        assert match, f"{stub.name}: unexpected canonical {canonical}"
        assert (int(match.group(1)), match.group(2)) in slugs, f"{stub.name}: canonical does not match a post: {canonical}"


STATUSES = {"published", "draft", "hidden", "skip"}


@pytest.mark.parametrize("source", sorted((BLOG_DIR.parent).rglob("*.rst")), ids=lambda p: p.name)
def test_status_values_are_known(source):
    status = _fields(source).get("status")
    assert status is None or status in STATUSES, f"{source.name}: unknown :status: {status!r}"


@pytest.mark.parametrize("post", [p for p in _posts() if _fields(p).get("doi")], ids=lambda p: p.name)
def test_doi_belongs_to_the_posts_own_citation(post):
    """The :doi: feeds the ScholarlyArticle node; it must be the paper's own DOI, i.e. appear in
    the block under the post's 'Citation' heading (not in a related-papers list)."""
    text = post.read_text(encoding="utf-8")
    doi = _fields(post)["doi"]
    # the block ends at the next section heading (a line underlined with = or -) or at the end
    match = re.search(r"^Citation\n=+\n(.*?)(?=\n[^\n]+\n[=-]{3,}\n|\Z)", text, re.M | re.S)
    assert match, f"{post.name}: no Citation section"
    assert doi in match.group(1), f"{post.name}: :doi: {doi} is not in the Citation block"


@pytest.mark.parametrize("post", [p for p in _posts() if _fields(p).get("doi")], ids=lambda p: p.name)
def test_paper_title_repeats_the_title_from_the_citation(post):
    """A post :title: is written for readers and for search and often differs from the title
    of the paper, so the paper's own title lives in :paper_title: and feeds the headline of
    the ScholarlyArticle node. It has to be the title in the post's own citation block."""
    text = post.read_text(encoding="utf-8")
    fields = _fields(post)
    doi = fields["doi"]
    assert fields.get("paper_title"), f"{post.name}: :doi: without :paper_title:"
    block = next((b for b in re.findall(r"(?:^[ \t]*\|.*\n)+", text, re.M) if doi in b), None)
    assert block, f"{post.name}: no citation block for {doi}"
    link = re.search(r":link-flat(?:-strong)?:`\s*(.+?)\s*<[^<>`]+>`", block.splitlines()[0], re.S)
    assert link, f"{post.name}: citation block does not start with the paper link"
    cited = " ".join(link.group(1).split())
    assert fields["paper_title"] == cited, (
        f"{post.name}: :paper_title: {fields['paper_title']!r} != cited {cited!r}")


ABSTRACT_RE = re.compile(r"^\.\. frame:: Abstract[ \t]*\n\n(?P<body>.*?)(?=\n\S|\Z)", re.M | re.S)


def _own_words(text: str) -> int:
    """Words of the post's own prose: the body before the abstract, without the metadata
    block, the directives and their options, and the citation line blocks."""
    body = text.split(".. frame:: Abstract")[0]
    keep = [line for line in body.splitlines()
            if line.strip() and not line.startswith((":", "..", "|"))
            and not line.strip().startswith((":", "|", ".."))]
    prose = re.sub(r"<\{?filename\}?[^>]*>|`|\*", " ", "\n".join(keep))
    return len([w for w in prose.split() if re.search(r"[A-Za-z]", w)])


@pytest.mark.parametrize("post", [p for p in _posts()
                                  if "frame:: Abstract" in p.read_text(encoding="utf-8")
                                  and _fields(p).get("status") != "skip"], ids=lambda p: p.name)
def test_own_text_outweighs_the_quoted_abstract(post):
    """A paper post reproduces the abstract of the paper. The post's own text has to stay
    the larger part of the page: a page whose substance is the publisher's abstract adds
    nothing that the publisher's own page does not already have."""
    text = post.read_text(encoding="utf-8")
    abstract = ABSTRACT_RE.search(text)
    assert abstract, f"{post.name}: abstract frame not recognised"
    quoted = len(abstract.group("body").split())
    own = _own_words(text)
    assert own >= 250, f"{post.name}: only {own} words of its own"
    assert own >= 1.5 * quoted, f"{post.name}: {own} own words against {quoted} quoted"
