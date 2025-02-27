#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://michaelwolfinger.com'
RELATIVE_URLS = True

#M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Roboto:300;400|Source+Code+Pro:200:300,400|Source+Sans+Pro:300,400',
#               'static/m-light.compiled.css',
#               'static/m-mtw.css']

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = 'G-T2RW3VW55N'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
