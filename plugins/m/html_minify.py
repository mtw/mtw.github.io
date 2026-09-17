# Last changed Time-stamp: <2022-09-22 14:11:47 mtw>
# Pelican HTML minity Plugin from https://cloudbytes.dev/snippets/pelican-plugin-to-minify-html-css-and-js

import minify_html
import glob
import os
import sys
import logging

from pelican import signals

logger = logging.getLogger()


def main(pelican):
    for file in glob.iglob(pelican.output_path + "/**/*.html", recursive=True):
        print(f"Processing {file}")
        try:
            with open(file, "r", encoding="utf-8") as html:
                minified = minify_html.minify(html.read(), do_not_minify_doctype=True)
            with open(file, "w", encoding="utf-8") as html:
                html.write(minified)
        except Exception as error:
            logging.error(error)

def register():
    signals.finalized.connect(main)
