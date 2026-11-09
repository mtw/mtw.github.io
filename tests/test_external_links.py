"""Outbound links of the production build resolve (opt-in: needs the network).

Run with  CHECK_EXTERNAL_LINKS=1 pytest tests/test_external_links.py -s
A redirect loop (urllib exhausts its redirect limit and reports the 3xx) counts as broken.
Hosts that answer 403/429 to non-browser clients are reported but do not fail the test;
404/410 and connection failures do.
"""
import http.cookiejar
import os
import re
import socket
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

import pytest

from tests.site_test_utils import build_site

pytestmark = pytest.mark.skipif(not os.environ.get("CHECK_EXTERNAL_LINKS"), reason="set CHECK_EXTERNAL_LINKS=1")
SITE_HOSTS = {"michaelwolfinger.com", "www.michaelwolfinger.com"}
# Single-page apps that answer 404 to non-browser or datacenter requests although the
# profile exists (verified in a browser); reported as blocked rather than broken.
UNRELIABLE_HOSTS = {"bsky.app", "loop.frontiersin.org"}
# A browser-like UA: single-page apps (Bluesky, Loop) answer 404 to anything else.
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"


def _fetch(url):
    # Keep cookies while following redirects. A HISinOne course page and Elsevier's OAuth
    # bounce both set a session cookie and redirect; without a jar the same request repeats
    # until urllib gives up, which is indistinguishable from a redirect loop.
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with opener.open(req, timeout=20) as resp:
                return resp.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 405, 501):
                continue
            return e.code
        except (urllib.error.URLError, socket.timeout, ConnectionError, OSError) as e:
            return f"error: {e}"
    return "error"


def test_external_links_resolve(tmp_path):
    output_dir = build_site(tmp_path, "publishconf.py")
    urls = {}
    for page in output_dir.rglob("*.html"):
        for href in re.findall(r"""href=["']?(https?://[^"' >]+)""", page.read_text(encoding="utf-8")):
            if urlparse(href).netloc not in SITE_HOSTS:
                urls.setdefault(href, page.relative_to(output_dir))
    with ThreadPoolExecutor(16) as pool:
        results = dict(zip(urls, pool.map(_fetch, urls)))
    unreliable = {u for u in results if urlparse(u).netloc in UNRELIABLE_HOSTS}
    # A 3xx can only reach us when urllib exhausted its redirect limit, i.e. a redirect
    # loop: the browser shows an error page, so it counts as broken. Ordinary redirects
    # are followed by urlopen and come back as the final status.
    broken = {
        u: r
        for u, r in results.items()
        if u not in unreliable
        and (r in (404, 410) or isinstance(r, str) or (isinstance(r, int) and 300 <= r < 400))
    }
    blocked = {u: r for u, r in results.items() if r in (401, 403, 429, 503) or (u in unreliable and r != 200)}
    print(f"\nchecked {len(urls)} URLs; {len(broken)} broken, {len(blocked)} blocked/rate-limited")
    for u, r in sorted(blocked.items()):
        print(f"  blocked  {r}  {u}  ({urls[u]})")
    for u, r in sorted(broken.items()):
        print(f"  BROKEN   {r}  {u}  ({urls[u]})")
    assert not broken, f"{len(broken)} broken outbound link(s), see output"
