<!--
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
-->
## Quick Commands
- **Build Site**: `pelican` or `python -m pelican --output=output`
- **Serve While Editing** (use your theme template): `python -m pelican --listen=0.0.0.0:8000 --template="themes/mytheme/templates/article.html"
- **Clean Output**: `rm -rf output/*`
- **Check Git Status**: `git status`
- **Commit Changes** (after refining with `Read`/`Edit`): `git add <file>\n git commit -m "[Auto] Description"`

## Big-Picture Architecture
This is a Pelican-based static site:
- **Content**: Markdown/ReST files in `content/` (or repo root)
- **Templates**: HTML templates under `themes/mytheme/templates/`
- **Output**: `output/` (default Pelican output)
- **Configuration**: `_config.yml` or `pelican.conf.py`

## Notable Files/Pipelines
- `.github/workflows/validate.yml`
- `.github/workflows/static.yml`
- `.github/dependabot.yml`
- `themes/mytheme/templates/*` (render your content)

## Notes
- Never commit generated outputs (`output/*`)—Pelican rebuilds them on each build.
- Adjust theme templates in `themes/mytheme/` for UI changes.
- Use descriptive commit messages focusing on why changes were made.
- If you’d like to add a new post, create a Markdown file in `content/` with appropriate front matter.
