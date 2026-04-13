import re
from urllib.parse import urlparse

from tests.site_test_utils import build_site


def test_site_build_smoke(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")

    assert (output_dir / "index.html").is_file()
    assert (output_dir / "sitemap.xml").is_file()
    assert (output_dir / "robots.txt").is_file()
    assert (output_dir / "static").is_dir()
    assert (output_dir / "blog").is_dir()


def test_key_pages_and_assets_exist(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")

    required_pages = [
        output_dir / "index.html",
        output_dir / "services" / "index.html",
        output_dir / "contact" / "index.html",
        output_dir / "research" / "index.html",
        output_dir / "legal" / "index.html",
        output_dir / "feeds" / "all.atom.xml",
    ]
    required_assets = [
        output_dir / "CNAME",
        output_dir / "favicon.ico",
        output_dir / "robots.txt",
        output_dir / "sitemap.xml",
        output_dir / "static" / "m-light.compiled.css",
        output_dir / "static" / "m-light.css",
        output_dir / "static" / "m-layout.css",
        output_dir / "static" / "m-grid.css",
        output_dir / "static" / "m-components.css",
    ]

    for path in required_pages + required_assets:
        assert path.exists(), path


def test_key_pages_reference_existing_local_assets(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")

    html_pages = [
        output_dir / "index.html",
        output_dir / "services" / "index.html",
        output_dir / "contact" / "index.html",
        output_dir / "research" / "index.html",
    ]

    for page in html_pages:
        html = page.read_text()
        asset_urls = re.findall(r"""(?:href|src)=["']?([^"' >]+)""", html)
        local_asset_urls = []
        for asset_url in asset_urls:
            parsed = urlparse(asset_url)
            if asset_url.startswith("//") or asset_url.startswith("mailto:") or asset_url.startswith("#"):
                continue
            if parsed.scheme and parsed.netloc not in {"michaelwolfinger.com", "www.michaelwolfinger.com"}:
                continue
            path = parsed.path.lstrip("/")
            if not path:
                continue
            if path.startswith("static/") or path in {"favicon.ico"}:
                local_asset_urls.append(path)

        assert "static/m-light.compiled.css" in local_asset_urls, page

        for asset_path in local_asset_urls:
            resolved = output_dir / asset_path
            assert resolved.exists(), f"{page}: missing asset {asset_path}"
