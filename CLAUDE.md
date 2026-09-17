# Project notes for Claude

The authoritative instructions are in `AGENTS.md` and `README.md`; this file only adds pointers.

- Plain Pelican project at the repository root. Build with `make devserver` (or
  `pelican -lr` from the root), production build with `make check`, tests with `make test`.
- Never commit `output/` or `output-publish/`; they are generated.
- No output URL may change. Compare `find . -type f | sort` of production builds of
  `master` and the branch; `tests/test_live_urls.py` guards the live sitemap.
- The served stylesheet is `pelican-theme/static/m-mtw.css` (the path pre-dates the 2026
  relaunch, which is why the relaunch added no new URL).
- Structured data comes from `pelican-theme/templates/_ldjson.html`.
- Never put Claude attribution in commit messages or pull requests.
