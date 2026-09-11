# Project notes for Claude

The authoritative instructions are in `AGENTS.md` and `README.md`; this file only adds pointers.

- Pelican project: `Pelican/` (content in `Pelican/content/`, theme in `Pelican/pelican-theme/`,
  settings in `Pelican/pelicanconf.py` with `Pelican/publishconf.py` for production builds).
- Build locally: `cd Pelican && ../.venv/bin/pelican content -s pelicanconf.py -o output`
  (or `./Pelican/make.sh`). Production build as used by CI: `python scripts/build_publish.py`.
- Validate: `./.venv/bin/python -m pytest` from the repository root.
- Never commit `Pelican/output/`; it is generated.
- No output URL may change. Check with a clean publish build of `master` and of the branch and
  diff `find . -type f | sort` of both trees; the diff must be empty.
- The served stylesheet is `Pelican/pelican-theme/static/m-mtw.css` (the path pre-dates the
  2026 relaunch, which is why the relaunch added no new URL).
- Structured data comes from `Pelican/pelican-theme/templates/_ldjson.html`.
