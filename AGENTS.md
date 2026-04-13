# Repository Instructions

## Scope

These instructions apply to the whole repository.

## Repository Layout

- `Pelican/` is the source of truth for site content, theme assets, and build configuration.
- The repository root is infrastructure-only. Do not reintroduce checked-in generated site output at the root.

## Build and Validation

- Prefer repository-relevant smoke tests over the bundled upstream theme snapshot suite in `Pelican/pelican-theme/test`.
- Default validation is `./.venv/bin/python -m pytest`.
- For local site checks, use `./Pelican/make.sh` or `cd Pelican && ../.venv/bin/pelican -Dlr content -o output -s pelicanconf.py`.

## Deployment

- GitHub Pages deployment is handled by GitHub Actions.
- Publish by committing to `master` and pushing `origin/master`.
- Do not use local `gh-pages` publishing flows unless the user explicitly asks for them.

## Workflow

- Stage and commit completed changes by default unless the user explicitly asks not to.
- Keep changes focused; do not mix unrelated cleanup into the same commit.
- When a change affects build or deployment, prefer updating the root documentation as part of the same task.
