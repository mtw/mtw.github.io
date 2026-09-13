"""Every URL that exists on the live site must keep resolving after a publish build.

tests/fixtures/live_sitemap_2026-09.xml is the sitemap taken from the live site in
September 2026 (108 unique URLs). A URL may legitimately leave the *sitemap* (e.g. the
services page is a no-index redirect until the business launch), but it must never stop
producing a file, because the site has a long search history.
"""
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

from tests.site_test_utils import build_site

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "live_sitemap_2026-09.xml"
SITE_HOSTS = {"michaelwolfinger.com", "www.michaelwolfinger.com"}


def _live_urls() -> list[str]:
    urls = sorted(set(re.findall(r"<loc>([^<]+)</loc>", FIXTURE.read_text(encoding="utf-8"))))
    assert len(urls) >= 100, "fixture looks truncated"
    return urls


def _output_file(output_dir: Path, url: str) -> Path:
    parsed = urlparse(url)
    assert parsed.netloc in SITE_HOSTS, url
    target = output_dir / unquote(parsed.path).lstrip("/")
    if target.is_dir() or not target.suffix:
        target = target / "index.html"
    return target


def test_every_live_url_still_resolves(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")
    missing = [url for url in _live_urls() if not _output_file(output_dir, url).exists()]
    assert not missing, f"{len(missing)} live URL(s) no longer produce a file: {missing[:10]}"


def test_new_sitemap_adds_no_unknown_urls_and_drops_only_hidden_pages(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")
    new = set(re.findall(r"<loc>([^<]+)</loc>", (output_dir / "sitemap.xml").read_text(encoding="utf-8")))
    live = set(_live_urls())
    # Pages hidden on purpose until the business launch may leave the sitemap, nothing else may.
    allowed_to_leave = {"https://michaelwolfinger.com/services/"}
    dropped = live - new - allowed_to_leave
    assert not dropped, f"URLs dropped from the sitemap: {sorted(dropped)}"
    added = new - live
    assert not added, f"unexpected new sitemap URLs (fine if intended, then update the fixture): {sorted(added)}"
