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
- `tools/`: source of the social-card images (`og-cards-source.html`) and other scripts
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

The development build leaves `SITEURL` empty, so its links are root-relative (`/about/`),
and it goes to `output/`; the production build carries absolute URLs and goes to
`output-publish/`, so the two never mix. Serve `output/` from its root when previewing,
e.g. with `python -m http.server`, not from a subdirectory.

## Tests

`make test` builds the site with the production settings and checks that every URL of
the live site (fixture in `tests/fixtures/`) still resolves, that internal links and
anchors exist, that content metadata is complete, and that publish-time minification
works. No output URL may change; the tests are the gate.

Checks that need the network or installed tooling are opt-in, so `make test` stays offline
and fast:

```
CHECK_EXTERNAL_LINKS=1 pytest tests/test_external_links.py -s   # every outbound link
CHECK_CROSSREF=1       pytest tests/test_paper_authors.py       # author lists vs Crossref
CHECK_AI_COMMANDS=1    pytest tests/test_howto_commands.py -s   # how-to flags vs the real CLIs
CHECK_AI_MODELS=1      pytest tests/test_howto_commands.py      # model ids still published
```

`tests/test_howto_commands.py` also runs offline, where it parses every `toml`, `json` and
`bash` block in the how-to posts, checks the config keys against the ones Codex reads, and
refuses a shell line that invokes a command the post never introduces. With
`CHECK_AI_COMMANDS=1` it additionally lists the posts whose quoted tool version has moved
on and are therefore due a re-run. Running a how-to's commands end to end stays manual:
no test substitutes for a model download and a real agent session.

## Conventions

- A new page means a new URL: add it to the allow-list in `tests/test_live_urls.py` in the
  same commit, so the guard stays binding for every page that is already live.
- The served stylesheet keeps the path `pelican-theme/static/m-mtw.css`. The name predates
  the 2026 relaunch and is kept so that no asset URL changes.
- Structured data for every page is built in `pelican-theme/templates/_ldjson.html`.

## Deployment

GitHub Actions builds, tests and deploys. Every push and pull request runs the build and
the tests; only a push to `master` deploys to GitHub Pages.

1. Commit content or theme changes.
2. Open a pull request, or push `master` directly.
3. The `Build and deploy` workflow publishes `output-publish/`.

There is no local `gh-pages` step.

## License

This project is licensed under the GNU Affero General Public License. See `LICENSE`.
