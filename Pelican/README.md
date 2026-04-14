michaelwolfinger.com
====================

This directory contains the Pelican source for https://michaelwolfinger.com.

Canonical workflows
-------------------

- Local build: ``./make.sh``
- Local live preview: ``../.venv/bin/pelican -Dlr content -o output -s pelicanconf.py``
- Validation: ``../.venv/bin/python -m pytest``
- Production deployment: GitHub Actions on ``master``

Legacy entry points
-------------------

``Makefile`` and ``tasks.py`` are kept for compatibility and local convenience, but they are not the authoritative deployment path.

CSS assets
----------

Theme CSS files used in production must exist as real files in ``pelican-theme/static/``. Do not replace them with symlinks to repo-root files.
