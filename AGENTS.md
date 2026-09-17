# Repository Instructions

## Scope

These instructions apply to the whole repository.

## Repository Layout

- A plain Pelican project at the repository root: `content/`, `pelican-theme/`, `plugins/`,
  `pelicanconf.py`, `publishconf.py`, `Makefile`.
- `output/` and `output-publish/` are generated and never committed.
- `design_handoff/` (untracked) holds the 2026 design mockups for reference only.

## Build and Validation

- `make devserver` for local work, `make check` for a production build, `make test` for the
  test suite (default validation: `./.venv/bin/python -m pytest`).
- Prefer the repository tests over the bundled upstream theme suite in `pelican-theme/test`.
- No output URL may change. `tests/test_live_urls.py` enforces the live sitemap; an intended
  new page must be added to its allow-list.

## Deployment

- GitHub Pages deployment is handled by `.github/workflows/build-deploy.yml`.
- Publish by merging to `master`; pull requests build and test but do not deploy.
- Do not use local `gh-pages` publishing flows unless the user explicitly asks for them.

## Workflow

- Stage and commit completed changes by default unless the user explicitly asks not to.
- Keep changes focused; do not mix unrelated cleanup into the same commit.
- Never add Claude attribution trailers to commit messages or pull requests.
- Nothing about commercial services or workshops may be visible before December 2026.
