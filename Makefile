# Convenience wrapper: the Pelican project lives in Pelican/, and `pelican` only finds its
# settings when run from there. These targets forward to Pelican/Makefile so the usual
# commands work from the repository root as well.

PELICAN ?= $(CURDIR)/.venv/bin/pelican
export PELICAN

.PHONY: help html devserver serve publish clean test

help:
	@echo 'make html       build the site with pelicanconf.py into Pelican/output'
	@echo 'make devserver  build, serve on http://127.0.0.1:8000 and rebuild on change'
	@echo 'make serve      serve the last build on http://127.0.0.1:8000'
	@echo 'make publish    production build (publishconf.py) into Pelican/output'
	@echo 'make clean      remove Pelican/output'
	@echo 'make test       run the test suite'

html devserver serve publish clean:
	$(MAKE) -C Pelican $@

test:
	$(CURDIR)/.venv/bin/python -m pytest -q
