#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Michael T. Wolfinger'
SITENAME = "Michael T. Wolfinger"
SITEURL = ''
OUTPUT_PATH = 'output'


PATH = 'content'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['']

# Explicit so local and CI builds render dates identically regardless of locale.
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
TIMEZONE = 'Europe/Vienna'
DEFAULT_DATE = None

DEFAULT_LANG = 'en'

THEME = 'pelican-theme'
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATHS = ['static']

DIRECT_TEMPLATES = ['index']

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

# One font request instead of three; the template escapes the ampersands once, so they
# must be plain '&' here (a pre-escaped '&amp;' would come out double-escaped).
M_CSS_FILES = [
    'https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap',
    'static/m-mtw.css',
]

M_THEME_COLOR = '#f1f0ec'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['m.htmlsanity',
           'm.components',
           'm.link',
           'm.sitemap',
           'm.images']

# Category listings are disallowed in robots.txt and the publications/papers/ stubs are
# canonicalised to their blog posts, so neither belongs in the sitemap.
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "weekly",
        "pages": "monthly"
    },
    "exclude": ["services", "consulting", "blog/archive/", "blog/author/", "blog/category/",
                "authors", "index", "legal", "publications/papers/", "404"]
}


#M_SITE_LOGO_TEXT = 'Your Brand'

# Links carry the trailing slash: that is the canonical form of every page URL, and the
# slash-less form costs a redirect on GitHub Pages.
M_LINKS_NAVBAR1 = [
                    ('About', '/about/', 'about', []),
                    ('Research', '/research/', 'research', [
                        ('Team', '/team/', 'team'),
                        ('Collaborations', '/collaborations/', 'collaborations'),
                    ]),
                    ('Publications', '/publications/', 'publications', [
                        ('Papers', '/publications/', 'papers'),
                        ('Presentations', '/publications/presentations/', 'publications/presentations'),
                        ('Posters', '/publications/posters/', 'publications/posters'),
                        ]),
                    ('Teaching', '/teaching/', 'teaching', []),
                    ('Contact', '/contact/', 'contact', []),
                    ('Writing', '/blog/', '[blog]',[])]

#M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]',[])]

# Footer: four link columns as in the mockups. The first entry of each list is the
# column heading (linked when it has a URL).
M_LINKS_FOOTER1 = [('Home', '/'),
                    ('About', '/about/'),
                    ('Research', '/research/'),
                    ('Publications', '/publications/'),
                    ('Teaching', '/teaching/'),
                    ('People & Supervision', '/team/'),
                    ('Writing', '/blog/'),
                    ]

M_LINKS_FOOTER2 = [('More', ''),
                    ('RNA Forecast', 'https://rnaforecast.com'),
                    ('Contact', '/contact/'),
                    ('Legal Note', '/legal/'),
                    ]

M_LINKS_FOOTER3 = [('My Profiles', ''),
                    ('Google Scholar', 'https://scholar.google.at/citations?user=w0PHGnEAAAAJ&hl=en'),
                    ('ResearchGate', 'https://www.researchgate.net/profile/Michael-Wolfinger'),
                    ('Scopus', 'https://www.scopus.com/authid/detail.uri?authorId=6508361997'),
                    ('Loop', 'https://loop.frontiersin.org/people/485709/overview'),
                    ]

M_LINKS_FOOTER4 = [('Social', ''),
                    ('LinkedIn', 'https://www.linkedin.com/in/michaelwolfinger/'),
                    ('Bluesky', 'https://bsky.app/profile/mtwolfinger.bsky.social'),
                    ('GitHub', 'https://github.com/mtw'),
                    ('ORCID', 'https://orcid.org/0000-0003-0925-5205'),
                    ]

M_FINE_PRINT = "© 2026 Michael T. Wolfinger · Vienna, Austria · michael.wolfinger@rnaforecast.com"

STATIC_PATHS = ['static', 'extra/CNAME', 'extra/robots.txt', 'extra/favicon.ico',
                'extra/llms.txt', 'extra/site.webmanifest']
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'extra/llms.txt': {'path': 'llms.txt'},
                        'extra/site.webmanifest': {'path': 'site.webmanifest'},
                        }


#M_HTML_HEADER = '<link rel="stylesheet" href="extra/css/extra.css"'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


M_BLOG_NAME = "michaelwolfinger.com Bioinformatics Blog"
M_BLOG_URL = 'https://michaelwolfinger.com/blog/'
M_BLOG_DESCRIPTION = "michaelwolfinger.com | Computational RNA biology: RNA structure, folding dynamics, functional RNA design, and structured viral RNAs"

M_SOCIAL_TWITTER_SITE = '@mtwolfinger'
M_SOCIAL_TWITTER_SITE_ID = 15105886
#M_SOCIAL_IMAGE = 'https://your.brand/static/site.png'
# Link-preview card (Open Graph / Twitter), 1200x630; source in tools/og-cards-source.html.
M_SOCIAL_IMAGE = '/static/og-wide-1200x630.png'
M_SOCIAL_IMAGE_WIDTH = 1200
M_SOCIAL_IMAGE_HEIGHT = 630
M_SOCIAL_IMAGE_ALT = 'RNA Structure, Function & Design - Michael T. Wolfinger, michaelwolfinger.com'
M_SOCIAL_CARD = 'summary_large_image'
# Portrait used as the Person image in structured data.
M_PERSON_IMAGE = '/static/mtw.jpg'
M_SOCIAL_BLOG_SUMMARY = "Computational RNA biology — RNA structure, folding dynamics, functional RNA design, and structured viral RNAs"

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
INDEX_URL = 'blog/'   # read by the sitemap plugin; without it the blog index is written as '/'
INDEX_SAVE_AS = 'blog/index.html'

#YEAR_ARCHIVE_URL = 'blog/archives/{date:%Y}.html'
#YEAR_ARCHIVE_SAVE_AS = 'blog/archives/{date:%Y}.html'

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'

DEFAULT_PAGINATION = 5

