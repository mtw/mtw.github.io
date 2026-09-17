PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
# The production build goes to its own directory: it carries absolute
# michaelwolfinger.com URLs, so mixing it into output/ breaks the local preview.
PUBLISHDIR=$(BASEDIR)/output-publish
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif

help:
	@echo 'make html                  (re)generate the site into output/'
	@echo 'make devserver [PORT=8000] serve http://localhost:8000 and regenerate on change'
	@echo 'make serve                 build and serve output/'
	@echo 'make publish               production build (publishconf.py) into output-publish/, minified'
	@echo 'make check                 production build under --fatal warnings + smoke checks'
	@echo 'make test                  run the pytest suite'
	@echo 'make clean                 remove output/ and output-publish/'

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"
	[ ! -d "$(PUBLISHDIR)" ] || rm -rf "$(PUBLISHDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve: html
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(PUBLISHDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS) --fatal warnings
	"$(PY)" scripts/optimize_publish.py "$(PUBLISHDIR)"

check: publish
	test -f "$(PUBLISHDIR)/index.html"
	test -f "$(PUBLISHDIR)/sitemap.xml"
	test -f "$(PUBLISHDIR)/robots.txt"
	test -f "$(PUBLISHDIR)/CNAME"
	test -f "$(PUBLISHDIR)/static/m-mtw.css"
	test -f "$(PUBLISHDIR)/feeds/all.atom.xml"

test:
	"$(PY)" -m pytest -q

.PHONY: help html clean regenerate serve devserver publish check test
