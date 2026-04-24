import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PELICAN_DIR = REPO_ROOT / "Pelican"
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
