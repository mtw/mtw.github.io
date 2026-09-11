michaelwolfinger.com
====================

This directory contains the Pelican source for https://michaelwolfinger.com.

Canonical workflows
-------------------

- Local build: ``./make.sh``
- Local build with production settings: ``./make.sh publishconf.py``
- Local live preview: ``../.venv/bin/pelican -Dlr content -o output -s pelicanconf.py``
- Production build with minification: ``../.venv/bin/python ../scripts/build_publish.py``
- Validation: ``../.venv/bin/python -m pytest``
- Production deployment: GitHub Actions on ``master``

Legacy entry points
-------------------

``Makefile`` and ``tasks.py`` are kept for compatibility and local convenience, but they are not the authoritative deployment path.

CSS assets
----------

Theme CSS files used in production must exist as real files in ``pelican-theme/static/``. Do not replace them with symlinks to repo-root files.

The site loads a single stylesheet, ``pelican-theme/static/m-mtw.css`` (plain CSS with custom
properties, no build step). The old m.css files next to it are unused legacy assets.

GitHub Actions minifies publish-only CSS, JS, and HTML output during the production build. Local development continues to use the unminified ``m-light.css`` from ``pelicanconf.py``.

``./make.sh`` now defaults to ``pelicanconf.py`` so local output keeps local asset URLs and preview styling. Pass ``publishconf.py`` explicitly only when you want a non-minified production-style build in ``output/``.
