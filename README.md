# michaelwolfinger.com

Source repository for the static site at <https://michaelwolfinger.com>, built with Pelican.
The layout is a plain Pelican project at the repository root; dependencies are managed
through `pyproject.toml`.

## Repository Layout

- `content/`: pages, blog posts, files, and static content source
- `pelican-theme/`: theme templates and the stylesheet (`static/m-mtw.css`)
- `plugins/`: the m.css plugins the content relies on
- `pelicanconf.py`: local development settings; `publishconf.py`: production settings
- `scripts/`: the publish-time minification step
- `tests/`: site tests (build, internal links, live URLs, content metadata)
- `tools/`: source of the social-card images (`og-cards-source.html`) and `analytics_report.py`
  (GA4 + Search Console summary; needs `pip install -e ".[analytics]"` and a service-account key
  outside the repository, see the script docstring)
- `.github/workflows/build-deploy.yml`: build, test and GitHub Pages deployment

## Local Development

Create or activate the virtual environment once:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev,test]"
```

Then, from the repository root:

```bash
make devserver          # build, serve http://localhost:8000, rebuild on change
make html               # development build into output/
make publish            # production build into output-publish/, minified
make check              # production build under --fatal warnings + smoke checks
make test               # run the test suite
make clean              # remove output/ and output-publish/
```

`pelican -lr` from the root does the same as `make devserver`. On macOS `make` needs the Xcode
command line tools (`xcode-select --install`).

The development build uses relative URLs and goes to `output/`; the production build
carries absolute URLs and goes to `output-publish/`, so the two never mix.

## Tests

`make test` builds the site with the production settings and checks that every URL of
the live site (fixture in `tests/fixtures/`) still resolves, that internal links and
anchors exist, that content metadata is complete, and that publish-time minification
works. No output URL may change; the tests are the gate.

## Deployment

GitHub Actions builds, tests and deploys. Every push and pull request runs the build and
the tests; only a push to `master` deploys to GitHub Pages.

1. Commit content or theme changes.
2. Open a pull request, or push `master` directly.
3. The `Build and deploy` workflow publishes `output-publish/`.

There is no local `gh-pages` step.

## License

This project is licensed under the GNU Affero General Public License. See `LICENSE`.
