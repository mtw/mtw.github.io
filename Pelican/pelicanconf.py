#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Michael T. Wolfinger'
SITENAME = "Michael T. Wolfinger"
SITEURL = ''

STATIC_URL = '{path}'

PATH = 'content'
PAGE_PATHS = ['']

TIMEZONE = 'Europe/Vienna'
DEFAULT_DATE = None

DEFAULT_LANG = 'en'

THEME = 'pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

#M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
#               '/static/m-dark.css']
#M_THEME_COLOR = '#22272e'

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Roboto:300;400|Source+Code+Pro:200:300,400|Source+Sans+Pro:300,400',
               'static/m-light.compiled.css',
               'static/academicons.min.css',
               'static/m-mtw.css']
M_THEME_COLOR = '#EAEAEA'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['m.htmlsanity',
           'm.components',
           'm.link',
           'sitemap']

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
    "exclude": ["tags/", "archives/", "authors/", "categories/", "index"]
}

GITHUB_URL = "https://github.com/mtw/mtw.github.io"

DEFAULT_PAGINATION = 10

#M_SITE_LOGO_TEXT = 'Your Brand'

M_LINKS_NAVBAR1 = [('Publications', '/publications', 'publications', [
                        ('Papers', '/publications', 'papers'),
                        ('Presentations', 'publications/presentations', 'publications/presentations'),
                        ('Posters', 'publications/posters', 'publications/posters'),
                        ]),
                   ('Teaching', '/teaching', 'teaching', []),
                   ('Contact', '/contact', 'contact', [])]

#M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]', [
#                        ('News', 'blog/news/', ''),
#                        ('Archive', 'blog/archive/', '')]),

M_LINKS_FOOTER1 = [('Home', '/'),
                    ('Teaching', '/teaching'),
                    ('Contact', '/contact')
                        ]

M_LINKS_FOOTER2 = [('Publications', '/publications'),
                    ('Presentations', 'publications/presentations'),
                    ('Posters', 'publications/posters'),
                        ]

M_LINKS_FOOTER3 = [('My Profiles',''),
                    ('Google Scholar', 'https://scholar.google.at/citations?user=w0PHGnEAAAAJ&hl=en'),
                    ('Publons', 'https://publons.com/researcher/2466680/michael-thomas-wolfinger/'),
                    ('GitHub', 'https://github.com/mtw'),
                    ('ORCID', 'https://orcid.org/0000-0003-0925-5205'),
                        ]

M_LINKS_FOOTER4 = [('Social', ''),
                    ('ResearchGate', 'https://www.researchgate.net/profile/Michael-Wolfinger'),
                    ('Twitter', 'https://twitter.com/mtwolfinger'),
                    ('Linkedin', 'https://www.linkedin.com/in/michaelwolfinger/')
                    ]

M_FINE_PRINT =  """
| michaelwolfinger.com. Copyright © Michael T. Wolfinger, 2021. Site
  powered by `Pelican <https://getpelican.com>`_ and m.css.
| Code and content is `available on GitHub <https://github.com/mtw/mtw.github.io>`_.
"""

STATIC_PATHS = ['static', 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        'static/academicons.min.css': {'path': 'static/academicons.min.css'}
                        }

DISPLAY_PAGES_ON_MENU = True
SLUGIFY_SOURCE = 'basename'

#DIRECT_TEMPLATES = ['archives']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
#ARCHIVES_URL = 'examples/'
#ARCHIVES_SAVE_AS = 'examples/index.html'
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
#ARTICLE_SAVE_AS = '{slug}/index.html'
#AUTHOR_URL = 'author/{slug}/'
#AUTHOR_SAVE_AS = 'author/{slug}/index.html'
#CATEGORY_URL = 'category/{slug}/'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = ''
TAG_SAVE_AS = ''

AUTHORS_SAVE_AS = '' # Not used
CATEGORIES_SAVE_AS = '' # Not used
TAGS_SAVE_AS = '' # Not used


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

M_BLOG_NAME = "michaelwolfinger.com"
M_BLOG_URL = 'https://michaelwolfinger.com/'
M_BLOG_DESCRIPTION = "michaelwolfinger.com | virus bioinformatics"

M_SOCIAL_TWITTER_SITE = '@mtwolfinger'
M_SOCIAL_TWITTER_SITE_ID = 15105886
#M_SOCIAL_IMAGE = 'https://your.brand/static/site.png'
M_SOCIAL_BLOG_SUMMARY = "Stuff that matters in virus bioinformatics"
