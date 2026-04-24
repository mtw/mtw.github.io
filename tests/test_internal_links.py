from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from tests.site_test_utils import build_site


SITE_HOSTS = {"michaelwolfinger.com", "www.michaelwolfinger.com"}
EXPECTED_HOME_LINK_TARGETS = {
    "/research",
    "/publications",
    "/services",
    "/contact",
    "/blog",
}


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        element_id = attrs_dict.get("id")
        if element_id:
            self.ids.add(element_id)

        if tag == "a":
            href = attrs_dict.get("href")
            if href:
                self.hrefs.append(href)


def _parse_html(path: Path) -> LinkCollector:
    parser = LinkCollector()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def _is_internal_link(href: str) -> bool:
    parsed = urlparse(href)
    if href.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return False
    if parsed.scheme and parsed.netloc:
        return parsed.netloc in SITE_HOSTS
    return not href.startswith("//")


def _normalize_target_path(page: Path, output_dir: Path, href: str) -> Path:
    parsed = urlparse(href)
    href_path = parsed.path

    if not href_path:
        return page
    if href_path.startswith("/"):
        candidate = output_dir / href_path.lstrip("/")
    else:
        candidate = page.parent / href_path

    if candidate.is_dir():
        return candidate / "index.html"
    if candidate.exists():
        return candidate
    if not candidate.suffix:
        return candidate / "index.html"
    return candidate


def _assert_fragment_exists(target_page: Path, fragment: str, source_page: Path, href: str) -> None:
    if not fragment:
        return

    target_parser = _parse_html(target_page)
    assert fragment in target_parser.ids, (
        f"{source_page}: missing fragment #{fragment} in {target_page} "
        f"from link {href!r}"
    )


def test_generated_internal_links_resolve_to_existing_pages_and_anchors(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")

    html_pages = sorted(output_dir.rglob("*.html"))
    assert html_pages, "Publish build did not generate any HTML pages"

    homepage = output_dir / "index.html"
    homepage_links = {
        urlparse(href).path.rstrip("/") or "/"
        for href in _parse_html(homepage).hrefs
        if _is_internal_link(href)
    }
    assert EXPECTED_HOME_LINK_TARGETS.issubset(homepage_links), homepage_links

    for page in html_pages:
        parser = _parse_html(page)
        for href in parser.hrefs:
            if not _is_internal_link(href):
                continue

            parsed = urlparse(href)
            target_path = _normalize_target_path(page, output_dir, href)
            assert target_path.exists(), (
                f"{page.relative_to(output_dir)}: missing internal link target "
                f"{href!r} -> {target_path.relative_to(output_dir)}"
            )

            if target_path.suffix == ".html":
                _assert_fragment_exists(target_path, parsed.fragment, page, href)
