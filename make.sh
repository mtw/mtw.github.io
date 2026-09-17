#!/bin/sh
# Development build into output/, then a production build into output-publish/.
pelican content -D -o output -s pelicanconf.py
pelican content -D -o output-publish -s publishconf.py
