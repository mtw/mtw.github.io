# michaelwolfinger.com

Source repository for the static site at <https://michaelwolfinger.com>.

The site is built with Pelican. All source content, theme assets, and build configuration live under `Pelican/`.

Dependencies are managed through `pyproject.toml`.

## Repository Layout

- `Pelican/content/`: pages, blog posts, files, and static content source
- `Pelican/pelican-theme/`: theme templates and theme-owned static assets
- `Pelican/pelicanconf.py`: local development settings
- `Pelican/publishconf.py`: production build settings
- `.github/workflows/`: validation and GitHub Pages deployment
- `tests/`: site-level smoke tests

## Local Development

Create or activate the repository virtual environment before building:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev,test]"
```

Useful commands:

```bash
./Pelican/make.sh
cd Pelican && ../.venv/bin/pelican -Dlr content -o output -s pelicanconf.py
./.venv/bin/python -m pytest
./scripts/cleanup.sh
```

What they do:

- `./Pelican/make.sh` builds the site into `Pelican/output/`
- `pelican -Dlr` runs a local development server with live regeneration
- `pytest` runs a site smoke test that verifies a deployable build can be produced
- `./scripts/cleanup.sh` removes generated and local-only artifacts from the working tree

## Deployment

Deployment is handled by GitHub Actions and GitHub Pages.

Workflow:

1. Edit content or theme files under `Pelican/`
2. Validate locally if needed
3. Commit changes
4. Push `master`

```bash
git push origin master
```

The Pages workflow builds `Pelican/output/` from `publishconf.py` and deploys that artifact. There is no need to run a local `gh-pages` publish step.

## Legacy Entry Points

Legacy local entry points still exist in `Pelican/Makefile` and `Pelican/tasks.py`.

- Keep using GitHub Actions on `master` as the canonical deploy path.
- Treat `Pelican/make.sh` as the canonical local build entry point.
- Treat `Makefile` and `tasks.py` as legacy compatibility interfaces unless they are explicitly being modernized.

## CSS Assets

Theme CSS files used in production must exist as real files inside `Pelican/pelican-theme/static/`.

If you update the light theme styles:

1. edit the relevant CSS in `Pelican/pelican-theme/static/`
2. regenerate the compiled stylesheet if needed
3. rebuild locally and confirm `Pelican/output/static/m-light.compiled.css` is present

Do not replace theme CSS files with symlinks to repo-root assets. GitHub Pages deployment depends on the theme shipping its own static files.

## License

This project is licensed under the GNU Affero General Public License. See `LICENSE`.
