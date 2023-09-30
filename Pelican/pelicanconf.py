#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Michael T. Wolfinger'
SITENAME = "Michael T. Wolfinger Bioinformatics"
SITEURL = ''

STATIC_URL = '{path}'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['blog/authors','blog/category','blog/tags']
PAGE_PATHS = ['']

TIMEZONE = 'Europe/Vienna'
DEFAULT_DATE = None

DEFAULT_LANG = 'en'

THEME = 'pelican-theme'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static']

DIRECT_TEMPLATES = ['index']

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

#<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?forceLang=en&customize=1&tracking=1&thirdparty=1&always=1"></script>

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Roboto:300;400|Source+Code+Pro:200:300,400|Source+Sans+Pro:300,400',
               'static/m-light.compiled.min.css',
               'static/m-mtw.min.css']
M_THEME_COLOR = '#EAEAEA'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['m.htmlsanity',
           'm.components',
           'm.link',
           'm.pelican_redirect',
           'm.sitemap',
           'm.images']

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "always",
        "indexes": "always",
        "pages": "always"
    },
    "exclude": ["blog/archive/", "blog/author/", "blog/category/", "blog/tag/", "archives", "authors", "categories", "tags", "index", "legal"]
}

GITHUB_URL = "https://github.com/mtw/mtw.github.io"

DEFAULT_PAGINATION = 10

#M_SITE_LOGO_TEXT = 'Your Brand'

M_LINKS_NAVBAR1 = [
                    ('Publications', '/publications', 'publications', [
                        ('Papers', '/publications', 'papers'),
                        ('Presentations', 'publications/presentations', 'publications/presentations'),
                        ('Posters', 'publications/posters', 'publications/posters'),
                        ]),
                    ('Teaching', '/teaching', 'teaching', []),
                    ('Consultancy', '/consulting', 'consulting', []),
                    ('Contact', '/contact', 'contact', []),
                    ('Blog', 'blog/', '[blog]',[])]

#M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]',[])]

M_LINKS_FOOTER1 = [('Home', '/'),
                    ('Publications', '/publications'),
                    ('Teaching', '/teaching'),
                    ('Contact', '/contact'),
                    ('Blog', '/blog'),
                        ]

M_LINKS_FOOTER2 = [('Services', ''),
                    ('Bioinformatics Consulting', '/consulting'),
                    ('RNA Forecast', 'https://rnaforecast.com'),
                    ('Legal Note','/legal')
                        ]

M_LINKS_FOOTER3 = [('My Profiles',''),
                    ('Google Scholar', 'https://scholar.google.at/citations?user=w0PHGnEAAAAJ&hl=en'),
                    ('Web of Science', 'https://www.webofscience.com/wos/author/record/N-9538-2014'),
                    ('ResearchGate', 'https://www.researchgate.net/profile/Michael-Wolfinger'),
                    ('Scopus', 'https://www.scopus.com/authid/detail.uri?authorId=6508361997'),

                        ]

M_LINKS_FOOTER4 = [('Social', ''),
                    ('Linkedin', 'https://www.linkedin.com/in/michaelwolfinger/'),
                    ('Twitter', 'https://twitter.com/mtwolfinger'),
                    ('GitHub', 'https://github.com/mtw'),
                    ('ORCID', 'https://orcid.org/0000-0003-0925-5205'),

                    ]

M_FINE_PRINT =  """
| michaelwolfinger.com - Copyright © Michael T. Wolfinger, 2021-2023
"""

STATIC_PATHS = ['static', 'extra/CNAME', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'static/academicons.min.css': {'path': 'static/academicons.min.css'}
                        }

DISPLAY_PAGES_ON_MENU = True

PATH_METADATA = '(?P<slug>.+).rst'

#M_HTML_HEADER = '<link rel="stylesheet" href="extra/css/extra.css"'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TWITTER_USERNAME = 'mtwolfinger'

M_BLOG_NAME = "michaelwolfinger.com Bioinformatics"
M_BLOG_URL = 'https://michaelwolfinger.com/blog'
M_BLOG_DESCRIPTION = "michaelwolfinger.com | virus bioinformatics"

M_SOCIAL_TWITTER_SITE = '@mtwolfinger'
M_SOCIAL_TWITTER_SITE_ID = 15105886
#M_SOCIAL_IMAGE = 'https://your.brand/static/site.png'
M_SOCIAL_BLOG_SUMMARY = "Stuff that matters in virus bioinformatics"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
REDIRECT_SAVE_AS = PAGE_SAVE_AS
ARCHIVES_URL = 'blog/archive/'
ARCHIVES_SAVE_AS = 'blog/archive/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
#AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
AUTHOR_SAVE_AS = ''
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
#CATEGORY_SAVE_AS = ''
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
#TAG_SAVE_AS = ''
INDEX_SAVE_AS = 'blog/index.html'

AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

YEAR_ARCHIVE_URL = 'blog/{date:%Y}/{slug}/'
#YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
YEAR_ARCHIVE_SAVE_AS = ''

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

DEFAULT_PAGINATION = 5
