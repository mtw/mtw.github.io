#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Michael T. Wolfinger'
SITENAME = "Michael T. Wolfinger"
SITEURL = ''

STATIC_URL = '{path}'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['blog/authors','blog/category','blog/tag']
PAGE_PATHS = ['']

TIMEZONE = 'Europe/Vienna'
DEFAULT_DATE = None

DEFAULT_LANG = 'en'

THEME = 'pelican-theme'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static']

DIRECT_TEMPLATES = ['index']

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Roboto:300;400|Source+Code+Pro:200:300,400|Source+Sans+Pro:300,400',
               'static/m-light.css']

M_THEME_COLOR = '#EAEAEA'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['m.htmlsanity',
           'm.components',
           'm.link',
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
    "exclude": ["blog/archive/", "blog/author/", "authors", "index", "legal"]
}

GITHUB_URL = "https://github.com/mtw/mtw.github.io"

DEFAULT_PAGINATION = 10

#M_SITE_LOGO_TEXT = 'Your Brand'

M_LINKS_NAVBAR1 = [
                    ('Research', '/research', 'research', [
                        ('Team', '/team', 'team'),
                    ]),
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
                    ('Research', '/research'),
                    ('Publications', '/publications'),
                    ('Teaching', '/teaching'),
                    ('Team', '/team'),
                    ('Blog', '/blog'),
                    ]

M_LINKS_FOOTER2 = [('Services', ''),
                    ('Bioinformatics Consulting', '/consulting'),
                    ('RNA Forecast', 'https://rnaforecast.com'),
                    ('xrRNA.bio', 'https://xrrna.bio'),
		            ('Contact', '/contact'),
                    ('Legal Note','/legal'),   
                    ]

M_LINKS_FOOTER3 = [('My Profiles',''),
                    ('Google Scholar', 'https://scholar.google.at/citations?user=w0PHGnEAAAAJ&hl=en'),
                    ('ResearchGate', 'https://www.researchgate.net/profile/Michael-Wolfinger'),
                    ('Scopus', 'https://www.scopus.com/authid/detail.uri?authorId=6508361997'),
                    ('Loop', 'https://loop.frontiersin.org/people/485709/overview'),
                    ]       

M_LINKS_FOOTER4 = [('Social', ''),
                    ('Linkedin', 'https://www.linkedin.com/in/michaelwolfinger/'),
                    ('Bluesky', 'https://bsky.app/profile/mtwolfinger.bsky.social'),
                    ('GitHub', 'https://github.com/mtw'),
                    ('ORCID', 'https://orcid.org/0000-0003-0925-5205'),
                    ]

M_FINE_PRINT =  """
| michaelwolfinger.com - Copyright © Michael T. Wolfinger, 2021-2025
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
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TWITTER_USERNAME = 'mtwolfinger'

M_BLOG_NAME = "michaelwolfinger.com Bioinformatics Blog"
M_BLOG_URL = 'https://michaelwolfinger.com/blog'
M_BLOG_DESCRIPTION = "michaelwolfinger.com | Advancing RNA biology through the innovative application of AI and computational techniques"

M_SOCIAL_TWITTER_SITE = '@mtwolfinger'
M_SOCIAL_TWITTER_SITE_ID = 15105886
#M_SOCIAL_IMAGE = 'https://your.brand/static/site.png'
M_SOCIAL_BLOG_SUMMARY = "Unlocking the future of RNA biology through innovative AI and computational techniques"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
#ARCHIVES_URL = 'blog/archives/archives.html'
#ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = ''
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'

#YEAR_ARCHIVE_URL = 'blog/archives/{date:%Y}.html'
#YEAR_ARCHIVE_SAVE_AS = 'blog/archives/{date:%Y}.html'

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

DEFAULT_PAGINATION = 5

CSS_MIN = True
HTML_MIN = True
