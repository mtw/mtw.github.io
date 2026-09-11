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

BLOG_DIR = Path(__file__).resolve().parents[1] / "Pelican" / "content" / "blog"
REQUIRED = ("date", "slug", "category", "tags", "summary", "description", "author")
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
    assert len(_posts()) >= 71


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
