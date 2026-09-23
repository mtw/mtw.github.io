"""Structured data, sitemap, and robots invariants of the production build.

The JSON-LD in pelican-theme/templates/_ldjson.html is hand-written JSON, and the sitemap
plugin builds its own XML; nothing else would notice a stray comma, a duplicate <loc>, or a
lastmod with a bogus timezone offset.
"""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import pytest

from tests.site_test_utils import build_site

SITEURL = "https://michaelwolfinger.com"
LDJSON_RE = re.compile(r'<script type="?application/ld\+json"?>(.*?)</script>', re.S)
LASTMOD_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:00)$")


@pytest.fixture(scope="module")
def output_dir(tmp_path_factory) -> Path:
    return build_site(tmp_path_factory.mktemp("seo"), "publishconf.py")


def _html_pages(output_dir: Path) -> list[Path]:
    """Real pages: not the 404 page, the services stub, or a redirect stub."""
    return sorted(p for p in output_dir.rglob("*.html")
                  if p.name != "404.html" and "services" not in p.parts
                  and "http-equiv=refresh" not in p.read_text(encoding="utf-8"))


def _graph(page: Path) -> list[dict]:
    blocks = LDJSON_RE.findall(page.read_text(encoding="utf-8"))
    assert blocks, f"{page}: no JSON-LD"
    nodes = []
    for block in blocks:
        data = json.loads(block)  # raises on malformed JSON
        nodes.extend(data.get("@graph", [data]))
    return nodes


def _types(node: dict) -> set[str]:
    t = node.get("@type", [])
    return set(t if isinstance(t, list) else [t])


def test_every_page_has_valid_jsonld_with_one_person(output_dir):
    persons = set()
    for page in _html_pages(output_dir):
        nodes = _graph(page)
        types = set().union(*(_types(n) for n in nodes))
        assert "WebSite" in types and "Person" in types, f"{page}: {types}"
        for node in nodes:
            for key in ("url", "@id"):
                value = node.get(key)
                if isinstance(value, str) and not value.startswith(("https://doi.org/", "https://rnaforecast.com")):
                    assert value.startswith(SITEURL), f"{page}: relative {key} {value}"
        persons.add(json.dumps(next(n for n in nodes if "Person" in _types(n)), sort_keys=True))
    assert len(persons) == 1, "Person node differs between pages"


def test_paper_posts_carry_scholarly_article_with_doi(output_dir):
    posts = sorted((output_dir / "blog").glob("20*/*/index.html"))
    assert posts
    with_doi = 0
    for post in posts:
        nodes = _graph(post)
        posting = next(n for n in nodes if "BlogPosting" in _types(n))
        for key in ("headline", "datePublished", "dateModified", "image", "author", "mainEntityOfPage"):
            assert posting.get(key), f"{post}: BlogPosting lacks {key}"
        scholarly = [n for n in nodes if "ScholarlyArticle" in _types(n)]
        if scholarly:
            with_doi += 1
            doi = scholarly[0]["identifier"]["value"]
            assert doi.startswith("10."), doi
            assert scholarly[0]["@id"] == f"https://doi.org/{doi}"
            assert posting["about"]["@id"] == scholarly[0]["@id"]
            assert isinstance(scholarly[0]["author"], list) and len(scholarly[0]["author"]) >= 1
            assert scholarly[0]["isPartOf"]["name"] and re.match(r"^\d{4}$", scholarly[0]["datePublished"])
    assert with_doi >= 50, with_doi


def test_publications_page_lists_papers(output_dir):
    nodes = _graph(output_dir / "publications" / "index.html")
    item_list = next(n for n in nodes if "ItemList" in _types(n))
    items = item_list["itemListElement"]
    assert item_list["numberOfItems"] == len(items) >= 50
    assert [i["position"] for i in items] == list(range(1, len(items) + 1))
    assert all(i["item"]["@id"].startswith("https://doi.org/10.") for i in items)


def test_talks_and_posters_are_event_lists(output_dir):
    for path, minimum in (("presentations", 15), ("posters", 20)):
        nodes = _graph(output_dir / "publications" / path / "index.html")
        item_list = next(n for n in nodes if "ItemList" in _types(n))
        items = item_list["itemListElement"]
        assert len(items) >= minimum, (path, len(items))
        for entry in items:
            event = entry["item"]
            assert event["@type"] == "Event" and event["name"] and event["location"]["address"]
            assert re.match(r"^\d{4}-\d{2}(-\d{2})?$", event["startDate"]), event
            if "workFeatured" in event and "url" in event["workFeatured"]:
                url = event["workFeatured"]["url"]
                assert url.startswith(SITEURL) and (output_dir / url[len(SITEURL) + 1:]).is_file(), url


def test_llms_full_lists_papers_and_talks(output_dir):
    text = (output_dir / "llms-full.txt").read_text(encoding="utf-8")
    for heading in ("## Publications", "## Talks and Presentations", "## Posters", "## Writing"):
        assert heading in text, heading
    assert text.count("https://doi.org/10.") >= 60
    assert text.count("\n- ") >= 90


def _sitemap_urls(output_dir: Path) -> list[tuple[str, str]]:
    xml = (output_dir / "sitemap.xml").read_text(encoding="utf-8")
    return re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", xml)


def test_sitemap_is_sane(output_dir):
    entries = _sitemap_urls(output_dir)
    urls = [u for u, _ in entries]
    assert len(urls) == len(set(urls)), "duplicate <loc> in sitemap"
    assert f"{SITEURL}/blog/" in urls, "blog index missing from sitemap"
    assert f"{SITEURL}/" in urls
    for url, lastmod in entries:
        assert url.startswith(SITEURL + "/"), url
        path = urlparse(url).path
        target = output_dir / path.lstrip("/")
        if path.endswith("/"):
            target = target / "index.html"
        assert target.is_file(), f"sitemap lists {url} but no file exists"
        assert LASTMOD_RE.match(lastmod), f"{url}: bad lastmod {lastmod}"
    for excluded in ("/blog/category/", "/publications/papers/", "/services/", "/404"):
        assert not any(excluded in u for u in urls), f"{excluded} must not be in the sitemap"


def test_sitemap_does_not_list_robots_disallowed_urls(output_dir):
    robots = (output_dir / "robots.txt").read_text(encoding="utf-8")
    prefixes = [line.split(":", 1)[1].strip().rstrip("*") for line in robots.splitlines() if line.lower().startswith("disallow:")]
    assert prefixes
    for url, _ in _sitemap_urls(output_dir):
        path = urlparse(url).path
        assert not any(path.startswith(p) for p in prefixes), f"{url} is in the sitemap but disallowed in robots.txt"


def test_noindex_and_auxiliary_files(output_dir):
    stub = (output_dir / "404.html").read_text(encoding="utf-8")
    assert "noindex" in stub and "/publications/" in stub
    for index_copy in sorted((output_dir / "blog").glob("index[0-9]*.html")):
        html = index_copy.read_text(encoding="utf-8")
        assert "noindex" in html and f'{SITEURL}/blog/' in html, index_copy
    assert (output_dir / "llms.txt").read_text(encoding="utf-8").startswith("# Michael T. Wolfinger")
    manifest = json.loads((output_dir / "site.webmanifest").read_text(encoding="utf-8"))
    for icon in manifest["icons"]:
        assert (output_dir / icon["src"].lstrip("/")).is_file(), icon
    assert (output_dir / "static" / "apple-touch-icon.png").is_file()


def _meta(html: str, name: str) -> str | None:
    m = re.search(r'<meta[^>]*name="?' + name + r'"?[^>]*>', html)
    if not m:
        return None
    c = re.search(r'content="([^"]*)"', m.group(0)) or re.search(r"content=([^\s>]+)", m.group(0))
    return c.group(1) if c else None


def test_titles_and_descriptions(output_dir):
    titles, descriptions = {}, {}
    for page in _html_pages(output_dir):
        html = page.read_text(encoding="utf-8")
        title = re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()
        assert title and title not in titles, f"{page}: duplicate/empty title ({titles.get(title)})"
        titles[title] = page
        desc = _meta(html, "description")
        assert desc and 50 <= len(desc) <= 160, f"{page}: description of {len(desc or '')} chars"
        assert desc not in descriptions, f"{page}: description duplicates {descriptions.get(desc)}"
        descriptions[desc] = page


def test_figure_images_carry_dimensions_and_lazy_loading(output_dir):
    checked = 0
    for post in sorted((output_dir / "blog").glob("20*/*/index.html")):
        imgs = re.findall(r"<img\b[^>]*>", post.read_text(encoding="utf-8"))
        if len(imgs) < 2:
            continue
        checked += 1
        assert all("width=" in i and "height=" in i for i in imgs), (post, imgs)
        assert "loading=lazy" in imgs[-1] and "loading=" not in imgs[0], (post, imgs)
    assert checked >= 1


def test_fonts_are_self_hosted(output_dir):
    css = (output_dir / "static" / "m-mtw.css").read_text(encoding="utf-8")
    fonts = set(re.findall(r"url\((fonts/[^)]+\.woff2)\)", css))
    assert len(fonts) >= 6
    for font in fonts:
        assert (output_dir / "static" / font).is_file(), font
    for page in list(output_dir.rglob("*.html")) + [output_dir / "static" / "m-mtw.css"]:
        assert "fonts.googleapis.com" not in page.read_text(encoding="utf-8"), page
        assert "fonts.gstatic.com" not in page.read_text(encoding="utf-8"), page


def test_analytics_are_consent_gated(output_dir):
    """No Google request before consent: gtag.js is never a static <script src>, the banner
    and the privacy page exist, and the footer offers a way to change the choice."""
    for page in output_dir.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        assert not re.search(r"<script[^>]*src=[\"']?https://www\.googletagmanager\.com", html), page
    home = (output_dir / "index.html").read_text(encoding="utf-8")
    assert "mtw-consent" in home and 'id=cookie-settings' in home.replace('"', "")
    assert "#cookie-settings" in home and "/datenschutz/" in home
    privacy = (output_dir / "datenschutz" / "index.html").read_text(encoding="utf-8")
    assert "Google Analytics" in privacy and "Datenschutzbehörde" in privacy


def test_commercial_pages_stay_hidden(output_dir):
    # AGENTS.md: a personal academic site with no commercial offer; /services/ is only a redirect.
    services = (output_dir / "services" / "index.html").read_text(encoding="utf-8")
    assert "noindex" in services and "http-equiv=refresh" in services
    assert not (output_dir / "consulting").exists() and not (output_dir / "services" / "workshops").exists()
    assert not list(output_dir.glob("content/services*"))
    for page in output_dir.rglob("*.html"):
        assert "hello@rnaforecast.com" not in page.read_text(encoding="utf-8"), page
